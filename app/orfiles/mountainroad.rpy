###################### MOUNTAIN ROAD
default mountainroad_firsttime = 0
default mountainroad_fluff = ""
default mountainroad_fluff_old = ""
default mountainroad_griffon_fluff = ""

default mountainroad_griffon = 1
default mountainroad_griffon_gone = 0
default mountainroad_griffon_lookedat = 0

default mountainroad_rope = 0
default mountainroad_bones = 0
default mountainroad_spear_lookedat = 0
default mountainroad_spear_taken = 0

default mountainroad_egg_lookedat = 0
default mountainroad_egg_interacted = 0
default mountainroad_egg_leftalone = 0
default mountainroad_egg_broken = 0
default mountainroad_egg_gone = 0
default mountainroad_egg_finished = 0

label mountainroad01:
    nvl clear
    $ pc_area = "mountainroad"
    stop music fadeout 4.0
    play nature "audio/ambient/mountainroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture mountainroad01 at basicfade behind mountainroadbronzerod, mountainroadegg, mountainroadspear
    if mountainroad_rope:
        show mountainroadrope at basicfade
    if eudocia_bronzerod_rodin_mountainroad:
        show mountainroadbronzerod at basicfade
    if mountainroad_egg_broken:
        show mountainroadegg broken at basicfade
    if mountainroad_egg_gone:
        show mountainroadegg gone at basicfade
    if mountainroad_spear_taken:
        show mountainroadspear gone at basicfade
    label mountainroad_fluffloop:
        $ mountainroad_fluff = renpy.random.choice(['The singing birds and dragon roars are concealed by the strong winds. You spot fresh claw marks and boot prints on the road.', 'A few pigeons are sitting on the rocks, cleaning their feathers. A single, yellow monkey is observing them curiously from a branch.', 'A few birds argue with each other on the ropes of the bridge, but they flee once your palfrey gets closer.', 'You spot the brown fur of a hoofed critter running on the plateau above you. Before you consider chasing after it, it flees with short skips, traversing smoothly through the rocky terrain.', 'The wind shakes the trees, and as they rustle, you notice a lynx sitting on a branch, doing its best to not fall down.'])
        if mountainroad_fluff_old == mountainroad_fluff:
            jump mountainroad_fluffloop
        else:
            $ mountainroad_fluff_old = mountainroad_fluff
    if not mountainroad_firsttime:
        $ world_known_areas += 1
        $ mountainroad_firsttime = 1
        $ giantstatue_unlocked = 1
        $ greenmountaintribe_unlocked = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        jump mountainroadfirsttime01
    else:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if mountainroad_egg_broken or mountainroad_egg_gone:
            $ mountainroad_griffon_gone = 1
        if not mountainroad_griffon_gone:
            if quarters <= 40: # 10
                $ mountainroad_griffon = 0
                $ mountainroad_griffon_fluff = "The griffon is nowhere in sight."
            else:
                $ mountainroad_griffon = 1
                if quarters > 40 and quarters <= world_daylength-28: # 10-14
                    $ mountainroad_griffon_fluff = "There are fresh blood stains next to the nest. The griffon is walking on the lower plateau, patrolling its surroundings. It screeches at you with its bird-like head as soon as you reach the bridge, then leaps forward."
                elif quarters <= (world_daylength-12): # 14-18
                    $ mountainroad_griffon_fluff = "The griffon is sitting in its nest, which seems too small for it to squeeze inside. Its limbs are resting on the ground, and its head is leaning against the tree. As soon as you reach the bridge, the beast opens its eyes and screeches at you with its bird-like head, but it’s a bit drowsy. It rises to its paws, preparing for a confrontation."
                elif quarters <= world_daylength: # 18-21
                    $ mountainroad_griffon_fluff = "The griffon is patrolling the area close to the nest, and as soon as it spots you, it spreads its wings and lowers its head, creeping forward."
                else: # 21+
                    $ mountainroad_griffon_fluff = "The griffon is standing above its nest, erratically looking around. As soon as you reach the bridge, the beast screeches at you with its bird-like head, but doesn’t move a step closer. In the moonlight, it looks more like prey than a predator."
                    $ bestiary_griffon_parenting = 1
        else:
            $ mountainroad_griffon = 0
            $ mountainroad_griffon_fluff = "The griffon is nowhere in sight."
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump mountainroadregular01

