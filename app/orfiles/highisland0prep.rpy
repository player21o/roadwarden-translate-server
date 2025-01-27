###################### HIGH ISLAND PREPARATION
default highisland_recruitment_option_aegidia = 0 # sniping, combat, boat trip, wants to work alone
default highisland_recruitment_option_dalit = 0 # sniping, combat, traps, leading, beasts lore
default highisland_recruitment_option_navica = 0 # boating, prepares tool after arrival
default highisland_recruitment_option_thyrsus = 0 # magic, combat, poisons, fear
default highisland_recruitment_option_pyrrhos = 0 # sniping, survival, crafting
default highisland_recruitment_option_bandit = 0 # shadow magic, sneaking, assassination
default highisland_recruitment_option_tulia = 0 # combat, tanking, bravery
default highisland_recruitment_option_tzvi = 0 # combat, sneaking, pragmatism, agility
default highisland_recruitment_option_quintus = 0 # strong, stout, stubborn, boating
default highisland_recruitment_option_efren = 0 # traps, tracking, guiding

default highisland_howlersguards_hp = 10
default highisland_howlersguards_spearwoman_dead = 0

default highisland_crew_left = 0
default highisland_crew_dmg_target = 0
default highisland_crew_dmg_target2 = 0
default highisland_crew_dmg_target3 = 0

default aegidia_highisland_opinion = 0
default dalit_highisland_opinion = 0
default efren_highisland_opinion = 0
default thyrsus_highisland_opinion = 0
default pyrrhos_highisland_opinion = 0
default bandit_highisland_opinion = 0
default tulia_highisland_opinion = 0
default tzvi_highisland_opinion = 0
default quintus_highisland_opinion = 0

default aegidia_highisland_tired = 0
default dalit_highisland_tired = 0
default efren_highisland_tired = 0
default thyrsus_highisland_tired = 0
default pyrrhos_highisland_tired = 0
default bandit_highisland_tired = 0
default tulia_highisland_tired = 0
default tzvi_highisland_tired = 0
default quintus_highisland_tired = 0

default aegidia_highisland_blocked = 0
default dalit_highisland_blocked = 0
default efren_highisland_blocked = 0
default thyrsus_highisland_blocked = 0
default pyrrhos_highisland_blocked = 0
default bandit_highisland_blocked = 0 # shortcut_darkforest_bandit_dead_troll
default tulia_highisland_blocked = 0
default tzvi_highisland_blocked = 0
default quintus_highisland_blocked = 0

default aegidia_highisland_dead = 0
default dalit_highisland_dead = 0
default efren_highisland_dead = 0
default thyrsus_highisland_dead = 0
default pyrrhos_highisland_dead = 0
default bandit_highisland_dead = 0
default tulia_highisland_dead = 0
default tzvi_highisland_dead = 0
default quintus_highisland_dead = 0

### Boat Interaction
label highisland_journey_beachALL:
    label highisland_journey_beach00:
        $ highisland_journey_inprogress = 1
        nvl clear
        $ pc_area = "beach"
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        stop music fadeout 4.0
        play nature "audio/ambient/beach01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        show areapicture galerockstobeach at basicfade
        $ quarters = 84
        with Fade(1.8, 1.5, 1.8, color="#0f2a3f")
        if not beach_boatprepared:
            $ beach_boatprepared = 1
        if highisland_mode == "solo":
            jump highisland_journey_beach_solo01
        if highisland_mode == "crew":
            jump highisland_journey_beach_crew01
        if highisland_mode == "howlers":
            jump highisland_journey_beach_howlers01

    label highisland_journey_beach_solo01:
        $ quest_gatheracrew = 3
        $ renpy.notify("Quest completed: Gather a Crew")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Gather a Crew{/i}')
        menu:
            'After shoving the boat into the water, you take a deep breath of the chilling air. You adjust your clothes, but even their second layer is barely enough to keep you warm in the breeze. There’s sand in your boots.
            \n\nYou stare into the night and listen to the roaring waves. The course ahead may be easy to remember, but all that you see are the teeth-like rocks, waiting to tear the planks of your boat apart, and the seagulls, roaming the beach in search of food.
            \n\nYou look around. {color=#f6d6bd}[horsename]{/color} is back in {color=#f6d6bd}Gale Rocks{/color}.
            '
            'I should have said farewell.' if pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should have said farewell.')
                jump highisland_journey_beach_solo02
            'I’ll be with it soon.' if pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll be with it soon.')
                jump highisland_journey_beach_solo02
            'I wonder what would it do without me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wonder what would it do without me.')
                jump highisland_journey_beach_solo02
            'It won’t even notice I’m gone.' if not pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It won’t even notice I’m away.')
                jump highisland_journey_beach_solo02
            'If I were to die here, I would leave behind quite a fortune.' if not pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- If I were to die here, I would leave behind quite a fortune.')
                label highisland_journey_beach_solo02:
                    if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                        $ pc_faithpoints_opportunities += 1
                    menu:
                        'You throw the oars into the boat, followed by your modest equipment. As you sit down next to them, you hold onto the planks, not used to the swaying.
                        '
                        'At least I’ve got plenty of space for {color=#f6d6bd}Asterion{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least I’ve got plenty of space for {color=#f6d6bd}Asterion{/color}.')
                            jump highisland_journey01
                        'No one would be able to help me anyway.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- No one would be able to help me anyway.')
                            jump highisland_journey01
                        'Too bad I couldn’t trust anyone.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Too bad I couldn’t trust anyone.')
                            jump highisland_journey01
                        'I can’t believe there’s not a soul here to help me.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can’t believe there’s not a soul here to help me.')
                            jump highisland_journey01
                        'I ask my ancestors for guidance.' if pc_religion == "pagan" or pc_religion == "unknown":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask my ancestors for guidance.')
                            $ pc_faithpoints += 1
                            jump highisland_journey01
                        'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
                            $ pc_faithpoints += 1
                            jump highisland_journey01
                        'It’s time to row.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s time to row.')
                            jump highisland_journey01

    label highisland_journey_beach_howlers01:
        $ quest_gatheracrew = 2
        $ renpy.notify("Quest completed: Gather a Crew")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Gather a Crew{/i}')
        $ thais_about_highisland_recruitment_done_used = 1
        menu:
            'The guards shove the boat into the water while you take a deep breath of the chilling air. You adjust your clothes, but even their second layer is barely enough to keep you warm in the breeze. You stare into the night and listen to the roaring waves. The seagulls jump between the teeth-like rocks, seeking food and rest.
            \n\n“Let’s get to it,” says {color=#f6d6bd}the guard with the sword{/color}. Even though {color=#f6d6bd}Thais{/color} introduced him to you as {color=#f6d6bd}the leader{/color}, you don’t remember his name.
            \n\nYou look around, almost forgetting that {color=#f6d6bd}[horsename]{/color} is back in {color=#f6d6bd}Howler’s{/color}. Your crew, five souls strong, can barely squeeze into the boat. You’d argued that there wouldn’t be enough space for {color=#f6d6bd}Asterion{/color}, but {color=#f6d6bd}the mayor{/color} had waved it off with a burst of laughter. “You don’t think he’s {i}really{/i} alive, do you?”
            \n\nHer men and women examine their gambesons and weapons. For the most part, they stay quiet.
            '
            '“If you’ve got any questions, now is a good moment to ask them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you’ve got any questions, now is a good moment to ask them.”')
                $ custom1 = "After they exchange looks, {color=#f6d6bd}the one with the bow{/color} shrugs. “You told us everything already. We’ll handle this, do ne worry. Now grab the oars.”"
                jump highisland_journey_beach_howlers02
            '“We’ve got a few rough hours ahead, but stick together, and we’re all going to make it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ve got a few rough hours ahead, but stick together, and we’re all going to make it.”')
                $ custom1 = "“En what’s the alternative?” {color=#f6d6bd}The one with the bow{/color} gives an irritated shrug. “Do ne waste your breath, {i}roadwarden{/i}, you’ve some rowing to do.”"
                jump highisland_journey_beach_howlers02
            'I clear my throat. “We’re heading into danger, but we’ll return as heroes!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clear my throat. “We’re heading into danger, but we’ll return as heroes!”')
                $ custom1 = "You fall silent after their angry glances. “Do ne lure beasts,” says {color=#f6d6bd}the one with the bow{/color}. “Better sit down en grab the oars.”"
                jump highisland_journey_beach_howlers02
            'I wait for them to order me around.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for them to order me around.')
                $ custom1 = "Once they’re done, {color=#f6d6bd}the leader{/color} stretches out. “Well. Here, {i}we{/i} are the ones who know how to fight. So you,” he cocks his head in your direction, “are going to row.”"
                label highisland_journey_beach_howlers02:
                    if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                        $ pc_faithpoints_opportunities += 1
                    menu:
                        '[custom1]
                        \n\nYou get in with your modest equipment and grab the planks, not used to the swaying.
                        '
                        'I scowl at the guards. They’d better follow orders once we reach the wilderness.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I scowl at the guards. They’d better follow orders once we reach the wilderness.')
                            jump highisland_journey01
                        'They may not be friendly, but at least {color=#f6d6bd}Thais{/color} promised they are {i}the best for the job{/i}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- They may not be friendly, but at least {color=#f6d6bd}Thais{/color} promised they are {i}the best for the job{/i}.')
                            jump highisland_journey01
                        'They’re hiding something from me. I keep an eye on them.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- They’re hiding something from me. I keep an eye on them.')
                            jump highisland_journey01
                        'I ask my ancestors for guidance.' if pc_religion == "pagan" or pc_religion == "unknown":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask my ancestors for guidance.')
                            $ pc_faithpoints += 1
                            jump highisland_journey01
                        'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
                            $ pc_faithpoints += 1
                            jump highisland_journey01
                        'No reason to wait.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- No reason to wait.')
                            jump highisland_journey01

    label highisland_journey_beach_crew01:
        $ quest_gatheracrew = 2
        $ renpy.notify("Quest completed: Gather a Crew")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Gather a Crew{/i}')
        if highisland_recruitment_option_aegidia:
            $ aegidia_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_dalit:
            $ dalit_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_efren:
            $ efren_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_navica:
            $ navica_highisland_joined = 1
        if highisland_recruitment_option_thyrsus:
            $ thyrsus_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_pyrrhos:
            $ pyrrhos_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_bandit:
            $ bandit_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_tulia:
            $ tulia_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_tzvi:
            $ tzvi_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_quintus:
            $ quintus_highisland_joined = 1
            $ highisland_crew_left += 1
        ##########
        if efren_highisland_joined:
            $ custom3 = ", unaware of {color=#f6d6bd}Efren’s{/color} hungry glances"
        else:
            $ custom3 = ""
        if navica_highisland_joined:
            $ custom4 = "You take a deep breath of the chilling air and adjust your clothes. Thanks to the additional layer of a clothes and pants given to you by {color=#f6d6bd}Navica{/color}, you resist the breeze."
        else:
            $ custom4 = "You take a deep breath of the chilling air and adjust your clothes, but even their second layer is barely enough to keep you warm in the breeze."
        if quintus_highisland_joined:
            $ custom10 = "{color=#f6d6bd}Quintus{/color} shoves"
        else:
            $ custom10 = "You and your companions shove"
        menu:
            '[custom10] the boat into the water. [custom4] You stare into the night and listen to the roaring waves. The seagulls jump between the teeth-like rocks, seeking food and rest[custom3].
            \n\nYou look around, almost forgetting that {color=#f6d6bd}[horsename]{/color} is waiting for you in {color=#f6d6bd}Gale Rocks{/color}, then turn toward the others.
            '
            '“If you’ve got any questions, now is a good moment to ask them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you’ve got any questions, now is a good moment to ask them.”')
                if dalit_highisland_joined:
                    $ custom2 = "“Is the water always so loud, and angry?” {color=#f6d6bd}Dalit{/color} addresses no one in particular. “Even if gorgeous.”\n\n"
                else:
                    $ custom2 = ""
                if thyrsus_highisland_joined:
                    $ custom5 = "{color=#f6d6bd}Thyrsus{/color} wraps his creepers around his arms. “Don’t let me start. I’ve got {i}all{/i} the questions.”\n\n"
                else:
                    $ custom5 = ""
                if pyrrhos_highisland_joined:
                    $ custom6 = "“How about turning back?” murmurs {color=#f6d6bd}Pyrrhos{/color}.\n\n"
                else:
                    $ custom6 = ""
                if bandit_highisland_joined:
                    $ custom7 = "{color=#f6d6bd}The bandit{/color}, as clean-shaven as ever, looks in the distance. His chin is worthy of a statue.\n\n"
                else:
                    $ custom7 = ""
                if tulia_highisland_joined:
                    if dalit_highisland_joined:
                        $ custom8 = "“I should just become a mercenary, seeing how my recent seasons have been going,” {color=#f6d6bd}Tulia{/color} lets out a somewhat relieved sigh, then glances at {color=#f6d6bd}the huntress{/color}. “Aren’t you hiring at {color=#f6d6bd}Pelt{/color}?”\n\n"
                    else:
                        $ custom8 = "“I should just become a mercenary, seeing how my recent seasons have been going,” {color=#f6d6bd}Tulia{/color} lets out a somewhat relieved sigh. “Or an adventurer.”\n\n"
                else:
                    $ custom8 = ""
                if tzvi_highisland_joined:
                    $ custom9 = "{color=#f6d6bd}Tzvi{/color} covers himself with his black cloak tightly. “Who grabs the oars?”\n\n"
                else:
                    $ custom9 = ""
                if custom2 == "" and custom5 == "" and custom6 == "" and custom7 == "" and custom8 == "" and custom9 == "":
                    $ custom1 = "After a few silent moments, you adjust your axe and step forward. "
                else:
                    $ custom1 = ""
                if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                menu:
                    '[custom1][custom2][custom5][custom6][custom7][custom8][custom9]You get in the boat and grab the planks, not used to the swaying.
                    '
                    'I can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can do this.')
                        jump highisland_journey01
                    '{i}We{/i} can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {i}We{/i} can do this.')
                        jump highisland_journey01
                    'I ask my ancestors for guidance.' if pc_religion == "pagan" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask my ancestors for guidance.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'Time to row.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to row.')
                        jump highisland_journey01
            '“We’ve got a few rough hours ahead, but stick together, and we’re all going to make it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ve got a few rough hours ahead, but stick together, and we’re all going to make it.”')
                if dalit_highisland_joined:
                    $ custom2 = "“I han’t seen this much water, ever. It’s so loud, and angry.” {color=#f6d6bd}Dalit’s{/color} whisper addresses no one in particular.\n\n"
                else:
                    $ custom2 = ""
                if thyrsus_highisland_joined:
                    $ custom5 = "{color=#f6d6bd}Thyrsus{/color} wraps his creepers around his arms. “Don’t you worry. I’ll hold you tightly.”\n\n"
                else:
                    $ custom5 = ""
                if pyrrhos_highisland_joined:
                    $ custom6 = "“So now we {i}are{/i} aiming to survive all this?” murmurs {color=#f6d6bd}Pyrrhos{/color}.\n\n"
                else:
                    $ custom6 = ""
                if bandit_highisland_joined:
                    $ custom7 = "{color=#f6d6bd}The bandit{/color}, as clean-shaven as ever, smirks at the waves and sits down swiftly in the spot that’s the farthest away from the oars.\n\n"
                else:
                    $ custom7 = ""
                if tulia_highisland_joined:
                    if dalit_highisland_joined:
                        $ custom8 = "“I should just become a mercenary, seeing how my recent seasons have been going,” {color=#f6d6bd}Tulia{/color} lets out a somewhat relieved sigh, then glances at {color=#f6d6bd}the huntress{/color}. “Aren’t you hiring at {color=#f6d6bd}Pelt{/color}?”\n\n"
                    else:
                        $ custom8 = "“I should just become a mercenary, seeing how my recent seasons have been going,” {color=#f6d6bd}Tulia{/color} lets out a somewhat relieved sigh. “Or an adventurer.”\n\n"
                else:
                    $ custom8 = ""
                if tzvi_highisland_joined:
                    $ custom9 = "{color=#f6d6bd}Tzvi{/color} covers himself with his black cloak tightly. “Obviously. {i}Someone{/i} has to row back this toy.”\n\n"
                else:
                    $ custom9 = ""
                if custom2 == "" and custom5 == "" and custom6 == "" and custom7 == "" and custom8 == "" and custom9 == "":
                    $ custom1 = "After a few silent moments, you adjust your axe and step forward. "
                else:
                    $ custom1 = ""
                if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                menu:
                    '[custom1][custom2][custom5][custom6][custom7][custom8][custom9]You get in the boat and grab the planks, not used to the swaying.
                    '
                    'I can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can do this.')
                        jump highisland_journey01
                    '{i}We{/i} can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {i}We{/i} can do this.')
                        jump highisland_journey01
                    'I ask my ancestors for guidance.' if pc_religion == "pagan" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask my ancestors for guidance.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'Time to row.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to row.')
                        jump highisland_journey01
            'I clear my throat. “We’re heading into danger, but we’ll return as heroes!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clear my throat. “We’re heading into danger, but we’ll return as heroes!”')
                if dalit_highisland_joined:
                    $ custom2 = "{color=#f6d6bd}Dalit{/color} gives you a warm look, but then once again observes the waves crashing against the rocks. Since arriving here, she has seemed unusually worried.\n\n"
                else:
                    $ custom2 = ""
                if thyrsus_highisland_joined:
                    $ custom5 = "{color=#f6d6bd}Thyrsus{/color} wraps his creepers around his arms. “As if this place needs more of them.”\n\n"
                else:
                    $ custom5 = ""
                if pyrrhos_highisland_joined:
                    $ custom6 = "“Aye, aye. Be so nice and spare me this,” murmurs {color=#f6d6bd}Pyrrhos{/color}.\n\n"
                else:
                    $ custom6 = ""
                if bandit_highisland_joined:
                    $ custom7 = "{color=#f6d6bd}The bandit{/color}, as clean-shaven as ever, smirks at the waves and sits down swiftly in the spot that’s the farthest away from the oars.\n\n"
                else:
                    $ custom7 = ""
                if tulia_highisland_joined:
                    $ custom8 = "“Heroes, you say? Who am I, an adventurer?” {color=#f6d6bd}Tulia{/color} freezes, then lets out a gentle chuckle. “Well, seeing my last few seasons...”\n\n"
                else:
                    $ custom8 = ""
                if tzvi_highisland_joined:
                    $ custom9 = "{color=#f6d6bd}Tzvi{/color} covers himself with his black cloak tightly. “But are you brave enough to grab the oars, boss?”\n\n"
                else:
                    $ custom9 = ""
                if custom2 == "" and custom5 == "" and custom6 == "" and custom7 == "" and custom8 == "" and custom9 == "":
                    $ custom1 = "After a few silent moments, you adjust your axe and step forward. "
                else:
                    $ custom1 = ""
                if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                menu:
                    '[custom1][custom2][custom5][custom6][custom7][custom8][custom9]You get in the boat and grab the planks, not used to the swaying.
                    '
                    'I can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can do this.')
                        jump highisland_journey01
                    '{i}We{/i} can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {i}We{/i} can do this.')
                        jump highisland_journey01
                    'I ask my ancestors for guidance.' if pc_religion == "pagan" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask my ancestors for guidance.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'Time to row.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to row.')
                        jump highisland_journey01
            'No time for politeness. “Let’s get this done.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- No time for politeness. “Let’s get this done.”')
                menu:
                    'You get in the boat before anyone else, but then grab the planks, not used to the swaying.
                    '
                    'I can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can do this.')
                        jump highisland_journey01
                    '{i}We{/i} can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {i}We{/i} can do this.')
                        jump highisland_journey01
                    'I ask my ancestors for guidance.' if pc_religion == "pagan" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask my ancestors for guidance.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'Time to row.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to row.')
                        jump highisland_journey01

