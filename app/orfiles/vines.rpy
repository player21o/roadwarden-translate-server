######### VINES
default vines_firsttime = 0
default vines_fluff = ""
default vines_fluff_old = ""

default vines_open_day = 0
default vines_open_sleep = 0
default vines_perma_open = 0
default vines_perma_closed = 0
default vines_perma_closed_seen = 0

default vines_passable = 0
default vines_mushroom = 0
default vines_poked = 0
default vines_water= 0

label vines01:
    nvl clear
    $ pc_area = "vines"
    stop music fadeout 4.0
    play nature "audio/ambient/bogroad01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if vines_open_sleep:
        show areapicture vines02 at basicfade behind vinesnomushroom
    if (vines_open_day != day and not vines_perma_open) or vines_perma_closed:
        show areapicture vines01 at basicfade behind vinesnomushroom
    else:
        show areapicture vines02 at basicfade behind vinesnomushroom
    if vines_mushroom:
        show vinesnomushroom at basicfade
    label vines_fluffloop:
        $ vines_fluff = renpy.random.choice(['The thick air makes you want to take a deep breath, but the scent of decomposing flesh makes it a risky venture.', 'You spot movement among the rocks, but find nothing on their surface.', 'A toad tries to disappear in a pond, but it ends up being swallowed by a small saurian that was waiting beneath the surface.', 'A rook observes you from a tree, unaware of the hawk preparing to strike.', 'There are fresh boot prints leading back to the crossroads, weirdly spread and dragged, as if their owner was trudging.'])
        if vines_fluff_old == vines_fluff:
            jump vines_fluffloop
        else:
            $ vines_fluff_old = vines_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ vines_passable = 0
    if not vines_firsttime:
        $ whitemarshes_unlocked = 1
        $ world_known_npcs += 0
        $ world_known_areas += 1
        $ vines_firsttime = 1
        if (vines_open_day != day and not vines_perma_open) or vines_perma_closed:
            $ vines_passable = 0
            jump vinesfirsttimeclosed01
        else:
            $ vines_passable = 1
            jump vinesfirsttimeopen01
    else:
        if vines_perma_closed:
            $ vines_perma_closed_seen = 1
            $ vines_passable = 0
            jump vines_perma_closed_seen01
        elif vines_open_sleep and not vines_perma_open:
            $ vines_open_sleep = 0
            $ vines_passable = 0
            jump vinesregularopen01alt
        elif (vines_open_day != day and not vines_perma_open) or vines_perma_closed:
            $ vines_passable = 0
            jump vinesregularclosed01
        else:
            if not whitemarshes_unlocked:
                $ whitemarshes_unlocked = 1
                $ vines_passable = 1
                jump vinesfirsttime02
            else:
                $ vines_passable = 1
                jump vinesregularopen01

label vinesfirsttimeclosed01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if pc_class == "scholar" and not vines_mushroom:
        $ at_unlock_knowledge = 1
        $ at = 0
    menu:
        'The leafless plants resemble tree roots rather than creepers, even though they’re dark green and sway from side to side slightly. {color=#f6d6bd}[horsename]{/color} stops without a command, unwilling to approach the nightmarish gate.
        \n\nThere’s no other path in sight.
        '
        'I approach the creepers with a drawn axe.' if not vines_passable and not vines_poked:
            jump vines_poked01
        'I pick up some branches and throw them at the creepers.' if not vines_passable and not vines_poked:
            jump vines_poked02
        'I examine the water.' if not vines_passable and vines_poked and not vines_water:
            jump vineswater01
        'I approach the mushroom growing behind the creepers.' ( condition="at == 'knowledge' and vines_passable and quarters >= ((world_daylength/2)+11-4) and quarters <= ((world_daylength/2)+11+4)" ) :
            jump vinesmushroom01
        'I recognize the mushroom growing behind the creepers. Once they’re gone, I can pick it, but only in the middle of the day. (disabled)' ( condition="at == 'knowledge' and not vines_passable" ) :
            pass
        'To properly use the mushroom growing behind the creepers, I have to pick it in the middle of the day. (disabled)' ( condition="(at == 'knowledge' and vines_passable and quarters < ((world_daylength/2)+11-4)) or (at == 'knowledge' and vines_passable and quarters > ((world_daylength/2)+11+4))" ) :
            pass
        'I can’t cross these creepers on my own. (disabled)' if not vines_passable and vines_water:
            pass
        'Nothing stops me from riding ahead. (disabled)' if vines_passable:
            pass

