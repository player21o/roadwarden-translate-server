###################### STONE BRIDGE (EAST)
default stonebridge_firsttime = 0
default stonebridge_fluff = ""
default stonebridge_fluff_old = ""
default stonebridge_dayfluff = ""
default stonebridge_bushes_cut = 0
default stonebridge_signpost = 0
default stonebridge_likedolmen = ""
default stonebridge_berries_fluff = ""
default stonebridge_roadeast_cleared = 0
default stonebridge_fish = 0
default stonebridge_fish_cleared = 0
default stonebridge_bridge_under = 0
default stonebridge_bath = 0

label stonebridge01:
    nvl clear
    $ pc_area = "stonebridge"
    stop music fadeout 4.0
    play nature "audio/ambient/stonebridge01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if stonebridge_signpost:
        show areapicture stonebridge03 at basicfade
    elif stonebridge_bushes_cut:
        show areapicture stonebridge02 at basicfade
    else:
        show areapicture stonebridge01 at basicfade
    label stonebridge_fluffloop:
        $ stonebridge_fluff = renpy.random.choice(['A purple squirrel is sitting on the broken boat, observing you with a hazelnut in its tiny paws. When your horse snorts, the critter runs away in panic.', 'The rustling of the bushes stops once you approach them.', 'A bunch of fish, as large as your hand, is swimming right under the water’s surface. They’re gathered around an extensive, red stain that flows down the stream.', 'You notice a bunch of large paw prints, both on the road and around it.', 'The water is unusually clean. Frogs croak on the banks loudly.'])
        if stonebridge_fluff_old == stonebridge_fluff:
            jump stonebridge_fluffloop
        else:
            $ stonebridge_fluff_old = stonebridge_fluff
    if quarters >= (world_daylength-8):
        $ stonebridge_dayfluff = 'With no trees blocking your view, you look at the bright and colorful stars.'
    else:
        $ stonebridge_dayfluff = 'With no trees or crags blocking the sun, the road is bright and inviting.'
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if stonebridge_firsttime < 2:
        $ world_known_areas += 1
        $ stonebridge_firsttime = 2
        $ watchtower_unlocked = 1
        $ huntercabin_unlocked = 1
        jump stonebridgefirsttime01
    elif elah_quest_easternpath_lumberjacks == 2:
        jump creekselahaboutquesteasternroadfallentree09
    else:
        jump stonebridgeregular01

label stonebridgefirsttime01:
    $ at_unlock_knowledge = 0
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if dolmen_firsttime:
        $ stonebridge_likedolmen = " It makes you think of the dolmen you saw south of here."
    else:
        $ stonebridge_likedolmen = ""
    if pc_class == "scholar":
        $ stonebridge_berries_fluff = "Knowing from the herbaria that the fruits are safe, you eat a few bitter-sweet ones as well."
    else:
        $ stonebridge_berries_fluff = "You think about picking some of the fruits, but you’re not sure if they’re edible."
    if pc_class == "scholar" and stonebridge_fish < 2:
        $ at_unlock_knowledge = 1
        $ at = 0
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '[stonebridge_dayfluff] The simple bridge is centuries old, bitten by time.[stonebridge_likedolmen]
        \n\nThe torrent here is deep and fast, with plenty of fish. The boat is destroyed beyond repair - rotten, falling to pieces, with holes in the floor and on the sides, overgrown with fungi and moss.
        \n\nThe thick shrubs lining the path are covered with thorns. Small birds are jumping from one twig to another, pecking at the brown berries. [stonebridge_berries_fluff]
        '
        'Time to stop lugging around this painted plank.' if not stonebridge_signpost and item_signpost:
            jump stonebridgesignpost01
        'It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if quest_reachthepaganvillage_description01 and not stonebridge_roadeast_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
            jump stonebridgemoveeast01
        'These are the fish that supposedly live in the stream that leads to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if not quest_reachthepaganvillage_description01 and description_greenmountaintribe02 and stonebridge_fish and not stonebridge_roadeast_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
            jump stonebridgemoveeast01
        'I wash myself in the river.' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness <= 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness <= 2):
            jump stonebridgebath01
        'I don’t need to wash myself. (disabled)' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness > 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness > 2):
            pass
        'No point in staying here. I move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and not pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and not pc_likeshorsename):
            pass
        'No point in staying here. We move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and pc_likeshorsename):
            pass
        'I take a closer look at the fish.' ( condition="at != 'knowledge' and not stonebridge_fish"):
            jump stonebridge_fish01
        'I think I’ve read something about these fish.' ( condition="at == 'knowledge' and stonebridge_fish < 2"):
            jump stonebridge_fish01alt
        '{image=d6} I look around for an hour or so. Maybe I can find something of use.' if not stonebridge_bridge_under and not quest_hiddenpurse:
            jump stonebridge_bridge_under01
        'I look for the purse of {color=#f6d6bd}the woman from White Marshes{/color}.' if not stonebridge_bridge_under and quest_hiddenpurse:
            jump stonebridge_bridge_under02