label highisland_journey_fishinghamletALL:
    label highisland_journey_fishinghamlet00:
        $ highisland_journey_inprogress = 1
        nvl clear
        $ pc_area = "fishinghamlet"
        stop music fadeout 4.0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show areapicture rockslidetofishinghamlet at basicfade
        play nature "audio/ambient/fishinghamlet01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        $ quarters = 84
        with Fade(1.8, 1.5, 1.8, color="#0f2a3f")
        if highisland_mode == "solo":
            jump highisland_journey_fishinghamlet_solo01
        if highisland_mode == "crew":
            jump highisland_journey_fishinghamlet_crew01

    label highisland_journey_fishinghamlet_solo01:
        $ quest_gatheracrew = 3
        $ renpy.notify("Quest completed: Gather a Crew")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Gather a Crew{/i}')
        menu:
            'You adjust your clothes, but even their second layer is barely enough to keep you warm in the breeze. There’s sand in your boots.
            \n\nStaring into the night, you take a deep breath of the chilling air, and listen to the roaring waves. The course ahead may be easy to remember, but all that you see are the teeth-like rocks, waiting to tear the planks of your boat apart, and the seagulls, roaming the beach in search of food.
            \n\n{color=#f6d6bd}Aegidia{/color} observes you from the end of the bridge, holding {color=#f6d6bd}[horsename]{/color} by the lead. She encouraged you to reconsider a lone expedition, but didn’t pressure you.
            '
            'I observe my companion for a bit more. Just in case.' if pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe my companion for a bit more. Just in case.')
                jump highisland_journey_fishinghamlet_solo02
            '“I’ll be back soon!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll be back soon!”')
                jump highisland_journey_fishinghamlet_solo02
            'The horse won’t even notice that I’m gone.' if not pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The horse won’t even notice that I’m gone.')
                jump highisland_journey_fishinghamlet_solo02
            'I’m leaving quite a fortune with this archeress.' if not pc_likeshorsename:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m leaving quite a fortune with this archeress.')
                label highisland_journey_fishinghamlet_solo02:
                    if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                        $ pc_faithpoints_opportunities += 1
                    menu:
                        'You throw the oars into the boat, followed by your modest equipment. As you sit down next to them, you hold the planks, not used to the swaying.
                        '
                        'At least I’ve got plenty of space for {color=#f6d6bd}Asterion{/color}.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- At least I’ve got plenty of space for {color=#f6d6bd}Asterion{/color}.')
                            jump highisland_journey01
                        'No one would be able to help me anyway.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- No one would be able to help me anyway.')
                            jump highisland_journey01
                        'Too bad I couldn’t trust anyone.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Too bad I couldn’t trust anyone.')
                            jump highisland_journey01
                        'I ask my ancestors for guidance.' if pc_religion == "pagan" or pc_religion == "unknown":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask my ancestors for guidance.')
                            $ pc_faithpoints += 1
                            jump highisland_journey01
                        'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
                            $ pc_faithpoints += 1
                            jump highisland_journey01
                        'It’s time to row.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s time to row.')
                            jump highisland_journey01

    label highisland_journey_fishinghamlet_crew01:
        $ quest_gatheracrew = 2
        $ renpy.notify("Quest completed: Gather a Crew")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Gather a Crew{/i}')
        if highisland_recruitment_option_aegidia:
            $ aegidia_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_dalit:
            $ dalit_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_efren:
            $ efren_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_navica:
            $ navica_highisland_joined = 1
        if highisland_recruitment_option_thyrsus:
            $ thyrsus_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_pyrrhos:
            $ pyrrhos_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_bandit:
            $ bandit_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_tulia:
            $ tulia_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_tzvi:
            $ tzvi_highisland_joined = 1
            $ highisland_crew_left += 1
        if highisland_recruitment_option_quintus:
            $ quintus_highisland_joined = 1
            $ highisland_crew_left += 1
        ##########
        if efren_highisland_joined:
            $ custom3 = ", unaware of {color=#f6d6bd}Efren’s{/color} hungry glances"
        else:
            $ custom3 = ""
        if navica_highisland_joined:
            $ custom4 = "You adjust your clothes, and thanks to the additional layer of a clothes and pants given to you by {color=#f6d6bd}Navica{/color}, you resist the breeze."
        else:
            $ custom4 = "You adjust your clothes, but even their second layer is barely enough to keep you warm in the breeze."
        if quintus_highisland_joined:
            $ custom10 = "{color=#f6d6bd}Quintus{/color} shoves"
        else:
            $ custom10 = "You and your companions shove"
        if aegidia_highisland_joined:
            $ custom1 = "is hidden inside {color=#f6d6bd}Aegidia’s{/color} cabin, but you doubt it’s going to have a good sleep"
        else:
            $ custom1 = "is at the end of the bridge, held by {color=#f6d6bd}Aegidia{/color}"
        menu:
            '[custom10] the boat into the water. You take a deep breath of the chilling air. [custom4] You stare into the night and listen to the roaring waves. The seagulls jump between the teeth-like rocks, seeking food and rest[custom3].
            \n\nYou look around. {color=#f6d6bd}[horsename]{/color} [custom1]. You turn toward the others.
            '
            '“If you’ve got any questions, now is a good moment to ask them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you’ve got any questions, now is a good moment to ask them.”')
                if dalit_highisland_joined:
                    $ custom2 = "“Is the water always so loud, and angry?” {color=#f6d6bd}Dalit{/color} addresses no one in particular. “Even if gorgeous.”\n\n"
                else:
                    $ custom2 = ""
                if thyrsus_highisland_joined:
                    $ custom5 = "{color=#f6d6bd}Thyrsus{/color} wraps his creepers around his arms. “Don’t let me start. I’ve got {i}all{/i} the questions.”\n\n"
                else:
                    $ custom5 = ""
                if pyrrhos_highisland_joined:
                    $ custom6 = "“How about turning back?” murmurs {color=#f6d6bd}Pyrrhos{/color}.\n\n"
                else:
                    $ custom6 = ""
                if bandit_highisland_joined:
                    $ custom7 = "{color=#f6d6bd}The bandit{/color}, as clean-shaven as ever, looks in the distance. His chin is worthy of a statue.\n\n"
                else:
                    $ custom7 = ""
                if tulia_highisland_joined:
                    if dalit_highisland_joined:
                        $ custom8 = "“I should just become a mercenary, seeing how my recent seasons have been going,” {color=#f6d6bd}Tulia{/color} lets out a somewhat relieved sigh, then glances at {color=#f6d6bd}the huntress{/color}. “Aren’t you hiring at {color=#f6d6bd}Pelt{/color}?”\n\n"
                    else:
                        $ custom8 = "“I should just become a mercenary, seeing how my recent seasons have been going,” {color=#f6d6bd}Tulia{/color} lets out a somewhat relieved sigh. “Or an adventurer.”\n\n"
                else:
                    $ custom8 = ""
                if tzvi_highisland_joined:
                    $ custom9 = "{color=#f6d6bd}Tzvi{/color} covers himself with his black cloak tightly. “Who grabs the oars?”\n\n"
                else:
                    $ custom9 = ""
                if custom2 == "" and custom5 == "" and custom6 == "" and custom7 == "" and custom8 == "" and custom9 == "":
                    $ custom1 = "After a few silent moments, you adjust your axe and step forward. "
                else:
                    $ custom1 = ""
                if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                menu:
                    '[custom1][custom2][custom5][custom6][custom7][custom8][custom9]You get in the boat and grab the planks, not used to the swaying.
                    '
                    'I can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can do this.')
                        jump highisland_journey01
                    '{i}We{/i} can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {i}We{/i} can do this.')
                        jump highisland_journey01
                    'I ask my ancestors for guidance.' if pc_religion == "pagan" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask my ancestors for guidance.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'Time to row.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to row.')
                        jump highisland_journey01
            '“We’ve got a few rough hours ahead, but stick together, and we’re all going to make it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We’ve got a few rough hours ahead, but stick together, and we’re all going to make it.”')
                if dalit_highisland_joined:
                    $ custom2 = "“I han’t seen this much water, ever. It’s so loud, and angry.” {color=#f6d6bd}Dalit’s{/color} whisper addresses no one in particular.\n\n"
                else:
                    $ custom2 = ""
                if thyrsus_highisland_joined:
                    $ custom5 = "{color=#f6d6bd}Thyrsus{/color} wraps his creepers around his arms. “Don’t you worry. I’ll hold you tightly.”\n\n"
                else:
                    $ custom5 = ""
                if pyrrhos_highisland_joined:
                    $ custom6 = "“So now we {i}are{/i} aiming to survive all this?” murmurs {color=#f6d6bd}Pyrrhos{/color}.\n\n"
                else:
                    $ custom6 = ""
                if bandit_highisland_joined:
                    $ custom7 = "{color=#f6d6bd}The bandit{/color}, as clean-shaven as ever, smirks at the waves and sits down swiftly in the spot that’s the farthest away from the oars.\n\n"
                else:
                    $ custom7 = ""
                if tulia_highisland_joined:
                    if dalit_highisland_joined:
                        $ custom8 = "“I should just become a mercenary, seeing how my recent seasons have been going,” {color=#f6d6bd}Tulia{/color} lets out a somewhat relieved sigh, then glances at {color=#f6d6bd}the huntress{/color}. “Aren’t you hiring at {color=#f6d6bd}Pelt{/color}?”\n\n"
                    else:
                        $ custom8 = "“I should just become a mercenary, seeing how my recent seasons have been going,” {color=#f6d6bd}Tulia{/color} lets out a somewhat relieved sigh. “Or an adventurer.”\n\n"
                else:
                    $ custom8 = ""
                if tzvi_highisland_joined:
                    $ custom9 = "{color=#f6d6bd}Tzvi{/color} covers himself with his black cloak tightly. “Obviously. {i}Someone{/i} has to row back this toy.”\n\n"
                else:
                    $ custom9 = ""
                if custom2 == "" and custom5 == "" and custom6 == "" and custom7 == "" and custom8 == "" and custom9 == "":
                    $ custom1 = "After a few silent moments, you adjust your axe and step forward. "
                else:
                    $ custom1 = ""
                if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                menu:
                    '[custom1][custom2][custom5][custom6][custom7][custom8][custom9]You get in the boat and grab the planks, not used to the swaying.
                    '
                    'I can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can do this.')
                        jump highisland_journey01
                    '{i}We{/i} can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {i}We{/i} can do this.')
                        jump highisland_journey01
                    'I ask my ancestors for guidance.' if pc_religion == "pagan" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask my ancestors for guidance.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'Time to row.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to row.')
                        jump highisland_journey01
            'I clear my throat. “We’re heading into danger, but we’ll return as heroes!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clear my throat. “We’re heading into danger, but we’ll return as heroes!”')
                if dalit_highisland_joined:
                    $ custom2 = "{color=#f6d6bd}Dalit{/color} gives you a warm look, but then once again observes the waves crushing the rocks. Since arriving here, she has seemed unusually worried.\n\n"
                else:
                    $ custom2 = ""
                if thyrsus_highisland_joined:
                    $ custom5 = "{color=#f6d6bd}Thyrsus{/color} wraps his creepers around his arms. “As if this place needs more of them.”\n\n"
                else:
                    $ custom5 = ""
                if pyrrhos_highisland_joined:
                    $ custom6 = "“Aye, aye. Be so nice and spare me this,” murmurs {color=#f6d6bd}Pyrrhos{/color}.\n\n"
                else:
                    $ custom6 = ""
                if bandit_highisland_joined:
                    $ custom7 = "{color=#f6d6bd}The bandit{/color}, as clean-shaven as ever, smirks at the waves and sits down swiftly in the spot that’s the farthest away from the oars.\n\n"
                else:
                    $ custom7 = ""
                if tulia_highisland_joined:
                    $ custom8 = "“Heroes, you say? Who am I, an adventurer?” {color=#f6d6bd}Tulia{/color} freezes, then lets out a gentle chuckle. “Well, seeing my last few seasons...”\n\n"
                else:
                    $ custom8 = ""
                if tzvi_highisland_joined:
                    $ custom9 = "{color=#f6d6bd}Tzvi{/color} covers himself with his black cloak tightly. “But are you brave enough to grab the oars, boss?”\n\n"
                else:
                    $ custom9 = ""
                if custom2 == "" and custom5 == "" and custom6 == "" and custom7 == "" and custom8 == "" and custom9 == "":
                    $ custom1 = "After a few silent moments, you adjust your axe and step forward. "
                else:
                    $ custom1 = ""
                if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                menu:
                    '[custom1][custom2][custom5][custom6][custom7][custom8][custom9]You get in the boat and grab the planks, not used to the swaying.
                    '
                    'I can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can do this.')
                        jump highisland_journey01
                    '{i}We{/i} can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {i}We{/i} can do this.')
                        jump highisland_journey01
                    'I ask my ancestors for guidance.' if pc_religion == "pagan" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask my ancestors for guidance.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'Time to row.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to row.')
                        jump highisland_journey01
            'No time for politeness. “Let’s get this done.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- No time for politeness. “Let’s get this done.”')
                menu:
                    'You get in the boat before anyone else, but then grab the planks, not used to the swaying.
                    '
                    'I can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can do this.')
                        jump highisland_journey01
                    '{i}We{/i} can do this.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {i}We{/i} can do this.')
                        jump highisland_journey01
                    'I ask my ancestors for guidance.' if pc_religion == "pagan" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask my ancestors for guidance.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
                        $ pc_faithpoints += 1
                        jump highisland_journey01
                    'Time to row.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to row.')
                        jump highisland_journey01