label vinesfirsttimeopen01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if pc_class == "scholar" and not vines_mushroom:
        $ at_unlock_knowledge = 1
        $ at = 0
    menu:
        'The leafless plants resemble tree roots rather than creepers, even though they’re dark green and sway up and down slightly, in the rhythm of a heartbeat. {color=#f6d6bd}[horsename]{/color} snorts and speeds up, unwilling to linger underneath the nightmarish gate. As you get to the other side, the plants seem to completely ignore you.
        '
        'I approach the creepers with a drawn axe.' if not vines_passable and not vines_poked:
            jump vines_poked01
        'I pick up some branches and throw them at the creepers.' if not vines_passable and not vines_poked:
            jump vines_poked02
        'I examine the water.' if not vines_passable and vines_poked and not vines_water:
            jump vineswater01
        'I approach the mushroom growing behind the creepers.' ( condition="at == 'knowledge' and vines_passable and quarters >= ((world_daylength/2)+11-4) and quarters <= ((world_daylength/2)+11+4)" ) :
            jump vinesmushroom01
        'I recognize the mushroom growing behind the creepers. Once they’re gone, I can pick it, but only in the middle of the day. (disabled)' ( condition="at == 'knowledge' and not vines_passable" ) :
            pass
        'To properly use the mushroom growing behind the creepers, I have to pick it in the middle of the day. (disabled)' ( condition="(at == 'knowledge' and vines_passable and quarters < ((world_daylength/2)+11-4)) or (at == 'knowledge' and vines_passable and quarters > ((world_daylength/2)+11+4))" ) :
            pass
        'I can’t cross these creepers on my own. (disabled)' if not vines_passable and vines_water:
            pass
        'Nothing stops me from riding ahead. (disabled)' if vines_passable:
            pass

label vinesfirsttime02:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if pc_class == "scholar" and not vines_mushroom:
        $ at_unlock_knowledge = 1
        $ at = 0
    menu:
        'The root-like creepers are raised at an angle, swaying up and down slowly, in the rhythm of a heartbeat. {color=#f6d6bd}[horsename]{/color} snorts and speeds up, unwilling to linger underneath the nightmarish gate. As you get to the other side, the plants seem to completely ignore you.
        '
        'I approach the creepers with a drawn axe.' if not vines_passable and not vines_poked:
            jump vines_poked01
        'I pick up some branches and throw them at the creepers.' if not vines_passable and not vines_poked:
            jump vines_poked02
        'I examine the water.' if not vines_passable and vines_poked and not vines_water:
            jump vineswater01
        'I approach the mushroom growing behind the creepers.' ( condition="at == 'knowledge' and vines_passable and quarters >= ((world_daylength/2)+11-4) and quarters <= ((world_daylength/2)+11+4)" ) :
            jump vinesmushroom01
        'I recognize the mushroom growing behind the creepers. Once they’re gone, I can pick it, but only in the middle of the day. (disabled)' ( condition="at == 'knowledge' and not vines_passable" ) :
            pass
        'To properly use the mushroom growing behind the creepers, I have to pick it in the middle of the day. (disabled)' ( condition="(at == 'knowledge' and vines_passable and quarters < ((world_daylength/2)+11-4)) or (at == 'knowledge' and vines_passable and quarters > ((world_daylength/2)+11+4))" ) :
            pass
        'I can’t cross these creepers on my own. (disabled)' if not vines_passable and vines_water:
            pass
        'Nothing stops me from riding ahead. (disabled)' if vines_passable:
            pass

