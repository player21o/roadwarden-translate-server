###################### OLD TUNNEL
default oldtunnel_firsttime = 0
default oldtunnel_inside_firsttime = 0

default oldtunnel_fluff = ""
default oldtunnel_fluff_old = ""
default oldtunnel_horsename_fluff_old = ""
default oldtunnel_horsename_fluff = ""

default oldtunnel_signpost = 0

default oldtunnel_lantern = 0
default oldtunnel_magiclight = 0
default oldtunnel_magiclight_firsttime = 0
default oldtunnel_magiclight_color = 0

label oldtunnel01:
    nvl clear
    $ pc_area = "oldtunnel"
    stop music fadeout 4.0
    play nature "audio/ambient/oldtunnelentrance01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture oldtunnel01 at basicfade behind oldtunnelbronzerod, oldtunnelsignpost
    if eudocia_bronzerod_rodin_oldtunnel:
        show oldtunnelbronzerod at basicfade
    if galerocks_iuno_about_oldtunnel_opened_day > (day+1):
        show oldtunnelsignpost at basicfade
    label oldtunnel_fluffloop:
        $ oldtunnel_fluff = renpy.random.choice(['The winds hit you at full strength. You adjust your cloak as the twisting tree branches fight for survival.', 'The gust of wind catches you by surprise, and a shiver runs down your spine. A small, creamy-brown critter jumps among the rocks, giving you worried looks.', 'The gentle wind brushes your hair. Listening to the hooves and rustling leaves makes you forget about your struggles.', 'A large shadow coming from above makes you reach for your blade, but the dragon doesn’t care about a meal as humble as you. It flies toward the sea, letting out a single roar.'])
        if oldtunnel_fluff_old == oldtunnel_fluff:
            jump oldtunnel_fluffloop
        else:
            $ oldtunnel_fluff_old = oldtunnel_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if not oldtunnel_firsttime:
        $ world_known_areas += 1
        $ oldtunnel_firsttime = 1
        $ galerocks_unlocked = 1
        $ foggylake_unlocked = 1
        jump oldtunnelfirsttime01
    if helvius_about_oldtunnel_paid and helvius_about_oldtunnel_paid < day and not oldtunnel_inside_undead_defeated_introduction:
        jump oldtunnelregular01whitemarshes
    else:
        jump oldtunnelregular01

label oldtunnelfirsttime01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if persistent.deafmode:
        $ deafcustom1 = " The distant songs of birds are the only sign that this area is not fully abandoned."
    else:
        $ deafcustom1 = ""
    $ at = 0
    $ at_unlock_spell = 0
    if oldtunnel_inside_firsttime and pc_class == "mage" and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
        $ at_unlock_spell = 1
        $ manacost = 1
    menu:
        'The road fades into an old tunnel. There are no signs of mining, no signposts, no human voices. The ceiling is supported by wooden beams, but the light only reaches so far.
        \n\nThe chilling wind mercilessly bends the few lonely trees, while the shrubs oppose the weather patiently.[deafcustom1]
        \n\nThe side path leading west is somewhat maintained, and you find both boot prints and cart tracks. It leads higher into the mountains.
        '
        'It may be the right time to take care of the corpses.' if (oldtunnel_lantern and item_lantern and oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial) or (oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial and oldtunnel_magiclight == day):
            jump oldtunnelburial01
        'I need to face the undead.' if (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_lantern and item_lantern) or (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_magiclight == day):
            jump oldtunnel_combat_lastclash_outside
        'I should leave the undead to Helvius and his people. (disabled)' if oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and helvius_about_oldtunnel_paid:
            pass
        'A simple magic trick should give me enough light. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            jump oldtunnelinsidemagiclight01
        'I grab my pearl pendant. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            jump oldtunnelinsidemagiclight02
        'I just need a bit of pneuma to make something glow... [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            pass
        'I lack pneuma to cast a spell of light. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            pass
        'I tether {color=#f6d6bd}[horsename]{/color} to the tree, then enter the tunnel.' if not oldtunnel_inside_firsttime:
            jump oldtunnelfirsttimeinside01
        'To explore the tunnel, I need a reliable source of light. (disabled)' if oldtunnel_inside_firsttime and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
            pass
        'Time to see what hides inside. I grab my lantern.' if oldtunnel_inside_firsttime and item_lantern and not oldtunnel_lantern and not oldtunnel_inside_opened:
            jump oldtunnelinsidelantern01
        'I enter the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the tunnel.')
            $ minutes += 4
            jump oldtunnel_exploration_scrap01
        'Maybe I missed something in the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I missed something in the tunnel.')
            $ minutes += 4
            jump oldtunnel_exploration_scrap01
        'I could place a bronze rod somewhere around.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_oldtunnel:
            jump oldtunnelbronzerod01
        'I take a look at the new signpost.' if galerocks_iuno_about_oldtunnel_opened_day > (day+1) and not oldtunnel_signpost:
            jump oldtunnelsignpost01
        'I’ve already explored the entire tunnel. (disabled)' if oldtunnel_inside_explored:
            pass

