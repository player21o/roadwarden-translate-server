###################### ASTERION + HIGH ISLAND RETURN
default highisland_returned = 0
default asterion_found = 0
default asterion_highisland_knowsabout = 0
default asterion_highisland_clues = 0
default highisland_howtoreach_pcknows = 0
default asterion_found_burnt = 0
default asterion_found_pcthought = 0 # "readyforanadventure", "readytoplayitsafe", "annoyedwithunsolvedmystery", "readytoletthemysterygo", "believeshewasrational", "doesntcareatall", "pchasseriousdoubts", "pchasseriousdoubts2"
default asterion_lie = 0 #"monsters", "bandits", "solitude"
default asterion_found_searched = 0
default asterion_found_cave_examined = 0
default asterion_found_cave_examined_picked = 0
default asterion_found_cave_tagged = 0
default asterion_found_cave_crew_aegidia = 0
default highisland_crew_returning = 0

label highisland_volcanoALL:
    label highisland_solo_asterionALL:
        label highisland_solo_volcano01:
            stop music fadeout 8.0
            play nature "audio/ambient/highisland02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            show areapicture hi_volcano01 at basicfade
            $ world_known_areas += 1
            menu:
                'The howling wind pushes you up the short path, between the tufts of grass, sparse yellow flowers, dormant ashes, and trails of cold lava. Your legs, unused to such long wayfaring, ache.
                \n\nIn the moonlight you see heavy boot prints that lead only in one direction.
                '
                'I follow them slowly, looking out for animals.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow them slowly, looking out for animals.')
                    show areapicture hi_volcano02 at basicfade
                    menu:
                        'There aren’t many signs of the past dwellers. The burnt cart, the collapsed shed, the digging tools made of antler or rusty steel.
                        \n\nThe trail ends at the cave mouth. The leaves of the gate are made of stone, now ajar. You push aside the battering ram.
                        '
                        'I drop my heavy bags by the entrance and prepare myself to fight in the narrow corridors.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop my heavy bags by the entrance and prepare myself to fight in the narrow corridors.')
                            play nature "audio/ambient/highisland03.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                            show areapicture hi_asterioncave01 at basicfade
                            if not highisland_lightsource:
                                $ custom1 = "Before you step into complete darkness, you prepare one of your last candles."
                            else:
                                $ custom1 = "The light you’re carrying guides you through the complete darkness."
                            menu:
                                '[custom1] The polished walls of the tunnel, free of pointy rocks, were no doubt carved by human hands.
                                \n\nYour steps are loud, unlike the gentle draft and the deep stream. You pass by another corridor, buried by the mountain.
                                \n\nYou stop in place. Something behind the corner kicked a rock that is now rolling on the floor.
                                '
                                '“{color=#f6d6bd}Asterion{/color}?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Asterion{/color}?”')
                                    $ custom1 = "The ghastly scream of a human-like throat makes you take a defensive stance, but, despite the passing breaths, no attack follows. Holding the light in front of you, you reach the next chamber."
                                    jump highisland_solo_asterion01
                                'I sneak forward, with my axe ready to strike.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sneak forward, with my axe ready to strike.')
                                    $ custom1 = "Holding the light in front of you, you reach the next chamber, where you’re greeted by the ghastly scream of a human-like throat. You step away, taking a defensive stance, but, despite the passing breaths, no attack follows. You enter again."
                                    jump highisland_solo_asterion01

        label highisland_solo_asterion01:
            show areapicture hi_asterioncave02 at basicfade
            $ renpy.music.play("audio/track_19asterion.ogg", channel=u'music', loop=None, fadeout=1.0, synchro_start=False, fadein=0, tight=None, if_changed=False, relative_volume=1.0)
            stop nature fadeout 4.0
            menu:
                '[custom1]
                \n\nThe undead is furiously squirming in its attempts to release itself, alternately pulling the spear that’s nailing it to the wall and reaching toward you, as if it’s hoping you’ll fall into its embrace. There are no other corpses in sight - the creature must be starving.
                '
                'I need to be sure it’s him.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to be sure it’s him.')
                    menu:
                        'The half-rotten flesh and the worn, torn tunic tell you little, but {color=#f6d6bd}Asterion’s{/color} short shell is still wearing the mail you were told about, now rusty, even more clangy than a new set. Some of the red hair and beard remain on the monstrous, pale face, but most of their strands are all over the floor.
                        \n\nThe knees of the creature are shattered. Next to them rests a large rock.
                        '
                        'A monster caught him here, something with great strength.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- A monster caught him here, something with great strength.')
                            jump highisland_solo_asterion01a
                        'He knew he was going to die, so he imprisoned himself here.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- He knew he was going to die, so he imprisoned himself here.')
                            jump highisland_solo_asterion01a
                        'He was betrayed, or maybe fell into some sort of a trap, then crawled in here.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- He was betrayed, or maybe fell into some sort of a trap, then crawled in here.')
                            label highisland_solo_asterion01a:
                                menu:
                                    'You step closer. The undead does its best to throw itself at you, but it’s not strong enough.
                                    '
                                    'I raise my blade. A few blows to the head should be enough.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise my blade. A few blows to the head should be enough.')
                                        $ custom1 = "When the shell stops moving, the dead hand is still clenched on your gambeson. The corpse leans forward, loosely resting on the haft of the spear. The pieces of the skull are scattered over the chamber."
                                        jump highisland_solo_asterion02
                                    'I prepare {color=#f6d6bd}Asterion’s{/color} spear.' if item_asterionspear:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare {color=#f6d6bd}Asterion’s{/color} spear.')
                                        $ custom1 = "You avoid the awkward grasp of the dead hand and land a few precise hits, scattering the pieces of the skull over the chamber. The corpse leans forward, loosely resting on the haft of the spear."
                                        jump highisland_solo_asterion02
                                    'I prepare my spear.' if not item_asterionspear and item_mountainroadspear:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my spear.')
                                        $ custom1 = "You avoid the awkward grasp of the dead hand and land a few precise hits, scattering the pieces of the skull over the chamber. The corpse leans forward, loosely resting on the haft of the spear."
                                        jump highisland_solo_asterion02
                                    'I just need one precise shot from my crossbow.' if item_crossbow and item_crossbowquarrels:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just need one precise shot from my crossbow.')
                                        $ item_crossbowquarrels -= 1
                                        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                                        $ custom1 = "The quarrel shatters the skull, scattering its pieces over the chamber. The corpse leans forward, loosely resting on the haft of the spear."
                                        jump highisland_solo_asterion02
                                    'I pick up the rock.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick up the rock.')
                                        $ custom1 = "When the shell stops moving, the dead hand is still clenched on your gambeson. The corpse leans forward, loosely resting on the haft of the spear. The pieces of the skull are scattered over the chamber."
                                        jump highisland_solo_asterion02

        label highisland_solo_asterion02:
            play nature "audio/ambient/highisland03.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            show areapicture hi_asterioncave03 at basicfade
            $ asterion_found = 1
            $ asterion_highisland_knowsabout = 1
            $ quest_asterion_description00asterion_highisland_knowsabout = "I discovered that {color=#f6d6bd}Asterion{/color} died during his lonely journey to an isolated island."
            if not quest_asterion_description00lies and not quest_asterion_description00gaveup:
                $ renpy.notify("Journal updated: Find the Roadwarden")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
            else:
                $ quest_asterion = 2
                $ renpy.notify("Quest completed: Find the Roadwarden")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Find the Roadwarden{/i}')
            menu:
                '[custom1]
                '
                'I search the shell’s bundles.' if not asterion_found_searched:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the shell’s bundles.')
                    $ asterion_found_searched = 1
                    if quest_asterion_description02:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                    else:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    $ coins += 20
                    show screen notifyimage( "+20", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+20 {image=cointest}{/i}')
                    jump highisland_solo_asterion02loop
                'I examine the cave.' if not asterion_found_cave_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the cave.')
                    $ asterion_found_cave_examined = 1
                    $ custom1 = "The centuries-old “treasure” spread among the collapsed racks and chests is mostly beyond use, but you do notice a few tools and statuettes made of now-green bronze. Judging by the simplicity of the chamber, it was likely little more than a basic storage room.\n\nThe corridors leading to the deeper caves have all been buried by time."
                    jump highisland_solo_asterion02loop
                'I can’t carry some trash through the woods on my own. (disabled)' if asterion_found_cave_examined and not asterion_found_cave_examined_picked:
                    pass
                'I carve my name on a wall with the magic chisel.' if item_magicchisel == 1 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with the magic chisel.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The soft hits of the butt of your axe result in sharp, deep cuts. Letter by letter, you leave behind the marks of your presence, then step away."
                    jump highisland_solo_asterion02tagging
                'I carve my name on a wall with The Tool of Destruction.' if item_magicchisel == 2 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with The Tool of Destruction.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The first hit with the butt of your weapon makes a pickaxe-worthy hole, so you try again in a different spot, trying to be as gentle as you can. Letter by letter, you leave behind the deep marks of your presence, then step away."
                    jump highisland_solo_asterion02tagging
                'I need to get back to the boat before sunrise.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to get back to the boat before sunrise.')
                    jump highisland_solo_asterion03

        label highisland_solo_asterion02tagging:
            menu:
                '[custom1] “[pcname],” you read out loud.
                '
                'I search the shell’s bundles.' if not asterion_found_searched:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the shell’s bundles.')
                    $ asterion_found_searched = 1
                    if quest_asterion_description02:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                    else:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    $ coins += 20
                    show screen notifyimage( "+20", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+20 {image=cointest}{/i}')
                    jump highisland_solo_asterion02loop
                'I examine the cave.' if not asterion_found_cave_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the cave.')
                    $ asterion_found_cave_examined = 1
                    $ custom1 = "The centuries-old “treasure” spread among the collapsed racks and chests is mostly beyond use, but you do notice a few tools and statuettes made of now-green bronze. Judging by the simplicity of the chamber, it was likely little more than a basic storage room.\n\nThe corridors leading to the deeper caves have all been buried by time."
                    jump highisland_solo_asterion02loop
                'I can’t carry some trash through the woods on my own. (disabled)' if asterion_found_cave_examined and not asterion_found_cave_examined_picked:
                    pass
                'I carve my name on a wall with the magic chisel.' if item_magicchisel == 1 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with the magic chisel.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The soft hits of the butt of your axe result in sharp, deep cuts. Letter by letter, you leave behind the marks of your presence, then step away."
                    jump highisland_solo_asterion02tagging
                'I carve my name on a wall with The Tool of Destruction.' if item_magicchisel == 2 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with The Tool of Destruction.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The first hit with the butt of your weapon makes a pickaxe-worthy hole, so you try again in a different spot, trying to be as gentle as you can. Letter by letter, you leave behind the deep marks of your presence, then step away."
                    jump highisland_solo_asterion02tagging
                'I need to get back to the boat before sunrise.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to get back to the boat before sunrise.')
                    jump highisland_solo_asterion03

        label highisland_solo_asterion02loop:
            menu:
                '[custom1]
                '
                'I search the shell’s bundles.' if not asterion_found_searched:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the shell’s bundles.')
                    $ asterion_found_searched = 1
                    if quest_asterion_description02:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                    else:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    $ coins += 20
                    show screen notifyimage( "+20", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+20 {image=cointest}{/i}')
                    jump highisland_solo_asterion02loop
                'I examine the cave.' if not asterion_found_cave_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the cave.')
                    $ asterion_found_cave_examined = 1
                    $ custom1 = "The centuries-old “treasure” spread among the collapsed racks and chests is mostly beyond use, but you do notice a few tools and statuettes made of now-green bronze. Judging by the simplicity of the chamber, it was likely little more than a basic storage room.\n\nThe corridors leading to the deeper caves have all been buried by time."
                    jump highisland_solo_asterion02loop
                'I can’t carry some trash through the woods on my own. (disabled)' if asterion_found_cave_examined and not asterion_found_cave_examined_picked:
                    pass
                'I carve my name on a wall with the magic chisel.' if item_magicchisel == 1 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with the magic chisel.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The soft hits of the butt of your axe result in sharp, deep cuts. Letter by letter, you leave behind the marks of your presence, then step away."
                    jump highisland_solo_asterion02tagging
                'I carve my name on a wall with The Tool of Destruction.' if item_magicchisel == 2 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with The Tool of Destruction.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The first hit with the butt of your weapon makes a pickaxe-worthy hole, so you try again in a different spot, trying to be as gentle as you can. Letter by letter, you leave behind the deep marks of your presence, then step away."
                    jump highisland_solo_asterion02tagging
                'I need to get back to the boat before sunrise.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to get back to the boat before sunrise.')
                    jump highisland_solo_asterion03

        label highisland_solo_asterion03:
            menu:
                'You spare the corpse one more look.
                '
                'I should burn the bones.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should burn the bones.')
                    $ asterion_found_burnt = 1
                    $ achievement_pyrepoints += 1
                    $ custom1 = "You surround {color=#f6d6bd}Asterion’s{/color} shell with a few wooden logs and some of his own possessions. The smoke drives you outside.\n\n"
                    jump highisland_solo_asterion03a
                'There’s no time to waste.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- There’s no time to waste.')
                    $ custom1 = ""
                    label highisland_solo_asterion03a:
                        stop music fadeout 8.0
                        play nature "audio/ambient/highisland02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                        show areapicture hi_volcano01 at basicfade
                        $ can_potions = 1
                        $ can_items = 1
                        if (pc_hp >= 4) or (pc_food >= 3 and pc_hp >= 3) or (pc_food >= 2 and armor >= 2 and pc_hp >= 3) or (pc_food >= 1 and armor >= 3 and pc_hp >= 3) or (armor >= 4 and pc_hp >= 3) or (pc_food >= 4 and pc_hp >= 2) or (pc_food >= 3 and armor >= 2 and pc_hp >= 2) or (pc_food >= 2 and armor >= 3 and pc_hp >= 2) or (pc_food >= 1 and armor >= 4 and pc_hp >= 2):
                            $ custom2 = "You may be running short on supplies, but as long as you can manage to follow the same trail, you should be able to reach the harbor before the low tide."
                        else:
                            $ custom2 = "You’re exhausted. You could try to reach the harbor before the low tide, but the chances are against you. You think of your supplies - if there’s anything left, you should use it now."
                        menu:
                            '[custom1]The fresh air makes you yawn. You grab your bags and approach the edge of the scarp, observing the woods of {color=#f6d6bd}High Island{/color}. You recognize the trail that led you here from the valley of the saurians. [custom2]
                            '
                            'I’m strong, I’m prepared. I can do this.' ( condition="(pc_hp >= 4) or (pc_food >= 3 and pc_hp >= 3) or (pc_food >= 2 and armor >= 2 and pc_hp >= 3) or (pc_food >= 1 and armor >= 3 and pc_hp >= 3) or (armor >= 4 and pc_hp >= 3) or (pc_food >= 4 and pc_hp >= 2) or (pc_food >= 3 and armor >= 2 and pc_hp >= 2) or (pc_food >= 2 and armor >= 3 and pc_hp >= 2) or (pc_food >= 1 and armor >= 4 and pc_hp >= 2)" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m strong, I’m prepared. I can do this.')
                                jump highisland_returning00
                            'Judging by my condition, I know I won’t make it. (disabled)' ( condition="not (pc_hp >= 4) and not (pc_food >= 3 and pc_hp >= 3) and not (pc_food >= 2 and armor >= 2 and pc_hp >= 3) and not (pc_food >= 1 and armor >= 3 and pc_hp >= 3) and not (armor >= 4 and pc_hp >= 3) and not (pc_food >= 4 and pc_hp >= 2) and not (pc_food >= 3 and armor >= 2 and pc_hp >= 2) and not (pc_food >= 2 and armor >= 3 and pc_hp >= 2) and not (pc_food >= 1 and armor >= 4 and pc_hp >= 2)" ):
                                pass
                            'Still, I’ve got to try to get back.' ( condition="not (pc_hp >= 4) and not (pc_food >= 3 and pc_hp >= 3) and not (pc_food >= 2 and armor >= 2 and pc_hp >= 3) and not (pc_food >= 1 and armor >= 3 and pc_hp >= 3) and not (armor >= 4 and pc_hp >= 3) and not (pc_food >= 4 and pc_hp >= 2) and not (pc_food >= 3 and armor >= 2 and pc_hp >= 2) and not (pc_food >= 2 and armor >= 3 and pc_hp >= 2) and not (pc_food >= 1 and armor >= 4 and pc_hp >= 2)" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Still, I’ve got to try to get back.')
                                $ pc_dead = 1
                                $ endgame_epilogue_fluff = "highisland"
                                jump hovlavan_road01

    label highisland_howlers_asterionALL:
        label highisland_howlers_volcano01:
            stop music fadeout 8.0
            play nature "audio/ambient/highisland02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            show areapicture hi_volcano01 at basicfade
            $ world_known_areas += 1
            menu:
                '{color=#f6d6bd}The guards{/color} walk in silence. The howling wind pushes you up the short path, between the tufts of grass, sparse yellow flowers, dormant ashes, and trails of cold lava. Your legs, unused to such long wayfaring, ache.
                \n\n{color=#f6d6bd}The one with the bow{/color} kneels down on the poorly lit ground. “Someone was here, long ago,” she says, “but went only in one direction.”
                '
                'I nod, but keep looking out for animals.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod, but keep looking out for animals.')
                    show areapicture hi_volcano02 at basicfade
                    menu:
                        'There aren’t many signs of the past dwellers. The burnt cart, the collapsed shed, the digging tools made of antler or rusty steel.
                        \n\nThe trail ends at the cave mouth. The leaves of the gate are made of stone, now ajar. You push aside the battering ram.
                        '
                        'I drop my heavy bags on the ground. “Be ready to fight in narrow corridors.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop my heavy bags on the ground. “Be ready to fight in narrow corridors.”')
                            play nature "audio/ambient/highisland03.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                            show areapicture hi_asterioncave01 at basicfade
                            if not highisland_lightsource:
                                $ custom1 = "Before you step into complete darkness, {color=#f6d6bd}the young druid{/color} prepares one of your last torches."
                            else:
                                $ custom1 = "The light you’re carrying guides your group through the complete darkness."
                            menu:
                                '[custom1] The polished walls of the tunnel, free of pointy rocks, were no doubt carved by human hands.
                                \n\nYour steps are loud, unlike the gentle draft and the deep stream. You pass by another corridor, buried by the mountain.
                                \n\n{color=#f6d6bd}The leader{/color} gestures for everyone to wait. Something behind the corner kicked a rock that is now rolling on the floor.
                                '
                                '“{color=#f6d6bd}Asterion{/color}?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Asterion{/color}?”')
                                    $ custom1 = "The ghastly scream of a human-like throat makes you take a defensive stance, but, despite the passing breaths, no attack follows. Holding the light in front of you, you reach the next chamber."
                                    jump highisland_howlers_asterion01
                                'I sneak forward, with my axe ready to strike.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sneak forward, with my axe ready to strike.')
                                    $ custom1 = "Holding the light in front of you, you reach the next chamber, where you’re greeted by the ghastly scream of a human-like throat. You step away, taking a defensive stance, but, despite the passing breaths, no attack follows. You enter again."
                                    jump highisland_howlers_asterion01

        label highisland_howlers_asterion01:
            show areapicture hi_asterioncave02 at basicfade
            $ renpy.music.play("audio/track_19asterion.ogg", channel=u'music', loop=None, fadeout=1.0, synchro_start=False, fadein=0, tight=None, if_changed=False, relative_volume=1.0)
            stop nature fadeout 4.0
            if not highisland_howlersguards_spearwoman_dead:
                $ custom2 = "{color=#f6d6bd}The one with a spear{/color} lets out a sigh. “Is this the one?”"
            else:
                $ custom2 = "{color=#f6d6bd}The leader{/color} lets out a sigh. “So? Was that him?”"
            menu:
                '[custom1]
                \n\nThe undead is furiously squirming in its attempts to release itself, alternately pulling the spear that’s nailing it to the wall and reaching toward you, as if it’s hoping you’ll fall into its embrace. There are no other corpses in sight - the creature must be starving.
                \n\n[custom2]
                '
                '“Let me take a look.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me take a look.”')
                    menu:
                        'The half-rotten flesh and the worn, torn tunic tell you little, but {color=#f6d6bd}Asterion’s{/color} short shell is still wearing the mail you were told about, now rusty, even more clangy than a new set. Some of the red hair and beard remain on the monstrous, pale face, but most of their strands are all over the floor.
                        \n\nThe knees of the creature are shattered. Next to them rests a large rock.
                        \n\n“What happened?” {color=#f6d6bd}The young druid’s{/color} voice carries a mixture of concern and annoyance.
                        '
                        '“A monster caught him here, something with great strength.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A monster caught him here, something with great strength.”')
                            jump highisland_howlers_asterion01a
                        '“He knew he was going to die, so he imprisoned himself here.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He knew he was going to die, so he imprisoned himself here.”')
                            jump highisland_howlers_asterion01a
                        '“He was betrayed, or maybe fell into some sort of a trap, then crawled in here.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He was betrayed, or maybe fell into some sort of a trap, then crawled in here.”')
                            label highisland_howlers_asterion01a:
                                menu:
                                    'You step closer. The undead does its best to throw itself at you, but it’s not strong enough.
                                    '
                                    'I raise my blade. A few blows to the head should be enough.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise my blade. A few blows to the head should be enough.')
                                        jump highisland_howlers_asterion02
                                    'I prepare {color=#f6d6bd}Asterion’s{/color} spear.' if item_asterionspear:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare {color=#f6d6bd}Asterion’s{/color} spear.')
                                        jump highisland_howlers_asterion02
                                    'I prepare my spear.' if not item_asterionspear and item_mountainroadspear:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my spear.')
                                        jump highisland_howlers_asterion02
                                    'I just need one precise shot from my crossbow.' if item_crossbow and item_crossbowquarrels:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just need one precise shot from my crossbow.')
                                        jump highisland_howlers_asterion02
                                    'I pick up the rock.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick up the rock.')
                                        jump highisland_howlers_asterion02

        label highisland_howlers_asterion02:
            play nature "audio/ambient/highisland03.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            show areapicture hi_asterioncave03 at basicfade
            $ asterion_found = 1
            $ quest_asterion_description00asterion_highisland_knowsabout = "I discovered that {color=#f6d6bd}Asterion{/color} died during his lonely journey to an isolated island."
            if not quest_asterion_description00lies and not quest_asterion_description00gaveup:
                $ renpy.notify("Journal updated: Find the Roadwarden")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
            else:
                $ quest_asterion = 2
                $ renpy.notify("Quest completed: Find the Roadwarden")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Find the Roadwarden{/i}')
            menu:
                'Before you make a decision, {color=#f6d6bd}the one with the mace{/color} lets out a shout, takes a few steps forward, and smashes the skull to pieces, scattering them over the chamber. The corpse leans forward, loosely resting on the haft of the spear.
                \n\n{color=#f6d6bd}The leader{/color} nods with approval and looks at the others. “See if there’s anything of value left.”
                '
                'I search the shell’s bundles.' if not asterion_found_searched:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the shell’s bundles.')
                    $ asterion_found_searched = 1
                    if quest_asterion_description02:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                    else:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    $ coins += 20
                    show screen notifyimage( "+20", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+20 {image=cointest}{/i}')
                    jump highisland_howlers_asterion02loop
                'I examine the cave.' if not asterion_found_cave_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the cave.')
                    $ asterion_found_cave_examined = 1
                    $ custom1 = "The centuries-old “treasure” spread among the collapsed racks and chests is mostly beyond use, but you do notice a few tools and statuettes made of now-green bronze. Judging by the simplicity of the chamber, it was likely little more than a basic storage room. The corridors leading to the deeper caves have all been buried by time.\n\nSeeing how your “crew” fills up their bags with pieces of copper and iron, you think about {color=#f6d6bd}Thais{/color}. She wouldn’t send this group here just for {i}your{/i} sake."
                    jump highisland_howlers_asterion02loop
                'I carve my name on a wall with the magic chisel.' if item_magicchisel == 1 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with the magic chisel.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The soft hits of the butt of your axe result in sharp, deep cuts. Letter by letter, you leave behind the marks of your presence, then step away."
                    jump highisland_howlers_asterion02tagging
                'I carve my name on a wall with The Tool of Destruction.' if item_magicchisel == 2 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with The Tool of Destruction.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The first hit with the butt of your weapon makes a pickaxe-worthy hole, so you try again in a different spot, trying to be as gentle as you can. Letter by letter, you leave behind the deep marks of your presence, then step away."
                    jump highisland_howlers_asterion02tagging
                '“We need to reach the boat before the sun rises.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We need to reach the boat before the sun rises.”')
                    jump highisland_howlers_asterion03

        label highisland_howlers_asterion02tagging:
            menu:
                '[custom1] “[pcname],” you read in silence.
                '
                'I search the shell’s bundles.' if not asterion_found_searched:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the shell’s bundles.')
                    $ asterion_found_searched = 1
                    if quest_asterion_description02:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                    else:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    $ coins += 20
                    show screen notifyimage( "+20", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+20 {image=cointest}{/i}')
                    jump highisland_howlers_asterion02loop
                'I examine the cave.' if not asterion_found_cave_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the cave.')
                    $ asterion_found_cave_examined = 1
                    $ custom1 = "The centuries-old “treasure” spread among the collapsed racks and chests is mostly beyond use, but you do notice a few tools and statuettes made of now-green bronze. Judging by the simplicity of the chamber, it was likely little more than a basic storage room. The corridors leading to the deeper caves have all been buried by time.\n\nSeeing how your “crew” fills up their bags with pieces of copper and iron, you think about {color=#f6d6bd}Thais{/color}. She wouldn’t send this group here just for {i}your{/i} sake."
                    jump highisland_howlers_asterion02loop
                'I carve my name on a wall with the magic chisel.' if item_magicchisel == 1 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with the magic chisel.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The soft hits of the butt of your axe result in sharp, deep cuts. Letter by letter, you leave behind the marks of your presence, then step away."
                    jump highisland_howlers_asterion02tagging
                'I carve my name on a wall with The Tool of Destruction.' if item_magicchisel == 2 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with The Tool of Destruction.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The first hit with the butt of your weapon makes a pickaxe-worthy hole, so you try again in a different spot, trying to be as gentle as you can. Letter by letter, you leave behind the deep marks of your presence, then step away."
                    jump highisland_howlers_asterion02tagging
                '“We need to reach the boat before the sun rises.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We need to reach the boat before the sun rises.”')
                    jump highisland_howlers_asterion03

        label highisland_howlers_asterion02loop:
            menu:
                '[custom1]
                '
                'I search the shell’s bundles.' if not asterion_found_searched:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the shell’s bundles.')
                    $ asterion_found_searched = 1
                    if quest_asterion_description02:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                    else:
                        $ custom1 = "Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    $ coins += 20
                    show screen notifyimage( "+20", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+20 {image=cointest}{/i}')
                    jump highisland_howlers_asterion02loop
                'I examine the cave.' if not asterion_found_cave_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the cave.')
                    $ asterion_found_cave_examined = 1
                    $ custom1 = "The centuries-old “treasure” spread among the collapsed racks and chests is mostly beyond use, but you do notice a few tools and statuettes made of now-green bronze. Judging by the simplicity of the chamber, it was likely little more than a basic storage room. The corridors leading to the deeper caves have all been buried by time.\n\nSeeing how your “crew” fills up their bags with pieces of copper and iron, you think about {color=#f6d6bd}Thais{/color}. She wouldn’t send this group here just for {i}your{/i} sake."
                    jump highisland_howlers_asterion02loop
                'I carve my name on a wall with the magic chisel.' if item_magicchisel == 1 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with the magic chisel.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The soft hits of the butt of your axe result in sharp, deep cuts. Letter by letter, you leave behind the marks of your presence, then step away."
                    jump highisland_howlers_asterion02tagging
                'I carve my name on a wall with The Tool of Destruction.' if item_magicchisel == 2 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with The Tool of Destruction.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The first hit with the butt of your weapon makes a pickaxe-worthy hole, so you try again in a different spot, trying to be as gentle as you can. Letter by letter, you leave behind the deep marks of your presence, then step away."
                    jump highisland_howlers_asterion02tagging
                '“We need to reach the boat before the sun rises.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We need to reach the boat before the sun rises.”')
                    jump highisland_howlers_asterion03

        label highisland_howlers_asterion03:
            menu:
                'You spare the corpse one more look.
                '
                '“We should burn the bones.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should burn the bones.”')
                    $ custom1 = "“Do ne make me laugh,” {color=#f6d6bd}the archeress’{/color} voice is nowhere near laughter. “Let’s keep on going.” You look at {color=#f6d6bd}the leader{/color}, but his scowl makes it clear you won’t have the last word.\n\n"
                    jump highisland_howlers_asterion03a
                'There’s no time to waste.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- There’s no time to waste.')
                    $ custom1 = ""
                    label highisland_howlers_asterion03a:
                        stop music fadeout 8.0
                        play nature "audio/ambient/highisland02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                        show areapicture hi_volcano01 at basicfade
                        $ can_potions = 1
                        $ can_items = 1
                        menu:
                            '[custom1]The fresh air makes you yawn. You grab your bags and approach the edge of the scarp, observing the woods of {color=#f6d6bd}High Island{/color}. You recognize the trail that led you here from the valley of the saurians.
                            '
                            '“Let’s try to follow the same trail. We should be able to reach the harbor before the low tide.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s try to follow the same trail. We should be able to reach the harbor before the low tide.”')
                                jump highisland_returning00

    label highisland_crew_asterionALL:
        label highisland_crew_volcano01:
            stop music fadeout 8.0
            play nature "audio/ambient/highisland02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            show areapicture hi_volcano01 at basicfade
            $ world_known_areas += 1
            if dalit_highisland_joined:
                $ custom11 = "{color=#f6d6bd}Dalit{/color} kneels down on the poorly lit ground. “Someone was here, long ago,” she says, “but went only in one direction.”"
            elif efren_highisland_joined:
                $ custom11 = "{color=#f6d6bd}Efren{/color} kneels down on the poorly lit ground. “There are boot prints here,” he says, “but they lead only one way.”"
            elif aegidia_highisland_joined:
                $ custom11 = "{color=#f6d6bd}Aegidia{/color} kneels down on the poorly lit ground. “Someone was here, long ago,” she says, “but went only in one direction.”"
            elif pyrrhos_highisland_joined:
                $ custom11 = "{color=#f6d6bd}Pyrrhos{/color} kneels down on the poorly lit ground. “Someone was here, long ago,” he says, “but went only in one direction.”"
            else:
                $ custom11 = "In the moonlight you see heavy boot prints that lead only in one direction."
            menu:
                'The howling wind pushes your crew up the short path, between the tufts of grass, sparse yellow flowers, dormant ashes, and trails of cold lava. Your legs, unused to such long wayfaring, ache.
                \n\n[custom11]
                '
                'I follow them slowly, looking out for animals.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow them slowly, looking out for animals.')
                    show areapicture hi_volcano02 at basicfade
                    if quintus_highisland_joined:
                        $ custom11 = " “Less work for us,” chuckles {color=#f6d6bd}Quintus{/color}."
                    else:
                        $ custom11 = ""
                    menu:
                        'There aren’t many signs of the past dwellers. The burnt cart, the collapsed shed, the digging tools made of antler or rusty steel.
                        \n\nThe trail ends at the cave mouth. The leaves of the gate are made of stone, now ajar. You push aside the battering ram.[custom11]
                        '
                        'I drop my heavy bags on the ground. “Be ready to fight in narrow corridors.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop my heavy bags on the ground. “Be ready to fight in narrow corridors.”')
                            play nature "audio/ambient/highisland03.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                            show areapicture hi_asterioncave01 at basicfade
                            if not highisland_lightsource:
                                $ custom1 = "Before your group steps into complete darkness, you prepare a few of your last candles."
                            else:
                                $ custom1 = "The light you’re carrying guides your group through the complete darkness."
                            menu:
                                '[custom1] The polished walls of the tunnel, free of pointy rocks, were no doubt carved by human hands.
                                \n\nYour steps are loud, unlike the gentle draft and the deep stream. You pass by another corridor, buried by the mountain.
                                \n\nYou gesture for the others to stop. Something behind the corner kicked a rock that is now rolling on the floor.
                                '
                                '“{color=#f6d6bd}Asterion{/color}?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Asterion{/color}?”')
                                    $ custom1 = "The ghastly scream of a human-like throat makes you take a defensive stance, but, despite the passing breaths, no attack follows. Holding the light in front of you, you reach the next chamber."
                                    jump highisland_crew_asterion01
                                'I sneak forward, with my axe ready to strike.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sneak forward, with my axe ready to strike.')
                                    $ custom1 = "Holding the light in front of you, you reach the next chamber, where you’re greeted by the ghastly scream of a human-like throat. You step away, taking a defensive stance, but, despite the passing breaths, no attack follows. You enter again."
                                    jump highisland_crew_asterion01

        label highisland_crew_asterion01:
            show areapicture hi_asterioncave02 at basicfade
            $ renpy.music.play("audio/track_19asterion.ogg", channel=u'music', loop=None, fadeout=1.0, synchro_start=False, fadein=0, tight=None, if_changed=False, relative_volume=1.0)
            stop nature fadeout 4.0
            if aegidia_highisland_joined:
                $ aegidia_about_asterion_found = 1
                $ aegidia_friendship += 2
                $ custom11 = "\n\n{color=#f6d6bd}Aegidia{/color} covers her mouth, stopping herself from screaming."
            else:
                $ custom11 = ""
            if tulia_highisland_joined:
                $ custom18 = "\n\n“Well,” {color=#f6d6bd}Tulia{/color} lets out a sigh. “I guess we found him.”"
            else:
                $ custom18 = ""
            if thyrsus_highisland_joined and tulia_highisland_joined:
                $ custom15 = "\n\n{color=#f6d6bd}Thyrsus{/color} narrows his eyes. “Yeah, we did.”"
            elif thyrsus_highisland_joined:
                $ custom15 = "\n\n{color=#f6d6bd}Thyrsus{/color} narrows his eyes. “Yeah, t’s him.”"
            else:
                $ custom15 = ""
            if tzvi_highisland_joined and tulia_highisland_joined:
                $ custom19 = "\n\n{color=#f6d6bd}Tzvi{/color} adjusts his cloak, hiding his dagger."
            elif tzvi_highisland_joined:
                $ custom19 = "\n\n{color=#f6d6bd}Tzvi{/color} adjusts his cloak, hiding his dagger. “Well then.”"
            else:
                $ custom19 = ""
            if dalit_highisland_joined:
                $ custom12 = "\n\n{color=#f6d6bd}Dalit{/color} gives you a worried glance. “I’m sorry.”"
            else:
                $ custom12 = ""
            if efren_highisland_joined:
                $ custom13 = "\n\n{color=#f6d6bd}Efren{/color} takes off his hat and holds it in front of his chest."
            else:
                $ custom13 = ""
            if pyrrhos_highisland_joined:
                $ custom16 = "\n\n{color=#f6d6bd}Pyrrhos{/color} spits on the floor, but then rubs it with his boot, as if he had done something inappropriate."
            else:
                $ custom16 = ""
            if bandit_highisland_joined and not shortcut_darkforest_bandit_dead_troll:
                $ custom17 = "\n\n{color=#f6d6bd}The bandit{/color} gives you a fearful look. “What happened here?”"
            else:
                $ custom17 = ""
            if quintus_highisland_joined:
                $ custom20 = "\n\n{color=#f6d6bd}Quintus{/color} stands close to the exit, forming his arms in the shape of an hourglass."
            else:
                $ custom20 = ""
            menu:
                '[custom1]
                \n\nThe undead is furiously squirming in its attempts to release itself, alternately pulling the spear that’s nailing it to the wall and reaching toward you, as if it’s hoping you’ll fall into its embrace. There are no other corpses in sight - the creature must be starving.[custom11][custom18][custom15][custom19][custom12][custom13][custom16][custom17][custom20]
                '
                '“Let me take a look.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me take a look.”')
                    menu:
                        'The half-rotten flesh and the worn, torn tunic tell you little, but {color=#f6d6bd}Asterion’s{/color} short shell is still wearing the mail you were told about, now rusty, even more clangy than a new set. Some of the red hair and beard remain on the monstrous, pale face, but most of their strands are all over the floor.
                        \n\nThe knees of the creature are shattered. Next to them rests a large rock.
                        '
                        '“A monster caught him here, something with great strength.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A monster caught him here, something with great strength.”')
                            jump highisland_crew_asterion01a
                        '“He knew he was going to die, so he imprisoned himself here.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He knew he was going to die, so he imprisoned himself here.”')
                            jump highisland_crew_asterion01a
                        '“He was betrayed, or maybe fell into some sort of a trap, then crawled in here.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He was betrayed, or maybe fell into some sort of a trap, then crawled in here.”')
                            label highisland_crew_asterion01a:
                                menu:
                                    'You step closer. The undead does its best to throw itself at you, but it’s not strong enough.
                                    '
                                    'I raise my blade. A few blows to the head should be enough.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise my blade. A few blows to the head should be enough.')
                                        $ custom1 = "When the shell stops moving, the dead hand is still clenched on your gambeson. The corpse leans forward, loosely resting on the haft of the spear. The pieces of the skull are scattered over the chamber."
                                        jump highisland_crew_asterion02
                                    'I prepare {color=#f6d6bd}Asterion’s{/color} spear.' if item_asterionspear:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare {color=#f6d6bd}Asterion’s{/color} spear.')
                                        $ custom1 = "You avoid the awkward grasp of the dead hand and land a few precise hits, scattering the pieces of the skull over the chamber. The corpse leans forward, loosely resting on the haft of the spear."
                                        jump highisland_crew_asterion02
                                    'I prepare my spear.' if not item_asterionspear and item_mountainroadspear:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my spear.')
                                        $ custom1 = "You avoid the awkward grasp of the dead hand and land a few precise hits, scattering the pieces of the skull over the chamber. The corpse leans forward, loosely resting on the haft of the spear."
                                        jump highisland_crew_asterion02
                                    'I just need one precise shot from my crossbow.' if item_crossbow and item_crossbowquarrels:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just need one precise shot from my crossbow.')
                                        $ item_crossbowquarrels -= 1
                                        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                                        $ custom1 = "The quarrel shatters the skull, scattering its pieces over the chamber. The corpse leans forward, loosely resting on the haft of the spear."
                                        jump highisland_crew_asterion02
                                    'I pick up the rock.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pick up the rock.')
                                        $ custom1 = "When the shell stops moving, the dead hand is still clenched on your gambeson. The corpse leans forward, loosely resting on the haft of the spear. The pieces of the skull are scattered over the chamber."
                                        jump highisland_crew_asterion02

        label highisland_crew_asterion02:
            play nature "audio/ambient/highisland03.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            show areapicture hi_asterioncave03 at basicfade
            $ asterion_found = 1
            $ quest_asterion_description00asterion_highisland_knowsabout = "I discovered that {color=#f6d6bd}Asterion{/color} died during his lonely journey to an isolated island."
            if not quest_asterion_description00lies and not quest_asterion_description00gaveup:
                $ renpy.notify("Journal updated: Find the Roadwarden")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
            else:
                $ quest_asterion = 2
                $ renpy.notify("Quest completed: Find the Roadwarden")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Find the Roadwarden{/i}')
            menu:
                '[custom1]
                \n\nYour crew remains silent. The light flickers.
                '
                'I search the shell’s bundles.' if not asterion_found_searched:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the shell’s bundles.')
                    $ asterion_found_searched = 1
                    if tzvi_highisland_joined:
                        if quest_asterion_description02:
                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                        else:
                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    else:
                        if quest_asterion_description02:
                            $ custom1 = "No one is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                        else:
                            $ custom1 = "No one is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    $ custom11 = ""
                    $ coins += 20
                    show screen notifyimage( "+20", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+20 {image=cointest}{/i}')
                    jump highisland_crew_asterion02loop
                'I examine the cave.' if not asterion_found_cave_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the cave.')
                    $ asterion_found_cave_examined = 1
                    $ custom1 = "The centuries-old “treasure” spread among the collapsed racks and chests is mostly beyond use, but you do notice a few tools and statuettes made of now-green bronze. Judging by the simplicity of the chamber, it was likely little more than a basic storage room.\n\nThe corridors leading to the deeper caves have all been buried by time."
                    $ custom11 = ""
                    jump highisland_crew_asterion02loop
                '“Let’s collect the useful scraps of bronze and iron.”' if asterion_found_cave_examined and not asterion_found_cave_examined_picked:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s collect the useful scraps of bronze and iron.”')
                    $ asterion_found_cave_examined_picked = 1
                    if (bandit_highisland_joined and shortcut_darkforest_bandit_dead_troll) or navica_highisland_joined or highisland_crew_left <= 1:
                        $ custom1 = "The clangs and rattles don’t last long, as you have to take only the most promising pieces to avoid encumbrance."
                        $ item_ironscraps += 1
                        $ renpy.notify("You collected the metal scraps.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You collected the metal scraps.{/i}')
                    else:
                        $ custom1 = "Since you have quite a few capable hands with you, the clangs and rattles last for quite a bit, even though you take only the most promising pieces to avoid encumbrance."
                        $ item_ironscraps += 2
                        $ renpy.notify("You collected the metal scraps.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You collected the metal scraps.{/i}')
                    if pyrrhos_highisland_joined:
                        $ item_ironscraps += 1
                        $ custom11 = " {color=#f6d6bd}Pyrrhos{/color} makes sure you don’t leave anything of great value behind."
                    elif thyrsus_highisland_joined:
                        $ thyrsus_friendship -= 1
                        $ custom11 = " {color=#f6d6bd}Thyrsus{/color} scowls at you, but follows the order."
                    jump highisland_crew_asterion02loop
                'I look at {color=#f6d6bd}Aegidia{/color}. “Are you alright?”' if aegidia_about_asterion_found and not asterion_found_cave_crew_aegidia:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}Aegidia{/color}. “Are you alright?”')
                    $ asterion_found_cave_crew_aegidia = 1
                    $ description_thais02a = "According to {color=#f6d6bd}Aegidia{/color}, she’s getting weaker with every year, struggling with a mysterious illness."
                    $ custom1 = "“Ah, shit fire,” her shoulders slope as she steps away. “Is this ne weird? How souls like his get swallowed by the forest, whilst {color=#f6d6bd}Thais{/color} sits on her throne of dragon bones? She gets weaker en weaker from that illness of hers, but still has enough of breath to lie en scheme. Just stupid.”"
                    $ custom11 = ""
                    jump highisland_crew_asterion02loop
                'I carve my name on a wall with the magic chisel.' if item_magicchisel == 1 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with the magic chisel.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The soft hits of the butt of your axe result in sharp, deep cuts. Letter by letter, you leave behind the marks of your presence, then step away."
                    if efren_highisland_joined:
                        $ custom11 = " {color=#f6d6bd}Efren{/color} observes the cuts curiously. “Don’t forget about us, too.”"
                    elif pyrrhos_highisland_joined:
                        $ custom11 = " {color=#f6d6bd}Pyrrhos{/color} touches the cuts. “Write our names too, ay?”"
                    elif thyrsus_highisland_joined:
                        $ custom11 = " {color=#f6d6bd}Thyrsus{/color} playfully waggles his finger, but doesn’t say anything."
                    elif quintus_highisland_joined:
                        $ custom11 = " {color=#f6d6bd}Quintus’{/color} eyes widen. “Carve our names too!”"
                    elif dalit_highisland_joined:
                        $ custom11 = " The chamber makes {color=#f6d6bd}Dalit’s{/color} giggle grim. “Write my name, too.”"
                    else:
                        $ custom11 = ""
                    jump highisland_crew_asterion02tagging
                'I carve my name on a wall with The Tool of Destruction.' if item_magicchisel == 2 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with The Tool of Destruction.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The first hit with the butt of your weapon makes a pickaxe-worthy hole, so you try again in a different spot, trying to be as gentle as you can. Letter by letter, you leave behind the deep marks of your presence, then step away."
                    if efren_highisland_joined:
                        $ custom11 = " {color=#f6d6bd}Efren{/color} observes the cuts curiously. “Don’t forget about us, too.”"
                    elif pyrrhos_highisland_joined:
                        $ custom11 = " {color=#f6d6bd}Pyrrhos{/color} touches the cuts. “Write our names too, ay?”"
                    elif thyrsus_highisland_joined:
                        $ custom11 = " {color=#f6d6bd}Thyrsus{/color} playfully waggles his finger, but doesn’t say anything."
                    elif quintus_highisland_joined:
                        $ custom11 = " {color=#f6d6bd}Quintus’{/color} eyes widen. “Carve our names too!”"
                    elif dalit_highisland_joined:
                        $ custom11 = " The chamber makes {color=#f6d6bd}Dalit’s{/color} giggle grim. “Write my name, too.”"
                    else:
                        $ custom11 = ""
                    jump highisland_crew_asterion02tagging
                '“Let’s get back to {color=#f6d6bd}Navica{/color} before the sun rises.”' if navica_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get back to {color=#f6d6bd}Navica{/color} before the sun rises.”')
                    jump highisland_crew_asterion03
                '“Let’s get back to the boat before the sun rises.”' if not navica_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get back to the boat before the sun rises.”')
                    jump highisland_crew_asterion03

        label highisland_crew_asterion02tagging:
            menu:
                '[custom1] “[pcname],” you read out loud. [custom11]
                '
                'I search the shell’s bundles.' if not asterion_found_searched:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the shell’s bundles.')
                    $ asterion_found_searched = 1
                    if tzvi_highisland_joined:
                        if quest_asterion_description02:
                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                        else:
                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    else:
                        if quest_asterion_description02:
                            $ custom1 = "No one is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                        else:
                            $ custom1 = "No one is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    $ custom11 = ""
                    $ coins += 20
                    show screen notifyimage( "+20", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+20 {image=cointest}{/i}')
                    jump highisland_crew_asterion02loop
                'I examine the cave.' if not asterion_found_cave_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the cave.')
                    $ asterion_found_cave_examined = 1
                    $ custom1 = "The centuries-old “treasure” spread among the collapsed racks and chests is mostly beyond use, but you do notice a few tools and statuettes made of now-green bronze. Judging by the simplicity of the chamber, it was likely little more than a basic storage room.\n\nThe corridors leading to the deeper caves have all been buried by time."
                    $ custom11 = ""
                    jump highisland_crew_asterion02loop
                '“Let’s collect the useful scraps of bronze and iron.”' if asterion_found_cave_examined and not asterion_found_cave_examined_picked:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s collect the useful scraps of bronze and iron.”')
                    $ asterion_found_cave_examined_picked = 1
                    if (bandit_highisland_joined and shortcut_darkforest_bandit_dead_troll) or navica_highisland_joined or highisland_crew_left <= 1:
                        $ custom1 = "The clangs and rattles don’t last long, as you have to take only the most promising pieces to avoid encumbrance."
                        $ item_ironscraps += 1
                        $ renpy.notify("You collected the metal scraps.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You collected the metal scraps.{/i}')
                    else:
                        $ custom1 = "Since you have quite a few capable hands with you, the clangs and rattles last for quite a bit, even though you take only the most promising pieces to avoid encumbrance."
                        $ item_ironscraps += 2
                        $ renpy.notify("You collected the metal scraps.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You collected the metal scraps.{/i}')
                    if pyrrhos_highisland_joined:
                        $ item_ironscraps += 1
                        $ custom11 = " {color=#f6d6bd}Pyrrhos{/color} makes sure you don’t leave anything of great value behind."
                    elif thyrsus_highisland_joined:
                        $ thyrsus_friendship -= 1
                        $ custom11 = " {color=#f6d6bd}Thyrsus{/color} scowls at you, but follows the order."
                    jump highisland_crew_asterion02loop
                'I look at {color=#f6d6bd}Aegidia{/color}. “Are you alright?”' if aegidia_about_asterion_found and not asterion_found_cave_crew_aegidia:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}Aegidia{/color}. “Are you alright?”')
                    $ asterion_found_cave_crew_aegidia = 1
                    $ description_thais02a = "According to {color=#f6d6bd}Aegidia{/color}, she’s getting weaker with every year, struggling with a mysterious illness."
                    $ custom1 = "“Ah, shit fire,” her shoulders slope as she steps away. “Is this ne weird? How souls like his get swallowed by the forest, whilst {color=#f6d6bd}Thais{/color} sits on her throne of dragon bones? She gets weaker en weaker from that illness of hers, but still has enough breath to lie en scheme. Just stupid.”"
                    $ custom11 = ""
                    jump highisland_crew_asterion02loop
                'I carve my name on a wall with the magic chisel.' if item_magicchisel == 1 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with the magic chisel.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The soft hits of the butt of your axe result in sharp, deep cuts. Letter by letter, you leave behind the marks of your presence, then step away."
                    if efren_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Efren{/color} observes the cuts curiously. “Don’t forget about us, too.”"
                    elif pyrrhos_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Pyrrhos{/color} touches the cuts. “Write our names too, ay?”"
                    elif thyrsus_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Thyrsus{/color} playfully waggles his finger, but doesn’t say anything."
                    elif quintus_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Quintus’{/color} eyes widen. “Carve our names too!”"
                    elif dalit_highisland_joined:
                        $ custom11 = "The chamber makes {color=#f6d6bd}Dalit’s{/color} giggle grim. “Write my name, too.”"
                    else:
                        $ custom11 = ""
                    jump highisland_crew_asterion02tagging
                'I carve my name on a wall with The Tool of Destruction.' if item_magicchisel == 2 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with The Tool of Destruction.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The first hit with the butt of your weapon makes a pickaxe-worthy hole, so you try again in a different spot, trying to be as gentle as you can. Letter by letter, you leave behind the deep marks of your presence, then step away."
                    if efren_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Efren{/color} observes the cuts curiously. “Don’t forget about us, too.”"
                    elif pyrrhos_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Pyrrhos{/color} touches the cuts. “Write our names too, ay?”"
                    elif thyrsus_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Thyrsus{/color} playfully waggles his finger, but doesn’t say anything."
                    elif quintus_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Quintus’{/color} eyes widen. “Carve our names too!”"
                    elif dalit_highisland_joined:
                        $ custom11 = "The chamber makes {color=#f6d6bd}Dalit’s{/color} giggle grim. “Write my name, too.”"
                    else:
                        $ custom11 = ""
                    jump highisland_crew_asterion02tagging
                '“Let’s get back to {color=#f6d6bd}Navica{/color} before the sun rises.”' if navica_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get back to {color=#f6d6bd}Navica{/color} before the sun rises.”')
                    jump highisland_crew_asterion03
                '“Let’s get back to the boat before the sun rises.”' if not navica_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get back to the boat before the sun rises.”')
                    jump highisland_crew_asterion03

        label highisland_crew_asterion02loop:
            menu:
                '[custom1][custom11]
                '
                'I search the shell’s bundles.' if not asterion_found_searched:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the shell’s bundles.')
                    $ asterion_found_searched = 1
                    if tzvi_highisland_joined:
                        if quest_asterion_description02:
                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                        else:
                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    else:
                        if quest_asterion_description02:
                            $ custom1 = "No one is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. Far from the 50 that you were asked to find by {color=#f6d6bd}Pelt’s{/color} innkeep.\n\nOther than that, you find no potions, weapons, or travel kit, only a few unassembled torches."
                        else:
                            $ custom1 = "No one is eager to assist you. Among the decomposing, soggy bags and pouches, you find a humble bunch of coins threaded on a bow string. There are no potions, weapons, or travel kit, only a few unassembled torches."
                    $ custom11 = ""
                    $ coins += 20
                    show screen notifyimage( "+20", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+20 {image=cointest}{/i}')
                    jump highisland_crew_asterion02loop
                'I examine the cave.' if not asterion_found_cave_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I examine the cave.')
                    $ asterion_found_cave_examined = 1
                    $ custom1 = "The centuries-old “treasure” spread among the collapsed racks and chests is mostly beyond use, but you do notice a few tools and statuettes made of now-green bronze. Judging by the simplicity of the chamber, it was likely little more than a basic storage room.\n\nThe corridors leading to the deeper caves have all been buried by time."
                    $ custom11 = ""
                    jump highisland_crew_asterion02loop
                '“Let’s collect the useful scraps of bronze and iron.”' if asterion_found_cave_examined and not asterion_found_cave_examined_picked:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s collect the useful scraps of bronze and iron.”')
                    $ asterion_found_cave_examined_picked = 1
                    if (bandit_highisland_joined and shortcut_darkforest_bandit_dead_troll) or navica_highisland_joined or highisland_crew_left <= 1:
                        $ custom1 = "The clangs and rattles don’t last long, as you have to take only the most promising pieces to avoid encumbrance."
                        $ item_ironscraps += 1
                        $ renpy.notify("You collected the metal scraps.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You collected the metal scraps.{/i}')
                    else:
                        $ custom1 = "Since you have quite a few capable hands with you, the clangs and rattles last for quite a bit, even though you take only the most promising pieces to avoid encumbrance."
                        $ item_ironscraps += 2
                        $ renpy.notify("You collected the metal scraps.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You collected the metal scraps.{/i}')
                    if pyrrhos_highisland_joined:
                        $ item_ironscraps += 1
                        $ custom11 = " {color=#f6d6bd}Pyrrhos{/color} makes sure you don’t leave anything of great value behind."
                    elif thyrsus_highisland_joined:
                        $ thyrsus_friendship -= 1
                        $ custom11 = " {color=#f6d6bd}Thyrsus{/color} scowls at you, but follows the order."
                    jump highisland_crew_asterion02loop
                'I look at {color=#f6d6bd}Aegidia{/color}. “Are you alright?”' if aegidia_about_asterion_found and not asterion_found_cave_crew_aegidia:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}Aegidia{/color}. “Are you alright?”')
                    $ asterion_found_cave_crew_aegidia = 1
                    $ description_thais02a = "According to {color=#f6d6bd}Aegidia{/color}, she’s getting weaker with every year, struggling with a mysterious illness."
                    $ custom1 = "“Ah, shit fire,” her shoulders slope as she steps away. “Is this ne weird? How souls like his get swallowed by the forest, whilst {color=#f6d6bd}Thais{/color} sits on her throne of dragon bones? She gets weaker en weaker from that illness of hers, but still has enough breath to lie en scheme. Just stupid.”"
                    $ custom11 = ""
                    jump highisland_crew_asterion02loop
                'I carve my name on a wall with the magic chisel.' if item_magicchisel == 1 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with the magic chisel.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The soft hits of the butt of your axe result in sharp, deep cuts. Letter by letter, you leave behind the marks of your presence, then step away."
                    if efren_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Efren{/color} observes the cuts curiously. “Don’t forget about us, too.”"
                    elif pyrrhos_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Pyrrhos{/color} touches the cuts. “Write our names too, ay?”"
                    elif thyrsus_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Thyrsus{/color} playfully waggles his finger, but doesn’t say anything."
                    elif quintus_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Quintus’{/color} eyes widen. “Carve our names too!”"
                    elif dalit_highisland_joined:
                        $ custom11 = "The chamber makes {color=#f6d6bd}Dalit’s{/color} giggle grim. “Write my name, too.”"
                    else:
                        $ custom11 = ""
                    jump highisland_crew_asterion02tagging
                'I carve my name on a wall with The Tool of Destruction.' if item_magicchisel == 2 and not asterion_found_cave_tagged and pc_class == "scholar":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I carve my name on a wall with The Tool of Destruction.')
                    $ asterion_found_cave_tagged = 1
                    $ custom1 = "The first hit with the butt of your weapon makes a pickaxe-worthy hole, so you try again in a different spot, trying to be as gentle as you can. Letter by letter, you leave behind the deep marks of your presence, then step away."
                    if efren_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Efren{/color} observes the cuts curiously. “Don’t forget about us, too.”"
                    elif pyrrhos_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Pyrrhos{/color} touches the cuts. “Write our names too, ay?”"
                    elif thyrsus_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Thyrsus{/color} playfully waggles his finger, but doesn’t say anything."
                    elif quintus_highisland_joined:
                        $ custom11 = "{color=#f6d6bd}Quintus’{/color} eyes widen. “Carve our names too!”"
                    elif dalit_highisland_joined:
                        $ custom11 = "The chamber makes {color=#f6d6bd}Dalit’s{/color} giggle grim. “Write my name, too.”"
                    else:
                        $ custom11 = ""
                    jump highisland_crew_asterion02tagging
                '“Let’s get back to {color=#f6d6bd}Navica{/color} before the sun rises.”' if navica_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get back to {color=#f6d6bd}Navica{/color} before the sun rises.”')
                    jump highisland_crew_asterion03
                '“Let’s get back to the boat before the sun rises.”' if not navica_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s get back to the boat before the sun rises.”')
                    jump highisland_crew_asterion03

        label highisland_crew_asterion03:
            if tulia_highisland_joined:
                $ custom11 = " {color=#f6d6bd}Tulia{/color} clears her throat. “We can’t leave him like that.”"
            elif quintus_highisland_joined:
                $ custom11 = " {color=#f6d6bd}Quintus{/color} is the first one to get outside."
            else:
                $ custom11 = ""
            menu:
                'You spare the corpse one more look.[custom11]
                '
                'I should burn the bones.' if not tulia_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should burn the bones.')
                    $ asterion_found_burnt = 1
                    $ achievement_pyrepoints += 1
                    $ custom1 = "You surround {color=#f6d6bd}Asterion’s{/color} shell with a few wooden logs and some of his own possessions. The smoke drives you outside.\n\n"
                    jump highisland_crew_asterion03a
                'There’s no time to waste.' if not tulia_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- There’s no time to waste.')
                    $ custom1 = ""
                    jump highisland_crew_asterion03a
                '“You’re right. Let’s gather some timber.”' if tulia_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re right. Let’s gather some timber.”')
                    $ asterion_found_burnt = 1
                    $ achievement_pyrepoints += 1
                    $ custom1 = "You surround {color=#f6d6bd}Asterion’s{/color} shell with a few wooden logs and some of his own possessions. The smoke drives you outside.\n\n"
                    jump highisland_crew_asterion03a
                '“We’ve no time to waste.”' if tulia_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ve no time to waste.”')
                    $ custom1 = ""
                    label highisland_crew_asterion03a:
                        stop music fadeout 8.0
                        play nature "audio/ambient/highisland02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
                        show areapicture hi_volcano01 at basicfade
                        $ can_potions = 1
                        $ can_items = 1
                        menu:
                            '[custom1]The fresh air makes you yawn. You grab your bags and approach the edge of the scarp, observing the woods of {color=#f6d6bd}High Island{/color}. You recognize the trail that led you here from the valley of the saurians.
                            '
                            '“Let’s try to follow the same trail. We should be able to reach the harbor before the low tide.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s try to follow the same trail. We should be able to reach the harbor before the low tide.”')
                                jump highisland_returning00

label highisland_returningALL:
    label highisland_returning00:
        $ pc_hp = limit_pc_hp(pc_hp-1)
        show minus1hp at hpchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
        $ highisland_journey_inprogress = 0
        $ highisland_spot = 0
        nvl clear
        stop music fadeout 8.0
        scene empty
        scene layoutfull
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ can_potions = 0
        $ ruinedvillage_curse_points = 0
        $ ruinedvillage_curse_block = 0
        if weathermud:
            $ weathermud = 0
        if weatherfog:
            $ weatherfog = 0
        if bogroad_clotheswet:
            $ bogroad_clotheswet = 0
        $ questionpreset = 0
        if quest_birdhunting == 1 and quest_birdhunting_description06 and foragers_quest_message_timer < (day-1):
            $ quest_birdhunting_description07 = "The bird is already in {color=#f6d6bd}Creeks{/color}. It’s too late for me to deliver the message."
            $ quest_birdhunting = 2
            $ renpy.notify("Quest completed: Bird Hunting")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bird Hunting{/i}')
        if (shortcut_darkforest_bandit_toldabouthuntercabin+3) < day and shortcut_darkforest_bandit_toldabouthuntercabin and not shortcut_darkforest_bandit_leftthepeninsula and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_inpeltnorth and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll and pc_area != "peltnorth":
            $ shortcut_darkforest_bandit_leftTOpeltnorth = 1
            $ shortcut_darkforest_bandit_inpeltnorth = 1
            $ peltnorth_bonusnpcs += 1
        if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
            $ world_daylength -= 1
            $ renpy.notify("The days are getting shorter.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
        if day == world_deadline-1 or day >= world_deadline:
            $ world_endmode = 1
        $ pc_food = limit_pc_food(pc_food-2)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
        $ cleanliness = limit_cleanliness(cleanliness-3)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
        $ day += 1
        if highisland_journey_startingpoint == "hamlet":
            $ pc_area = "fishinghamlet"
            show howlersdelldarkbackground at basicfade
            if fishinghamlet_areas_seen_01:
                show fishinghamletscrap01 at basicfade
            if fishinghamlet_areas_seen_02:
                show fishinghamletscrap02 at basicfade
            if fishinghamlet_areas_seen_03:
                show fishinghamletscrap03 at basicfade
            if fishinghamlet_areas_seen_04:
                show fishinghamletscrap04 at basicfade
            if fishinghamlet_areas_seen_05:
                show fishinghamletscrap05 at basicfade
            if fishinghamlet_areas_seen_06:
                show fishinghamletscrap06 at basicfade
            if fishinghamlet_areas_seen_07:
                show fishinghamletscrap07 at basicfade
            play nature "audio/ambient/fishinghamlet01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            $ quarters = 32
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            nvl clear
            if highisland_mode == "solo":
                jump highisland_returning_fishinghamlet_solo01
            if highisland_mode == "crew":
                jump highisland_returning_fishinghamlet_crew01
        if highisland_journey_startingpoint == "beach":
            $ pc_area = "beach"
            play nature "audio/ambient/beach01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            if not beach_boatprepared:
                show areapicture beach01 at basicfade
            else:
                show areapicture beach02 at basicfade
            $ quarters = 30
            nvl clear
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            if highisland_mode == "solo":
                jump highisland_returning_beach_solo01
            if highisland_mode == "crew":
                jump highisland_returning_beach_crew01
            if highisland_mode == "howlers":
                jump highisland_returning_beach_howlers01

    label highisland_returning_fishinghamlet_solo01:
        if item_sharpeningpotion_used and item_sharpeningpotion_used == day-1:
            $ item_sharpeningpotion_used = 0
            $ pc_battlecounter -= 20
            $ pc_throwingxp -= 20
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-3)
            $ custom1 = "You lean toward the water and vomit out blood, then wipe the sweat from your forehead. You blink - the world has grown fast and dull. The sharpening poison has left your shell."
        else:
            $ custom1 = "You don’t know how to answer."
        $ aegidia_about_asterion_found = 1
        $ aegidia_friendship += 2
        menu:
            'After {color=#f6d6bd}Aegidia{/color} saw your arriving boat, she woke up {color=#f6d6bd}[horsename]{/color} and brought it to the shore. She helps you get on the pier and observes your face carefully. There’s pain in her eyes. “Are you alright?”
            \n\n[custom1]
            \n\nAfter a short moment, she follows with another question. “What happened to him?”
            \n\nYou share as little as you need, and she doesn’t inquire further. “Is this ne weird? How souls like his get swallowed by the forest, whilst {color=#f6d6bd}Thais{/color} sits on her throne of dragon bones? She gets weaker en weaker from that illness of hers, but still has enough breath to lie en scheme. Just stupid.”
            '
            'I rub my eyes. “I need to get ready. Or to find a decent bed for myself.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I rub my eyes. “I need to get ready. Or to find a decent bed for myself.”')
                $ highisland_returned = 1
                if pc_goal == "iwanttoberemembered":
                    $ pc_goal_iwanttoberememberedpoints += 2
                if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                    $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                if not world_endmode:
                    menu:
                        'She nods and steps away. Judging by her own eyes, she hasn’t slept either.
                        \n\nYou scratch {color=#f6d6bd}[horsename]’s{/color} neck, take off your bundles, splash your face with cold water.
                        '
                        'I prepare us for the further journey.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare us for the further journey.')
                            $ can_leave = 1
                            $ can_rest = 1
                            $ can_items = 1
                            jump fishinghamletselectwheretogo
                else:
                    menu:
                        'She nods and steps away. Judging by her own eyes, she hasn’t slept either.
                        \n\nYou scratch {color=#f6d6bd}[horsename]’s{/color} neck. It’s skinnier than on the day you crossed {color=#f6d6bd}Hag Hills{/color}. You take off your bundles splash your face with cold water.
                        \n\nTime to head back to {color=#f6d6bd}Hovlavan{/color}.
                        '
                        'I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.' if militarycamp_destroyed_firsttime_tulia:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.')
                            $ travel_destination = "peltnorth"
                            jump finaldestinationafterevent
                        'The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.' if not militarycamp_destroyed_firsttime_tulia and militarycamp_destroyed_firsttime_southerncrossroads:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.')
                            $ travel_destination = "peltnorth"
                            jump finaldestinationafterevent
                        'I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.' if not militarycamp_destroyed_firsttime_tulia and not militarycamp_destroyed_firsttime_southerncrossroads:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.')
                            $ travel_destination = "southerncrossroads"
                            jump finaldestinationafterevent

    label highisland_returning_fishinghamlet_crew01:
        $ highisland_crew_returning = 1
        if not aegidia_about_asterion_found:
            if item_sharpeningpotion_used and item_sharpeningpotion_used == day-1:
                $ item_sharpeningpotion_used = 0
                $ pc_battlecounter -= 20
                $ pc_throwingxp -= 20
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ cleanliness = limit_cleanliness(cleanliness-3)
                $ custom1 = "You lean toward the water and vomit out blood, then wipe the sweat from your forehead. You blink - the world has grown fast and dull. The sharpening poison has left your shell."
            else:
                $ custom1 = "You don’t know how to answer."
            $ aegidia_about_asterion_found = 1
            $ aegidia_friendship += 2
            menu:
                'After {color=#f6d6bd}Aegidia{/color} saw your arriving boat, she woke up {color=#f6d6bd}[horsename]{/color} and brought it to the shore. She helps your group get on the pier and observes your face carefully. There’s pain in her eyes. “Are you alright?”
                \n\n[custom1]
                \n\nAfter a short moment, she follows with another question. “What happened to him?”
                \n\nYou share as little as you need, and she doesn’t inquire further. “Is this ne weird? How souls like his get swallowed by the forest, whilst {color=#f6d6bd}Thais{/color} sits on her throne of dragon bones? She gets weaker en weaker from that illness of hers, but still has enough breath to lie en scheme. Just stupid.”
                '
                'I rub my eyes. “I need to get ready. Or to find a decent bed for myself.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I rub my eyes. “I need to get ready. Or to find a decent bed for myself.”')
                    $ highisland_returned = 1
                    if pc_goal == "iwanttoberemembered":
                        $ pc_goal_iwanttoberememberedpoints += 2
                    if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                        $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                    $ custom11 = "{color=#f6d6bd}Aegidia{/color} pats your back and returns to the others, answering various questions about this place.\n\n"
                    if dalit_highisland_joined:
                        $ custom12 = "{color=#f6d6bd}Dalit{/color} makes sure her crossbow didn’t suffer from the salt water. She’s seasick again, and doesn’t say much, but her giggling remains as honest as ever.\n\n"
                    else:
                        $ custom12 = ""
                    if efren_highisland_joined:
                        $ custom13 = "{color=#f6d6bd}Efren{/color} has a wide smile and keeps raising his voice. “I {i}knew{/i} I’d be alright!” He announces as he pounds his chest.\n\n"
                    else:
                        $ custom13 = ""
                    if navica_highisland_joined:
                        $ custom14 = "{color=#f6d6bd}Navica{/color} keeps observing the island. She didn’t want to tell any of you how her night went by, and asked you no questions.\n\n"
                    else:
                        $ custom14 = ""
                    if thyrsus_highisland_joined:
                        $ custom15 = "{color=#f6d6bd}Thyrsus{/color} throws away one of his creepers. “Gotta make a new one when I get home.”\n\n"
                    else:
                        $ custom15 = ""
                    if pyrrhos_highisland_joined:
                        $ custom16 = "{color=#f6d6bd}Pyrrhos{/color} recalls the dangerous encounters from a few hours back, though in his tales, he’s the one who saved your skin each time.\n\n"
                    else:
                        $ custom16 = ""
                    if bandit_highisland_joined and not shortcut_darkforest_bandit_dead_troll:
                        $ custom17 = "{color=#f6d6bd}The bandit{/color} stays away from the others, listening carefully to each word.\n\n"
                    else:
                        $ custom17 = ""
                    if tulia_highisland_joined:
                        $ custom18 = "{color=#f6d6bd}Tulia{/color} lets out a weak chuckle and helps the conversation keep to a friendly tone. She resembles the same woman you saw in the camp all those days back, but this time she holds herself like a leader.\n\n"
                    else:
                        $ custom18 = ""
                    if tzvi_highisland_joined:
                        $ custom19 = "{color=#f6d6bd}Tzvi{/color} holds his black, soaked cloak in his hands. He says he can’t wait to put your coins to use and leave the peninsula for good.\n\n"
                    else:
                        $ custom19 = ""
                    if quintus_highisland_joined:
                        $ custom20 = "{color=#f6d6bd}Quintus{/color} is moody, though you can’t tell if he’d rather fall asleep, get drunk, or eat a boar.\n\n"
                    else:
                        $ custom20 = ""
                    if not world_endmode:
                        menu:
                            'She nods and steps away. Judging by her own eyes, she hasn’t slept either.
                            \n\nThe others start to plan their return home. [custom11][custom12][custom13][custom14][custom15][custom16][custom17][custom18][custom19][custom20]You scratch {color=#f6d6bd}[horsename]’s{/color} neck, take off your bundles, and quickly wash yourself in the cold water. Now you need to take everyone to safety before you stop somewhere for the night.
                            \n\nYou’re going to end the day at...
                            '
                            'The southern crossroads.' if southerncrossroads_firsttime:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The southern crossroads.')
                                $ travel_destination = "southerncrossroads"
                                jump finaldestinationafterevent
                            'The western crossroads.' if westerncrossroads_firsttime:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western crossroads.')
                                $ travel_destination = "westerncrossroads"
                                jump finaldestinationafterevent
                            'Foggy Lake.' if foggylake_firsttime:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Foggy Lake.')
                                $ travel_destination = "foggylake"
                                jump finaldestinationafterevent
                            'The watchtower.' if watchtower_firsttime:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The watchtower.')
                                $ travel_destination = "watchtower"
                                jump finaldestinationafterevent
                    else:
                        menu:
                            'She nods and steps away. Judging by her own eyes, she hasn’t slept either. You scratch {color=#f6d6bd}[horsename]’s{/color} neck. It’s skinnier than on the day you crossed {color=#f6d6bd}Hag Hills{/color}.
                            \n\nThe others start to plan their return home. [custom11][custom12][custom13][custom14][custom15][custom16][custom17][custom18][custom19][custom20]You take off your bundles splash your face with cold water.
                            \n\nYou need to take everyone to safety, but then, it’ll be time to head back to {color=#f6d6bd}Hovlavan{/color}.
                            '
                            '“So, {color=#f6d6bd}Tulia{/color}. Let’s take all of them home, then head back to {color=#f6d6bd}Pelt{/color} and prepare ourselves for our journey to the city.”' if tulia_highisland_joined:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, {color=#f6d6bd}Tulia{/color}. Let’s take all of them home, then head back to {color=#f6d6bd}Pelt{/color} and prepare ourselves for our journey to the city.”')
                                $ tulia_about_highisland_narration = 1
                                $ travel_destination = "peltnorth"
                                jump finaldestinationafterevent
                            'I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.' if not tulia_highisland_joined and militarycamp_destroyed_firsttime_tulia:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.')
                                $ travel_destination = "peltnorth"
                                jump finaldestinationafterevent
                            'The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.' if not tulia_highisland_joined and not militarycamp_destroyed_firsttime_tulia and militarycamp_destroyed_firsttime_southerncrossroads:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.')
                                $ travel_destination = "peltnorth"
                                jump finaldestinationafterevent
                            'I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.' if not tulia_highisland_joined and not militarycamp_destroyed_firsttime_tulia and not militarycamp_destroyed_firsttime_southerncrossroads:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.')
                                $ travel_destination = "southerncrossroads"
                                jump finaldestinationafterevent
        else:
            if item_sharpeningpotion_used and item_sharpeningpotion_used == day-1:
                $ item_sharpeningpotion_used = 0
                $ pc_battlecounter -= 20
                $ pc_throwingxp -= 20
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                $ cleanliness = limit_cleanliness(cleanliness-3)
                $ custom1 = "Your group ties the boat to the piling while you lean toward the water and vomit out blood, then wipe the sweat from your forehead. You blink - the world has grown fast and dull. The sharpening poison has left your shell."
            else:
                $ custom1 = "You help your group tie the boat to the piling."
            $ custom11 = ""
            if dalit_highisland_joined:
                $ custom12 = "\n\n{color=#f6d6bd}Dalit{/color} makes sure her crossbow didn’t suffer from the salt water. She’s seasick again, and doesn’t say much, but her giggling remains as honest as ever."
            else:
                $ custom12 = ""
            if efren_highisland_joined:
                $ custom13 = "\n\n{color=#f6d6bd}Efren{/color} has a wide smile and keeps raising his voice. “I {i}knew{/i} I’d be alright!” He announces as he pounds his chest."
            else:
                $ custom13 = ""
            if navica_highisland_joined:
                $ custom14 = "\n\n{color=#f6d6bd}Navica{/color} keeps observing the island. She didn’t want to tell any of you how her night went by, and asked you no questions."
            else:
                $ custom14 = ""
            if thyrsus_highisland_joined:
                $ custom15 = "\n\n{color=#f6d6bd}Thyrsus{/color} throws away one of his creepers. “Gotta make a new one when I get home.”"
            else:
                $ custom15 = ""
            if pyrrhos_highisland_joined:
                $ custom16 = "\n\n{color=#f6d6bd}Pyrrhos{/color} recalls the dangerous encounters from a few hours back, though in his tales, he’s the one who saved your skin each time."
            else:
                $ custom16 = ""
            if bandit_highisland_joined and not shortcut_darkforest_bandit_dead_troll:
                $ custom17 = "\n\n{color=#f6d6bd}The bandit{/color} stays away from the others, listening carefully to each word."
            else:
                $ custom17 = ""
            if tulia_highisland_joined:
                $ custom18 = "\n\n{color=#f6d6bd}Tulia{/color} lets out a weak chuckle and helps the conversation keep to a friendly tone. She resembles the same woman you saw in the camp all those days back, but this time she holds herself like a leader."
            else:
                $ custom18 = ""
            if tzvi_highisland_joined:
                $ custom19 = "\n\n{color=#f6d6bd}Tzvi{/color} holds his black, soaked cloak in his hands. He says he can’t wait to put your coins to use and leave the peninsula for good."
            else:
                $ custom19 = ""
            if quintus_highisland_joined:
                $ custom20 = "\n\n{color=#f6d6bd}Quintus{/color} is moody, though you can’t tell if he’d rather fall asleep, get drunk, or eat a boar."
            else:
                $ custom20 = ""
            menu:
                '[custom1] {color=#f6d6bd}Aegidia{/color}, worried about {color=#f6d6bd}[horsename]{/color}, is the first one to enter the hamlet. The others start to plan their return home.[custom11][custom12][custom13][custom14][custom15][custom16][custom17][custom18][custom19][custom20]
                '
                'I rub my eyes and follow {color=#f6d6bd}Aegidia{/color}. “I better get ready.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I rub my eyes and follow {color=#f6d6bd}Aegidia{/color}. “I better get ready.”')
                    $ highisland_returned = 1
                    if pc_goal == "iwanttoberemembered":
                        $ pc_goal_iwanttoberememberedpoints += 2
                    if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                        $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                    if not world_endmode:
                        $ highisland_crew_returning = 1
                        menu:
                            'You scratch {color=#f6d6bd}[horsename]’s{/color} neck, take off your bundles, splash your face with cold water. Now you need to take everyone to safety before you stop somewhere for the night.
                            \n\nYou’re going to end the day at...
                            '
                            'The southern crossroads.' if southerncrossroads_firsttime:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The southern crossroads.')
                                $ travel_destination = "southerncrossroads"
                                jump finaldestinationafterevent
                            'The western crossroads.' if westerncrossroads_firsttime:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western crossroads.')
                                $ travel_destination = "westerncrossroads"
                                jump finaldestinationafterevent
                            'Foggy Lake.' if foggylake_firsttime:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Foggy Lake.')
                                $ travel_destination = "foggylake"
                                jump finaldestinationafterevent
                            'The watchtower.' if watchtower_firsttime:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The watchtower.')
                                $ travel_destination = "watchtower"
                                jump finaldestinationafterevent
                    else:
                        menu:
                            'You scratch {color=#f6d6bd}[horsename]’s{/color} neck. It’s skinnier than on the day you crossed {color=#f6d6bd}Hag Hills{/color}. You take off your bundles splash your face with cold water.
                            \n\nYou need to take everyone to safety, but then, it’ll be time to head back to {color=#f6d6bd}Hovlavan{/color}.
                            '
                            'I approach {color=#f6d6bd}Tulia{/color}. “Let’s take all of them home, then head back to {color=#f6d6bd}Pelt{/color} and prepare ourselves for our journey to the city.”' if tulia_highisland_joined:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Tulia{/color}. “Let’s take all of them home, then head back to {color=#f6d6bd}Pelt{/color} and prepare ourselves for our journey to the city.”')
                                $ tulia_about_highisland_narration = 1
                                $ travel_destination = "peltnorth"
                                jump finaldestinationafterevent
                            'I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.' if not tulia_highisland_joined and militarycamp_destroyed_firsttime_tulia:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.')
                                $ travel_destination = "peltnorth"
                                jump finaldestinationafterevent
                            'The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.' if not tulia_highisland_joined and not militarycamp_destroyed_firsttime_tulia and militarycamp_destroyed_firsttime_southerncrossroads:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.')
                                $ travel_destination = "peltnorth"
                                jump finaldestinationafterevent
                            'I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.' if not tulia_highisland_joined and not militarycamp_destroyed_firsttime_tulia and not militarycamp_destroyed_firsttime_southerncrossroads:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.')
                                $ travel_destination = "southerncrossroads"
                                jump finaldestinationafterevent

    label highisland_returning_beach_solo01:
        if item_sharpeningpotion_used and item_sharpeningpotion_used == day-1:
            $ item_sharpeningpotion_used = 0
            $ pc_battlecounter -= 20
            $ pc_throwingxp -= 20
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-3)
            $ custom1 = "You push the boat into the sand, turn around, vomit out blood, and wipe the sweat from your forehead. You blink - the world has grown fast and dull. The sharpening poison has left your shell.\n\n"
        else:
            $ custom1 = "You push the boat into the sand. "
        if world_endmode:
            $ custom2 = "\n\nYou cast one more glance at the volcano of {color=#f6d6bd}High Island{/color}, then turn toward the hills of the peninsula. Time to head back to {color=#f6d6bd}Hovlavan{/color}."
        else:
            $ custom2 = ""
        if pc_goal == "iwanttoberemembered":
            $ pc_goal_iwanttoberememberedpoints += 2
        if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
            $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
        menu:
            '[custom1]A few splashes of water won’t be enough to get rid off all the sweat gathered beneath your gambeson, and you still need to reach {color=#f6d6bd}Gale Rocks{/color} on your own feet. Maybe at least {color=#f6d6bd}[horsename]{/color} had a nice rest.[custom2]
            '
            'I rub my eyes and leave this place before the harpies get here.' if not world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I rub my eyes and leave this place before the harpies get here.')
                $ highisland_returned = 1
                $ galerocks_fluff_special1 = 1
                $ travel_destination = "galerocks"
                jump finaldestinationafterevent
            'I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.' if militarycamp_destroyed_firsttime_tulia and world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.')
                $ travel_destination = "peltnorth"
                jump finaldestinationafterevent
            'The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.' if not militarycamp_destroyed_firsttime_tulia and militarycamp_destroyed_firsttime_southerncrossroads and world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.')
                $ travel_destination = "peltnorth"
                jump finaldestinationafterevent
            'I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.' if not militarycamp_destroyed_firsttime_tulia and not militarycamp_destroyed_firsttime_southerncrossroads and world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.')
                $ travel_destination = "southerncrossroads"
                jump finaldestinationafterevent

    label highisland_returning_beach_howlers01:
        if item_sharpeningpotion_used and item_sharpeningpotion_used == day-1:
            $ item_sharpeningpotion_used = 0
            $ pc_battlecounter -= 20
            $ pc_throwingxp -= 20
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-3)
            $ custom1 = "You help the others push the boat into the sand, then turn around, vomit out blood, and wipe the sweat from your forehead. You blink - the world has grown fast and dull. The sharpening poison has left your shell.\n\n"
        else:
            $ custom1 = "You help the others push the boat into the sand. "
        if highisland_howlersguards_spearwoman_dead:
            $ thais_about_asterion_comment = 3
            $ howlersdell_reputation -= 2
            $ custom3 = "\n\n{color=#f6d6bd}The guards{/color} stay solemn. They mentioned {color=#f6d6bd}the spearwoman{/color} only a few times, but they don’t hide the fact that they blame {i}you{/i} for her death. They don’t even offer to join you on your way south."
        elif highisland_howlersguards_hp <= 0:
            $ thais_about_asterion_comment = 3
            $ howlersdell_reputation -= 1
            $ highisland_howlersguards_spearwoman_dead = 1
            $ custom3 = "\n\n{color=#f6d6bd}The guards{/color} stay solemn. {color=#f6d6bd}The spearwoman{/color} didn’t reach land with you - once she stopped breathing, her companions decided to throw her shell overboard. As far as you can tell, the blame for her death is split between you and {color=#f6d6bd}Thais{/color}."
        elif highisland_howlersguards_hp < 10:
            $ thais_about_asterion_comment = 1
            $ custom3 = "\n\n{color=#f6d6bd}The guards{/color} share a relieved conversation. Their night might have been difficult, but they all made it. You’re even offered a shared journey to their village, but you refuse politely."
        else:
            $ thais_about_asterion_comment = 2
            $ howlersdell_reputation += 1
            $ custom3 = "\n\nDespite the long night they had, {color=#f6d6bd}the guards{/color} are rather cheerful, and {color=#f6d6bd}the leader{/color} admits the journey was much easier than he expected - in part because of your preparations. From what you can tell, the crew can’t wait to tell the others about the things they’ve seen. You’re even offered a shared journey to their village, but you refuse politely."
        if world_endmode:
            $ custom2 = "\n\nYou cast one more glance at the volcano of {color=#f6d6bd}High Island{/color}, then turn toward the hills of the peninsula. Time to head back to {color=#f6d6bd}Hovlavan{/color}."
        else:
            $ custom2 = ""
        if pc_goal == "iwanttoberemembered":
            $ pc_goal_iwanttoberememberedpoints += 2
        if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
            $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
        menu:
            '[custom1]A few splashes of water won’t be enough to get rid off all the sweat gathered beneath your gambeson, and you still need to reach {color=#f6d6bd}Gale Rocks{/color} on your own feet. Maybe at least {color=#f6d6bd}[horsename]{/color} had a nice rest.[custom3][custom2]
            '
            'I rub my eyes and leave this place before the harpies get here.' if not world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I rub my eyes and leave this place before the harpies get here.')
                $ highisland_returned = 1
                $ galerocks_fluff_special1 = 1
                $ travel_destination = "galerocks"
                jump finaldestinationafterevent
            'I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.' if militarycamp_destroyed_firsttime_tulia and world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.')
                $ travel_destination = "peltnorth"
                jump finaldestinationafterevent
            'The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.' if not militarycamp_destroyed_firsttime_tulia and militarycamp_destroyed_firsttime_southerncrossroads and world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.')
                $ travel_destination = "peltnorth"
                jump finaldestinationafterevent
            'I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.' if not militarycamp_destroyed_firsttime_tulia and not militarycamp_destroyed_firsttime_southerncrossroads and world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.')
                $ travel_destination = "southerncrossroads"
                jump finaldestinationafterevent

    label highisland_returning_beach_crew01:
        $ highisland_crew_returning = 1
        if item_sharpeningpotion_used and item_sharpeningpotion_used == day-1:
            $ item_sharpeningpotion_used = 0
            $ pc_battlecounter -= 20
            $ pc_throwingxp -= 20
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ cleanliness = limit_cleanliness(cleanliness-3)
            $ custom1 = "You help the others push the boat into the sand, then turn around, vomit out blood, and wipe the sweat from your forehead. You blink - the world has grown fast and dull. The sharpening poison has left your shell."
        else:
            $ custom1 = "You help the others push the boat into the sand."
        if aegidia_highisland_joined:
            $ custom11 = "\n\n{color=#f6d6bd}Aegidia{/color} raises her bow and lets out a triumphant cry. “{i}Legendary island{/i}, huh? Who’s the legend now!”"
        else:
            $ custom11 = ""
        if dalit_highisland_joined:
            $ custom12 = "\n\n{color=#f6d6bd}Dalit{/color} makes sure her crossbow didn’t suffer from the salt water. She’s seasick again, and doesn’t say much, but her giggling remains as honest as ever."
        else:
            $ custom12 = ""
        if efren_highisland_joined:
            $ custom13 = "\n\n{color=#f6d6bd}Efren{/color} has a wide smile and keeps raising his voice. “I {i}knew{/i} I’d be alright!” He announces as he pounds his chest."
        else:
            $ custom13 = ""
        if navica_highisland_joined:
            $ custom14 = "\n\n{color=#f6d6bd}Navica{/color} keeps observing the island. She didn’t want to tell any of you how her night went by, and asked you no questions."
        else:
            $ custom14 = ""
        if thyrsus_highisland_joined:
            $ custom15 = "\n\n{color=#f6d6bd}Thyrsus{/color} throws away one of his creepers. “Gotta make a new one when I get home.”"
        else:
            $ custom15 = ""
        if pyrrhos_highisland_joined:
            $ custom16 = "\n\n{color=#f6d6bd}Pyrrhos{/color} recalls the dangerous encounters from a few hours back, though in his tales, he’s the one who saved your skin each time."
        else:
            $ custom16 = ""
        if bandit_highisland_joined and not shortcut_darkforest_bandit_dead_troll:
            $ custom17 = "\n\n{color=#f6d6bd}The bandit{/color} stays away from the others, listening carefully to each word."
        else:
            $ custom17 = ""
        if tulia_highisland_joined:
            $ custom18 = "\n\n{color=#f6d6bd}Tulia{/color} lets out a weak chuckle and helps the conversation keep to a friendly tone. She resembles the same woman you saw in the camp all these days back, but this time she holds herself like a leader."
        else:
            $ custom18 = ""
        if tzvi_highisland_joined:
            $ custom19 = "\n\n{color=#f6d6bd}Tzvi{/color} holds his black, soaked cloak in his hands. He says he can’t wait to put your coins to use and leave the peninsula for good."
        else:
            $ custom19 = ""
        if quintus_highisland_joined:
            $ custom20 = "\n\n{color=#f6d6bd}Quintus{/color} is moody, though you can’t tell if he’d rather fall asleep, get drunk, or eat a boar."
        else:
            $ custom20 = ""
        menu:
            '[custom1] Soon, your crew starts to plan their return home.[custom11][custom12][custom13][custom14][custom15][custom16][custom17][custom18][custom19][custom20]
            '
            'I rub my eyes. “We still need to reach {color=#f6d6bd}Gale Rocks{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I rub my eyes. “We still need to reach {color=#f6d6bd}Gale Rocks{/color}.”')
                $ highisland_returned = 1
                if pc_goal == "iwanttoberemembered":
                    $ pc_goal_iwanttoberememberedpoints += 2
                if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                    $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                if not world_endmode:
                    $ highisland_crew_returning = 1
                    menu:
                        'You take off your bundles splash your face with cold water. Now you need to take everyone to safety before you stop somewhere for the night.
                        \n\nYou’re going to end the day at...
                        '
                        'The southern crossroads.' if southerncrossroads_firsttime:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The southern crossroads.')
                            $ travel_destination = "southerncrossroads"
                            jump finaldestinationafterevent
                        'The western crossroads.' if westerncrossroads_firsttime:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western crossroads.')
                            $ travel_destination = "westerncrossroads"
                            jump finaldestinationafterevent
                        'Foggy Lake.' if foggylake_firsttime:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Foggy Lake.')
                            $ travel_destination = "foggylake"
                            jump finaldestinationafterevent
                        'The watchtower.' if watchtower_firsttime:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The watchtower.')
                            $ travel_destination = "watchtower"
                            jump finaldestinationafterevent
                else:
                    menu:
                        'You take off your bundles splash your face with cold water. You need to take everyone to safety, but then, it’ll be time to head back to {color=#f6d6bd}Hovlavan{/color}.
                        '
                        '“So, {color=#f6d6bd}Tulia{/color}. Let’s take all of them home, then head back to {color=#f6d6bd}Pelt{/color} and prepare ourselves for our journey to the city.”' if tulia_highisland_joined:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, {color=#f6d6bd}Tulia{/color}. Let’s take all of them home, then head back to {color=#f6d6bd}Pelt{/color} and prepare ourselves for our journey to the city.”')
                            $ tulia_about_highisland_narration = 1
                            $ travel_destination = "peltnorth"
                            jump finaldestinationafterevent
                        'I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.' if not tulia_highisland_joined and militarycamp_destroyed_firsttime_tulia:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt{/color}.')
                            $ travel_destination = "peltnorth"
                            jump finaldestinationafterevent
                        'The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.' if not tulia_highisland_joined and not militarycamp_destroyed_firsttime_tulia and militarycamp_destroyed_firsttime_southerncrossroads:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The camp may be destroyed, but maybe I can find {color=#f6d6bd}Tulia{/color} in {color=#f6d6bd}Pelt of the North{/color}.')
                            $ travel_destination = "peltnorth"
                            jump finaldestinationafterevent
                        'I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.' if not tulia_highisland_joined and not militarycamp_destroyed_firsttime_tulia and not militarycamp_destroyed_firsttime_southerncrossroads:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should return to the camp and speak with {color=#f6d6bd}Tulia{/color}.')
                            $ travel_destination = "southerncrossroads"
                            jump finaldestinationafterevent