label stonebridgeregular01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ at_unlock_knowledge = 0
    if pc_class == "scholar" and stonebridge_fish < 2:
        $ at_unlock_knowledge = 1
        $ at = 0
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '[stonebridge_fluff]
        '
        'Time to stop lugging around this painted plank.' if not stonebridge_signpost and item_signpost:
            jump stonebridgesignpost01
        'It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if quest_reachthepaganvillage_description01 and not stonebridge_roadeast_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
            jump stonebridgemoveeast01
        'These are the fish that supposedly live in the stream that leads to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if not quest_reachthepaganvillage_description01 and description_greenmountaintribe02 and stonebridge_fish and not stonebridge_roadeast_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
            jump stonebridgemoveeast01
        'I wash myself in the river.' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness <= 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness <= 2):
            jump stonebridgebath01
        'I don’t need to wash myself. (disabled)' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness > 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness > 2):
            pass
        'No point in staying here. I move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and not pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and not pc_likeshorsename):
            pass
        'No point in staying here. We move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and pc_likeshorsename):
            pass
        'I take a closer look at the fish.' ( condition="at != 'knowledge' and not stonebridge_fish"):
            jump stonebridge_fish01
        'I think I’ve read something about these fish.' ( condition="at == 'knowledge' and stonebridge_fish < 2"):
            jump stonebridge_fish01alt
        '{image=d6} I look around for an hour or so. Maybe I can find something of use.' if not stonebridge_bridge_under and not quest_hiddenpurse:
            jump stonebridge_bridge_under01
        'I look for the purse of {color=#f6d6bd}the woman from White Marshes{/color}.' if not stonebridge_bridge_under and quest_hiddenpurse:
            jump stonebridge_bridge_under02

label stonebridgeafterinteraction01:
    $ at_unlock_knowledge = 0
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if pc_class == "scholar" and stonebridge_fish < 2:
        $ at_unlock_knowledge = 1
        $ at = 0
    if quarters < (world_daylength-8):
        $ custom1 = "peacefully chews the grass, enjoying the sun on its back, ready to take a nap"
    else:
        $ custom1 = "looks around nervously and approaches you when when it notices your attention"
    menu:
        '{color=#f6d6bd}[horsename]{/color} [custom1].
        '
        'Time to stop lugging around this painted plank.' if not stonebridge_signpost and item_signpost:
            jump stonebridgesignpost01
        'It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if quest_reachthepaganvillage_description01 and not stonebridge_roadeast_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
            jump stonebridgemoveeast01
        'These are the fish that supposedly live in the stream that leads to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if not quest_reachthepaganvillage_description01 and description_greenmountaintribe02 and stonebridge_fish and not stonebridge_roadeast_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
            jump stonebridgemoveeast01
        'I wash myself in the river.' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness <= 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness <= 2):
            jump stonebridgebath01
        'I don’t need to wash myself. (disabled)' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness > 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness > 2):
            pass
        'No point in staying here. I move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and not pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and not pc_likeshorsename):
            pass
        'No point in staying here. We move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and pc_likeshorsename):
            pass
        'I take a closer look at the fish.' ( condition="at != 'knowledge' and not stonebridge_fish"):
            jump stonebridge_fish01
        'I think I’ve read something about these fish.' ( condition="at == 'knowledge' and stonebridge_fish < 2"):
            jump stonebridge_fish01alt
        '{image=d6} I look around for an hour or so. Maybe I can find something of use.' if not stonebridge_bridge_under and not quest_hiddenpurse:
            jump stonebridge_bridge_under01
        'I look for the purse of {color=#f6d6bd}the woman from White Marshes{/color}.' if not stonebridge_bridge_under and quest_hiddenpurse:
            jump stonebridge_bridge_under02

