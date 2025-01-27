###################### FORAGING GROUND
default foragingground_firsttime = 0
default foragingground_fluff = ""
default foragingground_fluff_old = ""

default foragingground_quest_timer = 20
default foragingground_bird_gone = 0
default foragingground_bird_timer = 0
default foragingground_bird_timer_max = 8
default foragingground_bird_threshold_timer = 3
default foragingground_bird_threshold = 0
default foragingground_bird_taken = 0 # 1 - taken, 2 - killed, 3 - escaped
default foragingground_bird_charged = 0
default foragingground_bird_charged_stopped = 0
default foragingground_bird_weaponsamount = 0
default foragingground_bird_timesdodged = 0

default foragingground_bird_used_stoat = 0
default foragingground_bird_used_chicken = 0
# default foragingground_bird_used_fish = 0
default foragingground_bird_used_shield = 0
default foragingground_bird_used_spear = 0
default foragingground_bird_used_rope = 0
default foragingground_bird_used_blindingpowder = 0
default foragingground_bird_used_crossbow = 0

default foragingground_bird_dmgtopc = 0

default foragingground_foragers_tofoggylake = 0
default foragingground_foragers_toforagingground = 0

default foragingground_foraging_amount = 0
default foragingground_foraging_day = 0
default foragingground_foraging_bag = 0
default foragingground_foraging_vein = 0
default foragingground_foraging_vein_sabotaged = 0
default foragingground_foraging_vein_rumor = 0

label foragingground01:
    nvl clear
    $ pc_area = "foragingground"
    stop music fadeout 4.0
    play nature "audio/ambient/foragingground01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture foragingground01 at basicfade
    label foragingground_fluffloop:
        if quarters < (world_daylength-12):
            $ foragingground_fluff = renpy.random.choice(['Your palfrey looks around. The short grass wouldn’t fill its stomach even after hours of grazing.', 'The sparse shrubs and bushes have been stripped of every berry, and there are no flowers among their leaves.', 'As far as you can tell, none of the nearby mushrooms can be trusted. Even the ants avoid them.', 'The sky is filled with croaking arguments of the mountain birds, and you notice almost no insects around you.', 'The valley seems especially peaceful today. A couple of lizards are resting on the rocks, basking with no worries.', 'Some little, furry critters flee away from you through the short grass. Nothing here is as loud as your palfrey’s hooves.'])
        else:
            $ foragingground_fluff = renpy.random.choice(['Your palfrey looks around. The short grass wouldn’t fill its stomach even after hours of grazing.', 'The sparse shrubs and bushes have been stripped of every berry, and there are no flowers among their leaves.', 'As far as you can tell, none of the nearby mushrooms can be trusted. Even the ants avoid them.', 'The sky is filled with croaking arguments of the mountain birds, and you notice almost no insects around you.', 'The valley seems especially peaceful today. A couple of lizards are resting on the rocks, basking with no worries.', 'Some little, furry critters flee away from you through the short grass. Nothing here is as loud as your palfrey’s hooves.'])
        if foragingground_fluff_old == foragingground_fluff:
            jump foragingground_fluffloop
        else:
            $ foragingground_fluff_old = foragingground_fluff
    if foragingground_firsttime < 2:
        $ world_known_npcs += 0
        $ foragingground_firsttime = 2
        $ world_known_areas += 1
        $ huntercabin_unlocked = 1
        $ wanderer_unlocked = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if foragingground_foragers_toforagingground:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            jump foraginggroundfirsttime01foragers
        else:
            jump foraginggroundfirsttime01
    else:
        if foragingground_foragers_toforagingground:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            jump foraginggroundregular01foragers
        elif elah_quest_easternpath_lumberjacks == 1:
            jump creekselahaboutquesteasternroadfallentree05
        else:
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            jump foraginggroundregular01

