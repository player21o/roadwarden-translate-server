# Exploration

default oldtunnel_inside_opened = 0
default oldtunnel_inside_explored = 0
default oldtunnel_inside_undead_seen = 0
default oldtunnel_inside_undead_pursuit = 0
default oldtunnel_inside_undead_defeated = 0
default oldtunnel_inside_undead_defeated_bypc = 0
default oldtunnel_inside_undead_defeated_burial = 0 # left, burnt, spread, smashed
default oldtunnel_inside_undead_defeated_introduction = 0

default oldtunnel_inside_undead_amount = 4
default oldtunnel_inside_undead_amount_0_description = 0
default oldtunnel_inside_undead_hp = 20
default oldtunnel_inside_undead_hp_old = 0

default oldtunnel_exploration_position = 0
default oldtunnel_exploration_combat = 0

default oldtunnel_exploration_crossbow_ready = 0
default oldtunnel_exploration_knowledge = 0
default oldtunnel_exploration_wood = 0
default oldtunnel_exploration_bones = 0
default oldtunnel_exploration_tools = 0
default oldtunnel_exploration_net = 0

default oldtunnel_exploration_trap_availability_deadfall = 2
default oldtunnel_exploration_trap_availability_whip = 2
default oldtunnel_exploration_trap_availability_foothold = 2
default oldtunnel_exploration_trap_availability_net = 1
# inne pułapki - sznurek w poprzek? coź z hakiem? belka spadająca z sufitu? stara sieć?

default oldtunnel_exploration_scrap00_firsttime = 0
default oldtunnel_exploration_scrap01_firsttime = 0
default oldtunnel_exploration_scrap01_search = 0
default oldtunnel_exploration_scrap01_trap = 0

default oldtunnel_exploration_scrap02_firsttime = 0
default oldtunnel_exploration_scrap02_search = 0
default oldtunnel_exploration_scrap02_trap = 0

default oldtunnel_exploration_scrap03_firsttime = 0
default oldtunnel_exploration_scrap03_search = 0
default oldtunnel_exploration_scrap03_trap = 0

default oldtunnel_exploration_scrap04_firsttime = 0
default oldtunnel_exploration_scrap04_search = 0

default oldtunnel_exploration_scrap05_firsttime = 0
default oldtunnel_exploration_scrap05_search = 0
default oldtunnel_exploration_scrap05_trap = 0

default oldtunnel_exploration_scrap06_firsttime = 0
default oldtunnel_exploration_scrap06_search = 0
default oldtunnel_exploration_scrap06_trap = 0
default oldtunnel_exploration_scrap07_firsttime = 0

default oldtunnel_exploration_scrap08_firsttime = 0
default oldtunnel_exploration_scrap08_search = 0
default oldtunnel_exploration_scrap08_trap = 0
default oldtunnel_exploration_scrap09_firsttime = 0

default oldtunnel_exploration_scrap10_firsttime = 0
default oldtunnel_exploration_scrap10_trap = 0

default oldtunnel_exploration_scrap11_firsttime = 0
default oldtunnel_exploration_scrap11_search = 0
default oldtunnel_exploration_scrap11_trap = 0
default oldtunnel_exploration_scrap11_time = 0

default oldtunnel_exploration_scrap12_firsttime = 0
default oldtunnel_exploration_scrap12_ironscraps = 0

default oldtunnel_exploration_scrap13_firsttime = 0
default oldtunnel_exploration_scrap13_search = 0
default oldtunnel_exploration_scrap13_open = 0

default oldtunnel_exploration_scrap14_firsttime = 0
default oldtunnel_exploration_scrap14_search = 0
default oldtunnel_exploration_scrap14_trap = 0

default oldtunnel_exploration_scrap15_firsttime = 0
default oldtunnel_exploration_scrap15_hidelight = 0
default oldtunnel_exploration_scrap15_trap = 0

default oldtunnel_exploration_scrap16_firsttime = 0
default oldtunnel_exploration_scrap16_search = 0

default oldtunnel_exploration_scrap17_firsttime = 0
default oldtunnel_exploration_scrap17_search = 0

default oldtunnel_exploration_scrap18_firsttime = 0
default oldtunnel_exploration_scrap18_dismantled = 0
default oldtunnel_exploration_scrap18_trap = 0

default oldtunnel_exploration_scrap19_firsttime = 0
default oldtunnel_exploration_scrap19_search = 0
default oldtunnel_exploration_scrap19_trygate = 0

label oldtunnel_exploration_scrap01ALL:
    label oldtunnel_exploration_scrap01: # skrzyżowanie
        if not renpy.get_screen("oldtunnel"):
            show screen oldtunnel with dissolve
        $ oldtunnel_exploration_position = 1
        $ at_unlock_spell = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 1
        $ can_potions = 1
        hide areapicture
        hide oldtunnelbronzerod
        hide oldtunnelsignpost
        if not oldtunnel_exploration_combat:
            if not oldtunnel_exploration_scrap01_firsttime == 2:
                $ oldtunnel_exploration_scrap01_firsttime = 2
                $ custom1 = "The road ahead is like the one you just crossed - a human-carved, straight corridor supported with beams - while the other paths are curved and narrow. The only light comes from the exit, minutes away from here."
                if persistent.deafmode:
                    $ deafcustom1 = " The winds also stay away, giving way to the falling droplets and a distant stream. You hear no roaring or gnawing."
                else:
                    $ deafcustom1 = ""
                $ custom2 = ""
            else:
                $ custom1 = "You feel the gentle movement of humid air."
                $ deafcustom1 = ""
            if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside01.ogg":
                play nature "audio/ambient/oldtunnelinside01.ogg" fadeout 2.0 fadein 2.0 volume 1.0
            menu:
                '[custom1][deafcustom1]
                '
                'I look around.' if not oldtunnel_exploration_scrap01_search:
                    jump oldtunnel_exploration_scrap01_search
                'I turn left.' if not oldtunnel_exploration_scrap02_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn left.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap02
                'I turn right.' if not oldtunnel_exploration_scrap03_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn right.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap03
                'I move forward.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                    $ minutes += 4
                    jump oldtunnel_exploration_scrap05
                'I go back to the sleeping chamber.' if oldtunnel_exploration_scrap02_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the sleeping chamber.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap02
                'I go back to the animal pen.' if oldtunnel_exploration_scrap03_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the animal pen.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap03
                'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                    if oldtunnel_exploration_scrap19_firsttime:
                        $ minutes += 30
                        jump oldtunnel_exploration_scrap19
                    if oldtunnel_exploration_scrap15_firsttime:
                        $ minutes += 23
                        jump oldtunnel_exploration_scrap15
                    if oldtunnel_exploration_scrap14_firsttime:
                        $ minutes += 21
                        jump oldtunnel_exploration_scrap14
                    if oldtunnel_exploration_scrap11_firsttime:
                        $ minutes += 16
                        jump oldtunnel_exploration_scrap11
                    if oldtunnel_exploration_scrap08_firsttime:
                        $ minutes += 13
                        jump oldtunnel_exploration_scrap08
                'I exit the tunnel.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I exit the tunnel.')
                    play nature "audio/ambient/oldtunnelentrance01.ogg" fadeout 2.0 fadein 4.0 volume 1.0
                    $ minutes += 4
                    jump oldtunnelafterinteraction01
        else:
            menu:
                'You don’t have much time. You can either leave the tunnel or enter a side corridor. If the choose the latter, you won’t have the option to turn back.
                '
                'I run to the sleeping chamber.' if oldtunnel_exploration_scrap02_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to the sleeping chamber.')
                    $ minutes += 1
                    jump oldtunnel_exploration_scrap02
                'I run to the animal pen.' if oldtunnel_exploration_scrap03_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to the animal pen.')
                    $ minutes += 1
                    jump oldtunnel_exploration_scrap03
                '{image=d6} It’s my last chance to use a spell.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                    jump oldtunnel_combat_spell
                '{image=d6} It’s my last chance to shoot the crossbow.' if oldtunnel_exploration_crossbow_ready:
                    jump oldtunnel_combat_crossbow
                '{image=d6} I’m ready to face the undead.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                    jump oldtunnel_combat_lastclash
                'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                    pass
                'I flee.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I flee.')
                    stop music fadeout 4.0
                    play nature "audio/ambient/oldtunnelentrance01.ogg" fadeout 2.0 fadein 4.0 volume 1.0
                    $ minutes += 2
                    jump oldtunnelafterinteraction01_flee

    label oldtunnel_exploration_scrap01_search:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around.')
        $ oldtunnel_exploration_scrap01_search = 1
        $ minutes += 5
        menu:
            'The remains of prey and fruit are rotting, but get sparser the deeper you enter the tunnel. The moist walls are shining, as if they’re made of an ore unknown to human tribes. You observe the dried trails. The ones left by boots lead toward both corridors. The path to your right also has marks left by hooves and wheels.
            \n\nSome of the fresher trails, leading deeper into the tunnel, resemble human soles, but deformed, lacking skin between their toes.
            '
            'I look around.' if not oldtunnel_exploration_scrap01_search:
                jump oldtunnel_exploration_scrap01_search
            'I turn left.' if not oldtunnel_exploration_scrap02_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn left.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap02
            'I turn right.' if not oldtunnel_exploration_scrap03_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn right.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap03
            'I move forward.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap05
            'I go back to the sleeping chamber.' if oldtunnel_exploration_scrap02_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the sleeping chamber.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap02
            'I go back to the animal pen.' if oldtunnel_exploration_scrap03_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the animal pen.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap03
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 30
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 23
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 21
                    jump oldtunnel_exploration_scrap14
                if oldtunnel_exploration_scrap11_firsttime:
                    $ minutes += 16
                    jump oldtunnel_exploration_scrap11
                if oldtunnel_exploration_scrap08_firsttime:
                    $ minutes += 13
                    jump oldtunnel_exploration_scrap08
            'I exit the tunnel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I exit the tunnel.')
                play nature "audio/ambient/oldtunnelentrance01.ogg" fadeout 2.0 fadein 4.0 volume 1.0
                $ minutes += 4
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap01_midcombat_afterinteraction:
        menu:
            '[custom1][custom2]
            '
            'I run to the sleeping chamber.' if oldtunnel_exploration_scrap02_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to the sleeping chamber.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap02
            'I run to the animal pen.' if oldtunnel_exploration_scrap03_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to the animal pen.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap03
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I flee.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I flee.')
                stop music fadeout 4.0
                play nature "audio/ambient/oldtunnelentrance01.ogg" fadeout 2.0 fadein 4.0 volume 1.0
                $ minutes += 2
                jump oldtunnelafterinteraction01_flee

    label oldtunnel_exploration_scrap01_midcombat_nothing:
        menu:
            'The undead are getting closer.
            '
            'I run to the sleeping chamber.' if oldtunnel_exploration_scrap02_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to the sleeping chamber.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap02
            'I run to the animal pen.' if oldtunnel_exploration_scrap03_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to the animal pen.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap03
            '{image=d6} It’s my last chance to use a spell.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} It’s my last chance to shoot the crossbow.' if oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'I flee.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I flee.')
                stop music fadeout 4.0
                play nature "audio/ambient/oldtunnelentrance01.ogg" fadeout 2.0 fadein 4.0 volume 1.0
                $ minutes += 2
                jump oldtunnelafterinteraction01_flee

