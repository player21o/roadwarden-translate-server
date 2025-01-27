default encounter_scavenger_dragonling_hurt = 0
default encounter_scavenger_dragonling_missed = 0

default encounter_scavenger_griffon_hurt = 0
default encounter_scavenger_griffon_hurt_quarrel = 0
default encounter_scavenger_griffon_shield = 0
default encounter_scavenger_griffon_blindingpowder = 0

default encounter_pebbler_firsttime = 0
default encounter_pebbler_secondtime = 0
default encounter_pebbler_gone = 0
default encounter_pebbler_modifier = 0
default encounter_pebbler_day = 0
default encounter_pebbler_check = 0
default encounter_pebbler_fluff = 0
default encounter_pebbler_fluff_old = 0
default encounter_pebbler_trollurine = 0
default encounter_pebbler_pickedapples = 0

default encounter_fallentree_goblins = 0
default encounter_fallentree_goblins_returndeath = 0
default encounter_fallentree_goblins_dmg = 0
default encounter_fallentree_goblins_amount = 2
default encounter_fallentree_goblins_afraid = 0
default encounter_fallentree_goblins_shield = 0
default encounter_fallentree_goblins_bloodonspear = 0

default encounter_spottedwolves = 0
default encounter_spottedwolves_hp = 5
default encounter_spottedwolves_gone = 0
default encounter_spottedwolves_available = 0

default fishinghamlet_harpies_firsttime = 0
default fishinghamlet_harpies_defeated = 0
default fishinghamlet_harpies_hp = 3
default fishinghamlet_harpies_crossbowused = 0 # item_crossbow and item_crossbowquarrels >= 1
default fishinghamlet_harpies_dust = 0
default fishinghamlet_harpies_spell = 0
default fishinghamlet_harpies_dragonhorn = 0
default fishinghamlet_harpies_spear = 0
default fishinghamlet_harpies_stance = 0