label oldtunnelregular01whitemarshes:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ oldtunnel_inside_undead_defeated_introduction = 1
    $ oldtunnel_inside_undead_defeated = 1
    $ oldtunnel_exploration_combat = 0
    $ at = 0
    $ at_unlock_spell = 0
    if oldtunnel_inside_firsttime and pc_class == "mage" and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
        $ at_unlock_spell = 1
        $ manacost = 1
    if not quest_closedtunnel_description03:
        $ renpy.notify("Journal updated: The Closed Tunnel")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Closed Tunnel{/i}')
        if quest_closedtunnel_description00:
            $ quest_closedtunnel_description03 = "The undead are destroyed, but I still need to open the gate."
        else:
            $ quest_closedtunnel_description03 = "The undead are destroyed, but I still need to make sure the tunnel can be crossed."
    menu:
        'You peek inside the tunnel. You spot bootprints, abandoned torches, the remains of a meal, scratches on the wall left by blades, and a small bloodstain. A few tiny bones are still behind one of the wooden beams - someone forgot to pick up a defeated skeleton’s hand.
        '
        'It may be the right time to take care of the corpses.' if (oldtunnel_lantern and item_lantern and oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial) or (oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial and oldtunnel_magiclight == day):
            jump oldtunnelburial01
        'I need to face the undead.' if (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_lantern and item_lantern) or (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_magiclight == day):
            jump oldtunnel_combat_lastclash_outside
        'I should leave the undead to Helvius and his people. (disabled)' if oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and helvius_about_oldtunnel_paid:
            pass
        'A simple magic trick should give me enough light. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            jump oldtunnelinsidemagiclight01
        'I grab my pearl pendant. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            jump oldtunnelinsidemagiclight02
        'I just need a bit of pneuma to make something glow... [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            pass
        'I lack pneuma to cast a spell of light. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            pass
        'I tether {color=#f6d6bd}[horsename]{/color} to the tree, then enter the tunnel.' if not oldtunnel_inside_firsttime:
            jump oldtunnelfirsttimeinside01
        'To explore the tunnel, I need a reliable source of light. (disabled)' if oldtunnel_inside_firsttime and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
            pass
        'Time to see what hides inside. I grab my lantern.' if oldtunnel_inside_firsttime and item_lantern and not oldtunnel_lantern and not oldtunnel_inside_opened:
            jump oldtunnelinsidelantern01
        'I enter the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the tunnel.')
            $ minutes += 4
            jump oldtunnel_exploration_scrap01
        'Maybe I missed something in the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I missed something in the tunnel.')
            $ minutes += 4
            jump oldtunnel_exploration_scrap01
        'I could place a bronze rod somewhere around.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_oldtunnel:
            jump oldtunnelbronzerod01
        'I take a look at the new signpost.' if galerocks_iuno_about_oldtunnel_opened_day > (day+1) and not oldtunnel_signpost:
            jump oldtunnelsignpost01
        'I’ve already explored the entire tunnel. (disabled)' if oldtunnel_inside_explored:
            pass

label oldtunnelregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ at = 0
    $ at_unlock_spell = 0
    if oldtunnel_inside_firsttime and pc_class == "mage" and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
        $ at_unlock_spell = 1
        $ manacost = 1
    menu:
        '[oldtunnel_fluff]
        '
        'It may be the right time to take care of the corpses.' if (oldtunnel_lantern and item_lantern and oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial) or (oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial and oldtunnel_magiclight == day):
            jump oldtunnelburial01
        'I need to face the undead.' if (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_lantern and item_lantern) or (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_magiclight == day):
            jump oldtunnel_combat_lastclash_outside
        'I should leave the undead to Helvius and his people. (disabled)' if oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and helvius_about_oldtunnel_paid:
            pass
        'A simple magic trick should give me enough light. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            jump oldtunnelinsidemagiclight01
        'I grab my pearl pendant. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            jump oldtunnelinsidemagiclight02
        'I just need a bit of pneuma to make something glow... [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            pass
        'I lack pneuma to cast a spell of light. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            pass
        'I tether {color=#f6d6bd}[horsename]{/color} to the tree, then enter the tunnel.' if not oldtunnel_inside_firsttime:
            jump oldtunnelfirsttimeinside01
        'To explore the tunnel, I need a reliable source of light. (disabled)' if oldtunnel_inside_firsttime and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
            pass
        'Time to see what hides inside. I grab my lantern.' if oldtunnel_inside_firsttime and item_lantern and not oldtunnel_lantern and not oldtunnel_inside_opened:
            jump oldtunnelinsidelantern01
        'I enter the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the tunnel.')
            $ minutes += 4
            jump oldtunnel_exploration_scrap01
        'Maybe I missed something in the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I missed something in the tunnel.')
            $ minutes += 4
            jump oldtunnel_exploration_scrap01
        'I could place a bronze rod somewhere around.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_oldtunnel:
            jump oldtunnelbronzerod01
        'I take a look at the new signpost.' if galerocks_iuno_about_oldtunnel_opened_day > (day+1) and not oldtunnel_signpost:
            jump oldtunnelsignpost01
        'I’ve already explored the entire tunnel. (disabled)' if oldtunnel_inside_explored:
            pass