label mountainroadfirsttime01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if persistent.deafmode:
        $ deafcustom1 = "The strong wind, the wooden bridge connecting the rock ledges, the distant singing of birds, roars of dragons..."
    else:
        $ deafcustom1 = "The strong wind, the wooden bridge connecting the rock ledges, the unusual terrain..."
    if quarters <= 40:
        $ mountainroad_fluff = "A large shadow circles above the ground, and its owner introduces itself quickly. A winged creature larger than a bear lands on the ground next to the nest, then screeches at you through its sharp, golden, black-tipped eagle-like beak. It spreads its wings, as wide as a barn gate."
    else:
        $ mountainroad_fluff = "A creature larger than a bear steps away from its nest, then screeches at you through its sharp, black-tipped, golden eagle-like beak. It spreads its wings, as wide as a barn gate."
    menu:
        '[deafcustom1] You can’t pay attention to any of that now. [mountainroad_fluff]
        \n\nYou stay in your saddle.
        '
        'I use a rope to climb down and take a closer look.' ( condition="(pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_spear_taken and quarters < world_daylength) or (pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_egg_finished and quarters < world_daylength)" ): # ropehook
            jump mountainroadwentdown01
        'I get back down.' ( condition="(pc_hp and not mountainroad_griffon and mountainroad_rope and not mountainroad_spear_taken and quarters < world_daylength) or (pc_hp and not mountainroad_griffon and mountainroad_rope and not mountainroad_egg_finished and quarters < world_daylength)" ):
            jump mountainroadwentdown02
        'It’s too dark to climb now. (disabled)' ( condition="(pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_spear_taken and quarters >= world_daylength) or (pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_egg_finished and quarters >= world_daylength) or (not mountainroad_griffon and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad and quarters >= world_daylength)" ):
            pass
        'It’s a decent place for a bronze rod.' if not mountainroad_griffon and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad and quarters < world_daylength:
            jump mountainroadbronzerod01
        'I look at the spear.' if not mountainroad_spear_taken and not mountainroad_spear_lookedat:
            jump mountainroad_spear_lookedat01
        'I examine the beast.' if mountainroad_griffon and not mountainroad_griffon_lookedat:
            jump mountainroad_griffon_lookedat01
        'I’m too weak to start climbing now. (Required vitality: 1) (disabled)' ( condition="(pc_hp <= 0 and not mountainroad_griffon and not mountainroad_spear_taken) or (pc_hp <= 0 and not mountainroad_griffon and not mountainroad_egg_finished)" ):
            pass
        'I can’t climb without a rope. (disabled)' ( condition="(item_rope <= 0 and not mountainroad_griffon and not mountainroad_spear_taken) or (item_rope <= 0 and not mountainroad_griffon and not mountainroad_egg_finished)" ): # ropehook
            pass
        'I could place one of the bronze rods somewhere here, but not with this beast around. (disabled)' if mountainroad_griffon and (quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad):
            pass
        'There’s not much for me to do here. (disabled)' if (mountainroad_spear_taken and mountainroad_egg_finished):
            pass
        'This beast could attack me at any moment. (disabled)' if (mountainroad_griffon and not mountainroad_spear_taken) or (mountainroad_griffon and not mountainroad_egg_finished):
            pass

label mountainroadregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        '[mountainroad_griffon_fluff] [mountainroad_fluff]
        '
        'I use a rope to climb down and take a closer look.' ( condition="(pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_spear_taken and quarters < world_daylength) or (pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_egg_finished and quarters < world_daylength)" ):
            jump mountainroadwentdown01
        'I get back down.' ( condition="(pc_hp and not mountainroad_griffon and mountainroad_rope and not mountainroad_spear_taken and quarters < world_daylength) or (pc_hp and not mountainroad_griffon and mountainroad_rope and not mountainroad_egg_finished and quarters < world_daylength)" ):
            jump mountainroadwentdown02
        'It’s too dark to climb now. (disabled)' ( condition="(pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_spear_taken and quarters >= world_daylength) or (pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_egg_finished and quarters >= world_daylength) or (not mountainroad_griffon and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad and quarters >= world_daylength)" ):
            pass
        'It’s a decent place for a bronze rod.' if not mountainroad_griffon and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad and quarters < world_daylength:
            jump mountainroadbronzerod01
        'I look at the spear.' if not mountainroad_spear_taken and not mountainroad_spear_lookedat:
            jump mountainroad_spear_lookedat01
        'I examine the beast.' if mountainroad_griffon and not mountainroad_griffon_lookedat:
            jump mountainroad_griffon_lookedat01
        'I’m too weak to start climbing now. (Required vitality: 1) (disabled)' ( condition="(pc_hp <= 0 and not mountainroad_griffon and not mountainroad_spear_taken) or (pc_hp <= 0 and not mountainroad_griffon and not mountainroad_egg_finished)" ):
            pass
        'I can’t climb without a rope. (disabled)' ( condition="(item_rope <= 0 and not mountainroad_griffon and not mountainroad_spear_taken) or (item_rope <= 0 and not mountainroad_griffon and not mountainroad_egg_finished)" ):
            pass
        'I could place one of the bronze rods somewhere here, but not with this beast around. (disabled)' if mountainroad_griffon and (quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad):
            pass
        'There’s not much for me to do here. (disabled)' if (mountainroad_spear_taken and mountainroad_egg_finished):
            pass
        'This beast could attack me at any moment. (disabled)' if (mountainroad_griffon and not mountainroad_spear_taken) or (mountainroad_griffon and not mountainroad_egg_finished):
            pass

