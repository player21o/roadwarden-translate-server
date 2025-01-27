###################### Druid's Cave / Druid Cave Inside

label druidcavecavernfirsttime01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I enter the cavern? I need a place to rest.”')
    $ druidcave_cave_open = 1
    menu:
        '“So be it. We are humble people en we do ne have much to offer, but at least the’s a scrap of floor for you to lie down on, en a stream to wash yourself. Follow me.”
        \n\nThe door, made of steel and surrounded by bricks, could protect a treasury, or an armory. The same amount of iron could be used for dozens of tools, or over a hundred high-quality spears. You wonder what would happen if there were no more druids around. Would scavengers detach it and melt it down? Would it stay here for centuries, as a relic of the past?
        \n\nThere’s a single plate in the middle, used to lock or unlock a latch, and an additional padlock, which requires its own, awkwardly large key. There may be a similar device on the other side.
        \n\nThe gate squeals, and moving it makes the man pant.
        '
        'We walk inside.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- We walk inside.')
            show areapicture druidcaveinside01 at basicfade
            hide druidcavebronzerod
            $ renpy.notify("New shelter unlocked.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
            play nature "audio/ambient/druidcaveinside01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            menu:
                'The cavern is austere, lit only by several candles. The corridor leading deeper underground is flooded. The air is humid, but free of mold and putridity, despite all the wooden furniture around.
                \n\nThe man points at a bunch of brown and gray furs laying on the floor, mostly taken from boars and deer, though there’s also an especially large one that belonged to a red-and-black bear. “Feel free to pile them up, they should make for a soft bed. Just be sure to spread them around when you wake up, I need them to cover as much of the ground as they can.”
                \n\nHe also nods toward a wooden table, where you see an array of expensive instruments made of glass, gold, and copper. Bottles, scales, knives, alembics, mortars, a crucible... “En if you do ne know much about alchemy, stay away. ‘Tis expensive, a keepsake. If I find a single scratch on it, you will ne be welcome here anymore.”
                '
                'I look at the woman lying in bed, covered by a blanket.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the woman laying in bed, covered by a blanket.')
                    menu:
                        'She’s more touched by time than the man. Her eyes are wide open and observe you with something between fear and curiosity, but when you make eye contact with her, she starts to murmur nervously and covers her head with a blanket.
                        \n\nThe man also notices her movement and strokes his beard when he sees you looking at her. “Tha’s ma wife, en the best thing you can do is to ignore her. Her soul is shattered, her shell is weak, she no longer speaks. She was the owner of this table.”
                        \n\nYou ask if she won’t be bothered by your presence and you see his sad smile. “She will forget about you soon after she looks away. But she’s dangerous, in a way. If you keep your distance, she will ne approach you, but when she’s stressed, her powers take control over her. Protecting a mad magic user... It’s difficult, traveler.”
                        '
                        'I nod. “I won’t bother her.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “I won’t bother her.”')
                            $ can_leave = 0
                            $ can_rest = 1
                            $ can_items = 1
                            menu:
                                'He nods and moves toward the door. “En you have my thanks. I will ne use the padlock, you can leave whenever you want. Your mount will be safe, you can be sure of it.” He leaves without another word.
                                '
                                'I approach the flooded corridor.' if not druidcave_cave_corridor:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the flooded corridor.')
                                    $ druidcave_cave_corridor = 1
                                    jump caverninsideactivity01
                                'I approach the alchemical instruments.' if pc_class != "scholar" and not druidcave_cave_alchemy:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
                                    jump caverninsideactivity02fail
                                'I approach the alchemical instruments.' if (pc_class == "scholar" and quarters < world_daylength and pc_hp) or (pc_class == "scholar" and quarters >= world_daylength and pc_hp and alchemytable_timer < day):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
                                    jump caverninsideactivity02
                                'I’m too exhausted to brew potions. (Required vitality: 1). (disabled)' if not pc_hp and pc_class == "scholar":
                                    pass
                                'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if alchemytable_timer >= day and pc_class == "scholar":
                                    pass
                                'I go outside.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                                    jump druidcaveregularleaving
                        '“I’m sorry for your loss.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sorry for your loss.”')
                            $ can_leave = 0
                            $ can_rest = 1
                            $ can_items = 1
                            menu:
                                'You caught him off guard, but after a couple of moments you see his smile. “Do ne be. She was ma best friend, en I’m glad she’s ne alone. I saw death, madness, en blood for many years, en whilst it feels different when it touches the people you love, I’m ready to help her. As much as I can.”
                                \n\nHe walks toward the door. “I will ne use the padlock, you can leave whenever you want. Your mount will be safe, you can be sure of it.” He leaves without another word.
                                '
                                'I approach the flooded corridor.' if not druidcave_cave_corridor:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the flooded corridor.')
                                    $ druidcave_cave_corridor = 1
                                    jump caverninsideactivity01
                                'I approach the alchemical instruments.' if pc_class != "scholar" and not druidcave_cave_alchemy:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
                                    jump caverninsideactivity02fail
                                'I approach the alchemical instruments.' if (pc_class == "scholar" and quarters < world_daylength and pc_hp) or (pc_class == "scholar" and quarters >= world_daylength and pc_hp and alchemytable_timer < day):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
                                    jump caverninsideactivity02
                                'I’m too exhausted to brew potions. (Required vitality: 1). (disabled)' if not pc_hp and pc_class == "scholar":
                                    pass
                                'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if alchemytable_timer >= day and pc_class == "scholar":
                                    pass
                                'I go outside.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                                    jump druidcaveregularleaving