############################################### saving the scavenber
label ruinedvillage01scavengerscamp01leavingspear:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Gather your bags. We’re going to {color=#f6d6bd}Pelt of the North{/color}.”')
    hide areapicture
    if ruinedvillage_part_topentrance == 1:
        if ruinedvillage_part_topentrance_gate_open:
            show ruinedvillage_part_topentrance 02 at basicfade
        else:
            show ruinedvillage_part_topentrance 01 at basicfade
    if ruinedvillage_part_topentranceinside == 1:
        if ruinedvillage_part_topentrance_gate_open:
            show ruinedvillage_part_topentranceinside 02 at basicfade
        else:
            show ruinedvillage_part_topentranceinside 01 at basicfade
    if ruinedvillage_part_clearing == 1:
        show ruinedvillage_part_clearing 01 at basicfade
    if ruinedvillage_part_river == 1:
        show ruinedvillage_part_river 01 at basicfade
    if ruinedvillage_part_leftentrance == 1:
        show ruinedvillage_part_leftentrance 01 at basicfade
    if ruinedvillage_part_leftwing == 1:
        show ruinedvillage_part_leftwing 01 at basicfade
    if ruinedvillage_part_rightwing == 1:
        show ruinedvillage_part_rightwing 01 at basicfade
    if ruinedvillage_part_square == 1:
        show ruinedvillage_part_square 01 at basicfade
    if ruinedvillage_part_bottomleftwing == 1:
        show ruinedvillage_part_bottomleftwing 01 at basicfade
    if ruinedvillage_part_bottomrightwing == 1:
        show ruinedvillage_part_bottomrightwing 01 at basicfade
    if ruinedvillage_part_leftfield == 1:
        show ruinedvillage_part_leftfield 01 at basicfade
    if ruinedvillage_part_rightpasture == 1:
        show ruinedvillage_part_rightpasture 01 at basicfade
    if ruinedvillage_part_bottomentrance == 1:
        show ruinedvillage_part_bottomentrance 01 at basicfade
    $ quarters += 1
    menu:
        '{color=#f6d6bd}The scavenger{/color} keeps asking you to watch out for beasts and wraps the sharper scraps of iron in his cape. Folding the tent and putting it on your horse takes a while, and neither of you can sit down on the large pile of sacks and bundles. There’s a long walk ahead of you, but for {color=#f6d6bd}[horsename]{/color} it won’t be much of a burden.
        \n\nOnce you clear the room, you walk away. At first you hear only the birds and horseshoes. Then, the man starts to whisper.
        \n\n“Faster, ay? The apes are looking at us.”
        \n\nYou don’t see any proof of that.
        '
        '“Nothing we can do about it.” I lead us to the southern gate.':
            $ pyrrhos_quest_escorting = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Nothing we can do about it.” I lead us to the southern gate.')
            jump ruinedvillage01scavengerscamp01leavingspear02
        '“Here, take this.” I lend him a spear for the journey.' if item_asterionspear or item_mountainroadspear:
            $ pyrrhos_quest_weapon = 1
            $ pyrrhos_quest_escorting = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here, take this.” I lend him a spear for the journey.')
            jump ruinedvillage01scavengerscamp01leavingspear02
        '“Here, take my second axe.” I lend him my old weapon for the journey.' if item_axe03 or item_axe02alt:
            $ pyrrhos_quest_weapon = 1
            $ pyrrhos_quest_escorting = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here, take my second axe.” I lend him my old weapon for the journey.')
            jump ruinedvillage01scavengerscamp01leavingspear02

    label ruinedvillage01scavengerscamp01leavingspear02:
        $ quarters += 3
        nvl clear
        scene empty #part A of...
        scene layoutfull #part B of hididng all images
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show areapicture peltnorthtoruinedvillage at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if pyrrhos_fed:
            $ custom1 = "Even though you shared your food with him, he’s not fully recovered from days of hunger"
        else:
            $ custom1 = "He’s weakened by days of hunger"
        menu:
            'You move forward, slowed down by having to secure the bundles on {color=#f6d6bd}[horsename]’s{/color} back and carry your own bags. After half an hour, the man asks for a break. [custom1], but the farther away you get from the ruins, the more cheerful and talkative he gets, mostly speaking about what he needs to buy and how much “he hated the damn place.”
            \n\nThen, the beasts show up.
            '
            'I prepare my axe.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my axe.')
                jump ruinedvillage01scavengerscamp01leavingspear03

    label ruinedvillage01scavengerscamp01leavingspear03:
        $ at = 0
        if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
            play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
        $ pyrrhos_quest_griffons = 1
        if encounter_scavenger_griffon_hurt_quarrel:
            $ custom2 = "Only one creature, with a distinct limp and signs of hunger, seemingly unmoved by your presence, as it approaches the water to quench its thirst."
        else:
            $ custom2 = ""
        if pyrrhos_quest_weapon:
            $ custom1 = "and the weapon you lent him"
        else:
            $ custom1 = "and dagger"
        menu:
            'A loud bunch of griffons blocks the road near a pond. For you, their colorful furs and feathers don’t look much different than the pack you faced in the valley, days ago. There’s still some distance between you and them, but it could be crossed in less than a minute.
            \n\nThere’re maybe twenty beasts in sight, and this time they pay you much more attention. They spread their wings and start to screech, some making a few leaps forward. Your mount is too overloaded for you to turn away and get out of their range. [custom2]
            \n\n“Better to hold our ground,” groans {color=#f6d6bd}the scavenger{/color}, preparing his crossbow [custom1].
            '
            '{image=d6} “True, let’s stay on the defensive. But keep an eye on the horse.”':
                label ruinedvillage01scavengerscamp01leavingspear03a:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “True, let’s stay on the defensive. But keep an eye on the horse.”')
                    if pc_class == "warrior":
                        $ at_unlock_force = 1
                    menu:
                        'He nods and blocks the path between the beasts and your mount, then raises his loaded weapon, moving his aim between the approaching creatures.
                        '
                        'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                            pass
                        'I better grab a fistful of blinding powder.' ( condition="item_blindingpowder" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better grab a fistful of blinding powder.')
                            $ encounter_scavenger_griffon_blindingpowder = 1
                            menu:
                                'You use your last free moments to open the sack. The powder pours through your fingers, but it will be enough to knock down at least one of the beasts.
                                '
                                '{image=d6} I stay close to {color=#f6d6bd}the scavenger{/color}, making sure nothing jumps on our backs.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I stay close to {color=#f6d6bd}the scavenger{/color}, making sure nothing jumps on our backs.')
                                    $ at_unlock_force = 0
                                    jump ruinedvillage01scavengerscamp01leavingspear03aa
                                '{image=d6} I keep a bit of distance between us, so we have enough space to fight.' ( condition="at != 'force'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I keep a bit of distance between us, so we have enough space to fight.')
                                    $ at_unlock_force = 0
                                    jump ruinedvillage01scavengerscamp01leavingspear03ab
                                'Having more space will only benefit the pack. (disabled)' ( condition="at == 'force'" ):
                                    pass
                                '{image=d6} I stay still until a creature gets in my range, trying to surprise it.' ( condition="at != 'force'" ) :
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I stay still until a creature gets in my range, trying to surprise it.')
                                    $ at_unlock_force = 0
                                    jump ruinedvillage01scavengerscamp01leavingspear03ac
                                'The beasts are so nimble they can easily attack you from the side. (disabled)' ( condition="at == 'force'" ):
                                    pass
                                'I’m too weak to use my experience here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                                    pass
                        'I prepare my shield.' ( condition="item_shield" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my shield.')
                            $ encounter_scavenger_griffon_shield = 1
                            menu:
                                'You use your last free moments to unpack it, then swing it to test your grasp. Considering the size of the creatures, they won’t able to break such a wall.
                                '
                                '{image=d6} I stay close to {color=#f6d6bd}the scavenger{/color}, making sure nothing jumps on our backs.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I stay close to {color=#f6d6bd}the scavenger{/color}, making sure nothing jumps on our backs.')
                                    $ at_unlock_force = 0
                                    jump ruinedvillage01scavengerscamp01leavingspear03aa
                                '{image=d6} I keep a bit of distance between us, so we have enough space to fight.' ( condition="at != 'force'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I keep a bit of distance between us, so we have enough space to fight.')
                                    $ at_unlock_force = 0
                                    jump ruinedvillage01scavengerscamp01leavingspear03ab
                                'Having more space will only benefit the pack. (disabled)' ( condition="at == 'force'" ):
                                    pass
                                '{image=d6} I stay still until a creature gets in my range, trying to surprise it.' ( condition="at != 'force'" ) :
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I stay still until a creature gets in my range, trying to surprise it.')
                                    $ at_unlock_force = 0
                                    jump ruinedvillage01scavengerscamp01leavingspear03ac
                                'The beasts are so nimble they can easily attack you from the side. (disabled)' ( condition="at == 'force'" ):
                                    pass
                                'I’m too weak to use my experience here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                                    pass
                        '{image=d6} Since I also have a crossbow, I follow his lead.' ( condition="item_crossbow and item_crossbowquarrels" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Since I also have a crossbow, I follow his lead.')
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
                            $ item_crossbowquarrels -= 1
                            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            if d100roll <= 50:
                                $ encounter_scavenger_griffon_hurt = 1
                                menu:
                                    'The arrow hits a creature in the torso, making it stumble and fall on the ground, twitching its limbs and squeaking in pain. A few other beasts stop in place, screeching at each other and looking around, but others are still on the move.
                                    \n\nYou put away the crossbow and prepare your blade.
                                    '
                                    '{image=d6} I stay close to {color=#f6d6bd}the scavenger{/color}, making sure nothing jumps on our backs.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I stay close to {color=#f6d6bd}the scavenger{/color}, making sure nothing jumps on our backs.')
                                        $ at_unlock_force = 0
                                        jump ruinedvillage01scavengerscamp01leavingspear03aa
                                    '{image=d6} I keep a bit of distance between us, so we have enough space to fight.' ( condition="at != 'force'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I keep a bit of distance between us, so we have enough space to fight.')
                                        $ at_unlock_force = 0
                                        jump ruinedvillage01scavengerscamp01leavingspear03ab
                                    'Having more space will only benefit the pack. (disabled)' ( condition="at == 'force'" ):
                                        pass
                                    '{image=d6} I stay still until a creature gets in my range, trying to surprise it.' ( condition="at != 'force'" ) :
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I stay still until a creature gets in my range, trying to surprise it.')
                                        $ at_unlock_force = 0
                                        jump ruinedvillage01scavengerscamp01leavingspear03ac
                                    'The beasts are so nimble they can easily attack you from the side. (disabled)' ( condition="at == 'force'" ):
                                        pass
                                    'I’m too weak to use my experience here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                                        pass
                            else:
                                menu:
                                    'Your bolt squeezes between a couple of beasts - they’re not even aware of the threat.
                                    \n\nYou put away the crossbow and prepare your blade.
                                    '
                                    '{image=d6} I stay close to {color=#f6d6bd}the scavenger{/color}, making sure nothing jumps on our backs.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I stay close to {color=#f6d6bd}the scavenger{/color}, making sure nothing jumps on our backs.')
                                        $ at_unlock_force = 0
                                        jump ruinedvillage01scavengerscamp01leavingspear03aa
                                    '{image=d6} I keep a bit of distance between us, so we have enough space to fight.' ( condition="at != 'force'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I keep a bit of distance between us, so we have enough space to fight.')
                                        $ at_unlock_force = 0
                                        jump ruinedvillage01scavengerscamp01leavingspear03ab
                                    'Having more space will only benefit the pack. (disabled)' ( condition="at == 'force'" ):
                                        pass
                                    '{image=d6} I stay still until a creature gets in my range, trying to surprise it.' ( condition="at != 'force'" ) :
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I stay still until a creature gets in my range, trying to surprise it.')
                                        $ at_unlock_force = 0
                                        jump ruinedvillage01scavengerscamp01leavingspear03ac
                                    'The beasts are so nimble they can easily attack you from the side. (disabled)' ( condition="at == 'force'" ):
                                        pass
                                    'I’m too weak to use my experience here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                                        pass
                        'Too bad I’m out of quarrels. (disabled)' ( condition="item_crossbow and not item_crossbowquarrels" ):
                            pass
                        'I don’t have a crossbow. (disabled)' if not item_crossbow:
                            pass
                        '{image=d6} I stay close to {color=#f6d6bd}the scavenger{/color}, making sure nothing jumps on our backs.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I stay close to {color=#f6d6bd}the scavenger{/color}, making sure nothing jumps on our backs.')
                            $ at_unlock_force = 0
                            jump ruinedvillage01scavengerscamp01leavingspear03aa
                        '{image=d6} I keep a bit of distance between us, so we have enough space to fight.' ( condition="at != 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I keep a bit of distance between us, so we have enough space to fight.')
                            $ at_unlock_force = 0
                            jump ruinedvillage01scavengerscamp01leavingspear03ab
                        'Having more space will only benefit the pack. (disabled)' ( condition="at == 'force'" ):
                            pass
                        '{image=d6} I stay still until a creature gets in my range, trying to surprise it.' ( condition="at != 'force'" ) :
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I stay still until a creature gets in my range, trying to surprise it.')
                            $ at_unlock_force = 0
                            jump ruinedvillage01scavengerscamp01leavingspear03ac
                        'The beasts are so nimble they can easily attack you from the side. (disabled)' ( condition="at == 'force'" ):
                            pass
                        'I’m too weak to use my experience here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                            pass
            '{image=d6} “Quite the opposite. We should charge at them, yelling and swinging our weapons. Let’s startle them.”':
                label ruinedvillage01scavengerscamp01leavingspear03b:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Quite the opposite. We should charge at them, yelling and swinging our weapons. Let’s startle them.”')
                    if pc_class == "warrior":
                        $ at_unlock_force = 1
                    menu:
                        'He hesitates, then purses his lips at you through his beard. “Fine. Ya the roadster here.”
                        '
                        '{image=d6} We do our best to startle one of them, hoping the others will also be affected.' ( condition="at != 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} We do our best to startle one of them, hoping the others will also be affected.')
                            $ at_unlock_force = 0
                            jump ruinedvillage01scavengerscamp01leavingspear03ba
                        'In the fervor of combat, we may not have enough time to stay with one of the creatures for long. (disabled)' ( condition="at == 'force'" ):
                            pass
                        '{image=d6} We run between the creatures, trying to wound some of them, but keeping our distance.' ( condition="at != 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} We run between the creatures, trying to wound some of them, but keeping our distance.')
                            $ at_unlock_force = 0
                            jump ruinedvillage01scavengerscamp01leavingspear03bb
                        'Spreading ourselves too thin will make our efforts worthless. (disabled)' ( condition="at == 'force'" ):
                            pass
                        '{image=d6} There’s no point in trying to kill them. Instead, we try to be as scary as we can, not bothering with the fight.' ( condition="at != 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} There’s no point in trying to kill them. Instead, we try to be as scary as we can, not bothering with the fight.')
                            $ at_unlock_force = 0
                            jump ruinedvillage01scavengerscamp01leavingspear03bc
                        'There’s no point in trying to kill them. Instead, we try to be as scary as we can, not bothering with the fight.' ( condition="at == 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- There’s no point in trying to kill them. Instead, we try to be as scary as we can, not bothering with the fight.')
                            $ at_unlock_force = 0
                            jump ruinedvillage01scavengerscamp01leavingspear03bc
                        'I’m too weak to use my experience here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                            pass
            '{image=d6} “Let’s focus on killing one of them as quickly as we can. Maybe the others will flee.”':
                label ruinedvillage01scavengerscamp01leavingspear03c:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Let’s focus on killing one of them as quickly as we can. Maybe the others will flee.”')
                    if pc_class == "warrior":
                        $ at_unlock_force = 1
                    menu:
                        'He nods and moves in front of your mount, then raises his loaded weapon, aiming at the closest creature. “Ready.”
                        '
                        '{image=d6} Since I also have a crossbow, I follow his lead.' ( condition="item_crossbow and item_crossbowquarrels" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Since I also have a crossbow, I follow his lead.')
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
                            $ item_crossbowquarrels -= 1
                            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            if d100roll <= 50:
                                $ encounter_scavenger_griffon_hurt = 1
                                menu:
                                    'The arrow hits a creature in the torso, making it stumble and fall on the ground, twitching its limbs and squeaking in pain. A few other beasts stop in place, screeching at each other and looking around, but others are still on the move.
                                    \n\nThen another griffon gets shot, this time by the other man, and its yells fill the area. Panic spreads among the creatures, some of which are already spreading out into the forest, while others surround their suffering companions.
                                    '
                                    '“Time to move,” I call for {color=#f6d6bd}[horsename]{/color}.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time to move,” I call for {color=#f6d6bd}%s{/color}.' %horsename)
                                        menu:
                                            '{color=#f6d6bd}The scavenger{/color} eagerly leads the way, reloading his crossbow as he takes a few cautious steps, then getting bolder whenever a nearby griffon gets out of his way. Their resentful eyes follow you, accepting their failure.
                                            '
                                            '“Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                                                $ travel_destination = "peltnorth"
                                                $ quarters += 2
                                                jump finaldestinationafterevent
                            else:
                                menu:
                                    'Your bolt squeezes between a couple of beasts - they’re not even aware of the threat.
                                    \n\nYou put away the crossbow and prepare your blade.
                                    '
                                    '{image=d6} I throw my axe at one of the beasts.' ( condition="at != 'force'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I throw my axe at one of the beasts.')
                                        $ at_unlock_force = 0
                                        jump ruinedvillage01scavengerscamp01leavingspear03ca
                                    'It’s not a good time to stay with just a dagger. (disabled)' ( condition="at == 'force'" ):
                                        pass
                                    '{image=d6} Once the man shoots, I dash toward the same target with a raised blade.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Once the man shoots, I dash toward the same target with a raised blade.')
                                        $ at_unlock_force = 0
                                        jump ruinedvillage01scavengerscamp01leavingspear03cb
                                    '{image=d6} I let the creatures get closer, then focus all my efforts on one of them.' ( condition="at != 'force'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I let the creatures get closer, then focus all my efforts on one of them.')
                                        $ at_unlock_force = 0
                                        jump ruinedvillage01scavengerscamp01leavingspear03cc
                                    'A fair fight may give them too much confidence. (disabled)' ( condition="at == 'force'" ):
                                        pass
                                    'I’m too weak to use my experience here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                                        pass
                        'Too bad I’m out of quarrels. (disabled)' ( condition="item_crossbow and not item_crossbowquarrels" ):
                            pass
                        'I don’t have a crossbow. (disabled)' if not item_crossbow:
                            pass
                        '{image=d6} I throw my axe at one of the beasts.' ( condition="at != 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I throw my axe at one of the beasts.')
                            $ at_unlock_force = 0
                            jump ruinedvillage01scavengerscamp01leavingspear03ca
                        'It’s not a good time to stay with just a dagger. (disabled)' ( condition="at == 'force'" ):
                            pass
                        '{image=d6} Once the man shoots, I dash toward the same target with a raised blade.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Once the man shoots, I dash toward the same target with a raised blade.')
                            $ at_unlock_force = 0
                            jump ruinedvillage01scavengerscamp01leavingspear03cb
                        '{image=d6} I let the creatures get closer, then focus all my efforts on one of them.' ( condition="at != 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I let the creatures get closer, then focus all my efforts on one of them.')
                            $ at_unlock_force = 0
                            jump ruinedvillage01scavengerscamp01leavingspear03cc
                        'A fair fight may give them too much confidence. (disabled)' ( condition="at == 'force'" ):
                            pass
                        'I’m too weak to use my experience here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                            pass
            'I turn toward the man. “What’s your plan?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your plan?”')
                menu:
                    'He shrugs. “Not much to plan here. Just kill as many as we can, and if we’re lucky, the rest will tuck their tails and scat. They won’t kill all three of us, ay? They’re just griffs.”
                    '
                    '{image=d6} “True, let’s stay on the defensive. But keep an eye on the horse.”':
                        jump ruinedvillage01scavengerscamp01leavingspear03a
                    '{image=d6} “Quite the opposite. We should charge at them, yelling and swinging our weapons. Let’s startle them.”':
                        jump ruinedvillage01scavengerscamp01leavingspear03b
                    '{image=d6} “Let’s focus on killing one of them as quickly as we can. Maybe the others will flee.”':
                        jump ruinedvillage01scavengerscamp01leavingspear03c

    label ruinedvillage01scavengerscamp01leavingspear03aa: # I stay close to {color=#f6d6bd}the scavenger{/color}, making sure nothing jumps on our backs.
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if pyrrhos_fed:
            $ d100roll -= 10
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
        if encounter_scavenger_griffon_shield:
            $ d100roll -= 20
        if encounter_scavenger_griffon_blindingpowder:
            $ d100roll -= 20
        if encounter_scavenger_griffon_hurt:
            $ d100roll -= 25
        if pyrrhos_quest_weapon:
            $ d100roll -= 15
        if d100roll <= 60:
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ custom3 = "Your fine gambeson keeps you in one piece, and is still in decent shape."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your gambeson keeps you in one piece."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            elif encounter_scavenger_griffon_blindingpowder:
                $ custom1 = ", even though you manage to stop their first strike through your alchemy"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "Judging by the angry shouts, {color=#f6d6bd}the scavenger{/color} is doing fairly well."
            else:
                $ custom2 = "Judging by the painful shouts, {color=#f6d6bd}the scavenger{/color} is struggling, but is still alive."
            menu:
                'The man’s arrow hits and stops one of the creatures, but it doesn’t buy you much time. He realizes your plan and also gets closer to you. The semicircle of beaks and talons is hardly organized - one of the creatures simply leaps at you, and the others follow.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The two creatures you butchered are on the ground, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! We’re a fine team, ye and I!” He laughs briefly. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
        else:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your fine gambeson keeps you in one piece."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson took some of the damage upon itself."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            elif encounter_scavenger_griffon_blindingpowder:
                $ custom1 = ", even though you manage to stop their first strike through your alchemy"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "Judging by the angry shouts, {color=#f6d6bd}the scavenger{/color} is doing fairly well."
            else:
                $ custom2 = "Judging by the painful shouts, {color=#f6d6bd}the scavenger{/color} is struggling, but is still alive."
            menu:
                'The man’s arrow hits and stops one of the creatures, but it doesn’t buy you much time. He realizes your plan and also gets closer to you. The semicircle of beaks and talons is hardly organized - one of the creatures simply leaps at you, and the others follow.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. You don’t always manage to stay focused as the pain pierces your shell after a few lucky hits. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The one creature you butchered is still convulsing from pain, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground, deeply hurt. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Ba’we’re alive, roadster! Ye and I, both!” He laughs briefly. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingspear03ab: #I keep a bit of distance between us, so we have enough space to fight.
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if pyrrhos_fed:
            $ d100roll -= 10
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
        if encounter_scavenger_griffon_shield:
            $ d100roll -= 20
        if encounter_scavenger_griffon_blindingpowder:
            $ d100roll -= 20
        if encounter_scavenger_griffon_hurt:
            $ d100roll -= 25
        if pyrrhos_quest_weapon:
            $ d100roll -= 15
        if d100roll <= 30:
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ custom3 = "Your fine gambeson keeps you in one piece, and is still in decent shape."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your gambeson keeps you in one piece."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            elif encounter_scavenger_griffon_blindingpowder:
                $ custom1 = ", even though you manage to stop their first strike through your alchemy"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'The man’s arrow hits and stops one of the creatures, but it doesn’t buy you much time. He observes your movements for a while. “The shit ya going,” he scolds you. “They’ll surround ye!” It’s too late to react. The semicircle of beaks and talons is hardly organized - one of the creatures simply leaps at you, and the others follow.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The two creatures you butchered are on the ground, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! I thought ya dumb, going away like that, ba’we’re a fine team, ye and I!” He laughs briefly. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
        else:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your fine gambeson keeps you in one piece."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson took some of the damage upon itself."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            elif encounter_scavenger_griffon_blindingpowder:
                $ custom1 = ", even though you manage to stop their first strike through your alchemy"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'The man’s arrow hits and stops one of the creatures, but it doesn’t buy you much time. He observes your movements for a while. “The shit ya going,” he scolds you. “They’ll surround ye!” It’s too late to react. The semicircle of beaks and talons is hardly organized - one of the creatures simply leaps at you, and the others follow.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The one creature you butchered is still convulsing from pain, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground, deeply hurt. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! I thought ya dumb, going away like that, ba’we’re alive! Ye and I, both!” He laughs briefly. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingspear03ac: # I stay still until a creature gets in my range, trying to surprise it.
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if pyrrhos_fed:
            $ d100roll -= 10
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
        if encounter_scavenger_griffon_shield:
            $ d100roll -= 20
        if encounter_scavenger_griffon_blindingpowder:
            $ d100roll -= 20
        if encounter_scavenger_griffon_hurt:
            $ d100roll -= 25
        if pyrrhos_quest_weapon:
            $ d100roll -= 15
        if d100roll <= 30:
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ custom3 = "Your fine gambeson keeps you in one piece, and is still in decent shape."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your gambeson keeps you in one piece."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            elif encounter_scavenger_griffon_blindingpowder:
                $ custom1 = ", even though you manage to stop their first strike through your alchemy"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'The man’s arrow hits and stops one of the creatures, but it doesn’t buy you much time. He looks at your still shell. “The shit ya doing,” he scolds you. “Wake up, they’ll surround ye!” It’s too late to react. The semicircle of beaks and talons is hardly organized - one of the creatures simply leaps at you, but you’re fast enough to react. You switch from playing a statue to taking a powerful swing, cutting the beast’s head off. Then, the others follow up the attack.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1].
                \n\nFinally, it all ends, though not because of a lack of opponents. The three creatures you butchered are on the ground, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! I thought ya were standing like a dimwit, ba’we’re a fine team, ye and I!” He laughs briefly. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
        else:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your fine gambeson keeps you in one piece."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson took some of the damage upon itself."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            elif encounter_scavenger_griffon_blindingpowder:
                $ custom1 = ", even though you manage to stop their first strike through your alchemy"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'The man’s arrow hits and stops one of the creatures, but it doesn’t buy you much time. He looks at your still shell. “The shit ya doing,” he scolds you. “Wake up, they’ll surround ye!” It’s too late to react. The semicircle of beaks and talons is hardly organized - one of the creatures simply leaps at you, and you’re not fast enough to react. You switch from playing a statue to taking a powerful swing, but the dodging beast gets hit only with the side of the axe. Then, the others follow up the attack.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1].
                \n\nFinally, it all ends, though not because of a lack of opponents. The one creature you butchered is still convulsing from pain, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground, deeply hurt. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! I thought ya were standing like a dimwit, ba’we’re alive! Ye and I, both!” He laughs briefly. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingspear03ba: # We do our best to startle one of them, hoping the others will also be affected.
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if pyrrhos_fed:
            $ d100roll -= 10
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
        if encounter_scavenger_griffon_shield:
            $ d100roll -= 20
        if encounter_scavenger_griffon_hurt:
            $ d100roll -= 25
        if pyrrhos_quest_weapon:
            $ d100roll -= 15
        if d100roll <= 40:
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ custom3 = "Your fine gambeson keeps you in one piece, and is still in decent shape."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your gambeson keeps you in one piece."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'You run at the nearest beast, besetting it with your loud screams, and while it runs away, others are so close they would have to fall over to stop. One of the griffons simply leaps at you, and the others follow.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The two creatures you butchered are on the ground, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! We’re a fine team, ye and I!” He laughs briefly. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
        else:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ custom3 = "Your fine gambeson keeps you in one piece, and is still in decent shape."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your gambeson keeps you in one piece."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'You run at the nearest beast, besetting it with your loud screams, and while it runs away, others are so close they would have to fall over to stop. One of the griffons simply leaps at you, and the others follow.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The one creature you butchered is still convulsing from pain, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground, deeply hurt. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! I thought ya dumb, with a plan like that, ba’we’re alive! Ye and I, both!” He laughs briefly, painfully. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingspear03bb: # We run between the creatures, trying to wound some of them, but keeping our distance.
        if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
            $ cleanliness_clothes_torn = 1
            $ cleanliness_clothes_blood = 1
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
        elif not cleanliness_clothes_blood:
            $ cleanliness_clothes_blood = 1
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        elif not cleanliness_clothes_torn:
            $ cleanliness_clothes_torn = 1
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        if armor >= 3:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ custom3 = "Your fine gambeson keeps you in one piece."
        elif armor >= 1:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ custom3 = "You’re bleeding. Your gambeson took some of the damage upon itself."
        else:
            $ pc_hp = limit_pc_hp(pc_hp-2)
            show minus2hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
        if encounter_scavenger_griffon_shield:
            $ custom1 = ", even though you manage to crack one of their skulls with the shield"
        else:
            $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
        if pyrrhos_quest_weapon:
            $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
        else:
            $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
        menu:
            'You run into the creatures like lunatics, waving your arms, swinging your weapons, and trying to find a balance between loud shouts and breathing, so you can strike some of the beasts, then jump away. Some of the creatures jump away, but others are so close they would have to fall over to stop. One of the griffons simply leaps at you, and the others follow.
            \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
            \n\nFinally, it all ends, though not because of a lack of opponents. The one creature you butchered is still convulsing from pain, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
            \n\n[custom3] The man spits on the ground, deeply hurt. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! I thought ya dumb, with a plan like that, ba’we’re alive! Ye and I, both!” He laughs briefly, painfully. “Let me draw my ballista and we can move forward.”
            '
            'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                $ travel_destination = "peltnorth"
                $ quarters += 2
                jump finaldestinationafterevent
            'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                $ travel_destination = "peltnorth"
                $ quarters += 2
                jump finaldestinationafterevent
            'I tell him to stay sharp. We still have a long road ahead of us.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                $ travel_destination = "peltnorth"
                $ quarters += 2
                jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingspear03bc: # There’s no point in trying to kill them. Instead, we try to be as scary as we can, not bothering with the fight.
        $ pyrrhos_quest_griffons_spared = 1
        menu:
            'You run among the creatures like lunatics, waving your arms, swinging your weapons, and shouting as much as your lungs allow it. Even {color=#f6d6bd}[horsename]{/color}, led by fear, joins the two of you, stomping with its horseshoes loudly. The confused beasts freeze, look around, then start to spread, as if a dragon might arrive from behind the hill. As they jump away over the bushes, their hungry beaks don’t turn back.
            \n\nOnce you’re sure the road is clear, {color=#f6d6bd}the scavenger{/color} laughs, though his words are weakened by a sore throat. “I must say, ya a brave one! And no blades to clean, ay?” Another laughter. “I swear, beasts are dumber than a pair of rocks.”
            '
            'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                $ travel_destination = "peltnorth"
                $ quarters += 2
                jump finaldestinationafterevent
            'I tell him to stay sharp. We still have a long road ahead of us.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                $ travel_destination = "peltnorth"
                $ quarters += 2
                jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingspear03ca: # I throw my axe at one of the beasts.
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if pyrrhos_fed:
            $ d100roll -= 10
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
        if encounter_scavenger_griffon_shield:
            $ d100roll -= 20
        if encounter_scavenger_griffon_hurt:
            $ d100roll -= 25
        if pyrrhos_quest_weapon:
            $ d100roll -= 15
        if d100roll <= 20:
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ custom3 = "Your fine gambeson keeps you in one piece, and is still in decent shape."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your gambeson keeps you in one piece."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'You dash forward and, with a loud scream, and throw your weapon at one of the creatures. It’s a clean hit - the edge lands in its head, sending it to the ground in convulsions. The man’s arrow hits and stops another creature, buying you enough time to get closer and grab the weapon again, then take a defensive stance, inviting the wave of beaks and talons.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The three creatures you butchered are still convulsing from pain, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! I thought ya dumb, going away like that, ba’we’re a fine team, ye and I!” He laughs briefly. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
        elif d100roll <= 80:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your fine gambeson keeps you in one piece."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson took some of the damage upon itself."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'The man’s arrow hits and stops one of the creatures. You have time to dash forward and, with a loud scream, throw your weapon at one of the creatures, but it’s a miss - the weapon hits it with its side, stunning it for a moment, but it’s only long enough for you to get closer and grab the weapon again. You hardly notice the set of talons and claws before they strike you.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The two creatures you butchered are still convulsing from pain, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground, deeply hurt. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! I thought ya dumb, going away like that, ba’we’re alive! Ye and I, both!” He laughs briefly, painfully. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
        else: # death
            $ pc_hp = limit_pc_hp(0)
            show minus5hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
            if pc_religion == "pagan":
                show areapicture gameover_alt at basicfade
            else:
                show areapicture gameover at basicfade
            menu:
                'You dash forward and, with a loud scream, throw your weapon at one of the creatures. The blade plunges into the mud. The griffons don’t bother considering what just happened, and simply charge at you. You try to block their talons and beaks with your arms, but you are unable to defend both your legs and your back.
                \n\nYou hit the ground. The man screams as he runs toward you, trying to push the creatures away.
                \n
                \n\n[pcname]’s soul has left its shell.
                '
                'Let me replay this encounter.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this encounter.')
                    stop music fadeout 4.0
                    $ renpy.load("combatsave")

    label ruinedvillage01scavengerscamp01leavingspear03cb: # Once the man shoots, I dash toward the same target with a raised blade.
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if pyrrhos_fed:
            $ d100roll -= 10
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
        if encounter_scavenger_griffon_shield:
            $ d100roll -= 20
        if encounter_scavenger_griffon_hurt:
            $ d100roll -= 25
        if pyrrhos_quest_weapon:
            $ d100roll -= 15
        if d100roll <= 60:
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ custom3 = "Your fine gambeson keeps you in one piece, and is still in decent shape."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your gambeson keeps you in one piece."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'You wait for just a few breaths, then dash forward with a scream, hoping the arrow will land. And so it does - all it takes is a strong swing with your axe to send the creature to the ground in convulsions. You have enough time to follow up this feat, so you run at another beast, making it run away in panic. But the other griffons, especially those behind you, are not so easily scared.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The three creatures you butchered are still convulsing from pain, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! I thought ya dumb, going away like that, ba’we’re a fine team, ye and I!” He laughs briefly. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
        else:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ custom3 = "Your fine gambeson keeps you in one piece, and is still in decent shape."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your gambeson keeps you in one piece."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'You wait for just a few breaths, then dash forward with a scream, hoping the arrow will land. And so it does - but as it pushes away the creature, your strong swing lands flat-sided on its flesh, only stunning it. You have enough time to follow up with another few cuts, sending it on the ground in convulsions, but you hardly have enough time to prepare for the wave of talons and beaks.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The three creatures you butchered are still convulsing from pain, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground, deeply hurt. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! I thought ya dumb, going away like that, ba’we’re alive! Ye and I, both!” He laughs briefly, painfully. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingspear03cc: # I let the creatures get closer, then focus all my efforts on one of them.
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if pyrrhos_fed:
            $ d100roll -= 10
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
        if encounter_scavenger_griffon_shield:
            $ d100roll -= 20
        if encounter_scavenger_griffon_hurt:
            $ d100roll -= 25
        if pyrrhos_quest_weapon:
            $ d100roll -= 15
        if d100roll <= 60:
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ custom3 = "Your fine gambeson keeps you in one piece, and is still in decent shape."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your gambeson keeps you in one piece."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'The man’s arrow hits and stops one of the creatures, but it doesn’t buy you much time. You point him toward the next victim, and the man understands right away. He switches his weapons, and tries to get to the monster’s side as it charges at you, or rather jumps at you with its talons and beak outstretched. Your powerful hit makes it fly to the side, landing just before {color=#f6d6bd}the scavenger’s{/color} boots. A pained shout pierces the air, and you have enough time to take a defensive stance.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The three creatures you butchered are still convulsing from pain, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! You made me sweat, ba’we’re a fine team, ye and I!” He laughs briefly. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
        else:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            if armor >= 3:
                $ custom3 = "Your fine gambeson keeps you in one piece, and is still in decent shape."
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ custom3 = "Your gambeson keeps you in one piece."
            else:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom3 = "You’re bleeding. Your gambeson was already in such bad shape that it made little difference."
            if encounter_scavenger_griffon_shield:
                $ custom1 = ", even though you manage to crack one of their skulls with the shield"
            else:
                $ custom1 = ", and it’s difficult to keep pushing them away with your free hand"
            if pyrrhos_quest_weapon:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing well, using your weapon to keep some distance, jumping away whenever he lands a hit."
            else:
                $ custom2 = "As you peek toward {color=#f6d6bd}the scavenger{/color}, you see he’s doing fairly well, jumping away whenever he lands a hit, but his short blade holds him back - you see blood coming from a few cuts through his clothes."
            menu:
                'The man’s arrow hits and stops one of the creatures, but it doesn’t buy you much time. You point him toward the next victim, but the man doesn’t see your command as he retreats and switches his weapons. The first monster charges at you, or rather jumps at you with its talons outstretched. Your powerful hit makes it fly to the side, but you then have to follow it with another few cuts, leaving it on the ground in convulsions. Its pained shout pierces the air, and you hardly have enough time to notice a wave of beaks before they hit you.
                \n\nFor the next minute, you slice and dice whatever you can hit, filling the air with screeches and feathers. The sheer number of opponents overwhelms you more than once[custom1]. [custom2]
                \n\nFinally, it all ends, though not because of a lack of opponents. The three creatures you butchered are still convulsing from pain, but the others, some of them hurt, have enough strength to run away. Their will is broken, yet the pack will go on, at least for some time.
                \n\n[custom3] The man spits on the ground, deeply hurt. “May apes and ibexes bang this place day after day,” he leans forward, taking a few deep breaths, then looks at you. “Roadster! I thought ya were standing like a dimwit, ba’we’re alive! Ye and I, both!” He laughs briefly, painfully. “Let me draw my ballista and we can move forward.”
                '
                'I just smile and try to ease {color=#f6d6bd}[horsename]’s{/color} thoughts. It’s better to keep moving.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just smile and try to ease {color=#f6d6bd}%s’s{/color} thoughts. It’s better to keep moving.' %horsename)
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent
                'I tell him to stay sharp. We still have a long road ahead of us.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell him to stay sharp. We still have a long road ahead of us.')
                    $ travel_destination = "peltnorth"
                    $ quarters += 2
                    jump finaldestinationafterevent

label ruinedvillage01scavengerscamp01leavingdell:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”')
    hide areapicture
    if ruinedvillage_part_topentrance == 1:
        if ruinedvillage_part_topentrance_gate_open:
            show ruinedvillage_part_topentrance 02 at basicfade
        else:
            show ruinedvillage_part_topentrance 01 at basicfade
    if ruinedvillage_part_topentranceinside == 1:
        if ruinedvillage_part_topentrance_gate_open:
            show ruinedvillage_part_topentranceinside 02 at basicfade
        else:
            show ruinedvillage_part_topentranceinside 01 at basicfade
    if ruinedvillage_part_clearing == 1:
        show ruinedvillage_part_clearing 01 at basicfade
    if ruinedvillage_part_river == 1:
        show ruinedvillage_part_river 01 at basicfade
    if ruinedvillage_part_leftentrance == 1:
        show ruinedvillage_part_leftentrance 01 at basicfade
    if ruinedvillage_part_leftwing == 1:
        show ruinedvillage_part_leftwing 01 at basicfade
    if ruinedvillage_part_rightwing == 1:
        show ruinedvillage_part_rightwing 01 at basicfade
    if ruinedvillage_part_square == 1:
        show ruinedvillage_part_square 01 at basicfade
    if ruinedvillage_part_bottomleftwing == 1:
        show ruinedvillage_part_bottomleftwing 01 at basicfade
    if ruinedvillage_part_bottomrightwing == 1:
        show ruinedvillage_part_bottomrightwing 01 at basicfade
    if ruinedvillage_part_leftfield == 1:
        show ruinedvillage_part_leftfield 01 at basicfade
    if ruinedvillage_part_rightpasture == 1:
        show ruinedvillage_part_rightpasture 01 at basicfade
    if ruinedvillage_part_bottomentrance == 1:
        show ruinedvillage_part_bottomentrance 01 at basicfade
    $ quarters += 1
    menu:
        '{color=#f6d6bd}The scavenger{/color} keeps asking you to watch out for beasts and wraps the sharper scraps of iron in his cape. Folding the tent and putting it on your horse takes a while, and neither of you can sit down on the large pile of sacks and bundles. There’s a long walk ahead of you, but for {color=#f6d6bd}[horsename]{/color} it won’t be much of a burden.
        \n\nOnce you clear the room, you walk away. At first you hear only the birds and horseshoes. Then, the man starts to whisper.
        \n\n“Faster, ay? The apes are looking at us.”
        \n\nYou don’t see any proof of that.
        '
        '“Nothing we can do about it.” I lead us to the northern road.':
            $ pyrrhos_quest_escorting = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Nothing we can do about it.” I lead us to the northern road.')
            jump ruinedvillage01scavengerscamp01leavingdell02
        '“Here, take this.” I lend him a spear for the journey.' if item_asterionspear or item_mountainroadspear:
            $ pyrrhos_quest_weapon = 1
            $ pyrrhos_quest_escorting = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here, take this.” I lend him a spear for the journey.')
            jump ruinedvillage01scavengerscamp01leavingdell02
        '“Here, take my second axe.” I lend him my old weapon for the journey.' if item_axe03 or item_axe02alt:
            $ pyrrhos_quest_weapon = 1
            $ pyrrhos_quest_escorting = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here, take my second axe.” I lend him my old weapon for the journey.')
            jump ruinedvillage01scavengerscamp01leavingdell02

    label ruinedvillage01scavengerscamp01leavingdell02:
        nvl clear
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        scene empty #part A of...
        scene layoutfull #part B of hididng all images
        show areapicture ruinedvillagetobeholder at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ quarters += 4
        if pyrrhos_fed:
            $ custom1 = "Even though you shared your food with him, he’s not fully recovered from days of hunger"
        else:
            $ custom1 = "He’s weakened by days of hunger"
        menu:
            'You move forward, slowed down by having to secure the bundles on {color=#f6d6bd}[horsename]’s{/color} back and carry your own bags. After half an hour, the man asks for a break. [custom1], but the farther away you get from the ruins, the more cheerful and talkative he gets, mostly speaking about the thing he needs to buy and how much “he hated the damn place.”
            \n\nThen, the beasts show up.
            '
            'I prepare my axe.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my axe.')
                jump ruinedvillage01scavengerscamp01leavingdell03

    label ruinedvillage01scavengerscamp01leavingdell03:
        if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
            play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
        $ at = 0
        if pc_class == "warrior":
            $ at_unlock_force = 1
        if pyrrhos_quest_weapon:
            $ custom1 = "The man reaches for the weapon you gave him. You can only hope he knows how to use it."
        else:
            $ custom1 = "The man reaches for a dagger, not much longer than the monster’s teeth."
        menu:
            'Two dragonlings, each about five feet long, approach you from opposite sides, getting ready to charge at you. They lash their tails and screech, but you know that panicking and running away is the worst thing you can do. They’re fast, used to chasing their prey near the roads, with a much larger advantage in an empty field than in the forests. Even on a horse you could barely outrun them, and your best option now is to hold your ground.
            \n\nThe scavenger knows it as well. He fires his crossbow, hitting one of the predators right in the skull. It clumsily falls down without another breath. The other dragonling jumps forward, surprisingly silent.
            \n\n[custom1]
            '
            '{image=d6} While there’s time, I also use a crossbow.' ( condition="item_crossbow and item_crossbowquarrels" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} While there’s time, I also use a crossbow.')
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
                $ item_crossbowquarrels -= 1
                $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                if d100roll <= 5: # killed
                    $ at_unlock_force = 0
                    menu:
                        'Maybe it’s just your luck, but the bolt hits the creature in the middle of its neck. It stumbles, still trying to get to you, then hits the ground, choking on its own blood.
                        \n\nThe man laughs. “Well, well, roadster! The two of us ought to shoot for crowds, not drift about, ay?” His laughter mixes with the gurgling of the beast. Then, the sound of a not-so-distant howling reaches you, and the man reloads his crossbow quickly.
                        \n\nYou can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
                        '
                        'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                            $ travel_destination = "howlersdell"
                            $ quarters += 4
                            $ item_dragonlingpaw += 1
                            $ renpy.notify("You picked a dragonling’s paw.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                            jump finaldestinationafterevent
                        'I don’t need more blood. I rush the man and leave this place.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                            $ travel_destination = "howlersdell"
                            $ quarters += 4
                            jump finaldestinationafterevent
                if d100roll <= 40: # wounded
                    $ encounter_scavenger_dragonling_hurt = 1
                    menu:
                        'You don’t have much time to aim, but the arrow still hits the beast’s chest. It stumbles in place, takes a few steps away, then turns around rapidly, continuing its slightly slower run.
                        \n\nYou have already replaced the crossbow with your blade.
                        '
                        '{image=d6} I do my best to defend myself.' ( condition="at != 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I do my best to defend myself.')
                            $ at_unlock_force = 0
                            $ d100roll = 0
                            $ d100roll = renpy.random.randint(1, 100)
                            if pyrrhos_fed:
                                $ d100roll -= 10
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
                            if encounter_scavenger_dragonling_missed:
                                $ d100roll += 10
                            if encounter_scavenger_dragonling_hurt:
                                $ d100roll -= 25
                            if pyrrhos_quest_weapon:
                                $ d100roll -= 15
                            if d100roll <= 60:
                                jump ruinedvillage01scavengerscamp01leavingdell04asuccess
                            else:
                                jump ruinedvillage01scavengerscamp01leavingdell04afail
                        '{image=d6} “Step aside, I’ve got this.” I move in front of the scavenger, even if it puts myself in danger.' ( condition="at != 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Step aside, I’ve got this.” I move in front of the scavenger, even if it puts myself in danger.')
                            $ at_unlock_force = 0
                            $ pyrrhos_quest_saved = 1
                            $ d100roll = 0
                            $ d100roll = renpy.random.randint(1, 100)
                            if pyrrhos_fed:
                                $ d100roll -= 10
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
                            if encounter_scavenger_dragonling_missed:
                                $ d100roll += 10
                            if encounter_scavenger_dragonling_hurt:
                                $ d100roll -= 25
                            if pyrrhos_quest_weapon:
                                $ d100roll -= 15
                            if d100roll <= 40:
                                jump ruinedvillage01scavengerscamp01leavingdell04bsuccess
                            else:
                                jump ruinedvillage01scavengerscamp01leavingdell04bfail
                        '{image=d6} I know a set of stances that will help me move from one strike to another. It’s still risky, but I should do well.' ( condition="at == 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I know a set of stances that will help me move from one strike to another. It’s still risky, but I should do well.')
                            $ at_unlock_force = 0
                            $ pyrrhos_quest_saved = 1
                            $ d100roll = 0
                            $ d100roll = renpy.random.randint(1, 100)
                            if pc_class == "warrior":
                                $ d100roll -= (pc_battlecounter)
                            else:
                                $ d100roll -= (pc_battlecounter/2)
                            if pyrrhos_fed:
                                $ d100roll -= 10
                            if not pc_food:
                                $ d100roll += 5
                            if pc_food == 3:
                                $ d100roll -= 5
                            if pc_food == 4:
                                $ d100roll -= 10
                            if armor == 4:
                                $ d100roll -= 5
                            if encounter_scavenger_dragonling_missed:
                                $ d100roll += 10
                            if encounter_scavenger_dragonling_hurt:
                                $ d100roll -= 25
                            if pyrrhos_quest_weapon:
                                $ d100roll -= 15
                            if d100roll <= 75:
                                jump ruinedvillage01scavengerscamp01leavingdell04csuccess
                            else:
                                jump ruinedvillage01scavengerscamp01leavingdell04cfail
                        'I’m too weak to use my experience here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                            pass
                else: # missed
                    $ encounter_scavenger_dragonling_missed = 1
                    menu:
                        'You don’t have much time to aim, and it shows. The arrow flies a good foot away from the creature.
                        \n\nWith a heavy heart, you put the crossbow away and reach for your blade. Having less time to focus on your stance makes you anxious.
                        '
                        '{image=d6} I do my best to defend myself.' ( condition="at != 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I do my best to defend myself.')
                            $ at_unlock_force = 0
                            $ d100roll = 0
                            $ d100roll = renpy.random.randint(1, 100)
                            if pyrrhos_fed:
                                $ d100roll -= 10
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
                            if encounter_scavenger_dragonling_missed:
                                $ d100roll += 10
                            if encounter_scavenger_dragonling_hurt:
                                $ d100roll -= 25
                            if pyrrhos_quest_weapon:
                                $ d100roll -= 15
                            if d100roll <= 60:
                                jump ruinedvillage01scavengerscamp01leavingdell04asuccess
                            else:
                                jump ruinedvillage01scavengerscamp01leavingdell04afail
                        '{image=d6} “Step aside, I’ve got this.” I move in front of the scavenger, even if it puts myself in danger.' ( condition="at != 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Step aside, I’ve got this.” I move in front of the scavenger, even if it puts myself in danger.')
                            $ at_unlock_force = 0
                            $ pyrrhos_quest_saved = 1
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
                            if encounter_scavenger_dragonling_missed:
                                $ d100roll += 10
                            if encounter_scavenger_dragonling_hurt:
                                $ d100roll -= 25
                            if pyrrhos_quest_weapon:
                                $ d100roll -= 15
                            if d100roll <= 40:
                                jump ruinedvillage01scavengerscamp01leavingdell04bsuccess
                            else:
                                jump ruinedvillage01scavengerscamp01leavingdell04bfail
                        '{image=d6} I know a set of stances that will help me move from one strike to another. It’s still risky, but I should do well.' ( condition="at == 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I know a set of stances that will help me move from one strike to another. It’s still risky, but I should do well.')
                            $ at_unlock_force = 0
                            $ pyrrhos_quest_saved = 1
                            $ d100roll = 0
                            $ d100roll = renpy.random.randint(1, 100)
                            if pc_class == "warrior":
                                $ d100roll -= (pc_battlecounter)
                            else:
                                $ d100roll -= (pc_battlecounter/2)
                            if not pc_food:
                                $ d100roll += 5
                            if pc_food == 3:
                                $ d100roll -= 5
                            if pc_food == 4:
                                $ d100roll -= 10
                            if armor == 4:
                                $ d100roll -= 5
                            if encounter_scavenger_dragonling_missed:
                                $ d100roll += 10
                            if encounter_scavenger_dragonling_hurt:
                                $ d100roll -= 25
                            if pyrrhos_quest_weapon:
                                $ d100roll -= 15
                            if d100roll <= 75:
                                jump ruinedvillage01scavengerscamp01leavingdell04csuccess
                            else:
                                jump ruinedvillage01scavengerscamp01leavingdell04cfail
                        'I’m too weak to use my experience here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                            pass
            'Too bad I’m out of quarrels. (disabled)' ( condition="item_crossbow and not item_crossbowquarrels" ):
                pass
            'I don’t have a crossbow. (disabled)' if not item_crossbow:
                pass
            'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                pass
            '{image=d6} I do my best to defend myself.' ( condition="at != 'force' and not item_blindingpowder" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I do my best to defend myself.')
                $ at_unlock_force = 0
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if pyrrhos_fed:
                    $ d100roll -= 10
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
                if encounter_scavenger_dragonling_missed:
                    $ d100roll += 10
                if encounter_scavenger_dragonling_hurt:
                    $ d100roll -= 25
                if pyrrhos_quest_weapon:
                    $ d100roll -= 15
                if d100roll <= 60:
                    jump ruinedvillage01scavengerscamp01leavingdell04asuccess
                else:
                    jump ruinedvillage01scavengerscamp01leavingdell04afail
            '{image=d6} “Step aside, I’ve got this.” I move in front of the scavenger, even if it puts myself in danger.' ( condition="at != 'force' and not item_blindingpowder" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Step aside, I’ve got this.” I move in front of the scavenger, even if it puts myself in danger.')
                $ at_unlock_force = 0
                $ pyrrhos_quest_saved = 1
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
                if encounter_scavenger_dragonling_missed:
                    $ d100roll += 10
                if encounter_scavenger_dragonling_hurt:
                    $ d100roll -= 25
                if pyrrhos_quest_weapon:
                    $ d100roll -= 15
                if d100roll <= 40:
                    jump ruinedvillage01scavengerscamp01leavingdell04bsuccess
                else:
                    jump ruinedvillage01scavengerscamp01leavingdell04bfail
            '{image=d6} The blinding powder will help me defend myself.' ( condition="at != 'force' and item_blindingpowder" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} The blinding powder will help me defend myself.')
                $ at_unlock_force = 0
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if pyrrhos_fed:
                    $ d100roll -= 10
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
                if encounter_scavenger_dragonling_missed:
                    $ d100roll += 10
                if encounter_scavenger_dragonling_hurt:
                    $ d100roll -= 25
                if pyrrhos_quest_weapon:
                    $ d100roll -= 15
                if item_blindingpowder:
                    $ d100roll -= 5
                if d100roll <= 60:
                    jump ruinedvillage01scavengerscamp01leavingdell04ablindingpowdersuccess
                else:
                    jump ruinedvillage01scavengerscamp01leavingdell04ablindingpowderfail
            '{image=d6} “Step aside, I’ve got this.” With a fistful of blinding powder, I move in front of the scavenger, even if it puts myself in danger.' ( condition="at != 'force' and item_blindingpowder" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Step aside, I’ve got this.” With a fistful of blinding powder, I move in front of the scavenger, even if it puts myself in danger.')
                $ at_unlock_force = 0
                $ pyrrhos_quest_saved = 1
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
                if encounter_scavenger_dragonling_missed:
                    $ d100roll += 10
                if encounter_scavenger_dragonling_hurt:
                    $ d100roll -= 25
                if pyrrhos_quest_weapon:
                    $ d100roll -= 15
                if item_blindingpowder:
                    $ d100roll -= 20
                if d100roll <= 40:
                    jump ruinedvillage01scavengerscamp01leavingdell04bblindingpowdersuccess
                else:
                    jump ruinedvillage01scavengerscamp01leavingdell04bblindingpowderfail
            '{image=d6} I know a set of stances that will help me move from one strike to another. It’s still risky, but I should do well.' ( condition="at == 'force'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I know a set of stances that will help me move from one strike to another. It’s still risky, but I should do well.')
                $ at_unlock_force = 0
                $ pyrrhos_quest_saved = 1
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter)
                else:
                    $ d100roll -= (pc_battlecounter/2)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if armor == 4:
                    $ d100roll -= 5
                if encounter_scavenger_dragonling_missed:
                    $ d100roll += 10
                if encounter_scavenger_dragonling_hurt:
                    $ d100roll -= 25
                if pyrrhos_quest_weapon:
                    $ d100roll -= 15
                if d100roll <= 75:
                    jump ruinedvillage01scavengerscamp01leavingdell04csuccess
                else:
                    jump ruinedvillage01scavengerscamp01leavingdell04cfail
            'I’m too weak to use my experience here. (Required vitality: 1) (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                pass

    label ruinedvillage01scavengerscamp01leavingdell04asuccess:
        $ pyrrhos_quest_saved = 1
        menu:
            'You prepare yourself to dodge, but the beast surprises you by suddenly changing its target. It jumps aside when it’s only a dozen feet away from you, then attacks the soul who appears to be less prepared. Still, you’re even faster. Before it sinks its teeth into your companion, you take a wide swing at the dragonling’s neck, from top to bottom. It’s all it takes - the head flies away and wetly thuds into the ground.
            \n\nThe man laughs from shock. “Thank ye,” he pants heavily. “I’m... It was way too fast. Without ye, I’d be dead by now! I better load the ballista again, ay?”
            \n\nYou take a moment to judge the situation. Neither of you is hurt, but a not-so-distant howling already reaches your ears. You can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
            '
            'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                $ travel_destination = "howlersdell"
                $ item_dragonlingpaw += 1
                $ renpy.notify("You picked a dragonling’s paw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                $ quarters += 4
                jump finaldestinationafterevent
            'I don’t need more blood. I rush the man and leave this place.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingdell04afail:
        menu:
            'You prepare yourself to dodge, but the beast surprises you by suddenly changing its target. It jumps aside when it’s only a dozen feet away from you, then attacks the soul who appears to be less prepared. You hear the man’s scream, and you move forward, having a single breath to take a wide swing at the dragonling’s neck, from top to bottom. It’s all it takes - the head flies away and wetly thuds into the ground.
            \n\nYou take a look at the scavenger, who lies on the ground, cursing and holding his back. The monster has bitten off a chunk of his flesh, and his blood covers the path. You help him calm down and give him water to clean his wound. He asks you to prepare for the rest of the journey. “Apeshit, I need to get to {color=#f6d6bd}Howler’s{/color}, ask the elders to help me.” He sighs. “Ba’good job, roadster. We can move after I load my ballista.”
            \n\nYou nod. You can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more and you also have to handle the man’s equipment. You need to get to the druids as quickly as you can. A not-so-distant howling already reaches your ears.
            '
            'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                $ item_dragonlingpaw += 1
                $ renpy.notify("You picked a dragonling’s paw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                jump finaldestinationafterevent
            'I don’t need more blood. I rush the man and leave this place.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                jump finaldestinationafterevent
            'With a heavy heart, I offer him a fresh healing potion.' ( condition="item_generichealingpotion" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- With a heavy heart, I offer him a fresh healing potion.')
                $ pyrrhos_quest_saved = 1
                jump ruinedvillage01scavengerscamp01leavingdell04a02generic
            'With a heavy heart, I offer him the healing potion that I found in the dolmen.' ( condition="item_potiondolmen and item_potiondolmen_known" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- With a heavy heart, I offer him the healing potion that I found in the dolmen.')
                $ pyrrhos_quest_saved = 1
                jump ruinedvillage01scavengerscamp01leavingdell04a02

    label ruinedvillage01scavengerscamp01leavingdell04ablindingpowdersuccess:
        $ pyrrhos_quest_saved = 1
        menu:
            'You prepare yourself to throw the dust, but the beast surprises you by suddenly changing its target. It jumps aside when it’s only a dozen feet away from you, then attacks the soul who appears to be less prepared. Still, you’re even faster. Before it sinks its teeth into your companion, you take a wide swing at the dragonling’s neck, from top to bottom. It’s all it takes - the head flies away and wetly thuds into the ground.
            \n\nThe man laughs from shock. “Thank ye,” he pants heavily. “I’m... It was way too fast. Without ye, I’d be dead by now! I better load the ballista again, ay?”
            \n\nYou take a moment to judge the situation. Neither of you is hurt, but a not-so-distant howling already reaches your ears. You can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
            '
            'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                $ travel_destination = "howlersdell"
                $ item_dragonlingpaw += 1
                $ renpy.notify("You picked a dragonling’s paw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                $ quarters += 4
                jump finaldestinationafterevent
            'I don’t need more blood. I rush the man and leave this place.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingdell04ablindingpowderfail:
        menu:
            'You prepare yourself to throw the dust, but the beast surprises you by suddenly changing its target. It jumps aside when it’s only a dozen feet away from you, then attacks the soul who appears to be less prepared. You hear the man’s scream, and you move forward, having a single breath to take a wide swing at the dragonling’s neck, from top to bottom. It’s all it takes - the head flies away and wetly thuds into the ground.
            \n\nYou take a look at the scavenger, who lies on the ground, cursing and holding his back. The monster has bitten off a chunk of his flesh, and his blood covers the path. You help him calm down and give him water to clean his wound. He asks you to prepare for the rest of the journey. “Apeshit, I need to get to {color=#f6d6bd}Howler’s{/color}, ask the elders to help me.” He sighs. “Ba’good job, roadster. We can move after I load my ballista.”
            \n\nYou nod. You can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more and you also have to handle the man’s equipment. You need to get to the druids as quickly as you can. A not-so-distant howling already reaches your ears.
            '
            'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                $ item_dragonlingpaw += 1
                $ renpy.notify("You picked a dragonling’s paw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                jump finaldestinationafterevent
            'I don’t need more blood. I rush the man and leave this place.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                jump finaldestinationafterevent
            'With a heavy heart, I offer him a fresh healing potion.' ( condition="item_generichealingpotion" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- With a heavy heart, I offer him a fresh healing potion.')
                $ pyrrhos_quest_saved = 1
                jump ruinedvillage01scavengerscamp01leavingdell04a02generic
            'With a heavy heart, I offer him the healing potion that I found in the dolmen.' ( condition="item_potiondolmen and item_potiondolmen_known" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- With a heavy heart, I offer him the healing potion that I found in the dolmen.')
                $ pyrrhos_quest_saved = 1
                jump ruinedvillage01scavengerscamp01leavingdell04a02

    label ruinedvillage01scavengerscamp01leavingdell04a02generic:
        $ item_generichealingpotion -= 1
        $ renpy.notify("You lost a potion.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a potion.{/i}')
        $ pyrrhos_quest_potion = 1
        if pc_goal == "iwanttohelp":
            $ pc_goal_iwanttohelppoints += 1
        menu:
            'The man looks at you without a word, but suddenly frowns and takes a deep breath, trying to ignore the new wave of pain. He reaches for the bottle. “Ye sure?” You open it. “Smells nice,” he chuckles and drinks the entire contents without stopping.
            \n\nThere’s no more suffering on his face. He starts to chuckle and smile, alternating between the two. He licks his lips and lifts his shirt. The wound has disappeared. “That was...” He giggles, trying to calm down. “Forgive me, I can’t control it. Ba’that was strong, thank ye, thank ye so much.”
            '
            'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                $ item_dragonlingpaw += 1
                $ renpy.notify("You picked a dragonling’s paw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                jump finaldestinationafterevent
            'I don’t need more blood. I rush the man and leave this place.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingdell04a02:
        $ item_potiondolmen = 0
        $ quest_healingpotion_description04 = "I have lost the potion."
        $ renpy.notify("You lost the potion.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion.{/i}')
        $ pyrrhos_quest_potion = 1
        if pc_goal == "iwanttohelp":
            $ pc_goal_iwanttohelppoints += 1
        menu:
            'The man looks at you without a word, but suddenly frowns and takes a deep breath, trying to ignore the new wave of pain. He reaches for the bottle. “Ye sure?” You open it. “Smells nice,” he chuckles and drinks the entire contents without stopping.
             \n\nThere’s no more suffering on his face. He starts to chuckle and smile, alternating between the two. He licks his lips and lifts his shirt. The wound has disappeared. “That was...” He giggles, trying to calm down. “Forgive me, I can’t control it. Ba’that was strong, thank ye, thank ye so much.”
            '
            'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                $ item_dragonlingpaw += 1
                $ renpy.notify("You picked a dragonling’s paw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                jump finaldestinationafterevent
            'I don’t need more blood. I rush the man and leave this place.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingdell04bsuccess:
        menu:
            'You step in front of the scavenger and the beast speeds up. You dash away just in time, dodging not only the creature’s jaws, but also its entire shell - turns out it tried to jump on you. You step left and forward, having a single breath to take a wide swing across its neck. The head flies away and wetly thuds into the ground.
            \n\nThe man laughs from shock. “Thank ye,” he pants heavily. “I’m... It was way too fast. If I were in ya place, I’d be dead by now! I better load the ballista again, ay?”
            \n\nYou take a moment to judge the situation. Neither of you is hurt, but a not-so-distant howling already reaches your ears. You can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
            '
            'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                $ travel_destination = "howlersdell"
                $ item_dragonlingpaw += 1
                $ renpy.notify("You picked a dragonling’s paw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                $ quarters += 4
                jump finaldestinationafterevent
            'I don’t need more blood. I rush the man and leave this place.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingdell04bblindingpowdersuccess:
        menu:
            'You step in front of the scavenger, then move forward and throw the dust in front of you, simultaneously turning your head away and jumping away. The beast stumbles once its eyes touch the burning substance. It still runs forward, gasping, but you have enough time to take a wide swing across its neck. The head flies away and wetly thuds into the ground.
            \n\nThe man laughs from shock. “Thank ye,” he pants heavily. “I’m... It was way too fast. If I were in ya place, I’d be dead by now! I better load the ballista again, ay?”
            \n\nYou take a moment to judge the situation. Neither of you is hurt, but a not-so-distant howling already reaches your ears. You can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
            '
            'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                $ travel_destination = "howlersdell"
                $ item_dragonlingpaw += 1
                $ renpy.notify("You picked a dragonling’s paw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                $ quarters += 4
                jump finaldestinationafterevent
            'I don’t need more blood. I rush the man and leave this place.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingdell04bblindingpowderfail:
        if armor >= 3:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            if not cleanliness_clothes_blood :
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            menu:
                'You step in front of the scavenger and the beast speeds up. You throw the dust in front of you, simultaneously turning your head away and jumping back, but you’re not fast enough. Instead of merely attacking you with its toothed jaws, the dragonling jumps at you and knocks you over, even though it’s now blinded. The gambeson is a huge help, but you know the claws will soon tear through it.
                \n\nYou hear the animal’s pained yelping. The man stabs and cuts it with quick thrusts from all directions, once, twice, a dozen times. You have enough strength to use this opportunity to strike the dragonling’s leg with your axe, then push it away. You get on your knees and hit it again with a single, powerful blow. It stops moving.
                \n\nHe helps you to stand up. “Thank ye, roadster. I’d be dead if I were ye!” He laughs, though you feel too much pain to join him. You look around. You’re not dangerously hurt, but all the scratches, abrasions, and cuts need to be cleaned with water. The man is now reloading his crossbow. A not-so-distant howling already reaches your ears.
                \n\nYou can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
                '
                'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    $ item_dragonlingpaw += 1
                    $ renpy.notify("You picked a dragonling’s paw.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                    jump finaldestinationafterevent
                'I don’t need more blood. I rush the man and leave this place.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    jump finaldestinationafterevent
        elif armor >= 1:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ pc_hp = limit_pc_hp(pc_hp-2)
            show minus2hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            menu:
                'You step in front of the scavenger and the beast speeds up. You throw the dust in front of you, simultaneously turning your head away and jumping back, but you’re not fast enough. Instead of merely attacking you with its toothed jaws, the dragonling jumps at you and knocks you over, even though it’s now blinded. The gambeson is a huge help, but you know the claws will soon tear through it.
                \n\nYou hear the animal’s painful yelling. The man stabs and cuts it with quick thrusts from all directions, once, twice, a dozen times. You have enough strength to use this opportunity to strike the dragonling’s leg with your axe, then push it away. You get on your knees and hit it again with a single, powerful blow. It stops moving.
                \n\nThe man helps you to stand up. “Thank ye, roadster. I’d be dead if I were ye!” He laughs, though you feel too much pain to join him. You look around. You’re not dangerously hurt, but all the scratches, abrasions, and cuts need some water to get cleaned. It could be worse. The man is now reloading his crossbow. A not-so-distant howling already reaches your ears.
                \n\nYou can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
                '
                'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    $ item_dragonlingpaw += 1
                    $ renpy.notify("You picked a dragonling’s paw.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                    jump finaldestinationafterevent
                'I don’t need more blood. I rush the man and leave this place.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    jump finaldestinationafterevent
        elif pc_hp >= 3:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ pc_hp = limit_pc_hp(pc_hp-3)
            show minus3hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
            menu:
                'You step in front of the scavenger and the beast speeds up. You throw the dust in front of you, simultaneously turning your head away and jumping back, but you’re not fast enough. Instead of merely attacking you with its toothed jaws, the dragonling jumps at you and knocks you over, even though it’s now blinded. The gambeson, already worn out, is not able to stop the beast’s powerful claws. You start to bleed, a lot. However, you soon hear the animal’s pained yelping. The man stabs and cuts it with quick thrusts from all directions, once, twice, a dozen times. You have enough strength to use this opportunity to strike the dragonling’s leg with your axe, then push it away. You get on your knees and hit it again with a single, powerful blow. It stops moving.
                \n\nThe man helps you to stand up. “Thank ye, roadster. I’d be dead if I were ye!” He laughs, though you feel too much pain to join him. You look around. You’re not dangerously hurt, but all the scratches, abrasions, and cuts need to be cleaned with water. You feel pain, but it could be worse. Much, much worse. The man is now reloading his crossbow. A not-so-distant howling already reaches your ears.
                \n\nYou can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
                '
                'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    $ item_dragonlingpaw += 1
                    $ renpy.notify("You picked a dragonling’s paw.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                    jump finaldestinationafterevent
                'I don’t need more blood. I rush the man and leave this place.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    jump finaldestinationafterevent
        else:
            $ pc_hp = limit_pc_hp(0)
            show minus5hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
            if pc_religion == "pagan":
                show areapicture gameover_alt at basicfade
            else:
                show areapicture gameover at basicfade
            menu:
                'You step in front of the scavenger and the beast speeds up. You throw the dust in front of you, simultaneously turning your head away and jumping back, but you’re not fast enough. Instead of merely attacking you with its toothed jaws, the dragonling jumps at you and knocks you over, even though it’s now blinded. The gambeson, already worn out, is not able to stop the beast’s powerful claws.
                \n\nAs you’re reached by the distant shout of the man, who runs toward you with a raised blade, the last thing you see is the blood bursting through your chest.
                \n
                \n\n[pcname]’s soul has left its shell.
                '
                'Let me replay this encounter.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this encounter.')
                    stop music fadeout 4.0
                    $ renpy.load("combatsave")

    label ruinedvillage01scavengerscamp01leavingdell04bfail:
        if armor >= 3:
            if not cleanliness_clothes_blood :
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            menu:
                'You step in front of the scavenger and the beast speeds up. You prepare yourself to dodge, but you’re not fast enough. Instead of merely attacking you with its toothed jaws, it jumps at you and knocks you over. The gambeson is a huge help, but you know the claws will soon tear through it. Before that happens, you hear the animal’s pained yelping. The man stabs and cuts it with quick thrusts from all directions, once, twice, a dozen times. You have enough strength to use this opportunity to strike the dragonling’s leg with your axe, then push it away. You get on your knees and hit it again with a single, powerful blow. It stops moving.
                \n\nHe helps you to stand up. “Thank ye, roadster. I’d be dead if I were ye!” He laughs, though you feel too much pain to join him. You look around. You’re not dangerously hurt, but all the scratches, abrasions, and cuts need to be cleaned with water. You feel pain, but it could be worse. Much, much worse. The man is now reloading his crossbow. A not-so-distant howling already reaches your ears.
                \n\nYou can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
                '
                'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    $ item_dragonlingpaw += 1
                    $ renpy.notify("You picked a dragonling’s paw.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                    jump finaldestinationafterevent
                'I don’t need more blood. I rush the man and leave this place.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    jump finaldestinationafterevent
        elif armor >= 1:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ pc_hp = limit_pc_hp(pc_hp-2)
            show minus2hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            menu:
                'You step in front of the scavenger and the beast speeds up. You prepare yourself to dodge, but you’re not fast enough. Instead of merely attacking you with its toothed jaws, it jumps at you and knocks you over. The gambeson is a huge help, but you know the claws will soon tear through it. However, you hear the animal’s painful yelling. The man stabs and cuts it with quick thrusts from all directions, once, twice, a dozen times. You have enough strength to use this opportunity to strike the dragonling’s leg with your axe, then push it away. You get on your knees and hit it again with a single, powerful blow. It stops moving.
                \n\nThe man helps you to stand up. “Thank ye, roadster. I’d be dead if I were ye!” He laughs, though you feel too much pain to join him. You look around. You’re not dangerously hurt, but all the scratches, abrasions, and cuts need some water to get cleaned. You feel pain, but it could be worse. Much, much worse. The man is now reloading his crossbow. A not-so-distant howling already reaches your ears.
                \n\nYou can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
                '
                'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    $ item_dragonlingpaw += 1
                    $ renpy.notify("You picked a dragonling’s paw.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                    jump finaldestinationafterevent
                'I don’t need more blood. I rush the man and leave this place.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    jump finaldestinationafterevent
        elif pc_hp >= 3:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ pc_hp = limit_pc_hp(pc_hp-3)
            show minus3hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
            menu:
                'You step in front of the scavenger and the beast speeds up. You prepare yourself to dodge, but you’re not fast enough. Instead of merely attacking you with its toothed jaws, it jumps at you and knocks you over. The gambeson, already worn out, is not able to stop the beast’s powerful claws. You start to bleed, a lot.
                \n\nYou hear the animal’s pained yelping. The man stabs and cuts it with quick thrusts from all directions, once, twice, a dozen times. You have enough strength to use this opportunity to strike the dragonling’s leg with your axe, then push it away. You get on your knees and hit it again with a single, powerful blow. It stops moving.
                \n\nThe man helps you to stand up. “Thank ye, roadster. I’d be dead if I were ye!” He laughs, though you feel too much pain to join him. You look around. You’re not dangerously hurt, but all the scratches, abrasions, and cuts need to be cleaned with water. You were lucky. The man is now reloading his crossbow. A not-so-distant howling already reaches your ears.
                \n\nYou can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
                '
                'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    $ item_dragonlingpaw += 1
                    $ renpy.notify("You picked a dragonling’s paw.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                    jump finaldestinationafterevent
                'I don’t need more blood. I rush the man and leave this place.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    jump finaldestinationafterevent
        else:
            $ pc_hp = limit_pc_hp(0)
            show minus5hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
            if pc_religion == "pagan":
                show areapicture gameover_alt at basicfade
            else:
                show areapicture gameover at basicfade
            menu:
                'You step in front of the scavenger and the beast speeds up. You prepare yourself to dodge, but you’re not fast enough. Instead of merely attacking you with its toothed jaws, it jumps at you and knocks you over. The gambeson, already worn out, is not able to stop the beast’s powerful claws.
                \n\nAs you’re reached by the distant shout of the man, who runs toward you with a raised blade, the last thing you see is the blood bursting through your chest.
                \n
                \n\n[pcname]’s soul has left its shell.
                '
                'Let me replay this encounter.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this encounter.')
                    stop music fadeout 4.0
                    $ renpy.load("combatsave")

    label ruinedvillage01scavengerscamp01leavingdell04csuccess:
        menu:
            'You have time to focus and take a few peaceful breaths. You step back, get closer to the scavenger, and take the proper stance. The monster has no shield, no armor, and your axe can surely cut through such thin scales. You just need to hit it once.
            \n\nYou step left and forward, having a single breath to take a wide swing across the monster’s neck. It’s all it takes - you made a bet and it turned out to be the right one. The head flies away and wetly thuds into the ground.
            \n\nThe man laughs from shock. “Thank ye,” he pants heavily. “I’m... It was way too fast. If I were in ya place, I’d be dead by now! I better load the ballista again, ay?”
            \n\nYou take a moment to judge the situation. Neither of you is hurt, but a not-so-distant howling already reaches your ears. You can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
            '
            'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                $ travel_destination = "howlersdell"
                $ item_dragonlingpaw += 1
                $ renpy.notify("You picked a dragonling’s paw.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                $ quarters += 4
                jump finaldestinationafterevent
            'I don’t need more blood. I rush the man and leave this place.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                $ travel_destination = "howlersdell"
                $ quarters += 4
                jump finaldestinationafterevent

    label ruinedvillage01scavengerscamp01leavingdell04cfail:
        if armor >= 3:
            if not cleanliness_clothes_blood :
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            menu:
                'You have time to focus and take a few peaceful breaths. You step back, get closer to the scavenger, and take the proper stance. The monster has no shield, no armor, and your axe can surely cut through such thin scales. You just need to hit it once.
                \n\nThe beast is smarter than you thought. Instead of merely attacking you with its toothed jaws, it jumps at you and knocks you over. The gambeson is a huge help, but you know the claws will soon tear through it.
                \n\nYou hear the animal’s pained yelping. The man stabs and cuts it with quick thrusts from all directions, once, twice, a dozen times. You have enough strength to use this opportunity to strike the dragonling’s leg with your axe, then push it away. You get on your knees and hit it again with a single, powerful blow. It stops moving.
                \n\nHe helps you to stand up. “Thank ye, roadster. I’d be dead if I were ye!” He laughs, though you feel too much pain to join him. You look around. You’re not dangerously hurt, but all the scratches, abrasions, and cuts need to be cleaned with water. The man is now reloading his crossbow. A not-so-distant howling already reaches your ears.
                \n\nYou can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
                '
                'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    $ item_dragonlingpaw += 1
                    $ renpy.notify("You picked a dragonling’s paw.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                    jump finaldestinationafterevent
                'I don’t need more blood. I rush the man and leave this place.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    jump finaldestinationafterevent
        elif armor >= 1:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ pc_hp = limit_pc_hp(pc_hp-2)
            show minus2hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            menu:
                'You have time to focus and take a few peaceful breaths. You step back, get closer to the scavenger, and take the proper stance. The monster has no shield, no armor, and your axe can surely cut through such thin scales. You just need to hit it once.
                \n\nThe beast is smarter than you thought. Instead of merely attacking you with its toothed jaws, it jumps at you and knocks you over. The gambeson is a huge help, but you know the claws will soon tear through it.
                \n\nYou hear the animal’s painful yelling. The man stabs and cuts it with quick thrusts from all directions, once, twice, a dozen times. You have enough strength to use this opportunity to strike the dragonling’s leg with your axe, then push it away. You get on your knees and hit it again with a single, powerful blow. It stops moving.
                \n\nThe man helps you to stand up. “Thank ye, roadster. I’d be dead if I were ye!” He laughs, though you feel too much pain to join him. You look around. You’re not dangerously hurt, but all the scratches, abrasions, and cuts need some water to get cleaned. The man is now reloading his crossbow. A not-so-distant howling already reaches your ears.
                \n\nYou can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
                '
                'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    $ item_dragonlingpaw += 1
                    $ renpy.notify("You picked a dragonling’s paw.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                    jump finaldestinationafterevent
                'I don’t need more blood. I rush the man and leave this place.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    jump finaldestinationafterevent
        elif pc_hp >= 3:
            if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                $ cleanliness_clothes_blood = 1
                show minus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            elif not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            elif not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ pc_hp = limit_pc_hp(pc_hp-3)
            show minus3hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
            menu:
                'You have time to focus and take a few peaceful breaths. You step back, get closer to the scavenger, and take the proper stance. The monster has no shield, no armor, and your axe can surely cut through such thin scales. You just need to hit it once.
                \n\nThe beast is smarter than you thought. Instead of merely attacking you with its toothed jaws, it jumps at you and knocks you over. The gambeson, already worn out, is not able to stop the beast’s powerful claws. You start to bleed, a lot.
                \n\nYou hear the animal’s pained yelping. The man stabs and cuts it with quick thrusts from all directions, once, twice, a dozen times. You have enough strength to use this opportunity to strike the dragonling’s leg with your axe, then push it away. You get on your knees and hit it again with a single, powerful blow. It stops moving.
                \n\nThe man helps you to stand up. “Thank ye, roadster. I’d be dead if I were ye!” He laughs, though you feel too much pain to join him. You look around. You’re not dangerously hurt, but all the scratches, abrasions, and cuts need to be cleaned with water. You’re lucky. The man is now reloading his crossbow. A not-so-distant howling already reaches your ears.
                \n\nYou can’t take the dead animals with you - {color=#f6d6bd}[horsename]{/color} won’t be able to carry much more. However, a few claws could be exchanged for a dragon bone or two.
                '
                'I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cut away one of the monster’s paws. “Let’s hurry. Wolves are going to catch the smell of blood soon.”')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    $ item_dragonlingpaw += 1
                    $ renpy.notify("You picked a dragonling’s paw.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a dragonling’s paw.{/i}')
                    jump finaldestinationafterevent
                'I don’t need more blood. I rush the man and leave this place.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need more blood. I rush the man and leave this place.')
                    $ travel_destination = "howlersdell"
                    $ quarters += 4
                    jump finaldestinationafterevent
        else:
            $ pc_hp = limit_pc_hp(0)
            show minus5hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
            if pc_religion == "pagan":
                show areapicture gameover_alt at basicfade
            else:
                show areapicture gameover at basicfade
            menu:
                'You have time to focus and take a few peaceful breaths. You step back, get closer to the scavenger, and take the proper stance. The monster has no shield, no armor, and your axe can surely cut through such thin scales. You just need to hit it once.
                \n\nThe beast is smarter than you thought. Instead of merely attacking you with its toothed jaws, it jumps at you and knocks you over. The gambeson, already worn out, is not able to stop the beast’s powerful claws.
                \n\nAs you’re reached by the distant shout of the man, who runs toward you with a raised blade, the last thing you see is the blood bursting through your chest.
                \n
                \n\n[pcname]’s soul has left its shell.
                '
                'Let me replay this encounter.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this encounter.')
                    stop music fadeout 4.0
                    $ renpy.load("combatsave")

############################################### pebbler
label roadtoencounter_pebbler01:
    if encounter_pebbler_trollurine == day or encounter_pebbler_day == day:
        jump finaldestinationafterevent
    elif not encounter_pebbler_firsttime:
        stop music fadeout 4.0
        play nature "audio/ambient/mountainroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        $ oldpagos_firsttime_intro = 1
        show areapicture westerncrossroadstooldpagos at basicfade
        if howlersdell_firsttime:
            $ custom1 = "a clean, shallow, yet wide creek that runs south"
        else:
            $ custom1 = "the clean, shallow, yet wide Howler’s Creek"
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        menu:
            'You cross [custom1], then follow the uphill path squeezed between the hills and the lush forest. You spend a good couple of minutes passing a haunting meadow, filled with dozens, maybe a hundred, cut-down trees, now overgrown by bushes and grass. You can’t think of another time when you’ve seen a clearing of such a size.
            '
            'Seems dangerous. If this goes on, the animals will join forces to strike down whoever is responsible for this.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Seems dangerous. If this goes on, the animals will forces to strike down whoever is responsible for this.')
                jump roadtoencounter_pebbler01a
            'The locals are surely ambitious. I wonder how far they can push it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The locals are surely ambitious. I wonder how far they can push it.')
                label roadtoencounter_pebbler01a:
                    $ encounter_pebbler_firsttime = 1
                    $ encounter_pebbler_day = day
                    $ encounter_pebbler_check = day
                    show areapicture westerncrossroadstooldpagos at basicfade
                    menu:
                        'Once the clearing ends and turns into a corridor of trees and hills, you stop your horse. There’s a monster in the middle of the road, reaching out with its long arms to grab and devour fruits and leaves from tree crowns, chewing them without haste. It’s standing on its hind legs and leaning on a thick tail. As there isn’t much hair on its gray skin, you see its impressive muscles. The beast is three times the size of a human, and while each move it makes is slow, its long claws and the ease with which it breaks one of the branches make you think that a single swing would be enough for it to pierce through your jacket or, just as likely, that it would simply break your bones and send you into the air.
                        \n\nLike most people, you know quite a bit about pebblers. Once they get used to an unfenced farm or a forest garden, getting rid of them can be a huge issue. There aren’t many blades able to cut through their thick skin and bones, and a single mistake may put them into a furious charge, encouraging them to look for human dwellings which they can tear down in revenge.
                        \n\nThe beast doesn’t give you as much as a glance, but also doesn’t move away. The best you can hope for is that it’s going to walk away on its own. Maybe tomorrow, maybe later.
                        '
                        'Facing it in a fight would end up badly. I return to the crossroads.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Facing it in a fight would end up badly. I return to the crossroads.')
                            $ quarters += 1
                            $ travel_destination = "westerncrossroads"
                            jump finaldestinationafterevent
    elif not encounter_pebbler_secondtime:
        stop music fadeout 4.0
        play nature "audio/ambient/mountainroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        show areapicture westerncrossroadstooldpagos at basicfade
        $ encounter_pebbler_secondtime = 1
        $ encounter_pebbler_check = day
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if day < 5:
            $ custom1 = "There are plenty of fruits and leaves the monster may chew on, so it may return any day now."
            $ custom2 = 1
        elif day < 10:
            $ custom1 = "There are many more fruits and leaves the monster may chew on, so it may return any day now."
            $ custom2 = 2
        elif day < 15:
            $ custom1 = "There is a sizable amount of fruits and leaves the monster may chew on, so it may return any day now."
            $ custom2 = 3
        elif day < 20:
            $ custom1 = "There are not that many fruits and leaves around for the monster to chew on, but it may still return here."
            $ custom2 = 4
        else:
            $ custom1 = "There is only a sparse amount of fruits and leaves around, and you wonder if the beast would be able to satisfy its hunger"
            $ custom2 = 5
        $ can_items = 1
        $ quarters += tooldpagos
        menu:
            'The path is clear, in a way. The pebbler is nowhere in sight, but the road is covered with leaves and broken branches. The only fruit-bearing trees are growing right on the sides of the road, surely planted there by humans. [custom1].
            '
            'Let’s hope the scavenger was right about the troll urine.' if item_trollurine and custom2 != 5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the scavenger was right about the troll urine.')
                $ encounter_pebbler_trollurine = day
                menu:
                    'You keep the jar far away from you, holding your breath, then you spread it around. A few splashes on the road, a few into the nearby bushes and on the tree trunks. {color=#f6d6bd}[horsename]{/color} snorts and walks in place, but once you also draw breath, there’s nothing unusual in the air. The urine smell is unpleasant, but nothing worse than {color=#f6d6bd}Hovlavan’s{/color} harbor.
                    '
                    'I hide the rest of the “potion” in my bag and continue my journey.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I hide the rest of the “potion” in my bag and continue my journey.')
                        $ quarters -= tooldpagos
                        jump finaldestinationafterevent
            'If it craves what this place has to offer so much, I should just get rid of its food. It may be a tiresome task, but at least I’ll gather some fruits for myself.' ( condition="quarters <= (world_daylength-12) and custom2 == 1 and pc_hp > 1" ): # ropehook
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- If it craves what this place has to offer so much, I should just get rid of its food. It may be a tiresome task, but at least I’ll gather some fruits for myself.')
                $ quarters += 8
                $ renpy.notify("You pick 3 bunches of wild plants.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You pick 3 bunches of wild plants.{/i}')
                $ item_wildplants += 3
                $ achievement_wildplants += 3
                $ encounter_pebbler_pickedapples = day
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                menu:
                    'You prepare all your tools, especially your thick, protective gloves, and tether {color=#f6d6bd}[horsename]{/color} to one of the younger trees.
                    \n\nIt’s not an easy task. You spend about two hours cutting down twigs, shaking off the fruits of the thinner branches, picking them by hand, or hitting them with a stick. Your rope helps you stay secure and the first few minutes of climbing is closer to fun than work, but the longer it takes, the more tired you become. You finally take a break to eat a couple of plums and apples, but the best ones you save for later, covering them with a blanket and putting it on the very top of your bundles.
                    \n\nYou’re standing on a carpet of greens, browns, reds, and purples. You drag some of the thicker branches to the side to make riding forward easier, but the earthworms and boars are going to have a feast.
                    '
                    'Let’s hope the pebbler is picky enough to ignore all the mess on the ground.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the pebbler is picky enough to ignore all the mess on the ground.')
                        $ quarters -= tooldpagos
                        jump finaldestinationafterevent
            'If it craves what this place has to offer so much, I should just get rid of its food. It may take me an hour or two, but at least I’ll gather some fruits for myself.' ( condition="quarters <= (world_daylength-10) and custom2 == 2 and pc_hp > 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- If it craves what this place has to offer so much, I should just get rid of its food. It may take me an hour or two, but at least I’ll gather some fruits for myself.')
                $ quarters += 6
                $ renpy.notify("You pick 2 bunches of wild plants.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You pick 2 bunches of wild plants.{/i}')
                $ item_wildplants += 2
                $ achievement_wildplants += 2
                $ encounter_pebbler_pickedapples = day
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                menu:
                    'You prepare all your tools, especially your thick, protective gloves, and tether {color=#f6d6bd}[horsename]{/color} to one of the younger trees.
                    \n\nIt’s not an easy task. You spend more than an hour cutting down twigs, shaking off the fruits of the thinner branches, picking them by hand, or hitting them with a stick. Your rope helps you stay secure and the first few minutes of climbing is closer to fun than work, but the longer it takes, the more tired you become. You finally take a break to eat a couple of plums and apples, but the best ones you save for later, covering them with a blanket and putting it on the very top of your bundles.
                    \n\nYou’re standing on a carpet of greens, browns, reds, and purples. You drag some of the thicker branches to the side to make riding forward easier, but the earthworms and boars are going to have a feast.
                    '
                    'Let’s hope the pebbler is picky enough to ignore all the mess on the ground.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the pebbler is picky enough to ignore all the mess on the ground.')
                        $ quarters -= tooldpagos
                        jump finaldestinationafterevent
            'If it craves what this place has to offer so much, I should just get rid of its food. It may take me an hour or two, but at least I’ll have a snack.' ( condition="quarters < (world_daylength-8) and custom2 == 3 and pc_hp > 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- If it craves what this place has to offer so much, I should just get rid of its food. It may take me a few hours, but at least I’ll have a snack.')
                $ quarters += 4
                $ renpy.notify("You pick a bunch of wild plants.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You pick a bunch of wild plants.{/i}')
                $ item_wildplants += 1
                $ achievement_wildplants += 1
                $ encounter_pebbler_pickedapples = day
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                menu:
                    'You prepare all your tools, especially your thick, protective gloves, and tether {color=#f6d6bd}[horsename]{/color} to one of the younger trees.
                    \n\nIt’s not an easy task. You spend about an hour cutting down twigs, shaking off the fruits of the thinner branches, picking them by hand, or hitting them with a stick. Your rope helps you stay secure and the first few minutes of climbing is closer to fun than work, but the longer it takes, the more tired you become. You take a break to eat a bunch of plums and apples, though there are not that many juicy or sweet ones left - the beast knew which ones to choose.
                    \n\nYou’re standing on a carpet of browns and greens, with some hints of reds and purples. You drag some of the thicker branches to the side to make riding forward easier, but the earthworms and boars are going to have a feast.
                    '
                    'Let’s hope the pebbler is picky enough to ignore all the mess on the ground.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the pebbler is picky enough to ignore all the mess on the ground.')
                        $ quarters -= tooldpagos
                        jump finaldestinationafterevent
            'If it craves what this place has to offer so much, I should just get rid of its food. It may take me an hour or two, but at least I’ll eat some fruits.' if quarters <= (world_daylength-6) and custom2 == 4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- If it craves what this place has to offer so much, I should just get rid of its food. It may take me a few hours, but at least I’ll eat some fruits.')
                $ quarters += 2
                $ pc_food = limit_pc_food(pc_food+1)
                show plus1food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 nourishment point.{/i}')
                $ encounter_pebbler_pickedapples = day
                menu:
                    'You prepare all your tools, especially your thick, protective gloves, and tether {color=#f6d6bd}[horsename]{/color} to one of the younger trees.
                    \n\nIt’s not an easy task, but it doesn’t take you more than half an hour. You cut down twigs, shake off the fruits of the thinner branches, pick them by hand, or hit them with a stick. Your rope helps you stay secure, and the climbing is closer to fun than work, especially since you’re done before you even get tired. There is only a fistful of tasty-looking plums and apples for you to snack on - the beast knew which fruit to choose.
                    \n\nYou’re standing on a carpet of browns and greens, with some hints of reds and purples. You drag some of the thicker branches to the side to make riding forward easier, but the earthworms and boars are going to have a feast.
                    '
                    'Let’s hope it’ll realize that all the food is already gone.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope it’ll realize that all the food is already gone.')
                        $ quarters -= tooldpagos
                        jump finaldestinationafterevent
            'I could get rid of these fruits so it wouldn’t come back... But it’s already almost dusk. (disabled)' if (quarters > (world_daylength-12) and custom2 == 1) or (quarters > (world_daylength-10) and custom2 == 2) or (quarters > (world_daylength-8) and custom2 == 3) or (quarters > (world_daylength-6) and custom2 == 4):
                pass
            'I’m too tired to climb so many trees and chop their branches. (Required vitality: 2) (disabled)' ( condition="(quarters <= (world_daylength-12) and custom2 == 1 and pc_hp <= 1) or (quarters <= (world_daylength-10) and custom2 == 2 and pc_hp <= 1) or (quarters <= (world_daylength-8) and custom2 == 3 and pc_hp <= 1)" ):
                pass
            'There’s almost no food left. I can just leave it as it is. (disabled)' if custom2 == 5:
                pass
            'Who knows, maybe it won’t be back.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Who knows, maybe it won’t be back.')
                $ quarters -= tooldpagos
                jump finaldestinationafterevent
    elif encounter_pebbler_pickedapples and encounter_pebbler_day < day:
        stop music fadeout 4.0
        play nature "audio/ambient/mountainroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        show areapicture westerncrossroadstooldpagos at basicfade
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ encounter_pebbler_gone = 1
        menu:
            'The road is still covered with the pebbler’s leftovers, as well as all the leaves and branches on the ground, but at least the beast is nowhere in sight, even though there are some fresh paw prints just nearby. Your plan worked just fine.
            '
            'Let’s hope the locals won’t be upset about the wasted fruits.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the locals won’t be upset about the wasted fruits.')
                jump finaldestinationafterevent
    elif encounter_pebbler_trollurine and encounter_pebbler_day < day:
        stop music fadeout 4.0
        play nature "audio/ambient/mountainroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        show areapicture westerncrossroadstooldpagos at basicfade
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ encounter_pebbler_gone = 1
        menu:
            'The road is still covered with the older branches and leaves, and there are some fresh paw prints just nearby, but at least the beast is nowhere in sight. You smell a whiff of urine, but it’s already at the verge of your senses. You wonder if the pebblers have a strong sense of smell.
            '
            'Most creatures have a stronger sense of smell than humans.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Most creatures have a stronger sense of smell than humans.')
                jump finaldestinationafterevent
    elif oldpagos_cured and encounter_pebbler_day < (day-1):
        stop music fadeout 4.0
        play nature "audio/ambient/mountainroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        show areapicture westerncrossroadstooldpagos at basicfade
        $ encounter_pebbler_gone = 1
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        menu:
            'There are still some leaves laying on the ground, but no more branches. Instead, you spot boot prints leading west. It looks like the people of {color=#f6d6bd}Old Págos{/color} took some time to clean this place. Maybe their increased activity will scare away the pebbler after all.
            '
            'Or maybe they’ll simply hunt it down.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Or maybe they’ll simply hunt it down.')
                jump finaldestinationafterevent
    elif day > 20:
        stop music fadeout 4.0
        play nature "audio/ambient/mountainroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        show areapicture westerncrossroadstooldpagos at basicfade
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ encounter_pebbler_gone = 1
        menu:
            'The road is still covered with the pebbler’s leftovers, but at least the beast is nowhere in sight. There are no more fruits among the trees and most of the branches are already stripped of any leaves.
            '
            'Maybe the creature needed to find a new spot for itself.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe the creature needed to find a new spot for itself.')
                jump finaldestinationafterevent
    else:
        stop music fadeout 4.0
        play nature "audio/ambient/mountainroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        show areapicture westerncrossroadstooldpagos at basicfade
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        $ d100roll -= encounter_pebbler_modifier
        $ encounter_pebbler_check = day
        if oldpagos_plague_helpfromgalerocks == 1 and quarters >= 40 and quarters <= 60 and oldpagos_plague_helpfromgalerocks_dayofleaving < day:
            jump encounter_pebblerspecialjump
        if d100roll > 50:
            $ encounter_pebbler_modifier += 25
            $ encounter_pebbler_day = day
            label encounter_pebbler_fluffloop:
                $ encounter_pebbler_fluff = renpy.random.choice(['It’s sitting in the middle of the road, looking at you as it chews the leaves still hanging from a branch.', 'It’s standing in the middle of the road, reaching out to the taller tree crowns.', 'It’s wandering about slowly, sniffing the ground and the nearby bushes. It stops once it notices your look.', 'It stands up on its hind legs, making a deep roar when you get closer.'])
                if encounter_pebbler_fluff == encounter_pebbler_fluff_old:
                    jump encounter_pebbler_fluffloop
                else:
                    $ encounter_pebbler_fluff_old = encounter_pebbler_fluff
            menu:
                'You reach the bottom of the hill and, unfortunately, the pebbler is already there. [encounter_pebbler_fluff]
                '
                'Facing it in a fight would end badly. I return to the crossroads.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Facing it in a fight would end badly. I return to the crossroads.')
                    $ quarters += 1
                    $ travel_destination = "westerncrossroads"
                    jump finaldestinationafterevent
        else:
            label encounter_pebblerspecialjump:
                $ encounter_pebbler_modifier = 0
                if day < 5:
                    $ custom1 = "There are plenty of fruit and leaves it may chew on, so it may return any day now."
                    $ custom2 = 1
                elif day < 10:
                    $ custom1 = "There are many more fruits and leaves it may chew on, so it may return any day now."
                    $ custom2 = 2
                elif day < 15:
                    $ custom1 = "There is a sizable amount of fruits and leaves it may chew on, so it may return any day now."
                    $ custom2 = 3
                elif day < 20:
                    $ custom1 = "There are not that many fruits and leaves around for it to chew on, but it may still return here."
                    $ custom2 = 4
                else:
                    $ custom1 = "There is only a sparse amount of fruits and leaves around, and you wonder if the beast would be able to satisfy its hunger"
                    $ custom2 = 5
                $ quarters += tooldpagos
                menu:
                    'You reach the bottom of the hill and the pebbler is nowhere in sight. [custom1]
                    '
                    'Let’s hope the scavenger was right about the troll urine.' if item_trollurine and custom2 != 5:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the scavenger was right about the troll urine.')
                        $ encounter_pebbler_trollurine = day
                        menu:
                            'You keep the jar far away from you, holding your breath, then you spread it around. A few splashes on the road, a few into the nearby bushes and on the tree trunks. {color=#f6d6bd}[horsename]{/color} snorts and walks in place, but once you also draw breath, there’s nothing unusual in the air. The urine smell is unpleasant, but nothing worse than {color=#f6d6bd}Hovlavan’s{/color} harbor.
                            '
                            'I hide the rest of the “potion” in my bag and continue my journey.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I hide the rest of the “potion” in my bag and continue my journey.')
                                $ quarters -= tooldpagos
                                jump finaldestinationafterevent
                    'If it craves what this place has to offer so much, I should just get rid of its food. It may be a tiresome task, but at least I’ll gather some fruits for myself.' ( condition="quarters <= (world_daylength-12) and custom2 == 1 and pc_hp > 1" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- If it craves what this place has to offer so much, I should just get rid of its food. It may be a tiresome task, but at least I’ll gather some fruits for myself.')
                        $ quarters += 8
                        $ renpy.notify("You pick 3 bunches of wild plants.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You pick 3 bunches of wild plants.{/i}')
                        $ item_wildplants += 3
                        $ achievement_wildplants += 3
                        $ encounter_pebbler_pickedapples = day
                        $ cleanliness = limit_cleanliness(cleanliness-1)
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                        menu:
                            'You prepare all your tools, especially your thick, protective gloves, and tether {color=#f6d6bd}[horsename]{/color} to one of the younger trees.
                            \n\nIt’s not an easy task. You spend about two hours cutting down twigs, shaking off the fruits of the thinner branches, picking them by hand, or hitting them with a stick. Your rope helps you stay secure and the first few minutes of climbing is closer to fun than work, but the longer it takes, the more tired you become. You finally take a break to eat a couple of plums and apples, but the best ones you save for later, covering them with a blanket and putting it on the very top of your bundles.
                            \n\nYou’re standing on a carpet of greens, browns, reds, and purples. You drag some of the thicker branches to the side to make riding forward easier, but the earthworms and boars are going to have a feast.
                            '
                            'Let’s hope the pebbler is picky enough to ignore all the mess on the ground.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the pebbler is picky enough to ignore all the mess on the ground.')
                                $ quarters -= tooldpagos
                                jump finaldestinationafterevent
                    'If it craves what this place has to offer so much, I should just get rid of its food. It may take me an hour or two, but at least I’ll gather some fruits for myself.' ( condition="quarters <= (world_daylength-10) and custom2 == 2 and pc_hp > 1" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- If it craves what this place has to offer so much, I should just get rid of its food. It may take me an hour or two, but at least I’ll gather some fruits for myself.')
                        $ quarters += 6
                        $ renpy.notify("You pick 2 bunches of wild plants.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You pick 2 bunches of wild plants.{/i}')
                        $ item_wildplants += 2
                        $ achievement_wildplants += 2
                        $ encounter_pebbler_pickedapples = day
                        $ cleanliness = limit_cleanliness(cleanliness-1)
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                        menu:
                            'You prepare all your tools, especially your thick, protective gloves, and tether {color=#f6d6bd}[horsename]{/color} to one of the younger trees.
                            \n\nIt’s not an easy task. You spend more than an hour cutting down twigs, shaking off the fruits of the thinner branches, picking them by hand, or hitting them with a stick. Your rope helps you stay secure and the first few minutes of climbing is closer to fun than work, but the longer it takes, the more tired you become. You finally take a break to eat a couple of plums and apples, but the best ones you save for later, covering them with a blanket and putting it on the very top of your bundles.
                            \n\nYou’re standing on a carpet of greens, browns, reds, and purples. You drag some of the thicker branches to the side to make riding forward easier, but the earthworms and boars are going to have a feast.
                            '
                            'Let’s hope the pebbler is picky enough to ignore all the mess on the ground.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the pebbler is picky enough to ignore all the mess on the ground.')
                                $ quarters -= tooldpagos
                                jump finaldestinationafterevent
                    'If it craves what this place has to offer so much, I should just get rid of its food. It may take me an hour or two, but at least I’ll have a snack.' ( condition="quarters < (world_daylength-8) and custom2 == 3 and pc_hp > 1" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- If it craves what this place has to offer so much, I should just get rid of its food. It may take me a few hours, but at least I’ll have a snack.')
                        $ quarters += 4
                        $ renpy.notify("You pick a bunch of wild plants.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You pick a bunch of wild plants.{/i}')
                        $ item_wildplants += 1
                        $ achievement_wildplants += 1
                        $ encounter_pebbler_pickedapples = day
                        $ cleanliness = limit_cleanliness(cleanliness-1)
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                        menu:
                            'You prepare all your tools, especially your thick, protective gloves, and tether {color=#f6d6bd}[horsename]{/color} to one of the younger trees.
                            \n\nIt’s not an easy task. You spend about an hour cutting down twigs, shaking off the fruits of the thinner branches, picking them by hand, or hitting them with a stick. Your rope helps you stay secure and the first few minutes of climbing is closer to fun than work, but the longer it takes, the more tired you become. You take a break to eat a bunch of plums and apples, though there are not that many juicy or sweet ones left - the beast knew which ones to choose.
                            \n\nYou’re standing on a carpet of browns and greens, with some hints of reds and purples. You drag some of the thicker branches to the side to make riding forward easier, but the earthworms and boars are going to have a feast.
                            '
                            'Let’s hope the pebbler is picky enough to ignore all the mess on the ground.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the pebbler is picky enough to ignore all the mess on the ground.')
                                $ quarters -= tooldpagos
                                jump finaldestinationafterevent
                    'If it craves what this place has to offer so much, I should just get rid of its food. It may take me an hour or two, but at least I’ll eat some fruits.' if quarters <= 78 and custom2 == 4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- If it craves what this place has to offer so much, I should just get rid of its food. It may take me a few hours, but at least I’ll eat some fruits.')
                        $ quarters += 2
                        $ pc_food = limit_pc_food(pc_food+1)
                        show plus1food at foodchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 nourishment point.{/i}')
                        $ encounter_pebbler_pickedapples = day
                        menu:
                            'You prepare all your tools, especially your thick, protective gloves, and tether {color=#f6d6bd}[horsename]{/color} to one of the younger trees.
                            \n\nIt’s not an easy task, but it doesn’t take you more than half an hour. You cut down twigs, shake off the fruits of the thinner branches, pick them by hand, or hit them with a stick. Your rope helps you stay secure, and the climbing is closer to fun than work, especially since you’re done before you even get tired. There is only a fistful of tasty-looking plums and apples for you to snack on - the beast knew which fruit to choose.
                            \n\nYou’re standing on a carpet of browns and greens, with some hints of reds and purples. You drag some of the thicker branches to the side to make riding forward easier, but the earthworms and boars are going to have a feast.
                            '
                            'Let’s hope it’ll realize that all the food is already gone.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope it’ll realize that all the food is already gone.')
                                $ quarters -= tooldpagos
                                jump finaldestinationafterevent
                    'I could get rid of these fruits so it wouldn’t come back... But it’s already almost dusk. (disabled)' if (quarters > (world_daylength-12) and custom2 == 1) or (quarters > (world_daylength-10) and custom2 == 2) or (quarters > (world_daylength-8) and custom2 == 3) or (quarters > (world_daylength-6) and custom2 == 4):
                        pass
                    'I’m too tired to climb so many trees and chop their branches. (Required vitality: 2) (disabled)' ( condition="(quarters <= (world_daylength-12) and custom2 == 1 and pc_hp <= 1) or (quarters <= (world_daylength-10) and custom2 == 2 and pc_hp <= 1) or (quarters <= (world_daylength-8) and custom2 == 3 and pc_hp <= 1)" ):
                        pass
                    'There’s almost no food left. I can just leave it as it is. (disabled)' if custom2 == 5:
                        pass
                    'Who knows, maybe it won’t be back.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Who knows, maybe it won’t be back.')
                        $ quarters -= tooldpagos
                        jump finaldestinationafterevent

############################################### goblins
label encounter_fallentree_goblins01all:
    label encounter_fallentree_goblins01:
        $ renpy.save("combatsave", extra_info='Combat Auto Save')
        if todolmen <= towatchtower and dolmen_firsttime:
            show areapicture dolmentofallentree at basicfade
        elif eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            show areapicture fallentreetowatchtower_fixed at basicfade
        else:
            show areapicture fallentreetowatchtower at basicfade
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        # if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
        play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
        $ can_potions = 1
        menu:
            'The neglected path barely finds any space among all the hills, trees, and streams. There’s a deer on the ground, lying in a red puddle, surrounded by a small pack of creatures which notice your presence quickly.
            \n\nThere’s about eight of them, with thick furs in shades of brown, gray, and black, and hairless faces with small eyes and large mouths, currently stained by the blood of their prey. Some of them move on all fours, while others comfortably stand on two feet. They are two to three heads shorter than you, but it’s your mount which truly towers over them, and you see how a couple of the beasts take a few steps back, grunting and glancing at one another.
            \n\nThe one with gray fur shouts, and the others move toward the rocks and sticks which are piled on the road. They hold them awkwardly, and some struggle to maintain a straight posture, leaning on their new weapons for support. Then, almost all of them spread to your left and right, blending with the shrubs loudly. Only two of the apes are standing still.
            '
            'I grab my axe and hold the reins tightly.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my axe and hold the reins tightly.')
                if pc_class == "warrior":
                    $ at_unlock_force = 1
                    $ at = 0
                menu:
                    '{color=#f6d6bd}[horsename]{/color} tries to turn around, but loyally follows your directions.
                    '
                    '{image=d6} I charge at the goblins in the middle of the road.' if not item_asterionspear and not item_goblinspear and not item_mountainroadspear:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I charge at the goblins in the middle of the road.')
                        $ custom1 = "swing"
                        $ at_unlock_force = 0
                        jump encounter_fallentree_goblins03charge
                    '{image=d6} I grab my spear and charge at the goblins in the middle of the road.' if item_asterionspear or item_mountainroadspear:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my spear and charge at the goblins in the middle of the road.')
                        $ custom1 = "thrust"
                        $ at_unlock_force = 0
                        jump encounter_fallentree_goblins03charge
                    '{image=d6} I grab the goblin’s spear and charge at the ones in the middle of the road.' if item_goblinspear and not item_asterionspear and not item_mountainroadspear:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab the goblin’s spear and charge at the ones in the middle of the road.')
                        $ custom1 = "thrust"
                        $ at_unlock_force = 0
                        jump encounter_fallentree_goblins03charge
                    '{image=d6} I scream at the pack, shaking my weapon. I try to scare them away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I scream at the pack, shaking my weapon. I try to scare them away.')
                        $ at_unlock_force = 0
                        $ d100roll = 0
                        $ d100roll = renpy.random.randint(1, 100)
                        if not pc_food:
                            $ d100roll += 5
                        if pc_food == 3:
                            $ d100roll -= 5
                        if pc_food == 4:
                            $ d100roll -= 10
                        $ encounter_fallentree_goblins_afraid += 5
                        if d100roll < (10+(pc_hp*5)):
                            $ encounter_fallentree_goblins_amount -= 1
                            $ custom1 = "You do your best, raising your voice in a fierce shout and showing that you’re ready to take them down. The gray goblin seems unmoved, showing you its long tusks and swinging its arms, but its younger companion looks around, grunting, then jumps into the bushes. The gray one looks after it, but then focuses its attention on you - or rather, something that’s just behind you."
                        else:
                            $ custom1 = "You do your best, raising your voice in a fierce shout and showing that you’re ready to take them down. The gray goblin seems unmoved, showing you its long tusks and swinging its arms, and its younger companion looks around, grunting, but then stays in place. The gray one then focuses its attention on you - or rather, something that’s just behind you."
                        jump encounter_fallentree_goblins02
                    'I may still have time to load my crossbow.' ( condition="at != 'force' and item_crossbow and item_crossbowquarrels" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may still have time to load my crossbow.')
                        $ custom1 = "You reach for your weapon, unstrapping it from the bundles and trying to simultaneously reach for a quarrel, but you realize it’s not going to work. Maybe the goblins know what’s going on, or maybe they feel encouraged by your passiveness - they jump forward from a couple of sides at once."
                        $ at_unlock_force = 0
                        jump encounter_fallentree_goblins02
                    'There’s no time to load the crossbow. (disabled)' ( condition="at == 'force' and item_crossbow and item_crossbowquarrels" ):
                        pass
                    'I don’t have a crossbow. (disabled)' if not item_crossbow:
                        pass
                    'It will take a moment, but I reach for my shield.' if item_shield:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will take a moment, but I reach for my shield.')
                        $ custom1 = "You unstrap it and grab it with your weaker hand, covering a significant part of your side, especially the bent leg. The goblins which see it still approach you, but carefully - you wonder if they know how a shield works."
                        $ encounter_fallentree_goblins_shield += 1
                        $ at_unlock_force = 0
                        jump encounter_fallentree_goblins02
                    'It will take a moment, but I reach for the jar with troll urine.' if item_trollurine:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will take a moment, but I reach for the jar with troll urine.')
                        $ custom1 = "You reach for the jar, trying to unstrap it from the bundles and take it out from its sack, but you realize it’s not going to work. Maybe the goblins know what’s going on, or maybe they feel encouraged by your passiveness - they jump forward from a couple of sides at once."
                        $ encounter_fallentree_goblins_shield += 1
                        $ at_unlock_force = 0
                        jump encounter_fallentree_goblins02
                    'I throw them some food. Maybe they’ll leave me alone.' if item_rations:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw them some food. Maybe they’ll leave me alone.')
                        $ item_rations -= 1
                        $ at_unlock_force = 0
                        if armor >= 2:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ renpy.notify('You lost a food ration.')
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                            $ custom2 = "Then, you get stabbed in the back - literally. You turn around, seeing a goblin that, as far as you can tell, was not a part of the group surrounding the carcass. It’s holding a wooden spear, or rather a pointed stick, longer than the creature is tall. Your armor was able to reduce the impact, but you feel the pain from the hit, and you can tell that the linen was torn. You’ll need to find someone able to fix it."
                        else:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                            $ encounter_fallentree_goblins_dmg += 1
                            $ renpy.notify('You lost a food ration.')
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                            $ custom2 = "Then, you get stabbed in the back - literally. You turn around, seeing a goblin that, as far as you can tell, was not a part of the group surrounding the carcass. It’s holding a wooden spear, or rather a pointed stick, longer than the creature is tall, and now covered with your blood on its tip. You could swear the creature is smiling at your pain. It triumphantly shouts, echoed by its companions."
                        menu:
                            'You reach for a food ration, cut the linen sheet with your blade, and throw the fruits, nuts, and meat in a couple of directions, but mostly toward the goblins on the road. They step back, then glance at the food laying in the deer’s blood, and look back at you, showing their tusks. They don’t seem hungry.
                            \n\n[custom2]
                            \n\nYou wonder how many of them are still hiding among the trees.
                            '
                            '{image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}[horsename]{/color} forward.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}%s{/color} forward.' %horsename)
                                jump encounter_fallentree_goblins03charge
                    'I look behind me, just to be sure they are not already there.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look behind me, just to be sure they are not already there.')
                        $ at_unlock_force = 0
                        jump encounter_fallentree_goblins02behind
                    'I make a few threatening swings, focusing my attention on the beasts that entered the forest.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make a few threatening swings, focusing my attention on the beasts that entered the forest.')
                        $ custom1 = "The goblins on your left and right take cautious steps, keeping some distance between one another, as if they want to be sure you won’t find a way of escaping. They keep making noises, some of them ape-like, some of them weirdly similar to those of humans. They grunt, screech, shout, and shake their weapons at you. You wonder if these gestures are something they make whenever they face an enemy, or just humans."
                        jump encounter_fallentree_goblins02
                    'I dismount and prepare for combat.' ( condition="at != 'force'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and prepare for combat.')
                        $ at_unlock_force = 0
                        jump encounter_fallentree_goblinsdeath
                    'I need to stay in the saddle. I won’t be able to keep my horse safe. (disabled)' ( condition="at == 'force'"):
                        pass
                    'I wait for their move.' ( condition="at != 'force'"):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for their move.')
                        $ at_unlock_force = 0
                        $ custom1 = "The goblins on your left and right take cautious steps, keeping some distance between one another, as if they want to be sure you won’t find a way of escaping. They keep making noises, some of them ape-like, some of them weirdly similar to those of humans. They grunt, screech, shout, and shake their weapons at you. The ones ahead of you show their tusks, holding their position, waving their arms, thudding with their wide feet."
                        jump encounter_fallentree_goblins02
                    'They’re going to surround me soon. It’s time to act. (disabled)' ( condition="at == 'force'"):
                        pass
            'I’m not prepared to face a pack of goblins. I turn around.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not prepared to face a pack of goblins. I turn around.')
                $ encounter_fallentree_goblins = day
                menu:
                    '{color=#f6d6bd}[horsename]{/color} is more than ready to do so. It hardly has enough space to make a swift turn, and a goblin tries to stab it with a pointed stick, but it’s too blunt, or the hit is too weak, to pierce through the skin. The shouting beasts behind you sound victorious, but they would never be able to catch up with a palfrey.
                    \n\nThey may spend the entire day feasting on such a large animal.
                    '
                    'I head back to the watchtower.' if watchtower_firsttime and towatchtower <= todolmen:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the watchtower.')
                        $ quarters += 1
                        $ travel_destination = "watchtower"
                        $ can_potions = 0
                        jump finaldestinationafterevent
                    'I head back to the crossroads.' if not watchtower_firsttime or (watchtower_firsttime and towatchtower > todolmen):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the crossroads.')
                        $ quarters += 1
                        $ travel_destination = "southerncrossroads"
                        $ can_potions = 0
                        jump finaldestinationafterevent

    label encounter_fallentree_goblins01return:
        $ renpy.save("combatsave", extra_info='Combat Auto Save')
        $ can_potions = 1
        if todolmen <= towatchtower and dolmen_firsttime:
            show areapicture dolmentofallentree at basicfade
        elif eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            show areapicture fallentreetowatchtower_fixed at basicfade
        else:
            show areapicture fallentreetowatchtower at basicfade
        if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
            play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ encounter_fallentree_goblins = 0
        if pc_class == "warrior":
            $ at_unlock_force = 1
            $ at = 0
        menu:
            'The goblins are still around, resting near the bones and flesh of their prey. They are already spread around and ready for combat, alerted by the familiar sound of hooves. This time, running away may be too difficult.
            \n\nThe axe is in your hand.
            '
            '{image=d6} I charge at the goblins in the middle of the road.' if not item_asterionspear and not item_goblinspear and not item_mountainroadspear:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I charge at the goblins in the middle of the road.')
                $ custom1 = "swing"
                $ at_unlock_force = 0
                jump encounter_fallentree_goblins03charge
            '{image=d6} I grab my spear and charge at the goblins in the middle of the road.' if item_asterionspear or item_mountainroadspear:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my spear and charge at the goblins in the middle of the road.')
                $ custom1 = "thrust"
                $ at_unlock_force = 0
                jump encounter_fallentree_goblins03charge
            '{image=d6} I grab the goblin’s spear and charge at the ones in the middle of the road.' if item_goblinspear and not item_asterionspear and not item_mountainroadspear:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab the goblin’s spear and charge at the ones in the middle of the road.')
                $ custom1 = "thrust"
                $ at_unlock_force = 0
                jump encounter_fallentree_goblins03charge
            '{image=d6} I scream at the pack, shaking my weapons. I try to scare them away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I scream at the pack, shaking my weapons. I try to scare them away.')
                $ at_unlock_force = 0
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 10
                if pc_food == 3:
                    $ d100roll -= 10
                if pc_food == 4:
                    $ d100roll -= 20
                $ encounter_fallentree_goblins_afraid += 5
                if d100roll < (10+(pc_hp*5)):
                    $ encounter_fallentree_goblins_amount -= 1
                    $ custom1 = "You do your best, raising your voice in a fierce shout and showing that you’re ready to take them down. The gray goblin seems unmoved, showing you its long tusks and swinging its arms, but its younger companion looks around, grunting, then jumps into the bushes. The gray one looks after it, but then focuses its attention on you - or rather, something that’s just behind you."
                else:
                    $ custom1 = "You do your best, raising your voice in a fierce shout and showing that you’re ready to take them down. The gray goblin seems unmoved, showing you its long tusks and swinging its arms, and its younger companion looks around, grunting, but then stays in place. The gray one then focuses its attention on you - or rather, something that’s just behind you."
                jump encounter_fallentree_goblins02
            'I may still have time to load my crossbow.' ( condition="at != 'force' and item_crossbow and item_crossbowquarrels" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may still have time to load my crossbow.')
                $ custom1 = "You reach for your weapon, unstrapping it from the bundles and trying to simultaneously reach for a quarrel, but you realize it’s not going to work. Maybe the goblins know what’s going on, or maybe they feel encouraged by your passiveness - they jump forward from a couple of sides at once."
                $ at_unlock_force = 0
                jump encounter_fallentree_goblins02
            'There’s no time to load the crossbow. (disabled)' ( condition="at == 'force' and item_crossbow and item_crossbowquarrels" ):
                pass
            'I don’t have a crossbow. (disabled)' if not item_crossbow:
                pass
            'It will take a moment, but I grab my shield.' if item_shield:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will take a moment, but I grab my shield.')
                $ custom1 = "You unstrap it and grab it with your weaker hand, covering a significant part of your side, especially the bent leg. The goblins which see it still approach you, but carefully - you wonder if they know how a shield works."
                $ encounter_fallentree_goblins_shield += 1
                $ at_unlock_force = 0
                jump encounter_fallentree_goblins02
            'It will take a moment, but I grab the jar with troll urine.' if item_trollurine:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will take a moment, but I grab the jar with troll urine.')
                $ custom1 = "You reach for the jar, trying to unstrap it from the bundles and take it out from its sack, but you realize it’s not going to work. Maybe the goblins know what’s going on, or maybe they feel encouraged by your passiveness - they jump forward from a couple of sides at once."
                $ encounter_fallentree_goblins_shield += 1
                $ at_unlock_force = 0
                jump encounter_fallentree_goblins02
            'I throw them some food. Maybe they’ll leave me alone.' if item_rations:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw them some food. Maybe they’ll leave me alone.')
                $ item_rations -= 1
                $ at_unlock_force = 0
                if armor >= 2:
                    $ armor = limit_armor(armor-1)
                    show minus1armor at armorchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                    $ custom2 = "Then, you get stabbed in the back - literally. You turn around, seeing a goblin that, as far as you can tell, was not a part of the group surrounding the carcass. It’s holding a wooden spear, or rather a pointed stick, longer than the creature is tall. Your armor was able to reduce the impact, but you feel the pain from the hit, and you can tell that the linen was torn. You’ll need to find someone able to fix it."
                else:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                    if not cleanliness_clothes_torn:
                        $ cleanliness_clothes_torn = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    $ encounter_fallentree_goblins_dmg += 1
                    $ renpy.notify('You lost a food ration.')
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                    $ custom2 = "Then, you get stabbed in the back - literally. You turn around, seeing a goblin that, as far as you can tell, was not a part of the group surrounding the carcass. It’s holding a wooden spear, or rather a pointed stick, longer than the creature is tall, and now covered with your blood on its tip. You could swear the creature is smiling at your pain. It triumphantly shouts, echoed by its companions. "
                menu:
                    'You reach for a food ration, cut the linen sheet with your blade and throw the fruits, nuts, and meat in a couple of directions, but mostly toward the goblins on the road. They step back, then glance at the food laying in the deer’s blood, and look back at you, showing their tusks. They don’t seem hungry.
                    \n\n[custom2]
                    \n\nYou wonder how many of them are still hiding among the trees.
                    '
                    '{image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}[horsename]{/color} forward.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}%s{/color} forward.' %horsename)
                        jump encounter_fallentree_goblins03charge
            'I look behind me, just to be sure they are not already there.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look behind me, just to be sure they are not already there.')
                $ at_unlock_force = 0
                jump encounter_fallentree_goblins02behind
            'I make a few threatening swings, focusing my attention on the beasts that entered the forest.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make a few threatening swings, focusing my attention on the beasts that entered the forest.')
                $ custom1 = "The goblins on your left and right take cautious steps, keeping some distance between one another, as if they want to be sure you won’t find a way of escaping. They keep making noises, some of them ape-like, some of them weirdly similar to those of humans. They grunt, screech, shout, and shake their weapons at you. You wonder if these gestures are something they make whenever they face an enemy, or just humans."
                jump encounter_fallentree_goblins02
            'I dismount and prepare for combat.' ( condition="at != 'force'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and prepare for combat.')
                $ at_unlock_force = 0
                jump encounter_fallentree_goblinsdeath
            'I need to stay in the saddle. I won’t be able to keep my horse safe. (disabled)' ( condition="at == 'force'"):
                pass
            'I wait for their move.' ( condition="at != 'force'"):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for their move.')
                $ at_unlock_force = 0
                $ custom1 = "The goblins on your left and right take cautious steps, keeping some distance between one another, as if they want to be sure you won’t find a way of escaping. They keep making noises, some of them ape-like, some of them weirdly similar to those of humans. They grunt, screech, shout, and shake their weapons at you. The ones ahead of you show their tusks, holding their position, waving their arms, thudding with their wide feet."
                jump encounter_fallentree_goblins02
            'They’re going to surround me soon. It’s time to act. (disabled)' ( condition="at == 'force'"):
                pass

    label encounter_fallentree_goblinsdeath:
        $ pc_hp = limit_pc_hp(0)
        show minus5hp at hpchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
        if pc_religion == "pagan":
            show areapicture gameover_alt at basicfade
        else:
            show areapicture gameover at basicfade
        menu:
            'You rise to your feet and realize that the goblins are not as small as they seemed from the saddle. They may hold weapons, but you now see their lengthy tusks and massive hands. You hear {color=#f6d6bd}[horsename]’s{/color} groans, then it runs away, with a wooden spear sticking out of its side. It clashes with the goblins, trampling one of them, while a second manages to cling to the horse’s side, biting it and tearing its skin with its claws. Your mount dies in silence, running to the very end.
            \n\nYou get stabbed from behind, then charged at from two sides at once. You have an advantage when it comes to fighting any one of the members of the pack, but you underestimated their numbers. There were a dozen more of them spread among the trees, and they hit you like a wave.
            \n\nThe furry foot stands on your chest, and the deer’s blood mixes with your own.
            \n
            \n\n[pcname]’s soul has left its shell.
            '
            'Let me replay this encounter.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this encounter.')
                stop music fadeout 4.0
                $ renpy.load("combatsave")

    label encounter_fallentree_goblins02:
        if armor >= 2:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ custom2 = "Then, you get stabbed in the back - literally. You turn around, seeing a goblin that, as far as you can tell, was not a part of the group surrounding the carcass. It’s holding a wooden spear, or rather a pointed stick, longer than the creature is tall. Your armor was able to reduce the impact, but you feel the pain from the hit, and you can tell that the linen was torn. You’ll need to find someone able to fix it."
        else:
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            $ encounter_fallentree_goblins_dmg += 1
            $ custom2 = "Then, you get stabbed in the back - literally. You turn around, seeing a goblin that, as far as you can tell, was not a part of the group surrounding the carcass. It’s holding a wooden spear, or rather a pointed stick, longer than the creature is tall, and now covered with your blood on its tip. You could swear the creature is smiling at your pain. It triumphantly shouts, echoed by its companions."
        menu:
            '[custom1]
            \n\n[custom2]
            \n\nYou wonder how many of them are still hiding among the trees.
            '
            '{image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}[horsename]{/color} forward.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}%s{/color} forward.' %horsename)
                jump encounter_fallentree_goblins03charge

    label encounter_fallentree_goblins02behind:
        $ encounter_fallentree_goblins_afraid += 5
        menu:
            'You see a surprised goblin which, as far as you can tell, was not a part of the group surrounding the carcass. It’s holding a wooden spear, or rather a pointed stick, longer than the creature is tall.
            '
            '{image=d6} I hit the spear with my axe.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I hit the spear with my axe.')
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 10
                if pc_food == 3:
                    $ d100roll -= 10
                if pc_food == 4:
                    $ d100roll -= 20
                if armor == 4:
                    $ d100roll -= 5
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                if item_golemglove:
                    $ d100roll -= 10
                if item_axe03:
                    $ d100roll -= 20
                elif item_axe02 or item_axe02alt:
                    $ d100roll -= 10
                if d100roll < (10+(pc_hp*10)):
                    $ item_goblinspear = 1
                    $ encounter_fallentree_goblins_afraid += 10
                    menu:
                        'You cut through the wooden shaft swiftly, sending the pointed end of the stick into the air. The beast lets go of the remaining weapon and jumps away, landing on all fours. It grunts in awe, and the other goblins shout both at you and at one another. They suddenly leap forward, trying to get to you from multiple directions at once. There’s more of them now than at the start, over a dozen.
                        '
                        '{image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}[horsename]{/color} forward.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}%s{/color} forward.' %horsename)
                            jump encounter_fallentree_goblins03charge
                else:
                    menu:
                        'You hit the wooden shaft, but either you’re lacking strength, or your weapon is just too blunt - the spear gets pushed away, but that’s all. The goblin grunts and raises it again, preparing for the attack. It makes a threatening cry, and the other goblins shout both at you and at one another. They suddenly leap forward, trying to get to you from multiple directions at once. There’s more of them now than at the start, over a dozen.
                        '
                        '{image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}[horsename]{/color} forward.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}%s{/color} forward.' %horsename)
                            jump encounter_fallentree_goblins03charge
            '{image=d6} I grab the spear and pull it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab the spear and pull it.')
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 10
                if pc_food == 3:
                    $ d100roll -= 10
                if pc_food == 4:
                    $ d100roll -= 20
                if armor == 4:
                    $ d100roll -= 5
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                if d100roll < (10+(pc_hp*20)):
                    $ item_goblinspear = 1
                    $ encounter_fallentree_goblins_afraid += 5
                    $ renpy.notify("You took the goblin spear.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You took the goblin spear.{/i}')
                    menu:
                        'You grab the spear and struggle a bit to take it away from the goblin, but the way the situation unfolds seems to shock it so much that it lets go of the weapon and jumps away, landing on all fours. It grunts in awe, and the other goblins shout both at you and at one another. They suddenly leap forward, trying to get to you from multiple directions at once. There’s more of them now than at the start, over a dozen.
                        '
                        '{image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}[horsename]{/color} forward.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}%s{/color} forward.' %horsename)
                            jump encounter_fallentree_goblins03charge
                else:
                    menu:
                        'You grab the spear and struggle a bit to take it away from the goblin, but it turns out to be stronger. It hits you, though only lightly, not even piercing through your armor. Still, it makes a triumphant cry, and the other goblins shout both at you and at one another. They suddenly leap forward, trying to get to you from multiple directions at once. There’s more of them now than at the start, over a dozen.
                        '
                        '{image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}[horsename]{/color} forward.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}%s{/color} forward.' %horsename)
                            jump encounter_fallentree_goblins03charge
            '{image=d6} I dodge the hit.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I dodge the hit.')
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 10
                if pc_food == 3:
                    $ d100roll -= 10
                if pc_food == 4:
                    $ d100roll -= 20
                if armor == 4:
                    $ d100roll -= 5
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                $ d100roll -= encounter_fallentree_goblins_afraid
                if d100roll < (10+(pc_hp*10)):
                    $ encounter_fallentree_goblins_afraid += 1
                    menu:
                        'You look at each other for a heartbeat, then the creature shouts loudly and leaps forward, trying to stab your side, but it finds only air. It lets out a fearful cry and drops the weapon, which falls on the ground, then jumps away, landing on all fours. It grunts in awe, and the other goblins shout both at you and at one another. They suddenly leap forward, trying to get to you from multiple directions at once. There’s more of them now than at the start, over a dozen.
                        '
                        '{image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}[horsename]{/color} forward.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}%s{/color} forward.' %horsename)
                            jump encounter_fallentree_goblins03charge
                else:
                    if armor >= 2:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom2 = "and while your armor was strong enough to protect you, you hear the material tear. You could swear the creature is smiling at your pain."
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        $ encounter_fallentree_goblins_dmg += 1
                        $ custom2 = "covering the tip with blood, and you could swear the creature is smiling at your pain"
                        menu:
                            'You look at each other for a heartbeat, then the creature shouts loudly and leaps forward, trying to stab your side, and your position is just too stiff for you to lean away. The hit lands, [custom2]. It triumphantly shouts, echoed by its companions. There’s more of them now than at the start, over a dozen.
                            '
                            '{image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}[horsename]{/color} forward.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I can’t win, and I can’t run away. I rush {color=#f6d6bd}%s{/color} forward.' %horsename)
                                jump encounter_fallentree_goblins03charge
            '{image=d6} I need to charge at the goblins down the road before this one attacks me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to charge at the goblins down the road before this one attacks me.')
                jump encounter_fallentree_goblins03charge

    label encounter_fallentree_goblins03charge:
        $ modifier = (50+(encounter_fallentree_goblins_amount*25))
        $ d100roll = 0
        $ d100roll = renpy.random.randint(1, 100)
        if not pc_food:
            $ d100roll += 10
        if pc_food == 3:
            $ d100roll -= 10
        if pc_food == 4:
            $ d100roll -= 20
        if armor == 4:
            $ d100roll -= 5
        if pc_class == "warrior":
            $ d100roll -= (pc_battlecounter*2)
        else:
            $ d100roll -= (pc_battlecounter)
        $ d100roll -= encounter_fallentree_goblins_afraid
        if encounter_fallentree_goblins_shield:
            $ d100roll += 10
        if item_asterionspear or item_mountainroadspear:
            $ d100roll += 20
        elif item_goblinspear:
            $ d100roll += 10
        if modifier < encounter_fallentree_goblins_afraid: # success
            if pc_class == "warrior":
                $ custom1 = "but while you may have hundreds of hours of training behind you, hardly any of them happened in the saddle. You do your best to focus"
            else:
                $ custom1 = "but while you feel fine with a blade when on foot, fighting from a saddle is completely unfamiliar to you"
            if encounter_fallentree_goblins_amount == 2:
                $ custom2 = "The two goblins don’t know how to react. The younger one tries to catch your horse, but the strike it receives sends it into the nearby bush, screaming in pain. The gray one is reaching out for your boot, but you’re well prepared for it."
            else:
                $ custom2 = "The other goblin didn’t return, and the gray one is reaching out for your boot, maybe hoping to get you on the ground, but you’re well prepared for it."
            if item_asterionspear or item_mountainroadspear:
                $ custom3 = "You hit it with the spear, not only piercing the beast’s skull, but also using the impact to push it out of your way. Still riding, you shake the blood off the spearhead."
            elif item_goblinspear:
                $ custom3 = "You hit it with the pointed stick, not only piercing the beast’s skull, but also using the impact to push it out of your way. The tip is covered with blood."
                $ encounter_fallentree_goblins_bloodonspear = 1
            elif encounter_fallentree_goblins_shield:
                $ custom3 = "You move your shield to keep the beast’s hands away, then hit its head, making the creature roll over the road."
            else: # axe
                $ custom3 = "A lucky swing of your axe hits its skull, not only crushing the bone, but also pushing it out of your way. Still riding, you shake the blood off your blade."
            menu:
                'Your mount speeds up, though it doesn’t have enough space to enter a gallop. You prepare your weapon, [custom1].
                \n\n[custom2] [custom3]
                '
                'We ride as fast as we can.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- We ride as fast as we can.')
                    jump encounter_fallentree_goblinsfinish
                'I ride as fast as I can.' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride as fast as I can.')
                    jump encounter_fallentree_goblinsfinish
        else:
            if pc_class == "warrior":
                $ custom1 = "but while you may have hundreds of hours of training behind you, hardly any of them happened in the saddle. You do your best to focus"
            else:
                $ custom1 = "but while you feel somewhat comfortable with a blade when on foot, fighting from a saddle is completely unfamiliar to you"
            if encounter_fallentree_goblins_amount == 2:
                $ custom2 = "The younger goblin attempts to stop your horse, but the strike it receives sends it into the nearby bush, screaming in pain. The gray one, however, manages to grab your boot, and is now trying to keep up with your speed, making one long leap after another."
            else:
                $ custom2 = "The other goblin didn’t return, but the gray one manages not only to jump aside, but also to bounce off the landing spot and grab your boot. It’s now trying to keep up with your speed, making one long leap after another."
            if item_asterionspear or item_mountainroadspear:
                $ custom3 = "\n\nYour attack with the spear almost hits the mark, but the creature makes such unpredictable movements that you struggle to land a good jab."
            elif item_goblinspear:
                $ custom3 = "\n\nYour attack with the pointed stick almost hits the mark, but the creature makes such unpredictable movements that you struggle to land a good jab."
            elif encounter_fallentree_goblins_shield:
                $ custom3 = "\n\nYour attack with the shield is of little help since the creature stays on the opposite side."
            else: # axe
                $ custom3 = "\n\nThe first strong swing of your axe wasn’t able to reach the target - a spear would do better in this scenario."
            if pc_class == "mage":
                $ at_unlock_spell = 1
                $ manacost = 2
                $ at = 0
            menu:
                'Your mount speeds up, though it doesn’t have enough space to enter a gallop. You prepare your weapon, [custom1].
                \n\n[custom2] [custom3]
                '
                '{image=d6} I try to hit it with magic. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I try to hit it with magic.')
                    $ at_unlock_spell = 0
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    $ d100roll -= (pc_battlecounter)
                    if not pc_food:
                        $ d100roll += 10
                    if pc_food == 3:
                        $ d100roll -= 10
                    if pc_food == 4:
                        $ d100roll -= 20
                    $ mana = limit_mana(mana-manacost)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                    if d100roll < 81:
                        menu:
                            'You unwrap the linen sheet and grab the willow wand, still as smooth as on the day you bought it. The pointy, carved twig is thin, but heavy from the injected quicksilver. You raise it as if you are about to stab the air with a dagger, then make a swipe.
                            \n\nThe invisible wave strikes the creature in the middle of its leap, making it let go of your boot. It rolls over the road, and your mount runs faster.
                            \n\nYour leg is free, the road is clear.
                            '
                            'We ride as fast as we can.' if pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We ride as fast as we can.')
                                jump encounter_fallentree_goblinsfinish
                            'I ride as fast as I can.' if not pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride as fast as I can.')
                                jump encounter_fallentree_goblinsfinish
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        menu:
                            'You unwrap the linen sheet and grab the willow wand, still as smooth as on the day you bought it. The pointy, carved twig is thin, but heavy from the injected quicksilver. You raise it as if you are about to stab the air with a dagger, then make a swipe.
                            \n\nThe invisible wave misses. It strikes your leg more than the creature, which, in its confusion, loses its balance, scratching the ground with its knees. Your foot hurts more and more, but the beast finally lets go, though your entire leg is in pain. The creature is lying on its stomach, and your mount runs faster.
                            \n\nYour leg is free, the road is clear.
                            '
                            'We ride as fast as we can.' if pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We ride as fast as we can.')
                                jump encounter_fallentree_goblinsfinish
                            'I ride as fast as I can.' if not pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride as fast as I can.')
                                jump encounter_fallentree_goblinsfinish
                'I have no pneuma left in my shell. [[Cost: [manacost]] (disabled)' ( condition= "at_unlock_spell == 1 and mana < manacost" ):
                    pass
                '{image=d6} I aim for the head.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I aim for the head.')
                    $ at_unlock_spell = 0
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    if not pc_food:
                        $ d100roll += 10
                    if pc_food == 3:
                        $ d100roll -= 10
                    if pc_food == 4:
                        $ d100roll -= 20
                    if armor == 4:
                        $ d100roll -= 5
                    if item_golemglove:
                        $ d100roll -= 10
                    if item_asterionspear or item_mountainroadspear:
                        $ d100roll -= 30
                    elif item_goblinspear or item_axe03:
                        $ d100roll -= 20
                    elif item_axe02 or item_axe02alt:
                        $ d100roll -= 10
                    if pc_class == "warrior":
                        $ d100roll -= (pc_battlecounter*2)
                    else:
                        $ d100roll -= (pc_battlecounter)
                    if d100roll < 60:
                        if item_asterionspear or item_mountainroadspear:
                            $ custom3 = "You hit it with the spear, not only piercing the beast’s skull, but also using the impact to push it out of your way. It rolls over the road, and your mount runs faster. Still riding, you shake the blood off the spearhead."
                        elif item_goblinspear:
                            $ custom3 = "You hit it with the pointed stick, not only piercing the beast’s skull, but also using the impact to push it out of your way. It rolls over the road, and your mount runs faster. The tip is covered with blood."
                            $ encounter_fallentree_goblins_bloodonspear = 1
                        else: # axe
                            $ custom3 = "A lucky swing of your axe hits its skull, not only crushing the bone, but also pushing it out of your way. It rolls over the road, and your mount runs faster. Still riding, you shake the blood off your blade."
                        menu:
                            '[custom3] Your leg is free, the road is clear.
                            '
                            'We ride as fast as we can.' if pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We ride as fast as we can.')
                                jump encounter_fallentree_goblinsfinish
                            'I ride as fast as I can.' if not pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride as fast as I can.')
                                jump encounter_fallentree_goblinsfinish
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        $ custom2 = ""
                        if item_asterionspear or item_mountainroadspear:
                            $ custom3 = "You scratched your thigh, though gently."
                            $ encounter_fallentree_goblins_dmg += 1
                        elif item_goblinspear:
                            $ custom3 = "You scratched your thigh, though gently."
                            $ encounter_fallentree_goblins_dmg += 1
                            $ encounter_fallentree_goblins_bloodonspear = 1
                        else: # axe
                            $ custom3 = "Thankfully, it was the blunt side, not the edge of your axe that hit your leg."
                        menu:
                            'It’s a difficult strike, and it lands on your own flesh. [custom3] The beast, however, gets scared. It lets go of the boot and leaps away, landing on its two hind limbs. It shouts after you, but stops its pursuit. Though it hurts, your leg is free, the road is clear.
                            '
                            'We ride as fast as we can.' if pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We ride as fast as we can.')
                                jump encounter_fallentree_goblinsfinish
                            'I ride as fast as I can.' if not pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride as fast as I can.')
                                jump encounter_fallentree_goblinsfinish
                '{image=d6} I kick it off.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I kick it off.')
                    $ at_unlock_spell = 0
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    if not pc_food:
                        $ d100roll += 10
                    if pc_food == 3:
                        $ d100roll -= 10
                    if pc_food == 4:
                        $ d100roll -= 20
                    if armor == 4:
                        $ d100roll -= 5
                    if pc_class == "warrior":
                        $ d100roll -= (pc_battlecounter*2)
                    else:
                        $ d100roll -= (pc_battlecounter)
                    if d100roll < (pc_hp*20):
                        menu:
                            'You swing your foot around, or at least you try, overwhelmed by the weight and muscles of the beast. You finally find the right moment just when the goblin lands on its paws. The precise hit between its eyes makes it roll over the road, and your mount runs faster. Your leg is free, the road is clear.
                            '
                            'We ride as fast as we can.' if pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We ride as fast as we can.')
                                jump encounter_fallentree_goblinsfinish
                            'I ride as fast as I can.' if not pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride as fast as I can.')
                                jump encounter_fallentree_goblinsfinish
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        $ encounter_fallentree_goblins_dmg += 1
                        $ custom2 = ""
                        menu:
                            'You swing your foot around, or at least you try, overwhelmed by the weight and muscles of the beast. Before you manage to land a hit, your leg is already in great pain. The beast, however, gets scared. It lets go of the boot and leaps away, landing on the two hind limbs. It shouts after you, but stops its pursuit. Though it hurts, your leg is free, the road is clear.
                            '
                            'We ride as fast as we can.' if pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We ride as fast as we can.')
                                jump encounter_fallentree_goblinsfinish
                            'I ride as fast as I can.' if not pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride as fast as I can.')
                                jump encounter_fallentree_goblinsfinish
                '{image=d6} I have to ride faster.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I have to ride faster.')
                    $ at_unlock_spell = 0
                    $ d100roll = 0
                    $ d100roll = renpy.random.randint(1, 100)
                    if d100roll < 50:
                        menu:
                            'You put your entire trust in your horse, trying to endure the pain in your ankle and focusing on the reins. {color=#f6d6bd}[horsename]{/color} does its best, and after your encouragement, it jumps, making the goblin lose its balance and roll over the road. Your leg hurts a bit, but it’s free, and the road is clear.
                            '
                            'We ride as fast as we can.' if pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We ride as fast as we can.')
                                jump encounter_fallentree_goblinsfinish
                            'I ride as fast as I can.' if not pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride as fast as I can.')
                                jump encounter_fallentree_goblinsfinish
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        menu:
                            'You put your entire trust in your horse, trying to endure the pain in your ankle and focusing on the reins. {color=#f6d6bd}[horsename]{/color} does its best, but your encouragement is not enough, and you underestimated how nimble the goblin can be. Even after your mount makes a long jump, the beast keeps up with it, making your leg hurt more and more. It takes over a minute before it gets too tired, or maybe just too scared, and it leaps away, landing on its hind limbs and shouting at you. Your leg is in pain, but it’s free, and the road is clear.
                            '
                            'We ride as fast as we can.' if pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- We ride as fast as we can.')
                                jump encounter_fallentree_goblinsfinish
                            'I ride as fast as I can.' if not pc_likeshorsename:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride as fast as I can.')
                                jump encounter_fallentree_goblinsfinish
                'I throw a fistful of blinding powder into its face.' if item_blindingpowder:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw a fistful of blinding powder into its face.')
                    $ at_unlock_spell = 0
                    menu:
                        'You unpack the pouch, trying to endure the pain in your ankle, and once you open it, you almost drop it on the ground, struggling to find the balance between grasping the dust and holding the reins. Once the small cloud hits the goblin’s face, it screeches loudly, and reaches to its face with its hands - which also means it lets go of your boot, and rolls over the road, covering its eyes in spasmodic movements. Your leg hurts a bit, but it’s free, and the road is clear.
                        '
                        'We ride as fast as we can.' if pc_likeshorsename:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- We ride as fast as we can.')
                            jump encounter_fallentree_goblinsfinish
                        'I ride as fast as I can.' if not pc_likeshorsename:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride as fast as I can.')
                            jump encounter_fallentree_goblinsfinish
                'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                    pass

    label encounter_fallentree_goblinsfinish:
        if item_goblinspear:
            menu:
                'For a few more moments you hear the angry shouts and screeches, but soon after that, it’s again only you and your mount. You realize that you still have the goblin spear, a primitive pointed stick which would be completely useless in most situations. There’s a light-blue scrap of linen tied to it, just beneath the pointed tip. You wonder why a monster would care about decorating their tool. Maybe it never bothered to get rid of it.
                '
                'I better attach it to my bundles.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better attach it to my bundles.')
                    $ at = 0
                    menu:
                        'The spear is light and you easily strap it along your mount’s side. It looks like a broom handle.
                        '
                        'Time to see what we’re going to find down the road.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to see what we’re going to find down the road.')
                            $ at_unlock_spell = 0
                            $ pc_battlecounter += 1
                            $ can_potions = 0
                            jump finaldestinationafterevent
                'I throw this piece of trash away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw this piece of trash away.')
                    $ item_goblinspear -= 1
                    $ renpy.notify("You lost the goblin spear.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the goblin spear.{/i}')
                    $ at = 0
                    menu:
                        'It lands among the bushes, hardly identifiable among all the leaves and branches.
                        '
                        'Time to see what we’re going to find down the road.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to see what we’re going to find down the road.')
                            $ at_unlock_spell = 0
                            $ pc_battlecounter += 1
                            $ can_potions = 0
                            jump finaldestinationafterevent
        else:
            $ at = 0
            menu:
                'For a few more moments, you hear the angry shouts and screeches, but soon after that, it’s again only you and your mount.
                '
                'Time to see what we’re going to find down the road.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to see what we’re going to find down the road.')
                    $ at_unlock_spell = 0
                    $ pc_battlecounter += 1
                    $ can_potions = 0
                    jump finaldestinationafterevent

############################################### spotted wolves
label spottedwolvesencountertonorth01: # from stonebridge to huntercabin
    $ encounter_spottedwolves = day
    show bridgetocabinsouth at basicfade
    $ quarters += tostonebridge
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    stop nature fadeout 2.0
    if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
        play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    menu:
        'The gentle road leads downhill, getting greener and less rocky the farther north you get. Just in case, your eyes run toward a few drier parts of the meadow, and you instantly shout at {color=#f6d6bd}[horsename]{/color} to make haste.
        \n\nA pack of short-haired wolves, at least twenty members strong, is chasing after you. Their coats are a mixture of yellow, black, and white spots, as if someone threw mud and paint at them. They move toward the road with a human-like speed, and you realize only some of them are running straight at you.
        '
        'They’re trying to cut through my path.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- They’re trying to cut through my path.')
            show bridgetocabinnorth at basicfade
            if huntercabin_firsttime:
                $ custom1 = "You ride past the wooden cabin, but the chase doesn’t stop yet."
            else:
                $ huntercabin_firsttime = 1
                $ custom1 = "You ride past a wooden cabin placed in the clearing at the bottom of a rock face, but you can’t stop while the pack is at your back."
            menu:
                'If it wasn’t for your palfrey, the beasts would have already caught up with you. Their trap was perfectly set up, not leaving you any path of escape. Your terrified mount is disciplined enough to stay on the beaten path, and even though one of the big-eared wolves almost sinks its teeth into your mount’s thigh, you manage to squeeze between the hunters.
                \n\nFor the next few minutes, you do your best to get further away, and while your gallop is indeed faster, the wolves easily shorten the distance by moving through the sparse forest. [custom1]
                '
                'Maybe I have something I could use here.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I have something I could use here.')
                    hide bridgetocabinsouth
                    hide bridgetocabinnorth
                    show cabintoforaginggroundsouth at basicfade
                    show cabintoforaginggroundmiddle at basicfade
                    $ quarters += 1
                    if pc_class == "mage":
                        $ at_unlock_spell = 1
                        $ at = 0
                        $ manacost = 3
                    menu:
                        'You think about your sacks and bundles, but the pack won’t wait for you to sort things out. The group gets larger the further you go, as even more of its members, previously hidden among the trees and grasses, now join the hunt, allowing their tired family members to slow down.
                        \n\nYou may be able to lose them after some time, but scaring or wounding some of them may force them to give up on their prey sooner.
                        '
                        'I’ll push away one of the beasts with pneuma. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll push away one of the beasts with pneuma.')
                            $ at_unlock_spell = 0
                            $ custom1 = "You reach for your wand and focus on channeling your strike, then push an invisible wave right at the wolf that’s closest to you, sending it flying. It hits a boulder with a painful cry, but as you get away, it still moves. Its concerned allies seem to be more confused than scared - only a few of them try to keep up, while many more stay behind and try to figure out what just happened, and if their pack member is safe."
                            $ encounter_spottedwolves_hp -= 2
                            $ mana = limit_mana(mana-manacost)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                            jump spottedwolvesencountertonorth01a
                        'I lack pneuma to cast a spell. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell and mana < manacost" ):
                            pass
                        'I reach for a spear.' if item_asterionspear or item_mountainroadspear:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for a spear.')
                            $ at_unlock_spell = 0
                            $ custom1 = "You grab the smooth shaft and lock your sights on the closest creature. Once it gets in range, you make a swift thrust, shedding the wolf’s blood as it lets out a painful cry. Its concerned allies howl with fear and anger. While a few of them try to keep up, many more stay behind and surround their pack member, protecting it from potential threats."
                            $ encounter_spottedwolves_hp -= 3
                            jump spottedwolvesencountertonorth01a
                        'An axe doesn’t have enough range to hit such a short animal. (disabled)' if not item_asterionspear and not item_mountainroadspear:
                            pass
                        'My crossbow is ready.' if item_crossbow and item_crossbowquarrels >= 1:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My crossbow is ready.')
                            $ at_unlock_spell = 0
                            $ custom1 = "You reach for the drawn crossbow and a bolt, then lock your sights on the closest creature. You wait until you learn it’s rhythm, then shoot once it’s in mid-air. The arrow flies through the wolf’s flesh, causing it to let out a pained cry and plunge to the ground. Its concerned allies howl with fear and anger. While a few of them try to keep up, many more stay behind and surround their pack member, protecting it from potential threats."
                            $ encounter_spottedwolves_hp -= 3
                            $ item_crossbowquarrels -= 1
                            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            jump spottedwolvesencountertonorth01a
                        'I don’t have any quarrels for my crossbow. (disabled)' if item_crossbow and item_crossbowquarrels <= 0:
                            pass
                        'I don’t have a crossbow. (disabled)' if not item_crossbow:
                            pass
                        'I reach for the blinding powder.' if item_blindingpowder:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for the blinding powder.')
                            $ at_unlock_spell = 0
                            $ custom1 = "You reach for the pouch and lock your sights on the closest creature. Once it gets in range, you throw a fistful of the mixture, making it run into the dangerous cloud without realizing. It instantly plunges into the ground, howling in panic, trying to run away. Its concerned allies seem to be more confused than scared - only a few of them try to keep up, while many more stay behind and try to figure out what just happened, and if their pack member is safe."
                            $ encounter_spottedwolves_hp -= 3
                            jump spottedwolvesencountertonorth01a
                        'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                            pass
                        # ' ' if item_bonehook and item_rope: # ropehook
                        #     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
                        #     $ at_unlock_spell = 0
                        #     $ custom1 = ""
                        #     $ encounter_spottedwolves_hp -= 1
                        #     jump spottedwolvesencountertonorth01a
                        'I have nothing to fight them off with.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have nothing to fight them off with.')
                            $ at_unlock_spell = 0
                            $ custom1 = "You focus on the road ahead, forcing your mount to speed up whenever a beast tries to catch it."
                            $ encounter_spottedwolves_hp -= 1
                            jump spottedwolvesencountertonorth01b

    label spottedwolvesencountertonorth01a:
        show cabintoforaginggroundnorth at basicfade
        $ quarters += 1
        $ cleanliness = limit_cleanliness(cleanliness-1)
        show minus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        if foragingground_firsttime:
            $ custom2 = ", and once again at the edge of the foraging ground."
        else:
            $ custom2 = ", this time at the edge of the hills."
        menu:
            '[custom1]
            \n\nAfter another few minutes, you are alone again[custom2] {color=#f6d6bd}[horsename]{/color} is tired, but patient, more happy to survive than it is angry at your wanderlust. At least you can hope the pack will move to a different place during the night.
            '
            'I let it rest for a bit and look around.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let it rest for a bit and look around.')
                $ quarters += 1
                scene empty
                scene layoutfull
                $ pc_area = "foragingground"
                if watchtower_firsttime and stonebridge_firsttime and huntercabin_firsttime and wanderer_firsttime and foggylake_firsttime:
                    $ NEcornerunlocked = 1
                #########TO SOUTHERN CROSSROADS
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                    $ tosoutherncrossroads = (SEcorner + FROMwatchtowerTOforaginggroundULT)
                elif wanderer_firsttime and foggylake_firsttime and NWcornerunlocked and SWcornerunlocked:
                    $ tosoutherncrossroads = (FROMfoggylakeTOforaginggroundULT + NWcorner + SWcorner)
                else:
                    $ tosoutherncrossroads = 100
                #########TO MILITARY CAMP
                $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
                #########TO WESTERN CROSSROADS
                if wanderer_firsttime and foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime and ford_firsttime:
                    $ towesterncrossroads = (FROMfoggylakeTOforaginggroundULT + NWcorner)
                elif huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime and beholder_firsttime and howlersdell_firsttime:
                    $ towesterncrossroads = (SEcorner + SWcorner + FROMwatchtowerTOforaginggroundULT)
                else:
                    $ towesterncrossroads = 100
                #########TO WEST GATE
                $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
                #########TO OLD PAGOS
                $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
                #########TO MONASTERY
                $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
                #########TO WATCHTOWER
                if huntercabin_firsttime and stonebridge_firsttime:
                    $ towatchtower = (FROMwatchtowerTOforaginggroundULT)
                elif SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                    $ towatchtower = (FROMfoggylakeTOstonebridgeULT + NWcorner + SWcorner + SEcorner)
                else:
                    $ towatchtower = 100
                #########TO EUDOCIA’S HOUSE
                $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
                #########TO STONE SIGN
                $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
                #########TO FOGGY LAKE
                if wanderer_firsttime:
                    $ tofoggylake = (FROMfoggylakeTOforaginggroundULT)
                elif huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime:
                    $ tofoggylake = (tosoutherncrossroads + SWcorner + NWcorner)
                else:
                    $ tofoggylake = 100
                #########TO CREEKS
                $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
                #########TO OLD TUNNEL
                $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
                #########TO GALE ROCKS
                $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
                #########TO BEACH
                $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
                #########TO PELT OF THE NORTH
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                    $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
                elif wanderer_firsttime and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
                    $ topeltnorth = (towesterncrossroads + FROMwesterncrossroadsTOpeltnorthULT)
                else:
                    $ topeltnorth = 100
                #########TO RUINED VILLAGE
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                    $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
                elif wanderer_firsttime and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime:
                    $ toruinedvillage = (towesterncrossroads + FROMwesterncrossroadsTOruinedvillageULT)
                else:
                    $ toruinedvillage = 100
                #########TO BEHOLDER
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime:
                    $ tobeholder = (tosoutherncrossroads + FROMsoutherncrossroadsTObeholderULT)
                elif wanderer_firsttime and NWcornerunlocked and howlersdell_firsttime:
                    $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
                else:
                    $ tobeholder = 100
                #########TO DRUID’S CAVE
                $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
                #########TO HOWLER’S DELL
                if wanderer_firsttime and NWcornerunlocked:
                    $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
                elif huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime and beholder_firsttime:
                    $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
                else:
                    $ tohowlersdell = 100
                #########TO ROCKSLIDE
                $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
                #########TO FISHING HAMLET
                $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
                #########TO DOLMEN
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and fallentree_firsttime:
                    $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
                elif SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                    $ todolmen = (tosoutherncrossroads + FROMsoutherncrossroadsTOdolmenULT)
                else:
                    $ todolmen = 100
                #########TO FALLEN TREE
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime:
                    $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
                elif dolmen_firsttime and SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                    $ tofallentree = (tosoutherncrossroads + FROMsoutherncrossroadsTOfallentreeULT)
                else:
                    $ tofallentree = 100
                #########TO STONE BRIDGE
                if huntercabin_firsttime:
                    $ tostonebridge = (FROMhuntercabinTOforagingground + FROMstonebridgeTOhuntercabin)
                elif wanderer_firsttime and foggylake_firsttime and NWcornerunlocked and SWcornerunlocked and SEcornerunlocked and watchtower_firsttime:
                    $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
                else:
                    $ tostonebridge = 100
                #########TO GHOUL CAVE
                $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
                #########TO GIANT STATUE
                $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
                #########TO MOUNTAIN ROAD
                $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
                #########TO TRIBE OF THE GREEN MOUNTAIN
                $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
                #########TO HUNTER’S CABIN
                $ tohuntercabin = (FROMhuntercabinTOforagingground)
                #########TO FORAGING GROUND
                $ toforagingground = 0
                #########TO WANDERER
                $ towanderer = FROMforaginggroundTOwanderer
                #########TO FORD
                if wanderer_firsttime and foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime:
                    $ toford = (tofoggylake + FROMfoggylakeTOfordULT)
                elif huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked:
                    $ toford = (towesterncrossroads + FROMwesterncrossroadsTOfordULT)
                else:
                    $ toford = 100
                #########TO BOG ENTRANCE
                if wanderer_firsttime and foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime:
                    $ tobogentrance = (tofoggylake + FROMfoggylakeTObogentranceULT)
                elif huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime:
                    $ tobogentrance = (towesterncrossroads + FROMwesterncrossroadsTObogentranceULT)
                else:
                    $ tobogentrance = 100
                #########TO BOG CROSSROADS
                $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
                #########TO BOG ROAD
                $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
                #########TO PEAT FIELD
                $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
                #########TO VINES
                $ tovines = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines)
                #########TO WHITE MARSHES
                $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
                #########TO RUINED SHELTER
                if wanderer_firsttime and foggylake_firsttime and northernroad_firsttime:
                    $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
                elif huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime:
                    $ toruinedshelter = (towesterncrossroads + FROMwesterncrossroadsTOruinedshelterULT)
                else:
                    $ toruinedshelter = 100
                #########TO NORTHERN ROAD
                if wanderer_firsttime and foggylake_firsttime:
                    $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
                elif huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime:
                    $ tonorthernroad = (towesterncrossroads + FROMwesterncrossroadsTOnorthernroadULT)
                else:
                    $ tonorthernroad = 100
                #########TO HOWLERS LAIR
                $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
                jump foragingground01

    label spottedwolvesencountertonorth01b:
        show cabintoforaginggroundnorth at basicfade
        $ quarters += 1
        if foragingground_firsttime:
            $ custom2 = "you return to the foraging ground"
        else:
            $ foragingground_firsttime = 1
            $ custom2 = "you leave the hills and enter the grasslands of a valley"
        menu:
            '[custom1] After another few minutes, [custom2], but the pack doesn’t give up on you yet. At least their numbers have stopped growing - you’re already outside of their territory, and the handful of spotted, colorful shells also seem tired, and are forced to stay on the beaten path.
            '
            'Without a palfrey, I would be dead already.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without a palfrey, I would be dead already.')
                hide cabintoforaginggroundsouth
                hide cabintoforaginggroundmiddle
                hide cabintoforaginggroundnorth
                show foraginggroundtowanderersouth at basicfade
                show foraginggroundtowanderermiddle at basicfade
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                menu:
                    'You get out of the valley and follow another narrow path through the hills and trees, clearly shaped by humans, at least in part. The leas and rocks start to blur into a vague memory, but after another few minutes, the howls stop. You don’t slow down just yet.
                    '
                    'Those were some stubborn wolves.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Those were some stubborn wolves.')
                        show foraginggroundtowanderernorth at basicfade
                        if wanderer_firsttime:
                            $ custom2 = "The familiar path leads to a small statue standing next to a willow."
                        else:
                            $ custom2 = "You reach a gentle, open path, seeing a lake to the west and hearing a gentle creek ahead of you."
                        menu:
                            '[custom2] {color=#f6d6bd}[horsename]{/color} is exhausted, but patient, more happy to survive than it is angry at your wanderlust. At least you can hope the pack will move to a different place during the night.
                            '
                            'I better get out of the saddle and let it rest for a bit before I move forward.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better get out of the saddle and let it rest for a bit before I move forward.')
                                $ quarters += 1
                                scene empty
                                scene layoutfull
                                $ pc_area = "wanderer"
                                if watchtower_firsttime and stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime and foggylake_firsttime:
                                    $ NEcornerunlocked = 1
                                #########TO FOGGY LAKE
                                $ tofoggylake = (FROMfoggylakeTOwandererULT)
                                #########TO SOUTHERN CROSSROADS
                                if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                                    $ tosoutherncrossroads = (SEcorner + FROMwatchtowerTOwandererULT)
                                elif foggylake_firsttime and NWcornerunlocked and SWcornerunlocked:
                                    $ tosoutherncrossroads = (tofoggylake + NWcorner + SWcorner)
                                else:
                                    $ tosoutherncrossroads = 100
                                #########TO CREEKS
                                $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
                                #########TO OLD TUNNEL
                                $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
                                #########TO GALE ROCKS
                                $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
                                #########TO BEACH
                                $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
                                #########TO MILITARY CAMP
                                $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
                                #########TO WESTERN CROSSROADS
                                if foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime and ford_firsttime:
                                    $ towesterncrossroads = (FROMfoggylakeTOwandererULT + NWcorner)
                                elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime and beholder_firsttime and howlersdell_firsttime:
                                    $ towesterncrossroads = (SEcorner + SWcorner + FROMwatchtowerTOwandererULT)
                                else:
                                    $ towesterncrossroads = 100
                                #########TO WEST GATE
                                $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
                                #########TO OLD PAGOS
                                $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
                                #########TO MONASTERY
                                $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
                                #########TO WATCHTOWER
                                if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime:
                                    $ towatchtower = (FROMwatchtowerTOwandererULT)
                                elif SWcornerunlocked and NWcornerunlocked and dolmen_firsttime and fallentree_firsttime:
                                    $ towatchtower = (FROMfoggylakeTOstonebridgeULT + NWcorner + SWcorner + SEcorner)
                                else:
                                    $ towatchtower = 100
                                #########TO EUDOCIA’S HOUSE
                                $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
                                #########TO STONE SIGN
                                $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
                                #########TO PELT OF THE NORTH
                                if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                                    $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
                                elif NWcornerunlocked and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
                                    $ topeltnorth = (towesterncrossroads + FROMwesterncrossroadsTOpeltnorthULT)
                                else:
                                    $ topeltnorth = 100
                                #########TO RUINED VILLAGE
                                if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                                    $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
                                elif NWcornerunlocked and howlersdell_firsttime and beholder_firsttime:
                                    $ toruinedvillage = (towesterncrossroads + FROMwesterncrossroadsTOruinedvillageULT)
                                else:
                                    $ toruinedvillage = 100
                                #########TO BEHOLDER
                                if NWcornerunlocked and howlersdell_firsttime:
                                    $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
                                elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime:
                                    $ tobeholder = (tosoutherncrossroads + FROMsoutherncrossroadsTObeholderULT)
                                else:
                                    $ tobeholder = 100
                                #########TO DRUID’S CAVE
                                $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
                                #########TO HOWLER’S DELL
                                if NWcornerunlocked:
                                    $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
                                elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime and beholder_firsttime:
                                    $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
                                else:
                                    $ tohowlersdell = 100
                                #########TO ROCKSLIDE
                                $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
                                #########TO FISHING HAMLET
                                $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
                                #########TO DOLMEN
                                if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and fallentree_firsttime:
                                    $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
                                elif SWcornerunlocked and NWcornerunlocked:
                                    $ todolmen = (tosoutherncrossroads + FROMsoutherncrossroadsTOdolmenULT)
                                else:
                                    $ todolmen = 100
                                #########TO FALLEN TREE
                                if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime:
                                    $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
                                elif dolmen_firsttime and SWcornerunlocked and NWcornerunlocked:
                                    $ tofallentree = (tosoutherncrossroads + FROMsoutherncrossroadsTOfallentreeULT)
                                else:
                                    $ tofallentree = 100
                                #########TO STONE BRIDGE
                                if foragingground_firsttime and huntercabin_firsttime:
                                    $ tostonebridge = (FROMforaginggroundTOwanderer + FROMhuntercabinTOforagingground + FROMstonebridgeTOhuntercabin)
                                elif foggylake_firsttime and NWcornerunlocked and SWcornerunlocked and SEcornerunlocked and watchtower_firsttime:
                                    $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
                                else:
                                    $ tostonebridge = 100
                                #########TO GHOUL CAVE
                                $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
                                #########TO GIANT STATUE
                                $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
                                #########TO MOUNTAIN ROAD
                                $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
                                #########TO TRIBE OF THE GREEN MOUNTAIN
                                $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
                                #########TO HUNTER’S CABIN
                                if foragingground_firsttime:
                                    $ tohuntercabin = (FROMforaginggroundTOwanderer + FROMhuntercabinTOforagingground)
                                elif stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and SWcornerunlocked and NWcornerunlocked:
                                    $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
                                else:
                                    $ tohuntercabin = 100
                                #########TO FORAGING GROUND
                                $ toforagingground = FROMforaginggroundTOwanderer
                                #########TO WANDERER
                                $ towanderer = 0
                                #########TO FORD
                                if foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime:
                                    $ toford = (tofoggylake + FROMfoggylakeTOfordULT)
                                elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked:
                                    $ toford = (towesterncrossroads + FROMwesterncrossroadsTOfordULT)
                                else:
                                    $ toford = 100
                                #########TO BOG ENTRANCE
                                if foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime:
                                    $ tobogentrance = (tofoggylake + FROMfoggylakeTObogentranceULT)
                                elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime:
                                    $ tobogentrance = (towesterncrossroads + FROMwesterncrossroadsTObogentranceULT)
                                else:
                                    $ tobogentrance = 100
                                #########TO BOG CROSSROADS
                                $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
                                #########TO BOG ROAD
                                $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
                                #########TO PEAT FIELD
                                $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
                                #########TO VINES
                                $ tovines = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines)
                                #########TO WHITE MARSHES
                                $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
                                #########TO RUINED SHELTER
                                if foggylake_firsttime and northernroad_firsttime:
                                    $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
                                elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime:
                                    $ toruinedshelter = (towesterncrossroads + FROMwesterncrossroadsTOruinedshelterULT)
                                else:
                                    $ toruinedshelter = 100
                                #########TO NORTHERN ROAD
                                if foggylake_firsttime:
                                    $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
                                elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime:
                                    $ tonorthernroad = (towesterncrossroads + FROMwesterncrossroadsTOnorthernroadULT)
                                else:
                                    $ tonorthernroad = 100
                                #########TO HOWLERS LAIR
                                $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
                                jump wanderer01