label oldtunnel_exploration_scrap02ALL:
    label oldtunnel_exploration_scrap02: # sypialnia
        $ oldtunnel_exploration_position = 2
        if not oldtunnel_exploration_combat:
            if not oldtunnel_exploration_scrap02_firsttime:
                $ oldtunnel_exploration_scrap02_firsttime = 1
                $ custom1 = "The air in the chamber is humid. The straw beds are covered with mold, the sagging racks are bending under their own weight, and the animal pelts on the floor release a terrible stench."
                $ custom2 = ""
            else:
                $ custom1 = "The water drips from the furniture loudly."
                if oldtunnel_exploration_scrap02_trap and not oldtunnel_inside_undead_defeated:
                    $ custom2 = " Your deadfall trap is still here."
                else:
                    $ custom2 = ""
            if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside02.ogg":
                play nature "audio/ambient/oldtunnelinside02.ogg" fadeout 2.0 fadein 2.0 volume 1.0
            menu:
                '[custom1][custom2]
                '
                'I search the room quickly.' if not oldtunnel_exploration_scrap02_search:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the room quickly.')
                    $ cleanliness = limit_cleanliness(cleanliness-1)
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                    $ custom1 = "You look under the furs and mattresses, letting out a cough after a cloud of spores and wet dust hits your face. Your gloves get sticky from touching all the odds and ends."
                    $ minutes += 5
                    jump oldtunnel_exploration_scrap02_search
                'I search the room carefully.' if not oldtunnel_exploration_scrap02_search:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the room carefully.')
                    $ custom1 = "Using an old walking stick you push the furs and mattresses aside, and you spare your gloves from touching the sticky odds and ends by wrapping them with a cloth."
                    $ minutes += 20
                    jump oldtunnel_exploration_scrap02_search
                'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap02_trap:
                    jump oldtunnel_exploration_scrap02_trap
                'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap02_trap:
                    pass
                'I leave the chamber.' if oldtunnel_exploration_scrap01_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap01
                'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                    if oldtunnel_exploration_scrap19_firsttime:
                        $ minutes += 32
                        jump oldtunnel_exploration_scrap19
                    if oldtunnel_exploration_scrap15_firsttime:
                        $ minutes += 25
                        jump oldtunnel_exploration_scrap15
                    if oldtunnel_exploration_scrap14_firsttime:
                        $ minutes += 23
                        jump oldtunnel_exploration_scrap14
                    if oldtunnel_exploration_scrap11_firsttime:
                        $ minutes += 18
                        jump oldtunnel_exploration_scrap11
                    if oldtunnel_exploration_scrap08_firsttime:
                        $ minutes += 15
                        jump oldtunnel_exploration_scrap08
                'I go back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                    $ minutes += 6
                    jump oldtunnelafterinteraction01
        else:
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            if oldtunnel_exploration_scrap02_trap == "deadfall":
                $ custom1 = "You pull the cord and drop the beams and rocks on an undead skull, though the wet timber causes little more than a stagger. "
                $ oldtunnel_inside_undead_hp -= 1
            else:
                $ custom1 = ""
            if oldtunnel_inside_undead_hp_old != oldtunnel_inside_undead_hp:
                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                    $ oldtunnel_inside_undead_amount = 3
                    $ custom2 = "It turns out to be enough - the loose bones of the first undead scatter over the floor.\n\n"
                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                    $ oldtunnel_inside_undead_amount = 2
                    $ custom2 = "It turns out to be enough - the skull of the second undead cracks, and it falls on the floor silently.\n\n"
                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                    $ oldtunnel_inside_undead_amount = 1
                    $ custom2 = "It turns out to be enough - the third undead lets out a quiet moan as it crumbles. There’s only one creature left.\n\n"
                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                    $ oldtunnel_inside_undead_amount_0_description = 1
                    $ custom2 = "It’s almost enough - the last undead shuffles forward, giving you an empty, yet somehow hungry look.\n\n"
                else:
                    $ custom2 = ""
            else:
                $ custom2 = ""
            menu:
                '[custom1][custom2]You’ve nowhere else to go.
                '
                '{image=d6} I face the undead.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I face the undead.')
                    jump oldtunnel_combat_lastclash

    label oldtunnel_exploration_scrap02_search:
        $ oldtunnel_exploration_scrap02_search = 1
        $ item_bonering = 1
        $ renpy.notify("You found a bone ring.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a bone ring.{/i}')
        menu:
            '[custom1] You find only one thing of value, hidden in a rare, dry bowl pushed to the side of a shelf - a tiny ring made of a bone. Not a coin, but a piece of jewelry: still elegant, with a distinguished carving of a fish on its top and scales on its side.
            '
            'I search the room quickly.' if not oldtunnel_exploration_scrap02_search:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the room quickly.')
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom1 = "You look under the furs and mattresses, letting out a cough after a cloud of spores and wet dust hits your face. Your gloves get sticky from touching all the odds and ends."
                $ minutes += 5
                jump oldtunnel_exploration_scrap02_search
            'I search the room carefully.' if not oldtunnel_exploration_scrap02_search:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the room carefully.')
                $ custom1 = "Using an old walking stick you push the furs and mattresses aside, and you spare your gloves from touching the sticky odds and ends by wrapping them with a cloth."
                $ minutes += 20
                jump oldtunnel_exploration_scrap02_search
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap02_trap:
                jump oldtunnel_exploration_scrap02_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap02_trap:
                pass
            'I leave the chamber.' if oldtunnel_exploration_scrap01_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap01
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 32
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 25
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 23
                    jump oldtunnel_exploration_scrap14
                if oldtunnel_exploration_scrap11_firsttime:
                    $ minutes += 18
                    jump oldtunnel_exploration_scrap11
                if oldtunnel_exploration_scrap08_firsttime:
                    $ minutes += 15
                    jump oldtunnel_exploration_scrap08
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 6
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap02_trap:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider putting a trap here.')
        menu:
            'You look around.
            '
            'I lack the knowledge to build complex traps. (disabled)' if not oldtunnel_exploration_knowledge:
                pass
            'I could crush the monsters with a deadfall trap.' if oldtunnel_exploration_knowledge and oldtunnel_exploration_trap_availability_deadfall and oldtunnel_exploration_wood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could crush the monsters with a deadfall trap.')
                if oldtunnel_exploration_tools:
                    $ custom1 = "Even with the tools you found, it will take you more than an hour."
                else:
                    $ custom1 = "Since you lack proper tools, it may take you up to two hours, and will be quite tiresome."
                if oldtunnel_exploration_trap_availability_deadfall == 2:
                    $ custom2 = "You have enough supplies to build 2 deadfall traps in the entire tunnel."
                else:
                    $ custom2 = "You have enough supplies to build 1 more deadfall trap in the entire tunnel."
                menu: # ropehook
                    'You could hang the load right next to the entrance with the help of the soggy rack and make it collapse with a pull of the rope. You can’t be sure if such moist wood will be effective at hurting anything.
                    \n\n[custom1]
                    \n\n[custom2]
                    '
                    'Let’s get to it.' ( condition="pc_hp >= 2" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        $ oldtunnel_exploration_scrap02_trap = "deadfall"
                        $ oldtunnel_exploration_trap_availability_deadfall -= 1
                        if oldtunnel_exploration_tools:
                            $ cleanliness = limit_cleanliness(cleanliness-1)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ quarters += 4
                        else:
                            $ quarters += 7
                            $ pc_food = limit_pc_food(pc_food-1)
                            show minus1food at foodchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
                            $ cleanliness = limit_cleanliness(cleanliness-2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                            show minus2appearance at appearancechange onlayer myoverlay
                        $ custom1 = "You put the triggering cord away from your usual path to avoid stumbling over it."
                        jump oldtunnel_exploration_scrap02_trap2
                    'I’m too tired to safely build a trap. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 2" ):
                        pass
                    'Forget it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                        $ custom1 = "You feel the gentle movement of humid air."
                        jump oldtunnel_exploration_scrap02_trap2
            'Unless I find some decent wood around here I won’t be able to build anything. (disabled)' if oldtunnel_exploration_trap_availability_deadfall and oldtunnel_exploration_knowledge and not oldtunnel_exploration_wood:
                pass
            'I won’t find enough supplies to build another deadfall trap. (disabled)' if not oldtunnel_exploration_trap_availability_deadfall:
                pass
            'Forget it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                $ custom1 = "You feel the gentle movement of humid air."
                jump oldtunnel_exploration_scrap02_trap2

    label oldtunnel_exploration_scrap02_trap2:
        menu:
            '[custom1]
            '
            'I search the room quickly.' if not oldtunnel_exploration_scrap02_search:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the room quickly.')
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom1 = "You look under the furs and mattresses, letting out a cough after a cloud of spores and wet dust hits your face. Your gloves get sticky from touching all the odds and ends."
                $ minutes += 5
                jump oldtunnel_exploration_scrap02_search
            'I search the room carefully.' if not oldtunnel_exploration_scrap02_search:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the room carefully.')
                $ custom1 = "Using an old walking stick you push the furs and mattresses aside, and you spare your gloves from touching the sticky odds and ends by wrapping them with a cloth."
                $ minutes += 20
                jump oldtunnel_exploration_scrap02_search
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap02_trap:
                jump oldtunnel_exploration_scrap02_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap02_trap:
                pass
            'I leave the chamber.' if oldtunnel_exploration_scrap01_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap01
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 32
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 25
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 23
                    jump oldtunnel_exploration_scrap14
                if oldtunnel_exploration_scrap11_firsttime:
                    $ minutes += 18
                    jump oldtunnel_exploration_scrap11
                if oldtunnel_exploration_scrap08_firsttime:
                    $ minutes += 15
                    jump oldtunnel_exploration_scrap08
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 6
                jump oldtunnelafterinteraction01

label oldtunnel_exploration_scrap03ALL:
    label oldtunnel_exploration_scrap03: # zagrody
        $ oldtunnel_exploration_position = 3
        if not oldtunnel_exploration_combat:
            if not oldtunnel_exploration_scrap03_firsttime:
                $ oldtunnel_exploration_scrap03_firsttime = 1
                $ custom1 = "The corridor is unlike the others, taller and more rounded, with claw marks on the walls. It leads you to a chamber with a ceiling supported by a single beam. There’s also an abandoned cart, the fence of an animal pen, and a few long sticks and planks.\n\nYou take a glance at the new exit - it leads slightly upward, and looks a bit like stairs."
                $ custom2 = ""
            else:
                $ custom1 = "The air here is stiff."
                if oldtunnel_exploration_scrap03_trap and not oldtunnel_inside_undead_defeated:
                    $ custom2 = " Your whip trap is still here."
                else:
                    $ custom2 = ""
            if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside02.ogg":
                play nature "audio/ambient/oldtunnelinside02.ogg" fadeout 2.0 fadein 2.0 volume 1.0
            menu:
                '[custom1][custom2]
                '
                'I search the room.' if not oldtunnel_exploration_scrap03_search:
                    jump oldtunnel_exploration_scrap03_search
                'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap03_search and not oldtunnel_exploration_scrap03_trap:
                    jump oldtunnel_exploration_scrap03_trap
                'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap03_trap:
                    pass
                'I climb up the stairs.' if not oldtunnel_exploration_scrap04_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb up the stairs.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap04
                'I go back to the large skeleton.' if oldtunnel_exploration_scrap04_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the large skeleton.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap04
                'I leave the chamber.' if oldtunnel_exploration_scrap01_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap01
                'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                    if oldtunnel_exploration_scrap19_firsttime:
                        $ minutes += 32
                        jump oldtunnel_exploration_scrap19
                    if oldtunnel_exploration_scrap15_firsttime:
                        $ minutes += 25
                        jump oldtunnel_exploration_scrap15
                    if oldtunnel_exploration_scrap14_firsttime:
                        $ minutes += 23
                        jump oldtunnel_exploration_scrap14
                    if oldtunnel_exploration_scrap11_firsttime:
                        $ minutes += 18
                        jump oldtunnel_exploration_scrap11
                    if oldtunnel_exploration_scrap08_firsttime:
                        $ minutes += 15
                        jump oldtunnel_exploration_scrap08
                'I go back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                    $ minutes += 6
                    jump oldtunnelafterinteraction01
        else:
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            if oldtunnel_exploration_scrap03_trap == "whip":
                $ custom1 = "You jump over the triggering cord, away from the undead’s sight. The powerful hit in the chest sends it back, and you hear a loud crack. "
                $ oldtunnel_inside_undead_hp -= 3
            else:
                $ custom1 = ""
            if oldtunnel_inside_undead_hp_old != oldtunnel_inside_undead_hp:
                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                    $ oldtunnel_inside_undead_amount = 3
                    $ custom2 = "The loose bones of the first undead scatter over the floor.\n\n"
                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                    $ oldtunnel_inside_undead_amount = 2
                    $ custom2 = "Having no more ribs, the second undead falls on the floor silently.\n\n"
                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                    $ oldtunnel_inside_undead_amount = 1
                    $ custom2 = "The third undead lets out a quiet moan as it crumbles. There’s only one creature left.\n\n"
                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                    $ oldtunnel_inside_undead_amount_0_description = 1
                    $ custom2 = "After a few moments, the last undead shuffles forward, giving you an empty, yet somehow hungry look.\n\n"
                else:
                    $ custom2 = ""
            else:
                $ custom2 = ""
            menu:
                '[custom1][custom2]You have hardly enough space to swing your weapon.
                '
                'I run to the skeleton of a beast.' if oldtunnel_exploration_scrap04_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to the skeleton of a beast.')
                    $ minutes += 1
                    jump oldtunnel_exploration_scrap04
                '{image=d6} I’m ready to face the undead.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                    jump oldtunnel_combat_lastclash

    label oldtunnel_exploration_scrap03_search:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the room.')
        $ oldtunnel_exploration_scrap03_search = 1
        $ oldtunnel_exploration_wood += 1
        $ minutes += 5
        menu:
            'You find no caches or boxes, and the cart is empty. The one thing that draws your attention are the planks and logs themselves - they’re in decent shape, flexible, though too moist to be worth carrying out of the cave. They could be turned into a new door, or maybe a table.
            '
            'I search the room.' if not oldtunnel_exploration_scrap03_search:
                jump oldtunnel_exploration_scrap03_search
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap03_search and not oldtunnel_exploration_scrap03_trap:
                jump oldtunnel_exploration_scrap03_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap03_trap:
                pass
            'I climb up the stairs.' if not oldtunnel_exploration_scrap04_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb up the stairs.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap04
            'I go back to the large skeleton.' if oldtunnel_exploration_scrap04_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the large skeleton.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap04
            'I leave the chamber.' if oldtunnel_exploration_scrap01_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap01
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 32
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 25
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 23
                    jump oldtunnel_exploration_scrap14
                if oldtunnel_exploration_scrap11_firsttime:
                    $ minutes += 18
                    jump oldtunnel_exploration_scrap11
                if oldtunnel_exploration_scrap08_firsttime:
                    $ minutes += 15
                    jump oldtunnel_exploration_scrap08
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 6
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap03_trap:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider putting a trap here.')
        menu:
            'You look around.
            '
            'I lack the knowledge to build complex traps. (disabled)' if not oldtunnel_exploration_knowledge:
                pass
            'Unless I find some decent wood around here I won’t be able to build anything. (disabled)' if oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_knowledge and not oldtunnel_exploration_wood:
                pass
            'I could tie the monster claws to a branch and construct a whip trap.' if oldtunnel_exploration_knowledge and oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_wood and oldtunnel_exploration_bones:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could tie the monster claws to a branch and construct a whip trap.')
                if oldtunnel_exploration_tools:
                    $ custom1 = "Thanks to the tools you found, it won’t take more than half an hour."
                else:
                    $ custom1 = "Since you lack proper tools, it will take you about an hour."
                if oldtunnel_exploration_trap_availability_whip == 2:
                    $ custom2 = "You have enough claws, cords, and wood to build 2 whip traps in the entire tunnel."
                else:
                    $ custom2 = "You have enough supplies to build 1 more whip trap in the entire tunnel."
                menu:
                    'You could conveniently hide it next to the entrance. Once something runs into the trigger mechanism, it won’t have much time to dodge the hit.
                    \n\n[custom1]
                    \n\n[custom2]
                    '
                    'Let’s get to it.' ( condition="pc_hp >= 2" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        $ oldtunnel_exploration_scrap03_trap = "whip"
                        $ oldtunnel_exploration_trap_availability_whip -= 1
                        if oldtunnel_exploration_tools:
                            $ quarters += 2
                        else:
                            $ quarters += 4
                        $ custom1 = "Once you’re done, you take a long look at the triggering cord. Getting hit with the monstrous claws could kill you on the spot."
                        jump oldtunnel_exploration_scrap03_trap2
                    'I’m too tired to safely build a trap. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1" ):
                        pass
                    'Forget it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                        $ custom1 = "You feel the gentle movement of humid air."
                        jump oldtunnel_exploration_scrap03_trap2
            'I lack sharp spikes that could help me place a more damaging trap. (disabled)' if oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_knowledge and not oldtunnel_exploration_bones:
                pass
            'I won’t find enough supplies to build another whip trap. (disabled)' if not oldtunnel_exploration_trap_availability_whip:
                pass
            'Forget it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                $ custom1 = "You feel the gentle movement of humid air."
                jump oldtunnel_exploration_scrap03_trap2

    label oldtunnel_exploration_scrap03_trap2:
        menu:
            '[custom1]
            '
            'I search the room.' if not oldtunnel_exploration_scrap03_search:
                jump oldtunnel_exploration_scrap03_search
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap03_search and not oldtunnel_exploration_scrap03_trap:
                jump oldtunnel_exploration_scrap03_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap03_trap:
                pass
            'I climb up the stairs.' if not oldtunnel_exploration_scrap04_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb up the stairs.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap04
            'I go back to the large skeleton.' if oldtunnel_exploration_scrap04_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the large skeleton.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap04
            'I leave the chamber.' if oldtunnel_exploration_scrap01_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap01
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 32
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 25
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 23
                    jump oldtunnel_exploration_scrap14
                if oldtunnel_exploration_scrap11_firsttime:
                    $ minutes += 18
                    jump oldtunnel_exploration_scrap11
                if oldtunnel_exploration_scrap08_firsttime:
                    $ minutes += 15
                    jump oldtunnel_exploration_scrap08
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 6
                jump oldtunnelafterinteraction01

label oldtunnel_exploration_scrap04ALL:
    label oldtunnel_exploration_scrap04: # leniwiec
        $ oldtunnel_exploration_position = 4
        if not oldtunnel_exploration_combat:
            if not oldtunnel_exploration_scrap04_firsttime:
                $ oldtunnel_exploration_scrap04_firsttime = 1
                $ custom1 = "You flinch after the light touches the resting bone, but nothing tries to jump at you, and you hear no shuffling feet. You step forward and take a closer look at the remains of the massive creature. It used to be two times as long as your palfrey, three if you were to count the hind limbs. It resembles a bear, but its skull has no sharp teeth and is of a different shape."
            else:
                $ custom1 = "The creature hasn’t moved since your last visit."
            if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside03.ogg":
                play nature "audio/ambient/oldtunnelinside03.ogg" fadeout 2.0 fadein 2.0 volume 1.0
            menu:
                '[custom1]
                '
                'I take a closer look at the skeleton.' if not oldtunnel_exploration_scrap04_search:
                    jump oldtunnel_exploration_scrap04_search
                'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                    pass
                'I leave the chamber.' if oldtunnel_exploration_scrap03_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap03
                'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                    if oldtunnel_exploration_scrap19_firsttime:
                        $ minutes += 34
                        jump oldtunnel_exploration_scrap19
                    if oldtunnel_exploration_scrap15_firsttime:
                        $ minutes += 27
                        jump oldtunnel_exploration_scrap15
                    if oldtunnel_exploration_scrap14_firsttime:
                        $ minutes += 25
                        jump oldtunnel_exploration_scrap14
                    if oldtunnel_exploration_scrap11_firsttime:
                        $ minutes += 20
                        jump oldtunnel_exploration_scrap11
                    if oldtunnel_exploration_scrap08_firsttime:
                        $ minutes += 17
                        jump oldtunnel_exploration_scrap08
                'I go back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                    $ minutes += 7
                    jump oldtunnelafterinteraction01
        else:
            menu:
                'You’ve nowhere else to go. At best, you can stay close to the skeleton, securing your weaker side.
                '
                '{image=d6} I face the undead.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I face the undead.')
                    jump oldtunnel_combat_lastclash

    label oldtunnel_exploration_scrap04_search:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the skeleton.')
        $ oldtunnel_exploration_scrap04_search = 1
        $ oldtunnel_exploration_bones = 1
        $ minutes += 5
        menu:
            'The ribs of the creature are as long as your own trunk, though the age makes them brittle. You observe the long legs, horse-like head, and the massive stomach. You can’t tell if you’ve ever seen such a beast alive, but surely not its trophies.
            \n\nA part that’s uniquely sharp are the creature’s claws - they could pierce two sides of your skull at once, as curved as a war pick and as heavy as an axe, and the marks on the walls perfectly match them. While impressive, they’re too old and awkward to be turned into tools.
            '
            'I take a closer look at the skeleton.' if not oldtunnel_exploration_scrap04_search:
                jump oldtunnel_exploration_scrap04_search
            'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                pass
            'I leave the chamber.' if oldtunnel_exploration_scrap03_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap03
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 34
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 27
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 25
                    jump oldtunnel_exploration_scrap14
                if oldtunnel_exploration_scrap11_firsttime:
                    $ minutes += 20
                    jump oldtunnel_exploration_scrap11
                if oldtunnel_exploration_scrap08_firsttime:
                    $ minutes += 17
                    jump oldtunnel_exploration_scrap08
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 7
                jump oldtunnelafterinteraction01

label oldtunnel_exploration_scrap05ALL:
    label oldtunnel_exploration_scrap05: # tunel do wody
        $ oldtunnel_exploration_position = 5
        if not oldtunnel_exploration_combat:
            if not oldtunnel_exploration_scrap05_firsttime:
                $ oldtunnel_exploration_scrap05_firsttime = 1
                $ custom1 = "You forge ahead for another few long minutes, no longer able to see the light from the exit. You’d need to stand on someone’s shoulders to touch the ceiling. So far, you could ride through the tunnel without getting out of the saddle.\n\nThe sound of a stream is reaching you from ahead. This time, there are no side paths. "
                $ custom2 = ""
            else:
                $ custom1 = "The tunnel hides no surprises."
                if oldtunnel_exploration_scrap05_trap == "whip" and not oldtunnel_inside_undead_defeated:
                    $ custom2 = " Your whip trap is still here."
                else:
                    $ custom2 = ""
            if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside04.ogg":
                play nature "audio/ambient/oldtunnelinside04.ogg" fadeout 2.0 fadein 2.0 volume 1.0
            menu:
                '[custom1][custom2]
                '
                'I examine the tunnel.' if not oldtunnel_exploration_scrap05_search:
                    jump oldtunnel_exploration_scrap05_search
                'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap05_search and not oldtunnel_exploration_scrap05_trap:
                    jump oldtunnel_exploration_scrap05_trap
                'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap05_trap:
                    pass
                'I move forward.' if not oldtunnel_exploration_scrap06_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                    $ minutes += 4
                    jump oldtunnel_exploration_scrap06
                'I head to the stream.' if oldtunnel_exploration_scrap06_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the stream.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap06
                'I head back to the crossroads.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the crossroads.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap01
                'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                    if oldtunnel_exploration_scrap19_firsttime:
                        $ minutes += 27
                        jump oldtunnel_exploration_scrap19
                    if oldtunnel_exploration_scrap15_firsttime:
                        $ minutes += 20
                        jump oldtunnel_exploration_scrap15
                    if oldtunnel_exploration_scrap14_firsttime:
                        $ minutes += 18
                        jump oldtunnel_exploration_scrap14
                    if oldtunnel_exploration_scrap11_firsttime:
                        $ minutes += 13
                        jump oldtunnel_exploration_scrap11
                    if oldtunnel_exploration_scrap08_firsttime:
                        $ minutes += 10
                        jump oldtunnel_exploration_scrap08
                'I go back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                    $ minutes += 7
                    jump oldtunnelafterinteraction01
        else:
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            if oldtunnel_exploration_scrap05_trap == "whip":
                $ custom1 = "You keep running, gasping for air. The monsters notice your jump over the triggering cord and mimic your maneuver easily. The whip trap remains untouched."
                $ oldtunnel_inside_undead_hp -= 0
            else:
                $ custom1 = "You keep running, gasping for air."
            menu:
                '[custom1]
                '
                '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                    jump oldtunnel_combat_spell
                '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                    jump oldtunnel_combat_crossbow
                '{image=d6} I’m ready to face the undead.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                    jump oldtunnel_combat_lastclash
                'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                    pass
                'I head back to the crossroads.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the crossroads.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap01

    label oldtunnel_exploration_scrap05_search:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the tunnel.')
        $ oldtunnel_exploration_scrap05_search = 1
        $ minutes += 10
        menu:
            'You spend a few minutes walking back and forth. Here, the wooden support is denser, with more beams both on the walls and on the ceiling. The trash, on the other hand, is sparse, and you find nothing of use. The animal trails turn back to the entrance, with the exception of the human-like bony prints.
            '
            'I examine the tunnel.' if not oldtunnel_exploration_scrap05_search:
                jump oldtunnel_exploration_scrap05_search
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap05_search and not oldtunnel_exploration_scrap05_trap:
                jump oldtunnel_exploration_scrap05_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap05_trap:
                pass
            'I move forward.' if not oldtunnel_exploration_scrap06_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap06
            'I head to the stream.' if oldtunnel_exploration_scrap06_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the stream.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap06
            'I head back to the crossroads.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the crossroads.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap01
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 27
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 20
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 18
                    jump oldtunnel_exploration_scrap14
                if oldtunnel_exploration_scrap11_firsttime:
                    $ minutes += 13
                    jump oldtunnel_exploration_scrap11
                if oldtunnel_exploration_scrap08_firsttime:
                    $ minutes += 10
                    jump oldtunnel_exploration_scrap08
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 7
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap05_trap:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider putting a trap here.')
        menu:
            'You look around.
            '
            'I lack the knowledge to build complex traps. (disabled)' if not oldtunnel_exploration_knowledge:
                pass
            'Unless I find some decent wood around here I won’t be able to build anything. (disabled)' if oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_knowledge and not oldtunnel_exploration_wood:
                pass
            'I could tie the monster claws to a branch and construct a whip trap.' if oldtunnel_exploration_knowledge and oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_wood and oldtunnel_exploration_bones:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could tie the monster claws to a branch and construct a whip trap.')
                if oldtunnel_exploration_tools:
                    $ custom1 = "Thanks to the tools you found, it won’t take more than half an hour."
                else:
                    $ custom1 = "Since you lack proper tools, it will take you about an hour."
                if oldtunnel_exploration_trap_availability_whip == 2:
                    $ custom2 = "You have enough claws, cords, and wood to build 2 whip traps in the entire tunnel."
                else:
                    $ custom2 = "You have enough supplies to build 1 more whip trap in the entire tunnel."
                menu:
                    'You could hide the bent branch behind one of the supporting beams, though it won’t be easy to camouflage the triggering cord in darkness.
                    \n\n[custom1]
                    \n\n[custom2]
                    '
                    'Let’s get to it.' ( condition="pc_hp >= 2" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        $ oldtunnel_exploration_scrap05_trap = "whip"
                        $ oldtunnel_exploration_trap_availability_whip -= 1
                        if oldtunnel_exploration_tools:
                            $ quarters += 2
                        else:
                            $ quarters += 4
                        $ custom1 = "Once you’re done, you take a long look at the triggering cord. Getting hit with the monstrous claws could kill you on the spot."
                        jump oldtunnel_exploration_scrap05_trap2
                    'I’m too tired to safely build a trap. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1" ):
                        pass
                    'Forget it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                        $ custom1 = "You feel the gentle movement of humid air."
                        jump oldtunnel_exploration_scrap05_trap2
            'I lack sharp spikes that could help me place a more damaging trap. (disabled)' if oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_knowledge and not oldtunnel_exploration_bones:
                pass
            'I won’t find enough supplies to build another whip trap. (disabled)' if not oldtunnel_exploration_trap_availability_whip:
                pass
            'Forget it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                $ custom1 = "You feel the gentle movement of humid air."
                jump oldtunnel_exploration_scrap05_trap2

    label oldtunnel_exploration_scrap05_trap2:
        menu:
            '[custom1]
            '
            'I examine the tunnel.' if not oldtunnel_exploration_scrap05_search:
                jump oldtunnel_exploration_scrap05_search
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap05_search and not oldtunnel_exploration_scrap05_trap:
                jump oldtunnel_exploration_scrap05_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap05_trap:
                pass
            'I move forward.' if not oldtunnel_exploration_scrap06_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap06
            'I head to the stream.' if oldtunnel_exploration_scrap06_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the stream.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap06
            'I head back to the crossroads.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the crossroads.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap01
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 27
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 20
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 18
                    jump oldtunnel_exploration_scrap14
                if oldtunnel_exploration_scrap11_firsttime:
                    $ minutes += 13
                    jump oldtunnel_exploration_scrap11
                if oldtunnel_exploration_scrap08_firsttime:
                    $ minutes += 10
                    jump oldtunnel_exploration_scrap08
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 7
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap05_midcombat_afterinteraction:
        menu:
            '[custom1][custom2]
            '
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I head back to the crossroads.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the crossroads.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap01

    label oldtunnel_exploration_scrap05_midcombat_nothing:
        menu:
            'The undead are getting closer.
            '
            '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'I head back to the crossroads.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the crossroads.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap01

label oldtunnel_exploration_scrap06ALL:
    label oldtunnel_exploration_scrap06: # woda
        $ oldtunnel_exploration_position = 6
        if not oldtunnel_exploration_combat:
            if not oldtunnel_exploration_scrap06_firsttime:
                $ oldtunnel_exploration_scrap06_firsttime = 1
                $ custom1 = "The stream has formed a wide pond. You stab it in a few spots, but it turns out to be only a finger or two deep. There’s no sign of a bridge."
                $ custom2 = ""
            else:
                $ custom1 = "The flow mercilessly carves its path through the mountain."
                if oldtunnel_exploration_scrap06_trap and not oldtunnel_inside_undead_defeated:
                    $ custom2 = " Your foothold trap is still here."
                else:
                    $ custom2 = ""
            if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside05.ogg":
                play nature "audio/ambient/oldtunnelinside05.ogg" fadeout 2.0 fadein 2.0 volume 1.0
            menu:
                '[custom1][custom2]
                '
                'I crouch and take a closer look at the water.' if not oldtunnel_exploration_scrap06_search:
                    jump oldtunnel_exploration_scrap06_search
                'I follow the water.' if oldtunnel_exploration_scrap06_search and not oldtunnel_exploration_scrap07_firsttime:
                    jump oldtunnel_exploration_scrap07_firsttime
                'I consider putting a trap here.' if oldtunnel_exploration_scrap06_search and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap06_trap:
                    jump oldtunnel_exploration_scrap06_trap
                'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap06_trap:
                    pass
                'I move forward.' if not oldtunnel_exploration_scrap08_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap08
                'I move deeper into the tunnel.' if oldtunnel_exploration_scrap08_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move deeper into the tunnel.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap08
                'I head to the exit.' if oldtunnel_exploration_scrap05_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the exit.')
                    $ minutes += 4
                    jump oldtunnel_exploration_scrap05
                'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap11_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                    if oldtunnel_exploration_scrap19_firsttime:
                        $ minutes += 23
                        jump oldtunnel_exploration_scrap19
                    if oldtunnel_exploration_scrap15_firsttime:
                        $ minutes += 16
                        jump oldtunnel_exploration_scrap15
                    if oldtunnel_exploration_scrap14_firsttime:
                        $ minutes += 14
                        jump oldtunnel_exploration_scrap14
                    if oldtunnel_exploration_scrap11_firsttime:
                        $ minutes += 9
                        jump oldtunnel_exploration_scrap11
                'I go back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                    $ minutes += 9
                    jump oldtunnelafterinteraction01
        else:
            $ at = 0
            if oldtunnel_exploration_scrap06_trap == "foothold":
                $ custom1 = "You slow down slightly, making sure to avoid all the foothold traps, and the undead spurt forward - but not for long. After one of them sinks into the bottom of the pond, the others come to a halt, helping it get out. It’s your opportunity to act."
                if pc_class == "mage" and mana >= manacost:
                    $ at_unlock_spell = 1
            else:
                $ custom1 = "The water splatters beneath your boots."
            menu:
                '[custom1]
                '
                'I reload my crossbow.' if oldtunnel_exploration_scrap06_trap == "foothold" and item_crossbow and item_crossbowquarrels and not oldtunnel_exploration_crossbow_ready:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reload my crossbow.')
                    $ oldtunnel_exploration_crossbow_ready = 1
                    $ at_unlock_spell = 0
                    $ at = 0
                    menu:
                        'You put all your strength into it, getting it done before the undead reach you.
                        '
                        'I run up the tunnel.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                            $ minutes += 2
                            jump oldtunnel_exploration_scrap05
                'It can’t dodge a shot from my crossbow now.' if oldtunnel_exploration_scrap06_trap == "foothold" and oldtunnel_exploration_crossbow_ready:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It can’t dodge a shot from my crossbow now.')
                    $ at_unlock_spell = 0
                    $ at = 0
                    $ oldtunnel_exploration_crossbow_ready = 0
                    $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                    menu:
                        'Where do you aim?
                        '
                        'The head.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The head.')
                            $ item_crossbowquarrels -= 1
                            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            $ oldtunnel_inside_undead_hp -= 4
                            if oldtunnel_inside_undead_hp_old != oldtunnel_inside_undead_hp:
                                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                                    $ oldtunnel_inside_undead_amount = 3
                                    $ custom2 = ". The loose bones of the first undead scatter over the pond."
                                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                                    $ oldtunnel_inside_undead_amount = 2
                                    $ custom2 = ". The second undead sinks into the water silently."
                                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                                    $ oldtunnel_inside_undead_amount = 1
                                    $ custom2 = ". The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
                                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                                    $ oldtunnel_inside_undead_amount_0_description = 1
                                    $ custom2 = ". After a few moments, the last undead shuffles forward, giving you an empty, yet somehow hungry look."
                                else:
                                    $ custom2 = ", and while the undead leans away for a few moments, it doesn’t take long for it to straighten up again."
                            menu:
                                'The quarrel pierces through the forehead and stays inside the skull[custom2]
                                '
                                '{image=d6} I’m ready to face the undead.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                                    jump oldtunnel_combat_lastclash
                                'I run up the tunnel.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                                    $ minutes += 2
                                    jump oldtunnel_exploration_scrap05
                        'The chest.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The chest.')
                            $ item_crossbowquarrels -= 1
                            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            menu:
                                'The quarrel grazes a rib, then disappears into the darkness. The undead follows it with its empty gaze, then looks back at you.
                                '
                                '{image=d6} I’m ready to face the undead.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                                    jump oldtunnel_combat_lastclash
                                'I run up the tunnel.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                                    $ minutes += 2
                                    jump oldtunnel_exploration_scrap05
                        'A leg.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- A leg')
                            $ item_crossbowquarrels -= 1
                            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            $ oldtunnel_inside_undead_hp -= 2
                            if oldtunnel_inside_undead_hp_old != oldtunnel_inside_undead_hp:
                                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                                    $ oldtunnel_inside_undead_amount = 3
                                    $ custom2 = "The quarrel shatters it completely. The loose bones of the first undead scatter over the pond."
                                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                                    $ oldtunnel_inside_undead_amount = 2
                                    $ custom2 = "The quarrel shatters it completely. The second undead sinks into the water silently."
                                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                                    $ oldtunnel_inside_undead_amount = 1
                                    $ custom2 = "The quarrel shatters it completely. The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
                                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                                    $ oldtunnel_inside_undead_amount_0_description = 1
                                    $ custom2 = "The quarrel breaks the leg, but the undead is still standing. After a few moments it shuffles forward, giving you an empty, yet somehow hungry look."
                                else:
                                    $ custom2 = "Even though the quarrel grazes the bone and makes your target stagger, the undead regains its composure quickly."
                            menu:
                                '[custom2]
                                '
                                '{image=d6} I’m ready to face the undead.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                                    jump oldtunnel_combat_lastclash
                                'I run up the tunnel.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                                    $ minutes += 2
                                    jump oldtunnel_exploration_scrap05
                'It can’t dodge my spell now. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="oldtunnel_exploration_scrap06_trap == 'foothold' and at == 'spell'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It can’t dodge my spell now.')
                    $ mana = limit_mana(mana-manacost)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                    $ at_unlock_spell = 0
                    $ at = 0
                    $ oldtunnel_inside_undead_hp -= 4
                    if oldtunnel_inside_undead_hp_old != oldtunnel_inside_undead_hp:
                        $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                        if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                            $ oldtunnel_inside_undead_amount = 3
                            $ custom2 = "They scatter over the pond - the first undead is no more."
                        elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                            $ oldtunnel_inside_undead_amount = 2
                            $ custom2 = "The second undead sinks into the water silently."
                        elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                            $ oldtunnel_inside_undead_amount = 1
                            $ custom2 = "The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
                        elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                            $ oldtunnel_inside_undead_amount_0_description = 1
                            $ custom2 = "The last undead leans away for a few moments, and after it straightens up again, it lacks its ribs."
                        else:
                            $ custom2 = "The undead leans away for a few moments, and after it straightens up again, it lacks its ribs."
                    menu:
                        'You reach for the willow wand and dash forward, casting the pneuma with a single swipe. It feels like stabbing the air with a wooden dagger.
                        \n\nThe invisible wave doesn’t spare the revealed bones. [custom2]
                        '
                        '{image=d6} I’m ready to face the undead.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                            jump oldtunnel_combat_lastclash
                        'I run up the tunnel.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                            $ minutes += 2
                            jump oldtunnel_exploration_scrap05
                '{image=d6} I reach for my wand.' ( condition="oldtunnel_exploration_scrap06_trap != 'foothold' and oldtunnel_exploration_crossbow_ready and pc_class == 'mage' and mana >= manacost" ):
                    $ at_unlock_spell = 0
                    $ at = 0
                    jump oldtunnel_combat_spell
                '{image=d6} I raise my crossbow.' if oldtunnel_exploration_scrap06_trap != "foothold" and oldtunnel_exploration_crossbow_ready:
                    $ at_unlock_spell = 0
                    $ at = 0
                    jump oldtunnel_combat_crossbow
                '{image=d6} I’m ready to face the undead.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                    $ at_unlock_spell = 0
                    $ at = 0
                    jump oldtunnel_combat_lastclash
                'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                    pass
                'I run up the tunnel.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                    $ at_unlock_spell = 0
                    $ at = 0
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap05

    label oldtunnel_exploration_scrap06_search:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I crouch and take a closer look at the water.')
        $ oldtunnel_exploration_scrap06_search = 1
        $ minutes += 5
        menu:
            'It’s clean, but the dark rocks and the lack of light camouflage its soft, sand-like bed. You find a few fish bones and other remains, but with every step you disturb the sediment, further clouding the water.
            \n\nThe water flows from your right to the left. Its trail is wide enough to follow, at least for a few steps, and so tall you can do so without crouching.
            '
            'I crouch and take a closer look at the water.' if not oldtunnel_exploration_scrap06_search:
                jump oldtunnel_exploration_scrap06_search
            'I follow the water.' if oldtunnel_exploration_scrap06_search and not oldtunnel_exploration_scrap07_firsttime:
                jump oldtunnel_exploration_scrap07_firsttime
            'I consider putting a trap here.' if oldtunnel_exploration_scrap06_search and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap06_trap:
                jump oldtunnel_exploration_scrap06_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap06_trap:
                pass
            'I move forward.' if not oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap08
            'I move deeper into the tunnel.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move deeper into the tunnel.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap08
            'I head to the exit.' if oldtunnel_exploration_scrap05_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the exit.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap05
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap11_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 23
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 16
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 14
                    jump oldtunnel_exploration_scrap14
                if oldtunnel_exploration_scrap11_firsttime:
                    $ minutes += 9
                    jump oldtunnel_exploration_scrap11
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 9
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap07_firsttime:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the water.')
        $ oldtunnel_exploration_scrap07_firsttime = 1
        $ minutes += 10
        $ item_cavemushroom += 1
        if pc_class != "scholar":
            $ renpy.notify("You picked the cave ear mushroom.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked the cave ear mushroom.{/i}')
        else:
            $ renpy.notify("You added the cave ear mushroom to your bag of ingredients.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You added the cave ear mushroom to your bag of ingredients.{/i}')
        if pc_class != "scholar":
            $ custom1 = "You may want to take it to an alchemist."
        else:
            $ custom1 = "Combined with the snake bait flower, it could be a helpful addition to your collection of potions."
        menu:
            'The corridors become less spacious after just a few steps, but you manage to take a good look around, moving both with and against the flow. The wet walls are home to worms, mold, and what looks like pale spiders, though with only six legs. Among the commotion you spot a {i}cave ear{/i} sticking out of the wall - a familiar, though unfriendly mushroom, the creamy color distorted by your light.
            \n\nYou grab your knife and cut away what seems like the least bug-infested chunk, and after wrapping it with a linen sheet you wash your hands. The cave ear is used by some fighters to enhance their senses in combat. [custom1]
            '
            'I crouch and take a closer look at the water.' if not oldtunnel_exploration_scrap06_search:
                jump oldtunnel_exploration_scrap06_search
            'I follow the water.' if oldtunnel_exploration_scrap06_search and not oldtunnel_exploration_scrap07_firsttime:
                jump oldtunnel_exploration_scrap07_firsttime
            'I consider putting a trap here.' if oldtunnel_exploration_scrap06_search and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap06_trap:
                jump oldtunnel_exploration_scrap06_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap06_trap:
                pass
            'I move forward.' if not oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap08
            'I move deeper into the tunnel.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move deeper into the tunnel.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap08
            'I head to the exit.' if oldtunnel_exploration_scrap05_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the exit.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap05
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap11_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 23
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 16
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 14
                    jump oldtunnel_exploration_scrap14
                if oldtunnel_exploration_scrap11_firsttime:
                    $ minutes += 9
                    jump oldtunnel_exploration_scrap11
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 9
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap06_trap:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider putting a trap here.')
        menu:
            'You look around.
            '
            'I lack the knowledge to build complex traps. (disabled)' if not oldtunnel_exploration_knowledge:
                pass
            'I could make a few foothold traps to slow down the undead.' if oldtunnel_exploration_knowledge and oldtunnel_exploration_trap_availability_foothold:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could make a few foothold traps to slow down the undead.')
                if oldtunnel_exploration_wood:
                    $ custom1 = "Since you already know where to find some decent wood, you can get this done in just a few minutes."
                else:
                    $ custom1 = "Since you need to bring wood from the outside and split it by yourself, it will take you almost an hour."
                menu:
                    'You can make a few deeper holes in the more static parts of the water and surround them with sticks. It should be enough to catch one’s foot, even if only for a few breaths.
                    \n\n[custom1]
                    '
                    'Let’s get to it.' ( condition="pc_hp >= 1" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        $ oldtunnel_exploration_scrap06_trap = "foothold"
                        $ oldtunnel_exploration_trap_availability_foothold -= 1
                        if oldtunnel_exploration_wood:
                            $ quarters += 1
                        else:
                            $ quarters += 3
                        $ custom1 = "Once you’re done, you observe the traps carefully. Even in strong light, they’re barely visible."
                        jump oldtunnel_exploration_scrap06_trap2
                    'I’m too tired to safely build a trap. (Required vitality: 1) (disabled)' ( condition="pc_hp <= 0" ):
                        pass
                    'Forget it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                        $ custom1 = "You feel the gentle movement of humid air."
                        jump oldtunnel_exploration_scrap06_trap2
            'Forget it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                $ custom1 = "You feel the gentle movement of humid air."
                jump oldtunnel_exploration_scrap06_trap2

    label oldtunnel_exploration_scrap06_trap2:
        menu:
            '[custom1]
            '
            'I crouch and take a closer look at the water.' if not oldtunnel_exploration_scrap06_search:
                jump oldtunnel_exploration_scrap06_search
            'I follow the water.' if oldtunnel_exploration_scrap06_search and not oldtunnel_exploration_scrap07_firsttime:
                jump oldtunnel_exploration_scrap07_firsttime
            'I consider putting a trap here.' if oldtunnel_exploration_scrap06_search and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap06_trap:
                jump oldtunnel_exploration_scrap06_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap06_trap:
                pass
            'I move forward.' if not oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move forward.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap08
            'I move deeper into the tunnel.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move deeper into the tunnel.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap08
            'I head to the exit.' if oldtunnel_exploration_scrap05_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the exit.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap05
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap11_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 23
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 16
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 14
                    jump oldtunnel_exploration_scrap14
                if oldtunnel_exploration_scrap11_firsttime:
                    $ minutes += 9
                    jump oldtunnel_exploration_scrap11
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 9
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap06_midcombat_afterinteraction:
        menu:
            '[custom1][custom2]
            '
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I run up the tunnel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap05

    label oldtunnel_exploration_scrap06_midcombat_nothing:
        menu:
            'The undead are getting closer.
            '
            '{image=d6} I reach for my wand.' ( condition="oldtunnel_exploration_scrap06_trap != 'foothold' and oldtunnel_exploration_crossbow_ready and pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_scrap06_trap != "foothold" and oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'I run up the tunnel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap05

label oldtunnel_exploration_scrap08ALL:
    label oldtunnel_exploration_scrap08: # wejście do części ludzkiej
        $ oldtunnel_exploration_position = 8
        if not oldtunnel_exploration_combat:
            if not oldtunnel_exploration_scrap08_firsttime:
                $ oldtunnel_exploration_scrap08_firsttime = 1
                $ custom1 = "The open door to your right leads to a narrow corridor. You take a look further down the tunnel - a cave-in broke the timber, blocking the path forward."
                $ custom2 = ""
            else:
                $ custom1 = "The path forward is blocked."
                if oldtunnel_exploration_scrap08_trap == "deadfall" and not oldtunnel_inside_undead_defeated:
                    $ custom2 = " Your deadfall trap is still here."
                elif oldtunnel_exploration_scrap08_trap == "whip" and not oldtunnel_inside_undead_defeated:
                    $ custom2 = " Your whip trap is still here."
                else:
                    $ custom2 = ""
            if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside04.ogg":
                play nature "audio/ambient/oldtunnelinside04.ogg" fadeout 2.0 fadein 2.0 volume 1.0
            menu:
                '[custom1][custom2]
                '
                'I take a closer look at the cave-in.' if not oldtunnel_exploration_scrap09_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the cave-in.')
                    $ minutes += 1
                    jump oldtunnel_exploration_scrap09
                'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap08_trap:
                    jump oldtunnel_exploration_scrap08_trap
                'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap08_trap:
                    pass
                'I walk through the door.' if not oldtunnel_exploration_scrap10_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk through the door.')
                    $ minutes += 1
                    jump oldtunnel_exploration_scrap10
                'I enter the dining chamber.' if oldtunnel_exploration_scrap10_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the dining chamber.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap11
                'I return to the stream.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the stream.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap06
                'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap14_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                    if oldtunnel_exploration_scrap19_firsttime:
                        $ minutes += 20
                        jump oldtunnel_exploration_scrap19
                    if oldtunnel_exploration_scrap15_firsttime:
                        $ minutes += 13
                        jump oldtunnel_exploration_scrap15
                    if oldtunnel_exploration_scrap14_firsttime:
                        $ minutes += 11
                        jump oldtunnel_exploration_scrap14
                'I go back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                    $ minutes += 13
                    jump oldtunnelafterinteraction01
        else:
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            if oldtunnel_exploration_scrap08_trap == "deadfall":
                $ custom1 = "You pull the cord and drop the sharp rocks on an undead skull, crushing it and making its owner collapse. "
                $ oldtunnel_inside_undead_hp -= 4
                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                    $ oldtunnel_inside_undead_amount = 3
                    $ custom2 = "The loose bones of the first undead scatter over the floor."
                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                    $ oldtunnel_inside_undead_amount = 2
                    $ custom2 = "It stops moving."
                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                    $ oldtunnel_inside_undead_amount = 1
                    $ custom2 = "It lets out a quiet moan and turns into a pile of bones. There’s only one creature left."
                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                    $ oldtunnel_inside_undead_amount_0_description = 1
                    $ custom2 = "It’s almost enough - the last undead shuffles forward, giving you an empty, yet somehow hungry look."
                else:
                    $ custom2 = "It’s hard to believe it can still get up."
            elif oldtunnel_exploration_scrap08_trap == "whip":
                $ custom1 = "You jump over the triggering cord, but the undead doesn’t even notice its presence. The powerful hit in the chest sends it back, and you hear a loud crack. "
                $ oldtunnel_inside_undead_hp -= 3
                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                    $ oldtunnel_inside_undead_amount = 3
                    $ custom2 = "Only three undead leave the corridor."
                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                    $ oldtunnel_inside_undead_amount = 2
                    $ custom2 = "Only two undead leave the corridor."
                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                    $ oldtunnel_inside_undead_amount = 1
                    $ custom2 = "Only one undead leaves the corridor."
                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                    $ oldtunnel_inside_undead_amount_0_description = 1
                    $ custom2 = "After a few moments, the last undead shuffles forward, giving you an empty, yet somehow hungry look."
                else:
                    $ custom2 = "After a few moments, the last undead shuffles forward, even though it has no ribs."
            else:
                $ custom1 = "You get through the door and look around. Only one path left."
                $ custom2 = ""
            menu:
                '[custom1][custom2]
                '
                '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                    jump oldtunnel_combat_spell
                '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                    jump oldtunnel_combat_crossbow
                '{image=d6} I’m ready to face the undead.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                    jump oldtunnel_combat_lastclash
                'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                    pass
                'I turn toward the stream.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn toward the stream.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap06

    label oldtunnel_exploration_scrap08_trap:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider putting a trap here.')
        menu:
            'You look around.
            '
            'I lack the knowledge to build complex traps. (disabled)' if not oldtunnel_exploration_knowledge:
                pass
            'I could crush the monsters with a deadfall trap.' if oldtunnel_exploration_scrap09_firsttime and oldtunnel_exploration_knowledge and oldtunnel_exploration_trap_availability_deadfall and oldtunnel_exploration_wood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could crush the monsters with a deadfall trap.')
                if oldtunnel_exploration_tools:
                    $ custom1 = "Even with the tools you found, it will take you more than an hour."
                else:
                    $ custom1 = "Since you lack proper tools, it may take you up to two hours, and will be quite tiresome."
                if oldtunnel_exploration_trap_availability_deadfall == 2:
                    $ custom2 = "You have enough supplies to build 2 deadfall traps in the entire tunnel."
                else:
                    $ custom2 = "You have enough supplies to build 1 more deadfall trap in the entire tunnel."
                menu:
                    'You could build a humble structure right above the entrance, using the rubble from the cave-in, then make it collapse by pulling a rope, though you can’t be sure the creatures won’t notice your attempt.
                    \n\n[custom1]
                    \n\n[custom2]
                    '
                    'Let’s get to it.' ( condition="pc_hp >= 3" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        $ oldtunnel_exploration_scrap08_trap = "deadfall"
                        $ oldtunnel_exploration_trap_availability_deadfall -= 1
                        if oldtunnel_exploration_tools:
                            $ cleanliness = limit_cleanliness(cleanliness-1)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ quarters += 4
                        else:
                            $ quarters += 7
                            $ pc_food = limit_pc_food(pc_food-1)
                            show minus1food at foodchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
                            $ cleanliness = limit_cleanliness(cleanliness-2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                            show minus2appearance at appearancechange onlayer myoverlay
                        $ custom1 = "You put the triggering cord away from your usual path to avoid stumbling over it."
                        jump oldtunnel_exploration_scrap08_trap2
                    'I’m too tired to safely build a trap. (Required vitality: 3) (disabled)' ( condition="pc_hp <= 2" ):
                        pass
                    'I think about another trap.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about another trap.')
                        jump oldtunnel_exploration_scrap08_trap
                    'Forget it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                        $ custom1 = "You feel the gentle movement of humid air."
                        jump oldtunnel_exploration_scrap08_trap2
            'Unless I find some decent wood around here I won’t be able to build anything. (disabled)' if (oldtunnel_exploration_scrap09_firsttime and oldtunnel_exploration_trap_availability_deadfall and oldtunnel_exploration_knowledge and not oldtunnel_exploration_wood) or (oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_knowledge and not oldtunnel_exploration_wood):
                pass
            'I won’t find enough supplies to build another deadfall trap. (disabled)' if oldtunnel_exploration_scrap09_firsttime and not oldtunnel_exploration_trap_availability_deadfall:
                pass
            'I could tie the monster claws to a branch and construct a whip trap.' if oldtunnel_exploration_knowledge and oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_wood and oldtunnel_exploration_bones:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could tie the monster claws to a branch and construct a whip trap.')
                if oldtunnel_exploration_tools:
                    $ custom1 = "Thanks to the tools you found, it won’t take more than half an hour."
                else:
                    $ custom1 = "Since you lack proper tools, it will take you about an hour."
                if oldtunnel_exploration_trap_availability_whip == 2:
                    $ custom2 = "You have enough claws, cords, and wood to build 2 whip traps in the entire tunnel."
                else:
                    $ custom2 = "You have enough supplies to build 1 more whip trap in the entire tunnel."
                menu:
                    'Unless the creatures have extraordinary reflexes, you doubt it could avoid the hit after it stumbles over the triggering cord.
                    \n\n[custom1]
                    \n\n[custom2]
                    '
                    'Let’s get to it.' ( condition="pc_hp >= 2" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        $ oldtunnel_exploration_scrap08_trap = "whip"
                        $ oldtunnel_exploration_trap_availability_whip -= 1
                        if oldtunnel_exploration_tools:
                            $ quarters += 2
                        else:
                            $ quarters += 4
                        $ custom1 = "Once you’re done, you take a long look at the triggering cord. Getting hit with the monstrous claws could kill you on the spot."
                        jump oldtunnel_exploration_scrap08_trap2
                    'I’m too tired to safely build a trap. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1" ):
                        pass
                    'I think about another trap.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about another trap.')
                        jump oldtunnel_exploration_scrap08_trap
                    'Forget it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                        $ custom1 = "You feel the gentle movement of humid air."
                        jump oldtunnel_exploration_scrap08_trap2
            'I lack sharp spikes that could help me place a more damaging trap. (disabled)' if oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_knowledge and not oldtunnel_exploration_bones:
                pass
            'I won’t find enough supplies to build another whip trap. (disabled)' if not oldtunnel_exploration_trap_availability_whip:
                pass
            'Forget it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                $ custom1 = "You feel the gentle movement of humid air."
                jump oldtunnel_exploration_scrap08_trap2

    label oldtunnel_exploration_scrap08_trap2:
        menu:
            '[custom1]
            '
            'I take a closer look at the cave-in.' if not oldtunnel_exploration_scrap09_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the cave-in.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap09
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap08_trap:
                jump oldtunnel_exploration_scrap08_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap08_trap:
                pass
            'I walk through the door.' if not oldtunnel_exploration_scrap10_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk through the door.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap10
            'I enter the dining chamber.' if oldtunnel_exploration_scrap10_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the dining chamber.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap11
            'I return to the stream.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the stream.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap06
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap14_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 20
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 13
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 11
                    jump oldtunnel_exploration_scrap14
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 13
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap08_midcombat_afterinteraction:
        menu:
            '[custom1][custom2]
            '
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I turn toward the stream.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn toward the stream.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap06

    label oldtunnel_exploration_scrap08_midcombat_nothing:
        menu:
            'The undead are getting closer.
            '
            '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'I turn toward the stream.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn toward the stream.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap06

    label oldtunnel_exploration_scrap09: # blokada
        $ oldtunnel_exploration_position = 9
        $ oldtunnel_exploration_scrap09_firsttime = 1
        if not oldtunnel_inside_undead_defeated:
            $ custom1 = "\n\nYou climb up a bit and peek through a larger hole, close to the ceiling. There’s a weak light coming from the distant end of the tunnel."
        else:
            $ custom1 = ""
        menu:
            'You push away a few rocks, making them roll on the floor, but the blockade is at least a few steps deep. It would take an entire team of diggers to get through, if it’s possible at all.[custom1]
            '
            'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                pass
            'I step away.' if oldtunnel_exploration_scrap08_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap08
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap14_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 21
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 14
                    jump oldtunnel_exploration_scrap15
                if oldtunnel_exploration_scrap14_firsttime:
                    $ minutes += 12
                    jump oldtunnel_exploration_scrap14
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 15
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap10: # korytarzyk
        $ oldtunnel_exploration_position = 10
        if not oldtunnel_exploration_combat:
            $ oldtunnel_exploration_scrap10_firsttime = 1
            if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside06alt.ogg":
                play nature "audio/ambient/oldtunnelinside06alt.ogg" fadeout 2.0 fadein 2.0 volume 1.0
            menu:
                'It squeaks. The corridor resembles the interiors of a fortress, with flat, regular walls, and a ceiling so low you couldn’t ride through it.
                \n\nYou reach another, much larger chamber, which seems to mimic the corridor’s style.
                '
                'I enter it.' if not oldtunnel_exploration_scrap11_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter it.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap11
        else:
            menu:
                'You lead the undead to the short corridor. The door has no lock, you can’t keep them away, but they have to enter one at a time.
                '
                '{image=d6} I use the opportunity to strike the closest one, then move back.':
                    jump oldtunnel_exploration_scrap10_clash
                '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                    jump oldtunnel_combat_spell
                'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                    pass
                'I keep running.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep running.')
                    jump oldtunnel_exploration_scrap08

    label oldtunnel_exploration_scrap10_clash:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I use the opportunity to strike the closest one, then move back.')
        $ minutes += 1
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
        $ pc_battlecounter += 1
        if d100roll <= 30:
            if d100roll <= 10:
                $ oldtunnel_inside_undead_hp -= 3
            else:
                $ oldtunnel_inside_undead_hp -= 2
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            $ custom1 = "You manage to surprise it with your fierce attack, cutting off its arm with a confident thrust, then step away, unable to swing your blade in such a limited space. "
            if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                $ oldtunnel_inside_undead_amount = 3
                $ custom2 = "The loose bones of the first undead scatter over the floor."
            elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                $ oldtunnel_inside_undead_amount = 2
                $ custom2 = "The second undead hits the ground silently."
            elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                $ oldtunnel_inside_undead_amount = 1
                $ custom2 = "The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
            elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                $ oldtunnel_inside_undead_amount_0_description = 1
                $ custom2 = "After a few moments, the last undead shuffles forward, giving you an empty, yet somehow hungry look."
            else:
                $ custom2 = "While the undead leans away for a few moments, it doesn’t take long for it to straighten up again."
            menu:
                '[custom1][custom2]
                '
                'I keep running.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep running.')
                    jump oldtunnel_exploration_scrap08
        elif d100roll <= 60:
            $ oldtunnel_inside_undead_hp -= 2
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
            else:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            $ custom1 = "You manage to land your fierce attack, but you only break one of the arm bones. The creature strikes you back with a crude sledgehammer. Limited by the size of the corridor, you fail your block. "
            if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                $ oldtunnel_inside_undead_amount = 3
                $ custom2 = "Still, the loose bones of the first undead scatter over the floor."
            elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                $ oldtunnel_inside_undead_amount = 2
                $ custom2 = "Still, the second undead hits the ground silently."
            elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                $ oldtunnel_inside_undead_amount = 1
                $ custom2 = "Still, the third undead lets out a quiet moan as it crumbles. There’s only one creature left."
            elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                $ oldtunnel_inside_undead_amount_0_description = 1
                $ custom2 = "After a few moments, the last undead shuffles forward, giving you an empty, yet somehow hungry look."
            else:
                $ custom2 = "While the undead leans away for a few moments, it doesn’t take long for it to straighten up again."
            menu:
                '[custom1][custom2]
                '
                'I keep running.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep running.')
                    jump oldtunnel_exploration_scrap08
        else:
            $ oldtunnel_inside_undead_hp -= 1
            if armor >= 3:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            elif armor == 2:
                $ armor = limit_armor(armor-2)
                show minus2armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                if not cleanliness_clothes_torn:
                    $ cleanliness_clothes_torn = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
            elif armor >= 1:
                $ armor = limit_armor(armor-1)
                show minus1armor at armorchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            else:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            $ custom1 = "You manage to land your reckless attack, barely hitting one of the arm bones. The creature strikes you back with a crude sledgehammer. Limited by the size of the corridor, you fail your block. "
            if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                $ oldtunnel_inside_undead_amount = 3
                $ custom2 = "The loose bones of the first undead scatter over the floor."
            elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                $ oldtunnel_inside_undead_amount = 2
                $ custom2 = "The second undead hits the ground silently."
            elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                $ oldtunnel_inside_undead_amount = 1
                $ custom2 = "The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
            elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                $ oldtunnel_inside_undead_amount_0_description = 1
                $ custom2 = "After a few moments, the last undead shuffles forward, giving you an empty, yet somehow hungry look."
            else:
                $ custom2 = "While the undead leans away for a few moments, it doesn’t take long for it to straighten up again."
            menu:
                '[custom1][custom2]
                '
                'I keep running.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep running.')
                    jump oldtunnel_exploration_scrap08

    label oldtunnel_exploration_scrap10_midcombat_afterinteraction:
        menu:
            '[custom1][custom2]
            '
            'I keep running.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep running.')
                jump oldtunnel_exploration_scrap08

    label oldtunnel_exploration_scrap10_midcombat_nothing:
        menu:
            'The undead are getting closer.
            '
            '{image=d6} I use the opportunity to strike the closest one, then move back.':
                jump oldtunnel_exploration_scrap10_clash
            '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'I keep running.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep running.')
                jump oldtunnel_exploration_scrap08