###############################

label druidcavecavernregular01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to enter the cavern.”')
    menu:
        '“So be it. Let me open the door for you.”
        '
        'I follow him to the entrance.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow him to the entrance.')
            $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            show areapicture druidcaveinside01 at basicfade
            hide druidcavebronzerod
            play nature "audio/ambient/druidcaveinside01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            menu:
                '[druidcave_druid_inside_fluff]
                '
                'I approach the flooded corridor.' if not druidcave_cave_corridor:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the flooded corridor.')
                    $ druidcave_cave_corridor = 1
                    jump caverninsideactivity01
                'I approach the alchemical instruments.' if pc_class != "scholar" and not druidcave_cave_alchemy:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
                    jump caverninsideactivity02fail
                'I approach the alchemical instruments.' if (pc_class == "scholar" and quarters < world_daylength and pc_hp) or (pc_class == "scholar" and quarters >= world_daylength and pc_hp and alchemytable_timer < day):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
                    jump caverninsideactivity02
                'I’m too exhausted to brew potions. (Required vitality: 1). (disabled)' if not pc_hp and pc_class == "scholar":
                    pass
                'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if alchemytable_timer >= day and pc_class == "scholar":
                    pass
                'I go outside.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                    jump druidcaveregularleaving

label druidcavecavernwakingup:
    stop music fadeout 4.0
    show areapicture druidcaveinside01 at basicfade
    hide druidcavebronzerod
    $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ quarters += 1
    $ druidcave_druid_inside_fluff = ""
    $ druidcave_druid_inside_fluff = renpy.random.choice(['The woman is moving in her sleep.', 'The woman is sitting next to her bed, swaying back and forth.', 'The woman is crouching next to her bed, sobbing, covering her face with a cloth.', 'The woman is sitting next to the flooded corridor, with her legs in water, humming rhythmless melody.'])
    play nature "audio/ambient/druidcaveinside01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    menu:
        'The man has already left the chamber. Once you start scattering the furs across the floor, the stinging in your back goes away. [druidcave_druid_inside_fluff]
        '
        'I approach the flooded corridor.' if not druidcave_cave_corridor:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the flooded corridor.')
            $ druidcave_cave_corridor = 1
            jump caverninsideactivity01
        'I approach the alchemical instruments.' if pc_class != "scholar" and not druidcave_cave_alchemy:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
            jump caverninsideactivity02fail
        'I approach the alchemical instruments.' if (pc_class == "scholar" and quarters < world_daylength and pc_hp) or (pc_class == "scholar" and quarters >= world_daylength and pc_hp and alchemytable_timer < day):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
            jump caverninsideactivity02
        'I’m too exhausted to brew potions. (Required vitality: 1). (disabled)' if not pc_hp and pc_class == "scholar":
            pass
        'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if alchemytable_timer >= day and pc_class == "scholar":
            pass
        'I go outside.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
            jump druidcaveregularleaving

