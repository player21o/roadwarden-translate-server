###################### GIANT STATUE
default giantstatue_firsttime = 0
default giantstatue_fluff = ""
default giantstatue_fluff_old = ""

default giantstatue_rock = 0

default giantstatue_scholarclue = 0
default giantstatue_amuletused = 0
default giantstatue_approached = 0
default giantstatue_blood = 0

default giantstatue_stance = "standing" # "kneeling" "crouching" "lying" "sitting"
default giantstatue_stance_fluff = "You’re standing in front of the statue."
default giantstatue_kneeled = 0
default giantstatue_pray_tried = 0
default giantstatue_pray_knows = 0
default giantstatue_pray_refused = 0
default giantstatue_pray_map_meaning = 0
default giantstatue_pray_map_learned = 0

default giantstatue_insulted = 0
default giantstatue_stolen = 0
default giantstatue_awoken = 0

label giantstatue01:
    nvl clear
    $ pc_area = "giantstatue"
    $ renpy.music.play("audio/track_05dolmen.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    if not giantstatue_awoken == day:
        show areapicture giantstatue01 at basicfade
    else:
        show areapicture giantstatue02 at basicfade
    label giantstatue_fluffloop:
        $ giantstatue_fluff = renpy.random.choice(['An eagle is sitting on the head of the statue, tearing a chunk of meat. Once it flies away, it carries the corpse of a fox that’s as large as its own shell.', 'It’s solemnly quiet here, like in a monastery garden.', 'The grass spreads onto the beaten path slowly. You almost don’t notice a fat rat that flees into the bushes.', 'There’s an unsettling rustle among the bushes above you. Just in case, you reach for your blade.', 'Your mount welcomes the stairs with an annoyed snort, and its ears flick back and forth.'])
        if giantstatue_fluff_old == giantstatue_fluff:
            jump giantstatue_fluffloop
        else:
            $ giantstatue_fluff_old = giantstatue_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not giantstatue_firsttime:
        $ world_known_areas += 1
        $ giantstatue_firsttime = 1
        $ ghoulcave_unlocked = 1
        $ mountainroad_unlocked = 1
        jump giantstatuefirsttime01
    else:
        jump giantstatueregular01

label giantstatuefirsttime01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if (pc_class == "scholar" and not giantstatue_rock and not item_powderedrock and not item_blindingpowder) or (pc_class == "scholar" and giantstatue_awoken and not giantstatue_pray_map_learned):
        $ at_unlock_knowledge = 1
        $ at = 0
    if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
        $ at_unlock_spell = 1
        $ manacost = 1
    menu:
        'The unbodied keeper of the garden is standing still, with a dark cloak on their shoulders and an eyeless face observing the woodlands. Their club, more than three times as tall as you are, is made of a single piece of rock, and could squash you by simply collapsing, without anyone’s will.
        \n\nA set of stairs leads into a convenient, corridor-like ravine. The gentle wind carries no shouts or scent of blood.
        '
        'I see something among the rocks.' ( condition="at == 'knowledge' and not giantstatue_rock" ):
            jump giantstatuepickingupbasalt01
        'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
            jump giantstatueusingamulet01
        'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
            pass
        'I approach the statue.' if not giantstatue_awoken and not giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue01
        'I return to the statue.' if not giantstatue_awoken and giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue02
        'I don’t know a prayer that could help me here. (disabled)' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and not giantstatue_pray_knows and not giantstatue_insulted and not giantstatue_pray_refused:
            pass
        'I kneel in front of the statue and speak the words of prayer I’ve learned.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and giantstatue_pray_knows and pc_religion != "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer I’ve learned.')
            jump giantstatuepraying01
        'I kneel in front of the statue and speak the words of prayer, just like my ancestors would.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and pc_religion == "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer, just like my ancestors would.')
            jump giantstatuepraying01alt
        '{image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp and at != 'knowledge'" ):
            jump giantstatuememorizingstatue01
        'I don’t need to memorize the signs. I’ll just write them down.' ( condition="at == 'knowledge' and giantstatue_awoken == day and not giantstatue_pray_map_learned" ):
            jump giantstatuememorizingstatue01alt
        'I can’t even imagine memorizing all of these little details. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp <= 0" ):
            pass
        'I pray to the statue again.' ( condition="giantstatue_awoken and giantstatue_awoken != day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp" ):
            jump giantstatuepraying02
        'I’m exhausted. I won’t learn anything from the statue. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken == day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp <= 0" ):
            pass
        'Seems like I’m done here. (disabled)' if giantstatue_pray_map_learned:
            pass
        'I don’t think the spirit in the statue is going to forgive me anytime soon. (disabled)' if giantstatue_insulted:
            pass
        'As a loyal follower of The Wright, I refuse to pray to an evil spirit. (disabled)' if giantstatue_pray_refused:
            pass

label giantstatueregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if (pc_class == "scholar" and not giantstatue_rock and not item_powderedrock and not item_blindingpowder) or (pc_class == "scholar" and giantstatue_awoken and not giantstatue_pray_map_learned):
        $ at_unlock_knowledge = 1
        $ at = 0
    if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
        $ at_unlock_spell = 1
        $ manacost = 1
    menu:
        '[giantstatue_fluff]
        '
        'I see something among the rocks.' ( condition="at == 'knowledge' and not giantstatue_rock" ):
            jump giantstatuepickingupbasalt01
        'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
            jump giantstatueusingamulet01
        'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
            pass
        'I approach the statue.' if not giantstatue_awoken and not giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue01
        'I return to the statue.' if not giantstatue_awoken and giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue02
        'I don’t know a prayer that could help me here. (disabled)' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and not giantstatue_pray_knows and not giantstatue_insulted and not giantstatue_pray_refused:
            pass
        'I kneel in front of the statue and speak the words of prayer I’ve learned.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and giantstatue_pray_knows and pc_religion != "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer I’ve learned.')
            jump giantstatuepraying01
        'I kneel in front of the statue and speak the words of prayer, just like my ancestors would.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and pc_religion == "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer, just like my ancestors would.')
            jump giantstatuepraying01alt
        '{image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp and at != 'knowledge'" ):
            jump giantstatuememorizingstatue01
        'I don’t need to memorize the signs. I’ll just write them down.' ( condition="at == 'knowledge' and giantstatue_awoken == day and not giantstatue_pray_map_learned" ):
            jump giantstatuememorizingstatue01alt
        'I can’t even imagine memorizing all of these little details. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp <= 0" ):
            pass
        'I pray to the statue again.' ( condition="giantstatue_awoken and giantstatue_awoken != day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp" ):
            jump giantstatuepraying02
        'I’m exhausted. I won’t learn anything from the statue. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken == day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp <= 0" ):
            pass
        'Seems like I’m done here. (disabled)' if giantstatue_pray_map_learned:
            pass
        'I don’t think the spirit in the statue is going to forgive me anytime soon. (disabled)' if giantstatue_insulted:
            pass
        'As a loyal follower of The Wright, I refuse to pray to an evil spirit. (disabled)' if giantstatue_pray_refused:
            pass