label mountainroad_spear_lookedat01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the spear.')
    $ mountainroad_spear_lookedat = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 0
    if mountainroad_griffon:
        menu:
            'A simple weapon, but not a cheap one. The light shaft makes you think of ash wood, and is neither soggy, nor bent. The head is made of iron or steel, and has a bar at the end that’s meant to stop the blade from getting too deep into the flesh. The ferrule placed at the bottom of the weapon could serve as a club in a desperate situation. There’s no way of telling if it was left here after an unsuccessful hunt, or carried here together with a monster’s victim.
            \n\nYou don’t have time to mull over it. The beast leaps toward the rock face. After it flaps its wings, the gust of wind brushes your hair.
            '
            'Time for us to go. (disabled)' if pc_likeshorsename:
                pass
            'Time for me to go. (disabled)' if not pc_likeshorsename:
                pass
    else:
        menu:
            'A simple weapon, but not a cheap one. The light shaft makes you think of ash wood, and is neither soggy, nor bent. The head is made of iron or steel, and has a bar at the end that’s meant to stop the blade from getting too deep into the flesh. The ferrule placed at the bottom of the weapon could serve as a club in a desperate situation. There’s no way of telling if it was left here after an unsuccessful hunt, or carried here together with a monster’s victim.
            '
            'I use a rope to climb down and take a closer look.' ( condition="(pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_spear_taken and quarters < world_daylength) or (pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_egg_finished and quarters < world_daylength)" ):
                jump mountainroadwentdown01
            'I get back down.' ( condition="(pc_hp and not mountainroad_griffon and mountainroad_rope and not mountainroad_spear_taken and quarters < world_daylength) or (pc_hp and not mountainroad_griffon and mountainroad_rope and not mountainroad_egg_finished and quarters < world_daylength)" ):
                jump mountainroadwentdown02
            'It’s too dark to climb now. (disabled)' ( condition="(pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_spear_taken and quarters >= world_daylength) or (pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_egg_finished and quarters >= world_daylength) or (not mountainroad_griffon and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad and quarters >= world_daylength)" ):
                pass
            'It’s a decent place for a bronze rod.' if not mountainroad_griffon and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad and quarters < world_daylength:
                jump mountainroadbronzerod01
            'I look at the spear.' if not mountainroad_spear_taken and not mountainroad_spear_lookedat:
                jump mountainroad_spear_lookedat01
            'I examine the beast.' if mountainroad_griffon and not mountainroad_griffon_lookedat:
                jump mountainroad_griffon_lookedat01
            'I’m too weak to start climbing now. (Required vitality: 1) (disabled)' ( condition="(pc_hp <= 0 and not mountainroad_griffon and not mountainroad_spear_taken) or (pc_hp <= 0 and not mountainroad_griffon and not mountainroad_egg_finished)" ):
                pass
            'I can’t climb without a rope. (disabled)' ( condition="(item_rope <= 0 and not mountainroad_griffon and not mountainroad_spear_taken) or (item_rope <= 0 and not mountainroad_griffon and not mountainroad_egg_finished)" ):
                pass
            'I could place one of the bronze rods somewhere here, but not with this beast around. (disabled)' if mountainroad_griffon and (quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad):
                pass
            'There’s not much for me to do here. (disabled)' if (mountainroad_spear_taken and mountainroad_egg_finished):
                pass
            'This beast could attack me at any moment. (disabled)' if (mountainroad_griffon and not mountainroad_spear_taken) or (mountainroad_griffon and not mountainroad_egg_finished):
                pass