### Sea Travel
label highisland_journey01:
    nvl clear
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ can_potions = 1
    $ pc_area = 0
    stop music fadeout 4.0
    play nature "audio/ambient/highisland01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if highisland_journey_startingpoint == "hamlet":
        $ pc_area = "sea_south1"
        show areapicture hi_sea_south1 at basicfade
        with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
    if highisland_journey_startingpoint == "beach":
        $ pc_area = "sea_north1"
        show areapicture hi_sea_north1 at basicfade
        with Fade(1.0, 0.75, 1.0, color="#0f2a3f")
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ renpy.save("combatsave", extra_info='Combat Auto Save')
    if highisland_mode == "solo":
        if persistent.deafmode:
            $ deafcustom1 = "You try to ignore the screeches of the beasts circling above you, the creaking boards, the angry tide, but you can’t hope for as much as a moment of silence."
        else:
            $ deafcustom1 = ""
        menu:
            'The first few minutes are the slowest. You push off the sharp rocks with the oars, and even your arms, but the restless waves charge at the boat, again and again. Above the dark salty waters, through the bright night, you can see the outline of {color=#f6d6bd}High Island{/color}.
            \n\nYou get used to the rhythm of rowing. [deafcustom1]
            '
            'My hands are getting cold.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My hands are getting cold.')
                jump highisland_solo_ocean01
    if highisland_mode == "howlers":
        if persistent.deafmode:
            $ deafcustom1 = "You try to ignore the screeches of the beasts circling above you, the creaking boards, the angry tide, but you can’t hope for as much as a moment of silence.\n\n"
        else:
            $ deafcustom1 = ""
        menu:
            'The first few minutes are the slowest. You push off the sharp rocks with the oars, and even your arms, but the restless waves charge at the boat, again and again. Above the dark salty waters, through the bright night, you can see the outline of {color=#f6d6bd}High Island{/color}.
            \n\nYou get used to the rhythm of rowing. [deafcustom1]The guards exchange a few words between themselves, but they mostly ignore your presence.
            '
            'My hands are getting cold.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My hands are getting cold.')
                jump highisland_howlers_ocean01
    if highisland_mode == "crew":
        if persistent.deafmode:
            $ deafcustom1 = "You try to ignore the screeches of the beasts circling above you, the creaking boards, the angry tide, but you can’t hope for as much as a moment of silence.\n\n"
        else:
            $ deafcustom1 = ""
        menu:
            'The first few minutes are the slowest. You push off the sharp rocks with the oars, and even your arms, but the restless waves charge at the boat, again and again. Above the dark salty waters, through the bright night, you can see the outline of {color=#f6d6bd}High Island{/color}.
            \n\nYou get used to the rhythm of rowing. [deafcustom1]Your allies are focused on the struggle at hand.
            '
            'Rowing will be harsh. Better to take turns.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Rowing will be harsh. Better to take turns.')
                jump highisland_crew_ocean01