label druidcavecavernafteractivity:
    $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    menu:
        'What do you want to do?
        '
        'I approach the flooded corridor.' if not druidcave_cave_corridor:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the flooded corridor.')
            $ druidcave_cave_corridor = 1
            jump caverninsideactivity01
        'I approach the alchemical instruments.' if pc_class != "scholar" and not druidcave_cave_alchemy:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
            jump caverninsideactivity02fail
        'I approach the alchemical instruments.' if (pc_class == "scholar" and quarters < world_daylength and pc_hp) or (pc_class == "scholar" and quarters >= world_daylength and pc_hp and alchemytable_timer < day):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
            jump caverninsideactivity02
        'I’m too exhausted to brew potions. (Required vitality: 1). (disabled)' if not pc_hp and pc_class == "scholar":
            pass
        'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if alchemytable_timer >= day and pc_class == "scholar":
            pass
        'I go outside.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
            jump druidcaveregularleaving

label caverninsideactivity01:
    if not quest_explorepeninsula_description10c:
        $ quest_explorepeninsula_description10c = "The old mine set in {color=#f6d6bd}Hag Hills{/color} is flooded. There’s no point in trying to restore it."
        $ renpy.notify("Journal updated: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
    menu:
        'You take a candle to look down the corridor, but it doesn’t help much. It leads downward, you see the spot where the ceiling touches water. Mines often resemble labyrinths, and even if there’s any sort of magic which would allow you to swim without air, the risk that you would lose your way back is too grave.
        '
        'I approach the flooded corridor.' if not druidcave_cave_corridor:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the flooded corridor.')
            $ druidcave_cave_corridor = 1
            jump caverninsideactivity01
        'I approach the alchemical instruments.' if pc_class != "scholar" and not druidcave_cave_alchemy:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
            jump caverninsideactivity02fail
        'I approach the alchemical instruments.' if (pc_class == "scholar" and quarters < world_daylength and pc_hp) or (pc_class == "scholar" and quarters >= world_daylength and pc_hp and alchemytable_timer < day):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
            jump caverninsideactivity02
        'I’m too exhausted to brew potions. (Required vitality: 1). (disabled)' if not pc_hp and pc_class == "scholar":
            pass
        'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if alchemytable_timer >= day and pc_class == "scholar":
            pass
        'I go outside.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
            jump druidcaveregularleaving

label caverninsideactivity02fail:
    $ druidcave_cave_alchemy = 1
    menu:
        'The table is filled with tools that you just barely recognize, but you have no idea how to use them. The instruments, some of which are needlessly colorful, are fairly clean.
        '
        'I approach the flooded corridor.' if not druidcave_cave_corridor:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the flooded corridor.')
            $ druidcave_cave_corridor = 1
            jump caverninsideactivity01
        'I approach the alchemical instruments.' if pc_class != "scholar" and not druidcave_cave_alchemy:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
            jump caverninsideactivity02fail
        'I approach the alchemical instruments.' if (pc_class == "scholar" and quarters < world_daylength and pc_hp) or (pc_class == "scholar" and quarters >= world_daylength and pc_hp and alchemytable_timer < day):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the alchemical instruments.')
            jump caverninsideactivity02
        'I’m too exhausted to brew potions. (Required vitality: 1). (disabled)' if not pc_hp and pc_class == "scholar":
            pass
        'It’s already late, and my eyes hurt after the last potion I brewed. (disabled)' if alchemytable_timer >= day and pc_class == "scholar":
            pass
        'I go outside.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
            jump druidcaveregularleaving

label caverninsideactivity02:
    if not druidcave_cave_alchemy_used:
        $ druidcave_cave_alchemy_used = 1
        $ custom6 = "The table and shelves contain precise tools and a decent supply of basic substances used as a base for various potions, balms, or powders, though some of them are a bit too old to be of use.\n\nAlchemical procedures take at least a couple of hours which involve complex preparations of tools, mixing of ingredients, and maintaining the brewing process. Because of this, you have to be of a strong shell and sharp soul to make any mixture. Some of them can only be used once.\n\nWhich mixture would you like to learn more about?"
    else:
        $ custom6 = "Which mixture would you like to learn more about?"
    menu:
        '[custom6]
        '
        'The herbal bug repellent I could use at the watchtower.' if quest_explorepeninsula_description05 and not watchtower_tower_bugs_cleared and not item_bugrepellent:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The herbal bug repellent I could use at the watchtower.')
            jump druidcavealchemytablebugrepellent01
        'The ointment that could help me at the ford.' if ford_firsttime and not ford_insects_dealtwith and not item_stingointment:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The ointment that could help me at the ford.')
            jump druidcavealchemytablestingointment01
        'A healing potion.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- A healing potion.')
            jump druidcavealchemytablehealingpotion01
        'The blinding powder that could help me in combat.' if not item_blindingpowder:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- A blinding powder that could help me in combat.')
            jump druidcavealchemytabletheblindingpowder01
        'The withering dust, for removing bushes and shrubs.' if not item_witheringdust:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The withering dust, for removing bushes and shrubs.')
            jump druidcavealchemytablewitheringdust01
        'The sharpening poison that can enhance my senses in combat.' if not achievement_alchemy_sharpeningpotion:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The sharpening poison that can enhance my senses in combat.')
            jump druidcavealchemytablesharpeningpotion01
        'I already have an herbal bug repellent. (disabled)' if item_bugrepellent:
            pass
        'I don’t need another bug repellent. (disabled)' if not item_bugrepellent and achievement_alchemy_bugrepellent:
            pass
        'I already have a sting ointment. (disabled)' if item_stingointment:
            pass
        'I already have the blinding powder. (disabled)' if item_blindingpowder:
            pass
        'I already have the withering dust. (disabled)' if item_witheringdust:
            pass
        'I already made the sharpening poison. (disabled)' if achievement_alchemy_sharpeningpotion:
            pass
        'I step away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
            jump druidcavecavernafteractivity

    label druidcavealchemytablebugrepellent01:
        menu:
            'You can’t make all of the bugs disappear in a day, but you know the recipe for a strong, poisonous balm with a tempting smell. It will kill most of these creatures right after consumption, while others will take pieces of it to their lairs and either eliminate their colonies, or force them to resettle. At least that’s what you’ve read.
            \n\nIt won’t help much with spiders, but the little ones aren’t dangerous anyway.
            \n\n{color=#f6d6bd}Preparation time:{/color} 2 hours
            '
            'I better get to foraging, then.' if quarters <= (world_daylength-8):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better get to foraging, then.')
                $ quarters += 8
                $ item_bugrepellent = 1
                $ achievement_alchemy_bugrepellent += 1
                $ renpy.notify("You made a jar of bug repellent.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You made a jar of bug repellent.{/i}')
                menu:
                    'You look for rue, wormwood, catmint, pale lavender, and wolf leaf, and you’re lucky to come across some clover and dill. Once you bring them all back to the table, you start with your knife and end with a mortar. It may not be a “real” alchemy, but the smell is quite something. At first harsh, pinching, then gentle and sweet. You add a drop of linseed oil, and the leaves blend into a green ointment.
                    '
                    'I wash one of the jars that are on a shelf and use it to store the balm.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash one of the jars that are on a shelf and use it to store the balm.')
                        jump druidcavecavernafteractivity
            'It’s already too dark for collecting herbs. (disabled)' if quarters > (world_daylength-8):
                pass
            'Maybe another time.':
                jump caverninsideactivity02

    label druidcavealchemytablestingointment01:
        menu:
            'The balm you know of won’t be enough to make the insects leave the water bank, but once you’ll put it on your skin, they should cease their bites. You can easily make a whole jar at once, and share it with your mount.
            \n\n{color=#f6d6bd}Preparation time:{/color} 1 hour
            '
            'I better get to foraging, then.' if quarters <= (world_daylength-4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better get to foraging, then.')
                $ quarters += 4
                $ item_stingointment = 1
                $ achievement_alchemy_stingointment += 1
                $ renpy.notify("You made a jar of sting ointment.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You made a jar of sting ointment.{/i}')
                menu:
                    'The herbs you’re looking for, such as basil, mint, and lavender, are common around here. You wash them with care and bring them all back to the table, where you start with your knife and end with a mortar. It would feel like cooking, if it wasn’t for the smell - harsh, overwhelming, it makes you sneeze more than once. You add a drop of linseed oil, and the leaves blend into a green and blue ointment.
                    '
                    'I wash one of the jars that are on a shelf and use it to store the balm.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash one of the jars that are on a shelf and use it to store the balm.')
                        jump druidcavecavernafteractivity
            'It’s already too dark for collecting herbs.' if quarters > (world_daylength-4):
                pass
            'Maybe another time.':
                jump caverninsideactivity02

    label druidcavealchemytabletheblindingpowder01:
        if item_cursedsoil:
            $ custom1 = "a jar of soil touched by a curse"
        else:
            $ custom1 = "{color=#6a6a6a}a jar of soil touched by a curse{/color}"
        if item_powderedrock:
            $ custom2 = "an entire basalt rock powdered at the top of a mountain"
        else:
            $ custom2 = "{color=#6a6a6a}an entire basalt rock powdered at the top of a mountain{/color}"
        menu:
            'The blinding powder doesn’t affect dry skin, but once it touches one’s eyes or tongue, it causes a painful burn. A pinch of it will blind a creature for a few minutes, while the larger doses take away one’s eyesight indefinitely. A single pouch will be enough for a couple of uses.
            \n\n{color=#f6d6bd}The first recipe requires:{/color} [custom1], [custom2]
            \n\n{color=#f6d6bd}Preparation time:{/color} 1 hour
            '
            'I make the powder.' if item_cursedsoil and item_powderedrock:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make the powder.')
                $ item_blindingpowder += 1
                $ item_cursedsoil -= 1
                $ item_powderedrock -= 1
                $ achievement_alchemy_blindingpowder += 1
                $ quarters += 4
                $ alchemytable_timer = day
                $ renpy.notify("You’ve created the blinding powder.\nYou lost the cursed soil\nand the powdered basalt.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve created the blinding powder.\nYou lost the cursed soil\nand the powdered basalt.{/i}')
                menu:
                    'You place a stool in a convenient spot, letting your arms rest on the table. Paying close attention, you fill a copper cauldron with an even layer of powder, then warm it up slightly. Keeping track of time with an hourglass, you move the flame to a different spot after every minute, then mark these positions in your wax tablet to avoid any mistakes.
                    \n\nFor half an hour, you heat up the tiniest speck of dust, then open the jar with soil and add it to the pot, mixing with a ladle. You keep doing so until you notice the effects of the pneuma. The entire mixture suddenly gets clay-brown, shrinks in half, and after you touch it, it’s ice-cold.
                    \n\nYou fill up a pouch and shake it around. You won’t underestimate your new weapon.
                    '
                    'I clean up everything and step away from the table.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clean up everything and step away from the table.')
                        jump druidcavecavernafteractivity
            'I don’t have all of the ingredients. (disabled)' if not item_cursedsoil or not item_powderedrock:
                pass
            'Maybe another time.':
                jump caverninsideactivity02

    label druidcavealchemytablehealingpotion01:
        if item_blackwoundwort:
            $ custom1 = "a bundle of black woundwort"
        else:
            $ custom1 = "{color=#6a6a6a}a bundle of black woundwort{/color}"
        if item_marshbules:
            $ custom2 = "a bunch of marshbules"
        else:
            $ custom2 = "{color=#6a6a6a}a bunch of marshbules{/color}"
        if item_shortcutherbs:
            $ custom3 = "some of the of herbs from the heart of the forest"
        else:
            $ custom3 = "{color=#6a6a6a}a collection of meadow herbs from the deep forest{/color}"
        menu:
            'Healing potions may be the most desired liquid in The Dragonwoods, especially among the travelers, hunters, and fighters. The ones you’ve followed so far are capable of keeping a soul on the verge of death, though it won’t “fix” a freshly cut off limb, nor cleanse one’s shell from an illness or poison.
            \n\nIt can only be used once.
            \n\n{color=#f6d6bd}The first recipe requires:{/color} [custom1], [custom2]
            \n\n{color=#f6d6bd}The second recipe requires:{/color} [custom3], [custom2]. You’ll keep the rest of the herbs.
            \n\n{color=#f6d6bd}Preparation time:{/color} 3 hours
            '
            'I use the first recipe.' if item_blackwoundwort and item_marshbules:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use the first recipe.')
                $ item_generichealingpotion += 1
                $ achievement_alchemy_healingpotion += 1
                $ item_blackwoundwort -= 1
                $ item_marshbules -= 1
                $ quarters += 12
                $ alchemytable_timer = day
                $ renpy.notify("You’ve brewed a healing potion.\nYou lost a bundle of woundwort\nand a bunch of marshbules.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve brewed a healing potion. You lost a bundle of woundwort and a bunch of marshbules.{/i}')
                menu:
                    'You chop and grind over two dozen of various herbs into a green pulp, making an ointment with a strong, woundworty smell, then mix it with the juice of carefully squeezed marshbules, clean of any seeds and peels. So far, so good.
                    \n\nThen you spend long, long minutes at the table, constantly keeping the liquid on the brink of boiling, every now and then lowering and raising the small cauldron that hangs above the flame of an oil lamp. The boredom bites your fingers, but you don’t even have the time to go grab some water to drink.
                    \n\nYou think of the alchemists who spend day after day repeating this procedure in their workshops. Hardly a tempting vision.
                    \n\nAt least the room is now filled with a pleasant aroma, making the nearby woman much calmer than usual. You pour the grass-green liquid into one of the earthenware bottles, then seal it. The potion is ready.
                    '
                    'I clean up everything and step away from the table.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clean up everything and step away from the table.')
                        jump druidcavecavernafteractivity
            'I can’t use the first recipe. (disabled)' if not item_blackwoundwort or not item_marshbules:
                pass
            'I use the second recipe.' if item_blackwoundwort and item_shortcutherbs:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use the second recipe.')
                $ item_generichealingpotion += 1
                $ achievement_alchemy_healingpotion += 1
                $ item_blackwoundwort -= 1
                $ quarters += 12
                $ alchemytable_timer = day
                $ renpy.notify("You’ve brewed a healing potion.\nYou lost a bundle of woundwort.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve brewed a healing potion. You lost a bundle of woundwort.{/i}')
                menu:
                    'You chop and grind over a dozen of various herbs into a green pulp, making an ointment with a strong, woundworty smell. So far, so good.
                    \n\nThen you spend long, long minutes at the table, constantly keeping the liquid on the brink of boiling, every now and then lowering and raising the small cauldron that hangs above the flame of an oil lamp. The boredom bites your fingers, but you don’t even have the time to go grab some water to drink.
                    \n\nYou think of the alchemists who spend day after day repeating this procedure in their workshops. Hardly a tempting vision.
                    \n\nAt least the room is now filled with a pleasant aroma, making the nearby woman much calmer than usual. You pour the grass-green liquid into one of the earthenware bottles, then seal it. The potion is ready.
                    '
                    'I clean up everything and step away from the table.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clean up everything and step away from the table.')
                        jump druidcavecavernafteractivity
            'I can’t use the second recipe. (disabled)' if not item_blackwoundwort or not item_shortcutherbs:
                pass
            'Maybe another time.':
                jump caverninsideactivity02

    label druidcavealchemytablewitheringdust01:
        if item_driftwood:
            $ custom1 = "a piece of flower-shaped driftwood"
        else:
            $ custom1 = "{color=#6a6a6a}a piece of flower-shaped driftwood{/color}"
        if item_bogfriend:
            $ custom2 = "a bogfriend picked in the middle of the day"
        else:
            $ custom2 = "{color=#6a6a6a}a bogfriend picked in the middle of the day{/color}"
        menu:
            'A yellow dust that’s meant to “wither” any plant. To use it, you should spread it on the ground near the roots, then sprinkle it with water. It doesn’t take a lot of dust at once, so a single bag will be a decent supply.
            \n\n{color=#f6d6bd}The recipe requires:{/color} [custom1], [custom2]
            \n\n{color=#f6d6bd}Preparation time:{/color} 1 hour
            '
            'I make the dust.' if item_driftwood and item_bogfriend:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make the dust.')
                $ item_witheringdust += 1
                $ achievement_alchemy_witheringdust += 1
                $ item_driftwood -= 1
                $ item_bogfriend -= 1
                $ quarters += 4
                $ alchemytable_timer = day
                $ renpy.notify("You’ve created a bag of withering dust.\nYou lost the driftwood\nand the bogfriend.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve created a bag of withering dust. You lost the spider venom and the bogfriend.{/i}')
                menu:
                    'You start by setting the driftwood on fire, then chop and roast the bogfriend, which for reasons unknown to you turns into a dust-like powder. You grind together the seeds of coriander, pepper, and celery and add them to the mushroom, making a pleasantly smelling mixture.
                    \n\nYou then grab one of the yellow calcites and break it into smaller pieces with a stone-ended club, then grind it to dust in a mortar, together with the seeds and dried, toxic plants that you were carrying among your own supplies. The longer it takes, the more foul the smell becomes. You chop and mash the garlic, mix it with some of the dust that fell off of the wood, add to the bowl, and allow yourself to take a short break.
                    \n\nThe pneuma fills your creation, drying it in just a few moments, then turning the entire mixture into an ash-colored dust. You make sure that your gloves are dry, then grind some more, until the smell completely disappears. You sweep everything into a leather bag, leaving not a single mote behind.
                    '
                    'I clean up everything and step away from the table.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clean up everything and step away from the table.')
                        jump druidcavecavernafteractivity
            'I don’t have all of the ingredients. (disabled)' if not item_driftwood or not item_bogfriend:
                pass
            'Maybe another time.':
                jump caverninsideactivity02

    label druidcavealchemytablesharpeningpotion01:
        if item_snakebait:
            $ custom1 = "a snake bait flower"
        else:
            $ custom1 = "{color=#6a6a6a}a snake bait flower{/color}"
        if item_cavemushroom:
            $ custom2 = "a cave ear mushroom"
        else:
            $ custom2 = "{color=#6a6a6a}a cave ear mushroom{/color}"
        menu:
            'After consumption, it makes one’s senses quicker and alerted. It gives an edge in combat for the rest of combat, but puts a burden on the shell during nightfall. You can make three doses at once.
            \n\n{color=#f6d6bd}The recipe requires:{/color} [custom1], [custom2]
            \n\n{color=#f6d6bd}Preparation time:{/color} 2 hours
            '
            'I make the poison.' if item_snakebait and item_cavemushroom:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make the poison.')
                $ item_sharpeningpotion += 3
                $ achievement_alchemy_sharpeningpotion += 1
                $ item_snakebait -= 1
                $ item_cavemushroom -= 1
                $ quarters += 8
                $ alchemytable_timer = day
                $ renpy.notify("You’ve created three doses of sharpening poison.\nYou lost the snake bait\nand the cave ear.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve created three doses of sharpening poison.\nYou lost the snake bait\nand the cave ear.{/i}')
                menu:
                    'You can’t dry up the mushroom, so you cut it in cubes and fry it above a gentle flame while keeping the orange petals in the hot air. You pick the mortar and pestle and prepare various dried herbs, tearing them with your fingers. You’re almost sure that at least the sage is not essential for the recipe, but adding to the powder’s final volume will reduce the substance’s intensity, and will make the dosing easier.
                    \n\nThe pleasant smell of a dinner is followed by long minutes of chopping, smashing, and grinding. Finally, the pneuma fills your creation - the entire mixture soaks up with the intense color of the snake bait. You fill up a small, wooden box.
                    '
                    'I clean up everything and step away from the table.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clean up everything and step away from the table.')
                        jump druidcavecavernafteractivity
            'I don’t have all of the ingredients. (disabled)' if not item_snakebait or not item_cavemushroom:
                pass
            'Maybe another time.':
                jump caverninsideactivity02

label druidcaveregularleaving:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "druidcave1"
    play nature "audio/ambient/druidcave01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if druidcave_druid_about_herbs == 2:
        show areapicture druidcave01alt02 at basicfade behind druidcavebronzerod
    else:
        show areapicture druidcave01 at basicfade behind druidcavebronzerod
    if eudocia_bronzerod_rodin_druidcave:
        show druidcavebronzerod at basicfade
    menu:
        'The druid is weeding the garden patches and doesn’t pay attention to you.
        '
        '(druidcave1 set)':
            pass