label stonebridge_fishALL:
    label stonebridge_fish01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the fish.')
        $ at_unlock_knowledge = 0
        if description_greenmountaintribe02:
            $ stonebridge_fish = 2
            if pc_class == "scholar" and stonebridge_fish < 2:
                $ at_unlock_knowledge = 1
                $ at = 0
            menu:
                'You see dozens of red-and-gray shells. As you walk by, they stay close, following your steps.
                \n\nYou think of the flesh-eating creatures you heard about. Seeing their sheer number, they could chew off your limbs in but a few breaths.
                '
                'Time to stop lugging around this painted plank.' if not stonebridge_signpost and item_signpost:
                    jump stonebridgesignpost01
                'It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if quest_reachthepaganvillage_description01 and not stonebridge_roadeast_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
                    jump stonebridgemoveeast01
                'These are the fish that supposedly live in the stream that leads to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if not quest_reachthepaganvillage_description01 and description_greenmountaintribe02 and stonebridge_fish and not stonebridge_roadeast_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
                    jump stonebridgemoveeast01
                'I wash myself in the river.' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness <= 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness <= 2):
                    jump stonebridgebath01
                'I don’t need to wash myself. (disabled)' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness > 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness > 2):
                    pass
                'No point in staying here. I move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and not pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and not pc_likeshorsename):
                    pass
                'No point in staying here. We move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and pc_likeshorsename):
                    pass
                'I take a closer look at the fish.' ( condition="at != 'knowledge' and not stonebridge_fish"):
                    jump stonebridge_fish01
                'I think I’ve read something about these fish.' ( condition="at == 'knowledge' and stonebridge_fish < 2"):
                    jump stonebridge_fish01alt
                '{image=d6} I look around for an hour or so. Maybe I can find something of use.' if not stonebridge_bridge_under and not quest_hiddenpurse:
                    jump stonebridge_bridge_under01
                'I look for the purse of {color=#f6d6bd}the woman from White Marshes{/color}.' if not stonebridge_bridge_under and quest_hiddenpurse:
                    jump stonebridge_bridge_under02
        else:
            $ stonebridge_fish = 1
            if pc_class == "scholar" and stonebridge_fish < 2:
                $ at_unlock_knowledge = 1
                $ at = 0
            menu:
                'You see dozens of red-and-gray shells. As you walk by, they stay close, following your steps.
                '
                'Time to stop lugging around this painted plank.' if not stonebridge_signpost and item_signpost:
                    jump stonebridgesignpost01
                'It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if quest_reachthepaganvillage_description01 and not stonebridge_roadeast_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
                    jump stonebridgemoveeast01
                'These are the fish that supposedly live in the stream that leads to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if not quest_reachthepaganvillage_description01 and description_greenmountaintribe02 and stonebridge_fish and not stonebridge_roadeast_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
                    jump stonebridgemoveeast01
                'I wash myself in the river.' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness <= 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness <= 2):
                    jump stonebridgebath01
                'I don’t need to wash myself. (disabled)' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness > 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness > 2):
                    pass
                'No point in staying here. I move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and not pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and not pc_likeshorsename):
                    pass
                'No point in staying here. We move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and pc_likeshorsename):
                    pass
                'I take a closer look at the fish.' ( condition="at != 'knowledge' and not stonebridge_fish"):
                    jump stonebridge_fish01
                'I think I’ve read something about these fish.' ( condition="at == 'knowledge' and stonebridge_fish < 2"):
                    jump stonebridge_fish01alt
                '{image=d6} I look around for an hour or so. Maybe I can find something of use.' if not stonebridge_bridge_under and not quest_hiddenpurse:
                    jump stonebridge_bridge_under01
                'I look for the purse of {color=#f6d6bd}the woman from White Marshes{/color}.' if not stonebridge_bridge_under and quest_hiddenpurse:
                    jump stonebridge_bridge_under02

    label stonebridge_fish01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I’ve read something about these fish.')
        $ at_unlock_knowledge = 0
        if stonebridge_fish:
            $ custom1 = ""
        else:
            $ custom1 = "You see dozens of red-and-gray shells. As you walk by, they stay close, following your steps. "
        $ stonebridge_fish = 2
        menu:
            '[custom1]According to the testimonies from a murder trial you’ve read about, they have long and sharp teeth, eat flesh, and could scrap your skull clean in a minute or so.
            '
            'Time to stop lugging around this painted plank.' if not stonebridge_signpost and item_signpost:
                jump stonebridgesignpost01
            'It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if quest_reachthepaganvillage_description01 and not stonebridge_roadeast_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
                jump stonebridgemoveeast01
            'These are the fish that supposedly live in the stream that leads to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.' if not quest_reachthepaganvillage_description01 and description_greenmountaintribe02 and stonebridge_fish and not stonebridge_roadeast_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s the spot from where I can move east, to {color=#f6d6bd}The Tribe of The Green Mountain{/color}.')
                jump stonebridgemoveeast01
            'I wash myself in the river.' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness <= 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness <= 2):
                jump stonebridgebath01
            'I don’t need to wash myself. (disabled)' if (not stonebridge_bath and stonebridge_fish < 2 and not cleanliness_equipment and cleanliness > 1) or (not stonebridge_bath and stonebridge_fish < 2 and cleanliness_equipment and cleanliness > 2):
                pass
            'No point in staying here. I move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and not pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and not pc_likeshorsename):
                pass
            'No point in staying here. We move forward. (disabled)' if (not item_signpost and not quest_reachthepaganvillage_description01 and stonebridge_bridge_under and pc_likeshorsename) or (not item_signpost and quest_reachthepaganvillage_description01 and stonebridge_roadeast_cleared and stonebridge_bridge_under and pc_likeshorsename):
                pass
            'I take a closer look at the fish.' ( condition="at != 'knowledge' and not stonebridge_fish"):
                jump stonebridge_fish01
            'I think I’ve read something about these fish.' ( condition="at == 'knowledge' and stonebridge_fish < 2"):
                jump stonebridge_fish01alt
            '{image=d6} I look around for an hour or so. Maybe I can find something of use.' if not stonebridge_bridge_under and not quest_hiddenpurse:
                jump stonebridge_bridge_under01
            'I look for the purse of {color=#f6d6bd}the woman from White Marshes{/color}.' if not stonebridge_bridge_under and quest_hiddenpurse:
                jump stonebridge_bridge_under02