label vinesregularopen01alt:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    show areapicture vines01 at basicfade behind vinesnomushroom
    if pc_class == "scholar" and not vines_mushroom:
        $ at_unlock_knowledge = 1
        $ at = 0
    menu:
        'The creepers get lower. {color=#f6d6bd}[horsename]{/color}, unwilling to stay around any longer, rushes ahead and takes you to the other side. Right after you pass the plants, they crush into the ground.
        '
        'I approach the creepers with a drawn axe.' if not vines_passable and not vines_poked:
            jump vines_poked01
        'I pick up some branches and throw them at the creepers.' if not vines_passable and not vines_poked:
            jump vines_poked02
        'I examine the water.' if not vines_passable and vines_poked and not vines_water:
            jump vineswater01
        'I approach the mushroom growing behind the creepers.' ( condition="at == 'knowledge' and vines_passable and quarters >= ((world_daylength/2)+11-4) and quarters <= ((world_daylength/2)+11+4)" ) :
            jump vinesmushroom01
        'I recognize the mushroom growing behind the creepers. Once they’re gone, I can pick it, but only in the middle of the day. (disabled)' ( condition="at == 'knowledge' and not vines_passable" ) :
            pass
        'To properly use the mushroom growing behind the creepers, I have to pick it in the middle of the day. (disabled)' ( condition="(at == 'knowledge' and vines_passable and quarters < ((world_daylength/2)+11-4)) or (at == 'knowledge' and vines_passable and quarters > ((world_daylength/2)+11+4))" ) :
            pass
        'I can’t cross these creepers on my own. (disabled)' if not vines_passable and vines_water:
            pass
        'Nothing stops me from riding ahead. (disabled)' if vines_passable:
            pass

label vinesregularclosed01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if pc_class == "scholar" and not vines_mushroom:
        $ at_unlock_knowledge = 1
        $ at = 0
    menu:
        '[vines_fluff] The slight twitches of the creepers in no way align with the gentle wind.
        '
        'I approach the creepers with a drawn axe.' if not vines_passable and not vines_poked:
            jump vines_poked01
        'I pick up some branches and throw them at the creepers.' if not vines_passable and not vines_poked:
            jump vines_poked02
        'I examine the water.' if not vines_passable and vines_poked and not vines_water:
            jump vineswater01
        'I approach the mushroom growing behind the creepers.' ( condition="at == 'knowledge' and vines_passable and quarters >= ((world_daylength/2)+11-4) and quarters <= ((world_daylength/2)+11+4)" ) :
            jump vinesmushroom01
        'I recognize the mushroom growing behind the creepers. Once they’re gone, I can pick it, but only in the middle of the day. (disabled)' ( condition="at == 'knowledge' and not vines_passable" ) :
            pass
        'To properly use the mushroom growing behind the creepers, I have to pick it in the middle of the day. (disabled)' ( condition="(at == 'knowledge' and vines_passable and quarters < ((world_daylength/2)+11-4)) or (at == 'knowledge' and vines_passable and quarters > ((world_daylength/2)+11+4))" ) :
            pass
        'I can’t cross these creepers on my own. (disabled)' if not vines_passable and vines_water:
            pass
        'Nothing stops me from riding ahead. (disabled)' if vines_passable:
            pass

label vinesregularopen01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if pc_class == "scholar" and not vines_mushroom:
        $ at_unlock_knowledge = 1
        $ at = 0
    menu:
        '[vines_fluff] The root-like creepers are raised at an angle, moving up and down slowly, in the rhythm of a heartbeat.
        '
        'I approach the creepers with a drawn axe.' if not vines_passable and not vines_poked:
            jump vines_poked01
        'I pick up some branches and throw them at the creepers.' if not vines_passable and not vines_poked:
            jump vines_poked02
        'I examine the water.' if not vines_passable and vines_poked and not vines_water:
            jump vineswater01
        'I approach the mushroom growing behind the creepers.' ( condition="at == 'knowledge' and vines_passable and quarters >= ((world_daylength/2)+11-4) and quarters <= ((world_daylength/2)+11+4)" ) :
            jump vinesmushroom01
        'I recognize the mushroom growing behind the creepers. Once they’re gone, I can pick it, but only in the middle of the day. (disabled)' ( condition="at == 'knowledge' and not vines_passable" ) :
            pass
        'To properly use the mushroom growing behind the creepers, I have to pick it in the middle of the day. (disabled)' ( condition="(at == 'knowledge' and vines_passable and quarters < ((world_daylength/2)+11-4)) or (at == 'knowledge' and vines_passable and quarters > ((world_daylength/2)+11+4))" ) :
            pass
        'I can’t cross these creepers on my own. (disabled)' if not vines_passable and vines_water:
            pass
        'Nothing stops me from riding ahead. (disabled)' if vines_passable:
            pass