label highisland_oceanALL:
    label highisland_solo_oceanALL:
        label highisland_solo_ocean01:
            $ can_items = 0
            $ can_potions = 0
            $ at = 0
            $ at_unlock_spell = 0
            if pc_class == "mage" and not highisland_harpies_magicused:
                $ at_unlock_spell = 1
                $ manacost = 3
            menu:
                'The waves in the deeper waters get tall enough to splash your lips. That’s when the harpies take their chance - the pack, a few monsters strong, lowers their flight, seeking an opportunity to strike.
                \n\nTheir fluttering, bat-like wings try to oppose the wind. The creatures are smaller than goblins, with ape-like features and talons that make you think of a parrot. It’s too dark to tell the color of their fur.
                '
                'Time for my crossbow.' if item_crossbow and item_crossbowquarrels >= 1 and not highisland_harpies_crossbowused:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for my crossbow.')
                    $ highisland_harpies_crossbowused += 1
                    if highisland_harpies_hp == 4:
                        $ custom1 = "After your quarrel hits a harpy’s hip, the creature tries to fly for a bit longer, but soon crashes into the water and disappears beneath the surface. The other beasts, confused at first, get even closer."
                    else:
                        $ custom1 = "After your quarrel hits a harpy’s hip, the creature tries to fly for a bit longer, but soon crashes into the water and disappears beneath the surface."
                    $ highisland_harpies_hp -= 1
                    $ item_crossbowquarrels -= 1
                    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                    jump highisland_solo_ocean02
                '{image=d6} I don’t have much time, but I reload and shoot.' if item_crossbow and item_crossbowquarrels >= 1 and highisland_harpies_crossbowused == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I don’t have much time, but I reload and shoot.')
                    $ highisland_harpies_crossbowused += 1
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
                    if d100roll <= 60:
                        $ custom1 = "The quarrel rips a hole in the leathery wing of one of the creatures. After a few moments of trying to stay in one spot, it clumsily flies away."
                        $ highisland_harpies_hp -= 1
                    else:
                        $ custom1 = "You pull the trigger just as the rocking boat makes you lose balance. The quarrel disappears in the darkness."
                    $ item_crossbowquarrels -= 1
                    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                    jump highisland_solo_ocean02
                'I lack any quarrels. (disabled)' if item_crossbow and not item_crossbowquarrels and highisland_harpies_crossbowused < 2:
                    pass
                'I don’t have a crossbow. (disabled)' if not item_crossbow:
                    pass
                'I grab my wand. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not highisland_harpies_magicused" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my wand.')
                    $ highisland_harpies_magicused += 1
                    $ mana = limit_mana(mana-manacost)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                    $ custom1 = "The invisible blast hits one of the beasts mid-flight, sending it into the sea. After a few moments, it shows up on the surface, using its wings to swim away."
                    $ highisland_harpies_hp -= 1
                    jump highisland_solo_ocean02
                'I lack pneuma to hit them with a spell. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and not highisland_harpies_magicused" ):
                    pass
                'I throw a fistful of blinding powder at them.' if item_blindingpowder and not highisland_harpies_blindingpowder:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw a fistful of blinding powder at them.')
                    $ highisland_harpies_blindingpowder += 1
                    $ custom1 = "Struggling to find your balance, you barely manage to send the panicking creature into the boat’s floor. During the precious few heartbeats, you grab your knife and lacerate the beast’s throat."
                    $ highisland_harpies_hp -= 1
                    jump highisland_solo_ocean02
                'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                    pass
                '{image=d6} I grab my spear and prepare myself to strike the closest target.' if item_asterionspear or item_mountainroadspear:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my spear and prepare myself to strike the closest target.')
                    $ custom1 = "Having the range advantage helps you tear through the first wing."
                    jump highisland_solo_ocean03
                '{image=d6} I grab my axe and prepare myself to strike the closest target.' if not item_asterionspear and not item_mountainroadspear:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my axe and prepare myself to strike the closest target.')
                    $ custom1 = "It’s not easy to hold your stance when the “ground” keeps moving."
                    jump highisland_solo_ocean03

        label highisland_solo_ocean02:
            stop nature fadeout 4.0
            $ at = 0
            $ at_unlock_spell = 0
            if not renpy.music.get_playing(channel='music') == "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg":
                play music "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg" fadeout 1.0 fadein 1.0
            $ at = 0
            $ at_unlock_spell = 0
            if highisland_harpies_hp:
                if pc_class == "mage" and not highisland_harpies_magicused:
                    $ at_unlock_spell = 1
                    $ manacost = 3
                menu:
                    '[custom1]
                    '
                    'Time for my crossbow.' if item_crossbow and item_crossbowquarrels >= 1 and not highisland_harpies_crossbowused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for my crossbow.')
                        $ highisland_harpies_crossbowused += 1
                        if highisland_harpies_hp == 4:
                            $ custom1 = "After your quarrel hits a harpy’s hip, the creature tries to fly for a bit longer, but soon crashes into the water and disappears beneath the surface. The other beasts, confused at first, get even closer."
                        else:
                            $ custom1 = "After your quarrel hits a harpy’s hip, the creature tries to fly for a bit longer, but soon crashes into the water and disappears beneath the surface."
                        $ highisland_harpies_hp -= 1
                        $ item_crossbowquarrels -= 1
                        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                        jump highisland_solo_ocean02
                    '{image=d6} I don’t have much time, but I reload and shoot.' if item_crossbow and item_crossbowquarrels >= 1 and highisland_harpies_crossbowused == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I don’t have much time, but I reload and shoot.')
                        $ highisland_harpies_crossbowused += 1
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
                        if d100roll <= 60:
                            $ custom1 = "The quarrel rips a hole in the leathery wing of one of the creatures. After a few moments of trying to stay in one spot, it clumsily flies away."
                            $ highisland_harpies_hp -= 1
                        else:
                            $ custom1 = "You pull the trigger just as the rocking boat makes you lose balance. The quarrel disappears in the darkness."
                        $ item_crossbowquarrels -= 1
                        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                        jump highisland_solo_ocean02
                    'I lack any quarrels. (disabled)' if item_crossbow and not item_crossbowquarrels and highisland_harpies_crossbowused < 2:
                        pass
                    'I don’t have a crossbow. (disabled)' if not item_crossbow:
                        pass
                    'I grab my wand. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not highisland_harpies_magicused" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my wand.')
                        $ highisland_harpies_magicused += 1
                        $ mana = limit_mana(mana-manacost)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                        $ custom1 = "The invisible blast hits one of the beasts mid-flight, sending it into the sea. After a few moments, it shows up on the surface, using its wings to swim away."
                        $ highisland_harpies_hp -= 1
                        jump highisland_solo_ocean02
                    'I lack pneuma to hit them with a spell. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and not highisland_harpies_magicused" ):
                        pass
                    'I throw a fistful of blinding powder at them.' if item_blindingpowder and not highisland_harpies_blindingpowder:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw a fistful of blinding powder at them.')
                        $ highisland_harpies_blindingpowder += 1
                        $ custom1 = "Struggling to find your balance, you barely manage to send the panicking creature into the boat’s floor. During the precious few heartbeats, you grab your knife and lacerate the beast’s throat."
                        $ highisland_harpies_hp -= 1
                        jump highisland_solo_ocean02
                    'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                        pass
                    '{image=d6} I grab my spear and prepare myself to strike the closest target.' if item_asterionspear or item_mountainroadspear:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my spear and prepare myself to strike the closest target.')
                        $ custom1 = "Having the range advantage helps you tear through the first wing."
                        jump highisland_solo_ocean03
                    '{image=d6} I grab my axe and prepare myself to strike the closest target.' if not item_asterionspear and not item_mountainroadspear:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my axe and prepare myself to strike the closest target.')
                        $ custom1 = "It’s not easy to hold your stance when the “ground” keeps moving."
                        jump highisland_solo_ocean03
            else:
                menu:
                    '[custom1]
                    \n\nThe remaining members of the pack take no more chances. They spread in various directions, seeking shelter among the tusk-like rocks.
                    '
                    'I take a deep breath and row ahead.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a deep breath and row ahead.')
                        jump highisland_afterharpies01

        label highisland_solo_ocean03:
            $ at = 0
            $ at_unlock_spell = 0
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg":
                play music "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg" fadeout 1.0 fadein 1.0
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
            if item_asterionspear or item_mountainroadspear:
                $ d100roll -= 20
            elif item_axe03:
                $ d100roll -= 15
            elif item_axe02 or item_axe02alt:
                $ d100roll -= 5
            $ d100roll += (highisland_harpies_hp*30)
            if d100roll <= 50:
                menu:
                    '[custom1] The gambeson on your arm stops the talons as you swing your blade and clenched fist. The harpies focus on your face, but neither their strength, nor their numbers, can make up for their predictability. After a few breaths, the scattered pack seeks shelter among the rocks. You put your bloodied hand in the chilling water.
                    '
                    'I adjust my cloak and row ahead.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I adjust my cloak and row ahead.')
                        jump highisland_afterharpies01
            else:
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
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-2)
                    show minus2hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                    if not cleanliness_clothes_torn:
                        $ cleanliness_clothes_torn = 1
                        show minus1appearance at appearancechange onlayer myoverlay
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                else:
                    $ custom1 = "The gambeson on your arm fails to stop the talons as you swing your blade and clenched fist desperately. The harpies focus on your face, and you can’t outmatch their overwhelming numbers. After a few breaths, the blood running from your empty eye sockets mixes with the salt water."
                    jump highisland_gameover
                menu:
                    '[custom1] The gambeson on your arm fails to stop the talons as you swing your blade and clenched fist desperately. The harpies try to focus on your face, but neither their strength, nor numbers, can make up for their predictability. After a few breaths, the scattered pack seeks shelter among the rocks.
                    '
                    'Gasping for air, I row ahead.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Gasping for air, I row ahead.')
                        jump highisland_afterharpies01

    label highisland_howlers_oceanALL:
        label highisland_howlers_ocean01:
            $ can_items = 0
            $ can_potions = 0
            $ highisland_harpies_hp -= 1
            $ at = 0
            $ at_unlock_spell = 0
            if pc_class == "mage" and not highisland_harpies_magicused:
                $ at_unlock_spell = 1
                $ manacost = 3
            menu:
                'The waves in the deeper waters get tall enough to splash your lips. That’s when the harpies take their chance - the pack, a few monsters strong, lowers their flight, seeking an opportunity to strike.
                \n\nTheir fluttering, bat-like wings try to oppose the wind. The creatures are smaller than goblins, with ape-like features and talons that make you think of a parrot. It’s too dark to tell the color of their fur.
                \n\nYour crew prepares their blades, while {color=#f6d6bd}the one with the bow{/color} shoots at the closest creature, sticking an arrow in its leg. It lets out a shriek, then flies away, toward the rocks. The other beasts, confused at first, get even closer.
                '
                'Time for my crossbow.' if item_crossbow and item_crossbowquarrels >= 1 and not highisland_harpies_crossbowused:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for my crossbow.')
                    $ highisland_harpies_crossbowused += 1
                    $ custom1 = "After your quarrel hits a harpy’s hip, the creature tries to fly for a bit longer, but soon crashes into the water and disappears beneath the surface. One of the animals tries to reach you, but gets scared off by the vigilant spearwoman."
                    $ highisland_harpies_hp -= 1
                    $ item_crossbowquarrels -= 1
                    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                    jump highisland_howlers_ocean02
                '{image=d6} I don’t have much time, but I reload and shoot.' if item_crossbow and item_crossbowquarrels >= 1 and highisland_harpies_crossbowused == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I don’t have much time, but I reload and shoot.')
                    $ highisland_harpies_crossbowused += 1
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
                    if d100roll <= 60:
                        $ custom1 = "The quarrel rips a hole in the leathery wing of one of the creatures. After a few moments of trying to stay in one spot, it clumsily flies away."
                        $ highisland_harpies_hp -= 1
                    else:
                        $ custom1 = "You pull the trigger just as the rocking boat makes you lose balance. The quarrel disappears in the darkness. {color=#f6d6bd}The one with a mace{/color} scoffs, but says nothing."
                    $ item_crossbowquarrels -= 1
                    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                    jump highisland_howlers_ocean02
                'I lack any quarrels. (disabled)' if item_crossbow and not item_crossbowquarrels and highisland_harpies_crossbowused < 2:
                    pass
                'I don’t have a crossbow. (disabled)' if not item_crossbow:
                    pass
                'I grab my wand. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not highisland_harpies_magicused" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my wand.')
                    $ highisland_harpies_magicused += 1
                    $ mana = limit_mana(mana-manacost)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                    $ custom1 = "The invisible blast hits one of the beasts mid-flight, sending it into the sea. After a few moments, it shows up on the surface, using its wings to swim away. {color=#f6d6bd}The young druid{/color} gives you a curious look, but says nothing."
                    $ highisland_harpies_hp -= 1
                    jump highisland_howlers_ocean02
                'I lack pneuma to hit them with a spell. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and not highisland_harpies_magicused" ):
                    pass
                'I throw a fistful of blinding powder at them.' if item_blindingpowder and not highisland_harpies_blindingpowder:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw a fistful of blinding powder at them.')
                    $ highisland_harpies_blindingpowder += 1
                    $ custom1 = "Struggling to find your balance, you barely manage to send the panicking creature into the boat’s floor. During the precious few heartbeats, one of the guards chops off the beast’s neck."
                    $ highisland_harpies_hp -= 1
                    jump highisland_howlers_ocean02
                'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                    pass
                '{image=d6} I grab my spear.' if item_asterionspear or item_mountainroadspear:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my spear.')
                    $ custom1 = "Having the range advantage helps you tear through the first wing."
                    jump highisland_howlers_ocean03
                '{image=d6} I grab my axe.' if not item_asterionspear and not item_mountainroadspear:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my axe.')
                    $ custom1 = "It’s not easy to hold your stance when the “ground” keeps moving."
                    jump highisland_howlers_ocean03

        label highisland_howlers_ocean02:
            $ at = 0
            $ at_unlock_spell = 0
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg":
                play music "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg" fadeout 1.0 fadein 1.0
            $ at = 0
            $ at_unlock_spell = 0
            if highisland_harpies_hp:
                if pc_class == "mage" and not highisland_harpies_magicused:
                    $ at_unlock_spell = 1
                    $ manacost = 3
                menu:
                    '[custom1]
                    '
                    'Time for my crossbow.' if item_crossbow and item_crossbowquarrels >= 1 and not highisland_harpies_crossbowused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for my crossbow.')
                        $ highisland_harpies_crossbowused += 1
                        $ custom1 = "After your quarrel hits a harpy’s hip, the creature tries to fly for a bit longer, but soon crashes into the water and disappears beneath the surface. One of the animals tries to reach you, but gets scared off by the vigilant spearwoman."
                        $ highisland_harpies_hp -= 1
                        $ item_crossbowquarrels -= 1
                        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                        jump highisland_howlers_ocean02
                    '{image=d6} I don’t have much time, but I reload and shoot.' if item_crossbow and item_crossbowquarrels >= 1 and highisland_harpies_crossbowused == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I don’t have much time, but I reload and shoot.')
                        $ highisland_harpies_crossbowused += 1
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
                        if d100roll <= 60:
                            $ custom1 = "The quarrel rips a hole in the leathery wing of one of the creatures. After a few moments of trying to stay in one spot, it clumsily flies away."
                            $ highisland_harpies_hp -= 1
                        else:
                            $ custom1 = "You pull the trigger just as the rocking boat makes you lose balance. The quarrel disappears in the darkness. {color=#f6d6bd}The one with a mace{/color} scoffs, but says nothing."
                        $ item_crossbowquarrels -= 1
                        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                        jump highisland_howlers_ocean02
                    'I lack any quarrels. (disabled)' if item_crossbow and not item_crossbowquarrels and highisland_harpies_crossbowused < 2:
                        pass
                    'I don’t have a crossbow. (disabled)' if not item_crossbow:
                        pass
                    'I grab my wand. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not highisland_harpies_magicused" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my wand.')
                        $ highisland_harpies_magicused += 1
                        $ mana = limit_mana(mana-manacost)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                        $ custom1 = "The invisible blast hits one of the beasts mid-flight, sending it into the sea. After a few moments, it shows up on the surface, using its wings to swim away. {color=#f6d6bd}The young druid{/color} gives you a curious look, but says nothing."
                        $ highisland_harpies_hp -= 1
                        jump highisland_howlers_ocean02
                    'I lack pneuma to hit them with a spell. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and not highisland_harpies_magicused" ):
                        pass
                    'I throw a fistful of blinding powder at them.' if item_blindingpowder and not highisland_harpies_blindingpowder:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw a fistful of blinding powder at them.')
                        $ highisland_harpies_blindingpowder += 1
                        $ custom1 = "Struggling to find your balance, you barely manage to send the panicking creature into the boat’s floor. During the precious few heartbeats, one of the guards chops off the beast’s neck."
                        $ highisland_harpies_hp -= 1
                        jump highisland_howlers_ocean02
                    'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                        pass
                    '{image=d6} I grab my spear.' if item_asterionspear or item_mountainroadspear:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my spear.')
                        $ custom1 = "Having the range advantage helps you tear through the first wing."
                        jump highisland_howlers_ocean03
                    '{image=d6} I grab my axe.' if not item_asterionspear and not item_mountainroadspear:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my axe.')
                        $ custom1 = "It’s not easy to hold your stance when the “ground” keeps moving."
                        jump highisland_howlers_ocean03
            else:
                menu:
                    '[custom1]
                    \n\nThe remaining members of the pack take no more chances. They spread in various directions, seeking shelter among the tusk-like rocks.
                    '
                    '“Great job, everyone.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Great job, everyone.”')
                        jump highisland_afterharpies01
                    '“Well, still alive!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, still alive!”')
                        jump highisland_afterharpies01
                    'I stare in the distance.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stare in the distance.')
                        jump highisland_afterharpies01

        label highisland_howlers_ocean03:
            $ at = 0
            $ at_unlock_spell = 0
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg":
                play music "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg" fadeout 1.0 fadein 1.0
            if highisland_harpies_hp <= 2:
                menu:
                    '[custom1] The gambeson on your arm stops the talons as you swing your blade and clenched fist. {color=#f6d6bd}The guards{/color} could stand against a well-trained squad - they stay side-by-side, asking for help or barking out vague commands so quickly you’re not sure what they even mean.
                    \n\nAfter a few breaths, the scattered pack seeks shelter among the rocks. You put your bloodied hand in the freezing water.
                    '
                    '“Well, still alive!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, still alive!”')
                        jump highisland_afterharpies01
                    'I stare in the distance.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stare in the distance.')
                        jump highisland_afterharpies01
            else:
                $ highisland_howlersguards_hp -= 1
                menu:
                    '[custom1] The gambeson on your arm stops the talons as you swing your blade and clenched fist. {color=#f6d6bd}The guards{/color} could stand against a well-trained squad - they stay side-by-side, asking for help or barking out vague commands so quickly you’re not sure what they even mean.
                    \n\nAfter a few breaths, the scattered pack seeks shelter among the rocks. Only one of the fighters was scratched during the onslaught, and even though she throws you angry glances, she simply starts to wash her wound, asking her companions for a bandage.
                    '
                    '“Well, still alive!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, still alive!”')
                        jump highisland_afterharpies01
                    'I stare in the distance.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stare in the distance.')
                        jump highisland_afterharpies01

    label highisland_crew_oceanALL:
        label highisland_crew_ocean01:
            $ can_items = 0
            $ can_potions = 0
            $ at = 0
            $ at_unlock_spell = 0
            if pc_class == "mage" and not highisland_harpies_magicused:
                $ at_unlock_spell = 1
                $ manacost = 3
            menu:
                'The waves in the deeper waters get tall enough to splash your lips. That’s when the harpies take their chance - the pack, a few monsters strong, lowers their flight, seeking an opportunity to strike.
                \n\nTheir fluttering, bat-like wings try to oppose the wind. The creatures are smaller than goblins, with ape-like features and talons that make you think of a parrot. It’s too dark to tell the color of their fur.
                '
                '“If you can - shoot them!”' if (aegidia_highisland_joined and not aegidia_highisland_blocked and not highisland_harpies_crewused) or (dalit_highisland_joined and not dalit_highisland_blocked and not highisland_harpies_crewused) or (pyrrhos_highisland_joined and not pyrrhos_highisland_blocked and not highisland_harpies_crewused):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you can - shoot them!”')
                    $ custom2 = ""
                    $ highisland_harpies_crewused += 1
                    if aegidia_highisland_joined and dalit_highisland_joined and pyrrhos_highisland_joined:
                        $ highisland_harpies_hp -= 4
                        $ custom1 = "{color=#f6d6bd}Aegidia’s{/color} arrows cause havoc, and keep you safe for another few breaths. The shells of harpies hit the water, only to get dragged away by the waves.\n\n{color=#f6d6bd}Dalit{/color} releases only one quarrel before she reaches for an axe, but her powerful shot tears off a harpy’s head. The dead shell sinks like a rock.\n\n{color=#f6d6bd}Pyrrhos’{/color} first shot misses, but he reloads his crossbow with sheer strength, releasing the second quarrel soon after. After his target loses its paw, it screeches in pain and attempts to flee, ignoring the dark blood dripping from its stump."
                    elif aegidia_highisland_joined and dalit_highisland_joined:
                        $ highisland_harpies_hp -= 3
                        $ custom1 = "{color=#f6d6bd}Aegidia’s{/color} arrows cause havoc, and keep you safe for another few breaths. The shells of harpies hit the water, only to get dragged away by the waves.\n\n{color=#f6d6bd}Dalit{/color} releases only one quarrel before she reaches for an axe, but her powerful shot tears off a harpy’s head. The dead shell sinks like a rock."
                    elif aegidia_highisland_joined and pyrrhos_highisland_joined:
                        $ highisland_harpies_hp -= 3
                        $ custom1 = "{color=#f6d6bd}Aegidia’s{/color} arrows cause havoc, and keep you safe for another few breaths. The shells of harpies hit the water, only to get dragged away by the waves.\n\n"
                    elif dalit_highisland_joined and pyrrhos_highisland_joined:
                        $ highisland_harpies_hp -= 2
                        $ custom1 = "The quarrels shot by {color=#f6d6bd}Dalit{/color} and {color=#f6d6bd}Pyrrhos{/color} keep you safe for another few breaths. The shells of harpies hit the water, only to get dragged away by the waves.\n\n{color=#f6d6bd}Pyrrhos’{/color} first shot misses, but he reloads his crossbow with sheer strength, releasing the second quarrel soon after. After his target loses its paw, it screeches in pain and attempts to flee, ignoring the dark blood dripping from its stump."
                    elif aegidia_highisland_joined:
                        $ highisland_harpies_hp -= 2
                        $ custom1 = "{color=#f6d6bd}Aegidia’s{/color} arrows cause havoc, and keep you safe for another few breaths. The shells of harpies hit the water, only to get dragged away by the waves."
                    elif dalit_highisland_joined:
                        $ highisland_harpies_hp -= 1
                        $ custom1 = "{color=#f6d6bd}Dalit{/color} releases only one quarrel before she reaches for an axe, but her powerful shot tears off a harpy’s head. The dead shell sinks like a rock."
                    elif pyrrhos_highisland_joined:
                        $ highisland_harpies_hp -= 1
                        $ custom1 = "{color=#f6d6bd}Pyrrhos’{/color} first shot misses, but he reloads his crossbow with sheer strength, releasing the second quarrel soon after. After his target loses its paw, it screeches in pain and attempts to flee, ignoring the dark blood dripping from its stump."
                    jump highisland_crew_ocean02
                'Time for my crossbow.' if item_crossbow and item_crossbowquarrels >= 1 and not highisland_harpies_crossbowused:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for my crossbow.')
                    $ highisland_harpies_crossbowused += 1
                    $ custom2 = ""
                    if highisland_harpies_hp == 4:
                        $ custom1 = "After your quarrel hits a harpy’s hip, the creature tries to fly for a bit longer, but soon crashes into the water and disappears beneath the surface. The other beasts, confused at first, get even closer."
                    else:
                        $ custom1 = "After your quarrel hits a harpy’s hip, the creature tries to fly for a bit longer, but soon crashes into the water and disappears beneath the surface."
                    $ highisland_harpies_hp -= 1
                    $ item_crossbowquarrels -= 1
                    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                    if dalit_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Dalit{/color} turns toward you with a quarrel in her teeth, which makes her look like she’s grinning widely."
                    elif pyrrhos_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Pyrrhos{/color} lets out a chuckle."
                    elif quintus_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Quintus{/color} tries to nudge you with his shoulder, but almost falls overboard."
                    else:
                        $ custom2 = ""
                    jump highisland_crew_ocean02
                '{image=d6} I don’t have much time, but I reload and shoot.' if item_crossbow and item_crossbowquarrels >= 1 and highisland_harpies_crossbowused == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I don’t have much time, but I reload and shoot.')
                    $ custom2 = ""
                    $ highisland_harpies_crossbowused += 1
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
                    if d100roll <= 60:
                        $ custom1 = "The quarrel rips a hole in the leathery wing of one of the creatures. After a few moments of trying to stay in one spot, it clumsily flies away."
                        $ highisland_harpies_hp -= 1
                    else:
                        $ custom1 = "You pull the trigger just as the rocking boat makes you lose balance. The quarrel disappears in the darkness."
                        if tzvi_highisland_joined:
                            $ custom2 = "“Careful,” growls {color=#f6d6bd}Tzvi{/color}."
                        elif aegidia_highisland_joined:
                            $ custom2 = "“Look out,” shouts {color=#f6d6bd}Aegidia{/color}."
                        elif efren_highisland_joined:
                            $ custom2 = "{color=#f6d6bd}Efren{/color} observes you for a bit, then sighs with relief."
                        elif tulia_highisland_joined:
                            $ custom2 = "{color=#f6d6bd}Tulia{/color} gives you an encouraging smile."
                        elif quintus_highisland_joined:
                            $ custom2 = "{color=#f6d6bd}Quintus{/color} grabs your shoulder, helping you find your balance."
                        elif dalit_highisland_joined:
                            $ custom2 = "{color=#f6d6bd}Dalit{/color} gives you an encouraging smile."
                        else:
                            $ custom2 = ""
                    $ item_crossbowquarrels -= 1
                    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                    jump highisland_crew_ocean02
                'I lack any quarrels. (disabled)' if item_crossbow and not item_crossbowquarrels and highisland_harpies_crossbowused < 2:
                    pass
                'I don’t have a crossbow. (disabled)' if not item_crossbow:
                    pass
                'I grab my wand. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not highisland_harpies_magicused" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my wand.')
                    $ custom2 = ""
                    $ highisland_harpies_magicused += 1
                    $ mana = limit_mana(mana-manacost)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                    $ custom1 = "The invisible blast hits one of the beasts mid-flight, sending it into the sea. After a few moments, it shows up on the surface, using its wings to swim away."
                    if thyrsus_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Thyrsus{/color} gives you a surprised, but approving look."
                    elif bandit_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}The bandit{/color} gives you a suspicious look."
                    elif navica_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Navica’s{/color} eyes widen."
                    elif aegidia_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Aegidia{/color} gives you a surprised, but approving look."
                    elif dalit_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Dalit{/color} gives you a surprised, but approving look."
                    elif efren_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Efren{/color} gives you a surprised, but approving look."
                    elif pyrrhos_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Pyrrhos{/color} gives you a suspicious look."
                    elif tulia_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Tulia{/color} gives you a surprised, but approving look."
                    elif tzvi_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Tzvi{/color} gives you a suspicious look."
                    elif quintus_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Quintus{/color} gives you a radiant smile."
                    else:
                        $ custom2 = ""
                    $ highisland_harpies_hp -= 1
                    jump highisland_crew_ocean02
                'I lack pneuma to hit them with a spell. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and not highisland_harpies_magicused" ):
                    pass
                'I throw a fistful of blinding powder at them.' if item_blindingpowder and not highisland_harpies_blindingpowder:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw a fistful of blinding powder at them.')
                    $ highisland_harpies_blindingpowder += 1
                    $ custom1 = "Struggling to find your balance, you barely manage to send the panicking creature into the boat’s floor."
                    if thyrsus_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Thyrsus{/color} reaches for the beast with his creepers and quickly throws it into the sea."
                    elif bandit_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}The bandit{/color} shouts in fear, but then jumps onto the beast and lacerates its throat with his dagger."
                    elif navica_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Navica{/color} moves away, shouting in fear, while you grab your knife and lacerate the beast’s throat."
                    elif tulia_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Tulia{/color} crouches next to the beast and stabs its throat with the tip of her sword."
                    elif efren_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Efren{/color} crouches next to the beast and lacerates its throat with his sharp club."
                    elif pyrrhos_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Pyrrhos{/color} takes a deep breath, grabs the beast’s wing, and throws it into the sea."
                    elif aegidia_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Aegidia{/color} kicks the beast’s head, giving you a precious few heartbeats to grab your knife and lacerate its throat."
                    elif dalit_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Dalit{/color}kicks the beast’s head, giving you a precious few heartbeats to grab your knife and lacerate its throat."
                    elif tzvi_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Tzvi{/color} lets out a shout, grabs the beast’s wing, and throws it into the sea."
                    elif quintus_highisland_joined:
                        $ custom2 = " {color=#f6d6bd}Quintus{/color} lets out a shout, grabs the beast’s wing, and throws it into the sea."
                    else:
                        $ custom2 = " During the precious few heartbeats, you grab your knife and lacerate the beast’s throat."
                    $ highisland_harpies_hp -= 1
                    jump highisland_crew_ocean02
                'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                    pass
                '{image=d6} I grab my spear. “Prepare yourselves!”' if item_asterionspear or item_mountainroadspear:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my spear. “Prepare yourselves!”')
                    $ custom1 = "Having the range advantage helps you tear through the first wing."
                    jump highisland_crew_ocean03
                '{image=d6} I grab my axe. “Prepare yourselves!”' if not item_asterionspear and not item_mountainroadspear:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my axe. “Prepare yourselves!”')
                    $ custom2 = "It’s not easy to hold your stance when the “ground” keeps moving."
                    jump highisland_crew_ocean03

        label highisland_crew_ocean02:
            $ at = 0
            $ at_unlock_spell = 0
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg":
                play music "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg" fadeout 1.0 fadein 1.0
            $ at = 0
            $ at_unlock_spell = 0
            if highisland_harpies_hp:
                if pc_class == "mage" and not highisland_harpies_magicused:
                    $ at_unlock_spell = 1
                    $ manacost = 3
                menu:
                    '[custom1][custom2]
                    '
                    '“If you can - shoot them!”' if (aegidia_highisland_joined and not aegidia_highisland_blocked and not highisland_harpies_crewused) or (dalit_highisland_joined and not dalit_highisland_blocked and not highisland_harpies_crewused) or (pyrrhos_highisland_joined and not pyrrhos_highisland_blocked and not highisland_harpies_crewused):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you can - shoot them!”')
                        $ custom2 = ""
                        $ highisland_harpies_crewused += 1
                        if aegidia_highisland_joined and dalit_highisland_joined and pyrrhos_highisland_joined:
                            $ highisland_harpies_hp -= 4
                            $ custom1 = "{color=#f6d6bd}Aegidia’s{/color} arrows cause havoc, and keep you safe for another few breaths. The shells of harpies hit the water, only to get dragged away by the waves.\n\n{color=#f6d6bd}Dalit{/color} releases only one quarrel before she reaches for an axe, but her powerful shot tears off a harpy’s head. The dead shell sinks like a rock.\n\n{color=#f6d6bd}Pyrrhos’{/color} first shot misses, but he reloads his crossbow with sheer strength, releasing the second quarrel soon after. After his target loses its paw, it screeches in pain and attempts to flee, ignoring the dark blood dripping from its stump."
                        elif aegidia_highisland_joined and dalit_highisland_joined:
                            $ highisland_harpies_hp -= 3
                            $ custom1 = "{color=#f6d6bd}Aegidia’s{/color} arrows cause havoc, and keep you safe for another few breaths. The shells of harpies hit the water, only to get dragged away by the waves.\n\n{color=#f6d6bd}Dalit{/color} releases only one quarrel before she reaches for an axe, but her powerful shot tears off a harpy’s head. The dead shell sinks like a rock."
                        elif aegidia_highisland_joined and pyrrhos_highisland_joined:
                            $ highisland_harpies_hp -= 3
                            $ custom1 = "{color=#f6d6bd}Aegidia’s{/color} arrows cause havoc, and keep you safe for another few breaths. The shells of harpies hit the water, only to get dragged away by the waves.\n\n"
                        elif dalit_highisland_joined and pyrrhos_highisland_joined:
                            $ highisland_harpies_hp -= 2
                            $ custom1 = "The quarrels shot by {color=#f6d6bd}Dalit{/color} and {color=#f6d6bd}Pyrrhos{/color} keep you safe for another few breaths. The shells of harpies hit the water, only to get dragged away by the waves.\n\n{color=#f6d6bd}Pyrrhos’{/color} first shot misses, but he reloads his crossbow with sheer strength, releasing the second quarrel soon after. After his target loses its paw, it screeches in pain and attempts to flee, ignoring the dark blood dripping from its stump."
                        elif aegidia_highisland_joined:
                            $ highisland_harpies_hp -= 2
                            $ custom1 = "{color=#f6d6bd}Aegidia’s{/color} arrows cause havoc, and keep you safe for another few breaths. The shells of harpies hit the water, only to get dragged away by the waves."
                        elif dalit_highisland_joined:
                            $ highisland_harpies_hp -= 1
                            $ custom1 = "{color=#f6d6bd}Dalit{/color} releases only one quarrel before she reaches for an axe, but her powerful shot tears off a harpy’s head. The dead shell sinks like a rock."
                        elif pyrrhos_highisland_joined:
                            $ highisland_harpies_hp -= 1
                            $ custom1 = "{color=#f6d6bd}Pyrrhos’{/color} first shot misses, but he reloads his crossbow with sheer strength, releasing the second quarrel soon after. After his target loses its paw, it screeches in pain and attempts to flee, ignoring the dark blood dripping from its stump."
                        jump highisland_crew_ocean02
                    'Time for my crossbow.' if item_crossbow and item_crossbowquarrels >= 1 and not highisland_harpies_crossbowused:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time for my crossbow.')
                        $ highisland_harpies_crossbowused += 1
                        $ custom2 = ""
                        if highisland_harpies_hp == 4:
                            $ custom1 = "After your quarrel hits a harpy’s hip, the creature tries to fly for a bit longer, but soon crashes into the water and disappears beneath the surface. The other beasts, confused at first, get even closer."
                        else:
                            $ custom1 = "After your quarrel hits a harpy’s hip, the creature tries to fly for a bit longer, but soon crashes into the water and disappears beneath the surface."
                        $ highisland_harpies_hp -= 1
                        $ item_crossbowquarrels -= 1
                        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                        if dalit_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Dalit{/color} turns toward you with a quarrel in her teeth, what makes her look like she’s making a wide grin."
                        elif pyrrhos_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Pyrrhos{/color} lets out a chuckle."
                        elif quintus_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Quintus{/color} tries to nudge you with his shoulder, but almost falls overboard."
                        else:
                            $ custom2 = ""
                        jump highisland_crew_ocean02
                    '{image=d6} I don’t have much time, but I reload and shoot.' if item_crossbow and item_crossbowquarrels >= 1 and highisland_harpies_crossbowused == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I don’t have much time, but I reload and shoot.')
                        $ custom2 = ""
                        $ highisland_harpies_crossbowused += 1
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
                        if d100roll <= 60:
                            $ custom1 = "The quarrel rips a hole in the leathery wing of one of the creatures. After a few moments of trying to stay in one spot, it clumsily flies away."
                            $ highisland_harpies_hp -= 1
                        else:
                            $ custom1 = "You pull the trigger just when the rocking boat makes you lose balance. The quarrel disappears in the darkness."
                            if tzvi_highisland_joined:
                                $ custom2 = "“Careful,” growls {color=#f6d6bd}Tzvi{/color}."
                            elif aegidia_highisland_joined:
                                $ custom2 = "“Look out,” shouts {color=#f6d6bd}Aegidia{/color}."
                            elif efren_highisland_joined:
                                $ custom2 = "{color=#f6d6bd}Efren{/color} observes you for a bit, then sighs with relief."
                            elif tulia_highisland_joined:
                                $ custom2 = "{color=#f6d6bd}Tulia{/color} gives you an encouraging smile."
                            elif quintus_highisland_joined:
                                $ custom2 = "{color=#f6d6bd}Quintus{/color} grabs your shoulder, helping you find your balance."
                            elif dalit_highisland_joined:
                                $ custom2 = "{color=#f6d6bd}Dalit{/color} gives you an encouraging smile."
                            else:
                                $ custom2 = ""
                        $ item_crossbowquarrels -= 1
                        $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                        jump highisland_crew_ocean02
                    'I lack any quarrels. (disabled)' if item_crossbow and not item_crossbowquarrels and highisland_harpies_crossbowused < 2:
                        pass
                    'I don’t have a crossbow. (disabled)' if not item_crossbow:
                        pass
                    'I grab my wand. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and not highisland_harpies_magicused" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my wand.')
                        $ custom2 = ""
                        $ highisland_harpies_magicused += 1
                        $ mana = limit_mana(mana-manacost)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                        $ custom1 = "The invisible blast hits one of the beasts mid-flight, sending it into the sea. After a few moments, it shows up on the surface, using its wings to swim away."
                        if thyrsus_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Thyrsus{/color} gives you a surprised, but approving look."
                        elif bandit_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}The bandit{/color} gives you a suspicious look."
                        elif navica_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Navica’s{/color} eyes widen."
                        elif aegidia_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Aegidia{/color} gives you a surprised, but approving look."
                        elif dalit_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Dalit{/color} gives you a surprised, but approving look."
                        elif efren_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Efren{/color} gives you a surprised, but approving look."
                        elif pyrrhos_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Pyrrhos{/color} gives you a suspicious look."
                        elif tulia_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Tulia{/color} gives you a surprised, but approving look."
                        elif tzvi_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Tzvi{/color} gives you a suspicious look."
                        elif quintus_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Quintus{/color} gives you a radiant smile."
                        else:
                            $ custom2 = ""
                        $ highisland_harpies_hp -= 1
                        jump highisland_crew_ocean02
                    'I lack pneuma to hit them with a spell. [[Cost: [manacost]] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost and not highisland_harpies_magicused" ):
                        pass
                    'I throw a fistful of blinding powder at them.' if item_blindingpowder and not highisland_harpies_blindingpowder:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I throw a fistful of blinding powder at them.')
                        $ highisland_harpies_blindingpowder += 1
                        $ custom1 = "Struggling to find your balance, you barely manage to send the panicking creature into the boat’s floor."
                        if thyrsus_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Thyrsus{/color} reaches for the beast with his creepers and throws it into the sea."
                        elif bandit_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}The bandit{/color} shouts in fear, but then jumps onto the beast and lacerates its throat with his dagger."
                        elif navica_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Navica{/color} moves away, shouting in fear, while you grab your knife and lacerate the beast’s throat."
                        elif tulia_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Tulia{/color} crouches next to the beast and stabs its throat with the tip of her sword."
                        elif efren_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Efren{/color} crouches next to the beast and lacerates its throat with his sharp club."
                        elif pyrrhos_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Pyrrhos{/color} takes a deep breath, grabs the beast’s wing, and throws it into the sea."
                        elif aegidia_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Aegidia{/color} kicks the beast’s head, giving you a precious few heartbeats to grab your knife and lacerate its throat."
                        elif dalit_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Dalit{/color}kicks the beast’s head, giving you a precious few heartbeats to grab your knife and lacerate its throat."
                        elif tzvi_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Tzvi{/color} lets out a shout, grabs the beast’s wing, and throws it into the sea."
                        elif quintus_highisland_joined:
                            $ custom2 = " {color=#f6d6bd}Quintus{/color} lets out a shout, grabs the beast’s wing, and throws it into the sea."
                        else:
                            $ custom2 = " During the precious few heartbeats, you grab your knife and lacerate the beast’s throat."
                        $ highisland_harpies_hp -= 1
                        jump highisland_crew_ocean02
                    'I don’t have any potion that could help me here. (disabled)' if not item_blindingpowder and pc_class == "scholar":
                        pass
                    '{image=d6} I grab my spear. “Prepare yourselves!”' if item_asterionspear or item_mountainroadspear:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my spear. “Prepare yourselves!”')
                        $ custom1 = "Having the range advantage helps you tear through the first wing."
                        jump highisland_crew_ocean03
                    '{image=d6} I grab my axe. “Prepare yourselves!”' if not item_asterionspear and not item_mountainroadspear:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab my axe. “Prepare yourselves!”')
                        $ custom2 = "It’s not easy to hold your stance when the “ground” keeps moving."
                        jump highisland_crew_ocean03
            else:
                menu:
                    '[custom1][custom2]
                    \n\nThe remaining members of the pack take no more chances. They spread in various directions, seeking shelter among the tusk-like rocks.
                    '
                    '“Great job, everyone.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Great job, everyone.”')
                        jump highisland_afterharpies01
                    '“Well, still alive!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, still alive!”')
                        jump highisland_afterharpies01
                    'I stare in the distance.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stare in the distance.')
                        jump highisland_afterharpies01

        label highisland_crew_ocean03:
            $ at = 0
            $ at_unlock_spell = 0
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg":
                play music "<loop 30.0>audio/dancaineenterthesea_highisland_loop.ogg" fadeout 1.0 fadein 1.0
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
            if item_asterionspear or item_mountainroadspear:
                $ d100roll -= 20
            elif item_axe03:
                $ d100roll -= 15
            elif item_axe02 or item_axe02alt:
                $ d100roll -= 5
            $ d100roll += (highisland_harpies_hp*30)
            $ d100roll -= (highisland_crew_left*10)
            if thyrsus_highisland_joined:
                $ d100roll -= 10
            if tulia_highisland_joined:
                $ d100roll -= 10
            if tzvi_highisland_joined:
                $ d100roll -= 10
            if quintus_highisland_joined:
                $ d100roll -= 10
            if aegidia_highisland_joined:
                $ custom11 = " {color=#f6d6bd}Aegidia{/color} dodges the attacks pretty well, using her unstrung bow as a staff."
            else:
                $ custom11 = ""
            if dalit_highisland_joined:
                $ custom12 = " As {color=#f6d6bd}Dalit{/color} swings her axe, her yellow armor cares little for the few scratches it receives."
            else:
                $ custom12 = ""
            if efren_highisland_joined:
                $ custom13 = " At times, {color=#f6d6bd}Efren{/color} seems torn between fighting and holding his “hat”, but manages to land a few crucial hits with his club."
            else:
                $ custom13 = ""
            if navica_highisland_joined:
                $ custom14 = " {color=#f6d6bd}Navica{/color} focuses on securing the oars, but also uses them to push away the beasts."
            else:
                $ custom14 = ""
            if thyrsus_highisland_joined:
                $ custom15 = " {color=#f6d6bd}Thyrsus’{/color} creepers are like a wall, crushing any enemy in their range."
            else:
                $ custom15 = ""
            if pyrrhos_highisland_joined:
                $ custom16 = " {color=#f6d6bd}Pyrrhos{/color} lets out a shout of profanity every time his knife and fist find a target, though he sounds more irritated than worried."
            else:
                $ custom16 = ""
            if bandit_highisland_joined:
                $ custom17 = " {color=#f6d6bd}The bandit{/color} dodges the attacks with ease, caring little for the rocking boat."
            else:
                $ custom17 = ""
            if tulia_highisland_joined:
                $ custom18 = " {color=#f6d6bd}Tulia{/color} lets out an encouraging shout, holding her sword with both hands. Whenever she cuts through a monster’s flesh, she strikes the pose of a hero."
            else:
                $ custom18 = ""
            if tzvi_highisland_joined:
                $ custom19 = " {color=#f6d6bd}Tzvi{/color} keeps muttering to himself. The harpies seem to ignore him, but he stays busy, aiding anyone who needs it with his dagger."
            else:
                $ custom19 = ""
            if quintus_highisland_joined:
                $ custom20 = " {color=#f6d6bd}Quintus{/color} bursts into laughter, grabbing one beast with his bare hands and throwing it in the water."
            else:
                $ custom20 = ""
            if d100roll <= 50:
                menu:
                    '[custom1] The gambeson on your arm stops the talons as you swing your blade and clenched fist. [custom11][custom12][custom13][custom14][custom15][custom16][custom17][custom18][custom19][custom20]
                    \n\nAfter a few breaths, the scattered pack seeks shelter among the rocks. You put your bloodied hand in the chilling water.
                    '
                    '“Great job, everyone.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Great job, everyone.”')
                        jump highisland_afterharpies01
                    '“Well, still alive!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, still alive!”')
                        jump highisland_afterharpies01
                    'I stare in the distance.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stare in the distance.')
                        jump highisland_afterharpies01
            else:
                label highisland_companiondamage_loop_ocean03:
                    $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus', 'pc'])
                    if highisland_crew_dmg_target == "aegidia":
                        if not aegidia_highisland_joined or aegidia_highisland_blocked:
                            jump highisland_companiondamage_loop_ocean03
                        else:
                            $ aegidia_highisland_blocked = 1
                            $ highisland_crew_left -= 1
                            $ custom2 = "{color=#f6d6bd}Aegidia{/color} is the only soul who suffered during the onslaught. You watch as she bandages her arm. It’s doubtful she’ll be of much use during further fights."
                    elif highisland_crew_dmg_target == "dalit":
                        if not dalit_highisland_joined or dalit_highisland_blocked:
                            jump highisland_companiondamage_loop_ocean03
                        else:
                            $ dalit_highisland_blocked = 1
                            $ highisland_crew_left -= 1
                            $ custom2 = "{color=#f6d6bd}Dalit{/color} is the only soul who suffered during the onslaught. You watch as she bandages her arm. It’s doubtful she’ll be of much use during further fights."
                    elif highisland_crew_dmg_target == "efren":
                        if not efren_highisland_joined or efren_highisland_blocked:
                            jump highisland_companiondamage_loop_ocean03
                        else:
                            $ efren_highisland_blocked = 1
                            $ highisland_crew_left -= 1
                            $ custom2 = "{color=#f6d6bd}Efren{/color} is the only soul who suffered during the onslaught. You watch as he bandages his arm. It’s doubtful he’ll be of much use during further fights."
                    elif highisland_crew_dmg_target == "thyrsus":
                        if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                            jump highisland_companiondamage_loop_ocean03
                        else:
                            $ thyrsus_highisland_blocked = 1
                            $ highisland_crew_left -= 1
                            $ custom2 = "{color=#f6d6bd}Thyrsus{/color} is the only soul who suffered during the onslaught. You watch as he bandages his arm. It’s doubtful he’ll be of much use during further fights."
                    elif highisland_crew_dmg_target == "pyrrhos":
                        if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                            jump highisland_companiondamage_loop_ocean03
                        else:
                            $ pyrrhos_highisland_blocked = 1
                            $ highisland_crew_left -= 1
                            $ custom2 = "{color=#f6d6bd}Pyrrhos{/color} is the only soul who suffered during the onslaught. You watch as he bandages his arm. It’s doubtful he’ll be of much use during further fights."
                    elif highisland_crew_dmg_target == "bandit":
                        if not bandit_highisland_joined or bandit_highisland_blocked:
                            jump highisland_companiondamage_loop_ocean03
                        else:
                            $ bandit_highisland_blocked = 1
                            $ highisland_crew_left -= 1
                            $ custom2 = "{color=#f6d6bd}The bandit{/color} is the only soul who suffered during the onslaught. You watch as he bandages his arm. It’s doubtful he’ll be of much use during further fights."
                    elif highisland_crew_dmg_target == "tulia":
                        if not tulia_highisland_joined or tulia_highisland_blocked:
                            jump highisland_companiondamage_loop_ocean03
                        else:
                            $ tulia_highisland_blocked = 1
                            $ highisland_crew_left -= 1
                            $ custom2 = "{color=#f6d6bd}Tulia{/color} is the only soul who suffered during the onslaught. You watch as she bandages her arm. It’s doubtful she’ll be of much use during further fights."
                    elif highisland_crew_dmg_target == "tzvi":
                        if not tzvi_highisland_joined or tzvi_highisland_blocked:
                            jump highisland_companiondamage_loop_ocean03
                        else:
                            $ tzvi_highisland_blocked = 1
                            $ highisland_crew_left -= 1
                            $ custom2 = "{color=#f6d6bd}Tzvi{/color} is the only soul who suffered during the onslaught. You watch as he bandages his arm. It’s doubtful he’ll be of much use during further fights."
                    elif highisland_crew_dmg_target == "quintus":
                        if not quintus_highisland_joined or quintus_highisland_blocked:
                            jump highisland_companiondamage_loop_ocean03
                        else:
                            $ quintus_highisland_blocked = 1
                            $ highisland_crew_left -= 1
                            $ custom2 = "{color=#f6d6bd}Quintus{/color} is the only soul who suffered during the onslaught. You watch as he bandages his arm. It’s doubtful he’ll be of much use during further fights."
                    elif highisland_crew_dmg_target == "pc":
                        $ custom2 = "You’re the only soul who suffered during the onslaught."
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
                        elif pc_hp > 0:
                            $ pc_hp = limit_pc_hp(pc_hp-2)
                            show minus2hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                            if not cleanliness_clothes_torn:
                                $ cleanliness_clothes_torn = 1
                                show minus1appearance at appearancechange onlayer myoverlay
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                        else:
                            $ custom1 = "The gambeson on your arm fails to stop the talons as you swing your blade and clenched fist desperately. The harpies focus on your face, and land a lucky hit. After a few breaths, the blood running from your empty eye sockets mixes with the salt water."
                            jump highisland_gameover
                menu:
                    '[custom1] The gambeson on your arm stops the talons as you swing your blade and clenched fist. [custom11][custom12][custom13][custom14][custom15][custom16][custom17][custom18][custom19][custom20]
                    \n\nAfter a few breaths, the scattered pack seeks shelter among the rocks. [custom2]
                    '
                    '“Great job, everyone.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Great job, everyone.”')
                        jump highisland_afterharpies01
                    '“Well, still alive!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, still alive!”')
                        jump highisland_afterharpies01
                    'I stare in the distance.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stare in the distance.')
                        jump highisland_afterharpies01