label stonebridge_bridge_underALL:
    label stonebridge_bridge_under01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I look around for an hour or so. Maybe I can find something of use.')
        $ stonebridge_bridge_under = 1
        $ at_unlock_knowledge = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ d100roll = renpy.random.randint(2, 5)
        $ quarters += d100roll
        menu:
            'After what feels like an eternity of searching around the boat, the banks, and the shrubs, you sit down on the bridge to take a break - then realize you haven’t actually looked {i}beneath{/i} it. You kneel on the grass and look into the darkness.
            \n\nAmong the cobwebs and bugs, you spot an old piece of fabric pinned under a rock. You pull it out and find a rotting, torn pouch that contains a single dragon bone. You make sure you haven’t missed the other ones in the dirt, but if they ever existed, they have rolled down and sunk for good.
            '
            'I throw the pouch away and stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw the pouch away and stand up.')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ coins += 1
                $ quest_hiddenpurse_description01 = "I found the pouch. It contained a single dragon bone."
                if quest_hiddenpurse == 1:
                    show screen notifyimage( "Journal updated: A Hidden Pouch\n+1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: A Hidden Pouch{/i}')
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 {image=cointest}{/i}')
                else:
                    show screen notifyimage( "+1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 {image=cointest}{/i}')
                jump stonebridgeafterinteraction01

    label stonebridge_bridge_under02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for the purse of {color=#f6d6bd}the woman from White Marshes{/color}.')
        $ stonebridge_bridge_under = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ minutes += 5
        $ at_unlock_knowledge = 0
        menu:
            'You kneel on the grass and look into the darkness. Among the cobwebs and bugs, you spot an old piece of fabric pinned under a rock. You pull it out and find a rotting, torn pouch that contains a single dragon bone. You make sure you haven’t missed the other ones in the dirt, but if they ever existed, they have rolled down and sunk for good.
            '
            'I throw the pouch away and stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw the pouch away and stand up.')
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ coins += 1
                $ quest_hiddenpurse_description01 = "I found the pouch. It contained a single dragon bone."
                if quest_hiddenpurse == 1:
                    show screen notifyimage( "Journal updated: A Hidden Pouch\n+1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: A Hidden Pouch{/i}')
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 {image=cointest}{/i}')
                else:
                    show screen notifyimage( "+1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 {image=cointest}{/i}')
                jump stonebridgeafterinteraction01

label stonebridgemoveeastALL:
    label stonebridgemoveeast01:
        $ at_unlock_knowledge = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'You don’t see any easy way to move east. If there’s any path you could take, it’s completely overgrown. The thorny bushes won’t allow you to move without harm and even if you could, you wouldn’t leave {color=#f6d6bd}[horsename]{/color} behind.
            '
            'I shouldn’t enter the water. The fish are going to kill me. (disabled)' if stonebridge_fish >= 2:
                pass
            'The withering dust will get me through these bushes.' if item_witheringdust:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The withering dust will get me through these bushes.')
                $ stonebridge_roadeast_cleared = 1
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description06 = "I cleared the bushes leading east of the old stone bridge."
                $ stonebridge_bushes_cut = 1
                $ quarters += 1
                jump stonebridgemoveeast02usingpotion
            'I pack my things, undress, and lead {color=#f6d6bd}[horsename]{/color} through the water until we reach a path.' if stonebridge_fish < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things, undress, and lead {color=#f6d6bd}%s{/color} through the water until we reach a path.' %horsename)
                $ stonebridge_fish = 2
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                jump stonebridgemoveeast02throughfish
            'I lack strength to clear the bushes with brute force, and I’d need at least 3 hours. (Required vitality: 2) (disabled)' ( condition="quarters > (world_daylength-12) and pc_hp <= 1" ):
                pass
            'To clear the bushes with brute force, I’d need at least 3 hours. (disabled)' ( condition="quarters > (world_daylength-12) and pc_hp > 1" ):
                pass
            'I lack strength to clear the bushes with brute force. (Required vitality: 2) (disabled)' ( condition="quarters <= (world_daylength-12) and pc_hp <= 1" ):
                pass
            'It will take a couple of hours, but I cut down the bushes with my axe, making a path for {color=#f6d6bd}[horsename]{/color} and me.' ( condition="quarters <= (world_daylength-12) and pc_hp > 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will take a couple of hours, but I cut down the bushes with my axe, making a path for {color=#f6d6bd}%s{/color} and me.' %horsename)
                $ stonebridge_roadeast_cleared = 1
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description06 = "I cleared the bushes leading east of the old stone bridge."
                $ stonebridge_bushes_cut = 1
                jump stonebridgemoveeast02cuttingbushes
            'I don’t possess any potion that could help me here. (disabled)' if not item_witheringdust:
                pass
            'I can’t handle this right now.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t handle this right now.')
                jump stonebridgeafterinteraction01

    label stonebridgemoveeast02throughfish:
        $ quarters += 1
        if pc_likeshorsename:
            $ custom1 = "an animal"
        else:
            $ custom1 = "a beast"
        menu:
            'Wearing nothing, you grab the lead rope and move forward, staying on the steep bank, but for [custom1] as large as {color=#f6d6bd}[horsename]{/color} it’s a difficult task. Finally, you have no other option but to get into the clean, warm water.
            \n\nYour mount pulls away, ignoring your firm grasp and calm voice. A harsh bite reaches your calf. You look down - another wave of pain runs through your legs, and your blood flows downstream. In a panic, you climb back out, grabbing a clump of grass.
            \n\nA fish is still holding your thigh. You pull it, and squeeze with anger. Its mouth is filled with thin, inch-long teeth. You need a bandage.
            '
            'I throw it back into the water.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw it back into the water.')
                $ quarters += 1
                $ achievement_animalssavedpoints += 1
                jump stonebridgeafterinteraction01
            'I cast it into the bushes and make it suffocate.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cast it into the bushes and make it suffocate.')
                $ quarters += 1
                jump stonebridgeafterinteraction01

    label stonebridgemoveeast02cuttingbushes:
        show areapicture stonebridge02 at basicfade
        $ quarters += 7
        $ cleanliness = limit_cleanliness(cleanliness-1)
        if not cleanliness_clothes_torn:
            $ cleanliness_clothes_torn = 1
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
        else:
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        $ pc_food = limit_pc_food(pc_food-1)
        show minus1food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
        menu:
            'The sun isn’t harsh. As long as no beasts are going to bother you, you can expect a fair bit of carefree labor.
            \n\nThe thick gloves allow you to move or clean the thorny branches. You push the plants away, then cut right above the ground. The stems are healthy and flexible, but with enough time and determination, you manage to cut through and throw them aside, one by one.
            \n\nAfter a few hours, you feel hungry, but at least you reached the game trail.
            '
            'I pack my things, sharpen the axe blade, and prepare for the rest of the journey.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things, sharpen the axe blade, and prepare for the rest of the journey.')
                $ quarters += 2
                $ ghoulcave_unlocked = 1
                jump stonebridgeafterinteraction01

    label stonebridgemoveeast02usingpotion:
        show areapicture stonebridge02 at basicfade
        $ quarters += 1
        menu:
            'You put on your thick, leather gloves, then spread the dust beneath the plants. You draw water from the river with a wooden bowl and sprinkle it over the poison. You don’t need to wait long - the yellow smoke appears immediately, so you step away and cover your mouth and nose.
            \n\nThe sizzling bush starts to shake, losing its twigs and leaves. In less than a minute you throw the plant into the stream, then end the job with your axe.
            '
            'That was easy. I hide the remaining poison in my bags.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- That was easy. I hide the remaining poison in my bags.')
                $ minutes += 5
                $ ghoulcave_unlocked = 1
                jump stonebridgeafterinteraction01

label stonebridgebath01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash myself in the river.')
    $ at_unlock_knowledge = 0
    $ minutes += 5
    $ stonebridge_fish = 2
    $ stonebridge_bath = 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ pc_hp = limit_pc_hp(pc_hp-1)
    show minus1hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
    menu:
        'You undress, keeping your axe at hand, and check the water with your hand. It’s as warm as it is clean.
        \n\nYou step in, hearing your mount’s fearful snort. You tell it to quench its thirst, but then a harsh bite reaches your calf. You look down - another wave of pain runs through your legs, and your blood flows downstream. In a panic, you climb back out, grabbing a clump of grass.
        \n\nA fish is still holding your thigh. You pull it, and squeeze with anger. Its mouth is filled with thin, inch-long teeth. You need a bandage.
        '
        'I throw it back into the water.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw it back into the water.')
            $ minutes += 5
            $ achievement_animalssavedpoints += 1
            jump stonebridgeafterinteraction01
        'I cast it into the bushes and make it suffocate.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cast it into the bushes and make it suffocate.')
            $ minutes += 5
            jump stonebridgeafterinteraction01