label oldtunnelafterinteraction01:
    $ oldtunnel_exploration_combat = 0
    $ at_unlock_spell = 0
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ can_potions = 0
    hide screen oldtunnel
    if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelentrance01.ogg":
        play nature "audio/ambient/oldtunnelentrance01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    stop music fadeout 4.0
    $ at = 0
    $ at_unlock_spell = 0
    if oldtunnel_inside_firsttime and pc_class == "mage" and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
        $ at_unlock_spell = 1
        $ manacost = 1
    label oldtunnel_horsename_fluffloop:
        $ oldtunnel_horsename_fluff = ""
        $ oldtunnel_horsename_fluff = renpy.random.choice(['is observing the short grass with little enthusiasm.', 'is looking around, but so far no other beasts have shown up.', 'is napping in the shadow of the tree.', 'snorts from boredom, then paws the ground.', 'welcomes you with a nicker.'])
        if oldtunnel_horsename_fluff_old == oldtunnel_horsename_fluff:
            jump oldtunnel_horsename_fluffloop
        else:
            $ oldtunnel_horsename_fluff_old = oldtunnel_horsename_fluff
    show areapicture oldtunnel01 at basicfade behind oldtunnelbronzerod, oldtunnelsignpost
    if eudocia_bronzerod_rodin_oldtunnel:
        show oldtunnelbronzerod at basicfade
    if galerocks_iuno_about_oldtunnel_opened_day > (day+1):
        show oldtunnelsignpost at basicfade
    if oldtunnel_inside_opened and oldtunnel_exploration_scrap02_firsttime and oldtunnel_exploration_scrap04_firsttime and oldtunnel_exploration_scrap07_firsttime and oldtunnel_exploration_scrap09_firsttime and oldtunnel_exploration_scrap13_firsttime and oldtunnel_exploration_scrap17_firsttime and oldtunnel_exploration_scrap03_search and oldtunnel_exploration_scrap12_ironscraps and oldtunnel_exploration_scrap13_open:
        $ oldtunnel_inside_explored = 1
    menu:
        '{color=#f6d6bd}[horsename]{/color} [oldtunnel_horsename_fluff]
        '
        'It may be the right time to take care of the corpses.' if (oldtunnel_lantern and item_lantern and oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial) or (oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial and oldtunnel_magiclight == day):
            jump oldtunnelburial01
        'I need to face the undead.' if (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_lantern and item_lantern) or (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_magiclight == day):
            jump oldtunnel_combat_lastclash_outside
        'I should leave the undead to Helvius and his people. (disabled)' if oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and helvius_about_oldtunnel_paid:
            pass
        'A simple magic trick should give me enough light. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            jump oldtunnelinsidemagiclight01
        'I grab my pearl pendant. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            jump oldtunnelinsidemagiclight02
        'I just need a bit of pneuma to make something glow... [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            pass
        'I lack pneuma to cast a spell of light. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            pass
        'I tether {color=#f6d6bd}[horsename]{/color} to the tree, then enter the tunnel.' if not oldtunnel_inside_firsttime:
            jump oldtunnelfirsttimeinside01
        'To explore the tunnel, I need a reliable source of light. (disabled)' if oldtunnel_inside_firsttime and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
            pass
        'Time to see what hides inside. I grab my lantern.' if oldtunnel_inside_firsttime and item_lantern and not oldtunnel_lantern and not oldtunnel_inside_opened:
            jump oldtunnelinsidelantern01
        'I enter the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the tunnel.')
            $ minutes += 4
            jump oldtunnel_exploration_scrap01
        'Maybe I missed something in the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I missed something in the tunnel.')
            $ minutes += 4
            jump oldtunnel_exploration_scrap01
        'I could place a bronze rod somewhere around.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_oldtunnel:
            jump oldtunnelbronzerod01
        'I take a look at the new signpost.' if galerocks_iuno_about_oldtunnel_opened_day > (day+1) and not oldtunnel_signpost:
            jump oldtunnelsignpost01
        'I’ve already explored the entire tunnel. (disabled)' if oldtunnel_inside_explored:
            pass