label highisland_afterharpiesALL:
    label highisland_afterharpies01:
        $ pc_battlecounter += 1
        if pc_area == "sea_south1":
            $ pc_area = "sea_south2"
            show areapicture hi_sea_south2_waterfall at basicfade
            if highisland_mode == "solo":
                jump highisland_solo_afterharpies_south201
            if highisland_mode == "crew":
                jump highisland_crew_afterharpies_south201
        if pc_area == "sea_north1":
            $ pc_area = "sea_north2"
            show areapicture hi_sea_north2_waterfall at basicfade
            if highisland_mode == "solo":
                jump highisland_solo_afterharpies_north201
            if highisland_mode == "crew":
                jump highisland_crew_afterharpies_north201
            if highisland_mode == "howlers":
                jump highisland_howlers_afterharpies_north201

    label highisland_solo_afterharpies_south201:
        menu:
            'After rowing for an hour or so, you leave the coastal rocks behind. The fierce waterfall ahead won’t be too difficult to reach, but if it’s not the spot that hides the old harbor, the wasted effort and cold winds will surely exhaust you before you find it.
            \n\nYou look north. There’s another waterfall there, a much gentler one.
            '
            'I try to land here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to land here.')
                menu:
                    'The long minutes go by, and the roar of the waterfall devours all other sounds. You spend some time trying to stop the boat somewhere to look up, behind the water, but to no avail.
                    '
                    'Well, I can’t stick to the cliffs. I enter the deep water, then head to the other waterfall.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, I can’t stick to the cliffs. I enter the deep water, then head to the other waterfall.')
                        show areapicture hi_sea_north2_waterfall at basicfade
                        if pc_food > 0:
                            $ pc_food = limit_pc_food(pc_food-2)
                            show minus2food at foodchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                            $ custom1 = "Tired, sleepy, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you hungry."
                        elif pc_hp > 0:
                            $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you gasp for air."
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        else:
                            $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor overwhelms you - you {i}must{/i} take a break.\n\nAfter a few minutes of listening to the waves, you fall asleep - never to wake again."
                            jump highisland_gameover
                        menu:
                            '[custom1]
                            \n\nFinally, you reach the right spot. The “wall” of the island isn’t as flat here, and the tide lets you reach a few high ledges, flat and wide enough for a boat. Even though it’s dark, you recognize some old wooden beams, as well as a few copper rods - remains of an old structure.
                            \n\nThere’s another boat, or rather a small chunk of it, tied to a post just a few steps away from you.
                            \n\nYou get out and scrape the hull against the ash-colored rocks.
                            '
                            'I secure my boat.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I secure my boat.')
                                jump highisland_landing00
            'I head for the northern waterfall instead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head for the northern waterfall instead.')
                show areapicture hi_sea_north2_waterfall at basicfade
                menu:
                    'Fifteen long minutes go by, and the roar of the waterfall devours all the other sounds. Here, the “wall” of the island isn’t as flat as it seemed to be from afar, and the tide lets you reach a few high ledges, flat and wide enough for a boat. Even though it’s dark, you recognize some old wooden beams, as well as a few copper rods - remains of an old structure.
                    \n\nThere’s another boat, or rather a small chunk of it, tied to a post just a few steps away from you.
                    \n\nYou get out and scrape the hull against the ash-colored rocks.
                    '
                    'I secure my boat.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I secure my boat.')
                        jump highisland_landing00

    label highisland_crew_afterharpies_south201:
        if navica_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Navica{/color} raises her voice. “We’re at the wrong spot.”"
        elif tzvi_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Tzvi’s{/color} high voice is grim. “Well?”"
        elif dalit_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Dalit{/color} looks at you, but says nothing. She seems to be seasick."
        elif aegidia_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Aegidia{/color} looks at you. “We can ne climb these rocks.”"
        elif efren_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Efren{/color} looks at you. “Is {i}this{/i} the place?”"
        elif thyrsus_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Thyrsus{/color} looks at you. “What now?”"
        elif pyrrhos_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Pyrrhos{/color} spits at the waves. “We can’t climb these rocks.”"
        elif bandit_highisland_joined:
            $ custom11 = "{color=#f6d6bd}The bandit{/color} rubs his hands, trying to get warmer."
        elif quintus_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Quintus{/color} looks at you. “What now?”"
        elif tulia_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Tulia{/color} looks at you, but says nothing."
        menu:
            'After rowing for an hour or so, you leave the coastal rocks behind. The fierce waterfall ahead won’t be too difficult to reach, but if it’s not the spot that hides the old harbor, the wasted effort and cold winds will surely exhaust you before you find it.
            \n\nYou look north. There’s another waterfall there, a much gentler one.
            \n\n[custom11]
            '
            '“This is the spot. Let’s try to land here.”' if not navica_highisland_joined:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This is the spot. Let’s try to land here.”')
                menu:
                    'The long minutes go by, and the roar of the waterfall devours all other sounds. You spend some time trying to stop the boat somewhere to look up, behind the water, but to no avail.
                    '
                    '“Well, we can’t stick to the cliffs. Let’s enter the deep water, then head to the other waterfall.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, we can’t stick to the cliffs. Let’s enter the deep water, then head to the other waterfall.”')
                        show areapicture hi_sea_north2_waterfall at basicfade
                        label highisland_companionexhaustion_loop_afterharpies_south201:
                            if highisland_crew_left <= 0:
                                if pc_food > 0:
                                    $ pc_food = limit_pc_food(pc_food-2)
                                    show minus2food at foodchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                                    $ custom1 = "Tired, sleepy, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you hungry."
                                elif pc_hp > 0:
                                    $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you gasp for air."
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                else:
                                    $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you gasp for air, and you’re forced to rely on the muscles of others."
                            else:
                                $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus', 'pc'])
                                if dalit_highisland_joined and not dalit_highisland_tired and not dalit_highisland_blocked:
                                    $ highisland_crew_dmg_target = "dalit"
                                if highisland_crew_dmg_target == "aegidia":
                                    if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not aegidia_highisland_tired:
                                            $ aegidia_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push her too much after you reach your destination."
                                        else:
                                            $ aegidia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Aegidia{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt she’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "dalit":
                                    if not dalit_highisland_joined or dalit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not dalit_highisland_tired:
                                            $ dalit_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Dalit{/color} sits down on the bottom boards, visibly exhausted from the seasickness. It may be better to not push her too much after you reach your destination."
                                        else:
                                            $ dalit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Dalit{/color}, already exhausted from the seasickness, sits down on the bottom boards, gasping for air. You doubt she’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "efren":
                                    if not efren_highisland_joined or efren_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not efren_highisland_tired:
                                            $ efren_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Efren{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ efren_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Efren{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "thyrsus":
                                    if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not thyrsus_highisland_tired:
                                            $ thyrsus_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Thyrsus{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ thyrsus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Thyrsus{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "pyrrhos":
                                    if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not pyrrhos_highisland_tired:
                                            $ pyrrhos_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ pyrrhos_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Pyrrhos{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "bandit":
                                    if not bandit_highisland_joined or bandit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not bandit_highisland_tired:
                                            $ bandit_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}The bandit{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ bandit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}The bandit{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "tulia":
                                    if not tulia_highisland_joined or tulia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not tulia_highisland_tired:
                                            $ tulia_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Tulia{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push her too much after you reach your destination."
                                        else:
                                            $ tulia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Tulia{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt she’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "tzvi":
                                    if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not tzvi_highisland_tired:
                                            $ tzvi_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ tzvi_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Tzvi{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "quintus":
                                    if not quintus_highisland_joined or quintus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not quintus_highisland_tired:
                                            $ quintus_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Quintus{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ quintus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Quintus{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "pc":
                                    if pc_food > 0:
                                        $ pc_food = limit_pc_food(pc_food-2)
                                        show minus2food at foodchange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                                        $ custom1 = "Tired, sleepy, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you hungry."
                                    elif pc_hp > 0:
                                        $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you gasp for air."
                                        $ pc_hp = limit_pc_hp(pc_hp-1)
                                        show minus1hp at hpchange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                    else:
                                        $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you gasp for air, and you’re forced to rely on the muscles of others."
                        menu:
                            '[custom1]
                            \n\nFinally, you reach the right spot. The “wall” of the island isn’t as flat here, and the tide lets you reach a few high ledges, flat and wide enough for a boat. Even though it’s dark, you recognize some old wooden beams, as well as a few copper rods - remains of an old structure.
                            \n\nThere’s another boat, or rather a small chunk of it, tied to a post just a few steps away from you.
                            \n\nAll of you get out and scrape the hull against the ash-colored rocks.
                            '
                            'Let’s prepare the ropes.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s prepare the ropes.')
                                jump highisland_landing00
            '“Let’s head for the northern waterfall.”' if not navica_highisland_joined:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s head for the northern waterfall.”')
                jump highisland_crew_afterharpies_south201a
            '“Very well. Let’s head for the northern waterfall.”' if navica_highisland_joined:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. Let’s head for the northern waterfall.”')
                label highisland_crew_afterharpies_south201a:
                    show areapicture hi_sea_north2_waterfall at basicfade
                    menu:
                        'Fifteen long minutes go by, and the roar of the waterfall devours all other sounds. Here, the “wall” of the island isn’t as flat as it seemed to be from afar, and the tide lets you reach a few high ledges, flat and wide enough for a boat. Even though it’s dark, you recognize some old wooden beams, as well as a few copper rods - remains of an old structure.
                        \n\nThere’s another boat, or rather a small chunk of it, tied to a post just a few steps away from you.
                        \n\nAll of you get out and scrape the hull against the ash-colored rocks.
                        '
                        'Let’s prepare the ropes.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s prepare the ropes.')
                            jump highisland_landing00

    label highisland_solo_afterharpies_north201:
        menu:
            'After rowing for an hour or so, you leave the coastal rocks behind. The gentle waterfall ahead won’t be too difficult to reach, but if it’s not the spot that hides the old harbor, the wasted effort and cold winds will surely exhaust you before you find it.
            \n\nYou look south. There’s another waterfall there, one much more fierce.
            '
            'I try to land here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to land here.')
                menu:
                    'The long minutes go by, and the roar of the waterfall devours all other sounds. Here, the “wall” of the island isn’t as flat as it seemed to be from afar, and the tide lets you reach a few high ledges, flat and wide enough for a boat. Even though it’s dark, you recognize some old wooden beams, as well as a few copper rods - remains of an old structure.
                    \n\nThere’s another boat, or rather a small chunk of it, tied to a post just a few steps away from you.
                    \n\nYou get out and scrape the hull against the ash-colored rocks.
                    '
                    'Let’s prepare the ropes.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s prepare the ropes.')
                        jump highisland_landing00
            'I head for the southern waterfall instead.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head for the southern waterfall instead.')
                show areapicture hi_sea_south2_waterfall at basicfade
                menu:
                    'Fifteen long minutes go by, and the roar of the waterfall devours all other sounds. You spend some time trying to stop the boat somewhere to look up, behind the water, but to no avail.
                    '
                    'Well, I can’t stick to the cliffs. I enter the deep water, then head to the other waterfall.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Well, I can’t stick to the cliffs. I enter the deep water, then head to the other waterfall.')
                        show areapicture hi_sea_north2_waterfall at basicfade
                        if pc_food > 0:
                            $ pc_food = limit_pc_food(pc_food-2)
                            show minus2food at foodchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                            $ custom1 = "Tired, sleepy, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you hungry."
                        elif pc_hp > 0:
                            $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you gasp for air."
                            $ pc_hp = limit_pc_hp(pc_hp-1)
                            show minus1hp at hpchange onlayer myoverlay
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                        else:
                            $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor overwhelms you - you {i}must{/i} take a break.\n\nAfter a few minutes of listening to the waves, you fall asleep - never to wake again."
                            jump highisland_gameover
                        menu:
                            '[custom1]
                            \n\nFinally, you reach the right spot. The “wall” of the island isn’t as flat here, and the tide lets you reach a few high ledges, flat and wide enough for a boat. Even though it’s dark, you recognize some old wooden beams, as well as a few copper rods - remains of an old structure.
                            \n\nThere’s another boat, or rather a small chunk of it, tied to a post just a few steps away from you.
                            \n\nYou get out and scrape the hull against the ash-colored rocks.
                            '
                            'Let’s prepare the ropes.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s prepare the ropes.')
                                jump highisland_landing00

    label highisland_howlers_afterharpies_north201:
        menu:
            'After rowing for an hour or so, you leave the coastal rocks behind. The gentle waterfall ahead won’t be too difficult to reach, but if it’s not the spot that hides the old harbor, the wasted effort and cold winds will surely exhaust you before you find it.
            \n\nYou look south. There’s another waterfall there, one much more fierce.
            \n\n{color=#f6d6bd}The leader{/color} looks at you. “Well? Where to?”
            '
            '“This is the spot. Let’s try to land here.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This is the spot. Let’s try to land here.”')
                menu:
                    'The long minutes go by, and the roar of the waterfall devours all other sounds. Here, the “wall” of the island isn’t as flat as it seemed to be from afar, and the tide lets you reach a few high ledges, flat and wide enough for a boat. Even though it’s dark, you recognize some old wooden beams, as well as a few copper rods - remains of an old structure.
                    \n\nThere’s another boat, or rather a small chunk of it, tied to a post just a few steps away from you.
                    \n\nAll of you get out and scrape the hull against the ash-colored rocks.
                    '
                    '“Let’s prepare the ropes.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s prepare the ropes.”')
                        jump highisland_landing00
            '“We should head for the southern waterfall.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should head for the southern waterfall.”')
                show areapicture hi_sea_south2_waterfall at basicfade
                menu:
                    'Fifteen long minutes go by, and the roar of the waterfall devours all other sounds. You spend some time trying to stop the boat somewhere to look up, behind the water, but to no avail.
                    '
                    '“Well, we can’t stick to the cliffs. Let’s enter the deep water, then head to the other spot.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, we can’t stick to the cliffs. Let’s enter the deep water, then head to the other spot.”')
                        show areapicture hi_sea_north2_waterfall at basicfade
                        $ highisland_howlersguards_hp -= 1
                        menu:
                            '{color=#f6d6bd}The guards{/color} give you angry looks, but remain silent. You can tell by their gestures how tired they’re getting.
                            \n\nFinally, you reach the right spot. The “wall” of the island isn’t as flat here, and the tide lets you reach a few high ledges, flat and wide enough for a boat. Even though it’s dark, you recognize some old wooden beams, as well as a few copper rods - remains of an old structure.
                            \n\nThere’s another boat, or rather a small chunk of it, tied to a post just a few steps away from you.
                            \n\nYou get out and scrape the hull against the ash-colored rocks.
                            '
                            'I secure my boat.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I secure my boat.')
                                jump highisland_landing00

    label highisland_crew_afterharpies_north201:
        if navica_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Navica{/color} raises her voice. “Yeah. We’re here.”"
        elif tzvi_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Tzvi’s{/color} high voice is grim. “Well?”"
        elif dalit_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Dalit{/color} looks at you, but says nothing. She seems to be seasick."
        elif aegidia_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Aegidia{/color} looks at you. “We can ne climb these rocks.”"
        elif efren_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Efren{/color} looks at you. “Is {i}this{/i} the place?”"
        elif thyrsus_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Thyrsus{/color} looks at you. “What now?”"
        elif pyrrhos_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Pyrrhos{/color} spits at the waves. “We can’t climb these rocks.”"
        elif bandit_highisland_joined:
            $ custom11 = "{color=#f6d6bd}The bandit{/color} rubs his hands, trying to get warmer."
        elif quintus_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Quintus{/color} looks at you. “What now?”"
        elif tulia_highisland_joined:
            $ custom11 = "{color=#f6d6bd}Tulia{/color} looks at you, but says nothing."
        menu:
            'After rowing for an hour or so, you leave the coastal rocks behind. The gentle waterfall ahead won’t be too difficult to reach, but if it’s not the spot that hides the old harbor, the wasted effort and cold winds will surely exhaust you before you find it.
            \n\nYou look south. There’s another waterfall there, one much more fierce.
            \n\n[custom11]
            '
            '“Very well. Let’s go ahead.”' if navica_highisland_joined:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. Let’s go ahead.”')
                jump highisland_crew_afterharpies_north201a
            '“This is the spot. Let’s try to land here.”' if not navica_highisland_joined:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This is the spot. Let’s try to land here.”')
                label highisland_crew_afterharpies_north201a:
                    menu:
                        'The long minutes go by, and the roar of the waterfall devours all the other sounds. Here, the “wall” of the island isn’t as flat as it seemed to be from afar, and the tide lets you reach a few high ledges, flat and wide enough for a boat. Even though it’s dark, you recognize some old wooden beams, as well as a few copper rods - remains of an old structure.
                        \n\nThere’s another boat, or rather a small chunk of it, tied to a post just a few steps away from you.
                        \n\nAll of you get out and scrape the hull against the ash-colored rocks.
                        '
                        '“Let’s prepare the ropes.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s prepare the ropes.”')
                            jump highisland_landing00
            '“We should head for the southern waterfall.”' if not navica_highisland_joined:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should head for the southern waterfall.”')
                show areapicture hi_sea_south2_waterfall at basicfade
                menu:
                    'Fifteen long minutes go by, and the roar of the waterfall devours all other sounds. You spend some time trying to stop the boat somewhere and to look up, behind the water, but to no avail.
                    '
                    '“Well, we can’t stick to the cliffs. Let’s enter the deep water, then head to the other spot.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, we can’t stick to the cliffs. Let’s enter the deep water, then head to the other spot.”')
                        show areapicture hi_sea_north2_waterfall at basicfade
                        label highisland_companionexhaustion_loop_afterharpies_north201:
                            if highisland_crew_left <= 0:
                                if pc_food > 0:
                                    $ pc_food = limit_pc_food(pc_food-2)
                                    show minus2food at foodchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                                    $ custom1 = "Tired, sleepy, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you hungry."
                                elif pc_hp > 0:
                                    $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you gasp for air."
                                    $ pc_hp = limit_pc_hp(pc_hp-1)
                                    show minus1hp at hpchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                else:
                                    $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you gasp for air, and you’re forced to rely on the muscles of others."
                            else:
                                $ highisland_crew_dmg_target = renpy.random.choice(['aegidia', 'dalit', 'efren', 'thyrsus', 'pyrrhos', 'bandit', 'tulia', 'tzvi', 'quintus', 'pc'])
                                if dalit_highisland_joined and not dalit_highisland_tired and not dalit_highisland_blocked:
                                    $ highisland_crew_dmg_target = "dalit"
                                if highisland_crew_dmg_target == "aegidia":
                                    if not aegidia_highisland_joined or aegidia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not aegidia_highisland_tired:
                                            $ aegidia_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Aegidia{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push her too much after you reach your destination."
                                        else:
                                            $ aegidia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Aegidia{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt she’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "dalit":
                                    if not dalit_highisland_joined or dalit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not dalit_highisland_tired:
                                            $ dalit_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Dalit{/color} sits down on the bottom boards, visibly exhausted from the seasickness. It may be better to not push her too much after you reach your destination."
                                        else:
                                            $ dalit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Dalit{/color}, already exhausted from the seasickness, sits down on the bottom boards, gasping for air. You doubt she’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "efren":
                                    if not efren_highisland_joined or efren_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not efren_highisland_tired:
                                            $ efren_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Efren{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ efren_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Efren{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "thyrsus":
                                    if not thyrsus_highisland_joined or thyrsus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not thyrsus_highisland_tired:
                                            $ thyrsus_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Thyrsus{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ thyrsus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Thyrsus{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "pyrrhos":
                                    if not pyrrhos_highisland_joined or pyrrhos_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not pyrrhos_highisland_tired:
                                            $ pyrrhos_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Pyrrhos{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ pyrrhos_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Pyrrhos{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "bandit":
                                    if not bandit_highisland_joined or bandit_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not bandit_highisland_tired:
                                            $ bandit_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}The bandit{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ bandit_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}The bandit{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "tulia":
                                    if not tulia_highisland_joined or tulia_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not tulia_highisland_tired:
                                            $ tulia_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Tulia{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push her too much after you reach your destination."
                                        else:
                                            $ tulia_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Tulia{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt she’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "tzvi":
                                    if not tzvi_highisland_joined or tzvi_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not tzvi_highisland_tired:
                                            $ tzvi_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Tzvi{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ tzvi_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Tzvi{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "quintus":
                                    if not quintus_highisland_joined or quintus_highisland_blocked:
                                        jump highisland_companionexhaustion_loop_afterharpies_north201
                                    else:
                                        if not quintus_highisland_tired:
                                            $ quintus_highisland_tired = 1
                                            $ custom1 = "{color=#f6d6bd}Quintus{/color} sits down on the bottom boards, visibly exhausted. It may be better to not push him too much after you reach your destination."
                                        else:
                                            $ quintus_highisland_blocked = 1
                                            $ highisland_crew_left -= 1
                                            $ custom1 = "{color=#f6d6bd}Quintus{/color}, already exhausted, sits down on the bottom boards, gasping for air. You doubt he’ll be of much help once you reach your destination."
                                elif highisland_crew_dmg_target == "pc":
                                    if pc_food > 0:
                                        $ pc_food = limit_pc_food(pc_food-2)
                                        show minus2food at foodchange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                                        $ custom1 = "Tired, sleepy, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you hungry."
                                    elif pc_hp > 0:
                                        $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you gasp for air."
                                        $ pc_hp = limit_pc_hp(pc_hp-1)
                                        show minus1hp at hpchange onlayer myoverlay
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                                    else:
                                        $ custom1 = "Sleepy, hungry, and with arms weakened by the rowing, you spend more precious minutes correcting your mistake. The grueling labor makes you gasp for air, and you’re forced to rely on the muscles of others."
                        menu:
                            '[custom1]
                            \n\nFinally, you reach the right spot. The “wall” of the island isn’t as flat here, and the tide lets you reach a few high ledges, flat and wide enough for a boat. Even though it’s dark, you recognize some old wooden beams, as well as a few copper rods - remains of an old structure.
                            \n\nThere’s another boat, or rather a small chunk of it, tied to a post just a few steps away from you.
                            \n\nAll of you get out and scrape the hull against the ash-colored rocks.
                            '
                            '“Let’s prepare the ropes.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s prepare the ropes.”')
                                jump highisland_landing00

label highisland_landingALL:
    label highisland_landing00:
        $ can_potions = 1
        if highisland_mode == "solo":
            jump highisland_solo_landing01
        if highisland_mode == "crew":
            jump highisland_crew_landing01
        if highisland_mode == "howlers":
            jump highisland_howlers_landing01

    label highisland_solo_landingALL:
        label highisland_solo_landing01:
            $ custom1 = "The cave behind the waterfall is maybe thirty feet above you, but getting to it will take some effort. The ancient stairs and handrails have mostly fallen apart, and the slippery rocks are nothing less than a trap."
            jump highisland_solo_landing02

        label highisland_solo_landing02:
            $ at_unlock_force = 0
            $ at = 0
            if highisland_cliff_hp <= 0:
                jump highisland_solo_landing04
            if pc_class == "warrior" and not highisland_cliff_forceused:
                $ at_unlock_force = 1
                $ at = 0
            menu:
                '[custom1]
                '
                'I shorten the distance with a few confident jumps.' ( condition="at == 'force' and not highisland_cliff_forceused" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shorten the distance with a few confident jumps.')
                    $ highisland_cliff_forceused = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "You notice one slab that’s wider than the others, and use it as the starting point. You reach a larger chunk of the broken stairs, and while the bronze structure protests with a loud screech, it won’t collapse any time soon."
                    jump highisland_solo_landing02
                'I can’t shorten the distance quickly. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0 and not highisland_cliff_forceused" ):
                    pass
                'The bone hook will make it {i}much{/i} easier.' if item_bonehook and not highisland_cliff_graplinghookused: # ropehook
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bone hook will make it {i}much{/i} easier.')
                    $ highisland_cliff_graplinghookused = 1
                    $ highisland_cliff_hp -= 2
                    $ custom1 = "You give it a shot - not only does the hook allow you to climb up the rope, it also helps you test the durability of the bronze rails and sticking-out roots of plants. You quickly reach the higher spots of the wall."
                    jump highisland_solo_landing02
                'The claw-tool I picked at {color=#f6d6bd}Pelt{/color} may be of use here.' if (item_peltnorthberrytools and not highisland_cliff_peltnorthberrytools) or (item_peltnorthberryclaw and not highisland_cliff_peltnorthberrytools):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The claw-tool I picked at {color=#f6d6bd}Pelt{/color} may be of use here.')
                    $ highisland_cliff_peltnorthberrytools = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "You make sure the claw is properly tied to the shaft, then seek a wide crack in the wall. It takes a few hits, but you manage to stick it into a wider gap and get to a spot that’s a bit higher up."
                    jump highisland_solo_landing02
                '{image=d6} I’ve got no more tricks. Time to climb.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ve got no more tricks. Time to climb.')
                    jump highisland_solo_landing03

        label highisland_solo_landing03:
            $ d100roll = renpy.random.randint(1, 100)
            $ at_unlock_force = 0
            $ at = 0
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            $ d100roll += (highisland_cliff_hp*20)
            if d100roll <= 40:
                $ custom1 = "With the bright night on your side, you look for ledges to support you, and avoid the shining, wet rocks."
                label highisland_solo_landing04:
                    menu:
                        '[custom1] Finally, you pull yourself up, into the dark mouth of the cave - the remains of the original stream.
                        '
                        'I light up a torch and examine the area.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I light up a torch and examine the area.')
                            $ highisland_destination = "cave1"
                            jump highisland_destination
            else:
                $ custom1 = "With the bright night on your side, you look for convenient ledges, but one of the steps betrays you - you slide off, painfully scratching your knee against the wall. You take a deep breath and carry on, your limbs growing quite tired, but you manage to reach the top. You pull yourself up, into the dark mouth of the cave - the remains of the original stream."
                if pc_food > 0:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    $ custom1 = "With the bright night on your side, you look for convenient ledges, but one of the steps betrays you - you slide off, painfully smashing your jaw against a rock, then hit the floor with your tense back. You feel no pain."
                    jump highisland_gameover
                menu:
                    '[custom1]
                    '
                    'I light up a torch and examine the area.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I light up a torch and examine the area.')
                        $ highisland_destination = "cave1"
                        jump highisland_destination

    label highisland_howlers_landingALL:
        label highisland_howlers_landing01:
            $ at_unlock_force = 0
            $ at = 0
            $ highisland_cliff_hp -= 2
            if pc_class == "warrior" and not highisland_cliff_forceused:
                $ at_unlock_force = 1
                $ at = 0
            menu:
                'The cave behind the waterfall is maybe thirty feet above you, but getting to it will take some effort. The ancient stairs and handrails have mostly fallen apart, and the slippery rocks are nothing less than a trap.
                \n\n“The {i}harbor{/i}...” {color=#f6d6bd}the guard with the mace{/color} sounds unconvinced. “Nae time to waste.” All five of them start to climb up carefully, supporting each other with muscles and ropes.
                '
                'I shorten the distance with a few confident jumps.' ( condition="at == 'force' and not highisland_cliff_forceused" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shorten the distance with a few confident jumps.')
                    $ highisland_cliff_forceused = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "You notice one slab that’s wider than the others, and use it as the starting point. You reach a larger chunk of the broken stairs, and while the bronze structure protests with a loud screech, it won’t collapse any time soon. You reach out to one of your companions and help them join you."
                    jump highisland_howlers_landing02
                'I can’t shorten the distance quickly. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0 and not highisland_cliff_forceused" ):
                    pass
                'The bone hook will make it {i}much{/i} easier.' if item_bonehook and not highisland_cliff_graplinghookused:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bone hook will make it {i}much{/i} easier.')
                    $ highisland_cliff_graplinghookused = 1
                    $ highisland_cliff_hp -= 2
                    $ custom1 = "You give it a shot - not only does the hook allow you to climb up the rope, it also helps you test the durability of the bronze rails and sticking-out roots of plants. You reach the higher spots of the wall quickly, followed by the rest of the group."
                    jump highisland_howlers_landing02
                'The claw-tool I picked at {color=#f6d6bd}Pelt{/color} may be of use here.' if (item_peltnorthberrytools and not highisland_cliff_peltnorthberrytools) or (item_peltnorthberryclaw and not highisland_cliff_peltnorthberrytools):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The claw-tool I picked at {color=#f6d6bd}Pelt{/color} may be of use here.')
                    $ highisland_cliff_peltnorthberrytools = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "You make sure the claw is properly tied to the shaft, then seek a wide crack in the wall. It takes a few hits, but you manage to stick it into a wider gap and get to a spot that’s a bit higher up, where you secure the rope for your companions."
                    jump highisland_howlers_landing02
                '{image=d6} I’ve got no more tricks. Time to climb.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ve got no more tricks. Time to climb.')
                    jump highisland_howlers_landing03

        label highisland_howlers_landing02:
            $ at_unlock_force = 0
            $ at = 0
            if highisland_cliff_hp <= 0:
                jump highisland_howlers_landing04
            if pc_class == "warrior" and not highisland_cliff_forceused:
                $ at_unlock_force = 1
                $ at = 0
            menu:
                '[custom1]
                '
                'I shorten the distance with a few confident jumps.' ( condition="at == 'force' and not highisland_cliff_forceused" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shorten the distance with a few confident jumps.')
                    $ highisland_cliff_forceused = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "You notice one slab that’s wider than the others, and use it as the starting point. You reach a larger chunk of the broken stairs, and while the bronze structure protests with a loud screech, it won’t collapse any time soon. You reach out to one of your companions and help them join you."
                    jump highisland_howlers_landing02
                'I can’t shorten the distance quickly. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0 and not highisland_cliff_forceused" ):
                    pass
                'The bone hook will make it {i}much{/i} easier.' if item_bonehook and not highisland_cliff_graplinghookused:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bone hook will make it {i}much{/i} easier.')
                    $ highisland_cliff_graplinghookused = 1
                    $ highisland_cliff_hp -= 2
                    $ custom1 = "You give it a shot - not only does the hook allow you to climb up the rope, it also helps you test the durability of the bronze rails and sticking-out roots of plants. You reach the higher spots of the wall quickly, followed by the rest of the group."
                    jump highisland_howlers_landing02
                'The claw-tool I picked at {color=#f6d6bd}Pelt{/color} may be of use here.' if (item_peltnorthberrytools and not highisland_cliff_peltnorthberrytools) or (item_peltnorthberryclaw and not highisland_cliff_peltnorthberrytools):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The claw-tool I picked at {color=#f6d6bd}Pelt{/color} may be of use here.')
                    $ highisland_cliff_peltnorthberrytools = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "You make sure the claw is properly tied to the shaft, then seek a wide crack in the wall. It takes a few hits, but you manage to stick it into a wider gap and get to a bit higher spot, where you secure the rope for your companions."
                    jump highisland_howlers_landing02
                '{image=d6} I’ve got no more tricks. Time to climb.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ve got no more tricks. Time to climb.')
                    jump highisland_howlers_landing03

        label highisland_howlers_landing03:
            $ d100roll = renpy.random.randint(1, 100)
            $ at_unlock_force = 0
            $ at = 0
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            $ d100roll += (highisland_cliff_hp*20)
            if d100roll <= 40:
                $ custom1 = "With the bright night on your side, you look for ledges to support you, and avoid the shining, wet rocks."
                label highisland_howlers_landing04:
                    menu:
                        '[custom1] Finally, you pull yourself up, into the dark mouth of the cave - the remains of the original stream.
                        '
                        'I light up a torch and examine the area.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I light up a torch and examine the area.')
                            $ highisland_destination = "cave1"
                            jump highisland_destination
            else:
                $ custom1 = "With the bright night on your side, you look for convenient ledges, but one of the steps betrays you - you slide off, painfully scratching your knee against the wall. You take a deep breath and carry on, your limbs growing quite tired, but you manage to reach the top. You pull yourself up, into the dark mouth of the cave - the remains of the original stream. "
                if pc_food > 0:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    $ custom1 = "With the bright night on your side, you look for convenient ledges, but one of the steps betrays you - you slide off, painfully smashing your jaw against a rock, then hit the floor with your tense back. You feel no pain."
                    jump highisland_gameover
                menu:
                    '[custom1]
                    '
                    'I light up a torch and examine the area.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I light up a torch and examine the area.')
                        $ highisland_destination = "cave1"
                        jump highisland_destination

    label highisland_crew_landingALL:
        label highisland_crew_landing01:
            $ at_unlock_force = 0
            $ at = 0
            if quintus_highisland_joined and not quintus_highisland_blocked:
                $ highisland_cliff_crewhelped_points += 1
            if tzvi_highisland_joined and not tzvi_highisland_blocked:
                $ highisland_cliff_crewhelped_points += 1
            if tulia_highisland_joined and not tulia_highisland_blocked:
                $ highisland_cliff_crewhelped_points += 1
            if thyrsus_highisland_joined and not thyrsus_highisland_blocked:
                $ highisland_cliff_crewhelped_points += 1
            $ highisland_cliff_crewhelped_available = 0
            if not highisland_cliff_crewhelped and highisland_cliff_crewhelped_points < 2:
                if (highisland_crew_left >= 4) or (highisland_crew_left >= 3 and navica_highisland_joined):
                    $ highisland_cliff_crewhelped_available = 1
            if pc_class == "warrior" and not highisland_cliff_forceused:
                $ at_unlock_force = 1
                $ at = 0
            menu:
                'The cave behind the waterfall is maybe thirty feet above you, but getting to it will take some effort. The ancient stairs and handrails have mostly fallen apart, and the slippery rocks are nothing less than a trap.
                '
                'I shorten the distance with a few confident jumps.' ( condition="at == 'force' and not highisland_cliff_forceused" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shorten the distance with a few confident jumps.')
                    $ highisland_cliff_forceused = 1
                    $ highisland_cliff_hp -= 2
                    $ custom1 = "You notice one slab that’s wider than the others, and use it as the starting point. You reach a larger chunk of the broken stairs, and while the bronze structure protests with a loud screech, it won’t collapse any time soon. You reach out to one of your companions and help them join you."
                    jump highisland_crew_landing02
                'I can’t shorten the distance quickly. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0 and not highisland_cliff_forceused" ):
                    pass
                '“{color=#f6d6bd}Thyrsus{/color}, put these creepers to use.”' if thyrsus_highisland_joined and not thyrsus_highisland_blocked and not highisland_cliff_thyrsushelped:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, put these creepers to use.”')
                    $ highisland_cliff_thyrsushelped = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "“Sure.” He stretches them out, not only easily grasping the nearest roots and broken stairs, but also supporting your back as you try to move."
                    jump highisland_crew_landing02
                'I reach out to {color=#f6d6bd}Tulia{/color}. “Together?”' if tulia_highisland_joined and not tulia_highisland_blocked and not highisland_cliff_tuliahelped:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach out to {color=#f6d6bd}Tulia{/color}. “Together?”')
                    $ highisland_cliff_tuliahelped = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "She chuckles, and spends the rest of the climb by your side, securing you with her uncanny strength. Her wet, shaved head is shining in the moonlight."
                    jump highisland_crew_landing02
                '“{color=#f6d6bd}Tzvi{/color}, take a rope and go first. We’ll climb after you.”' if tzvi_highisland_joined and not tzvi_highisland_blocked and not highisland_cliff_tzvihelped:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tzvi{/color}, take a rope and go first. We’ll climb after you.”')
                    $ highisland_cliff_tzvihelped = 1
                    $ highisland_cliff_hp -= 2
                    $ custom1 = "He snorts, but then rolls up his cloak and easily jumps between the shelves. He attaches the rope to one of the rods that stick out of the wall, allowing you to follow him."
                    jump highisland_crew_landing02
                'I nod at {color=#f6d6bd}Quintus{/color}. “Lift us up to that high ledge. You’ll go last.”' if quintus_highisland_joined and not quintus_highisland_blocked and not highisland_cliff_quintushelped:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod at {color=#f6d6bd}Quintus{/color}. “Lift us up to that high ledge. You’ll go last.”')
                    $ highisland_cliff_quintushelped = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "He bends his knees and clasps his fingers, forming a helpful step that lets everyone reach the highest shelf."
                    jump highisland_crew_landing02
                '“We have five strong souls here... Let’s move slowly, helping each other at every step.”' if (highisland_cliff_crewhelped_available and not highisland_cliff_crewhelped):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have five strong souls here... Let’s move slowly, helping each other at every step.”')
                    $ highisland_cliff_crewhelped = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "Having someone always waiting in the back to help the others climb up may slow you down, but your progress is indisputable, and you have enough time to secure a safe way back."
                    jump highisland_crew_landing02
                'The bone hook will make it {i}much{/i} easier.' if item_bonehook and not highisland_cliff_graplinghookused:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bone hook will make it {i}much{/i} easier.')
                    $ highisland_cliff_graplinghookused = 1
                    $ highisland_cliff_hp -= 2
                    $ custom1 = "You give it a shot - not only does the hook allow you to climb up the rope, it also helps you test the durability of the bronze rails and sticking-out roots of plants. You reach the higher spots of the wall quickly, followed by the rest of the group."
                    jump highisland_crew_landing02
                'The claw-tool I picked at {color=#f6d6bd}Pelt{/color} may be of use here.' if (item_peltnorthberrytools and not highisland_cliff_peltnorthberrytools) or (item_peltnorthberryclaw and not highisland_cliff_peltnorthberrytools):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The claw-tool I picked at {color=#f6d6bd}Pelt{/color} may be of use here.')
                    $ highisland_cliff_peltnorthberrytools = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "You make sure the claw is properly tied to the shaft, then seek a wide crack in the wall. It takes a few hits, but you manage to stick it into a wider gap and get to a spot that’s a bit higher up, where you secure the rope for your companions."
                    jump highisland_crew_landing02
                '{image=d6} I’ve got no more tricks. Time to climb.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ve got no more tricks. Time to climb.')
                    jump highisland_crew_landing03

        label highisland_crew_landing02:
            $ at_unlock_force = 0
            $ at = 0
            $ highisland_cliff_crewhelped_available = 0
            if not highisland_cliff_crewhelped and highisland_cliff_crewhelped_points < 2:
                if (highisland_crew_left >= 4) or (highisland_crew_left >= 3 and navica_highisland_joined):
                    $ highisland_cliff_crewhelped_available = 1
            if highisland_cliff_hp <= 0:
                jump highisland_crew_landing04
            if pc_class == "warrior" and not highisland_cliff_forceused:
                $ at_unlock_force = 1
                $ at = 0
            menu:
                '[custom1]
                '
                'I shorten the distance with a few confident jumps.' ( condition="at == 'force' and not highisland_cliff_forceused" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shorten the distance with a few confident jumps.')
                    $ highisland_cliff_forceused = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "You notice one slab that’s wider than the others, and use it as the starting point. You reach a larger chunk of the broken stairs, and while the bronze structure protests with a loud screech, it won’t collapse any time soon. You reach out to one of your companions and help them join you."
                    jump highisland_crew_landing02
                'I can’t shorten the distance quickly. (Required vitality: 1) (disabled)' ( condition="at != 'force' and at_unlock_force and pc_hp <= 0 and not highisland_cliff_forceused" ):
                    pass
                '“{color=#f6d6bd}Thyrsus{/color}, put these creepers to use.”' if thyrsus_highisland_joined and not thyrsus_highisland_blocked and not highisland_cliff_thyrsushelped:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thyrsus{/color}, put these creepers to use.”')
                    $ highisland_cliff_thyrsushelped = 1
                    $ highisland_cliff_hp -= 2
                    $ custom1 = "“Sure.” He stretches them out, not only easily grasping the nearest roots and broken stairs, but also supporting your back as you try to move."
                    jump highisland_crew_landing02
                'I reach out to {color=#f6d6bd}Tulia{/color}. “Together?”' if tulia_highisland_joined and not tulia_highisland_blocked and not highisland_cliff_tuliahelped:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach out to {color=#f6d6bd}Tulia{/color}. “Together?”')
                    $ highisland_cliff_tuliahelped = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "She chuckles, and spends the rest of the climb by your side, securing you with her uncanny strength. Her wet, shaved head is shining in the moonlight."
                    jump highisland_crew_landing02
                '“{color=#f6d6bd}Tzvi{/color}, take a rope and go first. We’ll climb after you.”' if tzvi_highisland_joined and not tzvi_highisland_blocked and not highisland_cliff_tzvihelped:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tzvi{/color}, take a rope and go first. We’ll climb after you.”')
                    $ highisland_cliff_tzvihelped = 1
                    $ highisland_cliff_hp -= 2
                    $ custom1 = "He snorts, but then rolls up his cloak and easily jumps between the shelves. He attaches the rope to one of the rods that stick out of the wall, allowing you to follow him."
                    jump highisland_crew_landing02
                'I nod at {color=#f6d6bd}Quintus{/color}. “Lift us up to that high ledge. You’ll go last.”' if quintus_highisland_joined and not quintus_highisland_blocked and not highisland_cliff_quintushelped:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod at {color=#f6d6bd}Quintus{/color}. “Lift us up to that high ledge. You’ll go last.”')
                    $ highisland_cliff_quintushelped = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "He bends his knees and clasps his fingers, forming a helpful step that lets everyone reach the highest shelf."
                    jump highisland_crew_landing02
                '“We have five strong souls here... Let’s move slowly, helping each other at every step.”' if (highisland_cliff_crewhelped_available and not highisland_cliff_crewhelped):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have five strong souls here... Let’s move slowly, helping each other at every step.”')
                    $ highisland_cliff_crewhelped = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "Having someone always waiting in the back to help the others climb up may slow you down, but your progress is indisputable, and you have enough time to secure a safe way back."
                    jump highisland_crew_landing02
                'The bone hook will make it {i}much{/i} easier.' if item_bonehook and not highisland_cliff_graplinghookused:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bone hook will make it {i}much{/i} easier.')
                    $ highisland_cliff_graplinghookused = 1
                    $ highisland_cliff_hp -= 2
                    $ custom1 = "You give it a shot - not only does the hook allow you to climb up the rope, it also helps you test the durability of the bronze rails and sticking-out roots of plants. You reach the higher spots of the wall quickly, followed by the rest of the group."
                    jump highisland_crew_landing02
                'The claw-tool I picked at {color=#f6d6bd}Pelt{/color} may be of use here.' if (item_peltnorthberrytools and not highisland_cliff_peltnorthberrytools) or (item_peltnorthberryclaw and not highisland_cliff_peltnorthberrytools):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- The claw-tool I picked at {color=#f6d6bd}Pelt{/color} may be of use here.')
                    $ highisland_cliff_peltnorthberrytools = 1
                    $ highisland_cliff_hp -= 1
                    $ custom1 = "You make sure the claw is properly tied to the shaft, then seek a wide crack in the wall. It takes a few hits, but you manage to stick it into a wider gap and get to a spot that’s a bit higher up, where you secure the rope for your companions."
                    jump highisland_crew_landing02
                '{image=d6} I’ve got no more tricks. Time to climb.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I’ve got no more tricks. Time to climb.')
                    jump highisland_crew_landing03

        label highisland_crew_landing03:
            $ d100roll = renpy.random.randint(1, 100)
            $ at_unlock_force = 0
            $ at = 0
            if not pc_food:
                $ d100roll += 5
            if pc_food == 3:
                $ d100roll -= 5
            if pc_food == 4:
                $ d100roll -= 10
            if armor == 4:
                $ d100roll -= 5
            $ d100roll += (highisland_cliff_hp*20)
            if d100roll <= 40:
                $ custom1 = "With the bright night on your side, you look for ledges to support you, and avoid the shining, wet rocks."
                label highisland_crew_landing04:
                    menu:
                        '[custom1] Finally, you pull yourself up, into the dark mouth of the cave - the remains of the original stream.
                        '
                        'I light up a torch and examine the area.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I light up a torch and examine the area.')
                            $ highisland_destination = "cave1"
                            jump highisland_destination
            else:
                $ custom1 = "With the bright night on your side, you look for convenient ledges, but one of the steps betrays you - you slide off, painfully scratching your knee against the wall. You take a deep breath and carry on, your limbs growing quite tired, but you manage to reach the top. You pull yourself up, into the dark mouth of the cave - the remains of the original stream. "
                if pc_food > 0:
                    $ pc_food = limit_pc_food(pc_food-2)
                    show minus2food at foodchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 nourishment points.{/i}')
                elif pc_hp > 0:
                    $ pc_hp = limit_pc_hp(pc_hp-1)
                    show minus1hp at hpchange onlayer myoverlay
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                else:
                    $ custom1 = "With the bright night on your side, you look for convenient ledges, but one of the steps betrays you - you slide off, painfully smashing your jaw against a rock, then hit the floor with your tense back. You feel no pain."
                    jump highisland_gameover
                menu:
                    '[custom1]
                    '
                    'I light up a torch and examine the area.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I light up a torch and examine the area.')
                        $ highisland_destination = "cave1"
                        jump highisland_destination