label giantstatueafterinteraction01:
    $ at_unlock_spell = 0
    $ at_unlock_knowledge = 0
    $ at = 0
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if (pc_class == "scholar" and not giantstatue_rock and not item_powderedrock and not item_blindingpowder) or (pc_class == "scholar" and giantstatue_awoken and not giantstatue_pray_map_learned):
        $ at_unlock_knowledge = 1
        $ at = 0
    if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
        $ at_unlock_spell = 1
        $ manacost = 1
    menu:
        'You return to {color=#f6d6bd}[horsename]{/color}.
        '
        'I see something among the rocks.' ( condition="at == 'knowledge' and not giantstatue_rock" ):
            jump giantstatuepickingupbasalt01
        'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
            jump giantstatueusingamulet01
        'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
            pass
        'I approach the statue.' if not giantstatue_awoken and not giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue01
        'I return to the statue.' if not giantstatue_awoken and giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue02
        'I don’t know a prayer that could help me here. (disabled)' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and not giantstatue_pray_knows and not giantstatue_insulted and not giantstatue_pray_refused:
            pass
        'I kneel in front of the statue and speak the words of prayer I’ve learned.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and giantstatue_pray_knows and pc_religion != "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer I’ve learned.')
            jump giantstatuepraying01
        'I kneel in front of the statue and speak the words of prayer, just like my ancestors would.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and pc_religion == "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer, just like my ancestors would.')
            jump giantstatuepraying01alt
        '{image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp and at != 'knowledge'" ):
            jump giantstatuememorizingstatue01
        'I don’t need to memorize the signs. I’ll just write them down.' ( condition="at == 'knowledge' and giantstatue_awoken == day and not giantstatue_pray_map_learned" ):
            jump giantstatuememorizingstatue01alt
        'I can’t even imagine memorizing all of these little details. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp <= 0" ):
            pass
        'I pray to the statue again.' ( condition="giantstatue_awoken and giantstatue_awoken != day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp" ):
            jump giantstatuepraying02
        'I’m exhausted. I won’t learn anything from the statue. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken == day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp <= 0" ):
            pass
        'Seems like I’m done here. (disabled)' if giantstatue_pray_map_learned:
            pass
        'I don’t think the spirit in the statue is going to forgive me anytime soon. (disabled)' if giantstatue_insulted:
            pass
        'As a loyal follower of The Wright, I refuse to pray to an evil spirit. (disabled)' if giantstatue_pray_refused:
            pass

label giantstatuepickingupbasalt01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I see something among the rocks.')
    $ at_unlock_knowledge = 0
    $ at_unlock_spell = 0
    $ at = 0
    $ giantstatue_rock = 1
    $ item_rocktobepowdered += 1
    $ renpy.notify("You add a basalt rock to your bag of ingredients.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You add a basalt rock to your bag of ingredients.{/i}')
    if (pc_class == "scholar" and not giantstatue_rock and not item_powderedrock and not item_blindingpowder) or (pc_class == "scholar" and giantstatue_awoken and not giantstatue_pray_map_learned):
        $ at_unlock_knowledge = 1
        $ at = 0
    if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
        $ at_unlock_spell = 1
        $ manacost = 1
    menu:
        'One of the rocks placed behind the statue does not belong here. A dark basalt, the size of your fist.
        \n\nYou look at the mountain peaks and let out a sigh. You could use such a rock to make blinding powder, but smashing it into dust won’t be enough. You have to perform the ritual the right way, ideally at the top of the mountain, or at least as high as you can get.
        \n\nFor now, you put the rock into a sack.
        '
        'I see something among the rocks.' ( condition="at == 'knowledge' and not giantstatue_rock" ):
            jump giantstatuepickingupbasalt01
        'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
            jump giantstatueusingamulet01
        'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
            pass
        'I approach the statue.' if not giantstatue_awoken and not giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue01
        'I return to the statue.' if not giantstatue_awoken and giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue02
        'I don’t know a prayer that could help me here. (disabled)' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and not giantstatue_pray_knows and not giantstatue_insulted and not giantstatue_pray_refused:
            pass
        'I kneel in front of the statue and speak the words of prayer I’ve learned.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and giantstatue_pray_knows and pc_religion != "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer I’ve learned.')
            jump giantstatuepraying01
        'I kneel in front of the statue and speak the words of prayer, just like my ancestors would.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and pc_religion == "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer, just like my ancestors would.')
            jump giantstatuepraying01alt
        '{image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp and at != 'knowledge'" ):
            jump giantstatuememorizingstatue01
        'I don’t need to memorize the signs. I’ll just write them down.' ( condition="at == 'knowledge' and giantstatue_awoken == day and not giantstatue_pray_map_learned" ):
            jump giantstatuememorizingstatue01alt
        'I can’t even imagine memorizing all of these little details. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp <= 0" ):
            pass
        'I pray to the statue again.' ( condition="giantstatue_awoken and giantstatue_awoken != day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp" ):
            jump giantstatuepraying02
        'I’m exhausted. I won’t learn anything from the statue. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken == day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp <= 0" ):
            pass
        'Seems like I’m done here. (disabled)' if giantstatue_pray_map_learned:
            pass
        'I don’t think the spirit in the statue is going to forgive me anytime soon. (disabled)' if giantstatue_insulted:
            pass
        'As a loyal follower of The Wright, I refuse to pray to an evil spirit. (disabled)' if giantstatue_pray_refused:
            pass