label spottedwolvesencountertosouth01: # from huntercabin to stonebridge
    $ encounter_spottedwolves = day
    show bridgetocabinnorth at basicfade
    $ quarters += tohuntercabin
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    stop nature fadeout 2.0
    if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
        play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    menu:
        'The gentle road leads uphill, getting more rocky and bright as the trees grow sparse. Just in case, your eyes run toward a few drier parts of the meadow, and you instantly shout at {color=#f6d6bd}[horsename]{/color} to make haste.
        \n\nA pack of short-haired wolves, at least twenty members strong, is chasing after you. Their coats are a mixture of yellow, black, and white spots, as if someone threw mud and paint at them. They move toward the road with a human-like speed, and you realize only some of them run straight at you.
        '
        'They’re trying to cut through my path.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- They’re trying to cut through my path.')
            show bridgetocabinsouth at basicfade
            if stonebridge_firsttime:
                $ custom1 = "You cross the bridge made of a stone slab, but the chase doesn’t stop yet."
            else:
                $ stonebridge_firsttime = 1
                $ custom1 = "You cross a weird river bridge made of a stone slab, but the chase doesn’t stop yet."
            menu:
                'If it wasn’t for your palfrey, the beast would have already caught up with you. Their trap was perfectly set up, not leaving you any path of escape. Your terrified mount is disciplined enough to stay on the beaten path, and even though one of the big-eared wolves almost sinks its teeth into your mount’s thigh, you manage to squeeze between the hunters.
                \n\nFor the next few minutes, you do your best to get further away, and while your gallop is indeed faster, the wolves easily shorten the distance by moving through the sparse forest. [custom1]
                '
                'Maybe I have something I could use here.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I have something I could use here.')
                    hide bridgetocabinnorth
                    hide bridgetocabinsouth
                    if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
                        show watchtowertostonebridgenorth_fixed at basicfade
                    else:
                        show watchtowertostonebridgenorth at basicfade
                    $ quarters += 1
                    if pc_class == "mage":
                        $ at_unlock_spell = 1
                        $ at = 0
                        $ manacost = 3
                    menu:
                        'You think about your sacks and bundles, but the pack won’t wait for you to sort through things. The group gets larger the further you go, as even more of its members, previously hidden among the rocks and grasses, now join the hunt, allowing their tired family members to slow down.
                        \n\nYou may be able to lose them after some time, but scaring or wounding some of them may force them to give up on their prey sooner.
                        '
                        'I’ll push away one of the beasts with pneuma. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll push away one of the beasts with pneuma.')
                            $ at_unlock_spell = 0
                            $ custom1 = "You reach for your wand and focus on channeling your strike, then push an invisible wave right at the wolf that’s closest to you, sending it flying. It hits a boulder with a painful cry, but as you get away, it still moves. Its concerned allies seem to be more confused than scared - only a few of them try to keep up, while many more stay behind and try to figure out what just happened, and if their pack member is safe."
                            $ encounter_spottedwolves_hp -= 2
                            $ mana = limit_mana(mana-manacost)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                            jump spottedwolvesencountertosouth01a
                        'I lack pneuma to cast a spell. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell and mana < manacost" ):
                            pass
                        'I reach for a spear.' if item_asterionspear or item_mountainroadspear:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for a spear.')
                            $ at_unlock_spell = 0
                            $ custom1 = "You grab the smooth shaft and lock your sights on the closest creature. Once it gets in range, you make a swift thrust, shedding the wolf’s blood as it lets out a painful cry. Its concerned allies howl with fear and anger. While a few of them try to keep up, many more stay behind and surround their pack member, protecting it from potential threats."
                            $ encounter_spottedwolves_hp -= 3
                            jump spottedwolvesencountertosouth01a
                        'An axe doesn’t have enough range to hit such a short animal. (disabled)' if not item_asterionspear and not item_mountainroadspear:
                            pass
                        'My crossbow is ready.' if item_crossbow and item_crossbowquarrels >= 1:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My crossbow is ready.')
                            $ at_unlock_spell = 0
                            $ custom1 = "You reach for the drawn crossbow and a bolt, then lock your sights on the closest creature. You wait until you learn it’s rhythm, then shoot once it’s in mid-air. The arrow flies through the wolf’s flesh, causing it to let out a pained cry and plunge to the ground. Its concerned allies howl with fear and anger. While a few of them try to keep up, many more stay behind and surround their pack member, protecting it from potential threats."
                            $ encounter_spottedwolves_hp -= 3
                            $ item_crossbowquarrels -= 1
                            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            jump spottedwolvesencountertosouth01a
                        'I don’t have any quarrels for my crossbow. (disabled)' if item_crossbow and item_crossbowquarrels <= 0:
                            pass
                        'I don’t have a crossbow. (disabled)' if not item_crossbow:
                            pass
                        'I reach for the blinding powder.' if item_blindingpowder:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for the blinding powder.')
                            $ at_unlock_spell = 0
                            $ custom1 = "You reach for the pouch and lock your sights on the closest creature. Once it gets in range, you throw a fistful of the mixture, making it run into the dangerous cloud without realizing. It instantly plunges into the ground, howling in panic, trying to run away. Its concerned allies seem to be more confused than scared - only a few of them try to keep up, while many more stay behind and try to figure out what just happened, and if their pack member is safe."
                            $ encounter_spottedwolves_hp -= 3
                            jump spottedwolvesencountertosouth01a
                        'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                            pass
                        # ' ' if item_bonehook and item_rope:
                        #     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
                        #     $ at_unlock_spell = 0
                        #     $ custom1 = ""
                        #     $ encounter_spottedwolves_hp -= 1
                        #     jump spottedwolvesencountertosouth01a
                        'I have nothing to fight them off with.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have nothing to fight them off with.')
                            $ at_unlock_spell = 0
                            $ custom1 = "You focus on the road ahead, forcing your mount to speed up whenever a beast tries to catch it."
                            $ encounter_spottedwolves_hp -= 1
                            jump spottedwolvesencountertosouth01b

    label spottedwolvesencountertosouth01a:
        if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            show watchtowertostonebridgesouth_fixed at basicfade
        else:
            show watchtowertostonebridgesouth at basicfade
        $ quarters += 1
        $ cleanliness = limit_cleanliness(cleanliness-1)
        show minus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        if watchtower_firsttime:
            $ custom2 = ", and once again at the foot of the watchtower."
        else:
            $ custom2 = ", this time on the crossroads at the foot of a watchtower."
        menu:
            '[custom1]
            \n\nAfter another few minutes, you are alone again[custom2] {color=#f6d6bd}[horsename]{/color} is tired, but patient, more happy to survive than it is angry at your wanderlust. At least you can hope the pack will move to a different place during the night.
            '
            'I let it rest for a bit and look around.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let it rest for a bit and look around.')
                $ quarters += 1
                scene empty
                scene layoutfull
                $ pc_area = "watchtower"
                if dolmen_firsttime and fallentree_firsttime:
                    $ SEcornerunlocked = 1
                if stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime and wanderer_firsttime and foggylake_firsttime:
                    $ NEcornerunlocked = 1
                #########TO SOUTHERN CROSSROADS
                if SEcornerunlocked:
                    $ tosoutherncrossroads = (SEcorner)
                elif NEcornerunlocked and NWcornerunlocked and SWcornerunlocked:
                    $ tosoutherncrossroads = (NEcorner + NWcorner + SWcorner)
                else:
                    $ tosoutherncrossroads = 100
                #########TO MILITARY CAMP
                $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
                #########TO WESTERN CROSSROADS
                if SEcornerunlocked and SWcornerunlocked:
                    $ towesterncrossroads = (SEcorner + SWcorner)
                elif NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime and ford_firsttime:
                    $ towesterncrossroads = (NEcorner + NWcorner)
                else:
                    $ towesterncrossroads = 100
                #########TO WEST GATE
                $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
                #########TO OLD PAGOS
                $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
                #########TO MONASTERY
                $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
                #########TO WATCHTOWER
                $ towatchtower = 0
                #########TO EUDOCIA’S HOUSE
                $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
                #########TO STONE SIGN
                $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
                #########TO FOGGY LAKE
                if NEcornerunlocked:
                    $ tofoggylake = (NEcorner)
                elif SEcornerunlocked and SWcornerunlocked and NWcornerunlocked:
                    $ tofoggylake = (SEcorner + SWcorner + NWcorner)
                else:
                    $ tofoggylake = 100
                #########TO CREEKS
                $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
                #########TO OLD TUNNEL
                $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
                #########TO GALE ROCKS
                $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
                #########TO BEACH
                $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
                #########TO PELT OF THE NORTH
                if SEcornerunlocked:
                    $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
                elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
                    $ topeltnorth = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOpeltnorthULT)
                else:
                    $ topeltnorth = 100
                #########TO RUINED VILLAGE
                if SEcornerunlocked:
                    $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
                elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime:
                    $ toruinedvillage = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOruinedvillageULT)
                else:
                    $ toruinedvillage = 100
                #########TO BEHOLDER
                if SEcornerunlocked and ruinedvillage_firsttime:
                    $ tobeholder = (tosoutherncrossroads + FROMsoutherncrossroadsTObeholderULT)
                elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime:
                    $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
                else:
                    $ tobeholder = 100
                #########TO DRUID’S CAVE
                $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
                #########TO HOWLER’S DELL
                if SEcornerunlocked and ruinedvillage_firsttime and beholder_firsttime:
                    $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
                elif NEcornerunlocked and NWcornerunlocked:
                    $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
                else:
                    $ tohowlersdell = 100
                #########TO ROCKSLIDE
                $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
                #########TO FISHING HAMLET
                $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
                #########TO DOLMEN
                if fallentree_firsttime:
                    $ todolmen = (FROMwatchtowerTOdolmenULT)
                elif tosoutherncrossroads < 100:
                    $ todolmen = (tosoutherncrossroads + FROMsoutherncrossroadsTOdolmenULT)
                else:
                    $ todolmen = 100
                #########TO FALLEN TREE
                $ tofallentree = (FROMwatchtowerTOfallentreeULT)
                #########TO STONE BRIDGE
                $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
                #########TO GHOUL CAVE
                $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
                #########TO GIANT STATUE
                $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
                #########TO MOUNTAIN ROAD
                $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
                #########TO TRIBE OF THE GREEN MOUNTAIN
                $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
                #########TO HUNTER’S CABIN
                if stonebridge_firsttime:
                    $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
                elif SEcornerunlocked and NWcornerunlocked and wanderer_firsttime and foragingground_firsttime:
                    $ tohuntercabin = (tofoggylake + FROMfoggylakeTOhuntercabinULT)
                else:
                    $ tohuntercabin = 100
                #########TO FORAGING GROUND
                if stonebridge_firsttime and huntercabin_firsttime:
                    $ toforagingground = (towatchtower + FROMwatchtowerTOforaginggroundULT)
                elif SEcornerunlocked and SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                    $ toforagingground = (tofoggylake + FROMfoggylakeTOforaginggroundULT)
                else:
                    $ toforagingground = 100
                #########TO WANDERER
                if stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime:
                    $ towanderer = (towatchtower + FROMwatchtowerTOwandererULT)
                elif SEcornerunlocked and SWcornerunlocked and foggylake_firsttime and NWcornerunlocked:
                    $ towanderer = (tofoggylake + FROMfoggylakeTOwandererULT)
                else:
                    $ towanderer = 100
                #########TO FORD
                if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime:
                    $ toford = (tofoggylake + FROMfoggylakeTOfordULT)
                elif SEcornerunlocked and SWcornerunlocked:
                    $ toford = (towesterncrossroads + FROMwesterncrossroadsTOfordULT)
                else:
                    $ toford = 100
                #########TO BOG ENTRANCE
                if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime:
                    $ tobogentrance = (tofoggylake + FROMfoggylakeTObogentranceULT)
                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime:
                    $ tobogentrance = (towesterncrossroads + FROMwesterncrossroadsTObogentranceULT)
                else:
                    $ tobogentrance = 100
                #########TO BOG CROSSROADS
                $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
                #########TO BOG ROAD
                $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
                #########TO PEAT FIELD
                $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
                #########TO VINES
                $ tovines = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines)
                #########TO WHITE MARSHES
                $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
                #########TO RUINED SHELTER
                if NEcornerunlocked and northernroad_firsttime:
                    $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime:
                    $ toruinedshelter = (towesterncrossroads + FROMwesterncrossroadsTOruinedshelterULT)
                else:
                    $ toruinedshelter = 100
                #########TO NORTHERN ROAD
                if NEcornerunlocked:
                    $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime:
                    $ tonorthernroad = (towesterncrossroads + FROMwesterncrossroadsTOnorthernroadULT)
                else:
                    $ tonorthernroad = 100
                #########TO HOWLERS LAIR
                $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
                jump watchtower01

    label spottedwolvesencountertosouth01b:
        if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            show watchtowertostonebridgesouth_fixed at basicfade
        else:
            show watchtowertostonebridgesouth at basicfade
        $ quarters += 1
        if watchtower_firsttime:
            $ custom2 = "you return to the watchtower"
        else:
            $ watchtower_firsttime = 1
            $ custom2 = "you reach the crossroads at the foot of a watchtower,"
        menu:
            '[custom1] After another few minutes, [custom2], but the pack doesn’t give up on you yet. At least their numbers have stopped growing - you’re already outside of their territory, and the handful of spotted, colorful shells also seem tired, and are forced to stay on the beaten path.
            \n\nThe gate cutting the road right next to the tower can’t be crossed in the saddle. You have to make a turn.
            '
            'I’m riding west.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m riding west.')
                hide watchtowertostonebridgenorth
                hide watchtowertostonebridgesouth
                if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
                    show stonesigntowatchtowereast_fixed at basicfade
                else:
                    show stonesigntowatchtowereast at basicfade
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                menu:
                    'The road here is much more neglected and overgrown by grasses. The leas and trees start to blur into a vague memory, but after another few minutes, the howls stop. You don’t slow down just yet.
                    '
                    'Those were some stubborn wolves.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Those were some stubborn wolves.')
                        if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
                            show stonesigntowatchtowerwest_fixed at basicfade
                        else:
                            show stonesigntowatchtowerwest at basicfade
                        if stonesign_firsttime:
                            $ custom2 = "The familiar path leads to the painted rock at the edge of the woodland."
                        else:
                            $ custom2 = "The farther west you get, the thicker the forest becomes."
                        menu:
                            '[custom2] {color=#f6d6bd}[horsename]{/color} Is exhausted, but patient, more happy to survive than it’s angry at your wanderlust. At least you can hope the pack will move to a different place during the night.
                            '
                            'I better get out of the saddle and let it rest for a bit before I move forward.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better get out of the saddle and let it rest for a bit before I move forward.')
                                scene empty
                                scene layoutfull
                                $ pc_area = "stonesign"
                                if dolmen_firsttime and fallentree_firsttime:
                                    $ SEcornerunlocked = 1
                                if watchtower_firsttime and stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime and wanderer_firsttime and foggylake_firsttime:
                                    $ NEcornerunlocked = 1
                                #########TO WATCHTOWER
                                $ towatchtower = FROMwatchtowerTOstonesign
                                #########TO SOUTHERN CROSSROADS
                                if SEcornerunlocked:
                                    $ tosoutherncrossroads = (towatchtower + SEcorner)
                                elif watchtower_firsttime and NEcornerunlocked and NWcornerunlocked and SWcornerunlocked:
                                    $ tosoutherncrossroads = (towatchtower + NEcorner + NWcorner + SWcorner)
                                else:
                                    $ tosoutherncrossroads = 100
                                #########TO MILITARY CAMP
                                $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
                                #########TO WESTERN CROSSROADS
                                if SEcornerunlocked and SWcornerunlocked:
                                    $ towesterncrossroads = (towatchtower + SEcorner + SWcorner)
                                elif watchtower_firsttime and NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime and ford_firsttime:
                                    $ towesterncrossroads = (towatchtower + NEcorner + NWcorner)
                                else:
                                    $ towesterncrossroads = 100
                                #########TO WEST GATE
                                $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
                                #########TO OLD PAGOS
                                $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
                                #########TO MONASTERY
                                $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
                                #########TO EUDOCIA’S HOUSE
                                $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
                                #########TO STONE SIGN
                                $ tostonesign = 0
                                #########TO FOGGY LAKE
                                if stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime and wanderer_firsttime:
                                    $ tofoggylake = (towatchtower + NEcorner)
                                elif SEcornerunlocked and SWcornerunlocked and NWcornerunlocked:
                                    $ tofoggylake = (tosoutherncrossroads + SWcorner + NWcorner)
                                else:
                                    $ tofoggylake = 100
                                #########TO CREEKS
                                $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
                                #########TO OLD TUNNEL
                                $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
                                #########TO GALE ROCKS
                                $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
                                #########TO BEACH
                                $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
                                #########TO PELT OF THE NORTH
                                if SEcornerunlocked:
                                    $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
                                elif watchtower_firsttime and NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
                                    $ topeltnorth = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOpeltnorthULT)
                                else:
                                    $ topeltnorth = 100
                                #########TO RUINED VILLAGE
                                if SEcornerunlocked:
                                    $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
                                elif watchtower_firsttime and NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime:
                                    $ toruinedvillage = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOruinedvillageULT)
                                else:
                                    $ toruinedvillage = 100
                                #########TO BEHOLDER
                                if watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime:
                                    $ tobeholder = (tosoutherncrossroads + FROMsoutherncrossroadsTObeholderULT)
                                elif watchtower_firsttime and NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime:
                                    $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
                                else:
                                    $ tobeholder = 100
                                #########TO DRUID’S CAVE
                                $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
                                #########TO HOWLER’S DELL
                                if watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime and beholder_firsttime:
                                    $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
                                elif watchtower_firsttime and NEcornerunlocked and NWcornerunlocked:
                                    $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
                                else:
                                    $ tohowlersdell = 100
                                #########TO ROCKSLIDE
                                $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
                                #########TO FISHING HAMLET
                                $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
                                #########TO DOLMEN
                                if watchtower_firsttime and fallentree_firsttime:
                                    $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
                                else:
                                    $ todolmen = 100
                                #########TO FALLEN TREE
                                if watchtower_firsttime:
                                    $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
                                else:
                                    $ tofallentree = 100
                                #########TO STONE BRIDGE
                                if watchtower_firsttime:
                                    $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
                                else:
                                    $ tostonebridge = 100
                                #########TO GHOUL CAVE
                                $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
                                #########TO GIANT STATUE
                                $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
                                #########TO MOUNTAIN ROAD
                                $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
                                #########TO TRIBE OF THE GREEN MOUNTAIN
                                $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
                                #########TO HUNTER’S CABIN
                                if watchtower_firsttime and stonebridge_firsttime:
                                    $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
                                elif watchtower_firsttime and SEcornerunlocked and NWcornerunlocked and wanderer_firsttime and foragingground_firsttime:
                                    $ tohuntercabin = (tofoggylake + FROMfoggylakeTOhuntercabinULT)
                                else:
                                    $ tohuntercabin = 100
                                #########TO FORAGING GROUND
                                if watchtower_firsttime and stonebridge_firsttime and huntercabin_firsttime:
                                    $ toforagingground = (towatchtower + FROMwatchtowerTOforaginggroundULT)
                                elif watchtower_firsttime and SEcornerunlocked and SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                                    $ toforagingground = (tofoggylake + FROMfoggylakeTOforaginggroundULT)
                                else:
                                    $ toforagingground = 100
                                #########TO WANDERER
                                if watchtower_firsttime and stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime:
                                    $ towanderer = (towatchtower + FROMwatchtowerTOwandererULT)
                                elif watchtower_firsttime and SEcornerunlocked and SWcornerunlocked and foggylake_firsttime and NWcornerunlocked:
                                    $ towanderer = (tofoggylake + FROMfoggylakeTOwandererULT)
                                else:
                                    $ towanderer = 100
                                #########TO FORD
                                if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime:
                                    $ toford = (tofoggylake + FROMfoggylakeTOfordULT)
                                elif SEcornerunlocked and SWcornerunlocked:
                                    $ toford = (towesterncrossroads + FROMwesterncrossroadsTOfordULT)
                                else:
                                    $ toford = 100
                                #########TO BOG ENTRANCE
                                if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime:
                                    $ tobogentrance = (tofoggylake + FROMfoggylakeTObogentranceULT)
                                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime:
                                    $ tobogentrance = (towesterncrossroads + FROMwesterncrossroadsTObogentranceULT)
                                else:
                                    $ tobogentrance = 100
                                #########TO BOG CROSSROADS
                                $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
                                #########TO BOG ROAD
                                $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
                                #########TO PEAT FIELD
                                $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
                                #########TO VINES
                                $ tovines = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines)
                                #########TO WHITE MARSHES
                                $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
                                #########TO RUINED SHELTER
                                if NEcornerunlocked and northernroad_firsttime:
                                    $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
                                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime:
                                    $ toruinedshelter = (towesterncrossroads + FROMwesterncrossroadsTOruinedshelterULT)
                                else:
                                    $ toruinedshelter = 100
                                #########TO NORTHERN ROAD
                                if NEcornerunlocked:
                                    $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
                                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime:
                                    $ tonorthernroad = (towesterncrossroads + FROMwesterncrossroadsTOnorthernroadULT)
                                else:
                                    $ tonorthernroad = 100
                                #########TO HOWLERS LAIR
                                $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
                                jump stonesign01
            'I’m riding east.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m riding east.')
                hide watchtowertostonebridgenorth
                hide watchtowertostonebridgesouth
                if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
                    show watchtowertoeudociawest_fixed at basicfade
                else:
                    show watchtowertoeudociawest at basicfade
                $ quarters += 1
                menu:
                    'The road is in great condition, the forest in the south is lush, despite the steep rock face that divides it in half. You barely recognize any shapes in the entanglement of grays, browns, and greens, but after another few minutes, the howls stop. You don’t slow down just yet.
                    '
                    'Those were some stubborn wolves.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Those were some stubborn wolves.')
                        if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
                            show watchtowertoeudociaeast_fixed at basicfade
                        else:
                            show watchtowertoeudociaeast at basicfade
                        if eudocia_firsttime:
                            $ custom2 = "The familiar path leads to the secluded residence. "
                        else:
                            $ custom2 = "The northern landscape is just a meadow, which then morphs into barren hills and mountains, barely covered by the grasses and bushes. No horse could travel through such a barrier. Maybe the riding ibexes of the clanspeople from The Growing Mountains would manage.\n\n"
                        menu:
                            '[custom2]{color=#f6d6bd}[horsename]{/color} is exhausted, but patient, more happy to survive than it is angry at your wanderlust. At least you can hope the pack will move to a different place during the night.
                            '
                            'I better get out of the saddle and let it rest for a bit before I move forward.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better get out of the saddle and let it rest for a bit before I move forward.')
                                $ quarters += 1
                                scene empty
                                scene layoutfull
                                $ pc_area = "eudociahouse"
                                #########TO WATCHTOWER
                                $ towatchtower = (FROMwatchtowerTOeudociahouseULT)
                                #########TO SOUTHERN CROSSROADS
                                if SEcornerunlocked:
                                    $ tosoutherncrossroads = (towatchtower + SEcorner)
                                elif NEcornerunlocked and NWcornerunlocked and SWcornerunlocked:
                                    $ tosoutherncrossroads = (towatchtower + NEcorner + NWcorner + SWcorner)
                                else:
                                    $ tosoutherncrossroads = 100
                                #########TO MILITARY CAMP
                                $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
                                #########TO WESTERN CROSSROADS
                                if SEcornerunlocked and SWcornerunlocked:
                                    $ towesterncrossroads = (towatchtower + SEcorner + SWcorner)
                                elif NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime and ford_firsttime:
                                    $ towesterncrossroads = (towatchtower + NEcorner + NWcorner)
                                else:
                                    $ towesterncrossroads = 100
                                #########TO WEST GATE
                                $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
                                #########TO OLD PAGOS
                                $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
                                #########TO MONASTERY
                                $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
                                #########TO EUDOCIA’S HOUSE
                                $ toeudociahouse = 0
                                #########TO STONE SIGN
                                $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
                                #########TO FOGGY LAKE
                                if stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime and wanderer_firsttime:
                                    $ tofoggylake = (towatchtower + NEcorner)
                                elif SEcornerunlocked and SWcornerunlocked and NWcornerunlocked:
                                    $ tofoggylake = (tosoutherncrossroads + SWcorner + NWcorner)
                                else:
                                    $ tofoggylake = 100
                                #########TO CREEKS
                                $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
                                #########TO OLD TUNNEL
                                $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
                                #########TO GALE ROCKS
                                $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
                                #########TO BEACH
                                $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
                                #########TO PELT OF THE NORTH
                                if SEcornerunlocked:
                                    $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
                                elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
                                    $ topeltnorth = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOpeltnorthULT)
                                else:
                                    $ topeltnorth = 100
                                #########TO RUINED VILLAGE
                                if SEcornerunlocked:
                                    $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
                                elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime:
                                    $ toruinedvillage = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOruinedvillageULT)
                                else:
                                    $ toruinedvillage = 100
                                #########TO BEHOLDER
                                if SEcornerunlocked and ruinedvillage_firsttime:
                                    $ tobeholder = (tosoutherncrossroads + FROMsoutherncrossroadsTObeholderULT)
                                elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime:
                                    $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
                                else:
                                    $ tobeholder = 100
                                #########TO DRUID’S CAVE
                                $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
                                #########TO HOWLER’S DELL
                                if SEcornerunlocked and ruinedvillage_firsttime and beholder_firsttime:
                                    $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
                                elif NEcornerunlocked and NWcornerunlocked:
                                    $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
                                else:
                                    $ tohowlersdell = 100
                                #########TO ROCKSLIDE
                                $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
                                #########TO FISHING HAMLET
                                $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
                                #########TO DOLMEN
                                if watchtower_firsttime and fallentree_firsttime:
                                    $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
                                else:
                                    $ todolmen = 100
                                #########TO FALLEN TREE
                                $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
                                #########TO STONE BRIDGE
                                $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
                                #########TO GHOUL CAVE
                                $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
                                #########TO GIANT STATUE
                                $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
                                #########TO MOUNTAIN ROAD
                                $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
                                #########TO TRIBE OF THE GREEN MOUNTAIN
                                $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
                                #########TO HUNTER’S CABIN
                                if stonebridge_firsttime:
                                    $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
                                elif SEcornerunlocked and NWcornerunlocked and wanderer_firsttime and foragingground_firsttime:
                                    $ tohuntercabin = (tofoggylake + FROMfoggylakeTOhuntercabinULT)
                                else:
                                    $ tohuntercabin = 100
                                #########TO FORAGING GROUND
                                if stonebridge_firsttime and huntercabin_firsttime:
                                    $ toforagingground = (towatchtower + FROMwatchtowerTOforaginggroundULT)
                                elif SEcornerunlocked and SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                                    $ toforagingground = (tofoggylake + FROMfoggylakeTOforaginggroundULT)
                                else:
                                    $ toforagingground = 100
                                #########TO WANDERER
                                if stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime:
                                    $ towanderer = (towatchtower + FROMwatchtowerTOwandererULT)
                                elif SEcornerunlocked and SWcornerunlocked and foggylake_firsttime and NWcornerunlocked:
                                    $ towanderer = (tofoggylake + FROMfoggylakeTOwandererULT)
                                else:
                                    $ towanderer = 100
                                #########TO FORD
                                if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime:
                                    $ toford = (tofoggylake + FROMfoggylakeTOfordULT)
                                elif SEcornerunlocked and SWcornerunlocked:
                                    $ toford = (towesterncrossroads + FROMwesterncrossroadsTOfordULT)
                                else:
                                    $ toford = 100
                                #########TO BOG ENTRANCE
                                if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime:
                                    $ tobogentrance = (tofoggylake + FROMfoggylakeTObogentranceULT)
                                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime:
                                    $ tobogentrance = (towesterncrossroads + FROMwesterncrossroadsTObogentranceULT)
                                else:
                                    $ tobogentrance = 100
                                #########TO BOG CROSSROADS
                                $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
                                #########TO BOG ROAD
                                $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
                                #########TO PEAT FIELD
                                $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
                                #########TO VINES
                                $ tovines = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines)
                                #########TO WHITE MARSHES
                                $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
                                #########TO RUINED SHELTER
                                if NEcornerunlocked and northernroad_firsttime:
                                    $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
                                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime:
                                    $ toruinedshelter = (towesterncrossroads + FROMwesterncrossroadsTOruinedshelterULT)
                                else:
                                    $ toruinedshelter = 100
                                #########TO NORTHERN ROAD
                                if NEcornerunlocked:
                                    $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
                                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime:
                                    $ tonorthernroad = (towesterncrossroads + FROMwesterncrossroadsTOnorthernroadULT)
                                else:
                                    $ tonorthernroad = 100
                                #########TO HOWLERS LAIR
                                $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
                                jump eudociahouse01