label mountainroad_griffon_lookedat01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the beast.')
    $ mountainroad_griffon_lookedat = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 0
    if pc_class == "mage":
        $ custom1 = "A single human with but a simple blade and a few magic tricks would never survive clashing with a monstrosity of this size."
    elif pc_class == "warrior":
        $ custom1 = "A single human with but a simple blade and a crossbow would never survive clashing with a monstrosity of this size."
    elif pc_class == "scholar":
        $ custom1 = "A single human with but a simple blade and a fistful of herbs would never survive clashing with a monstrosity of this size."
    menu:
        'Its movements are deliberate and confident. It makes a tiger-like leap, then stands still like a statue, while the brown, white, and yellow feathers covering the front half of its shell are still dancing with the wind. The wings hinder your sight, so you spot only glimpses of the cat-like claws and the clay-like fur. Its large chest rises and falls slowly.
        \n\nThe noble griffon’s yellow eyes speak only of violence. Its curved beak is longer than your forearm, and the talons on its front paws are like sickles. You don’t doubt that its cruel promises may not only be fulfilled, but are a certainty. [custom1]
        \n\nYou don’t have more time to mull over it. The beast leaps toward the rock face. After it flaps its wings, the gust of wind brushes your hair.
        '
        'Time for us to go. (disabled)' if pc_likeshorsename:
            pass
        'Time for me to go. (disabled)' if not pc_likeshorsename:
            pass

label mountainroadafterinteraction01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 0
    if not mountainroad_griffon_gone:
        $ mountainroad_griffon = 1
        menu:
            'You return to the hanging bridge and hear the beast’s screech. It’s on its way here.
            '
            'Time for us to go. (disabled)' if pc_likeshorsename:
                pass
            'Time for me to go. (disabled)' if not pc_likeshorsename:
                pass
    else:
        menu:
            'You return to the hanging bridge. So far, you hear no sign of the beast’s arrival.
            '
            'I use a rope to climb down and take a closer look.' ( condition="(pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_spear_taken and quarters < world_daylength) or (pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_egg_finished and quarters < world_daylength)" ):
                jump mountainroadwentdown01
            'I get back down.' ( condition="(pc_hp and not mountainroad_griffon and mountainroad_rope and not mountainroad_spear_taken and quarters < world_daylength) or (pc_hp and not mountainroad_griffon and mountainroad_rope and not mountainroad_egg_finished and quarters < world_daylength)" ):
                jump mountainroadwentdown02
            'It’s too dark to climb now. (disabled)' ( condition="(pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_spear_taken and quarters >= world_daylength) or (pc_hp and not mountainroad_griffon and not mountainroad_rope and not mountainroad_egg_finished and quarters >= world_daylength) or (not mountainroad_griffon and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad and quarters >= world_daylength)" ):
                pass
            'It’s a decent place for a bronze rod.' if not mountainroad_griffon and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad and quarters < world_daylength:
                jump mountainroadbronzerod01
            'I look at the spear.' if not mountainroad_spear_taken and not mountainroad_spear_lookedat:
                jump mountainroad_spear_lookedat01
            'I examine the beast.' if mountainroad_griffon and not mountainroad_griffon_lookedat:
                jump mountainroad_griffon_lookedat01
            'I’m too weak to start climbing now. (Required vitality: 1) (disabled)' ( condition="(pc_hp <= 0 and not mountainroad_griffon and not mountainroad_spear_taken) or (pc_hp <= 0 and not mountainroad_griffon and not mountainroad_egg_finished)" ):
                pass
            'I can’t climb without a rope. (disabled)' ( condition="(item_rope <= 0 and not mountainroad_griffon and not mountainroad_spear_taken) or (item_rope <= 0 and not mountainroad_griffon and not mountainroad_egg_finished)" ):
                pass
            'I could place one of the bronze rods somewhere here, but not with this beast around. (disabled)' if mountainroad_griffon and (quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_mountainroad):
                pass
            'There’s not much for me to do here. (disabled)' if (mountainroad_spear_taken and mountainroad_egg_finished):
                pass
            'This beast could attack me at any moment. (disabled)' if (mountainroad_griffon and not mountainroad_spear_taken) or (mountainroad_griffon and not mountainroad_egg_finished):
                pass