label giantstatueusingamulet01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use my amulets to look for magic in the area.')
    $ at_unlock_knowledge = 0
    $ at_unlock_spell = 0
    $ mana = limit_mana(mana-manacost)
    $ at = 0
    $ giantstatue_amuletused = 1
    $ quarters += 1
    $ quest_sleepinggiant_description01 = "My amulets have found magic in the area."
    if not quest_sleepinggiant:
        $ quest_sleepinggiant = 1
        $ renpy.notify("New entry: The Sleeping Giant")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Sleeping Giant{/i}')
    else:
        $ renpy.notify("Journal updated: The Sleeping Giant")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Sleeping Giant{/i}')
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
    if (pc_class == "scholar" and not giantstatue_rock and not item_powderedrock and not item_blindingpowder) or (pc_class == "scholar" and giantstatue_awoken and not giantstatue_pray_map_learned):
        $ at_unlock_knowledge = 1
        $ at = 0
    if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
        $ at_unlock_spell = 1
        $ manacost = 1
    menu:
        'You unpack the wooden spheres, pleasantly smooth and light. The entire set fits in the palm of your hand. You place them in various spots - on the socle, on the statue’s disembodied boot, on the nearby ground. You begin the ritual, after which all you can do is wait. You let {color=#f6d6bd}[horsename]{/color} graze for a bit, making sure there are no monsters in your vicinity.
        \n\nWhen you return to collect your amulets, they differ from each other. The closer they were to the statue, the warmer they got, even if cloaked by shadows. Those placed on the statue’s sides and behind it are all cold, while the one placed on the ground directly in front of it is as warm as your own skin.
        \n\nYou shake the spheres until they cool off, then hide them in your satchel.
        '
        'I see something among the rocks.' ( condition="at == 'knowledge' and not giantstatue_rock" ):
            jump giantstatuepickingupbasalt01
        'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
            jump giantstatueusingamulet01
        'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
            pass
        'I approach the statue.' if not giantstatue_awoken and not giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue01
        'I return to the statue.' if not giantstatue_awoken and giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue02
        'I don’t know a prayer that could help me here. (disabled)' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and not giantstatue_pray_knows and not giantstatue_insulted and not giantstatue_pray_refused:
            pass
        'I kneel in front of the statue and speak the words of prayer I’ve learned.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and giantstatue_pray_knows and pc_religion != "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer I’ve learned.')
            jump giantstatuepraying01
        'I kneel in front of the statue and speak the words of prayer, just like my ancestors would.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and pc_religion == "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer, just like my ancestors would.')
            jump giantstatuepraying01alt
        '{image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp and at != 'knowledge'" ):
            jump giantstatuememorizingstatue01
        'I don’t need to memorize the signs. I’ll just write them down.' ( condition="at == 'knowledge' and giantstatue_awoken == day and not giantstatue_pray_map_learned" ):
            jump giantstatuememorizingstatue01alt
        'I can’t even imagine memorizing all of these little details. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp <= 0" ):
            pass
        'I pray to the statue again.' ( condition="giantstatue_awoken and giantstatue_awoken != day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp" ):
            jump giantstatuepraying02
        'I’m exhausted. I won’t learn anything from the statue. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken == day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp <= 0" ):
            pass
        'Seems like I’m done here. (disabled)' if giantstatue_pray_map_learned:
            pass
        'I don’t think the spirit in the statue is going to forgive me anytime soon. (disabled)' if giantstatue_insulted:
            pass
        'As a loyal follower of The Wright, I refuse to pray to an evil spirit. (disabled)' if giantstatue_pray_refused:
            pass