label spottedwolvesencountertonorth02:
    show areapicture bridgetocabin at basicfade
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ quarters += tostonebridge
    $ quarters += 1
    $ encounter_spottedwolves = day
    stop nature fadeout 2.0
    if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
        play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if pc_class == "mage":
        $ at_unlock_spell = 1
        $ at = 0
        $ manacost = 3
    menu:
        'The familiar howls make you sigh. The spotted wolves dash out of the meadows, starting their chase anew.
        \n\nSeems like they return here every now and then. You look for anything that could teach them a lesson.
        '
        'I’ll push away one of the beasts with pneuma. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll push away one of the beasts with pneuma.')
            $ at_unlock_spell = 0
            $ custom1 = "You reach for your wand and focus on channeling your strike, then push an invisible wave right at the wolf that’s closest to you, sending it flying. It hits a boulder with a painful cry, but as you get away, it still moves. Its concerned allies seem to be more confused than scared - only a few of them try to keep up, while many more stay behind and try to figure out what just happened, and if their pack member is safe."
            $ encounter_spottedwolves_hp -= 2
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
            jump spottedwolvesencountertonorth02a
        'I lack pneuma to cast a spell. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell and mana < manacost" ):
            pass
        'I reach for a spear.' if item_asterionspear or item_mountainroadspear:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for a spear.')
            $ at_unlock_spell = 0
            $ custom1 = "You grab the smooth shaft and lock your sights on the closest creature. Once it gets in range, you make a swift thrust, shedding the wolf’s blood as it lets out a painful cry. Its concerned allies howl with fear and anger. While a few of them try to keep up, many more stay behind and surround their pack member, protecting it from potential threats."
            $ encounter_spottedwolves_hp -= 3
            jump spottedwolvesencountertonorth02a
        'An axe doesn’t have enough range to hit such a short animal. (disabled)' if not item_asterionspear and not item_mountainroadspear:
            pass
        'My crossbow is ready.' if item_crossbow and item_crossbowquarrels >= 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My crossbow is ready.')
            $ at_unlock_spell = 0
            $ custom1 = "You reach for the drawn crossbow and a bolt, then lock your sights on the closest creature. You wait until you learn it’s rhythm, then shoot once it’s in mid-air. The arrow flies through the wolf’s flesh, causing it to let out a pained cry and plunge to the ground. Its concerned allies howl with fear and anger. While a few of them try to keep up, many more stay behind and surround their pack member, protecting it from potential threats."
            $ encounter_spottedwolves_hp -= 3
            $ item_crossbowquarrels -= 1
            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
            jump spottedwolvesencountertonorth02a
        'I don’t have any quarrels for my crossbow. (disabled)' if item_crossbow and item_crossbowquarrels <= 0:
            pass
        'I don’t have a crossbow. (disabled)' if not item_crossbow:
            pass
        'I reach for the blinding powder.' if item_blindingpowder:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for the blinding powder.')
            $ at_unlock_spell = 0
            $ custom1 = "You reach for the pouch and lock your sights on the closest creature. Once it gets in range, you throw a fistful of the mixture, making it run into the dangerous cloud without realizing. It instantly plunges into the ground, howling in panic, trying to run away. Its concerned allies seem to be more confused than scared - only a few of them try to keep up, while many more stay behind and try to figure out what just happened, and if their pack member is safe."
            $ encounter_spottedwolves_hp -= 3
            jump spottedwolvesencountertonorth02a
        'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
            pass
        'I have nothing to fight them off with.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have nothing to fight them off with.')
            $ at_unlock_spell = 0
            $ custom1 = "You focus on the road ahead, forcing your mount to speed up whenever a beast tries to catch it."
            $ encounter_spottedwolves_hp -= 1
            jump spottedwolvesencountertonorth02b

    label spottedwolvesencountertonorth02a:
        show areapicture cabintoforagingground at basicfade
        $ quarters += 1
        $ cleanliness = limit_cleanliness(cleanliness-1)
        show minus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        menu:
            '[custom1]
            \n\nAfter another few minutes, you are alone again, this time at the foraging grounds.
            '
            'Let’s hope the pack will now move to a different spot, at least for a few days.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the pack will now move to a different spot, at least for a few days.')
                $ quarters += 1
                scene empty
                scene layoutfull
                $ pc_area = "foragingground"
                if watchtower_firsttime and stonebridge_firsttime and huntercabin_firsttime and wanderer_firsttime and foggylake_firsttime:
                    $ NEcornerunlocked = 1
                #########TO SOUTHERN CROSSROADS
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                    $ tosoutherncrossroads = (SEcorner + FROMwatchtowerTOforaginggroundULT)
                elif wanderer_firsttime and foggylake_firsttime and NWcornerunlocked and SWcornerunlocked:
                    $ tosoutherncrossroads = (FROMfoggylakeTOforaginggroundULT + NWcorner + SWcorner)
                else:
                    $ tosoutherncrossroads = 100
                #########TO MILITARY CAMP
                $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
                #########TO WESTERN CROSSROADS
                if wanderer_firsttime and foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime and ford_firsttime:
                    $ towesterncrossroads = (FROMfoggylakeTOforaginggroundULT + NWcorner)
                elif huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime and beholder_firsttime and howlersdell_firsttime:
                    $ towesterncrossroads = (SEcorner + SWcorner + FROMwatchtowerTOforaginggroundULT)
                else:
                    $ towesterncrossroads = 100
                #########TO WEST GATE
                $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
                #########TO OLD PAGOS
                $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
                #########TO MONASTERY
                $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
                #########TO WATCHTOWER
                if huntercabin_firsttime and stonebridge_firsttime:
                    $ towatchtower = (FROMwatchtowerTOforaginggroundULT)
                elif SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                    $ towatchtower = (FROMfoggylakeTOstonebridgeULT + NWcorner + SWcorner + SEcorner)
                else:
                    $ towatchtower = 100
                #########TO EUDOCIA’S HOUSE
                $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
                #########TO STONE SIGN
                $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
                #########TO FOGGY LAKE
                if wanderer_firsttime:
                    $ tofoggylake = (FROMfoggylakeTOforaginggroundULT)
                elif huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime:
                    $ tofoggylake = (tosoutherncrossroads + SWcorner + NWcorner)
                else:
                    $ tofoggylake = 100
                #########TO CREEKS
                $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
                #########TO OLD TUNNEL
                $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
                #########TO GALE ROCKS
                $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
                #########TO BEACH
                $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
                #########TO PELT OF THE NORTH
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                    $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
                elif wanderer_firsttime and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
                    $ topeltnorth = (towesterncrossroads + FROMwesterncrossroadsTOpeltnorthULT)
                else:
                    $ topeltnorth = 100
                #########TO RUINED VILLAGE
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                    $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
                elif wanderer_firsttime and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime:
                    $ toruinedvillage = (towesterncrossroads + FROMwesterncrossroadsTOruinedvillageULT)
                else:
                    $ toruinedvillage = 100
                #########TO BEHOLDER
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime:
                    $ tobeholder = (tosoutherncrossroads + FROMsoutherncrossroadsTObeholderULT)
                elif wanderer_firsttime and NWcornerunlocked and howlersdell_firsttime:
                    $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
                else:
                    $ tobeholder = 100
                #########TO DRUID’S CAVE
                $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
                #########TO HOWLER’S DELL
                if wanderer_firsttime and NWcornerunlocked:
                    $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
                elif huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime and beholder_firsttime:
                    $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
                else:
                    $ tohowlersdell = 100
                #########TO ROCKSLIDE
                $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
                #########TO FISHING HAMLET
                $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
                #########TO DOLMEN
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and fallentree_firsttime:
                    $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
                elif SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                    $ todolmen = (tosoutherncrossroads + FROMsoutherncrossroadsTOdolmenULT)
                else:
                    $ todolmen = 100
                #########TO FALLEN TREE
                if huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime:
                    $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
                elif dolmen_firsttime and SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                    $ tofallentree = (tosoutherncrossroads + FROMsoutherncrossroadsTOfallentreeULT)
                else:
                    $ tofallentree = 100
                #########TO STONE BRIDGE
                if huntercabin_firsttime:
                    $ tostonebridge = (FROMhuntercabinTOforagingground + FROMstonebridgeTOhuntercabin)
                elif wanderer_firsttime and foggylake_firsttime and NWcornerunlocked and SWcornerunlocked and SEcornerunlocked and watchtower_firsttime:
                    $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
                else:
                    $ tostonebridge = 100
                #########TO GHOUL CAVE
                $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
                #########TO GIANT STATUE
                $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
                #########TO MOUNTAIN ROAD
                $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
                #########TO TRIBE OF THE GREEN MOUNTAIN
                $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
                #########TO HUNTER’S CABIN
                $ tohuntercabin = (FROMhuntercabinTOforagingground)
                #########TO FORAGING GROUND
                $ toforagingground = 0
                #########TO WANDERER
                $ towanderer = FROMforaginggroundTOwanderer
                #########TO FORD
                if wanderer_firsttime and foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime:
                    $ toford = (tofoggylake + FROMfoggylakeTOfordULT)
                elif huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked:
                    $ toford = (towesterncrossroads + FROMwesterncrossroadsTOfordULT)
                else:
                    $ toford = 100
                #########TO BOG ENTRANCE
                if wanderer_firsttime and foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime:
                    $ tobogentrance = (tofoggylake + FROMfoggylakeTObogentranceULT)
                elif huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime:
                    $ tobogentrance = (towesterncrossroads + FROMwesterncrossroadsTObogentranceULT)
                else:
                    $ tobogentrance = 100
                #########TO BOG CROSSROADS
                $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
                #########TO BOG ROAD
                $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
                #########TO PEAT FIELD
                $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
                #########TO VINES
                $ tovines = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines)
                #########TO WHITE MARSHES
                $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
                #########TO RUINED SHELTER
                if wanderer_firsttime and foggylake_firsttime and northernroad_firsttime:
                    $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
                elif huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime:
                    $ toruinedshelter = (towesterncrossroads + FROMwesterncrossroadsTOruinedshelterULT)
                else:
                    $ toruinedshelter = 100
                #########TO NORTHERN ROAD
                if wanderer_firsttime and foggylake_firsttime:
                    $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
                elif huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime:
                    $ tonorthernroad = (towesterncrossroads + FROMwesterncrossroadsTOnorthernroadULT)
                else:
                    $ tonorthernroad = 100
                #########TO HOWLERS LAIR
                $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
                jump foragingground01

    label spottedwolvesencountertonorth02b:
        show areapicture cabintoforagingground at basicfade
        $ quarters += 1
        if foragingground_firsttime:
            $ custom2 = "you return to the foraging ground"
        else:
            $ foragingground_firsttime = 1
            $ custom2 = "you leave the hills and enter the grasslands of a valley"
        menu:
            '[custom1] After another few minutes, [custom2], but the pack doesn’t give up on you yet. At least their numbers have stopped growing - you’re already outside of their territory, and the handful of spotted, colorful shells also seem tired, and are forced to stay on the beaten path.
            '
            'Without a palfrey, I would be dead already.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without a palfrey, I would be dead already.')
                show areapicture foraginggroundtowanderer at basicfade
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                if wanderer_firsttime:
                    $ custom2 = "The familiar path leads to a small statue standing next to a willow."
                else:
                    $ custom2 = "You reach a gentle, open path, seeing a lake to the west and hearing a gentle creek ahead of you."
                menu:
                    '[custom2]
                    '
                    'Let’s hope the pack will now move to a different spot, at least for a few days.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the pack will now move to a different spot, at least for a few days.')
                        $ quarters += 2
                        scene empty
                        scene layoutfull
                        $ pc_area = "wanderer"
                        if watchtower_firsttime and stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime and foggylake_firsttime:
                            $ NEcornerunlocked = 1
                        #########TO FOGGY LAKE
                        $ tofoggylake = (FROMfoggylakeTOwandererULT)
                        #########TO SOUTHERN CROSSROADS
                        if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                            $ tosoutherncrossroads = (SEcorner + FROMwatchtowerTOwandererULT)
                        elif foggylake_firsttime and NWcornerunlocked and SWcornerunlocked:
                            $ tosoutherncrossroads = (tofoggylake + NWcorner + SWcorner)
                        else:
                            $ tosoutherncrossroads = 100
                        #########TO CREEKS
                        $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
                        #########TO OLD TUNNEL
                        $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
                        #########TO GALE ROCKS
                        $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
                        #########TO BEACH
                        $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
                        #########TO MILITARY CAMP
                        $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
                        #########TO WESTERN CROSSROADS
                        if foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime and ford_firsttime:
                            $ towesterncrossroads = (FROMfoggylakeTOwandererULT + NWcorner)
                        elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime and beholder_firsttime and howlersdell_firsttime:
                            $ towesterncrossroads = (SEcorner + SWcorner + FROMwatchtowerTOwandererULT)
                        else:
                            $ towesterncrossroads = 100
                        #########TO WEST GATE
                        $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
                        #########TO OLD PAGOS
                        $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
                        #########TO MONASTERY
                        $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
                        #########TO WATCHTOWER
                        if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime:
                            $ towatchtower = (FROMwatchtowerTOwandererULT)
                        elif SWcornerunlocked and NWcornerunlocked and dolmen_firsttime and fallentree_firsttime:
                            $ towatchtower = (FROMfoggylakeTOstonebridgeULT + NWcorner + SWcorner + SEcorner)
                        else:
                            $ towatchtower = 100
                        #########TO EUDOCIA’S HOUSE
                        $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
                        #########TO STONE SIGN
                        $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
                        #########TO PELT OF THE NORTH
                        if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                            $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
                        elif NWcornerunlocked and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
                            $ topeltnorth = (towesterncrossroads + FROMwesterncrossroadsTOpeltnorthULT)
                        else:
                            $ topeltnorth = 100
                        #########TO RUINED VILLAGE
                        if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked:
                            $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
                        elif NWcornerunlocked and howlersdell_firsttime and beholder_firsttime:
                            $ toruinedvillage = (towesterncrossroads + FROMwesterncrossroadsTOruinedvillageULT)
                        else:
                            $ toruinedvillage = 100
                        #########TO BEHOLDER
                        if NWcornerunlocked and howlersdell_firsttime:
                            $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
                        elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime:
                            $ tobeholder = (tosoutherncrossroads + FROMsoutherncrossroadsTObeholderULT)
                        else:
                            $ tobeholder = 100
                        #########TO DRUID’S CAVE
                        $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
                        #########TO HOWLER’S DELL
                        if NWcornerunlocked:
                            $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
                        elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime and beholder_firsttime:
                            $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
                        else:
                            $ tohowlersdell = 100
                        #########TO ROCKSLIDE
                        $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
                        #########TO FISHING HAMLET
                        $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
                        #########TO DOLMEN
                        if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime and fallentree_firsttime:
                            $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
                        elif SWcornerunlocked and NWcornerunlocked:
                            $ todolmen = (tosoutherncrossroads + FROMsoutherncrossroadsTOdolmenULT)
                        else:
                            $ todolmen = 100
                        #########TO FALLEN TREE
                        if foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and watchtower_firsttime:
                            $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
                        elif dolmen_firsttime and SWcornerunlocked and NWcornerunlocked:
                            $ tofallentree = (tosoutherncrossroads + FROMsoutherncrossroadsTOfallentreeULT)
                        else:
                            $ tofallentree = 100
                        #########TO STONE BRIDGE
                        if foragingground_firsttime and huntercabin_firsttime:
                            $ tostonebridge = (FROMforaginggroundTOwanderer + FROMhuntercabinTOforagingground + FROMstonebridgeTOhuntercabin)
                        elif foggylake_firsttime and NWcornerunlocked and SWcornerunlocked and SEcornerunlocked and watchtower_firsttime:
                            $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
                        else:
                            $ tostonebridge = 100
                        #########TO GHOUL CAVE
                        $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
                        #########TO GIANT STATUE
                        $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
                        #########TO MOUNTAIN ROAD
                        $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
                        #########TO TRIBE OF THE GREEN MOUNTAIN
                        $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
                        #########TO HUNTER’S CABIN
                        if foragingground_firsttime:
                            $ tohuntercabin = (FROMforaginggroundTOwanderer + FROMhuntercabinTOforagingground)
                        elif stonebridge_firsttime and watchtower_firsttime and SEcornerunlocked and SWcornerunlocked and NWcornerunlocked:
                            $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
                        else:
                            $ tohuntercabin = 100
                        #########TO FORAGING GROUND
                        $ toforagingground = FROMforaginggroundTOwanderer
                        #########TO WANDERER
                        $ towanderer = 0
                        #########TO FORD
                        if foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime:
                            $ toford = (tofoggylake + FROMfoggylakeTOfordULT)
                        elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked:
                            $ toford = (towesterncrossroads + FROMwesterncrossroadsTOfordULT)
                        else:
                            $ toford = 100
                        #########TO BOG ENTRANCE
                        if foggylake_firsttime and northernroad_firsttime and ruinedshelter_firsttime:
                            $ tobogentrance = (tofoggylake + FROMfoggylakeTObogentranceULT)
                        elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime:
                            $ tobogentrance = (towesterncrossroads + FROMwesterncrossroadsTObogentranceULT)
                        else:
                            $ tobogentrance = 100
                        #########TO BOG CROSSROADS
                        $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
                        #########TO BOG ROAD
                        $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
                        #########TO PEAT FIELD
                        $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
                        #########TO VINES
                        $ tovines = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines)
                        #########TO WHITE MARSHES
                        $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
                        #########TO RUINED SHELTER
                        if foggylake_firsttime and northernroad_firsttime:
                            $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
                        elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime:
                            $ toruinedshelter = (towesterncrossroads + FROMwesterncrossroadsTOruinedshelterULT)
                        else:
                            $ toruinedshelter = 100
                        #########TO NORTHERN ROAD
                        if foggylake_firsttime:
                            $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
                        elif foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime and SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime:
                            $ tonorthernroad = (towesterncrossroads + FROMwesterncrossroadsTOnorthernroadULT)
                        else:
                            $ tonorthernroad = 100
                        #########TO HOWLERS LAIR
                        $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
                        jump wanderer01