label oldtunnelafterinteraction01_flee:
    $ oldtunnel_exploration_combat = 0
    $ at_unlock_spell = 0
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ can_potions = 0
    $ cleanliness = limit_cleanliness(cleanliness-1)
    show minus1appearance at appearancechange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
    $ pc_food = limit_pc_food(pc_food-1)
    show minus1food at foodchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
    $ at = 0
    $ at_unlock_spell = 0
    hide screen oldtunnel
    stop music fadeout 4.0
    play nature "audio/ambient/oldtunnelentrance01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if oldtunnel_inside_firsttime and pc_class == "mage" and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
        $ at_unlock_spell = 1
        $ manacost = 1
    show areapicture oldtunnel01 at basicfade behind oldtunnelbronzerod, oldtunnelsignpost
    if eudocia_bronzerod_rodin_oldtunnel:
        show oldtunnelbronzerod at basicfade
    if galerocks_iuno_about_oldtunnel_opened_day > (day+1):
        show oldtunnelsignpost at basicfade
    if oldtunnel_inside_opened and oldtunnel_exploration_scrap02_firsttime and oldtunnel_exploration_scrap04_firsttime and oldtunnel_exploration_scrap07_firsttime and oldtunnel_exploration_scrap09_firsttime and oldtunnel_exploration_scrap13_firsttime and oldtunnel_exploration_scrap17_firsttime and oldtunnel_exploration_scrap03_search and oldtunnel_exploration_scrap12_ironscraps and oldtunnel_exploration_scrap13_open:
        $ oldtunnel_inside_explored = 1
    if not quest_closedtunnel_description02:
        $ quest_closedtunnel_description02 = "The undead are going stay at the entrance. Before I face them, I should prepare myself for combat."
        $ renpy.notify("Journal updated: The Closed Tunnel")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Closed Tunnel{/i}')
    menu:
        'You run through the last, straight corridor. Midway through the skeletons’ rattle recedes. They let you be even before you reach {color=#f6d6bd}[horsename]{/color}.
        \n\nHungry and sweaty, you look back. The light stops a few minutes away from here, somewhere close to the crossroads. You won’t have a chance to sneak by them.
        '
        'It may be the right time to take care of the corpses.' if (oldtunnel_lantern and item_lantern and oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial) or (oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial and oldtunnel_magiclight == day):
            jump oldtunnelburial01
        'I need to face the undead.' if (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_lantern and item_lantern) or (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_magiclight == day):
            jump oldtunnel_combat_lastclash_outside
        'I should leave the undead to Helvius and his people. (disabled)' if oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and helvius_about_oldtunnel_paid:
            pass
        'A simple magic trick should give me enough light. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            jump oldtunnelinsidemagiclight01
        'I grab my pearl pendant. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            jump oldtunnelinsidemagiclight02
        'I just need a bit of pneuma to make something glow... [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            pass
        'I lack pneuma to cast a spell of light. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
            pass
        'I tether {color=#f6d6bd}[horsename]{/color} to the tree, then enter the tunnel.' if not oldtunnel_inside_firsttime:
            jump oldtunnelfirsttimeinside01
        'To explore the tunnel, I need a reliable source of light. (disabled)' if oldtunnel_inside_firsttime and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
            pass
        'Time to see what hides inside. I grab my lantern.' if oldtunnel_inside_firsttime and item_lantern and not oldtunnel_lantern and not oldtunnel_inside_opened:
            jump oldtunnelinsidelantern01
        'I enter the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the tunnel.')
            $ minutes += 4
            jump oldtunnel_exploration_scrap01
        'Maybe I missed something in the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I missed something in the tunnel.')
            $ minutes += 4
            jump oldtunnel_exploration_scrap01
        'I could place a bronze rod somewhere around.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_oldtunnel:
            jump oldtunnelbronzerod01
        'I take a look at the new signpost.' if galerocks_iuno_about_oldtunnel_opened_day > (day+1) and not oldtunnel_signpost:
            jump oldtunnelsignpost01
        'I’ve already explored the entire tunnel. (disabled)' if oldtunnel_inside_explored:
            pass

label oldtunnelbronzerod01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could place a bronze rod somewhere around.')
    $ minutes += 5
    $ at_unlock_spell = 0
    show oldtunnelbronzerod at basicfade
    $ renpy.notify("Journal updated: Bronze Rods")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
    $ item_bronzerod -= 1
    $ eudocia_bronzerod_rodin_oldtunnel = 1
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
        'You find the perfect spot - a small crack between two massive rocks. You use the rod to broaden it just a bit, then push it halfway in and fill the gaps with a rag.
        '
        'I dust off my hands.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dust off my hands.')
            jump oldtunnelafterinteraction01

label oldtunnelsignpost01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a look at the new signpost.')
    $ at_unlock_spell = 0
    $ oldtunnel_signpost = 1
    menu:
        'It’s nothing more than a plank covered with green paint. “Safe road,” as you understand it.
        '
        'I did a good job here.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I did a good job here.')
            jump oldtunnelafterinteraction01
        '...Definitely doesn’t sound like a trap.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...Definitely doesn’t sound like a trap.')
            jump oldtunnelafterinteraction01