label giantstatueprayingALL:
    label giantstatuepraying00:
        $ giantstatue_pray_tried = 1
        $ quest_sleepinggiant_description00 = "I have reason to believe that the huge statue at the foot of the mountain is tied to a ritual of sorts."
        if not quest_sleepinggiant:
            $ quest_sleepinggiant = 1
            $ renpy.notify("New entry: The Sleeping Giant")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Sleeping Giant{/i}')
        else:
            $ renpy.notify("Journal updated: The Sleeping Giant")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Sleeping Giant{/i}')
        if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
            $ pc_faithpoints_opportunities += 1
            menu:
                'You say a few words, and your thoughts are unusually keen and focused, as if you’ve entered a new stage of the ritual. You utter a complete, short prayer, but nothing happens.
                \n\nYou suddenly hesitate. This is not something Wright’s followers are supposed to do.
                '
                'I don’t care, I won’t sabotage my journey now.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care, I won’t sabotage my journey now.')
                    if pc_religion == "theunitedchurch":
                        $ pc_faithpoints -= 3
                    else:
                        $ pc_faithpoints -= 2
                    menu:
                        'As your head leans even lower, it feels heavier, and your heart beats faster.
                        '
                        'I repeat the phrases in the Old Speech that I was taught before.' if giantstatue_pray_knows and not pc_religion == "pagan":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I repeat the phrases in the Old Speech that I was taught before.')
                            jump giantstatuepraying01
                        'I try my best to imagine how a pagan would pray.' if pc_religion != "pagan" and not giantstatue_pray_knows:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try my best to imagine how a pagan would pray.')
                            jump giantstatuepraying00b
                'Whatever this statue does, I can live without it. I won’t hinder my faith.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Whatever this statue does, I can live without it. I won’t hinder my faith faith.')
                    $ giantstatue_pray_refused = 1
                    $ quest_sleepinggiant_description05 = "I’ve decided to stay true to my faith. I won’t pray at the statue."
                    $ renpy.notify("Quest completed: The Sleeping Giant")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Sleeping Giant{/i}')
                    $ quest_sleepinggiant = 3
                    if pc_religion == "theunitedchurch":
                        $ pc_faithpoints += 3
                    else:
                        $ pc_faithpoints += 2
                    $ at_unlock_spell = 0
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    if (pc_class == "scholar" and not giantstatue_rock and not item_powderedrock and not item_blindingpowder) or (pc_class == "scholar" and giantstatue_awoken and not giantstatue_pray_map_learned):
                        $ at_unlock_knowledge = 1
                        $ at = 0
                    if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
                        $ at_unlock_spell = 1
                        $ manacost = 1
                    menu:
                        'As you straighten up, your shoulders and head are much lighter. You blink, and the area seems brighter.
                        '
                        'I see something among the rocks.' ( condition="at == 'knowledge' and not giantstatue_rock" ):
                            jump giantstatuepickingupbasalt01
                        'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                            jump giantstatueusingamulet01
                        'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
                            pass
                        'I approach the statue.' if not giantstatue_awoken and not giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
                            jump giantstatueinteractingstatue01
                        'I return to the statue.' if not giantstatue_awoken and giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
                            jump giantstatueinteractingstatue02
                        'I don’t know a prayer that could help me here. (disabled)' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and not giantstatue_pray_knows and not giantstatue_insulted and not giantstatue_pray_refused:
                            pass
                        'I kneel in front of the statue and speak the words of prayer I’ve learned.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and giantstatue_pray_knows and pc_religion != "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer I’ve learned.')
                            jump giantstatuepraying01
                        'I kneel in front of the statue and speak the words of prayer, just like my ancestors would.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and pc_religion == "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer, just like my ancestors would.')
                            jump giantstatuepraying01alt
                        '{image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp and at != 'knowledge'" ):
                            jump giantstatuememorizingstatue01
                        'I don’t need to memorize the signs. I’ll just write them down.' ( condition="at == 'knowledge' and giantstatue_awoken == day and not giantstatue_pray_map_learned" ):
                            jump giantstatuememorizingstatue01alt
                        'I can’t even imagine memorizing all of these little details. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp <= 0" ):
                            pass
                        'I pray to the statue again.' ( condition="giantstatue_awoken and giantstatue_awoken != day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp" ):
                            jump giantstatuepraying02
                        'I’m exhausted. I won’t learn anything from the statue. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken == day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp <= 0" ):
                            pass
                        'Seems like I’m done here. (disabled)' if giantstatue_pray_map_learned:
                            pass
                        'I don’t think the spirit in the statue is going to forgive me anytime soon. (disabled)' if giantstatue_insulted:
                            pass
                        'As a loyal follower of The Wright, I refuse to pray to an evil spirit. (disabled)' if giantstatue_pray_refused:
                            pass
        else:
            menu:
                'You say a few words, and your thoughts are unusually keen and focused, as if you’ve entered a new stage of the ritual.
                '
                'I repeat the phrases in the Old Speech that I was taught before.' if giantstatue_pray_knows and not pc_religion == "pagan":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I repeat the phrases in the Old Speech that I was taught before.')
                    jump giantstatuepraying01
                'I follow the lead of my ancestors, and pray as they would.' if pc_religion == "pagan":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the lead of my ancestors, and pray as they would.')
                    jump giantstatuepraying01alt
                'I try my best to imagine how a pagan would pray.' if pc_religion != "pagan" and not giantstatue_pray_knows:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try my best to imagine how a pagan would pray.')
                    jump giantstatuepraying00b

    label giantstatuepraying00b:
        $ quarters += 1
        $ quest_sleepinggiant_description02 = "I won’t be able to get anywhere without a proper prayer, or a spell."
        $ renpy.notify("Journal updated: The Sleeping Giant")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Sleeping Giant{/i}')
        if (pc_class == "scholar"):
            $ at_unlock_knowledge = 1
            $ at = 0
        menu:
            'You try to address your ancestors, the forest spirits, the sky itself, but to no avail. Maybe the things you say are off the mark, or maybe the statue needs a specific password you can’t guess by yourself.
            '
            'After thinking about it, I realize that pagans would most likely use the {i}Old Speech{/i} while casting magic. Maybe an elder would be able to help me. (disabled)' ( condition="at == 'knowledge'" ):
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01

    label giantstatuepraying01:
        $ at_unlock_knowledge = 0
        $ at_unlock_spell = 0
        $ at = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
            $ custom1 = " and which sound to you like a dragon’s hiss."
        else:
            $ custom1 = ". Their empty sounds mean nothing to you, but the wind is gentle, and there are no monsters to distract you."
        menu:
            'You place the blanket beneath your knees. You bow down your head and stretch out your arms, reciting the strange sounds you’ve memorized[custom1]
            \n\n{color=#f6d6bd}[horsename]{/color} grazes on the grass, unmoved by your efforts.
            '
            'Long minutes go by.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Long minutes go by.')
                $ quarters += 1
                $ giantstatue_awoken = day
                show areapicture giantstatue02 at basicfade
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                if (pc_class == "scholar" and not giantstatue_rock and not item_powderedrock and not item_blindingpowder) or (pc_class == "scholar" and giantstatue_awoken and not giantstatue_pray_map_learned):
                    $ at_unlock_knowledge = 1
                    $ at = 0
                if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
                    $ at_unlock_spell = 1
                    $ manacost = 1
                $ quest_sleepinggiant_description03 = "I’ve managed to awaken the statue, but I still need to spend time by it to memorize its secrets."
                $ renpy.notify("Journal updated: The Sleeping Giant")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Sleeping Giant{/i}')
                menu:
                    'Tiny stars, white, blue, orange, and yellow, emerge from the dark cloak, one after another. Some of them grow in size and intensity, while many more stay dim. After a few moments, they move no more, and you get used to the hollow darkness remaining between them.
                    '
                    'I see something among the rocks.' ( condition="at == 'knowledge' and not giantstatue_rock" ):
                        jump giantstatuepickingupbasalt01
                    'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                        jump giantstatueusingamulet01
                    'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
                        pass
                    'I approach the statue.' if not giantstatue_awoken and not giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
                        jump giantstatueinteractingstatue01
                    'I return to the statue.' if not giantstatue_awoken and giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
                        jump giantstatueinteractingstatue02
                    'I don’t know a prayer that could help me here. (disabled)' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and not giantstatue_pray_knows and not giantstatue_insulted and not giantstatue_pray_refused:
                        pass
                    'I kneel in front of the statue and speak the words of prayer I’ve learned.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and giantstatue_pray_knows and pc_religion != "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer I’ve learned.')
                        jump giantstatuepraying01
                    'I kneel in front of the statue and speak the words of prayer, just like my ancestors would.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and pc_religion == "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer, just like my ancestors would.')
                        jump giantstatuepraying01alt
                    '{image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp and at != 'knowledge'" ):
                        jump giantstatuememorizingstatue01
                    'I don’t need to memorize the signs. I’ll just write them down.' ( condition="at == 'knowledge' and giantstatue_awoken == day and not giantstatue_pray_map_learned" ):
                        jump giantstatuememorizingstatue01alt
                    'I can’t even imagine memorizing all of these little details. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp <= 0" ):
                        pass
                    'I pray to the statue again.' ( condition="giantstatue_awoken and giantstatue_awoken != day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp" ):
                        jump giantstatuepraying02
                    'I’m exhausted. I won’t learn anything from the statue. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken == day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp <= 0" ):
                        pass
                    'Seems like I’m done here. (disabled)' if giantstatue_pray_map_learned:
                        pass
                    'I don’t think the spirit in the statue is going to forgive me anytime soon. (disabled)' if giantstatue_insulted:
                        pass
                    'As a loyal follower of The Wright, I refuse to pray to an evil spirit. (disabled)' if giantstatue_pray_refused:
                        pass

    label giantstatuepraying01alt:
        $ at_unlock_knowledge = 0
        $ at_unlock_spell = 0
        $ at = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'You place the blanket beneath your knees and prepare yourself for a long prayer. You bow down your head and stretch out your arms, whispering the words that simply {i}feel{/i} right. You address the spirits living in the garden and the mountains, asking the ancestors’ for guidance and wisdom. You can’t be sure they’re listening, but with many breaths, your thoughts get clear and tranquil.
            \n\nEven {color=#f6d6bd}[horsename]{/color} is quiet.
            '
            'I pay no attention to the passing minutes.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pay no attention to the passing minutes.')
                $ quarters += 1
                $ giantstatue_awoken = day
                show areapicture giantstatue02 at basicfade
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                if (pc_class == "scholar" and not giantstatue_rock and not item_powderedrock and not item_blindingpowder) or (pc_class == "scholar" and giantstatue_awoken and not giantstatue_pray_map_learned):
                    $ at_unlock_knowledge = 1
                    $ at = 0
                if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
                    $ at_unlock_spell = 1
                    $ manacost = 1
                $ pc_faithpoints += 1
                $ quest_sleepinggiant_description03 = "I’ve managed to awaken the statue, but I still need to spend time by it to memorize its secrets."
                $ renpy.notify("Journal updated: The Sleeping Giant")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Sleeping Giant{/i}')
                menu:
                    'One after another, tiny stars, white, blue, orange, and yellow, emerge from the dark cloak. Some of them get wider and more intense, while many more stay dim. After a few moments, they move no more, and you get used to the hollow darkness remaining between them.
                    '
                    'I see something among the rocks.' ( condition="at == 'knowledge' and not giantstatue_rock" ):
                        jump giantstatuepickingupbasalt01
                    'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                        jump giantstatueusingamulet01
                    'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
                        pass
                    'I approach the statue.' if not giantstatue_awoken and not giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
                        jump giantstatueinteractingstatue01
                    'I return to the statue.' if not giantstatue_awoken and giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
                        jump giantstatueinteractingstatue02
                    'I don’t know a prayer that could help me here. (disabled)' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and not giantstatue_pray_knows and not giantstatue_insulted and not giantstatue_pray_refused:
                        pass
                    'I kneel in front of the statue and speak the words of prayer I’ve learned.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and giantstatue_pray_knows and pc_religion != "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer I’ve learned.')
                        jump giantstatuepraying01
                    'I kneel in front of the statue and speak the words of prayer, just like my ancestors would.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and pc_religion == "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer, just like my ancestors would.')
                        jump giantstatuepraying01alt
                    '{image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp and at != 'knowledge'" ):
                        jump giantstatuememorizingstatue01
                    'I don’t need to memorize the signs. I’ll just write them down.' ( condition="at == 'knowledge' and giantstatue_awoken == day and not giantstatue_pray_map_learned" ):
                        jump giantstatuememorizingstatue01alt
                    'I can’t even imagine memorizing all of these little details. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp <= 0" ):
                        pass
                    'I pray to the statue again.' ( condition="giantstatue_awoken and giantstatue_awoken != day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp" ):
                        jump giantstatuepraying02
                    'I’m exhausted. I won’t learn anything from the statue. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken == day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp <= 0" ):
                        pass
                    'Seems like I’m done here. (disabled)' if giantstatue_pray_map_learned:
                        pass
                    'I don’t think the spirit in the statue is going to forgive me anytime soon. (disabled)' if giantstatue_insulted:
                        pass
                    'As a loyal follower of The Wright, I refuse to pray to an evil spirit. (disabled)' if giantstatue_pray_refused:
                        pass

    label giantstatuepraying02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pray to the statue again.')
        $ at_unlock_knowledge = 0
        $ at_unlock_spell = 0
        $ at = 0
        $ quarters += 1
        $ giantstatue_awoken = day
        show areapicture giantstatue02 at basicfade
        if (pc_class == "scholar" and not giantstatue_rock and not item_powderedrock and not item_blindingpowder) or (pc_class == "scholar" and giantstatue_awoken and not giantstatue_pray_map_learned):
            $ at_unlock_knowledge = 1
            $ at = 0
        if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
            $ at_unlock_spell = 1
            $ manacost = 1
        menu:
            'Your prayer is long and rough on your knees, but it does awaken the statue.
            '
            'I see something among the rocks.' ( condition="at == 'knowledge' and not giantstatue_rock" ):
                jump giantstatuepickingupbasalt01
            'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                jump giantstatueusingamulet01
            'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
                pass
            'I approach the statue.' if not giantstatue_awoken and not giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
                jump giantstatueinteractingstatue01
            'I return to the statue.' if not giantstatue_awoken and giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
                jump giantstatueinteractingstatue02
            'I don’t know a prayer that could help me here. (disabled)' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and not giantstatue_pray_knows and not giantstatue_insulted and not giantstatue_pray_refused:
                pass
            'I kneel in front of the statue and speak the words of prayer I’ve learned.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and giantstatue_pray_knows and pc_religion != "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer I’ve learned.')
                jump giantstatuepraying01
            'I kneel in front of the statue and speak the words of prayer, just like my ancestors would.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and pc_religion == "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer, just like my ancestors would.')
                jump giantstatuepraying01alt
            '{image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp and at != 'knowledge'" ):
                jump giantstatuememorizingstatue01
            'I don’t need to memorize the signs. I’ll just write them down.' ( condition="at == 'knowledge' and giantstatue_awoken == day and not giantstatue_pray_map_learned" ):
                jump giantstatuememorizingstatue01alt
            'I can’t even imagine memorizing all of these little details. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp <= 0" ):
                pass
            'I pray to the statue again.' ( condition="giantstatue_awoken and giantstatue_awoken != day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp" ):
                jump giantstatuepraying02
            'I’m exhausted. I won’t learn anything from the statue. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken == day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp <= 0" ):
                pass
            'Seems like I’m done here. (disabled)' if giantstatue_pray_map_learned:
                pass
            'I don’t think the spirit in the statue is going to forgive me anytime soon. (disabled)' if giantstatue_insulted:
                pass
            'As a loyal follower of The Wright, I refuse to pray to an evil spirit. (disabled)' if giantstatue_pray_refused:
                pass