label spottedwolvesencountertosouth02:
    $ encounter_spottedwolves = day
    show areapicture bridgetocabin at basicfade
    $ quarters += tohuntercabin
    $ quarters += 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    stop nature fadeout 2.0
    if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
        play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if pc_class == "mage":
        $ at_unlock_spell = 1
        $ at = 0
        $ manacost = 3
    menu:
        'The familiar howls make you sigh. The spotted wolves dash out of the meadows, starting their chase anew.
        \n\nSeems like they return here every now and then. You look for anything that could teach them a lesson.
        '
        'I’ll push away one of the beasts with pneuma. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll push away one of the beasts with pneuma.')
            $ at_unlock_spell = 0
            $ custom1 = "You reach for your wand and focus on channeling your strike, then push an invisible wave right at the wolf that’s closest to you, sending it flying. It hits a boulder with a painful cry, but as you get away, it still moves. Its concerned allies seem to be more confused than scared - only a few of them try to keep up, while many more stay behind and try to figure out what just happened, and if their pack member is safe."
            $ encounter_spottedwolves_hp -= 2
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
            jump spottedwolvesencountertosouth02a
        'I lack pneuma to cast a spell. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell and mana < manacost" ):
            pass
        'I reach for a spear.' if item_asterionspear or item_mountainroadspear:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for a spear.')
            $ at_unlock_spell = 0
            $ custom1 = "You grab the smooth shaft and lock your sights on the closest creature. Once it gets in range, you make a swift thrust, shedding the wolf’s blood as it lets out a painful cry. Its concerned allies howl with fear and anger. While a few of them try to keep up, many more stay behind and surround their pack member, protecting it from potential threats."
            $ encounter_spottedwolves_hp -= 3
            jump spottedwolvesencountertosouth02a
        'An axe doesn’t have enough range to hit such a short animal. (disabled)' if not item_asterionspear and not item_mountainroadspear:
            pass
        'My crossbow is ready.' if item_crossbow and item_crossbowquarrels >= 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My crossbow is ready.')
            $ at_unlock_spell = 0
            $ custom1 = "You reach for the drawn crossbow and a bolt, then lock your sights on the closest creature. You wait until you learn it’s rhythm, then shoot once it’s in mid-air. The arrow flies through the wolf’s flesh, causing it to let out a pained cry and plunge to the ground. Its concerned allies howl with fear and anger. While a few of them try to keep up, many more stay behind and surround their pack member, protecting it from potential threats."
            $ encounter_spottedwolves_hp -= 3
            $ item_crossbowquarrels -= 1
            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
            jump spottedwolvesencountertosouth02a
        'I don’t have any quarrels for my crossbow. (disabled)' if item_crossbow and item_crossbowquarrels <= 0:
            pass
        'I don’t have a crossbow. (disabled)' if not item_crossbow:
            pass
        'I reach for the blinding powder.' if item_blindingpowder:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for the blinding powder.')
            $ at_unlock_spell = 0
            $ custom1 = "You reach for the pouch and lock your sights on the closest creature. Once it gets in range, you throw a fistful of the mixture, making it run into the dangerous cloud without realizing. It instantly plunges into the ground, howling in panic, trying to run away. Its concerned allies seem to be more confused than scared - only a few of them try to keep up, while many more stay behind and try to figure out what just happened, and if their pack member is safe."
            $ encounter_spottedwolves_hp -= 3
            jump spottedwolvesencountertosouth02a
        'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
            pass
        'I have nothing to fight them off with.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have nothing to fight them off with.')
            $ at_unlock_spell = 0
            $ custom1 = "You focus on the road ahead, forcing your mount to speed up whenever a beast tries to catch it."
            $ encounter_spottedwolves_hp -= 1
            jump spottedwolvesencountertosouth02b

    label spottedwolvesencountertosouth02a:
        if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            show areapicture watchtowertostonebridge_fixed at basicfade
        else:
            show areapicture watchtowertostonebridge at basicfade
        $ quarters += 1
        $ cleanliness = limit_cleanliness(cleanliness-1)
        show minus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        menu:
            '[custom1]
            \n\nAfter another few minutes, you are alone again, this time on the crossroads at the foot of a watchtower.
            '
            'Let’s hope the pack will now move to a different spot, at least for a few days.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the pack will now move to a different spot, at least for a few days.')
                $ quarters += 1
                scene empty
                scene layoutfull
                $ pc_area = "watchtower"
                if dolmen_firsttime and fallentree_firsttime:
                    $ SEcornerunlocked = 1
                if stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime and wanderer_firsttime and foggylake_firsttime:
                    $ NEcornerunlocked = 1
                #########TO SOUTHERN CROSSROADS
                if SEcornerunlocked:
                    $ tosoutherncrossroads = (SEcorner)
                elif NEcornerunlocked and NWcornerunlocked and SWcornerunlocked:
                    $ tosoutherncrossroads = (NEcorner + NWcorner + SWcorner)
                else:
                    $ tosoutherncrossroads = 100
                #########TO MILITARY CAMP
                $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
                #########TO WESTERN CROSSROADS
                if SEcornerunlocked and SWcornerunlocked:
                    $ towesterncrossroads = (SEcorner + SWcorner)
                elif NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime and ford_firsttime:
                    $ towesterncrossroads = (NEcorner + NWcorner)
                else:
                    $ towesterncrossroads = 100
                #########TO WEST GATE
                $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
                #########TO OLD PAGOS
                $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
                #########TO MONASTERY
                $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
                #########TO WATCHTOWER
                $ towatchtower = 0
                #########TO EUDOCIA’S HOUSE
                $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
                #########TO STONE SIGN
                $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
                #########TO FOGGY LAKE
                if NEcornerunlocked:
                    $ tofoggylake = (NEcorner)
                elif SEcornerunlocked and SWcornerunlocked and NWcornerunlocked:
                    $ tofoggylake = (SEcorner + SWcorner + NWcorner)
                else:
                    $ tofoggylake = 100
                #########TO CREEKS
                $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
                #########TO OLD TUNNEL
                $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
                #########TO GALE ROCKS
                $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
                #########TO BEACH
                $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
                #########TO PELT OF THE NORTH
                if SEcornerunlocked:
                    $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
                elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
                    $ topeltnorth = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOpeltnorthULT)
                else:
                    $ topeltnorth = 100
                #########TO RUINED VILLAGE
                if SEcornerunlocked:
                    $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
                elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime:
                    $ toruinedvillage = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOruinedvillageULT)
                else:
                    $ toruinedvillage = 100
                #########TO BEHOLDER
                if SEcornerunlocked and ruinedvillage_firsttime:
                    $ tobeholder = (tosoutherncrossroads + FROMsoutherncrossroadsTObeholderULT)
                elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime:
                    $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
                else:
                    $ tobeholder = 100
                #########TO DRUID’S CAVE
                $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
                #########TO HOWLER’S DELL
                if SEcornerunlocked and ruinedvillage_firsttime and beholder_firsttime:
                    $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
                elif NEcornerunlocked and NWcornerunlocked:
                    $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
                else:
                    $ tohowlersdell = 100
                #########TO ROCKSLIDE
                $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
                #########TO FISHING HAMLET
                $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
                #########TO DOLMEN
                if fallentree_firsttime:
                    $ todolmen = (FROMwatchtowerTOdolmenULT)
                elif tosoutherncrossroads < 100:
                    $ todolmen = (tosoutherncrossroads + FROMsoutherncrossroadsTOdolmenULT)
                else:
                    $ todolmen = 100
                #########TO FALLEN TREE
                $ tofallentree = (FROMwatchtowerTOfallentreeULT)
                #########TO STONE BRIDGE
                $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
                #########TO GHOUL CAVE
                $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
                #########TO GIANT STATUE
                $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
                #########TO MOUNTAIN ROAD
                $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
                #########TO TRIBE OF THE GREEN MOUNTAIN
                $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
                #########TO HUNTER’S CABIN
                if stonebridge_firsttime:
                    $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
                elif SEcornerunlocked and NWcornerunlocked and wanderer_firsttime and foragingground_firsttime:
                    $ tohuntercabin = (tofoggylake + FROMfoggylakeTOhuntercabinULT)
                else:
                    $ tohuntercabin = 100
                #########TO FORAGING GROUND
                if stonebridge_firsttime and huntercabin_firsttime:
                    $ toforagingground = (towatchtower + FROMwatchtowerTOforaginggroundULT)
                elif SEcornerunlocked and SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                    $ toforagingground = (tofoggylake + FROMfoggylakeTOforaginggroundULT)
                else:
                    $ toforagingground = 100
                #########TO WANDERER
                if stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime:
                    $ towanderer = (towatchtower + FROMwatchtowerTOwandererULT)
                elif SEcornerunlocked and SWcornerunlocked and foggylake_firsttime and NWcornerunlocked:
                    $ towanderer = (tofoggylake + FROMfoggylakeTOwandererULT)
                else:
                    $ towanderer = 100
                #########TO FORD
                if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime:
                    $ toford = (tofoggylake + FROMfoggylakeTOfordULT)
                elif SEcornerunlocked and SWcornerunlocked:
                    $ toford = (towesterncrossroads + FROMwesterncrossroadsTOfordULT)
                else:
                    $ toford = 100
                #########TO BOG ENTRANCE
                if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime:
                    $ tobogentrance = (tofoggylake + FROMfoggylakeTObogentranceULT)
                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime:
                    $ tobogentrance = (towesterncrossroads + FROMwesterncrossroadsTObogentranceULT)
                else:
                    $ tobogentrance = 100
                #########TO BOG CROSSROADS
                $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
                #########TO BOG ROAD
                $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
                #########TO PEAT FIELD
                $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
                #########TO VINES
                $ tovines = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines)
                #########TO WHITE MARSHES
                $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
                #########TO RUINED SHELTER
                if NEcornerunlocked and northernroad_firsttime:
                    $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime:
                    $ toruinedshelter = (towesterncrossroads + FROMwesterncrossroadsTOruinedshelterULT)
                else:
                    $ toruinedshelter = 100
                #########TO NORTHERN ROAD
                if NEcornerunlocked:
                    $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
                elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime:
                    $ tonorthernroad = (towesterncrossroads + FROMwesterncrossroadsTOnorthernroadULT)
                else:
                    $ tonorthernroad = 100
                #########TO HOWLERS LAIR
                $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
                jump watchtower01

    label spottedwolvesencountertosouth02b:
        if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            show areapicture watchtowertostonebridge_fixed at basicfade
        else:
            show areapicture watchtowertostonebridge at basicfade
        $ quarters += 1
        menu:
            '[custom1] After another few minutes, you reach the crossroads, but the pack doesn’t give up on you yet. At least their numbers have stopped growing - you’re already outside of their territory, and the handful of spotted, colorful shells also seem tired, and are forced to stay on the beaten path.
            \n\nThe gate next to the watchtower blocks your path forward.
            '
            'I’m riding west.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m riding west.')
                if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
                    show areapicture stonesigntowatchtower_fixed at basicfade
                else:
                    show areapicture stonesigntowatchtower at basicfade
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                if stonesign_firsttime:
                    $ custom2 = "The familiar path leads to the painted rock at the edge of the woodland."
                else:
                    $ custom2 = "The farther west you get, the thicker the forest becomes."
                menu:
                    '[custom2]
                    '
                    'Let’s hope the pack will now move to a different spot, at least for a few days.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the pack will now move to a different spot, at least for a few days.')
                        scene empty
                        scene layoutfull
                        $ quarters += 1
                        $ pc_area = "stonesign"
                        if dolmen_firsttime and fallentree_firsttime:
                            $ SEcornerunlocked = 1
                        if watchtower_firsttime and stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime and wanderer_firsttime and foggylake_firsttime:
                            $ NEcornerunlocked = 1
                        #########TO WATCHTOWER
                        $ towatchtower = FROMwatchtowerTOstonesign
                        #########TO SOUTHERN CROSSROADS
                        if SEcornerunlocked:
                            $ tosoutherncrossroads = (towatchtower + SEcorner)
                        elif watchtower_firsttime and NEcornerunlocked and NWcornerunlocked and SWcornerunlocked:
                            $ tosoutherncrossroads = (towatchtower + NEcorner + NWcorner + SWcorner)
                        else:
                            $ tosoutherncrossroads = 100
                        #########TO MILITARY CAMP
                        $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
                        #########TO WESTERN CROSSROADS
                        if SEcornerunlocked and SWcornerunlocked:
                            $ towesterncrossroads = (towatchtower + SEcorner + SWcorner)
                        elif watchtower_firsttime and NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime and ford_firsttime:
                            $ towesterncrossroads = (towatchtower + NEcorner + NWcorner)
                        else:
                            $ towesterncrossroads = 100
                        #########TO WEST GATE
                        $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
                        #########TO OLD PAGOS
                        $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
                        #########TO MONASTERY
                        $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
                        #########TO EUDOCIA’S HOUSE
                        $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
                        #########TO STONE SIGN
                        $ tostonesign = 0
                        #########TO FOGGY LAKE
                        if stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime and wanderer_firsttime:
                            $ tofoggylake = (towatchtower + NEcorner)
                        elif SEcornerunlocked and SWcornerunlocked and NWcornerunlocked:
                            $ tofoggylake = (tosoutherncrossroads + SWcorner + NWcorner)
                        else:
                            $ tofoggylake = 100
                        #########TO CREEKS
                        $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
                        #########TO OLD TUNNEL
                        $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
                        #########TO GALE ROCKS
                        $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
                        #########TO BEACH
                        $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
                        #########TO PELT OF THE NORTH
                        if SEcornerunlocked:
                            $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
                        elif watchtower_firsttime and NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
                            $ topeltnorth = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOpeltnorthULT)
                        else:
                            $ topeltnorth = 100
                        #########TO RUINED VILLAGE
                        if SEcornerunlocked:
                            $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
                        elif watchtower_firsttime and NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime:
                            $ toruinedvillage = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOruinedvillageULT)
                        else:
                            $ toruinedvillage = 100
                        #########TO BEHOLDER
                        if watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime:
                            $ tobeholder = (tosoutherncrossroads + FROMsoutherncrossroadsTObeholderULT)
                        elif watchtower_firsttime and NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime:
                            $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
                        else:
                            $ tobeholder = 100
                        #########TO DRUID’S CAVE
                        $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
                        #########TO HOWLER’S DELL
                        if watchtower_firsttime and SEcornerunlocked and ruinedvillage_firsttime and beholder_firsttime:
                            $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
                        elif watchtower_firsttime and NEcornerunlocked and NWcornerunlocked:
                            $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
                        else:
                            $ tohowlersdell = 100
                        #########TO ROCKSLIDE
                        $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
                        #########TO FISHING HAMLET
                        $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
                        #########TO DOLMEN
                        if watchtower_firsttime and fallentree_firsttime:
                            $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
                        else:
                            $ todolmen = 100
                        #########TO FALLEN TREE
                        if watchtower_firsttime:
                            $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
                        else:
                            $ tofallentree = 100
                        #########TO STONE BRIDGE
                        if watchtower_firsttime:
                            $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
                        else:
                            $ tostonebridge = 100
                        #########TO GHOUL CAVE
                        $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
                        #########TO GIANT STATUE
                        $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
                        #########TO MOUNTAIN ROAD
                        $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
                        #########TO TRIBE OF THE GREEN MOUNTAIN
                        $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
                        #########TO HUNTER’S CABIN
                        if watchtower_firsttime and stonebridge_firsttime:
                            $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
                        elif watchtower_firsttime and SEcornerunlocked and NWcornerunlocked and wanderer_firsttime and foragingground_firsttime:
                            $ tohuntercabin = (tofoggylake + FROMfoggylakeTOhuntercabinULT)
                        else:
                            $ tohuntercabin = 100
                        #########TO FORAGING GROUND
                        if watchtower_firsttime and stonebridge_firsttime and huntercabin_firsttime:
                            $ toforagingground = (towatchtower + FROMwatchtowerTOforaginggroundULT)
                        elif watchtower_firsttime and SEcornerunlocked and SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                            $ toforagingground = (tofoggylake + FROMfoggylakeTOforaginggroundULT)
                        else:
                            $ toforagingground = 100
                        #########TO WANDERER
                        if watchtower_firsttime and stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime:
                            $ towanderer = (towatchtower + FROMwatchtowerTOwandererULT)
                        elif watchtower_firsttime and SEcornerunlocked and SWcornerunlocked and foggylake_firsttime and NWcornerunlocked:
                            $ towanderer = (tofoggylake + FROMfoggylakeTOwandererULT)
                        else:
                            $ towanderer = 100
                        #########TO FORD
                        if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime:
                            $ toford = (tofoggylake + FROMfoggylakeTOfordULT)
                        elif SEcornerunlocked and SWcornerunlocked:
                            $ toford = (towesterncrossroads + FROMwesterncrossroadsTOfordULT)
                        else:
                            $ toford = 100
                        #########TO BOG ENTRANCE
                        if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime:
                            $ tobogentrance = (tofoggylake + FROMfoggylakeTObogentranceULT)
                        elif SEcornerunlocked and SWcornerunlocked and ford_firsttime:
                            $ tobogentrance = (towesterncrossroads + FROMwesterncrossroadsTObogentranceULT)
                        else:
                            $ tobogentrance = 100
                        #########TO BOG CROSSROADS
                        $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
                        #########TO BOG ROAD
                        $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
                        #########TO PEAT FIELD
                        $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
                        #########TO VINES
                        $ tovines = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines)
                        #########TO WHITE MARSHES
                        $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
                        #########TO RUINED SHELTER
                        if NEcornerunlocked and northernroad_firsttime:
                            $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
                        elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime:
                            $ toruinedshelter = (towesterncrossroads + FROMwesterncrossroadsTOruinedshelterULT)
                        else:
                            $ toruinedshelter = 100
                        #########TO NORTHERN ROAD
                        if NEcornerunlocked:
                            $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
                        elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime:
                            $ tonorthernroad = (towesterncrossroads + FROMwesterncrossroadsTOnorthernroadULT)
                        else:
                            $ tonorthernroad = 100
                        #########TO HOWLERS LAIR
                        $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
                        jump stonesign01
            'I’m riding east.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m riding east.')
                if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
                    show areapicture watchtowertoeudocia_fixed at basicfade
                else:
                    show areapicture watchtowertoeudocia at basicfade
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                if eudocia_firsttime:
                    $ custom2 = "The familiar path leads to the secluded residence. "
                else:
                    $ custom2 = "The forest in the south is lush, despite the steep rock face that divides it in half. You barely recognize any shapes in the entanglement of grays, browns, and greens. The northern landscape is just a meadow, which then morphs into barren hills and mountains, barely covered by the grasses and bushes. No horse could travel through such a barrier. Maybe the riding ibexes of the clanspeople from The Growing Mountains would manage."
                menu:
                    '[custom2]
                    '
                    'Let’s hope the pack will now move to a different spot, at least for a few days.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope the pack will now move to a different spot, at least for a few days.')
                        $ quarters += 2
                        scene empty
                        scene layoutfull
                        $ pc_area = "eudociahouse"
                        #########TO WATCHTOWER
                        $ towatchtower = (FROMwatchtowerTOeudociahouseULT)
                        #########TO SOUTHERN CROSSROADS
                        if SEcornerunlocked:
                            $ tosoutherncrossroads = (towatchtower + SEcorner)
                        elif NEcornerunlocked and NWcornerunlocked and SWcornerunlocked:
                            $ tosoutherncrossroads = (towatchtower + NEcorner + NWcorner + SWcorner)
                        else:
                            $ tosoutherncrossroads = 100
                        #########TO MILITARY CAMP
                        $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
                        #########TO WESTERN CROSSROADS
                        if SEcornerunlocked and SWcornerunlocked:
                            $ towesterncrossroads = (towatchtower + SEcorner + SWcorner)
                        elif NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime and ford_firsttime:
                            $ towesterncrossroads = (towatchtower + NEcorner + NWcorner)
                        else:
                            $ towesterncrossroads = 100
                        #########TO WEST GATE
                        $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
                        #########TO OLD PAGOS
                        $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
                        #########TO MONASTERY
                        $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
                        #########TO EUDOCIA’S HOUSE
                        $ toeudociahouse = 0
                        #########TO STONE SIGN
                        $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
                        #########TO FOGGY LAKE
                        if stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime and wanderer_firsttime:
                            $ tofoggylake = (towatchtower + NEcorner)
                        elif SEcornerunlocked and SWcornerunlocked and NWcornerunlocked:
                            $ tofoggylake = (tosoutherncrossroads + SWcorner + NWcorner)
                        else:
                            $ tofoggylake = 100
                        #########TO CREEKS
                        $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
                        #########TO OLD TUNNEL
                        $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
                        #########TO GALE ROCKS
                        $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
                        #########TO BEACH
                        $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
                        #########TO PELT OF THE NORTH
                        if SEcornerunlocked:
                            $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
                        elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
                            $ topeltnorth = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOpeltnorthULT)
                        else:
                            $ topeltnorth = 100
                        #########TO RUINED VILLAGE
                        if SEcornerunlocked:
                            $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
                        elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime and beholder_firsttime:
                            $ toruinedvillage = (towatchtower + NWcorner + NEcorner + FROMwesterncrossroadsTOruinedvillageULT)
                        else:
                            $ toruinedvillage = 100
                        #########TO BEHOLDER
                        if SEcornerunlocked and ruinedvillage_firsttime:
                            $ tobeholder = (tosoutherncrossroads + FROMsoutherncrossroadsTObeholderULT)
                        elif NEcornerunlocked and NWcornerunlocked and howlersdell_firsttime:
                            $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
                        else:
                            $ tobeholder = 100
                        #########TO DRUID’S CAVE
                        $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
                        #########TO HOWLER’S DELL
                        if SEcornerunlocked and ruinedvillage_firsttime and beholder_firsttime:
                            $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
                        elif NEcornerunlocked and NWcornerunlocked:
                            $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
                        else:
                            $ tohowlersdell = 100
                        #########TO ROCKSLIDE
                        $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
                        #########TO FISHING HAMLET
                        $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
                        #########TO DOLMEN
                        if watchtower_firsttime and fallentree_firsttime:
                            $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
                        else:
                            $ todolmen = 100
                        #########TO FALLEN TREE
                        $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
                        #########TO STONE BRIDGE
                        $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
                        #########TO GHOUL CAVE
                        $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
                        #########TO GIANT STATUE
                        $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
                        #########TO MOUNTAIN ROAD
                        $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
                        #########TO TRIBE OF THE GREEN MOUNTAIN
                        $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
                        #########TO HUNTER’S CABIN
                        if stonebridge_firsttime:
                            $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
                        elif SEcornerunlocked and NWcornerunlocked and wanderer_firsttime and foragingground_firsttime:
                            $ tohuntercabin = (tofoggylake + FROMfoggylakeTOhuntercabinULT)
                        else:
                            $ tohuntercabin = 100
                        #########TO FORAGING GROUND
                        if stonebridge_firsttime and huntercabin_firsttime:
                            $ toforagingground = (towatchtower + FROMwatchtowerTOforaginggroundULT)
                        elif SEcornerunlocked and SWcornerunlocked and NWcornerunlocked and wanderer_firsttime:
                            $ toforagingground = (tofoggylake + FROMfoggylakeTOforaginggroundULT)
                        else:
                            $ toforagingground = 100
                        #########TO WANDERER
                        if stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime:
                            $ towanderer = (towatchtower + FROMwatchtowerTOwandererULT)
                        elif SEcornerunlocked and SWcornerunlocked and foggylake_firsttime and NWcornerunlocked:
                            $ towanderer = (tofoggylake + FROMfoggylakeTOwandererULT)
                        else:
                            $ towanderer = 100
                        #########TO FORD
                        if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime and bogentrance_firsttime:
                            $ toford = (tofoggylake + FROMfoggylakeTOfordULT)
                        elif SEcornerunlocked and SWcornerunlocked:
                            $ toford = (towesterncrossroads + FROMwesterncrossroadsTOfordULT)
                        else:
                            $ toford = 100
                        #########TO BOG ENTRANCE
                        if NEcornerunlocked and northernroad_firsttime and ruinedshelter_firsttime:
                            $ tobogentrance = (tofoggylake + FROMfoggylakeTObogentranceULT)
                        elif SEcornerunlocked and SWcornerunlocked and ford_firsttime:
                            $ tobogentrance = (towesterncrossroads + FROMwesterncrossroadsTObogentranceULT)
                        else:
                            $ tobogentrance = 100
                        #########TO BOG CROSSROADS
                        $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
                        #########TO BOG ROAD
                        $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
                        #########TO PEAT FIELD
                        $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
                        #########TO VINES
                        $ tovines = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines)
                        #########TO WHITE MARSHES
                        $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
                        #########TO RUINED SHELTER
                        if NEcornerunlocked and northernroad_firsttime:
                            $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
                        elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime:
                            $ toruinedshelter = (towesterncrossroads + FROMwesterncrossroadsTOruinedshelterULT)
                        else:
                            $ toruinedshelter = 100
                        #########TO NORTHERN ROAD
                        if NEcornerunlocked:
                            $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
                        elif SEcornerunlocked and SWcornerunlocked and ford_firsttime and bogentrance_firsttime and ruinedshelter_firsttime:
                            $ tonorthernroad = (towesterncrossroads + FROMwesterncrossroadsTOnorthernroadULT)
                        else:
                            $ tonorthernroad = 100
                        #########TO HOWLERS LAIR
                        $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
                        jump eudociahouse01

