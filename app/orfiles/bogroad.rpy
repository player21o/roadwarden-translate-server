###################### BOG CROSSROADS
default bogcrossroads_firsttime = 0
label bogcrossroads01:
    nvl clear
    $ pc_area = "bogcrossroads"
    stop music fadeout 4.0
    play nature "audio/ambient/bogroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture bogentrancetobogcrossroads at basicfade
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ world_known_areas += 1
    $ bogcrossroads_firsttime = 1
    $ bogroad_unlocked = 1
    $ bogentrance_unlocked = 1
    $ vines_unlocked = 1
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        'You’re not used to the scents of the bogs, but you weren’t expecting them to be so gentle. The humid air makes you think of smoked meat, and even though you ride by a few rotting carcasses and animal droppings, just as often you cross tiny meadows of pink, yellow, and red flowers.
        \n\nThe noises tell stories of neverending wars between the swarms of insects, frogs in their hideouts, snakes lurking among the purple grasses, birds patrolling both the water and the sky, and the saurians preparing to strike from beneath the surface. You can’t separate the sounds of the living from those of the dying, if they’re even different at all.
        \n\nYou reach a boulder in the middle of the road, on the edge of a large pond. The road splits from here in two directions, but the only smoke you see is to the southeast.
        '
        'From the saddle, I see no creatures standing in my way. (disabled)':
            pass

###################### BOG ROAD
default bogroad_firsttime = 0
default bogroad_triedtohelp = 0
default bogroad_leftrightaway = 0
default bogroad_observing = 0 # 0 - no, 1 - yes, and failed / 2 - yes, and succeeded
default bogroad_noclothes = 0
default bogroad_clotheswet = 0
default bogroad_cathp = 5
default bogroad_birdkilled = 0
default bogroad_fleeattempt = 0
default bogroad_turns = 0
default bogroad_fierceattack = 0

label bogroad01:
    $ renpy.save("combatsave", extra_info='Combat Auto Save')
    nvl clear
    $ pc_area = "bogroad"
    stop nature fadeout 4.0
    if not renpy.music.get_playing(channel='music') == "<loop 5.0>audio/weloveindies_duringthenight_batteloop.ogg":
        play music "<loop 5.0>audio/weloveindies_duringthenight_batteloop.ogg" fadeout 1.0 fadein 1.0
    show areapicture bogcrossroadstobogroad at basicfade
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ world_known_areas += 1
    $ bogroad_firsttime = 1
    $ bogcrossroads_unlocked = 1
    $ peatfield_unlocked = 1
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        'The road takes you to the edge of the woods. A few trees have found lucky scraps of soil towering above the water, while others, shorter and not as lush, have roots sunk in the pond. Some of the plants were felled with tools, so the route itself isn’t so dark, while the few sunbeams getting through the weaker branches on your left are surrounded by darkness and swarms of insects.
        \n\n“Help me! Help!” The sudden cry, as well as screams of pain, reaches you from between the trees. A woman, or a child.
        '
        'I think about my goal. “Wait here, {color=#f6d6bd}[horsename]{/color}. Someone needs me.”' if pc_goal == "iwanttoberemembered" or pc_goal == "iwanttohelp":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about my goal. “Wait here, {color=#f6d6bd}%s{/color}. Someone needs me.”' %horsename)
            jump bogroadhelping01
        'I dismount and grab my axe.' if pc_goal != "iwanttoberemembered" or pc_goal != "iwanttohelp":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and grab my axe.')
            jump bogroadhelping01
        'I try to spot anyone.' if not bogroad_observing:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to spot anyone.')
            jump bogroad_observing01
        'It may be a trap, and even if it’s not, I can’t help them.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be a trap, and even if it’s not, I can’t help them')
            jump bogroadquitting01

label bogroadquitting01:
    $ bogroad_leftrightaway = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        '{color=#f6d6bd}[horsename]{/color} seems to agree with your decision. It enters a trot, leading you farther east.
        \n\nA minute passes, but you still hear the constant shouts, as if someone’s getting whipped to their very bones.
        '
        'I just have to ignore it. (disabled)' if pc_goal != "iwanttoberemembered" and pc_goal != "iwanttohelp":
            pass
        'Dying here won’t be helpful to anyone. (disabled)' if pc_goal == "iwanttohelp":
            pass
        'Dying here won’t make me a hero. (disabled)' if pc_goal == "iwanttoberemembered":
            pass

label bogroad_observing01:
    $ bogroad_observing = 1
    menu:
        'Among the green and red leaves you don’t see any unusual colors. Come to think of it, there’s but a few creatures in sight, other than the flies and mosquitoes. The dark-winged birds are quiet, the sparse toads let out sporadic, tense croaks.
        '
        'I think about my goal. “Wait here, {color=#f6d6bd}[horsename]{/color}. Someone needs me.”' if pc_goal == "iwanttoberemembered" or pc_goal == "iwanttohelp":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about my goal. “Wait here, {color=#f6d6bd}%s{/color}. Someone needs me.”' %horsename)
            jump bogroadhelping01
        'I dismount and grab my axe.' if pc_goal != "iwanttoberemembered" or pc_goal != "iwanttohelp":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and grab my axe.')
            jump bogroadhelping01
        'I try to spot anyone.' if not bogroad_observing:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to spot anyone.')
            jump bogroad_observing01
        'It may be a trap, and if it’s not, I can’t help them.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be a trap, and if it’s not, I can’t help them')
            jump bogroadquitting01