label foraginggroundfirsttime01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        'The valley is flanked by the hills. To the west the grasses and bushes blend into the horizon and turn into another part of the forest. The southern hills are gray and tall, with fortress-like rock faces and a crown of conifers. The northern ones have countless sand-colored rocks, lumped together like piles of rubble and clay, bearing hardly any soil or weeds.
        \n\nThe plants here are struggling. The grass is short and yellowish, sometimes dried out. The bushes have silver leaves, like many plants from sunny areas. The mushrooms can’t hide in the shadows, but as you approach one, you see it’s growing from the remains of a dead bird, while others are covering old branches and other plants. They won’t last much longer.
        '
        'It will be easy to spot any larger beasts around.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will be easy to spot any larger beasts around.')
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            if day > foragingground_quest_timer and not foragingground_bird_taken and not foragingground_bird_gone:
                $ foragingground_bird_gone = 1
            if watchtower_unlocked:
                $ custom1 = "fresher than on any other part of the eastern road."
            else:
                $ custom1 = "fresher than even on the western roads."
            if not foragingground_bird_taken and not foragingground_bird_gone:
                $ custom2 = "You have to squint to spot the first threatening creature. A runner is in the far east, close to the hills, though it completely ignores you, walking around and observing the grass, looking for its next prey. You don’t have to worry about it for now.\n\n"
            else:
                $ custom2 = "Even though you squint, you spot no creature that you need to worry about. "
            menu:
                '[custom2]There are boot prints on the road, as well as in the short grass, [custom1] Since many mushrooms were cut away with a knife and you notice few berries on the shrubs, you conclude it’s a foraging spot for the people from the North, though there doesn’t seem to be much food left.
                \n\nThere are almost no prints leading farther south.
                '
                'I shouldn’t fight this bird by myself... But maybe I can scare it off.' if foragingground_foraging_amount != 0 and not foragingground_bird_taken and not foragingground_bird_gone:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shouldn’t fight this bird by myself... But maybe I can scare it off.')
                    jump foraginggroundtakingalookatequipment01
                'I could take a look at the remains in the small ravine. I ride there and prepare my equipment.' if foragingground_foraging_bag and not foragingground_foraging_vein:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could take a look at the remains in the small ravine. I ride there and prepare my equipment.')
                    jump foraginggroundexploringravine01
                'I follow the directions to the spot where the dead man was found.' if (foragingground_foraging_vein_rumor and foragingground_bird_taken and not foragingground_foraging_vein and not foragingground_foraging_bag) or (foragingground_foraging_vein_rumor and foragingground_bird_gone and not foragingground_foraging_vein and not foragingground_foraging_bag):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the directions to the spot where the dead man was found..')
                    jump foraginggroundexploringravine01ALT
                'I could follow the directions to the spot where the dead man was found, but the bird is just nearby. (disabled)' if foragingground_foraging_vein_rumor and not foragingground_bird_taken and not foragingground_bird_gone and not foragingground_foraging_vein and not foragingground_foraging_bag:
                    pass
                'I could try to forage for a bit.' if foragingground_foraging_amount <= 0 and not foragingground_bird_taken and not foragingground_bird_gone:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could try to forage for a bit.')
                    jump foraginggroundforaging01bird
                'I could try to forage for a bit, but not while the bird is near. (disabled)' if foragingground_foraging_amount and not foragingground_bird_taken and not foragingground_bird_gone:
                    pass
                'I won’t find much more food today. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day == day and foragingground_foraging_amount < 4) or (foragingground_bird_gone and foragingground_foraging_day == day and foragingground_foraging_amount < 4):
                    pass
                'Since the area is free of beasts, I spend some time foraging.' if (foragingground_bird_taken and foragingground_foraging_day != day and not foragingground_foraging_amount and quarters < (world_daylength-4)) or (foragingground_bird_gone and foragingground_foraging_day != day and not foragingground_foraging_amount and quarters < (world_daylength-4)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since the area is free of beasts, I spend some time foraging.')
                    jump foraginggroundforaging01
                'I could try to forage, though it will take even more time.' if (foragingground_bird_taken and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount < 4 and quarters < (world_daylength-4)) or (foragingground_bird_gone and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount < 4 and quarters < (world_daylength-4)):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could try to forage, though it will take even more time.')
                    jump foraginggroundforaging01
                'I’ve been foraging here a lot. I won’t find much more food. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount >= 4) or (foragingground_bird_gone and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount >= 4):
                    pass
                'It’s too dark to forage. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day != day and foragingground_foraging_amount < 4 and quarters >= (world_daylength-4)) or (foragingground_bird_gone and foragingground_foraging_day != day and foragingground_foraging_amount < 4 and quarters >= (world_daylength-4)):
                    pass

label foraginggroundregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if day > foragingground_quest_timer and not foragingground_bird_taken and not foragingground_bird_gone:
        $ foragingground_bird_gone = 1
        $ achievement_animalssavedpoints += 1
    if not foragingground_bird_taken and not foragingground_bird_gone:
        $ custom1 = "The runner is still in sight, looking for prey."
    else:
        $ custom1 = "You don’t spot any larger predator."
    menu:
        '[foragingground_fluff] [custom1]
        '
        'I shouldn’t fight this bird by myself... But maybe I can scare it off.' if foragingground_foraging_amount != 0 and not foragingground_bird_taken and not foragingground_bird_gone:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shouldn’t fight this bird by myself... But maybe I can scare it off.')
            jump foraginggroundtakingalookatequipment01
        'I could take a look at the remains in the small ravine. I ride there and prepare my equipment.' if foragingground_foraging_bag and not foragingground_foraging_vein:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could take a look at the remains in the small ravine. I ride there and prepare my equipment.')
            jump foraginggroundexploringravine01
        'I follow the directions to the spot where the dead man was found.' if (foragingground_foraging_vein_rumor and foragingground_bird_taken and not foragingground_foraging_vein and not foragingground_foraging_bag) or (foragingground_foraging_vein_rumor and foragingground_bird_gone and not foragingground_foraging_vein and not foragingground_foraging_bag):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the directions to the spot where the dead man was found.')
            jump foraginggroundexploringravine01ALT
        'I could follow the directions to the spot where the dead man was found, but the bird is just nearby. (disabled)' if foragingground_foraging_vein_rumor and not foragingground_bird_taken and not foragingground_bird_gone and not foragingground_foraging_vein and not foragingground_foraging_bag:
            pass
        'I could try to forage for a bit.' if foragingground_foraging_amount <= 0 and not foragingground_bird_taken and not foragingground_bird_gone:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could try to forage for a bit.')
            jump foraginggroundforaging01bird
        'I could try to forage for a bit, but not while the bird is near. (disabled)' if foragingground_foraging_amount and not foragingground_bird_taken and not foragingground_bird_gone:
            pass
        'I won’t find much more food today. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day == day and foragingground_foraging_amount < 4) or (foragingground_bird_gone and foragingground_foraging_day == day and foragingground_foraging_amount < 4):
            pass
        'Since the area is free of beasts, I spend some time foraging.' if (foragingground_bird_taken and foragingground_foraging_day != day and not foragingground_foraging_amount and quarters < (world_daylength-4)) or (foragingground_bird_gone and foragingground_foraging_day != day and not foragingground_foraging_amount and quarters < (world_daylength-4)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since the area is free of beasts, I spend some time foraging.')
            jump foraginggroundforaging01
        'I could try to forage, though it will take even more time.' if (foragingground_bird_taken and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount < 4 and quarters < (world_daylength-4)) or (foragingground_bird_gone and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount < 4 and quarters < (world_daylength-4)):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could try to forage, though it will take even more time.')
            jump foraginggroundforaging01
        'I’ve been foraging here a lot. I won’t find much more food. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount >= 4) or (foragingground_bird_gone and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount >= 4):
            pass
        'It’s too dark to forage. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day != day and foragingground_foraging_amount < 4 and quarters >= (world_daylength-4)) or (foragingground_bird_gone and foragingground_foraging_day != day and foragingground_foraging_amount < 4 and quarters >= (world_daylength-4)):
            pass

    label foraginggroundafterinteraction01:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'You prepare yourself for the further journey.
            '
            'I shouldn’t fight this bird by myself... But maybe I can scare it off.' if foragingground_foraging_amount != 0 and not foragingground_bird_taken and not foragingground_bird_gone:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shouldn’t fight this bird by myself... But maybe I can scare it off.')
                jump foraginggroundtakingalookatequipment01
            'I could take a look at the remains in the small ravine. I ride there and prepare my equipment.' if foragingground_foraging_bag and not foragingground_foraging_vein:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could take a look at the remains in the small ravine. I ride there and prepare my equipment.')
                jump foraginggroundexploringravine01
            'I follow the directions to the spot where the dead man was found.' if (foragingground_foraging_vein_rumor and foragingground_bird_taken and not foragingground_foraging_vein and not foragingground_foraging_bag) or (foragingground_foraging_vein_rumor and foragingground_bird_gone and not foragingground_foraging_vein and not foragingground_foraging_bag):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the directions to the spot where the dead man was found.')
                jump foraginggroundexploringravine01ALT
            'I could follow the directions to the spot where the dead man was found, but the bird is just nearby. (disabled)' if foragingground_foraging_vein_rumor and not foragingground_bird_taken and not foragingground_bird_gone and not foragingground_foraging_vein and not foragingground_foraging_bag:
                pass
            'I could try to forage for a bit.' if foragingground_foraging_amount <= 0 and not foragingground_bird_taken and not foragingground_bird_gone:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could try to forage for a bit.')
                jump foraginggroundforaging01bird
            'I could try to forage for a bit, but not while the bird is near. (disabled)' if foragingground_foraging_amount and not foragingground_bird_taken and not foragingground_bird_gone:
                pass
            'I won’t find much more food today. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day == day and foragingground_foraging_amount < 4) or (foragingground_bird_gone and foragingground_foraging_day == day and foragingground_foraging_amount < 4):
                pass
            'Since the area is free of beasts, I spend some time foraging.' if (foragingground_bird_taken and foragingground_foraging_day != day and not foragingground_foraging_amount and quarters < (world_daylength-4)) or (foragingground_bird_gone and foragingground_foraging_day != day and not foragingground_foraging_amount and quarters < (world_daylength-4)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since the area is free of beasts, I spend some time foraging.')
                jump foraginggroundforaging01
            'I could try to forage, though it will take even more time.' if (foragingground_bird_taken and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount < 4 and quarters < (world_daylength-4)) or (foragingground_bird_gone and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount < 4 and quarters < (world_daylength-4)):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could try to forage, though it will take even more time.')
                jump foraginggroundforaging01
            'I’ve been foraging here a lot. I won’t find much more food. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount >= 4) or (foragingground_bird_gone and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount >= 4):
                pass
            'It’s too dark to forage. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day != day and foragingground_foraging_amount < 4 and quarters >= (world_daylength-4)) or (foragingground_bird_gone and foragingground_foraging_day != day and foragingground_foraging_amount < 4 and quarters >= (world_daylength-4)):
                pass

label foraginggroundscaringthebardawayALL:
    label foraginggroundtakingalookatequipment01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ foragingground_bird_weaponsamount = 0
        if pc_class == "mage":
            $ at_unlock_spell = 1
            $ manacost = 3
            $ at = 0
        if item_crossbow and item_crossbowquarrels:
            $ foragingground_bird_weaponsamount += 1
            $ custom1 = "You could start with a shot from a crossbow."
        elif item_crossbow and not item_crossbowquarrels:
            $ foragingground_bird_weaponsamount += 0
            $ custom1 = "{color=#6a6a6a}You could start with a shot from a crossbow, but you have no quarrels left.{/color}"
        else:
            $ custom1 = "{color=#6a6a6a}You don’t possess a ranged weapon.{/color}"
        if item_blindingpowder:
            $ foragingground_bird_weaponsamount += 1
            $ custom2 = "\n\nThe blinding powder will do for a surprise attack."
        elif not item_blindingpowder and pc_class == "scholar":
            $ custom2 = "\n\n{color=#6a6a6a}You possess no blinding powder.{/color}"
        else:
            $ custom2 = ""
        if pc_class == "mage" and mana >= manacost:
            $ foragingground_bird_weaponsamount += 1
            $ custom3 = "\n\nYou could strike it with a spell from a medium range. Cost: {color=#f6d6bd}3{/color}"
        elif pc_class == "mage" and mana < manacost:
            $ custom3 = "\n\n{color=#6a6a6a}You lack pneuma to strike it with a spell from a medium range. Cost: 3{/color}"
        else:
            $ custom3 = ""
        if item_mountainroadspear or item_asterionspear:
            $ foragingground_bird_weaponsamount += 1
            $ custom4 = "\n\nYour spear will help you stop the beast’s charge."
        elif item_shield:
            $ foragingground_bird_weaponsamount += 1
            $ custom4 = "\n\nYour shield will help you stop the beast’s charge."
        elif pc_class == "warrior":
            $ foragingground_bird_weaponsamount += 1
            $ custom4 = "\n\nYou lack a close-range weapon that could stop the beast’s charge, but as an experienced warrior, you may handle a bit of dodging."
        else:
            $ custom4 = "\n\n{color=#6a6a6a}You lack a close-range weapon that could stop the beast’s charge.{/color}"
        if pc_hp >= 5:
            $ foragingground_bird_weaponsamount += 1
            $ custom5 = "\n\nYour shell is in great shape."
        elif pc_hp == 0:
            $ foragingground_bird_weaponsamount = 0
            $ custom5 = "\n\n{color=#6a6a6a}You are barely standing straight.{/color}"
        else:
            $ custom5 = ""
        menu:
            'You take a look at your bundles.
            \n\n[custom1][custom2][custom3][custom4][custom5]
            '
            'I have everything I need to take care of this.' ( condition="(foragingground_bird_weaponsamount >= 3) or (foragingground_bird_weaponsamount == 2 and at == 'spell')" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have everything I need to take care of this.')
                jump foraginggroundtakingalookatequipment01outcome1
            'I could still be better prepared for a fight. (disabled)' ( condition="(foragingground_bird_weaponsamount == 2) or (foragingground_bird_weaponsamount == 1 and at == 'spell') or (foragingground_bird_weaponsamount == 1) or (foragingground_bird_weaponsamount == 0 and at == 'spell')" ):
                pass
            '{image=d6} I’ll try to keep my distance, and hurt it before it gets too close.' ( condition="(foragingground_bird_weaponsamount == 2) or (foragingground_bird_weaponsamount == 1 and at == 'spell')" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ll try to keep my distance, and hurt it before it gets too close.')
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                $ d100roll -= pc_battlecounter
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if armor == 4:
                    $ d100roll -= 5
                $ foragingground_bird_gone = 1
                $ pc_battlecounter += 1
                if d100roll < 40:
                    jump foraginggroundtakingalookatequipment01outcome1
                else:
                    jump foraginggroundtakingalookatequipment01outcome2
            '{image=d6} I’ll trust my muscles.' ( condition="(foragingground_bird_weaponsamount == 1) or (foragingground_bird_weaponsamount == 0 and at == 'spell')" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ll trust my muscles.')
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                $ d100roll -= pc_battlecounter
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if armor == 4:
                    $ d100roll -= 5
                $ foragingground_bird_gone = 1
                $ pc_battlecounter += 1
                if d100roll < 40:
                    jump foraginggroundtakingalookatequipment01outcome2
                else:
                    jump foraginggroundtakingalookatequipment01outcome3
            'I have no equipment to help me here. (disabled)' ( condition="(foragingground_bird_weaponsamount == 0) and not (at == 'spell') and pc_hp" ):
                pass
            'I’m too exhausted to face the beast now. (Required vitality: 1) (disabled)' ( condition="pc_hp == 0" ):
                pass
            'Better to not risk it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Better to not risk it.')
                $ at_unlock_spell = 0
                $ at = 0
                jump foraginggroundafterinteraction01

    label foraginggroundtakingalookatequipment01outcome1:
        if item_crossbow and item_crossbowquarrels:
            $ custom1 = "You rest the crossbow’s stock on your shoulder, take a few deep breaths, and pull the trigger. The powerful arrow hits the beast’s chest. It wails in pain and anger, stumbles, but doesn’t fall or stop. You switch your gear."
            $ item_crossbowquarrels -= 1
            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
        else:
            $ custom1 = "Having nothing to shoot it with, you prepare your gear and jump in place, relaxing your shoulders."
        if item_blindingpowder:
            $ foragingground_bird_charged_stopped = 1
            $ custom2 = "\n\nOnce the bird gets so close you know it won’t stop, you step forward and throw a fistful of dust. It closes its eyelids almost in time. You jump - the beak cuts through the air behind you, and while the beast lets out a vague grunt, shaking its head to bring release to its aching eyes, it then seeks you again. You’re already back on your feet."
        else:
            $ custom2 = ""
        if at == 'spell':
            $ foragingground_bird_charged_stopped = 1
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
            $ custom3 = "\n\nOnce the bird gets so close you know it won’t stop, you step forward and raise your willow wand. Casting the pneuma feels like stabbing the air with a wooden dagger. The invisible wave strikes the creature while it’s jumping, sending it back into the ground. Shocked, it rolls twice, trying to get up, surrounded by a cloud of dust. It looks at you with new respect."
        else:
            $ custom3 = ""
        if pc_hp >= 5:
            $ custom5 = "Your strong, relaxed shell moves with confidence and determination. "
        else:
            $ custom5 = ""
        if item_mountainroadspear or item_asterionspear:
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, making a confident thrust with your spear. Still confused, it opens its beak in pain, shaking its orange head as it’s stepping away from you."
                $ custom6 = "leaving a trail of blood and "
            else:
                $ custom4 = "You almost crouch, using the ground to support your spear, and while the bird tries to change the direction of its charge, you manage to get through the layers of feathers. It opens its beak in pain, shaking its orange head as it’s stepping away from you."
                $ custom6 = "leaving a trail of blood and "
        elif item_shield:
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, holding the shield between the two of you like a wall. Still confused, it opens its beak in annoyance, shaking its orange head as it’s stepping away from you."
                $ custom6 = ""
            else:
                $ custom4 = "In the last moment, you move the shield between the two of you, using it to stop the charging monster, and while the impact sends you into the air, your shocked opponent rolls on the ground, trying to get up. Still confused, it opens its beak in annoyance, shaking its orange head as it’s stepping away from you."
                $ custom6 = ""
        elif pc_class == "warrior":
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, dashing at it with your axe and cutting through its layers of feathers. Still confused, it opens its beak in pain, shaking its orange head as it’s stepping away from you."
                $ custom6 = "leaving a trail of blood and "
            else:
                $ custom4 = "You wait to duck at the very last moment, then cut it while you’re still in the air, barely getting through the layers of feathers. Still confused, it leaves you behind and opens its beak in pain, shaking its orange head."
                $ custom6 = "leaving a trail of blood and "
        else:
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, dashing at it with your axe and landing a hit, even if not a strong one. Still confused, it opens its beak in pain, shaking its orange head as it’s stepping away from you."
                $ custom6 = ""
            else:
                $ custom4 = "You wait to duck at the very last moment, then cut it while you’re still in the air, though you fail to get through the layers of feathers. Confused, it leaves you behind and opens its beak in pain, shaking its orange head."
                $ custom6 = ""
        $ at_unlock_spell = 0
        $ at = 0
        $ cleanliness = limit_cleanliness(cleanliness-1)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        show minus1appearance at appearancechange onlayer myoverlay
        $ foragingground_bird_gone = 1
        $ pc_battlecounter += 1
        menu:
            'You grab everything you need and head toward the beast. It’s taller than {color=#f6d6bd}[horsename]{/color}, with wide breast and long, thick, partially feathered legs that could easily trample your chest. Its thighs are thick and powerful, the pointy beak could swallow your entire forearm. Once it notices your challenge, it runs at you, speeding up with every breath.
            \n\n[custom1][custom2][custom3]
            \n\n[custom5][custom4] Weakened, it turns around and flees in panic toward the western wilderness, [custom6]still finding strength to let out a furious screech. {color=#f6d6bd}[horsename]{/color} spares it a curious glance, but gets out of its way smoothly and trots toward you.
            \n\nYou may be covered in dust and sweat, but you get out of all this without as much as a scratch.
            '
            'I pack my stuff.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my staff.')
                jump foraginggroundafterinteraction01

    label foraginggroundtakingalookatequipment01outcome2:
        if item_crossbow and item_crossbowquarrels:
            $ custom1 = "You rest the crossbow’s stock on your shoulder, take a few deep breaths, and pull the trigger. The powerful arrow hits the beast’s chest. It wails in pain and anger, stumbles, but doesn’t fall or stop. You switch your gear."
            $ item_crossbowquarrels -= 1
            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
        else:
            $ custom1 = "Having nothing to shoot it with, you prepare your gear and jump in place, relaxing your shoulders."
        if item_blindingpowder:
            $ foragingground_bird_charged_stopped = 1
            $ custom2 = "\n\nOnce the bird gets so close you know it won’t stop, you step forward and throw a fistful of dust. It closes its eyelids almost in time. You jump away - the beak cuts through the air behind you, and while the beast lets out a vague grunt, shaking its head to bring release to its aching eyes, it then seeks you again. You’re already back on your feet."
        else:
            $ custom2 = ""
        if at == 'spell':
            $ foragingground_bird_charged_stopped = 1
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
            $ custom3 = "\n\nOnce the bird gets so close you know it won’t stop, you step forward and raise your willow wand. Casting the pneuma feels like stabbing the air with a wooden dagger. The invisible wave strikes the creature while it’s jumping, sending it back into the ground. Shocked, it rolls twice, trying to get up, surrounded by a cloud of dust. It looks at you with new respect."
        else:
            $ custom3 = ""
        if pc_hp >= 5:
            $ custom5 = "Your strong, relaxed shell moves with confidence and determination. "
        else:
            $ custom5 = ""
        if item_mountainroadspear or item_asterionspear:
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, making a confident thrust with your spear, but it’s fast enough to peck your arm in return. Your strike makes it shake its orange head, and it scurries away from you."
                $ custom6 = "leaving a trail of blood and "
            else:
                $ custom4 = "You almost crouch, using the ground to support your spear, and while the bird tries to change the direction of its charge, you manage to get through the layers of feathers. The bird is quick enough to strike your arm, but then passes you by, shaking its orange head from pain."
                $ custom6 = "leaving a trail of blood and "
        elif item_shield:
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, holding the shield between the two of you like a wall, yet the beast tries to land a hit after all. While the shield remains strong, the blow pushes you into the ground. The pain pierces through your back and you’re sure it’s too late to stand up, but the creature is scurrying away, shaking its orange head in confusion."
                $ custom6 = ""
            else:
                $ custom4 = "In the last moment, you move the shield between the two of you, using it to stop the charging monster, and the impact sends you into the air. The pain pierces through your back and you’re sure it’s too late to stand up, but the creature is scurrying away, shaking its orange head in confusion."
                $ custom6 = ""
        elif pc_class == "warrior":
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, dashing at it with your axe and cutting through its layers of feathers, but it’s fast enough to peck your arm in return. Your strike makes it shake its orange head, and it scurries away from you."
                $ custom6 = "leaving a trail of blood and "
            else:
                $ custom4 = "You wait to duck at the very last moment, then cut it while you’re still in the air, barely getting through the layers of feathers, but it’s fast enough to peck your arm in return. Your strike makes it shake its orange head, and it scurries away from you."
                $ custom6 = "leaving a trail of blood and "
        else:
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, dashing at it with your axe and landing a hit, even if not a strong one, but it’s fast enough to peck your arm in return. Still confused, it opens its beak in pain, shaking its orange head as it’s stepping away from you."
                $ custom6 = ""
            else:
                $ custom4 = "You wait to duck at the very last moment, then cut it while you’re still in the air, though you fail to get through the layers of feathers, and it’s fast enough to peck your arm in return. Confused, it leaves you behind and opens its beak in pain, shaking its orange head."
                $ custom6 = ""
        if cleanliness_clothes_torn:
            $ cleanliness = limit_cleanliness(cleanliness-1)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
            show minus1appearance at appearancechange onlayer myoverlay
        else:
            $ cleanliness_clothes_torn = 1
            $ cleanliness = limit_cleanliness(cleanliness-2)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            show minus2appearance at appearancechange onlayer myoverlay
        if armor >= 3:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ custom7 = "and your fine gambeson keeps you in one piece."
        else:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ custom7 = "and your fine gambeson keeps you in one piece."
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ custom7 = "and your gambeson wasn’t enough to stop the beast from reaching your flesh."
        $ at_unlock_spell = 0
        $ at = 0
        menu:
            'You grab everything you need and head toward the beast. It’s taller than {color=#f6d6bd}[horsename]{/color}, with wide breast and long, thick, partially feathered legs that could easily trample your chest. Its thighs are thick and powerful, the pointy beak could swallow your entire forearm. Once it notices your challenge, it runs at you, speeding up with every breath.
            \n\n[custom1][custom2][custom3]
            \n\n[custom5][custom4] Weakened, it turns around and flees in panic toward the western wilderness, [custom6]still finding strength to let out a furious screech. {color=#f6d6bd}[horsename]{/color} spares it a curious glance, but gets out of its way smoothly and trots toward you.
            \n\nYou are covered in sweat and dust, [custom7].
            '
            'I gather my stuff and try to remain calm.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather my stuff and try to remain calm.')
                $ quarters += 1
                jump foraginggroundafterinteraction01

    label foraginggroundtakingalookatequipment01outcome3:
        if item_crossbow and item_crossbowquarrels:
            $ custom1 = "You rest the crossbow’s stock on your shoulder, take a few deep breaths, and pull the trigger, but the powerful arrow misses the beast’s chest and shatters against a rock. You switch your gear."
            $ item_crossbowquarrels -= 1
            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
        else:
            $ custom1 = "Having nothing to shoot it with, you prepare your gear and jump in place, relaxing your shoulders."
        if item_blindingpowder:
            $ custom2 = "\n\nOnce the bird gets so close you know it won’t stop, you step forward and throw a fistful of dust. It closes its eyelids in time. You jump away - the beak cuts through the air behind you, but then the monster turns around swiftly, ready to confront you again. Thankfully, you’re already back on your feet."
        else:
            $ custom2 = ""
        if at == 'spell':
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
            $ custom3 = "\n\nOnce the bird gets so close you know it won’t stop, you step forward and raise your willow wand. Casting the pneuma feels like stabbing the air with a wooden dagger. The invisible wave strikes the creature while both of its feet are on the ground, and while it’s shocked after it gets stopped, it stays untouched. It observes you for a moment, but then steps closer."
        else:
            $ custom3 = ""
        if pc_hp >= 5:
            $ custom5 = "Your strong, relaxed shell moves with confidence and determination. "
        else:
            $ custom5 = ""
        if item_mountainroadspear or item_asterionspear:
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, making a confident thrust with your spear, but it’s fast enough to peck your arm in return. Your strike makes it shake its orange head, and it scurries away from you."
                $ custom6 = "leaving a trail of blood and "
            else:
                $ custom4 = "You almost crouch, using the ground to support your spear, and while the bird tries to change the direction of its charge, you manage to get through the layers of feathers. The bird is quick enough to strike your arm, but then passes you by, shaking its orange head from pain."
                $ custom6 = "leaving a trail of blood and "
        elif item_shield:
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, holding the shield between the two of you like a wall, yet the beast tries to land a hit after all. While the shield remains strong, the blow pushes you into the ground. The pain pierces through your back and you’re sure it’s too late to stand up, but the creature is scurrying away, shaking its orange head in confusion."
                $ custom6 = ""
            else:
                $ custom4 = "In the last moment, you move the shield between the two of you, using it to stop the charging monster, and the impact sends you into the air. The pain pierces through your back and you’re sure it’s too late to stand up, but the creature is scurrying away, shaking its orange head in confusion."
                $ custom6 = ""
        elif pc_class == "warrior":
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, dashing at it with your axe and cutting through its layers of feathers, but it’s fast enough to peck your arm in return. Your strike makes it shake its orange head, and it scurries away from you."
                $ custom6 = "leaving a trail of blood and "
            else:
                $ custom4 = "You wait to duck at the very last moment, then cut it while you’re still in the air, barely getting through the layers of feathers, but it’s fast enough to peck your arm in return. Your strike makes it shake its orange head, and it scurries away from you."
                $ custom6 = "leaving a trail of blood and "
        else:
            if foragingground_bird_charged_stopped:
                $ custom4 = "You give your opponent no time to think, dashing at it with your axe and landing a hit, even if not a strong one, but it’s fast enough to peck your arm in return. Still confused, it opens its beak in pain, shaking its orange head as it’s stepping away from you."
                $ custom6 = ""
            else:
                $ custom4 = "You wait to duck at the very last moment, then cut it while you’re still in the air, though you fail to get through the layers of feathers, and it’s fast enough to peck your arm in return. Confused, it leaves you behind and opens its beak in pain, shaking its orange head."
                $ custom6 = ""
        if not cleanliness_clothes_blood and not cleanliness_clothes_torn:
            $ cleanliness_clothes_torn = 1
            $ cleanliness_clothes_blood = 1
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
        elif not cleanliness_clothes_blood:
            $ cleanliness_clothes_blood = 1
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        elif not cleanliness_clothes_torn:
            $ cleanliness_clothes_torn = 1
            show minus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
        if armor >= 3:
            $ armor = limit_armor(armor-2)
            show minus2armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
            $ custom7 = "and while your fine gambeson keeps you in one piece, it now needs major repairs."
        elif armor >= 1:
            $ armor = limit_armor(armor-1)
            show minus1armor at armorchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ custom7 = "and while your gambeson keeps you in one piece, you still end up wounded, and with torn clothes and armor."
        else:
            $ pc_hp = limit_pc_hp(pc_hp-2)
            show minus2hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            $ custom7 = "and your gambeson wasn’t enough to stop the beast from reaching your flesh."
            if not cleanliness_clothes_blood:
                $ cleanliness_clothes_blood = 1
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
        $ at_unlock_spell = 0
        $ at = 0
        menu:
            'You grab everything you need and head toward the beast. It’s taller than {color=#f6d6bd}[horsename]{/color}, with wide breast and long, thick, partially feathered legs that could easily trample your chest. Its thighs are thick and powerful, the pointy beak could swallow your entire forearm. Once it notices your challenge, it runs at you, speeding up with every breath.
            \n\n[custom1][custom2][custom3]
            \n\n[custom5][custom4] It observes you with hesitation for a few heartbeats, then flees toward the western wilderness, letting out a furious screech. {color=#f6d6bd}[horsename]{/color} spares it a curious glance, but gets out of its way smoothly and trots toward you.
            \n\nYou are covered in sweat and dust, [custom7].
            '
            'I gather my stuff and prepare some bandages.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather my stuff and prepare some bandages.')
                $ quarters += 1
                jump foraginggroundafterinteraction01

label foraginggroundforagingALL:
    label foraginggroundforaging01bird:
        $ quarters += (2+foragingground_foraging_amount)
        $ foragingground_foraging_amount += 1
        $ renpy.notify("You picked two bunches of wild plants.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked two bunches of wild plants.{/i}')
        $ item_wildplants += 2
        $ achievement_wildplants += 2
        $ foragingground_foraging_day = day
        $ can_items = 0
        menu:
            'You let [horsename] keep itself busy while you walk around, looking for anything edible. It takes a fair bit of time - you don’t plan to carry around raw mushrooms and bugs, and the wild vegetables need to be washed before you put them in your bags.
            \n\nYou finally find a few handfuls of plants, fruits, and nuts. Next time, however, it’s not going to be so easy, especially since the runner, a bird both taller and wider than you, observes you carefully, at first from a distance, then circling around you.
            \n\nAfter about half an hour, you hear its piercing screech. As the creature runs at you, shaking a beak larger than your head, you throw everything into a sack and get in the saddle.
            '
            'I should avoid this place while this beast is hanging around. (disabled)':
                pass

    label foraginggroundforaging01:
        $ quarters += (2+foragingground_foraging_amount)
        $ foragingground_foraging_amount += 1
        if foragingground_foraging_amount == 1:
            $ renpy.notify("You picked two bunches of wild plants.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked two bunches of wild plants.{/i}')
            $ item_wildplants += 2
            $ achievement_wildplants += 2
            $ foragingground_foraging_day = day
            menu:
                'You let [horsename] keep itself busy while you walk around, looking for anything edible. It takes a fair bit of time - you don’t plan to carry around raw mushrooms and bugs, and the wild vegetables need to be washed before you put them in your bags.
                \n\nYou finally find a few handfuls of plants, fruits, and nuts. Next time, however, it’s not going to be so easy - the area has been already cleared by other foragers.
                '
                'I won’t find much more food today. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day == day and foragingground_foraging_amount < 4) or (foragingground_bird_gone and foragingground_foraging_day == day and foragingground_foraging_amount < 4):
                    pass
                'I follow the directions to the spot where the dead man was found.' if (foragingground_foraging_vein_rumor and foragingground_bird_taken and not foragingground_foraging_vein and not foragingground_foraging_bag) or (foragingground_foraging_vein_rumor and foragingground_bird_gone and not foragingground_foraging_vein and not foragingground_foraging_bag):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the directions to the spot where the dead man was found.')
                    jump foraginggroundexploringravine01ALT
        elif foragingground_foraging_amount == 2:
            $ renpy.notify("You picked two bunches of wild plants.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked two bunches of wild plants.{/i}')
            $ item_wildplants += 2
            $ achievement_wildplants += 2
            $ foragingground_foraging_day = day
            menu:
                'The time goes by as you roam about, until you stumble upon a bush full of juicy berries hidden behind a boulder. Together with a couple of wild carrots and an onion, you’ll have more than enough to fill your belly.
                \n\nYou grow familiar with the valley, but you don’t think it hides much more food.
                '
                'I won’t find much more food today. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day == day and foragingground_foraging_amount < 4) or (foragingground_bird_gone and foragingground_foraging_day == day and foragingground_foraging_amount < 4):
                    pass
                'I follow the directions to the spot where the dead man was found.' if (foragingground_foraging_vein_rumor and foragingground_bird_taken and not foragingground_foraging_vein and not foragingground_foraging_bag) or (foragingground_foraging_vein_rumor and foragingground_bird_gone and not foragingground_foraging_vein and not foragingground_foraging_bag):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the directions to the spot where the dead man was found.')
                    jump foraginggroundexploringravine01ALT
        elif foragingground_foraging_amount == 3:
            $ renpy.notify("You picked a new food ration.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked a new food ration.{/i}')
            $ item_rations += 1
            $ achievement_wildplants += 1
            $ foragingground_foraging_day = day
            menu:
                'This time, the berry bush won’t help. You keep leading {color=#f6d6bd}[horsename]{/color} further away from the road, until you get to a spot covered with walnuts dropped by a tree growing on top of the crag. You’ll have a chance to break their shells before you go to sleep.
                '
                'I won’t find much more food today. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day == day and foragingground_foraging_amount < 4) or (foragingground_bird_gone and foragingground_foraging_day == day and foragingground_foraging_amount < 4):
                    pass
                'I follow the directions to the spot where the dead man was found.' if (foragingground_foraging_vein_rumor and foragingground_bird_taken and not foragingground_foraging_vein and not foragingground_foraging_bag) or (foragingground_foraging_vein_rumor and foragingground_bird_gone and not foragingground_foraging_vein and not foragingground_foraging_bag):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow the directions to the spot where the dead man was found.')
                    jump foraginggroundexploringravine01ALT
        else:
            if not foragingground_foraging_bag:
                $ foragingground_foraging_bag = 1
                show areapicture ravine01 at basicfade
                menu:
                    'You put even more effort into exploring the area, but you only find things that you can’t use on the road - honey, mushrooms, insects, acorns, eggs, or little critters, snakes, and lizards.
                    \n\nYou do, however, find an unusual spot in the far east, near a shallow pond. A small ravine of sorts, though instead of water, it hides torn clothes, broken tools, and remains of a camp. There are no bones around - whoever had found their end in this place surely turned into an undead years or decades ago.
                    \n\nThere’s a broken rope hanging from a tree stump. The other part of the plant is already at the bottom of the ravine.
                    '
                    'Maybe I’ll find something of value in the bag or the tent. I better get down there.': # ropehook
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe I’ll find something of value in the bag or the tent. I better get down there.')
                        jump foraginggroundexploringravine01
                    'I’ve already wasted enough time. I turn around and get back on the road. (disabled)':
                        pass
            else:
                $ quarters += 2
                menu:
                    'You put even more effort into exploring the area, but you only find things that you can’t use on the road - honey, mushrooms, insects, acorns, eggs, or little critters, snakes, and lizards.
                    '
                    'I could take a look at the remains in the small ravine. I ride there and prepare my equipment.' if foragingground_foraging_bag and not foragingground_foraging_vein:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could take a look at the remains in the small ravine. I ride there and prepare my equipment.')
                        jump foraginggroundexploringravine01
                    'I’ve been foraging here a lot. I won’t find much more food. (disabled)' if (foragingground_bird_taken and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount >= 4) or (foragingground_bird_gone and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount >= 4):
                        pass

    label foraginggroundexploringravine01ALT:
        $ foragingground_foraging_bag = 1
        show areapicture ravine01 at basicfade
        $ quarters += 1
        menu:
            'You head behind the shallow pond in the far east and find the small ravine of sorts, though instead of water, it hides torn clothes, broken tools, and remains of a camp. There are no bones around - whoever had found their end in this place surely turned into an undead years or decades ago.
            \n\nThere’s a broken rope hanging from a tree stump. The other part of the plant is already at the bottom of the ravine.
            '
            'Time to take a closer look.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to take a closer look.')
                jump foraginggroundexploringravine01

    label foraginggroundexploringravine01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ quarters += 1
        show areapicture ravine01 at basicfade
        if pc_likeshorsename:
            $ custom3 = "You pat its side. “It won’t take long,” you say, knowing both that it doesn’t understand you, and that you can’t be sure if the words are true. It lowers its head and starts to paw the ground."
        else:
            $ custom3 = "{i}I should save its strength{/i}, you think to yourself."
        menu:
            'You grab {color=#f6d6bd}[horsename]’s{/color} halter. Your mount observes the area nervously, not willing to graze on the sparse, dry grass. [custom3]
            \n\nNot willing to repeat the mistake of the previous traveler, you tie your rope to a stone instead of any of the plants. You take only what’s necessary and descend, leaning with your boots against the rock face. The sounds of wind and birds are muffled and echoed. You end up in a corridor of rocks.
            '
            'I approach the traveler’s possessions.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the traveler’s possessions.')
                menu:
                    'You find no blood, flesh, or bones, but the clues tell you all you need. Someone was betrayed by their own rope, now lying on the ground with a torn loop. They landed on their bag, in which you find a bunch of broken supply jars and scraps of linen, then tried to crawl away. You find nothing of value, not even dragon bones. Maybe that’s why the dead used to own such unreliable equipment.
                    \n\nYou’re ready to climb back, but once you turn around, you realize that you’ve overlooked something sticking out from the wall. A pickaxe, surrounded by dozens of cracks. Some of the smaller rocks have already crumbled up.
                    '
                    'I grab the tool.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the tool.')
                        $ can_leave = 1
                        $ can_rest = 1
                        $ can_items = 1
                        $ renpy.notify("Journal updated: Explore the Peninsula")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                        $ quest_explorepeninsula_description16 = "I found a spot at the eastern road that may be a part of a larger copper vein. It should be investigated by an experienced team, and {color=#f6d6bd}Hovlavan{/color} will surely appreciate it if they can be the first ones to get to it."
                        $ foragingground_foraging_vein = 1
                        $ quarters += 1
                        menu:
                            'It gives way easily, more thanks to the rust than to your muscles. You throw it away, using your hands to pull away the shards of the wall, and gasp once you recognize the patina on their surface. You kneel down and take a better look at other rocks - at least a half of them bear a touch of the green copper, like a statue in an old temple.
                            \n\nYou come to your senses, pushing away the images of fortune and future idleness. A large group would have to set up a hamlet here to even inspect the vein, with workers, guards, wood, supplies, tools... All under the noses of the locals. Squabbles over ore can turn violent pretty fast.
                            '
                            'Now I have to decide if it’s a secret I take to {color=#f6d6bd}Hovlavan{/color}, or something I share with the locals. (disabled)':
                                pass
                            'I could try to forage, though it will take even more time.' if (foragingground_bird_taken and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount < 4 and quarters < (world_daylength-4)) or (foragingground_bird_gone and foragingground_foraging_day != day and foragingground_foraging_amount and foragingground_foraging_amount < 4 and quarters < (world_daylength-4)):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could try to forage, though it will take even more time.')
                                jump foraginggroundforaging01

label foraginggroundforagersALL:
    label foraginggroundfirsttime01foragers:
        $ renpy.force_autosave(take_screenshot=True, block=True)
        $ quarters += 1
        menu:
            'The valley is flanked by the hills. To the west the grasses and bushes blend into the horizon and turn into another part of the forest. The southern hills are gray and tall, with fortress-like rock faces and a crown of conifers. The northern ones have countless sand-colored rocks, lumped together like piles of rubble and clay, bearing hardly any soil or weeds.
            \n\nThe plants here are struggling. The grass is short and yellowish, sometimes dried out. The bushes have silver leaves, like many plants from sunny areas. The mushrooms can’t hide in the shadows, but as you approach one, you see it’s growing from the remains of a dead bird, while others are covering old branches and other plants. They won’t last much longer.
            \n\n{color=#f6d6bd}Ilan{/color} points east, to the large bird at the edge of the horizon, which freezes in the middle of a step and turns its orange head in your direction. “See? Time to get ready.”
            '
            '“What’s the plan?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s the plan?”')
                jump foraginggroundhunting02

    label foraginggroundregular01foragers:
        $ renpy.force_autosave(take_screenshot=True, block=True)
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ quarters += 1
        menu:
            'The valley seems especially peaceful today. A couple of lizards are resting on the rocks, basking with no worries. {color=#f6d6bd}Ilan{/color} points east, to the large bird at the edge of the horizon, which freezes in the middle of a step and turns its orange head in your direction. “See? Time to get ready.”
            '
            '“What’s the plan?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s the plan?”')
                jump foraginggroundhunting02

    label foraginggroundhunting02:
        $ foragingground_bird_timer = foragingground_bird_timer_max
        $ renpy.save("combatsave", extra_info='Combat Auto Save')
        menu:
            '“Well, avoid the beak, and the legs, and the trample.” He pauses, inspecting the loop at the end of his rope. “And don’t hurt it, if you don’t have to. We don’t want it to be a bother.”
            \n\n{color=#f6d6bd}Tzvi{/color} jauntily drops his belongings in the middle of the road and jumps in place, rhythmically breathing. After he takes off his black cloak, he reveals a set of fancy clothes made of black leather. Clothes of a sneaky adventurer. “It charges like a moron. Be nimble, that’s all. One or two ropes on the neck and we’re halfway home. But don’t let it pass you by, aye?”
            '
            '“I’ll stay alive, and you’ll do the rest.”' if not item_shield and not item_blindingpowder:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll stay alive, and you’ll do the rest.”')
                menu:
                    '“Pretty much.” {color=#f6d6bd}Ilan{/color} bursts into laughter. “Just be careful. We don’t have magic on our hands.”
                    \n\n“And we can’t buy another roadwarden,” adds {color=#f6d6bd}his companion{/color}. “So don’t make this a bad trade for us.”
                    '
                    'I wait for them to get to the sides of the valley, then approach the bird.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for them to get to the sides of the valley, then approach the bird.')
                        jump foraginggroundhuntingregular01
            'I shake my shield. “I can handle a charge, don’t you worry. I’ll buy you some time.”' if item_shield:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake my shield. “I can handle a charge, don’t you worry.”')
                menu:
                    '“Aye, such’ wall can’t hurt.” {color=#f6d6bd}Ilan{/color} bursts into laughter. “Just be careful. We don’t have magic on our hands.”
                    \n\n“And we can’t buy another roadwarden,” adds {color=#f6d6bd}his companion{/color}. “So don’t make this a bad trade for us.”
                    '
                    'I wait for them to get to the sides of the valley, then approach the bird.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for them to get to the sides of the valley, then approach the bird.')
                        jump foraginggroundhuntingregular01
            'I put on a glove and place my hand on the pouch of blinding dust. “I have a little surprise for it. You’ll have your time.”' if item_blindingpowder:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put on a glove and place my hand on the pouch of blinding dust. “I have a little surprise for it. You’ll have your time.”')
                menu:
                    '“Magic, aye? Just don’t hurt it too much.” {color=#f6d6bd}Ilan{/color} remains unconvinced. “Don’t melt its heart, but also be careful. We are no healers.”
                    \n\n“And we can’t buy another roadwarden,” adds {color=#f6d6bd}his companion{/color}. “So don’t make this a bad trade for us.”
                    '
                    'I wait for them to get to the sides of the valley, then approach the bird.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for them to get to the sides of the valley, then approach the bird.')
                        jump foraginggroundhuntingregular01
            '“Should I also take a rope? I can throw it at the bird and pull once it gets behind me.”': # ropehook
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Should I also take a rope? I can throw it at the bird and pull once it gets behind me.”')
                menu:
                    '“I don’t know, friend,” says {color=#f6d6bd}Ilan{/color}. “Roping isn’t easy. Don’t be too reckless. We don’t have magic on our hands.”
                    \n\n“And we can’t buy another roadwarden,” adds {color=#f6d6bd}his companion{/color}. “So don’t make this a bad trade for us.”
                    '
                    'I wait for them to get to the sides of the valley, then approach the bird.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for them to get to the sides of the valley, then approach the bird.')
                        jump foraginggroundhuntingregular01
            'I pat my crossbow and nod toward the shorter guy. “How about you play the bait. I’ll keep aiming and if things go wrong, I’ll put the bird down before it hurts anyone.”' if item_crossbow and item_crossbowquarrels:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pat my crossbow and nod toward the shorter guy. “How about you play the bait. I’ll keep aiming, and will put it down the bird before it hurts anyone.”')
                menu:
                    '{color=#f6d6bd}Tzvi{/color} scowls at you and spits on the ground. {color=#f6d6bd}Ilan{/color} gives you a serious look. “I don’t know, friend. We don’t pay you to stay away from danger. We don’t have magic on our hands, so we won’t be reckless. Just trust that we’ll do well.”
                    \n\n“We can’t buy another roadwarden,” adds {color=#f6d6bd}his companion{/color}, “but there are even fewer of me out there, you know? I won’t bet my life against your aim. Load it just in case, but don’t use it if you don’t have to.”
                    '
                    'I prepare my weapon and wait for them to get to the sides of the valley, then approach the bird.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I prepare my weapon and wait for them to get to the sides of the valley, then approach the bird.')
                        jump foraginggroundhuntingregular01
            'I show them a roast chicken. “This should catch its attention for a while.”' if item_chicken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show them a roast chicken. “This should catch its attention for a while.”')
                menu:
                    '{color=#f6d6bd}Tzvi{/color} smirks. “And I was wondering hwy you took it. Took you for a weirdo.”
                    \n\n{color=#f6d6bd}Ilan{/color} nods approvingly. “Aye, some bait may do the job. We don’t have magic on our hands, so it’s better for you to stay safe.”
                    \n\n“And we can’t buy another roadwarden,” adds {color=#f6d6bd}his companion{/color}, now from far away. “So don’t make this a bad trade for us.”
                    '
                    'I wait for them to get to the sides of the valley, then approach the bird.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for them to get to the sides of the valley, then approach the bird.')
                        jump foraginggroundhuntingregular01
            'I grab the stoat’s carcass I own. “I can bait it with this. That’s what it’s looking for, right?”' if item_stoat:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the stoat’s carcass I own. “I can bait it with this. That’s what it’s looking for, right?”')
                menu:
                    '{color=#f6d6bd}Tzvi{/color} smirks. “And I was wondering hwy you took it. Took you for a weirdo.”
                    \n\n{color=#f6d6bd}Ilan{/color} nods approvingly. “Aye, it may do the job. We don’t have magic on our hands, so it’s better for you to stay safe.”
                    \n\n“And we can’t buy another roadwarden,” adds {color=#f6d6bd}his companion{/color}, now from far away. “So don’t make this a bad trade for us.”
                    '
                    'I wait for them to get to the sides of the valley, then approach the bird.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for them to get to the sides of the valley, then approach the bird.')
                        jump foraginggroundhuntingregular01

    label foraginggroundhuntingregular01:
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 5.0>audio/weloveindies_duringthenight_batteloop.ogg":
            play music "<loop 5.0>audio/weloveindies_duringthenight_batteloop.ogg" fadeout 1.0 fadein 1.0
        show areapicture foragingground02 at basicfade
        menu:
            'It’s taller than {color=#f6d6bd}[horsename]{/color}, with wide breast and long, thick, partially feathered legs that could easily trample your chest. Its thighs are thick and powerful, the pointy beak could swallow your entire forearm.
            \n\nYour steps are getting slower.
            '
            'I look around nervously. Are the foragers in position?':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look around nervously. Are the foragers in position?')
                $ custom1 = "At a quick glance, they are rushing ahead to outpace your walk. They stay silent, not drawing too much attention to themselves, though they can’t vanish into thin air, and the creature observes them carefully. They are an experienced team, understanding each other without words. Their confidence cools your soul."
                jump foraginggroundhuntingregular02
            'I need to calm myself down. I focus on my breath.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to calm myself down. I focus on my breath.')
                $ custom1 = "You put your right hand on your chest, noticing its rising and falling as the air moves through your nose. You can’t take your eyes away from the creature’s overwhelming posture, but as your breath remains deep and slow, you don’t feel afraid, just ready to defend yourself."
                jump foraginggroundhuntingregular02
            'I grab the hourglass on my chest.' if item_wingedhourglass_worn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab the hourglass on my chest.')
                $ pc_faithpoints += 1
                $ custom1 = "The steel is soothingly cold. It won’t scare the monster away, but for just a few moments you don’t feel alone."
                jump foraginggroundhuntingregular02
            'I try to speak confidently. “How’s it going? Can you just, maybe, wait patiently in place, so my companions can nicely tie you up? Once you get to the pen with us, you’ll have all the rats and pigeons you can eat.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to speak confidently. “How’s it going? Can you just, maybe, wait patiently in place, so my can companions nicely tie you up? Once you get to the pen with us, you’ll have all the rats and pigeons you can eat.”')
                $ custom1 = "The bird moves forward even before you finish your sentence, clearly unimpressed by your promises, but the sound of your voice and the illusion of control helps you calm down. Your hands hold your equipment firmly, and your legs are already bent, ready to jump. You can handle it."
                jump foraginggroundhuntingregular02
            'I beat my chest with a fist and let out a shout. I won’t die to some stupid bird.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I beat my chest with a fist and let out a shout. I won’t die to some stupid bird.')
                $ custom1 = "The surprised creature steps back, its eyes are wide-open. Once you’re done, moving even closer, it also regains its confidence, flapping its wings, but you’re ready to face it. Your steps are confident, yet nimble, ready to jump away."
                jump foraginggroundhuntingregular02

    label foraginggroundhuntingregular02:
        menu:
            '[custom1]
            \n\nSoon, the bird is surrounded by your group, and the pond behind it blocks its path of escape. Once it realizes that, it speeds up, charging in your direction.
            '
            'I take a good look at the monster.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a good look at the monster.')
                menu:
                    'It’s tall, wide, with a massive head. Its feathers are torn by the wind - they are vividly brown, white, and creamy, longer than your handspan, coating the creature like a cape.
                    \n\nIts steps are heavy and deliberate. The neck, as long as a limb, keeps moving around, sometimes staring at you with but a single, black pupil surrounded by deep orange.
                    \n\nThe light-gray beak resembles the leaves of the local plants. The tip is curved, pointy, and in no way smooth - it carries dozens of grooves, maybe a sign of an old age, or maybe a trace of hundreds of hunts.
                    '
                    'I try to find its weak spot. It’s just a huge duck.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to find its weak spot. It’s just a huge duck.')
                        jump foraginggroundhuntingregular03
                    'A respectable opponent. I may be forced to kill it after all.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- A respectable opponent. I may be forced to kill it after all.')
                        jump foraginggroundhuntingregular03
                    'Am I even ready to face it?':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Am I even ready to face it?')
                        jump foraginggroundhuntingregular03

    label foraginggroundhuntingregular03:
        $ can_potions = 1
        menu:
            'It waits no more. It raises its head and makes a long, piercing screech which fills up the entire valley. The feathers on its neck are shaking, but also waving, moved by the muscles. It then flaps its wings and lunges forward, still shouting, charging at you with full force.
            '
            'I distract it with a stoat. I don’t need it anyway.' if item_stoat:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I distract it with a stoat. I don’t need it anyway.')
                $ foragingground_bird_timer -= 2
                $ foragingground_bird_used_stoat = 1
                $ item_stoat = 0
                $ renpy.notify("You lost the stoat.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the stoat.{/i}')
                $ custom2 = ""
                $ custom3 = "The dead critter hits the ground with a muffled smack. The bird, unsure what’s happening, ceases its advance and spreads its wings. After a few breaths and a brief screech, it lowers its long neck to pick up the offering, then springs up and steps back. It gives you another look, then raises its head and starts to swallow. Your allies have plenty of time to move forward."
                if foragingground_bird_timer <= 0:
                    jump foraginggroundhuntingregular06victory
                if foragingground_bird_timer <= foragingground_bird_threshold_timer and not foragingground_bird_threshold:
                    $ foragingground_bird_threshold = 1
                    jump foraginggroundhuntingregular05fear
                jump foraginggroundhuntingregular04
            'Time to lure it with a chicken.' if item_chicken:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to lure it with a chicken.')
                $ foragingground_bird_timer -= 2
                $ foragingground_bird_used_chicken = 1
                $ item_chicken -= 1
                $ renpy.notify("You lost a chicken.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a chicken.{/i}')
                $ custom2 = ""
                $ custom3 = "The dead critter hits the ground with a muffled smack. The bird, unsure what’s happening, ceases its advance and spreads its wings. After a few breaths and a brief screech, it lowers its long neck to pick up the offering, then springs up and steps back. It gives you another look, then raises its head and starts to swallow. Your allies have plenty of time to move forward."
                if foragingground_bird_timer <= 0:
                    jump foraginggroundhuntingregular06victory
                if foragingground_bird_timer <= foragingground_bird_threshold_timer and not foragingground_bird_threshold:
                    $ foragingground_bird_threshold = 1
                    jump foraginggroundhuntingregular05fear
                jump foraginggroundhuntingregular04
            'I let it charge at me, then suddenly cover myself with the shield.' if item_shield and not foragingground_bird_used_shield:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let it charge at me, then suddenly cover myself with the shield.')
                $ foragingground_bird_timer -= 2
                $ foragingground_bird_used_shield += 1
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. "
                else:
                    $ custom2 = ""
                $ custom3 = "You wait until the last moment before raising the heavy wooden planks. You hold them with both hands, as if you’re trying to stop a rolling boulder. It’s too late for the creature to stop, yet it attempts to - it crashes into you with its side, knocking you away, but you land on your feet.\n\nThe beast crawls away in panic, then springs up and runs away, preparing itself for another strike. You think of another maneuver."
                if foragingground_bird_timer <= 0:
                    jump foraginggroundhuntingregular06victory
                if foragingground_bird_timer <= foragingground_bird_threshold_timer and not foragingground_bird_threshold:
                    $ foragingground_bird_threshold = 1
                    jump foraginggroundhuntingregular05fear
                jump foraginggroundhuntingregular04
            'I use a spear to keep the distance between me and the bird.' if (item_asterionspear and not foragingground_bird_used_spear) or (item_mountainroadspear and not foragingground_bird_used_spear):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use a spear to keep the distance between me and the bird.')
                $ foragingground_bird_timer -= 1
                $ foragingground_bird_used_spear = 1
                $ custom2 = ""
                $ custom3 = "The long weapon makes the beast stop and reconsider its charge. You wonder if it can ever recognize the purpose of your pointy stick - could it have faced other humans, or maybe goblins, in the past?\n\nAfter a few precious moments, the bird abandons its doubts, once again making a brief screech and getting ready to run at you."
                if foragingground_bird_timer <= 0:
                    jump foraginggroundhuntingregular06victory
                if foragingground_bird_timer <= foragingground_bird_threshold_timer and not foragingground_bird_threshold:
                    $ foragingground_bird_threshold = 1
                    jump foraginggroundhuntingregular05fear
                jump foraginggroundhuntingregular04
            'Once it gets close, I throw a fistful of blinding powder.' if item_blindingpowder and not foragingground_bird_used_blindingpowder:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Once it gets close, I throw a fistful of blinding powder.')
                $ foragingground_bird_used_blindingpowder = 1
                $ foragingground_bird_timer -= 2
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. "
                else:
                    $ custom2 = ""
                $ custom3 = "At the very last moment you throw it at the creature’s beak and jump away, avoiding the hit. The bird stumbles over its own feet and smashes into the ground, painfully scratching its side. You move around it, making sure to block its path again, but it springs up quickly. It {i}should{/i} be blind, yet moves with ease, and keeps observing you through the narrowed eyes."
                if foragingground_bird_timer <= 0:
                    jump foraginggroundhuntingregular06victory
                if foragingground_bird_timer <= foragingground_bird_threshold_timer and not foragingground_bird_threshold:
                    $ foragingground_bird_threshold = 1
                    jump foraginggroundhuntingregular05fear
                jump foraginggroundhuntingregular04
            'I don’t have a potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                pass
            'I better roll up the rope again, even though the creature will use this time to attack me.' if foragingground_bird_used_rope == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better roll up the rope again, even though the creature will use this time to attack me.')
                $ foragingground_bird_timer -= 1
                $ foragingground_bird_used_rope = 0
                $ custom2 = ""
                if pc_hp:
                    if armor >= 3:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom3 = "You move away, doing your best to get ready for another roping, but the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. Finally, it lands a hit. Your gambeson does its job and protects your flesh. You leap away, ready for another try with the rope, but the bird is also preparing itself."
                    elif armor >= 1:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom3 = "You move away, doing your best to get ready for another roping, but the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. Finally, it lands a hit. Your gambeson does its job and protects your flesh. Hurt by the sheer strength of the hit, you manage to leap away, ready for another try with the rope, but the bird is also preparing itself."
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        $ foragingground_bird_dmgtopc += 1
                        $ custom3 = "You move away, doing your best to get ready for another roping, but the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. Finally, it lands a hit, piercing through your worn gambeson. Underneath the pain, you feel the stickiness of your blood. You manage to leap away, ready for another try with the rope, but the bird is also preparing itself."
                        if not cleanliness_clothes_blood:
                            $ cleanliness_clothes_blood = 1
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                else:
                    $ custom6 = "You move away, doing your best to get ready for another roping, but the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. The cold beak sinks into your skull."
                    jump foraginggroundgameover
                if foragingground_bird_timer <= 0:
                    jump foraginggroundhuntingregular06victory
                if foragingground_bird_timer <= foragingground_bird_threshold_timer and not foragingground_bird_threshold:
                    $ foragingground_bird_threshold = 1
                    jump foraginggroundhuntingregular05fear
                jump foraginggroundhuntingregular04
            '{image=d6} I should try to rope it.' if not foragingground_bird_used_rope:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I should try to rope it.')
                $ custom2 = ""
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if armor == 4:
                    $ d100roll -= 5
                $ d100roll += (foragingground_bird_timer*10)
                if d100roll < 80:
                    $ foragingground_bird_used_rope = 1
                    $ custom3 = "The creature pays attention to your movements, and once the rope flies toward it, it steps away, then moves into a charge quickly. Preparing the rope for the next attempt will take some time, but will also put you in a vulnerable position."
                else:
                    $ foragingground_bird_used_rope = 2
                    $ custom3 = "You prepare yourself to throw, and the creature gets distracted by the approach of your companions. Your loop lands on its head, so you pull, squeezing the monster’s thick neck. It twists its shell in anger, then runs at you, not giving you a chance to choke it.\n\nWhile you may still be in danger, you now have an additional way to stop it from running away."
                jump foraginggroundhuntingregular04
            '{image=d6} I keep my distance and dodge, when necessary.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I keep my distance and dodge, when necessary.')
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. "
                else:
                    $ custom2 = ""
                $ foragingground_bird_timer -= 1
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if armor == 4:
                    $ d100roll -= 5
                $ d100roll -= (pc_hp*10)
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                $ d100roll += (foragingground_bird_timesdodged*10)
                $ foragingground_bird_timesdodged += 1
                if d100roll > 80: # fail and escaped
                    if not foragingground_bird_charged:
                        $ foragingground_bird_charged = 1
                        $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nYou suddenly jump to the side, afraid of an incoming hit, and lose your balance. The bird passes you by and gives you a surprised look, but as it sees the other two men are getting closer, it makes a single, long screech and flees west, as quickly as it can."
                    else:
                        $ custom2 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nYou suddenly jump to the side, afraid of an incoming hit, and lose your balance. The bird passes you by and gives you a surprised look, but as it sees the other two men are getting closer, it makes a single, long screech and flees west, as quickly as it can."
                    jump foraginggroundhuntingregular05fail
                elif d100roll > 30: # fail
                    if pc_hp:
                        if armor >= 3:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom3 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nFinally, the beast lands a hit. Your gambeson does its job and protects your flesh. Though in pain, you manage to leap away, then wait for another charge."
                        elif armor >= 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom3 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nFinally, the beast lands a hit. Your gambeson does its job and protects your flesh. Though in pain, you manage to leap away, then wait for another charge."
                        else:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            $ foragingground_bird_dmgtopc += 1
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            $ custom3 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nFinally, the beast lands a hit. Your gambeson, already damaged, isn’t enough, and you feel the stickiness of your blood. Though in pain, you manage to leap away, then wait for another charge."
                        jump foraginggroundhuntingregular04
                    else:
                        if not foragingground_bird_charged:
                            $ foragingground_bird_charged = 1
                            $ custom6 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nNevertheless, the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. The cold beak sinks into your skull."
                        else:
                            $ custom6 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nNevertheless, the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. The cold beak sinks into your skull."
                        jump foraginggroundgameover
                else: # success
                    $ custom3 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nYet the creature doesn’t find a way to land a hit, and observes you with respect. It turns around, but stops in place when it sees your companions. It looks at you again, preparing for the next charge."
                jump foraginggroundhuntingregular04
            '{image=d6} I hold my ground - make a quick dodge, then grapple the bird.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I hold my ground - make a quick dodge, then try to hold the bird where it is.')
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. "
                else:
                    $ custom2 = ""
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if armor == 4:
                    $ d100roll -= 5
                $ d100roll -= (pc_hp*10)
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                $ d100roll += (10*foragingground_bird_timesdodged)
                $ foragingground_bird_timesdodged += 1
                if d100roll > 70: #epic fail
                    $ foragingground_bird_timer -= 1
                    if pc_hp:
                        if armor >= 3:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder, then your back. Your gambeson does its job and protects your flesh. Though in pain, you press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                        elif armor == 2:
                            $ armor = limit_armor(armor-2)
                            show minus2armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                            $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder, then your back. Your gambeson does its job and protects your flesh. Though in pain, you press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        elif armor == 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder, then your back. Your gambeson is of little use, and you scream in pain as your blood releases.\n\nyou press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        else:
                            $ pc_hp = limit_pc_hp(pc_hp-2)
                            $ foragingground_bird_dmgtopc += 2
                            $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder, then your back. Your gambeson is of little use, and you scream in pain as your blood releases.\n\nyou press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                            show minus2hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        jump foraginggroundhuntingregular04
                    else:
                        if not foragingground_bird_charged:
                            $ foragingground_bird_charged = 1
                            $ custom6 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. You wait to duck at the very last moment, but you’re already too weak and tired to stay in control. Your neck releases blood."
                        else:
                            $ custom6 = "You wait to duck at the very last moment, but you’re already too weak and tired to stay in control. The cold beak sinks into your skull."
                        jump foraginggroundgameover
                elif d100roll > 20: #slight fail
                    $ foragingground_bird_timer -= 2
                    if armor >= 3:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder. Your gambeson does its job and protects your flesh. Though in pain, you press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                        jump foraginggroundhuntingregular04
                    elif armor >= 1:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder. Your gambeson does its job and protects your flesh. Though in pain, you press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                        jump foraginggroundhuntingregular04
                    else:
                        if pc_hp:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            $ foragingground_bird_dmgtopc += 1
                            $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder. Your gambeson, already damaged, isn’t enough, and you feel the stickiness of your blood.\n\nyou press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            jump foraginggroundhuntingregular04
                        else:
                            if not foragingground_bird_charged:
                                $ foragingground_bird_charged = 1
                                $ custom6 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. You wait to duck at the very last moment, but you’re already too weak and tired to stay in control. Your neck releases blood."
                            else:
                                $ custom6 = "You wait to duck at the very last moment, but you’re already too weak and tired to stay in control. The cold beak sinks into your skull."
                            jump foraginggroundgameover
                else: # success
                    $ foragingground_bird_timer -= 3
                    $ custom3 = "You wait to duck at the very last moment. In the blink of an eye, you show up at the beast’s side, pressing your shell to its large chest, too large for you to wrap your arms around it. You try to avoid the massive legs, but the monster turns out to be as confused as you are, making an angry screech and trying to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                jump foraginggroundhuntingregular04
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass
            'I can’t win. Once it charges at me, I roll away, giving it a chance to run away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t win. Once it charges at me, I roll away, giving it a chance to run away.')
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. Then, as you suddenly jump to the side, the bird passes you by and gives you a surprised look, but as it sees the other two men are getting closer, it makes a single, long screech and flees west, as quickly as it can."
                else:
                    $ custom2 = "The bird passes you by and gives you a surprised look, but as it sees the other two men are getting closer, it makes a single, long screech and flees west, as quickly as it can."
                jump foraginggroundhuntingregular05fail

    label foraginggroundhuntingregular04: #afterinteraction
        $ can_potions = 1
        if foragingground_bird_timer <= foragingground_bird_threshold_timer and not foragingground_bird_threshold:
            $ foragingground_bird_threshold = 1
            jump foraginggroundhuntingregular05fear
        menu:
            '[custom2][custom3]
            '
            'It already sees me as an enemy. It won’t take the bait anymore. (disabled)' if (item_stoat and not foragingground_bird_used_stoat) or (item_chicken and not foragingground_bird_used_chicken):
                pass
            'I let it charge at me, then suddenly cover myself with the shield.' if item_shield and not foragingground_bird_used_shield:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let it charge at me, then suddenly cover myself with the shield.')
                $ foragingground_bird_timer -= 2
                $ foragingground_bird_used_shield += 1
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. "
                else:
                    $ custom2 = ""
                $ custom3 = "You wait until the last moment before raising the heavy wooden planks. You hold them with both hands, as if you’re trying to stop a rolling boulder. It’s too late for the creature to stop, yet it attempts to - it crashes into you with its side, knocking you away, but you land on your feet.\n\nThe beast crawls away in panic, then springs up and runs away, preparing itself for another strike. You think of another maneuver.."
                if foragingground_bird_timer <= 0:
                    jump foraginggroundhuntingregular06victory
                if foragingground_bird_timer <= foragingground_bird_threshold_timer and not foragingground_bird_threshold:
                    $ foragingground_bird_threshold = 1
                    jump foraginggroundhuntingregular05fear
                jump foraginggroundhuntingregular04
            'I use a spear to keep the distance between me and the bird.' if (item_asterionspear and not foragingground_bird_used_spear) or (item_mountainroadspear and not foragingground_bird_used_spear):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use a spear to keep the distance between me and the bird.')
                $ foragingground_bird_timer -= 1
                $ foragingground_bird_used_spear = 1
                $ custom2 = ""
                $ custom3 = "The long weapon makes the beast stop and reconsider its charge. You wonder if it can ever recognize the purpose of your pointy stick - could it have faced other humans, or maybe goblins, in the past?\n\nAfter a few precious moments, the bird abandons its doubts, once again making a brief screech and getting ready to run at you."
                if foragingground_bird_timer <= 0:
                    jump foraginggroundhuntingregular06victory
                if foragingground_bird_timer <= foragingground_bird_threshold_timer and not foragingground_bird_threshold:
                    $ foragingground_bird_threshold = 1
                    jump foraginggroundhuntingregular05fear
                jump foraginggroundhuntingregular04
            'Once it gets close, I throw a fistful of blinding powder.' if item_blindingpowder and not foragingground_bird_used_blindingpowder:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Once it gets close, I throw a fistful of blinding powder.')
                $ foragingground_bird_used_blindingpowder = 1
                $ foragingground_bird_timer -= 2
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. "
                else:
                    $ custom2 = ""
                $ custom3 = "At the very last moment you throw it at the creature’s beak and jump away, avoiding the hit. The bird stumbles over its own feet and smashes into the ground, painfully scratching its side. You move around it, making sure to block its path again, but it springs up. It {i}should{/i} be blind, yet moves with ease, and keeps observing you through the narrowed eyes."
                if foragingground_bird_timer <= 0:
                    jump foraginggroundhuntingregular06victory
                if foragingground_bird_timer <= foragingground_bird_threshold_timer and not foragingground_bird_threshold:
                    $ foragingground_bird_threshold = 1
                    jump foraginggroundhuntingregular05fear
                jump foraginggroundhuntingregular04
            'I don’t have a potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                pass
            'I better roll up the rope again, even though the creature will use this time to attack me.' if foragingground_bird_used_rope == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better roll up the rope again, even though the creature will use this time to attack me.')
                $ foragingground_bird_timer -= 1
                $ foragingground_bird_used_rope = 0
                $ custom2 = ""
                if pc_hp:
                    if armor >= 3:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom3 = "You move away, doing your best to get ready for another roping, but the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. Finally, it lands a hit. Your gambeson does its job and protects your flesh. You leap away, ready for another try with the rope, but the bird is also preparing itself."
                    elif armor >= 1:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom3 = "You move away, doing your best to get ready for another roping, but the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. Finally, it lands a hit. Your gambeson does its job and protects your flesh. Hurt by the sheer strength of the hit, you manage to leap away, ready for another try with the rope, but the bird is also preparing itself."
                    else:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        $ foragingground_bird_dmgtopc += 1
                        $ custom3 = "You move away, doing your best to get ready for another roping, but the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. Finally, it lands a hit, piercing through your worn gambeson. Underneath the pain, you feel the stickiness of your blood. You manage to leap away, ready for another try with the rope, but the bird is also preparing itself."
                        if not cleanliness_clothes_blood:
                            $ cleanliness_clothes_blood = 1
                            show minus1appearance at appearancechange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                else:
                    $ custom6 = "You move away, doing your best to get ready for another roping, but the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. The cold beak sinks into your skull."
                    jump foraginggroundgameover
                if foragingground_bird_timer <= 0:
                    jump foraginggroundhuntingregular06victory
                if foragingground_bird_timer <= foragingground_bird_threshold_timer and not foragingground_bird_threshold:
                    $ foragingground_bird_threshold = 1
                    jump foraginggroundhuntingregular05fear
                jump foraginggroundhuntingregular04
            '{image=d6} I should try to rope it.' if not foragingground_bird_used_rope:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I should try to rope it.')
                $ custom2 = ""
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if armor == 4:
                    $ d100roll -= 5
                $ d100roll += (foragingground_bird_timer*10)
                if d100roll < 80:
                    $ foragingground_bird_used_rope = 1
                    $ custom3 = "The creature pays attention to your movements, and once the rope flies toward it, it steps away, then moves into a charge. Preparing the rope for the next attempt will take some time, but will also put you in a vulnerable position."
                else:
                    $ foragingground_bird_used_rope = 2
                    $ custom3 = "You prepare yourself to throw, and the creature gets distracted by the approach of your companions. Your loop lands on its head, so you pull, squeezing the monster’s thick neck. It twists its shell in anger, then runs at you, not giving you a chance to choke it.\n\nWhile you may still be in danger, you now have an additional way to stop it from running away."
                jump foraginggroundhuntingregular04
            '{image=d6} I keep my distance and dodge, when necessary.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I keep my distance and dodge, when necessary.')
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. "
                else:
                    $ custom2 = ""
                $ foragingground_bird_timer -= 1
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if armor == 4:
                    $ d100roll -= 5
                $ d100roll -= (pc_hp*10)
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                $ d100roll += (foragingground_bird_timesdodged*10)
                $ foragingground_bird_timesdodged += 1
                if d100roll > 80: # fail and escaped
                    if not foragingground_bird_charged:
                        $ foragingground_bird_charged = 1
                        $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nYou suddenly jump to the side, afraid of an incoming hit, and lose your balance. The bird passes you by and gives you a surprised look, but as it sees the other two men are getting closer, it makes a single, long screech and flees west, as quickly as it can."
                    else:
                        $ custom2 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nYou suddenly jump to the side, afraid of an incoming hit, and lose your balance. The bird passes you by and gives you a surprised look, but as it sees the other two men are getting closer, it makes a single, long screech and flees west, as quickly as it can."
                    jump foraginggroundhuntingregular05fail
                elif d100roll > 30: # fail
                    if pc_hp:
                        if armor >= 3:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom3 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nFinally, the beast lands a hit. Your gambeson does its job and protects your flesh. Though in pain, you manage to leap away, then wait for another charge."
                        elif armor >= 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom3 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nFinally, the beast lands a hit. Your gambeson does its job and protects your flesh. Though in pain, you manage to leap away, then wait for another charge."
                        else:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            $ foragingground_bird_dmgtopc += 1
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            $ custom3 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nFinally, the beast lands a hit. Your gambeson, already damaged, isn’t enough, and you feel the stickiness of your blood. Though in pain, you manage to leap away, then wait for another charge."
                        jump foraginggroundhuntingregular04
                    else:
                        if not foragingground_bird_charged:
                            $ foragingground_bird_charged = 1
                            $ custom6 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nNevertheless, the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. The cold beak sinks into your skull."
                        else:
                            $ custom6 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nNevertheless, the creature is merciless. It keeps pushing, flapping its wings and moving its head, hoping to reach you with a strong thrust. The cold beak sinks into your skull."
                        jump foraginggroundgameover
                else: # success
                    $ custom3 = "You do your best to find a balance between running to safety, jumping away from the beak, and staying close to hold the bird’s attention. Its reflexes are so quick that you can’t imagine doing all this while also trying to strike it back.\n\nFinally, you’re lucky. The creature doesn’t find a way to land a hit, and observes you with respect. It turns around, but stops in place when it sees your companions. It looks at you again, preparing for the next charge."
                jump foraginggroundhuntingregular04
            '{image=d6} I hold my ground - make a quick dodge, then grapple the bird.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I hold my ground - make a quick dodge, then try to hold the bird where it is.')
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. "
                else:
                    $ custom2 = ""
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if armor == 4:
                    $ d100roll -= 5
                $ d100roll -= (pc_hp*10)
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                $ d100roll += (10*foragingground_bird_timesdodged)
                $ foragingground_bird_timesdodged += 1
                if d100roll > 70: #epic fail
                    $ foragingground_bird_timer -= 1
                    if pc_hp:
                        if armor >= 3:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder, then your back. Your gambeson does its job and protects your flesh. Though in pain, you press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                        elif armor == 2:
                            $ armor = limit_armor(armor-2)
                            show minus2armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 armor points.{/i}')
                            $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder, then your back. Your gambeson does its job and protects your flesh. Though in pain, you press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        elif armor == 1:
                            $ armor = limit_armor(armor-1)
                            show minus1armor at armorchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                            $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder, then your back. Your gambeson is of little use, and you scream in pain as your blood releases.\n\nyou press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        else:
                            $ pc_hp = limit_pc_hp(pc_hp-2)
                            $ foragingground_bird_dmgtopc += 2
                            $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder, then your back. Your gambeson is of little use, and you scream in pain as your blood releases.\n\nyou press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                            show minus2hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                            if not cleanliness_clothes_blood:
                                $ cleanliness_clothes_blood = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance points.{/i}')
                        jump foraginggroundhuntingregular04
                    else:
                        if not foragingground_bird_charged:
                            $ foragingground_bird_charged = 1
                            $ custom6 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. You wait to duck at the very last moment, but you’re already too weak and tired to stay in control. Your neck releases blood."
                        else:
                            $ custom6 = "You wait to duck at the very last moment, but you’re already too weak and tired to stay in control. The cold beak sinks into your skull."
                        jump foraginggroundgameover
                elif d100roll > 20: #slight fail
                    $ foragingground_bird_timer -= 2
                    if armor >= 3:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder. Your gambeson does its job and protects your flesh. Though in pain, you press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                        jump foraginggroundhuntingregular04
                    elif armor >= 1:
                        $ armor = limit_armor(armor-1)
                        show minus1armor at armorchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 armor point.{/i}')
                        $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder. Your gambeson does its job and protects your flesh. Though in pain, you press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                        jump foraginggroundhuntingregular04
                    else:
                        if pc_hp:
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            $ foragingground_bird_dmgtopc += 1
                            $ custom3 = "You wait to duck at the very last moment. You try to catch the beast from the side, but it has enough time to peck your shoulder. Your gambeson, already damaged, isn’t enough, and you feel the stickiness of your blood.\n\nyou press your shell against the monster’s wing, trying to avoid its legs. The runner, as confused as you are, makes an angry screech and tries to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                            jump foraginggroundhuntingregular04
                        else:
                            if not foragingground_bird_charged:
                                $ foragingground_bird_charged = 1
                                $ custom6 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. You wait to duck at the very last moment, but you’re already too weak and tired to stay in control. Your neck releases blood."
                            else:
                                $ custom6 = "You wait to duck at the very last moment, but you’re already too weak and tired to stay in control. The cold beak sinks into your skull."
                            jump foraginggroundgameover
                else: # success
                    $ foragingground_bird_timer -= 3
                    $ custom3 = "You wait to duck at the very last moment. In the blink of an eye, you show up at the beast’s side, pressing your shell to its large chest, too large for you to wrap your arms around it. You try to avoid the massive legs, but the monster turns out to be as confused as you are, making an angry screech and trying to shake you off. The feathers are scratching your cheeks and getting in your mouth.\n\nOnce the bird gets rid of you, it runs east, not aware that it only helps your companions."
                jump foraginggroundhuntingregular04
            'It may be a good moment to open my bag and drink a healing potion. (disabled)' ( condition="(pc_hp <= 3 and item_generichealingpotion) or (pc_hp <= 3 and item_potiondolmen and item_potiondolmen_known) or (pc_hp <= 3 and item_smallhealingpotion)" ):
                pass
            'I can’t win. Once it charges at me, I roll away, giving it a chance to run away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t win. Once it charges at me, I roll away, giving it a chance to run away.')
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. It lowers its long neck, pointing it at you like one would a spear. Then, as you suddenly jump to the side, the bird passes you by and gives you a surprised look, but as it sees the other two men are getting closer, it makes a single, long screech and flees west, as quickly as it can."
                else:
                    $ custom2 = "The bird passes you by and gives you a surprised look, but as it sees the other two men are getting closer, it makes a single, long screech and flees west, as quickly as it can."
                jump foraginggroundhuntingregular05fail

    label foraginggroundhuntingregular05fear: #fear, afterinteraction
        $ can_potions = 0
        if pc_class == "warrior":
            $ at_unlock_force = 1
            $ at = 0
        menu:
            '[custom2][custom3]
            \n\nThat’s when the loop lands on its neck, tightening quickly, and {color=#f6d6bd}Tzvi{/color} shouts cheerfully. The bird remains silent, maybe already out of breath.
            \n\nBut then it dashes forward, so fast you can’t help but step back. It either doesn’t understand the danger involved in moving in its situation, or doesn’t care about it. It runs forward, trying to flee. It makes two, five jumps... You hear {color=#f6d6bd}Ilan’s{/color} swear. Without looking at him, you know that he let go of the rope.
            '
            'The beast is not in control. I am. I gather all my strength and stand in its way.' ( condition="at == 'force'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The beast is not in control. I am. I gather all my strength and stand in its way.')
                $ at_unlock_force = 0
                $ at = 0
                $ foragingground_bird_used_shield += 1
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. "
                else:
                    $ custom2 = ""
                $ custom3 = "You confidently dash forward, knowing that the bird won’t escape if it decides to fight you - it needs to ignore you, and count for the best.\n\nYou dodge its strike, then catch the bird’s wing with both of your hands. The harsh touch of feathers means nothing - you focus on your firm stance. It takes but a breath - the bird runs forward, but you turn it around, making it plunge into the ground.\n\nIt tries to get back on its feet, but the rope around its neck is already hindering its movements. After {color=#f6d6bd}Tzvi{/color} ropes it with yet another loop, the battle is over."
                $ custom4 = "I stretch out and dust off my hands. Easy."
                jump foraginggroundhuntingregular06victory
            'Since I’ve already caught it with my own rope, all I have to do is stop it from getting away.' if foragingground_bird_used_rope == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since it’s already caught with my own rope, all I have to do is stop it from getting away.')
                $ custom2 = ""
                $ at_unlock_force = 0
                $ at = 0
                if not cleanliness_clothes_torn:
                    $ cleanliness_clothes_torn = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom3 = "You dash to your rope and start to roll it with both hands. You plant your feet on a convenient rock, then pull, felling the bird on its side - but its strength and weight knocks you down as well.\n\nIt tries to get up, but you keep pulling, fighting against its muscular neck and legs. {color=#f6d6bd}Ilan{/color} comes to the rescue - it’s now two against one, and the beast can’t make as much as a step. Once {color=#f6d6bd}Tzvi{/color} grabs the second rope, the battle is over. The bird staggers, trying to keep its head straight, until, exhausted, falls on the ground."
                $ custom4 = "Time to regroup."
                jump foraginggroundhuntingregular06victory
            'I need to stop the bird before it runs away. I grab the loose rope and pull with all my strength.' if pc_hp >= 3 and foragingground_bird_used_rope != 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to stop the bird before it runs away. I grab the loose rope and pull with all my strength.')
                $ custom2 = ""
                $ at_unlock_force = 0
                $ at = 0
                if not cleanliness_clothes_torn:
                    $ cleanliness_clothes_torn = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                $ custom3 = "You dash forward, barely reaching the pulled rope, then start to roll it with both hands. You plant your feet on a convenient rock, then pull, felling the bird on its side - but its strength and weight knocks you down as well.\n\nIt tries to get up, but you keep pulling, fighting against its muscular neck and legs. {color=#f6d6bd}Ilan{/color} comes to the rescue - it’s now two against one, and the beast can’t make as much as a step. After {color=#f6d6bd}Tzvi{/color} ropes it with yet another loop, the battle is over. The bird staggers, trying to keep its head straight, until, exhausted, falls on the ground."
                $ custom4 = "Time to regroup."
                jump foraginggroundhuntingregular06victory
            'I’m too weak to keep it in place by holding the loose rope. (Required vitality: 3) (disabled)' if pc_hp < 3 and foragingground_bird_used_rope != 2:
                pass
            'I stand in its way, raising my shield. It’ll have to stop.' ( condition="item_shield and pc_hp > 0 and at != 'force'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand in its way, raising my shield. It’ll have to stop.')
                $ at_unlock_force = 0
                $ at = 0
                $ foragingground_bird_used_shield += 1
                if not cleanliness_clothes_torn:
                    $ cleanliness_clothes_torn = 1
                    show minus1appearance at appearancechange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                if not foragingground_bird_charged:
                    $ foragingground_bird_charged = 1
                    $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. "
                else:
                    $ custom2 = ""
                $ custom3 = "You barely manage to get in its way, but once it crashes into you, you wish you hadn’t. You’re on the ground, pinned by the heavy shell, though your armor softens the impact. It tries to get off you, and as your arms are behind the thick layer of lumber, you can’t do much to stop it. Thankfully, the stunned creature can’t get back on its feet yet - once it releases you, you get back to safety.\n\nSoon after, the rope around its neck gets pulled. The bird staggers, trying to keep its head straight, but can’t help but hit the ground again. After {color=#f6d6bd}Tzvi{/color} ropes it with yet another loop, the battle is over."
                $ custom4 = "I step away and dust myself off."
                jump foraginggroundhuntingregular06victory
            'I’m too weak to block it with my shield. (Required vitality: 1) (disabled)' ( condition="item_shield and pc_hp == 0 and at != 'force'" ) :
                pass
            '{image=d6} I stand in its way and, once it gets close, I try to catch it.' ( condition="at != 'force'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I stand in its way and, once it gets close, I try to catch it.')
                $ at_unlock_force = 0
                $ at = 0
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if armor == 4:
                    $ d100roll -= 5
                $ d100roll -= (pc_hp*10)
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                $ d100roll += (foragingground_bird_timesdodged*10)
                $ foragingground_bird_timesdodged += 1
                if d100roll > 50: # fail and escaped
                    if not foragingground_bird_charged:
                        $ foragingground_bird_charged = 1
                        $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. You try to get in the bird’s way without putting yourself at risk, but it manages to get away from you. Your hands manage to grasp a few feathers, but the creature pushes you away with such a strength you land on your back. Your prey leaves you behind, triumphantly screeching."
                    else:
                        $ custom2 = "You try to get in the bird’s way without putting yourself at risk, but it manages to get away from you. Your hands manage to grasp a few feathers, but the creature pushes you away with such a strength you land on your back. Your prey leaves you behind, triumphantly screeching."
                    jump foraginggroundhuntingregular05fail
                else: # success
                    if not foragingground_bird_charged:
                        $ foragingground_bird_charged = 1
                        $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. "
                    else:
                        $ custom2 = ""
                    $ custom3 = "You try to get in the bird’s way without putting yourself at risk. It nimbly avoids you, but you manage to grab its wing. You both stagger, then land on the ground, trying to both get up, and stay away from each other.\n\nIt’s too late for the creature - the rope around its neck gets pulled, sending it to the ground again. After {color=#f6d6bd}Tzvi{/color} ropes it with yet another loop, the battle is over."
                    $ custom4 = "I throw the feathers away."
                jump foraginggroundhuntingregular06victory
            'I have to block its path, and hope I won’t get trampled to death.' ( condition="at != 'force'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have to block its path, and hope I won’t get trampled to death.')
                $ at_unlock_force = 0
                $ at = 0
                if armor > 2:
                    $ custom4 = "I stand up, step away, and dust myself off."
                    if not foragingground_bird_charged:
                        $ foragingground_bird_charged = 1
                        $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. "
                    else:
                        $ custom2 = ""
                    $ custom3 = "You barely manage to get in its way, but once it crashes into you, you wish you hadn’t. You’re on the ground, pinned by the heavy shell, though your armor softens the impact. You hold the bird tight, tearing away its feathers without even realizing it. The monster is twisting in your arms, trying to crush you with its legs and chest, or reach your flesh with its beak. Thankfully, the rope around its neck gets pulled, setting you free. The bird staggers, and can’t help but hit the ground again. After {color=#f6d6bd}Tzvi{/color} ropes it with yet another loop, the battle is over."
                    jump foraginggroundhuntingregular06victory
                else:
                    if pc_hp:
                        $ pc_hp = limit_pc_hp(pc_hp-1)
                        show minus1hp at hpchange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        $ foragingground_bird_dmgtopc += 1
                        $ custom4 = "I stand up, step away, and dust myself off."
                        if not foragingground_bird_charged:
                            $ foragingground_bird_charged = 1
                            $ custom2 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. "
                        else:
                            $ custom2 = ""
                        $ custom3 = "You barely manage to get in its way, but once it crashes into you, you wish you hadn’t. You’re on the ground, pinned by the heavy shell, gasping for air as your stomach is crushed. You hold the bird tight, tearing away its feathers without even realizing it. The monster is twisting in your arms, trying to crush you with its legs and chest, or reach your flesh with its beak. Thankfully, the rope around its neck gets pulled, setting you free. The bird staggers, and can’t help but hit the ground again. After {color=#f6d6bd}Tzvi{/color} ropes it with yet another loop, the battle is over."
                        jump foraginggroundhuntingregular06victory
                    else:
                        if not foragingground_bird_charged:
                            $ foragingground_bird_charged = 1
                            $ custom6 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. You barely manage to get in its way, but once it crashes into you, you wish you hadn’t. You’re on the ground, pinned by the heavy shell, gasping for air as your stomach is crushed. You hold the bird tight, tearing away its feathers without even realizing it, but you’re too weak. The creature manages to get away, then reaches for your chest with its beak. Your bones crack."
                            jump foraginggroundgameover
                        else:
                            $ custom6 = "You barely manage to get in its way, but once it crashes into you, you wish you hadn’t. You’re on the ground, pinned by the heavy shell, gasping for air as your stomach is crushed. You hold the bird tight, tearing away its feathers without even realizing it, but you’re too weak. The creature manages to get away, then reaches for your chest with its beak. Your bones crack."
                            jump foraginggroundgameover
            '{image=d6} I have to shoot it with a crossbow. It’s my only chance.' if item_crossbow and item_crossbowquarrels:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I have to shoot it with a crossbow. It’s my only chance.')
                $ at_unlock_force = 0
                $ at = 0
                $ custom2 = ""
                $ foragingground_bird_used_crossbow = 1
                $ at_unlock_force = 0
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if not pc_food:
                    $ d100roll += 5
                if pc_food == 3:
                    $ d100roll -= 5
                if pc_food == 4:
                    $ d100roll -= 10
                if armor == 4:
                    $ d100roll -= 5
                $ item_crossbowquarrels -= 1
                $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel.{/i}')
                if pc_class == "warrior":
                    $ d100roll -= (pc_battlecounter*2)
                else:
                    $ d100roll -= (pc_battlecounter)
                if d100roll > 80:
                    $ foragingground_bird_taken = 3
                    $ foragers_friendship -= 1
                    menu:
                        'You grab your loaded weapon, aim, and shoot - but it’s a miss. The bolt smashes against the rock. The bird runs west, as fast as a horse, giving you no chance to reload in time. After a minute, the foragers approach you slowly, with {color=#f6d6bd}Tzvi{/color} wiping his nose on his sleeve. “Well, shit, friend,” {color=#f6d6bd}Ilan{/color} says with a sigh. “It won’t be back any day soon. We better get back.” His tone is friendly, but betrayed by his angry, rapid movements. He doesn’t look at you, doesn’t wait, just hits the road without looking back. His shorter companion shakes his head and follows him energetically.
                        '
                        'Like they said. There’s nothing we can do now.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Like they said. There’s nothing we can do now.')
                            $ at_unlock_spell = 0
                            jump leadingtheforagersFROMforagingground
                elif d100roll > 40:
                    jump foraginggroundhuntingregular05birddead
                else:
                    jump foraginggroundhuntingregular05crossbowvictory
            'I may not be able to stop it, but I can charge at it with my axe. Better dead than gone.' ( condition="at != 'force' and pc_hp >= 2" ) :
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I have to shoot it with a crossbow. It’s my only chance.')
                $ at_unlock_force = 0
                $ at = 0
                $ custom2 = ""
                jump foraginggroundhuntingregular05axingthebird
            'I’m too tired to charge at it with my axe. (Required vitality: 2) (disabled)' ( condition="at != 'force' and pc_hp < 2" ) :
                pass
            'I can’t face the beast. I let it escape.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t face the beast. I let it escape.')
                $ at_unlock_force = 0
                $ at = 0
                $ foragingground_bird_taken = 3
                $ foragers_friendship -= 3
                $ creeks_reputation -= 1
                $ foggy_friendship -= 1
                $ foragers_caius_friendship -= 1
                menu:
                    'The bird doesn’t spare you a glance. It runs west, as quick as a horse. After a minute, the foragers approach you slowly, with {color=#f6d6bd}Tzvi{/color} wiping his nose on his sleeve. “Well, shit, friend,” {color=#f6d6bd}Ilan{/color} says with a sigh. “It won’t be back any day soon. We better get back.” His tone is friendly, but betrayed by his angry, rapid movements. He doesn’t look at you, doesn’t wait, just hits the road without looking back. His shorter companion shakes his head and follows him energetically.
                    '
                    'Like they said. There’s nothing we can do now.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Like they said. There’s nothing we can do now.')
                        $ at_unlock_spell = 0
                        jump leadingtheforagersFROMforagingground

    label foraginggroundhuntingregular05birddead: # crossbow fail
        $ foragingground_bird_taken = 2
        $ foragers_friendship -= 1
        $ foragers_caius_friendship += 1
        menu:
            'The bolt hits the bird’s side, knocking it to the ground. The runner tries to stand up, but staggers, screeching. It withers away right in front of you, and stops moving before you reach it.
            \n\n{color=#f6d6bd}Tzvi{/color} wipes his nose on his sleeve, whispering some moderate profanities. “Well, friend, at least you saved the meat,” says {color=#f6d6bd}Ilan{/color} with an unconvincing sigh. “It’s better than nothing, though you know what it means. Worse pay for you.” He looks at the sun, then at the bird again. “Turns out it’s a shit luck that we don’t have your horse with us. Let’s cut away the legs to make it lighter.” Without looking at you, the foragers head toward it with an axe and a dagger.
            '
            'I wait for them to be done with the dirty work and get ready to move on.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for them to be done with the dirty work and get ready to move on.')
                $ at_unlock_spell = 0
                jump leadingtheforagersFROMforagingground

    label foraginggroundhuntingregular05fail: # fail
        $ can_potions = 0
        $ foragingground_bird_taken = 3
        $ foragers_friendship -= 3
        $ creeks_reputation -= 1
        $ foggy_friendship -= 1
        $ cleanliness = limit_cleanliness(cleanliness-2)
        show minus2appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
        menu:
            '[custom2]You look at it in panic, afraid that it may get to {color=#f6d6bd}[horsename]{/color}, before you realize that you left it at {color=#f6d6bd}Foggy’s{/color} place.
            \n\nYou stand up and dust yourself off. After a minute, the foragers approach you slowly, with {color=#f6d6bd}Tzvi{/color} wiping his nose on his sleeve. “Well, shit, friend,” {color=#f6d6bd}Ilan{/color} says with a sigh. “It won’t be back any day soon. We better get back.” His tone is friendly, but betrayed by his angry, rapid movements. He doesn’t look at you, doesn’t wait, just hits the road without looking back. His shorter companion shakes his head and follows him energetically.
            '
            'Like they said. There’s nothing we can do now.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Like they said. There’s nothing we can do now.')
                $ at_unlock_spell = 0
                jump leadingtheforagersFROMforagingground

    label foraginggroundhuntingregular06victory: # victory
        $ can_potions = 0
        $ foragingground_bird_taken = 1
        $ creeks_reputation += 1
        $ foggy_friendship += 2
        $ foragers_friendship += 1
        $ foragers_caius_friendship -= 1
        $ cleanliness = limit_cleanliness(cleanliness-2)
        show minus2appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
        menu:
            '[custom2][custom3]
            '
            '[custom4]':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- %s' %custom4)
                if foragingground_bird_used_shield:
                    $ custom2 = "He points at your shield. “Nice idea, taking this. You dazed the shit out of it.” {color=#f6d6bd}His companion{/color} nods with a grin. "
                else:
                    $ custom2 = ""
                if foragingground_bird_used_blindingpowder:
                    $ custom3 = "“You know your magic tricks, good thing you didn’t blind it for good. Leading it to back would be a bother.” "
                else:
                    $ custom3 = ""
                if foragingground_bird_used_stoat or foragingground_bird_used_chicken:
                    $ custom5 = "He shakes his head. “I wish I knew that throwing a piece of meat would work that well. Didn’t even think about it before.” "
                else:
                    $ custom5 = ""
                if foragingground_bird_timesdodged >= 3:
                    $ custom4 = "He starts to laugh. “You were jumping around like a monkey, you have some legs!”"
                else:
                    $ custom4 = ""
                if foragingground_bird_used_rope == 2:
                    $ custom1 = "“Aye, you’re good with the loop,” adds {color=#f6d6bd}Tzvi{/color} loudly, gasping for breath after a long run. “Better take this,” he gives you his own fine quality rope. “We won’t untie that one of yours any time soon. Shag me, I missed my throw!” He shakes his head with a mixture of anger and embarrassment. “Good thing we hired you.”"
                else:
                    $ custom1 = "“Shag me, I missed my throw with the rope!” adds {color=#f6d6bd}Tzvi{/color} loudly, gasping for breath after a long run, though he keeps smiling with pride. “At least the second try worked out. The bird is damn ours, and that’s all that matters, aye?”"
                menu:
                    'The bird keeps trying to find a way out, but with little luck. Once it regains a bit of strength, it charges at you, but after just two leaps it gets stopped by the second rope. It regains its voice, screeching at its tormentors, but there’s something more hidden behind its previous threats and anger. Maybe pain, maybe contempt.
                    \n\n“A damn, damn good job,” thunders {color=#f6d6bd}Ilan{/color}. [custom2][custom3][custom5][custom4]
                    \n\n[custom1]
                    '
                    'I smile. “Good team work.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Good team work.')
                        $ foragers_friendship += 1
                        menu:
                            '“Aye, you deserve your coins,” {color=#f6d6bd}Ilan{/color} taps his pouch, but doesn’t pull out any dragons. “Let’s move on, the sooner we get back, the better.” {color=#f6d6bd}The other forager{/color} lets you know that he’s ready. The runner is still far away, held on the taut rope.
                            '
                            'I gather my belongings and lead the men north, chit-chatting about our hunt.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather my belongings and lead the men north, chit-chatting about our hunt.')
                                $ at_unlock_spell = 0
                                jump leadingtheforagersFROMforagingground
                    'I nod at our prey. “We should go. If anything tries to get to us, we’ll struggle to keep the bird on the rope.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod at our prey. “We should go. If anything tries to get to us, we’ll struggle to keep the bird on the rope.”')
                        $ foragers_friendship += 1
                        menu:
                            '“Aye, can’t argue with that.” {color=#f6d6bd}Ilan{/color} stretches his large legs and prepares his bags. “We’re not much of fighters, I don’t wish to pay you for saving us on the road.” {color=#f6d6bd}The other forager{/color} chuckles as he stays away, keeping the exhausted bird on the taut rope. “We’re ready, if you are.”
                            '
                            'I gather my belongings and lead the men north, looking out for any beasts.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather my belongings and lead the men north, looking out for any beasts.')
                                $ at_unlock_spell = 0
                                jump leadingtheforagersFROMforagingground

        label foraginggroundhuntingregular05crossbowvictory:
            $ foragingground_bird_taken = 1
            $ foragers_caius_friendship -= 1
            $ foragers_friendship += 1
            $ creeks_reputation += 1
            $ foggy_friendship += 1
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            if foragingground_bird_used_shield:
                $ custom2 = "He points at your shield. “Nice idea, taking this. You dazed the shit out of it.” {color=#f6d6bd}His companion{/color} nods with a grin. "
            else:
                $ custom2 = ""
            if foragingground_bird_used_blindingpowder:
                $ custom3 = "“You know your magic tricks, good thing you didn’t blind it for good. Leading it to back would be a bother.” "
            else:
                $ custom3 = ""
            if foragingground_bird_used_stoat or foragingground_bird_used_chicken:
                $ custom5 = "He shakes his head. “I wish I knew that throwing a piece of meat would work that well. Didn’t even think about it before.” "
            else:
                $ custom5 = ""
            if foragingground_bird_timesdodged >= 3:
                $ custom4 = "He starts to laugh. “You were jumping around like a monkey, you have some legs!”"
            else:
                $ custom4 = ""
            if foragingground_bird_used_rope == 2:
                $ custom1 = "“Aye, you’re good with the loop,” adds {color=#f6d6bd}Tzvi{/color} loudly, gasping for breath after a long run. “Better take this,” he gives you his own fine quality rope. “We won’t untie that one of yours any time soon. Shag me, I missed my throw!” He shakes his head with a mixture of anger and embarrassment. “Good thing we hired you.”"
            else:
                $ custom1 = "“Shag me, I missed my throw with the rope!” adds {color=#f6d6bd}Tzvi{/color} loudly, gasping for breath after a long run, though he keeps smiling with pride. “At least the second try worked out. The bird is damn ours, and that’s all that matters, aye?”"
            menu:
                'The bolt hits the bird’s thigh, knocking it on the ground. Once it gets up, it’s limping, making an upset screech whenever it puts its weight on the wounded leg. The foragers catch up with it easily, grabbing the ropes from a safe distance. The bird, unaware of the situation, still tries to charge at {color=#f6d6bd}Tzvi{/color}, but fails to overcome {color=#f6d6bd}Ilan’s{/color} grasp. A strong pull chokes it in the middle of its step. It looks around, more exhausted with every breath.
                \n\n“Good aim,” {color=#f6d6bd}the shorter man{/color} must shout to be heard. “Risky, but good!”
                \n\n“All that’s left is the path back home. Won’t be difficult with such a wound,” thunders {color=#f6d6bd}Ilan{/color}. [custom2][custom3][custom5][custom4]
                '
                'I smile. “Good team work.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Good team work.')
                    $ foragers_friendship += 1
                    menu:
                        '“Aye, you deserve your coins,” {color=#f6d6bd}Ilan{/color} taps his pouch, but doesn’t pull out any dragons. “Let’s move on, the sooner we get back, the better.” {color=#f6d6bd}The other forager{/color} lets you know that he’s ready. The runner is still far away, held on the taut rope.
                        '
                        'I gather my belongings and lead the men north, chit-chatting about our hunt.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather my belongings and lead the men north, chit-chatting about our hunt.')
                            $ at_unlock_spell = 0
                            jump leadingtheforagersFROMforagingground
                'I nod at our prey. “We should go. If anything tries to get to us, we’ll struggle to keep the bird on the rope.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod at our prey. “We should go. If anything tries to get to us, we’ll struggle to keep the bird on the rope.”')
                    $ foragers_friendship += 1
                    menu:
                        '“Aye, can’t argue with that.” {color=#f6d6bd}Ilan{/color} stretches his large legs and prepares his bags. “We’re not much of fighters, I don’t wish to pay you for saving us on the road.” {color=#f6d6bd}The other forager{/color} chuckles as he stays away, keeping the exhausted bird on the taut rope. “We’re ready, if you are.”
                        '
                        'I gather my belongings and lead the men north, looking out for any beasts.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I gather my belongings and lead the men north, looking out for any beasts.')
                            $ at_unlock_spell = 0
                            jump leadingtheforagersFROMforagingground

        label foraginggroundhuntingregular05axingthebird:
            $ foragingground_bird_taken = 2
            $ foragers_friendship -= 1
            $ foragers_caius_friendship += 1
            $ cleanliness = limit_cleanliness(cleanliness-2)
            show minus2appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 appearance points.{/i}')
            if not foragingground_bird_charged:
                $ foragingground_bird_charged = 1
                $ custom1 = "The giant feet are pounding the ground, with every leap scuffing up clouds of leaves and sand. "
            else:
                $ custom1 = ""
            menu:
                'You dash forward, preparing to take a swing. [custom1]You barely get there in time, hitting the beast’s side not just with your blade, but also crashing into it with your entire shell. You bounce back, but the beast also staggers, then falls on the ground, trying to retrieve control over its legs. You try to stand up, using your hands to move forward even a heartbeat earlier, then you swipe, and again, and again, aiming at whatever you can and sending blood into the air. The creature isn’t in pain for long, as once the blood gushes out of its neck, it stops moving.
                \n\n{color=#f6d6bd}Tzvi{/color} wipes his nose on his sleeve, whispering some moderate profanities. “Well, friend, at least you saved the meat,” says {color=#f6d6bd}Ilan{/color} with an unconvincing sigh. “It’s better than nothing, though you know what it means. Worse pay for you.” He looks at the sun, then at the bird again. “Turns out it’s a shit luck that we don’t have your horse with us. Let’s cut away the legs to make it lighter.” Without looking at you, the foragers head toward it with an axe and a dagger.
                '
                'I wait for them to be done with the dirty work and get ready to move on.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for them to be done with the dirty work and get ready to move on.')
                    $ at_unlock_spell = 0
                    jump leadingtheforagersFROMforagingground

    label foraginggroundgameover:
        $ can_potions = 0
        $ pc_hp = 0
        show minus5hp at hpchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
        if pc_religion == "pagan":
            show areapicture gameover_alt at basicfade
        else:
            show areapicture gameover at basicfade
        menu:
            '[custom6]
            \n
            \n\n[pcname]’s soul has left its shell.
            '
            'Let me replay this encounter.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this encounter.')
                stop music fadeout 4.0
                $ renpy.load("combatsave")