label vines_poked01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the creepers with a drawn axe.')
    $ vines_poked += 1
    $ at_unlock_knowledge = 0
    $ pc_hp = limit_pc_hp(pc_hp-1)
    show minus1hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
    if pc_class == "scholar" and not vines_mushroom:
        $ at_unlock_knowledge = 1
        $ at = 0
    menu:
        'Before you get in reach to poke them, the creepers bend backward swiftly, then swing at you with the strength of a troll. You try to dodge, but the hit flings you back, landing you on your back. Gasping, you crawl away and rise to your feet, but the plants don’t follow you.
        '
        'I approach the creepers with a drawn axe.' if not vines_passable and not vines_poked:
            jump vines_poked01
        'I pick up some branches and throw them at the creepers.' if not vines_passable and not vines_poked:
            jump vines_poked02
        'I examine the water.' if not vines_passable and vines_poked and not vines_water:
            jump vineswater01
        'I approach the mushroom growing behind the creepers.' ( condition="at == 'knowledge' and vines_passable and quarters >= ((world_daylength/2)+11-4) and quarters <= ((world_daylength/2)+11+4)" ) :
            jump vinesmushroom01
        'I recognize the mushroom growing behind the creepers. Once they’re gone, I can pick it, but only in the middle of the day. (disabled)' ( condition="at == 'knowledge' and not vines_passable" ) :
            pass
        'To properly use the mushroom growing behind the creepers, I have to pick it in the middle of the day. (disabled)' ( condition="(at == 'knowledge' and vines_passable and quarters < ((world_daylength/2)+11-4)) or (at == 'knowledge' and vines_passable and quarters > ((world_daylength/2)+11+4))" ) :
            pass
        'I can’t cross these creepers on my own. (disabled)' if not vines_passable and vines_water:
            pass
        'Nothing stops me from riding ahead. (disabled)' if vines_passable:
            pass

label vines_poked02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick up some branches and throw them at the creepers.')
    $ vines_poked += 1
    $ at_unlock_knowledge = 0
    $ minutes += 5
    if pc_class == "scholar" and not vines_mushroom:
        $ at_unlock_knowledge = 1
        $ at = 0
    menu:
        'You step among the muds and grasses, but some desperate creature scraped this land clean of any wood they could eat - it takes you a few moments before you find any that doesn’t fall apart under your touch.
        \n\nOnce it hits the creepers, they bend backward swiftly, then try to reach you with a loud swish, getting a bit longer as they repeat this attempt a few times. You tell your mount to step away, but the plants don’t chase after you.
        '
        'I approach the creepers with a drawn axe.' if not vines_passable and not vines_poked:
            jump vines_poked01
        'I pick up some branches and throw them at the creepers.' if not vines_passable and not vines_poked:
            jump vines_poked02
        'I examine the water.' if not vines_passable and vines_poked and not vines_water:
            jump vineswater01
        'I approach the mushroom growing behind the creepers.' ( condition="at == 'knowledge' and vines_passable and quarters >= ((world_daylength/2)+11-4) and quarters <= ((world_daylength/2)+11+4)" ) :
            jump vinesmushroom01
        'I recognize the mushroom growing behind the creepers. Once they’re gone, I can pick it, but only in the middle of the day. (disabled)' ( condition="at == 'knowledge' and not vines_passable" ) :
            pass
        'To properly use the mushroom growing behind the creepers, I have to pick it in the middle of the day. (disabled)' ( condition="(at == 'knowledge' and vines_passable and quarters < ((world_daylength/2)+11-4)) or (at == 'knowledge' and vines_passable and quarters > ((world_daylength/2)+11+4))" ) :
            pass
        'I can’t cross these creepers on my own. (disabled)' if not vines_passable and vines_water:
            pass
        'Nothing stops me from riding ahead. (disabled)' if vines_passable:
            pass