############################################### harpies
label fishinghamlet_harpiesALL:
    label fishinghamlet_harpies00:
        $ pc_area = "rockslide2"
        show areapicture rockslidetofishinghamleta at basicfade
        stop music fadeout 4.0
        play nature "audio/ambient/mountainroad01.ogg" fadeout 2.0 fadein 2.0 volume 1.0
        $ can_items = 0
        $ can_potions = 1
        $ quarters -= 2
        if not fishinghamlet_harpies_firsttime:
            $ fishinghamlet_harpies_firsttime = 1
            $ custom1 = "The longer you follow the corridor of hills, the more daring the harpies get, observing you as they lower their flight. For now, there’s five of them - their fluttering, bat-like wings let them hang in a spot, though loudly. The creatures are smaller than goblins, with ape-like features and talons that make you think of a parrot. Their fur is in shades of browns and grays. \n\nYou could try to get through them, but you have to scare them off for good. Otherwise, you won’t be able to ride back east, uphill."
        else:
            $ custom1 = "You don’t have to wait long for the harpies to reach you. Their fluttering, bat-like wings let them hang in a spot, though loudly. The creatures are smaller than goblins, with ape-like features and talons that make you think of a parrot. Their fur is in shades of browns and grays."
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ renpy.save("combatsave", extra_info='Combat Auto Save')
        menu:
            '[custom1]
            '
            'I’m ready to face them.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m ready to face them.')
                jump fishinghamlet_harpies01
            'I turn back, to {color=#f6d6bd}Howlers’ Dell{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn back, to {color=#f6d6bd}Howlers’ Dell{/color}.')
                $ tohowlersdell = (FROMhowlersdellTOrockslide + FROMrockslideTOfishinghamlet - 2)
                $ travel_destination = "howlersdell"
                jump finaldestinationafterevent

    label fishinghamlet_harpies01:
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg":
            play music "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg" fadeout 1.0 fadein 1.0
        $ can_items = 0
        $ can_potions = 0
        $ at = 0
        $ at_unlock_spell = 0
        if pc_class == "mage" and not fishinghamlet_harpies_spell:
            $ at_unlock_spell = 1
            $ manacost = 3
        menu:
            'You keep riding forward, and unpack every piece of equipment that could be of use here. It’d be better to weaken the beasts before you clash with them.
            '
            'The dragon horn may scare them away.' if item_dragonhorn and not fishinghamlet_harpies_dragonhorn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The dragon horn may scare them away.')
                $ fishinghamlet_harpies_dragonhorn += 1
                $ custom1 = "You press the horn to your lips and after the first, failed attempt, you fill the hills with the terrifying shout of a monster. The surprised harpies spread, giving you enough time to cross the next few dozen feet, and are forced to speed up to catch up with you, risking your hits will reach them."
                jump fishinghamlet_harpies02
            'I use my crossbow.' if item_crossbow and item_crossbowquarrels >= 1 and not fishinghamlet_harpies_crossbowused:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use my crossbow.')
                $ fishinghamlet_harpies_crossbowused += 1
                $ custom1 = "Your quarrel hits a harpy’s side, making it screech. It stays in the air, flapping its wings desperately, but gets lower and lower, unaware of the stream of blood leaving its shell."
                $ fishinghamlet_harpies_hp -= 1
                $ item_crossbowquarrels -= 1
                $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                jump fishinghamlet_harpies02
            'I lack any quarrels. (disabled)' if item_crossbow and not item_crossbowquarrels and not fishinghamlet_harpies_crossbowused:
                pass
            'I don’t have a crossbow. (disabled)' if not item_crossbow:
                pass
            'I grab my wand. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not fishinghamlet_harpies_spell" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my wand.')
                $ fishinghamlet_harpies_spell += 1
                $ mana = limit_mana(mana-manacost)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                $ custom1 = "You focus on channeling the direction of the pneuma, then push an invisible wave into one of the beasts mid-flight, making it crash into the rocks. Without so much as a gasp, it rolls down the hill."
                $ fishinghamlet_harpies_hp -= 1
                jump fishinghamlet_harpies02
            'I lack pneuma to hit them with a spell. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and not fishinghamlet_harpies_spell" ):
                pass
            'I throw a fistful of blinding powder at one of them.' if item_blindingpowder and not fishinghamlet_harpies_dust:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw a fistful of blinding powder at one of them.')
                $ fishinghamlet_harpies_dust += 1
                $ custom1 = "You speed up, making a beast lower its guard as it tries to reach you with its claws, then surprise it by throwing the powder in its eyes. It screams in panic, hitting the ground behind you and squirming in pain."
                $ fishinghamlet_harpies_hp -= 1
                jump fishinghamlet_harpies02
            'I’ve got no potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                pass
            'I hit one of them with my spear.' if (item_asterionspear and not fishinghamlet_harpies_spear) or (item_mountainroadspear and not fishinghamlet_harpies_spear):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I hit one of them with my spear.')
                $ fishinghamlet_harpies_spear += 1
                $ custom1 = "You tear through one of the wings, but it takes quite a maneuver to release the weapon without stopping. You try to attack again, but this time the pack knows what to expect - one of them catches the haft with its feet, screaming at you as it tries to steal it, but you manage to get away. You burst forward and tie the spear to the saddle, then reach for your axe."
                jump fishinghamlet_harpies02
            'I take a swing with my axe and let the beasts get closer.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a swing with my axe and let the beasts get closer.')
                jump fishinghamlet_harpies03

    label fishinghamlet_harpies02:
        $ at = 0
        $ at_unlock_spell = 0
        if pc_class == "mage" and not fishinghamlet_harpies_spell:
            $ at_unlock_spell = 1
            $ manacost = 3
        menu:
            '[custom1]
            '
            'The dragon horn may scare them away.' if item_dragonhorn and not fishinghamlet_harpies_dragonhorn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The dragon horn may scare them away.')
                $ fishinghamlet_harpies_dragonhorn += 1
                $ custom1 = "You press the horn to your lips and after the first, failed attempt, you fill the hills with the terrifying shout of a monster. The surprised harpies spread, giving you enough time to cross the next few dozen feet, and are forced to speed up to catch up with you, risking your hits will reach them."
                jump fishinghamlet_harpies02
            'I use my crossbow.' if item_crossbow and item_crossbowquarrels >= 1 and not fishinghamlet_harpies_crossbowused:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use my crossbow.')
                $ fishinghamlet_harpies_crossbowused += 1
                $ custom1 = "Your quarrel hits a harpy’s side, making it screech. It stays in the air, flapping its wings desperately, but gets lower and lower, unaware of the stream of blood leaving its shell."
                $ fishinghamlet_harpies_hp -= 1
                $ item_crossbowquarrels -= 1
                $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                jump fishinghamlet_harpies02
            'I lack any quarrels. (disabled)' if item_crossbow and not item_crossbowquarrels and not fishinghamlet_harpies_crossbowused:
                pass
            'I don’t have a crossbow. (disabled)' if not item_crossbow:
                pass
            'I grab my wand. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not fishinghamlet_harpies_spell" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my wand.')
                $ fishinghamlet_harpies_spell += 1
                $ mana = limit_mana(mana-manacost)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                $ custom1 = "You focus on channeling the direction of the pneuma, then push an invisible wave into one of the beasts mid-flight, making it crash into the rocks. Without so much as a gasp, it rolls down the hill."
                $ fishinghamlet_harpies_hp -= 1
                jump fishinghamlet_harpies02
            'I lack pneuma to hit them with a spell. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and not fishinghamlet_harpies_spell" ):
                pass
            'I throw a fistful of blinding powder at one of them.' if item_blindingpowder and not fishinghamlet_harpies_dust:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw a fistful of blinding powder at one of them.')
                $ fishinghamlet_harpies_dust += 1
                $ custom1 = "You speed up, making a beast lower its guard as it tries to reach you with its claws, then surprise it by throwing the powder in its eyes. It screams in panic, hitting the ground behind you and squirming in pain."
                $ fishinghamlet_harpies_hp -= 1
                jump fishinghamlet_harpies02
            'I’ve got no potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                pass
            'I hit one of them with my spear.' if (item_asterionspear and not fishinghamlet_harpies_spear) or (item_mountainroadspear and not fishinghamlet_harpies_spear):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I hit one of them with my spear.')
                $ fishinghamlet_harpies_spear += 1
                $ custom1 = "You tear through one of the wings, but it takes quite a maneuver to release the weapon without stopping. You try to attack again, but this time the pack knows what to expect - one of them catches the haft with its feet, screaming at you as it tries to steal it, but you manage to get away. You burst forward and tie the spear to the saddle, then reach for your axe."
                jump fishinghamlet_harpies02
            'I take a swing with my axe and let the beasts get closer.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a swing with my axe and let the beasts get closer.')
                jump fishinghamlet_harpies03

    label fishinghamlet_harpies03:
        if pc_class == "warrior" and pc_hp < 4:
            $ at_unlock_force = 1
            $ at = 0
        menu:
            'You find comfort in the rhythm dictated by your palfrey, but you’ll struggle to protect both of you, not to mention trying to push away the onslaught. You have to use your axe to scare away anything from reaching {color=#f6d6bd}[horsename]’s{/color} eyes.
            '
            '{image=d6} I’ll hide my head behind my shield.' if item_shield:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ll hide my head behind my shield.')
                $ fishinghamlet_harpies_stance = "shield"
                jump fishinghamlet_harpies04
            'I don’t have a shield. (disabled)' if not item_shield:
                pass
            '{image=d6} I’m strong enough to stay on the offence.' ( condition="pc_hp >= 4 or at == 'force'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m strong enough to stay on the offence.')
                $ fishinghamlet_harpies_stance = "aggro"
                jump fishinghamlet_harpies04
            'I’m too weak to stay on the offence. (disabled)' ( condition="pc_hp < 4 and at != 'force'" ):
                pass
            'I’m too weak to use my experience here. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0" ):
                pass
            '{image=d6} I’ll cover my head with my armored arms.' if armor >= 3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ll cover my head with my armored arms.')
                $ fishinghamlet_harpies_stance = "armor"
                jump fishinghamlet_harpies04
            'My armor is too damaged to help me here. (disabled)' if armor < 3:
                pass
            '{image=d6} I’ve got no tricks to help me here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ve got no tricks to help me here.')
                $ fishinghamlet_harpies_stance = 0
                jump fishinghamlet_harpies04

    label fishinghamlet_harpies04:
        $ at_unlock_force = 0
        $ at = 0
        $ at_unlock_spell = 0
        stop nature fadeout 4.0
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
        if item_golemglove:
            $ d100roll -= 10
        if item_axe03:
            $ d100roll -= 15
        elif item_axe02 or item_axe02alt:
            $ d100roll -= 5
        if fishinghamlet_harpies_dragonhorn:
            $ d100roll -= 10
        if fishinghamlet_harpies_spear:
            $ d100roll -= 10
        $ d100roll += (fishinghamlet_harpies_hp*20)
        if d100roll <= 50:
            $ pc_battlecounter += 1
            if fishinghamlet_harpies_stance == 0:
                if armor >= 1:
                    $ armor = limit_armor(armor-1)
                    show minus1armor at armorchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-2)
                    show minus2hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                    if not cleanliness_clothes_torn:
                        $ cleanliness_clothes_torn = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                else:
                    $ custom1 = "Trying to keep your mount safe, you struggle to protect your own face from a cunning attack of one of the harpies. You lose your first eye faster than you can finish your shout, and soon the talons reach for your neck."
                    jump fishinghamlet_harpies_gameover
            if fishinghamlet_harpies_stance == "shield":
                $ custom1 = "The beasts are too weak to get through the planks of wood. Once you cut through one of their necks, the others let you be, exchanging sad glances as they land next to their wounded allies."
            elif fishinghamlet_harpies_stance == "aggro":
                $ custom1 = "The beasts are too slow to dodge your strikes. Once you cut through one of their necks, the others let you be, exchanging sad glances as they land next to their wounded allies."
            elif fishinghamlet_harpies_stance == "armor":
                $ custom1 = "A beast grabs your arm, but isn’t strong enough to hurt you before you cut through one of their necks. The others let you be, exchanging sad glances as they land next to their wounded allies."
            else:
                $ custom1 = "A beast grabs your arm, cutting through the gambeson, but isn’t strong enough to reach the muscles before you cut through its neck. The others let you be, exchanging sad glances as they land next to their wounded allies."
            menu:
                '[custom1]
                \n\nAfter not even half an hour, you hear the sound of the sea.
                '
                'Finally.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Finally.')
                    $ fishinghamlet_harpies_defeated = 1
                    jump finaldestinationafterevent
        else:
            if fishinghamlet_harpies_stance == 0:
                if armor >= 1:
                    $ armor = limit_armor(armor-1)
                    show minus1armor at armorchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-2)
                    show minus2hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                    if not cleanliness_clothes_torn:
                        $ cleanliness_clothes_torn = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                elif pc_hp > 1:
                    $ pc_hp = limit_pc_hp(pc_hp-3)
                    show minus3hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                    if not cleanliness_clothes_torn:
                        $ cleanliness_clothes_torn = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                else:
                    $ custom1 = "Trying to keep your mount safe, you struggle to protect your own face from a cunning attack of one of the harpies. You lose your first eye faster than you can finish your shout, and soon the talons reach for your neck."
                    jump fishinghamlet_harpies_gameover
            else:
                if armor >= 3:
                    $ armor = limit_armor(armor-1)
                    show minus1armor at armorchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                elif armor >= 1:
                    $ armor = limit_armor(armor-1)
                    show minus1armor at armorchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-2)
                    show minus2hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                    if not cleanliness_clothes_torn:
                        $ cleanliness_clothes_torn = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                else:
                    $ custom1 = "Trying to keep your mount safe, you struggle to protect your own face from a cunning attack of one of the harpies. You lose your first eye faster than you can finish your shout, and soon the talons reach for your neck."
                    jump fishinghamlet_harpies_gameover
            $ pc_battlecounter += 1
            if fishinghamlet_harpies_stance == "shield":
                $ custom1 = "The beasts are too weak to get through the planks of wood, but there’s enough of them to surround you, sinking into your other arm. Once you cut through one of their necks, the others let you be, exchanging sad glances as they land next to their wounded allies."
            elif fishinghamlet_harpies_stance == "aggro":
                $ custom1 = "The beasts are too slow to dodge your strikes, but there’s enough of them to surround you, sinking into your other arm. Once you cut through one of their necks, the others let you be, exchanging sad glances as they land next to their wounded allies."
            elif fishinghamlet_harpies_stance == "armor":
                $ custom1 = "After a beast grabs your arm, there’s another one that strikes you from the other side, sinking into your shoulder. Once you cut through one of their necks, the others let you be, exchanging sad glances as they land next to their wounded allies."
            else:
                $ custom1 = "A beast grabs your arm, cutting through the gambeson, and is strong enough to reach the deep flesh before you cut through its neck. The others let you be, exchanging sad glances as they land next to their wounded allies."
            menu:
                '[custom1]
                \n\nAfter not even half an hour, you hear the sound of the sea.
                '
                'Finally.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Finally.')
                    $ fishinghamlet_harpies_defeated = 1
                    jump finaldestinationafterevent

    label fishinghamlet_harpies_gameover:
        $ pc_hp = 0
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