label stonebridgesignpost01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to stop lugging around this painted plank.')
    $ at_unlock_knowledge = 0
    $ quarters += 1
    $ item_signpost = 0
    $ stonebridge_signpost = 1
    show areapicture stonebridge03 at basicfade
    if quest_easternpath == 1 and quest_easternpath_description01:
        $ renpy.notify("Journal updated: The Eastern Path")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
    else:
        $ renpy.notify("You built a signpost")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You built a signpost{/i}')
    $ quest_easternpath_description06alt = "I placed the sign at the path leading east of the old stone bridge."
    menu:
        'The convenient remains of a shrub help you tie the plank above the ground. After a few minutes, you step away and take a look at the new sign.
        '
        'It may save someone’s life.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may save someone’s life.')
            jump stonebridgeafterinteraction01
        'I’d rather see people building new paths, not hide them.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’d rather see people building new paths, not hide them.')
            jump stonebridgeafterinteraction01
        'I wonder if the days of iron nails are ever coming back.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder if the days of iron nails are ever coming back.')
            jump stonebridgeafterinteraction01
        'What soul would enter a path that looks like this, anyway?':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- What soul would enter a path that looks like this, anyway?')
            jump stonebridgeafterinteraction01
        'Well, that was easy.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, that was easy.')
            jump stonebridgeafterinteraction01