label oldtunnel_exploration_scrap11ALL:
    label oldtunnel_exploration_scrap11: # jadalnia
        $ oldtunnel_exploration_position = 11
        if not oldtunnel_exploration_combat:
            if not oldtunnel_exploration_scrap11_firsttime:
                $ oldtunnel_exploration_scrap11_firsttime = 1
                $ custom1 = "The spoiled food and moldy planks make you hold your breath. The chamber used to serve as a dining spot, with tables, chairs, shelves for mugs, and barrels of drinks, but all that’s left are worms and mustiness.\n\nYou don’t see the furthest wall until you bring your light closer. The open door leads to a new, natural cavern. Another, closed door is in the corner of the room, opposite the one you came from."
                $ custom2 = ""
            else:
                $ custom1 = "The spoiled food and moldy planks make you hold your breath."
                if oldtunnel_exploration_scrap11_trap == "other" and not oldtunnel_inside_undead_defeated:
                    $ custom2 = " The floor is both sticky and slippery."
                elif oldtunnel_exploration_scrap11_trap == "deadfall" and not oldtunnel_inside_undead_defeated:
                    $ custom2 = " Your deadfall trap is still here."
                else:
                    $ custom2 = ""
            if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside06alt.ogg":
                play nature "audio/ambient/oldtunnelinside06alt.ogg" fadeout 2.0 fadein 2.0 volume 1.0
            menu:
                '[custom1][custom2]
                '
                'I search the chamber.' if not oldtunnel_exploration_scrap11_search:
                    jump oldtunnel_exploration_scrap11_search
                'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap11_search and not oldtunnel_exploration_scrap11_trap:
                    jump oldtunnel_exploration_scrap11_trap
                'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap11_trap:
                    pass
                'I walk through the ajar door.' if not oldtunnel_exploration_scrap14_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk through the ajar door.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap14
                'I try to open the door in the corner.' if not oldtunnel_exploration_scrap12_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to open the door in the corner.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap12
                'I head to the chamber with stalactites.' if oldtunnel_exploration_scrap14_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the chamber with stalactites.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap14
                'I head back to the armory.' if oldtunnel_exploration_scrap12_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the armory.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap12
                'I return to the main tunnel.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the main tunnel.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap08
                'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap15_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                    if oldtunnel_exploration_scrap19_firsttime:
                        $ minutes += 16
                        jump oldtunnel_exploration_scrap19
                    if oldtunnel_exploration_scrap15_firsttime:
                        $ minutes += 10
                        jump oldtunnel_exploration_scrap15
                'I go back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                    $ minutes += 16
                    jump oldtunnelafterinteraction01
        else:
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            if oldtunnel_exploration_scrap11_trap == "other":
                $ oldtunnel_inside_undead_hp -= 1
                if pc_hp <= 1:
                    $ cleanliness = limit_cleanliness(cleanliness-3)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
                    show minus3appearance at appearancechange onlayer myoverlay
                    $ custom1 = "After a few steps, you hear the rattling of bones - the undead hit the ground, though their skulls show no concern. They get up slowly, exactly at the same moment when you land on your own bottom, bathing in slime. You grab a chair and use it to get back on your feet.\n\nYou don’t have much time - if you want to keep any distance between you and them, you have to flee."
                else:
                    $ oldtunnel_exploration_scrap11_time = 1
                    $ custom1 = "After a few steps, you hear the rattling of bones - the undead hit the ground, though their skulls show no concern. They get up slowly, but you still have a few moments to turn against them."
            elif oldtunnel_exploration_scrap11_trap == "deadfall":
                $ custom1 = "You pull the cord and drop the beams and boards on an undead skull. The wet timber causes little more than a stagger, but gives you a few moments to react. "
                $ oldtunnel_inside_undead_hp -= 1
                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                $ oldtunnel_exploration_scrap11_time = 1
            else:
                $ custom1 = "You give the door behind you another look. There’s no way to lock it."
            menu:
                '[custom1]
                '
                'I reload my crossbow.' if oldtunnel_exploration_scrap11_time and item_crossbow and item_crossbowquarrels and not oldtunnel_exploration_crossbow_ready:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reload my crossbow.')
                    $ oldtunnel_exploration_crossbow_ready = 1
                    $ at_unlock_spell = 0
                    menu:
                        'You put all your strength into it, getting it done before the undead reach you.
                        '
                        'I leave the chamber.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                            $ minutes += 2
                            jump oldtunnel_exploration_scrap10
                '{image=d6} I reach for my wand.' ( condition="oldtunnel_exploration_scrap11_time and pc_class == 'mage' and mana >= manacost" ):
                    jump oldtunnel_combat_spell
                '{image=d6} I raise my crossbow.' if oldtunnel_exploration_scrap11_time and oldtunnel_exploration_crossbow_ready:
                    jump oldtunnel_combat_crossbow
                '{image=d6} I’m ready to face the undead.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                    jump oldtunnel_combat_lastclash
                'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="oldtunnel_exploration_scrap11_time and pc_class == 'mage' and mana < manacost" ):
                    pass
                'I leave the chamber.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap10

    label oldtunnel_exploration_scrap11_search:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the chamber.')
        $ oldtunnel_exploration_scrap11_search = 1
        $ quarters += 1
        $ item_oldtunnesmallkey += 1
        $ renpy.notify("You found a small iron key.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found a small iron key.{/i}')
        menu:
            'The place was abandoned in haste, but you find no signs of large creatures, bones, or destruction. The wood gives way only to time. A few of the barrels still contain liquids, though you wouldn’t dare open them.
            \n\nClose to the exit leading to a cave you find a hook with a simple iron key. You pick it up, and it stains your hand with rust.
            '
            'I search the chamber.' if not oldtunnel_exploration_scrap11_search:
                jump oldtunnel_exploration_scrap11_search
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap11_search and not oldtunnel_exploration_scrap11_trap:
                jump oldtunnel_exploration_scrap11_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap11_trap:
                pass
            'I walk through the open door.' if not oldtunnel_exploration_scrap14_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk through the open door.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap14
            'I try to open the door in the corner.' if not oldtunnel_exploration_scrap12_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to open the door in the corner.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap12
            'I head to the chamber with stalactites.' if oldtunnel_exploration_scrap14_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the chamber with stalactites.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap14
            'I head back to the armory.' if oldtunnel_exploration_scrap12_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the armory.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap12
            'I return to the main tunnel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the main tunnel.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap08
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap15_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 16
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 10
                    jump oldtunnel_exploration_scrap15
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 16
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap11_trap:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider putting a trap here.')
        menu:
            'You look around.
            '
            'I lack the knowledge to build complex traps. (disabled)' if not oldtunnel_exploration_knowledge:
                pass
            'I could break the barrels and cover the floor with slippery liquid.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could break the barrels and cover the floor with slippery liquid.')
                menu:
                    'They should contain more than enough old drink, but unless you trust that your own shell can manage on a difficult surface, it may hurt you more than the undead.
                    '
                    'Let’s get to it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        $ oldtunnel_exploration_scrap11_trap = "other"
                        $ minutes += 10
                        $ custom1 = "It doesn’t take long, but the stench is gut wrenching. The moldy ales and ciders spill over the floor, making it both sticky and slippery. You wash your blade with a waterskin."
                        jump oldtunnel_exploration_scrap11_trap2
                    'I think about another trap.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about another trap.')
                        jump oldtunnel_exploration_scrap11_trap
                    'Forget it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                        $ custom1 = "You feel the gentle movement of humid air."
                        jump oldtunnel_exploration_scrap11_trap2
            'I could crush the monsters with a deadfall trap.' if oldtunnel_exploration_knowledge and oldtunnel_exploration_trap_availability_deadfall and oldtunnel_exploration_wood:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could crush the monsters with a deadfall trap.')
                if oldtunnel_exploration_tools:
                    $ custom1 = "Even with the tools you found, it will take you more than an hour."
                else:
                    $ custom1 = "Since you lack proper tools, it may take you up to two hours, and will be quite tiresome."
                if oldtunnel_exploration_trap_availability_deadfall == 2:
                    $ custom2 = "You have enough supplies to build 2 deadfall traps in the entire tunnel."
                else:
                    $ custom2 = "You have enough supplies to build 1 more deadfall trap in the entire tunnel."
                menu:
                    'You could hang the load of wooden planks and beams right above the entrance and make it collapse with a pull of the rope. You can’t be sure if such moist wood will be effective at hurting anything.
                    \n\n[custom1]
                    \n\n[custom2]
                    '
                    'Let’s get to it.' ( condition="pc_hp >= 2" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        $ oldtunnel_exploration_scrap11_trap = "deadfall"
                        $ oldtunnel_exploration_trap_availability_deadfall -= 1
                        if oldtunnel_exploration_tools:
                            $ cleanliness = limit_cleanliness(cleanliness-1)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ quarters += 4
                        else:
                            $ quarters += 7
                            $ pc_food = limit_pc_food(pc_food-1)
                            show minus1food at foodchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
                            $ cleanliness = limit_cleanliness(cleanliness-2)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
                            show minus2appearance at appearancechange onlayer myoverlay
                        $ custom1 = "You put the triggering cord away from your usual path to avoid stumbling over it."
                        jump oldtunnel_exploration_scrap11_trap2
                    'I’m too tired to safely build a trap. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 2" ):
                        pass
                    'I think about another trap.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about another trap.')
                        jump oldtunnel_exploration_scrap11_trap
                    'Forget it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                        $ custom1 = "You feel the gentle movement of humid air."
                        jump oldtunnel_exploration_scrap11_trap2
            'Unless I find some decent wood around here I won’t be able to build anything. (disabled)' if oldtunnel_exploration_trap_availability_deadfall and oldtunnel_exploration_knowledge and not oldtunnel_exploration_wood:
                pass
            'I won’t find enough supplies to build another deadfall trap. (disabled)' if not oldtunnel_exploration_trap_availability_deadfall:
                pass
            'Forget it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                $ custom1 = "You feel the gentle movement of humid air."
                jump oldtunnel_exploration_scrap11_trap2

    label oldtunnel_exploration_scrap11_trap2:
        menu:
            '[custom1]
            '
            'I search the chamber.' if not oldtunnel_exploration_scrap11_search:
                jump oldtunnel_exploration_scrap11_search
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap11_search and not oldtunnel_exploration_scrap11_trap:
                jump oldtunnel_exploration_scrap11_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap11_trap:
                pass
            'I walk through the open door.' if not oldtunnel_exploration_scrap14_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk through the open door.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap14
            'I try to open the door in the corner.' if not oldtunnel_exploration_scrap12_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to open the door in the corner.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap12
            'I head to the chamber with stalactites.' if oldtunnel_exploration_scrap14_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the chamber with stalactites.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap14
            'I head back to the armory.' if oldtunnel_exploration_scrap12_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the armory.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap12
            'I return to the main tunnel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the main tunnel.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap08
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap15_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 16
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 10
                    jump oldtunnel_exploration_scrap15
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 16
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap11_midcombat_afterinteraction:
        menu:
            '[custom1][custom2]
            '
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I leave the chamber.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap10

    label oldtunnel_exploration_scrap11_midcombat_nothing:
        menu:
            'The undead are getting closer.
            '
            'I reload my crossbow.' if oldtunnel_exploration_scrap11_time and item_crossbow and item_crossbowquarrels and not oldtunnel_exploration_crossbow_ready:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reload my crossbow.')
                $ oldtunnel_exploration_crossbow_ready = 1
                $ at_unlock_spell = 0
                menu:
                    'You put all your strength into it, getting it done before the undead reach you.
                    '
                    'I leave the chamber.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                        $ minutes += 2
                        jump oldtunnel_exploration_scrap10
            '{image=d6} I reach for my wand.' ( condition="oldtunnel_exploration_scrap11_time and pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_scrap11_time and oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="oldtunnel_exploration_scrap11_time and pc_class == 'mage' and mana < manacost" ):
                pass
            'I leave the chamber.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the chamber.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap10

label oldtunnel_exploration_scrap12ALL:
    label oldtunnel_exploration_scrap12: # armory
        $ oldtunnel_exploration_position = 12
        if not oldtunnel_exploration_scrap12_firsttime:
            $ oldtunnel_exploration_scrap12_firsttime = 1
            $ custom1 = "The door gives way. The next room is also too large for your light to reach all the corners at once. The empty shelves, chests, and spear racks give you no promise of a hidden treasure, but you also find a box with rusty nails, a cracked barrel in the corner, and a broken blade. You could spend some time collecting these and other iron scraps, then sell them in a village.\n\nIn the room’s corner, you notice a wide sheet of moldy fabric that covers a large part of the wall."
        else:
            $ custom1 = "You find no surprises in the armory."
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside06alt.ogg":
            play nature "audio/ambient/oldtunnelinside06alt.ogg" fadeout 2.0 fadein 2.0 volume 1.0
        menu:
            '[custom1]
            '
            'I collect the metal scraps scattered in the room.' if not oldtunnel_exploration_scrap12_ironscraps:
                jump oldtunnel_exploration_scrap12_ironscraps
            'I examine the curtain.' if not oldtunnel_exploration_scrap13_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the small room in the corner.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap13
            'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                pass
            'I return to the tiny room.' if oldtunnel_exploration_scrap13_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the tiny room.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap13
            'I leave the room.' if oldtunnel_exploration_scrap11_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the room.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap11
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap15_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 18
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 12
                    jump oldtunnel_exploration_scrap15
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 20
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap12_ironscraps:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I collect the metal scraps scattered in the room.')
        $ oldtunnel_exploration_scrap12_ironscraps = 1
        if oldtunnel_exploration_tools:
            $ quarters += 1
            $ custom1 = "Knowing where to find the useful tools, you dismantle the barrel and prepare a decent sack of clanging pieces of iron and steel."
        else:
            $ quarters += 3
            $ custom1 = "Having no useful tools at hand, you struggle to dismantle the barrel and cut away all the bits of wood that are attached to the pieces of iron and steel. After a long while, you prepare a decent, clanging sack."
        $ item_ironscraps += 1
        $ renpy.notify("You collected the iron scraps.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You collected the iron scraps.{/i}')
        menu:
            '[custom1] For now, you move it to the dining chamber and leave it by the exit.
            '
            'I collect the metal scraps scattered in the room.' if not oldtunnel_exploration_scrap12_ironscraps:
                jump oldtunnel_exploration_scrap12_ironscraps
            'I examine the curtain.' if not oldtunnel_exploration_scrap13_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the small room in the corner.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap13
            'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                pass
            'I return to the tiny room.' if oldtunnel_exploration_scrap13_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the tiny room.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap13
            'I leave the room.' if oldtunnel_exploration_scrap11_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the room.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap11
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap15_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 18
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 12
                    jump oldtunnel_exploration_scrap15
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 20
                jump oldtunnelafterinteraction01

label oldtunnel_exploration_scrap13ALL:
    label oldtunnel_exploration_scrap13: # klucz
        $ oldtunnel_exploration_position = 13
        if not oldtunnel_exploration_scrap13_firsttime:
            $ oldtunnel_exploration_scrap13_firsttime = 1
            $ custom1 = "It’s divided in the center, allowing you to draw it. Behind it, you find a tiny room, maybe two steps wide and three steps deep. It’s silent, not as humid.\n\nThe wall ahead isn’t like the others. It’s covered with red and purple bricks."
        else:
            $ custom1 = "Almost no sound reaches this spot."
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside06alt.ogg":
            play nature "audio/ambient/oldtunnelinside06alt.ogg" fadeout 1.0 fadein 1.0 volume 0.5
        menu:
            '[custom1]
            '
            'I look for anything unusual.' if not oldtunnel_exploration_scrap13_search:
                jump oldtunnel_exploration_scrap13_search
            'I touch the shape of the hourglass with the pendant I own.' if oldtunnel_exploration_scrap13_search and not oldtunnel_exploration_scrap13_open and item_wingedhourglass:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I touch the shape of the hourglass with the pendant I own.')
                $ custom1 = "It’s a match. You fit it into the grooves, then press. The brick moves deeper inside, then bounces back, allowing you to draw it out completely.\n\nIn the secret compartment you find a key made of bronze. It’s as large as your forearm."
                $ minutes += 1
                jump oldtunnel_exploration_scrap13_open
            'I lack a winged hourglass I could use here. (disabled)' if oldtunnel_exploration_scrap13_search and not oldtunnel_exploration_scrap13_open and not item_wingedhourglass:
                pass
            'I break the brick with The Tool of Destruction.' if oldtunnel_exploration_scrap13_search and item_magicchisel == 2 and not oldtunnel_exploration_scrap13_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the brick with The Tool of Destruction.')
                $ custom1 = "It takes only two hits. You move the broken pieces on the ground, then reach inside the secret compartment. You find a key made of bronze, as large as your forearm. The now-destroyed brick used to be held by some sort of mechanism."
                $ achievement_breakingstuff_points += 1
                $ minutes += 2
                jump oldtunnel_exploration_scrap13_open
            'I bring over the tools I found in the store room and crush the wall.' if oldtunnel_exploration_scrap13_search and oldtunnel_exploration_tools and not oldtunnel_exploration_scrap13_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bring over the tools I found in the store room and crush the wall.')
                $ custom1 = "It takes quite a few hits, but finally you move the broken pieces on the ground, then reach inside the secret compartment. You find a key made of bronze, as large as your forearm. The now-destroyed brick used to be held by some sort of mechanism."
                $ achievement_breakingstuff_points += 1
                $ minutes += 20
                jump oldtunnel_exploration_scrap13_open
            'I lack any tools I could use here. (disabled)' if oldtunnel_exploration_scrap13_search and not oldtunnel_exploration_scrap13_open and not item_magicchisel == 2 and not oldtunnel_exploration_tools:
                pass
            'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                pass
            'I leave the room.' if oldtunnel_exploration_scrap12_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the room.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap12
            'I turn back and go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap15_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn back and go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 19
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 13
                    jump oldtunnel_exploration_scrap15
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 21
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap13_search:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for anything unusual.')
        $ oldtunnel_exploration_scrap13_search = 1
        $ minutes += 3
        menu:
            'The walls to your left and right bear a few iron hooks that could be used to hang cloaks, paintings, or trophies. The corners aren’t too dusty, and there are no footprints on the floor.
            \n\nYou inspect the brick wall further. In its center, at chest height, you spot a distinctive engraving. It’s a winged hourglass, about a finger long.
            '
            'I look for anything unusual.' if not oldtunnel_exploration_scrap13_search:
                jump oldtunnel_exploration_scrap13_search
            'I touch the shape of the hourglass with the pendant I own.' if oldtunnel_exploration_scrap13_search and not oldtunnel_exploration_scrap13_open and item_wingedhourglass:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I touch the shape of the hourglass with the pendant I own.')
                $ custom1 = "It’s a match. You fit it into the grooves, then press. The brick moves deeper inside, then bounces back, allowing you to draw it out completely.\n\nIn the secret compartment you find a key made of bronze. It’s as large as your forearm."
                $ minutes += 1
                jump oldtunnel_exploration_scrap13_open
            'I lack a winged hourglass I could use here. (disabled)' if oldtunnel_exploration_scrap13_search and not oldtunnel_exploration_scrap13_open and not item_wingedhourglass:
                pass
            'I break the brick with The Tool of Destruction.' if oldtunnel_exploration_scrap13_search and item_magicchisel == 2 and not oldtunnel_exploration_scrap13_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the brick with The Tool of Destruction.')
                $ custom1 = "It takes only two hits. You move the broken pieces on the ground, then reach inside the secret compartment. You find a key made of bronze, as large as your forearm. The now-destroyed brick used to be held by some sort of mechanism."
                $ achievement_breakingstuff_points += 1
                $ minutes += 2
                jump oldtunnel_exploration_scrap13_open
            'I bring over the tools I found in the store room and crush the wall.' if oldtunnel_exploration_scrap13_search and oldtunnel_exploration_tools and not oldtunnel_exploration_scrap13_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bring over the tools I found in the store room and crush the wall.')
                $ custom1 = "It takes quite a few hits, but finally you move the broken pieces on the ground, then reach inside the secret compartment. You find a key made of bronze, as large as your forearm. The now-destroyed brick used to be held by some sort of mechanism."
                $ achievement_breakingstuff_points += 1
                $ minutes += 20
                jump oldtunnel_exploration_scrap13_open
            'I lack any tools I could use here. (disabled)' if oldtunnel_exploration_scrap13_search and not oldtunnel_exploration_scrap13_open and not item_magicchisel == 2 and not oldtunnel_exploration_tools:
                pass
            'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                pass
            'I leave the room.' if oldtunnel_exploration_scrap12_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the room.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap12
            'I turn back and go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap15_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn back and go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 19
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 13
                    jump oldtunnel_exploration_scrap15
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 21
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap13_open:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I touch the shape of the hourglass with the pendant I own.')
        $ oldtunnel_exploration_scrap13_open = 1
        $ item_oldtunnelkey = 1
        $ renpy.notify("You pick up a massive bronze key.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You pick up a massive bronze key.{/i}')
        menu:
            '[custom1]
            '
            'I look for anything unusual.' if not oldtunnel_exploration_scrap13_search:
                jump oldtunnel_exploration_scrap13_search
            'I touch the shape of the hourglass with the pendant I own.' if oldtunnel_exploration_scrap13_search and not oldtunnel_exploration_scrap13_open and item_wingedhourglass:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I touch the shape of the hourglass with the pendant I own.')
                $ custom1 = "It’s a match. You fit it into the grooves, then press. The brick moves deeper inside, then bounces back, allowing you to draw it out completely.\n\nIn the secret compartment you find a key made of bronze. It’s as large as your forearm."
                $ minutes += 1
                jump oldtunnel_exploration_scrap13_open
            'I lack a winged hourglass I could use here. (disabled)' if oldtunnel_exploration_scrap13_search and not oldtunnel_exploration_scrap13_open and not item_wingedhourglass:
                pass
            'I break the brick with The Tool of Destruction.' if oldtunnel_exploration_scrap13_search and item_magicchisel == 2 and not oldtunnel_exploration_scrap13_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I break the brick with The Tool of Destruction.')
                $ custom1 = "It takes only two hits. You move the broken pieces on the ground, then reach inside the secret compartment. You find a key made of bronze, as large as your forearm. The now-destroyed brick used to be held by some sort of mechanism."
                $ achievement_breakingstuff_points += 1
                $ minutes += 2
                jump oldtunnel_exploration_scrap13_open
            'I bring over the tools I found in the store room and crush the wall.' if oldtunnel_exploration_scrap13_search and oldtunnel_exploration_tools and not oldtunnel_exploration_scrap13_open:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bring over the tools I found in the store room and crush the wall.')
                $ custom1 = "It takes quite a few hits, but finally you move the broken pieces on the ground, then reach inside the secret compartment. You find a key made of bronze, as large as your forearm. The now-destroyed brick used to be held by some sort of mechanism."
                $ achievement_breakingstuff_points += 1
                $ minutes += 20
                jump oldtunnel_exploration_scrap13_open
            'I lack any tools I could use here. (disabled)' if oldtunnel_exploration_scrap13_search and not oldtunnel_exploration_scrap13_open and not item_magicchisel == 2 and not oldtunnel_exploration_tools:
                pass
            'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                pass
            'I leave the room.' if oldtunnel_exploration_scrap12_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the room.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap12
            'I turn back and go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap15_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn back and go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 19
                    jump oldtunnel_exploration_scrap19
                if oldtunnel_exploration_scrap15_firsttime:
                    $ minutes += 13
                    jump oldtunnel_exploration_scrap15
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 21
                jump oldtunnelafterinteraction01

label oldtunnel_exploration_scrap14ALL: # ropehook
    label oldtunnel_exploration_scrap14: # stalaktyty
        $ oldtunnel_exploration_position = 14
        if not oldtunnel_exploration_combat:
            if not oldtunnel_exploration_scrap14_firsttime:
                $ oldtunnel_exploration_scrap14_firsttime = 1
                $ custom1 = "The cave is so moist that the diggers placed planks on the ground, serving as a now-useless bridge through the puddles. The rocks shaped like icicles ominously hang from the ceiling, in some spots merging with their on-the-floor counterparts and forming hourglass-like columns."
                $ custom2 = ""
            else:
                $ custom1 = "The droplets hit the ground and the teeth-like stalagmites."
                if oldtunnel_exploration_scrap14_trap == "whip" and not oldtunnel_inside_undead_defeated:
                    $ custom2 = " Your whip trap is still here."
                elif oldtunnel_exploration_scrap14_trap == "foothold" and not oldtunnel_inside_undead_defeated:
                    $ custom2 = " Your foothold trap is still here."
                else:
                    $ custom2 = ""
            if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside02.ogg":
                play nature "audio/ambient/oldtunnelinside02.ogg" fadeout 2.0 fadein 2.0 volume 1.0
            menu:
                '[custom1][custom2]
                '
                'I search the chamber.' if not oldtunnel_exploration_scrap14_search:
                    jump oldtunnel_exploration_scrap14_search
                'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap14_trap:
                    jump oldtunnel_exploration_scrap14_trap
                'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap14_trap:
                    pass
                'I try to open the door.' if not oldtunnel_exploration_scrap15_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to open the door.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap15
                'I enter the main tunnel.' if oldtunnel_exploration_scrap15_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the main tunnel.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap15
                'I move back to the dining room.' if oldtunnel_exploration_scrap11_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move back to the dining room.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap11
                'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap19_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                    if oldtunnel_exploration_scrap19_firsttime:
                        $ minutes += 13
                        jump oldtunnel_exploration_scrap19
                'I go back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                    $ minutes += 21
                    jump oldtunnelafterinteraction01
        else:
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            $ at = 0
            if oldtunnel_exploration_scrap14_trap == "foothold":
                $ custom1 = "You jump over the foothold traps awkwardly, but the undead don’t realize what’s happening. After one of them sinks into the hollowed plank, the others come to a halt, helping it get out. It’s your opportunity to act."
                if pc_class == "mage" and mana >= manacost:
                    $ at_unlock_spell = 1
            elif oldtunnel_exploration_scrap14_trap == "whip":
                $ custom1 = "While the undead does stumble upon the cord, the stalagmite can’t hold the force put on it by your whip trap. It shatters, making the branch splatter the water around."
            else:
                $ custom1 = "The water splatters beneath your boots."
            menu:
                '[custom1]
                '
                'I reload my crossbow.' if oldtunnel_exploration_scrap14_trap == "foothold" and item_crossbow and item_crossbowquarrels and not oldtunnel_exploration_crossbow_ready:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reload my crossbow.')
                    $ oldtunnel_exploration_crossbow_ready = 1
                    $ at_unlock_spell = 0
                    $ at = 0
                    menu:
                        'You put all your strength into it, getting it done before the undead reach you.
                        '
                        'I run to the dining chamber.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                            $ minutes += 2
                            jump oldtunnel_exploration_scrap11
                'It can’t dodge a shot from my crossbow now.' if oldtunnel_exploration_scrap14_trap == "foothold" and oldtunnel_exploration_crossbow_ready:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It can’t dodge a shot from my crossbow now.')
                    $ oldtunnel_exploration_crossbow_ready = 0
                    $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                    $ at_unlock_spell = 0
                    $ at = 0
                    menu:
                        'Where do you aim?
                        '
                        'The stalactite above it.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stalactite above it.')
                            $ item_crossbowquarrels -= 1
                            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            $ oldtunnel_inside_undead_hp -= 5
                            if oldtunnel_inside_undead_hp_old != oldtunnel_inside_undead_hp:
                                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                                    $ oldtunnel_inside_undead_amount = 3
                                    $ custom2 = "Its loose bones scatter over the soggy planks."
                                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                                    $ oldtunnel_inside_undead_amount = 2
                                    $ custom2 = "It hits the wet ground silently and moves no longer."
                                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                                    $ oldtunnel_inside_undead_amount = 1
                                    $ custom2 = "It lets out a quiet moan as it crumbles. There’s only one creature left."
                                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                                    $ oldtunnel_inside_undead_amount_0_description = 1
                                    $ custom2 = "Somehow, it still shuffles forward, giving you an empty, yet hungry look."
                                else:
                                    $ custom2 = "Somehow, it still shuffles forward, giving you an empty, yet hungry look."
                            menu:
                                'The undead has no time to escape - the massive spike pierces its skull and reaches the thorax. [custom2]
                                '
                                '{image=d6} I’m ready to face the undead.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                                    jump oldtunnel_combat_lastclash
                                'I run to the dining chamber.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                                    $ minutes += 2
                                    jump oldtunnel_exploration_scrap11
                        'The head.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The head.')
                            $ item_crossbowquarrels -= 1
                            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            $ oldtunnel_inside_undead_hp -= 4
                            if oldtunnel_inside_undead_hp_old != oldtunnel_inside_undead_hp:
                                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                                    $ oldtunnel_inside_undead_amount = 3
                                    $ custom2 = ". The loose bones of the first undead scatter over the soggy planks."
                                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                                    $ oldtunnel_inside_undead_amount = 2
                                    $ custom2 = ". The second undead hits the wet ground silently."
                                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                                    $ oldtunnel_inside_undead_amount = 1
                                    $ custom2 = ". The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
                                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                                    $ oldtunnel_inside_undead_amount_0_description = 1
                                    $ custom2 = ". After a few moments, the last undead shuffles forward, giving you an empty, yet somehow hungry look."
                                else:
                                    $ custom2 = ", and while the undead leans away for a few moments, it doesn’t take long for it to straighten up again."
                            menu:
                                'The quarrel pierces through the forehead and stays inside the skull[custom2]
                                '
                                '{image=d6} I’m ready to face the undead.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                                    jump oldtunnel_combat_lastclash
                                'I run to the dining chamber.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                                    $ minutes += 2
                                    jump oldtunnel_exploration_scrap11
                        'The chest.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The chest.')
                            $ item_crossbowquarrels -= 1
                            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            menu:
                                'The quarrel grazes a rib, then disappears into the darkness. The undead follows it with its empty gaze, then looks back at you.
                                '
                                '{image=d6} I’m ready to face the undead.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                                    jump oldtunnel_combat_lastclash
                                'I run to the dining chamber.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                                    $ minutes += 2
                                    jump oldtunnel_exploration_scrap11
                        'A leg.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- A leg')
                            $ item_crossbowquarrels -= 1
                            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                            $ oldtunnel_inside_undead_hp -= 2
                            if oldtunnel_inside_undead_hp_old != oldtunnel_inside_undead_hp:
                                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                                    $ oldtunnel_inside_undead_amount = 3
                                    $ custom2 = "The quarrel shatters it completely. The loose bones of the first undead scatter over the soggy planks."
                                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                                    $ oldtunnel_inside_undead_amount = 2
                                    $ custom2 = "The quarrel shatters it completely. The second undead hits the wet planks silently."
                                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                                    $ oldtunnel_inside_undead_amount = 1
                                    $ custom2 = "The quarrel shatters it completely. The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
                                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                                    $ oldtunnel_inside_undead_amount_0_description = 1
                                    $ custom2 = "The quarrel breaks the leg, but the undead is still standing. After a few moments it shuffles forward, giving you an empty, yet somehow hungry look."
                                else:
                                    $ custom2 = "Even though the quarrel grazes the bone and makes your target stagger, the undead regains its composure quickly."
                            menu:
                                '[custom2]
                                '
                                '{image=d6} I’m ready to face the undead.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                                    jump oldtunnel_combat_lastclash
                                'I run to the dining chamber.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                                    $ minutes += 2
                                    jump oldtunnel_exploration_scrap11
                'It can’t dodge my spell now. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="oldtunnel_exploration_scrap14_trap == 'foothold' and at == 'spell'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It can’t dodge my spell now.')
                    $ mana = limit_mana(mana-manacost)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                    $ at_unlock_spell = 0
                    $ at = 0
                    $ oldtunnel_inside_undead_hp -= 4
                    if oldtunnel_inside_undead_hp_old != oldtunnel_inside_undead_hp:
                        $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                        if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                            $ oldtunnel_inside_undead_amount = 3
                            $ custom2 = "They scatter over the pond - the first undead is no more."
                        elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                            $ oldtunnel_inside_undead_amount = 2
                            $ custom2 = "The second undead sinks into the water silently."
                        elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                            $ oldtunnel_inside_undead_amount = 1
                            $ custom2 = "The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
                        elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                            $ oldtunnel_inside_undead_amount_0_description = 1
                            $ custom2 = "The last undead leans away for a few moments, and after it straightens up again, it lacks its ribs."
                        else:
                            $ custom2 = "The undead leans away for a few moments, and after it straightens up again, it lacks its ribs."
                    menu:
                        'You reach for the willow wand and dash forward, casting the pneuma with a single swipe. It feels like stabbing the air with a wooden dagger.
                        \n\nThe invisible wave doesn’t spare the revealed bones. [custom2]
                        '
                        '{image=d6} I’m ready to face the undead.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                            jump oldtunnel_combat_lastclash
                        'I run to the dining chamber.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                            $ minutes += 2
                            jump oldtunnel_exploration_scrap11
                '{image=d6} I reach for my wand.' ( condition="oldtunnel_exploration_scrap14_trap != 'foothold' and oldtunnel_exploration_crossbow_ready and pc_class == 'mage' and mana >= manacost" ):
                    $ at_unlock_spell = 0
                    $ at = 0
                    jump oldtunnel_combat_spell
                '{image=d6} I raise my crossbow.' if oldtunnel_exploration_scrap14_trap != "foothold" and oldtunnel_exploration_crossbow_ready:
                    $ at_unlock_spell = 0
                    $ at = 0
                    jump oldtunnel_combat_crossbow
                '{image=d6} I’m ready to face the undead.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                    $ at_unlock_spell = 0
                    $ at = 0
                    jump oldtunnel_combat_lastclash
                'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                    pass
                'I run to the dining chamber.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                    $ at_unlock_spell = 0
                    $ at = 0
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap11

    label oldtunnel_exploration_scrap14_search:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the chamber.')
        $ oldtunnel_exploration_scrap14_search = 1
        $ minutes += 10
        menu:
            'You leave the rotten planks and explore the cavern carefully, making the light dance on the droplets and puddles, but you find nothing of use or value.
            '
            'I search the chamber.' if not oldtunnel_exploration_scrap14_search:
                jump oldtunnel_exploration_scrap14_search
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap14_trap:
                jump oldtunnel_exploration_scrap14_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap14_trap:
                pass
            'I try to open the door.' if not oldtunnel_exploration_scrap15_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to open the door.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap15
            'I enter the main tunnel.' if oldtunnel_exploration_scrap15_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the main tunnel.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap15
            'I move back to the dining room.' if oldtunnel_exploration_scrap11_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move back to the dining room.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap11
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap19_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 13
                    jump oldtunnel_exploration_scrap19
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 21
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap14_trap:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider putting a trap here.')
        menu:
            'You look around.
            '
            'I lack the knowledge to build complex traps. (disabled)' if not oldtunnel_exploration_knowledge:
                pass
            'I could make a few foothold traps to slow down the undead.' if oldtunnel_exploration_knowledge and oldtunnel_exploration_trap_availability_foothold:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could make a few foothold traps to slow down the undead.')
                if oldtunnel_exploration_wood:
                    $ custom1 = "Since you already know where to find some decent wood, you can get this done in just a few minutes."
                else:
                    $ custom1 = "Since you need to bring wood from the outside and split it by yourself, it will take you almost an hour."
                menu:
                    'It would be easy to carve holes in the soggy planks and surround them with sticks. It should be enough to catch one’s foot, even if only for a few breaths.
                    \n\n[custom1]
                    '
                    'Let’s get to it.' ( condition="pc_hp >= 1" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        $ oldtunnel_exploration_scrap14_trap = "foothold"
                        $ oldtunnel_exploration_trap_availability_foothold -= 1
                        if oldtunnel_exploration_wood:
                            $ quarters += 1
                        else:
                            $ quarters += 3
                        $ custom1 = "Once you’re done, you observe the traps carefully. Even in strong light, they’re barely visible."
                        jump oldtunnel_exploration_scrap14_trap2
                    'I’m too tired to safely build a trap. (Required vitality: 1) (disabled)' ( condition="pc_hp <= 0" ):
                        pass
                    'I think about another trap.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about another trap.')
                        jump oldtunnel_exploration_scrap14_trap
                    'Forget it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                        $ custom1 = "You feel the gentle movement of humid air."
                        jump oldtunnel_exploration_scrap14_trap2
            'I could tie the monster claws to a branch and construct a whip trap.' if oldtunnel_exploration_knowledge and oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_wood and oldtunnel_exploration_bones:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could tie the monster claws to a branch and construct a whip trap.')
                if oldtunnel_exploration_tools:
                    $ custom1 = "Thanks to the tools you found, it won’t take more than half an hour."
                else:
                    $ custom1 = "Since you lack proper tools, it will take you about an hour."
                if oldtunnel_exploration_trap_availability_whip == 2:
                    $ custom2 = "You have enough claws, cords, and wood to build 2 whip traps in the entire tunnel."
                else:
                    $ custom2 = "You have enough supplies to build 1 more whip trap in the entire tunnel."
                menu:
                    'You could attach the bent branch to one of the stalagmites, giving it some decent camouflage, though the rocks here are rather brittle.
                    \n\n[custom1]
                    \n\n[custom2]
                    '
                    'Let’s get to it.' ( condition="pc_hp >= 2" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        $ oldtunnel_exploration_scrap14_trap = "whip"
                        $ oldtunnel_exploration_trap_availability_whip -= 1
                        if oldtunnel_exploration_tools:
                            $ quarters += 2
                        else:
                            $ quarters += 4
                        $ custom1 = "Once you’re done, you take a long look at the triggering cord. Getting hit with the monstrous claws could kill you on the spot."
                        jump oldtunnel_exploration_scrap14_trap2
                    'I’m too tired to safely build a trap. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1" ):
                        pass
                    'I think about another trap.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think about another trap.')
                        jump oldtunnel_exploration_scrap14_trap
                    'Forget it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                        $ custom1 = "You feel the gentle movement of humid air."
                        jump oldtunnel_exploration_scrap14_trap2
            'Unless I find some decent wood around here I won’t be able to build anything. (disabled)' if oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_knowledge and not oldtunnel_exploration_wood:
                pass
            'I lack sharp spikes that could help me place a more damaging trap. (disabled)' if oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_knowledge and not oldtunnel_exploration_bones:
                pass
            'I won’t find enough supplies to build another whip trap. (disabled)' if not oldtunnel_exploration_trap_availability_whip:
                pass
            'Forget it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                $ custom1 = "You feel the gentle movement of humid air."
                jump oldtunnel_exploration_scrap14_trap2

    label oldtunnel_exploration_scrap14_trap2:
        menu:
            '[custom1]
            '
            'I search the chamber.' if not oldtunnel_exploration_scrap14_search:
                jump oldtunnel_exploration_scrap14_search
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap14_trap:
                jump oldtunnel_exploration_scrap14_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap14_trap:
                pass
            'I try to open the door.' if not oldtunnel_exploration_scrap15_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to open the door.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap15
            'I enter the main tunnel.' if oldtunnel_exploration_scrap15_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the main tunnel.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap15
            'I move back to the dining room.' if oldtunnel_exploration_scrap11_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move back to the dining room.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap11
            'I go as deep into the tunnel as I can.' if oldtunnel_exploration_scrap19_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go as deep into the tunnel as I can.')
                if oldtunnel_exploration_scrap19_firsttime:
                    $ minutes += 13
                    jump oldtunnel_exploration_scrap19
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 21
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap14_midcombat_afterinteraction:
        menu:
            '[custom1][custom2]
            '
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I run to the dining chamber.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap11

    label oldtunnel_exploration_scrap14_midcombat_nothing:
        menu:
            'The undead are getting closer.
            '
            '{image=d6} I reach for my wand.' ( condition="oldtunnel_exploration_scrap14_trap != 'foothold' and oldtunnel_exploration_crossbow_ready and pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_scrap14_trap != "foothold" and oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'I run to the dining chamber.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run up the tunnel.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap11

label oldtunnel_exploration_scrap15ALL:
    label oldtunnel_exploration_scrap15: # wyjście z części ludzkiej
        $ oldtunnel_exploration_position = 15
        if not oldtunnel_exploration_combat:
            if not oldtunnel_exploration_scrap15_firsttime:
                $ oldtunnel_exploration_scrap15_firsttime = 1
                $ custom1 = "The door opens quietly and you return to the main tunnel. You could turn south again and see if there’s anything you missed, but after you blink a few times, you realize there’s a light at the opposite end of the tunnel, far ahead - it’s weak and flickers, like a torch."
                $ custom2 = ""
            else:
                if not oldtunnel_inside_undead_defeated:
                    if oldtunnel_exploration_scrap16_firsttime:
                        $ custom1 = "You can still see the light flickering at the end of the tunnel."
                    else:
                        $ custom1 = "You can still see the light flickering at the end of the tunnel. You could also go south to make sure you haven’t missed anything."
                    $ custom2 = ""
                elif oldtunnel_inside_opened:
                    if oldtunnel_exploration_scrap16_firsttime:
                        $ custom1 = "The open gate lets in the light at the end of the tunnel."
                    else:
                        $ custom1 = "The open gate lets in the light at the end of the tunnel. You could go south to make sure you haven’t missed anything."
                    $ custom2 = ""
                else:
                    if oldtunnel_exploration_scrap16_firsttime:
                        $ custom1 = "The dark crossroads are quiet and humid."
                    else:
                        $ custom1 = "The dark crossroads are quiet and humid. You could also go south to make sure you haven’t missed anything."
                    $ custom2 = ""
                if oldtunnel_exploration_scrap15_trap and not oldtunnel_inside_undead_defeated:
                    $ custom2 = " Your whip trap is still here."
                else:
                    $ custom2 = ""
            if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside07.ogg":
                play nature "audio/ambient/oldtunnelinside07.ogg" fadeout 2.0 fadein 2.0 volume 1.0
            menu:
                '[custom1][custom2]
                '
                'I move closer to the light.' if not oldtunnel_exploration_scrap18_firsttime and not oldtunnel_inside_undead_defeated:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move closer to the light.')
                    jump oldtunnel_exploration_scrap18
                'I follow the long tunnel north.' if not oldtunnel_exploration_scrap18_firsttime and oldtunnel_inside_undead_defeated:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the long tunnel north.')
                    jump oldtunnel_exploration_scrap18
                'I hide my own light.' if not oldtunnel_exploration_scrap15_hidelight and not oldtunnel_inside_undead_defeated:
                    jump oldtunnel_exploration_scrap15_hidelight
                'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap15_trap:
                    jump oldtunnel_exploration_scrap15_trap
                'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap15_trap:
                    pass
                'I head south, in the direction I came from.' if not oldtunnel_exploration_scrap16_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head south, in the direction I came from.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap16
                'I follow the long tunnel north.' if oldtunnel_exploration_scrap18_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the long tunnel north.')
                    jump oldtunnel_exploration_scrap18
                'I head toward the cave-in.' if oldtunnel_exploration_scrap16_firsttime:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the cave-in.')
                    $ minutes += 3
                    jump oldtunnel_exploration_scrap16
                'I head back to the cave with stalactites.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the cave with stalactites.')
                    $ minutes += 2
                    jump oldtunnel_exploration_scrap14
                'I go back to {color=#f6d6bd}[horsename]{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                    $ minutes += 23
                    jump oldtunnelafterinteraction01
        else:
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            if oldtunnel_exploration_scrap15_trap == "whip":
                $ custom1 = "You jump over the cord stretched above the floor, but after one of the undead triggers it, it gets hit only with the tip of the branch, not too forcefully. "
                $ oldtunnel_inside_undead_hp -= 1
            else:
                $ custom1 = "You run with confidence, making sure you have your equipment at hand."
            if oldtunnel_inside_undead_hp_old != oldtunnel_inside_undead_hp:
                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                    $ oldtunnel_inside_undead_amount = 3
                    $ custom2 = "Still, it’s enough. The loose bones of the first undead scatter over the floor."
                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                    $ oldtunnel_inside_undead_amount = 2
                    $ custom2 = "Still, it’s enough. Having no more ribs, the second undead falls on the floor silently."
                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                    $ oldtunnel_inside_undead_amount = 1
                    $ custom2 = "Still, it’s enough. The third undead lets out a quiet moan as it turns into a pile of bones. There’s only one creature left."
                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                    $ oldtunnel_inside_undead_amount_0_description = 1
                    $ custom2 = "Still, it’s almost enough. After a few moments, the last undead shuffles forward, giving you an empty, yet somehow hungry look."
                else:
                    $ custom2 = "You glance behind and while the creature needs to get back on its feet, it’s still going."
            else:
                $ custom2 = ""
            menu:
                '[custom1][custom2]
                '
                'I run to the chamber with stalactites.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to the chamber with stalactites.')
                    $ minutes += 1
                    jump oldtunnel_exploration_scrap14
                '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                    jump oldtunnel_combat_spell
                '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                    jump oldtunnel_combat_crossbow
                '{image=d6} I’m ready to face the undead.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                    jump oldtunnel_combat_lastclash
                'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                    pass
                'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                    pass

    label oldtunnel_exploration_scrap15_hidelight:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I hide my own light.')
        $ oldtunnel_exploration_scrap15_hidelight = 1
        menu:
            'You simply put it on the ground, in the entrance to the cavern with the stalactites. You’ll pick it up if you need it.
            '
            'I move closer to the light.' if not oldtunnel_exploration_scrap18_firsttime and not oldtunnel_inside_undead_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move closer to the light.')
                jump oldtunnel_exploration_scrap18
            'I follow the long tunnel north.' if not oldtunnel_exploration_scrap18_firsttime and oldtunnel_inside_undead_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the long tunnel north.')
                jump oldtunnel_exploration_scrap18
            'I hide my own light.' if not oldtunnel_exploration_scrap15_hidelight and not oldtunnel_inside_undead_defeated:
                jump oldtunnel_exploration_scrap15_hidelight
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap15_trap:
                jump oldtunnel_exploration_scrap15_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap15_trap:
                pass
            'I head south, in the direction I came from.' if not oldtunnel_exploration_scrap16_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head south, in the direction I came from.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap16
            'I follow the long tunnel north.' if oldtunnel_exploration_scrap18_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the long tunnel north.')
                jump oldtunnel_exploration_scrap18
            'I head toward the cave-in.' if oldtunnel_exploration_scrap16_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the cave-in.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap16
            'I head back to the cave with stalactites.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the cave with stalactites.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap14
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 23
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap15_trap:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider putting a trap here.')
        menu:
            'Being so close to the undead may alert them with noises. To place a trap here you have to be quiet and careful.
            '
            'I lack the knowledge to build complex traps. (disabled)' if not oldtunnel_exploration_knowledge:
                pass
            'Unless I find some decent wood around here I won’t be able to build anything. (disabled)' if oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_knowledge and not oldtunnel_exploration_wood:
                pass
            'I could tie the monster claws to a branch and construct a whip trap.' if oldtunnel_exploration_knowledge and oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_wood and oldtunnel_exploration_bones:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could tie the monster claws to a branch and construct a whip trap.')
                if oldtunnel_exploration_tools:
                    $ custom1 = "You need to be careful, but thanks to the tools you found, it will take less than an hour."
                else:
                    $ custom1 = "Since you lack proper tools and you have to be careful, it will take you more than an hour."
                if oldtunnel_exploration_trap_availability_whip == 2:
                    $ custom2 = "You have enough claws, cords, and wood to build 2 whip traps in the entire tunnel."
                else:
                    $ custom2 = "You have enough supplies to build 1 more whip trap in the entire tunnel."
                menu:
                    'You could hide the bent branch behind one of the supporting beams, though it won’t be easy to camouflage the triggering cord in darkness.
                    \n\n[custom1]
                    \n\n[custom2]
                    '
                    'Let’s get to it.' ( condition="pc_hp >= 2" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get to it.')
                        $ oldtunnel_exploration_scrap15_trap = "whip"
                        $ oldtunnel_exploration_trap_availability_whip -= 1
                        if oldtunnel_exploration_tools:
                            $ quarters += 3
                        else:
                            $ quarters += 5
                        $ custom1 = "Once you’re done, you take a long look at the triggering cord. Getting hit with the monstrous claws could kill you on the spot."
                        jump oldtunnel_exploration_scrap15_trap2
                    'I’m too tired to safely build a trap. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1" ):
                        pass
                    'Forget it.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                        $ custom1 = "You feel the gentle movement of humid air."
                        jump oldtunnel_exploration_scrap15_trap2
            'I lack sharp spikes that could help me place a more damaging trap. (disabled)' if oldtunnel_exploration_trap_availability_whip and oldtunnel_exploration_knowledge and not oldtunnel_exploration_bones:
                pass
            'I won’t find enough supplies to build another whip trap. (disabled)' if not oldtunnel_exploration_trap_availability_whip:
                pass
            'Forget it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Forget it.')
                $ custom1 = "You feel the gentle movement of humid air."
                jump oldtunnel_exploration_scrap15_trap2

    label oldtunnel_exploration_scrap15_trap2:
        menu:
            '[custom1]
            '
            'I move closer to the light.' if not oldtunnel_exploration_scrap18_firsttime and not oldtunnel_inside_undead_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I move closer to the light.')
                jump oldtunnel_exploration_scrap18
            'I follow the long tunnel north.' if not oldtunnel_exploration_scrap18_firsttime and oldtunnel_inside_undead_defeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the long tunnel north.')
                jump oldtunnel_exploration_scrap18
            'I hide my own light.' if not oldtunnel_exploration_scrap15_hidelight and not oldtunnel_inside_undead_defeated:
                jump oldtunnel_exploration_scrap15_hidelight
            'I consider putting a trap here.' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap15_trap:
                jump oldtunnel_exploration_scrap15_trap
            'I already set a trap here. (disabled)' if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap15_trap:
                pass
            'I head south, in the direction I came from.' if not oldtunnel_exploration_scrap16_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head south, in the direction I came from.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap16
            'I follow the long tunnel north.' if oldtunnel_exploration_scrap18_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the long tunnel north.')
                jump oldtunnel_exploration_scrap18
            'I head toward the cave-in.' if oldtunnel_exploration_scrap16_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the cave-in.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap16
            'I head back to the cave with stalactites.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head back to the cave with stalactites.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap14
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 23
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap15_midcombat_afterinteraction:
        menu:
            '[custom1][custom2]
            '
            'I run to the chamber with stalactites.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to the chamber with stalactites.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap14
            '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass

    label oldtunnel_exploration_scrap15_midcombat_nothing:
        menu:
            'The undead are getting closer.
            '
            'I run to the chamber with stalactites.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to the chamber with stalactites.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap14
            '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass

label oldtunnel_exploration_scrap16ALL:
    label oldtunnel_exploration_scrap16: # druga strona blokady, wejście do magazynu
        $ oldtunnel_exploration_position = 16
        if not oldtunnel_exploration_scrap16_firsttime:
            $ oldtunnel_exploration_scrap16_firsttime = 1
            $ custom1 = "You reach the other side of the cave-in, getting a good view at its size. You find a new door here - it’s a bit tilted, closed, and soggy."
        else:
            $ custom1 = "You reach the door."
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside07.ogg":
            play nature "audio/ambient/oldtunnelinside07.ogg" fadeout 2.0 fadein 2.0 volume 1.0
        menu:
            '[custom1]
            '
            'I try to open the door.' if not oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime:
                jump oldtunnel_exploration_scrap16_search
            'I don’t have a matching key. (disabled)' if not item_oldtunnesmallkey and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime:
                pass
            'I try the key I found in the dining chamber.' if item_oldtunnesmallkey and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try the key I found in the dining chamber.')
                $ minutes += 2
                $ custom1 = "After a bit of wiggling, the padlock gives in. The door lets out a sigh and you enter a humble cave that’s been turned into a store room. Your light reveals crates, a pile of timber, a stack of rocks, and another of bricks."
                jump oldtunnel_exploration_scrap17
            'It’s nothing that The Tool of Destruction can’t handle.' if item_magicchisel == 2 and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s nothing that The Tool of Destruction can’t handle.')
                $ minutes += 5
                $ custom1 = "The padlock breaks after two hits, taking with it the entire hasp. The door lets out a sigh and you enter a humble cave that’s been turned into a store room. Your light reveals crates, a pile of timber, a stack of rocks, and another of bricks."
                $ achievement_breakingstuff_points += 1
                jump oldtunnel_exploration_scrap17
            'I’m too weak to destroy the door. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1 and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime" ):
                pass
            'I take my axe and break through.' ( condition="pc_hp >= 2 and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime and not oldtunnel_inside_undead_defeated" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take my axe and break through.')
                $ achievement_breakingstuff_points += 1
                $ quarters += 1
                jump oldtunnel_exploration_scrap17opencombat
            'I take my axe and break through.' ( condition="pc_hp >= 2 and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime and oldtunnel_inside_undead_defeated" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take my axe and break through.')
                $ achievement_breakingstuff_points += 1
                $ quarters += 1
                $ custom1 = "You need a few good swings before you break away the hasp, but it finally lands on the ground with a loud clang. The door lets out a sigh and you enter a humble cave that’s been turned into a store room. Your light reveals crates, a pile of timber, a stack of rocks, and another of bricks."
                jump oldtunnel_exploration_scrap17
            'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                pass
            'I enter the store room.' if oldtunnel_exploration_scrap17_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the store room.')
                $ minutes += 1
                $ custom1 = "The crates weren’t touched since your last visit."
                jump oldtunnel_exploration_scrap17
            'I return to the crossroads.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the crossroads.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap15
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 26
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap16_search:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to open the door.')
        $ oldtunnel_exploration_scrap16_search = 1
        $ minutes += 1
        menu:
            'The small, iron padlock won’t budge.
            '
            'I try to open the door.' if not oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime:
                jump oldtunnel_exploration_scrap16_search
            'I don’t have a matching key. (disabled)' if not item_oldtunnesmallkey and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime:
                pass
            'I try the key I found in the dining chamber.' if item_oldtunnesmallkey and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try the key I found in the dining chamber.')
                $ minutes += 2
                $ custom1 = "After a bit of wiggling, the padlock gives in. The door lets out a sigh and you enter a humble cave that’s been turned into a store room. Your light reveals crates, a pile of timber, a stack of rocks, and another of bricks."
                jump oldtunnel_exploration_scrap17
            'It’s nothing that The Tool of Destruction can’t handle.' if item_magicchisel == 2 and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s nothing that The Tool of Destruction can’t handle.')
                $ achievement_breakingstuff_points += 1
                $ minutes += 5
                $ custom1 = "The padlock breaks after two hits, taking with it the entire hasp. The door lets out a sigh and you enter a humble cave that’s been turned into a store room. Your light reveals crates, a pile of timber, a stack of rocks, and another of bricks."
                jump oldtunnel_exploration_scrap17
            'I’m too weak to destroy the door. (Required vitality: 2) (disabled)' ( condition="pc_hp <= 1 and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime" ):
                pass
            'I take my axe and break through.' ( condition="pc_hp >= 2 and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime and not oldtunnel_inside_undead_defeated" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take my axe and break through.')
                $ achievement_breakingstuff_points += 1
                $ quarters += 1
                jump oldtunnel_exploration_scrap17opencombat
            'I take my axe and break through.' ( condition="pc_hp >= 2 and oldtunnel_exploration_scrap16_search and not oldtunnel_exploration_scrap17_firsttime and oldtunnel_inside_undead_defeated" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take my axe and break through.')
                $ achievement_breakingstuff_points += 1
                $ quarters += 1
                $ custom1 = "You need a few good swings before you break away the hasp, but it finally lands on the ground with a loud clang. The door lets out a sigh and you enter a humble cave that’s been turned into a store room. Your light reveals crates, a pile of timber, a stack of rocks, and another of bricks."
                jump oldtunnel_exploration_scrap17
            'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                pass
            'I enter the store room.' if oldtunnel_exploration_scrap17_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the store room.')
                $ minutes += 1
                $ custom1 = "The crates weren’t touched since your last visit."
                jump oldtunnel_exploration_scrap17
            'I return to the crossroads.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the crossroads.')
                $ minutes += 3
                jump oldtunnel_exploration_scrap15
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 26
                jump oldtunnelafterinteraction01

label oldtunnel_exploration_scrap17ALL:
    label oldtunnel_exploration_scrap17: # magazyn
        $ oldtunnel_exploration_position = 17
        if not oldtunnel_exploration_scrap17_firsttime:
            $ oldtunnel_exploration_scrap17_firsttime = 1
        else:
            $ custom1 = "The chamber is quiet, and not as humid as the rest of the tunnel."
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside07.ogg":
            play nature "audio/ambient/oldtunnelinside07.ogg" fadeout 2.0 fadein 2.0 volume 1.0
        menu:
            '[custom1]
            '
            'I search the chamber.' if not oldtunnel_exploration_scrap17_search:
                jump oldtunnel_exploration_scrap17_search
            'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                pass
            'I walk outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk outside.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap16
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 26
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap17_search:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the chamber.')
        $ oldtunnel_exploration_scrap17_search = 1
        $ oldtunnel_exploration_tools = 1
        $ oldtunnel_exploration_wood += 1
        $ minutes += 5
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside03.ogg":
            play nature "audio/ambient/oldtunnelinside03.ogg" fadeout 2.0 fadein 2.0 volume 1.0
        menu:
            'You move the building materials aside, taking note of the somewhat dry timber, but the first thing of use you find are the tools stored in one of the crates. The crude axes, hammers, chisels, pickaxes, and digging bars are all old and made of rocks, antlers, and bones. Though they’re worthless, you move a few of them closer to the tunnel. If necessary, you’ll know where to find them.
            '
            'I search the chamber.' if not oldtunnel_exploration_scrap17_search:
                jump oldtunnel_exploration_scrap17_search
            'I can’t set a trap here. (disabled)' if oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_defeated:
                pass
            'I walk outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk outside.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap16
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 26
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap17opencombat:
        $ oldtunnel_exploration_position = 17
        $ oldtunnel_exploration_scrap17_firsttime = 1
        menu:
            'You need a few good swings before you break away the hasp, but it finally lands on the ground with a loud clang. The door lets out a sigh and you enter a humble cave that’s been turned into a store room. Your light reveals crates, a pile of timber, a stack of rocks, and another of bricks.
            \n\nYou suddenly hear steps coming from the main tunnel, far ahead. The light draws near.
            '
            'I run back to the crossroads before I’m cornered.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run back to the crossroads before I’m cornered.')
                jump oldtunnel_exploration_scrap15combat_afterlock

label oldtunnel_exploration_scrap18ALL:
    label oldtunnel_exploration_scrap18: # korytarz do wyjścia
        $ oldtunnel_exploration_position = 18
        if not oldtunnel_exploration_scrap18_firsttime:
            $ oldtunnel_exploration_scrap18_firsttime = 1
            if not oldtunnel_inside_undead_defeated and oldtunnel_exploration_scrap15_hidelight:
                $ custom3 = "You put away your light and sneak forward. "
            elif not oldtunnel_inside_undead_defeated:
                $ custom3 = "Still carrying your light, you move forward carefully. "
            else:
                $ custom1 = ""
            if not oldtunnel_inside_undead_defeated:
                $ custom1 = " You pay attention to sounds and movements, but there’s no crackling of a campfire, no wandering or chatter. You see a shape of a gate, far in the distance."
            else:
                $ custom1 = " There’s no more light at the end of the tunnel. So far, there’s nothing unusual about the walls or the ceiling."
        else:
            if not oldtunnel_inside_undead_defeated:
                $ custom1 = " Your slow pace only makes the long tunnel more exhausting."
            else:
                $ custom1 = " The tunnel is quiet and dry."
            if oldtunnel_exploration_scrap15_hidelight and oldtunnel_inside_undead_defeated:
                $ custom3 = "You put away your light and sneak forward. "
            elif not oldtunnel_exploration_scrap15_hidelight and not oldtunnel_inside_undead_defeated:
                $ custom3 = "Still carrying your light, you move forward carefully. "
            else:
                $ custom3 = ""
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside07.ogg":
            play nature "audio/ambient/oldtunnelinside07.ogg" fadeout 2.0 fadein 2.0 volume 1.0
        menu:
            '[custom3][custom1]
            '
            'I try to get close enough to see who’s responsible for the light.' if not oldtunnel_inside_undead_defeated and not oldtunnel_inside_undead_seen:
                jump oldtunnel_exploration_scrap18_seen
            'I cup my hands around my mouth and let out a shout.' if not oldtunnel_inside_undead_defeated and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit:
                jump oldtunnel_exploration_scrap18_pursuit01
            'I look for anything unusual.' if not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap18_dismantled:
                jump oldtunnel_exploration_scrap18_dismantled
            'I enter the dark chamber ahead.' if oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap19_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the dark chamber ahead.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap19
            'I head toward the bronze gate.' if oldtunnel_exploration_scrap19_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the bronze gate.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap19
            'I go back to the crossroads.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the crossroads.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap15
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 26
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap18_dismantled:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for anything unusual.')
        $ oldtunnel_exploration_scrap18_dismantled = 1
        if not oldtunnel_exploration_scrap15_hidelight:
            $ minutes += 5
            $ custom1 = "You look down, and just in time - there’s a cord stretched right above the ground, in a few spots holding pieces of wood and bone that are meant to make a sound if disturbed. You crouch and carefully cut it, putting the remains of the trap on the floor."
        else:
            $ minutes += 15
            $ custom1 = "Though you do so in almost complete darkness, you notice something blocking your boot. You crouch and touch the long cord, stretched right above the ground, in a few spots holding pieces of wood and bone that are meant to make a sound if disturbed. You cut it carefully, putting the remains of the trap on the floor."
        menu:
            '[custom1]
            '
            'I try to get close enough to see who’s responsible for the light.' if not oldtunnel_inside_undead_defeated and not oldtunnel_inside_undead_seen:
                jump oldtunnel_exploration_scrap18_seen
            'I cup my hands around my mouth and let out a shout.' if not oldtunnel_inside_undead_defeated and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit:
                jump oldtunnel_exploration_scrap18_pursuit01
            'I look for anything unusual.' if not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap18_dismantled:
                jump oldtunnel_exploration_scrap18_dismantled
            'I enter the dark chamber ahead.' if oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap19_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the dark chamber ahead.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap19
            'I head toward the bronze gate.' if oldtunnel_exploration_scrap19_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the bronze gate.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap19
            'I go back to the crossroads.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the crossroads.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap15
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ minutes += 26
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap15combat_afterlock:
        $ oldtunnel_exploration_position = 15
        stop nature fadeout 2.0
        if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg":
            play music "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg" fadeout 1.0 fadein 1.0
        $ oldtunnel_inside_undead_seen = 1
        $ oldtunnel_inside_undead_pursuit = 1
        $ oldtunnel_exploration_combat = 1
        $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
        $ can_items = 0
        $ can_potions = 1
        $ manacost = 3
        if item_crossbow and item_crossbowquarrels:
            $ oldtunnel_exploration_crossbow_ready = 1
        $ renpy.save("combatsave", extra_info='Combat Auto Save')
        if not quest_closedtunnel_description01:
            $ quest_closedtunnel_description01 = "The tunnel hides a group of undead."
            if not quest_closedtunnel:
                $ quest_closedtunnel = 1
                $ renpy.notify("New entry: The Closed Tunnel")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Closed Tunnel{/i}')
            else:
                $ renpy.notify("Journal updated: The Closed Tunnel")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Closed Tunnel{/i}')
        menu:
            'You reach the door first. The creatures that chase after you don’t shout or wail, and neither make threatening gestures nor cast angry glances. You hear only the rattle of their bones as they hit against the rocky floor. The empty eye sockets of the naked skulls reveal nothing.
            \n\nThe four skeletons wear a few rags and two of them still have scraps of flesh on their limbs. Their weapons are unconvincing - simple digging tools and spears tipped with rocks - but you notice the speed and confidence of their movement. The one in the back is holding a wooden lantern while another one is carrying a fresh torch, but the group doesn’t pay much attention to their steps.
            '
            'I run to the chamber with stalactites.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run to the chamber with stalactites.')
                $ minutes += 1
                jump oldtunnel_exploration_scrap14
            '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            'I don’t have a crossbow. (disabled)' if not item_crossbow:
                pass
            '{image=d6} I’m ready to face them.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face them.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass

    label oldtunnel_exploration_scrap18_seen:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to get close enough to see who’s responsible for the light.')
        $ minutes += 5
        $ oldtunnel_inside_undead_seen = 1
        if not oldtunnel_exploration_scrap18_dismantled:
            $ oldtunnel_inside_undead_pursuit = 1
            $ oldtunnel_exploration_combat = 1
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            $ can_items = 0
            $ can_potions = 1
            $ manacost = 3
            if item_crossbow and item_crossbowquarrels:
                $ oldtunnel_exploration_crossbow_ready = 1
            $ renpy.save("combatsave", extra_info='Combat Auto Save')
            menu:
                'You stumble over the cord that’s stretched right above the ground, starting the clatter of pieces of wood and bone that are hanging from it. The light at the end of the tunnel draws near, followed by a few human-like figures.
                '
                'I take a few steps back and try to see who am I dealing with.':
                    label oldtunnel_exploration_scrap18_seen_fail:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a few steps back and try to see who am I dealing with.')
                        if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg":
                            play music "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg" fadeout 1.0 fadein 1.0
                        stop nature fadeout 2.0
                        if not quest_closedtunnel_description01:
                            $ quest_closedtunnel_description01 = "The tunnel hides a group of undead."
                            if not quest_closedtunnel:
                                $ quest_closedtunnel = 1
                                $ renpy.notify("New entry: The Closed Tunnel")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Closed Tunnel{/i}')
                            else:
                                $ renpy.notify("Journal updated: The Closed Tunnel")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Closed Tunnel{/i}')
                        menu:
                            'The creatures don’t shout or wail, and neither make threatening gestures nor cast angry glances. You hear only the rattle of their bones as they hit against the rocky floor. The empty eye sockets of the naked skulls reveal nothing.
                            \n\nThe four skeletons wear a few rags and two of them still have scraps of flesh on their limbs. Their weapons are unconvincing - simple digging tools and spears tipped with rocks - but you notice the speed and confidence of their movement. The one in the back is holding a wooden lantern while another one is carrying a fresh torch, but the group doesn’t pay much attention to their steps.
                            '
                            'I run toward the door behind me.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run toward the door behind me.')
                                $ minutes += 2
                                jump oldtunnel_exploration_scrap15
                            '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                                jump oldtunnel_combat_spell
                            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                                jump oldtunnel_combat_crossbow
                            'I don’t have a crossbow. (disabled)' if not item_crossbow:
                                pass
                            '{image=d6} I’m ready to face them.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face them.')
                                jump oldtunnel_combat_lastclash
                            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                                pass
                            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                                pass
        elif not oldtunnel_exploration_scrap15_hidelight:
            $ oldtunnel_inside_undead_pursuit = 1
            $ oldtunnel_exploration_combat = 1
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            $ can_items = 0
            $ can_potions = 1
            $ manacost = 3
            if item_crossbow and item_crossbowquarrels:
                $ oldtunnel_exploration_crossbow_ready = 1
            $ renpy.save("combatsave", extra_info='Combat Auto Save')
            menu:
                'You get close enough to recognize more distinctive shapes in the shadows, but your own light also draws attention. The one at the end of the tunnel draws near, followed by a few human-like figures.
                '
                'I take a few steps back and try to see who am I dealing with.':
                    jump oldtunnel_exploration_scrap18_seen_fail
        else:
            if pc_class == "scholar":
                $ at_unlock_knowledge= 1
                $ at = 0
            menu:
                'Slowly but surely, you reach the edge of the light, but don’t dare to get any closer. The distinctive shadows belong to unmoving, human-like shadows that have no flesh on their necks and chests - only the bones.
                \n\nYou move back. There may be three undead there, if not more.
                \n\nYou could prepare some surprises in the tunnel to slow them down or even weaken them, but who knows how easy it would be to outsmart them.
                '
                'I may not have much practice with hunting, but I know a few things about traps.' ( condition="at == 'knowledge'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may not have much practice with hunting, but I know a few things about traps.')
                    $ at_unlock_knowledge= 0
                    $ at = 0
                    $ oldtunnel_exploration_knowledge = 1
                    if not quest_closedtunnel_description01:
                        $ quest_closedtunnel_description01 = "The tunnel hides a group of undead. To have a better chance at fighting them, I could ask someone to teach me how to construct simple traps."
                        $ quest_closedtunnel_description01a = "The tunnel hides a group of undead. To have a better chance at fighting them, I could construct some simple traps."
                        if not quest_closedtunnel:
                            $ quest_closedtunnel = 1
                            $ renpy.notify("New entry: The Closed Tunnel")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Closed Tunnel{/i}')
                        else:
                            $ renpy.notify("Journal updated: The Closed Tunnel")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Closed Tunnel{/i}')
                    menu:
                        'With your vague knowledge of carpentry and a few attempts you should be able to figure out a few tricks - deadfalls, whip traps, or footholds. All you need is to pay close attention to your surroundings and to find some wood, tools, and sharp rocks - it shouldn’t be too difficult in these corridors.
                        \n\nHowever, not all traps will be equally effective in every spot.
                        '
                        'I try to get close enough to see who’s responsible for the light.' if not oldtunnel_inside_undead_defeated and not oldtunnel_inside_undead_seen:
                            jump oldtunnel_exploration_scrap18_seen
                        'I cup my hands around my mouth and let out a shout.' if not oldtunnel_inside_undead_defeated and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit:
                            jump oldtunnel_exploration_scrap18_pursuit01
                        'I look for anything unusual.' if not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap18_dismantled:
                            jump oldtunnel_exploration_scrap18_dismantled
                        'I enter the dark chamber ahead.' if oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap19_firsttime:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the dark chamber ahead.')
                            $ minutes += 4
                            jump oldtunnel_exploration_scrap19
                        'I head toward the bronze gate.' if oldtunnel_exploration_scrap19_firsttime:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the bronze gate.')
                            $ minutes += 4
                            jump oldtunnel_exploration_scrap19
                        'I go back to the crossroads.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the crossroads.')
                            $ minutes += 4
                            jump oldtunnel_exploration_scrap15
                        'I go back to {color=#f6d6bd}[horsename]{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                            $ minutes += 26
                            jump oldtunnelafterinteraction01
                'I better speak with someone who knows how to set traps.' ( condition="at != 'knowledge'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better speak with someone who knows how to set traps.')
                    $ at_unlock_knowledge= 0
                    $ at = 0
                    if not quest_closedtunnel_description01:
                        $ quest_closedtunnel_description01 = "The tunnel hides a group of undead. To have a better chance at fighting them, I could ask someone to teach me how to construct simple traps."
                        if not quest_closedtunnel:
                            $ quest_closedtunnel = 1
                            $ renpy.notify("New entry: The Closed Tunnel")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Closed Tunnel{/i}')
                        else:
                            $ renpy.notify("Journal updated: The Closed Tunnel")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Closed Tunnel{/i}')
                    menu:
                        'You move to a safer position.
                        '
                        'I try to get close enough to see who’s responsible for the light.' if not oldtunnel_inside_undead_defeated and not oldtunnel_inside_undead_seen:
                            jump oldtunnel_exploration_scrap18_seen
                        'I cup my hands around my mouth and let out a shout.' if not oldtunnel_inside_undead_defeated and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit:
                            jump oldtunnel_exploration_scrap18_pursuit01
                        'I look for anything unusual.' if not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap18_dismantled:
                            jump oldtunnel_exploration_scrap18_dismantled
                        'I enter the dark chamber ahead.' if oldtunnel_inside_undead_defeated and not oldtunnel_exploration_scrap19_firsttime:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the dark chamber ahead.')
                            $ minutes += 4
                            jump oldtunnel_exploration_scrap19
                        'I head toward the bronze gate.' if oldtunnel_exploration_scrap19_firsttime:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head toward the bronze gate.')
                            $ minutes += 4
                            jump oldtunnel_exploration_scrap19
                        'I go back to the crossroads.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the crossroads.')
                            $ minutes += 4
                            jump oldtunnel_exploration_scrap15
                        'I go back to {color=#f6d6bd}[horsename]{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                            $ minutes += 26
                            jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap18_pursuit01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cup my hands around my mouth and let out a shout.')
        $ minutes += 1
        $ oldtunnel_inside_undead_pursuit = 1
        $ oldtunnel_exploration_combat = 1
        $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
        $ can_items = 0
        $ can_potions = 1
        $ manacost = 3
        if item_crossbow and item_crossbowquarrels:
            $ oldtunnel_exploration_crossbow_ready = 1
        menu:
            'You take a deep breath.
            '
            '“Hey you! Come and get me!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Hey you! Come and get me!”')
                jump oldtunnel_exploration_scrap18_pursuit02
            '“I will purge this land of you!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I will purge this land of you!”')
                jump oldtunnel_exploration_scrap18_pursuit02
            '“I come in peace!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I come in peace!”')
                jump oldtunnel_exploration_scrap18_pursuit02
            'I don’t know. I just shout.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t know. I just shout.')
                jump oldtunnel_exploration_scrap18_pursuit02

    label oldtunnel_exploration_scrap18_pursuit02:
        if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg":
            play music "<loop 15.0>audio/dancainedarkcolors_battletheme_loop.ogg" fadeout 1.0 fadein 1.0
        stop nature fadeout 2.0
        $ renpy.save("combatsave", extra_info='Combat Auto Save')
        menu:
            'The creatures don’t scream or wail, and neither make threatening gestures nor cast angry glances. You hear only the rattle of their bones as they hit against the rocky floor. The empty eye sockets of the naked skulls reveal nothing.
            \n\nThe four skeletons wear a few rags and two of them still have scraps of flesh on their limbs. Their weapons are unconvincing - simple digging tools and spears tipped with rocks - but you notice the speed and confidence of their movement. The one in the back is holding a wooden lantern while another one is carrying a fresh torch, but the group doesn’t pay much attention to their steps.
            '
            'I run toward the door behind me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run toward the door behind me.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap15
            '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            'I don’t have a crossbow. (disabled)' if not item_crossbow:
                pass
            '{image=d6} I’m ready to face them.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face them.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass

    label oldtunnel_exploration_scrap18_midcombat_afterinteraction:
        menu:
            '[custom1][custom2]
            '
            'I run toward the door behind me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run toward the door behind me.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap15
            '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass

    label oldtunnel_exploration_scrap18_midcombat_nothing:
        menu:
            'The undead are getting closer.
            '
            'I run toward the door behind me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I run toward the door behind me.')
                $ minutes += 2
                jump oldtunnel_exploration_scrap15
            '{image=d6} I reach for my wand.' ( condition="pc_class == 'mage' and mana >= manacost" ):
                jump oldtunnel_combat_spell
            '{image=d6} I raise my crossbow.' if oldtunnel_exploration_crossbow_ready:
                jump oldtunnel_combat_crossbow
            '{image=d6} I’m ready to face the undead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’m ready to face the undead.')
                jump oldtunnel_combat_lastclash
            'I’ve no pneuma left. [[Cost: [manacost]] (disabled)' ( condition="pc_class == 'mage' and mana < manacost" ):
                pass
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass

label oldtunnel_exploration_scrap19ALL:
    label oldtunnel_exploration_scrap19: # wyjście
        $ oldtunnel_exploration_position = 19
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside07.ogg":
            play nature "audio/ambient/oldtunnelinside07.ogg" fadeout 2.0 fadein 2.0 volume 1.0
        if not oldtunnel_exploration_scrap19_firsttime:
            $ oldtunnel_exploration_scrap19_firsttime = 1
            $ custom1 = "While the chamber is in shambles, you recognize its unusual furniture - the sharpened stakes, shield-like tables for crossbow users, empty spear racks. If necessary, it could be the last line of defense for guards and diggers, surrounding any beast or a bandit determined enough to reach this end of the tunnel.\n\nYou’re in front of a massive double-leaf gate, taller than two humans, made of bronze. You’re not sure if a single shell can even move it."
        else:
            $ custom1 = "The chamber is like a battlefield."
        if not quest_closedtunnel_description00:
            $ quest_closedtunnel_description00 = "The tunnel leading through the northern mountains is closed. Opening the gate would make this route safer."
            $ renpy.notify("Journal updated: The Closed Tunnel")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Closed Tunnel{/i}')
        if not renpy.music.get_playing(channel='nature') == "audio/ambient/oldtunnelinside01.ogg":
            play nature "audio/ambient/oldtunnelinside01.ogg" fadeout 2.0 fadein 2.0 volume 1.0
        menu:
            '[custom1]
            '
            'I search the room.' if not oldtunnel_exploration_scrap19_search:
                jump oldtunnel_exploration_scrap19_search
            'I take a look at the gate.' if not oldtunnel_exploration_scrap19_trygate:
                jump oldtunnel_exploration_scrap19_trygate
            'I open the gate with the huge key.' ( condition="pc_hp >= 3 and oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened and item_oldtunnelkey" ):
                jump oldtunnel_exploration_scrap19_open
            'The gate requires some sort of a massive key. (disabled)' ( condition="oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened and not item_oldtunnelkey" ):
                pass
            'I’m too weak to push such a huge gate. (Required vitality: 3) (disabled)' ( condition="pc_hp <= 2 and oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened" ):
                pass
            'I return to the tunnel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the tunnel.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap18
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ quarters += 2
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap19_search:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the room.')
        $ oldtunnel_exploration_scrap19_search = 1
        $ minutes += 10
        menu:
            'While there’s plenty of furniture to look under or push aside, the undead left little to no signs of their presence, as if they were idly standing for years. A small pile of candles and another, much larger one of candle stumps don’t explain why the walking corpses would use light.
            \n\nYou grab a few of the candles for later.
            '
            'I search the room.' if not oldtunnel_exploration_scrap19_search:
                jump oldtunnel_exploration_scrap19_search
            'I take a look at the gate.' if not oldtunnel_exploration_scrap19_trygate:
                jump oldtunnel_exploration_scrap19_trygate
            'I open the gate with the huge key.' ( condition="pc_hp >= 3 and oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened and item_oldtunnelkey" ):
                jump oldtunnel_exploration_scrap19_open
            'The gate requires some sort of a massive key. (disabled)' ( condition="oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened and not item_oldtunnelkey" ):
                pass
            'I’m too weak to push such a huge gate. (Required vitality: 3) (disabled)' ( condition="pc_hp <= 2 and oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened" ):
                pass
            'I return to the tunnel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the tunnel.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap18
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ quarters += 2
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap19_trygate:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a look at the gate.')
        $ oldtunnel_exploration_scrap19_trygate = 1
        $ minutes += 1
        if not item_oldtunnelkey:
            $ custom1 = " A key of this size shouldn’t be difficult to find."
        else:
            $ custom1 = ""
        menu:
            'It’s made of sheets held by thick bars. The pictures impressed on the surface portray fishers and their catch, sea monsters covered with nets, falling harpies, and working diggers. While it’s doubtful it’s made of a material worthy of turning into blades, it’s priceless.
            \n\nYou look through the keyhole, observing the continuing path and the clear sky with ease, despite the cobwebs. You take a deep breath of fresh air, then put four fingers inside.[custom1]
            '
            'I search the room.' if not oldtunnel_exploration_scrap19_search:
                jump oldtunnel_exploration_scrap19_search
            'I take a look at the gate.' if not oldtunnel_exploration_scrap19_trygate:
                jump oldtunnel_exploration_scrap19_trygate
            'I open the gate with the huge key.' ( condition="pc_hp >= 3 and oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened and item_oldtunnelkey" ):
                jump oldtunnel_exploration_scrap19_open
            'The gate requires some sort of a massive key. (disabled)' ( condition="oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened and not item_oldtunnelkey" ):
                pass
            'I’m too weak to push such a huge gate. (Required vitality: 3) (disabled)' ( condition="pc_hp <= 2 and oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened" ):
                pass
            'I return to the tunnel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the tunnel.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap18
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ quarters += 2
                jump oldtunnelafterinteraction01

    label oldtunnel_exploration_scrap19_open:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I open the gate with the huge key.')
        $ oldtunnel_inside_opened = 1
        $ togalerocks -= 2
        $ tobeach -= 2
        $ minutes += 5
        $ quest_closedtunnel_description04 = "The gate is now open. The locals could be interested in this."
        $ quest_closedtunnel = 2
        if pc_goal == "iwanttohelp":
            $ pc_goal_iwanttohelppoints += 2
        if oldtunnel_inside_undead_defeated_bypc and quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
            $ pc_goal_iwanttoberememberedpoints += 1
        if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered" and oldtunnel_inside_undead_defeated_bypc:
            $ renpy.notify("Quest completed: The Closed Tunnel.\nJournal updated: %s" %quest_pc_goal_name)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Closed Tunnel. Journal updated: %s{/i}' %quest_pc_goal_name)
        else:
            $ renpy.notify("Quest completed: The Closed Tunnel")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Closed Tunnel{/i}')
        menu:
            'Easier said than done - rotating the key alone makes you hold your breath, and as you work at pushing the leaves open, you puff and blow, taking breaks. After it’s done, you wipe your sweaty forehead, giving a proud look at the light that has now entered the chamber.
            '
            'I search the room.' if not oldtunnel_exploration_scrap19_search:
                jump oldtunnel_exploration_scrap19_search
            'I take a look at the gate.' if not oldtunnel_exploration_scrap19_trygate:
                jump oldtunnel_exploration_scrap19_trygate
            'I open the gate with the huge key.' ( condition="pc_hp >= 3 and oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened and item_oldtunnelkey" ):
                jump oldtunnel_exploration_scrap19_open
            'The gate requires some sort of a massive key. (disabled)' ( condition="oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened and not item_oldtunnelkey" ):
                pass
            'I’m too weak to push such a huge gate. (Required vitality: 3) (disabled)' ( condition="pc_hp <= 2 and oldtunnel_exploration_scrap19_trygate and not oldtunnel_inside_opened" ):
                pass
            'I return to the tunnel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the tunnel.')
                $ minutes += 4
                jump oldtunnel_exploration_scrap18
            'I go back to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}%s{/color}.' %horsename)
                $ quarters += 2
                jump oldtunnelafterinteraction01