label bogroadhelpingTURN1ALL:
    label bogroadhelping01:
        $ can_potions = 1
        if item_shield:
            $ custom11 = "\n\nYou prepare your shield."
        else:
            $ custom11 = ""
        menu:
            'You lean toward the pond. It’s cleaner than in the other parts of the bog, allowing you to see the bottom. Parts of it are still more than knee-deep, and the sulfuric odor makes you step away with a frown. The brownish color can’t hide all the bones and plant remains that are sticking out of the bed.[custom11]
            '
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass
            'I take off everything below my waist.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take off everything below my waist.')
                $ can_potions = 0
                $ bogroad_noclothes = 1
                $ minutes += 5
                $ cleanliness = limit_cleanliness(cleanliness-2)
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                menu:
                    'You undo your boots and buckles, then hang your pants on the saddle. As your naked skin touches the water, you expect it to be more like a slime, but nothing of the sort happens - only your eyes and nose notice the difference between this place and a regular pond. The cold water makes you shiver.
                    \n\nThe voice doesn’t stop. You gather your bravery and move forward, disturbing the sediment so much that it forms a cloud of mud after every step. You run into the trees.
                    '
                    'I look around.':
                        jump bogroadhelping01a
                    'I follow the voice.':
                        jump bogroadhelping01b
                    'I observe the tree crowns.':
                        jump bogroadhelping01c
            'I’ve no time to waste. I rush into the water.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve no time to waste. I rush into the water.')
                $ can_potions = 0
                $ cleanliness = limit_cleanliness(cleanliness-4)
                show minus4appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 appearance points.{/i}')
                $ bogroad_clotheswet = day
                menu:
                    'You get slower with every step, as your pants and boots are soaked in water and mud. The cold water makes you shiver, and the sulfuric odor makes you glance at the animal bones sticking out of the pond bed.
                    \n\nThe voice doesn’t stop. You gather your bravery and move forward, disturbing the sediment so much that it forms a cloud of mud after every step. You run into the trees.
                    '
                    'I look around.':
                        jump bogroadhelping01a
                    'I follow the voice.':
                        jump bogroadhelping01b
                    'I observe the tree crowns.':
                        jump bogroadhelping01c

    label bogroadhelping01a:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around.')
        if armor <= 1 and pc_hp <= 1:
            $ custom1 = "As you walk among the trunks and branches, you see no large creatures. The water in the distance is static, with small fish snacking on lily pads and chasing one another.\n\nSomething lands on your back, and you plunge into the water, getting pinned down to the mud by massive paws. You’re choking, hearing only splashes. The blood joins the cloud of dirt."
            jump bogroadgameover01
        if bogroad_noclothes:
            $ custom2 = ""
        else:
            $ custom2 = "Your clothes turn every step into a struggle. "
        menu:
            '[custom2]As you walk among the trunks and branches, you see no large creatures. The water in the distance is static, with small fish snacking on lily pads and chasing one another.
            \n\nSomething lands on your back, and you plunge into the water, getting pinned down to the mud by massive paws. You’re choking, hearing only splashes.
            '
            '{image=d6} I need to get out of the water.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to get out of the water.')
                jump bogroadhelping01gettingoutofwater

    label bogroadhelping01b:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the voice.')
        if armor <= 1 and pc_hp <= 1:
            $ custom1 = "It leads you deeper into the trees. You think it’s coming from one of the larger plants, with a crown so dense you can barely see anything between the branches.\n\nSomething lands on your back, and you plunge into the water, getting pinned down to the mud by massive paws. You’re choking, hearing only splashes. The blood joins the cloud of dirt."
            jump bogroadgameover01
        if bogroad_noclothes:
            $ custom2 = ""
        else:
            $ custom2 = ", but your clothes turn every step into a struggle"
        menu:
            'It leads you deeper into the trees[custom2]. You think it’s coming from one of the larger plants, with a crown so dense you can barely see anything between the branches.
            \n\nSomething lands on your back, and you plunge into the water, getting pinned down to the mud by massive paws. You’re choking, hearing only splashes.
            '
            '{image=d6} I need to get out of the water.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to get out of the water.')
                jump bogroadhelping01gettingoutofwater

    label bogroadhelping01c:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe the tree crowns.')
        if bogroad_noclothes:
            $ custom2 = "You move deeper in."
        else:
            $ custom2 = "You move deeper in, but your clothes turn every step into a struggle."
        menu:
            '[custom2] You don’t spot anything peculiar among the branches, until your eyes land on an unusual gray bird, which seems to open its beak just at the same time as you hear a painful shout.
            \n\nA dark shape is descending toward you from the very same tree.
            '
            'I catch it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I catch it.')
                if armor <= 1 and pc_hp <= 0:
                    $ custom1 = "You reach out to it, and the hit lands on your chest. You plunge into the water, getting pinned down to the mud by massive paws. You’re choking, hearing only splashes.The pink, open jaws pierce the water and reach for your face."
                    jump bogroadgameover01
                menu:
                    'You reach out to it, and the hit lands on your chest. You plunge into the water, getting pinned down to the mud by massive paws. You’re choking, hearing only splashes.
                    '
                    '{image=d6} I need to get out of the water.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to get out of the water.')
                        jump bogroadhelping01gettingoutofwaterALT
            'I strike it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I strike it.')
                if item_golemglove:
                    $ bogroad_cathp -= 1
                    $ custom2 = "The golem glove makes your swipe much faster. "
                else:
                    $ custom2 = ""
                if item_axe03:
                    $ bogroad_cathp -= 2
                    $ custom3 = "The axe you bought from {color=#f6d6bd}Akakios{/color} cuts through the air and sinks into the beast’s side. The blood splashes on your hands as you step away, avoiding the pounce. The dark creature plunges into the water."
                elif item_axe02alt:
                    $ bogroad_cathp -= 2
                    $ custom3 = "Your bronze axe may not be too elegant, but it cuts the air with ease, sinking into the beast’s shoulder. The blood splashes on your hands as you step away, avoiding the pounce. The dark creature plunges into the water."
                elif item_axe02:
                    $ bogroad_cathp -= 2
                    $ custom3 = "The axe you brought North may not be too elegant, but it cuts the air with ease, sinking into the beast’s shoulder. The blood splashes on your hands as you step away, avoiding the pounce. The dark creature plunges into the water."
                elif item_axe01:
                    $ bogroad_cathp -= 1
                    $ custom3 = "The axe you brought North almost doesn’t land, but your quick reaction overcomes the blade’s shortcomings. It hits the beast, cutting the skin on its shoulder slightly, but also pushing it with a powerful blow. You step away, avoiding the pounce. The dark creature plunges into the water."
                menu:
                    '[custom2][custom3]
                    '
                    'I turn around and take a look at it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn around and take a look at it.')
                        jump bogroadhelpingturn02
            'I jump away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I jump away.')
                $ bogroad_turns += 1
                menu:
                    'The beast’s pounce misses you - a dark, furry creature gracefully lands in the water, partially turning around mid-air, but as it growls, it doesn’t charge at you yet, maybe not expecting your swift reaction.
                    '
                    'Still moving and keeping my distance, I take a look at it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Still moving and keeping my distance, I take a look at it.')
                        jump bogroadhelpingturn02
            'I examine it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine it.')
                if armor <= 1 and pc_hp <= 0:
                    $ custom1 = "You glance at the dark, spotted creature that now lands on your chest. You plunge into the water, getting pinned down to the mud by massive paws. You’re choking, hearing only splashes.The pink, open jaws pierce the water and reach for your face."
                    jump bogroadgameover01
                menu:
                    'You glance at the dark, spotted creature that now lands on your chest. You plunge into the water, getting pinned down to the mud by massive paws. You’re choking, hearing only splashes.
                    '
                    '{image=d6} I need to get out of the water.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to get out of the water.')
                        jump bogroadhelping01gettingoutofwaterALT

    label bogroadhelping01gettingoutofwater:
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter*2)
        else:
            $ d100roll -= (pc_battlecounter)
        $ d100roll -= (pc_hp*5)
        if bogroad_noclothes:
            $ d100roll -= 10
        if d100roll > 60: # fail
            $ custom1 = "You try to roll away and knock the creature off you, but it’s heavy, with large paws and strong legs. In panic, you gasp for air, filling your mouth with dirt. The bite shatters your skull."
            jump bogroadgameover01
        elif d100roll > 30: # semi success
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your fine gambeson helps you avoid the pain and distractions."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your gambeson helps you avoid the pain and distractions."
            else:
                if pc_hp <= 0:
                    $ custom1 = "You try to roll away and knock the creature off you, but it’s heavy, with large paws and strong legs. You put trust in your armor, but to no avail - it was already in such bad shape it made little difference, and the beast pressures your chest like a boulder. The bite shatters your skull."
                    jump bogroadgameover01
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom4 = "Your gambeson is too weak to protect you from the claws, but you manage to ignore the pain."
                $ cleanliness = limit_cleanliness(cleanliness-2)
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                menu:
                    'You try to roll away. [custom4] While the creature seems to be as heavy as you are, with large paws and strong legs, you’re strong enough to knock it off yourself. You bounce from the ground and dash through the shallow water, getting back on your feet, still holding your blade.
                    '
                    'I gasp for air and look at the beast.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gasp for air and look at the beast.')
                        jump bogroadhelpingturn02
        else: # success
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            menu:
                'You try to roll away, and while the creature is heavy, with large paws and strong legs, you’re strong enough to knock it off yourself. You bounce from the ground and dash through the shallow water, smoothly getting back on your feet, still holding your blade.
                '
                'I gasp for air and look at the beast.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gasp for air and look at the beast.')
                    jump bogroadhelpingturn02

    label bogroadhelping01gettingoutofwaterALT:
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter*2)
        else:
            $ d100roll -= (pc_battlecounter)
        $ d100roll -= (pc_hp*5)
        if bogroad_noclothes:
            $ d100roll -= 10
        if d100roll > 70: # fail
            $ custom1 = "You try to roll away and knock the creature off you, but it’s heavy, with large paws and strong legs. In panic, you gasp for air, filling your mouth with dirt.The pink, open jaws pierce the water and reach for your face."
            jump bogroadgameover01
        elif d100roll > 30: # semi success
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your fine gambeson helps you avoid the pain and distractions."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your gambeson helps you avoid the pain and distractions."
            else:
                if pc_hp <= 0:
                    $ custom1 = "You try to roll away and knock the creature off you, but it’s heavy, with large paws and strong legs. You put trust in your armor, but to no avail - it was already in such bad shape it made little difference, and the beast pressures your chest like a boulder.The pink, open jaws pierce the water and reach for your face."
                    jump bogroadgameover01
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom4 = "Your gambeson is too weak to protect you from the claws, but you manage to ignore the pain."
                $ cleanliness = limit_cleanliness(cleanliness-2)
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                menu:
                    'You try to roll away. [custom4] While the creature seems to be as heavy as you are, with large paws and strong legs, you’re strong enough to knock it off yourself. You bounce from the ground and dash through the shallow water, getting back on your feet, still holding your blade.
                    '
                    'I gasp for air and look at the beast.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gasp for air and look at the beast.')
                        jump bogroadhelpingturn02
        else: # success
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            menu:
                'You try to roll away, and while the creature is heavy, with large paws and strong legs, you’re strong enough to knock it off yourself. You bounce from the ground and dash through the shallow water, getting back on your feet, still holding your blade.
                '
                'I gasp for air and look at the beast.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gasp for air and look at the beast.')
                    jump bogroadhelpingturn02