########################
    label leadingtheforagersFROMforagingground:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show areapicture foraginggroundtowanderer at basicfade
        $ renpy.music.play("audio/track_02foggylake.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        stop nature fadeout 4.0
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ quarters += 1
        $ foragingground_foragers_tofoggylake = 1
        $ pc_battlecounter += 1
        if foragingground_bird_taken == 1: # taken
            if foragingground_bird_used_crossbow:
                $ quarters += 1
                $ custom1 = "though its wounded leg helps you keep it in place"
            else:
                $ quarters += 2
                $ custom1 = "and even though it’s exhausted, you have to move slowly, paying attention to its steps"
            menu:
                'Every few minutes the runner tries to get away, [custom1]. The foragers seem to know what they’re doing, and at no point you feel threatened by the creature.
                \n\nYou keep looking around, but the other beasts seem to stay away. At one point you notice a blue wolf among the shorter grasses, but it only observes you in silence, standing on all paws as if it’s ready to run away. Your anxious companions fall quiet, but you keep moving forward.
                \n\nIn the middle of your journey, you think about {color=#f6d6bd}[horsename]{/color}. During your stroll everything seems taller, and the creatures you pass by feel more {i}real{/i}, as if they are no longer just shadows for you to leave behind.
                '
                'Being on the road without it feels lonely.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Being on the road without it feels lonely.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
                'I feel vulnerable, as if I’m inviting predators to chase after me.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I feel vulnerable, as if I’m inviting predators to chase after me.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
                'What matters even more is that I don’t have most of my stuff. I’m unprepared for any threats.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- What matters even more is that I don’t have most of my stuff. I’m unprepared for any threats.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
                'It would be a welcome rest from the sounds of the hooves, though the bird’s feet are scratching the ground in an even more annoying way.' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It would be a welcome rest from the sounds of the hooves, though the bird’s feet are scratching the ground in an even more annoying way.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
        if foragingground_bird_taken == 2: # killed
            $ quarters += 3
            stop nature fadeout 4.0
            menu:
                'The bird’s corpse may provide the locals with plenty of meat, but it’s too heavy for your group. The first plan was to attach the animal to a long stick and carry it between you, but it didn’t help much. Finally, you tie up your prey and drag it on the ground, hoping the feathers will protect the part of its flesh that drags on the surface of the road. It’s hard work, but the men are convinced it’s worth it, though you must take a few longer breaks.
                \n\nYou keep looking around, but the other beasts stay away. At one point you notice a blue wolf among the shorter grasses, but it only observes you in silence, standing on all paws as if it’s ready to run away. Your anxious companions fall quiet, but you keep moving forward.
                \n\nIn the middle of your journey, you think about {color=#f6d6bd}[horsename]{/color}. During your stroll everything seems taller, and the creatures you pass by feel more {i}real{/i}, as if they are no longer just shadows for you to leave behind.
                '
                'Being on the road without it feels lonely.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Being on the road without it feels lonely.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
                'I feel vulnerable, as if I’m inviting predators to chase after me.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I feel vulnerable, as if I’m inviting predators to chase after me.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
                'What matters even more is that I don’t have most of my stuff. I’m unprepared for any threats.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- What matters even more is that I don’t have most of my stuff. I’m unprepared for any threats.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
                'It would be a welcome rest from the sounds of the hooves, though the bird scratching the ground annoys me even more.' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It would be a welcome rest from the sounds of the hooves, though the bird scratching the ground annoys me even more.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
        if foragingground_bird_taken == 3: # escaped
            menu:
                'Your companions are grumbly, but at least you move at a good pace. You have time to listen to birds and observe the hills and meadows. After you reach the lake a blue wolf starts to follow you, hiding among the tall grasses, but it ends up disappearing among the thicker bushes. “See, nothing to be afraid of,” says {color=#f6d6bd}Tzvi{/color} with a smile as he wipes off the sweat from his forehead.
                \n\nIn the middle of your journey, you think about {color=#f6d6bd}[horsename]{/color}. During your stroll everything seems taller, and the creatures you pass by feel more {i}real{/i}, as if they are no longer just shadows for you to leave behind.
                '
                'Being on the road without it feels lonely.' if pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Being on the road without it feels lonely.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
                'I feel vulnerable, as if I’m inviting predators to chase after me.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I feel vulnerable, as if I’m inviting predators to chase after me.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
                'What matters even more is that I don’t have most of my stuff. I’m unprepared for any threats.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- What matters even more is that I don’t have most of my stuff. I’m unprepared for any threats.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
                'It’s a welcome rest from the sounds of the hooves.' if not pc_likeshorsename:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s a welcome rest from the sounds of the hooves.')
                    $ travel_destination = "foggylake"
                    $ quarters += 1
                    jump finaldestinationafterevent