label oldtunnelfirsttimeinsideALL:
    label oldtunnelfirsttimeinside01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} to the tree, then enter the tunnel.' %horsename)
        $ oldtunnel_inside_firsttime = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 1
        $ minutes += 5
        if pc_likeshorsename:
            $ custom1 = ", so you stay for a moment to give it a good scratch under its neck and say some confident-sounding rubbish"
        else:
            $ custom1 = ", so you tell it that this won’t take long"
        menu:
            'Your mount observes the area anxiously[custom1]. You unpack all the things you need to make a new, simple torch - a log, some old rugs, a bit of oil. You grab your tinderbox and sit on the ground for a couple of minutes, preparing the flint and the linen char cloth. Decades ago, before The Southern Invasion, people used fire strikers made of thick steel, but all you have is a cube-like piece of harsh pyrite. It’s not the best, but it’s enough to make a couple of sparks.
            \n\nThe loud, flickering, yellow light unevenly hits your cheek with heat. You raise the torch, but hold it at an angle, letting the oil drip on the ground.
            '
            'Let’s see where the tunnel leads.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s see where the tunnel leads.')
                play nature "audio/ambient/oldtunnelinside01.ogg" fadeout 1.0 fadein 2.0 volume 1.0
                if not renpy.get_screen("oldtunnel"):
                    show screen oldtunnel with dissolve
                $ oldtunnel_exploration_position = 20 # to make it "dark"
                $ oldtunnel_exploration_scrap00_firsttime = 1
                $ oldtunnel_exploration_scrap01_firsttime = 1
                hide areapicture
                hide oldtunnelbronzerod
                hide oldtunnelsignpost
                $ at = 0
                $ at_unlock_spell = 0
                if oldtunnel_inside_firsttime and pc_class == "mage" and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
                    $ at_unlock_spell = 1
                    $ manacost = 1
                menu:
                    'For a few minutes, you follow a fairly straight corridor. The timber supporting the ceiling is decaying, but you don’t spot any signs of collapse. The floor is littered with bones and rotting food, most likely dragged in here by wild beasts, but there are also signs of soot above you, and boot prints left on the dried mud.
                    \n\nYou reach the crossroads and stop in place. There’s no sconce in sight, so you’d have to constantly carry the torch, or lose it for good - and it won’t last for long anyway. The draft is hardly noticeable, so looking for an exit in the dark could be dangerous.
                    '
                    'A simple magic trick should give me enough light. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not oldtunnel_magiclight_firsttime" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- A simple magic trick should do the job.')
                        $ at_unlock_spell = 0
                        $ oldtunnel_magiclight_firsttime = 1
                        $ oldtunnel_magiclight = day
                        $ mana = limit_mana(mana-manacost)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                        menu:
                            'You lean the torch against the wall, letting it mark this spot, then draw both your axe and one of your oldest amulets, a pendant made of leather and a single dim pearl. The little sphere is covered by cryptic engravings, but if there’s any special meaning behind them, you’ve never been able to find out what that could be.
                            \n\nYou bite into the strap, sense the pleasant, familiar warmth, then press the blade with your open palms. After a minute of repeating the simple incantation, the pearl and your weapon start to glow...
                            '
                            'White.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- White.')
                                $ oldtunnel_magiclight_color = "white"
                                menu:
                                    'It casts a blinding blast, then remains still, evenly covering the area. You avoid looking directly at it, but it reveals every tiny detail on the walls.
                                    \n\nWithout haste, you hide the pendant back in your satchel.
                                    '
                                    'I go deeper.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                                        $ minutes += 4
                                        jump oldtunnel_exploration_scrap01
                            'Yellow.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Yellow.')
                                $ oldtunnel_magiclight_color = "yellow"
                                menu:
                                    'Just like the torch, it glimmers, but also covers your hand with an assuring warmth. The familiar smell of charcoal returns.
                                    \n\nYour lips are slightly burnt, so you hang the pendant on your belt, letting it cool down.
                                    '
                                    'I go deeper.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                                        $ minutes += 4
                                        jump oldtunnel_exploration_scrap01
                            'Red.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Red.')
                                $ oldtunnel_magiclight_color = "red"
                                menu:
                                    'It spreads around slowly, like a puddle of thick liquid. When you raise your weapon, the boundaries of light reluctantly follow.
                                    \n\nYour mouth catches an iron-like aftertaste, so you put the pendant back in your satchel.
                                    '
                                    'I go deeper.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                                        $ minutes += 4
                                        jump oldtunnel_exploration_scrap01
                            'Blue.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Blue.')
                                $ oldtunnel_magiclight_color = "blue"
                                menu:
                                    'It spreads around with the sound of breaking ice, and covers your hand and lips with a chilling aura. You hide the pendant back in your satchel.
                                    '
                                    'I go deeper.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                                        $ minutes += 4
                                        jump oldtunnel_exploration_scrap01
                            'Green.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Green.')
                                $ oldtunnel_magiclight_color = "green"
                                menu:
                                    'It’s warm and tranquil, trimmed with blues, yellows, and whites. Your axe hums like rustling leaves.
                                    \n\nYour lips catch a honey-like aftertaste, so you don’t mind holding on to the pendant for a bit before you put it back in your satchel.
                                    '
                                    'I go deeper.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                                        $ minutes += 4
                                        jump oldtunnel_exploration_scrap01
                            'Purple.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Purple.')
                                $ oldtunnel_magiclight_color = "purple"
                                menu:
                                    'It covers the walls with a pulsating, uneasy light. Its rhythm and strength keep changing, and you feel tingling in your fingers.
                                    \n\nYour lips catch a rotten aftertaste, so you surround the pendant with a cloth, then put it back in your satchel.
                                    '
                                    'I go deeper.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                                        $ minutes += 4
                                        jump oldtunnel_exploration_scrap01
                    'I just need a bit of pneuma to make something glow... [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and not oldtunnel_magiclight_firsttime" ):
                        pass
                    'To explore the tunnel, I need a reliable source of light. (disabled)' if oldtunnel_inside_firsttime and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
                        pass
                    'My lantern should last long enough.' if oldtunnel_inside_firsttime and item_lantern and not oldtunnel_lantern and not oldtunnel_inside_opened:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to see what hides inside. I grab my lantern.')
                        $ at_unlock_spell = 0
                        $ oldtunnel_lantern = 1
                        menu:
                            'You place a candle on the ground, then light it up with another few sparks from your tinderbox. You shove it inside the lantern through the hole in its top, pressing it onto a nail. You shake it for a bit, making sure it will stay standing.
                            \n\nThe candle isn’t as bright as your torch, but it’s safer, will last longer, and can easily be replaced by another one.
                            '
                            'I go deeper.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                                $ minutes += 4
                                jump oldtunnel_exploration_scrap01
                    'I go outside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                        play nature "audio/ambient/oldtunnelentrance01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                        jump oldtunnelafterinteraction01

    label oldtunnelinsidemagiclight01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- A simple magic trick should do the job.')
        $ at_unlock_spell = 0
        $ oldtunnel_magiclight_firsttime = 1
        $ oldtunnel_magiclight = day
        $ mana = limit_mana(mana-manacost)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
        menu:
            'You draw both your axe and one of your oldest amulets, a pendant made of leather and a single dim pearl. The little sphere is covered by cryptic engravings, but if there’s any special meaning behind them, you’ve never been able to find out what that could be.
            \n\nYou bite into the strap, sense the pleasant, familiar warmth, then press the blade with your open palms. After a minute of repeating the simple incantation, the pearl and your weapon start to glow...
            '
            'White.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- White.')
                $ oldtunnel_magiclight_color = "white"
                menu:
                    'It casts a blinding blast, then remains still, evenly covering the area. You avoid looking directly at it, but it reveals every tiny detail on the walls.
                    \n\nWithout haste, you hide the pendant back in your satchel.
                    '
                    'I go deeper.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                        $ minutes += 4
                        jump oldtunnel_exploration_scrap01
            'Yellow.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Yellow.')
                $ oldtunnel_magiclight_color = "yellow"
                menu:
                    'Just like the torch, it glimmers, but also covers your hand with an assuring warmth. The familiar smell of charcoal returns.
                    \n\nYour lips are slightly burnt, so you hang the pendant on your belt, letting it cool down.
                    '
                    'I go deeper.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                        $ minutes += 4
                        jump oldtunnel_exploration_scrap01
            'Red.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Red.')
                $ oldtunnel_magiclight_color = "red"
                menu:
                    'It spreads around slowly, like a puddle of thick liquid. When you raise your weapon, the boundaries of light reluctantly follow.
                    \n\nYour mouth catches an iron-like aftertaste, so you put the pendant back in your satchel.
                    '
                    'I go deeper.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                        $ minutes += 4
                        jump oldtunnel_exploration_scrap01
            'Blue.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Blue.')
                $ oldtunnel_magiclight_color = "blue"
                menu:
                    'It spreads around with the sound of breaking ice, and covers your hand and lips with a chilling aura. You hide the pendant back in your satchel.
                    '
                    'I go deeper.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                        $ minutes += 4
                        jump oldtunnel_exploration_scrap01
            'Green.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Green.')
                $ oldtunnel_magiclight_color = "green"
                menu:
                    'It’s warm and tranquil, trimmed with blues, yellows, and whites. Your axe hums like rustling leaves.
                    \n\nYour lips catch a honey-like aftertaste, so you don’t mind holding on to the pendant for a bit before you put it back in your satchel.
                    '
                    'I go deeper.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                        $ minutes += 4
                        jump oldtunnel_exploration_scrap01
            'Purple.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Purple.')
                $ oldtunnel_magiclight_color = "purple"
                menu:
                    'It covers the walls with a pulsating, uneasy light. Its rhythm and strength keep changing, and you feel tingling in your fingers.
                    \n\nYour lips catch a rotten aftertaste, so you surround the pendant with a cloth, then put it back in your satchel.
                    '
                    'I go deeper.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go deeper.')
                        $ minutes += 4
                        jump oldtunnel_exploration_scrap01
    label oldtunnelinsidemagiclight02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my pearl pendant.')
        $ at_unlock_spell = 0
        $ oldtunnel_magiclight = day
        $ mana = limit_mana(mana-manacost)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
        if oldtunnel_magiclight_color == "white":
            $ custom1 = ", covering the walls with a blinding white blast. The light remains still, evenly covering the area.\n\nWithout haste, you hide the pendant back in your satchel."
        elif oldtunnel_magiclight_color == "yellow":
            $ custom1 = ", covering the walls with the yellowish light, just like a torch. It glimmers, but also covers your hand with an assuring warmth. The familiar smell of charcoal returns.\n\nYour lips are slightly burnt, so you hang the pendant on your belt, letting it cool down."
        elif oldtunnel_magiclight_color == "red":
            $ custom1 = ", covering the walls with the red light slowly, spreading like a puddle of thick liquid. When you raise your weapon, the boundaries of the glow reluctantly follow.\n\nYour mouth catches an iron-like aftertaste, so you put the pendant back in your satchel."
        elif oldtunnel_magiclight_color == "blue":
            $ custom1 = ", making a sound of a breaking ice and covering the walls with a blue light. Your hand and lips are surrounded by a chilling aura. You hide the pendant back in your satchel."
        elif oldtunnel_magiclight_color == "green":
            $ custom1 = ", covering the walls with the green light, warm and tranquil, trimmed with blues, yellows, and whites. Your axe hums like rustling leaves, and your lips catch a honey-like aftertaste, so you don’t mind holding on to the pendant for a bit before you put it back in your satchel."
        elif oldtunnel_magiclight_color == "purple":
            $ custom1 = ", covering the walls with a pulsating, uneasy purple light. Its rhythm and strength keep changing, and you feel tingling in your fingers.\n\nYour lips catch a rotten aftertaste, so you surround the pendant with a cloth, then put it back in your satchel."
        menu:
            'You bite into the strap, sense the pleasant, familiar warmth, then press the blade with your open palms. After a minute of repeating the simple incantation, the pearl and your weapon start to glow[custom1]
            '
            'It may be the right time to take care of the corpses.' if (oldtunnel_lantern and item_lantern and oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial) or (oldtunnel_inside_undead_defeated_bypc and not oldtunnel_inside_undead_defeated_burial and oldtunnel_magiclight == day):
                jump oldtunnelburial01
            'I need to face the undead.' if (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_lantern and item_lantern) or (oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not helvius_about_oldtunnel_paid and oldtunnel_magiclight == day):
                jump oldtunnel_combat_lastclash_outside
            'I should leave the undead to Helvius and his people. (disabled)' if oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and helvius_about_oldtunnel_paid:
                pass
            'A simple magic trick should give me enough light. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
                jump oldtunnelinsidemagiclight01
            'I grab my pearl pendant. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
                jump oldtunnelinsidemagiclight02
            'I just need a bit of pneuma to make something glow... [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and not oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
                pass
            'I lack pneuma to cast a spell of light. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and at_unlock_spell and manacost > mana and oldtunnel_magiclight_firsttime and oldtunnel_magiclight != day" ):
                pass
            'I tether {color=#f6d6bd}[horsename]{/color} to the tree, then enter the tunnel.' if not oldtunnel_inside_firsttime:
                jump oldtunnelfirsttimeinside01
            'To explore the tunnel, I need a reliable source of light. (disabled)' if oldtunnel_inside_firsttime and not item_lantern and oldtunnel_magiclight != day and not oldtunnel_inside_explored:
                pass
            'Time to see what hides inside. I grab my lantern.' if oldtunnel_inside_firsttime and item_lantern and not oldtunnel_lantern and not oldtunnel_inside_opened:
                jump oldtunnelinsidelantern01
            'I enter the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and not oldtunnel_inside_opened and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the tunnel.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap01
            'Maybe I missed something in the tunnel.' if (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and item_lantern and oldtunnel_lantern and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and not oldtunnel_inside_undead_pursuit) or (oldtunnel_inside_firsttime and oldtunnel_magiclight == day and oldtunnel_magiclight_firsttime and oldtunnel_inside_opened and not oldtunnel_inside_explored and oldtunnel_inside_undead_pursuit and oldtunnel_inside_undead_defeated):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I missed something in the tunnel.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap01
            'I could place a bronze rod somewhere around.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_oldtunnel:
                jump oldtunnelbronzerod01
            'I take a look at the new signpost.' if galerocks_iuno_about_oldtunnel_opened_day > (day+1) and not oldtunnel_signpost:
                jump oldtunnelsignpost01
            'I’ve already explored the entire tunnel. (disabled)' if oldtunnel_inside_explored:
                pass

    label oldtunnelinsidelantern01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to see what hides inside. I grab my lantern.')
        $ at_unlock_spell = 0
        $ oldtunnel_lantern = 1
        menu:
            'You place a candle on the ground, then light it up with a few sparks from your tinderbox. You shove it inside the lantern through the hole in its top, pressing it onto a nail. You shake it for a bit, making sure it will stay standing.
            \n\nThe candle isn’t as bright as your torch, but it’s safer, will last longer, and can easily be replaced by another one.
            '
            'I enter the tunnel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the tunnel.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap01