label mountainroadbronzerod01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s a decent place for a bronze rod.')
    show mountainroadbronzerod at basicfade
    $ quarters += 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ renpy.notify("Journal updated: Bronze Rods")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
    $ item_bronzerod -= 1
    $ eudocia_bronzerod_rodin_mountainroad = 1
    $ eudocia_bronzerod_installed += 1
    if not item_bronzerod:
        $ renpy.notify("Journal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
        if eudocia_bronzerod_installed < 4:
            $ quest_bronzerod_description07 = "I’ve placed fewer than four rods, but I don’t have any of them left. I should inform {color=#f6d6bd}Eudocia{/color}."
        elif eudocia_bronzerod_installed < eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
            $ quest_bronzerod_description04 = "I’ve placed some of the rods, but don’t have any of them left. I should collect my reward."
        elif eudocia_bronzerod_installed >= eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
            $ quest_bronzerod_description05 = "I’ve placed all of the rods. I should collect my reward."
        else:
            $ quest_bronzerod_description03 = "I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
    else:
        if eudocia_bronzerod_installed >= 4:
            if not quest_bronzerod_description04:
                $ renpy.notify("Journal updated: Bronze Rods")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                $ quest_bronzerod_description02 = 0
    menu:
        'You kick and shake the wooden posts to see if they’re stable. You grab a rod and tools and climb up, using the wall for support. Finally, grabbing a clump of grass, you get to the top of the shelf.
        \n\nWith a knife, a stick, and your own hands, you spend a few minutes digging a hole for cold bronze. You cover it with dirt and tread around it until you’re sure it won’t move.
        '
        'I climb down.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb down.')
            jump mountainroadafterinteraction01

