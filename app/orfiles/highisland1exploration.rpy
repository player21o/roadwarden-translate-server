###################### HIGH ISLAND
default highisland_journey_startingpoint = 0 # beach / hamlet
default highisland_journey_inprogress = 0
default highisland_mode = 0 # solo / crew / howlers
default highisland_destination = 0

default highisland_spot = 0

default highisland_harpies_hp = 4
default highisland_harpies_crossbowused = 0
default highisland_harpies_magicused = 0
default highisland_harpies_blindingpowder = 0
default highisland_harpies_crewused = 0

default highisland_cliff_hp = 5
default highisland_cliff_graplinghookused = 0
default highisland_cliff_peltnorthberrytools = 0
default highisland_cliff_forceused = 0
default highisland_cliff_crewhelped = 0
default highisland_cliff_crewhelped_available = 0
default highisland_cliff_crewhelped_points = 0
default highisland_cliff_quintushelped = 0
default highisland_cliff_tzvihelped = 0
default highisland_cliff_tuliahelped = 0
default highisland_cliff_thyrsushelped = 0

default highisland_trailstart_map = 0

default highisland_lightsource_artisanready = 0
default highisland_lightsource = 0

default highisland_howlers_points = 4
default highisland_howlers_earplugs = 0
default highisland_howlers_dragonhorn = 0
default highisland_howlers_crossbow = 0
default highisland_howlers_crewused = 0

default highisland_wallofinsects_howlersrefused = 0

default highisland_monitorlizards_observearea = 0
default highisland_monitorlizards_tryingtofeed = 0
default highisland_monitorlizards_tryingtofeed_narration_points = 0
default highisland_monitorlizards_tryingtofeed_meat = 0
default highisland_monitorlizards_tryingtofeed_plants = 0
default highisland_yellowdotsaurian_knowsabout = 0

default highisland_camp1_examine = 0
default highisland_camp1_canpray = 0
default highisland_camp1_prayed = 0
default highisland_camp1_guards_food_offered = 0
default highisland_camp1_asterioncloak_used = 0
default highisland_camp1_tuliahelp_available = 0
default highisland_camp1_tuliahelp_used = 0

default highisland_denseplants_points = 3
default highisland_denseplants_witheringdust = 0
default highisland_denseplants_axe = 0
default highisland_denseplants_axe_amount = 0
default highisland_denseplants_golemglove = 0
default highisland_denseplants_crew = 0

default highisland_trolltunnel_map = 0
default highisland_trolltunnel_examine = 0
default highisland_trolltunnel_howlersdmg = 0
default highisland_trolltunnel_howlerspotion = 0
default highisland_trolltunnel_trollmet = 0

default highisland_beastfolk_feeding_points = 0
default highisland_beastfolk_feeding_foodestimation = 0
default highisland_beastfolk_feeding_foodestimation_success = 0
default highisland_beastfolk_feeding_threshhold1 = 5
default highisland_beastfolk_feeding_threshhold1descrip = 0
default highisland_beastfolk_feeding_threshhold2 = 10
default highisland_beastfolk_feeding_threshhold2descrip = 0
default highisland_beastfolk_feeding_threshhold3 = 15
default highisland_beastfolk_feeding_threshhold3descrip = 0
default highisland_beastfolk_feeding_threshhold4 = 20
default highisland_beastfolk_feeding_root = 0
default highisland_beastfolk_feeding_root_description = 0
default highisland_beastfolk_howlersguards_tier = 0
default highisland_beastfolk_attack_harshmodifier = 0
default highisland_beastfolk_assassination_available = 0

default highisland_climbingmountain_reached = 0
default highisland_climbingmountain_points = 3
default highisland_climbingmountain_chisel = 0
default highisland_climbingmountain_ironscraps = 0
default highisland_climbingmountain_hook = 0
default highisland_climbingmountain_fighter = 0
default highisland_climbingmountain_navica = 0
default highisland_climbingmountain_crewstrength = 0
default highisland_climbingmountain_crewstrength_calculate = 0

label highisland_cave1ALL:
    label highisland_solo_cave101:
        $ world_known_areas += 2
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg":
            play music "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg" fadeout 1.0 fadein 1.0
        menu:
            'The stream roars above you. You light up a torch - the long, dark tunnel is moist and full of bats, which, surprised by your presence, flee into the deeper corridors.
            \n\nThe remains of the harbor aren’t any more dignified than a pillaged hamlet. The mold and insects spared only a few scraps of wood, while the scavengers scraped clean any pieces of steel and copper.
            \n\nYou run your eyes over the spread stone tools and the scratches left by dragged carts and hulls. Ahead is a brick wall with no door or hinges.
            '
            'I prepare my equipment and get ready to reach the surface.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my equipment and get ready to reach the surface.')
                show areapicture hi_cave02 at basicfade
                menu:
                    'For a few more minutes, you walk by the remnants of the past dwellers - the scraps of fabric, stone bowls, a spot with broken chairs and a table. You walk past a few anxious bats and salamanders, and plenty of spots from which water drips into the tunnel. Sooner or later, the stream will break through one of the countless cracks and reclaim its old bed.
                    \n\nYou freeze when your light touches the black-and-creamy fur of the beast. Not sure if you should run, you give the monster a chance to turn its boulder-like head, capped with a single horn that’s the size of an adult human. The creature may be as large and heavy as a house, but its eyes open one at a time, slowly, as if they haven’t decided yet if you’re really here.
                    '
                    'I’ve got no time to see what it does.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve got no time to see what it does.')
                        $ at_activate = 1
                        $ at = 0
                        menu:
                            'It blinks, observing your torch. You look left and right - the creature almost fills up the width of the tunnel.
                            '
                            ' (disabled)' ( condition="at == 0" ):
                                pass
                            'I raise my open palms. “Er... Nice cave you’ve got here. I’ll just walk by you, alright?”' ( condition="at == 'friendly'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - I raise my open palms. “Er... Nice cave you’ve got here. I’ll just walk by you, alright?”')
                                $ at_activate = 0
                                $ at = 0
                                menu:
                                    'You talk for a bit longer, until the unicorn lowers its head and lets out a loud snort, hitting you with the air from its nostrils. You take a step closer, then walk around the creature’s bear-worthy fur. Before you get behind its rear, you have to put your boot on a rock to step over the outstretched leg.
                                    \n\nThe beast returns to sleep.
                                    '
                                    'I head toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination
                            'I reach toward its horn. “Who’s a sleepy nightmare monster?”' ( condition="at == 'playful'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I reach toward its horn. “Who’s a sleepy nightmare monster?”')
                                $ at_activate = 0
                                $ at = 0
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
                                else:
                                    $ custom1 = "Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground. The light of your torch dances on the sharp rock sticking out a few feet above you, covered in blood."
                                    jump highisland_gameover
                                menu:
                                    'Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground, waiting for your doom to crush you, but the beast turns on its side and curls its legs up under its stomach, returning to its slumber.
                                    \n\nYou get up slowly and move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                                    '
                                    'Gasping for air, I head toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I head toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination
                            'I walk around it.' ( condition="at == 'distanced'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I walk around it.')
                                $ at_activate = 0
                                $ at = 0
                                if armor >= 1:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                else:
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                menu:
                                    'The beast suddenly swings its leg, sending you into the air. You crash into the floor, hearing the unicorn’s surprised snort, but as you raise your head, the creature doesn’t pay you any attention. It turns on its side and curls its legs up under its stomach, returning to its slumber.
                                    \n\nYou get up slowly and move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                                    '
                                    'Gasping for air, I head toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I head toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination
                            'I step away slowly, raise the dragon horn to my lips, and blow as loudly as I can.' ( condition="at == 'intimidating' and item_dragonhorn" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I step away slowly, raise the dragon horn to my lips, and blow as loudly as I can.')
                                $ at_activate = 0
                                $ at = 0
                                menu:
                                    'The echoing roar fills up the corridor, making the surprised beast shake its head and answer with its own cry. It gets on its feet and starts to walk backwards, until it finds enough space to turn around. It then trots away, thundering with every step.
                                    \n\nYou reach for your ear to stop the headache.
                                    '
                                    'I head toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination
                            'I raise my fists and shout. “Get out of my way!”' ( condition="at == 'intimidating' and not item_dragonhorn" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I raise my fists and shout. “Get out of my way!”')
                                $ at_activate = 0
                                $ at = 0
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
                                else:
                                    $ custom1 = "You hardly even notice when it hits your side with its horn. You smash into the wall, then fall to the ground. The light of your torch dances on the sharp rock sticking out a few feet above you, covered in blood."
                                    jump highisland_gameover
                                menu:
                                    'You hardly even notice when it hits your side with its horn. You smash into the wall, then fall to the ground, waiting for your doom to crush you, but the beast turns on its side and curls its legs up under its stomach, returning to its slumber.
                                    \n\nYou get up slowly and move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                                    '
                                    'Gasping for air, I head toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I head toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination
                            'I reach toward its horn. “Listen, I really need to get on the other side.”' ( condition="at == 'vulnerable'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I reach toward its horn. “Listen, I really need to get on the other side.”')
                                $ at_activate = 0
                                $ at = 0
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
                                else:
                                    $ custom1 = "Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground. The light of your torch dances on the sharp rock sticking out a few feet above you, covered in blood."
                                    jump highisland_gameover
                                menu:
                                    'Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground, waiting for your doom to crush you, but the beast turns on its side and curls its legs up under its stomach, returning to its slumber.
                                    \n\nYou get up slowly and move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                                    '
                                    'Gasping for air, I head toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I head toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination

    label highisland_howlers_cave101:
        $ world_known_areas += 2
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg":
            play music "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg" fadeout 1.0 fadein 1.0
        $ highisland_lightsource_artisanready = 1
        menu:
            'The stream roars above you. You light up a torch - the long, dark tunnel is moist and full of bats, which, surprised by your presence, flee into the deeper corridors.
            \n\nThe remains of the harbor aren’t any more dignified than a pillaged hamlet. The mold and insects spared only a few scraps of wood, while the scavengers scraped clean any pieces of steel and copper.
            \n\nYou run your eyes over the spread stone tools and the scratches left by dragged carts and hulls. Ahead is a brick wall with no door or hinges.
            \n\n{color=#f6d6bd}The one with the mace{/color} tells you to wait for him. He drops his heavy bag and starts to prepare a bunch of fine torches. “Should last us for a few hours,” he mutters.
            '
            'I prepare my equipment and get ready to reach the surface.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my equipment and get ready to reach the surface.')
                show areapicture hi_cave02 at basicfade
                menu:
                    'For a few more minutes, you walk by the remnants of the past dwellers - the scraps of fabric, stone bowls, a spot with broken chairs and a table. You walk past a few anxious bats and salamanders, and plenty of spots from which water drips into the tunnel. Sooner or later, the stream will break through one of the countless cracks and reclaim its old bed.
                    \n\nYou freeze when your light touches the black-and-creamy fur of the beast. Not sure if you should run, you give the monster a chance to turn its boulder-like head, capped with a single horn that’s the size of an adult human. The creature may be as large and heavy as a house, but its eyes open one at a time, slowly, as if they haven’t decided yet if you’re really here.
                    '
                    'I glance at the guards.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the guards.')
                        $ at_activate = 1
                        $ at = 0
                        menu:
                            'They’re on the verge of panic. “Unicorn,” says {color=#f6d6bd}the one with the spear{/color}.
                            \n\n“Do ne. Touch. It,” {color=#f6d6bd}the young druid{/color} whispers. “If its calves are here, we’re {i}dead{/i}.”
                            \n\nYou look left and right - the creature almost fills up the width of the tunnel.
                            '
                            ' (disabled)' ( condition="at == 0" ):
                                pass
                            'I raise my open palms. “Er... Nice cave you’ve got here. I’ll just walk by you, alright?”' ( condition="at == 'friendly'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - I raise my open palms. “Er... Nice cave you’ve got here. I’ll just walk by you, alright?”')
                                $ at_activate = 0
                                $ at = 0
                                menu:
                                    'You talk for a bit longer, until the unicorn lowers its head and lets out a loud snort, hitting you with the air from its nostrils. You take a step closer, then walk around the creature’s bear-worthy fur. Before you get behind its rear, you have to put your boot on a rock to step over the outstretched leg.
                                    \n\nThe beast returns to sleep, while your allies look at you as if you’re crazy, but obediently follow your command.
                                    '
                                    'I lead them toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead the others toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination
                            'I reach toward its horn. “Who’s a sleepy nightmare monster?”' ( condition="at == 'playful'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I reach toward its horn. “Who’s a sleepy nightmare monster?”')
                                $ at_activate = 0
                                $ at = 0
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
                                else:
                                    $ custom1 = "Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground. The light of your torch dances on the sharp rock sticking out a few feet above you, covered in blood."
                                    jump highisland_gameover
                                menu:
                                    'Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground, waiting for your doom to crush you, but the beast turns on its side and curls its legs up under its stomach, returning to its slumber.
                                    \n\nSomeone helps you get up. You move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                                    '
                                    'Gasping for air, I lead the others toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I lead the others toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination
                            'I walk around it.' ( condition="at == 'distanced'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I walk around it.')
                                $ at_activate = 0
                                $ at = 0
                                if armor >= 1:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                else:
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                menu:
                                    'The beast suddenly swings its leg, sending you into the air. You crash into the floor, hearing the unicorn’s surprised snort, but as you raise your head, the creature doesn’t pay you any attention. It turns on its side and curls its legs up under its stomach, returning to its slumber.
                                    \n\nSomeone helps you get up. You move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                                    '
                                    'Gasping for air, I lead the others toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I lead the others toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination
                            'I step away slowly, raise the dragon horn to my lips, and blow as loudly as I can.' ( condition="at == 'intimidating' and item_dragonhorn" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I step away slowly, raise the dragon horn to my lips, and blow as loudly as I can.')
                                $ at_activate = 0
                                $ at = 0
                                menu:
                                    'The echoing roar fills up the corridor, making the surprised beast shake its head and answer with its own cry. It gets on its feet and starts to walk backwards, until it finds enough space to turn around. It then trots away, thundering with every step.
                                    \n\nYou reach for your ear to stop the headache. The others give you respectful glances.
                                    '
                                    'I lead them toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead them toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination
                            'I raise my fists and shout. “Get out of my way!”' ( condition="at == 'intimidating' and not item_dragonhorn" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I raise my fists and shout. “Get out of my way!”')
                                $ at_activate = 0
                                $ at = 0
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
                                else:
                                    $ custom1 = "You hardly even notice when it hits your side with its horn. You smash into the wall, then fall to the ground. The light of your torch dances on the sharp rock sticking out a few feet above you, covered in blood."
                                    jump highisland_gameover
                                menu:
                                    'You hardly even notice when it hits your side with its horn. You smash into the wall, then fall to the ground, waiting for your doom to crush you, but the beast turns on its side and curls its legs up under its stomach, returning to its slumber.
                                    \n\nSomeone helps you get up. You move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                                    '
                                    'Gasping for air, I lead the others toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I lead the others toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination
                            'I reach toward its horn. “Listen, I really need to get on the other side.”' ( condition="at == 'vulnerable'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I reach toward its horn. “Listen, I really need to get on the other side.”')
                                $ at_activate = 0
                                $ at = 0
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
                                else:
                                    $ custom1 = "Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground. The light of your torch dances on the sharp rock sticking out a few feet above you, covered in blood."
                                    jump highisland_gameover
                                menu:
                                    'Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground, waiting for your doom to crush you, but the beast turns on its side and curls its legs up under its stomach, returning to its slumber.
                                    \n\nSomeone helps you get up. You move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                                    '
                                    'Gasping for air, I lead the others toward the exit.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I lead the others toward the exit.')
                                        $ highisland_destination = "trailstart"
                                        jump highisland_destination

    label highisland_crew_cave1ALL:
        label highisland_crew_cave101:
            $ world_known_areas += 2
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg":
                play music "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg" fadeout 1.0 fadein 1.0
            if navica_highisland_joined:
                $ highisland_lightsource_artisanready = 1
                if item_axeset or item_axehead:
                    $ item_axeset = 0
                    $ item_axehead = 0
                    $ item_axe02alt = 1
                    $ renpy.notify("You received a bronze axe.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a bronze axe.{/i}')
                    $ custom1 = "{color=#f6d6bd}Navica{/color} unpacks her belongings and prepares a bunch of fine torches, as well as a brass lantern. “Will last you for a few hours,” she states matter-of-factly. “That axe head you’re carrying... Give it to me.”\n\nIn less than five minutes, she hands you the restored weapon. “Just sharpen the blade and it’ll be as good as new. Right, I ain’t following you into the jungle, but I’ve prepared you a few useful tools. Better scat now.”"
                else:
                    $ custom1 = "{color=#f6d6bd}Navica{/color} unpacks her belongings and prepares a bunch of fine torches, as well as a brass lantern. “Will last you for a few hours,” she states matter-of-factly. “Right, I ain’t following you into the woods, but I’ve prepared you a few useful tools. Better scat now.”"
            elif pyrrhos_highisland_joined:
                $ highisland_lightsource_artisanready = 1
                if item_axeset or item_axehead:
                    $ item_axeset = 0
                    $ item_axehead = 0
                    $ item_axe02alt = 1
                    $ renpy.notify("You received a bronze axe.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a bronze axe.{/i}')
                    $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} unpacks his belongings and prepares a bunch of fine torches. “Will last us for a few hours, ay? Now, that axe head you’re carrying... don’t waste it like that.” You hand it to him, and after just a few minutes he sharpens the now-restored blade. “Well, we should get going.”"
                else:
                    $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} unpacks his belongings and prepares a bunch of fine torches. “Will last us for a few hours, ay? We should get going.”"
            else:
                $ custom1 = "Your crew prepares a few torches, enough to last maybe half an hour."
            if dalit_highisland_joined:
                $ custom11 = " “Finally off the damn boat,” {color=#f6d6bd}Dalit’s{/color} face regains its color slowly. Her soaked hair is now maybe one-eighth of its regular volume."
            elif aegidia_highisland_joined:
                $ custom11 = " “Well, even the stairs were in better shape than this spot,” {color=#f6d6bd}Aegidia’s{/color} voice is solemn. “At least my backup strings are dry.”"
            elif bandit_highisland_joined:
                $ custom11 = " “Cozy,” says {color=#f6d6bd}the bandit{/color}. “You think we can find anything worth a coin here?”"
            elif thyrsus_highisland_joined:
                $ custom11 = " {color=#f6d6bd}Thyrsus{/color} observes them. “I betta collect some of their poop. The’s enough of it here to fertilize a few fields.”"
            elif quintus_highisland_joined:
                $ custom11 = " “Some ugly rats,” says {color=#f6d6bd}Quintus{/color}. “What do they eat? Blood?”"
            elif tulia_highisland_joined:
                $ custom11 = " {color=#f6d6bd}Tulia{/color} moves forward quietly, with a hand on her hilt, making sure nothing hides in the shadows."
            elif tzvi_highisland_joined:
                $ custom11 = " {color=#f6d6bd}Tzvi{/color} unrolls his cloak, ignoring the water that drips from it onto the floor."
            else:
                $ custom11 = ""
            if efren_highisland_joined:
                $ custom12 = "\n\n{color=#f6d6bd}Efren{/color} looks around and takes off his {i}hat{/i}, as if you’ve just entered a tomb."
            else:
                $ custom12 = ""
            menu:
                'The stream roars above you. You light up a torch - the long, dark tunnel is moist and full of bats, which, surprised by your presence, flee into the deeper corridors.[custom11][custom12]
                \n\nThe remains of the harbor aren’t any more dignified than a pillaged hamlet. The mold and insects spared only a few scraps of wood, while the scavengers scraped clean any pieces of steel and copper.
                \n\nYou run your eyes over the spread stone tools and the scratches left by dragged carts and hulls. Ahead is a brick wall with no door or hinges.
                \n\n[custom1]
                '
                'I prepare my equipment and get ready to reach the surface.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my equipment and get ready to reach the surface.')
                    show areapicture hi_cave02 at basicfade
                    menu:
                        'For a few more minutes, you walk by the remnants of the past dwellers - the scraps of fabric, stone bowls, a spot with broken chairs and a table. You walk past a few anxious bats and salamanders, and plenty of spots from which water drips into the tunnel. Sooner or later, the stream will break through one of the countless cracks and reclaim its old bed.
                        \n\nYou freeze when your light touches the black-and-creamy fur of the beast. Not sure if you should run, you give the monster a chance to turn its boulder-like head, capped with a single horn that’s the size of an adult human. The creature may be as large and heavy as a house, but its eyes open one at a time, slowly, as if they haven’t decided yet if you’re really here.
                        '
                        'I look left and right.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look left and right.')
                            menu:
                                'The creature almost fills up the width of the tunnel. Your crew looks paralyzed, with eyes wide open. You lower your voice to a whisper.
                                '
                                '“Thoughts, {color=#f6d6bd}Aegidia{/color}?”' if aegidia_highisland_joined and not aegidia_highisland_opinion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thoughts, {color=#f6d6bd}Aegidia{/color}?”')
                                    $ aegidia_highisland_opinion = 1
                                    $ custom1 = "Her lips barely move. “Do ne. Touch. It.”"
                                    jump highisland_crew_cave101a
                                '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and not dalit_highisland_blocked and not dalit_highisland_opinion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                                    $ dalit_highisland_opinion = 1
                                    $ custom1 = "She scoffs. “Brought any giants with you? Or living dragons?”"
                                    jump highisland_crew_cave101a
                                '“Any tips, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and not efren_highisland_opinion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips, {color=#f6d6bd}Efren{/color}?”')
                                    $ efren_highisland_opinion = 1
                                    $ custom1 = "He takes his hand off his lips. “Stay calm.”"
                                    jump highisland_crew_cave101a
                                '“{color=#f6d6bd}Thyrsus{/color}, suggestions?”' if thyrsus_highisland_joined and not thyrsus_highisland_blocked and not thyrsus_highisland_opinion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, suggestions?”')
                                    $ thyrsus_highisland_opinion = 1
                                    $ custom1 = "The few amulets he has with him rattle as he leans toward you. “I’ve no poisons for... Unicorns.”"
                                    jump highisland_crew_cave101a
                                '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and not pyrrhos_highisland_opinion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                                    $ pyrrhos_highisland_opinion = 1
                                    $ custom1 = "He gives you a terrified look."
                                    jump highisland_crew_cave101a
                                'I look at {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and not bandit_highisland_opinion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}the bandit{/color}.')
                                    $ bandit_highisland_opinion = 1
                                    $ custom1 = "“Well, {i}I{/i} can walk around it. But can you?”"
                                    jump highisland_crew_cave101a
                                '“{color=#f6d6bd}Tulia{/color}, what do you recommend?”' if tulia_highisland_joined and not tulia_highisland_opinion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, what do you recommend?”')
                                    $ tulia_highisland_opinion = 1
                                    $ custom1 = "She frowns and shakes her head."
                                    jump highisland_crew_cave101a
                                '“Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”' if tzvi_highisland_joined and not tzvi_highisland_opinion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”')
                                    $ tzvi_highisland_opinion = 1
                                    $ custom1 = "“What am I, a hunter?”"
                                    jump highisland_crew_cave101a
                                '“{color=#f6d6bd}Quintus{/color}, any ideas?”' if quintus_highisland_joined and not quintus_highisland_opinion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Quintus{/color}, any ideas?”')
                                    $ quintus_highisland_opinion = 1
                                    $ custom1 = "He pays you no attention, too afraid to move."
                                    jump highisland_crew_cave101a
                                'I sigh. “I’ll handle it.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh. “I’ll handle it.”')
                                    jump highisland_crew_cave102

        label highisland_crew_cave101a:
            menu:
                '[custom1]
                '
                '“Thoughts, {color=#f6d6bd}Aegidia{/color}?”' if aegidia_highisland_joined and not aegidia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thoughts, {color=#f6d6bd}Aegidia{/color}?”')
                    $ aegidia_highisland_opinion = 1
                    $ custom1 = "Her lips barely move. “Do ne. Touch. It.”"
                    jump highisland_crew_cave101a
                '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and not dalit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                    $ dalit_highisland_opinion = 1
                    $ custom1 = "She scoffs. “Brought any giants with you? Or living dragons?”"
                    jump highisland_crew_cave101a
                '“Any tips, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and not efren_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips, {color=#f6d6bd}Efren{/color}?”')
                    $ efren_highisland_opinion = 1
                    $ custom1 = "He takes his hand off his lips. “Stay calm.”"
                    jump highisland_crew_cave101a
                '“{color=#f6d6bd}Thyrsus{/color}, suggestions?”' if thyrsus_highisland_joined and not thyrsus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, suggestions?”')
                    $ thyrsus_highisland_opinion = 1
                    $ custom1 = "The few amulets he has with him rattle as he leans toward you. “I’ve no poisons for... Unicorns.”"
                    jump highisland_crew_cave101a
                '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and not pyrrhos_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                    $ pyrrhos_highisland_opinion = 1
                    $ custom1 = "He gives you a terrified look."
                    jump highisland_crew_cave101a
                'I look at {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and not bandit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}the bandit{/color}.')
                    $ bandit_highisland_opinion = 1
                    $ custom1 = "“Well, {i}I{/i} can walk around it. But can you?”"
                    jump highisland_crew_cave101a
                '“{color=#f6d6bd}Tulia{/color}, what do you recommend?”' if tulia_highisland_joined and not tulia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, what do you recommend?”')
                    $ tulia_highisland_opinion = 1
                    $ custom1 = "She frowns and shakes her head."
                    jump highisland_crew_cave101a
                '“Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”' if tzvi_highisland_joined and not tzvi_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”')
                    $ tzvi_highisland_opinion = 1
                    $ custom1 = "“What am I, a hunter?”"
                    jump highisland_crew_cave101a
                '“{color=#f6d6bd}Quintus{/color}, any ideas?”' if quintus_highisland_joined and not quintus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Quintus{/color}, any ideas?”')
                    $ quintus_highisland_opinion = 1
                    $ custom1 = "He pays you no attention, too afraid to move."
                    jump highisland_crew_cave101a
                'I sigh. “I’ll handle it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh. “I’ll handle it.”')
                    jump highisland_crew_cave102

        label highisland_crew_cave102:
            $ at_activate = 1
            $ at = 0
            menu:
                'It blinks, observing your torch.
                '
                ' (disabled)' ( condition="at == 0" ):
                    pass
                'I raise my open palms. “Er... Nice cave you’ve got here. I’ll just walk by you, alright?”' ( condition="at == 'friendly'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - I raise my open palms. “Er... Nice cave you’ve got here. I’ll just walk by you, alright?”')
                    $ at_activate = 0
                    $ at = 0
                    menu:
                        'You talk for a bit longer, until the unicorn lowers its head and lets out a loud snort, hitting you with the air from its nostrils. You take a step closer, then walk around the creature’s bear-worthy fur. Before you get behind its rear, you have to put your boot on a rock to step over the outstretched leg.
                        \n\nThe beast returns to sleep, while your allies look at you as if you’re crazy, but obediently follow your command.
                        '
                        'I lead them toward the exit.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead the others toward the exit.')
                            $ highisland_destination = "trailstart"
                            jump highisland_destination
                'I reach toward its horn. “Who’s a sleepy nightmare monster?”' ( condition="at == 'playful'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I reach toward its horn. “Who’s a sleepy nightmare monster?”')
                    $ at_activate = 0
                    $ at = 0
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
                    else:
                        $ custom1 = "Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground. The light of your torch dances on the sharp rock sticking out a few feet above you, covered in blood."
                        jump highisland_gameover
                    menu:
                        'Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground, waiting for your doom to crush you, but the beast turns on its side and curls its legs up under its stomach, returning to its slumber.
                        \n\nSomeone helps you get up. You move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                        '
                        'Gasping for air, I lead the others toward the exit.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I lead the others toward the exit.')
                            $ highisland_destination = "trailstart"
                            jump highisland_destination
                'I walk around it.' ( condition="at == 'distanced'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I walk around it.')
                    $ at_activate = 0
                    $ at = 0
                    if armor >= 1:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                    menu:
                        'The beast suddenly swings its leg, sending you into the air. You crash into the floor, hearing the unicorn’s surprised snort, but as you raise your head, the creature doesn’t pay you any attention. It turns on its side and curls its legs up under its stomach, returning to its slumber.
                        \n\nSomeone helps you get up. You move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                        '
                        'Gasping for air, I lead the others toward the exit.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I lead the others toward the exit.')
                            $ highisland_destination = "trailstart"
                            jump highisland_destination
                'I step away slowly, raise the dragon horn to my lips, and blow as loudly as I can.' ( condition="at == 'intimidating' and item_dragonhorn" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I step away slowly, raise the dragon horn to my lips, and blow as loudly as I can.')
                    $ at_activate = 0
                    $ at = 0
                    menu:
                        'The echoing roar fills up the corridor, making the surprised beast shake its head and answer with its own cry. It gets on its feet and starts to walk backwards, until it finds enough space to turn around. It then trots away, thundering with every step.
                        \n\nYou reach for your ear to stop the headache. The others give you respectful glances.
                        '
                        'I lead them toward the exit.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead them toward the exit.')
                            $ highisland_destination = "trailstart"
                            jump highisland_destination
                'I raise my fists and shout. “Get out of my way!”' ( condition="at == 'intimidating' and not item_dragonhorn" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I raise my fists and shout. “Get out of my way!”')
                    $ at_activate = 0
                    $ at = 0
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
                    else:
                        $ custom1 = "You hardly even notice when it hits your side with its horn. You smash into the wall, then fall to the ground. The light of your torch dances on the sharp rock sticking out a few feet above you, covered in blood."
                        jump highisland_gameover
                    menu:
                        'You hardly even notice when it hits your side with its horn. You smash into the wall, then fall to the ground, waiting for your doom to crush you, but the beast turns on its side and curls its legs up under its stomach, returning to its slumber.
                        \n\nSomeone helps you get up. You move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                        '
                        'Gasping for air, I lead the others toward the exit.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I lead the others toward the exit.')
                            $ highisland_destination = "trailstart"
                            jump highisland_destination
                'I reach toward its horn. “Listen, I really need to get on the other side.”' ( condition="at == 'vulnerable'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I reach toward its horn. “Listen, I really need to get on the other side.”')
                    $ at_activate = 0
                    $ at = 0
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
                    else:
                        $ custom1 = "Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground. The light of your torch dances on the sharp rock sticking out a few feet above you, covered in blood."
                        jump highisland_gameover
                    menu:
                        'Before you touch it, it shakes its head angrily, hitting your side with its horn. You smash into the wall, then fall to the ground, waiting for your doom to crush you, but the beast turns on its side and curls its legs up under its stomach, returning to its slumber.
                        \n\nSomeone helps you get up. You move the torch away from the beast’s eye. Listening to its snorts, you look ahead - there’s now plenty of space to walk forward.
                        '
                        'Gasping for air, I lead the others toward the exit.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I lead the others toward the exit.')
                            $ highisland_destination = "trailstart"
                            jump highisland_destination

label highisland_trailstartALL:
    label highisland_solo_trailstartALL:
        label highisland_solo_trailstart01:
            menu:
                'Only a few boulders separate you from the deep woods. The song of the sea and the hum of the stream are overshadowed by the screeches of beasts and their prey.
                \n\nWhile there are some rusty remains of an old cart, and the gentle slope was carved by tools, it leads you toward a wall of shrubs and creepers. You get on top of a large rock - there are no roads in sight, but you spot a humble trail made by hooves and paws.
                '
                'I think about the map from the giant statue.' if giantstatue_pray_map_learned and not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about the map from the giant statue.')
                    $ highisland_trailstart_map = 1
                    $ custom1 = "While the path doesn’t lead directly to the volcano, it matches the ancient trail of stars that’s meant to take you to the main road - if it still exists."
                    jump highisland_solo_trailstart01a
                '{image=d6} I follow the game trail.' if not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight, and the plants that surround it grow from the remains of an old road, hardened with rocks. An owl gives you a curious glance from a branch above your head.\n\n"
                    $ custom2 = ""
                    jump highisland_solo_trailstart03
                'I follow the game trail.' if highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight. The plants that surround it grow from the remains of the old road, hardened with rocks. An owl gives you a curious glance from a branch above your head.\n\n"
                    $ custom2 = ""
                    jump highisland_solo_trailstart03
                '{image=d6} I seek the shape of the volcano and head toward it, through the wilderness.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I seek the shape of the volcano and head toward it, through the wilderness.')
                    jump highisland_solo_trailstart02

        label highisland_solo_trailstart01a:
            menu:
                '[custom1]
                '
                'I think about the map from the giant statue.' if giantstatue_pray_map_learned and not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about the map from the giant statue.')
                    $ highisland_trailstart_map = 1
                    $ custom1 = "While the path doesn’t lead directly to the volcano, it matches the ancient trail of stars that’s meant to take you to the main road - if it still exists."
                    jump highisland_solo_trailstart01a
                '{image=d6} I follow the game trail.' if not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight, and the plants that surround it grow from the remains of an old road, hardened with rocks. An owl gives you a curious glance from a branch above your head.\n\n"
                    $ custom2 = ""
                    jump highisland_solo_trailstart03
                'I follow the game trail.' if highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight. The plants that surround it grow from the remains of the old road, hardened with rocks. An owl gives you a curious glance from a branch above your head.\n\n"
                    $ custom2 = ""
                    jump highisland_solo_trailstart03
                '{image=d6} I seek the shape of the volcano and head toward it, through the wilderness.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I seek the shape of the volcano and head toward it, through the wilderness.')
                    jump highisland_solo_trailstart02

        label highisland_solo_trailstart02:
            $ at = 0
            $ d100roll = renpy.random.randint(1, 100)
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            $ d100roll -= (shortcut_traveled*2)
            if d100roll <= 60:
                if shortcut_traveled >= 6:
                    $ custom1 = "The time you’ve spent exploring the wilderness of the peninsula quickly pays off. You find a passable route right away, avoiding an upset family of monkeys and crossing the thicket with little difficulty. "
                elif shortcut_traveled >= 3:
                    $ custom1 = "The time you’ve spent exploring the wilderness of the peninsula soon pays off. You find a passable route, avoiding an upset family of monkeys and crossing the thicket with little difficulty. "
                elif shortcut_traveled >= 1:
                    $ custom1 = "You don’t know much about crossing the wilderness, but you use what you’ve seen in the heart of the woods to find a passable route, luckily avoiding an upset family of monkeys. "
                else:
                    $ custom1 = "Confused at first, you luckily find a passable route and avoid an upset family of monkeys. "
                $ custom2 = ""
                label highisland_solo_trailstart03:
                    menu:
                        '[custom1][custom2]After a few minutes, you reach what seems to be a proper trail, beaten, wider than a wagon, and leading both toward the volcano and away from it. Among the thicket you spot the remains of the stone wall, long since collapsed.
                        '
                        'For now, I’ll stick to it.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For now, I’ll stick to it.')
                            $ highisland_destination = "darkness"
                            jump highisland_destination
            else:
                if shortcut_traveled >= 6:
                    $ custom1 = "Despite all the time you’ve spent exploring the wilderness of the peninsula, you find yourself stumbling upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                elif shortcut_traveled >= 3:
                    $ custom1 = "The time you’ve spent exploring the wilderness of the peninsula has not prepared you for such lush undergrowth. You stumble upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                elif shortcut_traveled >= 1:
                    $ custom1 = "Knowing little about crossing the wilderness, you stumble upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                else:
                    $ custom1 = "Confused, you get lost in the woods, stumbling upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                $ custom2 = ""
                if pc_food:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    $ custom1 = "Confused, you soon stumble upon upset monkeys and foxes. Forced to roam and gasping for air, you try to flee from their angry shouts, only to get lost deeper in the woods - for good."
                    jump highisland_gameover
                menu:
                    '[custom1][custom2]After a few minutes, you reach what seems to be a proper trail, beaten, wider than a wagon, and leading both toward the volcano and away from it. Among the thicket you spot the remains of the stone wall, long since collapsed.
                    '
                    'For now, I’ll stick to it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- For now, I’ll stick to it.')
                        $ highisland_destination = "darkness"
                        jump highisland_destination

    label highisland_howlers_trailstartALL:
        label highisland_howlers_trailstart01:
            menu:
                'Only a few boulders separate you from the deep woods. The song of the sea and the hum of the stream are overshadowed by the screeches of beasts and their prey.
                \n\nWhile there are some rusty remains of an old cart, and the gentle slope was carved by tools, it leads you toward a wall of shrubs and creepers. You get on top of a large rock - there are no roads in sight, but you spot a humble trail made by hooves and paws.
                \n\n{color=#f6d6bd}The leader{/color} swallows loudly, then looks at you. “Well? Where now?”
                '
                'I think about the map from the giant statue.' if giantstatue_pray_map_learned and not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about the map from the giant statue.')
                    $ highisland_trailstart_map = 1
                    $ custom1 = "While the path doesn’t lead directly to the volcano, it matches the ancient trail of stars that’s meant to take you to the main road - if it still exists."
                    jump highisland_howlers_trailstart01a
                '{image=d6} I follow the game trail.' if not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight, and the plants that surround it grow from the remains of an old road, hardened with rocks. An owl gives your group a curious glance from a branch above your heads.\n\n"
                    $ custom2 = ""
                    jump highisland_howlers_trailstart03
                'I follow the game trail.' if highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight. The plants that surround it grow from the remains of the old road, hardened with rocks. An owl gives your group a curious glance from a branch above your heads.\n\n"
                    $ custom2 = ""
                    jump highisland_howlers_trailstart03
                '{image=d6} I seek the shape of the volcano and head toward it, through the wilderness.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I seek the shape of the volcano and head toward it, through the wilderness.')
                    jump highisland_howlers_trailstart02

        label highisland_howlers_trailstart01a:
            menu:
                '[custom1]
                '
                'I think about the map from the giant statue.' if giantstatue_pray_map_learned and not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about the map from the giant statue.')
                    $ highisland_trailstart_map = 1
                    $ custom1 = "While the path doesn’t lead directly to the volcano, it matches the ancient trail of stars that’s meant to take you to the main road - if it still exists."
                    jump highisland_howlers_trailstart01a
                '{image=d6} I follow the game trail.' if not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight, and the plants that surround it grow from the remains of an old road, hardened with rocks. An owl gives your group a curious glance from a branch above your heads.\n\n"
                    $ custom2 = ""
                    jump highisland_howlers_trailstart03
                'I follow the game trail.' if highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight. The plants that surround it grow from the remains of the old road, hardened with rocks. An owl gives your group a curious glance from a branch above your heads.\n\n"
                    $ custom2 = ""
                    jump highisland_howlers_trailstart03
                '{image=d6} I seek the shape of the volcano and head toward it, through the wilderness.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I seek the shape of the volcano and head toward it, through the wilderness.')
                    jump highisland_howlers_trailstart02

        label highisland_howlers_trailstart02:
            $ at = 0
            $ d100roll = renpy.random.randint(1, 100)
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            $ d100roll -= (shortcut_traveled*2)
            if d100roll <= 60:
                if shortcut_traveled >= 6:
                    $ custom1 = "The time you’ve spent exploring the wilderness of the peninsula quickly pays off. You find a passable route right away, avoiding an upset family of monkeys and crossing the thicket with little difficulty. "
                elif shortcut_traveled >= 3:
                    $ custom1 = "The time you’ve spent exploring the wilderness of the peninsula soon pays off. You find a passable route, avoiding an upset family of monkeys and crossing the thicket with little difficulty. "
                elif shortcut_traveled >= 1:
                    $ custom1 = "You don’t know much about crossing the wilderness, but you use what you’ve seen in the heart of the woods to find a passable route, luckily avoiding an upset family of monkeys. "
                else:
                    $ custom1 = "Confused at first, you luckily find a passable route and avoid an upset family of monkeys. "
                $ custom2 = "{color=#f6d6bd}The guards{/color} stay right behind you, and while they don’t say much, their eyes are vigilant, rather than afraid.\n\n"
                label highisland_howlers_trailstart03:
                    menu:
                        '[custom1][custom2]After a few minutes, you reach what seems to be a proper trail, beaten, wider than a wagon, and leading both toward the volcano and away from it. Among the thicket you spot the remains of the stone wall, long since collapsed.
                        '
                        '“For now, we’ll stick to this route.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “For now, we’ll stick to this route.”')
                            $ highisland_destination = "darkness"
                            jump highisland_destination
            else:
                if shortcut_traveled >= 6:
                    $ custom1 = "Despite all the time you’ve spent exploring the wilderness of the peninsula, you find yourself stumbling upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                elif shortcut_traveled >= 3:
                    $ custom1 = "The time you’ve spent exploring the wilderness of the peninsula has not prepared you for such lush undergrowth. You stumble upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                elif shortcut_traveled >= 1:
                    $ custom1 = "Knowing little about crossing the wilderness, you stumble upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                else:
                    $ custom1 = "Confused, you get lost in the woods, stumbling upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                $ custom2 = "\n\n{color=#f6d6bd}The guards{/color} stay a bit behind you, and while they don’t say much, they give you angry looks. You wait for them for a few moments - one of them slipped on a wet root, and needs to have his bruised face washed."
                $ highisland_howlersguards_hp -= 1
                menu:
                    '[custom1]After a few minutes, you reach what seems to be a proper trail, beaten, wider than a wagon, and leading both toward the volcano and away from it. Among the thicket you spot the remains of the stone wall, long since collapsed.[custom2]
                    '
                    '“For now, we’ll stick to this route.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “For now, we’ll stick to this route.”')
                        $ highisland_destination = "darkness"
                        jump highisland_destination

    label highisland_crew_trailstartALL:
        label highisland_crew_trailstart01:
            menu:
                'Only a few boulders separate you from the deep woods. The song of the sea and the hum of the stream are overshadowed by the screeches of beasts and their prey.
                \n\nWhile there are some rusty remains of an old cart, and the gentle slope was carved by tools, it leads you toward a wall of shrubs and creepers. You get on top of a large rock - there are no roads in sight, but you spot a humble trail made by hooves and paws.
                \n\nThe worried looks of your crew are as lost as you are.
                '
                'I think about the map from the giant statue.' if giantstatue_pray_map_learned and not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about the map from the giant statue.')
                    $ highisland_trailstart_map = 1
                    $ custom1 = "While the path doesn’t lead directly to the volcano, it matches the ancient trail of stars that’s meant to take you to the main road - if it still exists."
                    jump highisland_crew_trailstart01a
                'I follow the game trail.' if highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight. The plants that surround it grow from the remains of the old road, hardened with rocks. An owl gives your group a curious glance from a branch above your heads.\n\n"
                    $ custom2 = ""
                    jump highisland_crew_trailstart03
                '“Thoughts, {color=#f6d6bd}Aegidia{/color}?”' if aegidia_highisland_joined and not aegidia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thoughts, {color=#f6d6bd}Aegidia{/color}?”')
                    $ aegidia_highisland_opinion = 1
                    $ custom1 = "She pokes the bushes with her bow. “I’m right behind you.”"
                    jump highisland_crew_trailstart01a
                '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and not dalit_highisland_blocked and not dalit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                    $ dalit_highisland_opinion = 1
                    $ custom1 = "“Oh, you {i}don’t{/i} know the way?” She pushes her wet hair behind her ear. “If you want, we can try through the thicket. But usually I left the pathfinding to other hunters.”"
                    jump highisland_crew_trailstart01a
                '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and dalit_highisland_blocked and not dalit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                    $ dalit_highisland_opinion = 1
                    $ custom1 = "“Oh, you {i}don’t{/i} know the way?” She pushes her wet hair behind her ear. “If you want, we can try through the thicket. But me, I’m too tired to lead you, and I usually leave the pathfinding to other hunters.”"
                    jump highisland_crew_trailstart01a
                '“Any tips, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and not efren_highisland_blocked and not efren_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips, {color=#f6d6bd}Efren{/color}?”')
                    $ efren_highisland_opinion = 1
                    $ custom1 = "He sniffs. “The woods here aren’t that different from ours, just wetter. I {i}should{/i} be able to get us through.”"
                    jump highisland_crew_trailstart01a
                '“Any tips, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and efren_highisland_blocked and not efren_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips, {color=#f6d6bd}Efren{/color}?”')
                    $ efren_highisland_opinion = 1
                    $ custom1 = "He sniffs. “The woods here aren’t that different from ours, just wetter. I {i}would{/i} be able to get us through, but I feel like I’m going to collapse soon.”"
                    jump highisland_crew_trailstart01a
                '“{color=#f6d6bd}Thyrsus{/color}, suggestions?”' if thyrsus_highisland_joined and not thyrsus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, suggestions?”')
                    $ thyrsus_highisland_opinion = 1
                    $ custom1 = "He doesn’t even notice your question, just observes a small cat that’s jumping between the tree crowns."
                    jump highisland_crew_trailstart01a
                '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and not pyrrhos_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                    $ pyrrhos_highisland_opinion = 1
                    $ custom1 = "“Ye know me, roadster,” he chuckles, “I’d rather follow the road.”"
                    jump highisland_crew_trailstart01a
                'I look at {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and not bandit_highisland_blocked and not bandit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}the bandit{/color}.')
                    $ bandit_highisland_opinion = 1
                    $ custom1 = "He sends you a heartwarming smile. “I ain’t a pathfinder, but I spent some time in the woods, I did, and so did you. We’ll figure out a trail.”"
                    jump highisland_crew_trailstart01a
                'I look at {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and bandit_highisland_blocked and not bandit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}the bandit{/color}.')
                    $ bandit_highisland_opinion = 1
                    $ custom1 = "He sends you a sad smile. “I ain’t a pathfinder, and I’m way too tired to guide you. But {i}you{/i} spent plenty of time in the wilderness, too, you did. Maybe you’ll figure out a trail.”"
                    jump highisland_crew_trailstart01a
                '“{color=#f6d6bd}Tulia{/color}, what do you recommend?”' if tulia_highisland_joined and not tulia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, what do you recommend?”')
                    $ tulia_highisland_opinion = 1
                    $ custom1 = "She nods toward the humble trail. “Let’s start with the easier option, then turn back if it leads us nowhere.”"
                    jump highisland_crew_trailstart01a
                '“Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”' if tzvi_highisland_joined and not tzvi_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”')
                    $ tzvi_highisland_opinion = 1
                    $ custom1 = "His voice is close to a screech. “I thought {i}you{/i} knew the way.”"
                    jump highisland_crew_trailstart01a
                '“{color=#f6d6bd}Quintus{/color}, any ideas?”' if quintus_highisland_joined and not quintus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Quintus{/color}, any ideas?”')
                    $ quintus_highisland_opinion = 1
                    $ custom1 = "He adjusts the bandage on his face. “I see no dragons from here. We can try whatever.”"
                    jump highisland_crew_trailstart01a
                '{image=d6} I follow the game trail.' if not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight, and the plants that surround it grow from the remains of an old road, hardened with rocks. An owl gives your group a curious glance from a branch above your heads.\n\n"
                    $ custom2 = ""
                    jump highisland_crew_trailstart03
                '{image=d6} I seek the shape of the volcano and head toward it, through the wilderness.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I seek the shape of the volcano and head toward it, through the wilderness.')
                    jump highisland_crew_trailstart02

        label highisland_crew_trailstart01a:
            menu:
                '[custom1]
                '
                'I think about the map from the giant statue.' if giantstatue_pray_map_learned and not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about the map from the giant statue.')
                    $ highisland_trailstart_map = 1
                    $ custom1 = "While the path doesn’t lead directly to the volcano, it matches the ancient trail of stars that’s meant to take you to the main road - if it still exists."
                    jump highisland_crew_trailstart01a
                'I follow the game trail.' if highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight. The plants that surround it grow from the remains of the old road, hardened with rocks. An owl gives your group a curious glance from a branch above your heads.\n\n"
                    $ custom2 = ""
                    jump highisland_crew_trailstart03
                '“Thoughts, {color=#f6d6bd}Aegidia{/color}?”' if aegidia_highisland_joined and not aegidia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thoughts, {color=#f6d6bd}Aegidia{/color}?”')
                    $ aegidia_highisland_opinion = 1
                    $ custom1 = "She pokes the bushes with her bow. “I’m right behind you.”"
                    jump highisland_crew_trailstart01a
                '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and not dalit_highisland_blocked and not dalit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                    $ dalit_highisland_opinion = 1
                    $ custom1 = "“Oh, you {i}don’t{/i} know the way?” She pushes her wet hair behind her ear. “If you want, we can try through the thicket. But usually I left the pathfinding to other hunters.”"
                    jump highisland_crew_trailstart01a
                '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and dalit_highisland_blocked and not dalit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                    $ dalit_highisland_opinion = 1
                    $ custom1 = "“Oh, you {i}don’t{/i} know the way?” She pushes her wet hair behind her ear. “If you want, we can try through the thicket. But me, I’m too tired to lead you, and I usually leave the pathfinding to other hunters.”"
                    jump highisland_crew_trailstart01a
                '“Any tips, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and not efren_highisland_blocked and not efren_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips, {color=#f6d6bd}Efren{/color}?”')
                    $ efren_highisland_opinion = 1
                    $ custom1 = "He sniffs. “The woods here aren’t that different from ours, just wetter. I {i}should{/i} be able to get us through.”"
                    jump highisland_crew_trailstart01a
                '“Any tips, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and efren_highisland_blocked and not efren_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips, {color=#f6d6bd}Efren{/color}?”')
                    $ efren_highisland_opinion = 1
                    $ custom1 = "He sniffs. “The woods here aren’t that different from ours, just wetter. I {i}would{/i} be able to get us through, but I feel like I’m going to collapse soon.”"
                    jump highisland_crew_trailstart01a
                '“{color=#f6d6bd}Thyrsus{/color}, suggestions?”' if thyrsus_highisland_joined and not thyrsus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, suggestions?”')
                    $ thyrsus_highisland_opinion = 1
                    $ custom1 = "He doesn’t even notice your question, just observes a small cat that’s jumping between the tree crowns."
                    jump highisland_crew_trailstart01a
                '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and not pyrrhos_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                    $ pyrrhos_highisland_opinion = 1
                    $ custom1 = "“Ye know me, roadster,” he chuckles, “I’d rather follow the road.”"
                    jump highisland_crew_trailstart01a
                'I look at {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and not bandit_highisland_blocked and not bandit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}the bandit{/color}.')
                    $ bandit_highisland_opinion = 1
                    $ custom1 = "He sends you a heartwarming smile. “I ain’t a pathfinder, but I spent some time in the woods, I did, and so did you. We’ll figure out a trail.”"
                    jump highisland_crew_trailstart01a
                'I look at {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and bandit_highisland_blocked and not bandit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}the bandit{/color}.')
                    $ bandit_highisland_opinion = 1
                    $ custom1 = "He sends you a sad smile. “I ain’t a pathfinder, and I’m way too tired to guide you. But {i}you{/i} spent plenty of time in the wilderness, too, you did. Maybe you’ll figure out a trail.”"
                    jump highisland_crew_trailstart01a
                '“{color=#f6d6bd}Tulia{/color}, what do you recommend?”' if tulia_highisland_joined and not tulia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, what do you recommend?”')
                    $ tulia_highisland_opinion = 1
                    $ custom1 = "She nods toward the humble trail. “Let’s start with the easier option, then turn back if it leads us nowhere.”"
                    jump highisland_crew_trailstart01a
                '“Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”' if tzvi_highisland_joined and not tzvi_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”')
                    $ tzvi_highisland_opinion = 1
                    $ custom1 = "His voice is close to a screech. “I thought {i}you{/i} knew the way.”"
                    jump highisland_crew_trailstart01a
                '“{color=#f6d6bd}Quintus{/color}, any ideas?”' if quintus_highisland_joined and not quintus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Quintus{/color}, any ideas?”')
                    $ quintus_highisland_opinion = 1
                    $ custom1 = "He adjusts the bandage on his face. “I see no dragons from here. We can try whatever.”"
                    jump highisland_crew_trailstart01a
                '{image=d6} I follow the game trail.' if not highisland_trailstart_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I follow the game trail.')
                    $ custom1 = "It may be narrow, but proves to be firm and straight, and the plants that surround it grow from the remains of an old road, hardened with rocks. An owl gives your group a curious glance from a branch above your heads.\n\n"
                    $ custom2 = ""
                    jump highisland_crew_trailstart03
                '{image=d6} I seek the shape of the volcano and head toward it, through the wilderness.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I seek the shape of the volcano and head toward it, through the wilderness.')
                    jump highisland_crew_trailstart02

        label highisland_crew_trailstart02:
            $ at = 0
            $ d100roll = renpy.random.randint(1, 100)
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            $ d100roll -= (shortcut_traveled*2)
            if efren_highisland_joined and not efren_highisland_blocked:
                $ d100roll -= 30
            if bandit_highisland_joined and not bandit_highisland_blocked:
                $ d100roll -= 20
            if dalit_highisland_joined and not dalit_highisland_blocked:
                $ d100roll -= 15
            if d100roll <= 60:
                if efren_highisland_joined and not efren_highisland_blocked:
                    $ custom1 = "Led by {color=#f6d6bd}Efren{/color}, you find a passable route right away, avoiding an upset family of monkeys and crossing the thicket with little difficulty. "
                elif bandit_highisland_joined and not bandit_highisland_blocked:
                    $ custom1 = "Led by {color=#f6d6bd}the bandit{/color}, you find a passable route right away, avoiding an upset family of monkeys and crossing the thicket with little difficulty. "
                elif dalit_highisland_joined and not dalit_highisland_blocked:
                    $ custom1 = "Led by {color=#f6d6bd}Dalit{/color}, you soon find a passable route, avoiding an upset family of monkeys and crossing the thicket with little difficulty. "
                elif shortcut_traveled >= 6:
                    $ custom1 = "The time you’ve spent exploring the wilderness of the peninsula pays off quickly. You find a passable route right away, avoiding an upset family of monkeys and crossing the thicket with little difficulty. "
                elif shortcut_traveled >= 3:
                    $ custom1 = "The time you’ve spent exploring the wilderness of the peninsula soon pays off. You find a passable route, avoiding an upset family of monkeys and crossing the thicket with little difficulty. "
                elif shortcut_traveled >= 1:
                    $ custom1 = "You don’t know much about crossing the wilderness, but you use what you’ve seen in the heart of the woods to find a passable route, luckily avoiding an upset family of monkeys. "
                else:
                    $ custom1 = "Confused at first, you luckily find a passable route and avoid an upset family of monkeys. "
                $ custom2 = ""
                label highisland_crew_trailstart03:
                    menu:
                        '[custom1]After a few minutes, you reach what seems to be a proper trail, beaten, wider than a wagon, and leading both toward the volcano and away from it. Among the thicket you spot the remains of the stone wall, long since collapsed.[custom2]
                        '
                        '“For now, we’ll stick to this route.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “For now, we’ll stick to this route.”')
                            $ highisland_destination = "darkness"
                            jump highisland_destination
            else:
                if efren_highisland_joined and not efren_highisland_blocked:
                    $ custom1 = "Even though {color=#f6d6bd}Efren{/color} tries to lead you, you stumble upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                elif bandit_highisland_joined and not bandit_highisland_blocked:
                    $ custom1 = "Even though {color=#f6d6bd}the bandit{/color} tries to lead you, you stumble upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                elif dalit_highisland_joined and not dalit_highisland_blocked:
                    $ custom1 = "Even though {color=#f6d6bd}Dalit{/color} tries to lead you, you stumble upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                elif shortcut_traveled >= 6:
                    $ custom1 = "Despite all the time you’ve spent exploring the wilderness of the peninsula, you find yourself stumbling upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                elif shortcut_traveled >= 3:
                    $ custom1 = "The time you’ve spent exploring the wilderness of the peninsula has not prepared you for such lush undergrowth. You stumble upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                elif shortcut_traveled >= 1:
                    $ custom1 = "Knowing little about crossing the wilderness, you stumble upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                else:
                    $ custom1 = "Confused, you get lost in the woods, stumbling upon upset monkeys and foxes. Forced to roam, you leave this scrap of land only after a long run through the thicket, annoyed and tired. "
                label highisland_companionexhaustion_loop_trailstart:
                    if highisland_crew_left <= 0:
                        if pc_food:
                            $ pc_food = limit_pc_food(pc_food-2)
                            show minus2food at foodchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                            $ custom2 = "You take a few deep breaths. It’s late, yet the constant hardship is making you hungry."
                        elif pc_hp >= 0:
                            $ custom2 = "You prepare a wet cloth. The nosebleed you got when you slipped on a wet root may become a problem."
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        else:
                            $ custom1 = "Confused, you soon stumble upon upset monkeys and foxes. Forced to roam and gasping for air, you try to flee from their angry shouts, only to get lost deeper in the woods - for good."
                            jump highisland_gameover
                    else:
                        $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus', 'pc'])
                        if highisland_crew_dmg_target == "aegidia":
                            if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                jump highisland_companionexhaustion_loop_trailstart
                            else:
                                if not aegidia_highisland_tired:
                                    $ aegidia_highisland_tired = 1
                                    $ custom2 = "{color=#f6d6bd}Aegidia{/color} prepares a wet cloth. The nosebleed she got when she slipped on a wet root may become a problem - it would be better to not push her too hard."
                                else:
                                    $ aegidia_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "{color=#f6d6bd}Aegidia{/color} looks down as she prepares a wet cloth. She was already exhausted, and with the nosebleed and the swollen eye she got when she slipped on a wet root you doubt she’ll be of much help to you."
                        elif highisland_crew_dmg_target == "dalit":
                            if not dalit_highisland_joined or dalit_highisland_blocked:
                                jump highisland_companionexhaustion_loop_trailstart
                            else:
                                if not dalit_highisland_tired:
                                    $ dalit_highisland_tired = 1
                                    $ custom2 = "{color=#f6d6bd}Dalit{/color} prepares a wet cloth. The nosebleed she got when she slipped on a wet root may become a problem - it would be better to not push her too hard."
                                else:
                                    $ dalit_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "{color=#f6d6bd}Dalit{/color} looks down as she prepares a wet cloth. She was already exhausted, and with the nosebleed and the swollen eye she got when she slipped on a wet root you doubt she’ll be of much help to you."
                        elif highisland_crew_dmg_target == "efren":
                            if not efren_highisland_joined or efren_highisland_blocked:
                                jump highisland_companionexhaustion_loop_trailstart
                            else:
                                if not efren_highisland_tired:
                                    $ efren_highisland_tired = 1
                                    $ custom2 = "{color=#f6d6bd}Efren{/color} prepares a wet cloth. The nosebleed he got when he slipped on a wet root may become a problem - it would be better to not push him too hard."
                                else:
                                    $ efren_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "{color=#f6d6bd}Efren{/color} looks down as he prepares a wet cloth. He was already exhausted, and with the nosebleed and the swollen eye he got when he slipped on a wet root you doubt he’ll be of much help to you."
                        elif highisland_crew_dmg_target == "thyrsus":
                            if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                jump highisland_companionexhaustion_loop_trailstart
                            else:
                                if not thyrsus_highisland_tired:
                                    $ thyrsus_highisland_tired = 1
                                    $ custom2 = "{color=#f6d6bd}Thyrsus{/color} prepares a wet cloth. The nosebleed he got when he slipped on a wet root may become a problem - it would be better to not push him too hard."
                                else:
                                    $ thyrsus_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "{color=#f6d6bd}Thyrsus{/color} looks down as he prepares a wet cloth. He was already exhausted, and with the nosebleed and the swollen eye he got when he slipped on a wet root you doubt he’ll be of much help to you."
                        elif highisland_crew_dmg_target == "pyrrhos":
                            if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                jump highisland_companionexhaustion_loop_trailstart
                            else:
                                if not pyrrhos_highisland_tired:
                                    $ pyrrhos_highisland_tired = 1
                                    $ custom2 = "{color=#f6d6bd}Pyrrhos{/color} prepares a wet cloth. The nosebleed he got when he slipped on a wet root may become a problem - it would be better to not push him too hard."
                                else:
                                    $ pyrrhos_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "{color=#f6d6bd}Pyrrhos{/color} looks down as he prepares a wet cloth. He was already exhausted, and with the nosebleed and the swollen eye he got when he slipped on a wet root you doubt he’ll be of much help to you."
                        elif highisland_crew_dmg_target == "bandit":
                            if not bandit_highisland_joined or bandit_highisland_blocked:
                                jump highisland_companionexhaustion_loop_trailstart
                            else:
                                if not bandit_highisland_tired:
                                    $ bandit_highisland_tired = 1
                                    $ custom2 = "{color=#f6d6bd}The bandit{/color} prepares a wet cloth. The nosebleed he got when he slipped on a wet root may become a problem - it would be better to not push him too hard."
                                else:
                                    $ bandit_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "{color=#f6d6bd}The bandit{/color} looks down as he prepares a wet cloth. He was already exhausted, and with the nosebleed and the swollen eye he got when he slipped on a wet root you doubt he’ll be of much help to you."
                        elif highisland_crew_dmg_target == "tulia":
                            if not tulia_highisland_joined or tulia_highisland_blocked:
                                jump highisland_companionexhaustion_loop_trailstart
                            else:
                                if not tulia_highisland_tired:
                                    $ tulia_highisland_tired = 1
                                    $ custom2 = "{color=#f6d6bd}Tulia{/color} prepares a wet cloth. The nosebleed she got when she slipped on a wet root may become a problem - it would be better to not push her too hard."
                                else:
                                    $ tulia_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "{color=#f6d6bd}Tulia{/color} looks down as she prepares a wet cloth. She was already exhausted, and with the nosebleed and the swollen eye she got when she slipped on a wet root you doubt she’ll be of much help to you."
                        elif highisland_crew_dmg_target == "tzvi":
                            if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                jump highisland_companionexhaustion_loop_trailstart
                            else:
                                if not tzvi_highisland_tired:
                                    $ tzvi_highisland_tired = 1
                                    $ custom2 = "{color=#f6d6bd}Tzvi{/color} prepares a wet cloth. The nosebleed he got when he slipped on a wet root may become a problem - it would be better to not push him too hard."
                                else:
                                    $ tzvi_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "{color=#f6d6bd}Tzvi{/color} looks down as he prepares a wet cloth. He was already exhausted, and with the nosebleed and the swollen eye he got when he slipped on a wet root you doubt he’ll be of much help to you."
                        elif highisland_crew_dmg_target == "quintus":
                            if not quintus_highisland_joined or quintus_highisland_blocked:
                                jump highisland_companionexhaustion_loop_trailstart
                            else:
                                if not quintus_highisland_tired:
                                    $ quintus_highisland_tired = 1
                                    $ custom2 = "{color=#f6d6bd}Quintus{/color} prepares a wet cloth. The nosebleed he got when he slipped on a wet root may become a problem - it would be better to not push him too hard."
                                else:
                                    $ quintus_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "{color=#f6d6bd}Quintus{/color} looks down as he prepares a wet cloth. He was already exhausted, and with the nosebleed and the swollen eye he got when he slipped on a wet root you doubt he’ll be of much help to you."
                        elif highisland_crew_dmg_target == "pc":
                            if pc_food:
                                $ pc_food = limit_pc_food(pc_food-2)
                                show minus2food at foodchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                                $ custom2 = "You take a few deep breaths. It’s late, yet the constant hardship is making you hungry."
                            else:
                                $ custom2 = "You prepare a wet cloth. The nosebleed you got when you slipped on a wet root may become a problem."
                                $ pc_hp = limit_pc_hp(pc_hp-1)
                                show minus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                menu:
                    '[custom1]After a few minutes, you reach what seems to be a proper trail, beaten, wider than a wagon, and leading both toward the volcano and away from it. Among the thicket you spot the remains of the stone wall, long since collapsed.
                    \n\n[custom2]
                    '
                    '“For now, we’ll stick to this route.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “For now, we’ll stick to this route.”')
                        $ highisland_destination = "darkness"
                        jump highisland_destination

label highisland_darknessALL:
    label highisland_solo_darknessALL:
        label highisland_solo_darkness01:
            $ at = 0
            $ at_unlock_spell = 0
            if pc_class == "mage":
                $ at_unlock_spell = 1
                $ manacost = 1
            menu:
                'The further trail is canopied by overhanging trees, blocking the moonlight. You hear panicked hooves and flapping wings, but you can hardly see anything.
                \n\nThe few torches you brought with you won’t last you for long.
                '
                'I fill my axe with the light spell. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill my axe with the light spell.')
                    $ highisland_lightsource = "magic"
                    $ mana = limit_mana(mana-manacost)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                    if oldtunnel_magiclight_color == "white":
                        $ custom1 = "You put your pendant in your teeth. The white flash makes you blink, but then remains as a static glow. You move on, free of the limits of the night sky."
                    elif oldtunnel_magiclight_color == "yellow":
                        $ custom1 = "You put your pendant in your teeth. The yellow glimmer warms up your fingers. You move on, free of the limits of the night sky."
                    elif oldtunnel_magiclight_color == "red":
                        $ custom1 = "You put your pendant in your teeth. The red glow spreads slowly, like a thick liquid. You move on, free of the limits of the night sky, and the light reluctantly follows."
                    elif oldtunnel_magiclight_color == "blue":
                        $ custom1 = "You put your pendant in your teeth. The blue glow spreads with the sound of breaking ice, and covers your hand and lips with a chilling aura. You move on, free of the limits of the night sky."
                    elif oldtunnel_magiclight_color == "green":
                        $ custom1 = "You put your pendant in your teeth. The green glow is warm, trimmed with blues, yellows, and whites. You move on, free of the limits of the night sky, and your axe hums like rustling leaves."
                    elif oldtunnel_magiclight_color == "purple":
                        $ custom1 = "You put your pendant in your teeth. The purple, uneasy glow pulsates, dancing among the leaves with varying strength. You move on, free of the limits of the night sky, trying to ignore the rotten aftertaste on your lips."
                    else:
                        $ custom1 = "You put your pendant in your teeth. The white flash makes you blink, but then remains as a static glow. You move on, free of the limits of the night sky."
                    jump highisland_solo_darkness02
                'I lack pneuma to cast any spell. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and at_unlock_spell" ):
                    pass
                'My lantern is going to be perfect here.' if item_lantern:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- My lantern is going to be perfect here.')
                    $ highisland_lightsource = "lantern"
                    $ custom1 = "You grab your tinderbox, crouch down, and after a few breaths you shove the lit candle into the frame. You stand up and shake the lantern - it holds. You move on, free of the limits of the night sky as the yellow glimmer dances on the leaves."
                    jump highisland_solo_darkness02
                'Maybe my eyes will adjust. For now, I need to rely on my ears.' if not item_lantern:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe my eyes will adjust. For now, I need to rely on my ears.')
                    $ highisland_lightsource = 0
                    $ at = 0
                    $ at_unlock_spell = 0
                    $ highisland_destination = "howlers"
                    jump highisland_destination

        label highisland_solo_darkness02:
            $ at = 0
            $ at_unlock_spell = 0
            menu:
                '[custom1]
                '
                'The plants here are so wet I couldn’t start a forest fire even with a torch.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The plants here are so wet I couldn’t start a forest fire even with a torch.')
                    $ highisland_destination = "howlers"
                    jump highisland_destination

    label highisland_howlers_darkness01:
        $ highisland_lightsource = "lantern"
        menu:
            'The further trail is canopied by overhanging trees, blocking the moonlight. You hear panicked hooves and flapping wings, but you can hardly see anything.
            \n\n{color=#f6d6bd}The guard with the mace{/color} hands you a torch. “The plants here are wet. Should be safe to carry it. For now, I’ve got a lantern we can use.”
            '
            'Maybe the beasts will get scared by so many moving lights.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe the beasts will get scared by so many moving lights.')
                $ highisland_destination = "howlers"
                jump highisland_destination

    label highisland_crew_darknessALL:
        label highisland_crew_darkness01:
            $ at = 0
            $ at_unlock_spell = 0
            if pc_class == "mage":
                $ at_unlock_spell = 1
                $ manacost = 1
            if pyrrhos_highisland_joined and not navica_highisland_joined:
                $ custom11 = "{color=#f6d6bd}Pyrrhos{/color} raises a few of the torches he prepared. “If ye’ve nothing better than this, we should light them up.”"
            elif quintus_highisland_joined:
                $ custom11 = "“No points in having strong arms without eyes,” {color=#f6d6bd}Quintus{/color} grumbles."
            elif aegidia_highisland_joined:
                $ custom11 = "{color=#f6d6bd}Aegidia{/color} steps ahead and looks around. “Brought any light?”"
            elif efren_highisland_joined:
                $ custom11 = "{color=#f6d6bd}Efren{/color} rubs his eyes. “We’re no cats. We need some light.”"
            elif bandit_highisland_joined:
                $ custom11 = "{color=#f6d6bd}The bandit{/color} seems to not be bothered by the darkness, but after he notices that you’ve slowed down, he waits for you."
            elif dalit_highisland_joined:
                $ custom11 = "{color=#f6d6bd}Dalit{/color} pushes some twigs away. “I’ve no light. Do you?”"
            elif tulia_highisland_joined:
                $ custom11 = "{color=#f6d6bd}Tulia{/color} pushes some twigs away. “I’ve no light. Do you?”"
            elif tzvi_highisland_joined:
                $ custom11 = "{color=#f6d6bd}Tzvi{/color} keeps his pace until he stumbles over a rock and gives you a telling look."
            elif thyrsus_highisland_joined:
                $ custom11 = "{color=#f6d6bd}Thyrsus{/color} keeps his pace until he stumbles over a rock and gives you a telling look."
            else:
                $ custom11 = "The few torches you brought with you won’t last you for long."
            menu:
                'The further trail is canopied by overhanging trees, blocking the moonlight. You hear panicked hooves and flapping wings, but you can hardly see anything.
                \n\n[custom11]
                '
                '“Let’s use the lantern {color=#f6d6bd}Navica{/color} gave us. We’ll save her torches for later.”' if highisland_lightsource_artisanready and navica_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s use the lantern {color=#f6d6bd}Navica{/color} gave us. We’ll save her torches for later.”')
                    $ highisland_lightsource = "lantern"
                    $ custom1 = "You grab your tinderbox, crouch down, and after a few breaths you shove the lit candle into the frame. You stand up and shake the lantern - it holds, but isn’t too quiet. You move on, free of the limits of the night sky as the yellow glimmer dances on the leaves."
                    jump highisland_crew_darkness02
                'I grab a few of {color=#f6d6bd}Pyrrhos’{/color} torches.' if highisland_lightsource_artisanready and not navica_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab a few of {color=#f6d6bd}Pyrrhos’{/color} torches.')
                    $ highisland_lightsource_artisanready = 0
                    $ highisland_lightsource = "torches"
                    $ custom1 = "You grab your tinderbox, crouch down, and after a few breaths you lit up two torches. They aren’t much, but are enough to get you through the darkest parts of the woods."
                    jump highisland_crew_darkness02
                'I fill my axe with the light spell. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I fill my axe with the light spell.')
                    $ highisland_lightsource = "magic"
                    $ mana = limit_mana(mana-manacost)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                    if oldtunnel_magiclight_color == "white":
                        $ custom1 = "You put your pendant in your teeth. The white flash makes you blink, but then remains as a static glow. You move on, free of the limits of the night sky."
                    elif oldtunnel_magiclight_color == "yellow":
                        $ custom1 = "You put your pendant in your teeth. The yellow glimmer warms up your fingers. You move on, free of the limits of the night sky."
                    elif oldtunnel_magiclight_color == "red":
                        $ custom1 = "You put your pendant in your teeth. The red glow spreads slowly, like a thick liquid. You move on, free of the limits of the night sky, and the light reluctantly follows."
                    elif oldtunnel_magiclight_color == "blue":
                        $ custom1 = "You put your pendant in your teeth. The blue glow spreads with the sound of breaking ice, and covers your hand and lips with a chilling aura. You move on, free of the limits of the night sky."
                    elif oldtunnel_magiclight_color == "green":
                        $ custom1 = "You put your pendant in your teeth. The green glow is warm, trimmed with blues, yellows, and whites. You move on, free of the limits of the night sky, and your axe hums like rustling leaves."
                    elif oldtunnel_magiclight_color == "purple":
                        $ custom1 = "You put your pendant in your teeth. The purple, uneasy glow pulsates, dancing among the leaves with varying strength. You move on, free of the limits of the night sky, trying to ignore the rotten aftertaste on your lips."
                    else:
                        $ custom1 = "You put your pendant in your teeth. The white flash makes you blink, but then remains as a static glow. You move on, free of the limits of the night sky."
                    jump highisland_crew_darkness02
                'I lack pneuma to cast any spell. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and at_unlock_spell" ):
                    pass
                '“I’ve got a lantern. Don’t worry.”' if item_lantern:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve got a lantern. Don’t worry.”')
                    $ highisland_lightsource = "lantern"
                    $ custom1 = "You grab your tinderbox, crouch down, and after a few breaths you shove the lit candle into the frame. You stand up and shake the lantern - it holds. You move on, free of the limits of the night sky as the yellow glimmer dances on the leaves."
                    jump highisland_crew_darkness02
                '“Maybe our eyes will adjust. For now, we need to rely on our ears.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe our eyes will adjust. For now, we need to rely on our ears.”')
                    $ highisland_lightsource = 0
                    $ at = 0
                    $ at_unlock_spell = 0
                    $ highisland_destination = "howlers"
                    jump highisland_destination

        label highisland_crew_darkness02:
            $ at = 0
            $ at_unlock_spell = 0
            menu:
                '[custom1]
                '
                'I ignore the curious looks of my crew. “Just pay attention to the sounds.”' if highisland_lightsource == "magic":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ignore the curious looks of my crew. “Just pay attention to the sounds.”')
                    $ highisland_destination = "howlers"
                    jump highisland_destination
                'The plants here are so wet even an open flame won’t start a forest fire.' if highisland_lightsource == "torches":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The plants here are so wet even an open flame won’t start a forest fire.')
                    $ highisland_destination = "howlers"
                    jump highisland_destination
                '“Just pay attention to the sounds.”' if highisland_lightsource == "lantern":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just pay attention to the sounds.”')
                    $ highisland_destination = "howlers"
                    jump highisland_destination

label highisland_howlersALL:
    label highisland_solo_howlersALL:
        label highisland_solo_howlers01:
            if northernroad_firsttime:
                $ custom1 = "The familiar yells of howlers fill up the path ahead. The monkeys are moving among the tree crowns, barely visible, and the longer you’re around, the greater the pain thumping inside your skull. Their territory is vast, and they don’t need to attack you to wound you."
            else:
                $ custom1 = "The deep, loud yells of howlers are piercing your ears, concealing any other sound in the area. The monkeys are moving among the tree crowns, barely visible, and the longer you’re around, the greater the pain thumping inside your skull. Their territory is vast, you’ve no time to avoid it."
            jump highisland_solo_howlers01a

        label highisland_solo_howlers01a:
            if highisland_howlers_points <= 0:
                menu:
                    '[custom1]
                    \n\nYou look around - as the number of monkeys dwindles, their noises don’t bother you as much. You take a few steps down the road and the remains of the pack move back, letting you through.
                    '
                    'Now or never. I run forward.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Now or never. I run forward.')
                        $ highisland_destination = "wallofinsects"
                        jump highisland_destination
            else:
                menu:
                    '[custom1]
                    '
                    'I plug my ears.' if item_earplugs and not highisland_howlers_earplugs:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I plug my ears.')
                        $ highisland_howlers_earplugs = 1
                        $ highisland_howlers_points -= 1
                        $ custom1 = "The howling becomes muffled, but as long as you have ears, some of it will reach you."
                        jump highisland_solo_howlers01a
                    'I blow into the dragon horn.' if item_dragonhorn and not highisland_howlers_dragonhorn:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I blow into the dragon horn.')
                        $ highisland_howlers_dragonhorn = 1
                        $ highisland_howlers_points -= 1
                        $ custom1 = "The terrifying bellow of a monster spreads through the night. The howls get higher and whinier as many of the beasts leap away."
                        jump highisland_solo_howlers01a
                    'I shoot one with my crossbow.' if item_crossbow and item_crossbowquarrels and not highisland_howlers_crossbow:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shoot one with my crossbow.')
                        $ highisland_howlers_crossbow = 1
                        $ highisland_howlers_points -= 1
                        $ item_crossbowquarrels -= 1
                        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                        $ custom1 = "You pull the trigger and your target lets out a scream as it falls into the lush bushes."
                        jump highisland_solo_howlers01a
                    'I don’t have any quarrels for my crossbow. (disabled)' if item_crossbow and not item_crossbowquarrels:
                        pass
                    'I don’t have a crossbow. (disabled)' if not item_crossbow:
                        pass
                    '{image=d6} I need to ignore the howls and run ahead.' if not item_shield:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to ignore the howls and run ahead.')
                        jump highisland_solo_howlers02
                    '{image=d6} Holding my shield, I barge through.' if item_shield:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Holding my shield, I barge through.')
                        jump highisland_solo_howlers02

        label highisland_solo_howlers02:
            $ d100roll = renpy.random.randint(1, 100)
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            if item_shield:
                $ d100roll -= 5
            if not highisland_lightsource:
                $ d100roll += 20
            if pc_class == "warrior":
                $ d100roll -= (pc_battlecounter*2)
            else:
                $ d100roll -= (pc_battlecounter)
            $ d100roll += (highisland_howlers_points*30)
            if d100roll <= 50:
                if not highisland_lightsource:
                    $ custom1 = "Despite having no reliable source of light with you, you manage to scare off the few howlers brave enough to get in your way."
                else:
                    $ custom1 = "Having a reliable source of light with you, you manage to scare off the few howlers brave enough to get in your way."
                $ custom2 = ""
                menu:
                    '[custom1][custom2] Without a scratch, you leave the beasts behind.
                    '
                    'I run until my head stops aching.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run until my head stops aching.')
                        $ highisland_destination = "wallofinsects"
                        jump highisland_destination
            else:
                if not highisland_lightsource:
                    $ custom1 = "You barely find your way in the darkness, and a few of the howlers are brave enough to get in your way, slowing you down enough to make the thunderous shouts insufferable."
                else:
                    $ custom1 = "A few of the howlers are brave enough to ignore the light and get in your way, slowing you down enough to make the thunderous shouts insufferable."
                $ custom2 = ""
                if pc_food:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    if not highisland_lightsource:
                        $ custom1 = "You barely find your way in the darkness, and a few of the howlers are brave enough to get in your way, slowing you down enough to make the thunderous shouts insufferable. Seeing how you sway on your feet, they chase after you, staying as loud as they can get.\n\nSuddenly, the forest grows silent, and your eyes fill up with blood."
                    else:
                        $ custom1 = "A few of the howlers are brave enough to ignore the light and get in your way, slowing you down enough to make the thunderous shouts insufferable. Seeing how you sway on your feet, they chase after you, staying as loud as they can get.\n\nSuddenly, the forest grows silent, and your eyes fill up with blood."
                    jump highisland_gameover
                menu:
                    '[custom1][custom2] The monkeys don’t chase after you, but you barely manage to stay on your legs.
                    '
                    'I run until my head stops aching.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run until my head stops aching.')
                        $ highisland_destination = "wallofinsects"
                        jump highisland_destination

    label highisland_howlers_howlersALL:
        label highisland_howlers_howlers01:
            $ highisland_howlers_points -= 1
            if northernroad_firsttime:
                $ custom1 = "The familiar yells of howlers fill up the path ahead. The monkeys are moving among the tree crowns, barely visible, and the longer you’re around, the greater the pain thumping inside your skull. Their territory is vast, and they don’t need to attack you to wound you.\n\n{color=#f6d6bd}The guard with the bow{/color} doesn’t wait. She shoots at a few of the creatures, hitting one of them. “Do something, anything,” shouts {color=#f6d6bd}the one with the spear{/color}."
            else:
                $ custom1 = "The deep, loud yells of howlers are piercing your ears, concealing any other sound in the area. The monkeys are moving among the tree crowns, barely visible, and the longer you’re around, the greater the pain thumping inside your skull. Their territory is vast, you’ve no time to avoid it.\n\n{color=#f6d6bd}The guard with the bow{/color} doesn’t wait. She shoots at a few of the creatures, hitting one of them. “Do something, anything,” shouts {color=#f6d6bd}the one with the spear{/color}."
            jump highisland_howlers_howlers01a

        label highisland_howlers_howlers01a:
            if highisland_howlers_points <= 0:
                menu:
                    '[custom1]
                    \n\nYou look around - as the number of monkeys dwindles, their noises don’t bother you as much. You take a few steps down the road and the remains of the pack move back, letting you through.
                    '
                    'Now or never. “Run!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Now or never. “Run!”')
                        $ highisland_destination = "wallofinsects"
                        jump highisland_destination
            else:
                menu:
                    '[custom1]
                    '
                    'I plug my ears. “Do the same!”' if item_earplugs and not highisland_howlers_earplugs:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I plug my ears. “Do the same!”')
                        $ highisland_howlers_earplugs = 1
                        $ highisland_howlers_points -= 1
                        $ custom1 = "{color=#f6d6bd}The young druid{/color} tears away parts of his woolen tunic, giving the scraps to his companions. The howling becomes muffled, but as long as you have ears, some of it will reach you."
                        jump highisland_howlers_howlers01a
                    'I blow into the dragon horn.' if item_dragonhorn and not highisland_howlers_dragonhorn:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I blow into the dragon horn.')
                        $ highisland_howlers_dragonhorn = 1
                        $ highisland_howlers_points -= 1
                        $ custom1 = "The terrifying bellow of a monster spreads through the night. The howls get higher and whinier as many of the beasts leap away. “More noise?” objects {color=#f6d6bd}the one with the mace{/color}, but after {color=#f6d6bd}the leader{/color} points at the fleeing beasts, you hear no further comments."
                        jump highisland_howlers_howlers01a
                    'I shoot one with my crossbow.' if item_crossbow and item_crossbowquarrels and not highisland_howlers_crossbow:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shoot one with my crossbow.')
                        $ highisland_howlers_crossbow = 1
                        $ highisland_howlers_points -= 1
                        $ item_crossbowquarrels -= 1
                        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                        $ custom1 = "You pull the trigger and your target lets out a scream as it falls into the lush bushes."
                        jump highisland_howlers_howlers01a
                    'I don’t have any quarrels for my crossbow. (disabled)' if item_crossbow and not item_crossbowquarrels:
                        pass
                    'I don’t have a crossbow. (disabled)' if not item_crossbow:
                        pass
                    '{image=d6} “Try to ignore them! We’re going to run to the other side!”' if not item_shield:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Try to ignore them! We’re going to run to the other side!”')
                        jump highisland_howlers_howlers02
                    '{image=d6} I raise my shield. “Try to ignore them! We’re going to run to the other side!”' if item_shield:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I raise my shield. “Try to ignore them! We’re going to run to the other side!”')
                        jump highisland_howlers_howlers02

        label highisland_howlers_howlers02:
            $ d100roll = renpy.random.randint(1, 100)
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            if item_shield:
                $ d100roll -= 5
            if not highisland_lightsource:
                $ d100roll += 20
            if pc_class == "warrior":
                $ d100roll -= (pc_battlecounter*2)
            else:
                $ d100roll -= (pc_battlecounter)
            $ d100roll += (highisland_howlers_points*30)
            if d100roll <= 50:
                if not highisland_lightsource:
                    $ custom1 = "Despite having no reliable source of light with you, you manage to scare off the few howlers brave enough to get in your way."
                else:
                    $ custom1 = "Having a reliable source of light with you, you manage to scare off the few howlers brave enough to get in your way."
                $ custom2 = " Some of {color=#f6d6bd}the guards{/color} are in better shape than you, and help you keep up with their pace."
                menu:
                    '[custom1][custom2] Without a scratch, you leave the beasts behind.
                    '
                    'I run until my head stops aching.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run until my head stops aching.')
                        $ highisland_destination = "wallofinsects"
                        jump highisland_destination
            else:
                if not highisland_lightsource:
                    $ custom1 = "You barely find your way in the darkness, and a few of the howlers are brave enough to get in your way, slowing you down enough to make the thunderous shouts insufferable."
                else:
                    $ custom1 = "A few of the howlers are brave enough to ignore the light and get in your way, slowing you down enough to make the thunderous shouts insufferable."
                $ custom2 = "You slow down, but one of {color=#f6d6bd}the guards{/color} pushes you forward as she lets out a pained shout, forcing you to keep up with the others."
                $ highisland_howlersguards_hp -= 1
                if pc_food:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                menu:
                    '[custom1][custom2] Thankfully, the monkeys don’t chase after you.
                    '
                    'I run until my head stops aching.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run until my head stops aching.')
                        $ highisland_destination = "wallofinsects"
                        jump highisland_destination

    label highisland_crew_howlersALL:
        label highisland_crew_howlers01:
            $ highisland_howlers_points -= 1
            if northernroad_firsttime:
                $ custom1 = "The familiar yells of howlers fill up the path ahead. The monkeys are moving among the tree crowns, barely visible, and the longer you’re around, the greater the pain thumping inside your skull. Their territory is vast, and they don’t need to attack you to wound you."
            else:
                $ custom1 = "The deep, loud yells of howlers are piercing your ears, concealing any other sound in the area. The monkeys are moving among the tree crowns, barely visible, and the longer you’re around, the greater the pain thumping inside your skull. Their territory is vast, you’ve no time to avoid it."
            jump highisland_crew_howlers01a

        label highisland_crew_howlers01a:
            if highisland_howlers_points <= 0:
                menu:
                    '[custom1]
                    \n\nYou look around - as the number of monkeys dwindles, their noises don’t bother you as much. You take a few steps down the road and the remains of the pack move back, letting you through.
                    '
                    'Now or never. “Run!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Now or never. “Run!”')
                        $ highisland_destination = "wallofinsects"
                        jump highisland_destination
            else:
                menu:
                    '[custom1]
                    '
                    'I plug my ears. “Do the same!”' if item_earplugs and not highisland_howlers_earplugs:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I plug my ears. “Do the same!”')
                        $ highisland_howlers_earplugs = 1
                        $ highisland_howlers_points -= 1
                        $ custom1 = "After you throw them a candle, it takes them a few minutes to shove some wax into their ears. The howling becomes muffled, but as long as you have ears, some of it will reach you."
                        jump highisland_crew_howlers01a
                    'I blow into the dragon horn.' if item_dragonhorn and not highisland_howlers_dragonhorn:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I blow into the dragon horn.')
                        $ highisland_howlers_dragonhorn = 1
                        $ highisland_howlers_points -= 1
                        $ custom1 = "The terrifying bellow of a monster spreads through the night. The howls get higher and whinier as many of the beasts leap away."
                        jump highisland_crew_howlers01a
                    '“If you can - shoot them!”' if (aegidia_highisland_joined and not aegidia_highisland_blocked and not highisland_howlers_crewused) or (dalit_highisland_joined and not dalit_highisland_blocked and not highisland_howlers_crewused) or (pyrrhos_highisland_joined and not pyrrhos_highisland_blocked and not highisland_howlers_crewused):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you can - shoot them!”')
                        $ highisland_howlers_crewused += 1
                        if (aegidia_highisland_joined and not aegidia_highisland_blocked) and (dalit_highisland_joined and not dalit_highisland_blocked) and (pyrrhos_highisland_joined and not pyrrhos_highisland_blocked):
                            $ highisland_howlers_points -= 2
                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} is fast, but just barely scratches one of the jumping monkeys - though it’s enough to throw it into a panic. {color=#f6d6bd}Dalit{/color} lands a precise shot into a beast’s head, bursting it open and splattering its contents. {color=#f6d6bd}Pyrrhos’{/color} waits for a bit, but then sends a quarrel into a howlers’ chest, pinnining it to a tree trunk."
                        elif (aegidia_highisland_joined and not aegidia_highisland_blocked) and (dalit_highisland_joined and not dalit_highisland_blocked):
                            $ highisland_howlers_points -= 2
                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} is fast, but just barely scratches one of the jumping monkeys - though it’s enough to throw it into a panic. {color=#f6d6bd}Dalit{/color} lands a precise shot into a beast’s head, bursting it open and splattering its contents."
                        elif (aegidia_highisland_joined and not aegidia_highisland_blocked) and (pyrrhos_highisland_joined and not pyrrhos_highisland_blocked):
                            $ highisland_howlers_points -= 2
                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} is fast, but just barely scratches one of the jumping monkeys - though it’s enough to throw it into a panic. {color=#f6d6bd}Pyrrhos’{/color} waits for a bit, but then sends a quarrel into a howlers’ chest, pinning it to a tree trunk."
                        elif (dalit_highisland_joined and not dalit_highisland_blocked) and (pyrrhos_highisland_joined and not pyrrhos_highisland_blocked):
                            $ highisland_howlers_points -= 2
                            $ custom1 = "{color=#f6d6bd}Dalit{/color} lands a precise shot into a beast’s head, bursting it open and splattering its contents. {color=#f6d6bd}Pyrrhos’{/color} waits for a bit, but then sends a quarrel into a howlers’ chest, pinning it to a tree trunk."
                        elif (aegidia_highisland_joined and not aegidia_highisland_blocked):
                            $ highisland_howlers_points -= 1
                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} is fast, but just barely scratches one of the jumping monkeys - though it’s enough to throw it into a panic."
                        elif (dalit_highisland_joined and not dalit_highisland_blocked):
                            $ highisland_howlers_points -= 1
                            $ custom1 = "{color=#f6d6bd}Dalit{/color} lands a precise shot into a beast’s head, bursting it open and splattering its contents."
                        elif (pyrrhos_highisland_joined and not pyrrhos_highisland_blocked):
                            $ highisland_howlers_points -= 1
                            $ custom1 = "{color=#f6d6bd}Pyrrhos’{/color} waits for a bit, but then sends a quarrel into a howlers’ chest, pinning it to a tree trunk."
                        jump highisland_crew_howlers01a
                    '“Thoughts, {color=#f6d6bd}Aegidia{/color}?”' if aegidia_highisland_joined and not aegidia_highisland_blocked and not aegidia_highisland_opinion and not highisland_howlers_crewused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thoughts, {color=#f6d6bd}Aegidia{/color}?”')
                        $ aegidia_highisland_opinion = 1
                        $ custom1 = "Her lips are twisted in a pained grimace. “Want me to shoot, I’m ready.”"
                        jump highisland_crew_howlers01a
                    '“Thoughts, {color=#f6d6bd}Aegidia{/color}?”' if aegidia_highisland_joined and aegidia_highisland_blocked and not aegidia_highisland_opinion and not highisland_howlers_crewused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thoughts, {color=#f6d6bd}Aegidia{/color}?”')
                        $ aegidia_highisland_opinion = 1
                        $ custom1 = "Her lips are twisted in a pained grimace. “I can {i}try{/i} to shoot, but I can ne focus.”"
                        jump highisland_crew_howlers01a
                    '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and not dalit_highisland_blocked and not dalit_highisland_opinion and not highisland_howlers_crewused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                        $ dalit_highisland_opinion = 1
                        $ custom1 = "She loads her crossbow."
                        jump highisland_crew_howlers01a
                    '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and dalit_highisland_blocked and not dalit_highisland_opinion and not highisland_howlers_crewused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                        $ dalit_highisland_opinion = 1
                        $ custom1 = "She tries to load her crossbow, but her hands are shaking from pain and exhaustion."
                        jump highisland_crew_howlers01a
                    '“Any tips, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and not efren_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips, {color=#f6d6bd}Efren{/color}?”')
                        $ efren_highisland_opinion = 1
                        if not highisland_howlers_earplugs:
                            $ highisland_howlers_earplugs = 1
                            if not item_earplugs:
                                $ item_earplugs = "wax"
                                $ renpy.notify("You add the wax earplugs\nto your travel set.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You add the wax earplugs\nto your travel set.{/i}')
                            $ custom1 = "“Huh?” He pulls out a piece of wax from his ear. “Hwat are we waiting for? You’ve no earplugs? Use this,” he grabs a candle and cuts away small chunks of it. You roll them in your hands and follow his lead. The howling becomes muffled, but as long as you have ears, some of it will reach you."
                        else:
                            $ custom1 = "“Huh?” He pulls out a piece of wax from his ear. “Hwat are we waiting for?”"
                        jump highisland_crew_howlers01a
                    '“{color=#f6d6bd}Thyrsus{/color}, suggestions?”' if thyrsus_highisland_joined and not thyrsus_highisland_blocked and not thyrsus_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, suggestions?”')
                        $ thyrsus_highisland_opinion = 1
                        $ custom1 = "He observes the closest monkey. “Even I canna reach them. {i}But{/i} they’d better not get any closer!”"
                        jump highisland_crew_howlers01a
                    '“{color=#f6d6bd}Thyrsus{/color}, suggestions?”' if thyrsus_highisland_joined and thyrsus_highisland_blocked and not thyrsus_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, suggestions?”')
                        $ thyrsus_highisland_opinion = 1
                        $ custom1 = "He observes the closest monkey. “Even I canna reach them, an’ I’m too weak to fight them.”"
                        jump highisland_crew_howlers01a
                    '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and not pyrrhos_highisland_blocked and not pyrrhos_highisland_opinion and not highisland_howlers_crewused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                        $ pyrrhos_highisland_opinion = 1
                        $ custom1 = "He keeps shaking his beard. “What are we waiting for?”"
                        jump highisland_crew_howlers01a
                    '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and pyrrhos_highisland_blocked and not pyrrhos_highisland_opinion and not highisland_howlers_crewused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                        $ pyrrhos_highisland_opinion = 1
                        $ custom1 = "He glances at you and drops his crossbow on the ground. The quarrel disappears among the shrubs."
                        jump highisland_crew_howlers01a
                    'I look at {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and not bandit_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}the bandit{/color}.')
                        $ bandit_highisland_opinion = 1
                        $ custom1 = "He’s rubbing his temples, looking down."
                        jump highisland_crew_howlers01a
                    '“{color=#f6d6bd}Tulia{/color}, what do you recommend?”' if tulia_highisland_joined and not tulia_highisland_blocked and not tulia_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, what do you recommend?”')
                        $ tulia_highisland_opinion = 1
                        $ custom1 = "The sweat on her forehead forms large droplets. “Let’s stick together, I’ll help you get through.”"
                        jump highisland_crew_howlers01a
                    '“{color=#f6d6bd}Tulia{/color}, what do you recommend?”' if tulia_highisland_joined and tulia_highisland_blocked and not tulia_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, what do you recommend?”')
                        $ tulia_highisland_opinion = 1
                        $ custom1 = "The sweat on her forehead forms large droplets. “May be rough to run through them.”"
                        jump highisland_crew_howlers01a
                    '“Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”' if tzvi_highisland_joined and not tzvi_highisland_blocked and not tzvi_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”')
                        $ tzvi_highisland_opinion = 1
                        $ custom1 = "He’s keeping a thumb in his ear. “Well, they won’t catch {i}me{/i}. I’ll help you, if anything.”"
                        jump highisland_crew_howlers01a
                    '“Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”' if tzvi_highisland_joined and tzvi_highisland_blocked and not tzvi_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”')
                        $ tzvi_highisland_opinion = 1
                        $ custom1 = "He’s keeping a thumb in his ear. “Well, they won’t catch {i}me{/i}, but I can’t promise I’ll keep you safe.”"
                        jump highisland_crew_howlers01a
                    '“{color=#f6d6bd}Quintus{/color}, any ideas?”' if quintus_highisland_joined and not quintus_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Quintus{/color}, any ideas?”')
                        $ quintus_highisland_opinion = 1
                        $ custom1 = "He jumps in place, as if he’s preparing for a brawl. “They’re not {i}that{/i} big! Let’s go!”"
                        jump highisland_crew_howlers01a
                    'I shoot one with my crossbow.' if item_crossbow and item_crossbowquarrels and not highisland_howlers_crossbow:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shoot one with my crossbow.')
                        $ highisland_howlers_crossbow = 1
                        $ highisland_howlers_points -= 1
                        $ item_crossbowquarrels -= 1
                        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                        $ custom1 = "You pull the trigger and your target lets out a scream as it falls into the lush bushes."
                        jump highisland_crew_howlers01a
                    'I don’t have any quarrels for my crossbow. (disabled)' if item_crossbow and not item_crossbowquarrels:
                        pass
                    'I don’t have a crossbow. (disabled)' if not item_crossbow:
                        pass
                    '{image=d6} “Try to ignore them! We’re going to run to the other side!”' if not item_shield:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Try to ignore them! We’re going to run to the other side!”')
                        jump highisland_crew_howlers02
                    '{image=d6} I raise my shield. “Try to ignore them! We’re going to run to the other side!”' if item_shield:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I raise my shield. “Try to ignore them! We’re going to run to the other side!”')
                        jump highisland_crew_howlers02

        label highisland_crew_howlers02:
            $ d100roll = renpy.random.randint(1, 100)
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            if item_shield:
                $ d100roll -= 5
            if pc_class == "warrior":
                $ d100roll -= (pc_battlecounter*2)
            else:
                $ d100roll -= (pc_battlecounter)
            if not highisland_lightsource:
                $ d100roll += 20
            if quintus_highisland_joined and not quintus_highisland_blocked:
                $ d100roll -= 15
            if thyrsus_highisland_joined and not thyrsus_highisland_blocked:
                $ d100roll -= 10
            if tulia_highisland_joined and not tulia_highisland_blocked:
                $ d100roll -= 10
            if tzvi_highisland_joined and not tzvi_highisland_blocked:
                $ d100roll -= 10
            $ d100roll += (highisland_howlers_points*30)
            if d100roll <= 60:
                if not highisland_lightsource:
                    $ custom1 = "Despite having no reliable source of light with you, you manage to scare off the few howlers brave enough to get in your way."
                else:
                    $ custom1 = "Having a reliable source of light with you, you manage to scare off the few howlers brave enough to get in your way."
                if quintus_highisland_joined and not quintus_highisland_blocked:
                    $ custom2 = "Following {color=#f6d6bd}Quintus’{/color} unstoppable charge, you leave the beasts behind, without a scratch."
                elif thyrsus_highisland_joined and not thyrsus_highisland_blocked:
                    $ custom2 = "Staying right behind {color=#f6d6bd}Thyrsus’{/color} unstoppable creepers, you leave the beasts behind, without a scratch."
                elif tulia_highisland_joined and not tulia_highisland_blocked:
                    $ custom2 = "Having {color=#f6d6bd}Tulia{/color} by your side, ready to stab whatever gets close to you, you soon leave the beasts behind, without a scratch."
                elif tzvi_highisland_joined and not tzvi_highisland_blocked:
                    $ custom2 = "{color=#f6d6bd}Tzvi{/color} outruns you quickly, but once he realizes this, he helps you catch up with him. You soon leave the beasts behind, without a scratch."
                else:
                    $ custom2 = "Your crew sticks close to you and you soon leave the beasts behind, without a scratch."
                menu:
                    '[custom1] [custom2]
                    '
                    'I run until my head stops aching.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run until my head stops aching.')
                        $ highisland_destination = "wallofinsects"
                        jump highisland_destination
            else:
                if not highisland_lightsource:
                    $ custom1 = "You barely find your way in the darkness, and a few of the howlers are brave enough to get in your way, slowing you down enough to make the thunderous shouts insufferable."
                else:
                    $ custom1 = "A few of the howlers are brave enough to ignore the light and get in your way, slowing you down enough to make the thunderous shouts insufferable."
                label highisland_companiondamage_loop_howlers:
                    if highisland_crew_left <= 0:
                        $ custom2 = "Overwhelmed, you fall to the ground, bleeding from an ear, but a friendly hand helps you get up, encouraging you to speed up."
                        if pc_food:
                            $ pc_food = limit_pc_food(pc_food-2)
                            show minus2food at foodchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                        elif pc_hp > 0:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        else:
                            if not highisland_lightsource:
                                $ custom1 = "You barely find your way in the darkness, and a few of the howlers are brave enough to get in your way, slowing you down enough to make the thunderous shouts insufferable. Seeing how you sway on your feet, they chase after you, staying as loud as they can get.\n\nSuddenly, the forest grows silent, and your eyes fill up with blood."
                            else:
                                $ custom1 = "A few of the howlers are brave enough to ignore the light and get in your way, slowing you down enough to make the thunderous shouts insufferable. Seeing how you sway on your feet, they chase after you, staying as loud as they can get.\n\nSuddenly, the forest grows silent, and your eyes fill up with blood."
                            jump highisland_gameover
                    else:
                        $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus', 'pc'])
                        if highisland_crew_dmg_target == "aegidia":
                            if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                jump highisland_companiondamage_loop_howlers
                            else:
                                $ aegidia_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom2 = "{color=#f6d6bd}Aegidia{/color}, already overwhelmed, falls to the ground, bleeding from an ear. You help her get up, encouraging her to speed up."
                        elif highisland_crew_dmg_target == "dalit":
                            if not dalit_highisland_joined or dalit_highisland_blocked:
                                jump highisland_companiondamage_loop_howlers
                            else:
                                $ dalit_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom2 = "{color=#f6d6bd}Dalit{/color}, already overwhelmed, falls to the ground, bleeding from an ear. You help her get up, encouraging her to speed up."
                        elif highisland_crew_dmg_target == "efren":
                            if not efren_highisland_joined or efren_highisland_blocked:
                                jump highisland_companiondamage_loop_howlers
                            else:
                                $ efren_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom2 = "{color=#f6d6bd}Efren{/color}, already overwhelmed, falls to the ground, bleeding from an ear. You help him get up, encouraging him to speed up."
                        elif highisland_crew_dmg_target == "thyrsus":
                            if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                jump highisland_companiondamage_loop_howlers
                            else:
                                $ thyrsus_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom2 = "{color=#f6d6bd}Thyrsus{/color}, already overwhelmed, falls to the ground, bleeding from an ear. You help him get up, encouraging him to speed up."
                        elif highisland_crew_dmg_target == "pyrrhos":
                            if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                jump highisland_companiondamage_loop_howlers
                            else:
                                $ pyrrhos_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom2 = "{color=#f6d6bd}Pyrrhos{/color}, already overwhelmed, falls to the ground, bleeding from an ear. You help him get up, encouraging him to speed up."
                        elif highisland_crew_dmg_target == "bandit":
                            if not bandit_highisland_joined or bandit_highisland_blocked:
                                jump highisland_companiondamage_loop_howlers
                            else:
                                $ bandit_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom2 = "{color=#f6d6bd}The bandit{/color}, already overwhelmed, falls to the ground, bleeding from an ear. You help him get up, encouraging him to speed up."
                        elif highisland_crew_dmg_target == "tulia":
                            if not tulia_highisland_joined or tulia_highisland_blocked:
                                jump highisland_companiondamage_loop_howlers
                            else:
                                $ tulia_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom2 = "{color=#f6d6bd}Tulia{/color}, already overwhelmed, falls to the ground, bleeding from an ear. You help her get up, encouraging her to speed up."
                        elif highisland_crew_dmg_target == "tzvi":
                            if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                jump highisland_companiondamage_loop_howlers
                            else:
                                $ tzvi_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom2 = "{color=#f6d6bd}Tzvi{/color}, already overwhelmed, falls to the ground, bleeding from an ear. You help him get up, encouraging him to speed up."
                        elif highisland_crew_dmg_target == "quintus":
                            if not quintus_highisland_joined or quintus_highisland_blocked:
                                jump highisland_companiondamage_loop_howlers
                            else:
                                $ quintus_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom2 = "{color=#f6d6bd}Quintus{/color}, already overwhelmed, falls to the ground, bleeding from an ear. You help him get up, encouraging him to speed up."
                        elif highisland_crew_dmg_target == "pc":
                            $ custom2 = "Overwhelmed, you fall on the ground, bleeding from an ear, but a friendly hand helps you get up, encouraging you to speed up."
                            if pc_food:
                                $ pc_food = limit_pc_food(pc_food-2)
                                show minus2food at foodchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                            elif pc_hp > 0:
                                $ pc_hp = limit_pc_hp(pc_hp-1)
                                show minus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            else:
                                if not highisland_lightsource:
                                    $ custom1 = "You barely find your way in the darkness, and a few of the howlers are brave enough to get in your way, slowing you down enough to make the thunderous shouts insufferable. Seeing how you sway on your feet, they chase after you, staying as loud as they can get.\n\nSuddenly, the forest grows silent, and your eyes fill up with blood."
                                else:
                                    $ custom1 = "A few of the howlers are brave enough to ignore the light and get in your way, slowing you down enough to make the thunderous shouts insufferable. Seeing how you sway on your feet, they chase after you, staying as loud as they can get.\n\nSuddenly, the forest grows silent, and your eyes fill up with blood."
                                jump highisland_gameover
                menu:
                    '[custom1] [custom2] Thankfully, the monkeys don’t chase after you.
                    '
                    'I run until my head stops aching.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run until my head stops aching.')
                        $ highisland_destination = "wallofinsects"
                        jump highisland_destination

label highisland_wallofinsectsALL:
    label highisland_solo_wallofinsects01:
        $ custom1 = "The relief is short. The pond ahead is swarmed with buzzing insects, and, judging by the bones of a dragonling you see on the bank, they’re as hungry as they are numerous. The only road ahead leads through them, and you may lack the strength to walk around their feeding ground."
        jump highisland_solo_wallofinsects01a

    label highisland_solo_wallofinsects01a:
        menu:
            '[custom1]
            '
            'Good thing I took the sting ointment with me.' if item_stingointment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Good thing I took the sting ointment with me.')
                menu:
                    'The scent of lavender, mint, and basil blends into the humid wilderness. You cover every ounce of your skin, wrap yourself up with scraps of fabric, then head straight into the cloud of wings.
                    \n\nThe creatures split in front of you, forming a dark tunnel. Their loud wings shine in the moonlight.
                    '
                    'Through the gaps between them I see the hills, and the volcano above them.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Through the gaps between them I see the hills, and the volcano above them.')
                        $ highisland_destination = "monitorlizards"
                        jump highisland_destination
            'They’ll eat me alive. I need to go through the woods.' if not item_stingointment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- They’ll eat me alive. I need to go through the woods.')
                if highisland_lightsource:
                    $ custom1 = "The light you’re carrying is not of great help here, but it helps you scare away a few curious cats. When you reach another part of the road, far away from the pond, you’re tired, but alive."
                    if pc_food:
                        $ pc_food = limit_pc_food(pc_food-2)
                        show minus2food at foodchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    $ custom1 = "Having no source of light, you barely escape the hungry cats. When you reach another part of the road, far away from the pond, you’re tired from running with your heavy bags."
                    if not cleanliness_clothes_torn:
                        $ cleanliness_clothes_torn = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                    if pc_food:
                        $ pc_food = limit_pc_food(pc_food-2)
                        show minus2food at foodchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                    elif pc_hp > 0:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                    else:
                        $ custom1 = "Having no source of light, you don’t even notice the cat that jumps at you from a tree, breaking your neck in an instant."
                        jump highisland_gameover
                menu:
                    '[custom1]
                    '
                    'I lean against a tree, taking a few breaths. I can see the volcano from here.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lean against a tree, taking a few breaths. I can see the volcano from here.')
                        $ highisland_destination = "monitorlizards"
                        jump highisland_destination

    label highisland_howlers_wallofinsects01:
        $ custom1 = "The relief is short-lived. The pond ahead is swarmed with buzzing insects, and, judging by the bones of a dragonling you see on the bank, they’re as hungry as they are numerous. The only road ahead leads through them, and you may lack the strength to walk around their feeding ground.\n\n{color=#f6d6bd}The leader{/color} scratches his chin. “They’ll eat us alive. Let’s light up all the torches we’re ne using, shelter ourselves with smoke.”"
        jump highisland_howlers_wallofinsects01a

    label highisland_howlers_wallofinsects01a:
        menu:
            '[custom1]
            '
            '“I’ve got a reliable sting ointment with me. Let’s use it instead.”' if item_stingointment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve got a reliable sting ointment with me. Let’s use it instead.”')
                menu:
                    'The scent of lavender, mint, and basil blends into the humid wilderness. Your group covers every ounce of their skin and wraps themselves up with scraps of fabric, but waits for you to enter the cloud of wings first. “{color=#f6d6bd}Thais{/color} may want us to protect you,” says {color=#f6d6bd}the one with the mace{/color}, “but I’m ne cutting ma own throat for you.”
                    \n\nThe creatures split in front of you, forming a dark tunnel. Their loud wings shine in the moonlight.
                    '
                    'Through the gaps between them I see the hills, and the volcano above them.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Through the gaps between them I see the hills, and the volcano above them.')
                        $ highisland_destination = "monitorlizards"
                        jump highisland_destination
            '“I guess we’ve no other choice.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I guess we’ve no other choice.”')
                if highisland_lightsource_artisanready:
                    $ highisland_lightsource_artisanready = 0
                else:
                    $ highisland_lightsource = 0
                menu:
                    'After you prepare the first flame, it’s easy to spread it. Each of you holds at least four burning torches, doing your best to not touch the hot oil as it drips on the ground. The smoke surrounds you like a dome, then disappears in the night sky.
                    \n\nThe creatures split in front of you, forming a dark tunnel. You’re getting sweaty from the fire.
                    '
                    'At least we can put out these torches in the water.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least we can put out these torches in the water.')
                        $ highisland_destination = "monitorlizards"
                        jump highisland_destination
            '“We should go through the woods for a bit, save the supplies that we have.”' if not highisland_wallofinsects_howlersrefused:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should go through the woods for a bit, save the supplies that we have.”')
                $ highisland_wallofinsects_howlersrefused = 1
                $ custom1 = "{color=#f6d6bd}The one with the spear{/color} scoffs. “Do ne be stupid. Waste of time en effort.”"
                jump highisland_howlers_wallofinsects01a

    label highisland_crew_wallofinsects01:
        $ custom1 = "The relief is short-lived. The pond ahead is swarmed with buzzing insects, and, judging by the bones of a dragonling you see on the bank, they’re as hungry as they are numerous. The only road ahead leads through them, and you may lack the strength to walk around their feeding ground."
        jump highisland_crew_wallofinsects01a

    label highisland_crew_wallofinsects01a:
        menu:
            '[custom1]
            '
            'I pull out the sting ointment. “Let’s get to it.”' if item_stingointment and not thyrsus_highisland_opinion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pull out the sting ointment. “Let’s get to it.”')
                jump highisland_crew_wallofinsects01b
            'I open the jar. “Fine. Let’s give it a shot.”' if item_stingointment and thyrsus_highisland_opinion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the jar. “Fine. Let’s give it a shot.”')
                label highisland_crew_wallofinsects01b:
                    menu:
                        'The scent of lavender, mint, and basil blends into the humid wilderness. Your group covers every ounce of their skin and wraps themselves up with scraps of fabric, but waits for you to enter the cloud of wings first.
                        \n\nThe creatures split in front of you, forming a dark tunnel. Their loud wings shine in the moonlight.
                        '
                        'Through the gaps between them I see the hills, and the volcano above them.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Through the gaps between them I see the hills, and the volcano above them.')
                            $ highisland_destination = "monitorlizards"
                            jump highisland_destination
            '“{color=#f6d6bd}Thyrsus{/color}, suggestions?”' if thyrsus_highisland_joined and not item_stingointment and not thyrsus_highisland_opinion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, suggestions?”')
                $ thyrsus_shop_stingointment = 1
                $ thyrsus_highisland_opinion = 1
                $ item_stingointment = 1
                $ renpy.notify("You received the sting ointment.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the sting ointment.{/i}')
                $ custom1 = "He leans away, looking for something in his pockets. “I never sold you the sting ointment? I guess not. Take this,” he hands you a small jar. “It will do wonders.”"
                jump highisland_crew_wallofinsects01a
            '“Let’s light up all the torches we have. We brought another source of light anyway.”' if highisland_lightsource_artisanready:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s light up all the torches we have. We brought another source of light anyway.”')
                $ highisland_lightsource_artisanready = 0
                jump highisland_crew_wallofinsects01c
            '“Let’s light up all the torches we have. The smoke will protect us, though we’ll then travel without light.”' if not highisland_lightsource_artisanready and highisland_lightsource == "torches":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s light up all the torches we have. The smoke will protect us, though we’ll then travel without light.”')
                $ highisland_lightsource = 0
                label highisland_crew_wallofinsects01c:
                    menu:
                        'After you prepare the first flame, it’s easy to spread it. Each of you holds at least four burning torches, doing your best to not touch the hot oil as it drips on the ground. The smoke surrounds you like a dome, then disappears in the night sky.
                        \n\nThe creatures split in front of you, forming a dark tunnel. You’re getting sweaty from the fire.
                        '
                        'At least we can put out these torches in the water.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least we can put out these torches in the water.')
                            $ highisland_destination = "monitorlizards"
                            jump highisland_destination
            '“We should go through the woods for a bit, save the supplies that we have.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should go through the woods for a bit, save the supplies that we have.”')
                if not cleanliness_clothes_torn:
                    $ cleanliness_clothes_torn = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                if highisland_lightsource:
                    $ custom1 = "The light you’re carrying is not of great help here, but it helps you scare away a few curious cats."
                else:
                    $ custom1 = "Having no source of light, you struggle to move forward."
                label highisland_companionexhaustion_loop_wallofinsects:
                    if highisland_crew_left <= 0:
                        if highisland_lightsource:
                            $ custom2 = "At one point, you almost fail to dodge a falling branch - after you leap away, you tumble down the hill. After that, you struggle to keep up your pace, even after you reach another part of the road."
                            if pc_food:
                                $ pc_food = limit_pc_food(pc_food-2)
                                show minus2food at foodchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                            else:
                                $ pc_hp = limit_pc_hp(pc_hp-1)
                                show minus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        else:
                            $ custom2 = "Even though your group manages to help you, by the time you reach another part of the road, far away from the pond, you’re tired from running with your heavy bags."
                            if pc_food:
                                $ pc_food = limit_pc_food(pc_food-2)
                                show minus2food at foodchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                            elif pc_hp > 0:
                                $ pc_hp = limit_pc_hp(pc_hp-1)
                                show minus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            else:
                                $ custom1 = "Having no source of light, you don’t even notice the cat that jumps at you from a tree, breaking your neck in an instant."
                                jump highisland_gameover
                    else:
                        $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus', 'pc'])
                        if highisland_crew_dmg_target == "aegidia":
                            if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                jump highisland_companionexhaustion_loop_wallofinsects
                            else:
                                if not aegidia_highisland_tired:
                                    $ aegidia_highisland_tired = 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Aegidia{/color} almost fails to dodge a falling branch. She leaps away, but tumbles down the hill. She struggles to keep up with you, even after you reach another part of the road."
                                else:
                                    $ aegidia_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Aegidia{/color} almost fails to dodge a falling branch. She leaps away, but tumbles down the hill. She struggles to keep up with you, even after you reach another part of the road. You doubt she’s going to be of much help during combat."
                        elif highisland_crew_dmg_target == "dalit":
                            if not dalit_highisland_joined or dalit_highisland_blocked:
                                jump highisland_companionexhaustion_loop_wallofinsects
                            else:
                                if not dalit_highisland_tired:
                                    $ dalit_highisland_tired = 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Dalit{/color} almost fails to dodge a falling branch. She leaps away, but tumbles down the hill. She struggles to keep up with you, even after you reach another part of the road."
                                else:
                                    $ dalit_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Dalit{/color} almost fails to dodge a falling branch. She leaps away, but tumbles down the hill. She struggles to keep up with you, even after you reach another part of the road. You doubt she’s going to be of much help during combat."
                        elif highisland_crew_dmg_target == "efren":
                            if not efren_highisland_joined or efren_highisland_blocked:
                                jump highisland_companionexhaustion_loop_wallofinsects
                            else:
                                if not efren_highisland_tired:
                                    $ efren_highisland_tired = 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Efren{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road."
                                else:
                                    $ efren_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Efren{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road. You doubt he’s going to be of much help during combat."
                        elif highisland_crew_dmg_target == "thyrsus":
                            if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                jump highisland_companionexhaustion_loop_wallofinsects
                            else:
                                if not thyrsus_highisland_tired:
                                    $ thyrsus_highisland_tired = 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Thyrsus{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road."
                                else:
                                    $ thyrsus_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Thyrsus{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road. You doubt he’s going to be of much help during combat."
                        elif highisland_crew_dmg_target == "pyrrhos":
                            if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                jump highisland_companionexhaustion_loop_wallofinsects
                            else:
                                if not pyrrhos_highisland_tired:
                                    $ pyrrhos_highisland_tired = 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Pyrrhos{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road."
                                else:
                                    $ pyrrhos_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Pyrrhos{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road. You doubt he’s going to be of much help during combat."
                        elif highisland_crew_dmg_target == "bandit":
                            if not bandit_highisland_joined or bandit_highisland_blocked:
                                jump highisland_companionexhaustion_loop_wallofinsects
                            else:
                                if not bandit_highisland_tired:
                                    $ bandit_highisland_tired = 1
                                    $ custom2 = "At one point, {color=#f6d6bd}the bandit{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road."
                                else:
                                    $ bandit_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "At one point, {color=#f6d6bd}the bandit{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road. You doubt he’s going to be of much help during combat."
                        elif highisland_crew_dmg_target == "tulia":
                            if not tulia_highisland_joined or tulia_highisland_blocked:
                                jump highisland_companionexhaustion_loop_wallofinsects
                            else:
                                if not tulia_highisland_tired:
                                    $ tulia_highisland_tired = 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Tulia{/color} almost fails to dodge a falling branch. She leaps away, but tumbles down the hill. She struggles to keep up with you, even after you reach another part of the road."
                                else:
                                    $ tulia_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Tulia{/color} almost fails to dodge a falling branch. She leaps away, but tumbles down the hill. She struggles to keep up with you, even after you reach another part of the road. You doubt she’s going to be of much help during combat."
                        elif highisland_crew_dmg_target == "tzvi":
                            if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                jump highisland_companionexhaustion_loop_wallofinsects
                            else:
                                if not tzvi_highisland_tired:
                                    $ tzvi_highisland_tired = 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Tzvi{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road."
                                else:
                                    $ tzvi_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Tzvi{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road. You doubt he’s going to be of much help during combat."
                        elif highisland_crew_dmg_target == "quintus":
                            if not quintus_highisland_joined or quintus_highisland_blocked:
                                jump highisland_companionexhaustion_loop_wallofinsects
                            else:
                                if not quintus_highisland_tired:
                                    $ quintus_highisland_tired = 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Quintus{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road."
                                else:
                                    $ quintus_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom2 = "At one point, {color=#f6d6bd}Quintus{/color} almost fails to dodge a falling branch. He leaps away, but tumbles down the hill. He struggles to keep up with you, even after you reach another part of the road. You doubt he’s going to be of much help during combat."
                        elif highisland_crew_dmg_target == "pc":
                            if highisland_lightsource:
                                $ custom2 = "At one point, you almost fail to dodge a falling branch - after you leap away, you tumble down the hill. After that, you struggle to keep up your pace, even after you reach another part of the road."
                                if pc_food:
                                    $ pc_food = limit_pc_food(pc_food-2)
                                    show minus2food at foodchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                                else:
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            else:
                                $ custom2 = "Even though your group manages to help you, by the time you reach another part of the road, far away from the pond, you’re tired from running with your heavy bags."
                                if pc_food:
                                    $ pc_food = limit_pc_food(pc_food-2)
                                    show minus2food at foodchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                                elif pc_hp > 0:
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                else:
                                    $ custom1 = "Having no source of light, you don’t even notice the cat that jumps at you from a tree, breaking your neck in an instant."
                                    jump highisland_gameover
                menu:
                    '[custom1] [custom2]
                    '
                    'I lean against a tree, taking a few breaths. I can see the volcano from here.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lean against a tree, taking a few breaths. I can see the volcano from here.')
                        $ highisland_destination = "monitorlizards"
                        jump highisland_destination

# label highisland_villageedgeALL: wioska goblinów - jest rozproszeniem, które odciąga od innej przeszkody. mapa ratuje. PLACEHOLDER
# - “Spalona polana, zwęglone krzewy i drzewa. Stojąc tam, ciało przechodzą dreszcze, czuć zimno” - można się wcześniej dowiedzieć, że to miejsce wysysa manę
# nieumarli z miasta?
#     # 3) ścieżka do wulkanu (małe ruiny na poboczu zwodzą - ratuje pyrrhos)
#     # giantstatue_pray_map_learned
#     # efren
#     # tzvi
#     # trochę dalit
#
#     # - gobliny - można przepędzić moczem
#     # item_trollurine = 0
#     # inaczej - walka? - thyrsus, tulia, tzvi, quintus
#     # navica, pyrrhos - jeśli 4 osoby highisland_crew_left >= 3/4, to można użyć jej pochodni, by przepędzić
#     # quintus_about_fatsmoke - jeśli:
#     # item_chicken = 0
#     # item_rawfishtotalnumber = 0
#     # item_stoat = 0 # 1 - owned, bad quality, 2 - owned, good quality
#     # item_furlesswolftrophy = 0 # 1 - owned
#     # i źródło ognia: navica, pyrrhos, (efren?)
#     label highisland_solo_villageedgeALL:
#         label highisland_solo_villageedge01:
#             $ custom1 = ""
#             jump highisland_solo_villageedge01a
#
#         label highisland_solo_villageedge01a:
#             menu:
#                 '[custom1]
#                 '
#                 '':
#                     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
#                     $ custom1 = ""
#                     jump highisland_solo_villageedge01a
#
#     label highisland_howlers_villageedgeALL:
#         label highisland_howlers_villageedge01:
#             $ custom1 = ""
#             jump highisland_howlers_villageedge01a
#
#         label highisland_howlers_villageedge01a:
#             menu:
#                 '[custom1]
#                 '
#                 '':
#                     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
#                     $ custom1 = ""
#                     jump highisland_howlers_villageedge01a
#
#     label highisland_crew_villageedgeALL:
#         label highisland_crew_villageedge01:
#             $ custom1 = ""
#             jump highisland_crew_villageedge01a
#
#         label highisland_crew_villageedge01a:
#             menu:
#                 '[custom1]
#                 '
#                 '':
#                     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
#                     $ custom1 = ""
#                     jump highisland_crew_villageedge01a

label highisland_monitorlizardsALL:
    label highisland_solo_monitorlizardsALL:
        label highisland_solo_monitorlizards01:
            $ custom1 = "You reach a humble valley. The trees here are sparse, and the stream, while gentle, has completely distorted the path. At least the moonlight can guide you.\n\nThe black saurians, covered with yellow spots, are too numerous to count, laying just a few steps away from one another, from the grasses to the branches. Most of them are asleep, but a few of the closer ones give you curious glances, sticking out and hiding their forked tongues rapidly. The beasts aren’t massive, maybe two steps long.\n\nYou look to the sides. The hills are impassable."
            jump highisland_solo_monitorlizards01a

        label highisland_solo_monitorlizards01a:
            menu:
                '[custom1]
                '
                'I examine the surroundings.' if not highisland_monitorlizards_observearea:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the surroundings.')
                    $ highisland_monitorlizards_observearea = 1
                    $ custom1 = "You vaguely recognize the shapes of fruit trees and shrubs, but no animals seem to browse on them. You crouch down - the road is marked with fresh prints left by various creatures."
                    jump highisland_solo_monitorlizards01a
                'I could learn something about them if I were to feed them. I search my bags.' if not highisland_monitorlizards_tryingtofeed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could learn something about them if I were to feed them. I search my bags.')
                    $ highisland_monitorlizards_tryingtofeed = 1
                    if item_rations >= 2:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_stoat:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_rawfishtotalnumber:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_chicken:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_wildplants:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if highisland_monitorlizards_tryingtofeed_narration_points >= 3:
                        $ custom1 = "You’ve got plenty of food to choose from, though you doubt the animals are going to be especially picky."
                    elif highisland_monitorlizards_tryingtofeed_narration_points >= 1:
                        $ custom1 = "You don’t have that many options to choose from."
                    else:
                        $ custom1 = "You find only crumbs and leftovers."
                    jump highisland_solo_monitorlizards01a
                'I throw them the meaty bits from my food rations.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_rations >= 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw them the meaty bits from my food rations.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_rations -= 1
                    $ renpy.notify("You lost a ration.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a ration.{/i}')
                    $ custom1 = "You approach the nearest creature and toss it the tasty scraps. It keeps moving its tongue, but steps away."
                    jump highisland_solo_monitorlizards01a
                'My last food ration has almost no meat. (disabled)' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_rations == 1:
                    pass
                'A raw fish should be enough.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_rawfishtotalnumber:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- A raw fish should be enough.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_rawfishtotalnumber -= 1
                    $ item_rawfish_losing = 1
                    $ renpy.notify("You have %s fish left." %item_rawfishtotalnumber)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You have %s fish left.{/i}' %item_rawfishtotalnumber)
                    $ custom1 = "You approach the nearest creature and toss it the fresh meal. It keeps moving its tongue, but steps away."
                    jump highisland_solo_monitorlizards01a
                'I grab the chicken from {color=#f6d6bd}Creeks{/color}.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_chicken:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the chicken from {color=#f6d6bd}Creeks{/color}.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_chicken -= 1
                    $ renpy.notify("You lost a chicken.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a chicken.{/i}')
                    $ custom1 = "You approach the nearest creature and toss it the aromatic meal. It keeps moving its tongue, but steps away."
                    jump highisland_solo_monitorlizards01a
                'Maybe the dead stoat will lure them away.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_stoat:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe the dead stoat will lure them away.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_stoat = 0
                    $ renpy.notify("You lost the stoat.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the stoat.{/i}')
                    $ custom1 = "You approach the nearest creature and toss it the fresh meal. It keeps moving its tongue, but steps away."
                    jump highisland_solo_monitorlizards01a
                'I wonder if they’ll go after some wild plants I picked.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_plants and item_wildplants:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder if they’ll go after some wild plants I picked.')
                    $ highisland_monitorlizards_tryingtofeed_plants = 1
                    $ item_wildplants -= 1
                    $ renpy.notify("You lost a bunch of wild plants.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a bunch of wild plants.{/i}')
                    $ custom1 = "You throw the saurian a few fruits and rolled up leaves. Distrustful at first, it steps closer and takes care of them with but a few chomps."
                    jump highisland_solo_monitorlizards01a
                '{image=d6} I move slowly, drawing as little attention as possible.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I move slowly, drawing as little attention as possible.')
                    menu:
                        'Your careful steps are greeted with hisses, but the beasts either stay in their spots, not bothering you as you walk around them, or move out of your way, crossing the stream. A few of them don’t even wake up.
                        \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                        '
                        'I glance at the volcano. I’m halfway there.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. I’m halfway there.')
                            $ highisland_destination = "camp1"
                            jump highisland_destination
                '{image=d6} I’ll stay on the main path and run by them quickly.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ll stay on the main path and run by them quickly.')
                    $ d100roll = renpy.random.randint(1, 100)
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 10
                    if armor == 4:
                        $ d100roll -= 5
                    if highisland_lightsource:
                        $ d100roll -= 10
                    if d100roll <= 40:
                        menu:
                            'You adjust your equipment and dash forward. The first few surprised beasts move out of your way, but their loud hisses and the splashes they make in the flowing water alert their companions. The largest ones are ready to face you, and you just barely find a gap between them. Unscathed, you get out of there.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. I’m halfway there.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. I’m halfway there.')
                                $ highisland_destination = "camp1"
                                jump highisland_destination
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
                        else:
                            $ custom1 = "You adjust your equipment and dash forward. The first few surprised beasts move out of your way, but their loud hisses and the splashes they make in the flowing water alert their companions. The largest ones are ready to face you, and you fail to find a gap between them.\n\nOne moment of hesitation is enough to punish you - a tail whips your side, knocking you to the ground, and you don’t have time to get away from the sharp claws of another tree-climber."
                            jump highisland_gameover
                        menu:
                            'You adjust your equipment and dash forward. The first few surprised beasts move out of your way, but their loud hisses and the splashes they make in the flowing water alert their companions. The largest ones are ready to face you, and you fail to find a gap between them.
                            \n\nOne moment of hesitation is enough to punish you - a tail whips your side, knocking you to the ground, and you just barely get away from the sharp claws of another tree-climber. Seeing the emerging wave of black-and-yellow shapes, you run for your life.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. I’m halfway there.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. I’m halfway there.')
                                $ highisland_destination = "camp1"
                                jump highisland_destination
                '{image=d6} I need to prepare my equipment and get ready to fight the saurians off.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to prepare my equipment and get ready to fight the saurians off.')
                    $ d100roll = renpy.random.randint(1, 100)
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 10
                    if armor == 4:
                        $ d100roll -= 5
                    if item_shield:
                        $ d100roll -= 10
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
                    if highisland_lightsource:
                        $ d100roll -= 10
                    $ pc_battlecounter += 1
                    if d100roll <= 30:
                        menu:
                            'You adjust your equipment and step forward, keeping your blade high. The smaller beasts move out of your way. You cut the skin of the first enemy, and even more creatures crawl away from you, alerting each other with their hisses. Only the largest ones throw you a challenge, but they’re disorganized - you find a gap between them, and, unscathed, push through, avoiding the swishes of the black-and-yellow tails.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. I’m halfway there.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. I’m halfway there.')
                                $ highisland_destination = "camp1"
                                jump highisland_destination
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
                            $ custom1 = "You adjust your equipment and step forward, keeping your blade high. The smaller beasts move out of your way. You cut the skin of the first enemy, and even more creatures crawl away from you, alerting each other with their hisses.\n\nOnly the largest ones throw you a challenge, but as you seek the best path forward, you don’t notice the nearby swish of a tail. It whips your side, knocking you to the ground, and you don’t have time to get away from the sharp claws of another tree-climber."
                            jump highisland_gameover
                        menu:
                            'You adjust your equipment and step forward, keeping your blade high. The smaller beasts move out of your way. You cut the skin of the first enemy, and even more creatures crawl away from you, alerting each other with their hisses.
                            \n\nOnly the largest ones throw you a challenge, but as you seek the best path forward, you don’t notice the nearby swish of a tail. It whips your side, knocking you to the ground, and you just barely get away from the sharp claws of another tree-climber. Seeing the emerging wave of black-and-yellow shapes, you run for your life.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. I’m halfway there.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. I’m halfway there.')
                                $ highisland_destination = "camp1"
                                jump highisland_destination

    label highisland_howlers_monitorlizardsALL:
        label highisland_howlers_monitorlizards01:
            $ custom1 = "You reach a humble valley. The trees here are sparse, and the stream, while gentle, has completely distorted the path. At least the moonlight can guide you.\n\nThe black saurians, covered with yellow spots, are too numerous to count, laying just a few steps away from one another, from the grasses to the branches. Most of them are asleep, but a few of the closer ones give you curious glances, sticking out and hiding their forked tongues rapidly. The beasts aren’t massive, maybe two steps long.\n\n“We can ne cross those hills,” {color=#f6d6bd}the guard with the bow{/color} points to the sides. “En we carry too many things to sneak by. Be ready to fight.”"
            jump highisland_howlers_monitorlizards01a

        label highisland_howlers_monitorlizards01a:
            menu:
                '[custom1]
                '
                'I examine the surroundings.' if not highisland_monitorlizards_observearea:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the surroundings.')
                    $ highisland_monitorlizards_observearea = 1
                    $ custom1 = "You vaguely recognize the shapes of fruit trees and shrubs, but no animals seem to browse on them. You crouch down - the road is marked with fresh prints left by various creatures."
                    jump highisland_howlers_monitorlizards01a
                'I could learn something about them if I were to feed them. I search my bags.' if not highisland_monitorlizards_tryingtofeed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could learn something about them if I were to feed them. I search my bags.')
                    $ highisland_monitorlizards_tryingtofeed = 1
                    if item_rations >= 2:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_stoat:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_rawfishtotalnumber:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_chicken:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_wildplants:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if highisland_monitorlizards_tryingtofeed_narration_points >= 3:
                        $ custom1 = "You’ve got plenty of food to choose from, though you doubt the animals are going to be especially picky."
                    elif highisland_monitorlizards_tryingtofeed_narration_points >= 1:
                        $ custom1 = "You don’t have that many options to choose from."
                    else:
                        $ custom1 = "You find only crumbs and leftovers."
                    jump highisland_howlers_monitorlizards01a
                'I throw them the meaty bits from my food rations.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_rations >= 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw them the meaty bits from my food rations.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_rations -= 1
                    $ renpy.notify("You lost a ration.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a ration.{/i}')
                    $ custom1 = "“Such a waste,” says {color=#f6d6bd}the one with the mace{/color} as you approach the nearest creature and toss it the tasty scraps. It keeps moving its tongue, but steps away."
                    jump highisland_howlers_monitorlizards01a
                'My last food ration has almost no meat. (disabled)' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_rations == 1:
                    pass
                'A raw fish should be enough.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_rawfishtotalnumber:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- A raw fish should be enough.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_rawfishtotalnumber -= 1
                    $ item_rawfish_losing = 1
                    $ renpy.notify("You have %s fish left." %item_rawfishtotalnumber)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You have %s fish left.{/i}' %item_rawfishtotalnumber)
                    $ custom1 = "“Such a waste,” says {color=#f6d6bd}the one with the mace{/color} as you approach the nearest creature and toss it the fresh meal. It keeps moving its tongue, but steps away."
                    jump highisland_howlers_monitorlizards01a
                'I grab the chicken from {color=#f6d6bd}Creeks{/color}.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_chicken:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the chicken from {color=#f6d6bd}Creeks{/color}.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_chicken -= 1
                    $ renpy.notify("You lost a chicken.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a chicken.{/i}')
                    $ custom1 = "“Such a waste,” says {color=#f6d6bd}the one with the mace{/color} as you approach the nearest creature and toss it the aromatic meal. It keeps moving its tongue, but steps away."
                    jump highisland_howlers_monitorlizards01a
                'Maybe the dead stoat will lure them away.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_stoat:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe the dead stoat will lure them away.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_stoat = 0
                    $ renpy.notify("You lost the stoat.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the stoat.{/i}')
                    $ custom1 = "“Such a waste,” says {color=#f6d6bd}the one with the mace{/color} as you approach the nearest creature and toss it the fresh meal. It keeps moving its tongue, but steps away."
                    jump highisland_howlers_monitorlizards01a
                'I wonder if they’ll go after some wild plants I picked.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_plants and item_wildplants:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder if they’ll go after some wild plants I picked.')
                    $ highisland_monitorlizards_tryingtofeed_plants = 1
                    $ item_wildplants -= 1
                    $ renpy.notify("You lost a bunch of wild plants.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a bunch of wild plants.{/i}')
                    $ custom1 = "You throw the saurian a few fruits and rolled up leaves. Distrustful at first, it steps closer and takes care of them with but a few chomps."
                    jump highisland_howlers_monitorlizards01a
                '{image=d6} “Let’s not draw their attention. We’ve got to move by them, slowly.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Let’s not draw their attention. We’ve got to move by them, slowly.”')
                    menu:
                        '“Go ahead, but I’m ne running there to burn your corpse,” says {color=#f6d6bd}the leader{/color}. Your careful steps are greeted with hisses, but the beasts either stay in their spots, not bothering you as you walk around them, or move out of your way, crossing the stream. A few of them don’t even wake up.
                        \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                        \n\n“Good call, roadwarden,” says {color=#f6d6bd}the young druid{/color} with a smile.
                        '
                        'I glance at the volcano. “We’re halfway there.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. “We’re halfway there.”')
                            $ highisland_destination = "camp1"
                            jump highisland_destination
                '{image=d6} “It will be better for us to stay on the main path and run by them quickly.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} It will be better for us to stay on the main path and run by them quickly')
                    $ d100roll = renpy.random.randint(1, 100)
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 10
                    if armor == 4:
                        $ d100roll -= 5
                    if highisland_lightsource:
                        $ d100roll -= 10
                    $ d100roll -= (3*highisland_howlersguards_hp)
                    if d100roll <= 40:
                        $ highisland_howlersguards_hp -= 1
                        menu:
                            'You adjust your equipment and dash forward. The first few surprised beasts move out of your way, but their loud hisses and the splashes they make in the flowing water alert their companions. The largest ones are ready to face you, and you just barely find a gap between them. Unscathed, you get out of there.
                            \n\nNot all of you were so lucky - a powerful tail knocked {color=#f6d6bd}the guard with the bow{/color} on the ground, but she was quickly rescued by the rest of her group.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. “We’re halfway there.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. “We’re halfway there.”')
                                $ highisland_destination = "camp1"
                                jump highisland_destination
                    else:
                        $ highisland_howlersguards_hp -= 2
                        if armor >= 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        elif pc_hp > 0:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        else:
                            $ custom1 = "You adjust your equipment and dash forward. The first few surprised beasts move out of your way, but their loud hisses and the splashes they make in the flowing water alert their companions. The largest ones are ready to face you, and you fail to find a gap between them.\n\nOne moment of hesitation is enough to punish you - a tail whips your side, knocking you to the ground, and you don’t have time to get away from the sharp claws of another tree-climber."
                            jump highisland_gameover
                        menu:
                            'You adjust your equipment and dash forward. The first few surprised beasts move out of your way, but their loud hisses and the splashes they make in the flowing water alert their companions. The largest ones are ready to face you, and you fail to find a gap between them.
                            \n\nOne moment of hesitation is enough to punish you - a tail whips your side, knocking you to the ground, and if it wasn’t for {color=#f6d6bd}the one with the mace{/color}, who helped you get back on your feet, you wouldn’t have escaped the sharp claws of a tree-climber. Seeing the emerging wave of black-and-yellow shapes, you run for your life.
                            \n\nYou’re not the only injured one - {color=#f6d6bd}the guard with the bow{/color} just barely got out in one piece. Your group has some bandaging to do.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. “We’re halfway there.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. “We’re halfway there.”')
                                $ highisland_destination = "camp1"
                                jump highisland_destination
                '{image=d6} “Well then. Let’s prepare our equipment.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to prepare my equipment and get ready to fight the saurians off.')
                    $ d100roll = renpy.random.randint(1, 100)
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 10
                    if armor == 4:
                        $ d100roll -= 5
                    if item_shield:
                        $ d100roll -= 10
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
                    if highisland_lightsource:
                        $ d100roll -= 10
                    $ d100roll -= (3*highisland_howlersguards_hp)
                    $ pc_battlecounter += 1
                    if d100roll <= 30:
                        $ highisland_howlersguards_hp -= 1
                        menu:
                            'You adjust your equipment and step forward, keeping your blade high. The smaller beasts move out of your way. You cut the skin of the first enemy, and even more creatures crawl away from you, alerting each other with their hisses. Only the largest ones throw you a challenge, but they’re disorganized - you find a gap between them, and, unscathed, push through, avoiding the swishes of the black-and-yellow tails.
                            \n\nNot all of you were so lucky - a powerful tail knocked {color=#f6d6bd}the guard with the bow{/color} to the ground, but she was quickly rescued by the rest of her group.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. “We’re halfway there.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. “We’re halfway there.”')
                                $ highisland_destination = "camp1"
                                jump highisland_destination
                    else:
                        $ highisland_howlersguards_hp -= 1
                        if armor >= 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        elif pc_hp > 0:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        else:
                            $ custom1 = "You adjust your equipment and step forward, keeping your blade high. The smaller beasts move out of your way. You cut the skin of the first enemy, and even more creatures crawl away from you, alerting each other with their hisses.\n\nOnly the largest ones throw you a challenge, but as you seek the best path forward, you don’t notice the nearby swish of a tail. It whips your side, knocking you to the ground, and you don’t have time to get away from the sharp claws of another tree-climber."
                            jump highisland_gameover
                        menu:
                            'You adjust your equipment and step forward, keeping your blade high. The smaller beasts move out of your way. You cut the skin of the first enemy, and even more creatures crawl away from you, alerting each other with their hisses.
                            \n\nOnly the largest ones throw you a challenge, but as you seek the best path forward, you don’t notice the nearby swish of a tail. It whips your side, knocking you to the ground, and if it wasn’t for {color=#f6d6bd}the one with the mace{/color}, who helped you get back on your feet, you wouldn’t have escaped the sharp claws of a tree-climber. Seeing the emerging wave of black-and-yellow shapes, you run for your life.
                            \n\nYou’re not the only injured one - {color=#f6d6bd}the guard with the bow{/color} just barely got out in one piece. Your group has some bandaging to do.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. “We’re halfway there.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. “We’re halfway there.”')
                                $ highisland_destination = "camp1"
                                jump highisland_destination

    label highisland_crew_monitorlizardsALL:
        label highisland_crew_monitorlizards01:
            $ custom1 = "You reach a humble valley. The trees here are sparse, and the stream, while gentle, has completely distorted the path. At least the moonlight can guide you.\n\nThe black saurians, covered with yellow spots, are too numerous to count, laying just a few steps away from one another, from the grasses to the branches. Most of them are asleep, but a few of the closer ones give you curious glances, sticking out and hiding their forked tongues rapidly. The beasts aren’t massive, maybe two steps long.\n\nYou look to the sides. The hills are impassable."
            jump highisland_crew_monitorlizards01a

        label highisland_crew_monitorlizards01a:
            menu:
                '[custom1]
                '
                'I examine the surroundings.' if not highisland_monitorlizards_observearea:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the surroundings.')
                    $ highisland_monitorlizards_observearea = 1
                    $ custom1 = "You vaguely recognize the shapes of fruit trees and shrubs, but no animals seem to browse on them. You crouch down - the road is marked with fresh prints left by various creatures."
                    jump highisland_crew_monitorlizards01a
                '“Thoughts, {color=#f6d6bd}Aegidia{/color}?”' if aegidia_highisland_joined and not aegidia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thoughts, {color=#f6d6bd}Aegidia{/color}?”')
                    $ aegidia_highisland_opinion = 1
                    $ custom1 = "She shoves an arrow back into a quiver. “There’s too many of them.”"
                    jump highisland_crew_monitorlizards01a
                '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and not dalit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                    $ dalit_highisland_opinion = 1
                    $ custom1 = "She looks around with care, then speaks thoughtfully. “Animals use this path all the time, so I doubt these saurians are dangerous. And they mostly eat fruits, not meat.”"
                    jump highisland_crew_monitorlizards01a
                '“Any tips, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and not efren_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips, {color=#f6d6bd}Efren{/color}?”')
                    $ efren_highisland_opinion = 1
                    $ custom1 = "He blows out his cheeks. “The one you and I saw was a hunter... Maybe these ones aren’t aggressive?”"
                    jump highisland_crew_monitorlizards01a
                '“{color=#f6d6bd}Thyrsus{/color}, suggestions?”' if thyrsus_highisland_joined and not thyrsus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, suggestions?”')
                    $ thyrsus_highisland_opinion = 1
                    if thyrsus_highisland_blocked:
                        $ custom1 = "“Not really,” he says. “T’s their land. Ba I’m getting weak, warden, I’d rather not fight.”"
                    else:
                        $ custom1 = "“Not really,” he says. “T’s their land. I can fight, I can run.”"
                    jump highisland_crew_monitorlizards01a
                '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and not pyrrhos_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                    $ pyrrhos_highisland_opinion = 1
                    $ custom1 = "“We can’t feed this many stomachs, and we can’t shoot this many thinkers...” he shrugs. “I don’t know.”"
                    jump highisland_crew_monitorlizards01a
                'I look at {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and not bandit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}the bandit{/color}.')
                    $ bandit_highisland_opinion = 1
                    $ custom1 = "He observes them keenly. “See their tongues? That’s how they smell things, they do. We can’t sneak by them, they care not about the night.”"
                    jump highisland_crew_monitorlizards01a
                '“{color=#f6d6bd}Tulia{/color}, what do you recommend?”' if tulia_highisland_joined and not tulia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, what do you recommend?”')
                    $ tulia_highisland_opinion = 1
                    if tulia_highisland_blocked:
                        $ custom1 = "“We {i}could{/i} try to chop through them...” She tries to straighten up, but says nothing more. She looks exhausted."
                    else:
                        $ custom1 = "“We {i}could{/i} try to chop through them, if you’re ready.” She straightens up. “My arm is still strong.”"
                    jump highisland_crew_monitorlizards01a
                '“Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”' if tzvi_highisland_joined and not tzvi_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”')
                    $ tzvi_highisland_opinion = 1
                    if not highisland_monitorlizards_tryingtofeed_plants:
                        $ item_wildplants += 1
                        $ renpy.notify("You got a bunch of wild plants.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You got a bunch of wild plants.{/i}')
                        $ custom1 = "He gives you a small sack of wild plants, mostly fruits, that he collected during the last hour. “Throw them some,” he shrieks, “maybe they don’t care for meat.”"
                    else:
                        $ custom1 = "“They eat fruits, so who knows, maybe they’ll ignore us.” He goes ahead, but, so far, no beast is running at him."
                    jump highisland_crew_monitorlizards01a
                '“{color=#f6d6bd}Quintus{/color}, any ideas?”' if quintus_highisland_joined and not quintus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Quintus{/color}, any ideas?”')
                    $ quintus_highisland_opinion = 1
                    if quintus_highisland_blocked:
                        $ custom1 = "Startled by your voice, his eyes are now wide open. “Huh?” He looks like he really needs to sleep."
                    else:
                        $ custom1 = "“I’m good at running. Are you?” He looks around. “It’s not like we can fight them.”"
                    jump highisland_crew_monitorlizards01a
                'I could learn something about them if I were to feed them. I search my bags.' if not highisland_monitorlizards_tryingtofeed:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could learn something about them if I were to feed them. I search my bags.')
                    $ highisland_monitorlizards_tryingtofeed = 1
                    if item_rations >= 2:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_stoat:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_rawfishtotalnumber:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_chicken:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if item_wildplants:
                        $ highisland_monitorlizards_tryingtofeed_narration_points += 1
                    if highisland_monitorlizards_tryingtofeed_narration_points >= 3:
                        $ custom1 = "You’ve got plenty of food to choose from, though you doubt the animals are going to be especially picky."
                    elif highisland_monitorlizards_tryingtofeed_narration_points >= 1:
                        $ custom1 = "You don’t have that many options to choose from."
                    else:
                        $ custom1 = "You find only crumbs and leftovers."
                    jump highisland_crew_monitorlizards01a
                'I throw them the meaty bits from my food rations.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_rations >= 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw them the meaty bits from my food rations.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_rations -= 1
                    $ renpy.notify("You lost a ration.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a ration.{/i}')
                    $ custom1 = "You approach the nearest creature and toss it the tasty scraps. It keeps moving its tongue, but steps away."
                    jump highisland_solo_monitorlizards01a
                'My last food ration has almost no meat. (disabled)' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_rations == 1:
                    pass
                'A raw fish should be enough.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_rawfishtotalnumber:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- A raw fish should be enough.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_rawfishtotalnumber -= 1
                    $ item_rawfish_losing = 1
                    $ renpy.notify("You have %s fish left." %item_rawfishtotalnumber)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You have %s fish left.{/i}' %item_rawfishtotalnumber)
                    $ custom1 = "You approach the nearest creature and toss it the fresh meal. It keeps moving its tongue, but steps away."
                    jump highisland_solo_monitorlizards01a
                'I grab the chicken from {color=#f6d6bd}Creeks{/color}.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_chicken:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the chicken from {color=#f6d6bd}Creeks{/color}.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_chicken -= 1
                    $ renpy.notify("You lost a chicken.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a chicken.{/i}')
                    $ custom1 = "You approach the nearest creature and toss it the aromatic meal. It keeps moving its tongue, but steps away."
                    jump highisland_solo_monitorlizards01a
                'Maybe the dead stoat will lure them away.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_meat and item_stoat:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe the dead stoat will lure them away.')
                    $ highisland_monitorlizards_tryingtofeed_meat += 1
                    $ item_stoat = 0
                    $ renpy.notify("You lost the stoat.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the stoat.{/i}')
                    $ custom1 = "You approach the nearest creature and toss it the fresh meal. It keeps moving its tongue, but steps away."
                    jump highisland_solo_monitorlizards01a
                'I wonder if they’ll go after some wild plants I picked.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_plants and item_wildplants and not tzvi_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder if they’ll go after some wild plants I picked.')
                    $ highisland_monitorlizards_tryingtofeed_plants = 1
                    $ item_wildplants -= 1
                    $ renpy.notify("You lost a bunch of wild plants.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a bunch of wild plants.{/i}')
                    $ custom1 = "You throw the saurian a few fruits and rolled up leaves. Distrustful at first, it steps closer and takes care of them with but a few chomps."
                    jump highisland_crew_monitorlizards01a
                'I give them the fruits from {color=#f6d6bd}Tzvi{/color}.' if highisland_monitorlizards_tryingtofeed and not highisland_monitorlizards_tryingtofeed_plants and item_wildplants and tzvi_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them the fruits from {color=#f6d6bd}Tzvi{/color}.')
                    $ highisland_monitorlizards_tryingtofeed_plants = 1
                    $ item_wildplants -= 1
                    $ renpy.notify("You lost a bunch of wild plants.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a bunch of wild plants.{/i}')
                    $ custom1 = "You throw the saurian a few fruits and rolled up leaves. Distrustful at first, it steps closer and takes care of them with but a few chomps."
                    jump highisland_crew_monitorlizards01a
                '{image=d6} “Let’s not draw their attention. We’ve got to move by them, slowly.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Let’s not draw their attention. We’ve got to move by them, slowly.”')
                    menu:
                        'Your careful steps are greeted with hisses, but the beasts either stay in their spots, not bothering you as you walk around them, or move out of your way, crossing the stream. A few of them don’t even wake up.
                        \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                        '
                        'I glance at the volcano. “We’re halfway there.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. “We’re halfway there.”')
                            $ highisland_destination = "camp1"
                            jump highisland_destination
                '{image=d6} “It will be better for us to stay on the main path and run by them quickly.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} It will be better for us to stay on the main path and run by them quickly')
                    $ d100roll = renpy.random.randint(1, 100)
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 10
                    if armor == 4:
                        $ d100roll -= 5
                    if highisland_lightsource:
                        $ d100roll -= 10
                    $ d100roll -= (10*highisland_crew_left)
                    if d100roll <= 40:
                        menu:
                            'You adjust your equipment and dash forward. The first few surprised beasts move out of your way, but their loud hisses and the splashes they make in the flowing water alert their companions. The largest ones are ready to face you, and you just barely find a gap between them. Unscathed, you get out of there, and so does the rest of your group.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. “We’re halfway there.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. “We’re halfway there.”')
                                $ highisland_destination = "camp1"
                                jump highisland_destination
                    else:
                        label highisland_companiondamage_loop_monitorlizards:
                            if highisland_crew_left <= 0:
                                $ custom1 = "One moment of hesitation is enough to punish you - a tail whips your side, knocking you to the ground, but your companions help you get back on your feet."
                                if armor >= 1:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                elif pc_hp > 0:
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                else:
                                    $ custom1 = "You adjust your equipment and dash forward. The first few surprised beasts move out of your way, but their loud hisses and the splashes they make in the flowing water alert their companions. The largest ones are ready to face you, and you fail to find a gap between them.\n\nOne moment of hesitation is enough to punish you - a tail whips your side, knocking you to the ground, and you don’t have time to get away from the sharp claws of another tree-climber."
                                    jump highisland_gameover
                            else:
                                $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus', 'pc'])
                                if highisland_crew_dmg_target == "aegidia":
                                    if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizards
                                    else:
                                        $ aegidia_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "This moment of hesitation is enough to punish {color=#f6d6bd}Aegidia{/color} - a tail whips her side and knocks her to the ground. You get her back on her feet, but she only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "dalit":
                                    if not dalit_highisland_joined or dalit_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizards
                                    else:
                                        $ dalit_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "This moment of hesitation is enough to punish {color=#f6d6bd}Dalit{/color} - a tail whips her side and knocks her to the ground. You get her back on her feet, but she only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "efren":
                                    if not efren_highisland_joined or efren_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizards
                                    else:
                                        $ efren_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "This moment of hesitation is enough to punish {color=#f6d6bd}Efren{/color} - a tail whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "thyrsus":
                                    if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizards
                                    else:
                                        $ thyrsus_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "This moment of hesitation is enough to punish {color=#f6d6bd}Thyrsus{/color} - a tail whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "pyrrhos":
                                    if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizards
                                    else:
                                        $ pyrrhos_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "This moment of hesitation is enough to punish {color=#f6d6bd}Pyrrhos{/color} - a tail whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "bandit":
                                    if not bandit_highisland_joined or bandit_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizards
                                    else:
                                        $ bandit_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "This moment of hesitation is enough to punish {color=#f6d6bd}the bandit{/color} - a tail whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "tulia":
                                    if not tulia_highisland_joined or tulia_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizards
                                    else:
                                        $ tulia_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "This moment of hesitation is enough to punish {color=#f6d6bd}Tulia{/color} - a tail whips her side and knocks her to the ground. You get her back on her feet, but she only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "tzvi":
                                    if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizards
                                    else:
                                        $ tzvi_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "This moment of hesitation is enough to punish {color=#f6d6bd}Tzvi{/color} - a tail whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "quintus":
                                    if not quintus_highisland_joined or quintus_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizards
                                    else:
                                        $ quintus_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "This moment of hesitation is enough to punish {color=#f6d6bd}Quintus{/color} - a tail whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "pc":
                                    $ custom1 = "One moment of hesitation is enough to punish you - a tail whips your side, knocking you to the ground, but your companions help you get back on your feet."
                                    if armor >= 1:
                                        $ armor = limit_armor(armor-1)
                                        show minus1armor at armorchange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                    elif pc_hp > 0:
                                        $ pc_hp = limit_pc_hp(pc_hp-1)
                                        show minus1hp at hpchange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                    else:
                                        $ custom1 = "You adjust your equipment and dash forward. The first few surprised beasts move out of your way, but their loud hisses and the splashes they make in the flowing water alert their companions. The largest ones are ready to face you, and you fail to find a gap between them.\n\nOne moment of hesitation is enough to punish you - a tail whips your side, knocking you to the ground, and you don’t have time to get away from the sharp claws of another tree-climber."
                                        jump highisland_gameover
                        menu:
                            'You adjust your equipment and dash forward. The first few surprised beasts move out of your way, but their loud hisses and the splashes they make in the flowing water alert their companions. The largest ones are ready to face you, and you fail to find a gap between them.
                            \n\n[custom1] Seeing the emerging wave of black-and-yellow shapes, you run for your life.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. “We’re halfway there.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. “We’re halfway there.”')
                                $ highisland_destination = "camp1"
                                jump highisland_destination
                '{image=d6} “Well then. Let’s prepare our equipment.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I need to prepare my equipment and get ready to fight the saurians off.')
                    $ d100roll = renpy.random.randint(1, 100)
                    if not pc_food:
                        $ d100roll += 5
                    if pc_food == 3:
                        $ d100roll -= 5
                    if pc_food == 4:
                        $ d100roll -= 10
                    if armor == 4:
                        $ d100roll -= 5
                    if item_shield:
                        $ d100roll -= 10
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
                    if highisland_lightsource:
                        $ d100roll -= 10
                    if quintus_highisland_joined and not quintus_highisland_blocked:
                        $ d100roll -= 15
                    if thyrsus_highisland_joined and not thyrsus_highisland_blocked:
                        $ d100roll -= 10
                    if tulia_highisland_joined and not tulia_highisland_blocked:
                        $ d100roll -= 10
                    if tzvi_highisland_joined and not tzvi_highisland_blocked:
                        $ d100roll -= 5
                    $ pc_battlecounter += 1
                    if d100roll <= 30:
                        menu:
                            'You adjust your equipment and step forward, keeping your blade high. The smaller beasts move out of your way. You cut the skin of the first enemy, and even more creatures crawl away from you, alerting each other with their hisses. Only the largest ones throw you a challenge, but they’re disorganized - you find a gap between them, and, unscathed, push through, leading your group through the swishes of the black-and-yellow tails.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. “We’re halfway there.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. “We’re halfway there.”')
                                $ highisland_destination = "camp1"
                                jump highisland_destination
                    else:
                        label highisland_companiondamage_loop_monitorlizardsalt:
                            if highisland_crew_left <= 0:
                                $ custom1 = "Only the largest ones throw you a challenge, but as you seek the best path forward, you don’t notice the nearby swish of a tail. It whips your side, knocking you to the ground, but your companions help you get back on your feet and escape the sharp claws of a tree-climber."
                                if armor >= 1:
                                    $ armor = limit_armor(armor-1)
                                    show minus1armor at armorchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                elif pc_hp > 0:
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                else:
                                    $ custom1 = "You adjust your equipment and step forward, keeping your blade high. The smaller beasts move out of your way. You cut the skin of the first enemy, and even more creatures crawl away from you, alerting each other with their hisses.\n\nOnly the largest ones throw you a challenge, but as you seek the best path forward, you don’t notice the nearby swish of a tail. It whips your side, knocking you to the ground, and you don’t have time to get away from the sharp claws of another tree-climber."
                                    jump highisland_gameover
                            else:
                                $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus', 'pc'])
                                if highisland_crew_dmg_target == "aegidia":
                                    if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizardsalt
                                    else:
                                        $ aegidia_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "Only the largest ones throw you a challenge, but as you seek the best path forward, {color=#f6d6bd}Aegidia{/color} doesn’t notice the nearby swish of a tail. It whips her side and knocks her to the ground. You get her back on her feet, but she only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "dalit":
                                    if not dalit_highisland_joined or dalit_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizardsalt
                                    else:
                                        $ dalit_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "Only the largest ones throw you a challenge, but as you seek the best path forward, {color=#f6d6bd}Dalit{/color} doesn’t notice the nearby swish of a tail. It whips her side and knocks her to the ground. You get her back on her feet, but she only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "efren":
                                    if not efren_highisland_joined or efren_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizardsalt
                                    else:
                                        $ efren_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "Only the largest ones throw you a challenge, but as you seek the best path forward, {color=#f6d6bd}Efren{/color} doesn’t notice the nearby swish of a tail. It whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "thyrsus":
                                    if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizardsalt
                                    else:
                                        $ thyrsus_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "Only the largest ones throw you a challenge, but as you seek the best path forward, {color=#f6d6bd}Thyrsus{/color} doesn’t notice the nearby swish of a tail. It whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "pyrrhos":
                                    if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizardsalt
                                    else:
                                        $ pyrrhos_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "Only the largest ones throw you a challenge, but as you seek the best path forward, {color=#f6d6bd}Pyrrhos{/color} doesn’t notice the nearby swish of a tail. It whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "bandit":
                                    if not bandit_highisland_joined or bandit_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizardsalt
                                    else:
                                        $ bandit_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "Only the largest ones throw you a challenge, but as you seek the best path forward, {color=#f6d6bd}the bandit{/color} doesn’t notice the nearby swish of a tail. It whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "tulia":
                                    if not tulia_highisland_joined or tulia_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizardsalt
                                    else:
                                        $ tulia_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "Only the largest ones throw you a challenge, but as you seek the best path forward, {color=#f6d6bd}Tulia{/color} doesn’t notice the nearby swish of a tail. It whips her side and knocks her to the ground. You get her back on her feet, but she only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "tzvi":
                                    if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizardsalt
                                    else:
                                        $ tzvi_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "Only the largest ones throw you a challenge, but as you seek the best path forward, {color=#f6d6bd}Tzvi{/color} doesn’t notice the nearby swish of a tail. It whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "quintus":
                                    if not quintus_highisland_joined or quintus_highisland_blocked:
                                        jump highisland_companiondamage_loop_monitorlizardsalt
                                    else:
                                        $ quintus_highisland_blocked = 1
                                        $ highisland_crew_left -= 1
                                        $ custom1 = "Only the largest ones throw you a challenge, but as you seek the best path forward, {color=#f6d6bd}Quintus{/color} doesn’t notice the nearby swish of a tail. It whips his side and knocks him to the ground. You get him back on his feet, but he only barely escapes the sharp claws of a tree-climber, and struggles to go on."
                                elif highisland_crew_dmg_target == "pc":
                                    $ custom1 = "Only the largest ones throw you a challenge, but as you seek the best path forward, you don’t notice the nearby swish of a tail. It whips your side, knocking you to the ground, but your companions help you get back on your feet and escape the sharp claws of a tree-climber."
                                    if armor >= 1:
                                        $ armor = limit_armor(armor-1)
                                        show minus1armor at armorchange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                                    elif pc_hp > 0:
                                        $ pc_hp = limit_pc_hp(pc_hp-1)
                                        show minus1hp at hpchange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                    else:
                                        $ custom1 = "You adjust your equipment and step forward, keeping your blade high. The smaller beasts move out of your way. You cut the skin of the first enemy, and even more creatures crawl away from you, alerting each other with their hisses.\n\nOnly the largest ones throw you a challenge, but as you seek the best path forward, you don’t notice the nearby swish of a tail. It whips your side, knocking you to the ground, and you don’t have time to get away from the sharp claws of another tree-climber."
                                        jump highisland_gameover
                        menu:
                            'You adjust your equipment and step forward, keeping your blade high. The smaller beasts move out of your way. You cut the skin of the first enemy, and even more creatures crawl away from you, alerting each other with their hisses.
                            \n\n[custom1]Seeing the emerging wave of black-and-yellow shapes, you run for your life.
                            \n\nThe valley once again turns into a lush forest. The path here is even narrower than it was before.
                            '
                            'I glance at the volcano. “We’re halfway there.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the volcano. “We’re halfway there.”')
                                $ highisland_destination = "camp1"
                                jump highisland_destination

label highisland_camp1ALL:
    label highisland_solo_camp1ALL:
        label highisland_solo_camp101:
            if not highisland_camp1_prayed:
                if (pc_religion == "theunitedchurch" and not description_druids10) or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                    if pc_faithpoints_opportunities >= 0 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                        $ highisland_camp1_canpray = 1
            $ custom1 = "The path ahead is overtaken by the thicket, but the fatigue is catching up with you. The remains of a hamlet have no dwellers other than rats and snakes. You find a flat rock, cover it with your cloak, and let yourself sit idly for a bit before you open your bags. You may not find another time to have a few bites of food."
            jump highisland_solo_camp101a

        label highisland_solo_camp101a:
            menu:
                '[custom1]
                '
                'I try to figure out what these ruins used to be.' if not highisland_camp1_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to figure out what these ruins used to be.')
                    $ highisland_camp1_examine = 1
                    $ custom1 = "Judging by the stone wall and the now-collapsed tower, it could have served as a shelter for two dozen humans at once. There are no remains of any sheds, working stations, or tools, and you see nothing unusual about the surrounding rocks and plants."
                    jump highisland_solo_camp101a
                'I look up at the night sky, seeking a sign from my ancestors.' if highisland_camp1_canpray and not highisland_camp1_prayed and pc_religion == "pagan":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look up at the night sky, seeking a sign from my ancestors.')
                    $ highisland_camp1_prayed = 1
                    $ highisland_camp1_canpray = 0
                    if pc_faithpoints_opportunities >= 8 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        show plus2hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        if pc_class == "mage":
                            $ mana = limit_mana(mana+2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                        $ custom1 = "Long minutes go by and your breath gets slower, your eyes sharper. Among the stars and clouds, you see the shapes of your tribe’s home. Your exhausted questions and requests turn into certainty. “You can do this,” a voice in the wind tells you, sending chills down your spine."
                    elif pc_faithpoints_opportunities >= 6 and (pc_faithpoints+(achievement_animalssavedpoints/2)) >= (pc_faithpoints_opportunities*0.75):
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        show plus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        if pc_class == "mage":
                            $ mana = limit_mana(mana+2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                        $ custom1 = "Long minutes go by and your breath gets slower, your eyes sharper. Among the stars and clouds, you see the shapes of your tribe’s home and of the animals you spared on your journey. Your exhausted questions and requests turn into certainty. “You can do this,” a voice in the wind tells you, sending chills down your spine."
                    else:
                        $ custom1 = "Long minutes go by, but the stars are as distant as always, distorted by the clouds."
                    jump highisland_solo_camp101a
                'I bow my head and try to ignore the loud beasts of the woods. I need Wright’s guidance.' if highisland_camp1_canpray and not highisland_camp1_prayed and pc_religion != "pagan":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bow my head and try to ignore the loud beasts of the woods. I need Wright’s guidance.')
                    $ highisland_camp1_prayed = 1
                    $ highisland_camp1_canpray = 0
                    if pc_faithpoints_opportunities >= 8 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        show plus2hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        if pc_class == "mage":
                            $ mana = limit_mana(mana+2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                        $ custom1 = "Long minutes go by, your shoulders slump. As you shape your awkward, exhausted prayers, you keep examining your deeds from the recent days, until a warm, rejuvenating gust of wind fills your mouth. You spring to your feet, ready to reach your destination."
                    else:
                        $ custom1 = "Long minutes go by, but the only answer you hear belongs to hungry creatures. Distracted, you keep glancing at the entrance."
                    jump highisland_solo_camp101a
                'I let my back and limbs rest for a bit, then prepare my tools to cut through the bushes.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let my back and limbs rest for a bit, then prepare my tools to cut through the bushes.')
                    $ highisland_destination = "denseplants"
                    jump highisland_destination

    label highisland_howlers_camp1ALL:
        label highisland_howlers_camp101:
            if not highisland_camp1_prayed:
                if (pc_religion == "theunitedchurch" and not description_druids10) or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                    if pc_faithpoints_opportunities >= 0 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                        $ highisland_camp1_canpray = 1
            $ custom1 = "The path ahead is overtaken by the thicket. “We should rest,” says {color=#f6d6bd}the leader{/color}. “Let’s see if this place is safe.”\n\nThe remains of a hamlet have no dwellers other than rats and snakes. You find a flat rock, cover it with your cloak, and let yourself sit idly for a bit before you open your bags. {color=#f6d6bd}The guards{/color} prepare a small fire in the middle of the path, and discuss among themselves if there’s any time to forage for food."
            jump highisland_howlers_camp101a

        label highisland_howlers_camp101a:
            menu:
                '[custom1]
                '
                'I try to figure out what these ruins used to be.' if not highisland_camp1_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to figure out what these ruins used to be.')
                    $ highisland_camp1_examine = 1
                    $ custom1 = "Judging by the stone wall and the now-collapsed tower, it could have served as a shelter for two dozen humans at once. There are no remains of any sheds, working stations, or tools, and you see nothing unusual about the surrounding rocks and plants."
                    jump highisland_howlers_camp101a
                'I look up at the night sky, seeking a sign from my ancestors.' if highisland_camp1_canpray and not highisland_camp1_prayed and pc_religion == "pagan":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look up at the night sky, seeking a sign from my ancestors.')
                    $ highisland_camp1_prayed = 1
                    $ highisland_camp1_canpray = 0
                    if pc_faithpoints_opportunities >= 8 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        show plus2hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        if pc_class == "mage":
                            $ mana = limit_mana(mana+2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                        $ custom1 = "Long minutes go by and your breath gets slower, your eyes sharper. Among the stars and clouds, you see the shapes of your tribe’s home. Your exhausted questions and requests turn into certainty. “You can do this,” a voice in the wind tells you, sending chills down your spine."
                    elif pc_faithpoints_opportunities >= 6 and (pc_faithpoints+(achievement_animalssavedpoints/2)) >= (pc_faithpoints_opportunities*0.75):
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        show plus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        if pc_class == "mage":
                            $ mana = limit_mana(mana+2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                        $ custom1 = "Long minutes go by and your breath gets slower, your eyes sharper. Among the stars and clouds, you see the shapes of your tribe’s home and of the animals you spared on your journey. Your exhausted questions and requests turn into certainty. “You can do this,” a voice in the wind tells you, sending chills down your spine."
                    else:
                        $ custom1 = "Long minutes go by, but the stars are as distant as always, distorted by the clouds."
                    jump highisland_howlers_camp101a
                'I bow my head and try to ignore the loud beasts of the woods. I need Wright’s guidance.' if highisland_camp1_canpray and not highisland_camp1_prayed and pc_religion != "pagan":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bow my head and try to ignore the loud beasts of the woods. I need Wright’s guidance.')
                    $ highisland_camp1_prayed = 1
                    $ highisland_camp1_canpray = 0
                    if pc_faithpoints_opportunities >= 8 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        show plus2hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        if pc_class == "mage":
                            $ mana = limit_mana(mana+2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                        $ custom1 = "Long minutes go by, your shoulders slump. As you shape your awkward, exhausted prayers, you keep examining your deeds from the recent days, until a warm, rejuvenating gust of wind fills your mouth. You spring to your feet, ready to reach your destination."
                    else:
                        $ custom1 = "Long minutes go by, but the only answer you hear belongs to hungry creatures. Distracted, you keep glancing at the entrance."
                    jump highisland_howlers_camp101a
                'I unpack my food rations and offer some to {color=#f6d6bd}the guards{/color}.' if not highisland_camp1_guards_food_offered and item_rations:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I unpack my food rations and offer some to {color=#f6d6bd}the guards{/color}.')
                    menu:
                        'You look at your supplies.
                        '
                        'I give {color=#f6d6bd}the leader{/color} the only ration I have.' if item_rations == 1:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give {color=#f6d6bd}the leader{/color} the only one I have.')
                            $ item_rations -= 1
                            $ renpy.notify("You lost a food ration.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                            $ highisland_howlersguards_hp += 1
                            $ highisland_camp1_guards_food_offered = 1
                            $ custom1 = "He grabs it with a polite nod. It may not be enough to feed anyone, but your crew is glad to have a few snacks."
                            jump highisland_howlers_camp101a
                        'I give {color=#f6d6bd}the leader{/color} one food ration to divide among his the crew.' if item_rations >= 2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give {color=#f6d6bd}the leader{/color} one food ration to divide among his the crew.')
                            $ item_rations -= 1
                            $ renpy.notify("You lost a food ration.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                            $ highisland_howlersguards_hp += 1
                            $ highisland_camp1_guards_food_offered = 1
                            $ custom1 = "He nods politely. It may not be enough to feed anyone, but his companions gladly bite into the sparse snacks."
                            jump highisland_howlers_camp101a
                        'I give them two food rations.' if item_rations >= 2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them two food rations.')
                            $ item_rations -= 2
                            $ renpy.notify("You lost 2 food rations.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost 2 food rations.{/i}')
                            $ highisland_howlersguards_hp += 2
                            $ highisland_camp1_guards_food_offered = 2
                            $ custom1 = "He nods politely. It may not be enough to feed anyone, but his companions gladly bite into the sparse snacks."
                            jump highisland_howlers_camp101a
                        'Three.' if item_rations >= 3:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Three.')
                            $ item_rations -= 3
                            $ renpy.notify("You lost 3 food rations.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost 3 food rations.{/i}')
                            $ highisland_howlersguards_hp += 3
                            $ highisland_camp1_guards_food_offered = 3
                            $ custom1 = "He smiles politely. {color=#f6d6bd}The young druid{/color} soon claims to be full, while his companions gladly bite into the remaining snacks."
                            jump highisland_howlers_camp101a
                        'Four.' if item_rations >= 4:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Four.')
                            $ item_rations -= 4
                            $ renpy.notify("You lost 4 food rations.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost 4 food rations.{/i}')
                            $ highisland_howlersguards_hp += 4
                            $ highisland_camp1_guards_food_offered = 4
                            $ custom1 = "He smiles politely. {color=#f6d6bd}The young druid{/color} and {color=#f6d6bd}the one with the bow{/color} soon claim to be full, while their companions gladly bite into the remaining snacks."
                            jump highisland_howlers_camp101a
                        'Five. One for each guard.' if item_rations >= 5:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Five. One for each guard.')
                            $ item_rations -= 5
                            $ renpy.notify("You lost 5 food rations.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost 5 food rations.{/i}')
                            $ highisland_howlersguards_hp += 5
                            $ highisland_camp1_guards_food_offered = 5
                            $ custom1 = "His surprised frown soon shifts into a wide grin. Both him and the rest of the crew take care of your treat quickly. While {color=#f6d6bd}the one with the bow{/color} and {color=#f6d6bd}the young druid{/color} leave a few bites unfinished, their larger companions are eager to help them."
                            jump highisland_howlers_camp101a
                        'Maybe not.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe not.')
                            $ custom1 = "You put the bag away."
                            jump highisland_howlers_camp101a
                'I let my back and limbs rest for a bit, then prepare my tools to cut through the bushes.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let my back and limbs rest for a bit, then prepare my tools to cut through the bushes.')
                    $ highisland_destination = "denseplants"
                    jump highisland_destination

    label highisland_crew_camp1ALL:
        label highisland_crew_camp101:
            if not highisland_camp1_prayed:
                if (pc_religion == "theunitedchurch" and not description_druids10) or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                    if pc_faithpoints_opportunities >= 0 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                        $ highisland_camp1_canpray = 1
            if tulia_highisland_joined and not highisland_camp1_tuliahelp_used and not tulia_highisland_blocked and not tulia_highisland_tired:
                $ highisland_camp1_tuliahelp_available = 1
            if aegidia_highisland_joined:
                $ custom11 = "\n\n{color=#f6d6bd}Aegidia{/color} sits by the ruined tower by herself, wipes her forehead with a cloth, and takes her boots off."
            else:
                $ custom11 = ""
            if dalit_highisland_joined:
                $ custom12 = "\n\n{color=#f6d6bd}Dalit{/color} sits down on another rock and grabs a bone comb. “What a mess,” she giggles."
            else:
                $ custom12 = ""
            if efren_highisland_joined:
                $ custom13 = "\n\n{color=#f6d6bd}Efren{/color} seems anxious at first, but finally sits down on the ground, turned toward the entrance, and takes off the head of the wolf."
            else:
                $ custom13 = ""
            if thyrsus_highisland_joined:
                $ custom15 = "\n\n{color=#f6d6bd}Thyrsus{/color} spends a few minutes looking through the amulets hanging from his neck. His creepers rest on the ground, twitching every now and then."
            else:
                $ custom15 = ""
            if pyrrhos_highisland_joined:
                $ custom16 = "\n\n{color=#f6d6bd}Pyrrhos{/color} clasps his hands and looks around, announcing loudly that he’s going to start a fire, but after he fails to find any dry wood, he takes off his shirt and sits by the entrance."
            else:
                $ custom16 = ""
            if bandit_highisland_joined:
                $ custom17 = "\n\n{color=#f6d6bd}The bandit{/color} crouches by the wall, in a spot where a beam of moonlight gets through the leaves, and rests his head against the bricks."
            else:
                $ custom17 = ""
            if tulia_highisland_joined:
                $ custom18 = "\n\n{color=#f6d6bd}Tulia{/color} sits by you. Her fingers are tapping on the hilt of her sword and you notice that she’s humming some sort of melody you’ve heard in the city harbor."
            else:
                $ custom18 = ""
            if tzvi_highisland_joined:
                $ custom19 = "\n\n{color=#f6d6bd}Tzvi{/color} makes an annoyed scoff and keeps wandering about, examining the shrubs and bushes."
            else:
                $ custom19 = ""
            if quintus_highisland_joined:
                $ custom20 = "\n\n“Any chances we found ancient mead storage?” mumbles {color=#f6d6bd}Quintus{/color}, then sits down on the ground, leaning against a tree."
            else:
                $ custom20 = ""
            menu:
                'The path ahead is overtaken by the thicket, but the fatigue is catching up with you. The remains of a hamlet have no dwellers other than rats and snakes. “We should rest here,” you say to your companions.
                \n\nYou find a flat rock, cover it with your cloak, and let yourself sit idly for a bit before you open your bags. You may not find another time to have a few bites of food.[custom19][custom11][custom12][custom13][custom15][custom16][custom17][custom18][custom20]
                '
                'I try to figure out what these ruins used to be.' if not highisland_camp1_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to figure out what these ruins used to be.')
                    $ highisland_camp1_examine = 1
                    $ custom1 = "Judging by the stone wall and the now-collapsed tower, it could have served as a shelter for two dozen humans at once. There are no remains of any sheds, working stations, or tools, and you see nothing unusual about the surrounding rocks and plants."
                    jump highisland_crew_camp101a
                'I look up at the night sky, seeking a sign from my ancestors.' if highisland_camp1_canpray and not highisland_camp1_prayed and pc_religion == "pagan":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look up at the night sky, seeking a sign from my ancestors.')
                    $ highisland_camp1_prayed = 1
                    $ highisland_camp1_canpray = 0
                    if pc_faithpoints_opportunities >= 8 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        show plus2hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        if pc_class == "mage":
                            $ mana = limit_mana(mana+2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                        $ custom1 = "Long minutes go by and your breath gets slower, your eyes sharper. Among the stars and clouds, you see the shapes of your tribe’s home. Your exhausted questions and requests turn into certainty. “You can do this,” a voice in the wind tells you, sending chills down your spine."
                    elif pc_faithpoints_opportunities >= 6 and (pc_faithpoints+(achievement_animalssavedpoints/2)) >= (pc_faithpoints_opportunities*0.75):
                        $ pc_hp = limit_pc_hp(pc_hp+1)
                        show plus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                        if pc_class == "mage":
                            $ mana = limit_mana(mana+2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                        $ custom1 = "Long minutes go by and your breath gets slower, your eyes sharper. Among the stars and clouds, you see the shapes of your tribe’s home and of the animals you spared on your journey. Your exhausted questions and requests turn into certainty. “You can do this,” a voice in the wind tells you, sending chills down your spine."
                    else:
                        $ custom1 = "Long minutes go by, but the stars are as distant as always, distorted by the clouds."
                    jump highisland_crew_camp101a
                'I bow my head and try to ignore the loud beasts of the woods. I need Wright’s guidance.' if highisland_camp1_canpray and not highisland_camp1_prayed and pc_religion != "pagan":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bow my head and try to ignore the loud beasts of the woods. I need Wright’s guidance.')
                    $ highisland_camp1_prayed = 1
                    $ highisland_camp1_canpray = 0
                    if pc_faithpoints_opportunities >= 8 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                        $ pc_hp = limit_pc_hp(pc_hp+2)
                        show plus2hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                        if pc_class == "mage":
                            $ mana = limit_mana(mana+2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                        $ custom1 = "Long minutes go by, your shoulders slump. As you shape your awkward, exhausted prayers, you keep examining your deeds from the recent days, until a warm, rejuvenating gust of wind fills your mouth. You spring to your feet, ready to reach your destination."
                    else:
                        $ custom1 = "Long minutes go by, but the only answer you hear belongs to hungry creatures. Distracted, you keep glancing at the entrance."
                    jump highisland_crew_camp101a
                'I look at {color=#f6d6bd}Aegidia{/color}.' if aegidia_highisland_joined and not aegidia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}Aegidia{/color}.')
                    if not aegidia_highisland_blocked and not aegidia_highisland_tired:
                        $ custom1 = "She returns your gaze and gives you a kind smile. She’s ready for the next challenge."
                        $ aegidia_highisland_opinion = 1
                        jump highisland_crew_camp101a
                    elif aegidia_highisland_blocked:
                        menu:
                            'She returns your gaze and gives you a sad smile. She holds her wounded side to stop the pain.
                            '
                            '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                $ highisland_camp1_tuliahelp_used = 1
                                $ aegidia_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                if not aegidia_highisland_tired:
                                    $ aegidia_highisland_opinion = 1
                                    $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Aegidia{/color} and pays you no more attention."
                                else:
                                    $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Aegidia{/color} and pays you no more attention. Soon after, her {i}patient{/i} mentions she’s a bit hungry, but seems to feel much better."
                                jump highisland_crew_camp101a
                            'I offer her a healing potion.' if item_generichealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a healing potion.')
                                $ item_generichealingpotion -= 1
                                $ renpy.notify("You lost a healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                $ aegidia_highisland_blocked = 0
                                $ aegidia_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ aegidia_highisland_opinion = 1
                                $ custom1 = "“Thank you,” she sniffs the contents, drinks it slowly, and leans away with a sigh."
                                jump highisland_crew_camp101a
                            'I offer her the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her the potion from the dolmen.')
                                $ item_potiondolmen -= 1
                                $ renpy.notify("You lost the potion from the dolmen.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                $ aegidia_highisland_blocked = 0
                                $ aegidia_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ aegidia_highisland_opinion = 1
                                $ custom1 = "“Thank you,” she sniffs the contents, drinks it slowly, and leans away with a sigh."
                                jump highisland_crew_camp101a
                            'I offer her a small healing potion.' if item_smallhealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a small healing potion.')
                                $ item_smallhealingpotion -= 1
                                $ renpy.notify("You lost a small healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                $ aegidia_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                if not aegidia_highisland_tired:
                                    $ aegidia_highisland_opinion = 1
                                    $ custom1 = "“Thank you,” she sniffs the contents, drinks it slowly, and leans away with a sigh."
                                else:
                                    $ custom1 = "“Thank you,” she sniffs the contents, drinks it slowly, and leans away with a sigh. “Such a stroll sure makes one hungry, huh?”"
                                jump highisland_crew_camp101a
                            'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                pass
                            'I look away.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look away.')
                                jump highisland_crew_camp101a
                    elif aegidia_highisland_tired:
                        menu:
                            'She returns your gaze and gives you a tired smile. “Such a stroll sure makes one hungry, huh?”
                            '
                            'I offer her a food ration.' if item_rations:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a food ration.')
                                $ item_rations -= 1
                                $ renpy.notify("You lost a food ration.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                $ aegidia_highisland_tired = 0
                                $ aegidia_highisland_opinion = 1
                                $ custom1 = "“Perfect,” still barefoot, she gets up and leaps toward you, grabbing the meal without wasting time on examining it."
                                jump highisland_crew_camp101a
                            'I offer her a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast fish and some fruits.')
                                $ item_cookedfish -= 1
                                $ item_wildplants -= 1
                                $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                $ aegidia_highisland_tired = 0
                                $ aegidia_highisland_opinion = 1
                                $ custom1 = "“Perfect,” still barefoot, she gets up and leaps toward you, grabbing the meal without wasting time on examining it."
                                jump highisland_crew_camp101a
                            'I offer her a roast chicken.' if item_chicken:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast chicken.')
                                $ item_chicken -= 1
                                $ renpy.notify("You lost a roast chicken.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                $ aegidia_highisland_tired = 0
                                $ aegidia_highisland_opinion = 1
                                $ custom1 = "“Perfect,” still barefoot, she gets up and leaps toward you, grabbing the meal without wasting time on examining it."
                                jump highisland_crew_camp101a
                            'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                pass
                            'I look away.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look away.')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                'I meet {color=#f6d6bd}Dalit’s{/color} eyes.' if dalit_highisland_joined and not dalit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I meet {color=#f6d6bd}Dalit’s{/color} eyes.')
                    if not dalit_highisland_blocked and not dalit_highisland_tired:
                        $ custom1 = "She gives you a playful smile, but says nothing. Her new ponytail reveals her small ears."
                        $ dalit_highisland_opinion = 1
                        jump highisland_crew_camp101a
                    elif dalit_highisland_blocked:
                        menu:
                            'Her new ponytail reveals her small ears. “I wish I could do something about this nasty wound...”
                            '
                            '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                $ highisland_camp1_tuliahelp_used = 1
                                $ dalit_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                if not dalit_highisland_tired:
                                    $ dalit_highisland_opinion = 1
                                    $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Dalit{/color} and pays you no more attention."
                                else:
                                    $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Dalit{/color} and pays you no more attention. Soon after, her {i}patient{/i} mentions she’s a bit hungry, but seems to feel much better."
                                jump highisland_crew_camp101a
                            'I offer her a healing potion.' if item_generichealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a healing potion.')
                                $ item_generichealingpotion -= 1
                                $ renpy.notify("You lost a healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                $ dalit_highisland_blocked = 0
                                $ dalit_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ dalit_highisland_opinion = 1
                                $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand. “I hope it tastes better than the ones from the monastery.”"
                                jump highisland_crew_camp101a
                            'I offer her the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her the potion from the dolmen.')
                                $ item_potiondolmen -= 1
                                $ renpy.notify("You lost the potion from the dolmen.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                $ dalit_highisland_blocked = 0
                                $ dalit_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ dalit_highisland_opinion = 1
                                $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand. “I hope it tastes better than the ones from the monastery.”"
                                jump highisland_crew_camp101a
                            'I offer her a small healing potion.' if item_smallhealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a small healing potion.')
                                $ item_smallhealingpotion -= 1
                                $ renpy.notify("You lost a small healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                $ dalit_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                if not dalit_highisland_tired:
                                    $ dalit_highisland_opinion = 1
                                    $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand. “I hope it tastes better than the ones from the monastery.”"
                                else:
                                    $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand. “I hope it tastes better than the ones from the monastery. Tell me if you have any leftovers to spare.”"
                                jump highisland_crew_camp101a
                            'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                pass
                            'I nod.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                    elif dalit_highisland_tired:
                        menu:
                            'Her new ponytail reveals her small ears. “I wish I had some water-resistant food with me... I got soaked on that boat, too!”
                            '
                            'I unroll {color=#f6d6bd}Asterion’s{/color} cloak. “You can warm yourself up with this.”' if item_asterioncloak and not highisland_camp1_asterioncloak_used:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I unroll {color=#f6d6bd}Asterion’s{/color} cloak. “You can warm yourself up with this.”')
                                $ dalit_highisland_tired = 0
                                $ dalit_highisland_opinion = 1
                                $ custom1 = "Hesitant at first, she wraps herself up, and her eyes widen. “Huh. That’s some {i}nice{/i} fabric.”"
                                jump highisland_crew_camp101a
                            'I offer her a food ration.' if item_rations:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a food ration.')
                                $ item_rations -= 1
                                $ renpy.notify("You lost a food ration.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                $ dalit_highisland_tired = 0
                                $ dalit_highisland_opinion = 1
                                $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand, licking her lips. She devours it like a dock worker on a break."
                                jump highisland_crew_camp101a
                            'I offer her a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast fish and some fruits.')
                                $ item_cookedfish -= 1
                                $ item_wildplants -= 1
                                $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                $ dalit_highisland_tired = 0
                                $ dalit_highisland_opinion = 1
                                $ custom1 = "She gestures for you to throw them to her, but after seeing your hesitation, she takes it from your hand, licking her lips. She devours it like a dock worker on a break."
                                jump highisland_crew_camp101a
                            'I offer her a roast chicken.' if item_chicken:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast chicken.')
                                $ item_chicken -= 1
                                $ renpy.notify("You lost a roast chicken.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                $ dalit_highisland_tired = 0
                                $ dalit_highisland_opinion = 1
                                $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand, licking her lips. She devours it like a dock worker on a break."
                                jump highisland_crew_camp101a
                            'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                pass
                            'I nod.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                '“Are you in one piece, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and not efren_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you in one piece, {color=#f6d6bd}Efren{/color}?”')
                    if not efren_highisland_blocked and not efren_highisland_tired:
                        $ custom1 = "He waves you off, constantly observing the entrance."
                        $ efren_highisland_opinion = 1
                        jump highisland_crew_camp101a
                    elif efren_highisland_blocked:
                        menu:
                            'He waves you off, constantly observing the entrance, but then lets out a hiss and reaches toward his wounded arm.
                            '
                            '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                $ highisland_camp1_tuliahelp_used = 1
                                $ efren_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                if not efren_highisland_tired:
                                    $ efren_highisland_opinion = 1
                                    $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Efren{/color} and pays you no more attention."
                                else:
                                    $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Efren{/color} and pays you no more attention. Soon after, her {i}patient{/i} mentions he’s a bit hungry, but seems to feel much better."
                                jump highisland_crew_camp101a
                            'I offer him a healing potion.' if item_generichealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a healing potion.')
                                $ item_generichealingpotion -= 1
                                $ renpy.notify("You lost a healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                $ efren_highisland_blocked = 0
                                $ efren_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ efren_highisland_opinion = 1
                                $ custom1 = "As he still ignores you, you stand up and put the bottle next to him. After a moment of hesitation, he empties the bottle with a single gulp."
                                jump highisland_crew_camp101a
                            'I offer him the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him the potion from the dolmen.')
                                $ item_potiondolmen -= 1
                                $ renpy.notify("You lost the potion from the dolmen.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                $ efren_highisland_blocked = 0
                                $ efren_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ efren_highisland_opinion = 1
                                $ custom1 = "As he still ignores you, you stand up and put the bottle next to him. After a moment of hesitation, he empties the bottle with a single gulp."
                                jump highisland_crew_camp101a
                            'I offer him a small healing potion.' if item_smallhealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a small healing potion.')
                                $ item_smallhealingpotion -= 1
                                $ renpy.notify("You lost a small healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                $ efren_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                if not efren_highisland_tired:
                                    $ efren_highisland_opinion = 1
                                    $ custom1 = "As he still ignores you, you stand up and put the bottle next to him. After a moment of hesitation, he empties the bottle with a single sip."
                                else:
                                    $ custom1 = "As he still ignores you, you stand up and put the bottle next to him. After a moment of hesitation, he empties the bottle with a single sip, but then his stomach makes a loud growl."
                                jump highisland_crew_camp101a
                            'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                pass
                            'I shrug.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug.')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                    elif efren_highisland_tired:
                        menu:
                            'He waves you off, constantly observing the entrance, but then his stomach makes a loud growl.
                            '
                            'I offer him a food ration.' if item_rations:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a food ration.')
                                $ item_rations -= 1
                                $ renpy.notify("You lost a food ration.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                $ efren_highisland_tired = 0
                                $ efren_highisland_opinion = 1
                                $ custom1 = "As he still ignores you, you stand up and put the meal next to him. After a moment of hesitation, he bites into it like a wolf."
                                jump highisland_crew_camp101a
                            'I offer him a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast fish and some fruits.')
                                $ item_cookedfish -= 1
                                $ item_wildplants -= 1
                                $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                $ efren_highisland_tired = 0
                                $ efren_highisland_opinion = 1
                                $ custom1 = "As he still ignores you, you stand up and put the meal next to him. After a moment of hesitation, he bites into it like a wolf."
                                jump highisland_crew_camp101a
                            'I offer him a roast chicken.' if item_chicken:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast chicken.')
                                $ item_chicken -= 1
                                $ renpy.notify("You lost a roast chicken.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                $ efren_highisland_tired = 0
                                $ efren_highisland_opinion = 1
                                $ custom1 = "As he still ignores you, you stand up and put the meal next to him. After a moment of hesitation, he bites into it like a wolf."
                                jump highisland_crew_camp101a
                            'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                pass
                            'I shrug.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug.')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                'I glance at {color=#f6d6bd}Thyrsus{/color}.' if thyrsus_highisland_joined and not thyrsus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at {color=#f6d6bd}Thyrsus{/color}.')
                    if not thyrsus_highisland_blocked and not thyrsus_highisland_tired:
                        $ custom1 = "After collecting his amulets, he winks at you and drinks something from a small flask. “Ready when you are.”"
                        $ thyrsus_highisland_opinion = 1
                        jump highisland_crew_camp101a
                    elif thyrsus_highisland_blocked and not thyrsus_highisland_tired:
                        $ custom1 = "After collecting his amulets, he opens a sizable flask and takes a big gulp, then puts on a disgusted grimace. He reaches for his wound and pats it a few times, then stretches out and winks at you. “Ready when you are.”"
                        $ thyrsus_highisland_blocked = 0
                        $ thyrsus_highisland_opinion = 1
                        $ highisland_crew_left += 1
                        jump highisland_crew_camp101a
                    elif thyrsus_highisland_tired:
                        if thyrsus_highisland_blocked:
                            $ custom1 = "After collecting his amulets, he opens a sizable flask and takes a big gulp, then puts on a disgusted grimace. He reaches for his wound and pats it a few times, then stretches out and winks at you. “Ready when you are, but I’d rather eat something first.”"
                            $ thyrsus_highisland_blocked = 0
                            $ highisland_crew_left += 1
                        else:
                            $ custom1 = "After collecting his amulets, he winks at you and drinks something from a small flask. “Ready when you are, but I’d rather eat something first.”"
                        menu:
                            '[custom1]
                            '
                            'I offer him a food ration.' if item_rations:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a food ration.')
                                $ item_rations -= 1
                                $ renpy.notify("You lost a food ration.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                $ thyrsus_highisland_tired = 0
                                $ thyrsus_highisland_opinion = 1
                                $ custom1 = "He reaches for it from where he sits with a creeper, but moves it so quickly he crashes the meal against his nose. He lets out an awkward chuckle."
                                jump highisland_crew_camp101a
                            'I offer him a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast fish and some fruits.')
                                $ item_cookedfish -= 1
                                $ item_wildplants -= 1
                                $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                $ thyrsus_highisland_tired = 0
                                $ thyrsus_highisland_opinion = 1
                                $ custom1 = "He reaches for them from where he sits with a creeper, but moves it so quickly he crashes the meal against his nose. He lets out an awkward chuckle."
                                jump highisland_crew_camp101a
                            'I offer him a roast chicken.' if item_chicken:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast chicken.')
                                $ item_chicken -= 1
                                $ renpy.notify("You lost a roast chicken.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                $ thyrsus_highisland_tired = 0
                                $ thyrsus_highisland_opinion = 1
                                $ custom1 = "He reaches for it from where he sits with a creeper, but moves it so quickly he crashes the meal against his nose. He lets out an awkward chuckle."
                                jump highisland_crew_camp101a
                            'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                pass
                            '“Great.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Great.”')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and not pyrrhos_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                    if not pyrrhos_highisland_blocked and not pyrrhos_highisland_tired:
                        $ custom1 = "He glances at you. “Huh? I’m alright.”"
                        $ pyrrhos_highisland_opinion = 1
                        jump highisland_crew_camp101a
                    elif pyrrhos_highisland_blocked:
                        menu:
                            'He glances at you. “Huh? My leg aches, but I’ll make it.”
                            '
                            '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                $ highisland_camp1_tuliahelp_used = 1
                                $ pyrrhos_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                if not pyrrhos_highisland_tired:
                                    $ pyrrhos_highisland_opinion = 1
                                    $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Pyrrhos{/color} and pays you no more attention."
                                else:
                                    $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Pyrrhos{/color} and pays you no more attention. Soon after, her {i}patient{/i} mentions he’s a bit hungry, but seems to feel much better."
                                jump highisland_crew_camp101a
                            'I offer him a healing potion.' if item_generichealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a healing potion.')
                                $ item_generichealingpotion -= 1
                                $ renpy.notify("You lost a healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                $ pyrrhos_highisland_blocked = 0
                                $ pyrrhos_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ pyrrhos_highisland_opinion = 1
                                $ custom1 = "“Ye sure, roadster?” He steps closer and, after you reach out to him with the flask on your open palm, he grabs it, smiling widely."
                                jump highisland_crew_camp101a
                            'I offer him the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him the potion from the dolmen.')
                                $ item_potiondolmen -= 1
                                $ renpy.notify("You lost the potion from the dolmen.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                $ pyrrhos_highisland_blocked = 0
                                $ pyrrhos_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ pyrrhos_highisland_opinion = 1
                                $ custom1 = "“Ye sure, roadster?” He steps closer and, after you reach out to him with the flask on your open palm, he grabs it, smiling widely."
                                jump highisland_crew_camp101a
                            'I offer him a small healing potion.' if item_smallhealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a small healing potion.')
                                $ item_smallhealingpotion -= 1
                                $ renpy.notify("You lost a small healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                $ pyrrhos_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                if not pyrrhos_highisland_tired:
                                    $ pyrrhos_highisland_opinion = 1
                                    $ custom1 = "“Ye sure, roadster?” He steps closer and, after you reach out to him with the flask on your open palm, he grabs it, smiling widely."
                                else:
                                    $ custom1 = "“Ye sure, roadster?” He steps closer and, after you reach out to him with the flask on your open palm, he grabs it, smiling widely. “And what now? Yer going to tell me ye’ve some oats to spare?”"
                                jump highisland_crew_camp101a
                            'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                pass
                            '“Very well.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well.”')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                    elif pyrrhos_highisland_tired:
                        menu:
                            'He glances at you. “Huh? I’m alright. Unless ye’ve got some oats to spare?”
                            '
                            'I offer him a food ration.' if item_rations:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a food ration.')
                                $ item_rations -= 1
                                $ renpy.notify("You lost a food ration.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                $ pyrrhos_highisland_tired = 0
                                $ pyrrhos_highisland_opinion = 1
                                $ custom1 = "His beard shakes from his chuckle. “Cheers, roadster!”"
                                jump highisland_crew_camp101a
                            'I offer him a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast fish and some fruits.')
                                $ item_cookedfish -= 1
                                $ item_wildplants -= 1
                                $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                $ pyrrhos_highisland_tired = 0
                                $ pyrrhos_highisland_opinion = 1
                                $ custom1 = "His beard shakes from his chuckle. “Cheers, roadster!”"
                                jump highisland_crew_camp101a
                            'I offer him a roast chicken.' if item_chicken:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast chicken.')
                                $ item_chicken -= 1
                                $ renpy.notify("You lost a roast chicken.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                $ pyrrhos_highisland_tired = 0
                                $ pyrrhos_highisland_opinion = 1
                                $ custom1 = "His beard shakes from his chuckle. “Cheers, roadster!”"
                                jump highisland_crew_camp101a
                            'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                pass
                            '“No. No oats.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No. No oats.”')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                'I observe {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and not bandit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe {color=#f6d6bd}the bandit{/color}.')
                    if not bandit_highisland_blocked and not bandit_highisland_tired:
                        $ custom1 = "When he raises his head, he looks like a thoughtful statue, but spares not a single glance to anyone around him."
                        $ bandit_highisland_opinion = 1
                        jump highisland_crew_camp101a
                    elif bandit_highisland_blocked:
                        menu:
                            'When he raises his head, he looks like a thoughtful statue, but spares not a single glance to anyone around him - despite the trail of blood reaching from his forehead to his chin. After you point it out, he lets out a sigh. “Right, they got me well, they did. Say, you have any snake bait? I need to sharpen my senses.”
                            '
                            '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                $ highisland_camp1_tuliahelp_used = 1
                                $ bandit_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                if not bandit_highisland_tired:
                                    $ bandit_highisland_opinion = 1
                                    $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}the bandit{/color} and pays you no more attention."
                                else:
                                    $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}the bandit{/color} and pays you no more attention. Soon after, her {i}patient{/i} mentions he’s a bit hungry, but seems to feel much better."
                                jump highisland_crew_camp101a
                            'I offer him a healing potion.' if item_generichealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a healing potion.')
                                $ item_generichealingpotion -= 1
                                $ renpy.notify("You lost a healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                $ bandit_highisland_blocked = 0
                                $ bandit_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ bandit_highisland_opinion = 1
                                $ custom1 = "He frowns as if you’ve just interrupted him, but obediently gets up and takes the flask from you."
                                jump highisland_crew_camp101a
                            'I offer him the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him the potion from the dolmen.')
                                $ item_potiondolmen -= 1
                                $ renpy.notify("You lost the potion from the dolmen.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                $ bandit_highisland_blocked = 0
                                $ bandit_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ bandit_highisland_opinion = 1
                                $ custom1 = "He frowns as if you’ve just interrupted him, but obediently gets up and takes the flask from you."
                                jump highisland_crew_camp101a
                            'I offer him a small healing potion.' if item_smallhealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a small healing potion.')
                                $ item_smallhealingpotion -= 1
                                $ renpy.notify("You lost a small healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                $ bandit_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                if not bandit_highisland_tired:
                                    $ bandit_highisland_opinion = 1
                                    $ custom1 = "He frowns as if you’ve just interrupted him, but obediently gets up and takes the flask from you."
                                else:
                                    $ custom1 = "He frowns as if you’ve just interrupted him, but obediently gets up and takes the flask from you. “Fine... But I still feel a bit weak.”"
                                jump highisland_crew_camp101a
                            'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                pass
                            '“Here. Some snake bait.”' if item_snakebait:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here. Some snake bait.”')
                                $ item_snakebait -= 1
                                $ renpy.notify("You lost the snake bait.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the snake bait.{/i}')
                                $ bandit_highisland_blocked = 0
                                $ bandit_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ bandit_highisland_opinion = 1
                                $ custom1 = "He grins widely. “I’ll put it to good use.”"
                                jump highisland_crew_camp101a
                            '“Better. Want the proper sharpening poison?”' if item_sharpeningpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Better. Want the proper sharpening poison?”')
                                $ item_sharpeningpotion -= 1
                                $ renpy.notify("You lost a dose of sharpening poison.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a dose of sharpening poison.{/i}')
                                $ bandit_highisland_blocked = 0
                                $ bandit_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ bandit_highisland_opinion = 1
                                $ custom1 = "He grins widely. “I’ll put it to good use.”"
                                jump highisland_crew_camp101a
                            'I can’t help him with that.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t help him with that.')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                    elif bandit_highisland_tired:
                        menu:
                            'When he raises his head, he looks like a thoughtful statue, but spares not a single glance to anyone around him. After you point out that his eyes look exhausted, he lets out a sigh. “Right. I guess I could eat.”
                            '
                            'I offer him a food ration.' if item_rations:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a food ration.')
                                $ item_rations -= 1
                                $ renpy.notify("You lost a food ration.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                $ bandit_highisland_tired = 0
                                $ bandit_highisland_opinion = 1
                                $ custom1 = "Unconvinced at first, he finally gets up and takes the meal from you. “Thanks, I guess.”"
                                jump highisland_crew_camp101a
                            'I offer him a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast fish and some fruits.')
                                $ item_cookedfish -= 1
                                $ item_wildplants -= 1
                                $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                $ bandit_highisland_tired = 0
                                $ bandit_highisland_opinion = 1
                                $ custom1 = "Unconvinced at first, he finally gets up and takes the meal from you. “Thanks, I guess.”"
                                jump highisland_crew_camp101a
                            'I offer him a roast chicken.' if item_chicken:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast chicken.')
                                $ item_chicken -= 1
                                $ renpy.notify("You lost a roast chicken.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                $ bandit_highisland_tired = 0
                                $ bandit_highisland_opinion = 1
                                $ custom1 = "Unconvinced at first, he finally gets up and takes the meal from you. “Thanks, I guess.”"
                                jump highisland_crew_camp101a
                            'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                pass
                            'I can’t help him with that.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t help him with that.')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                '“How are you doing, {color=#f6d6bd}Tulia{/color}?”' if tulia_highisland_joined and not tulia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How are you doing, {color=#f6d6bd}Tulia{/color}?”')
                    if not tulia_highisland_blocked and not tulia_highisland_tired:
                        if highisland_camp1_tuliahelp_used:
                            $ custom1 = "She steps away from her patient and throws away a scrap of dirty fabric. “Better than some, that’s for sure.”"
                        else:
                            $ custom1 = "You feel the warmth of her shoulder. “Pretty well. If anyone here needs someone to look at their wounds, just let me know. I’ve got enough balms and bandages for one person.”"
                        $ tulia_highisland_opinion = 1
                        jump highisland_crew_camp101a
                    elif tulia_highisland_blocked and not tulia_highisland_tired:
                        $ custom1 = "You feel the warmth of her shoulder. She cleans the wound on her neck, soaking the bandages with a remedy that smells like swamp herbs. “Pretty well.”"
                        $ highisland_camp1_tuliahelp_used = 1
                        $ tulia_highisland_blocked = 0
                        $ tulia_highisland_opinion = 1
                        $ highisland_crew_left += 1
                        jump highisland_crew_camp101a
                    elif tulia_highisland_tired:
                        if tulia_highisland_blocked:
                            $ highisland_camp1_tuliahelp_used = 1
                            $ custom1 = "You feel the warmth of her shoulder. She cleans the wound on her neck, soaking the bandages with a remedy that smells like swamp herbs. “Pretty well. Just a bit hungry.”"
                            $ tulia_highisland_blocked = 0
                            $ highisland_crew_left += 1
                        else:
                            $ custom1 = "You feel the warmth of her shoulder. “Pretty well. Just a bit hungry.”"
                        menu:
                            '[custom1]
                            '
                            'I offer her a food ration.' if item_rations:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a food ration.')
                                $ item_rations -= 1
                                $ renpy.notify("You lost a food ration.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                $ tulia_highisland_tired = 0
                                $ tulia_highisland_opinion = 1
                                if not highisland_camp1_tuliahelp_used:
                                    $ highisland_camp1_tuliahelp_available = 1
                                    $ custom1 = "“Thank you. Now, if anyone here needs someone to look at their wounds, just let me know. I’ve got enough balms and bandages for one person.”"
                                else:
                                    $ custom1 = "“Thank you. I just need to rest now.”"
                                jump highisland_crew_camp101a
                            'I offer her a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast fish and some fruits.')
                                $ item_cookedfish -= 1
                                $ item_wildplants -= 1
                                $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                $ tulia_highisland_tired = 0
                                $ tulia_highisland_opinion = 1
                                if not highisland_camp1_tuliahelp_used:
                                    $ highisland_camp1_tuliahelp_available = 1
                                    $ custom1 = "“Thank you. Now, if anyone here needs someone to look at their wounds, just let me know. I’ve got enough balms and bandages for one person.”"
                                else:
                                    $ custom1 = "“Thank you. I just need to rest now.”"
                                jump highisland_crew_camp101a
                            'I offer her a roast chicken.' if item_chicken:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast chicken.')
                                $ item_chicken -= 1
                                $ renpy.notify("You lost a roast chicken.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                $ tulia_highisland_tired = 0
                                $ tulia_highisland_opinion = 1
                                if not highisland_camp1_tuliahelp_used:
                                    $ highisland_camp1_tuliahelp_available = 1
                                    $ custom1 = "“Thank you. Now, if anyone here needs someone to look at their wounds, just let me know. I’ve got enough balms and bandages for one person.”"
                                else:
                                    $ custom1 = "“Thank you. I just need to rest now.”"
                                jump highisland_crew_camp101a
                            'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                pass
                            '“I’m glad you’re alright.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad you’re alright.”')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                '“Are you hanging in there, {color=#f6d6bd}Tzvi{/color}?”' if tzvi_highisland_joined and not tzvi_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you hanging in there, {color=#f6d6bd}Tzvi{/color}?”')
                    if not tzvi_highisland_blocked:
                        $ tzvi_highisland_tired = 0
                        $ custom1 = "“Very green, this forest,” he sounds as if he’s talking to himself, but then brings you a few wild fruits. “Here. I found more than I can eat.”"
                        $ tzvi_highisland_opinion = 1
                        $ item_wildplants += 1
                        $ renpy.notify("You got a bunch of wild plants.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You got a bunch of wild plants.{/i}')
                        jump highisland_crew_camp101a
                    elif tzvi_highisland_blocked:
                        if tzvi_highisland_tired:
                            $ tzvi_highisland_tired = 0
                            $ custom1 = "He shrugs, chewing on some leaves he found growing around. “I could use something for my wound.”"
                        else:
                            $ custom1 = "“Very green, this forest,” he sounds as if he’s talking to himself, but then brings you a few wild fruits. “Here. I found more than I can eat. But I could use something for my wound.”"
                            $ item_wildplants += 1
                            $ renpy.notify("You got a bunch of wild plants.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You got a bunch of wild plants.{/i}')
                        menu:
                            '[custom1]
                            '
                            '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                $ highisland_camp1_tuliahelp_used = 1
                                $ tzvi_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                $ tzvi_highisland_opinion = 1
                                $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Tzvi{/color} and pays you no more attention."
                                jump highisland_crew_camp101a
                            'I offer him a healing potion.' if item_generichealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a healing potion.')
                                $ item_generichealingpotion -= 1
                                $ renpy.notify("You lost a healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                $ tzvi_highisland_blocked = 0
                                $ tzvi_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ tzvi_highisland_opinion = 1
                                $ custom1 = "With a nod, he grabs the flask and carries it away."
                                jump highisland_crew_camp101a
                            'I offer him the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him the potion from the dolmen.')
                                $ item_potiondolmen -= 1
                                $ renpy.notify("You lost the potion from the dolmen.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                $ tzvi_highisland_blocked = 0
                                $ tzvi_highisland_tired = 0
                                $ highisland_crew_left += 1
                                $ tzvi_highisland_opinion = 1
                                $ custom1 = "With a nod, he grabs the flask and carries it away."
                                jump highisland_crew_camp101a
                            'I offer him a small healing potion.' if item_smallhealingpotion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a small healing potion.')
                                $ item_smallhealingpotion -= 1
                                $ renpy.notify("You lost a small healing potion.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                $ tzvi_highisland_blocked = 0
                                $ highisland_crew_left += 1
                                $ tzvi_highisland_opinion = 1
                                $ custom1 = "With a nod, he grabs the flask and carries it away."
                                jump highisland_crew_camp101a
                            'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                pass
                            '“I’ll see what I can do.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll see what I can do.”')
                                $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                jump highisland_crew_camp101a
                '“{color=#f6d6bd}Quintus{/color}, still alive?”' if quintus_highisland_joined and not quintus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Quintus{/color}, still alive?”')
                    if not quintus_highisland_blocked and not quintus_highisland_tired:
                        if item_crossbow:
                            $ custom1 = "“Duh,” he mutters while looking into his bag, then smiles at you. “It’s easier than I thought! And good thing I brought no crossbow to slow me down, I can’t see shit. Want to take the quarrels that I forgot to unpack?”"
                            $ item_crossbowquarrels += 2
                            $ renpy.notify("You received 2 quarrels.\nYou’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost two quarrels. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                        else:
                            $ custom1 = "“Duh,” he mutters while looking into his bag, then smiles at you. “It’s easier than I thought! And good thing I brought no crossbow, I can’t see shit. It would only slow me down.”"
                        $ quintus_highisland_opinion = 1
                        jump highisland_crew_camp101a
                    elif quintus_highisland_blocked:
                        $ quintus_highisland_blocked = 0
                        $ quintus_highisland_tired = 0
                        $ highisland_crew_left += 1
                        $ quintus_highisland_opinion = 1
                        if item_crossbow:
                            $ custom1 = "“Duh,” he mutters while holding the now-empty bottle of a healing potion that he brought with him. “They {i}almost{/i} got me, but I’m fine. And good thing I brought no crossbow to slow me down, I can’t see shit. Want to take the quarrels that I forgot to unpack?”"
                            $ item_crossbowquarrels += 2
                            $ renpy.notify("You received 2 quarrels.\nYou’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost two quarrels. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                        else:
                            $ custom1 = "“Duh,” he mutters while holding the now-empty bottle of a healing potion that he brought with him. “They {i}almost{/i} got me, but I’m fine. And good thing I brought no crossbow, I can’t see shit. It would only slow me down.”"
                        jump highisland_crew_camp101a
                    elif quintus_highisland_tired:
                        menu:
                            '“Duh,” he mutters while looking into his bag. “It’s easier than I thought! And good thing I brought no crossbow to slow me down, I can’t see shit.” He then looks at you and adjusts his bandage. “Got anything to eat, [pcname]?”
                            '
                            'I offer him a food ration.' if item_rations:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a food ration.')
                                $ item_rations -= 1
                                $ quintus_highisland_tired = 0
                                $ quintus_highisland_opinion = 1
                                if item_crossbow:
                                    $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready. Want to take the quarrels that I forgot to unpack?”"
                                    $ item_crossbowquarrels += 2
                                    $ renpy.notify("You lost a food ration.\nYou received 2 quarrels.\nYou’ve got %s quarrels left." %item_crossbowquarrels)
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration. You lost two quarrels. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                                else:
                                    $ renpy.notify("You lost a food ration.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                    $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready.”"
                                jump highisland_crew_camp101a
                            'I offer him a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast fish and some fruits.')
                                $ item_cookedfish -= 1
                                $ item_wildplants -= 1
                                $ quintus_highisland_tired = 0
                                $ quintus_highisland_opinion = 1
                                if item_crossbow:
                                    $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready. Want to take the quarrels that I forgot to unpack?”"
                                    $ item_crossbowquarrels += 2
                                    $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.\nYou received 2 quarrels.\nYou’ve got %s quarrels left." %item_crossbowquarrels)
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants. You lost two quarrels. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                                else:
                                    $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                    $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready.”"
                                jump highisland_crew_camp101a
                            'I offer him a roast chicken.' if item_chicken:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast chicken.')
                                $ item_chicken -= 1
                                $ quintus_highisland_tired = 0
                                $ quintus_highisland_opinion = 1
                                if item_crossbow:
                                    $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready. Want to take the quarrels that I forgot to unpack?”"
                                    $ item_crossbowquarrels += 2
                                    $ renpy.notify("You lost a roast chicken.\nYou received 2 quarrels.\nYou’ve got %s quarrels left." %item_crossbowquarrels)
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken. You lost two quarrels. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                                else:
                                    $ renpy.notify("You lost a roast chicken.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                    $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready.”"
                                jump highisland_crew_camp101a
                            'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                pass
                            '“I don’t think so...”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t think so...”')
                                $ custom1 = "He lets out a disappointed sigh."
                                jump highisland_crew_camp101a
                'I let my back and limbs rest for a bit, then prepare my tools to cut through the bushes. “Time to carry on.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let my back and limbs rest for a bit, then prepare my tools to cut through the bushes. “Time to carry on.”')
                    $ highisland_destination = "denseplants"
                    jump highisland_destination

        label highisland_crew_camp101a:
            if pyrrhos_highisland_opinion == 1 and armor < 3:
                $ pyrrhos_highisland_opinion = 2
                menu:
                    'Soon after you look away, {color=#f6d6bd}Pyrrhos{/color} calls you back. “I’ve no fancy tools, but if ye help me, we’ll fix that jacket of yas a bit.”
                    '
                    '“I’ve a proper repair set. Let’s get to it.”' if item_gambesonrepairset:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve a proper repair set. Let’s get to it.”')
                        $ armor = limit_armor(armor+2)
                        show plus2armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 armor points.{/i}')
                        $ custom1 = "The simple repairs go smoothly and you soon put on the restored gambeson."
                        jump highisland_crew_camp101a
                    '“Thanks.”' if not item_gambesonrepairset:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                        $ armor = limit_armor(armor+1)
                        show plus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 armor point.{/i}')
                        $ custom1 = "The simple repairs go smoothly and you soon put on the restored gambeson."
                        jump highisland_crew_camp101a
            else:
                menu:
                    '[custom1]
                    '
                    'I try to figure out what these ruins used to be.' if not highisland_camp1_examine:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to figure out what these ruins used to be.')
                        $ highisland_camp1_examine = 1
                        $ custom1 = "Judging by the stone wall and the now-collapsed tower, it could have served as a shelter for two dozen humans at once. There are no remains of any sheds, working stations, or tools, and you see nothing unusual about the surrounding rocks and plants."
                        jump highisland_crew_camp101a
                    'I look up at the night sky, seeking a sign from my ancestors.' if highisland_camp1_canpray and not highisland_camp1_prayed and pc_religion == "pagan":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look up at the night sky, seeking a sign from my ancestors.')
                        $ highisland_camp1_prayed = 1
                        $ highisland_camp1_canpray = 0
                        if pc_faithpoints_opportunities >= 8 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                            $ pc_hp = limit_pc_hp(pc_hp+2)
                            show plus2hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                            if pc_class == "mage":
                                $ mana = limit_mana(mana+2)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                            $ custom1 = "Long minutes go by and your breath gets slower, your eyes sharper. Among the stars and clouds, you see the shapes of your tribe’s home. Your exhausted questions and requests turn into certainty. “You can do this,” a voice in the wind tells you, sending chills down your spine."
                        elif pc_faithpoints_opportunities >= 6 and (pc_faithpoints+(achievement_animalssavedpoints/2)) >= (pc_faithpoints_opportunities*0.75):
                            $ pc_hp = limit_pc_hp(pc_hp+1)
                            show plus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 vitality point.{/i}')
                            if pc_class == "mage":
                                $ mana = limit_mana(mana+2)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                            $ custom1 = "Long minutes go by and your breath gets slower, your eyes sharper. Among the stars and clouds, you see the shapes of your tribe’s home and of the animals you spared on your journey. Your exhausted questions and requests turn into certainty. “You can do this,” a voice in the wind tells you, sending chills down your spine."
                        else:
                            $ custom1 = "Long minutes go by, but the stars are as distant as always, distorted by the clouds."
                        jump highisland_crew_camp101a
                    'I bow my head and try to ignore the loud beasts of the woods. I need Wright’s guidance.' if highisland_camp1_canpray and not highisland_camp1_prayed and pc_religion != "pagan":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bow my head and try to ignore the loud beasts of the woods. I need Wright’s guidance.')
                        $ highisland_camp1_prayed = 1
                        $ highisland_camp1_canpray = 0
                        if pc_faithpoints_opportunities >= 8 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                            $ pc_hp = limit_pc_hp(pc_hp+2)
                            show plus2hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 vitality points.{/i}')
                            if pc_class == "mage":
                                $ mana = limit_mana(mana+2)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 pneuma.{/i}')
                            $ custom1 = "Long minutes go by, your shoulders slump. As you shape your awkward, exhausted prayers, you keep examining your deeds from the recent days, until a warm, rejuvenating gust of wind fills your mouth. You spring to your feet, ready to reach your destination."
                        else:
                            $ custom1 = "Long minutes go by, but the only answer you hear belongs to hungry creatures. Distracted, you keep glancing at the entrance."
                        jump highisland_crew_camp101a
                    'I look at {color=#f6d6bd}Aegidia{/color}.' if aegidia_highisland_joined and not aegidia_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}Aegidia{/color}.')
                        if not aegidia_highisland_blocked and not aegidia_highisland_tired:
                            $ custom1 = "She returns your gaze and gives you a kind smile. She’s ready for the next challenge."
                            $ aegidia_highisland_opinion = 1
                            jump highisland_crew_camp101a
                        elif aegidia_highisland_blocked:
                            menu:
                                'She returns your gaze and gives you a sad smile. She holds her wounded side to stop the pain.
                                '
                                '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                    $ highisland_camp1_tuliahelp_used = 1
                                    $ aegidia_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    if not aegidia_highisland_tired:
                                        $ aegidia_highisland_opinion = 1
                                        $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Aegidia{/color} and pays you no more attention."
                                    else:
                                        $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Aegidia{/color} and pays you no more attention. Soon after, her {i}patient{/i} mentions she’s a bit hungry, but seems to feel much better."
                                    jump highisland_crew_camp101a
                                'I offer her a healing potion.' if item_generichealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a healing potion.')
                                    $ item_generichealingpotion -= 1
                                    $ renpy.notify("You lost a healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                    $ aegidia_highisland_blocked = 0
                                    $ aegidia_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ aegidia_highisland_opinion = 1
                                    $ custom1 = "“Thank you,” she sniffs the contents, drinks it slowly, and leans away with a sigh."
                                    jump highisland_crew_camp101a
                                'I offer her the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her the potion from the dolmen.')
                                    $ item_potiondolmen -= 1
                                    $ renpy.notify("You lost the potion from the dolmen.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                    $ aegidia_highisland_blocked = 0
                                    $ aegidia_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ aegidia_highisland_opinion = 1
                                    $ custom1 = "“Thank you,” she sniffs the contents, drinks it slowly, and leans away with a sigh."
                                    jump highisland_crew_camp101a
                                'I offer her a small healing potion.' if item_smallhealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a small healing potion.')
                                    $ item_smallhealingpotion -= 1
                                    $ renpy.notify("You lost a small healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                    $ aegidia_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    if not aegidia_highisland_tired:
                                        $ aegidia_highisland_opinion = 1
                                        $ custom1 = "“Thank you,” she sniffs the contents, drinks it slowly, and leans away with a sigh."
                                    else:
                                        $ custom1 = "“Thank you,” she sniffs the contents, drinks it slowly, and leans away with a sigh. “Such a stroll sure makes one hungry, huh?”"
                                    jump highisland_crew_camp101a
                                'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                    pass
                                'I look away.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look away.')
                                    jump highisland_crew_camp101a
                        elif aegidia_highisland_tired:
                            menu:
                                'She returns your gaze and gives you a tired smile. “Such a stroll sure makes one hungry, huh?”
                                '
                                'I offer her a food ration.' if item_rations:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a food ration.')
                                    $ item_rations -= 1
                                    $ renpy.notify("You lost a food ration.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                    $ aegidia_highisland_tired = 0
                                    $ aegidia_highisland_opinion = 1
                                    $ custom1 = "“Perfect,” still barefoot, she gets up and leaps toward you, grabbing the meal without wasting time on examining it."
                                    jump highisland_crew_camp101a
                                'I offer her a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast fish and some fruits.')
                                    $ item_cookedfish -= 1
                                    $ item_wildplants -= 1
                                    $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                    $ aegidia_highisland_tired = 0
                                    $ aegidia_highisland_opinion = 1
                                    $ custom1 = "“Perfect,” still barefoot, she gets up and leaps toward you, grabbing the meal without wasting time on examining it."
                                    jump highisland_crew_camp101a
                                'I offer her a roast chicken.' if item_chicken:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast chicken.')
                                    $ item_chicken -= 1
                                    $ renpy.notify("You lost a roast chicken.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                    $ aegidia_highisland_tired = 0
                                    $ aegidia_highisland_opinion = 1
                                    $ custom1 = "“Perfect,” still barefoot, she gets up and leaps toward you, grabbing the meal without wasting time on examining it."
                                    jump highisland_crew_camp101a
                                'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                    pass
                                'I look away.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look away.')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                    'I meet {color=#f6d6bd}Dalit’s{/color} eyes.' if dalit_highisland_joined and not dalit_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I meet {color=#f6d6bd}Dalit’s{/color} eyes.')
                        if not dalit_highisland_blocked and not dalit_highisland_tired:
                            $ custom1 = "She gives you a playful smile, but says nothing. Her new ponytail reveals her small ears."
                            $ dalit_highisland_opinion = 1
                            jump highisland_crew_camp101a
                        elif dalit_highisland_blocked:
                            menu:
                                'Her new ponytail reveals her small ears. “I wish I could do something about this nasty wound...”
                                '
                                '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                    $ highisland_camp1_tuliahelp_used = 1
                                    $ dalit_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    if not dalit_highisland_tired:
                                        $ dalit_highisland_opinion = 1
                                        $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Dalit{/color} and pays you no more attention."
                                    else:
                                        $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Dalit{/color} and pays you no more attention. Soon after, her {i}patient{/i} mentions she’s a bit hungry, but seems to feel much better."
                                    jump highisland_crew_camp101a
                                'I offer her a healing potion.' if item_generichealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a healing potion.')
                                    $ item_generichealingpotion -= 1
                                    $ renpy.notify("You lost a healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                    $ dalit_highisland_blocked = 0
                                    $ dalit_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ dalit_highisland_opinion = 1
                                    $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand. “I hope it tastes better than the ones from the monastery.”"
                                    jump highisland_crew_camp101a
                                'I offer her the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her the potion from the dolmen.')
                                    $ item_potiondolmen -= 1
                                    $ renpy.notify("You lost the potion from the dolmen.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                    $ dalit_highisland_blocked = 0
                                    $ dalit_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ dalit_highisland_opinion = 1
                                    $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand. “I hope it tastes better than the ones from the monastery.”"
                                    jump highisland_crew_camp101a
                                'I offer her a small healing potion.' if item_smallhealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a small healing potion.')
                                    $ item_smallhealingpotion -= 1
                                    $ renpy.notify("You lost a small healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                    $ dalit_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    if not dalit_highisland_tired:
                                        $ dalit_highisland_opinion = 1
                                        $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand. “I hope it tastes better than the ones from the monastery.”"
                                    else:
                                        $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand. “I hope it tastes better than the ones from the monastery. Tell me if you have any leftovers to spare.”"
                                    jump highisland_crew_camp101a
                                'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                    pass
                                'I nod.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                        elif dalit_highisland_tired:
                            menu:
                                'Her new ponytail reveals her small ears. “I wish I had some water-resistant food with me... I got soaked on that boat, too!”
                                '
                                'I unroll {color=#f6d6bd}Asterion’s{/color} cloak. “You can warm yourself up with this.”' if item_asterioncloak and not highisland_camp1_asterioncloak_used:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I unroll {color=#f6d6bd}Asterion’s{/color} cloak. “You can warm yourself up with this.”')
                                    $ dalit_highisland_tired = 0
                                    $ dalit_highisland_opinion = 1
                                    $ custom1 = "Hesitant at first, she wraps herself up, and her eyes widen. “Huh. That’s some {i}nice{/i} fabric.”"
                                    jump highisland_crew_camp101a
                                'I offer her a food ration.' if item_rations:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a food ration.')
                                    $ item_rations -= 1
                                    $ renpy.notify("You lost a food ration.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                    $ dalit_highisland_tired = 0
                                    $ dalit_highisland_opinion = 1
                                    $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand, licking her lips. She devours it like a dock worker on a break."
                                    jump highisland_crew_camp101a
                                'I offer her a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast fish and some fruits.')
                                    $ item_cookedfish -= 1
                                    $ item_wildplants -= 1
                                    $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                    $ dalit_highisland_tired = 0
                                    $ dalit_highisland_opinion = 1
                                    $ custom1 = "She gestures for you to throw them to her, but after seeing your hesitation, she takes it from your hand, licking her lips. She devours it like a dock worker on a break."
                                    jump highisland_crew_camp101a
                                'I offer her a roast chicken.' if item_chicken:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast chicken.')
                                    $ item_chicken -= 1
                                    $ renpy.notify("You lost a roast chicken.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                    $ dalit_highisland_tired = 0
                                    $ dalit_highisland_opinion = 1
                                    $ custom1 = "She gestures for you to throw it to her, but after seeing your hesitation, she takes it from your hand, licking her lips. She devours it like a dock worker on a break."
                                    jump highisland_crew_camp101a
                                'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                    pass
                                'I nod.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                    '“Are you in one piece, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and not efren_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you in one piece, {color=#f6d6bd}Efren{/color}?”')
                        if not efren_highisland_blocked and not efren_highisland_tired:
                            $ custom1 = "He waves you off, constantly observing the entrance."
                            $ efren_highisland_opinion = 1
                            jump highisland_crew_camp101a
                        elif efren_highisland_blocked:
                            menu:
                                'He waves you off, constantly observing the entrance, but then lets out a hiss and reaches toward his wounded arm.
                                '
                                '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                    $ highisland_camp1_tuliahelp_used = 1
                                    $ efren_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    if not efren_highisland_tired:
                                        $ efren_highisland_opinion = 1
                                        $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Efren{/color} and pays you no more attention."
                                    else:
                                        $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Efren{/color} and pays you no more attention. Soon after, her {i}patient{/i} mentions he’s a bit hungry, but seems to feel much better."
                                    jump highisland_crew_camp101a
                                'I offer him a healing potion.' if item_generichealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a healing potion.')
                                    $ item_generichealingpotion -= 1
                                    $ renpy.notify("You lost a healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                    $ efren_highisland_blocked = 0
                                    $ efren_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ efren_highisland_opinion = 1
                                    $ custom1 = "As he still ignores you, you stand up and put the bottle next to him. After a moment of hesitation, he empties the bottle with a single gulp."
                                    jump highisland_crew_camp101a
                                'I offer him the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him the potion from the dolmen.')
                                    $ item_potiondolmen -= 1
                                    $ renpy.notify("You lost the potion from the dolmen.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                    $ efren_highisland_blocked = 0
                                    $ efren_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ efren_highisland_opinion = 1
                                    $ custom1 = "As he still ignores you, you stand up and put the bottle next to him. After a moment of hesitation, he empties the bottle with a single gulp."
                                    jump highisland_crew_camp101a
                                'I offer him a small healing potion.' if item_smallhealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a small healing potion.')
                                    $ item_smallhealingpotion -= 1
                                    $ renpy.notify("You lost a small healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                    $ efren_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    if not efren_highisland_tired:
                                        $ efren_highisland_opinion = 1
                                        $ custom1 = "As he still ignores you, you stand up and put the bottle next to him. After a moment of hesitation, he empties the bottle with a single sip."
                                    else:
                                        $ custom1 = "As he still ignores you, you stand up and put the bottle next to him. After a moment of hesitation, he empties the bottle with a single sip, but then his stomach makes a loud growl."
                                    jump highisland_crew_camp101a
                                'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                    pass
                                'I shrug.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug.')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                        elif efren_highisland_tired:
                            menu:
                                'He waves you off, constantly observing the entrance, but then his stomach makes a loud growl.
                                '
                                'I offer him a food ration.' if item_rations:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a food ration.')
                                    $ item_rations -= 1
                                    $ renpy.notify("You lost a food ration.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                    $ efren_highisland_tired = 0
                                    $ efren_highisland_opinion = 1
                                    $ custom1 = "As he still ignores you, you stand up and put the meal next to him. After a moment of hesitation, he bites into it like a wolf."
                                    jump highisland_crew_camp101a
                                'I offer him a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast fish and some fruits.')
                                    $ item_cookedfish -= 1
                                    $ item_wildplants -= 1
                                    $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                    $ efren_highisland_tired = 0
                                    $ efren_highisland_opinion = 1
                                    $ custom1 = "As he still ignores you, you stand up and put the meal next to him. After a moment of hesitation, he bites into it like a wolf."
                                    jump highisland_crew_camp101a
                                'I offer him a roast chicken.' if item_chicken:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast chicken.')
                                    $ item_chicken -= 1
                                    $ renpy.notify("You lost a roast chicken.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                    $ efren_highisland_tired = 0
                                    $ efren_highisland_opinion = 1
                                    $ custom1 = "As he still ignores you, you stand up and put the meal next to him. After a moment of hesitation, he bites into it like a wolf."
                                    jump highisland_crew_camp101a
                                'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                    pass
                                'I shrug.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug.')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                    'I glance at {color=#f6d6bd}Thyrsus{/color}.' if thyrsus_highisland_joined and not thyrsus_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at {color=#f6d6bd}Thyrsus{/color}.')
                        if not thyrsus_highisland_blocked and not thyrsus_highisland_tired:
                            $ custom1 = "After collecting his amulets, he winks at you and drinks something from a small flask. “Ready when you are.”"
                            $ thyrsus_highisland_opinion = 1
                            jump highisland_crew_camp101a
                        elif thyrsus_highisland_blocked and not thyrsus_highisland_tired:
                            $ custom1 = "After collecting his amulets, he opens a sizable flask and takes a big gulp, then puts on a disgusted grimace. He reaches for his wound and pats it a few times, then stretches out and winks at you. “Ready when you are.”"
                            $ thyrsus_highisland_blocked = 0
                            $ thyrsus_highisland_opinion = 1
                            $ highisland_crew_left += 1
                            jump highisland_crew_camp101a
                        elif thyrsus_highisland_tired:
                            if thyrsus_highisland_blocked:
                                $ custom1 = "After collecting his amulets, he opens a sizable flask and takes a big gulp, then puts on a disgusted grimace. He reaches for his wound and pats it a few times, then stretches out and winks at you. “Ready when you are, but I’d rather eat something first.”"
                                $ thyrsus_highisland_blocked = 0
                                $ highisland_crew_left += 1
                            else:
                                $ custom1 = "After collecting his amulets, he winks at you and drinks something from a small flask. “Ready when you are, but I’d rather eat something first.”"
                            menu:
                                '[custom1]
                                '
                                'I offer him a food ration.' if item_rations:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a food ration.')
                                    $ item_rations -= 1
                                    $ renpy.notify("You lost a food ration.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                    $ thyrsus_highisland_tired = 0
                                    $ thyrsus_highisland_opinion = 1
                                    $ custom1 = "He reaches for it from where he sits with a creeper, but moves it so quickly he crashes the meal against his nose. He lets out an awkward chuckle."
                                    jump highisland_crew_camp101a
                                'I offer him a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast fish and some fruits.')
                                    $ item_cookedfish -= 1
                                    $ item_wildplants -= 1
                                    $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                    $ thyrsus_highisland_tired = 0
                                    $ thyrsus_highisland_opinion = 1
                                    $ custom1 = "He reaches for them from where he sits with a creeper, but moves it so quickly he crashes the meal against his nose. He lets out an awkward chuckle."
                                    jump highisland_crew_camp101a
                                'I offer him a roast chicken.' if item_chicken:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast chicken.')
                                    $ item_chicken -= 1
                                    $ renpy.notify("You lost a roast chicken.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                    $ thyrsus_highisland_tired = 0
                                    $ thyrsus_highisland_opinion = 1
                                    $ custom1 = "He reaches for it from where he sits with a creeper, but moves it so quickly he crashes the meal against his nose. He lets out an awkward chuckle."
                                    jump highisland_crew_camp101a
                                'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                    pass
                                '“Great.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Great.”')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                    '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and not pyrrhos_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                        if not pyrrhos_highisland_blocked and not pyrrhos_highisland_tired:
                            $ custom1 = "He glances at you. “Huh? I’m alright.”"
                            $ pyrrhos_highisland_opinion = 1
                            jump highisland_crew_camp101a
                        elif pyrrhos_highisland_blocked:
                            menu:
                                'He glances at you. “Huh? My leg aches, but I’ll make it.”
                                '
                                '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                    $ highisland_camp1_tuliahelp_used = 1
                                    $ pyrrhos_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    if not pyrrhos_highisland_tired:
                                        $ pyrrhos_highisland_opinion = 1
                                        $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Pyrrhos{/color} and pays you no more attention."
                                    else:
                                        $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Pyrrhos{/color} and pays you no more attention. Soon after, her {i}patient{/i} mentions he’s a bit hungry, but seems to feel much better."
                                    jump highisland_crew_camp101a
                                'I offer him a healing potion.' if item_generichealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a healing potion.')
                                    $ item_generichealingpotion -= 1
                                    $ renpy.notify("You lost a healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                    $ pyrrhos_highisland_blocked = 0
                                    $ pyrrhos_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ pyrrhos_highisland_opinion = 1
                                    $ custom1 = "“Ye sure, roadster?” He steps closer and, after you reach out to him with the flask on your open palm, he grabs it, smiling widely."
                                    jump highisland_crew_camp101a
                                'I offer him the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him the potion from the dolmen.')
                                    $ item_potiondolmen -= 1
                                    $ renpy.notify("You lost the potion from the dolmen.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                    $ pyrrhos_highisland_blocked = 0
                                    $ pyrrhos_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ pyrrhos_highisland_opinion = 1
                                    $ custom1 = "“Ye sure, roadster?” He steps closer and, after you reach out to him with the flask on your open palm, he grabs it, smiling widely."
                                    jump highisland_crew_camp101a
                                'I offer him a small healing potion.' if item_smallhealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a small healing potion.')
                                    $ item_smallhealingpotion -= 1
                                    $ renpy.notify("You lost a small healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                    $ pyrrhos_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    if not pyrrhos_highisland_tired:
                                        $ pyrrhos_highisland_opinion = 1
                                        $ custom1 = "“Ye sure, roadster?” He steps closer and, after you reach out to him with the flask on your open palm, he grabs it, smiling widely."
                                    else:
                                        $ custom1 = "“Ye sure, roadster?” He steps closer and, after you reach out to him with the flask on your open palm, he grabs it, smiling widely. “And what now? Yer going to tell me ye’ve some oats to spare?”"
                                    jump highisland_crew_camp101a
                                'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                    pass
                                '“Very well.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well.”')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                        elif pyrrhos_highisland_tired:
                            menu:
                                'He glances at you. “Huh? I’m alright. Unless ye’ve got some oats to spare?”
                                '
                                'I offer him a food ration.' if item_rations:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a food ration.')
                                    $ item_rations -= 1
                                    $ renpy.notify("You lost a food ration.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                    $ pyrrhos_highisland_tired = 0
                                    $ pyrrhos_highisland_opinion = 1
                                    $ custom1 = "His beard shakes from his chuckle. “Cheers, roadster!”"
                                    jump highisland_crew_camp101a
                                'I offer him a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast fish and some fruits.')
                                    $ item_cookedfish -= 1
                                    $ item_wildplants -= 1
                                    $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                    $ pyrrhos_highisland_tired = 0
                                    $ pyrrhos_highisland_opinion = 1
                                    $ custom1 = "His beard shakes from his chuckle. “Cheers, roadster!”"
                                    jump highisland_crew_camp101a
                                'I offer him a roast chicken.' if item_chicken:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast chicken.')
                                    $ item_chicken -= 1
                                    $ renpy.notify("You lost a roast chicken.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                    $ pyrrhos_highisland_tired = 0
                                    $ pyrrhos_highisland_opinion = 1
                                    $ custom1 = "His beard shakes from his chuckle. “Cheers, roadster!”"
                                    jump highisland_crew_camp101a
                                'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                    pass
                                '“No. No oats.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No. No oats.”')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                    'I observe {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and not bandit_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe {color=#f6d6bd}the bandit{/color}.')
                        if not bandit_highisland_blocked and not bandit_highisland_tired:
                            $ custom1 = "When he raises his head, he looks like a thoughtful statue, but spares not a single glance to anyone around him."
                            $ bandit_highisland_opinion = 1
                            jump highisland_crew_camp101a
                        elif bandit_highisland_blocked:
                            menu:
                                'When he raises his head, he looks like a thoughtful statue, but spares not a single glance to anyone around him - despite the trail of blood reaching from his forehead to his chin. After you point it out, he lets out a sigh. “Right, they got me well, they did. Say, you have any snake bait? I need to sharpen my senses.”
                                '
                                '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                    $ highisland_camp1_tuliahelp_used = 1
                                    $ bandit_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    if not bandit_highisland_tired:
                                        $ bandit_highisland_opinion = 1
                                        $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}the bandit{/color} and pays you no more attention."
                                    else:
                                        $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}the bandit{/color} and pays you no more attention. Soon after, her {i}patient{/i} mentions he’s a bit hungry, but seems to feel much better."
                                    jump highisland_crew_camp101a
                                'I offer him a healing potion.' if item_generichealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a healing potion.')
                                    $ item_generichealingpotion -= 1
                                    $ renpy.notify("You lost a healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                    $ bandit_highisland_blocked = 0
                                    $ bandit_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ bandit_highisland_opinion = 1
                                    $ custom1 = "He frowns as if you’ve just interrupted him, but obediently gets up and takes the flask from you."
                                    jump highisland_crew_camp101a
                                'I offer him the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him the potion from the dolmen.')
                                    $ item_potiondolmen -= 1
                                    $ renpy.notify("You lost the potion from the dolmen.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                    $ bandit_highisland_blocked = 0
                                    $ bandit_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ bandit_highisland_opinion = 1
                                    $ custom1 = "He frowns as if you’ve just interrupted him, but obediently gets up and takes the flask from you."
                                    jump highisland_crew_camp101a
                                'I offer him a small healing potion.' if item_smallhealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a small healing potion.')
                                    $ item_smallhealingpotion -= 1
                                    $ renpy.notify("You lost a small healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                    $ bandit_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    if not bandit_highisland_tired:
                                        $ bandit_highisland_opinion = 1
                                        $ custom1 = "He frowns as if you’ve just interrupted him, but obediently gets up and takes the flask from you."
                                    else:
                                        $ custom1 = "He frowns as if you’ve just interrupted him, but obediently gets up and takes the flask from you. “Fine... But I still feel a bit weak.”"
                                    jump highisland_crew_camp101a
                                'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                    pass
                                '“Here. Some snake bait.”' if item_snakebait:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here. Some snake bait.”')
                                    $ item_snakebait -= 1
                                    $ renpy.notify("You lost the snake bait.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the snake bait.{/i}')
                                    $ bandit_highisland_blocked = 0
                                    $ bandit_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ bandit_highisland_opinion = 1
                                    $ custom1 = "He grins widely. “I’ll put it to good use.”"
                                    jump highisland_crew_camp101a
                                '“Better. Want the proper sharpening poison?”' if item_sharpeningpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Better. Want the proper sharpening poison?”')
                                    $ item_sharpeningpotion -= 1
                                    $ renpy.notify("You lost a dose of sharpening poison.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a dose of sharpening poison.{/i}')
                                    $ bandit_highisland_blocked = 0
                                    $ bandit_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ bandit_highisland_opinion = 1
                                    $ custom1 = "He grins widely. “I’ll put it to good use.”"
                                    jump highisland_crew_camp101a
                                'I can’t help him with that.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t help him with that.')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                        elif bandit_highisland_tired:
                            menu:
                                'When he raises his head, he looks like a thoughtful statue, but spares not a single glance to anyone around him. After you point out that his eyes look exhausted, he lets out a sigh. “Right. I guess I could eat.”
                                '
                                'I offer him a food ration.' if item_rations:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a food ration.')
                                    $ item_rations -= 1
                                    $ renpy.notify("You lost a food ration.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                    $ bandit_highisland_tired = 0
                                    $ bandit_highisland_opinion = 1
                                    $ custom1 = "Unconvinced at first, he finally gets up and takes the meal from you. “Thanks, I guess.”"
                                    jump highisland_crew_camp101a
                                'I offer him a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast fish and some fruits.')
                                    $ item_cookedfish -= 1
                                    $ item_wildplants -= 1
                                    $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                    $ bandit_highisland_tired = 0
                                    $ bandit_highisland_opinion = 1
                                    $ custom1 = "Unconvinced at first, he finally gets up and takes the meal from you. “Thanks, I guess.”"
                                    jump highisland_crew_camp101a
                                'I offer him a roast chicken.' if item_chicken:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast chicken.')
                                    $ item_chicken -= 1
                                    $ renpy.notify("You lost a roast chicken.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                    $ bandit_highisland_tired = 0
                                    $ bandit_highisland_opinion = 1
                                    $ custom1 = "Unconvinced at first, he finally gets up and takes the meal from you. “Thanks, I guess.”"
                                    jump highisland_crew_camp101a
                                'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                    pass
                                'I can’t help him with that.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t help him with that.')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                    '“How are you doing, {color=#f6d6bd}Tulia{/color}?”' if tulia_highisland_joined and not tulia_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How are you doing, {color=#f6d6bd}Tulia{/color}?”')
                        if not tulia_highisland_blocked and not tulia_highisland_tired:
                            if highisland_camp1_tuliahelp_used:
                                $ custom1 = "She steps away from her patient and throws away a scrap of dirty fabric. “Better than some, that’s for sure.”"
                            else:
                                $ custom1 = "You feel the warmth of her shoulder. “Pretty well. If anyone here needs someone to look at their wounds, just let me know. I’ve got enough balms and bandages for one person.”"
                            $ tulia_highisland_opinion = 1
                            jump highisland_crew_camp101a
                        elif tulia_highisland_blocked and not tulia_highisland_tired:
                            $ custom1 = "You feel the warmth of her shoulder. She cleans the wound on her neck, soaking the bandages with a remedy that smells like swamp herbs. “Pretty well.”"
                            $ highisland_camp1_tuliahelp_used = 1
                            $ tulia_highisland_blocked = 0
                            $ tulia_highisland_opinion = 1
                            $ highisland_crew_left += 1
                            jump highisland_crew_camp101a
                        elif tulia_highisland_tired:
                            if tulia_highisland_blocked:
                                $ highisland_camp1_tuliahelp_used = 1
                                $ custom1 = "You feel the warmth of her shoulder. She cleans the wound on her neck, soaking the bandages with a remedy that smells like swamp herbs. “Pretty well. Just a bit hungry.”"
                                $ tulia_highisland_blocked = 0
                                $ highisland_crew_left += 1
                            else:
                                $ custom1 = "You feel the warmth of her shoulder. “Pretty well. Just a bit hungry.”"
                            menu:
                                '[custom1]
                                '
                                'I offer her a food ration.' if item_rations:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a food ration.')
                                    $ item_rations -= 1
                                    $ renpy.notify("You lost a food ration.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                    $ tulia_highisland_tired = 0
                                    $ tulia_highisland_opinion = 1
                                    if not highisland_camp1_tuliahelp_used:
                                        $ highisland_camp1_tuliahelp_available = 1
                                        $ custom1 = "“Thank you. Now, if anyone here needs someone to look at their wounds, just let me know. I’ve got enough balms and bandages for one person.”"
                                    else:
                                        $ custom1 = "“Thank you. I just need to rest now.”"
                                    jump highisland_crew_camp101a
                                'I offer her a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast fish and some fruits.')
                                    $ item_cookedfish -= 1
                                    $ item_wildplants -= 1
                                    $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                    $ tulia_highisland_tired = 0
                                    $ tulia_highisland_opinion = 1
                                    if not highisland_camp1_tuliahelp_used:
                                        $ highisland_camp1_tuliahelp_available = 1
                                        $ custom1 = "“Thank you. Now, if anyone here needs someone to look at their wounds, just let me know. I’ve got enough balms and bandages for one person.”"
                                    else:
                                        $ custom1 = "“Thank you. I just need to rest now.”"
                                    jump highisland_crew_camp101a
                                'I offer her a roast chicken.' if item_chicken:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer her a roast chicken.')
                                    $ item_chicken -= 1
                                    $ renpy.notify("You lost a roast chicken.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                    $ tulia_highisland_tired = 0
                                    $ tulia_highisland_opinion = 1
                                    if not highisland_camp1_tuliahelp_used:
                                        $ highisland_camp1_tuliahelp_available = 1
                                        $ custom1 = "“Thank you. Now, if anyone here needs someone to look at their wounds, just let me know. I’ve got enough balms and bandages for one person.”"
                                    else:
                                        $ custom1 = "“Thank you. I just need to rest now.”"
                                    jump highisland_crew_camp101a
                                'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                    pass
                                '“I’m glad you’re alright.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m glad you’re alright.”')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                    '“Are you hanging there, {color=#f6d6bd}Tzvi{/color}?”' if tzvi_highisland_joined and not tzvi_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you hanging there, {color=#f6d6bd}Tzvi{/color}?”')
                        if not tzvi_highisland_blocked:
                            $ tzvi_highisland_tired = 0
                            $ custom1 = "“Very green, this forest,” he sounds as if he’s talking to himself, but then brings you a few wild fruits. “Here. I found more than I can eat.”"
                            $ tzvi_highisland_opinion = 1
                            $ item_wildplants += 1
                            $ renpy.notify("You got a bunch of wild plants.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You got a bunch of wild plants.{/i}')
                            jump highisland_crew_camp101a
                        elif tzvi_highisland_blocked:
                            if tzvi_highisland_tired:
                                $ tzvi_highisland_tired = 0
                                $ custom1 = "He shrugs, chewing on some leaves he found growing around. “I could use something for my wound.”"
                            else:
                                $ custom1 = "“Very green, this forest,” he sounds as if he’s talking to himself, but then brings you a few wild fruits. “Here. I found more than I can eat. But I could use something for my wound.”"
                                $ item_wildplants += 1
                                $ renpy.notify("You got a bunch of wild plants.")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You got a bunch of wild plants.{/i}')
                            menu:
                                '[custom1]
                                '
                                '“{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”' if highisland_camp1_tuliahelp_available and not highisland_camp1_tuliahelp_used:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, can you lend a hand here?”')
                                    $ highisland_camp1_tuliahelp_used = 1
                                    $ tzvi_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    $ tzvi_highisland_opinion = 1
                                    $ custom1 = "She grabs a few bandages from her travel kit. “Show me where it hurts,” she instructs {color=#f6d6bd}Tzvi{/color} and pays you no more attention."
                                    jump highisland_crew_camp101a
                                'I offer him a healing potion.' if item_generichealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a healing potion.')
                                    $ item_generichealingpotion -= 1
                                    $ renpy.notify("You lost a healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                                    $ tzvi_highisland_blocked = 0
                                    $ tzvi_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ tzvi_highisland_opinion = 1
                                    $ custom1 = "With a nod, he grabs the flask and carries it away."
                                    jump highisland_crew_camp101a
                                'I offer him the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him the potion from the dolmen.')
                                    $ item_potiondolmen -= 1
                                    $ renpy.notify("You lost the potion from the dolmen.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                                    $ tzvi_highisland_blocked = 0
                                    $ tzvi_highisland_tired = 0
                                    $ highisland_crew_left += 1
                                    $ tzvi_highisland_opinion = 1
                                    $ custom1 = "With a nod, he grabs the flask and carries it away."
                                    jump highisland_crew_camp101a
                                'I offer him a small healing potion.' if item_smallhealingpotion:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a small healing potion.')
                                    $ item_smallhealingpotion -= 1
                                    $ renpy.notify("You lost a small healing potion.")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                                    $ tzvi_highisland_blocked = 0
                                    $ highisland_crew_left += 1
                                    $ tzvi_highisland_opinion = 1
                                    $ custom1 = "With a nod, he grabs the flask and carries it away."
                                    jump highisland_crew_camp101a
                                'I’ve got no potions to spare. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                                    pass
                                '“I’ll see what I can do.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll see what I can do.”')
                                    $ custom1 = "The jungle may be loud, but isn’t all that different from what you’ve seen on the peninsula."
                                    jump highisland_crew_camp101a
                    '“{color=#f6d6bd}Quintus{/color}, still alive?”' if quintus_highisland_joined and not quintus_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Quintus{/color}, still alive?”')
                        if not quintus_highisland_blocked and not quintus_highisland_tired:
                            if item_crossbow:
                                $ custom1 = "“Duh,” he mutters while looking into his bag, then smiles at you. “It’s easier than I thought! And good thing I brought no crossbow to slow me down, I can’t see shit. Want to take the quarrels that I forgot to unpack?”"
                                $ item_crossbowquarrels += 2
                                $ renpy.notify("You received 2 quarrels.\nYou’ve got %s quarrels left." %item_crossbowquarrels)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost two quarrels. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            else:
                                $ custom1 = "“Duh,” he mutters while looking into his bag, then smiles at you. “It’s easier than I thought! And good thing I brought no crossbow, I can’t see shit. It would only slow me down.”"
                            $ quintus_highisland_opinion = 1
                            jump highisland_crew_camp101a
                        elif quintus_highisland_blocked:
                            $ quintus_highisland_blocked = 0
                            $ quintus_highisland_tired = 0
                            $ highisland_crew_left += 1
                            $ quintus_highisland_opinion = 1
                            if item_crossbow:
                                $ custom1 = "“Duh,” he mutters while holding the now-empty bottle of a healing potion that he brought with him. “They {i}almost{/i} got me, but I’m fine. And good thing I brought no crossbow to slow me down, I can’t see shit. Want to take the quarrels that I forgot to unpack?”"
                                $ item_crossbowquarrels += 2
                                $ renpy.notify("You received 2 quarrels.\nYou’ve got %s quarrels left." %item_crossbowquarrels)
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost two quarrels. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            else:
                                $ custom1 = "“Duh,” he mutters while holding the now-empty bottle of a healing potion that he brought with him. “They {i}almost{/i} got me, but I’m fine. And good thing I brought no crossbow, I can’t see shit. It would only slow me down.”"
                            jump highisland_crew_camp101a
                        elif quintus_highisland_tired:
                            menu:
                                '“Duh,” he mutters while looking into his bag. “It’s easier than I thought! And good thing I brought no crossbow to slow me down, I can’t see shit.” He then looks at you and adjusts his bandage. “Got anything to eat, [pcname]?”
                                '
                                'I offer him a food ration.' if item_rations:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a food ration.')
                                    $ item_rations -= 1
                                    $ quintus_highisland_tired = 0
                                    $ quintus_highisland_opinion = 1
                                    if item_crossbow:
                                        $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready. Want to take the quarrels that I forgot to unpack?”"
                                        $ item_crossbowquarrels += 2
                                        $ renpy.notify("You lost a food ration.\nYou received 2 quarrels.\nYou’ve got %s quarrels left." %item_crossbowquarrels)
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration. You lost two quarrels. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                                    else:
                                        $ renpy.notify("You lost a food ration.")
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                                        $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready.”"
                                    jump highisland_crew_camp101a
                                'I offer him a roast fish and some fruits.' if item_cookedfish and item_wildplants:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast fish and some fruits.')
                                    $ item_cookedfish -= 1
                                    $ item_wildplants -= 1
                                    $ quintus_highisland_tired = 0
                                    $ quintus_highisland_opinion = 1
                                    if item_crossbow:
                                        $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready. Want to take the quarrels that I forgot to unpack?”"
                                        $ item_crossbowquarrels += 2
                                        $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.\nYou received 2 quarrels.\nYou’ve got %s quarrels left." %item_crossbowquarrels)
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants. You lost two quarrels. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                                    else:
                                        $ renpy.notify("You lost a roast fish\nand a bunch of wild plants.")
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish and a bunch of wild plants.{/i}')
                                        $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready.”"
                                    jump highisland_crew_camp101a
                                'I offer him a roast chicken.' if item_chicken:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer him a roast chicken.')
                                    $ item_chicken -= 1
                                    $ quintus_highisland_tired = 0
                                    $ quintus_highisland_opinion = 1
                                    if item_crossbow:
                                        $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready. Want to take the quarrels that I forgot to unpack?”"
                                        $ item_crossbowquarrels += 2
                                        $ renpy.notify("You lost a roast chicken.\nYou received 2 quarrels.\nYou’ve got %s quarrels left." %item_crossbowquarrels)
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken. You lost two quarrels. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                                    else:
                                        $ renpy.notify("You lost a roast chicken.")
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                                        $ custom1 = "“Nice,” he gets up to take it from you. “Let me finish it and I’ll be done and ready.”"
                                    jump highisland_crew_camp101a
                                'I’ve got no food to spare. (disabled)' if (not item_rations and not item_chicken and not item_cookedfish) or (not item_rations and not item_chicken and not item_wildplants):
                                    pass
                                '“I don’t think so...”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t think so...”')
                                    $ custom1 = "He lets out a disappointed sigh."
                                    jump highisland_crew_camp101a
                    'I let my back and limbs rest for a bit, then prepare my tools to cut through the bushes. “Time to carry on.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let my back and limbs rest for a bit, then prepare my tools to cut through the bushes. “Time to carry on.”')
                        $ highisland_destination = "denseplants"
                        jump highisland_destination

label highisland_denseplantsALL:
    label highisland_solo_denseplantsALL:
        label highisland_solo_denseplants01:
            if item_axe03:
                $ highisland_denseplants_axe_amount += 1
            if item_axe02:
                $ highisland_denseplants_axe_amount += 1
            if item_axe02alt:
                $ highisland_denseplants_axe_amount += 1
            if highisland_lightsource:
                $ custom1 = "You climb to the top of the wall and get a look ahead. The trail must have overgrown only recently, but the thorny bushes won’t be crossed easily. Reaching the beaten track that leads to the proper woods will take some effort."
            else:
                $ highisland_denseplants_points += 1
                $ custom1 = "You climb to the top of the wall and get a look ahead. The trail must have overgrown only recently, but the thorny bushes won’t be crossed easily. Reaching the beaten track that leads to the proper woods will take some effort, and since you’ve got no reliable source of light, spotting all the obstacles will take even more of your time."
            jump highisland_solo_denseplants01a

        label highisland_solo_denseplants01a:
            if highisland_denseplants_points <= 0:
                show areapicture hi_denseplants at basicfade
                menu:
                    '[custom1]
                    \n\nOnce you reach the next section of the old road, you take off your thick gloves.
                    '
                    'I make sure there are no thorns stuck in my pants.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make sure there are no thorns stuck in my pants.')
                        $ highisland_destination = "trolltunnel"
                        jump highisland_destination
            else:
                menu:
                    '[custom1]
                    '
                    'I don’t need the withering dust anymore. I use it all.' if item_witheringdust and highisland_denseplants_points >= 2 and not highisland_denseplants_witheringdust:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need the withering dust anymore. I use it all.')
                        $ highisland_denseplants_witheringdust = 1
                        $ highisland_denseplants_points -= 3
                        $ item_witheringdust -= 1
                        $ renpy.notify("You used up the withering dust.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You used up the withering dust.{/i}')
                        $ custom1 = "After covering your skin and drawing a mugful of stream water, you spread the poison on the ground, step by step, and form a passage of twisted, burnt stems, still hissing as you move them to the side with your boot."
                        jump highisland_solo_denseplants01a
                    'I use a large part of the withering dust, but save some of it for later.' if item_witheringdust and not highisland_denseplants_witheringdust:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use a large part of the withering dust, but save some of it for later.')
                        $ highisland_denseplants_witheringdust = 1
                        $ highisland_denseplants_points -= 1
                        $ custom1 = "After covering your skin and drawing a mugful of stream water, you spread the poison on the ground, step by step, and form a passage of twisted, burnt stems, still hissing as you move them to the side with your boot."
                        jump highisland_solo_denseplants01a
                    'I’ve a backup axe... It’s not a problem if it gets a bit blunt.' if highisland_denseplants_axe_amount >= 2 and not highisland_denseplants_axe:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve a backup axe... It’s not a problem if it gets a bit blunt.')
                        $ highisland_denseplants_axe = 1
                        $ highisland_denseplants_points -= 1
                        $ custom1 = "You take a few swings to see how it goes. While the stems are resilient, you only have to cut through the more obtrusive chunks."
                        jump highisland_solo_denseplants01a
                    'The golem glove will make it a bit easier.' if item_golemglove and not highisland_denseplants_golemglove:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- The golem glove will make it a bit easier.')
                        $ highisland_denseplants_golemglove = 1
                        $ highisland_denseplants_points -= 1
                        $ custom1 = "While you have to look out for the thorns, your fierce grasp helps you break and pull any stem that opposes the cuts of your blade."
                        jump highisland_solo_denseplants01a
                    'I’ve no more tools to help me.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve no more tools to help me.')
                        jump highisland_solo_denseplants02

        label highisland_solo_denseplants02:
            show areapicture hi_denseplants at basicfade
            if highisland_denseplants_points <= 1:
                $ custom1 = "The work is tiring, and would go faster if it wasn’t for the harpy circling above you. Once you reach the other side, your stomach growls from hunger."
                if pc_food:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    $ custom1 = "The work is grueling, but not as much as trying to scare away the harpy that circles above you. Finally, once it realizes you are swaying on your feet, it plunges its talons into your eyes."
                    jump highisland_gameover
                menu:
                    '[custom1]
                    \n\nOnce you reach the next section of the old road, you take off your thick gloves.
                    '
                    'I make sure there are no thorns stuck in my pants.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make sure there are no thorns stuck in my pants.')
                        $ highisland_destination = "trolltunnel"
                        jump highisland_destination
            else:
                $ custom1 = "The work is exhausting, and would go faster if it wasn’t for the harpy circling above you. Once you reach the other side, your stomach growls from hunger."
                if pc_food:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    $ custom1 = "The work is grueling, but not as much as trying to scare away the harpy that circles above you. Finally, once it realizes you are swaying on your feet, it plunges its talons into your eyes."
                    jump highisland_gameover
                menu:
                    '[custom1]
                    \n\nOnce you reach the next section of the old road, you take off your thick gloves.
                    '
                    'I make sure there are no thorns stuck in my pants.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make sure there are no thorns stuck in my pants.')
                        $ highisland_destination = "trolltunnel"
                        jump highisland_destination

    label highisland_howlers_denseplantsALL:
        label highisland_howlers_denseplants01:
            $ highisland_denseplants_points -= 2
            if item_axe03:
                $ highisland_denseplants_axe_amount += 1
            if item_axe02:
                $ highisland_denseplants_axe_amount += 1
            if item_axe02alt:
                $ highisland_denseplants_axe_amount += 1
            if highisland_lightsource:
                $ custom1 = "You climb to the top of the wall and get a look ahead. The trail must have overgrown only recently, but the thorny bushes won’t be crossed easily. Reaching the beaten track that leads to the proper woods will take some effort.\n\n{color=#f6d6bd}The leader{/color} doesn’t wait. He unwraps a steel sickle sword he hasn’t used before and gets to chopping - the swings of his blade are much better at cutting the bush stems than a heavy axe."
            else:
                $ highisland_denseplants_points += 1
                $ custom1 = "You climb to the top of the wall and get a look ahead. The trail must have overgrown only recently, but the thorny bushes won’t be crossed easily. Reaching the beaten track that leads to the proper woods will take some effort, and since you’ve got no reliable source of light, spotting all the obstacles will take even more of your time.\n\n{color=#f6d6bd}The leader{/color} doesn’t wait. He unwraps a steel sickle sword he hasn’t used before and gets to chopping - the swings of his blade are much better at cutting the bush stems than a heavy axe."
            jump highisland_howlers_denseplants01a

        label highisland_howlers_denseplants01a:
            if highisland_denseplants_points <= 0:
                show areapicture hi_denseplants at basicfade
                menu:
                    '[custom1]
                    \n\nOnce you reach the next section of the old road, you take off your thick gloves. {color=#f6d6bd}The guards{/color} examine their pants, pulling out any stuck thorns.
                    '
                    'I do the same.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do the same.')
                        $ highisland_destination = "trolltunnel"
                        jump highisland_destination
            else:
                menu:
                    '[custom1]
                    '
                    'I don’t need the withering dust anymore. I use it all.' if item_witheringdust and highisland_denseplants_points >= 2 and not highisland_denseplants_witheringdust:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need the withering dust anymore. I use it all.')
                        $ highisland_denseplants_witheringdust = 1
                        $ highisland_denseplants_points -= 3
                        $ item_witheringdust -= 1
                        $ renpy.notify("You used up the withering dust.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You used up the withering dust.{/i}')
                        $ custom1 = "After covering your skin and drawing a mugful of stream water, you spread the poison on the ground, step by step, and form a passage of twisted, burnt stems, still hissing as you move them to the side with your boot."
                        jump highisland_howlers_denseplants01a
                    'I use a large part of the withering dust, but save some of it for later.' if item_witheringdust and not highisland_denseplants_witheringdust:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use a large part of the withering dust, but save some of it for later.')
                        $ highisland_denseplants_witheringdust = 1
                        $ highisland_denseplants_points -= 1
                        $ custom1 = "After covering your skin and drawing a mugful of stream water, you spread the poison on the ground, step by step, and form a passage of twisted, burnt stems, still hissing as you move them to the side with your boot."
                        jump highisland_howlers_denseplants01a
                    'I’ve a backup axe... It’s not a problem if it gets a bit blunt.' if highisland_denseplants_axe_amount >= 2 and not highisland_denseplants_axe:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve a backup axe... It’s not a problem if it gets a bit blunt.')
                        $ highisland_denseplants_axe = 1
                        $ highisland_denseplants_points -= 1
                        $ custom1 = "You take a few swings to see how it goes. While the stems are resilient, you only have to cut through the more obtrusive chunks."
                        jump highisland_howlers_denseplants01a
                    'The golem glove will make it a bit easier.' if item_golemglove and not highisland_denseplants_golemglove:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- The golem glove will make it a bit easier.')
                        $ highisland_denseplants_golemglove = 1
                        $ highisland_denseplants_points -= 1
                        $ custom1 = "While you have to look out for the thorns, your fierce grasp helps you break and pull any stem that opposes the cuts of your blade."
                        jump highisland_howlers_denseplants01a
                    'I’ve no more tools to help me.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve no more tools to help me.')
                        jump highisland_howlers_denseplants02

        label highisland_howlers_denseplants02:
            show areapicture hi_denseplants at basicfade
            if highisland_denseplants_points <= 1:
                if pc_food:
                    $ custom1 = "The work is tiring, and would go faster if it wasn’t for the harpies circling above you. Eventually, they leave after getting discouraged by your numbers. Once you reach the other side, your stomach growls from hunger."
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                else:
                    $ highisland_howlersguards_hp -= 2
                    $ custom1 = "The work is tiring, and would go faster if it wasn’t for the harpies circling above you. Eventually, they leave after getting discouraged by your numbers. Seeing how you sway on your feet, your “crew” tells you to rest, cutting through the further bushes on their own, but not before they send you a few angry looks. {color=#f6d6bd}The one with the mace{/color} spits into the shrubs."
                menu:
                    '[custom1]
                    \n\nOnce you reach the next section of the old road, you take off your thick gloves. {color=#f6d6bd}The guards{/color} examine their pants, pulling out any stuck thorns.
                    '
                    'I do the same.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do the same.')
                        $ highisland_destination = "trolltunnel"
                        jump highisland_destination
            else:
                if pc_food:
                    $ custom1 = "The work is tiring, and would go faster if it wasn’t for the harpies circling above you. Eventually, they leave after getting discouraged by your numbers. Once you reach the other side, your stomach growls from hunger."
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ highisland_howlersguards_hp -= 1
                    $ custom1 = "The work is tiring, and would go faster if it wasn’t for the few harpies circling above you. Eventually, they leave after getting discouraged by your numbers. Once you reach the other side, your stomach growls from hunger."
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    $ highisland_howlersguards_hp -= 3
                    $ custom1 = "The work is tiring, and would go faster if it wasn’t for the few harpies circling above you. Eventually, they leave after getting discouraged by your numbers. Seeing how you sway on your feet, your “crew” tells you to rest, cutting through the further bushes on their own, but not before they send you a few angry looks. {color=#f6d6bd}The one with the mace{/color} spits into the shrubs."
                menu:
                    '[custom1]
                    \n\nOnce you reach the next section of the old road, you take off your thick gloves. {color=#f6d6bd}The guards{/color} examine their pants, pulling out any stuck thorns.
                    '
                    'I do the same.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do the same.')
                        $ highisland_destination = "trolltunnel"
                        jump highisland_destination

    label highisland_crew_denseplantsALL:
        label highisland_crew_denseplants01:
            if item_axe03:
                $ highisland_denseplants_axe_amount += 1
            if item_axe02:
                $ highisland_denseplants_axe_amount += 1
            if item_axe02alt:
                $ highisland_denseplants_axe_amount += 1
            if highisland_lightsource:
                $ custom1 = "You climb to the top of the wall and get a look ahead. The trail must have overgrown only recently, but the thorny bushes won’t be crossed easily. Reaching the beaten track that leads to the proper woods will take some effort."
            else:
                $ highisland_denseplants_points += 1
                $ custom1 = "You climb to the top of the wall and get a look ahead. The trail must have overgrown only recently, but the thorny bushes won’t be crossed easily. Reaching the beaten track that leads to the proper woods will take some effort, and since you’ve got no reliable source of light, spotting all the obstacles will take even more of your time."
            jump highisland_crew_denseplants01a

        label highisland_crew_denseplants01a:
            if highisland_denseplants_points <= 0:
                show areapicture hi_denseplants at basicfade
                menu:
                    '[custom1]
                    \n\nOnce you reach the next section of the old road, you take off your thick gloves.
                    '
                    '“Make sure there are no thorns stuck in your pants!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Make sure there are no thorns stuck in your pants!”')
                        $ highisland_destination = "trolltunnel"
                        jump highisland_destination
            else:
                menu:
                    '[custom1]
                    '
                    'I don’t need the withering dust anymore. I use it all.' if item_witheringdust and highisland_denseplants_points >= 2 and not highisland_denseplants_witheringdust:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need the withering dust anymore. I use it all.')
                        $ highisland_denseplants_witheringdust = 1
                        $ highisland_denseplants_points -= 3
                        $ item_witheringdust -= 1
                        $ renpy.notify("You used up the withering dust.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You used up the withering dust.{/i}')
                        $ custom1 = "After covering your skin and drawing a mugful of stream water, you spread the poison on the ground, step by step, and form a passage of twisted, burnt stems, still hissing as you move them to the side with your boot."
                        jump highisland_crew_denseplants01a
                    '“Let’s divide the labor between all of us. That way, we’ll let our arms rest.”' if not highisland_denseplants_crew and highisland_crew_left >= 3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s divide the labor between all of us. That way, we’ll let our arms rest.”')
                        $ highisland_denseplants_crew = 1
                        $ highisland_denseplants_points -= 1
                        $ custom1 = "While not every soul in your crew is of great strength, you make slow progress."
                        jump highisland_crew_denseplants01a
                    '“Thoughts, {color=#f6d6bd}Aegidia{/color}?”' if aegidia_highisland_joined and not aegidia_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thoughts, {color=#f6d6bd}Aegidia{/color}?”')
                        $ aegidia_highisland_opinion = 1
                        $ custom1 = "“See those harpies?” She points above you with her bow. “Let’s wait nae longer.”"
                        jump highisland_crew_denseplants01a
                    '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and not dalit_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                        $ dalit_highisland_opinion = 1
                        $ custom1 = "“Buy a sickle sword, I guess,” she lets out a weak giggle."
                        jump highisland_crew_denseplants01a
                    '“Any tips, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and not efren_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips, {color=#f6d6bd}Efren{/color}?”')
                        $ efren_highisland_opinion = 1
                        $ custom1 = "He reaches for a prickle. “Well, I assume we can’t go back.”"
                        jump highisland_crew_denseplants01a
                    '“{color=#f6d6bd}Thyrsus{/color}, suggestions?”' if thyrsus_highisland_joined and not thyrsus_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, suggestions?”')
                        $ thyrsus_highisland_opinion = 1
                        if not thyrsus_highisland_blocked:
                            $ highisland_denseplants_points -= 2
                            $ custom1 = "“I’ll give it a try!” He puts on a confident smile and reaches forward with his creepers. At first, you think he’s going to tear through the plants, but he then starts to mutter, and the bushes bend to the sides, forming a humble tunnel for you."
                        else:
                            $ custom1 = "He sighs. “After all this traveling, I’m of weak pneuma. I canna bend these bushes away, an’ I don’t want to tear my plants.” As if to demonstrate his words, he uses one of the creepers to scratch the top of his foot."
                        jump highisland_crew_denseplants01a
                    '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and not pyrrhos_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                        $ pyrrhos_highisland_opinion = 1
                        $ custom1 = "He shows you his open palms. “That’s all I’ve got.”"
                        jump highisland_crew_denseplants01a
                    'I look at {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and not bandit_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}the bandit{/color}.')
                        $ bandit_highisland_opinion = 1
                        $ custom1 = "He looks away. “I see no other path, alright.”"
                        jump highisland_crew_denseplants01a
                    '“{color=#f6d6bd}Tulia{/color}, what do you recommend?”' if tulia_highisland_joined and not tulia_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, what do you recommend?”')
                        $ tulia_highisland_opinion = 1
                        if not tulia_highisland_blocked:
                            $ highisland_denseplants_points -= 1
                            $ custom1 = "She rubs the top of her head and lets out a sigh. “I’ve some strength left. I’ll cut for a bit.” You step away and lend her an axe."
                        else:
                            $ custom1 = "She rubs the top of her head. “I’m too tired to play garden weeding now.”"
                        jump highisland_crew_denseplants01a
                    '“Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”' if tzvi_highisland_joined and not tzvi_highisland_blocked and not tzvi_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”')
                        $ tzvi_highisland_opinion = 1
                        $ custom1 = "“I can’t fly,” he mutters."
                        jump highisland_crew_denseplants01a
                    '“{color=#f6d6bd}Quintus{/color}, any ideas?”' if quintus_highisland_joined and not quintus_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Quintus{/color}, any ideas?”')
                        $ quintus_highisland_opinion = 1
                        if not quintus_highisland_blocked:
                            $ highisland_denseplants_points -= 1
                            $ custom1 = "“Ideas, here? Better roll up ya sleeves!” His voice may be loud, but after he notices all the thorns, he keeps his sleeves dropped and uses his own hatchet to get through a few shrubs."
                        else:
                            $ custom1 = "He yawns. “I’ll cut for a bit, but no promises.”"
                        jump highisland_crew_denseplants01a
                    'I use a large part of the withering dust, but save some of it for later.' if item_witheringdust and not highisland_denseplants_witheringdust:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use a large part of the withering dust, but save some of it for later.')
                        $ highisland_denseplants_witheringdust = 1
                        $ highisland_denseplants_points -= 1
                        $ custom1 = "After covering your skin and drawing a mugful of stream water, you spread the poison on the ground, step by step, and form a passage of twisted, burnt stems, still hissing as you move them to the side with your boot."
                        jump highisland_crew_denseplants01a
                    'I’ve a backup axe... It’s not a problem if it gets a bit blunt.' if highisland_denseplants_axe_amount >= 2 and not highisland_denseplants_axe:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve a backup axe... It’s not a problem if it gets a bit blunt.')
                        $ highisland_denseplants_axe = 1
                        $ highisland_denseplants_points -= 1
                        $ custom1 = "You take a few swings to see how it goes. While the stems are resilient, you only have to cut through the more obtrusive chunks."
                        jump highisland_crew_denseplants01a
                    'The golem glove will make it a bit easier.' if item_golemglove and not highisland_denseplants_golemglove:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- The golem glove will make it a bit easier.')
                        $ highisland_denseplants_golemglove = 1
                        $ highisland_denseplants_points -= 1
                        $ custom1 = "While you have to look out for the thorns, your fierce grasp helps you break and pull any stem that opposes the cuts of your blade."
                        jump highisland_crew_denseplants01a
                    'I’ve no more tools to help me.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve no more tools to help me.')
                        jump highisland_crew_denseplants02

        label highisland_crew_denseplants02:
            show areapicture hi_denseplants at basicfade
            if highisland_denseplants_points <= 1:
                label highisland_companionexhaustion_loop_denseplants:
                    if highisland_crew_left <= 0:
                        $ custom1 = "Once you reach the next section of the trail, your stomach growls from hunger."
                        if pc_food:
                            $ pc_food = limit_pc_food(pc_food-2)
                            show minus2food at foodchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                        elif pc_hp > 0:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        else:
                            $ custom1 = "The work is grueling, but not as much as scaring away the harpies that are circling above you. Once they realize you are swaying on your feet, they dive at you, plunging their talons into your eyes."
                            jump highisland_gameover
                    else:
                        $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus', 'pc'])
                        if highisland_crew_dmg_target == "aegidia":
                            if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                jump highisland_companionexhaustion_loop_denseplants
                            else:
                                if not aegidia_highisland_tired:
                                    $ aegidia_highisland_tired = 1
                                    $ custom1 = "Once you reach the next section of the trail, {color=#f6d6bd}Aegidia{/color} gestures for you to slow down and give her time to catch her breath."
                                else:
                                    $ aegidia_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom1 = "{color=#f6d6bd}Aegidia{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "dalit":
                            if not dalit_highisland_joined or dalit_highisland_blocked:
                                jump highisland_companionexhaustion_loop_denseplants
                            else:
                                if not dalit_highisland_tired:
                                    $ dalit_highisland_tired = 1
                                    $ custom1 = "Once you reach the next section of the trail, {color=#f6d6bd}Dalit{/color} gestures for you to slow down and give her time to catch her breath."
                                else:
                                    $ dalit_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom1 = "{color=#f6d6bd}Dalit{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "efren":
                            if not efren_highisland_joined or efren_highisland_blocked:
                                jump highisland_companionexhaustion_loop_denseplants
                            else:
                                if not efren_highisland_tired:
                                    $ efren_highisland_tired = 1
                                    $ custom1 = "Once you reach the next section of the trail, {color=#f6d6bd}Efren{/color} gestures for you to slow down and give him time to catch his breath."
                                else:
                                    $ efren_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom1 = "{color=#f6d6bd}Efren{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "thyrsus":
                            if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                jump highisland_companionexhaustion_loop_denseplants
                            else:
                                if not thyrsus_highisland_tired:
                                    $ thyrsus_highisland_tired = 1
                                    $ custom1 = "Once you reach the next section of the trail, {color=#f6d6bd}Thyrsus{/color} gestures for you to slow down and give him time to catch his breath."
                                else:
                                    $ thyrsus_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom1 = "{color=#f6d6bd}Thyrsus{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "pyrrhos":
                            if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                jump highisland_companionexhaustion_loop_denseplants
                            else:
                                if not pyrrhos_highisland_tired:
                                    $ pyrrhos_highisland_tired = 1
                                    $ custom1 = "Once you reach the next section of the trail, {color=#f6d6bd}Pyrrhos{/color} gestures for you to slow down and give him time to catch his breath."
                                else:
                                    $ pyrrhos_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "bandit":
                            if not bandit_highisland_joined or bandit_highisland_blocked:
                                jump highisland_companionexhaustion_loop_denseplants
                            else:
                                if not bandit_highisland_tired:
                                    $ bandit_highisland_tired = 1
                                    $ custom1 = "Once you reach the next section of the trail, {color=#f6d6bd}the bandit{/color} gestures for you to slow down and give him time to catch his breath."
                                else:
                                    $ bandit_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom1 = "{color=#f6d6bd}The bandit{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "tulia":
                            if not tulia_highisland_joined or tulia_highisland_blocked:
                                jump highisland_companionexhaustion_loop_denseplants
                            else:
                                if not tulia_highisland_tired:
                                    $ tulia_highisland_tired = 1
                                    $ custom1 = "Once you reach the next section of the trail, {color=#f6d6bd}Tulia{/color} gestures for you to slow down and give her time to catch her breath."
                                else:
                                    $ tulia_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom1 = "{color=#f6d6bd}Tulia{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "tzvi":
                            if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                jump highisland_companionexhaustion_loop_denseplants
                            else:
                                if not tzvi_highisland_tired:
                                    $ tzvi_highisland_tired = 1
                                    $ custom1 = "Once you reach the next section of the trail, {color=#f6d6bd}Tzvi{/color} gestures for you to slow down and give him time to catch his breath."
                                else:
                                    $ tzvi_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom1 = "{color=#f6d6bd}Tzvi{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "quintus":
                            if not quintus_highisland_joined or quintus_highisland_blocked:
                                jump highisland_companionexhaustion_loop_denseplants
                            else:
                                if not quintus_highisland_tired:
                                    $ quintus_highisland_tired = 1
                                    $ custom1 = "Once you reach the next section of the trail, {color=#f6d6bd}Quintus{/color} gestures for you to slow down and give him time to catch his breath."
                                else:
                                    $ quintus_highisland_blocked = 1
                                    $ highisland_crew_left -= 1
                                    $ custom1 = "{color=#f6d6bd}Quintus{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "pc":
                            $ custom1 = "Once you reach the next section of the trail, your stomach growls from hunger."
                            if pc_food:
                                $ pc_food = limit_pc_food(pc_food-2)
                                show minus2food at foodchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                            elif pc_hp > 0:
                                $ pc_hp = limit_pc_hp(pc_hp-1)
                                show minus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            else:
                                $ custom1 = "The work is grueling, but not as much as scaring away the harpies that are circling above you. Once they realize you are swaying on your feet, they dive at you, plunging their talons into your eyes."
                                jump highisland_gameover
                menu:
                    'The work is tiring, and would go faster if it wasn’t for the harpies circling above you. [custom1]
                    '
                    '“Make sure there are no thorns stuck in your pants!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Make sure there are no thorns stuck in your pants!”')
                        $ highisland_destination = "trolltunnel"
                        jump highisland_destination
            else:
                label highisland_companiondamage_loop_denseplants:
                    if highisland_crew_left <= 0:
                        $ custom1 = "Once you reach the next section of the trail, your stomach growls from hunger."
                        if pc_food:
                            $ pc_food = limit_pc_food(pc_food-2)
                            show minus2food at foodchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                        elif pc_hp > 0:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        else:
                            $ custom1 = "The work is grueling, but not as much as scaring away the harpies that are circling above you. Once they realize you are swaying on your feet, they dive at you, plunging their talons into your eyes."
                            jump highisland_gameover
                    else:
                        $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus', 'pc'])
                        if highisland_crew_dmg_target == "aegidia":
                            if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                jump highisland_companiondamage_loop_denseplants
                            else:
                                $ aegidia_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Aegidia{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "dalit":
                            if not dalit_highisland_joined or dalit_highisland_blocked:
                                jump highisland_companiondamage_loop_denseplants
                            else:
                                $ dalit_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Dalit{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "efren":
                            if not efren_highisland_joined or efren_highisland_blocked:
                                jump highisland_companiondamage_loop_denseplants
                            else:
                                $ efren_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Efren{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "thyrsus":
                            if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                jump highisland_companiondamage_loop_denseplants
                            else:
                                $ thyrsus_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Thyrsus{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "pyrrhos":
                            if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                jump highisland_companiondamage_loop_denseplants
                            else:
                                $ pyrrhos_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "bandit":
                            if not bandit_highisland_joined or bandit_highisland_blocked:
                                jump highisland_companiondamage_loop_denseplants
                            else:
                                $ bandit_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}The bandit{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "tulia":
                            if not tulia_highisland_joined or tulia_highisland_blocked:
                                jump highisland_companiondamage_loop_denseplants
                            else:
                                $ tulia_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Tulia{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "tzvi":
                            if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                jump highisland_companiondamage_loop_denseplants
                            else:
                                $ tzvi_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Tzvi{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "quintus":
                            if not quintus_highisland_joined or quintus_highisland_blocked:
                                jump highisland_companiondamage_loop_denseplants
                            else:
                                $ quintus_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Quintus{/color} struggles to reach the next section of the trail, completely exhausted."
                        elif highisland_crew_dmg_target == "pc":
                            $ custom1 = "Once you reach the next section of the trail, your stomach growls from hunger."
                            if pc_food:
                                $ pc_food = limit_pc_food(pc_food-2)
                                show minus2food at foodchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                            elif pc_hp > 0:
                                $ pc_hp = limit_pc_hp(pc_hp-1)
                                show minus1hp at hpchange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            else:
                                $ custom1 = "The work is grueling, but not as much as scaring away the harpies that are circling above you. Once they realize you are swaying on your feet, they dive at you, plunging their talons into your eyes."
                                jump highisland_gameover
                menu:
                    'The work is tiring, and would go faster if it wasn’t for the harpies circling above you. [custom1]
                    '
                    '“Make sure there are no thorns stuck in your pants!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Make sure there are no thorns stuck in your pants!”')
                        $ highisland_destination = "trolltunnel"
                        jump highisland_destination

label highisland_trolltunnelALL:
    label highisland_solo_trolltunnelALL:
        label highisland_solo_trolltunnel01:
            $ custom1 = "The road goes straight forward, suddenly getting much wider. The ground is surrounded with collapsed branches, trampled seedlings, and dead roe deer, but judging by the beaten path and the pebbles under the surface, this trail is as old as the previous ones."
            jump highisland_solo_trolltunnel01a

        label highisland_solo_trolltunnel01a:
            menu:
                '[custom1]
                '
                'I head in the direction of the volcano.' if not highisland_trolltunnel_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head in the direction of the volcano.')
                    jump highisland_solo_trolltunnel04
                'I think about the map from the giant statue.' if giantstatue_pray_map_learned and not highisland_trolltunnel_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about the map from the giant statue.')
                    $ highisland_trolltunnel_map = 1
                    $ custom1 = "You’ve no doubt that this trail is the main road to the volcano, but it’s not the {i}only{/i} route. According to the stars portrayed on the statue, there should be a shortcut somewhere around here, a narrower one, but much more direct."
                    jump highisland_solo_trolltunnel01a
                'I check if the shortcut is still there.' if highisland_trolltunnel_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check if the shortcut is still there.')
                    $ custom1 = "Behind a few fallen trunks you find the remnants of the path. The rotten, dug-in wooden stairs leading up the hill offer no support, but there’s plenty of paw prints on the ground and claw marks on the trees. It’s now a convenient game trail."
                    jump highisland_solo_trolltunnel03
                'I examine the area.' if not highisland_trolltunnel_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the area.')
                    $ highisland_trolltunnel_examine = 1
                    if highisland_lightsource:
                        $ highisland_trolltunnel_examine = 2
                        $ custom1 = "The light source helps you look around. Most of the fallen boughs still bear leaves, and some of the chest-size puddles turn out to be footprints left by some sort of a huge ape."
                    else:
                        $ highisland_trolltunnel_examine = 1
                        $ custom1 = "It’s not so easy without a decent light source, but you can tell that most of the fallen boughs are still coated with leaves."
                    jump highisland_solo_trolltunnel01a
                '{image=d6} I follow the main trail.' if highisland_trolltunnel_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I follow the main trail.')
                    jump highisland_solo_trolltunnel04
                '{image=d6} I look for another path.' if not highisland_trolltunnel_map and highisland_trolltunnel_examine >= 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I look for another path.')
                    jump highisland_solo_trolltunnel02

        label highisland_solo_trolltunnel02:
            show areapicture hi_trolltunnelgood at basicfade
            $ at = 0
            $ d100roll = renpy.random.randint(1, 100)
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            $ d100roll -= (shortcut_traveled*2)
            if not highisland_lightsource:
                $ d100roll += 15
            if d100roll <= 40:
                $ custom1 = "After a short search, you find remnants of an old path behind a few fallen trunks. The rotten, dug-in wooden stairs leading up the hill offer no support, but there’s plenty of paw prints on the ground and claw marks on the trees. It’s now a convenient game trail."
                label highisland_solo_trolltunnel03:
                    menu:
                        '[custom1]
                        '
                        'Maybe it’s a shortcut.' if not highisland_trolltunnel_map:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe it’s a shortcut.')
                            $ highisland_destination = "beastfolk"
                            jump highisland_destination
                        'Let’s see if it’s passable.' if highisland_trolltunnel_map:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s see if it’s passable.')
                            $ highisland_destination = "beastfolk"
                            jump highisland_destination
            else:
                if pc_food:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                menu:
                    'Not knowing where to start, you spend a good few minutes exploring the thicket, hardly able to press on, until you find remnants of an old path behind a few fallen trunks. The rotten, dug-in wooden stairs leading up the hill offer no support, but there’s plenty of paw prints on the ground and claw marks on the trees. It’s now a convenient game trail.
                    '
                    'Maybe it’s a shortcut.' if not highisland_trolltunnel_map:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe it’s a shortcut.')
                        $ highisland_destination = "beastfolk"
                        jump highisland_destination
                    'Let’s see if it’s passable.' if highisland_trolltunnel_map:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s see if it’s passable.')
                        $ highisland_destination = "beastfolk"
                        jump highisland_destination

        label highisland_solo_trolltunnel04:
            show areapicture hi_trolltunnelbad at basicfade
            $ highisland_trolltunnel_trollmet = 1
            menu:
                'After a few minutes, you come across an unusual crossroad. It’s of a similar size to the road you’ve been following and has even more signs of destruction, but other than that, it’s much more neglected, with tufts of grass and mushrooms and no rocks on the ground.
                \n\nBefore you come to a decision about what to do next, the roars and thumps of a beast make you flee. Carrying heavy bags and weapons, you try to pace your steps, knowing the hills ahead are not a trifle, but after the creature gets closer, you let yourself look behind only once, and barely stop yourself from a shout. The troll has the stature of a palisade, dark, thick fur, and long limbs, so massive they could tear you apart.
                '
                '{image=d6} I run for my life.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I run for my life.')
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
                    if not highisland_lightsource:
                        $ d100roll += 10
                    if d100roll <= 50:
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
                        else:
                            $ custom1 = "The sweat and tears mix on your face as you run forward, half-blind and gasping for air, thinking about the things you should drop. The beast’s legs are almost as long as you are tall, its every step matches a few of your leaps, and even though you look for a hideout desperately, you find none. The top of the hill is just ahead, but what then?\n\nThe creature’s hand hits your side before you learn the answer. Your back breaks after you hit the tree a few steps to your right."
                            jump highisland_gameover
                    else:
                        if armor >= 3:
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
                        elif armor == 1 and pc_hp >= 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ pc_hp = limit_pc_hp(pc_hp-2)
                            show minus2hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        elif pc_hp >= 2:
                            $ pc_hp = limit_pc_hp(pc_hp-3)
                            show minus3hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        else:
                            $ custom1 = "The sweat and tears mix on your face as you run forward, half-blind and gasping for air, thinking about the things you should drop. The beast’s legs are almost as long as you are tall, its every step matches a few of your leaps, and even though you look for a hideout desperately, you find none. The top of the hill is just ahead, but what then?\n\nThe creature’s hand hits your side before you learn the answer. Your back breaks after you hit the tree a few steps to your right."
                            jump highisland_gameover
                    menu:
                        'The sweat and tears mix on your face as you run forward, half-blind and gasping for air, thinking about the things you should drop. The beast’s legs are almost as long as you are tall, its every step matches a few of your leaps, and even though you look for a hideout desperately, you find none. The top of the hill is just ahead, but what then?
                        \n\nTired, you don’t stop, just let your instincts guide you. You fall on your side and keep the momentum going, either rolling down the hillside or dashing forward, crushing into the ground. Your head hits a few rocks and at one point you almost break your arm, but you can’t stop now, even if you wanted to.
                        \n\nFinally, you stop at the bottom of the hill and let out a moan. The songs of birds and monkeys, distracting from the distant roars, are almost soothing.
                        '
                        'I can’t stay here.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t stay here.')
                            $ highisland_destination = "beastfolk"
                            jump highisland_destination

    label highisland_howlers_trolltunnelALL:
        label highisland_howlers_trolltunnel01:
            $ custom1 = "The road goes straight forward, suddenly getting much wider. The ground is surrounded with collapsed branches, trampled seedlings, and dead roe deer, but judging by the beaten path and the pebbles under the surface, this trail is as old as the previous ones. “Finally some space to spread one’s arms,” says {color=#f6d6bd}the guard with the spear{/color}, but {color=#f6d6bd}the one with the bow{/color} gestures for her to wait. “I do ne trust this place. ‘Tis weird, as if someone trimmed the trees above.”"
            jump highisland_howlers_trolltunnel01a

        label highisland_howlers_trolltunnel01a:
            menu:
                '[custom1]
                '
                'I gesture for them to keep going. “The volcano is this way.”' if not highisland_trolltunnel_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gesture for them to keep going. “The volcano is this way.”')
                    jump highisland_howlers_trolltunnel04
                'I think about the map from the giant statue.' if giantstatue_pray_map_learned and not highisland_trolltunnel_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about the map from the giant statue.')
                    $ highisland_trolltunnel_map = 1
                    $ custom1 = "You’ve no doubt that this trail is the main road to the volcano, but it’s not the {i}only{/i} route. According to the stars portrayed on the statue, there should be a shortcut somewhere around here, a narrower one, but much more direct."
                    jump highisland_howlers_trolltunnel01a
                'I check if the shortcut is still there.' if highisland_trolltunnel_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check if the shortcut is still there.')
                    $ custom1 = "Behind a few fallen trunks you find the remnants of the path. The rotten, dug-in wooden stairs leading up the hill offer no support, but there’s plenty of paw prints on the ground and claw marks on the trees. It’s now a convenient game trail."
                    jump highisland_howlers_trolltunnel03
                'I examine the area.' if not highisland_trolltunnel_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the area.')
                    $ highisland_trolltunnel_examine = 2
                    if highisland_lightsource:
                        $ custom1 = "The light source helps you look around, and {color=#f6d6bd}the guards{/color} are quick to join you. “Something ran here and broke these branches,” says {color=#f6d6bd}the young druid{/color}. “See those puddles? These are paw prints of a troll.”"
                    else:
                        $ custom1 = "It’s not so easy without a decent light source, but {color=#f6d6bd}the guards{/color} are quick to join you. “Something ran here and broke these branches,” says {color=#f6d6bd}the young druid{/color}. “See those puddles? These are paw prints of a troll.”"
                    jump highisland_howlers_trolltunnel01a
                '{image=d6} “We should follow the main trail.”' if highisland_trolltunnel_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “We should follow the main trail.”')
                    jump highisland_howlers_trolltunnel04
                '{image=d6} “Let’s look for another path.”' if not highisland_trolltunnel_map and highisland_trolltunnel_examine >= 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Let’s look for another path.”')
                    jump highisland_howlers_trolltunnel02

        label highisland_howlers_trolltunnel02:
            show areapicture hi_trolltunnelgood at basicfade
            $ at = 0
            $ d100roll = renpy.random.randint(1, 100)
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            $ d100roll -= (shortcut_traveled*2)
            if not highisland_lightsource:
                $ d100roll += 15
            $ d100roll -= (highisland_howlersguards_hp*5)
            if d100roll <= 40:
                $ custom1 = "After a short search, you find remnants of an old path behind a few fallen trunks. The rotten, dug-in wooden stairs leading up the hill offer no support, but there’s plenty of paw prints on the ground and claw marks on the trees. It’s now a convenient game trail."
                label highisland_howlers_trolltunnel03:
                    menu:
                        '[custom1]
                        '
                        'I call the others. “Let’s see if this path is clear!”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I call the others. “Let’s see if this path is clear!”')
                            $ highisland_destination = "beastfolk"
                            jump highisland_destination
            else:
                $ highisland_howlersguards_hp -= 1
                menu:
                    'Not knowing where to start, you ask the others to help you, and spend a good few minutes exploring the thicket, hardly able to press on, until you find remnants of an old path behind a few fallen trunks. The rotten, dug-in wooden stairs leading up the hill offer no support, but there’s plenty of paw prints on the ground and claw marks on the trees. It’s now a convenient game trail.
                    '
                    'I call the others. “Let’s see if this path is clear!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I call the others. “Let’s see if this path is clear!”')
                        $ highisland_destination = "beastfolk"
                        jump highisland_destination

        label highisland_howlers_trolltunnel04:
            show areapicture hi_trolltunnelbad at basicfade
            $ highisland_trolltunnel_trollmet = 1
            menu:
                'After a few minutes, you come across an unusual crossroad. It’s of a similar size to the road you’ve been following and has even more signs of destruction, but other than that, it’s much more neglected, with tufts of grass and mushrooms and no rocks on the ground.
                \n\nBefore you come to a decision about what to do next, the roars and thumps of a beast make you flinch. You step back, rattling with your heavy bags and weapons, and look at your companions. {color=#f6d6bd}The young druid{/color} is as pale as the moonlight. “Spirits, dwell in our hands.”
                \n\n{color=#f6d6bd}The leader{/color} raises his voice, but his eyes are locked on you. “Hold your ground! We can ne escape from it!”
                '
                '{image=d6} I leave my bundles on the ground and pull out my fighting equipment.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I leave my bundles on the ground and pull out my fighting equipment.')
                    $ d100roll = renpy.random.randint(40, 75)
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
                    if not highisland_lightsource:
                        $ d100roll += 10
                    if item_golemglove:
                        $ d100roll -= 10
                    if item_axe03:
                        $ d100roll -= 20
                    elif item_axe02 or item_axe02alt:
                        $ d100roll -= 10
                    if item_asterionspear or item_mountainroadspear:
                        $ d100roll -= 5
                    if item_shield:
                        $ d100roll -= 5
                    if item_blindingpowder:
                        $ d100roll -= 5
                    $ d100roll -= (highisland_howlersguards_hp*5)
                    if d100roll >= 1:
                        $ highisland_trolltunnel_howlersdmg = ((d100roll/10)+1)
                    else:
                        $ highisland_trolltunnel_howlersdmg = 1
                    $ highisland_howlersguards_hp -= highisland_trolltunnel_howlersdmg
                    $ pc_battlecounter += 1
                    if highisland_howlersguards_hp <= 1:
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
                        else:
                            $ custom1 = "The dark-furred beast, heavier than your entire group and as tall as a palisade, comes out of the tunnel of leaves, ignoring any arrows that hit it, and reaches for the spearwoman, the first shell in its range. She stabs its arm, but fails to dodge its grasp - the troll lifts her up and tears her in half, giving her no time to scream.\n\nThe rest of your exhausted group scatters in panic, and the monster chases after you, with each of its steps covering as much as a few of your desperate leaps."
                            jump highisland_gameover
                    elif highisland_howlersguards_hp <= 4:
                        if armor >= 3:
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
                        elif armor == 1 and pc_hp >= 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ pc_hp = limit_pc_hp(pc_hp-2)
                            show minus2hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        elif pc_hp >= 2:
                            $ pc_hp = limit_pc_hp(pc_hp-3)
                            show minus3hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        else:
                            $ custom1 = "The dark-furred beast, heavier than your entire group and as tall as a palisade, comes out of the tunnel of leaves, ignoring any arrows that hit it, and reaches for the spearwoman, the first shell in its range. She stabs its arm, but fails to dodge its grasp - the troll lifts her up and tears her in half, giving her no time to scream.\n\nThe rest of your exhausted group scatters in panic, and the monster chases after you, with each of its steps covering as much as a few of your desperate leaps."
                            jump highisland_gameover
                    else:
                        if armor == 4:
                            $ armor = limit_armor(armor-3)
                            show minus3armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 armor points.{/i}')
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        elif armor == 3 and pc_hp >= 1:
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
                        elif armor == 2 and pc_hp >= 1:
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
                        elif armor == 1 and pc_hp >= 2:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ pc_hp = limit_pc_hp(pc_hp-3)
                            show minus3hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        elif pc_hp >= 3:
                            $ pc_hp = limit_pc_hp(pc_hp-4)
                            show minus4hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        else:
                            $ custom1 = "The dark-furred beast, heavier than your entire group and as tall as a palisade, comes out of the tunnel of leaves, ignoring any arrows that hit it, and reaches for the spearwoman, the first shell in its range. She stabs its arm, but fails to dodge its grasp - the troll lifts her up and tears her in half, giving her no time to scream.\n\nThe rest of your exhausted group scatters in panic, and the monster chases after you, with each of its steps covering as much as a few of your desperate leaps."
                            jump highisland_gameover
                    if highisland_trolltunnel_howlersdmg <= 1:
                        $ custom1 = "Thankfully, all of you got out of the battle with only minor bruises."
                    elif highisland_trolltunnel_howlersdmg == 2:
                        $ custom1 = "Thankfully, with {color=#f6d6bd}the young druid’s{/color} healing spells, all of you got out of the battle with only mild injuries."
                    elif highisland_trolltunnel_howlersdmg == 3:
                        $ custom1 = "Despite {color=#f6d6bd}the young druid’s{/color} healing spells, some of you suffered rather serious wounds."
                    elif highisland_trolltunnel_howlersdmg == 4:
                        $ custom1 = "Despite {color=#f6d6bd}the young druid’s{/color} healing spells, some of you suffered rather severe wounds. {color=#f6d6bd}The one with the spear{/color} has to carry on with a broken arm."
                    else:
                        $ custom1 = "Despite {color=#f6d6bd}the young druid’s{/color} healing spells, some of you suffered rather severe wounds. {color=#f6d6bd}The one with the spear{/color} was brought back from the verge of death, but needs to carry on with a broken arm."
                    nvl clear
                    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                    menu:
                        '“We can ne stay here,” declares {color=#f6d6bd}the leader{/color} with a voice that sounds as if it’s coming through the mist.
                        \n\nYou wipe the sweat and tears from your lips. The dark-furred, warm carcass, heavier than your entire group and as tall as a palisade, is now laying on its back, in a puddle of blood - not all of which belongs to it. [custom1]
                        \n\nYou stretch your back and let out a moan, still looking at the arms of the beast, large enough to tear a human apart. The songs of birds and monkeys, distracting from the distant roars, are almost soothing.
                        \n\n“You heard me?” growls {color=#f6d6bd}the guard{/color} as he wipes blood from the troll’s tusk.
                        '
                        'I nod. “Let’s go.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “Let’s go.”')
                            $ highisland_destination = "beastfolk"
                            jump highisland_destination
                        'I offer them a healing potion.' if item_generichealingpotion:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer them a healing potion.')
                            $ item_generichealingpotion -= 1
                            $ renpy.notify("You lost a healing potion.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a healing potion.{/i}')
                            $ highisland_howlersguards_hp += 4
                            $ highisland_trolltunnel_howlerspotion += 1
                            menu:
                                '“Thanks,” mutters {color=#f6d6bd}the spearwoman{/color} and takes a few sips, then shares the rest with {color=#f6d6bd}the one with the mace{/color}. The cuts and bruises on her face seal and turn pale right away.
                                '
                                'I collect my bundles.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I collect my bundles.')
                                    $ highisland_destination = "beastfolk"
                                    jump highisland_destination
                        'I offer them the potion from the dolmen.' if item_potiondolmen and item_potiondolmen_known:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer them the potion from the dolmen.')
                            $ item_potiondolmen -= 1
                            $ renpy.notify("You lost the potion from the dolmen.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the potion from the dolmen.{/i}')
                            $ highisland_howlersguards_hp += 4
                            $ highisland_trolltunnel_howlerspotion += 1
                            menu:
                                '“Thanks,” mutters {color=#f6d6bd}the spearwoman{/color} and takes a few sips, then shares the rest with {color=#f6d6bd}the one with the mace{/color}. The cuts and bruises on her face seal and turn pale right away.
                                '
                                'I collect my bundles.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I collect my bundles.')
                                    $ highisland_destination = "beastfolk"
                                    jump highisland_destination
                        'I offer them a small healing potion.' if item_smallhealingpotion:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer them a small healing potion.')
                            $ item_smallhealingpotion -= 1
                            $ renpy.notify("You lost a small healing potion.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a small healing potion.{/i}')
                            $ highisland_howlersguards_hp += 2
                            $ highisland_trolltunnel_howlerspotion += 1
                            menu:
                                '“Thanks,” mutters {color=#f6d6bd}the spearwoman{/color} and drinks it all in one large gulp. The cuts and bruises on her face seal and turn pale right away.
                                '
                                'I collect my bundles.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I collect my bundles.')
                                    $ highisland_destination = "beastfolk"
                                    jump highisland_destination
                        'I’ve got no potions to offer. (disabled)' if (not item_generichealingpotion and not item_potiondolmen and not item_smallhealingpotion) or (not item_generichealingpotion and item_potiondolmen and not item_potiondolmen_known and not item_smallhealingpotion):
                            pass

    label highisland_crew_trolltunnelALL:
        label highisland_crew_trolltunnel01:
            $ custom1 = "The road goes straight forward, suddenly getting much wider. The ground is surrounded with collapsed branches, trampled seedlings, and dead roe deer, but judging by the beaten path and the pebbles under the surface, this trail is as old as the previous ones."
            jump highisland_crew_trolltunnel01a

        label highisland_crew_trolltunnel01a:
            menu:
                '[custom1]
                '
                'I head in the direction of the volcano.' if not highisland_trolltunnel_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head in the direction of the volcano.')
                    jump highisland_crew_trolltunnel04
                'I think about the map from the giant statue.' if giantstatue_pray_map_learned and not highisland_trolltunnel_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about the map from the giant statue.')
                    $ highisland_trolltunnel_map = 1
                    $ custom1 = "You’ve no doubt that this trail is the main road to the volcano, but it’s not the {i}only{/i} route. According to the stars portrayed on the statue, there should be a shortcut somewhere around here, a narrower one, but much more direct."
                    jump highisland_crew_trolltunnel01a
                'I check if the shortcut is still there.' if highisland_trolltunnel_map:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check if the shortcut is still there.')
                    $ custom1 = "Behind a few fallen trunks you find the remnants of the path. The rotten, dug-in wooden stairs leading up the hill offer no support, but there’s plenty of paw prints on the ground and claw marks on the trees. It’s now a convenient game trail."
                    jump highisland_crew_trolltunnel03
                '“Thoughts, {color=#f6d6bd}Aegidia{/color}?”' if aegidia_highisland_joined and not aegidia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thoughts, {color=#f6d6bd}Aegidia{/color}?”')
                    $ aegidia_highisland_opinion = 1
                    $ custom1 = "“Such a wide trail? Here?” She taps her lips with the tip of her bow."
                    jump highisland_crew_trolltunnel01a
                '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and not dalit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                    $ dalit_highisland_opinion = 1
                    if not dalit_highisland_blocked:
                        $ highisland_trolltunnel_examine = 2
                        $ custom1 = "She crouches down and gestures for you to join her. “See these puddles? Troll prints,” she draws the shape of an ape foot with her hand. “It walks here often, both ways. Better to look for another path.”"
                    else:
                        $ custom1 = "She blinks a few times before she says anything. She’s so tired she looks like she’s going to fall."
                    jump highisland_crew_trolltunnel01a
                '“Any tips, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and not efren_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips, {color=#f6d6bd}Efren{/color}?”')
                    $ efren_highisland_opinion = 1
                    if not efren_highisland_blocked:
                        $ highisland_trolltunnel_examine = 2
                        $ custom1 = "He pushes away the wolf’s nose. “Don’t you see the troll prints, friend? It’s a dangerous path.”"
                    else:
                        $ custom1 = "He wipes his forehead into the wolf’s nose. “Give me a break, friend. The road looks fine. Maybe there are other folks around?”"
                    jump highisland_crew_trolltunnel01a
                '“{color=#f6d6bd}Thyrsus{/color}, suggestions?”' if thyrsus_highisland_joined and not thyrsus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, suggestions?”')
                    $ thyrsus_highisland_opinion = 1
                    $ custom1 = "“Better this than the thicket.”"
                    jump highisland_crew_trolltunnel01a
                '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and not pyrrhos_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                    $ pyrrhos_highisland_opinion = 1
                    $ custom1 = ""
                    if not pyrrhos_highisland_blocked:
                        $ highisland_trolltunnel_examine = 2
                        $ custom1 = "He takes a few sips of water, his eyes serious. “Something large came here, broke the branches going both this way,” he nods forward, “and back,” he points behind him with his thumb. “I’d say, let’s look for another path.”"
                    else:
                        $ custom1 = "He takes a few sips of water. “Eh? What, ye think something’s off?”"
                    jump highisland_crew_trolltunnel01a
                'I look at {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and not bandit_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}the bandit{/color}.')
                    $ bandit_highisland_opinion = 1
                    $ custom1 = "He observes the stars, frowning."
                    jump highisland_crew_trolltunnel01a
                '“{color=#f6d6bd}Tulia{/color}, what do you recommend?”' if tulia_highisland_joined and not tulia_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, what do you recommend?”')
                    $ tulia_highisland_opinion = 1
                    $ custom1 = "She looks around. “We should make a formation and protect the weaker members of the group.”"
                    jump highisland_crew_trolltunnel01a
                '“Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”' if tzvi_highisland_joined and not tzvi_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”')
                    $ tzvi_highisland_opinion = 1
                    $ custom1 = "“Hwat do you mean? A road is a road.”"
                    jump highisland_crew_trolltunnel01a
                '“{color=#f6d6bd}Quintus{/color}, any ideas?”' if quintus_highisland_joined and not quintus_highisland_opinion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Quintus{/color}, any ideas?”')
                    $ quintus_highisland_opinion = 1
                    $ custom1 = "He shrugs and takes a few steps up the road."
                    jump highisland_crew_trolltunnel01a
                'I examine the area.' if not highisland_trolltunnel_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the area.')
                    if highisland_lightsource:
                        $ highisland_trolltunnel_examine = 2
                        $ custom1 = "The light source helps you look around. Most of the fallen boughs still bear leaves, and some of the chest-size puddles turn out to be footprints left by some sort of a huge ape."
                    else:
                        $ highisland_trolltunnel_examine = 1
                        $ custom1 = "It’s not so easy without a decent light source, but you can tell that most of the fallen boughs are still coated with leaves."
                    jump highisland_crew_trolltunnel01a
                '{image=d6} “We should follow the main trail.”' if highisland_trolltunnel_examine:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “We should follow the main trail.”')
                    jump highisland_crew_trolltunnel04
                '{image=d6} “Let’s look for another path.”' if not highisland_trolltunnel_map and highisland_trolltunnel_examine >= 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “Let’s look for another path.”')
                    jump highisland_crew_trolltunnel02

        label highisland_crew_trolltunnel02:
            show areapicture hi_trolltunnelgood at basicfade
            $ at = 0
            $ d100roll = renpy.random.randint(1, 100)
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            $ d100roll -= (shortcut_traveled*2)
            if not highisland_lightsource:
                $ d100roll += 15
            if d100roll <= 40:
                $ custom1 = "After a short search, you find remnants of an old path behind a few fallen trunks. The rotten, dug-in wooden stairs leading up the hill offer no support, but there’s plenty of paw prints on the ground and claw marks on the trees. It’s now a convenient game trail."
                label highisland_crew_trolltunnel03:
                    menu:
                        '[custom1]
                        '
                        'I call the others. “Let’s see if this path is clear!”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I call the others. “Let’s see if this path is clear!”')
                            $ highisland_destination = "beastfolk"
                            jump highisland_destination
            else:
                if pc_food:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                menu:
                    'Not knowing where to start, you ask the others to help you, and spend a good few minutes exploring the thicket, hardly able to press on, until you find remnants of an old path behind a few fallen trunks. The rotten, dug-in wooden stairs leading up the hill offer no support, but there’s plenty of paw prints on the ground and claw marks on the trees. It’s now a convenient game trail.
                    '
                    'I call the others. “Let’s see if this path is clear!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I call the others. “Let’s see if this path is clear!”')
                        $ highisland_destination = "beastfolk"
                        jump highisland_destination

        label highisland_crew_trolltunnel04:
            show areapicture hi_trolltunnelbad at basicfade
            $ highisland_trolltunnel_trollmet = 1
            if tulia_highisland_joined:
                $ custom18 = " {color=#f6d6bd}Tulia{/color} is the first one to pull out her blade and make an angry grunt. “I know that sound.”"
            else:
                $ custom18 = ""
            menu:
                'After a few minutes, you come across an unusual crossroad. It’s of a similar size to the road you’ve been following and has even more signs of destruction, but other than that, it’s much more neglected, with tufts of grass and mushrooms and no rocks on the ground.
                \n\nBefore you come to a decision about what to do next, the roars and thumps of a beast make you flinch. You step back, rattling with your heavy bags and weapons, and look at your pale companions.[custom18]
                '
                '{image=d6} I drop my bundles and grab my axe. “We can’t outrun it. Prepare yourselves!”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I drop my bundles and grab my axe. “We can’t outrun it. Prepare yourselves!”')
                    if bandit_highisland_joined:
                        if not bandit_highisland_tired and not bandit_highisland_blocked:
                            $ bandit_highisland_blocked = 1
                            $ highisland_crew_left -= 1
                        else:
                            $ shortcut_darkforest_bandit_dead_troll = 1
                            $ shortcut_darkforest_bandit_inpeltnorth = 0
                            $ peltnorth_bonusnpcs -= 1
                            $ highisland_crew_left -= 1
                        menu:
                            '{color=#f6d6bd}The bandit{/color} pulls your shoulder. His eyes pierce yours.
                            \n\n“Troll. I’ll lure it away. You run. Stay on the road so I can find you, but don’t wait.”
                            \n\nBefore you respond, he dashes into the leafy corridor, blending with the night.
                            '
                            'I collect my things and flee, up the main path.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I collect my things and flee, up the main path.')
                                if quintus_highisland_joined:
                                    $ custom11 = "\n\n“A brave soul,” {color=#f6d6bd}Quintus{/color} pants. “I’ll buy him a few rounds back in the inn.”"
                                else:
                                    $ custom11 = ""
                                if tzvi_highisland_joined:
                                    $ custom12 = "\n\n“He’s not coming back,” {color=#f6d6bd}Tzvi{/color} adjusts his cape."
                                else:
                                    $ custom12 = ""
                                if aegidia_highisland_joined:
                                    $ custom13 = "\n\n“He saved us,” states {color=#f6d6bd}Aegidia{/color} and raises her bow in salute, in the direction of the noises."
                                else:
                                    $ custom13 = ""
                                if dalit_highisland_joined:
                                    $ custom14 = "\n\n“It was a troll, wasn’t it?” {color=#f6d6bd}Dalit{/color} shoves a strand of hair behind her ear. “He saved us.”"
                                else:
                                    $ custom14 = ""
                                if efren_highisland_joined:
                                    $ custom15 = "\n\n{color=#f6d6bd}Efren{/color} snorts and wipes his nose into his sleeve."
                                else:
                                    $ custom15 = ""
                                if thyrsus_highisland_joined:
                                    $ custom16 = "\n\n{color=#f6d6bd}Thyrsus’{/color} fingers are clenched around his amulets."
                                else:
                                    $ custom16 = ""
                                if pyrrhos_highisland_joined:
                                    $ custom17 = "\n\n{color=#f6d6bd}Pyrrhos{/color} examines his crossbow and prepares himself to climb down."
                                else:
                                    $ custom17 = ""
                                if tulia_highisland_joined:
                                    $ custom18 = "\n\n{color=#f6d6bd}Tulia{/color} rubs her temples."
                                else:
                                    $ custom18 = ""
                                menu:
                                    'You pace your steps, knowing the hills ahead are not a trifle. Behind you sounds a battle cry, soon followed by a nightmarish roar and the sound of broken branches. Despite everything, the sounds of the chase don’t stop, and while the monster’s voice remains furious, it moves further and further away.
                                    \n\nWhen your crew reaches the top of the hill, you slow down, ready to climb down. Your hearts are pounding, and a few curious eyes turn around.[custom11][custom12][custom13][custom14][custom15][custom16][custom17][custom18]
                                    '
                                    '“Let’s wait for him. Just in case.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s wait for him. Just in case.”')
                                        if not shortcut_darkforest_bandit_dead_troll:
                                            $ custom1 = " You walk in silence until {color=#f6d6bd}the bandit{/color} gets to you through the bushes, without a sound - pale, wounded, quiet, and with eyes wide open. The others start to thank him, but he makes sure no one gets close enough to touch him. “My pneuma’s dry now,” he looks down, at the blood dripping from his arm. “Don’t think I’ll do that again.”"
                                        else:
                                            $ custom1 = ""
                                        menu:
                                            'The long minutes go by, and the sounds of a clash between the beasts in the deep woods make it clear you can’t stay here any longer.[custom1]
                                            '
                                            'I nod to him. “Thank you.”' if not shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to him. “Thank you.”')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                                            '“Good job. Let’s not wait for another beast.”' if not shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Good job. Let’s not wait for another beast.”')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                                            'I let the others do the talking.' if not shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the others do the talking.')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                                            'He’s not one to sacrifice himself for the sake of others. He’ll be back.' if shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s not one to sacrifice himself for the sake of others. He’ll be back.')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                                            'It was his choice, not mine.' if shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It was his choice, not mine.')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                                            'He’s gone because of me. I wasn’t ready for this place.' if shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s gone because of me. I wasn’t ready for this place.')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                                    '“He told us to keep going.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He told us to keep going.”')
                                        if not shortcut_darkforest_bandit_dead_troll:
                                            $ custom1 = " You walk in silence until {color=#f6d6bd}the bandit{/color} gets to you through the bushes, without a sound - pale, wounded, quiet, and with eyes wide open. The others start to thank him, but he makes sure no one gets close enough to touch him. “My pneuma’s dry now,” he looks down, at the blood dripping from his arm. “Don’t think I’ll do that again.”"
                                        else:
                                            $ custom1 = ""
                                        menu:
                                            'The path down is gentle, cleared by the recent forest fire.[custom1]
                                            '
                                            'I nod to him. “Thank you.”' if not shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to him. “Thank you.”')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                                            '“Good job. Let’s not wait for another beast.”' if not shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Good job. Let’s not wait for another beast.”')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                                            'I let the others do the talking.' if not shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let the others do the talking.')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                                            'He’s not one to sacrifice himself for the sake of others. He’ll be back.' if shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s not one to sacrifice himself for the sake of others. He’ll be back.')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                                            'It was his choice, not mine.' if shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It was his choice, not mine.')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                                            'He’s gone because of me. I wasn’t ready for this place.' if shortcut_darkforest_bandit_dead_troll:
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s gone because of me. I wasn’t ready for this place.')
                                                $ highisland_destination = "beastfolk"
                                                jump highisland_destination
                    $ d100roll = renpy.random.randint(40, 75)
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
                    if not highisland_lightsource:
                        $ d100roll += 10
                    if item_golemglove:
                        $ d100roll -= 10
                    if item_axe03:
                        $ d100roll -= 20
                    elif item_axe02 or item_axe02alt:
                        $ d100roll -= 10
                    if item_asterionspear or item_mountainroadspear:
                        $ d100roll -= 5
                    if item_shield:
                        $ d100roll -= 5
                    if item_blindingpowder:
                        $ d100roll -= 5
                    if aegidia_highisland_joined and not aegidia_highisland_blocked:
                        $ d100roll -= 5
                    if dalit_highisland_joined and not dalit_highisland_blocked:
                        $ d100roll -= 10
                    if efren_highisland_joined and not efren_highisland_blocked:
                        $ d100roll -= 5
                    if thyrsus_highisland_joined and not thyrsus_highisland_blocked:
                        $ d100roll -= 10
                    if pyrrhos_highisland_joined and not pyrrhos_highisland_blocked:
                        $ d100roll -= 5
                    if bandit_highisland_joined and not bandit_highisland_blocked:
                        $ d100roll -= 5
                    if tulia_highisland_joined and not tulia_highisland_blocked:
                        $ d100roll -= 15
                    if tzvi_highisland_joined and not tzvi_highisland_blocked:
                        $ d100roll -= 5
                    if quintus_highisland_joined and not quintus_highisland_blocked:
                        $ d100roll -= 10
                    $ custom1 = ""
                    $ custom2 = ""
                    $ custom3 = ""
                    $ custom4 = ""
                    $ pc_battlecounter += 1
                    if d100roll <= 0:
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
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        else:
                            $ custom1 = "The dark-furred beast, heavier than your entire group and as tall as a palisade, comes out of the tunnel of leaves, ignoring anything you throw at it, and reaches for the nearest shell. The troll lifts them up, then tears them in half before they make as much as a scream.\n\nThe rest of your exhausted group scatters in panic, and the monster chases after you, with each of its steps covering as much as a few of your desperate leaps."
                            jump highisland_gameover
                        if highisland_crew_left >= 2:
                            label highisland_companionexhaustion_loop_trolltunnel4a:
                                $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus'])
                                if highisland_crew_dmg_target == "aegidia":
                                    if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4a
                                    else:
                                        if not aegidia_highisland_tired:
                                            $ aegidia_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ aegidia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "dalit":
                                    if not dalit_highisland_joined or dalit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4a
                                    else:
                                        if not dalit_highisland_tired:
                                            $ dalit_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Dalit{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ dalit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Dalit{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "efren":
                                    if not efren_highisland_joined or efren_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4a
                                    else:
                                        if not efren_highisland_tired:
                                            $ efren_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Efren{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ efren_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Efren{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "thyrsus":
                                    if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4a
                                    else:
                                        if not thyrsus_highisland_tired:
                                            $ thyrsus_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Thyrsus{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ thyrsus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Thyrsus{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "pyrrhos":
                                    if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4a
                                    else:
                                        if not pyrrhos_highisland_tired:
                                            $ pyrrhos_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ pyrrhos_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "bandit":
                                    if not bandit_highisland_joined or bandit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4a
                                    else:
                                        if not bandit_highisland_tired:
                                            $ bandit_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}The bandit{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ bandit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}The bandit{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "tulia":
                                    if not tulia_highisland_joined or tulia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4a
                                    else:
                                        if not tulia_highisland_tired:
                                            $ tulia_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Tulia{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ tulia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Tulia{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "tzvi":
                                    if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4a
                                    else:
                                        if not tzvi_highisland_tired:
                                            $ tzvi_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ tzvi_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "quintus":
                                    if not quintus_highisland_joined or quintus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4a
                                    else:
                                        if not quintus_highisland_tired:
                                            $ quintus_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Quintus{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ quintus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Quintus{/color} got severely wounded."
                        else:
                            $ custom1 = "You run your eyes over your crew, wounded and exhausted. You doubt they can go much further."
                        nvl clear
                        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                        menu:
                            'You wipe the sweat and tears from your lips. The dark-furred, warm carcass is heavier than your entire group and as tall as a palisade, with arms large enough to tear a human apart. It’s laying on its back, in a puddle of blood - not all of which belongs to it. [custom1]
                            \n\nYou stretch your back and let out a moan. The songs of birds and monkeys, distracting from the distant roars, are almost soothing.
                            '
                            '“We can’t stay here. Let’s move on.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We can’t stay here. Let’s move on.”')
                                $ highisland_destination = "beastfolk"
                                jump highisland_destination
                    elif d100roll <= 15:
                        if armor >= 3:
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
                        elif armor == 1 and pc_hp >= 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ pc_hp = limit_pc_hp(pc_hp-2)
                            show minus2hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        elif pc_hp >= 2:
                            $ pc_hp = limit_pc_hp(pc_hp-3)
                            show minus3hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        else:
                            $ custom1 = "The dark-furred beast, heavier than your entire group and as tall as a palisade, comes out of the tunnel of leaves, ignoring anything you throw at it, and reaches for the nearest shell. The troll lifts them up, then tears them in half before they make as much as a scream.\n\nThe rest of your exhausted group scatters in panic, and the monster chases after you, with each of its steps covering as much as a few of your desperate leaps."
                            jump highisland_gameover
                        if highisland_crew_left >= 3:
                            label highisland_companionexhaustion_loop_trolltunnel4b:
                                $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus'])
                                if highisland_crew_dmg_target == "aegidia":
                                    if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4b
                                    else:
                                        if not aegidia_highisland_tired:
                                            $ aegidia_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ aegidia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "dalit":
                                    if not dalit_highisland_joined or dalit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4b
                                    else:
                                        if not dalit_highisland_tired:
                                            $ dalit_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Dalit{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ dalit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Dalit{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "efren":
                                    if not efren_highisland_joined or efren_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4b
                                    else:
                                        if not efren_highisland_tired:
                                            $ efren_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Efren{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ efren_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Efren{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "thyrsus":
                                    if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4b
                                    else:
                                        if not thyrsus_highisland_tired:
                                            $ thyrsus_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Thyrsus{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ thyrsus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Thyrsus{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "pyrrhos":
                                    if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4b
                                    else:
                                        if not pyrrhos_highisland_tired:
                                            $ pyrrhos_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ pyrrhos_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "bandit":
                                    if not bandit_highisland_joined or bandit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4b
                                    else:
                                        if not bandit_highisland_tired:
                                            $ bandit_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}The bandit{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ bandit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}The bandit{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "tulia":
                                    if not tulia_highisland_joined or tulia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4b
                                    else:
                                        if not tulia_highisland_tired:
                                            $ tulia_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Tulia{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ tulia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Tulia{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "tzvi":
                                    if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4b
                                    else:
                                        if not tzvi_highisland_tired:
                                            $ tzvi_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ tzvi_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "quintus":
                                    if not quintus_highisland_joined or quintus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4b
                                    else:
                                        if not quintus_highisland_tired:
                                            $ quintus_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Quintus{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ quintus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Quintus{/color} got severely wounded."
                            label highisland_companionexhaustion_loop_trolltunnel4bb:
                                $ highisland_crew_dmg_target2 = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus'])
                                if highisland_crew_dmg_target2 == highisland_crew_dmg_target:
                                    jump highisland_companionexhaustion_loop_trolltunnel4bb
                                if highisland_crew_dmg_target2 == "aegidia":
                                    if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4bb
                                    else:
                                        if not aegidia_highisland_tired:
                                            $ aegidia_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Aegidia{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ aegidia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Aegidia{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "dalit":
                                    if not dalit_highisland_joined or dalit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4bb
                                    else:
                                        if not dalit_highisland_tired:
                                            $ dalit_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Dalit{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ dalit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Dalit{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "efren":
                                    if not efren_highisland_joined or efren_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4bb
                                    else:
                                        if not efren_highisland_tired:
                                            $ efren_highisland_tired = 1
                                            $ custom2 = "{color=#f6d6bd}Efren{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ efren_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Efren{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "thyrsus":
                                    if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4bb
                                    else:
                                        if not thyrsus_highisland_tired:
                                            $ thyrsus_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Thyrsus{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ thyrsus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Thyrsus{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "pyrrhos":
                                    if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4bb
                                    else:
                                        if not pyrrhos_highisland_tired:
                                            $ pyrrhos_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Pyrrhos{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ pyrrhos_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Pyrrhos{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "bandit":
                                    if not bandit_highisland_joined or bandit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4bb
                                    else:
                                        if not bandit_highisland_tired:
                                            $ bandit_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}The bandit{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ bandit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}The bandit{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "tulia":
                                    if not tulia_highisland_joined or tulia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4bb
                                    else:
                                        if not tulia_highisland_tired:
                                            $ tulia_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Tulia{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ tulia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Tulia{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "tzvi":
                                    if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4bb
                                    else:
                                        if not tzvi_highisland_tired:
                                            $ tzvi_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Tzvi{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ tzvi_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Tzvi{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "quintus":
                                    if not quintus_highisland_joined or quintus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4bb
                                    else:
                                        if not quintus_highisland_tired:
                                            $ quintus_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Quintus{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ quintus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Quintus{/color} is barely standing."
                        else:
                            $ aegidia_highisland_blocked = 1
                            $ dalit_highisland_blocked = 1
                            $ efren_highisland_blocked = 1
                            $ thyrsus_highisland_blocked = 1
                            $ pyrrhos_highisland_blocked = 1
                            $ bandit_highisland_blocked = 1
                            $ tulia_highisland_blocked = 1
                            $ tzvi_highisland_blocked = 1
                            $ quintus_highisland_blocked = 1
                            $ custom1 = "You run your eyes over your crew, wounded and exhausted. You doubt they can go much further."
                            $ custom2 = ""
                        nvl clear
                        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                        menu:
                            'You wipe the sweat and tears from your lips. The dark-furred, warm carcass is heavier than your entire group and as tall as a palisade, with arms large enough to tear a human apart. It’s laying on its back, in a puddle of blood - not all of which belongs to it. [custom1][custom2]
                            \n\nYou stretch your back and let out a moan. The songs of birds and monkeys, distracting from the distant roars, are almost soothing.
                            '
                            '“We can’t stay here. Let’s move on.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We can’t stay here. Let’s move on.”')
                                $ highisland_destination = "beastfolk"
                                jump highisland_destination
                    else:
                        if armor == 4:
                            $ armor = limit_armor(armor-3)
                            show minus3armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 armor points.{/i}')
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        elif armor == 3 and pc_hp >= 1:
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
                        elif armor == 2 and pc_hp >= 1:
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
                        elif armor == 1 and pc_hp >= 2:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ pc_hp = limit_pc_hp(pc_hp-3)
                            show minus3hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        elif pc_hp >= 3:
                            $ pc_hp = limit_pc_hp(pc_hp-4)
                            show minus4hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        else:
                            $ custom1 = "The dark-furred beast, heavier than your entire group and as tall as a palisade, comes out of the tunnel of leaves, ignoring anything you throw at it, and reaches for the nearest shell. The troll lifts them up, then tears them in half before they make as much as a scream.\n\nThe rest of your exhausted group scatters in panic, and the monster chases after you, with each of its steps covering as much as a few of your desperate leaps."
                            jump highisland_gameover
                        if highisland_crew_left >= 4:
                            label highisland_companionexhaustion_loop_trolltunnel4c:
                                $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus'])
                                if highisland_crew_dmg_target == "aegidia":
                                    if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4c
                                    else:
                                        if not aegidia_highisland_tired:
                                            $ aegidia_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ aegidia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "dalit":
                                    if not dalit_highisland_joined or dalit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4c
                                    else:
                                        if not dalit_highisland_tired:
                                            $ dalit_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Dalit{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ dalit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Dalit{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "efren":
                                    if not efren_highisland_joined or efren_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4c
                                    else:
                                        if not efren_highisland_tired:
                                            $ efren_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Efren{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ efren_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Efren{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "thyrsus":
                                    if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4c
                                    else:
                                        if not thyrsus_highisland_tired:
                                            $ thyrsus_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Thyrsus{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ thyrsus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Thyrsus{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "pyrrhos":
                                    if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4c
                                    else:
                                        if not pyrrhos_highisland_tired:
                                            $ pyrrhos_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ pyrrhos_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "bandit":
                                    if not bandit_highisland_joined or bandit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4c
                                    else:
                                        if not bandit_highisland_tired:
                                            $ bandit_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}The bandit{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ bandit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}The bandit{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "tulia":
                                    if not tulia_highisland_joined or tulia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4c
                                    else:
                                        if not tulia_highisland_tired:
                                            $ tulia_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Tulia{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ tulia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Tulia{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "tzvi":
                                    if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4c
                                    else:
                                        if not tzvi_highisland_tired:
                                            $ tzvi_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ tzvi_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} got severely wounded."
                                elif highisland_crew_dmg_target == "quintus":
                                    if not quintus_highisland_joined or quintus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4c
                                    else:
                                        if not quintus_highisland_tired:
                                            $ quintus_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Quintus{/color} got hit pretty badly, but is still standing."
                                        else:
                                            $ quintus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Quintus{/color} got severely wounded."
                            label highisland_companionexhaustion_loop_trolltunnel4cb:
                                $ highisland_crew_dmg_target2 = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus'])
                                if highisland_crew_dmg_target2 == highisland_crew_dmg_target:
                                    jump highisland_companionexhaustion_loop_trolltunnel4cb
                                if highisland_crew_dmg_target2 == "aegidia":
                                    if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cb
                                    else:
                                        if not aegidia_highisland_tired:
                                            $ aegidia_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Aegidia{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ aegidia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Aegidia{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "dalit":
                                    if not dalit_highisland_joined or dalit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cb
                                    else:
                                        if not dalit_highisland_tired:
                                            $ dalit_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Dalit{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ dalit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Dalit{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "efren":
                                    if not efren_highisland_joined or efren_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cb
                                    else:
                                        if not efren_highisland_tired:
                                            $ efren_highisland_tired = 1
                                            $ custom2 = "{color=#f6d6bd}Efren{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ efren_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Efren{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "thyrsus":
                                    if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cb
                                    else:
                                        if not thyrsus_highisland_tired:
                                            $ thyrsus_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Thyrsus{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ thyrsus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Thyrsus{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "pyrrhos":
                                    if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cb
                                    else:
                                        if not pyrrhos_highisland_tired:
                                            $ pyrrhos_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Pyrrhos{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ pyrrhos_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Pyrrhos{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "bandit":
                                    if not bandit_highisland_joined or bandit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cb
                                    else:
                                        if not bandit_highisland_tired:
                                            $ bandit_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}The bandit{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ bandit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}The bandit{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "tulia":
                                    if not tulia_highisland_joined or tulia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cb
                                    else:
                                        if not tulia_highisland_tired:
                                            $ tulia_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Tulia{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ tulia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Tulia{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "tzvi":
                                    if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cb
                                    else:
                                        if not tzvi_highisland_tired:
                                            $ tzvi_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Tzvi{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ tzvi_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Tzvi{/color} is barely standing."
                                elif highisland_crew_dmg_target2 == "quintus":
                                    if not quintus_highisland_joined or quintus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cb
                                    else:
                                        if not quintus_highisland_tired:
                                            $ quintus_highisland_tired = 1
                                            $ custom2 = " {color=#f6d6bd}Quintus{/color} is exhausted, but tries to hide it."
                                        else:
                                            $ quintus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom2 = " {color=#f6d6bd}Quintus{/color} is barely standing."
                            label highisland_companionexhaustion_loop_trolltunnel4cc:
                                $ highisland_crew_dmg_target3 = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus'])
                                if highisland_crew_dmg_target3 == highisland_crew_dmg_target or highisland_crew_dmg_target3 == highisland_crew_dmg_target2:
                                    jump highisland_companionexhaustion_loop_trolltunnel4cc
                                if highisland_crew_dmg_target3 == "aegidia":
                                    if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cc
                                    else:
                                        if not aegidia_highisland_tired:
                                            $ aegidia_highisland_tired = 1
                                            $ custom3 = " {color=#f6d6bd}Aegidia{/color} holds her forehead, trying to calm down."
                                        else:
                                            $ aegidia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom3 = " {color=#f6d6bd}Aegidia{/color} is in even worse shape."
                                elif highisland_crew_dmg_target3 == "dalit":
                                    if not dalit_highisland_joined or dalit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cc
                                    else:
                                        if not dalit_highisland_tired:
                                            $ dalit_highisland_tired = 1
                                            $ custom3 = " {color=#f6d6bd}Dalit{/color} holds her forehead, trying to calm down."
                                        else:
                                            $ dalit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom3 = " {color=#f6d6bd}Dalit{/color} is in even worse shape."
                                elif highisland_crew_dmg_target3 == "efren":
                                    if not efren_highisland_joined or efren_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cc
                                    else:
                                        if not efren_highisland_tired:
                                            $ efren_highisland_tired = 1
                                            $ custom3 = "{color=#f6d6bd}Efren{/color} holds his forehead, trying to calm down."
                                        else:
                                            $ efren_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom3 = " {color=#f6d6bd}Efren{/color} is in even worse shape."
                                elif highisland_crew_dmg_target3 == "thyrsus":
                                    if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cc
                                    else:
                                        if not thyrsus_highisland_tired:
                                            $ thyrsus_highisland_tired = 1
                                            $ custom3 = " {color=#f6d6bd}Thyrsus{/color} holds his forehead, trying to calm down."
                                        else:
                                            $ thyrsus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom3 = " {color=#f6d6bd}Thyrsus{/color} is in even worse shape."
                                elif highisland_crew_dmg_target3 == "pyrrhos":
                                    if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cc
                                    else:
                                        if not pyrrhos_highisland_tired:
                                            $ pyrrhos_highisland_tired = 1
                                            $ custom3 = " {color=#f6d6bd}Pyrrhos{/color} holds his forehead, trying to calm down."
                                        else:
                                            $ pyrrhos_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom3 = " {color=#f6d6bd}Pyrrhos{/color} is in even worse shape."
                                elif highisland_crew_dmg_target3 == "bandit":
                                    if not bandit_highisland_joined or bandit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cc
                                    else:
                                        if not bandit_highisland_tired:
                                            $ bandit_highisland_tired = 1
                                            $ custom3 = " {color=#f6d6bd}The bandit{/color} holds his forehead, trying to calm down."
                                        else:
                                            $ bandit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom3 = " {color=#f6d6bd}The bandit{/color} is in even worse shape."
                                elif highisland_crew_dmg_target3 == "tulia":
                                    if not tulia_highisland_joined or tulia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cc
                                    else:
                                        if not tulia_highisland_tired:
                                            $ tulia_highisland_tired = 1
                                            $ custom3 = " {color=#f6d6bd}Tulia{/color} holds her forehead, trying to calm down."
                                        else:
                                            $ tulia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom3 = " {color=#f6d6bd}Tulia{/color} is in even worse shape."
                                elif highisland_crew_dmg_target3 == "tzvi":
                                    if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cc
                                    else:
                                        if not tzvi_highisland_tired:
                                            $ tzvi_highisland_tired = 1
                                            $ custom3 = " {color=#f6d6bd}Tzvi{/color} holds his forehead, trying to calm down."
                                        else:
                                            $ tzvi_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom3 = " {color=#f6d6bd}Tzvi{/color} is in even worse shape."
                                elif highisland_crew_dmg_target3 == "quintus":
                                    if not quintus_highisland_joined or quintus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_trolltunnel4cc
                                    else:
                                        if not quintus_highisland_tired:
                                            $ quintus_highisland_tired = 1
                                            $ custom3 = " {color=#f6d6bd}Quintus{/color} holds his forehead, trying to calm down."
                                        else:
                                            $ quintus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom3 = " {color=#f6d6bd}Quintus{/color} is in even worse shape."
                        else:
                            $ aegidia_highisland_blocked = 1
                            $ dalit_highisland_blocked = 1
                            $ efren_highisland_blocked = 1
                            $ thyrsus_highisland_blocked = 1
                            $ pyrrhos_highisland_blocked = 1
                            $ bandit_highisland_blocked = 1
                            $ tulia_highisland_blocked = 1
                            $ tzvi_highisland_blocked = 1
                            $ quintus_highisland_blocked = 1
                            $ custom1 = "You run your eyes over your crew, wounded and exhausted. You doubt they can go much further."
                            $ custom2 = ""
                            $ custom3 = ""
                        nvl clear
                        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
                        menu:
                            'You wipe the sweat and tears from your lips. The dark-furred, warm carcass is heavier than your entire group and as tall as a palisade, with arms large enough to tear a human apart. It’s laying on its back, in a puddle of blood - not all of which belongs to it. [custom1][custom2][custom3]
                            \n\nYou stretch your back and let out a moan. The songs of birds and monkeys, distracting from the distant roars, are almost soothing.
                            '
                            '“We can’t stay here. Let’s move on.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We can’t stay here. Let’s move on.”')
                                $ highisland_destination = "beastfolk"
                                jump highisland_destination

label highisland_beastfolkALL:
    label highisland_solo_beastfolkALL:
        label highisland_solo_beastfolk01:
            if highisland_trolltunnel_trollmet:
                $ custom1 = ""
            else:
                $ custom1 = "The narrow, twisted path takes you to a creek, then down the human-carved tunnel leading through a rocky hill.\n\n"
            menu:
                '[custom1]The closer you are to the volcano, the more signs of humans you find - the abandoned tools, the overgrown fences and fire holes, the fruit trees and trimmed, centuries-old oaks. The ribbon of smoke hides the stars behind it, though you still can’t smell it.
                \n\nThe mountain’s upper half is black-and-gray from cold lava and ashes, while the lower half is mostly green, with short, but lush trees and thriving flowers bathing in the moonlight.
                \n\nYou see the shape of an open gate at the end of the road.
                '
                'This is it. The path to the volcano.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- This is it. The path to the volcano.')
                    show areapicture hi_beastfolk2 at basicfade
                    menu:
                        'The stone posts are dark from dust, but as good as new, even though the crooked planks of the wooden leaves are beyond restoration. Seeing nothing on the top of the wall, you enter the partially buried ruins, with humble buildings sticking out from the layers spit out by the volcano.
                        \n\nIt takes only a few breaths before the first enemy jumps on the road from the roof of a ruined hut. It’s a head shorter than you and walks on its hind legs, but has the head of a raccoon, though its ears are too small, the fangs too long, and the eyes resemble those of an ape. Despite its human-like posture, it leans slightly forward, with arms curled up. It has no tail, and keeps sniffing, as if it barely sees you.
                        \n\nYou consider starting the clash, but then its boar-headed companion shows up, with two sets of remarkable tusks and bristles instead of puffy fur. Then they’re joined by two long-tailed ratfolks, and a foxfolk, and a lizardfolk...
                        '
                        'I look for the leader of their pack.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for the leader of their pack.')
                            $ highisland_beastfolk_feeding_foodestimation += (item_rations*3)
                            $ highisland_beastfolk_feeding_foodestimation += (item_chicken*5)
                            $ highisland_beastfolk_feeding_foodestimation += (item_wildplants*1)
                            $ highisland_beastfolk_feeding_foodestimation += (item_stoat*3)
                            $ highisland_beastfolk_feeding_foodestimation += (item_rawfishtotalnumber*2)
                            $ highisland_beastfolk_feeding_foodestimation += (item_cookedfish*3)
                            $ highisland_beastfolk_feeding_foodestimation += (item_beholderroot*10)
                            if highisland_beastfolk_feeding_foodestimation <= 0:
                                $ custom1 = "However, you’ve got no food that could convince them to leave you alone."
                            elif highisland_beastfolk_feeding_foodestimation < highisland_beastfolk_feeding_threshhold1:
                                $ custom1 = "You’ve got some food that you could offer to the creatures, but seeing their numbers, you doubt they’re going to accept such a humble offering."
                            elif highisland_beastfolk_feeding_foodestimation < highisland_beastfolk_feeding_threshhold2:
                                $ custom1 = "You’ve got some food that you could offer to the creatures, but it’s not enough to fill this many stomachs."
                            elif highisland_beastfolk_feeding_foodestimation < highisland_beastfolk_feeding_threshhold4:
                                $ highisland_beastfolk_feeding_foodestimation_success = 1
                                $ custom1 = "You’ve got some food that you could offer to the creatures, but it’s not enough to fill this many stomachs. However, you {i}could{/i} try to get through them once they’re distracted."
                            else:
                                $ highisland_beastfolk_feeding_foodestimation_success = 1
                                $ custom1 = "You’ve got some food that you could offer to the creatures. Maybe even enough to fill their stomachs."
                            menu:
                                'The tallest one of them all is the beast with deer antlers. It steps forward and crouches down, touching the ground with an open palm. It doesn’t make a sound, just pierces you with its almost-human eyes. Its pack blocks the twisty path forward that is carved in the mountainside, narrow and completely open from one side.
                                \n\nYou think of the tales taught to all children in The Dragonwoods. The beastfolk may be destructive, but if not threatened, they’re willing to “trade”. [custom1]
                                '
                                'I observe them more closely.' if highisland_beastfolk_feeding_foodestimation_success:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe them more closely.')
                                    if not shortcut_easternentrance_gnolls:
                                        $ custom1 = "They wear no clothes and carry no tools or weapons. You can’t tell if they’re hungry, muscular, healthy - their shapes resemble no creature you’ve seen before."
                                    else:
                                        $ custom1 = "They wear no clothes and carry no tools or weapons. You can’t tell if they’re hungry, muscular, healthy - their shapes resemble no creature you’ve seen before, other than gnolls."
                                    jump highisland_solo_beastfolk01a
                                'I should seek another path and save my supplies.' if highisland_beastfolk_feeding_foodestimation_success:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should seek another path and save my supplies.')
                                    $ highisland_destination = "climbingmountain"
                                    jump highisland_destination
                                'Having no food, I should seek another path.' if not highisland_beastfolk_feeding_foodestimation_success:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Having no food, I should seek another path.')
                                    $ highisland_destination = "climbingmountain"
                                    jump highisland_destination

        label highisland_solo_beastfolk01a:
            $ at = 0
            $ at_unlock_spell = 0
            if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold4:
                $ at = 0
                if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                    $ highisland_beastfolk_feeding_root_description = 1
                    $ custom1 = "The “boar” picks up your offering with its hands, and after it sniffs it, it raises its head, lets out a triumphant grunt, and bites off a bit of the root. Its curious companions approach it quickly, sharing the stinking snack between them. The smallest one among them, the “squirrel”, gets nothing.\n\nAfter the “boar” squeals loudly, its pack spreads, clearing the path for you. While they curiously observe you, they keep their distance."
                else:
                    $ custom1 = "The “boar” warns the others to stay away with a grunt, then, placing heavy steps and swinging its arms, it grabs a large share of your offering. It throws you a warning look, but then squeals loudly, and its pack spreads, clearing the path for you. While they curiously observe you, they keep their distance."
                menu:
                    '[custom1]
                    '
                    'Disgusting creatures.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Disgusting creatures.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
                    'I wonder where they learned this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder where they learned this.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
                    'It’s all starting to feel a bit like a dream.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s all starting to feel a bit like a dream.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
            else:
                if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold1 and not highisland_beastfolk_feeding_threshhold1descrip:
                    $ highisland_beastfolk_feeding_threshhold1descrip = 1
                    if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                        $ highisland_beastfolk_feeding_root_description = 1
                        $ custom1 = "The “deer” picks up your offering with its hands, and after it sniffs it, it raises its head, lets out a triumphant call, and bites off a bit of the root. Its curious companions approach it quickly, sharing the stinking snack between them.\n\nThe smallest one among them, the “squirrel”, gets nothing."
                    else:
                        $ custom1 = "The “deer” steps closer and eagerly picks up your offering with its hands, then turns around, as if you’re not a threat. It then sits down at the threshold of one of the ruined buildings and starts to chew your gifts."
                elif highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold2 and not highisland_beastfolk_feeding_threshhold2descrip:
                    $ highisland_beastfolk_feeding_threshhold2descrip = 1
                    if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                        $ highisland_beastfolk_feeding_root_description = 1
                        $ custom1 = "One of the “rats” picks up your offering with its hands, and after it sniffs it, it makes a cheerful jump, grinds its teeth, and bites off a bit of the root. Its curious companions approach it quickly, sharing the stinking snack between them.\n\nThe smallest one among them, the “squirrel”, gets nothing."
                    else:
                        $ custom1 = "The “rats” leap forward, grab the food with their teeth, then run as if they’re in a panic. They disappear behind a rock, chased by the “lizard”."
                elif highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold3 and not highisland_beastfolk_feeding_threshhold3descrip:
                    $ highisland_beastfolk_feeding_threshhold3descrip = 1
                    if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                        $ highisland_beastfolk_feeding_root_description = 1
                        $ custom1 = "The “raccoon” picks up your offering with its hands, and after it sniffs it, it lets out a cheerful chitter and bites off a bit of the root, making a satisfied purr. Its curious companions approach it quickly, sharing the stinking snack between them.\n\nThe smallest one among them, the “squirrel”, gets nothing."
                    else:
                        $ custom1 = "The “raccoon” steps away, then runs ahead, grabbing the offering in the middle of a step, and turns around, tearing away and spreading parts of your meal among the others."
                elif custom1 == "donation":
                    $ custom1 = "They’re waiting for more."
                if pc_class == "mage" and highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold2 and highisland_beastfolk_feeding_points < highisland_beastfolk_feeding_threshhold4:
                    $ at = 0
                    $ at_unlock_spell = 1
                    $ manacost = 3
                menu:
                    '[custom1]
                    '
                    'I’ll run for it, and use my wand to push away any pursuers. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll run for it, and use my wand to push away any pursuers.')
                        jump highisland_solo_beastfolk02spell
                    'I lack pneuma to use my wand. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and at_unlock_spell" ):
                        pass
                    'I offer them the root I took at the altar.' if item_beholderroot:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer them the root I took at the altar.')
                        $ item_beholderroot -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the weird root.{/i}')
                        $ highisland_beastfolk_feeding_root = 1
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 10
                        $ highisland_beastfolk_feeding_foodestimation += 10
                        jump highisland_solo_beastfolk01a
                    'I give them a food ration.' if item_rations:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a food ration.')
                        $ item_rations -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 3
                        $ highisland_beastfolk_feeding_foodestimation += 3
                        jump highisland_solo_beastfolk01a
                    'I give them a roast chicken.' if item_chicken:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a roast chicken.')
                        $ item_chicken -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 5
                        $ highisland_beastfolk_feeding_foodestimation += 5
                        jump highisland_solo_beastfolk01a
                    'I give them a bunch of wild plants.' if item_wildplants:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a bunch of wild plants.')
                        $ item_wildplants -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a bunch of wild plants.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 1
                        $ highisland_beastfolk_feeding_foodestimation += 1
                        jump highisland_solo_beastfolk01a
                    'I give them a raw fish.' if item_rawfishtotalnumber:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a raw fish.')
                        $ item_rawfishtotalnumber -= 1
                        $ item_rawfish_losing = 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You have %s fish left.{/i}' %item_rawfishtotalnumber)
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 2
                        $ highisland_beastfolk_feeding_foodestimation += 2
                        jump highisland_solo_beastfolk01a
                    'I give them a roast fish.' if item_cookedfish:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a roast fish.')
                        $ item_cookedfish -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 3
                        $ highisland_beastfolk_feeding_foodestimation += 3
                        jump highisland_solo_beastfolk01a
                    'I give them the stoat.' if item_stoat:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them the stoat.')
                        $ item_stoat = 0
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the stoat.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 3
                        $ highisland_beastfolk_feeding_foodestimation += 3
                        jump highisland_solo_beastfolk01a
                    '{image=d6} With a few of them gone, I could try to get through them.' if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold2 and highisland_beastfolk_feeding_points < highisland_beastfolk_feeding_threshhold3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} With a few of them gone, I could try to get through them.')
                        $ highisland_beastfolk_attack_harshmodifier = 1
                        jump highisland_solo_beastfolk02
                    '{image=d6} With most of them gone, I could try to get on the other side.' if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} With most of them gone, I could try to get on the other side.')
                        jump highisland_solo_beastfolk02
                    'I’ll keep the rest of my supplies for myself. I seek another path.' if highisland_beastfolk_feeding_foodestimation >= 1 and highisland_beastfolk_feeding_points >= 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll keep the rest of my supplies for myself. I seek another path.')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination
                    'I’ll keep my supplies for myself. I seek another path.' if highisland_beastfolk_feeding_foodestimation >= 1 and highisland_beastfolk_feeding_points <= 0:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll keep my supplies for myself. I seek another path.')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination
                    'I’ve got nothing else to give them. I’ll try another path.' if highisland_beastfolk_feeding_foodestimation <= 0 and highisland_beastfolk_feeding_points >= 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve got nothing else to give them. I’ll try another path.')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination
                    'I’ve got nothing to give them. I’ll try another path.' if highisland_beastfolk_feeding_foodestimation <= 0 and highisland_beastfolk_feeding_points <= 0:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve got nothing to give them. I’ll try another path.')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination

        label highisland_solo_beastfolk02:
            $ at = 0
            $ at_unlock_spell = 0
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
                $ d100roll -= 20
            elif item_axe02 or item_axe02alt:
                $ d100roll -= 10
            if item_shield:
                $ d100roll -= 5
            $ pc_battlecounter += 1
            $ highisland_beastfolk_attack_harshmodifier += 25
            if d100roll <= 40:
                menu:
                    'Knowing you can’t defeat them, you put every breath into your legs, heading up the path. The beasts, more surprised than anything, step away, and while the “boar” tries to chase after you, the others stay idle. Soon, you leave the ruins behind.
                    '
                    'Let’s hope there’s another path down.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope there’s another path down.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
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
                    if not cleanliness_clothes_blood:
                        $ cleanliness_clothes_blood = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                else:
                    $ custom1 = "Knowing you can’t defeat them, you put every breath into your legs, heading up the path. The beasts, more surprised than anything, step away, but the “boar” doesn’t need time to think - it chases after you and slams into the bags on your back, breaking your spine and sending you over a nearby ledge."
                    jump highisland_gameover
                menu:
                    'Knowing you can’t defeat them, you put every breath into your legs, heading up the path. The beasts, more surprised than anything, step away, but the “boar” doesn’t need time to think - it chases after you and slams into the bags on your back on your back, sending you over a nearby ledge.
                    \n\nYou crash into the ground, but once you get up, you realize the other beastfolk keep their distance, giving you grim looks. You crawl away, get up, and realize that the “deer” is holding their tusked companion by its scruff, keeping you safe.
                    \n\nYou spot a gap in the wall and run for your life.
                    '
                    'I seek another entrance.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I seek another entrance')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination

        label highisland_solo_beastfolk02spell:
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
            $ at = 0
            $ at_unlock_spell = 0
            menu:
                'You take a deep breath and run up the path. The beasts, more surprised than anything, step away, and once the “boar” starts to chase after you, you point at it with your wand. While the wave of pneuma doesn’t seem to impact the beast, it lets out a shocked squeal and covers its snout.
                \n\nSoon, you leave the ruins behind.
                '
                'Let’s hope there’s another path down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope there’s another path down.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination

    label highisland_howlers_beastfolkALL:
        label highisland_howlers_beastfolk01:
            if highisland_trolltunnel_trollmet:
                $ custom1 = ""
            else:
                $ custom1 = "The narrow, twisted path takes you to a creek, then down the human-carved tunnel leading through a rocky hill.\n\n"
            menu:
                '[custom1]The closer you are to the volcano, the more signs of humans you find - the abandoned tools, the overgrown fences and fire holes, the fruit trees and trimmed, centuries-old oaks. The ribbon of smoke hides the stars behind it, though you still can’t smell it.
                \n\nThe mountain’s upper half is black-and-gray from cold lava and ashes, while the lower half is mostly green, with short, but lush trees and thriving flowers bathing in the moonlight.
                \n\nYou see the shape of an open gate at the end of the road.
                '
                '“This is it. The path to the volcano.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This is it. The path to the volcano.”')
                    show areapicture hi_beastfolk2 at basicfade
                    menu:
                        'The stone posts are dark from dust, but as good as new, even though the crooked planks of the wooden leaves are beyond restoration. Seeing nothing on the top of the wall, you enter the partially buried ruins, with humble buildings sticking out from the layers spit out by the volcano.
                        \n\nIt takes only a few breaths before the first enemy jumps on the road from the roof of a ruined hut, and {color=#f6d6bd}the guards{/color} prepare their weapons. It’s a head shorter than you and walks on its hind legs, but has the head of a raccoon, though its ears are too small, the fangs too long, and the eyes resemble those of an ape. Despite its human-like posture, it leans slightly forward, with arms curled up. It has no tail, and keeps sniffing, as if it barely sees you.
                        \n\n“Do we...” starts {color=#f6d6bd}the one with the bow{/color}, but doesn’t continue as she observes the newly arrived boar-headed beast, with two sets of remarkable tusks and bristles instead of puffy fur. Then they’re joined by two long-tailed ratfolks, and a foxfolk, and a lizardfolk...
                        '
                        'I gesture for {color=#f6d6bd}the guards{/color} to stay calm.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gesture for {color=#f6d6bd}the guards{/color} to stay calm.')
                            $ highisland_beastfolk_feeding_foodestimation += (item_rations*3)
                            $ highisland_beastfolk_feeding_foodestimation += (item_chicken*5)
                            $ highisland_beastfolk_feeding_foodestimation += (item_wildplants*1)
                            $ highisland_beastfolk_feeding_foodestimation += (item_stoat*3)
                            $ highisland_beastfolk_feeding_foodestimation += (item_rawfishtotalnumber*2)
                            $ highisland_beastfolk_feeding_foodestimation += (item_cookedfish*3)
                            $ highisland_beastfolk_feeding_foodestimation += (item_beholderroot*10)
                            if highisland_howlersguards_hp >= 10:
                                $ highisland_beastfolk_howlersguards_tier = 3
                            elif highisland_howlersguards_hp >= 7:
                                $ highisland_beastfolk_howlersguards_tier = 2
                            elif highisland_howlersguards_hp >= 4:
                                $ highisland_beastfolk_howlersguards_tier = 1
                            if highisland_beastfolk_feeding_foodestimation <= 0:
                                $ custom1 = "However, you’ve got no food that could convince them to leave you alone."
                                $ custom2 = "\n\n{color=#f6d6bd}The leader of the guards{/color} starts to whisper. “We can ne fight all of them at once.”"
                            elif highisland_beastfolk_feeding_foodestimation < highisland_beastfolk_feeding_threshhold1:
                                $ custom1 = "You’ve got some food that you could offer to the creatures, but seeing their numbers, you doubt they’re going to accept such a humble offering."
                                $ custom2 = "\n\n{color=#f6d6bd}The leader of the guards{/color} starts to whisper. “We can ne fight all of them at once.”"
                            elif highisland_beastfolk_feeding_foodestimation < highisland_beastfolk_feeding_threshhold2:
                                $ custom1 = "You’ve got some food that you could offer to the creatures, but it’s not enough to fill this many stomachs."
                                if highisland_beastfolk_howlersguards_tier >= 3:
                                    $ highisland_beastfolk_feeding_foodestimation_success = 1
                                    $ custom2 = "\n\n{color=#f6d6bd}The leader of the guards{/color} starts to whisper. “If you distract some of them with offerings, we’ll get us through.”"
                                else:
                                    $ custom2 = "\n\n{color=#f6d6bd}The leader of the guards{/color} starts to whisper. “We’re too weak.”"
                            elif highisland_beastfolk_feeding_foodestimation < highisland_beastfolk_feeding_threshhold3:
                                $ highisland_beastfolk_feeding_foodestimation_success = 1
                                $ custom1 = "You’ve got some food that you could offer to the creatures, but it’s not enough to fill this many stomachs."
                                if highisland_beastfolk_howlersguards_tier >= 1:
                                    $ highisland_beastfolk_feeding_foodestimation_success = 1
                                    $ custom2 = "\n\n{color=#f6d6bd}The leader of the guards{/color} starts to whisper. “If you distract some of them with offerings, we’ll get us through.”"
                                else:
                                    $ custom2 = "\n\n{color=#f6d6bd}The leader of the guards{/color} starts to whisper. “We’re too weak.”"
                            elif highisland_beastfolk_feeding_foodestimation < highisland_beastfolk_feeding_threshhold4:
                                $ highisland_beastfolk_feeding_foodestimation_success = 1
                                $ custom1 = "You’ve got some food that you could offer to the creatures, but it’s not enough to fill this many stomachs."
                                if highisland_beastfolk_howlersguards_tier >= 1:
                                    $ highisland_beastfolk_feeding_foodestimation_success = 1
                                    $ custom2 = "\n\n{color=#f6d6bd}The leader of the guards{/color} starts to whisper. “If you distract some of them with offerings, we’ll get us through.”"
                                else:
                                    $ custom2 = "\n\n{color=#f6d6bd}The leader of the guards{/color} starts to whisper. “We’re too weak.”"
                            else:
                                $ highisland_beastfolk_feeding_foodestimation_success = 1
                                $ custom1 = "You’ve got plenty of food that you could offer to the creatures. Maybe even enough to fill their stomachs."
                                if highisland_beastfolk_howlersguards_tier >= 1:
                                    $ custom2 = "\n\n{color=#f6d6bd}The leader of the guards{/color} starts to whisper. “If you distract some of them with offerings, we’ll get us through.”"
                                else:
                                    $ custom2 = "\n\n{color=#f6d6bd}The leader of the guards{/color} starts to whisper. “We’re too weak.”"
                            menu:
                                'The tallest beast of them all has a pair of deer antlers. It steps forward and crouches down, touching the ground with an open palm. It doesn’t make a sound, just pierces you with its almost-human eyes. Its pack blocks the twisty path forward that is carved in the mountainside, narrow and completely open from one side.
                                \n\nYou think of the tales taught to all children in The Dragonwoods. The beastfolk may be destructive, but if not threatened, they’re willing to “trade”. [custom1][custom2]
                                '
                                'I observe them more closely.' if highisland_beastfolk_feeding_foodestimation_success:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe them more closely.')
                                    if not shortcut_easternentrance_gnolls:
                                        $ custom1 = "They wear no clothes and carry no tools or weapons. You can’t tell if they’re hungry, muscular, healthy - their shapes resemble no creature you’ve seen before."
                                    else:
                                        $ custom1 = "They wear no clothes and carry no tools or weapons. You can’t tell if they’re hungry, muscular, healthy - their shapes resemble no creature you’ve seen before, other than gnolls."
                                    jump highisland_howlers_beastfolk01a
                                '“Let’s seek another path.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s seek another path.”')
                                    $ highisland_destination = "climbingmountain"
                                    jump highisland_destination

        label highisland_howlers_beastfolk01a:
            $ at_unlock_spell = 0
            $ at = 0
            if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold4:
                if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                    $ highisland_beastfolk_feeding_root_description = 1
                    $ custom1 = "The “boar” picks up your offering with its hands, and after it sniffs it, it raises its head, lets out a triumphant grunt, and bites off a bit of the root. Its curious companions approach it quickly, sharing the stinking snack between them. The smallest one among them, the “squirrel”, gets nothing.\n\nAfter the “boar” squeals loudly, its pack spreads, clearing the path for you. While they curiously observe you, they keep their distance."
                else:
                    $ custom1 = "The “boar” warns the others to stay away with a grunt, then, placing heavy steps and swinging its arms, it grabs a large share of your offering. It throws you a warning look, but then squeals loudly, and its pack spreads, clearing the path for you. While they curiously observe you, they keep their distance."
                menu:
                    '[custom1]
                    '
                    'Disgusting creatures.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Disgusting creatures.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
                    'I wonder where they learned this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder where they learned this.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
                    'All of this is starting to feel a bit like a dream.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- All of this is starting to feel a bit like a dream.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
            elif highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold3 and highisland_beastfolk_howlersguards_tier >= 1:
                if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                    $ highisland_beastfolk_feeding_root_description = 1
                    $ custom1 = "The “raccoon” picks up your offering with its hands, and after it sniffs it, it lets out a cheerful chitter and bites off a bit of the root, making a satisfied purr. Its curious companions approach it quickly, sharing the stinking snack between them.\n\nThe smallest one among them, the “squirrel”, gets nothing."
                else:
                    $ custom1 = "The “raccoon” steps away, then runs ahead, grabbing the offering in the middle of a step, and turns around, tearing away and spreading parts of your meal among the others."
                menu:
                    '[custom1]
                    \n\n“Now!” shouts {color=#f6d6bd}the leader{/color} as he pushes your shoulder. Your entire group heads up the path, kicking away the surprised beasts and, in a few instances, cutting their skin. A group led by the “boar” tries to chase after you, but once {color=#f6d6bd}the young druid{/color} sends a cloud of dust in their direction, and your blades stop the last few pursuers. Soon, you leave the ruins behind.
                    '
                    'Let’s hope there’s another path down.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope there’s another path down.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
            elif highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold2 and highisland_beastfolk_howlersguards_tier >= 2:
                if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                    $ highisland_beastfolk_feeding_root_description = 1
                    $ custom1 = "One of the “rats” picks up your offering with its hands, and after it sniffs it, it makes a cheerful jump, grinds its teeth, and bites off a bit of the root. Its curious companions approach it quickly, sharing the stinking snack between them. The smallest one among them, the “squirrel”, gets nothing."
                else:
                    $ custom1 = "The “rats” leap forward, grab the food with their teeth, then run as if they’re in a panic. They disappear behind a rock, chased by the “lizard”."
                menu:
                    '[custom1]
                    \n\n“Now!” shouts {color=#f6d6bd}the leader{/color} as he pushes your shoulder. Your entire group heads up the path, kicking away the surprised beasts and, in a few instances, cutting their skin. A group led by the “boar” tries to chase after you, but once {color=#f6d6bd}the young druid{/color} sends a cloud of dust in their direction, and your blades stop the last few pursuers. Soon, you leave the ruins behind.
                    '
                    'Let’s hope there’s another path down.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope there’s another path down.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
            elif highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold1 and highisland_beastfolk_howlersguards_tier >= 3:
                if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                    $ highisland_beastfolk_feeding_root_description = 1
                    $ custom1 = "The “deer” picks up your offering with its hands, and after it sniffs it, it raises its head, lets out a triumphant call, and bites off a bit of the root. Its curious companions approach it quickly, sharing the stinking snack between them. The smallest one among them, the “squirrel”, gets nothing."
                else:
                    $ custom1 = "The “deer” steps closer and eagerly picks up your offering with its hands, then turns around, as if you’re not a threat. It then sits down at the threshold of one of the ruined buildings and starts to chew your gifts."
                menu:
                    '[custom1]
                    \n\n“Now!” shouts {color=#f6d6bd}the leader{/color} as he pushes your shoulder. Your entire group heads up the path, kicking away the surprised beasts and, in a few instances, cutting their skin. A group led by the “boar” tries to chase after you, but once {color=#f6d6bd}the young druid{/color} sends a cloud of dust in their direction, and your blades stop the last few pursuers. Soon, you leave the ruins behind.
                    '
                    'Let’s hope there’s another path down.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope there’s another path down.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
            else:
                $ at = 0
                if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold1 and not highisland_beastfolk_feeding_threshhold1descrip:
                    $ highisland_beastfolk_feeding_threshhold1descrip = 1
                    if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                        $ highisland_beastfolk_feeding_root_description = 1
                        $ custom1 = "The “deer” picks up your offering with its hands, and after it sniffs it, it raises its head, lets out a triumphant call, and bites off a bit of the root. Its curious companions approach it quickly, sharing the stinking snack between them.\n\nThe smallest one among them, the “squirrel”, gets nothing."
                    else:
                        $ custom1 = "The “deer” steps closer and eagerly picks up your offering with its hands, then turns around, as if you’re not a threat. It then sits down at the threshold of one of the ruined buildings and starts to chew your gifts."
                elif highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold2 and not highisland_beastfolk_feeding_threshhold2descrip:
                    $ highisland_beastfolk_feeding_threshhold2descrip = 1
                    if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                        $ highisland_beastfolk_feeding_root_description = 1
                        $ custom1 = "One of the “rats” picks up your offering with its hands, and after it sniffs it, it makes a cheerful jump, grinds its teeth, and bites off a bit of the root. Its curious companions approach it quickly, sharing the stinking snack between them.\n\nThe smallest one among them, the “squirrel”, gets nothing."
                    else:
                        $ custom1 = "The “rats” leap forward, grab the food with their teeth, then run as if they’re in a panic. They disappear behind a rock, chased by the “lizard”."
                elif highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold3 and not highisland_beastfolk_feeding_threshhold3descrip:
                    $ highisland_beastfolk_feeding_threshhold3descrip = 1
                    if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                        $ highisland_beastfolk_feeding_root_description = 1
                        $ custom1 = "The “raccoon” picks up your offering with its hands, and after it sniffs it, it lets out a cheerful chitter and bites off a bit of the root, making a satisfied purr. Its curious companions approach it quickly, sharing the stinking snack between them.\n\nThe smallest one among them, the “squirrel”, gets nothing."
                    else:
                        $ custom1 = "The “raccoon” steps away, then runs ahead, grabbing the offering in the middle of a step, and turns around, tearing away and spreading parts of your meal among the others."
                elif custom1 == "donation":
                    $ custom1 = "They’re waiting for more."
                if pc_class == "mage" and highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold2 and highisland_beastfolk_feeding_points < highisland_beastfolk_feeding_threshhold4:
                    $ at = 0
                    $ at_unlock_spell = 1
                    $ manacost = 3
                menu:
                    '[custom1]
                    '
                    'I’ll run for it, and use my wand to push away any pursuers. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll run for it, and use my wand to push away any pursuers.')
                        jump highisland_solo_beastfolk02spell
                    'I lack pneuma to use my wand. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and at_unlock_spell" ):
                        pass
                    'I offer them the root I took at the altar.' if item_beholderroot:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer them the root I took at the altar.')
                        $ item_beholderroot -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the weird root.{/i}')
                        $ highisland_beastfolk_feeding_root = 1
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 10
                        $ highisland_beastfolk_feeding_foodestimation += 10
                        jump highisland_howlers_beastfolk01a
                    'I give them a food ration.' if item_rations:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a food ration.')
                        $ item_rations -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 3
                        $ highisland_beastfolk_feeding_foodestimation += 3
                        jump highisland_howlers_beastfolk01a
                    'I give them a roast chicken.' if item_chicken:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a roast chicken.')
                        $ item_chicken -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 5
                        $ highisland_beastfolk_feeding_foodestimation += 5
                        jump highisland_howlers_beastfolk01a
                    'I give them a bunch of wild plants.' if item_wildplants:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a bunch of wild plants.')
                        $ item_wildplants -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a bunch of wild plants.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 1
                        $ highisland_beastfolk_feeding_foodestimation += 1
                        jump highisland_howlers_beastfolk01a
                    'I give them a raw fish.' if item_rawfishtotalnumber:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a raw fish.')
                        $ item_rawfishtotalnumber -= 1
                        $ item_rawfish_losing = 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You have %s fish left.{/i}' %item_rawfishtotalnumber)
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 2
                        $ highisland_beastfolk_feeding_foodestimation += 2
                        jump highisland_howlers_beastfolk01a
                    'I give them a roast fish.' if item_cookedfish:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a roast fish.')
                        $ item_cookedfish -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 3
                        $ highisland_beastfolk_feeding_foodestimation += 3
                        jump highisland_howlers_beastfolk01a
                    'I give them the stoat.' if item_stoat:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them the stoat.')
                        $ item_stoat = 0
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the stoat.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 3
                        $ highisland_beastfolk_feeding_foodestimation += 3
                        jump highisland_howlers_beastfolk01a
                    'With a few of them gone, we can get through. “Run!”' if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- With a few of them gone, we can get through. “Run!”')
                        jump highisland_howlers_beastfolk02
                    'I’ll keep the rest of my supplies for myself. “Let’s look for another path.”' if highisland_beastfolk_feeding_foodestimation >= 1 and highisland_beastfolk_feeding_points >= 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll keep the rest of my supplies for myself. “Let’s look for another path.”')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination
                    'I’ll keep my supplies for myself. “Let’s look for another path.”' if highisland_beastfolk_feeding_foodestimation >= 1 and highisland_beastfolk_feeding_points <= 0:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll keep my supplies for myself. “Let’s look for another path.”')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination
                    'I’ve got nothing else to give them. “Let’s try another path.”' if highisland_beastfolk_feeding_foodestimation <= 0 and highisland_beastfolk_feeding_points >= 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve got nothing else to give them. “Let’s try another path.”')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination
                    'I’ve got nothing to give them. “Let’s try another path.”' if highisland_beastfolk_feeding_foodestimation <= 0 and highisland_beastfolk_feeding_points <= 0:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve got nothing to give them. “Let’s try another path.”')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination

        label highisland_howlers_beastfolk02:
            $ at = 0
            $ at_unlock_spell = 0
            $ highisland_howlersguards_hp -= 2
            $ highisland_howlersguards_spearwoman_dead = 1
            menu:
                '“Now!” You wave for the others to follow you up the path, then put every breath into your legs. The majority of the beasts, more surprised than anything, step away, but a group of the larger ones chases after you. {color=#f6d6bd}The young druid{/color} sends a cloud of dust in their direction, but {color=#f6d6bd}the one with the spear{/color}, already weakened, struggles to keep up with your pace.
                \n\nThe charging “boar” hits her in the back, sending her over a nearby ledge. You hear the scream, then the crash, but {color=#f6d6bd}the one with the mace{/color} is already pushing you forward. You can’t stop now.
                \n\nSoon, you leave the ruins behind.
                '
                'Let’s hope there’s another path down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope there’s another path down.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination

        label highisland_howlers_beastfolk02spell:
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
            $ at = 0
            $ at_unlock_spell = 0
            menu:
                '“Now!” You wave for the others to follow you up the path, then take a deep breath. The beasts, more surprised than anything, step away, and once the “boar” starts to chase after you, you point at it with your wand. While the wave of pneuma doesn’t seem to impact the beast, it lets out a shocked squeal and covers its snout. Then, {color=#f6d6bd}the young druid{/color} leaves a cloud of burning dust behind him, and you get away easily.
                '
                'Let’s hope there’s another path down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope there’s another path down.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination

    label highisland_crew_beastfolkALL:
        label highisland_crew_beastfolk01:
            if highisland_trolltunnel_trollmet:
                $ custom1 = ""
            else:
                $ custom1 = "The narrow, twisted path takes you to a creek, then down the human-carved tunnel leading through a rocky hill.\n\n"
            menu:
                '[custom1]The closer you are to the volcano, the more signs of humans you find - the abandoned tools, the overgrown fences and fire holes, the fruit trees and trimmed, centuries-old oaks. The ribbon of smoke hides the stars behind it, though you still can’t smell it.
                \n\nThe mountain’s upper half is black-and-gray from cold lava and ashes, while the lower half is mostly green, with short, but lush trees and thriving flowers bathing in the moonlight.
                \n\nYou see the shape of an open gate at the end of the road.
                '
                '“This is it. The path to the volcano.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This is it. The path to the volcano.”')
                    show areapicture hi_beastfolk2 at basicfade
                    if tzvi_highisland_joined:
                        $ custom11 = "“Don’t panic,” squeaks {color=#f6d6bd}Tzvi{/color}, hiding in his hood."
                    elif bandit_highisland_joined and not shortcut_darkforest_bandit_dead_troll:
                        $ custom11 = "“We can’t face them on their own ground,” grunts {color=#f6d6bd}the bandit{/color}."
                    elif aegidia_highisland_joined:
                        $ custom11 = "“Let’s be gentle, do ne startle them,” whispers {color=#f6d6bd}Aegidia{/color} with a trembling voice."
                    elif dalit_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Dalit{/color} keeps her crossbow ready, but you can hear her whisper. “Too many.”"
                    elif efren_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Efren{/color} lowers his head, but he can’t mimic the shape of the pack’s hybrid bodies."
                    elif thyrsus_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Thyrsus{/color} lets out a chuckle. “Now {i}that{/i} would be quite a battle.”"
                    elif pyrrhos_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Pyrrhos{/color} gets closer to the exit. For now, the path back is clear."
                    elif tulia_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Tulia{/color} stands between you and the beasts, with her sword ready."
                    elif quintus_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Quintus{/color} puts a hand on your shoulder, but as you glance at him, you notice his terrified eyes."
                    else:
                        $ custom11 = ""
                    menu:
                        'The stone posts are dark from dust, but as good as new, even though the crooked planks of the wooden leaves are beyond restoration. Seeing nothing on the top of the wall, you enter the partially buried ruins, with humble buildings sticking out from the layers spit out by the volcano.
                        \n\nIt takes only a few breaths before the first enemy jumps on the road from the roof of a ruined hut, and your crew prepares their weapons. It’s a head shorter than you and walks on its hind legs, but has the head of a raccoon, though its ears are too small, the fangs too long, and the eyes resemble those of an ape. Despite its human-like posture, it leans slightly forward, with arms curled up. It has no tail, and keeps sniffing, as if it barely sees you.
                        \n\nNext is the boar-headed beast, with two sets of remarkable tusks and bristles instead of puffy fur. Then they’re joined by two long-tailed ratfolks, and a foxfolk, and a lizardfolk... [custom11]
                        '
                        'I look for the leader of their pack.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for the leader of their pack.')
                            $ highisland_beastfolk_feeding_foodestimation += (item_rations*3)
                            $ highisland_beastfolk_feeding_foodestimation += (item_chicken*5)
                            $ highisland_beastfolk_feeding_foodestimation += (item_wildplants*1)
                            $ highisland_beastfolk_feeding_foodestimation += (item_stoat*3)
                            $ highisland_beastfolk_feeding_foodestimation += (item_rawfishtotalnumber*2)
                            $ highisland_beastfolk_feeding_foodestimation += (item_cookedfish*3)
                            $ highisland_beastfolk_feeding_foodestimation += (item_beholderroot*10)
                            if highisland_beastfolk_feeding_foodestimation <= 0:
                                $ custom1 = "However, you’ve got no food that could convince them to leave you alone."
                            elif highisland_beastfolk_feeding_foodestimation < highisland_beastfolk_feeding_threshhold1:
                                $ custom1 = "You’ve got some food that you could offer to the creatures, but seeing their numbers, you doubt they’re going to accept such a humble offering."
                            elif highisland_beastfolk_feeding_foodestimation < highisland_beastfolk_feeding_threshhold2:
                                if tzvi_highisland_joined and not tzvi_highisland_blocked:
                                    $ highisland_beastfolk_feeding_foodestimation_success = 1
                                    $ highisland_beastfolk_assassination_available = 1
                                    $ custom1 = "You’ve got some food that you could offer to the creatures, but it’s not enough to fill this many stomachs. {color=#f6d6bd}Tzvi{/color} gets closer and starts to whisper. “Make at least one of them go away, and I’ll clear the path for us.”"
                                else:
                                    $ custom1 = "You’ve got some food that you could offer to the creatures, but it’s not enough to fill this many stomachs."
                            elif highisland_beastfolk_feeding_foodestimation < highisland_beastfolk_feeding_threshhold4:
                                $ highisland_beastfolk_feeding_foodestimation_success = 1
                                if tzvi_highisland_joined and not tzvi_highisland_blocked:
                                    $ highisland_beastfolk_assassination_available = 1
                                    $ custom1 = "You’ve got some food that you could offer to the creatures, but it’s not enough to fill this many stomachs. However, you {i}could{/i} try to get through them once they get distracted. {color=#f6d6bd}Tzvi{/color} gets closer and starts to whisper. “Make at least one of them go away, and I’ll clear the path for us.”"
                                else:
                                    $ custom1 = "You’ve got some food that you could offer to the creatures, but it’s not enough to fill this many stomachs. However, you {i}could{/i} try to get through them once they get distracted."
                            else:
                                $ highisland_beastfolk_feeding_foodestimation_success = 1
                                if tzvi_highisland_joined and not tzvi_highisland_blocked:
                                    $ highisland_beastfolk_assassination_available = 1
                                    $ custom1 = "You’ve got some food that you could offer to the creatures. Maybe even enough to fill their stomachs. {color=#f6d6bd}Tzvi{/color} gets closer and starts to whisper. “Make at least one of them go away, and I’ll clear the path for us.”"
                                else:
                                    $ custom1 = "You’ve got some food that you could offer to the creatures. Maybe even enough to fill their stomachs."
                            menu:
                                'The tallest one of them all is the beast with deer antlers. It steps forward and crouches down, touching the ground with an open palm. It doesn’t make a sound, just pierces you with its almost-human eyes. Its pack blocks the twisty path forward that is carved in the mountainside, narrow and completely open from one side.
                                \n\nYou think of the tales taught to all children in The Dragonwoods. The beastfolk may be destructive, but if not threatened, they’re willing to “trade”. [custom1]
                                '
                                'I observe them more closely.' if highisland_beastfolk_feeding_foodestimation_success:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe them more closely.')
                                    if not shortcut_easternentrance_gnolls:
                                        $ custom1 = "They wear no clothes and carry no tools or weapons. You can’t tell if they’re hungry, muscular, healthy - their shapes resemble no creature you’ve seen before."
                                    else:
                                        $ custom1 = "They wear no clothes and carry no tools or weapons. You can’t tell if they’re hungry, muscular, healthy - their shapes resemble no creature you’ve seen before, other than gnolls."
                                    jump highisland_crew_beastfolk01a
                                '“Let’s seek another path and save our supplies.”' if highisland_beastfolk_feeding_foodestimation_success:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s seek another path and save our supplies.”')
                                    $ highisland_destination = "climbingmountain"
                                    jump highisland_destination
                                '“We’ve got no supplies. We should seek another path.”' if not highisland_beastfolk_feeding_foodestimation_success:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ve got no supplies. We should seek another path.”')
                                    $ highisland_destination = "climbingmountain"
                                    jump highisland_destination

        label highisland_crew_beastfolk01a:
            $ at_unlock_spell = 0
            $ at = 0
            if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold4:
                if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                    $ highisland_beastfolk_feeding_root_description = 1
                    $ custom1 = "The “boar” picks up your offering with its hands, and after it sniffs it, it raises its head, lets out a triumphant grunt, and bites off a bit of the root. Its curious companions approach it quickly, sharing the stinking snack between them. The smallest one among them, the “squirrel”, gets nothing.\n\nAfter the “boar” squeals loudly, its pack spreads, clearing the path for you. While they observe your group curiously, they keep their distance."
                else:
                    $ custom1 = "The “boar” warns the others to stay away with a grunt, then, placing heavy steps and swinging its arms, it grabs a large share of your offering. It throws you a warning look, but then squeals loudly, and its pack spreads, clearing the path for you. While they observe your group curiously, they keep their distance."
                menu:
                    '[custom1]
                    '
                    'Disgusting creatures.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Disgusting creatures.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
                    'I wonder where they learned this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder where they learned this.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
                    'It’s all starting to feel a bit like a dream.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s all starting to feel a bit like a dream.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
            else:
                $ at = 0
                if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold1 and not highisland_beastfolk_feeding_threshhold1descrip:
                    $ highisland_beastfolk_feeding_threshhold1descrip = 1
                    if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                        $ highisland_beastfolk_feeding_root_description = 1
                        $ custom1 = "The “deer” picks up your offering with its hands, and after it sniffs it, it raises its head, lets out a triumphant call, and bites off a bit of the root. Its curious companions approach it quickly, sharing the stinking snack between them.\n\nThe smallest one among them, the “squirrel”, gets nothing."
                    else:
                        $ custom1 = "The “deer” steps closer and eagerly picks up your offering with its hands, then turns around, as if you’re not a threat. It then sits down at the threshold of one of the ruined buildings and starts to chew your gifts."
                elif highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold2 and not highisland_beastfolk_feeding_threshhold2descrip:
                    $ highisland_beastfolk_feeding_threshhold2descrip = 1
                    if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                        $ highisland_beastfolk_feeding_root_description = 1
                        $ custom1 = "One of the “rats” picks up your offering with its hands, and after it sniffs it, it makes a cheerful jump, grinds its teeth, and bites off a bit of the root. Its curious companions approach it quickly, sharing the stinking snack between them.\n\nThe smallest one among them, the “squirrel”, gets nothing."
                    else:
                        $ custom1 = "The “rats” leap forward, grab the food with their teeth, then run as if they’re in a panic. They disappear behind a rock, chased by the “lizard”."
                elif highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold3 and not highisland_beastfolk_feeding_threshhold3descrip:
                    $ highisland_beastfolk_feeding_threshhold3descrip = 1
                    if highisland_beastfolk_feeding_root and not highisland_beastfolk_feeding_root_description:
                        $ highisland_beastfolk_feeding_root_description = 1
                        $ custom1 = "The “raccoon” picks up your offering with its hands, and after it sniffs it, it lets out a cheerful chitter and bites off a bit of the root, making a satisfied purr. Its curious companions approach it quickly, sharing the stinking snack between them.\n\nThe smallest one among them, the “squirrel”, gets nothing."
                    else:
                        $ custom1 = "The “raccoon” steps away, then runs ahead, grabbing the offering in the middle of a step, and turns around, tearing away and spreading parts of your meal among the others."
                elif custom1 == "donation":
                    $ custom1 = "They’re waiting for more."
                if pc_class == "mage" and highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold2 and highisland_beastfolk_feeding_points < highisland_beastfolk_feeding_threshhold4:
                    $ at = 0
                    $ at_unlock_spell = 1
                    $ manacost = 3
                menu:
                    '[custom1]
                    '
                    'I’ll run for it, and use my wand to push away any pursuers. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll run for it, and use my wand to push away any pursuers.')
                        jump highisland_solo_beastfolk02spell
                    'I lack pneuma to use my wand. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and at_unlock_spell" ):
                        pass
                    'I offer them the root I took at the altar.' if item_beholderroot:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer them the root I took at the altar.')
                        $ item_beholderroot -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the weird root.{/i}')
                        $ highisland_beastfolk_feeding_root = 1
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 10
                        $ highisland_beastfolk_feeding_foodestimation += 10
                        jump highisland_crew_beastfolk01a
                    'I give them a food ration.' if item_rations:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a food ration.')
                        $ item_rations -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 3
                        $ highisland_beastfolk_feeding_foodestimation += 3
                        jump highisland_crew_beastfolk01a
                    'I give them a roast chicken.' if item_chicken:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a roast chicken.')
                        $ item_chicken -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast chicken.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 5
                        $ highisland_beastfolk_feeding_foodestimation += 5
                        jump highisland_crew_beastfolk01a
                    'I give them a bunch of wild plants.' if item_wildplants:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a bunch of wild plants.')
                        $ item_wildplants -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a bunch of wild plants.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 1
                        $ highisland_beastfolk_feeding_foodestimation += 1
                        jump highisland_crew_beastfolk01a
                    'I give them a raw fish.' if item_rawfishtotalnumber:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a raw fish.')
                        $ item_rawfishtotalnumber -= 1
                        $ item_rawfish_losing = 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You have %s fish left.{/i}' %item_rawfishtotalnumber)
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 2
                        $ highisland_beastfolk_feeding_foodestimation += 2
                        jump highisland_crew_beastfolk01a
                    'I give them a roast fish.' if item_cookedfish:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them a roast fish.')
                        $ item_cookedfish -= 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a roast fish.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 3
                        $ highisland_beastfolk_feeding_foodestimation += 3
                        jump highisland_crew_beastfolk01a
                    'I give them the stoat.' if item_stoat:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give them the stoat.')
                        $ item_stoat = 0
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the stoat.{/i}')
                        $ custom1 = "donation"
                        $ highisland_beastfolk_feeding_points += 3
                        $ highisland_beastfolk_feeding_foodestimation += 3
                        jump highisland_crew_beastfolk01a
                    '“Thoughts, {color=#f6d6bd}Aegidia{/color}?”' if aegidia_highisland_joined and not aegidia_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thoughts, {color=#f6d6bd}Aegidia{/color}?”')
                        $ aegidia_highisland_opinion = 1
                        $ custom1 = "Her hands are shaking. “We should ne be here.”"
                        jump highisland_crew_beastfolk01a
                    '“What would you do, {color=#f6d6bd}Dalit{/color}?”' if dalit_highisland_joined and not dalit_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What would you do, {color=#f6d6bd}Dalit{/color}?”')
                        $ dalit_highisland_opinion = 1
                        $ custom1 = "“Uh, give them a heart of a dragon, some flesh made of pneuma?” She shrugs. “I know only tales.”"
                        jump highisland_crew_beastfolk01a
                    '“Any tips, {color=#f6d6bd}Efren{/color}?”' if efren_highisland_joined and not efren_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips, {color=#f6d6bd}Efren{/color}?”')
                        $ efren_highisland_opinion = 1
                        $ custom1 = "“There are no beastfolk in our woods,” he straightens up. “Are they even animals?”"
                        jump highisland_crew_beastfolk01a
                    '“{color=#f6d6bd}Thyrsus{/color}, suggestions?”' if thyrsus_highisland_joined and not thyrsus_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, suggestions?”')
                        $ thyrsus_highisland_opinion = 1
                        $ custom1 = "He looks through his amulets, then kicks away a pebble. One of the “rats” moves away. “I canna help you here.”"
                        jump highisland_crew_beastfolk01a
                    '“{color=#f6d6bd}Pyrrhos{/color}?”' if pyrrhos_highisland_joined and not pyrrhos_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pyrrhos{/color}?”')
                        $ pyrrhos_highisland_opinion = 1
                        $ custom1 = "“I met a pack like this before,” his voice is thoughtful. “They’ll take whatever, but it’s easier to make them go away with things they can’t find in the woods. Bread, roast meat, aye?”"
                        jump highisland_crew_beastfolk01a
                    'I look at {color=#f6d6bd}the bandit{/color}.' if bandit_highisland_joined and not bandit_highisland_opinion and not shortcut_darkforest_bandit_dead_troll:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}the bandit{/color}.')
                        $ bandit_highisland_opinion = 1
                        $ custom1 = "He nods slowly, staring away from you. “It may be the easier way, but if you think we can handle some climbing, all them mountain slopes here are rather gentle.”"
                        jump highisland_crew_beastfolk01a
                    '“{color=#f6d6bd}Tulia{/color}, what do you recommend?”' if tulia_highisland_joined and not tulia_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, what do you recommend?”')
                        $ tulia_highisland_opinion = 1
                        $ custom1 = "“They have slaves and leaders,” she stares at the “deer”. “I doubt we have to feed {i}all{/i} of them.”"
                        jump highisland_crew_beastfolk01a
                    '“Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”' if tzvi_highisland_joined and not tzvi_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s hear it, {color=#f6d6bd}Tzvi{/color}.”')
                        $ tzvi_highisland_opinion = 1
                        if not tzvi_highisland_blocked:
                            $ custom1 = "He nods and reveals his blade. “Ready when you are.”"
                        else:
                            $ custom1 = "He shakes his head. “I’m exhausted, warden. I can’t help you here.”"
                        jump highisland_crew_beastfolk01a
                    '“{color=#f6d6bd}Quintus{/color}, any ideas?”' if quintus_highisland_joined and not quintus_highisland_opinion:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Quintus{/color}, any ideas?”')
                        $ quintus_highisland_opinion = 1
                        $ custom1 = "He keeps rubbing his neck. “Better please them. Those of us who got wounded or tired may not get to the other side.”"
                        jump highisland_crew_beastfolk01a
                    'I look at {color=#f6d6bd}Tzvi{/color} and make sure he’s ready. We’ll get through by force.' if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold1 and highisland_beastfolk_assassination_available:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}Tzvi{/color} and make sure he’s ready. We’ll get through by force.')
                        jump highisland_crew_beastfolk02alt
                    'To use Tzvi’s help, I need to feed some of them. (disabled)' if highisland_beastfolk_feeding_points < highisland_beastfolk_feeding_threshhold1 and highisland_beastfolk_assassination_available:
                        pass
                    '{image=d6} With a few of them gone, we could try to get through them.' if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold2 and highisland_beastfolk_feeding_points < highisland_beastfolk_feeding_threshhold3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} With a few of them gone, we could try to get through them.')
                        $ highisland_beastfolk_attack_harshmodifier = 1
                        jump highisland_crew_beastfolk02
                    '{image=d6} With most of them gone, we could try to get to the other side.' if highisland_beastfolk_feeding_points >= highisland_beastfolk_feeding_threshhold3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} With most of them gone, we could try to get to the other side.')
                        jump highisland_crew_beastfolk02
                    'I’ll keep the rest of my supplies for myself. “Let’s look for another path.”' if highisland_beastfolk_feeding_foodestimation >= 1 and highisland_beastfolk_feeding_points >= 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll keep the rest of my supplies for myself. “Let’s look for another path.”')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination
                    'I’ll keep my supplies for myself. “Let’s look for another path.”' if highisland_beastfolk_feeding_foodestimation >= 1 and highisland_beastfolk_feeding_points <= 0:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll keep my supplies for myself. “Let’s look for another path.”')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination
                    'I’ve got nothing else to give them. “Let’s try another path.”' if highisland_beastfolk_feeding_foodestimation <= 0 and highisland_beastfolk_feeding_points >= 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve got nothing else to give them. “Let’s try another path.”')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination
                    'I’ve got nothing to give them. “Let’s try another path.”' if highisland_beastfolk_feeding_foodestimation <= 0 and highisland_beastfolk_feeding_points <= 0:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve got nothing to give them. “Let’s try another path.”')
                        $ highisland_destination = "climbingmountain"
                        jump highisland_destination

        label highisland_crew_beastfolk02:
            $ at = 0
            $ at_unlock_spell = 0
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
                $ d100roll -= 20
            elif item_axe02 or item_axe02alt:
                $ d100roll -= 10
            if item_shield:
                $ d100roll -= 5
            if quintus_highisland_joined and not quintus_highisland_blocked:
                $ d100roll -= 5
            if thyrsus_highisland_joined and not thyrsus_highisland_blocked:
                $ d100roll -= 5
            if tulia_highisland_joined and not tulia_highisland_blocked:
                $ d100roll -= 5
            if tzvi_highisland_joined and not tzvi_highisland_blocked:
                $ d100roll -= 5
            if aegidia_highisland_tired or aegidia_highisland_blocked:
                $ d100roll += 5
            if dalit_highisland_tired or dalit_highisland_blocked:
                $ d100roll += 5
            if efren_highisland_tired or efren_highisland_blocked:
                $ d100roll += 5
            if thyrsus_highisland_tired or thyrsus_highisland_blocked:
                $ d100roll += 5
            if pyrrhos_highisland_tired or pyrrhos_highisland_blocked:
                $ d100roll += 5
            if bandit_highisland_tired or bandit_highisland_blocked and not shortcut_darkforest_bandit_dead_troll:
                $ d100roll += 5
            if tulia_highisland_tired or tulia_highisland_blocked:
                $ d100roll += 5
            if tzvi_highisland_tired or tzvi_highisland_blocked:
                $ d100roll += 5
            if quintus_highisland_tired or quintus_highisland_blocked:
                $ d100roll += 5
            $ pc_battlecounter += 1
            $ highisland_beastfolk_attack_harshmodifier += 25
            if d100roll <= 40:
                menu:
                    '“Now!” You wave for the others to follow you, and put every breath into your legs, heading up the path. The beasts, more surprised than anything, step away, and while the “boar” tries to chase after you, the others stay idle. Soon, your crew leaves the ruins behind.
                    '
                    'Let’s hope there’s another path down.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope there’s another path down.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
            else:
                label highisland_companiondamage_loop_beastfolk:
                    if highisland_crew_left <= 0:
                        $ custom1 = "you into the ground, almost breaking your ribs, but then, cut and clubbed, it withdraws. Though in pain, you manage to get back on your feet."
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
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        else:
                            $ custom1 = "“Now!” You wave for the others to follow you, and put every breath into your legs, heading up the path. The beasts, more surprised than anything, step away, step away, but the “boar” doesn’t need time to think - it chases after you and slams into the bags on your back, breaking your spine and sending you over a nearby ledge."
                            jump highisland_gameover
                    else:
                        $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus', 'pc'])
                        if highisland_crew_dmg_target == "aegidia":
                            if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                jump highisland_companiondamage_loop_beastfolk
                            else:
                                $ aegidia_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Aegidia{/color} into the ground, almost breaking her ribs, but then, cut and clubbed, it withdraws. Though in pain, she manages to get back on her feet."
                        elif highisland_crew_dmg_target == "dalit":
                            if not dalit_highisland_joined or dalit_highisland_blocked:
                                jump highisland_companiondamage_loop_beastfolk
                            else:
                                $ dalit_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Dalit{/color} into the ground, almost breaking her ribs, but then, cut and clubbed, it withdraws. Though in pain, she manages to get back on her feet."
                        elif highisland_crew_dmg_target == "efren":
                            if not efren_highisland_joined or efren_highisland_blocked:
                                jump highisland_companiondamage_loop_beastfolk
                            else:
                                $ efren_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Efren{/color} into the ground, almost breaking his ribs, but then, cut and clubbed, it withdraws. Though in pain, he manages to get back on his feet."
                        elif highisland_crew_dmg_target == "thyrsus":
                            if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                jump highisland_companiondamage_loop_beastfolk
                            else:
                                $ thyrsus_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Thyrsus{/color} into the ground, almost breaking his ribs, but then, cut and clubbed, it withdraws. Though in pain, he manages to get back on his feet."
                        elif highisland_crew_dmg_target == "pyrrhos":
                            if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                jump highisland_companiondamage_loop_beastfolk
                            else:
                                $ pyrrhos_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} into the ground, almost breaking his ribs, but then, cut and clubbed, it withdraws. Though in pain, he manages to get back on his feet."
                        elif highisland_crew_dmg_target == "bandit":
                            if not bandit_highisland_joined or bandit_highisland_blocked:
                                jump highisland_companiondamage_loop_beastfolk
                            else:
                                $ bandit_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}the bandit{/color} into the ground, almost breaking his ribs, but then, cut and clubbed, it withdraws. Though in pain, he manages to get back on his feet."
                        elif highisland_crew_dmg_target == "tulia":
                            if not tulia_highisland_joined or tulia_highisland_blocked:
                                jump highisland_companiondamage_loop_beastfolk
                            else:
                                $ tulia_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Tulia{/color} into the ground, almost breaking her ribs, but then, cut and clubbed, it withdraws. Though in pain, she manages to get back on her feet."
                        elif highisland_crew_dmg_target == "tzvi":
                            if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                jump highisland_companiondamage_loop_beastfolk
                            else:
                                $ tzvi_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Tzvi{/color} into the ground, almost breaking his ribs, but then, cut and clubbed, it withdraws. Though in pain, he manages to get back on his feet."
                        elif highisland_crew_dmg_target == "quintus":
                            if not quintus_highisland_joined or quintus_highisland_blocked:
                                jump highisland_companiondamage_loop_beastfolk
                            else:
                                $ quintus_highisland_blocked = 1
                                $ highisland_crew_left -= 1
                                $ custom1 = "{color=#f6d6bd}Quintus{/color} into the ground, almost breaking his ribs, but then, cut and clubbed, it withdraws. Though in pain, he manages to get back on his feet."
                        elif highisland_crew_dmg_target == "pc":
                            $ custom1 = "you into the ground, almost breaking your ribs, but then, cut and clubbed, it withdraws. Though in pain, you manage to get back on your feet."
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
                                if not cleanliness_clothes_blood:
                                    $ cleanliness_clothes_blood = 1
                                    show minus1appearance at appearancechange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                            else:
                                $ custom1 = "“Now!” You wave for the others to follow you, and put every breath into your legs, heading up the path. The beasts, more surprised than anything, step away, step away, but the “boar” doesn’t need time to think - it chases after you and slams into the bags on your back, breaking your spine and sending you over a nearby ledge."
                                jump highisland_gameover
                menu:
                    '“Now!” You wave for the others to follow you up the path, then put every breath into your legs. The majority of the beasts, more surprised than anything, step away, but a group of the larger ones chases after you. The “boar’s” charge outpaces you all, and even though your group manages to slow it down, the hit of its tusks sends [custom1]
                    \n\nSoon, your crew leaves the ruins behind.
                    '
                    'Let’s hope there’s another path down.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope there’s another path down.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination

        label highisland_crew_beastfolk02alt:
            $ at = 0
            $ at_unlock_spell = 0
            menu:
                '“Now!” You wave for the others to follow you up the path, while {color=#f6d6bd}Tzvi’s{/color} fancy steel dagger cuts through the “boar’s” neck. The other beasts let out howls and squeals, but get out of your way. Soon, your crew leaves the ruins behind.
                '
                'Let’s hope there’s another path down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope there’s another path down.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination

        label highisland_crew_beastfolk02spell:
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
            $ at = 0
            $ at_unlock_spell = 0
            menu:
                '“Now!” You wave for the others to follow you up the path, then take a deep breath. The beasts, more surprised than anything, step away, and once the “boar” starts to chase after you, you point at it with your wand. While the wave of pneuma doesn’t seem to impact the beast, it lets out a shocked squeal and covers its snout.
                \n\nSoon, your crew leaves the ruins behind.
                '
                'Let’s hope there’s another path down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope there’s another path down.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination

label highisland_climbingmountainALL:
    label highisland_solo_climbingmountainALL:
        label highisland_solo_climbingmountain01:
            $ custom1 = "The beasts stay in the ruined village. You follow the narrow sidepath, reaching a lone tower made of stone, though seeing how most of the loose bricks are on the outside of the structure, it could have been a hollow building used to lower down boulders from the platforms at the top.\n\nYou roll up your sleeves and stretch out your arms. It may be an endeavor, but you can do this."
            jump highisland_solo_climbingmountain01a

        label highisland_solo_climbingmountain01a:
            $ at_unlock_force = 0
            $ at = 0
            if highisland_climbingmountain_points <= 0:
                menu:
                    '[custom1]
                    \n\nOnce you get to the top of the tower, you easily reach the collapsing, wooden platform. After pulling yourself up a few more times, you’re on the ground, gasping for air. There are no monsters in sight, just the trail forward.
                    '
                    'I turn on my back and give the stars another look.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn on my back and give the stars another look.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
                    'At least it should be easier to climb down.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least it should be easier to climb down.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
            else:
                if pc_class == "warrior" and not highisland_climbingmountain_fighter:
                    $ at_unlock_force = 1
                    $ at = 0
                menu:
                    '[custom1]
                    '
                    'My muscles will help me cross the largest gaps.' ( condition="at == 'force' and not highisland_climbingmountain_fighter" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- My muscles will help me cross the largest gaps.')
                        $ highisland_climbingmountain_fighter = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "You compensate for the lack of technique and tools with your vigor and confidence."
                        jump highisland_solo_climbingmountain01a
                    'I can’t climb up any faster. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0 and not highisland_climbingmountain_fighter" ):
                        pass
                    'I’ll use The Tool of Destruction to shape my path.' if item_magicchisel == 2 and not highisland_climbingmountain_chisel:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll use The Tool of Destruction to shape my path.')
                        $ highisland_climbingmountain_chisel = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "You shatter the bricks or break into the mountainside whenever you find no spot to rest your hands and feet."
                        jump highisland_solo_climbingmountain01a
                    'The perfect opportunity to use the bone hook.' if item_bonehook and not highisland_climbingmountain_hook: # ropehook
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- The perfect opportunity to use the bone hook.')
                        $ highisland_climbingmountain_hook = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "You don’t put enough trust in the structure to simply climb up the rope, but it secures you as you get higher."
                        jump highisland_solo_climbingmountain01a
                    'I can leave behind a few scraps of iron, use them as spikes for my boots.' if item_ironscraps and not highisland_climbingmountain_ironscraps:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can leave behind a few scraps of iron, use them as spikes for my boots.')
                        $ highisland_climbingmountain_ironscraps = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "The butt of your axe helps you easily stick a few long pieces into the gaps between the bricks."
                        jump highisland_solo_climbingmountain01a
                    'There are no more tools I can use. Either I’ll get there, or I won’t.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- There are no more tools I can use. Either I’ll get there, or I won’t.')
                        jump highisland_solo_climbingmountain02

        label highisland_solo_climbingmountain02:
            $ at_unlock_force = 0
            $ at = 0
            if highisland_climbingmountain_points == 1:
                if pc_food:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            elif highisland_climbingmountain_points == 2:
                if pc_food >= 2:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_food == 1:
                    $ pc_food = limit_pc_food(pc_food-1)
                    show minus1food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-2)
                    show minus2hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            else:
                if pc_food >= 2:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    $ pc_food = limit_pc_food(pc_food-1)
                    show minus1food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-2)
                    show minus2hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            menu:
                'After a few long minutes, you pull yourself up one last time, reaching the collapsing, wooden platform, then one more jump gets you onto the ground. You fall on your aching knees, gasping for air, covered in sweat, with tired eyes and bleeding fingers.
                \n\nThere are no monsters in sight, just the trail forward.
                '
                'I turn on my back and give the stars another look.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn on my back and give the stars another look.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination
                'At least it should be easier to climb down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least it should be easier to climb down.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination

    label highisland_howlers_climbingmountainALL:
        label highisland_howlers_climbingmountain01:
            if highisland_howlersguards_hp >= 8:
                $ highisland_climbingmountain_points -= 2
                $ custom1 = "The beasts stay in the ruined village. You follow the narrow sidepath, reaching a lone tower made of stone, though seeing how most of the loose bricks are on the outside of the structure, it could have been a hollow building used to lower down boulders from the platforms at the top.\n\nYou roll up your sleeves and stretch out your arms. So far, {color=#f6d6bd}the guards{/color} have proved to be remarkably durable. They don’t need much encouragement, and help you reach the higher parts of the building."
            elif highisland_howlersguards_hp >= 4:
                $ highisland_climbingmountain_points -= 1
                $ custom1 = "The beasts stay in the ruined village. You follow the narrow sidepath, reaching a lone tower made of stone, though seeing how most of the loose bricks are on the outside of the structure, it could have been a hollow building used to lower down boulders from the platforms at the top.\n\nYou roll up your sleeves and stretch out your arms. {color=#f6d6bd}The guards{/color} still have some strength left. After a short break, they’re ready to support both you and each other as you climb up the walls."
            else:
                $ custom1 = "The beasts stay in the ruined village. You follow the narrow sidepath, reaching a lone tower made of stone, though seeing how most of the loose bricks are on the outside of the structure, it could have been a hollow building used to lower down boulders from the platforms at the top.\n\nYou roll up your sleeves and stretch out your arms. “Another troll shit,” {color=#f6d6bd}the one with the mace{/color} spits on the wall and you give {color=#f6d6bd}the guards{/color} a closer look. Exhausted, they take a short break. They’re not going to be of much help during the climb."
            jump highisland_howlers_climbingmountain01a

        label highisland_howlers_climbingmountain01a:
            $ at_unlock_force = 0
            $ at = 0
            if highisland_climbingmountain_points <= 0:
                menu:
                    '[custom1]
                    \n\nOnce you get to the top of the tower, you easily reach the collapsing, wooden platform. After pulling yourself up a few more times, you’re on the ground, gasping for air. There are no monsters in sight, just the trail forward.
                    '
                    'At least it should be easier to climb down.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least it should be easier to climb down.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
                    'I make sure the others are safe.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make sure the others are safe.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
                    'I turn on my back and give the stars another look.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn on my back and give the stars another look.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
            else:
                if pc_class == "warrior" and not highisland_climbingmountain_fighter:
                    $ at_unlock_force = 1
                    $ at = 0
                menu:
                    '[custom1]
                    '
                    'My muscles will help me cross the largest gaps.' ( condition="at == 'force' and not highisland_climbingmountain_fighter" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- My muscles will help me cross the largest gaps.')
                        $ highisland_climbingmountain_fighter = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "You compensate for the lack of technique and tools with your vigor and confidence."
                        jump highisland_howlers_climbingmountain01a
                    'I can’t climb up any faster. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0 and not highisland_climbingmountain_fighter" ):
                        pass
                    'I’ll use The Tool of Destruction to shape my path.' if item_magicchisel == 2 and not highisland_climbingmountain_chisel:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll use The Tool of Destruction to shape my path.')
                        $ highisland_climbingmountain_chisel = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "You shatter the bricks or break into the mountainside whenever you find no spot to rest your hands and feet."
                        jump highisland_howlers_climbingmountain01a
                    'The perfect opportunity to use the bone hook.' if item_bonehook and not highisland_climbingmountain_hook:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- The perfect opportunity to use the bone hook.')
                        $ highisland_climbingmountain_hook = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "You don’t put enough trust in the structure to simply climb up the rope, but it secures you as you get higher."
                        jump highisland_howlers_climbingmountain01a
                    'I can leave behind a few scraps of iron, use them as spikes for my boots.' if item_ironscraps and not highisland_climbingmountain_ironscraps:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can leave behind a few scraps of iron, use them as spikes for my boots.')
                        $ highisland_climbingmountain_ironscraps = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "The butt of your axe helps you easily stick a few long pieces into the gaps between the bricks."
                        jump highisland_howlers_climbingmountain01a
                    'There are no more tools I can use. Either we’ll get there, or we won’t.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- There are no more tools I can use. Either we’ll get there, or we won’t.')
                        jump highisland_howlers_climbingmountain02

        label highisland_howlers_climbingmountain02:
            $ at_unlock_force = 0
            $ at = 0
            if highisland_climbingmountain_points == 1:
                if pc_food:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            elif highisland_climbingmountain_points == 2:
                if pc_food >= 2:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_food == 1:
                    $ pc_food = limit_pc_food(pc_food-1)
                    show minus1food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-2)
                    show minus2hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            else:
                if pc_food >= 2:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    $ pc_food = limit_pc_food(pc_food-1)
                    show minus1food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-2)
                    show minus2hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            menu:
                'After a few long minutes, you pull yourself up once last time, reaching the collapsing, wooden platform, then one more jump gets you onto the ground. You fall on your aching knees, gasping for air, covered in sweat, with tired eyes and bleeding fingers.
                \n\nThere are no monsters in sight, just the trail forward.
                '
                'At least it should be easier to climb down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least it should be easier to climb down.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination
                'I make sure the others are safe.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make sure the others are safe.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination
                'I turn on my back and give the stars another look.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn on my back and give the stars another look.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination

    label highisland_crew_climbingmountainALL:
        label highisland_crew_climbingmountain01:
            $ custom1 = "The beasts stay in the ruined village. You follow the narrow sidepath, reaching a lone tower made of stone, though seeing how most of the loose bricks are on the outside of the structure, it could have been a hollow building used to lower down boulders from the platforms at the top.\n\nYou roll up your sleeves and stretch out your arms. It may be an endeavor, but you can do this."
            jump highisland_crew_climbingmountain01a

        label highisland_crew_climbingmountain01a:
            $ at_unlock_force = 0
            $ at = 0
            if highisland_climbingmountain_points <= 0:
                menu:
                    '[custom1]
                    \n\nOnce you get to the top of the tower, you easily reach the collapsing, wooden platform. After pulling yourself up a few more times, you’re on the ground, gasping for air. There are no monsters in sight, just the trail forward.
                    '
                    'At least it should be easier to climb down.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least it should be easier to climb down.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
                    'I make sure the others are safe.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make sure the others are safe.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
                    'I turn on my back and give the stars another look.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn on my back and give the stars another look.')
                        $ highisland_destination = "volcano"
                        jump highisland_destination
            else:
                if pc_class == "warrior" and not highisland_climbingmountain_fighter:
                    $ at_unlock_force = 1
                    $ at = 0
                menu:
                    '[custom1]
                    '
                    'My muscles will help me cross the largest gaps.' ( condition="at == 'force' and not highisland_climbingmountain_fighter" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- My muscles will help me cross the largest gaps.')
                        $ highisland_climbingmountain_fighter = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "You compensate for the lack of technique and tools with your vigor and confidence."
                        jump highisland_crew_climbingmountain01a
                    'I can’t climb up any faster. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0 and not highisland_climbingmountain_fighter" ):
                        pass
                    'I look at my crew. “What do you say? A bit more effort and we’re there?”' if not highisland_climbingmountain_crewstrength:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at my crew. “What do you say? A bit more effort and we’re there?”')
                        $ highisland_climbingmountain_crewstrength = 1
                        if aegidia_highisland_joined and aegidia_highisland_blocked:
                            $ highisland_climbingmountain_crewstrength_calculate += 0
                        elif aegidia_highisland_joined and aegidia_highisland_tired:
                            $ highisland_climbingmountain_crewstrength_calculate += 1
                        elif aegidia_highisland_joined:
                            $ highisland_climbingmountain_crewstrength_calculate += 2
                        if efren_highisland_joined and efren_highisland_blocked:
                            $ highisland_climbingmountain_crewstrength_calculate += 0
                        elif efren_highisland_joined and efren_highisland_tired:
                            $ highisland_climbingmountain_crewstrength_calculate += 1
                        elif efren_highisland_joined:
                            $ highisland_climbingmountain_crewstrength_calculate += 2
                        if thyrsus_highisland_joined and thyrsus_highisland_blocked:
                            $ highisland_climbingmountain_crewstrength_calculate += 1
                        elif thyrsus_highisland_joined and thyrsus_highisland_tired:
                            $ highisland_climbingmountain_crewstrength_calculate += 2
                        elif thyrsus_highisland_joined:
                            $ highisland_climbingmountain_crewstrength_calculate += 3
                        if pyrrhos_highisland_joined and pyrrhos_highisland_blocked:
                            $ highisland_climbingmountain_crewstrength_calculate += 0
                        elif pyrrhos_highisland_joined and pyrrhos_highisland_tired:
                            $ highisland_climbingmountain_crewstrength_calculate += 1
                        elif pyrrhos_highisland_joined:
                            $ highisland_climbingmountain_crewstrength_calculate += 2
                        if not shortcut_darkforest_bandit_dead_troll:
                            if bandit_highisland_joined and bandit_highisland_blocked:
                                $ highisland_climbingmountain_crewstrength_calculate += 0
                            elif bandit_highisland_joined and bandit_highisland_tired:
                                $ highisland_climbingmountain_crewstrength_calculate += 1
                            elif bandit_highisland_joined:
                                $ highisland_climbingmountain_crewstrength_calculate += 2
                        if tulia_highisland_joined and tulia_highisland_blocked:
                            $ highisland_climbingmountain_crewstrength_calculate += 1
                        elif tulia_highisland_joined and tulia_highisland_tired:
                            $ highisland_climbingmountain_crewstrength_calculate += 2
                        elif tulia_highisland_joined:
                            $ highisland_climbingmountain_crewstrength_calculate += 3
                        if tzvi_highisland_joined and tzvi_highisland_blocked:
                            $ highisland_climbingmountain_crewstrength_calculate += 1
                        elif tzvi_highisland_joined and tzvi_highisland_tired:
                            $ highisland_climbingmountain_crewstrength_calculate += 2
                        elif tzvi_highisland_joined:
                            $ highisland_climbingmountain_crewstrength_calculate += 3
                        if quintus_highisland_joined and quintus_highisland_blocked:
                            $ highisland_climbingmountain_crewstrength_calculate += 1
                        elif quintus_highisland_joined and quintus_highisland_tired:
                            $ highisland_climbingmountain_crewstrength_calculate += 2
                        elif quintus_highisland_joined:
                            $ highisland_climbingmountain_crewstrength_calculate += 3
                        if highisland_climbingmountain_crewstrength_calculate >= 8:
                            $ highisland_climbingmountain_points -= 2
                            $ custom1 = "They may be tired, but give you encouraging nods and get to work, helping you reach the tougher spots."
                        elif highisland_climbingmountain_crewstrength_calculate >= 4:
                            $ highisland_climbingmountain_points -= 1
                            $ custom1 = "Despite the troubles of the journey, they give you determined nods. After a short break, they get to work, helping you reach the tougher spots."
                        else:
                            $ custom1 = "Tired, they exchange hesitant looks. While they’ll follow you to the end, you’re the one who needs to cross this wall first."
                        jump highisland_crew_climbingmountain01a
                    'I’ll use The Tool of Destruction to shape my path.' if item_magicchisel == 2 and not highisland_climbingmountain_chisel:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll use The Tool of Destruction to shape my path.')
                        $ highisland_climbingmountain_chisel = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "You shatter the bricks or break into the mountainside whenever you find no spot to rest your hands and feet."
                        jump highisland_crew_climbingmountain01a
                    'The perfect opportunity to use the bone hook.' if item_bonehook and not highisland_climbingmountain_hook:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- The perfect opportunity to use the bone hook.')
                        $ highisland_climbingmountain_hook = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "You don’t put enough trust in the structure to simply climb up the rope, but it secures you as you get higher."
                        jump highisland_crew_climbingmountain01a
                    '{color=#f6d6bd}Navica{/color} gave me a few spikes I could use here.' if navica_highisland_joined and not highisland_climbingmountain_navica:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Navica{/color} gave me a few spikes I could use here.')
                        $ highisland_climbingmountain_navica = 1
                        if item_ironscraps:
                            $ highisland_climbingmountain_points -= 2
                            $ custom1 = "The butt of your axe helps you easily stick them into the gaps between the bricks. Together with the few scraps of steel you brought with you, you don’t even have to use them that sparingly."
                        else:
                            $ highisland_climbingmountain_points -= 1
                            $ custom1 = "The butt of your axe helps you easily stick them into the gaps between the bricks."
                        jump highisland_crew_climbingmountain01a
                    'I can leave behind a few scraps of iron, use them as spikes for my boots.' if item_ironscraps and not highisland_climbingmountain_ironscraps and not navica_highisland_joined:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can leave behind a few scraps of iron, use them as spikes for my boots.')
                        $ highisland_climbingmountain_ironscraps = 1
                        $ highisland_climbingmountain_points -= 1
                        $ custom1 = "The butt of your axe helps you easily stick a few long pieces into the gaps between the bricks."
                        jump highisland_crew_climbingmountain01a
                    'There are no more tools I can use. Either we’ll get there, or we won’t.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- There are no more tools I can use. Either we’ll get there, or we won’t.')
                        jump highisland_crew_climbingmountain02

        label highisland_crew_climbingmountain02:
            $ at_unlock_force = 0
            $ at = 0
            if highisland_climbingmountain_points == 1:
                if pc_food:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            elif highisland_climbingmountain_points == 2:
                if pc_food >= 2:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_food == 1:
                    $ pc_food = limit_pc_food(pc_food-1)
                    show minus1food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-2)
                    show minus2hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            else:
                if pc_food >= 2:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    $ pc_food = limit_pc_food(pc_food-1)
                    show minus1food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
                    $ pc_hp = limit_pc_hp(pc_hp-2)
                    show minus2hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            menu:
                'After a few long minutes, you pull yourself up one last time, reaching the collapsing, wooden platform, then one more jump gets you onto the ground. You fall on your aching knees, gasping for air, covered in sweat, with tired eyes and bleeding fingers.
                \n\nThere are no monsters in sight, just the trail forward.
                '
                'At least it should be easier to climb down.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least it should be easier to climb down.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination
                'I make sure the others are safe.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make sure the others are safe.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination
                'I turn on my back and give the stars another look.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn on my back and give the stars another look.')
                    $ highisland_destination = "volcano"
                    jump highisland_destination

label highisland_destination:
    $ aegidia_highisland_opinion = 0
    $ dalit_highisland_opinion = 0
    $ efren_highisland_opinion = 0
    $ thyrsus_highisland_opinion = 0
    $ pyrrhos_highisland_opinion = 0
    $ bandit_highisland_opinion = 0
    $ tulia_highisland_opinion = 0
    $ tzvi_highisland_opinion = 0
    $ quintus_highisland_opinion = 0
    $ can_potions = 1
    $ can_items = 0
    if highisland_destination == "cave1":
        show areapicture hi_cave01 at basicfade
        $ highisland_spot = "cave1"
        if highisland_mode == "solo":
            jump highisland_solo_cave101
        if highisland_mode == "crew":
            jump highisland_crew_cave101
        if highisland_mode == "howlers":
            jump highisland_howlers_cave101
    if highisland_destination == "trailstart":
        show areapicture hi_trailstart at basicfade
        $ highisland_spot = "trailstart"
        if highisland_mode == "solo":
            jump highisland_solo_trailstart01
        if highisland_mode == "crew":
            jump highisland_crew_trailstart01
        if highisland_mode == "howlers":
            jump highisland_howlers_trailstart01
    if highisland_destination == "darkness":
        show areapicture hi_darkness at basicfade
        $ highisland_spot = "darkness"
        if highisland_mode == "solo":
            jump highisland_solo_darkness01
        if highisland_mode == "howlers":
            jump highisland_howlers_darkness01
        if highisland_mode == "crew":
            jump highisland_crew_darkness01
    if highisland_destination == "howlers":
        show areapicture hi_howlers at basicfade
        $ highisland_spot = "howlers"
        if highisland_mode == "solo":
            jump highisland_solo_howlers01
        if highisland_mode == "howlers":
            jump highisland_howlers_howlers01
        if highisland_mode == "crew":
            jump highisland_crew_howlers01
    if highisland_destination == "wallofinsects":
        show areapicture hi_wallofinsects at basicfade
        $ highisland_spot = "wallofinsects"
        if highisland_mode == "solo":
            jump highisland_solo_wallofinsects01
        if highisland_mode == "howlers":
            jump highisland_howlers_wallofinsects01
        if highisland_mode == "crew":
            jump highisland_crew_wallofinsects01
    if highisland_destination == "monitorlizards":
        show areapicture hi_monitorlizards at basicfade
        $ highisland_spot = "monitorlizards"
        if highisland_mode == "solo":
            jump highisland_solo_monitorlizards01
        if highisland_mode == "howlers":
            jump highisland_howlers_monitorlizards01
        if highisland_mode == "crew":
            jump highisland_crew_monitorlizards01
    if highisland_destination == "camp1":
        $ can_potions = 1
        $ can_items = 1
        show areapicture hi_camp1 at basicfade
        $ highisland_spot = "camp1"
        if highisland_mode == "solo":
            jump highisland_solo_camp101
        if highisland_mode == "howlers":
            jump highisland_howlers_camp101
        if highisland_mode == "crew":
            jump highisland_crew_camp101
    if highisland_destination == "denseplants":
        # show areapicture hi_denseplants at basicfade
        show areapicture hi_camp1 at basicfade
        $ highisland_spot = "denseplants"
        if highisland_mode == "solo":
            jump highisland_solo_denseplants01
        if highisland_mode == "howlers":
            jump highisland_howlers_denseplants01
        if highisland_mode == "crew":
            jump highisland_crew_denseplants01
    if highisland_destination == "trolltunnel":
        show areapicture hi_trolltunnel at basicfade
        $ highisland_spot = "trolltunnel"
        if highisland_mode == "solo":
            jump highisland_solo_trolltunnel01
        if highisland_mode == "howlers":
            jump highisland_howlers_trolltunnel01
        if highisland_mode == "crew":
            jump highisland_crew_trolltunnel01
    if highisland_destination == "beastfolk":
        show areapicture hi_beastfolk1 at basicfade
        $ highisland_spot = "beastfolk"
        if highisland_mode == "solo":
            jump highisland_solo_beastfolk01
        if highisland_mode == "howlers":
            jump highisland_howlers_beastfolk01
        if highisland_mode == "crew":
            jump highisland_crew_beastfolk01
    if highisland_destination == "climbingmountain":
        show areapicture hi_climbingmountain at basicfade
        $ highisland_spot = "climbingmountain"
        if highisland_mode == "solo":
            jump highisland_solo_climbingmountain01
        if highisland_mode == "howlers":
            jump highisland_howlers_climbingmountain01
        if highisland_mode == "crew":
            jump highisland_crew_climbingmountain01
    if highisland_destination == "volcano":
        $ highisland_spot = "volcano"
        if highisland_mode == "solo":
            jump highisland_solo_volcano01
        if highisland_mode == "howlers":
            jump highisland_howlers_volcano01
        if highisland_mode == "crew":
            jump highisland_crew_volcano01

label highisland_gameover:
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
        'I wasn’t ready for {color=#f6d6bd}High Island{/color}. Let me prepare better.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wasn’t ready for {color=#f6d6bd}High Island{/color}. Let me prepare better.')
            stop music fadeout 4.0
            $ renpy.load("highisland")

# label highisland_scentbeastALL:
#     if highisland_destination == "villageedge":
#         show areapicture hi_villageedge at basicfade
#         $ highisland_spot = "villageedge"
#         if highisland_mode == "solo":
#             jump highisland_solo_villageedge01
#         if highisland_mode == "howlers":
#             jump highisland_howlers_villageedge01
#         if highisland_mode == "crew":
#             jump highisland_crew_villageedge01
#     if highisland_destination == "scentbeast":
#         show areapicture hi_scentbeast at basicfade
#         $ highisland_spot = "scentbeast"
#         if highisland_mode == "solo":
#             jump highisland_solo_scentbeast01
#         if highisland_mode == "howlers":
#             jump highisland_howlers_scentbeast01
#         if highisland_mode == "crew":
#             jump highisland_crew_scentbeast01
#     if highisland_destination == "goblins":
#         show areapicture hi_goblins at basicfade
#         $ highisland_spot = "goblins"
#         if highisland_mode == "solo":
#             jump highisland_solo_goblins01
#         if highisland_mode == "howlers":
#             jump highisland_howlers_goblins01
#         if highisland_mode == "crew":
#             jump highisland_crew_goblins01
#
#     # - coś, co można ogłupić zapachami
#     # thyrsus
#     # item_shortcutherbs = 0
#     # item_soap = 0
#     # item_perfume = 0
#     label highisland_solo_scentbeastALL:
#         label highisland_solo_scentbeast01:
#             $ custom1 = ""
#             jump highisland_solo_scentbeast01a
#
#         label highisland_solo_scentbeast01a:
#             menu:
#                 '[custom1]
#                 '
#                 '':
#                     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
#                     $ custom1 = ""
#                     jump highisland_solo_scentbeast01a
#
#     label highisland_howlers_scentbeastALL:
#         label highisland_howlers_scentbeast01:
#             $ custom1 = ""
#             jump highisland_howlers_scentbeast01a
#
#         label highisland_howlers_scentbeast01a:
#             menu:
#                 '[custom1]
#                 '
#                 '':
#                     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
#                     $ custom1 = ""
#                     jump highisland_howlers_scentbeast01a
#
#     label highisland_crew_scentbeastALL:
#         label highisland_crew_scentbeast01:
#             $ custom1 = ""
#             jump highisland_crew_scentbeast01a
#
#         label highisland_crew_scentbeast01a:
#             menu:
#                 '[custom1]
#                 '
#                 '':
#                     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
#                     $ custom1 = ""
#                     jump highisland_crew_scentbeast01a
#
# label highisland_goblinsALL: # they give food if explored, but waste resources otherwise
#     label highisland_solo_goblinsALL:
#         label highisland_solo_goblins01:
#             $ custom1 = ""
#             jump highisland_solo_goblins01a
#
#         label highisland_solo_goblins01a:
#             menu:
#                 '[custom1]
#                 '
#                 '':
#                     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
#                     $ custom1 = ""
#                     jump highisland_solo_goblins01a
#
#     label highisland_howlers_goblinsALL:
#         label highisland_howlers_goblins01:
#             $ custom1 = ""
#             jump highisland_howlers_goblins01a
#
#         label highisland_howlers_goblins01a:
#             menu:
#                 '[custom1]
#                 '
#                 '':
#                     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
#                     $ custom1 = ""
#                     jump highisland_howlers_goblins01a
#
#     label highisland_crew_goblinsALL:
#         label highisland_crew_goblins01:
#             $ custom1 = ""
#             jump highisland_crew_goblins01a
#
#         label highisland_crew_goblins01a:
#             menu:
#                 '[custom1]
#                 '
#                 '':
#                     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
#                     $ custom1 = ""
#                     jump highisland_crew_goblins01a