# ############################################### clearing eudocia
# label encounter_eudociahouse_road01:
#     if not eudociahouse_road_firsttime:
#         $ eudociahouse_road_firsttime = ""
#         $ custom1 = ""
#     else:
#         $ custom1 = ""
#     menu:
#         '[custom1]
#         \n\n
#         '
#         '':
#             $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
#             jump Z
#
#
# default eudociahouse_road_firsttime = 0
# default eudocia_about_roadclearing_cleared = 0
# default eudociahouse_road_clearing_skip = 0 # day
# default eudociahouse_road_clearing_points = 3
#
# finaldestination_repeat # "eudociahouseleaving" # eudocia_about_roadclearing_cleared
# eudociahouse_road_clearing_skip
#     if travel_destination == "eudociahouse" and eudocia_firsttime:
#        if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
#            show areapicture watchtowertoeudocia_fixed at basicfade
#        else:
#            show areapicture watchtowertoeudocia at basicfade
#         stop music fadeout 4.0
#         play nature "audio/ambient/shortcutmeadow01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
#         menu:
#             'The road is free of overgrowing plants, while the steep crag divides the lush forest in half. You barely recognize any shapes in the entanglement of grays, browns, and greens.
#             \n\nThe northern landscape, while similarly impenetrable, is the exact opposite. The meadow turns into barren hills and mountains, barely covered by grass and bushes. Maybe the riding ibexes of the clanspeople from The Growing Mountains would get through such a barrier.
#             '
#             'There are no clans here.':
#                 $ narrator.add_history(kind='nvl', who=narrator.name, what='- There are no clans here.')
#                 jump finaldestinationafterevent # finaldestination_repeat
#
#
#        if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
#            show areapicture watchtowertoeudocia_fixed at basicfade
#        else:
#            show areapicture watchtowertoeudocia at basicfade
#             stop music fadeout 4.0
#             play nature "audio/ambient/druidcave01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
#             menu:
#                 'The road is free of overgrowing plants, while the steep crag divides the lush forest in half. You barely recognize any shapes in the entanglement of grays, browns, and greens.
#                 \n\nThe northern landscape, while similarly impenetrable, is the exact opposite. The meadow turns into barren hills and mountains, barely covered by grass and bushes. Maybe the riding ibexes of the clanspeople from The Growing Mountains would get through such a barrier.
#                 '
#                 'There are no clans here.':
#                     $ narrator.add_history(kind='nvl', who=narrator.name, what='- There are no clans here.')
#                     jump finaldestinationafterevent