label giantstatuememorizingstatue01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.')
    $ giantstatue_pray_map_learned = 1
    $ at_unlock_knowledge = 0
    $ at_unlock_spell = 0
    $ at = 0
    $ pc_food = limit_pc_food(pc_food-1)
    show minus1food at foodchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
    $ quarters += (7-pc_hp)
    if (pc_class == "scholar" and not giantstatue_rock and not item_powderedrock and not item_blindingpowder) or (pc_class == "scholar" and giantstatue_awoken and not giantstatue_pray_map_learned):
        $ at_unlock_knowledge = 1
        $ at = 0
    if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
        $ at_unlock_spell = 1
        $ manacost = 1
    $ quest_sleepinggiant_description04 = "I’ve memorized the pattern of “stars” that I found at the statue."
    $ renpy.notify("Quest completed: The Sleeping Giant")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Sleeping Giant{/i}')
    $ quest_sleepinggiant = 2
    if pc_hp == 1:
        $ custom1 = "Tired as you are, your head gets heavy, pulling your thoughts away from the tiresome and boring task. For more than an hour you spell out the positions and colors of the larger dots, but whenever you put your memory to the test, it fails you. Finally, led more by your frustration than determination, you manage to get it right, then again and again. You step away and relax your shoulders."
    elif pc_hp == 2:
        $ custom1 = "You keep getting distracted by all sorts of thoughts, but you do your best to stay focused on the tiresome and boring task. For more than an hour you spell out the positions and colors of the larger dots, but whenever you put your memory to the test, it fails you. Finally, with enough determination, you manage to get it right, then again and again. You step away and relax your shoulders."
    elif pc_hp == 3:
        $ custom1 = "You keep getting distracted by sounds and movements, but you do your best to stay focused on the task. For almost an hour you spell out the positions and colors of the larger dots, and some of these attempts fail, others succeed. Finally, you manage to repeat everything from memory, then again and again. You step away convinced you’ve got this."
    elif pc_hp == 4:
        $ custom1 = "For most of the time, you manage to stay focused. After less than an hour you manage to spell out the positions and colors of the larger dots from memory, then again and again. You step away convinced you’ve got this."
    elif pc_hp >= 5:
        $ custom1 = "You manage to stay focused all the way through, getting it done in only half an hour. You spell out the positions and colors of the larger dots from memory, then again and again. You step away convinced you’ve got this."
    menu:
        'You try to get used to the curved surface of the cloak and the plentitude of distracting, small dots. [custom1]
        '
        'I see something among the rocks.' ( condition="at == 'knowledge' and not giantstatue_rock" ):
            jump giantstatuepickingupbasalt01
        'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
            jump giantstatueusingamulet01
        'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
            pass
        'I approach the statue.' if not giantstatue_awoken and not giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue01
        'I return to the statue.' if not giantstatue_awoken and giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
            jump giantstatueinteractingstatue02
        'I don’t know a prayer that could help me here. (disabled)' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and not giantstatue_pray_knows and not giantstatue_insulted and not giantstatue_pray_refused:
            pass
        'I kneel in front of the statue and speak the words of prayer I’ve learned.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and giantstatue_pray_knows and pc_religion != "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer I’ve learned.')
            jump giantstatuepraying01
        'I kneel in front of the statue and speak the words of prayer, just like my ancestors would.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and pc_religion == "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer, just like my ancestors would.')
            jump giantstatuepraying01alt
        '{image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp and at != 'knowledge'" ):
            jump giantstatuememorizingstatue01
        'I don’t need to memorize the signs. I’ll just write them down.' ( condition="at == 'knowledge' and giantstatue_awoken == day and not giantstatue_pray_map_learned" ):
            jump giantstatuememorizingstatue01alt
        'I can’t even imagine memorizing all of these little details. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp <= 0" ):
            pass
        'I pray to the statue again.' ( condition="giantstatue_awoken and giantstatue_awoken != day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp" ):
            jump giantstatuepraying02
        'I’m exhausted. I won’t learn anything from the statue. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken == day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp <= 0" ):
            pass
        'Seems like I’m done here. (disabled)' if giantstatue_pray_map_learned:
            pass
        'I don’t think the spirit in the statue is going to forgive me anytime soon. (disabled)' if giantstatue_insulted:
            pass
        'As a loyal follower of The Wright, I refuse to pray to an evil spirit. (disabled)' if giantstatue_pray_refused:
            pass

    label giantstatuememorizingstatue01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t need to memorize it right now. I’ll just write it down.')
        $ at_unlock_knowledge = 0
        $ at_unlock_spell = 0
        $ at = 0
        $ quarters -= 1
        $ giantstatue_pray_map_learned = 1
        if (pc_class == "scholar" and not giantstatue_rock and not item_powderedrock and not item_blindingpowder) or (pc_class == "scholar" and giantstatue_awoken and not giantstatue_pray_map_learned):
            $ at_unlock_knowledge = 1
            $ at = 0
        if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
            $ at_unlock_spell = 1
            $ manacost = 1
        $ quest_sleepinggiant_description04 = "I’ve recorded the pattern of “stars” that I found at the statue."
        $ renpy.notify("Quest completed: The Sleeping Giant")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Sleeping Giant{/i}')
        $ quest_sleepinggiant = 2
        menu:
            'You grab your wax tablet and copy the larger dots onto it, forming a simple picture that’s much easier to comprehend while it’s flat. You double check your notes, then add a few letters to mark the specific colors, just in case it’s of importance.
            '
            'I see something among the rocks.' ( condition="at == 'knowledge' and not giantstatue_rock" ):
                jump giantstatuepickingupbasalt01
            'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                jump giantstatueusingamulet01
            'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
                pass
            'I approach the statue.' if not giantstatue_awoken and not giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
                jump giantstatueinteractingstatue01
            'I return to the statue.' if not giantstatue_awoken and giantstatue_approached and not giantstatue_pray_tried and not giantstatue_insulted and not giantstatue_pray_refused:
                jump giantstatueinteractingstatue02
            'I don’t know a prayer that could help me here. (disabled)' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and not giantstatue_pray_knows and not giantstatue_insulted and not giantstatue_pray_refused:
                pass
            'I kneel in front of the statue and speak the words of prayer I’ve learned.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and giantstatue_pray_knows and pc_religion != "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer I’ve learned.')
                jump giantstatuepraying01
            'I kneel in front of the statue and speak the words of prayer, just like my ancestors would.' if not giantstatue_awoken and giantstatue_pray_tried and giantstatue_kneeled and pc_religion == "pagan" and not giantstatue_insulted and not giantstatue_pray_refused:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I kneel in front of the statue and speak the words of prayer, just like my ancestors would.')
                jump giantstatuepraying01alt
            '{image=d6} It may take me hours, but I do my best to memorize everything I can about the signs presented on the statue.' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp and at != 'knowledge'" ):
                jump giantstatuememorizingstatue01
            'I don’t need to memorize the signs. I’ll just write them down.' ( condition="at == 'knowledge' and giantstatue_awoken == day and not giantstatue_pray_map_learned" ):
                jump giantstatuememorizingstatue01alt
            'I can’t even imagine memorizing all of these little details. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken and not giantstatue_pray_map_learned and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_awoken == day and pc_hp <= 0" ):
                pass
            'I pray to the statue again.' ( condition="giantstatue_awoken and giantstatue_awoken != day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp" ):
                jump giantstatuepraying02
            'I’m exhausted. I won’t learn anything from the statue. (Required vitality: 1) (disabled)' ( condition="giantstatue_awoken == day and not giantstatue_insulted and not giantstatue_pray_refused and not giantstatue_pray_map_learned and pc_hp <= 0" ):
                pass
            'Seems like I’m done here. (disabled)' if giantstatue_pray_map_learned:
                pass
            'I don’t think the spirit in the statue is going to forgive me anytime soon. (disabled)' if giantstatue_insulted:
                pass
            'As a loyal follower of The Wright, I refuse to pray to an evil spirit. (disabled)' if giantstatue_pray_refused:
                pass