label oldtunnel_combat_crossbow:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I raise my crossbow.')
    menu:
        'Depending on the undead’s movements and how much time and space it has to dodge, it may be difficult to hit it with a quarrel. Also, you may have no more opportunities to load your weapon.
        '
        '{image=d6} I aim at a stalactite.' if oldtunnel_exploration_position == 14:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I aim at a stalactite.')
            $ oldtunnel_exploration_crossbow_ready = 0
            $ item_crossbowquarrels -= 1
            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
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
            $ d100roll -= 10 # stalactite
            if d100roll <= 60:
                $ oldtunnel_inside_undead_hp -= 4
                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                $ custom1 = "The undead doesn’t notice the threat - the massive spike pierces its skull and reaches the thorax. "
                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                    $ oldtunnel_inside_undead_amount = 3
                    $ custom2 = "Its loose bones scatter over the soggy planks."
                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                    $ oldtunnel_inside_undead_amount = 2
                    $ custom2 = "It hits the wet ground silently and moves no longer."
                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                    $ oldtunnel_inside_undead_amount = 1
                    $ custom2 = "It lets out a quiet moan as it crumbles. There’s only one creature left."
                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                    $ oldtunnel_inside_undead_amount_0_description = 1
                    $ custom2 = "Somehow, it still shuffles forward, giving you an empty, yet hungry look."
                else:
                    $ custom2 = "Somehow, it still shuffles forward, giving you an empty, yet hungry look."
            else:
                $ custom1 = ""
                $ custom2 = "You hit, but the undead leap away before the rocks hit them."
            jump oldtunnel_exploration_scrap14_midcombat_afterinteraction
        '{image=d6} I aim at the head.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I aim at the head.')
            $ oldtunnel_exploration_crossbow_ready = 0
            $ item_crossbowquarrels -= 1
            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
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
            if oldtunnel_exploration_position == 1 or oldtunnel_exploration_position == 5 or (oldtunnel_exploration_position == 8 and oldtunnel_exploration_scrap08_trap != "deadfall") or (oldtunnel_exploration_position == 11 and not oldtunnel_exploration_scrap11_trap) or (oldtunnel_exploration_position == 15 and not oldtunnel_exploration_scrap15_trap) or oldtunnel_exploration_position == 18:
                $ d100roll -= 0
            if oldtunnel_exploration_position == 6 or (oldtunnel_exploration_position == 8 and oldtunnel_exploration_scrap08_trap == "deadfall") or (oldtunnel_exploration_position == 11 and oldtunnel_exploration_scrap11_trap) or oldtunnel_exploration_position == 14 or (oldtunnel_exploration_position == 15 and oldtunnel_exploration_scrap15_trap):
                $ d100roll -= 10
            if oldtunnel_exploration_position == 10:
                $ d100roll -= 20
            if d100roll <= 60:
                if d100roll <= 20:
                    $ oldtunnel_inside_undead_hp -= 3
                else:
                    $ oldtunnel_inside_undead_hp -= 2
                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                $ custom1 = "The quarrel pierces through the forehead and stays inside the skull"
                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                    $ oldtunnel_inside_undead_amount = 3
                    $ custom2 = ". The loose bones of the first undead scatter over the floor."
                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                    $ oldtunnel_inside_undead_amount = 2
                    $ custom2 = ". The second undead hits the ground silently."
                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                    $ oldtunnel_inside_undead_amount = 1
                    $ custom2 = ". The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                    $ oldtunnel_inside_undead_amount_0_description = 1
                    $ custom2 = ". After a few moments, the last undead shuffles forward, giving you an empty, yet somehow hungry look."
                else:
                    $ custom2 = ", and while the undead leans away for a few moments, it doesn’t take long for it to straighten up again."
            else:
                $ custom1 = ""
                $ custom2 = "You miss. The undead doesn’t even look at the quarrel."
            if oldtunnel_exploration_position == 1:
                jump oldtunnel_exploration_scrap01_midcombat_afterinteraction
            if oldtunnel_exploration_position == 5:
                jump oldtunnel_exploration_scrap05_midcombat_afterinteraction
            if oldtunnel_exploration_position == 6:
                jump oldtunnel_exploration_scrap06_midcombat_afterinteraction
            if oldtunnel_exploration_position == 8:
                jump oldtunnel_exploration_scrap08_midcombat_afterinteraction
            if oldtunnel_exploration_position == 10:
                jump oldtunnel_exploration_scrap10_midcombat_afterinteraction
            if oldtunnel_exploration_position == 11:
                jump oldtunnel_exploration_scrap11_midcombat_afterinteraction
            if oldtunnel_exploration_position == 14:
                jump oldtunnel_exploration_scrap14_midcombat_afterinteraction
            if oldtunnel_exploration_position == 15:
                jump oldtunnel_exploration_scrap15_midcombat_afterinteraction
            if oldtunnel_exploration_position == 18:
                jump oldtunnel_exploration_scrap18_midcombat_afterinteraction
        '{image=d6} I aim at the chest.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I aim at the chest.')
            $ custom1 = "The quarrel grazes a rib, then disappears into the darkness. The undead doesn’t even turn around."
            $ custom2 = ""
            $ oldtunnel_exploration_crossbow_ready = 0
            $ item_crossbowquarrels -= 1
            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            if oldtunnel_exploration_position == 1:
                jump oldtunnel_exploration_scrap01_midcombat_afterinteraction
            if oldtunnel_exploration_position == 5:
                jump oldtunnel_exploration_scrap05_midcombat_afterinteraction
            if oldtunnel_exploration_position == 6:
                jump oldtunnel_exploration_scrap06_midcombat_afterinteraction
            if oldtunnel_exploration_position == 8:
                jump oldtunnel_exploration_scrap08_midcombat_afterinteraction
            if oldtunnel_exploration_position == 10:
                jump oldtunnel_exploration_scrap10_midcombat_afterinteraction
            if oldtunnel_exploration_position == 11:
                jump oldtunnel_exploration_scrap11_midcombat_afterinteraction
            if oldtunnel_exploration_position == 14:
                jump oldtunnel_exploration_scrap14_midcombat_afterinteraction
            if oldtunnel_exploration_position == 15:
                jump oldtunnel_exploration_scrap15_midcombat_afterinteraction
            if oldtunnel_exploration_position == 18:
                jump oldtunnel_exploration_scrap18_midcombat_afterinteraction
        '{image=d6} I aim at a leg.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I aim at a leg.')
            $ oldtunnel_exploration_crossbow_ready = 0
            $ item_crossbowquarrels -= 1
            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
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
            if oldtunnel_exploration_position == 1 or oldtunnel_exploration_position == 5 or (oldtunnel_exploration_position == 8 and oldtunnel_exploration_scrap08_trap != "deadfall") or (oldtunnel_exploration_position == 11 and not oldtunnel_exploration_scrap11_trap) or (oldtunnel_exploration_position == 15 and not oldtunnel_exploration_scrap15_trap) or oldtunnel_exploration_position == 18:
                $ d100roll -= 0
            if oldtunnel_exploration_position == 6 or (oldtunnel_exploration_position == 8 and oldtunnel_exploration_scrap08_trap == "deadfall") or (oldtunnel_exploration_position == 11 and oldtunnel_exploration_scrap11_trap) or oldtunnel_exploration_position == 14 or (oldtunnel_exploration_position == 15 and oldtunnel_exploration_scrap15_trap):
                $ d100roll -= 10
            if oldtunnel_exploration_position == 10:
                $ d100roll -= 20
            if d100roll <= 50:
                if d100roll <= 10:
                    $ oldtunnel_inside_undead_hp -= 2
                else:
                    $ oldtunnel_inside_undead_hp -= 1
                $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
                $ custom1 = ""
                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                    $ oldtunnel_inside_undead_amount = 3
                    $ custom2 = "The quarrel shatters it completely. The loose bones of the first undead scatter over the floor."
                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                    $ oldtunnel_inside_undead_amount = 2
                    $ custom2 = "The quarrel shatters it completely. The second undead hits the ground silently."
                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                    $ oldtunnel_inside_undead_amount = 1
                    $ custom2 = "The quarrel shatters it completely. The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                    $ oldtunnel_inside_undead_amount_0_description = 1
                    $ custom2 = "The quarrel breaks the bone, but the undead is still standing. After a few moments it shuffles forward, giving you an empty, yet somehow hungry look."
                else:
                    $ custom2 = "Even though the quarrel grazes the bone and makes your target stagger, the undead regains its composure quickly."
            else:
                $ custom1 = ""
                $ custom2 = "You miss. The undead doesn’t even look at the quarrel."
            if oldtunnel_exploration_position == 1:
                jump oldtunnel_exploration_scrap01_midcombat_afterinteraction
            if oldtunnel_exploration_position == 5:
                jump oldtunnel_exploration_scrap05_midcombat_afterinteraction
            if oldtunnel_exploration_position == 6:
                jump oldtunnel_exploration_scrap06_midcombat_afterinteraction
            if oldtunnel_exploration_position == 8:
                jump oldtunnel_exploration_scrap08_midcombat_afterinteraction
            if oldtunnel_exploration_position == 10:
                jump oldtunnel_exploration_scrap10_midcombat_afterinteraction
            if oldtunnel_exploration_position == 11:
                jump oldtunnel_exploration_scrap11_midcombat_afterinteraction
            if oldtunnel_exploration_position == 14:
                jump oldtunnel_exploration_scrap14_midcombat_afterinteraction
            if oldtunnel_exploration_position == 15:
                jump oldtunnel_exploration_scrap15_midcombat_afterinteraction
            if oldtunnel_exploration_position == 18:
                jump oldtunnel_exploration_scrap18_midcombat_afterinteraction
        'Maybe not.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe not.')
            if oldtunnel_exploration_position == 1:
                jump oldtunnel_exploration_scrap01_midcombat_nothing
            if oldtunnel_exploration_position == 5:
                jump oldtunnel_exploration_scrap05_midcombat_nothing
            if oldtunnel_exploration_position == 6:
                jump oldtunnel_exploration_scrap06_midcombat_nothing
            if oldtunnel_exploration_position == 8:
                jump oldtunnel_exploration_scrap08_midcombat_nothing
            if oldtunnel_exploration_position == 11:
                jump oldtunnel_exploration_scrap11_midcombat_nothing
            if oldtunnel_exploration_position == 14:
                jump oldtunnel_exploration_scrap14_midcombat_nothing
            if oldtunnel_exploration_position == 15:
                jump oldtunnel_exploration_scrap15_midcombat_nothing
            if oldtunnel_exploration_position == 18:
                jump oldtunnel_exploration_scrap18_midcombat_nothing