label mountainroaddownALL:
    label mountainroadwentdown01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use a rope to climb down and take a closer look.')
        $ mountainroad_rope = 1
        $ quarters += 1
        #$ item_rope -= 1
        # $ renpy.notify("You used a rope.")
        # $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You used a rope.{/i}')
        show mountainroadrope at basicfade
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'In a few minutes, you tie it to a wooden post and use its support to safely get down, basing your feet on the rock face. Once you touch the grass again, the beast’s realm is oddly quiet.
            '
            'I grab the spear.' if not mountainroad_spear_taken:
                jump mountainroadtakingspear01
            'I examine the nearby bones.' if not mountainroad_bones:
                jump mountainroad_bones01
            'I approach the nest.' if not mountainroad_egg_lookedat:
                jump mountainroadnest01
            'My ancestors would leave this egg as it is, and so should I.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My ancestors would leave this egg as it is, and so should I.')
                jump mountainroadnest02d
            'The United Church’s teachings are clear. I need to shatter this egg.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The United Church’s teachings are clear. I need to shatter this egg.')
                jump mountainroadnest02a
            'Maybe shattering this egg will make the beast leave this place.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion != "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe shattering this egg will make the beast leave this place.')
                jump mountainroadnest02a
            'This egg would be worth a fortune in {color=#f6d6bd}Hovlavan{/color}.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_interacted:
                jump mountainroadnest02b
            'Well, maybe someone in the lowlands will buy it.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and mountainroad_egg_interacted:
                jump mountainroadnest02c
            'I have no right to this egg. I leave it behind.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_leftalone and pc_religion != "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have no right to this egg. I leave it behind.')
                jump mountainroadnest02d
            'I climb back up.' if mountainroad_egg_lookedat or mountainroad_spear_taken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb back up.')
                jump mountainroadafterinteraction01

    label mountainroadwentdown02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I get back down.')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'Having the rope already attached, you get there in no time.
            '
            'I grab the spear.' if not mountainroad_spear_taken:
                jump mountainroadtakingspear01
            'I examine the nearby bones.' if not mountainroad_bones:
                jump mountainroad_bones01
            'I approach the nest.' if not mountainroad_egg_lookedat:
                jump mountainroadnest01
            'My ancestors would leave this egg as it is, and so should I.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My ancestors would leave this egg as it is, and so should I.')
                jump mountainroadnest02d
            'The United Church’s teachings are clear. I need to shatter this egg.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The United Church’s teachings are clear. I need to shatter this egg.')
                jump mountainroadnest02a
            'Maybe shattering this egg will make the beast leave this place.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion != "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe shattering this egg will make the beast leave this place.')
                jump mountainroadnest02a
            'This egg would be worth a fortune in {color=#f6d6bd}Hovlavan{/color}.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_interacted:
                jump mountainroadnest02b
            'Well, maybe someone in the lowlands will buy it.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and mountainroad_egg_interacted:
                jump mountainroadnest02c
            'I have no right to this egg. I leave it behind.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_leftalone and pc_religion != "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have no right to this egg. I leave it behind.')
                jump mountainroadnest02d
            'I climb back up.' if mountainroad_egg_lookedat or mountainroad_spear_taken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb back up.')
                jump mountainroadafterinteraction01

    label mountainroadtakingspear01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the spear.')
        show mountainroadspear gone at basicfade
        $ mountainroad_spear_taken = 1
        if not mountainroad_spear_lookedat:
            $ mountainroad_spear_lookedat = 1
            $ custom1 = "It’s simple weapon, but not a cheap one. The light shaft makes you think of ash wood, and is neither soggy, nor bent. The head is made of iron, and has a bar at the end that’s meant to stop the blade from getting too deep into the flesh. The ferrule placed at the bottom of the weapon could serve as a club in a desperate situation. There’s no way of telling if it was left here after an unsuccessful hunt, or carried here together with a monster’s victim.\n\n"
        else:
            $ custom1 = "You’re now sure that the spear head is made of iron, but it’s not rusty yet. "
        $ item_mountainroadspear = 1
        $ renpy.notify("You picked the spear.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked the spear.{/i}')
        menu:
            '[custom1]You carry the weapon back to the rock face and push it into the grasses, so it won’t bother you while climbing.
            '
            'I grab the spear.' if not mountainroad_spear_taken:
                jump mountainroadtakingspear01
            'I examine the nearby bones.' if not mountainroad_bones:
                jump mountainroad_bones01
            'I approach the nest.' if not mountainroad_egg_lookedat:
                jump mountainroadnest01
            'My ancestors would leave this egg as it is, and so should I.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My ancestors would leave this egg as it is, and so should I.')
                jump mountainroadnest02d
            'The United Church’s teachings are clear. I need to shatter this egg.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The United Church’s teachings are clear. I need to shatter this egg.')
                jump mountainroadnest02a
            'Maybe shattering this egg will make the beast leave this place.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion != "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe shattering this egg will make the beast leave this place.')
                jump mountainroadnest02a
            'This egg would be worth a fortune in {color=#f6d6bd}Hovlavan{/color}.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_interacted:
                jump mountainroadnest02b
            'Well, maybe someone in the lowlands will buy it.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and mountainroad_egg_interacted:
                jump mountainroadnest02c
            'I have no right to this egg. I leave it behind.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_leftalone and pc_religion != "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have no right to this egg. I leave it behind.')
                jump mountainroadnest02d
            'I climb back up.' if mountainroad_egg_lookedat or mountainroad_spear_taken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb back up.')
                jump mountainroadafterinteraction01

    label mountainroad_bones01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the nearby bones.')
        $ mountainroad_bones = 1
        $ minutes += 5
        menu:
            'You dig through the ribs, spines, femurs, and skulls. You find nothing that could be of use.
            '
            'I grab the spear.' if not mountainroad_spear_taken:
                jump mountainroadtakingspear01
            'I examine the nearby bones.' if not mountainroad_bones:
                jump mountainroad_bones01
            'I approach the nest.' if not mountainroad_egg_lookedat:
                jump mountainroadnest01
            'My ancestors would leave this egg as it is, and so should I.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My ancestors would leave this egg as it is, and so should I.')
                jump mountainroadnest02d
            'The United Church’s teachings are clear. I need to shatter this egg.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The United Church’s teachings are clear. I need to shatter this egg.')
                jump mountainroadnest02a
            'Maybe shattering this egg will make the beast leave this place.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion != "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe shattering this egg will make the beast leave this place.')
                jump mountainroadnest02a
            'This egg would be worth a fortune in {color=#f6d6bd}Hovlavan{/color}.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_interacted:
                jump mountainroadnest02b
            'Well, maybe someone in the lowlands will buy it.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and mountainroad_egg_interacted:
                jump mountainroadnest02c
            'I have no right to this egg. I leave it behind.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_leftalone and pc_religion != "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have no right to this egg. I leave it behind.')
                jump mountainroadnest02d
            'I climb back up.' if mountainroad_egg_lookedat or mountainroad_spear_taken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb back up.')
                jump mountainroadafterinteraction01

    label mountainroadnest01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the nest.')
        $ mountainroad_egg_lookedat = 1
        if pc_religion == "theunitedchurch" or pc_religion == "pagan":
            $ pc_faithpoints_opportunities += 1
        menu:
            'You could easily fit inside and sit down with outstretched legs. It resembles a multi-layered wicker fence, made of branches much larger than the little twigs usually carried by birds, as well as bones and plant stalks. Plenty of light gets through the wall gaps, but the nest’s bedding is much denser, padded with moss and grasses.
            \n\nThe partially buried egg is larger than your head. It’s more oblong than chicken eggs, but of a similar color.
            '
            'I grab the spear.' if not mountainroad_spear_taken:
                jump mountainroadtakingspear01
            'I examine the nearby bones.' if not mountainroad_bones:
                jump mountainroad_bones01
            'I approach the nest.' if not mountainroad_egg_lookedat:
                jump mountainroadnest01
            'My ancestors would leave this egg as it is, and so should I.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My ancestors would leave this egg as it is, and so should I.')
                jump mountainroadnest02d
            'The United Church’s teachings are clear. I need to shatter this egg.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The United Church’s teachings are clear. I need to shatter this egg.')
                jump mountainroadnest02a
            'Maybe shattering this egg will make the beast leave this place.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion != "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe shattering this egg will make the beast leave this place.')
                jump mountainroadnest02a
            'This egg would be worth a fortune in {color=#f6d6bd}Hovlavan{/color}.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_interacted:
                jump mountainroadnest02b
            'Well, maybe someone in the lowlands will buy it.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and mountainroad_egg_interacted:
                jump mountainroadnest02c
            'I have no right to this egg. I leave it behind.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_leftalone and pc_religion != "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have no right to this egg. I leave it behind.')
                jump mountainroadnest02d
            'I climb back up.' if mountainroad_egg_lookedat or mountainroad_spear_taken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb back up.')
                jump mountainroadafterinteraction01

    label mountainroadnest02d:
        if pc_religion == "pagan":
            $ pc_faithpoints += 1
            $ custom1 = "It carries a grateful whisper."
        else:
            $ custom1 = "The wilderness sounds bit more familiar to you."
        $ mountainroad_egg_leftalone = 1
        $ mountainroad_egg_finished = 1
        menu:
            'You step away, touched by a gentle gust of wind. [custom1]
            '
            'I grab the spear.' if not mountainroad_spear_taken:
                jump mountainroadtakingspear01
            'I examine the nearby bones.' if not mountainroad_bones:
                jump mountainroad_bones01
            'I approach the nest.' if not mountainroad_egg_lookedat:
                jump mountainroadnest01
            'My ancestors would leave this egg as it is, and so should I.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My ancestors would leave this egg as it is, and so should I.')
                jump mountainroadnest02d
            'The United Church’s teachings are clear. I need to shatter this egg.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The United Church’s teachings are clear. I need to shatter this egg.')
                jump mountainroadnest02a
            'Maybe shattering this egg will make the beast leave this place.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion != "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe shattering this egg will make the beast leave this place.')
                jump mountainroadnest02a
            'This egg would be worth a fortune in {color=#f6d6bd}Hovlavan{/color}.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_interacted:
                jump mountainroadnest02b
            'Well, maybe someone in the lowlands will buy it.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and mountainroad_egg_interacted:
                jump mountainroadnest02c
            'I have no right to this egg. I leave it behind.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_leftalone and pc_religion != "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have no right to this egg. I leave it behind.')
                jump mountainroadnest02d
            'I climb back up.' if mountainroad_egg_lookedat or mountainroad_spear_taken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb back up.')
                jump mountainroadafterinteraction01

    label mountainroadnest02a:
        if pc_religion == "theunitedchurch":
            $ pc_faithpoints += 1
            $ custom1 = "\n\nAfter a few moments you realize that your breath is fast and shallow, and how your hands are squeezing the wood strongly. You throw it away and climb outside."
        else:
            $ custom1 = " You throw the piece of wood away and climb outside."
        $ mountainroad_egg_broken = 1
        $ mountainroad_egg_finished = 1
        if mountainroad_egg_interacted:
            $ custom2 = ""
        else:
            $ custom2 = " It has been dead for a very long time now."
        show mountainroadegg broken at basicfade
        menu:
            'You look for a heavy stick, something that won’t bend too much. You stand above the egg and crush the shell fiercely, but no whites or yolk spill from it, only a small, dry sphere rolls through the nest.[custom2][custom1]
            '
            'I grab the spear.' if not mountainroad_spear_taken:
                jump mountainroadtakingspear01
            'I examine the nearby bones.' if not mountainroad_bones:
                jump mountainroad_bones01
            'I approach the nest.' if not mountainroad_egg_lookedat:
                jump mountainroadnest01
            'My ancestors would leave this egg as it is, and so should I.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My ancestors would leave this egg as it is, and so should I.')
                jump mountainroadnest02d
            'The United Church’s teachings are clear. I need to shatter this egg.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The United Church’s teachings are clear. I need to shatter this egg.')
                jump mountainroadnest02a
            'Maybe shattering this egg will make the beast leave this place.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion != "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe shattering this egg will make the beast leave this place.')
                jump mountainroadnest02a
            'This egg would be worth a fortune in {color=#f6d6bd}Hovlavan{/color}.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_interacted:
                jump mountainroadnest02b
            'Well, maybe someone in the lowlands will buy it.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and mountainroad_egg_interacted:
                jump mountainroadnest02c
            'I have no right to this egg. I leave it behind.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_leftalone and pc_religion != "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have no right to this egg. I leave it behind.')
                jump mountainroadnest02d
            'I climb back up.' if mountainroad_egg_lookedat or mountainroad_spear_taken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb back up.')
                jump mountainroadafterinteraction01

    label mountainroadnest02b:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- This egg would be worth a fortune in {color=#f6d6bd}Hovlavan{/color}.')
        $ mountainroad_egg_interacted = 1
        menu:
            'You climb inside and put your hands on the egg. You let out a curse - the shell is extraordinarily light, as if it’s completely empty. You lift it up and shake it. The shriveled contents hit against the walls.
            \n\nIt’s not clear to you why a monster would put so much effort into looking after an egg that died months ago, if not years.
            '
            'I grab the spear.' if not mountainroad_spear_taken:
                jump mountainroadtakingspear01
            'I examine the nearby bones.' if not mountainroad_bones:
                jump mountainroad_bones01
            'I approach the nest.' if not mountainroad_egg_lookedat:
                jump mountainroadnest01
            'My ancestors would leave this egg as it is, and so should I.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My ancestors would leave this egg as it is, and so should I.')
                jump mountainroadnest02d
            'The United Church’s teachings are clear. I need to shatter this egg.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The United Church’s teachings are clear. I need to shatter this egg.')
                jump mountainroadnest02a
            'Maybe shattering this egg will make the beast leave this place.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion != "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe shattering this egg will make the beast leave this place.')
                jump mountainroadnest02a
            'This egg would be worth a fortune in {color=#f6d6bd}Hovlavan{/color}.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_interacted:
                jump mountainroadnest02b
            'Well, maybe someone in the lowlands will buy it.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and mountainroad_egg_interacted:
                jump mountainroadnest02c
            'I have no right to this egg. I leave it behind.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_leftalone and pc_religion != "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have no right to this egg. I leave it behind.')
                jump mountainroadnest02d
            'I climb back up.' if mountainroad_egg_lookedat or mountainroad_spear_taken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb back up.')
                jump mountainroadafterinteraction01

    label mountainroadnest02c:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, maybe someone in the lowlands will buy it.')
        $ mountainroad_egg_gone = 1
        $ mountainroad_egg_finished = 1
        show mountainroadegg gone at basicfade
        $ item_griffonegg = 1
        $ renpy.notify("You steal the dead egg.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You steal the dead egg.{/i}')
        menu:
            'For now, you tie it with a few cords, forming a net-like bag. You’ll put it into a box once you reach the saddle.
            '
            'I grab the spear.' if not mountainroad_spear_taken:
                jump mountainroadtakingspear01
            'I examine the nearby bones.' if not mountainroad_bones:
                jump mountainroad_bones01
            'I approach the nest.' if not mountainroad_egg_lookedat:
                jump mountainroadnest01
            'My ancestors would leave this egg as it is, and so should I.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My ancestors would leave this egg as it is, and so should I.')
                jump mountainroadnest02d
            'The United Church’s teachings are clear. I need to shatter this egg.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion == "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The United Church’s teachings are clear. I need to shatter this egg.')
                jump mountainroadnest02a
            'Maybe shattering this egg will make the beast leave this place.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and pc_religion != "theunitedchurch":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe shattering this egg will make the beast leave this place.')
                jump mountainroadnest02a
            'This egg would be worth a fortune in {color=#f6d6bd}Hovlavan{/color}.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_interacted:
                jump mountainroadnest02b
            'Well, maybe someone in the lowlands will buy it.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and mountainroad_egg_interacted:
                jump mountainroadnest02c
            'I have no right to this egg. I leave it behind.' if mountainroad_egg_lookedat and not mountainroad_egg_broken and not mountainroad_egg_gone and not mountainroad_egg_leftalone and not mountainroad_egg_leftalone and pc_religion != "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have no right to this egg. I leave it behind.')
                jump mountainroadnest02d
            'I climb back up.' if mountainroad_egg_lookedat or mountainroad_spear_taken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb back up.')
                jump mountainroadafterinteraction01