label oldtunnelburial01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It may be the right time to take care of the corpses.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ can_potions = 0
    menu:
        'Picking up the bones won’t take you much time, but the funeral traditions are rather demanding. You’d need to chop and gather enough wood to form a big pile somewhere down the hill.
        \n\nOf course, the {i}orthodox{/i} approach is not the only one possible.
        '
        'Whoever those creatures used to be, they deserve proper parting rites. It may take me three hours or so, but I’ll let them rest on a pyre.' if quarters <= (world_daylength-11):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Whoever those creatures used to be, they deserve proper parting rites. It may take me three hours or so, but I’ll let them rest on a pyre.')
            $ oldtunnel_inside_undead_defeated_burial = "burnt"
            $ achievement_pyrepoints += 2
            $ quarters += 12
            if pc_religion == "theunitedchurch":
                $ pc_faithpoints += 3
            elif pc_religion == "ordersoftruth":
                $ pc_faithpoints += 2
            elif pc_religion == "fellowship":
                $ pc_faithpoints += 2
            elif pc_religion == "pagan":
                $ pc_faithpoints += 2
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            menu:
                'After spending a few more minutes in the darkness you bring the three sacks filled with human remains to a small, regrowing clearing. You put on gloves, prepare some tools, and collect wood from the thicket and the tunnel, crudely splitting branches and logs.
                \n\nCovered with sweat, soil, and the scent of smoke, you observe the head-high flames. The bones are sticking out of the wood like hedgehog’s quills, and crack from the heat loudly.
                '
                'I should wash my hands.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should wash my hands.')
                    jump oldtunnelafterinteraction01
        'It would take me three hours to prepare a decent pyre for these shells. (disabled)' if quarters >= (world_daylength-11):
            pass
        'I’ll spend an hour and a half breaking and crushing the bones, then spread them around.' if quarters <= (world_daylength-5):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll spend an hour and a half breaking and crushing the bones, then spread them around.')
            $ oldtunnel_inside_undead_defeated_burial = "smashed"
            $ achievement_pyrepoints += 1
            $ quarters += 4
            if pc_religion == "theunitedchurch":
                $ pc_faithpoints -= 1
            elif pc_religion == "ordersoftruth":
                $ pc_faithpoints -= 0
            elif pc_religion == "fellowship":
                $ pc_faithpoints -= 0
            elif pc_religion == "pagan":
                $ pc_faithpoints += 1
            $ cleanliness = limit_cleanliness(cleanliness-1)
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            menu:
                'After spending a few more minutes in the darkness you take three sacks filled with human remains to a large, flat boulder, then start to hit them - either with the blunt side of your axe, or the conveniently shaped rocks. The skulls and hips take especially long, and as the long minutes go by, the area becomes surrounded by the white and yellow dust and chunks of bone, as well as teeth.
                \n\nThe longer it takes, the more numb you become. When you step away, you’re still sweating.
                '
                'Good thing I have my gloves.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Good thing I have my gloves.')
                    jump oldtunnelafterinteraction01
        'I’d need an hour and a half to crush the loose bones. (disabled)' if quarters >= (world_daylength-5):
            pass
        'In half an hour I’ll pick up all the bones and throw them around the hills. Let the wolves and deer do the work.' if quarters <= (world_daylength-1):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- In half an hour I’ll pick up all the bones and throw them around the hills. Let the wolves and deer do the work.')
            $ oldtunnel_inside_undead_defeated_burial = "spread"
            $ quarters += 2
            if pc_religion == "theunitedchurch":
                $ pc_faithpoints -= 2
            elif pc_religion == "ordersoftruth":
                $ pc_faithpoints -= 1
            elif pc_religion == "fellowship":
                $ pc_faithpoints -= 1
            elif pc_religion == "pagan":
                $ pc_faithpoints += 1
            menu:
                'After spending a few more minutes in the darkness, you step outside of the beaten path with three sacks filled with human remains. You throw their contents at the bushes, into the tall grasses, down the crags, into the pond.
                \n\nIt may not be too elegant, but nothing stops you.
                '
                'I just don’t have time to follow the tradition right now.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just don’t have time to follow the tradition right now.')
                    jump oldtunnelafterinteraction01
                'I wonder why anyone bothers with burning human remains.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder why anyone bothers with burning human remains.')
                    if pc_religion == "theunitedchurch":
                        $ pc_faithpoints -= 2
                    jump oldtunnelafterinteraction01
        'I’ll get back to it later.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll get back to it later.')
            jump oldtunnelafterinteraction01