label bogroadhelpingturn02:
    if bogroad_cathp >= 5:
        $ custom1 = "It’s unscathed, confident."
    elif bogroad_cathp == 4:
        $ custom1 = "The slight wound in its shoulder doesn’t seem to bother it."
    elif bogroad_cathp == 3:
        $ custom1 = "With the deep wound in its shoulder, it raises its leg slightly."
    else:
        $ custom1 = "The deep wound makes it lean to one side. A twitch of pain twists its mouth."
    menu:
        'The cat’s legs are bent, ready to jump, wide and muscular. Its eyes, staring at you without a blink, are round and yellow, with pitch black irises in the center. It’s waist-high, with its chin hanging just above the water, and a jaw that could bite off your limb in a heartbeat.
        \n\nIt has short hair and whiskers, and a nose as big as your hand. Even without the dirt, it’s almost black, with glimpses of yellow that form a rose-like pattern on its sides and dots on its head. You can’t see the creature’s paws through the now-clouded water.
        \n\nThe cat lets out a growl, like a saw cutting a log. [custom1]
        '
        'I take a defensive stance.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a defensive stance.')
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your fine gambeson keeps you in one piece."
            elif armor >= 1 and item_shield:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your gambeson and shield keep you in one piece."
            elif armor >= 1:
                $ armor = limit_armor(armor-2)
                show minus2armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                $ custom4 = "Your gambeson keeps you in one piece."
            else:
                if pc_hp <= 0:
                    $ custom1 = "When you hear the flapping of wings, it’s already too late. Bird talons sink into your face, and once you get distracted, the cat darts forward, reaching for your thighs. You collapse, and realize that you have only one leg left."
                    jump bogroadgameover01
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom4 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            menu:
                'When you hear the flapping of wings, it’s already too late. Bird talons sink into your shoulder, and once you get distracted, the cat darts forward, reaching for your thighs. You evade its first strike, but it then pushes your stomach with its huge paw, cutting through the armor. Before you can reach it with your blade, it’s already out of your range.
                \n\n[custom4] The gray bird also flies away, now circling around you, gracefully avoiding the tree trunks and branches. It has a red tail and a short, curved, vulture-like beak. It growls just like the cat did a moment ago, and you notice that the human screams have disappeared.
                '
                'So it’s two against one.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- So it’s two against one.')
                    jump bogroadhelpingturn03plus
        'I run away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run away.')
            $ bogroad_fleeattempt = 1
            if pc_hp <= 0:
                $ custom1 = "When you hear the flapping of wings, it’s already too late. Bird talons sink into your face, and once you get distracted, the cat darts forward, reaching for your thighs. You collapse, and realize that you have only one leg left."
                jump bogroadgameover01
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your fine gambeson keeps you in one piece."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your gambeson keeps you in one piece."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom4 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            menu:
                'Right after your foot hits one of the roots hidden beneath the floating sludge, you realize that crossing the water is going to take some time - a luxury that you don’t have.
                \n\nWhen you hear the flapping of wings, it’s already too late. Bird talons sink into your shoulder, and once you get distracted, the cat darts forward, reaching for your thighs. You evade its first strike, but it then pushes your back with its huge paw, cutting through the armor. Before you can reach it with your blade, it’s already out of your range.
                \n\n[custom4] The gray bird also flies away, now circling around you, gracefully avoiding the tree trunks and branches. It has a red tail and a short, curved, vulture-like beak. It growls just like the cat did a moment ago, and you notice that the human screams have disappeared.
                '
                'So it’s two against one.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- So it’s two against one.')
                    jump bogroadhelpingturn03plus
        'If the human voice is still around, I try to focus on it.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- If the human voice is still around, I try to focus on it.')
            $ bogroad_birdkilled = 1
            menu:
                'The screams have disappeared, and you notice the sudden noise of flapping wings coming straight at you. You instinctively take a swing.
                \n\nThe blade sends the halves of the raven-sized creature into the water, to the enjoyment of the local scavengers. A few gray and red feathers are drifting next to you.
                '
                'I raise the axe and look at the cat.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise the axe and look at the cat.')
                    jump bogroadhelpingturn03plus

