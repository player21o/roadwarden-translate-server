###################### HOWLERS LAIR
default howlerslair_firsttime = 0
default howlerslair_dmgtopc = 0
default howlerslair_corpse_status = 0 # "abandoned" / "seen" / "burned"
default howlerslair_corpse_timer = 0
default howlerslair_corpse_item = 0
default howlerslair_corpse_predator = 0

default howlerslair_advantage_points_bonus = 0
default howlerslair_advantage_points_needed = 5
default howlerslair_advantage_points = 0

default howlerslair_used_force = 0
default howlerslair_used_spell = 0
default howlerslair_used_shield = 0
default howlerslair_used_dragonhorn = 0
default howlerslair_used_crossbow = 0
default howlerslair_used_trollurine = 0
default howlerslair_used_blindingpowder = 0
default howlerslair_used_sharpeningpotion = 0
default howlerslairpileofbonesgathered = 0

label howlerslair01ALL:
    label howlerslair01:
        $ renpy.save("combatsave", extra_info='Combat Auto Save')
        nvl clear
        $ pc_area = "howlerslair"
        stop music fadeout 4.0
        play nature "audio/ambient/shortcutmeadow01.ogg" fadeout 2.0 fadein 3.0 volume 1.0
        show areapicture northernroadtofoggylake at basicfade
        $ quarters -= 3
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ world_known_areas += 1
        $ howlerslair_firsttime = 1
        $ renpy.force_autosave(take_screenshot=True, block=True)
        if persistent.deafmode:
            $ deafcustom1 = " The birds are answering each other through their songs, and the repetitive humming of insects numbs your senses."
        else:
            $ deafcustom1 = ""
        menu:
            'You’re more used to {color=#f6d6bd}[horsename]’s{/color} trot than to your own gait. You rush forward as if you’re tracking your next meal, or delivering a message.
            \n\nAfter a few minutes, the light dancing on the calm surface of the lake lures your eyes, and the whispering meadow calms down your breath.[deafcustom1]
            '
            'A fine opportunity for a stroll.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- A fine opportunity for a stroll.')
                $ quarters += 2
                menu:
                    'You stretch out, then allow your shoulders to rest for a bit. Your pace lets you observe the fish trying to catch their tiny prey above the water, the nests hidden among the branches, the mouse living in an old stump. So far, no larger beast has approached the road.
                    \n\nYou reach the trail of blood again, then the gully. The shadows cast by the trees makes you alert, as if you’re entering a very different world. Your axe is not much comfort. You take a better look at your belts, cords, and the rest of your equipment.
                    \n\nHaving no horse, you find a way to squeeze through the thicket.
                    '
                    'I walk down, into the valley.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk down, into the valley.')
                        jump howlerslair01a
            'I need no “calming down”. The less time I spend on the road, the better.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need no “calming down”. The less time I spend on the road, the better.')
                $ quarters += 1
                menu:
                    'You warm up your shoulders and focus on any movement that could belong to a lurking beast. You reach the trail of blood again, then the gully. The shadows cast by the trees make you aware, but not worried. You make sure your belts and cords are properly attached. The axe’s handle is solid, the head is firmly attached.
                    \n\nHaving no horse, you find a way to squeeze through the thicket.
                    '
                    'I walk down, into the valley.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk down, into the valley.')
                        jump howlerslair01a

    label howlerslair01a:
        show areapicture northernroadtohowlerslair at basicfade
        $ quarters += 2
        play nature "audio/ambient/howlerslair01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        if persistent.deafmode:
            $ deafcustom1 = "All of them call to each other with distracting, intermittent gurgling, but as you look through the darkness, there are countless more black-and-golden furs letting out the ghastly cries, dragged out with no end."
        else:
            $ deafcustom1 = "Their gurgling is distracting, but as you look through the darkness, there are countless more black-and-golden furs letting out the ghastly cries."
        menu:
            'Not much light gets through the tree crowns. The cauldron-shaped basin is filled with howls of monkeys and chirping of insects. As soon as you enter the lair, hundreds of throats burst up with threats and worries. Some of the monkeys run away, others gather in groups, following your movements like a loyal squad.
            \n\n[deafcustom1] This distant army is hardly aware of your arrival - most of them eat, sleep, or groom their companions. You follow the trail of blood, but it only leads farther downhill. Your head starts to spin from the overwhelming noise.
            '
            'Better not linger. I follow the trail, putting trust in the earplugs.' if item_earplugs:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Better not linger. I follow the trail, putting trust in the earplugs.')
                play nature "audio/ambient/howlerslair01alt.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                $ custom1 = "The sound gets gentler on your ears, but no matter how much you try, your thoughts keep returning to the vibrations in your head and stomach, and the blunt pain that grows slowly. Your plugged ears may keep you safer, but not for long."
                jump howlerslair02
            'I have to follow the trail... Even though I have nothing to plug my ears with.' if not item_earplugs:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have to follow the trail... Even though I have nothing to plug my ears with.')
                $ custom1 = "With every step, the blunt pain grows in your stomach and limbs. You shake your head to focus your eyes on what’s right in front of you, but the relief is brief. If this goes on for too long, you won’t be able to endure it."
                jump howlerslair02

    label howlerslair02:
        if howlerslair_advantage_points_bonus:
            $ custom2 = "Especially if they remember what happened to them the last time."
        else:
            $ custom2 = "Though it didn’t go so well the last time."
        menu:
            '[custom1]
            \n\nThe first large monkey touches the ground, but after you raise your axe and show your teeth, it climbs back up again - though you right away notice a similar movement on the other side. Nothing attacks you just yet.
            \n\nIt’s obvious that you, or any human, could never single-handedly put an end to such a grand pack of creatures, but if you broke through their strike, maybe the rest would be too afraid to push on. [custom2]
            '
            'I better rub the sharpening poison in my gums.' if item_sharpeningpotion and item_sharpeningpotion_used != day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may never get so far again. I need to use this opportunity.')
                $ item_sharpeningpotion_used = day
                $ item_sharpeningpotion -= 1
                $ pc_throwingxp += 20
                $ pc_battlecounter += 20
                menu:
                    'The taste of ash grows intense, while the world slows down. You blink a few times, getting used to the sharp lights and colors. Each gesture of yours is precise and conscious, your heavy breathing is full of excitement.
                    '
                    'Let’s get to it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        jump howlerslair03
            'I may never get so far again. I need to use this opportunity.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may never get so far again. I need to use this opportunity.')
                jump howlerslair03
            'There’s no way the huntress survived such a blood loss in the valley of monsters. I get back to {color=#f6d6bd}Foggy’s{/color}, no need to put myself in danger.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- There’s no way the huntress survived such a blood loss in the valley of monsters. I get back to {color=#f6d6bd}Foggy’s{/color}, no need to put myself in danger.')
                $ howlerslair_corpse_status = "abandoned"
                play nature "audio/ambient/shortcutmeadow01.ogg" fadeout 2.0 fadein 3.0 volume 1.0
                show areapicture northernroadtofoggylake at basicfade
                menu:
                    'You run your eyes over the few groups of beasts, then rush toward the gully. The monkeys triumphantly howl, giving you a headache, and chase after you until you reach the meadow. You have no doubt that they won’t flee from you ever again.
                    \n\nYou can only hope that {color=#f6d6bd}Efren{/color} will accept your explanation.
                    '
                    'Doesn’t take a sage to figure out what happened here.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Doesn’t take a sage to figure out what happened here.')
                        $ travel_destination = "foggylake"
                        jump finaldestinationafterevent
                    'I can’t risk my life for such a minor task.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t risk my life for such a minor task.')
                        $ travel_destination = "foggylake"
                        jump finaldestinationafterevent

    label howlerslair03:
        if howlerslair_advantage_points_bonus:
            $ howlerslair_advantage_points += 1
            $ custom1 = "The monkeys observe you with respect, pouting their lips and growling, but keeping their distance for quite a few breaths. Soon, the first monster falls from a high branch, breaking through the foliage of shrubs, then leaps at you with a shout."
        else:
            $ custom1 = "You hardly cover any distance before the first monster falls from a high branch, breaking through the foliage of shrubs, then leaps at you with a shout."
        if pc_class == "mage" and not howlerslair_used_spell:
            $ at_unlock_spell = 1
            $ at = 0
            $ manacost = 3
        if pc_class == "warrior" and not howlerslair_used_force:
            $ at_unlock_force = 1
            $ at = 0
        menu:
            '[custom1]
            \n\nYou reach for anything that could be of assistance to you.
            '
            'Time to put my training into practice.' ( condition="at == 'force' and not howlerslair_used_force" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to put my training into practice.')
                $ howlerslair_used_force = 1
                $ howlerslair_advantage_points += 1
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "With a few dancing steps you shorten the distance between you and the nearest beast. Confused, it tries to catch you, but you effortlessly elude it, then put all your strength into turning around, and your wide swing lands on the creature’s back. It falls to the ground, but you’re already far behind it. A few of the monkeys climb back up the trees, and as you go farther, the pressure weakens. Finally, you reach your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "With a few dancing steps you shorten the distance between you and the nearest beast. Confused, it tries to catch you, but you effortlessly elude it, then put all your strength into turning around, and your wide swing lands on the creature’s back. It falls to the ground, but you’re already far behind it.\n\nA few of the monkeys climb back up the trees, and as you go farther, the pressure weakens. "
                    jump howlerslair03selectingitem
            'The sharpening poison helps me avoid the attacks.' if item_sharpeningpotion_used and item_sharpeningpotion_used == day and not howlerslair_used_sharpeningpotion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The sharpening poison helps me avoid the attacks.')
                $ howlerslair_used_sharpeningpotion = 1
                $ howlerslair_advantage_points += 1
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "Your feet are like feathers, and the blurry shapes of the monsters can’t keep up with you. For a moment you forget where you are, until you slip away from the grasp of one of the monkeys. You try to collect your senses, while the pack finally yields, allowing you to reach your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "Your feet are like feathers, and the blurry shapes of the monsters can’t keep up with you. For a moment you forget where you are, until you slip away from the grasp of one of the monkeys. You try to collect your senses.\n\n"
                    jump howlerslair03selectingitem
            'My pneuma is too weak to help me. (disabled)' ( condition= "at_unlock_spell == 1 and mana < manacost and not howlerslair_used_spell" ):
                pass
            'I grab my willow wand, ready to strike a beast with pneuma. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and mana >= manacost and not howlerslair_used_spell" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my willow wand, ready to strike a beast with pneuma.')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                $ howlerslair_used_spell = 1
                $ howlerslair_advantage_points += 1
                $ mana = limit_mana(mana-manacost)
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "You focus on channeling the direction of the pneuma, then push an invisible wave right at the monkey that tried to land next to you, sending it flying. It hits a tree trunk and twists disquietingly, then falls into the shrubs. You move ahead through the terrified and furious shouts and hide your wand. It takes you a few moments to realize that nothing chases after you - you’ve reached your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "You focus on channeling the direction of the pneuma, then push an invisible wave right at the monkey that tried to land next to you, sending it flying. It hits a tree trunk and twists disquietingly, then falls into the shrubs. You move ahead through the terrified and furious shouts and hide your wand.\n\n"
                    jump howlerslair03selectingitem
            'I take a few deep breaths, ready to push away as many monkeys as my soul allows. [[Cost: {color=#f6d6bd}5{/color}]' ( condition="at == 'spell' and mana >= 5 and not howlerslair_used_spell" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a few deep breaths, ready to push away as many monkeys as my soul allows.')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {i}-%5 pneuma.{/i}')
                $ howlerslair_used_spell = 1
                $ howlerslair_advantage_points += 2
                $ mana = limit_mana(mana-5)
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "You focus on channeling the direction of the pneuma, then push an invisible wave at the tree that blocks your way, or rather - at its residents, sending a whole group of beasts into the air. Their angry screams are loud enough to cut through the onslaught of furious and terrified howls, and while most of them get right up and climb up the trees slowly, a few were less lucky - they either landed harshly on the ground, or hit the trunks with their backs.\n\nBut you don’t have time to count monkeys. You move forward and hide your wand. It takes you a few moments to realize that nothing chases after you - you’ve reached your destination. "
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "You focus on channeling the direction of the pneuma, then push an invisible wave at the tree that blocks your way, or rather - at its residents, sending a whole group of beasts into the air. Their angry screams are loud enough to cut through the onslaught of furious and terrified howls, and while most of them get right up and climb up the trees slowly, a few were less lucky - they either landed harshly on the ground, or hit the trunks with their backs.\n\nBut you don’t have time to count monkeys. You move forward and hide your wand. "
                    jump howlerslair03selectingitem
            'If anything jumps at me, I’ll push it away with my shield.' if item_shield and not howlerslair_used_shield:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- If anything jumps at me, I’ll push it away with my shield.')
                $ howlerslair_used_shield = 1
                $ howlerslair_advantage_points += 1
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "You do so once or twice, but you can’t move forward while putting so much effort into defense. After a minute or so, you change your strategy, and start to use the shield to run through the groups of enemies. Those who don’t spread out right away turn out to be too inexperienced in warfare, and once you bash into them, they land under your boots. It’s an exhausting strategy, but after a while, the pack finally yields, allowing you to reach your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "You do so once or twice, but you can’t move forward while putting so much effort into defense. After a minute or so, you change your strategy, and start to use the shield to run through the groups of enemies. Those who don’t spread out right away turn out to be too inexperienced in warfare, and once you bash into them, they land under your boots.\n\nIt’s an exhausting strategy, but once you return to simpler blocks, a few of the groups have already backed down.\n\n"
                    jump howlerslair03selectingitem
            'Not much time to aim, but I can stop one of the charging beasts with my crossbow.' if item_crossbow and item_crossbowquarrels and not howlerslair_used_crossbow:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Not much time to aim, but I can stop one of the charging beasts with my crossbow.')
                $ howlerslair_used_crossbow = 1
                $ howlerslair_advantage_points += 1
                $ item_crossbowquarrels -= 1
                $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "There’s a lot of creatures to choose from, and since they’re unfamiliar with your weapon, hitting one of them right in the skull is as easy as pulling the trigger. Without so much as a gasp, the creature plunges to the ground. You don’t have time to reload, but the monkeys don’t know it yet. After a few moments you realize that the pack yields - you’ve reached your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "There’s a lot of creatures to choose from, and since they’re unfamiliar with your weapon, hitting one of them right in the skull is as easy as pulling the trigger. Without so much as a gasp, the creature plunges to the ground.\n\nYou don’t have time to reload, but the monkeys don’t know it yet. For some time, you walk undisturbed.\n\n"
                    jump howlerslair03selectingitem
            'Too bad I don’t have any quarrels. (disabled)' if item_crossbow and not item_crossbowquarrels and not howlerslair_used_crossbow:
                pass
            'I don’t have a crossbow. (disabled)' if not item_crossbow:
                pass
            'Better to scare some of them with the troll urine.' if item_trollurine and not howlerslair_used_trollurine:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Better to scare some of them with the troll urine.')
                $ howlerslair_used_trollurine = 1
                $ howlerslair_advantage_points += 1
                $ cleanliness = limit_cleanliness(cleanliness-2)
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "You open the “repellent” and generously scatter it around, though a splash of it also lands on your pants and hands, instantly making you regret it. But you don’t have to wait for the effects long - half of the animals climb up the trees again, many others are fleeing through the thicket. The howls get lower, and you keep spilling the urine for another minute, until you realize that the pack yields - you’ve reached your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "You open the “repellent” and generously scatter it around, though a splash of it also lands on your pants and hands, instantly making you regret it. But you don’t have to wait for the effects long - half of the animals climb up the trees again, many others are fleeing through the thicket. The howls get lower, and you keep spilling the urine for another minute, until the beasts gather enough courage to ignore it.\n\n"
                    jump howlerslair03selectingitem
            'Time for my blinding powder.' if item_blindingpowder and not howlerslair_used_blindingpowder:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for my blinding powder.')
                $ howlerslair_used_blindingpowder = 1
                $ howlerslair_advantage_points += 1
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "You throw it in front of you and jump away from the monkeys. You don’t look at them for a few heartbeats, but their painful screams assure you that the dust is working. They cover their faces with their large hands, landing on their buns or moving away in panic. The remaining few are standing still, not sure what exactly happened. You move forward, keeping your hand in the bag, but after a few moments you realize that the pack yields - you’ve reached your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "You throw it in front of you and jump away from the monkeys. You don’t look at them for a few heartbeats, but their painful screams assure you that the dust is working. They cover their faces with their large hands, landing on their buns or moving away in panic. The remaining few are standing still, not sure what exactly happened.\n\nAfter you get deeper into the forest, you try to repeat this attack, but this time the creatures are aware of the threat, doing their best to duck. You hide the remaining dust before it goes to waste.\n\n"
                    jump howlerslair03selectingitem
            'I don’t have a potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                pass
            'I’m out of options. I move forward, relying solely on my axe.' if not item_axe03 and not item_golemglove:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m out of options. I move forward, relying solely on my axe.')
                $ custom2 = ""
                jump howlerslair04
            'I’m out of options, but The Golem Glove will help me get through.' if item_golemglove and not item_axe03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m out of options, but The Golem Glove will help me get through.')
                $ howlerslair_advantage_points += 1
                $ custom2 = ""
                jump howlerslair04
            'I’m out of options, but my fine battle axe will help me get through.' if item_axe03 and not item_golemglove:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m out of options, but my fine battle axe will help me get through.')
                $ howlerslair_advantage_points += 1
                $ custom2 = ""
                jump howlerslair04
            'I’m out of options, but the combination of The Golem Glove and my fine battle axe will help me get through.' if item_golemglove and item_axe03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m out of options, but the combination of The Golem Glove and my fine battle axe will help me get through.')
                $ howlerslair_advantage_points += 2
                $ custom2 = ""
                jump howlerslair04

    label howlerslair03selectingitem:
        if pc_class == "mage" and not howlerslair_used_spell:
            $ at_unlock_spell = 1
            $ at = 0
            $ manacost = 3
        else:
            $ at_unlock_spell = 0
            $ at = 0
        if pc_class == "warrior" and not howlerslair_used_force:
            $ at_unlock_force = 1
            $ at = 0
        else:
            $ at_unlock_force = 0
            $ at = 0
        if howlerslair_advantage_points == 1:
            $ custom3 = "As you look ahead, you see no end of the blood trail. It may be that the creature carried the huntress to the very end of the valley, not to its center."
        elif howlerslair_advantage_points == 2:
            $ custom3 = "The forest gets darker, but the trail of blood is still easy to follow, which may not be a good sign."
        elif howlerslair_advantage_points == 3:
            $ custom3 = "The trail of blood gets weaker, and you estimate that the middle of the valley is already behind you."
        elif howlerslair_advantage_points == 4:
            $ custom3 = "The trail of blood is scarce, and you think it leads into the brighter part of the valley. As you approach the rock face, the forest gets sparser."
        else:
            $ custom3 = ""
        menu:
            '[custom2][custom3]
            '
            'Time to put my training into practice.' ( condition="at == 'force' and not howlerslair_used_force" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to put my training into practice.')
                $ howlerslair_used_force = 1
                $ howlerslair_advantage_points += 1
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "With a few dancing steps you shorten the distance between you and the nearest beast. Confused, it tries to catch you, but you effortlessly elude it, then put all your strength into turning around, and your wide swing lands on the creature’s back. It falls to the ground, but you’re already far behind it. A few of the monkeys climb back up the trees, and as you go farther, the pressure weakens. Finally, you reach your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "With a few dancing steps you shorten the distance between you and the nearest beast. Confused, it tries to catch you, but you effortlessly elude it, then put all your strength into turning around, and your wide swing lands on the creature’s back. It falls to the ground, but you’re already far behind it.\n\nA few of the monkeys climb back up the trees, and as you go farther, the pressure weakens. "
                    jump howlerslair03selectingitem
            'The sharpening poison helps me avoid the attacks.' if item_sharpeningpotion_used and item_sharpeningpotion_used == day and not howlerslair_used_sharpeningpotion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The sharpening poison helps me avoid the attacks.')
                $ howlerslair_used_sharpeningpotion = 1
                $ howlerslair_advantage_points += 1
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "Your feet are like feathers, and the blurry shapes of the monsters can’t keep up with you. For a moment you forget where you are, until you slip away from the grasp of one of the monkeys. You try to collect your senses, while the pack finally yields, allowing you to reach your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "Your feet are like feathers, and the blurry shapes of the monsters can’t keep up with you. For a moment you forget where you are, until you slip away from the grasp of one of the monkeys. You try to collect your senses.\n\n"
                    jump howlerslair03selectingitem
            'My pneuma is too weak to help me. (disabled)' ( condition= "at_unlock_spell == 1 and mana < manacost and not howlerslair_used_spell" ):
                pass
            'I grab my willow wand, ready to strike a beast with pneuma. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and mana >= manacost and not howlerslair_used_spell" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my willow wand, ready to strike a beast with pneuma.')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                $ howlerslair_used_spell = 1
                $ howlerslair_advantage_points += 1
                $ mana = limit_mana(mana-manacost)
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "You focus on channeling the direction of the pneuma, then push an invisible wave right at the monkey that tried to land next to you, sending it flying. It hits a tree trunk and twists disquietingly, then falls into the shrubs. You move ahead through the terrified and furious shouts and hide your wand. It takes you a few moments to realize that nothing chases after you - you’ve reached your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "You focus on channeling the direction of the pneuma, then push an invisible wave right at the monkey that tried to land next to you, sending it flying. It hits a tree trunk and twists disquietingly, then falls into the shrubs. You move ahead through the terrified and furious shouts and hide your wand.\n\n"
                    jump howlerslair03selectingitem
            'I take a few deep breaths, ready to push away as many monkeys as my soul allows. [[Cost: {color=#f6d6bd}5{/color}]' ( condition="at == 'spell' and mana >= 5 and not howlerslair_used_spell" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a few deep breaths, ready to push away as many monkeys as my soul allows.')
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {i}-%5 pneuma.{/i}')
                $ howlerslair_used_spell = 1
                $ howlerslair_advantage_points += 2
                $ mana = limit_mana(mana-5)
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "You focus on channeling the direction of the pneuma, then push an invisible wave at the tree that blocks your way, or rather - at its residents, sending a whole group of beasts into the air. Their angry screams are loud enough to cut through the onslaught of furious and terrified howls, and while most of them get right up and climb up the trees slowly, a few were less lucky - they either landed harshly on the ground, or hit the trunks with their backs.\n\nBut you don’t have time to count monkeys. You move forward and hide your wand. It takes you a few moments to realize that nothing chases after you - you’ve reached your destination. "
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "You focus on channeling the direction of the pneuma, then push an invisible wave at the tree that blocks your way, or rather - at its residents, sending a whole group of beasts into the air. Their angry screams are loud enough to cut through the onslaught of furious and terrified howls, and while most of them get right up and climb up the trees slowly, a few were less lucky - they either landed harshly on the ground, or hit the trunks with their backs.\n\nBut you don’t have time to count monkeys. You move forward and hide your wand. "
                    jump howlerslair03selectingitem
            'If anything jumps at me, I’ll push it away with my shield.' if item_shield and not howlerslair_used_shield:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- If anything jumps at me, I’ll push it away with my shield.')
                $ howlerslair_used_shield = 1
                $ howlerslair_advantage_points += 1
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "You do so once or twice, but you can’t move forward while putting so much effort into defense. After a minute or so, you change your strategy, and start to use the shield to run through the groups of enemies. Those who don’t spread out right away turn out to be too inexperienced in warfare, and once you bash into them, they land under your boots. It’s an exhausting strategy, but after a while, the pack finally yields, allowing you to reach your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "You do so once or twice, but you can’t move forward while putting so much effort into defense. After a minute or so, you change your strategy, and start to use the shield to run through the groups of enemies. Those who don’t spread out right away turn out to be too inexperienced in warfare, and once you bash into them, they land under your boots.\n\nIt’s an exhausting strategy, but once you return to simpler blocks, a few of the groups have already backed down. "
                    jump howlerslair03selectingitem
            'Not much time to aim, but I can stop one of the charging beasts with my crossbow.' if item_crossbow and item_crossbowquarrels and not howlerslair_used_crossbow:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Not much time to aim, but I can stop one of the charging beasts with my crossbow.')
                $ howlerslair_used_crossbow = 1
                $ howlerslair_advantage_points += 1
                $ item_crossbowquarrels -= 1
                $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "There’s a lot of creatures to choose from, and since they’re unfamiliar with your weapon, hitting one of them right in the skull is as easy as pulling the trigger. Without so much as a gasp, the creature plunges to the ground. You don’t have time to reload, but the monkeys don’t know it yet. After a few moments you realize that the pack yields - you’ve reached your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "There’s a lot of creatures to choose from, and since they’re unfamiliar with your weapon, hitting one of them right in the skull is as easy as pulling the trigger. Without so much as a gasp, the creature plunges to the ground.\n\nYou don’t have time to reload, but the monkeys don’t know it yet. For some time, you walk undisturbed. "
                    jump howlerslair03selectingitem
            'Too bad I don’t have any quarrels. (disabled)' if item_crossbow and not item_crossbowquarrels and not howlerslair_used_crossbow:
                pass
            'I don’t have a crossbow. (disabled)' if not item_crossbow:
                pass
            'Better to scare some of them with the troll urine.' if item_trollurine and not howlerslair_used_trollurine:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Better to scare some of them with the troll urine.')
                $ howlerslair_used_trollurine = 1
                $ howlerslair_advantage_points += 1
                $ cleanliness = limit_cleanliness(cleanliness-2)
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "You open the “repellent” and generously scatter it around, though a splash of it also lands on your pants and hands, instantly making you regret it. But you don’t have to wait for the effects long - half of the animals climb up the trees again, many others are fleeing through the thicket. The howls get lower, and you keep spilling the urine for another minute, until you realize that the pack yields - you’ve reached your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "You open the “repellent” and generously scatter it around, though a splash of it also lands on your pants and hands, instantly making you regret it. But you don’t have to wait for the effects long - half of the animals climb up the trees again, many others are fleeing through the thicket. The howls get lower, and you keep spilling the urine for another minute, until the beasts gather enough courage to ignore it.\n\n"
                    jump howlerslair03selectingitem
            'Time for my blinding powder.' if item_blindingpowder and not howlerslair_used_blindingpowder:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for my blinding powder.')
                $ howlerslair_used_blindingpowder = 1
                $ howlerslair_advantage_points += 1
                if howlerslair_advantage_points >= howlerslair_advantage_points_needed:
                    $ custom2 = "You throw it in front of you and jump away from the monkeys. You don’t look at them for a few heartbeats, but their painful screams assure you that the dust is working. They cover their faces with their large hands, landing on their buns or moving away in panic. The remaining few are standing still, not sure what exactly happened. You move forward, keeping your hand in the bag, but after a few moments you realize that the pack yields - you’ve reached your destination.\n\n"
                    jump howlerslair05reachingbythemselves
                else:
                    $ custom2 = "You throw it in front of you and jump away from the monkeys. You don’t look at them for a few heartbeats, but their painful screams assure you that the dust is working. They cover their faces with their large hands, landing on their buns or moving away in panic. The remaining few are standing still, not sure what exactly happened.\n\nAfter you get deeper into the forest, you try to repeat this attack, but this time the creatures are aware of the threat, doing their best to duck. You hide the remaining dust before it goes to waste.\n\n"
                    jump howlerslair03selectingitem
            'I don’t have a potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                pass
            'I’m out of options. I move forward, relying solely on my axe.' if not item_axe03 and not item_golemglove:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m out of options. I move forward, relying solely on my axe.')
                $ custom2 = ""
                jump howlerslair04
            'I’m out of options, but The Golem Glove will help me get through.' if item_golemglove and not item_axe03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m out of options, but The Golem Glove will help me get through.')
                $ howlerslair_advantage_points += 1
                $ custom2 = ""
                jump howlerslair04
            'I’m out of options, but my fine battle axe will help me get through.' if item_axe03 and not item_golemglove:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m out of options, but my fine battle axe will help me get through.')
                $ howlerslair_advantage_points += 1
                $ custom2 = ""
                jump howlerslair04
            'I’m out of options, but the combination of The Golem Glove and my fine battle axe will help me get through.' if item_golemglove and item_axe03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m out of options, but the combination of The Golem Glove and my fine battle axe will help me get through.')
                $ howlerslair_advantage_points += 2
                $ custom2 = ""
                jump howlerslair04

    label howlerslair04:
        $ at_unlock_spell = 0
        $ at_unlock_force = 0
        $ at = 0
        if not item_earplugs:
            $ custom1 = "Your head aches, your face is coevered in sweat, which now gets to your eyes, distracting your steps and slowing you down almost as much as your adversaries."
            $ howlerslair_advantage_points -= 1
        else:
            $ custom1 = "Your head starts to ache from all the howls and shouts, your face is covered in sweat."
        $ custom5 = (howlerslair_advantage_points_needed-howlerslair_advantage_points)
        $ custom6 = (pc_hp+armor-3)
        if (custom6-custom5) <= 0:
            $ pc_hp = limit_pc_hp(0)
            show minus5hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
            show areapicture gameover at basicfade
            menu:
                'You push forward, struggling to find a path between the remaining groups of monkeys. You duck, leap, sprint, and at one point you manage to reach the final group. You swing your blade left and right, hoping to squeeze through the wall of black-and-golden furs...
                \n\nA strong arm clasps around your waist. You hit the ground, trampled by feet. The blunt pain in your leg is followed by something tearing it off.
                \n
                \n\n[pcname]’s soul has left its shell.
                '
                'Let me replay this encounter.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this encounter.')
                    stop music fadeout 4.0
                    $ renpy.load("combatsave")
        elif (custom6-custom5) <= 1:
            if not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                $ cleanliness = limit_cleanliness(cleanliness-3)
                show minus4appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 appearance points.{/i}')
            else:
                $ cleanliness = limit_cleanliness(cleanliness-3)
                show minus3appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
            if armor == 4:
                $ howlerslair_dmgtopc += 1
                $ armor = limit_armor(armor-2)
                show minus2armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            elif armor == 3:
                $ howlerslair_dmgtopc += 2
                $ armor = limit_armor(armor-2)
                show minus2armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            elif armor == 2:
                $ howlerslair_dmgtopc += 3
                $ armor = limit_armor(armor-2)
                show minus2armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-3)
                show minus3hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
            elif armor == 1:
                $ howlerslair_dmgtopc += 4
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-4)
                show minus4hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
            else:
                $ howlerslair_dmgtopc += 5
                $ pc_hp = limit_pc_hp(pc_hp-5)
                show minus5hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
            $ custom3 = "Holding your axe, you duck, leap, sprint, and at one point you reach the final group. You swing left and right, hoping to squeeze through the wall of black-and-golden furs. Then, a strong arm clasps around your waist and throws you. You hit the ground, where animal feet trample your shell.\n\nLarge hands try to pull off your leg, but You shout, gathering the remains of your strength. You release your arm, and the blade hits the beasts’ legs, shoulders, skulls - you can’t tell if the blood on your neck is yours. The grasp of howlers falters. You stand up and run for it, and the whining pack doesn’t follow."
        elif (custom6-custom5) <= 2:
            if not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                $ cleanliness = limit_cleanliness(cleanliness-2)
                show minus3appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
            else:
                $ cleanliness = limit_cleanliness(cleanliness-2)
                show minus3appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            if armor == 4:
                $ howlerslair_dmgtopc += 1
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            elif armor == 3:
                $ howlerslair_dmgtopc += 1
                $ armor = limit_armor(armor-2)
                show minus2armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            elif armor == 2:
                $ howlerslair_dmgtopc += 2
                $ armor = limit_armor(armor-2)
                show minus2armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            elif armor == 1:
                $ howlerslair_dmgtopc += 3
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-3)
                show minus3hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
            else:
                $ howlerslair_dmgtopc += 4
                $ pc_hp = limit_pc_hp(pc_hp-4)
                show minus4hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
            $ custom3 = "Holding your axe, you duck, leap, sprint, and at one point you manage to reach the final group. You swing left and right, hoping to squeeze through the wall of black-and-golden furs. Then, a strong arm clasps around your waist and throws you. You hit the ground, where animal feet trample your shell.\n\nYou feel the hands clasping onto your legs, but You shout, gathering the remains of your strength. You release your arm, and the blade hits the beasts’ legs, shoulders, skulls - you can’t tell if the blood on your neck is yours. The grasp of howlers falters. You stand up and run for it, and the whining pack doesn’t follow."
        elif (custom6-custom5) <= 3:
            if not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                $ cleanliness = limit_cleanliness(cleanliness-2)
                show minus3appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
            else:
                $ cleanliness = limit_cleanliness(cleanliness-2)
                show minus3appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            if armor == 4:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            elif armor == 3:
                $ howlerslair_dmgtopc += 1
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            elif armor == 2:
                $ howlerslair_dmgtopc += 2
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            elif armor == 1:
                $ howlerslair_dmgtopc += 3
                $ pc_hp = limit_pc_hp(pc_hp-3)
                show minus3hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
            else:
                $ howlerslair_dmgtopc += 4
                $ pc_hp = limit_pc_hp(pc_hp-4)
                show minus4hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
            $ custom3 = "Holding your axe, you duck, leap, sprint, and at one point you manage to reach the final group. You swing left and right, hoping to squeeze through the wall of black-and-golden furs. Then, a strong arm clasps around your waist and throws you. You hit the ground, where animal feet trample your shell.\n\nYou shout, gathering the remains of your strength. You release your arm, and the blade hits the beasts’ legs, shoulders, skulls - you can’t tell if the blood on your neck is yours. The grasp of howlers falters. You stand up and run for it, and the whining pack doesn’t follow."
        elif (custom6-custom5) <= 4:
            if not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            else:
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor == 4:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            elif armor == 3:
                $ howlerslair_dmgtopc += 1
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            elif armor == 2:
                $ howlerslair_dmgtopc += 2
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            elif armor == 1:
                $ howlerslair_dmgtopc += 3
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            else:
                $ howlerslair_dmgtopc += 3
                $ pc_hp = limit_pc_hp(pc_hp-3)
                show minus3hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
            $ custom3 = "Holding your axe, you duck, leap, sprint, and at one point you manage to reach the final group. You swing left and right, hoping to squeeze through the wall of black-and-golden furs. Then, a strong arm clasps around your waist and throws you. You hit the ground, where animal feet trample your shell.\n\nYou shout, gathering the remains of your strength. You release your arm, and the blade hits the beasts’ legs, shoulders, skulls - you can’t tell if the blood on your neck is yours. The grasp of howlers falters. You stand up and run for it, and the whining pack doesn’t follow."
        elif (custom6-custom5) <= 5:
            if not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            elif armor == 2:
                $ howlerslair_dmgtopc += 1
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            else:
                $ howlerslair_dmgtopc += 2
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            $ custom3 = "Holding your axe, you duck, lunge, sprint, and at one point you manage to reach the final group. You swing left and right, hoping to squeeze through the wall of black-and-golden furs. Then, a strong arm clasps around your waist and throws you into the air, but you land on your feet.\n\nYou shout, gathering the remains of your strength. Your blade hits the beasts’ legs, shoulders, skulls - you can’t tell if the blood on your neck is yours. You run for it, and the whining pack doesn’t follow."
        else:
            $ custom3 = "Holding your axe, you duck, lunge, sprint, and at one point you manage to reach the final group. You swing left and right, and your fine blade hits the beasts’ legs, shoulders, skulls - you can’t tell if the blood on your neck is yours. You run for it, and the whining pack doesn’t follow."
        menu: # 1 - earplugs, 2 - the last used item, if any, 3 - general description
            '[custom1] [custom2][custom3]
            '
            'What do I find at the end of the blood trail?':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- What do I find at the end of the blood trail?')
                jump howlerslair05reachingafterfight

    label howlerslair05reachingafterfight:
        $ pc_battlecounter += 1
        $ quest_missinghunters_daliafound = 1
        if not item_earplugs:
            $ custom1 = "especially without anything to plug your ears"
        else:
            $ custom1 = "but your plugged ears {i}may{/i} give you enough time to look around"
            $ howlerslair_corpse_timer -= 1
        $ can_potions = 1
        menu:
            'It leads you to a lone, treeless, rocky mound at the edge of the valley. The light falls on the short grasses and flowers growing around the pale human bones. The flesh is almost scraped clean, and the few ravens feasting on them lazily move aside, at first observing you, then preening their feathers.
            \n\nThe remains are resting in a pool of dark blood, now serving as a breeding ground for worms. The torn clothes are spread around, most of them made of leather and rawhide.
            \n\nThe howls reach you again. The monkeys may be far away, but their presence is overwhelming. You can’t prepare a pyre with the constantly increasing pain in your head and stomach, [custom1].
            '
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass
            'I press the dragon horn to my lips and blow as hard as I can.' if item_dragonhorn and not howlerslair_used_dragonhorn:
                jump howlerslair05horn
            'I look for the beast that brought the shell here.' if not howlerslair_corpse_predator:
                jump howlerslair05lookingforpredator
            'I search the huntresses’ possessions.' if not howlerslair_corpse_item:
                jump howlerslair05bonebuckle
            'I collect the bones to carry them with me.' if not howlerslairpileofbonesgathered:
                jump howlerslair05carrying
            'I’m not staying here any longer. I found her shell, that should be enough.':
                jump howlerslairseen

    label howlerslair05reachingbythemselves:
        $ at_unlock_spell = 0
        $ at_unlock_force = 0
        $ at = 0
        $ pc_battlecounter += 1
        $ quest_missinghunters_daliafound = 1
        if not item_earplugs:
            $ custom1 = "especially without anything to plug your ears"
        else:
            $ custom1 = "but your plugged ears may give you enough time to look around"
            $ howlerslair_corpse_timer -= 1
        $ can_potions = 1
        menu:
            '[custom2]The trail leads you to a lone, treeless, rocky mound at the edge of the valley. The light falls on the short grasses and flowers growing around the pale human bones. The flesh is almost scraped clean, and the few ravens feasting on them lazily move aside, at first observing you, then preening their feathers.
            \n\nThe remains are resting in a pool of dark blood, now serving as a breeding ground for worms. The torn clothes are spread around, most of them made of leather and rawhide.
            \n\nThe howls reach you again. The monkeys may be far away, but their presence is overwhelming. You can’t prepare a pyre with the constantly increasing pain in your head and stomach, [custom1].
            '
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass
            'I press the dragon horn to my lips and blow as hard as I can.' if item_dragonhorn and not howlerslair_used_dragonhorn:
                jump howlerslair05horn
            'I look for the beast that brought the shell here.' if not howlerslair_corpse_predator:
                jump howlerslair05lookingforpredator
            'I search the huntresses’ possessions.' if not howlerslair_corpse_item:
                jump howlerslair05bonebuckle
            'I collect the bones to carry them with me.' if not howlerslairpileofbonesgathered:
                jump howlerslair05carrying
            'I’m not staying here any longer. I found her shell, that should be enough.' if not howlerslairpileofbonesgathered and not howlerslair_corpse_item:
                jump howlerslairseen
            'I leave this place.' if not howlerslairpileofbonesgathered or howlerslair_corpse_item:
                jump howlerslaircollectedsomething

    label howlerslair05horn:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I press the dragon horn to my lips and blow as hard as I can.')
        $ howlerslair_used_dragonhorn = 1
        $ howlerslair_corpse_timer = 0
        play nature "audio/ambient/howlerslair02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        menu:
            'The terrifying shout of a monster hits the trees and fills their shadows. There are still some anxious growls coming from the larger beasts, now clenching onto the tree trunks, but the more distant howls don’t hurt you as much.
            \n\nYou wipe the sweat off your forehead. You may be the center of attention, but you doubt anything is going to oppose you now.
            '
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass
            'I press the dragon horn to my lips and blow as hard as I can.' if item_dragonhorn and not howlerslair_used_dragonhorn:
                jump howlerslair05horn
            'I look for the beast that brought the shell here.' if not howlerslair_corpse_predator:
                jump howlerslair05lookingforpredator
            'I search the huntresses’ possessions.' if not howlerslair_corpse_item:
                jump howlerslair05bonebuckle
            'I collect the bones to carry them with me.' if not howlerslairpileofbonesgathered:
                jump howlerslair05carrying
            'I’m not staying here any longer. I found her shell, that should be enough.' if not howlerslairpileofbonesgathered and not howlerslair_corpse_item:
                jump howlerslairseen
            'I leave this place.' if not howlerslairpileofbonesgathered or howlerslair_corpse_item:
                jump howlerslaircollectedsomething

    label howlerslair05lookingforpredator:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for the beast that brought the shell here.')
        $ howlerslair_corpse_predator = 1
        $ howlerslair_corpse_timer += 1
        if howlerslair_used_dragonhorn:
            $ custom1 = "Ever since you used the dragon horn, your stomach and head have been calming down."
        elif howlerslair_corpse_timer < 1:
            $ custom1 = "The howls are crawling underneath your skin. You’re on the edge of losing your senses."
        else:
            if not pc_hp:
                jump howlerslairsoundgameover01
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom1 = "The howls are shaking your shell so much that you feel as if your bones are going to break soon."
        menu:
            'You spot not a single wolf, bear, or cat. The paw prints surrounding the corpse are so muddled that they’re hard to identify, yet none are so fresh that you should worry about them. One thing that catches your attention is that there are no marks of ape feet anywhere nearby.
            \n\n[custom1]
            '
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass
            'I press the dragon horn to my lips and blow as hard as I can.' if item_dragonhorn and not howlerslair_used_dragonhorn:
                jump howlerslair05horn
            'I look for the beast that brought the shell here.' if not howlerslair_corpse_predator:
                jump howlerslair05lookingforpredator
            'I search the huntresses’ possessions.' if not howlerslair_corpse_item:
                jump howlerslair05bonebuckle
            'I collect the bones to carry them with me.' if not howlerslairpileofbonesgathered:
                jump howlerslair05carrying
            'I’m not staying here any longer. I found her shell, that should be enough.' if not howlerslairpileofbonesgathered and not howlerslair_corpse_item:
                jump howlerslairseen
            'I leave this place.' if not howlerslairpileofbonesgathered or howlerslair_corpse_item:
                jump howlerslaircollectedsomething

    label howlerslair05bonebuckle:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the huntresses’ possessions.')
        $ howlerslair_corpse_timer += 1
        if howlerslair_used_dragonhorn:
            $ custom1 = "Ever since you used the dragon horn, your stomach and head have been calming down."
        elif howlerslair_corpse_timer < 1:
            $ custom1 = "The howls are crawling underneath your skin. You’re on the edge of losing your senses."
        else:
            if not pc_hp:
                jump howlerslairsoundgameover01
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom1 = "The howls are shaking your shell so much that you feel as if your bones are going to break soon."
        $ item_bonebuckle = 1
        $ howlerslair_corpse_item = 1
        $ creek_woodenweapons = 1
        $ renpy.notify("You found a decorative belt buckle.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a decorative belt buckle.{/i}')
        menu:
            'The now soggy club with an unusual row of {i}teeth{/i} carved in its edge is of no value to you. There’s no sack or bag in sight, and after you investigate the clothes, you estimate that the only unspoiled, undamaged thing around is the pretty belt buckle made of yellowish bone, carved into the shape of a jumping boar. You hide it in your pocket.
            \n\n[custom1]
            '
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass
            'I press the dragon horn to my lips and blow as hard as I can.' if item_dragonhorn and not howlerslair_used_dragonhorn:
                jump howlerslair05horn
            'I look for the beast that brought the shell here.' if not howlerslair_corpse_predator:
                jump howlerslair05lookingforpredator
            'I search the huntresses’ possessions.' if not howlerslair_corpse_item:
                jump howlerslair05bonebuckle
            'I collect the bones to carry them with me.' if not howlerslairpileofbonesgathered:
                jump howlerslair05carrying
            'I’m not staying here any longer. I found her shell, that should be enough.' if not howlerslairpileofbonesgathered and not howlerslair_corpse_item:
                jump howlerslairseen
            'I leave this place.' if not howlerslairpileofbonesgathered or howlerslair_corpse_item:
                jump howlerslaircollectedsomething

    label howlerslair05carrying:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I collect the bones to carry them with me.')
        $ howlerslair_corpse_timer += 2
        if howlerslair_used_dragonhorn:
            $ custom1 = "Ever since you used the dragon horn, your stomach and head have been calming down."
        elif howlerslair_corpse_timer < 1:
            $ custom1 = "The howls are crawling underneath your skin. You’re on the edge of losing your senses."
        else:
            if not pc_hp:
                jump howlerslairsoundgameover01
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom1 = "The howls are shaking your shell so much that you feel as if your bones are going to break soon."
        $ item_pileofbones = 1
        $ howlerslairpileofbonesgathered = 1
        $ renpy.notify("You collect a pile of human bones.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You collect a pile of human bones.{/i}')
        menu:
            'Since they’re detached from each other, you shove them all into a sack. The skull, spine, ribs, pelvis... Too many of them to wonder if they’re complete. They’re warm from the sun.
            \n\nThe stench of rotten blood is gut wrenching, and you gladly step away from it.
            '
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass
            'I press the dragon horn to my lips and blow as hard as I can.' if item_dragonhorn and not howlerslair_used_dragonhorn:
                jump howlerslair05horn
            'I look for the beast that brought the shell here.' if not howlerslair_corpse_predator:
                jump howlerslair05lookingforpredator
            'I search the huntresses’ possessions.' if not howlerslair_corpse_item:
                jump howlerslair05bonebuckle
            'I collect the bones to carry them with me.' if not howlerslairpileofbonesgathered:
                jump howlerslair05carrying
            'I’m not staying here any longer. I found her shell, that should be enough.' if not howlerslairpileofbonesgathered and not howlerslair_corpse_item:
                jump howlerslairseen
            'I leave this place.' if not howlerslairpileofbonesgathered or howlerslair_corpse_item:
                jump howlerslaircollectedsomething

label howlerslairsoundgameover01:
    $ pc_hp = limit_pc_hp(0)
    show minus5hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
    if pc_religion == "pagan":
        show areapicture gameover_alt at basicfade
    else:
        show areapicture gameover at basicfade
    $ can_potions = 0
    menu:
        'You try, but you can’t handle the awful sounds any longer. You run back to the entrance, ignoring the animal corpses, but suddenly lose control over your limbs.
        \n\nThen comes the silence, and your blood fills up your eyes.
        \n
        \n\n[pcname]’s soul has left its shell.
        '
        'Let me replay this encounter.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this encounter.')
            stop music fadeout 4.0
            $ renpy.load("combatsave")

label howlerslairseen:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not staying here any longer. I found her shell, that should be enough.')
    $ howlerslair_corpse_status = "seen"
    play nature "audio/ambient/shortcutmeadow01.ogg" fadeout 2.0 fadein 3.0 volume 1.0
    show areapicture northernroadtofoggylake at basicfade
    $ can_potions = 0
    menu:
        'You hold your head briefly, hoping it will stop spinning, then rush toward the gully. The monkeys’ howls are both painful and desperate, which seems proper as you run through the blood and shells of their pack members. Once you reach the meadow, you gasp for breath, and your guts stop twisting your soul.
        \n\n{color=#f6d6bd}Efren{/color} may not be thrilled about what you’ve learnt, but at least you can bring him the truth.
        '
        'I did as much as I could.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I did as much as I could.')
            $ travel_destination = "foggylake"
            jump finaldestinationafterevent
        'I can’t risk my life for such a minor task.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t risk my life for such a minor task.')
            $ travel_destination = "foggylake"
            jump finaldestinationafterevent

