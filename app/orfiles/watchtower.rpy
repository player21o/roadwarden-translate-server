###################### Watchtower
default watchtower_firsttime = 0
default watchtower_fluff = ""
default watchtower_fluff_old = ""

default watchtower_wildplants_start = 10
default watchtower_wildplants_left = 2
default watchtower_wildplants_display = 0

default watchtower_tower_explored = 0
default watchtower_tower_firsttime = 0
default watchtower_tower_keyhole = 0
default watchtower_tower_bugs_cleared = 0

default watchtower_sign = 0
default watchtower_gate = 0
default watchtower_open = 0
default watchtower_trees = 0
default watchtower_tracks = 0
default watchtower_campfire = 0
default watchtower_campfire_fire = 0
default watchtower_campfire_prepared = 1

label watchtower01:
    nvl clear
    $ pc_area = "watchtower"
    # $ renpy.music.play("audio/track_18military.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop music fadeout 4.0
    if not renpy.music.get_playing(channel='nature') == "audio/ambient/watchtower01.ogg":
        play nature "audio/ambient/watchtower01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if watchtower_open == "axe":
        show areapicture watchtower01door at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
    else:
        show areapicture watchtower01 at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
    if eudocia_bronzerod_rodin_watchtower:
        show watchtowerbronzerod at basicfade
    if watchtower_campfire_fire:
        if watchtower_campfire_fire < day:
            if watchtower_campfire_prepared:
                show watchtower_campfire_fire 03 at basicfade
            else:
                show watchtower_campfire_fire 02 at basicfade
        else:
            if watchtower_campfire_prepared:
                show watchtower_campfire_fire 04 at basicfade
            else:
                show watchtower_campfire_fire 01 at basicfade
    else:
        hide watchtower_campfire_fire
    label watchtower_fluffloop:
        $ watchtower_fluff = renpy.random.choice(['The wind is chilly, strong enough to sway the shrubs and trees. You’re surrounded with the fresh scent of needles and plant litter.', 'For a moment, you think that the gate’s position has changed since your last visit, but once you get closer, you’re sure there are no fresh tracks.', 'You’re surrounded by the thunderous humming of trees. The blue-and-black birds are carrying small sticks, leaves, and grass in their beaks, and move these spoils to the roof.', 'A spider the size of a human head crawls up the wall. When it senses your presence, it runs to the top and disappears on the other side.', 'There are small creatures ahead of you, not larger than a hare, running from one side of the road to the other. Before you get to the crossroads, they vanish among the shrubs and bushes, which are now rustling and shaking disquietingly.'])
        if watchtower_fluff_old == watchtower_fluff:
            jump watchtower_fluffloop
        else:
            $ watchtower_fluff_old = watchtower_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if day < watchtower_wildplants_start-24 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 8
    elif day < watchtower_wildplants_start-20 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 7
    elif day < watchtower_wildplants_start-16 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 6
    elif day < watchtower_wildplants_start-12 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 5
    elif day < watchtower_wildplants_start-8 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 4
    elif day < watchtower_wildplants_start-4 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 3
    elif day < watchtower_wildplants_start and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 2
    elif day >= watchtower_wildplants_start and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 1
    else:
        $ watchtower_wildplants_display = 0
    if watchtower_firsttime < 2:
        $ world_known_areas += 1
        $ watchtower_firsttime = 2
        $ easternbridgeunlocked = 1
        $ easternshortcut_entranceunlocked = 1
        $ fallentree_unlocked = 1
        $ eudociahouse_unlocked = 1
        $ stonebridge_unlocked = 1
        $ stonesign_unlocked = 1
        jump watchtowerfirsttime01
    elif elah_quest_easternpath_lumberjacks == 1:
        jump creekselahaboutquesteasternroadfallentree07
    else:
        jump watchtowerregular01

label watchtowerfirsttime01:
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if persistent.deafmode:
        $ deafcustom1 = "You struggle to ignore the overwhelming layers of the howling wilderness - the birds, insects, monkeys, windblown leaves. It takes some time before you isolate the more distant roaring of large monsters from the west, hidden in the deep forests of the lowland, the realm of no humans. Still, you don’t hear anything coming from the watchtower.\n\n"
    else:
        $ deafcustom1 = "While the hills are full of life, you don’t hear anything coming from the watchtower. "
    menu:
        '[deafcustom1]Its upper level lacks a wooden platform from which the guards could fire their crossbows or drop stones on the opponents below, so this place was not meant to be used in combat, but rather as a shelter from claws and fangs.
        \n\nSuch structures can be found in especially untamed parts of The Dragonwoods, used occasionally by travelers or patrolling squads. Since the end of the war, The Cities can’t find enough people and dragon bones to keep them in good shape.
        \n\nYou see no footsteps, no lights, no fresh trash or a latrine. The birds are preening their feathers on the top of the tower, while the branches of nearby trees are swaying in the fierce, cold wind.
        '
        'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ): # ropehook
            jump watchtowerinstallingrod01alt
        'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
            pass
        'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
            pass
        'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
            jump watchtowertracks01
        'I approach the entrance.' if not watchtower_open:
            jump watchtowerdoor01
        'I enter the tower.' if watchtower_open:
            jump watchtowerentrance01
        'I take a look at the signpost.':
            jump watchtower_signpost01
        'I walk to the gate.' if not watchtower_gate:
            jump watchtower_gate01
        'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
            jump watchtower_trees01
        'I examine the campfire spot at the fence.' if not watchtower_campfire:
            jump watchtower_campfire01
        'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
            jump watchtower_campfire01a
        'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
            pass
        'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
            jump watchtowerforaging01
        'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
            pass
        'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
            pass
        'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
            pass
        'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
            pass
        'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
            pass
        'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
            pass
        'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
            pass

label watchtowerregular01:
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'The watchtower is blending with the wilderness slowly. [watchtower_fluff]
        '
        'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
            jump watchtowerinstallingrod01alt
        'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
            pass
        'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
            pass
        'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
            jump watchtowertracks01
        'I approach the entrance.' if not watchtower_open:
            jump watchtowerdoor01
        'I enter the tower.' if watchtower_open:
            jump watchtowerentrance01
        'I take a look at the signpost.':
            jump watchtower_signpost01
        'I walk to the gate.' if not watchtower_gate:
            jump watchtower_gate01
        'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
            jump watchtower_trees01
        'I examine the campfire spot at the fence.' if not watchtower_campfire:
            jump watchtower_campfire01
        'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
            jump watchtower_campfire01a
        'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
            pass
        'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
            jump watchtowerforaging01
        'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
            pass
        'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
            pass
        'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
            pass
        'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
            pass
        'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
            pass
        'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
            pass
        'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
            pass

label watchtowerafterinteraction01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if watchtower_open == "axe":
        show areapicture watchtower01door at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
    else:
        show areapicture watchtower01 at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
    if eudocia_bronzerod_rodin_watchtower:
        show watchtowerbronzerod at basicfade
    if watchtower_campfire_fire:
        if watchtower_campfire_fire < day:
            if watchtower_campfire_prepared:
                show watchtower_campfire_fire 03 at basicfade
            else:
                show watchtower_campfire_fire 02 at basicfade
        else:
            if watchtower_campfire_prepared:
                show watchtower_campfire_fire 04 at basicfade
            else:
                show watchtower_campfire_fire 01 at basicfade
    else:
        hide watchtower_campfire_fire
    menu:
        'You’re standing at the crossroads.
        '
        'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
            jump watchtowerinstallingrod01alt
        'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
            pass
        'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
            pass
        'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
            jump watchtowertracks01
        'I approach the entrance.' if not watchtower_open:
            jump watchtowerdoor01
        'I enter the tower.' if watchtower_open:
            jump watchtowerentrance01
        'I take a look at the signpost.':
            jump watchtower_signpost01
        'I walk to the gate.' if not watchtower_gate:
            jump watchtower_gate01
        'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
            jump watchtower_trees01
        'I examine the campfire spot at the fence.' if not watchtower_campfire:
            jump watchtower_campfire01
        'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
            jump watchtower_campfire01a
        'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
            pass
        'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
            jump watchtowerforaging01
        'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
            pass
        'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
            pass
        'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
            pass
        'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
            pass
        'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
            pass
        'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
            pass
        'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
            pass