label bogroadhelpingturn03ALL:
    label bogroadhelpingturn03plus:
        $ at = 0
        if bogroad_birdkilled:
            if bogroad_cathp == 5:
                $ custom1 = "The cat roars toward its dead companion, then looks into your eyes. As it moves forward, you don’t see any wounds on its shell."
            elif bogroad_cathp == 4:
                $ custom1 = "The cat roars toward its dead companion, then looks into your eyes. As it moves forward, you hardly see any blood on its shell."
            elif bogroad_cathp == 3:
                $ custom1 = "The cat roars toward its dead companion, then looks into your eyes. As it moves forward slowly, its blood mixes with the cloud of dirt."
            else:
                $ custom1 = "The cat looks at its dead companion, and, without a second thought, leaps away, then partially swims, crossing the pond with a speed matching your palfrey’s gallop. You consider following it, but after it reaches a tree crown with just two jumps, then gets to another one within a single breath, you wipe your forehead and turn away."
                jump bogroadleavingafterhelping01
        else:
            if bogroad_cathp >= 5:
                $ custom1 = "The cat looks into your eyes, then roars. As it moves forward, you don’t see any wounds on its shell. Its companion circles around you, looking for an opportunity to attack from above."
            elif bogroad_cathp == 4:
                $ custom1 = "The cat looks into your eyes, then roars. As it moves forward, you hardly see any blood on its shell. Its companion circles around you, looking for an opportunity to attack from above."
            elif bogroad_cathp == 3:
                $ custom1 = "The cat looks into your eyes. As it moves forward slowly, its blood mixes with the cloud of dirt. Its companion seems to keep a larger distance than it did before."
            elif bogroad_cathp == 2:
                $ custom1 = "The cat looks around, staggering forward. Its blood mixes with the cloud of dirt. Its companion seems to keep a larger distance than it did before."
            elif bogroad_cathp == 1:
                $ custom1 = "The cat looks around, keeping its distance. Its blood mixes with the cloud of dirt. Its companion imitates the beast’s roars and growls, as if trying to give it an order."
            else:
                $ custom1 = "The cat looks at you fearfully, gasping for breath. After it looks at its screeching companion, it leaps away, but is too weak to land on its paws. It staggers away.\n\nYou follow it, but after maybe a minute, a large saurian jumps from beneath the surface and grabs the cat by its head, pulling it into a deeper part of the pond. Both of them disappear in a cloud of kicked-up dirt, and the splashes of water cease quickly. You turn away before a similar fate befalls you. “Help me,” shouts the bird before it flies farther north."
                jump bogroadleavingafterhelping01
        if bogroad_turns >= 4 and bogroad_birdkilled:
            $ custom1 = "The cat observes you with new respect, surprised that you’re still standing. It looks at its dead companion and, without a second thought, leaps away, then partially swims, crossing the pond with a speed matching your palfrey’s gallop. You consider following it, but after it reaches a tree crown with just two jumps, then gets to another one within a single breath, you wipe your forehead and turn away. "
            jump bogroadleavingafterhelping01
        elif bogroad_turns >= 4:
            $ custom1 = "The cat observes you with new respect, surprised that you’re still standing. It growls toward the bird, then leaps away and partially swims, crossing the pond with a speed matching your palfrey’s gallop. You consider following it, but after it reaches a tree crown with just two jumps, then gets to another one within a single breath, you wipe your forehead and turn away. “Help me,” shouts the bird as it follows its ally."
            jump bogroadleavingafterhelping01
        else:
            $ bogroad_turns += 1
        if pc_class == "warrior" and not bogroad_birdkilled:
            $ at_unlock_force = 1
            $ at = 0
        menu:
            '[custom1]
            '
            'I put my trust in the armor and focus on making fierce cuts.' if armor >= 3 and not bogroad_fierceattack:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put my trust in the armor and focus on making fierce cuts.')
                $ at_unlock_force = 0
                $ at = 0
                $ bogroad_fierceattack += 1
                jump bogroadturn03strongattack
            'I can’t rely on my gambeson in its current state. (disabled)' if armor <= 2 and not bogroad_fierceattack:
                pass
            '{image=d6} I try to stay safe, looking for an opportunity to make a precise strike.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I try to stay safe, looking for an opportunity to make a precise strike.')
                $ at_unlock_force = 0
                $ at = 0
                jump bogroadturn03safeattack
            '{image=d6} I keep the beast at a distance, playing for time.' if pc_hp > 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I keep the beast at a distance, playing for time.')
                $ at_unlock_force = 0
                $ at = 0
                jump bogroadturn03fulldefence
            'I won’t be able to evade all of its strikes. (Required vitality: 2) (disabled)' if pc_hp <= 1:
                pass
            'I run away.' if not bogroad_fleeattempt:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run away.')
                $ at_unlock_force = 0
                $ at = 0
                jump bogroadturn03fleeing
            'I can’t outrun the cat in this water. (disabled)' if bogroad_fleeattempt:
                pass
            '{image=d6} I attack the bird.' ( condition="at != 'force' and not bogroad_birdkilled" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I attack the bird.')
                $ at_unlock_force = 0
                $ at = 0
                jump bogroadturn03attackingthebird
            'Cutting that bird should be easy enough.' ( condition="at == 'force' and not bogroad_birdkilled" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Cutting that bird should be easy enough.')
                $ at_unlock_force = 0
                $ at = 0
                jump bogroadturn03attackingthebirdalt

    label bogroadturn03strongattack:
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter*2)
        else:
            $ d100roll -= (pc_battlecounter)
        if item_axe03:
            $ bogroad_cathp -= 3
            $ custom3 = "your new axe sinks into the beast’s back, and you find enough time to then cut its stomach, though only slightly."
        elif item_axe02alt:
            $ bogroad_cathp -= 2
            $ custom3 = "your bronze axe sinks into the beast’s back."
        elif item_axe02:
            $ bogroad_cathp -= 2
            $ custom3 = "your sharp axe sinks into the beast’s back."
        elif item_axe01:
            $ bogroad_cathp -= 1
            $ custom3 = "your old axe cuts the beast’s back slightly."
        if armor >= 3:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ custom4 = "Your fine gambeson keeps you in one piece."
        else:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ custom4 = "Your gambeson keeps you in one piece."
        if not bogroad_birdkilled:
            if item_golemglove:
                $ custom5 = "The bird distracts you by pecking at your hair, jacket, and hands, but you use The Golem Glove to your advantage."
                $ bogroad_cathp -= 1
            else:
                $ custom5 = "The bird distracts you by pecking at your hair, jacket, and hands."
        else:
            if item_golemglove:
                $ custom5 = "Not distracted by the bird, you give it your all, making use of The Golem Glove."
                $ bogroad_cathp -= 2
            else:
                $ custom5 = "Not distracted by the bird, you give it your all."
                $ bogroad_cathp -= 1
        menu:
            '[custom5] You let the cat get close to you, grabbing its heavy neck with your arm, but unable to avoid its paws. [custom4] In the meantime, [custom3] The creature leaps away, roaring in anger and pain.
            '
            'I “wash” the blade in water and follow the cat’s movements.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I “wash” the blade in water and follow the cat’s movements.')
                jump bogroadhelpingturn03plus

    label bogroadturn03safeattack:
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter*2)
        else:
            $ d100roll -= (pc_battlecounter)
        if armor >= 3:
            $ d100roll -= 25
        elif armor >= 1:
            $ d100roll -= 15
        if item_golemglove:
            $ d100roll -= 15
        if item_axe03:
            $ d100roll -= 25
        elif item_axe02alt:
            $ d100roll -= 15
        elif item_axe02:
            $ d100roll -= 10
        $ d100roll -= (pc_hp*10)
        $ d100roll += (bogroad_cathp*10)
        if not bogroad_birdkilled:
            $ d100roll += 20
            $ custom5 = "The bird distracts you by pecking at your hair, jacket, and hands. "
        else:
            $ custom5 = ""
        if d100roll > 70: # fail
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your fine gambeson keeps you in one piece."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your gambeson keeps you in one piece."
            else:
                if pc_hp <= 0:
                    $ custom1 = "You do your best to evade the cat’s attack, then to strike it as it charges at you, but your attempt fails miserably. It manages to get its teeth into your stomach, sinking into your flesh.\n\nIn its jaws, it holds a piece of your meat."
                    jump bogroadgameover01
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom4 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            menu:
                '[custom5]You do your best to evade the cat’s attack, then to strike it as it charges at you, but your attempt fails miserably. It manages to reach your stomach with its claws, slashing through your jacket.
                \n\n[custom4]
                '
                'Struggling, I push it away with my axe, then prepare for the next clash.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Struggling, I push it away with my axe, then prepare for the next clash.')
                    jump bogroadhelpingturn03plus
        if d100roll > 40: # harsh success
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your fine gambeson keeps you in one piece."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your gambeson keeps you in one piece."
            else:
                if pc_hp <= 0:
                    $ custom1 = "You do your best to evade the cat’s attack, then to strike it as it charges at you, but your attempt fails miserably, even though you also land a hit. The beast manages to get its teeth into your stomach, sinking into your flesh.\n\nIn its jaws, it holds a piece of your meat."
                    jump bogroadgameover01
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom4 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if item_golemglove:
                $ bogroad_cathp -= 1
            if item_axe03:
                $ bogroad_cathp -= 2
                $ custom3 = "your new axe sinks into the beast’s side."
            elif item_axe02alt:
                $ bogroad_cathp -= 2
                $ custom3 = "your bronze axe sinks into the beast’s back."
            elif item_axe02:
                $ bogroad_cathp -= 2
                $ custom3 = "your sharp axe sinks into the beast’s back."
            elif item_axe01:
                $ bogroad_cathp -= 1
                $ custom3 = "your old axe cuts the beast’s shoulder slightly."
            menu:
                '[custom5]You do your best to evade the cat’s attack, then to strike it as it charges at you, but your attempt fails, even though you also land a hit. The beast manages to reach your stomach with its claws, slashing through your armor, while [custom3]
                \n\n[custom4]
                '
                'Struggling, I push it away with my axe, then prepare for the next clash.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Struggling, I push it away with my axe, then prepare for the next clash.')
                    jump bogroadhelpingturn03plus
        else: # full success
            if item_golemglove:
                $ bogroad_cathp -= 1
            if item_axe03:
                $ bogroad_cathp -= 2
                $ custom3 = "your new axe gets into the beast’s side."
            elif item_axe02alt:
                $ bogroad_cathp -= 2
                $ custom3 = "your bronze axe gets into the beast’s back."
            elif item_axe02:
                $ bogroad_cathp -= 2
                $ custom3 = "your sharp axe gets into the beast’s back."
            elif item_axe01:
                $ bogroad_cathp -= 1
                $ custom3 = "your old axe cuts the beast’s shoulder slightly."
            menu:
                '[custom5]You do your best to evade the cat’s attack, then to strike it as it charges at you. You somehow avoid its claws and teeth, and [custom3]
                '
                'I get away from it quickly, then prepare for the next clash.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get away from it quickly, then prepare for the next clash.')
                    jump bogroadhelpingturn03plus

    label bogroadturn03fulldefence:
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter*2)
        else:
            $ d100roll -= (pc_battlecounter)
        $ d100roll -= (pc_hp*15)
        $ d100roll += (bogroad_cathp*10)
        if not bogroad_birdkilled:
            $ d100roll += 20
            $ custom5 = "The bird distracts you by pecking at your hair, jacket, and hands. "
        else:
            $ custom5 = ""
        if d100roll > 60: # fail
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your fine gambeson keeps you in one piece."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your gambeson keeps you in one piece."
            else:
                if pc_hp <= 0:
                    $ custom1 = "You keep your distance, then duck as the beast jumps at you, but you poorly place your feet on the muddy ground. The cat manages to get its teeth into your stomach, sinking into your flesh.\n\nIn its jaws, it holds a piece of your meat."
                    jump bogroadgameover01
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom4 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            menu:
                '[custom5]You keep your distance, then duck as the beast jumps at you, but you poorly place your feet on the muddy ground. The cat manages to reach your stomach with its claws, slashing through your armor, then leaps away. After a few breaths, it prepares itself for another pounce.
                \n\n[custom4]
                '
                'Struggling, I hold my axe in front of me, then prepare for the next clash.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Struggling, I hold my axe in front of me, then prepare for the next clash.')
                    jump bogroadhelpingturn03plus
        else:
            $ bogroad_turns += 1
            menu:
                '[custom5]You keep your distance, then duck as the beast jumps at you. So far, your reflex is beyond reproach. After a few breaths, the cat prepares itself for another pounce.
                '
                'Let’s hope it’s not too patient.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope it’s not too patient.')
                    jump bogroadhelpingturn03plus

    label bogroadturn03fleeing:
        $ bogroad_fleeattempt = 1
        if not bogroad_birdkilled:
            if armor >= 2:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "tearing the armor on your arms and back"
            elif armor == 1:
                if pc_hp <= 0:
                    $ custom1 = "Your foot gets stuck between a curvy root and the mud. Before you get it out, the bird cuts through the skin on your neck. Distracted, you don’t notice the cat’s pounce. The water is pouring into the hole in your back."
                    jump bogroadgameover01
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom4 = "tearing the armor on your arms and cutting your back"
            else:
                if pc_hp <= 1:
                    $ custom1 = "Your foot gets stuck between a curvy root and the mud. Before you get it out, the bird cuts through the skin on your neck. Distracted, you don’t notice the cat’s pounce. The water is pouring into the hole in your back."
                    jump bogroadgameover01
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                $ custom4 = "cutting your arm and back"
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
            menu:
                'Right after your foot hits one of the roots hidden beneath the floating sludge, you realize that crossing the water is going to take some time - a luxury that you don’t have.
                \n\nThe bird and the cat try to get to you again, [custom4].
                '
                'Well, fleeing is not an option.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, fleeing is not an option.')
                    jump bogroadhelpingturn03plus
        else:
            if armor >= 2:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "tearing the armor on your back"
            elif armor == 1:
                if pc_hp <= 0:
                    $ custom1 = "Your foot gets stuck between a curvy root and the mud. Before you get it out, the cat gets close, but your movements are restricted. Still bent, you raise your weapon, but you don’t have time to prepare yourself for the pounce.\n\nThe water pours into the hole in your stomach."
                    jump bogroadgameover01
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "tearing the armor on your back"
            else:
                if pc_hp <= 0:
                    $ custom1 = "Your foot gets stuck between a curvy root and the mud. Before you get it out, the cat gets close, but your movements are restricted. Still bent, you raise your weapon, but you don’t have time to prepare yourself for the pounce.\n\nThe water pours into the hole in your stomach."
                    jump bogroadgameover01
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom4 = "cutting your back"
            menu:
                'Right after your foot hits one of the roots hidden beneath the floating sludge, you realize that crossing the water is going to take some time - a luxury that you don’t have.
                \n\nThe bird and the cat try to get to you again, [custom4].
                '
                'Well, fleeing is not an option.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, fleeing is not an option.')
                    jump bogroadhelpingturn03plus

    label bogroadturn03attackingthebird:
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 5
        if pc_food == 3:
            $ d100roll -= 5
        if pc_food == 4:
            $ d100roll -= 10
        if armor == 4:
            $ d100roll -= 5
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter*2)
        else:
            $ d100roll -= (pc_battlecounter)
        $ d100roll -= (pc_hp*5)
        if bogroad_noclothes:
            $ d100roll -= 10
        if d100roll > 70: # fail
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your fine gambeson keeps you in one piece."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your gambeson keeps you in one piece."
            else:
                if pc_hp <= 0:
                    $ custom1 = "You spot the bird as it dives at you, then try to cut it - but it’s a miss. It pierces your eyes, and the cat’s jaws are closing onto your leg."
                    jump bogroadgameover01
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom4 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            menu:
                'You wait for the bird to dive at you, then take a swing, but your target evades the blade, then circles around you.
                \n\nBefore you return to the proper stance, the cat tries to knock you down again, getting stopped by your block, but still reaching you with a paw. [custom4]
                '
                'I move away, getting ready for the next attack.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move away, getting ready for the next attack.')
                    jump bogroadhelpingturn03plus
        elif d100roll > 40: # semi-success
            $ bogroad_birdkilled = 1
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your fine gambeson keeps you in one piece."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom4 = "Your gambeson keeps you in one piece."
            else:
                if pc_hp <= 0:
                    $ custom1 = "You spot the bird as it dives at you, then try to cut it - but it’s a miss. It pierces your eyes, and the cat’s jaws are closing onto your leg."
                    jump bogroadgameover01
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom4 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            menu:
                'You wait for the bird to dive at you, then take a swing. The blade sends the halves of the raven-sized creature into the water, to the enjoyment of the local scavengers. A few gray and red feathers are drifting next to you.
                \n\nStill, you weren’t fast enough to stay away from the cat. Before you return to the proper stance, it tries to knock you down again, getting stopped by your block, but still reaching you with a paw. [custom4]
                '
                'I move away, then take a look at the cat.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move away, then take a look at the cat.')
                    jump bogroadhelpingturn03plus
        else: # success
            label bogroadturn03attackingthebirdalt:
                $ bogroad_birdkilled = 1
                menu:
                    'You wait for the bird to dive at you, then take a swing, using your time to get further away from the cat. The blade sends the halves of the raven-sized creature into the water, to the enjoyment of the local scavengers. A few gray and red feathers are drifting next to you.
                    '
                    'I raise the axe and look at the cat.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise the axe and look at the cat.')
                        jump bogroadhelpingturn03plus