label vineswater01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the water.')
    $ vines_water = 1
    $ at_unlock_knowledge = 0
    $ minutes += 10
    if pc_class == "scholar" and not vines_mushroom:
        $ at_unlock_knowledge = 1
        $ at = 0
    $ description_whitemarshes07 = "It’s possible that the only paths connecting the deeper bogs with the rest of the peninsula were built from scratch by the locals."
    menu:
        'The dirty ponds are hard to see through. It takes a few minutes before you find a stick long enough to poke the water and reach its bottom. Even at the very bank the water is as deep as your palfrey is tall, and it’s quite possible that none of these conveniently spread paths appeared here on their own. Could it be that the locals carried much of this soil by themselves, connecting the deeper bogs with the other parts of the peninsula?
        \n\nBefore you have time to dwell on it, you jump back, dodging the strike of a green saurian. You run away so quickly that it gives up its pursuit.
        '
        'I approach the creepers with a drawn axe.' if not vines_passable and not vines_poked:
            jump vines_poked01
        'I pick up some branches and throw them at the creepers.' if not vines_passable and not vines_poked:
            jump vines_poked02
        'I examine the water.' if not vines_passable and vines_poked and not vines_water:
            jump vineswater01
        'I approach the mushroom growing behind the creepers.' ( condition="at == 'knowledge' and vines_passable and quarters >= ((world_daylength/2)+11-4) and quarters <= ((world_daylength/2)+11+4)" ) :
            jump vinesmushroom01
        'I recognize the mushroom growing behind the creepers. Once they’re gone, I can pick it, but only in the middle of the day. (disabled)' ( condition="at == 'knowledge' and not vines_passable" ) :
            pass
        'To properly use the mushroom growing behind the creepers, I have to pick it in the middle of the day. (disabled)' ( condition="(at == 'knowledge' and vines_passable and quarters < ((world_daylength/2)+11-4)) or (at == 'knowledge' and vines_passable and quarters > ((world_daylength/2)+11+4))" ) :
            pass
        'I can’t cross these creepers on my own. (disabled)' if not vines_passable and vines_water:
            pass
        'Nothing stops me from riding ahead. (disabled)' if vines_passable:
            pass

label vinesmushroom01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the mushroom growing behind the creepers.')
    $ at_unlock_knowledge = 0
    $ vines_mushroom = 1
    $ at = 0
    show vinesnomushroom at basicfade
    $ item_bogfriend += 1
    $ renpy.notify("You added a bogfriend to your bag of ingredients.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You added a bogfriend to your bag of ingredients.{/i}')
    if pc_class == "scholar" and not vines_mushroom:
        $ at_unlock_knowledge = 1
        $ at = 0
    menu:
        'Once you cover your hands with protective gloves, you get it done with a swift cut. The bogfriend is brown, with a few red, vertical lines, and a cap covered with holes that resemble fish gills. As you’re shaking off the soil, you expect the mushroom to be slimy, but the opposite is true - once cleaned, it resembles a morel, but you know well how poisonous it can get.
        \n\nYou wrap it with a cloth and hide it among your bundles.
        '
        'I approach the creepers with a drawn axe.' if not vines_passable and not vines_poked:
            jump vines_poked01
        'I pick up some branches and throw them at the creepers.' if not vines_passable and not vines_poked:
            jump vines_poked02
        'I examine the water.' if not vines_passable and vines_poked and not vines_water:
            jump vineswater01
        'I approach the mushroom growing behind the creepers.' ( condition="at == 'knowledge' and vines_passable and quarters >= ((world_daylength/2)+11-4) and quarters <= ((world_daylength/2)+11+4)" ) :
            jump vinesmushroom01
        'I recognize the mushroom growing behind the creepers. Once they’re gone, I can pick it, but only in the middle of the day. (disabled)' ( condition="at == 'knowledge' and not vines_passable" ) :
            pass
        'To properly use the mushroom growing behind the creepers, I have to pick it in the middle of the day. (disabled)' ( condition="(at == 'knowledge' and vines_passable and quarters < ((world_daylength/2)+11-4)) or (at == 'knowledge' and vines_passable and quarters > ((world_daylength/2)+11+4))" ) :
            pass
        'I can’t cross these creepers on my own. (disabled)' if not vines_passable and vines_water:
            pass
        'Nothing stops me from riding ahead. (disabled)' if vines_passable:
            pass

label vines_perma_closed_seen01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        '[vines_fluff] The twitches of the creepers are even more rapid than they used to be, as if they’re trying to reach you long before you approach them.
        '
        'I won’t cross this road anytime soon. (disabled)':
            pass