label oldtunnel_combat_spell:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I reach for my wand.')
    menu:
        'Depending on the undead’s movements and how much time and space it has to dodge, it may be difficult to land a perfect spell.
        '
        '{image=d6} I strike it. [[Cost: {color=#f6d6bd}[manacost]{/color}]':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I strike it. [[Cost: {color=#f6d6bd}%s{/color}]' %manacost)
            $ at = 0
            $ at_unlock_spell = 0
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
            if oldtunnel_exploration_position == 1 or oldtunnel_exploration_position == 5 or (oldtunnel_exploration_position == 8 and oldtunnel_exploration_scrap08_trap != "deadfall") or (oldtunnel_exploration_position == 11 and not oldtunnel_exploration_scrap11_trap) or (oldtunnel_exploration_position == 15 and not oldtunnel_exploration_scrap15_trap) or oldtunnel_exploration_position == 18:
                $ oldtunnel_inside_undead_hp -= 1
                $ custom1 = "You reach for the willow wand and dash forward, casting the pneuma with a single swipe. It feels like stabbing the air with a wooden dagger.\n\nYour target almost dodges the invisible wave"
                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                    $ oldtunnel_inside_undead_amount = 3
                    $ custom2 = ", yet, the gentle hit is enough. The bones scatter over the pond - the first undead is no more."
                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                    $ oldtunnel_inside_undead_amount = 2
                    $ custom2 = ", yet, the gentle hit is enough. The second undead sinks into the water silently."
                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                    $ oldtunnel_inside_undead_amount = 1
                    $ custom2 = ", yet, the gentle hit is enough. The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                    $ oldtunnel_inside_undead_amount_0_description = 1
                    $ custom2 = ", yet, the gentle hit is almost enough. The last undead leans away for a few moments, and after it straightens up again, it lacks a rib."
                else:
                    $ custom2 = ". The undead leans away for a few moments, and after it straightens up again, it runs after you, despite its broken rib."
            if oldtunnel_exploration_position == 6 or (oldtunnel_exploration_position == 8 and oldtunnel_exploration_scrap08_trap == "deadfall") or (oldtunnel_exploration_position == 11 and oldtunnel_exploration_scrap11_trap) or oldtunnel_exploration_position == 14 or (oldtunnel_exploration_position == 15 and oldtunnel_exploration_scrap15_trap):
                $ oldtunnel_inside_undead_hp -= 2
                $ custom1 = "You reach for the willow wand and dash forward, casting the pneuma with a single swipe. It feels like stabbing the air with a wooden dagger.\n\nThe invisible barely hit the chest. "
                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                    $ oldtunnel_inside_undead_amount = 3
                    $ custom2 = "The bones scatter over the pond - the first undead is no more."
                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                    $ oldtunnel_inside_undead_amount = 2
                    $ custom2 = "The second undead sinks into the water silently."
                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                    $ oldtunnel_inside_undead_amount = 1
                    $ custom2 = "The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                    $ oldtunnel_inside_undead_amount_0_description = 1
                    $ custom2 = "The last undead leans away for a few moments, and after it straightens up again, it lacks a few ribs."
                else:
                    $ custom2 = "The undead leans away for a few moments, and after it straightens up again, it lacks a few ribs."
            if oldtunnel_exploration_position == 10:
                $ oldtunnel_inside_undead_hp -= 3
                $ custom1 = "You reach for the willow wand and dash forward, casting the pneuma with a single swipe. It feels like stabbing the air with a wooden dagger.\n\nThe invisible wave doesn’t spare the revealed bones. "
                if oldtunnel_inside_undead_hp <= 15 and oldtunnel_inside_undead_amount == 4:
                    $ oldtunnel_inside_undead_amount = 3
                    $ custom2 = "They scatter over the pond - the first undead is no more."
                elif oldtunnel_inside_undead_hp <= 10 and oldtunnel_inside_undead_amount == 3:
                    $ oldtunnel_inside_undead_amount = 2
                    $ custom2 = "The second undead sinks into the water silently."
                elif oldtunnel_inside_undead_hp <= 5 and oldtunnel_inside_undead_amount == 2:
                    $ oldtunnel_inside_undead_amount = 1
                    $ custom2 = "The third undead lets out a quiet moan as it crumbles. There’s only one creature left."
                elif oldtunnel_inside_undead_hp <= 0 and not oldtunnel_inside_undead_amount_0_description:
                    $ oldtunnel_inside_undead_amount_0_description = 1
                    $ custom2 = "The last undead leans away for a few moments, and after it straightens up again, it lacks its ribs."
                else:
                    $ custom2 = "The undead leans away for a few moments, and after it straightens up again, it lacks its ribs."
            $ oldtunnel_inside_undead_hp_old = oldtunnel_inside_undead_hp
            if oldtunnel_exploration_position == 1:
                jump oldtunnel_exploration_scrap01_midcombat_afterinteraction
            if oldtunnel_exploration_position == 5:
                jump oldtunnel_exploration_scrap05_midcombat_afterinteraction
            if oldtunnel_exploration_position == 6:
                jump oldtunnel_exploration_scrap06_midcombat_afterinteraction
            if oldtunnel_exploration_position == 8:
                jump oldtunnel_exploration_scrap08_midcombat_afterinteraction
            if oldtunnel_exploration_position == 10:
                jump oldtunnel_exploration_scrap10_midcombat_afterinteraction
            if oldtunnel_exploration_position == 11:
                jump oldtunnel_exploration_scrap11_midcombat_afterinteraction
            if oldtunnel_exploration_position == 14:
                jump oldtunnel_exploration_scrap14_midcombat_afterinteraction
            if oldtunnel_exploration_position == 15:
                jump oldtunnel_exploration_scrap15_midcombat_afterinteraction
            if oldtunnel_exploration_position == 18:
                jump oldtunnel_exploration_scrap18_midcombat_afterinteraction
        'Let’s try something else.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s try something else.')
            $ at = 0
            $ at_unlock_spell = 0
            if oldtunnel_exploration_position == 1:
                jump oldtunnel_exploration_scrap01_midcombat_nothing
            if oldtunnel_exploration_position == 5:
                jump oldtunnel_exploration_scrap05_midcombat_nothing
            if oldtunnel_exploration_position == 6:
                jump oldtunnel_exploration_scrap06_midcombat_nothing
            if oldtunnel_exploration_position == 8:
                jump oldtunnel_exploration_scrap08_midcombat_nothing
            if oldtunnel_exploration_position == 10:
                jump oldtunnel_exploration_scrap10_midcombat_nothing
            if oldtunnel_exploration_position == 11:
                jump oldtunnel_exploration_scrap11_midcombat_nothing
            if oldtunnel_exploration_position == 14:
                jump oldtunnel_exploration_scrap14_midcombat_nothing
            if oldtunnel_exploration_position == 15:
                jump oldtunnel_exploration_scrap15_midcombat_nothing
            if oldtunnel_exploration_position == 18:
                jump oldtunnel_exploration_scrap18_midcombat_nothing

label oldtunnel_combat_lastclash_outside:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to face the undead.')
    $ at_unlock_spell = 0
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 1
    $ can_potions = 1
    $ oldtunnel_exploration_combat = 1
    if oldtunnel_inside_undead_amount == 4:
        $ custom1 = "The four undead would be a life-threatening enemy even for an experienced fighter."
    elif oldtunnel_inside_undead_amount == 3:
        $ custom1 = "There’s at least three undead left. A note-worthy threat."
    elif oldtunnel_inside_undead_amount == 2:
        $ custom1 = "There’s at least two undead left. If you were rested and well-equipped, you should be able to take them down."
    else:
        $ custom1 = "There’s at least one undead left. You may be able to take it down by yourself."
    $ renpy.save("combatsave", extra_info='Combat Auto Save')
    menu:
        'You look into the tunnel. The weak light invites you with its flicker. [custom1]
        '
        'I better prepare myself first.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better prepare myself first.')
            $ can_potions = 0
            jump oldtunnelafterinteraction01
        '{image=d6} I go in.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I go in.')
            if not renpy.get_screen("oldtunnel"):
                show screen oldtunnel with dissolve
            if oldtunnel_inside_undead_amount <= 1:
                $ custom3 = "You move up the corridor, heading toward the light. The skeleton is awaiting you as it takes a proper stance, filling the chambers with the thuds of its feet."
            else:
                $ custom3 = "You move up the corridor, heading toward the light. The skeletons are awaiting you as they take a proper stance, filling the chambers with the thuds of their feet."
            stop nature fadeout 2.0
            if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
                play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
            $ oldtunnel_exploration_position = 1
            $ minutes += 10
            hide areapicture
            hide oldtunnelbronzerod
            hide oldtunnelsignpost
            jump oldtunnel_combat_lastclash