label bogroadleavingafterhelping01:
    $ bogroad_triedtohelp += 1
    if pc_goal == "iwanttohelp":
        $ pc_goal_iwanttohelppoints += 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if pc_likeshorsename:
        $ custom3 = "and you try to ease its soul with a few encouraging words, hoping it will leave you alone for a minute"
    else:
        $ custom3 = ", but you don’t have enough patience to bother with its fears right now"
    if bogroad_noclothes:
        $ custom2 = "You wash your skin, then put on your dry clothes. At least your boots won’t give you a cold."
    else:
        $ custom2 = "You consider washing your clothes, but you’d need a washtub for it, if not a stream. You put on as many dry clothes as you can find, hoping your wet boots won’t give you a cold."
    $ pc_battlecounter += 1
    menu:
        '[custom1]
        \n\nGasping, wet, and frustrated, you hobble back to the beaten path. {color=#f6d6bd}[horsename]{/color} seems worried [custom3]. [custom2]
        '
        'Well, I did my best. (disabled)' if pc_goal != "iwanttoberemembered" and pc_goal != "iwanttohelp":
            pass
        'At least I know no soul is in danger. (disabled)' if pc_goal == "iwanttohelp":
            pass
        'Such a waste of time. (disabled)' if pc_goal == "iwanttoberemembered":
            pass

label bogroadgameover01:
    $ pc_hp = limit_pc_hp(0)
    show minus5hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
    if pc_religion == "pagan":
        show areapicture gameover_alt at basicfade
    else:
        show areapicture gameover at basicfade
    menu:
        '[custom1]
        \n
        \n\n[pcname]’s soul has left its shell.
        '
        'Let me replay this encounter.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this encounter.')
            stop music fadeout 4.0
            $ renpy.load("combatsave")