label giantstatueinteractingstatueALL:
    label giantstatueinteractingstatue01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the statue.')
        $ at_unlock_knowledge = 0
        $ at_unlock_spell = 0
        $ at = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ giantstatue_approached = 1
        if pc_class == "mage" and not giantstatue_amuletused and not giantstatue_awoken and not giantstatue_insulted and not giantstatue_pray_refused and giantstatue_approached and not giantstatue_pray_tried:
            $ at_unlock_spell = 1
            $ manacost = 1
        menu:
            'The statue’s face has no features, and the shell ends with the neck, revealing a dark space instead of a torso. You lean closer and notice the coarseness of black-and-gray gritstone, and how bitten by time it is. Both the figure and the socle are stained with white guano. Still, it’s extraordinary work - the weight of the giant doesn’t rest on its club, but rather on the boots, which are cleverly attached to the cloak.
            \n\nSooner or later, something will break, most likely the arms. Without them, the statue won’t hold its stance.
            '
            'I use my amulets to look for magic in the area. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
                jump giantstatueusingamulet01
            'There’s not enough pneuma in my shell to detect magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
                pass
            'Let’s see if it reacts to my actions.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s see if it reacts to my actions.')
                if not tutorial_input:
                    $ tutorial_input = 1
                python:
                    search = renpy.input("What do you try to do? (example: talk)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                $ tutorial_input = 2
                jump giantstatuesearch01

    label giantstatueinteractingstatue02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the statue.')
        $ at_unlock_knowledge = 0
        $ at_unlock_spell = 0
        $ at = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '[giantstatue_stance_fluff]
            '
            'I try to awaken it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to awaken it.')
                if not tutorial_input:
                    $ tutorial_input = 1
                python:
                    search = renpy.input("What do you try to do? (example: talk)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                $ tutorial_input = 2
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01

label giantstatuesearch01:
    $ at_unlock_knowledge = 0
    $ at_unlock_spell = 0
    $ at = 0
    if search == "nothing" or search == "none" or search == "something" or search == "anything" or search == "whatever" or search == " " or search == "":
        menu:
            'And you do nothing.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "fuck" or search == "sex" or search == "wtf" or search == "shit" or search == "nigger" or search == "nigga" or search == "fag":
        menu:
            'Grow up.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    # real searches that do nothing
    elif search == "dance":
        menu:
            'After a few exhausting minutes you give yourself a break.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "talk" or search == "whisper" or search == "communicate" or search == "speak" or search == "talkto" or search == "say" or search == "gossip" or search == "chatter" or search == "smalltalk" or search == "orate" or search == "utter" or search == "introduce" or search == "address" or search == "address" or search == "chitchat" or search == "chat" or search == "haveachat" or search == "havechat":
        menu:
            'You introduce yourself and try to have a chat with the statue. It remains the same.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "search" or search == "inspect" or search == "examine" or search == "look" or search == "lookat" or search == "study" or search == "gaze" or search == "stare" or search == "observe" or search == "takealook" or search == "explore":
        menu:
            'You find nothing new about the statue, nor the area around it.
            \n\nThe statue’s face has no features, and the shell ends with the neck, revealing a dark space instead of a torso. You lean closer and notice the coarseness of black-and-gray gritstone, and how bitten by time it is. Both the figure and the socle are stained with white guano. Still, it’s extraordinary work - the weight of the giant doesn’t rest on its club, but rather on the boots, which are cleverly attached to the cloak.
            \n\nSooner or later, something will break, most likely the arms. Without them, the statue won’t hold its stance.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "yell" or search == "shout" or search == "yellat" or search == "scream" or search == "howl" or search == "screech" or search == "raisevoice":
        menu:
            'You let out a loud shout. The statue remains the same.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "cry" or search == "sob" or search == "weep":
        menu:
            'You let out a silent sob. The statue remains the same.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "sing" or search == "chant" or search == "hum":
        menu:
            'You hum a simple tune from the docks of {color=#f6d6bd}Hovlavan{/color}. The statue remains the same.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "pull" or search == "move" or search == "push" or search == "shake" or search == "rotate" or search == "drag" or search == "draw" or search == "carry" or search == "transfer" or search == "shift" or search == "raise":
        menu:
            'It doesn’t move.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "bow" or search == "incline" or search == "greet" or search == "curtsy" or search == "bend":
        menu:
            'It doesn’t bow back.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "kick" or search == "kickit" or search == "boot" or search == "hit" or search == "punch" or search == "blow" or search == "bash" or search == "fist" or search == "strike":
        menu:
            'It hurts you more than it does the statue.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "hug" or search == "cuddle" or search == "squeeze" or search == "touch" or search == "handle" or search == "hold" or search == "grab" or search == "pat" or search == "poke" or search == "sitonstatue" or search == "sitstatue" or search == "statuesit":
        menu:
            'The stone is cold.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "lick" or search == "kiss" or search == "bite" or search == "makeout" or search == "eat" or search == "chew" or search == "munch":
        menu:
            'The stone is cold and coarse. Not very tasty.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    # real searches that aren’t right
    elif search == "stand" or search == "standing" or search == "istand" or search == "rise" or search == "standup" or search == "getup" or search == "straightup":
        $ giantstatue_stance = "standing"
        $ giantstatue_stance_fluff = "You’re standing in front of the statue."
        menu:
            'You straighten up. The statue doesn’t look at you.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "crouching" or search == "squatting" or search == "crouch" or search == "icrouch" or search == "squat" or search == "isquat" or search == "duck":
        $ giantstatue_stance = "crouching"
        $ giantstatue_stance_fluff = "You’re crouching in front of the statue."
        menu:
            'As you crouch, you see nothing unusual about the path, nor the grass.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "liedown" or search == "lie" or search == "fall" or search == "ilie" or search == "iliedown" or search == "lieback" or search == "recline":
        $ giantstatue_stance = "lying"
        $ giantstatue_stance_fluff = "You’re lying on the ground."
        menu:
            'As you’re lying on your back, you observe the peaceful sky.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "sit" or search == "sitting" or search == "isit" or search == "sitdown" or search == "isitdown" or search == "takeaseat" or search == "itakeaseat":
        $ giantstatue_stance = "sitting"
        $ giantstatue_stance_fluff = "You’re sitting in front of the statue."
        menu:
            'You sit down. The beaten path is hard and dusty.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "blood" or search == "sacrifice" or search == "myblood" or search == "giveblood" or search == "theblood" or search == "donation" or search == "offer" or search == "offering":
        if giantstatue_blood:
            menu:
                'Last time you tried it, it didn’t make a difference.
                '
                'I do something else.':
                    python:
                        search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump giantstatuesearch01
                'I step away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                    jump giantstatueafterinteraction01
        else:
            menu:
                'You touch your skin with the edge of your knife.
                '
                'I sacrifice my blood.' ( condition="pc_hp >= 1" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sacrifice my blood.')
                    $ giantstatue_blood = 1
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                    menu:
                        'You leave a red splash on the socle, then bandage your wound and wait for a minute. Nothing seems to happen.
                        '
                        'I do something else.':
                            python:
                                search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                                search = search.strip().lower().replace(" ", "")
                                if not search:
                                    search = "nothing"
                            jump giantstatuesearch01
                        'I step away.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                            jump giantstatueafterinteraction01
                'I need to be careful. (Required vitality: 1) (disabled)' ( condition="pc_hp <= 0" ):
                    pass
                'I do something else.':
                    python:
                        search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump giantstatuesearch01
                'I step away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                    jump giantstatueafterinteraction01
    elif search == "break" or search == "destroy" or search == "shatter" or search == "smash" or search == "attack" or search == "fracture" or search == "crack" or search == "snap" or search == "fragment" or search == "splinter" or search == "damage" or search == "ruin":
        # $ giantstatue_insulted = 1
        menu:
            'You grab a rock and spend the next minute breaking off a piece of the statue’s cloak. The thing you can’t crush is the statue’s patience.
            '
            'I step away quickly.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away quickly.')
                jump giantstatueafterinteraction01
    elif search == "cut" or search == "slit" or search == "slash" or search == "pierce" or search == "gash" or search == "injure" or search == "hurt" or search == "lacerate" or search == "chop":
        menu:
            'You press a knife to the statue, then make a cut. The blade is just a little more dull.
            '
            'I step away quickly.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away quickly.')
                jump giantstatueafterinteraction01
    # real searches that give good results
    elif search == "kneel" or search == "kneeling" or search == "ikneel" or search == "falltomyknees" or search == "falltoknees" or search == "knees" or search == "getdown" or search == "genuflect" or search == "igenuflect" or search == "bendtheknee" or search == "knee" or search == "respect" or search == "honor" or search == "prone":
        $ giantstatue_kneeled = 1
        $ giantstatue_stance = "kneeling"
        if pc_religion == "theunitedchurch":
            $ giantstatue_stance_fluff = "You’re kneeling in front of the statue. It makes you feel like a traitor."
            $ custom1 = ". Priests wouldn’t be happy about this."
        elif pc_religion == "ordersoftruth":
            $ giantstatue_stance_fluff = "You’re kneeling in front of the statue. It feels sinful."
            $ custom1 = ". Monks wouldn’t be happy about this."
        elif pc_religion == "fellowship":
            $ giantstatue_stance_fluff = "You’re kneeling in front of the statue. It feels sinful."
            $ custom1 = ". Your fellowship wouldn’t be happy about this."
        elif pc_religion == "pagan":
            $ giantstatue_stance_fluff = "You’re kneeling in front of the statue. It feels right."
            $ custom1 = ", just like your ancestors would."
        else:
            $ giantstatue_stance_fluff = "You’re kneeling in front of the statue."
            $ custom1 = ", like Wright’s followers do when they enter their temples."
        menu:
            'You rest your knees on the ground to show your respect and humility[custom1]
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
    elif search == "pray" or search == "beg" or search == "plead" or search == "ipray" or search == "praying" or search == "devotion" or search == "praise" or search == "bowhead" or search == "bowdownhead":
        if giantstatue_stance == "kneeling":
            jump giantstatuepraying00
        else:
            if giantstatue_stance == "lying":
                $ custom1 = "You try to utter a simple prayer, but as you’re on your back, it feels more like a mockery."
            elif giantstatue_stance == "sitting":
                $ custom1 = "You try to utter a simple prayer, but as you’re sitting on the ground, it feels more like a chatter."
            elif giantstatue_stance == "crouching":
                $ custom1 = "You try to utter a simple prayer, but as you’re crouching, it feels as if you’re giving it advice."
            else:
                $ custom1 = "You try to utter a simple prayer, but as a minute goes by and you shift your weight from one leg to the other, you struggle to focus."
            menu:
                '[custom1]
                '
                'I do something else.':
                    python:
                        search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump giantstatuesearch01
                'I step away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                    jump giantstatueafterinteraction01
    elif search == "kneelandpray" or search == "kneelpray" or search == "ikneelandpray" or search == "prayandkneel" or search == "praykneel" or search == "iprayandkneel" or search == "prostrate":
        $ giantstatue_kneeled = 1
        $ giantstatue_stance = "kneeling"
        jump giantstatuepraying00
    else:
        menu:
            'Either you can’t do that, or I don’t understand you.
            '
            'I do something else.':
                python:
                    search = renpy.input("%s" %giantstatue_stance_fluff, default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump giantstatuesearch01
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump giantstatueafterinteraction01