label howlerslaircollectedsomething:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave this place.')
    $ pc_food = limit_pc_food(pc_food-1)
    show minus1food at foodchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
    $ howlerslair_corpse_status = "burned"
    play nature "audio/ambient/shortcutmeadow01.ogg" fadeout 2.0 fadein 3.0 volume 1.0
    show areapicture northernroadtofoggylake at basicfade
    $ can_potions = 0
    if howlerslairpileofbonesgathered and howlerslair_corpse_item:
        $ custom1 = "You glance at the belt buckle. It’s nothing extraordinary, but may be worth a dragon or two. The large sack of human remains, however, is going to bother you with its rattling. You stay for a bit in the middle of the road, unpack your sacks, then tie together as many bones as you can and hide them again. Let’s hope they won’t form an undead once they get touched by a fog."
        $ quarters += 1
    elif howlerslairpileofbonesgathered:
        $ custom1 = "The large sack of human remains is going to bother you with its rattling. You stay for a bit in the middle of the road, unpack your sacks, then tie together as many bones as you can and hide them again. Let’s hope they won’t form an undead once they get touched by a fog."
        $ quarters += 1
    elif howlerslair_corpse_item:
        $ custom1 = "You glance at the belt buckle. It’s nothing extraordinary, but may be worth a dragon or two."
    menu:
        'You hold your head briefly, hoping it will stop spinning, then rush toward the gully. The monkeys’ howls are both painful and desperate, which seems proper while you run through the blood and shells of their pack members. Once you reach the meadow, you gasp for breath, and your guts stop twisting your soul.
        \n\n[custom1] {color=#f6d6bd}Efren{/color} will surely appreciate your efforts.
        '
        'He’d better, and generously so.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’d better, and generously so.')
            $ travel_destination = "foggylake"
            jump finaldestinationafterevent
        'I did it to keep the roads safer.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I did it to keep the roads safer.')
            $ travel_destination = "foggylake"
            jump finaldestinationafterevent