label watchtoweraftersleep01:
    if watchtower_open == "axe":
        show areapicture watchtower01door at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
    else:
        show areapicture watchtower01 at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
    if eudocia_bronzerod_rodin_watchtower:
        show watchtowerbronzerod at basicfade
    if watchtower_campfire_fire:
        if watchtower_campfire_fire < day:
            if watchtower_campfire_prepared:
                show watchtower_campfire_fire 03 at basicfade
            else:
                show watchtower_campfire_fire 02 at basicfade
        else:
            if watchtower_campfire_prepared:
                show watchtower_campfire_fire 04 at basicfade
            else:
                show watchtower_campfire_fire 01 at basicfade
    else:
        hide watchtower_campfire_fire
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    # $ renpy.music.play("audio/track_18military.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop music fadeout 4.0
    play nature "audio/ambient/watchtower01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if day < watchtower_wildplants_start-24 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 8
    elif day < watchtower_wildplants_start-20 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 7
    elif day < watchtower_wildplants_start-16 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 6
    elif day < watchtower_wildplants_start-12 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 5
    elif day < watchtower_wildplants_start-8 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 4
    elif day < watchtower_wildplants_start-4 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 3
    elif day < watchtower_wildplants_start and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 2
    elif day >= watchtower_wildplants_start and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 1
    else:
        $ watchtower_wildplants_display = 0
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    if watchtower_open == "key":
        $ quarters += 4
        if pc_likeshorsename:
            $ custom1 = "is observing you patiently, unmoved by the commotion."
        else:
            $ custom1 = "seems to be frustrated as well, traipsing near the door and snorting, constantly shifting the position of its head."
        if not cleanliness_clothes_torn:
            $ cleanliness_clothes_torn = 1
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
        menu:
            'You open your eyes and there’s an unpleasant tingling on your cheek. You reach for what turns out to be a small bug. You throw it away and look around, only to see dozens of tiny creatures swarming on the floor and the bed, as well as your blanket, clothes, and bags. You push some of them away, gathering your things, with thoughts still clouded by dreams. You gather your things and look through the bags, removing as many insects, worms, and spiders from them as you can find.
            \n\n{color=#f6d6bd}[horsename]{/color} [custom1] You walk it outside and allow it to graze on the grass for half an hour. In the meantime, you equip it with your riding set, and use the sunlight to double-check your belongings. The thought that no matter how scrupulous you are, you may keep finding new creatures in your food doesn’t leave you alone.
            '
            'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
                jump watchtowerinstallingrod01alt
            'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
                pass
            'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
                pass
            'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
                jump watchtowertracks01
            'I approach the entrance.' if not watchtower_open:
                jump watchtowerdoor01
            'I enter the tower.' if watchtower_open:
                jump watchtowerentrance01
            'I take a look at the signpost.':
                jump watchtower_signpost01
            'I walk to the gate.' if not watchtower_gate:
                jump watchtower_gate01
            'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
                jump watchtower_trees01
            'I examine the campfire spot at the fence.' if not watchtower_campfire:
                jump watchtower_campfire01
            'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
                jump watchtower_campfire01a
            'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
                pass
            'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
                jump watchtowerforaging01
            'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
                pass
            'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
                pass
            'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
                pass
            'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
                pass
            'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
                pass
            'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
                pass
            'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
                pass
    if watchtower_open == "axe":
        $ quarters += 5
        if pc_likeshorsename:
            $ custom1 = "is observing you patiently, unmoved by the commotion."
        else:
            $ custom1 = "seems to be frustrated as well, traipsing near the door and snorting, constantly shifting the position of its head."
        if not cleanliness_clothes_torn:
            $ cleanliness_clothes_torn = 1
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
        menu:
            'You open your eyes and there’s this unpleasant tingling on your cheek. You reach for what turns out to be a small bug. You throw it away and look around, only to see dozens of tiny creatures swarming on the floor and the bed, as well as your blanket, clothes, and bags. You push some of them away, gathering your things, with thoughts still clouded by dreams. You gather your things and look through the bags, removing as many insects, worms, and spiders from them as you can find.
            \n\n[horsename] [custom1] You push away all the furniture that you used to barricade the door, walk your palfrey outside, and allow it to graze on the grass for half an hour. In the meantime, you equip it with your riding set, and use the sunlight to double-check your belongings. The thought that no matter how scrupulous you are, you may keep finding new creatures in your food doesn’t leave you alone.
            '
            'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
                jump watchtowerinstallingrod01alt
            'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
                pass
            'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
                pass
            'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
                jump watchtowertracks01
            'I approach the entrance.' if not watchtower_open:
                jump watchtowerdoor01
            'I enter the tower.' if watchtower_open:
                jump watchtowerentrance01
            'I take a look at the signpost.':
                jump watchtower_signpost01
            'I walk to the gate.' if not watchtower_gate:
                jump watchtower_gate01
            'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
                jump watchtower_trees01
            'I examine the campfire spot at the fence.' if not watchtower_campfire:
                jump watchtower_campfire01
            'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
                jump watchtower_campfire01a
            'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
                pass
            'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
                jump watchtowerforaging01
            'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
                pass
            'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
                pass
            'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
                pass
            'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
                pass
            'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
                pass
            'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
                pass
            'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
                pass

label watchtoweraftersleep01nobugs:
    if watchtower_open == "axe":
        show areapicture watchtower01door at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
    else:
        show areapicture watchtower01 at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
    if eudocia_bronzerod_rodin_watchtower:
        show watchtowerbronzerod at basicfade
    if watchtower_campfire_fire:
        if watchtower_campfire_fire < day:
            if watchtower_campfire_prepared:
                show watchtower_campfire_fire 03 at basicfade
            else:
                show watchtower_campfire_fire 02 at basicfade
        else:
            if watchtower_campfire_prepared:
                show watchtower_campfire_fire 04 at basicfade
            else:
                show watchtower_campfire_fire 01 at basicfade
    else:
        hide watchtower_campfire_fire
    # $ renpy.music.play("audio/track_18military.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop music fadeout 4.0
    play nature "audio/ambient/watchtower01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if day < watchtower_wildplants_start-24 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 8
    elif day < watchtower_wildplants_start-20 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 7
    elif day < watchtower_wildplants_start-16 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 6
    elif day < watchtower_wildplants_start-12 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 5
    elif day < watchtower_wildplants_start-8 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 4
    elif day < watchtower_wildplants_start-4 and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 3
    elif day < watchtower_wildplants_start and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 2
    elif day >= watchtower_wildplants_start and watchtower_wildplants_left:
        $ watchtower_wildplants_display = 1
    else:
        $ watchtower_wildplants_display = 0
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    if watchtower_open == "key":
        $ quarters += 2
        if pc_likeshorsename:
            $ custom1 = "is napping. You walk it outside, allowing it to graze on the grass for half an hour. You place all your riding equipment on it and check your belongings."
        else:
            $ custom1 = "stands right next to the door, with its ears pointing back, as if it’s already annoyed with you. You walk it outside and allow it to graze on the grass for half an hour. You place all your riding equipment on it, then check your belongings."
        menu:
            'You wake up in silence, barely hearing the wind outside the tower walls. You gather your things and climb down to where {color=#f6d6bd}[horsename]{/color} [custom1] Thankfully, you find no sign of bugs.
            '
            'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
                jump watchtowerinstallingrod01alt
            'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
                pass
            'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
                pass
            'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
                jump watchtowertracks01
            'I approach the entrance.' if not watchtower_open:
                jump watchtowerdoor01
            'I enter the tower.' if watchtower_open:
                jump watchtowerentrance01
            'I take a look at the signpost.':
                jump watchtower_signpost01
            'I walk to the gate.' if not watchtower_gate:
                jump watchtower_gate01
            'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
                jump watchtower_trees01
            'I examine the campfire spot at the fence.' if not watchtower_campfire:
                jump watchtower_campfire01
            'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
                jump watchtower_campfire01a
            'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
                pass
            'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
                jump watchtowerforaging01
            'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
                pass
            'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
                pass
            'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
                pass
            'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
                pass
            'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
                pass
            'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
                pass
            'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
                pass
    else:
        $ quarters += 3
        if pc_likeshorsename:
            $ custom1 = "is napping. You push away all the furniture that you used to barricade the door and finally walk your mount outside."
        else:
            $ custom1 = "is standing right next to the door, with its ears pointing back, as if it’s already annoyed with you. You push away all the furniture that you used to barricade the door and finally walk your mount outside."
        menu:
            'You wake up in silence, barely hearing the wind outside the tower walls. You gather your things and climb down, where {color=#f6d6bd}[horsename]{/color} [custom1] You allow it to graze on the grass for half an hour and you place all your riding equipment on it, then check your belongings. Thankfully, you find no sign of bugs.
            '
            'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
                jump watchtowerinstallingrod01alt
            'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
                pass
            'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
                pass
            'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
                jump watchtowertracks01
            'I approach the entrance.' if not watchtower_open:
                jump watchtowerdoor01
            'I enter the tower.' if watchtower_open:
                jump watchtowerentrance01
            'I take a look at the signpost.':
                jump watchtower_signpost01
            'I walk to the gate.' if not watchtower_gate:
                jump watchtower_gate01
            'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
                jump watchtower_trees01
            'I examine the campfire spot at the fence.' if not watchtower_campfire:
                jump watchtower_campfire01
            'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
                jump watchtower_campfire01a
            'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
                pass
            'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
                jump watchtowerforaging01
            'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
                pass
            'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
                pass
            'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
                pass
            'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
                pass
            'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
                pass
            'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
                pass
            'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
                pass

label watchtowertracks01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for the tracks I saw near the fallen tree.')
    $ watchtower_tracks = 1
    if quest_fallentree == 1:
        $ renpy.notify("Journal updated: Fallen Tree")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Fallen Tree{/i}')
    $ quest_fallentree_description02 = "Whoever was present at the wagon, was then passing by the abandoned watchtower. They’ve gone west."
    menu:
        'The tracks lead here, through the narrow gate, then west. The hard heels are especially noticeable.
        '
        'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
            jump watchtowerinstallingrod01alt
        'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
            pass
        'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
            pass
        'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
            jump watchtowertracks01
        'I approach the entrance.' if not watchtower_open:
            jump watchtowerdoor01
        'I enter the tower.' if watchtower_open:
            jump watchtowerentrance01
        'I take a look at the signpost.':
            jump watchtower_signpost01
        'I walk to the gate.' if not watchtower_gate:
            jump watchtower_gate01
        'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
            jump watchtower_trees01
        'I examine the campfire spot at the fence.' if not watchtower_campfire:
            jump watchtower_campfire01
        'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
            jump watchtower_campfire01a
        'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
            pass
        'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
            jump watchtowerforaging01
        'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
            pass
        'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
            pass
        'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
            pass
        'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
            pass
        'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
            pass
        'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
            pass
        'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
            pass

label watchtower_signpost01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a look at the signpost.')
    $ watchtower_sign = 1
    if watchtower_campfire and watchtower_trees and watchtower_gate and watchtower_sign and watchtower_open and not watchtower_tower_explored:
        $ watchtower_tower_explored = 1
    if pc_class == "scholar":
        menu:
            'The wood and letters are damaged by decades of rains, frosts, borers, claws, and mosses. You scratch off some of the moss. The plank on the top points both toward the watchtower, where the letters spell {i}south{/i}, and away from it, with the additionally carved {i}north{/i}.
            \n\nThe one beneath it points east and this time you see a tidily written word, painted on the wood in blue: {i}enchanting{/i}. In {color=#f6d6bd}Hovlavan{/color}, {i}enchanters{/i} are artisans specialized in filling ordinary items with magical pneuma and sure enough, the “arrow” here looks more like a magic wand.
            \n\nThe bottom plank, pointing west, has a picture of a tall tower on it, surrounded by little houses. The carving spells {i}monastery{/i}, but the wood is covered in red paint, suggesting danger.
            '
            'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
                jump watchtowerinstallingrod01alt
            'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
                pass
            'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
                pass
            'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
                jump watchtowertracks01
            'I approach the entrance.' if not watchtower_open:
                jump watchtowerdoor01
            'I enter the tower.' if watchtower_open:
                jump watchtowerentrance01
            'I walk to the gate.' if not watchtower_gate:
                jump watchtower_gate01
            'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
                jump watchtower_trees01
            'I examine the campfire spot at the fence.' if not watchtower_campfire:
                jump watchtower_campfire01
            'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
                jump watchtower_campfire01a
            'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
                pass
            'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
                jump watchtowerforaging01
            'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
                pass
            'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
                pass
            'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
                pass
            'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
                pass
            'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
                pass
            'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
                pass
            'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
                pass
    else:
        menu:
            'The planks and letters are damaged by decades of rains, frosts, borers, and claws. You scratch off some of the moss. There are three planks on the signpost, each one pointing in a different direction. The letters don’t tell you anything.
            \n\nThe plank on the top points both south and north, but there are no pictures that would tell you anything more than that. The one beneath it points east, and there’s a word written in blue paint. The “arrow” here looks more like a magic wand. The bottom plank has a picture of a tall tower surrounded by little houses, and points west. The wood is covered in red paint, suggesting danger.
            '
            'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
                jump watchtowerinstallingrod01alt
            'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
                pass
            'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
                pass
            'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
                jump watchtowertracks01
            'I approach the entrance.' if not watchtower_open:
                jump watchtowerdoor01
            'I enter the tower.' if watchtower_open:
                jump watchtowerentrance01
            'I walk to the gate.' if not watchtower_gate:
                jump watchtower_gate01
            'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
                jump watchtower_trees01
            'I examine the campfire spot at the fence.' if not watchtower_campfire:
                jump watchtower_campfire01
            'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
                jump watchtower_campfire01a
            'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
                pass
            'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
                jump watchtowerforaging01
            'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
                pass
            'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
                pass
            'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
                pass
            'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
                pass
            'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
                pass
            'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
                pass
            'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
                pass

label watchtower_gate01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk to the gate.')
    $ watchtower_gate = 1
    if watchtower_campfire and watchtower_trees and watchtower_gate and watchtower_sign and watchtower_open and not watchtower_tower_explored:
        $ watchtower_tower_explored = 1
    menu:
        'Setting up a firm wall in a place like this is a bit unusual. It goes on for no more than forty feet, until it connects with a natural rock face. Such a structure could be found near the city, acting as a checkpoint at which to stop any travelers to search through their belongings or request a fee.
        \n\nBut in the middle of nowhere? Deer and other animals, used to running here with no hindrance, must have been more than annoyed. A risky investment.
        \n\nYou touch the gate made of a high-quality wood, previously soaked in oil, now mostly wiped-off. It was left open and you don’t see any wooden bar that would be used to lock it. You try to move the cold planks, buried in dried-out mud, but with no luck - it would require some wearying digging.
        '
        'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
            jump watchtowerinstallingrod01alt
        'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
            pass
        'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
            pass
        'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
            jump watchtowertracks01
        'I approach the entrance.' if not watchtower_open:
            jump watchtowerdoor01
        'I enter the tower.' if watchtower_open:
            jump watchtowerentrance01
        'I take a look at the signpost.':
            jump watchtower_signpost01
        'I walk to the gate.' if not watchtower_gate:
            jump watchtower_gate01
        'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
            jump watchtower_trees01
        'I examine the campfire spot at the fence.' if not watchtower_campfire:
            jump watchtower_campfire01
        'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
            jump watchtower_campfire01a
        'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
            pass
        'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
            jump watchtowerforaging01
        'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
            pass
        'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
            pass
        'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
            pass
        'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
            pass
        'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
            pass
        'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
            pass
        'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
            pass

label watchtower_trees01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe there’s something interesting among the spruce trees.')
    $ watchtower_trees = 1
    if watchtower_campfire and watchtower_trees and watchtower_gate and watchtower_sign and watchtower_open and not watchtower_tower_explored:
        $ watchtower_tower_explored = 1
    menu:
        'It must be a human-made copse. Only the smallest of the spruces are out of order, born of wild seeds. The largest trees are as tall as the tower itself, which surely doesn’t help those who were meant to observe their surroundings. There are also some stumps, most of which used to belong to young saplings.
        \n\nThese trees were likely meant to be sold to carpenters and coopers, but they were left alone many years ago.
        \n\nIn the copse, you find wild fennel and lettuce, thriving in shadows, and there are pears and berries growing among nearby trees and shrubs.
        '
        'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
            jump watchtowerinstallingrod01alt
        'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
            pass
        'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
            pass
        'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
            jump watchtowertracks01
        'I approach the entrance.' if not watchtower_open:
            jump watchtowerdoor01
        'I enter the tower.' if watchtower_open:
            jump watchtowerentrance01
        'I take a look at the signpost.':
            jump watchtower_signpost01
        'I walk to the gate.' if not watchtower_gate:
            jump watchtower_gate01
        'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
            jump watchtower_trees01
        'I examine the campfire spot at the fence.' if not watchtower_campfire:
            jump watchtower_campfire01
        'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
            jump watchtower_campfire01a
        'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
            pass
        'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
            jump watchtowerforaging01
        'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
            pass
        'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
            pass
        'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
            pass
        'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
            pass
        'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
            pass
        'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
            pass
        'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
            pass

label watchtower_campfire01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the campfire spot at the fence.')
    $ watchtower_campfire = 1
    if watchtower_campfire and watchtower_trees and watchtower_gate and watchtower_sign and watchtower_open and not watchtower_tower_explored:
        $ watchtower_tower_explored = 1
    if watchtower_tower_firsttime:
        $ custom1 = ", even when it’s locked"
    else:
        $ custom1 = ""
    menu:
        'You see a shattered bowl, the remains of a meal from many years ago. However, the firewood and the lonely stool are not too old. You don’t doubt that the watchtower seems less threatening to wayfarers than the wilderness around it[custom1].
        '
        'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
            jump watchtowerinstallingrod01alt
        'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
            pass
        'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
            pass
        'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
            jump watchtowertracks01
        'I approach the entrance.' if not watchtower_open:
            jump watchtowerdoor01
        'I enter the tower.' if watchtower_open:
            jump watchtowerentrance01
        'I take a look at the signpost.':
            jump watchtower_signpost01
        'I walk to the gate.' if not watchtower_gate:
            jump watchtower_gate01
        'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
            jump watchtower_trees01
        'I examine the campfire spot at the fence.' if not watchtower_campfire:
            jump watchtower_campfire01
        'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
            jump watchtower_campfire01a
        'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
            pass
        'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
            jump watchtowerforaging01
        'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
            pass
        'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
            pass
        'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
            pass
        'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
            pass
        'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
            pass
        'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
            pass
        'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
            pass

label watchtowerdoorALL:
    label watchtowerdoor01:
        if not watchtower_tower_firsttime:
            $ watchtower_tower_firsttime = 1
            menu:
                'You take a look at {color=#f6d6bd}[horsename]{/color}. If necessary, it could bow its head and walk inside. This place should be a decent shelter for both of you.
                \n\nThe planks are strong, heavy, well protected from rain and wind, and when you knock, they seem to be thick. While the door shakes at your push, it won’t open. Defensive structures usually have a locking bar on the inner side, but you also see a large keyhole.
                \n\nYou walk around the tower, making sure there are no open windows or other entrances. It doesn’t look like you can get in without destroying the door, and doing so is going to make a potential entryway for wild creatures.
                '
                'I don’t have a key. (disabled)' if not item_watchtowerkey and not item_asterionkey:
                    pass
                'I use the key from {color=#f6d6bd}Gale Rocks{/color}.' if item_watchtowerkey:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use the key from {color=#f6d6bd}Gale Rocks{/color}.')
                    $ watchtower_open = "key"
                    jump watchtowerdoor02openkey
                'I try {color=#f6d6bd}Asterion’s{/color} key.' if item_asterionkey:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try {color=#f6d6bd}Asterion’s{/color} key.')
                    $ watchtower_open = "key"
                    jump watchtowerdoor02openkey
                'I look through the keyhole.' if not watchtower_tower_keyhole:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look through the keyhole.')
                    $ watchtower_tower_keyhole = 1
                    jump watchtowerdoor01keyhole
                'I’m too weak to destroy the door. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1" ):
                    pass
                'I take my axe and break through.' ( condition="pc_hp >= 2" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take my axe and break through.')
                    $ watchtower_open = "axe"
                    $ achievement_breakingstuff_points += 1
                    $ quarters += 1
                    jump watchtowerdoor02openaxe
                'I use The Tool of Destruction to break through.' if item_magicchisel == 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use The Tool of Destruction to break through.')
                    $ watchtower_open = "axe"
                    $ achievement_breakingstuff_points += 1
                    jump watchtowerdoor02openchisel
                'I return to the crossroads.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the crossroads.')
                    jump watchtowerafterinteraction01
        else:
            menu:
                'The door is locked. Without destroying the door, it doesn’t look like you can get inside - and after breaking through, you’re going to make it much easier for potential predators to get inside.
                '
                'I don’t have a key. (disabled)' if not item_watchtowerkey and not item_asterionkey:
                    pass
                'I use the key from {color=#f6d6bd}Gale Rocks{/color}.' if item_watchtowerkey:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use the key from {color=#f6d6bd}Gale Rocks{/color}.')
                    $ watchtower_open = "key"
                    jump watchtowerdoor02openkey
                'I try {color=#f6d6bd}Asterion’s{/color} key.' if item_asterionkey:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try {color=#f6d6bd}Asterion’s{/color} key.')
                    $ watchtower_open = "key"
                    jump watchtowerdoor02openkey
                'I look through the keyhole.' if not watchtower_tower_keyhole:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look through the keyhole.')
                    $ watchtower_tower_keyhole = 1
                    jump watchtowerdoor01keyhole
                'I’m too weak to destroy the door. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1" ):
                    pass
                'I take my axe and break through.' ( condition="pc_hp >= 2" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take my axe and break through.')
                    $ watchtower_open = "axe"
                    $ achievement_breakingstuff_points += 1
                    $ quarters += 1
                    jump watchtowerdoor02openaxe
                'I use The Tool of Destruction to break through.' if item_magicchisel == 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use The Tool of Destruction to break through.')
                    $ watchtower_open = "axe"
                    $ achievement_breakingstuff_points += 1
                    jump watchtowerdoor02openchisel
                'I return to the crossroads.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the crossroads.')
                    jump watchtowerafterinteraction01

    label watchtowerdoor01keyhole:
        menu:
            'You kneel down and take a peek. There’s nothing in the hole, but the room is dark, with tiny bits of light passing through the crevices of the windows. You see the shapes of wooden furniture, like tables, casks, and a ladder, but the only movement you notice belongs to the dust dancing in sunbeams.
            '
            'I don’t have a key. (disabled)' if not item_watchtowerkey and not item_asterionkey:
                pass
            'I use the key from {color=#f6d6bd}Gale Rocks{/color}.' if item_watchtowerkey:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use the key from {color=#f6d6bd}Gale Rocks{/color}.')
                $ watchtower_open = "key"
                jump watchtowerdoor02openkey
            'I try {color=#f6d6bd}Asterion’s{/color} key.' if item_asterionkey:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try {color=#f6d6bd}Asterion’s{/color} key.')
                $ watchtower_open = "key"
                jump watchtowerdoor02openkey
            'I’m too weak to destroy the door. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1" ):
                pass
            'I take my axe and break through.' ( condition="pc_hp >= 2" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take my axe and break through.')
                $ watchtower_open = "axe"
                $ achievement_breakingstuff_points += 1
                $ quarters += 1
                jump watchtowerdoor02openaxe
            'I use The Tool of Destruction to break through.' if item_magicchisel == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use The Tool of Destruction to break through.')
                $ watchtower_open = "axe"
                $ achievement_breakingstuff_points += 1
                jump watchtowerdoor02openchisel
            'I return to the crossroads.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the crossroads.')
                jump watchtowerafterinteraction01

    label watchtowerdoor02openkey:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ renpy.notify("New shelter unlocked.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
        menu:
            'It goes in smoothly and after a bit of fidgeting, you find the right spot. You hear the heavy mechanism giving in to your will, followed by the creaking of rusty hinges. An empty table stands in the middle of a large, round room filled with dusty furniture. Without the opened door you’d struggle to see anything.
            '
            'I wait to make sure there’s nothing trying to jump on me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait to make sure there’s nothing trying to jump on me.')
                jump watchtowerdoor03

    label watchtowerdoor02openaxe:
        $ quarters += 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ renpy.notify("New shelter unlocked.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
        if watchtower_open == "axe":
            show areapicture watchtower01door at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
        else:
            show areapicture watchtower01 at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
        if eudocia_bronzerod_rodin_watchtower:
            show watchtowerbronzerod at basicfade
        if watchtower_campfire_fire:
            if watchtower_campfire_fire < day:
                if watchtower_campfire_prepared:
                    show watchtower_campfire_fire 03 at basicfade
                else:
                    show watchtower_campfire_fire 02 at basicfade
            else:
                if watchtower_campfire_prepared:
                    show watchtower_campfire_fire 04 at basicfade
                else:
                    show watchtower_campfire_fire 01 at basicfade
        else:
            hide watchtower_campfire_fire
        menu:
            'You start chopping the door in a spot where two planks are connected to one another. It takes a bit of time and some precision, especially since you struggle to find the right angle to take a swing. Finally, the wood cracks. When you push it, it lets out the dizzy creaking of rusty hinges. An empty table stands in the middle of a large, round room filled with dusty furniture.
            \n\nWithout the opened door you’d struggle to see anything. You wait to be sure that nothing tries to jump on you and finally hide your weapon.
            '
            'I need to remember to sharpen it later on.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to remember to sharpen it later on.')
                jump watchtowerdoor03

    label watchtowerdoor02openchisel:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ renpy.notify("New shelter unlocked.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
        if watchtower_open == "axe":
            show areapicture watchtower01door at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
        else:
            show areapicture watchtower01 at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
        if eudocia_bronzerod_rodin_watchtower:
            show watchtowerbronzerod at basicfade
        if watchtower_campfire_fire:
            if watchtower_campfire_fire < day:
                if watchtower_campfire_prepared:
                    show watchtower_campfire_fire 03 at basicfade
                else:
                    show watchtower_campfire_fire 02 at basicfade
            else:
                if watchtower_campfire_prepared:
                    show watchtower_campfire_fire 04 at basicfade
                else:
                    show watchtower_campfire_fire 01 at basicfade
        else:
            hide watchtower_campfire_fire
        menu:
            'You grab the chisel and a large rock that you found outside. You appose it to the lock and it takes only two good strikes before it cracks and falls inside, causing a couple of wooden planks to break in half. When you push the door, there’s the dizzy creaking of rusty hinges. An empty table stands in the middle of a large, round room filled with dusty furniture. Without the opened door you’d struggle to see anything.
            '
            'I wait to make sure there’s nothing trying to jump on me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait to make sure there’s nothing trying to jump on me.')
                jump watchtowerdoor03

    label watchtowerdoor03:
        if watchtower_open == "axe":
            show areapicture watchtower01insidedoor at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
        else:
            show areapicture watchtower01inside at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
        if eudocia_bronzerod_rodin_watchtower:
            show watchtowerbronzerod at basicfade
        if watchtower_campfire and watchtower_trees and watchtower_gate and watchtower_sign and watchtower_open and not watchtower_tower_explored:
            $ watchtower_tower_explored = 1
        $ quest_explorepeninsula_description05 = "I found an abandoned watchtower set near the eastern road. It needs some renovations, but could easily be turned into a military post."
        $ renpy.notify("Journal updated: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
        menu:
            'The first thing you notice is that the room isn’t high and, just like the windows suggested, there’s the second floor above it. The scent sparks an image of a cellar, humid, but without much mustiness. Tree stumps, used as stools, surround a round table in the center, now covered in dust. The shelves are empty, with no tools left behind, and you see a couple of dishes laying in various spots, empty, sticky.
            \n\nThe bugs are crawling both on the furniture and near the walls. Spiders, roaches, worms... You think about taking a look into one of the casks, but the smell coming from it makes you change your plans. Instead, you climb up the ladder.
            \n\nThe view there isn’t much different. The floor is covered with pieces of trash, dirty furniture, and sleeping pallets, which are moist, smelly, and full of wriggling and chirping creatures.
            '
            'I don’t care about some bugs. I just need to ignore them.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care about some bugs. I just need to forget about them.')
                jump watchtowerdoor04
            'It gives me shivers. I try to not look at them.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It gives me shivers. I try to not look at them.')
                jump watchtowerdoor04

    label watchtowerdoor04:
        $ at = 0
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if quarters < (world_daylength-4):
            $ custom1 = "is looking at the grass outside, still touched by sunlight."
        else:
            $ custom1 = "is standing as far away from the dark exit as possible, afraid of what may come inside."
        menu:
            'You climb down. {color=#f6d6bd}[horsename]{/color} [custom1] You approach the windows, each one locked with two heavy, wooden bars. Opening them would not be a problem, but knocking them down from the outside won’t be an easy task.
            \n\nYou sigh with relief. It’s a safe place.
            '
            'Following the clue from {color=#f6d6bd}Old Págos{/color}, I look for anything that {color=#f6d6bd}Asterion{/color} could have left behind.' if not item_asteriontablet and quest_asterion_description08:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Following the clue from {color=#f6d6bd}Old Págos{/color}, I look for anything that {color=#f6d6bd}Asterion{/color} could have left behind.')
                $ at = 0
                jump watchtolookingforasterionsitems01
            'I don’t have anything that would help me get rid of these bugs. (disabled)' if not item_bugrepellent and not watchtower_tower_bugs_cleared and pc_class != "scholar":
                pass
            'I should spread the bug repellent around. At least they won’t bother me in my sleep.' if item_bugrepellent and not watchtower_tower_bugs_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should spread the bug repellent around. At least they won’t bother me in my sleep.')
                $ watchtower_tower_bugs_cleared = 1
                $ at = 0
                $ item_bugrepellent = 0
                $ quarters += 2
                jump watchtower_tower_bugs_clearedfinish
            'With access to an alchemy table, I could prepare an herbal bug repellent. (disabled)' ( condition="not item_bugrepellent and not watchtower_tower_bugs_cleared and pc_class == 'scholar'"):
                pass
            'I could open the trapdoor and leave a bronze rod on the roof.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could open the trapdoor and leave a bronze rod on the roof.')
                $ at = 0
                jump watchtowerinstallingrod01
            'I go outside.' ( condition="quarters < world_daylength" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                $ at = 0
                jump watchtowerafterinteraction01
            'It’s too late for me to go outside. (disabled)' ( condition="quarters >= world_daylength" ):
                pass

label watchtolookingforasterionsitems01:
    if pc_class == "scholar":
        $ at_unlock_knowledge = 1
        $ at = 0
    $ item_asteriontablet = 1
    $ renpy.notify("You found a wax tablet.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a wax tablet.{/i}')
    $ quarters += 2
    menu:
        'You start to move around all sorts of furniture, light and heavy. Among various pieces of garbage that you have to push aside, you find something unusual in the space between one of the pallets and the wall - an old, molding, wax tablet. There are some writings inside it.
        \n\nOther than that, the place seems to be empty, unless you count broken pottery and ragged clothes.
        '
        'For now, I hide it in my bag and put everything back in its place. Time to wash my hands.' ( condition="at != 'knowledge'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For now, I hide it in my bag and put everything back in its place. Time to wash my hands.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump watchtowerentrance01
        'I open it and take a closer look.' ( condition="at == 'knowledge'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- For now, I hide it in my bag and put everything back in its place. Time to wash my hands.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump watchtolookingforasterionsitems02

    label watchtolookingforasterionsitems02:
        $ item_asteriontablet_read = 1
        $ asterion_highisland_clues += 1
        if quest_asterion == 1 and not asterion_found and asterion_highisland_clues >= 3:
            $ renpy.notify("Journal updated: Find the Roadwarden")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
        menu:
            'As far as you can tell, the tablet is filled with small pictures and chaotic notes focused on the construction of boats and oars, as well as on the nature of volcanoes. One word seems to be a name: {i}Navica{/i}.
            '
            'For now, I hide it in my bag and put everything back in its place. Time to wash my hands.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- For now, I hide it in my bag and put everything back in its place. Time to wash my hands.')
                jump watchtowerentrance01

label watchtowerentrance01:
    if watchtower_open == "axe":
        show areapicture watchtower01insidedoor at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
    else:
        show areapicture watchtower01inside at basicfade behind watchtowerbronzerod, watchtower_campfire_fire
    if eudocia_bronzerod_rodin_watchtower:
        show watchtowerbronzerod at basicfade
    if watchtower_campfire and watchtower_trees and watchtower_gate and watchtower_sign and watchtower_open and not watchtower_tower_explored:
        $ watchtower_tower_explored = 1
    $ at = 0
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if watchtower_tower_bugs_cleared:
        $ custom1 = "You’re at the ground floor of the watchtower. It’s weirdly quiet here and you see almost no movement."
    else:
        $ custom1 = "You’re at the ground floor of the watchtower. Dozens of little creatures run away from the new source of light."
    menu:
        '[custom1]
        '
        'Following the clue from {color=#f6d6bd}Old Págos{/color}, I look for anything that {color=#f6d6bd}Asterion{/color} could have left behind.' if not item_asteriontablet and quest_asterion_description08:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Following the clue from {color=#f6d6bd}Old Págos{/color}, I look for anything that {color=#f6d6bd}Asterion{/color} could have left behind.')
            $ at = 0
            jump watchtolookingforasterionsitems01
        'I don’t have anything that would help me get rid of these bugs. (disabled)' if not item_bugrepellent and not watchtower_tower_bugs_cleared and pc_class != "scholar":
            pass
        'I should spread the bug repellent around. At least they won’t bother me in my sleep.' if item_bugrepellent and not watchtower_tower_bugs_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should spread the bug repellent around. At least they won’t bother me in my sleep.')
            $ watchtower_tower_bugs_cleared = 1
            $ at = 0
            $ item_bugrepellent = 0
            $ quarters += 2
            jump watchtower_tower_bugs_clearedfinish
        'With access to an alchemy table, I could prepare an herbal bug repellent. (disabled)' ( condition="not item_bugrepellent and not watchtower_tower_bugs_cleared and pc_class == 'scholar'"):
            pass
        'I could open the trapdoor and leave a bronze rod on the roof.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could open the trapdoor and leave a bronze rod on the roof.')
            $ at = 0
            jump watchtowerinstallingrod01
        'I go outside.' ( condition="quarters < world_daylength" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
            $ at = 0
            jump watchtowerafterinteraction01
        'It’s too late for me to go outside. (disabled)' ( condition="quarters >= world_daylength" ):
            pass

label watchtower_tower_bugs_clearedfinish:
    $ item_bugrepellent = 0
    if item_asteriontablet == 1:
        if watchtower_open == "key":
            if quest_easternpath == 1 and quest_easternpath_description01:
                $ renpy.notify("Journal updated: The Eastern Path")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
            $ quest_easternpath_description08 = "The watchtower is clear and ready for new guards."
        else:
            if quest_easternpath == 1 and quest_easternpath_description01:
                $ renpy.notify("Journal updated: The Eastern Path")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
            $ quest_easternpath_description08alt = "The watchtower is clear, though its door is broken."
        menu:
            'You open the jar, releasing the pleasant, herbal sweetness. You take a stick and use it like a brush, spreading the ointment near the larger pieces of furniture, under which you’d expect to find the colonies of worms and insects. You also put it on the top of and inside the pallets, as well as around the windows, under the door, and in the corners. The remaining balm finds its place in a couple of holes that you spotted between the bricks.
            \n\nIn less than half an hour you already see roaches that either lie still or kick their legs desperately while on their backs.
            '
            'I put the empty jar on a table. Maybe something will fly into it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put the empty jar on a table. Maybe something will fly into it.')
                jump watchtowerentrance01
    else:
        $ item_asteriontablet = 1
        if watchtower_open == "key":
            if quest_easternpath == 1 and quest_easternpath_description01:
                $ renpy.notify("You found a wax tablet.\nJournal updated: The Eastern Path")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
            else:
                $ renpy.notify("You found a wax tablet.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a wax tablet.{/i}')
            $ quest_easternpath_description08 = "The watchtower is clear and ready for new guards."
        else:
            if quest_easternpath == 1 and quest_easternpath_description01:
                $ renpy.notify("You found a wax tablet.\nJournal updated: The Eastern Path")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a wax tablet.\nJournal updated: The Eastern Path{/i}')
            else:
                $ renpy.notify("You found a wax tablet.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a wax tablet.{/i}')
            $ quest_easternpath_description08alt = "The watchtower is clear, though its door is broken."
        menu:
            'You open the jar, releasing the pleasant, herbal sweetness. You take a stick and use it like a brush, spreading the ointment near the larger pieces of furniture, under which you’d expect to find the colonies of worms and insects. You also put it on the top of and inside the pallets, as well as around the windows, under the door, and in the corners. The remaining balm finds its place in a couple of holes that you spotted between the bricks.
            \n\nYou found something unusual in the space between one of the pallets and the wall - an old, molding, wax tablet. The are some writings inside it. For now, you put it in your bag.
            \n\nIn less than half an hour you already see roaches that either lie still or kick their legs desperately while on their backs.
            '
            'I put the empty jar on a table. Maybe something will fly into it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put the empty jar on a table. Maybe something will fly into it.')
                jump watchtowerentrance01

label watchtowerinstallingrod01:
    $ quarters += 1
    $ renpy.notify("Journal updated: Bronze Rods")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
    $ eudocia_bronzerod_rodin_watchtower = 1
    $ item_bronzerod -= 1
    $ eudocia_bronzerod_installed += 1
    if not item_bronzerod:
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
                $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                $ quest_bronzerod_description02 = 0
    if eudocia_bronzerod_rodin_watchtower:
        show watchtowerbronzerod at basicfade
    menu:
        'You climb up the ladder and push the trapdoor with one hand. The planks are thick and as they fall down under their own weight, they make a loud thud.
        \n\nYou find a crack between two of the bricks and use the rod to widen it a bit. You push it halfway in and fill the gaps with a linen cloth. You move it a couple of times, just to be sure it won’t detach. You wonder if it’s going to lure any lightning.
        '
        'I climb down.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb down.')
            jump watchtowerentrance01

label watchtowerinstallingrod01alt:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use the bone hook of mine to leave the bronze rod on the top of the watchtower.')
    $ quarters += 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ renpy.notify("Journal updated: Bronze Rods")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
    $ eudocia_bronzerod_rodin_watchtower = 1
    $ item_bronzerod -= 1
    $ eudocia_bronzerod_installed += 1
    if not item_bronzerod:
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
                $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                $ quest_bronzerod_description02 = 0
    if eudocia_bronzerod_rodin_watchtower:
        show watchtowerbronzerod at basicfade
    menu:
        'Getting to the roof takes you a good few minutes. Tying the rope to the bone hook is easy enough, though you struggle to throw it just right. After a few attempts, it finally lands in such a way that it’s stuck at one of the crenels. You pull it, jump in place to make sure it won’t let go under your weight, then get to the top, “walking” on the surface of the wall.
        \n\nYou find a crack between two of the bricks and use the rod to widen it a bit. You push it halfway in and fill the gaps with a linen cloth. You move it a couple of times, just to be sure it won’t fall down. You wonder if it’s going to lure any lightning.
        '
        'I climb down slowly.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb down slowly.')
            $ quarters += 1
            jump watchtowerafterinteraction01

label watchtower_campfire01a:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the campfire spot.')
    menu:
        'You have [item_rawfishtotalnumber] raw fish in your possession. What would you like to do?
        '
        'I gather some firewood for another day.' if not watchtower_campfire_prepared and watchtower_campfire_fire == day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather some firewood for another day.')
            show watchtower_campfire_fire 04 at basicfade
            $ watchtower_campfire_prepared = 1
            $ quarters += 2
            $ custom1 = "It’s not difficult to find dead trees in the woods, but you take some time to find such pieces that won’t force you to use your battle axe. You find tinder beneath the shrubs and some dry branches dropped by the healthy trees. You don’t need to warm yourself up for long, so once you’re sure you have enough for the basic cooking, you move everything next to the camp."
            jump watchtower_campfire02
        'I gather some firewood.' if not watchtower_campfire_prepared and watchtower_campfire_fire != day:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather some firewood.')
            show watchtower_campfire_fire 03 at basicfade
            $ watchtower_campfire_prepared = 1
            $ quarters += 2
            $ custom1 = "It’s not difficult to find dead trees in the woods, but you take some time to find such pieces that won’t force you to use your battle axe. You find tinder beneath the shrubs and some dry branches dropped by the healthy trees. You don’t need to warm yourself up for long, so once you’re sure you have enough for the basic cooking, you move everything next to the camp."
            jump watchtower_campfire02
        'I don’t need more firewood right now. (disabled)' if watchtower_campfire_prepared:
            pass
        'To cook a fish, I need to first prepare some firewood. (disabled)' if not watchtower_campfire_prepared and item_rawfishtotalnumber >= 1 and not watchtower_campfire_fire == day:
            pass
        'I don’t have any fish to cook. (disabled)' if not watchtower_campfire_prepared and item_rawfishtotalnumber:
            pass
        'I cook a fish.' if (item_rawfishtotalnumber >= 1 and watchtower_campfire_prepared) or (item_rawfishtotalnumber >= 1 and watchtower_campfire_fire == day):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cook a fish.')
            $ quarters += 2
            if watchtower_campfire_fire != day:
                show watchtower_campfire_fire 01 at basicfade
                $ watchtower_campfire_prepared = 0
                $ watchtower_campfire_fire = day
                $ quarters += 1
                $ custom1 = "It takes you a good few minutes before the fire gets started, then grows strong enough for you to cook. In the meantime, you prepare the captured creature - you cut through the stomach, remove the guts with your fingers, then pierce through the animal with a pointed stick. Keeping it at a safe distance, you roast it slowly, until it both looks and smells prepared."
            else:
                $ custom1 = "Since you’ve already prepared the fire, you can get straight to the cooking. You cut through the stomach, remove the guts with your fingers, then pierce through the animal with a pointed stick. Keeping it at a safe distance, you roast it slowly, until it both looks and smells prepared."
            $ item_cookedfish += 1
            $ achievement_fish_cooked += 1
            $ item_rawfishtotalnumber -= 1
            $ item_rawfish_losing = 1
            $ renpy.notify("You cooked a fish.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You cooked a fish.{/i}')
            jump watchtower_campfire02
        'I cook 2 fish.' if (item_rawfishtotalnumber >= 2 and watchtower_campfire_prepared) or (item_rawfishtotalnumber >= 2 and watchtower_campfire_fire == day):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cook 2 fish.')
            $ custom1 = ""
            $ quarters += 2
            if watchtower_campfire_fire != day:
                show watchtower_campfire_fire 01 at basicfade
                $ watchtower_campfire_prepared = 0
                $ watchtower_campfire_fire = day
                $ quarters += 1
                $ custom1 = "It takes you a good few minutes before the fire gets started, then grows strong enough for you to cook. In the meantime, you prepare the captured creatures - you cut through the stomachs, remove the guts with your fingers, then pierce through the animals with pointed sticks. Keeping them at a safe distance, you roast them slowly, until they both look and smell prepared."
            else:
                $ custom1 = "Since you’ve already prepared the fire, you can get straight to the cooking. You cut through the stomachs, remove the guts with your fingers, then pierce through the animals with pointed sticks. Keeping them at a safe distance, you roast them slowly, until they both look and smell prepared."
            $ item_cookedfish += 2
            $ achievement_fish_cooked += 2
            $ item_rawfishtotalnumber -= 2
            $ item_rawfish_losing = 2
            $ renpy.notify("You cooked two fish.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You cooked two fish.{/i}')
            jump watchtower_campfire02
        'I cook 3 fish.' if (item_rawfishtotalnumber >= 3 and watchtower_campfire_prepared) or (item_rawfishtotalnumber >= 3 and watchtower_campfire_fire == day):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cook 3 fish.')
            $ custom1 = ""
            $ quarters += 2
            if watchtower_campfire_fire != day:
                show watchtower_campfire_fire 01 at basicfade
                $ watchtower_campfire_prepared = 0
                $ watchtower_campfire_fire = day
                $ quarters += 1
                $ custom1 = "It takes you a good few minutes before the fire gets started, then grows strong enough for you to cook. In the meantime, you prepare the captured creatures - you cut through the stomachs, remove the guts with your fingers, then pierce through the animals with pointed sticks. Keeping them at a safe distance, you roast them slowly, until they both look and smell prepared."
            else:
                $ custom1 = "Since you’ve already prepared the fire, you can get straight to the cooking. You cut through the stomachs, remove the guts with your fingers, then pierce through the animals with pointed sticks. Keeping them at a safe distance, you roast them slowly, until they both look and smell prepared."
            $ item_cookedfish += 3
            $ achievement_fish_cooked += 3
            $ item_rawfishtotalnumber -= 3
            $ item_rawfish_losing = 3
            $ renpy.notify("You cooked three fish.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You cooked three fish.{/i}')
            jump watchtower_campfire02
        'I step away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
            jump watchtowerafterinteraction01

    label watchtower_campfire02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the campfire spot.')
        menu:
            '[custom1]
            '
            'I gather some firewood for another day.' if not watchtower_campfire_prepared and watchtower_campfire_fire == day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather some firewood for another day.')
                show watchtower_campfire_fire 04 at basicfade
                $ watchtower_campfire_prepared = 1
                $ quarters += 2
                $ custom1 = "It’s not difficult to find the dead trees in the woods, but you take some time to find such pieces that won’t force you to use your battle axe. You find tinder beneath the shrubs and some dry branches dropped by the healthy trees. You don’t need to warm yourself up for long, so once you’re sure you have enough for the basic cooking, you move everything next to the camp."
                jump watchtower_campfire02
            'I gather some firewood.' if not watchtower_campfire_prepared and watchtower_campfire_fire != day:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather some firewood.')
                show watchtower_campfire_fire 03 at basicfade
                $ watchtower_campfire_prepared = 1
                $ quarters += 2
                $ custom1 = "It’s not difficult to find dead trees in the woods, but you take some time to find such pieces that won’t force you to use your battle axe. You find tinder beneath the shrubs and some dry branches dropped by the healthy trees. You don’t need to warm yourself up for long, so once you’re sure you have enough for the basic cooking, you move everything next to the camp."
                jump watchtower_campfire02
            'I don’t need more firewood right now. (disabled)' if watchtower_campfire_prepared:
                pass
            'To cook a fish, I need to first prepare some firewood. (disabled)' if not watchtower_campfire_prepared and item_rawfishtotalnumber >= 1 and not watchtower_campfire_fire == day:
                pass
            'I don’t have any fish to cook. (disabled)' if not watchtower_campfire_prepared and item_rawfishtotalnumber:
                pass
            'I cook a fish.' if (item_rawfishtotalnumber >= 1 and watchtower_campfire_prepared) or (item_rawfishtotalnumber >= 1 and watchtower_campfire_fire == day):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cook a fish.')
                $ quarters += 2
                if watchtower_campfire_fire != day:
                    show watchtower_campfire_fire 01 at basicfade
                    $ watchtower_campfire_prepared = 0
                    $ watchtower_campfire_fire = day
                    $ quarters += 1
                    $ custom1 = "It takes you a good few minutes before the fire gets started, then grows strong enough for you to cook. In the meantime, you prepare the captured creature - you cut through the stomach, remove the guts with your fingers, then pierce through the animal with a pointed stick. Keeping it at a safe distance, you roast it slowly, until it both looks and smells prepared."
                else:
                    $ custom1 = "Since you’ve already prepared the fire, you can get straight to the cooking. You cut through the stomach, remove the guts with your fingers, then pierce through the animal with a pointed stick. Keeping it at a safe distance, you roast it slowly, until it both looks and smells prepared."
                $ item_cookedfish += 1
                $ achievement_fish_cooked += 1
                $ item_rawfishtotalnumber -= 1
                $ item_rawfish_losing = 1
                $ renpy.notify("You cooked a fish.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You cooked a fish.{/i}')
                jump watchtower_campfire02
            'I cook 2 fish.' if (item_rawfishtotalnumber >= 2 and watchtower_campfire_prepared) or (item_rawfishtotalnumber >= 2 and watchtower_campfire_fire == day):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cook 2 fish.')
                $ custom1 = ""
                $ quarters += 2
                if watchtower_campfire_fire != day:
                    show watchtower_campfire_fire 01 at basicfade
                    $ watchtower_campfire_prepared = 0
                    $ watchtower_campfire_fire = day
                    $ quarters += 1
                    $ custom1 = "It takes you a good few minutes before the fire gets started, then grows strong enough for you to cook. In the meantime, you prepare the captured creatures - you cut through the stomachs, remove the guts with your fingers, then pierce through the animals with pointed sticks. Keeping them at a safe distance, you roast them slowly, until they both look and smell prepared."
                else:
                    $ custom1 = "Since you’ve already prepared the fire, you can get straight to the cooking. You cut through the stomachs, remove the guts with your fingers, then pierce through the animals with pointed sticks. Keeping them at a safe distance, you roast them slowly, until they both look and smell prepared."
                $ item_cookedfish += 2
                $ achievement_fish_cooked += 2
                $ item_rawfishtotalnumber -= 2
                $ item_rawfish_losing = 2
                $ renpy.notify("You cooked two fish.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You cooked two fish.{/i}')
                jump watchtower_campfire02
            'I cook 3 fish.' if (item_rawfishtotalnumber >= 3 and watchtower_campfire_prepared) or (item_rawfishtotalnumber >= 3 and watchtower_campfire_fire == day):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cook 3 fish.')
                $ custom1 = ""
                $ quarters += 2
                if watchtower_campfire_fire != day:
                    show watchtower_campfire_fire 01 at basicfade
                    $ watchtower_campfire_prepared = 0
                    $ watchtower_campfire_fire = day
                    $ quarters += 1
                    $ custom1 = "It takes you a good few minutes before the fire gets started, then grows strong enough for you to cook. In the meantime, you prepare the captured creatures - you cut through the stomachs, remove the guts with your fingers, then pierce through the animals with pointed sticks. Keeping them at a safe distance, you roast them slowly, until they both look and smell prepared."
                else:
                    $ custom1 = "Since you’ve already prepared the fire, you can get straight to the cooking. You cut through the stomachs, remove the guts with your fingers, then pierce through the animals with pointed sticks. Keeping them at a safe distance, you roast them slowly, until they both look and smell prepared."
                $ item_cookedfish += 3
                $ achievement_fish_cooked += 3
                $ item_rawfishtotalnumber -= 3
                $ item_rawfish_losing = 3
                $ renpy.notify("You cooked three fish.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You cooked three fish.{/i}')
                jump watchtower_campfire02
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump watchtowerafterinteraction01

label watchtowerforaging01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.')
    $ watchtower_wildplants_display = 0
    $ item_wildplants += 2
    $ achievement_wildplants += 2
    $ watchtower_wildplants_left = 0
    $ renpy.notify("You picked 2 bunches of wild plants.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked 2 bunches of wild plants.{/i}')
    $ quarters += 2
    menu:
        '{color=#f6d6bd}[horsename]{/color} grazes at the fence while you cross the short meadows, seeking edible leaves of fennels, sorrel, and lettuce that hide in the shadows of spruce trees, forcing you to get on your knees and push the branches away. After some time, with needles in your hood and sleeves, you carry the vegetables to the gate, washing them with your waterskin and spreading them on a blanket, allowing them to dry up.
        \n\nAs you pick the very few remaining pears and berries, you notice a wide tree hollow. You take a look inside and find a stash of acorns and chestnuts, but also hazelnuts and walnuts.
        '
        'Sweet, more food for me.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Sweet, more food for me.')
            $ item_rations += 1
            $ renpy.notify("You gathered a new food ration.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gathered a new food ration.{/i}')
            $ minutes += 5
            menu:
                'You pick out enough of the stomach-friendly nuts to satiate a day-long hunger of even a portly human.
                '
                'I use the bone hook of mine to leave the bronze rod on the top of the watchtower.' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp > 1" ):
                    jump watchtowerinstallingrod01alt
                'I’m too exhausted to climb the tower, even with my bone hook. (Required vitality: 2) (disabled)' ( condition="watchtower_tower_firsttime and not watchtower_open and item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower and pc_hp <= 1" ):
                    pass
                'It’s a good spot for one of the bronze rods, but I’d have to somehow get to the roof first. (disabled)' if watchtower_tower_firsttime and not watchtower_open and not item_bonehook and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_watchtower:
                    pass
                'I look for the tracks I saw near the fallen tree.' if quest_fallentree == 1 and fallentree_investigated_opinion04 == "were taken north" and not watchtower_tracks:
                    jump watchtowertracks01
                'I approach the entrance.' if not watchtower_open:
                    jump watchtowerdoor01
                'I enter the tower.' if watchtower_open:
                    jump watchtowerentrance01
                'I take a look at the signpost.':
                    jump watchtower_signpost01
                'I walk to the gate.' if not watchtower_gate:
                    jump watchtower_gate01
                'Maybe there’s something interesting among the spruce trees.' if not watchtower_trees:
                    jump watchtower_trees01
                'I examine the campfire spot at the fence.' if not watchtower_campfire:
                    jump watchtower_campfire01
                'I approach the campfire spot.' if (watchtower_campfire and watchtower_campfire_fire) or (watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber >= 1):
                    jump watchtower_campfire01a
                'I may use this campfire spot in the future if I have any raw meat with me. (disabled)' if watchtower_campfire and not watchtower_campfire_fire and item_rawfishtotalnumber < 1:
                    pass
                'Picking fruits and vegetables should be easy on an open hill. I spend half an hour foraging.' if watchtower_wildplants_display == 1 and watchtower_wildplants_left and watchtower_trees:
                    jump watchtowerforaging01
                'The wild plants here need just a few more days before they ripe. (disabled)' if watchtower_wildplants_display == 2 and watchtower_trees:
                    pass
                'The wild plants here need maybe another week before they ripe. (disabled)' if watchtower_wildplants_display == 3 and watchtower_trees:
                    pass
                'The wild plants here need more than one week before they ripe. (disabled)' if watchtower_wildplants_display == 4 and watchtower_trees:
                    pass
                'The wild plants here need about two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 5 and watchtower_trees:
                    pass
                'The wild plants here need more than two more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 6 and watchtower_trees:
                    pass
                'The wild plants here need about three more weeks before they ripe. (disabled)' if watchtower_wildplants_display == 7 and watchtower_trees:
                    pass
                'The wild plants here will be ripe just before the end of summer. (disabled)' if watchtower_wildplants_display == 8 and watchtower_trees:
                    pass
        'Squirrels will need them more. I take the fruits back to my bundles.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Squirrels will need them more. I take the fruits back to my bundles.')
            $ achievement_animalssavedpoints += 1
            jump watchtowerafterinteraction01