label oldtunnel_combat_lastclash:
    # $ d100roll = renpy.random.randint(1, 100)
    $ d100roll = 10
    if not pc_food:
        $ d100roll += 5
    if pc_food == 3:
        $ d100roll -= 5
    if pc_food == 4:
        $ d100roll -= 10
    if armor == 4:
        $ d100roll -= 5
    if pc_hp == 5:
        $ d100roll -= 10
    elif pc_hp == 4:
        $ d100roll -= 5
    elif pc_hp == 1:
        $ d100roll += 5
    elif pc_hp == 0:
        $ d100roll += 10
    if pc_class == "warrior":
        $ d100roll -= (pc_battlecounter*2)
    else:
        $ d100roll -= (pc_battlecounter)
    if item_golemglove:
        $ d100roll -= 5
    if item_axe03:
        $ d100roll -= 10
    elif item_axe02 or item_axe02alt:
        $ d100roll -= 5
    ######
    if custom3 != "You move up the corridor, heading toward the light. The skeleton is awaiting you as it takes a proper stance, filling the chambers with the thuds of its feet." and custom3 != "You move up the corridor, heading toward the light. The skeletons are awaiting you as they take a proper stance, filling the chambers with the thuds of their feet.":
        $ pc_food = limit_pc_food(pc_food-1)
        show minus1food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
        if oldtunnel_inside_undead_amount <= 1:
            if oldtunnel_exploration_position == 6:
                $ d100roll += 5
                $ custom3 = "Your boots are wading the stream. After you exchange a few hits with the skeleton, which seems to have much greater control over its stance than its light shell would suggest, you almost slip."
            elif oldtunnel_exploration_position == 1 or oldtunnel_exploration_position == 2 or oldtunnel_exploration_position == 3 or oldtunnel_exploration_position == 5 or (oldtunnel_exploration_position == 8 and oldtunnel_exploration_scrap08_trap != "deadfall") or (oldtunnel_exploration_position == 11 and not oldtunnel_exploration_scrap11_trap) or (oldtunnel_exploration_position == 15 and not oldtunnel_exploration_scrap15_trap) or oldtunnel_exploration_position == 18:
                $ d100roll -= 0
                $ custom3 = "Both you and the skeleton have the time to take a proper stance, filling the chambers with the thuds of your boots and bones."
            elif oldtunnel_exploration_position == 4 or oldtunnel_exploration_position == 14:
                $ d100roll -= 5
                $ custom3 = "The limited space helps you predict the skeleton’s movements and defend your side."
            elif (oldtunnel_exploration_position == 15 and oldtunnel_exploration_scrap15_trap):
                $ d100roll -= 5
                $ custom3 = "With the trap pushing the skeleton away, you have a few precious moments to strike."
            elif (oldtunnel_exploration_position == 8 and oldtunnel_exploration_scrap08_trap == "deadfall") or (oldtunnel_exploration_position == 11 and oldtunnel_exploration_scrap11_trap) or (oldtunnel_exploration_position == 15 and oldtunnel_exploration_scrap15_trap):
                $ d100roll -= 10
                $ custom3 = "As the trap hinders the skeleton’s movements, you have a few precious moments to strike."
            elif oldtunnel_exploration_position == 10:
                $ custom3 = "You face each other in a duel, shackled by narrow walls."
            else:
                $ d100roll -= 0
                $ custom3 = "Both you and the skeletons have time to take a proper stance, filling the chambers with the thuds of your boots and bones."
        else:
            if oldtunnel_exploration_position == 6:
                $ d100roll += 5
                $ custom3 = "Your boots are wading the stream. After you exchange a few hits with the skeletons, which seem to have much greater control over their stance than their light shells would suggest, you almost slip."
            elif oldtunnel_exploration_position == 1 or oldtunnel_exploration_position == 2 or oldtunnel_exploration_position == 3 or oldtunnel_exploration_position == 5 or (oldtunnel_exploration_position == 8 and oldtunnel_exploration_scrap08_trap != "deadfall") or (oldtunnel_exploration_position == 11 and not oldtunnel_exploration_scrap11_trap) or (oldtunnel_exploration_position == 15 and not oldtunnel_exploration_scrap15_trap) or oldtunnel_exploration_position == 18:
                $ d100roll -= 0
                $ custom3 = "Both you and the skeletons have the time to take a proper stance, filling the chambers with the thuds of your boots and bones."
            elif oldtunnel_exploration_position == 4 or oldtunnel_exploration_position == 14:
                $ d100roll -= 10
                $ custom3 = "The limited space helps you predict the skeletons’ movements and defend your side."
            elif (oldtunnel_exploration_position == 15 and oldtunnel_exploration_scrap15_trap):
                $ d100roll -= 10
                $ custom3 = "With the trap pushing one of the skeletons away, you have a few precious moments to strike."
            elif (oldtunnel_exploration_position == 8 and oldtunnel_exploration_scrap08_trap == "deadfall") or (oldtunnel_exploration_position == 11 and oldtunnel_exploration_scrap11_trap) or (oldtunnel_exploration_position == 15 and oldtunnel_exploration_scrap15_trap):
                $ d100roll -= 10
                $ custom3 = "As the trap hinders the skeletons’ movements, you have a few precious moments to strike."
            elif oldtunnel_exploration_position == 10:
                $ d100roll -= 20
                $ custom3 = "Fighting them one by one, you have a few precious moments to strike."
            else:
                $ d100roll -= 0
                $ custom3 = "Both you and the skeletons have time to take a proper stance, filling the chambers with the thuds of your boots and bones."
    else:
        $ d100roll += 5
    ######
    if oldtunnel_inside_undead_hp <= 0 and d100roll >= 0:
        $ d100roll = 0
    elif oldtunnel_inside_undead_hp <= 5:
        $ d100roll += 15
    elif oldtunnel_inside_undead_hp <= 10:
        $ d100roll += 30
    elif oldtunnel_inside_undead_hp <= 15:
        $ d100roll += 45
    elif oldtunnel_inside_undead_hp <= 20:
        $ d100roll += 55
    else:
        $ d100roll += 65
    ######
    if d100roll <= -10:
        $ minutes += 5
        $ custom1 = "With or without flesh, your target blocks and dodges, making you fight as if you’re facing a human, not a bloodthirsty beast. You swing your axe with a speed and confidence that your opponent can’t match. After just a few moments, you, unscathed, leave a pile of bones on the ground, cut and crushed. You calm down your breath and listen to the droplets of water. Nothing else runs at you."
        $ custom2 = ""
    elif d100roll <= 0:
        $ minutes += 5
        $ custom1 = "With or without flesh, your target blocks and dodges, making you fight as if you’re facing a human, not a bloodthirsty beast. You swing your axe with a speed and confidence that your opponent can’t match. After just a few moments, you leave just a pile of bones on the ground, cut and crushed."
        if armor >= 2:
            $ custom2 = "The few hits that landed on your gambeson didn’t even cut it."
        elif armor >= 1:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ custom2 = "Your gambeson stopped any cut it took, protecting your flesh."
        else:
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ custom2 = "One hit landed on your arm, causing it to bleed."
    elif d100roll <= 10:
        $ minutes += 5
        $ custom1 = "With or without flesh, your target blocks and dodges, making you fight as if you’re facing a human, not a bloodthirsty beast. While you swing your axe with strength, cutting through the bones isn’t easy, especially when the enemy parries with its own tools.\n\nDuring the clash you take a few hits, but you end up surrounded with crushed and detached bones, gasping for air, yet victorious."
        if armor >= 3:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ custom2 = "Your gambeson stopped any cut it took, protecting your flesh."
        elif armor == 2:
            $ armor = limit_armor(armor-2)
            show minus2armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
            $ custom2 = "Your gambeson stopped any cut it took, protecting your flesh."
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
        elif armor >= 1:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            if pc_hp >= 1:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom2 = "One hit landed on your arm, causing it to bleed slightly."
            else:
                jump oldtunnel_combat_lastclash_dead
        else:
            if pc_hp >= 2:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                $ custom2 = "Your arm is bleeding heavily. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
    elif d100roll <= 20:
        $ minutes += 10
        $ custom1 = "With or without flesh, your target blocks and dodges, making you fight as if you’re facing a human, not a bloodthirsty beast. While you swing your axe with strength, cutting through the bones isn’t easy, especially when the enemy parries with its own tools. At one point, you have to take a few leaps back, disoriented by the rattling and darkness.\n\nDuring the clash you take a few hits, but you end up surrounded with crushed and detached bones, gasping for air, yet victorious."
        if armor >= 3:
            $ armor = limit_armor(armor-2)
            show minus2armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
            $ custom2 = "Your gambeson stopped any cut it took, protecting your flesh."
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
        elif armor == 2:
            $ armor = limit_armor(armor-2)
            show minus2armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
            if pc_hp >= 1:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom2 = "One hit landed on your arm, causing it to bleed slightly."
            else:
                jump oldtunnel_combat_lastclash_dead
        elif armor >= 1:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            if pc_hp >= 2:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "Your arm is bleeding heavily. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
        else:
            if pc_hp >= 3:
                $ minutes += 5
                $ pc_hp = limit_pc_hp(pc_hp-3)
                show minus3hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "Your arm and leg are bleeding heavily. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
    elif d100roll <= 30:
        $ minutes += 10
        $ custom1 = "With or without flesh, your target blocks and dodges, making you fight as if you’re facing a human, not a bloodthirsty beast. You struggle to land any hit, with the weight of your axe hardly compensating for all the parrying, darkness, and rattling. Your brave swings shift into a defensive stance when a powerful blow reaches your back, dangerously close to the spine. You try to lead your enemy to a different spot.\n\nDuring the clash you take quite a few hits, but you end up surrounded with crushed and detached bones, gasping for air. The corridors fall silent."
        if armor >= 3:
            $ armor = limit_armor(armor-3)
            show minus3armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 armor points.{/i}')
            $ custom2 = "Your gambeson stopped any cut it took, protecting your flesh, though barely."
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
        elif armor == 2:
            $ armor = limit_armor(armor-2)
            show minus2armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
            if pc_hp >= 2:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "Your arm is bleeding heavily. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
        elif armor >= 1:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            if pc_hp >= 3:
                $ minutes += 5
                $ pc_hp = limit_pc_hp(pc_hp-3)
                show minus3hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "Your arm and leg are bleeding heavily. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
        else:
            if pc_hp >= 4:
                $ minutes += 10
                $ pc_hp = limit_pc_hp(pc_hp-4)
                show minus4hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "Your arm and stomach are bleeding heavily. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
    elif d100roll <= 40:
        $ minutes += 15
        $ custom1 = "With or without flesh, your target blocks and dodges, making you fight as if you’re facing a human, not a bloodthirsty beast. You struggle to land any hit, with the weight of your axe hardly compensating for all the parrying, darkness, and rattling. Your brave swings shift into a defensive stance when a powerful blow reaches your back, dangerously close to the spine, and is then followed by a strike to your cheek. You try to lead your enemy to a different spot.\n\nFinally, you end up surrounded with crushed and detached bones, gasping for air and hurting. The corridors fall silent."
        if armor >= 3:
            $ armor = limit_armor(armor-3)
            show minus3armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 armor points.{/i}')
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
            if pc_hp >= 1:
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ custom2 = "One hit landed on your arm, causing it to bleed slightly."
            else:
                jump oldtunnel_combat_lastclash_dead
        elif armor == 2:
            $ armor = limit_armor(armor-2)
            show minus2armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
            if pc_hp >= 3:
                $ minutes += 5
                $ pc_hp = limit_pc_hp(pc_hp-3)
                show minus3hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "Your arm and leg are bleeding heavily. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
        elif armor >= 1:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            if pc_hp >= 4:
                $ minutes += 10
                $ pc_hp = limit_pc_hp(pc_hp-4)
                show minus4hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "Your arm and leg are bleeding heavily. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
        else:
            if pc_hp >= 5:
                $ minutes += 15
                $ pc_hp = limit_pc_hp(pc_hp-5)
                show minus5hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "You cough out blood. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
    elif d100roll <= 50:
        $ minutes += 15
        $ custom1 = "With or without flesh, your target blocks and dodges, making you fight as if you’re facing a human, not a bloodthirsty beast. You struggle to land any hit, with the weight of your axe hardly compensating for all the parrying, darkness, and rattling. Your brave swings turn into a desperate fight for survival when a powerful blow reaches your back, dangerously close to the spine, and is then followed by a strike to your cheek.\n\nFinally, you end up surrounded with crushed and detached bones, hurting so much you have tears in your eyes. The corridors fall silent."
        if armor >= 3:
            $ armor = limit_armor(armor-4)
            show minus4armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 armor points.{/i}')
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
            if pc_hp >= 2:
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "Your arm is bleeding heavily. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
        elif armor == 2:
            $ armor = limit_armor(armor-2)
            show minus2armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
            if pc_hp >= 4:
                $ minutes += 10
                $ pc_hp = limit_pc_hp(pc_hp-4)
                show minus4hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "You cough out blood. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
        elif armor >= 1:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            if pc_hp >= 5:
                $ minutes += 15
                $ pc_hp = limit_pc_hp(pc_hp-5)
                show minus5hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "You cough out blood. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
        else:
            if pc_hp >= 5:
                $ minutes += 15
                $ pc_hp = limit_pc_hp(pc_hp-5)
                show minus5hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "You cough out blood. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
    else:
        $ custom1 = "With or without flesh, your target blocks and dodges, making you fight as if you’re facing a human, not a bloodthirsty beast. You struggle to land any hit, with the weight of your axe hardly compensating for all the parrying, darkness, and rattling. Your brave swings turn into a desperate fight for survival when a powerful blow reaches your back, sending you into the ground, where you take a strong blow to your cheek. You crawl away before getting to your feet once more, seeking hope in starting anew.\n\nFinally, you end up surrounded with crushed and detached bones, hurting so much you have tears in your eyes. The corridors fall silent."
        if armor >= 3:
            $ armor = limit_armor(armor-4)
            show minus4armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 armor points.{/i}')
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
            if pc_hp >= 3:
                $ minutes += 5
                $ pc_hp = limit_pc_hp(pc_hp-3)
                show minus3hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "Your arm and leg are bleeding heavily. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
        elif armor == 2:
            $ armor = limit_armor(armor-2)
            show minus2armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
            if not cleanliness_clothes_torn:
                $ cleanliness_clothes_torn = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
            if pc_hp >= 4:
                $ minutes += 10
                $ pc_hp = limit_pc_hp(pc_hp-4)
                show minus4hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "You cough out blood. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
        elif armor >= 1:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            if pc_hp >= 5:
                $ minutes += 15
                $ pc_hp = limit_pc_hp(pc_hp-5)
                show minus5hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "You cough out blood. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
        else:
            if pc_hp >= 5:
                $ minutes += 15
                $ pc_hp = limit_pc_hp(pc_hp-5)
                show minus5hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
                if not cleanliness_clothes_blood:
                    $ cleanliness_clothes_blood = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom2 = "You cough out blood. You search your bags for bandages."
            else:
                jump oldtunnel_combat_lastclash_dead
    $ pc_battlecounter += 2
    $ oldtunnel_inside_undead_defeated = 1
    $ oldtunnel_inside_undead_defeated_bypc = 1
    $ oldtunnel_exploration_combat = 0
    $ oldtunnel_inside_undead_amount = 0
    $ oldtunnel_inside_undead_hp = 0
    menu:
        '[custom3] [custom1] [custom2]
        '
        'I’ll decide what to do with the corpses after I leave the tunnel.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll decide what to do with the corpses after I leave the tunnel.')
            stop music fadeout 4.0
            if oldtunnel_exploration_position == 1:
                play nature "audio/ambient/oldtunnelinside01.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            if oldtunnel_exploration_position == 2:
                play nature "audio/ambient/oldtunnelinside02.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            if oldtunnel_exploration_position == 3:
                play nature "audio/ambient/oldtunnelinside02.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            if oldtunnel_exploration_position == 4:
                play nature "audio/ambient/oldtunnelinside03.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            if oldtunnel_exploration_position == 5:
                play nature "audio/ambient/oldtunnelinside04.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            if oldtunnel_exploration_position == 6:
                play nature "audio/ambient/oldtunnelinside05.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            if oldtunnel_exploration_position == 8:
                play nature "audio/ambient/oldtunnelinside04.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            if oldtunnel_exploration_position == 10:
                play nature "audio/ambient/oldtunnelinside06alt.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            if oldtunnel_exploration_position == 11:
                play nature "audio/ambient/oldtunnelinside06alt.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            if oldtunnel_exploration_position == 14:
                play nature "audio/ambient/oldtunnelinside02.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            if oldtunnel_exploration_position == 15:
                play nature "audio/ambient/oldtunnelinside07.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            if oldtunnel_exploration_position == 18:
                play nature "audio/ambient/oldtunnelinside07.ogg" fadeout 2.0 fadein 4.0 volume 1.0
            $ can_items = 1
            $ can_potions = 1
            if not quest_closedtunnel_description03:
                $ renpy.notify("Journal updated: The Closed Tunnel")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Closed Tunnel{/i}')
                if quest_closedtunnel_description00:
                    $ quest_closedtunnel_description03 = "The undead are destroyed, but I still need to open the gate."
                else:
                    $ quest_closedtunnel_description03 = "The undead are destroyed, but I still need to make sure the tunnel can be crossed."
            if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                $ pc_faithpoints_opportunities += 1
            if oldtunnel_exploration_position == 1:
                jump oldtunnel_exploration_scrap01
            if oldtunnel_exploration_position == 2:
                jump oldtunnel_exploration_scrap02
            if oldtunnel_exploration_position == 3:
                jump oldtunnel_exploration_scrap03
            if oldtunnel_exploration_position == 4:
                jump oldtunnel_exploration_scrap04
            if oldtunnel_exploration_position == 5:
                jump oldtunnel_exploration_scrap05
            if oldtunnel_exploration_position == 6:
                jump oldtunnel_exploration_scrap06
            if oldtunnel_exploration_position == 8:
                jump oldtunnel_exploration_scrap08
            if oldtunnel_exploration_position == 10:
                jump oldtunnel_exploration_scrap10
            if oldtunnel_exploration_position == 11:
                jump oldtunnel_exploration_scrap11
            if oldtunnel_exploration_position == 14:
                jump oldtunnel_exploration_scrap14
            if oldtunnel_exploration_position == 15:
                jump oldtunnel_exploration_scrap15
            if oldtunnel_exploration_position == 18:
                jump oldtunnel_exploration_scrap18

label oldtunnel_combat_lastclash_dead:
    if pc_religion == "pagan":
        show areapicture gameover_alt at basicfade
    else:
        show areapicture gameover at basicfade
    $ can_potions = 0
    $ can_items = 0
    hide screen oldtunnel
    $ pc_hp = limit_pc_hp(pc_hp-5)
    show minus5hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality point.{/i}')
    menu:
        '[custom3] With or without flesh, your target blocks and dodges, making you fight as if you’re facing a human, not a bloodthirsty beast. You struggle to land any hit, with the weight of your axe hardly compensating for all the parrying, darkness, and rattling. A powerful blow reaches your back, sending you into the ground, where you take a kick in your cheek.
        \n\nYou crawl away, but the thin fingers are already on your neck.
        \n
        \n\n[pcname]’s soul has left its shell.
        '
        'Let me replay this encounter.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this encounter.')
            stop music fadeout 4.0
            $ renpy.load("combatsave")
