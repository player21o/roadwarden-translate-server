####################################### TENT
default pyrrhos_dead = 0
default pyrrhos_deathcounter_unmet = 10
default pyrrhos_ruinedvillage_fluff = ""
default pyrrhos_ruinedvillage_fluff_old = ""
default ruinedvillage_camp_UNLOCKED = 0
default pyrrhos_friendship = 0
default pyrrhos_firstattitude = 0

default pyrrhos_saving_base = 0
default pyrrhos_fed = 0
default pyrrhos_deathcounter_met = 0
default pyrrhos_foodcounter = 0
default pyrrhos_quest_counter = 0
default pyrrhos_quest_question1 = 0
default pyrrhos_quest_question2 = 0
default pyrrhos_quest_question3 = 0
default pyrrhos_about_himselfinpeltnorth = 0
default pyrrhos_about_himself = 0
default pyrrhos_about_goblins = 0
default pyrrhos_about_undead = 0
default pyrrhos_about_curse = 0
default pyrrhos_about_thingsleftbehind = 0
default pyrrhos_about_ruins = 0
default pyrrhos_about_bandits = 0
default pyrrhos_about_asterion = 0
default pyrrhos_about_newplace = 0
default pyrrhos_about_peninsula = 0

default pyrrhos_quest_weapon = 0

default pyrrhos_quest_tohowlersdell = 0
default pyrrhos_quest_canpelt = 0
default pyrrhos_quest_escorting = 0
default pyrrhos_quest_saved = 0
default pyrrhos_quest_potion = 0
default pyrrhos_quest_monstersdevoured = 0
default pyrrhos_quest_griffons = 0
default pyrrhos_quest_griffons_spared = 0
default pyrrhos_quest_reward_debt = 0
default pyrrhos_quest_reward_debt_paid = 0

default pyrrhos_peltnorth = 0
default pyrrhos_peltnorth_counter = 0
default pyrrhos_peltnorth_fluff = ""
default pyrrhos_peltnorth_fluff_old = ""

default pyrrhos_howlersdell = 0
default pyrrhos_howlersdell_himself = 0
default pyrrhos_howlersdell_arrivalcounter = 0
default pyrrhos_howlersdell_fluff = ""
default pyrrhos_howlersdell_about_returning = 0

default pyrrhos_about_ironingot = 0
default pyrrhos_gave_ironingot = 0
default pyrrhos_debt = 0

default pyrrhos_about_highisland_recruitment = 0
default pyrrhos_about_highisland_recruitment_done = 0
default pyrrhos_highisland_joined = 0

#######################################

label ruinedvillage01scavengerscamp01ALL:
    label ruinedvillage01scavengerscamp01firsttime:
        show areapicture ruinedvillagetent01half at basicfade
        $ at_activate = 1
        $ at = 0
        $ world_known_npcs += 1
        $ pyrrhos_saving_base += (day+3)
        if game_mode == 1 or difficultypick_advanced_questseasier:
            $ pyrrhos_saving_base += 5
        $ pyrrhos_deathcounter_met = (day+3)
        $ pyrrhos_quest_counter = day
        menu:
            'You step cautiously, toward the scent of urine and sweat. The flickering candle light shows you broken furniture, yet no signs of burnt wood.
            \n\nYou consider pulling the other door when a masculine voice proves that your presence is not unnoticed.
            \n\n“I dinnae want it to come to this, ba’stay where ye are. Whatever ye put inside, be it a shoe, a hand, or ye damn thinker, it’ll get a bolt.”
            '
            ' (disabled)' ( condition="at == 0" ):
                pass
            '“Relax, stranger. I’m a roadwarden.”' ( condition="at == 'friendly'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (friendly) “Relax, stranger. I’m a roadwarden.”')
                $ at_activate = 0
                $ at = 0
                $ pyrrhos_firstattitude = "friendly"
                menu:
                    '“And ye chose this place to visit, from all that there are? Even outlaws don’t come here.” He pauses, then goes on before you respond. “It may be yer telling the truth, so let’s say this. My lil ballista here is all pulled and ready, b’ye won’t do anything stupid, right? No running, no jumping around. Show ya hands.”
                    \n\nThe man’s voice lacks confidence, and his accent is tricky for you. He could be from the distant South, but as long as you don’t speak too quickly, you understand one another.
                    \n\nYou don’t hear any other movements, breathing, voices. You lean your axe against the door frame and make sure that your knife is well-hidden.
                    '
                    'I walk inside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk inside.')
                        jump ruinedvillage01scavengerscamp01firsttime02neutral
            '“I’m a roadwarden, so I kind of need my {i}thinker{/i}. Will the boot be enough?”' ( condition="at == 'playful'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (playful) “I’m a roadwarden, so I kind of need my {i}thinker{/i}. Will the boot be enough?”')
                $ at_activate = 0
                $ at = 0
                $ pyrrhos_friendship -= 1
                $ pyrrhos_firstattitude = "playful"
                menu:
                    '“Aren’t ye a funny one,” he growls. “How do I know a droll like ye is telling the truth? Walk slowly, roadster, ay? If ye’re not an outlaw, yer safe. And even if ye are, don’t try anything funny. Leave ya arms out, my lil ballista here is all pulled and ready.”
                    \n\nThe man’s voice is imposing, and his accent is tricky for you. He could be from the distant South, but as long as you don’t speak too quickly, you understand one another.
                    \n\nYou don’t hear any other movements, breathing, voices. You lean your axe against the door frame and make sure that your knife is well-hidden.
                    '
                    'I walk inside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk inside.')
                        jump ruinedvillage01scavengerscamp01firsttime02negative
            '“I’m the new roadwarden. Let’s talk.”' ( condition="at == 'distanced'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (distanced) “I’m the new roadwarden. Let’s talk.”')
                $ at_activate = 0
                $ at = 0
                $ pyrrhos_firstattitude = "distanced"
                menu:
                    'A short pause. “Well, we can talk, we can. Ba’how is it that ye chose this place to visit, from all that there are?” He goes on before you respond. “It may be yer telling the truth, so let’s say this. My lil ballista here is all pulled and ready, b’ye won’t do anything stupid, right? No running, no jumping around. Show ya hands.”
                    \n\nThe man’s voice lacks confidence, and his accent is tricky for you. He could be from the distant South, but as long as you don’t speak too quickly, you understand one another.
                    \n\nYou don’t hear any other movements, breathing, voices. You lean your axe against the door frame and make sure that your knife is well-hidden.
                    '
                    'I walk inside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk inside.')
                        jump ruinedvillage01scavengerscamp01firsttime02neutral
            '“Are you really going to bet everything on a single shot? Don’t miss, or I’ll get angry. Angry enough to swing my axe.”' ( condition="at == 'intimidating'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (intimidating) “Are you really going to bet everything on a single shot? Don’t miss, or I’ll get angry. Angry enough to swing my axe.”')
                $ at_activate = 0
                $ at = 0
                $ pyrrhos_friendship += 1
                $ pyrrhos_firstattitude = "intimidating"
                menu:
                    'You hear a long sigh. “Yer right, yer right. I’m not even a brawler, hear that?” There’s the sound of a heavy object being put on the floor. “That’s my ballista. I’m no threat, ye know, just keeping myself safe, scaring away the outlaws and apemen. Come in, roadster, ba’don’t breathe too deeply, this place reeks.”
                    \n\nThe man’s voice is shaking, and his accent is tricky for you. He could be from the distant South, but as long as you don’t speak too quickly, you understand one another. You don’t hear any other movements, breathing, voices.
                    '
                    'Still holding my weapon, I walk inside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Still holding my weapon, I walk inside.')
                        jump ruinedvillage01scavengerscamp01firsttime02positive
            '“Don’t hurt me, I’m not looking for trouble. I’m a roadwarden.”' ( condition="at == 'vulnerable'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (vulnerable) “Don’t hurt me, I’m not looking for trouble. I’m a roadwarden.”')
                $ at_activate = 0
                $ at = 0
                $ pyrrhos_friendship -= 1
                $ pyrrhos_firstattitude = "vulnerable"
                menu:
                    '“Don’t ye try to fool me,” he scoffs. “No wimp grows to be a roadster, ye wouldn’t come here if you couldn’t handle it.”A brief pause. “Ye can enter, ba’slowly. If ye’re not an outlaw, yer safe. And even if ye are, my lil ballista here is all pulled and ready, b’ye won’t do anything stupid, right? Step slowly, I wanna see ya hands.”
                    \n\nThe man’s voice is imposing, and his accent is tricky for you. He could be from the distant South, but as long as you don’t speak too quickly, you understand one another.
                    \n\nYou don’t hear any other movements, breathing, voices. You lean your axe against the door frame.
                    '
                    'I walk inside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk inside.')
                        jump ruinedvillage01scavengerscamp01firsttime02negative

    label ruinedvillage01scavengerscamp01firsttime02negative:
        show areapicture ruinedvillagetent01 at basicfade
        menu:
            'The dense smell of urine hits you with full force, while the tools and utensils are hard to distinguish from the rubbish. The route to the upper floor is blocked by the collapsed roof and loose, wooden beams. There are scraps of rusting iron and steel on the ground, detached from now destroyed barrels.
            \n\n{color=#f6d6bd}The scavenger{/color} is sitting on a blanket in front of the tent, pointing at you with a loaded crossbow. Not a short man, though a bit skinny. He’s tanned, dark haired, and has seen his share of struggles - there are long claw scars on his left cheek, and another one that would divide his eyebrow in half if it hadn’t been consumed by a fire, just like the rest of his forehead.
            \n\nHis clothes are untainted by vanity. He’s barefoot, in a dirty, linen shirt with rolled up sleeves and simple pants that use a cord for a belt. His long beard and hair are untrimmed and tangled.
            '
            'I sit on the stairs, with raised hands. I’m not a threat.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit on the stairs, with raised hands. I’m not a threat.')
                jump ruinedvillage01scavengerscamp01firsttime03stairs
            'I stand near the door, watching his weapon. I’m prepared.' if pyrrhos_firstattitude != "vulnerable":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand near the door, watching his weapon. I’m prepared.')
                jump ruinedvillage01scavengerscamp01firsttime03ready

    label ruinedvillage01scavengerscamp01firsttime02neutral:
        show areapicture ruinedvillagetent01 at basicfade
        menu:
            'The dense smell of urine hits you with full force, while the tools and utensils are hard to distinguish from the rubbish. The route to the upper floor is blocked by the collapsed roof and loose, wooden beams. There are scraps of rusting iron and steel on the ground, detached from now destroyed barrels.
            \n\n{color=#f6d6bd}The scavenger{/color} is sitting on a blanket in front of the tent, pointing at the floor with his loaded crossbow. Not a short man, though a bit skinny. He’s tanned, dark haired, and has seen his share of struggles - there are long claw scars on his left cheek, and another one that would divide his eyebrow in half if it hadn’t been consumed by a fire, just like the rest of his forehead.
            \n\nHis clothes are untainted by vanity. He’s barefoot, in a dirty, linen shirt with rolled up sleeves and simple pants that use a cord for a belt. His long beard and hair are untrimmed and tangled.
            '
            'I sit on the stairs, with raised hands. I’m not a threat.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit on the stairs, with raised hands. I’m not a threat.')
                jump ruinedvillage01scavengerscamp01firsttime03stairs
            'I stand near the door, watching his weapon. I’m prepared.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand near the door, watching his weapon. I’m prepared.')
                jump ruinedvillage01scavengerscamp01firsttime03ready

    label ruinedvillage01scavengerscamp01firsttime02positive:
        show areapicture ruinedvillagetent01 at basicfade
        menu:
            'The dense smell of urine hits you with full force, while the tools and utensils are hard to distinguish from the rubbish. The route to the upper floor is blocked by the collapsed roof and loose, wooden beams. There are scraps of rusting iron and steel on the ground, detached from now destroyed barrels.
            \n\n{color=#f6d6bd}The scavenger{/color} is sitting on a blanket in front of the tent, right next to his unloaded crossbow. Not a short man, though a bit skinny. He’s tanned, dark haired, and has seen his share of struggles - there are long claw scars on his left cheek, and another one that would divide his eyebrow in half if it hadn’t been consumed by a fire, just like the rest of his forehead.
            \n\nHis clothes are untainted by vanity. He’s barefoot, in a dirty, linen shirt with rolled up sleeves and simple pants that use a cord for a belt. His long beard and hair are untrimmed and tangled.
            '
            'I sit on the stairs. I’m not a threat.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit on the stairs. I’m not a threat.')
                jump ruinedvillage01scavengerscamp01firsttime03stairsb
            'I stand nearby, with a hand on my axe. I’m in control.':
                $ pyrrhos_friendship += 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand nearby, with a hand on my axe. I’m in control.')
                jump ruinedvillage01scavengerscamp01firsttime03control

    label ruinedvillage01scavengerscamp01firsttime03stairs:
        menu:
            'You wipe the dust off the steps, but before you sit down, you hear the man’s annoyed voice. “Now, don’t get too homey! It’s the only place here that’s not just ashes and debris, and I’m not sharing it. Ye better ride ahead, I already piled up whatever hasn’t rotten.”
            \n\nThe candle lights are dancing on his burnt face and arms. He moves his crossbow just enough to make sure he won’t shoot you by accident. “I saw ya horse. Maybe ye could help me, hm? What are ye looking for in this place? Ye don’t sound like yer from the North.”
            '
            '“I want to make sure there are no undead crawling around.”':
                jump ruinedvillage01scavengerscamp01firsttime04undead
            '“I need to get to know the peninsula if I’m going to patrol it.”':
                jump ruinedvillage01scavengerscamp01firsttime04explore
            '“I’m short on dragon bones. I wanted to see if there was anything left behind.”':
                jump ruinedvillage01scavengerscamp01firsttime04coin
            '“I was wondering what caused this place to collapse.”':
                jump ruinedvillage01scavengerscamp01firsttime04knowtruth
            '“I’ve heard about some bandits. They could have a hideout nearby.”' if not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01firsttime04bandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found:
                jump ruinedvillage01scavengerscamp01firsttime04asterion
            'I shrug. “That’s not your problem.”':
                jump ruinedvillage01scavengerscamp01firsttime04mybusiness

    label ruinedvillage01scavengerscamp01firsttime03stairsb:
        menu:
            'You wipe the dust off the steps, but before you sit down, you hear the man’s annoyed voice. “Now, don’t get too homey! It’s the only place here that’s not just ashes and debris, and I’m not sharing it. Ye better ride ahead, I already piled up whatever hasn’t rotten.”
            \n\nThe candle lights are dancing on his burnt face and arms. “I saw ya horse. Maybe ye could help me, hm? What are ye looking for in this place? Ye don’t sound like yer from the North.”
            '
            '“I want to make sure there are no undead crawling around.”':
                jump ruinedvillage01scavengerscamp01firsttime04undead
            '“I need to get to know the peninsula if I’m going to patrol it.”':
                jump ruinedvillage01scavengerscamp01firsttime04explore
            '“I’m short on dragon bones. I wanted to see if there was anything left behind.”':
                jump ruinedvillage01scavengerscamp01firsttime04coin
            '“I was wondering what caused this place to collapse.”':
                jump ruinedvillage01scavengerscamp01firsttime04knowtruth
            '“I’ve heard about some bandits. They could have a hideout nearby.”' if not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01firsttime04bandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found:
                jump ruinedvillage01scavengerscamp01firsttime04asterion
            'I shrug. “That’s not your problem.”':
                jump ruinedvillage01scavengerscamp01firsttime04mybusiness

    label ruinedvillage01scavengerscamp01firsttime03ready:
        menu:
            'He follows your gaze. “Not a good way to make the air warmer, ay? I try to be safe, that’s all. And I can’t let ye stay in my shelter. Ye better ride ahead, I already piled up whatever hasn’t rotten.”
            \n\nThe candle lights are dancing on his burnt face and arms. “I saw ya horse. Maybe ye could help me, hm? What are ye looking for in this place? Ye don’t sound like yer from the North.”
            '
            '“I want to make sure there are no undead crawling around.”':
                jump ruinedvillage01scavengerscamp01firsttime04undead
            '“I need to get to know the peninsula if I’m going to patrol it.”':
                jump ruinedvillage01scavengerscamp01firsttime04explore
            '“I’m short on dragon bones. I wanted to see if there was anything left behind.”':
                jump ruinedvillage01scavengerscamp01firsttime04coin
            '“I was wondering what caused this place to collapse.”':
                jump ruinedvillage01scavengerscamp01firsttime04knowtruth
            '“I’ve heard about some bandits. They could have a hideout nearby.”' if not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01firsttime04bandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found:
                jump ruinedvillage01scavengerscamp01firsttime04asterion
            'I shrug. “That’s not your problem.”':
                jump ruinedvillage01scavengerscamp01firsttime04mybusiness

    label ruinedvillage01scavengerscamp01firsttime03control:
        menu:
            'You touch the head of your axe and the man flinches. His voice is full of resignation. “I have to tell ye, I’m glad yer here. If I stay for much longer, I’ll end up on a pyre or in the fogs. I can’t even share this shelter with ye, there’s no place for another shell, even more so a horse.”
            \n\nThe candle lights are dancing on his burnt face and arms. “What are ye looking for in this place? Ye don’t sound like yer from the North.”
            '
            '“I want to make sure there are no undead crawling around.”':
                jump ruinedvillage01scavengerscamp01firsttime04undead
            '“I need to get to know the peninsula if I’m going to patrol it.”':
                jump ruinedvillage01scavengerscamp01firsttime04explore
            '“I’m short on dragon bones. I wanted to see if there was anything left behind.”':
                jump ruinedvillage01scavengerscamp01firsttime04coin
            '“I was wondering what caused this place to collapse.”':
                jump ruinedvillage01scavengerscamp01firsttime04knowtruth
            '“I’ve heard about some bandits. They could have a hideout nearby.”' if not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01firsttime04bandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if quest_asterion == 1 and not asterion_found:
                jump ruinedvillage01scavengerscamp01firsttime04asterion
            'I shrug. “That’s not your problem.”':
                jump ruinedvillage01scavengerscamp01firsttime04mybusiness

        label ruinedvillage01scavengerscamp01firsttime04undead:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to make sure there are no undead crawling around.”')
            $ pyrrhos_about_undead = 1
            if quest_ruins == 1 and not quest_ruins_description01:
                $ quest_ruins_description01 = "I heard that the village was destroyed almost ten years ago."
                $ renpy.notify("Journal updated: The Ruined Village")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
            menu:
                'He nods. “I’ve seen none. People say it’s been less than ten years since the herds came here, b’I don’t know if anyone bothered with raising the pyres. If not, the dead are all roaming in the forest now.” He clicks his tongue with frustration. “It may be that there’s a walker somewhere under the debris, waiting to break through like a dragon in an egg.” He looks straight at you. “Ay, ye’d better not dig.”
                \n\n“Listen,” He scratches his thighs nervously. “I’m hungry, so damn hungry. I can’t hunt or fish with all the apemen around. Can ye share anything, roadster? I may be a drifter, b’I wouldn’t beg if I had not lost my bags on the road.”
                '
                '“Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”' ( condition="item_rations > 1" ):
                    $ item_rations = limit_item_rations(item_rations-2)
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 2
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave2
                '“Take these cereals and crackers. With some water you’ll have a gruel.”' ( condition="item_rations" ):
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 1
                    $ item_rations = limit_item_rations(item_rations-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take these cereals and crackers. With some water you’ll have a gruel.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave1
                '(lie) “I’m sorry, I don’t have anything.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’m sorry, I don’t have anything.”')
                    $ pc_lies += 1
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I need to save it for myself.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to save it for myself.”')
                    jump ruinedvillage01scavengerscamp01firsttime05ihavetosave
                'I don’t have anything I could give him. (disabled)' ( condition="not item_rations" ):
                    pass
                '“I’m sorry, I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m sorry, I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I may have something later on.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may have something later on.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave

        label ruinedvillage01scavengerscamp01firsttime04explore:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to get to know the peninsula if I’m going to patrol it.”')
            menu:
                '“Then better stay away from the eastern paths, no shell rides there anyway. B’even the West and the coast have roads like moosecrap. I’ve traveled and peddled for years now, ye know? I wait for some group to join. And here? People don’t travel, or know damn anything about anyplace. Just a waste of time, I tell ye.” A long pause.
                \n\n“Listen,” He scratches his thighs nervously. “I’m hungry, so damn hungry. I can’t hunt or fish with all the apemen around. Can ye share anything, roadster? I may be a drifter, b’I wouldn’t beg if I had not lost my bags on the road.”
                '
                '“Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”' ( condition="item_rations > 1" ):
                    $ item_rations = limit_item_rations(item_rations-2)
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 2
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave2
                '“Take these cereals and crackers. With some water you’ll have a gruel.”' ( condition="item_rations" ):
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 1
                    $ item_rations = limit_item_rations(item_rations-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take these cereals and crackers. With some water you’ll have a gruel.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave1
                '(lie) “I’m sorry, I don’t have anything.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’m sorry, I don’t have anything.”')
                    $ pc_lies += 1
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I need to save it for myself.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to save it for myself.”')
                    jump ruinedvillage01scavengerscamp01firsttime05ihavetosave
                'I don’t have anything I could give him. (disabled)' ( condition="not item_rations" ):
                    pass
                '“I’m sorry, I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m sorry, I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I may have something later on.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may have something later on.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave

        label ruinedvillage01scavengerscamp01firsttime04coin:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m short on dragon boness. I wanted to see if there was anything left behind.”')
            $ pyrrhos_about_thingsleftbehind += 1
            $ pyrrhos_friendship += 1
            menu:
                '“Aren’t we all, aren’t we all,” he smiles. “You came to the wrong place. Time, moisture, and the damn borers devoured all the loot. I’ve been here for a couple of days now, and all that’s left is this iron I carried here. I was planning to get back here with some hired muscle and clear the collapsed buildings, b’I doubt it’s worth the time and risk.”
                \n\n“So, listen...” He scratches his thighs and you ask what’s bothering him. He sighs, but doesn’t look away. “I’m hungry, so damn hungry. I can’t hunt or fish with all the apemen around. Can ye share anything, roadster? I may be a drifter, b’I wouldn’t beg if I had not lost my bags on the road.”
                '
                '“Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”' ( condition="item_rations > 1" ):
                    $ item_rations = limit_item_rations(item_rations-2)
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 2
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave2
                '“Take these cereals and crackers. With some water you’ll have a gruel.”' ( condition="item_rations" ):
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 1
                    $ item_rations = limit_item_rations(item_rations-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take these cereals and crackers. With some water you’ll have a gruel.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave1
                '(lie) “I’m sorry, I don’t have anything.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’m sorry, I don’t have anything.”')
                    $ pc_lies += 1
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I need to save it for myself.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to save it for myself.”')
                    jump ruinedvillage01scavengerscamp01firsttime05ihavetosave
                'I don’t have anything I could give him. (disabled)' ( condition="not item_rations" ):
                    pass
                '“I’m sorry, I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m sorry, I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I may have something later on.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may have something later on.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave

        label ruinedvillage01scavengerscamp01firsttime04knowtruth:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was wondering what caused this place to collapse.”')
            $ pyrrhos_about_ruins += 1
            menu:
                '“Well, I won’t guess, but I saw many ruins. There’s no treasure and skeletons here, so this place means as much as dirt. Someone was barking too loud, so the beasts broke through and made them quiet again,” he clicks his tongue. “And that’s that. Talking about nature’s fury brings bad luck, don’t ye know?”
                \n\n“Listen,” He scratches his thighs nervously. “I’m hungry, so damn hungry. I can’t hunt or fish with all the apemen around. Can ye share anything, roadster? I may be a drifter, b’I wouldn’t beg if I had not lost my bags on the road.”
                '
                '“Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”' ( condition="item_rations > 1" ):
                    $ item_rations = limit_item_rations(item_rations-2)
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 2
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave2
                '“Take these cereals and crackers. With some water you’ll have a gruel.”' ( condition="item_rations" ):
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 1
                    $ item_rations = limit_item_rations(item_rations-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take these cereals and crackers. With some water you’ll have a gruel.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave1
                '(lie) “I’m sorry, I don’t have anything.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’m sorry, I don’t have anything.”')
                    $ pc_lies += 1
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I need to save it for myself.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to save it for myself.”')
                    jump ruinedvillage01scavengerscamp01firsttime05ihavetosave
                'I don’t have anything I could give him. (disabled)' ( condition="not item_rations" ):
                    pass
                '“I’m sorry, I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m sorry, I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I may have something later on.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may have something later on.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave

        label ruinedvillage01scavengerscamp01firsttime04bandits:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. They could have a hideout nearby.”')
            $ pyrrhos_about_bandits = 1
            menu:
                '“Nah, I think they are in the North, or East. I stuck to the western road and no shell bothered me. Sorry, can’t help ye.”
                \n\n“Listen,” He scratches his thighs nervously. “I’m hungry, so damn hungry. I can’t hunt or fish with all the apemen around. Can ye share anything, roadster? I may be a drifter, b’I wouldn’t beg if I had not lost my bags on the road.”
                '
                '“Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”' ( condition="item_rations > 1" ):
                    $ item_rations = limit_item_rations(item_rations-2)
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 2
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave2
                '“Take these cereals and crackers. With some water you’ll have a gruel.”' ( condition="item_rations" ):
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 1
                    $ item_rations = limit_item_rations(item_rations-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take these cereals and crackers. With some water you’ll have a gruel.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave1
                '(lie) “I’m sorry, I don’t have anything.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’m sorry, I don’t have anything.”')
                    $ pc_lies += 1
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I need to save it for myself.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to save it for myself.”')
                    jump ruinedvillage01scavengerscamp01firsttime05ihavetosave
                'I don’t have anything I could give him. (disabled)' ( condition="not item_rations" ):
                    pass
                '“I’m sorry, I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m sorry, I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I may have something later on.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may have something later on.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave

        label ruinedvillage01scavengerscamp01firsttime04asterion:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”')
            $ pyrrhos_about_asterion += 1
            $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
            menu:
                '“Ay, I’ve never met him, b’I surely heard this name many times. He vanished long before I got to the coast. At first, people were asking about him. Now they think he’s dead.”
                \n\n“Listen,” He scratches his thighs nervously. “I’m hungry, so damn hungry. I can’t hunt or fish with all the apemen around. Can ye share anything, roadster? I may be a drifter, b’I wouldn’t beg if I had not lost my bags on the road.”
                '
                '“Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”' ( condition="item_rations > 1" ):
                    $ item_rations = limit_item_rations(item_rations-2)
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 2
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave2
                '“Take these cereals and crackers. With some water you’ll have a gruel.”' ( condition="item_rations" ):
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 1
                    $ item_rations = limit_item_rations(item_rations-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take these cereals and crackers. With some water you’ll have a gruel.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave1
                '(lie) “I’m sorry, I don’t have anything.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’m sorry, I don’t have anything.”')
                    $ pc_lies += 1
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I need to save it for myself.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to save it for myself.”')
                    jump ruinedvillage01scavengerscamp01firsttime05ihavetosave
                'I don’t have anything I could give him. (disabled)' ( condition="not item_rations" ):
                    pass
                '“I’m sorry, I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m sorry, I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I may have something later on.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may have something later on.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave

        label ruinedvillage01scavengerscamp01firsttime04mybusiness:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug. “That’s not your problem.”')
            $ pyrrhos_friendship -= 1
            menu:
                'With a groan, he slashes the air between you with his hand. “Sure, I don’t {i}need{/i} to know. Ba’, listen...” He scratches his thighs nervously, then sighs loudly. “I’m hungry, so damn hungry. I can’t hunt or fish with all the apemen around. Can ye share anything, roadster? I may be a drifter, b’I wouldn’t beg if I had not lost my bags on the road.”
                '
                '“Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”' ( condition="item_rations > 1" ):
                    $ item_rations = limit_item_rations(item_rations-2)
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 2
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here. I have a few prunes, a sausage, and some nuts. Should be enough for tomorrow as well.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave2
                '“Take these cereals and crackers. With some water you’ll have a gruel.”' ( condition="item_rations" ):
                    $ pyrrhos_friendship += 1
                    $ pyrrhos_fed += 1
                    $ item_rations = limit_item_rations(item_rations-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Take these cereals and crackers. With some water you’ll have a gruel.”')
                    jump ruinedvillage01scavengerscamp01firsttime05gave1
                '(lie) “I’m sorry, I don’t have anything.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’m sorry, I don’t have anything.”')
                    $ pc_lies += 1
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I need to save it for myself.”' ( condition="item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to save it for myself.”')
                    jump ruinedvillage01scavengerscamp01firsttime05ihavetosave
                'I don’t have anything I could give him. (disabled)' ( condition="not item_rations" ):
                    pass
                '“I’m sorry, I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m sorry, I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I don’t have anything.”' ( condition="not item_rations" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have anything.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave
                '“I may have something later on.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may have something later on.”')
                    jump ruinedvillage01scavengerscamp01firsttime05idonthave

label ruinedvillage01scavengerscamp01firsttime05gave2:
    $ pyrrhos_foodcounter = day
    $ renpy.notify("You gave away two food rations.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away two food rations.{/i}')
    menu:
        '“Ha! Ye say so, b’ye don’t know my dearth.” He bites into the sausage right away, but after a couple of solid bites, he puts your gifts on an unfolded tunic that’s lying on the floor. “Without ya, I would have to run after birds with my ballista, b’I need to save the bolts for the apemen. And because of those stinkers, I can’t roast here, and raw meat makes me want to puke. Thank ye.”
        \n\nAfter a moment of hesitation, he grabs one of the plums. “Now, roadster,” he says with a full mouth. “If you have questions, ask. I’ll say a lot to make ye get me out of here.”
        '
        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
            jump ruinedvillage01scavengerscamp01aboutironingot01
        'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
            pass
        'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutquest
        '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
            jump ruinedvillage01scavengerscamp01aboutgettingsick
        '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
            jump ruinedvillage01scavengerscamp01abouthimself
        'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
            pass
        '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
            jump ruinedvillage01scavengerscamp01broughtfood
        '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutgoblins
        '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
            jump ruinedvillage01scavengerscamp01aboutundead
        '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
            jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
        '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
            jump ruinedvillage01scavengerscamp01aboutruins
        '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
            jump ruinedvillage01scavengerscamp01aboutbandits
        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
            jump ruinedvillage01scavengerscamp01aboutasterion
        '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
            jump ruinedvillage01scavengerscamp01leavingdell
        '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
            jump ruinedvillage01scavengerscamp01leavingspear
        'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
            pass
        '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
            jump ruinedvillage01scavengerscamp01aboutquestBquestions
        'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
            pass
        'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
            pass
        'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
            pass
        '“Time for me to leave.”' if quest_escortpyrrhos:
            hide areapicture
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
            jump ruinedvillageselectarea

    label ruinedvillage01scavengerscamp01firsttime05gave1:
        $ pyrrhos_foodcounter = day
        $ renpy.notify("You gave away a food ration.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away a food ration.{/i}')
        menu:
            'He lets out a relieved breath. “Ay, I may even boil it.” After a moment of hesitation, he grabs a cracker. “Without ya, I would have to run after birds with my ballista, b’I need to save the bolts for the apemen. And because of those stinkers, I can’t roast here, and raw meat makes me want to puke. Thank ye.”
            \n\nAfter a couple of solid bites, he puts your gifts in two wooden bowls. “Now, roadster,” he says with a full mouth. “If you have questions, ask. I’ll say a lot to make ye get me out of here.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                jump ruinedvillage01scavengerscamp01aboutironingot01
            'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                pass
            'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutquest
            '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                jump ruinedvillage01scavengerscamp01aboutgettingsick
            '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                jump ruinedvillage01scavengerscamp01abouthimself
            'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                pass
            '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                jump ruinedvillage01scavengerscamp01broughtfood
            '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutgoblins
            '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                jump ruinedvillage01scavengerscamp01aboutundead
            '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
            '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                jump ruinedvillage01scavengerscamp01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                jump ruinedvillage01scavengerscamp01aboutasterion
            '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                jump ruinedvillage01scavengerscamp01leavingdell
            '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                jump ruinedvillage01scavengerscamp01leavingspear
            'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                pass
            '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                jump ruinedvillage01scavengerscamp01aboutquestBquestions
            'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                pass
            'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                pass
            'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                pass
            '“Time for me to leave.”' if quest_escortpyrrhos:
                hide areapicture
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                jump ruinedvillageselectarea

    label ruinedvillage01scavengerscamp01firsttime05idonthave:
        menu:
            '“Just my luck, I tell ye,” he clicks his tongue. “Well, I’ll try to shoot down a bird or two tomorrow. I’m saving my bolts for the apemen. And because of those stinkers, I can’t even roast anything, and raw meat makes me want to puke.” A long sigh. “Everything’s shit, stranger. So, if you have questions, ask. I’ll say a lot to make ye get me out of here.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                jump ruinedvillage01scavengerscamp01aboutironingot01
            'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                pass
            'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutquest
            '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                jump ruinedvillage01scavengerscamp01aboutgettingsick
            '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                jump ruinedvillage01scavengerscamp01abouthimself
            'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                pass
            '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                jump ruinedvillage01scavengerscamp01broughtfood
            '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutgoblins
            '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                jump ruinedvillage01scavengerscamp01aboutundead
            '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
            '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                jump ruinedvillage01scavengerscamp01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                jump ruinedvillage01scavengerscamp01aboutasterion
            '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                jump ruinedvillage01scavengerscamp01leavingdell
            '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                jump ruinedvillage01scavengerscamp01leavingspear
            'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                pass
            '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                jump ruinedvillage01scavengerscamp01aboutquestBquestions
            'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                pass
            'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                pass
            'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                pass
            '“Time for me to leave.”' if quest_escortpyrrhos:
                hide areapicture
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                jump ruinedvillageselectarea

    label ruinedvillage01scavengerscamp01firsttime05ihavetosave:
        menu:
            '“Sure, sure, just my bloody luck,” he clicks his tongue. “I’ll try to shoot down a bird or two tomorrow. I avoid it when I can, I’m saving my bolts for the apemen. And because of those stinkers, I can’t even roast anything, and raw meat makes me want to puke.” A long sigh. “Everything’s shit, stranger. So, if you have questions, ask. I’ll say a lot to make ye get me out of here.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                jump ruinedvillage01scavengerscamp01aboutironingot01
            'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                pass
            'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutquest
            '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                jump ruinedvillage01scavengerscamp01aboutgettingsick
            '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                jump ruinedvillage01scavengerscamp01abouthimself
            'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                pass
            '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                jump ruinedvillage01scavengerscamp01broughtfood
            '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutgoblins
            '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                jump ruinedvillage01scavengerscamp01aboutundead
            '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
            '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                jump ruinedvillage01scavengerscamp01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                jump ruinedvillage01scavengerscamp01aboutasterion
            '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                jump ruinedvillage01scavengerscamp01leavingdell
            '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                jump ruinedvillage01scavengerscamp01leavingspear
            'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                pass
            '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                jump ruinedvillage01scavengerscamp01aboutquestBquestions
            'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                pass
            'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                pass
            'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                pass
            '“Time for me to leave.”' if quest_escortpyrrhos:
                hide areapicture
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                jump ruinedvillageselectarea

    label ruinedvillage01scavengerscamp01regularquestions:
        $ renpy.save("combatsave", extra_info='Combat Auto Save')
        menu:
            '“Ay, we can talk. Go ahead.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                jump ruinedvillage01scavengerscamp01aboutironingot01
            'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                pass
            'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutquest
            '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                jump ruinedvillage01scavengerscamp01aboutgettingsick
            '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                jump ruinedvillage01scavengerscamp01abouthimself
            'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                pass
            '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                jump ruinedvillage01scavengerscamp01broughtfood
            '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutgoblins
            '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                jump ruinedvillage01scavengerscamp01aboutundead
            '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
            '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                jump ruinedvillage01scavengerscamp01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                jump ruinedvillage01scavengerscamp01aboutasterion
            '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                jump ruinedvillage01scavengerscamp01leavingdell
            '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                jump ruinedvillage01scavengerscamp01leavingspear
            'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                pass
            '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                jump ruinedvillage01scavengerscamp01aboutquestBquestions
            'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                pass
            'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                pass
            'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                pass
            '“Time for me to leave.”' if quest_escortpyrrhos:
                hide areapicture
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                jump ruinedvillageselectarea

    label ruinedvillage01scavengerscamp01regularquestionsv02:
        menu:
            '“So, what else bothers ye?”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                jump ruinedvillage01scavengerscamp01aboutironingot01
            'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                pass
            'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutquest
            '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                jump ruinedvillage01scavengerscamp01aboutgettingsick
            '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                jump ruinedvillage01scavengerscamp01abouthimself
            'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                pass
            '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                jump ruinedvillage01scavengerscamp01broughtfood
            '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutgoblins
            '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                jump ruinedvillage01scavengerscamp01aboutundead
            '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
            '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                jump ruinedvillage01scavengerscamp01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                jump ruinedvillage01scavengerscamp01aboutasterion
            '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                jump ruinedvillage01scavengerscamp01leavingdell
            '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                jump ruinedvillage01scavengerscamp01leavingspear
            'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                pass
            '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                jump ruinedvillage01scavengerscamp01aboutquestBquestions
            'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                pass
            'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                pass
            'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                pass
            '“Time for me to leave.”' if quest_escortpyrrhos:
                hide areapicture
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                jump ruinedvillageselectarea

    label ruinedvillage01scavengerscamp01regularquestionsv03:
        menu:
            '“Thanks, roadster! Just come tomorrow, I’ll make it worth ya time.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                jump ruinedvillage01scavengerscamp01aboutironingot01
            'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                pass
            'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutquest
            '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                jump ruinedvillage01scavengerscamp01aboutgettingsick
            '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                jump ruinedvillage01scavengerscamp01abouthimself
            'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                pass
            '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                jump ruinedvillage01scavengerscamp01broughtfood
            '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutgoblins
            '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                jump ruinedvillage01scavengerscamp01aboutundead
            '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
            '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                jump ruinedvillage01scavengerscamp01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                jump ruinedvillage01scavengerscamp01aboutasterion
            '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                jump ruinedvillage01scavengerscamp01leavingdell
            '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                jump ruinedvillage01scavengerscamp01leavingspear
            'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                pass
            '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                jump ruinedvillage01scavengerscamp01aboutquestBquestions
            'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                pass
            'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                pass
            'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                pass
            '“Time for me to leave.”' if quest_escortpyrrhos:
                hide areapicture
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                jump ruinedvillageselectarea

    label ruinedvillage01scavengerscamp01regularquestionsv04:
        menu:
            '“Well, if {i}ye{/i} won’t help me, I’ll save myself.” He scratches the scars on his cheek. “Ba’don’t leave me here, roadster, just come get me tomorrow, it’s easy dragons for ye.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                jump ruinedvillage01scavengerscamp01aboutironingot01
            'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                pass
            'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutquest
            '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                jump ruinedvillage01scavengerscamp01aboutgettingsick
            '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                jump ruinedvillage01scavengerscamp01abouthimself
            'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                pass
            '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                jump ruinedvillage01scavengerscamp01broughtfood
            '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutgoblins
            '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                jump ruinedvillage01scavengerscamp01aboutundead
            '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
            '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                jump ruinedvillage01scavengerscamp01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                jump ruinedvillage01scavengerscamp01aboutasterion
            '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                jump ruinedvillage01scavengerscamp01leavingdell
            '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                jump ruinedvillage01scavengerscamp01leavingspear
            'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                pass
            '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                jump ruinedvillage01scavengerscamp01aboutquestBquestions
            'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                pass
            'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                pass
            'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                pass
            '“Time for me to leave.”' if quest_escortpyrrhos:
                hide areapicture
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01aboutgettingsick:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This village makes me sick.”')
    $ pyrrhos_about_curse = 1
    $ ruinedvillage_clues += 1
    $ quest_ruins_insideclues10 = "I experienced mysterious symptoms of an illness while exploring the village, and the scavenger felt the same thing."
    if quest_ruins == 1:
        $ renpy.notify("Journal updated: The Ruined Village")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
    menu:
        '“Me too, in the guts and the thinker. Gets easier with time, if yer patient. Must be the air, the smell of death. Death and apemen piss!” He pats his stomach while laughing.
        '
        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
            jump ruinedvillage01scavengerscamp01aboutironingot01
        'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
            pass
        'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutquest
        '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
            jump ruinedvillage01scavengerscamp01aboutgettingsick
        '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
            jump ruinedvillage01scavengerscamp01abouthimself
        'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
            pass
        '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
            jump ruinedvillage01scavengerscamp01broughtfood
        '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutgoblins
        '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
            jump ruinedvillage01scavengerscamp01aboutundead
        '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
            jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
        '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
            jump ruinedvillage01scavengerscamp01aboutruins
        '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
            jump ruinedvillage01scavengerscamp01aboutbandits
        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
            jump ruinedvillage01scavengerscamp01aboutasterion
        '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
            jump ruinedvillage01scavengerscamp01leavingdell
        '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
            jump ruinedvillage01scavengerscamp01leavingspear
        'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
            pass
        '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
            jump ruinedvillage01scavengerscamp01aboutquestBquestions
        'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
            pass
        'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
            pass
        'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
            pass
        '“Time for me to leave.”' if quest_escortpyrrhos:
            hide areapicture
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
            jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01abouthimself:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
    if (pyrrhos_friendship+appearance_charisma) < 5 and pyrrhos_firstattitude != "intimidating":
        $ pyrrhos_about_himself = 1
        menu:
            'He gives you a sullen glance. “What for? I’ve no {i}legacy{/i} to keep alive in tales. I may tell ye this and that {i}after{/i} you take me out of here.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                jump ruinedvillage01scavengerscamp01aboutironingot01
            'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                pass
            'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutquest
            '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                jump ruinedvillage01scavengerscamp01aboutgettingsick
            '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                jump ruinedvillage01scavengerscamp01abouthimself
            'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                pass
            '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                jump ruinedvillage01scavengerscamp01broughtfood
            '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutgoblins
            '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                jump ruinedvillage01scavengerscamp01aboutundead
            '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
            '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                jump ruinedvillage01scavengerscamp01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                jump ruinedvillage01scavengerscamp01aboutasterion
            '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                jump ruinedvillage01scavengerscamp01leavingdell
            '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                jump ruinedvillage01scavengerscamp01leavingspear
            'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                pass
            '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                jump ruinedvillage01scavengerscamp01aboutquestBquestions
            'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                pass
            'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                pass
            'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                pass
            '“Time for me to leave.”' if quest_escortpyrrhos:
                hide areapicture
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                jump ruinedvillageselectarea
    else:
        $ pyrrhos_about_himself = 2
        $ description_pyrrhos01 = "He calls himself a drifter and a trader, and isn’t afraid of some more dangerous tasks. He claims that he came here by ship, looking for dragon bones."
        $ description_pyrrhos02 = "He claims that he was healed by powerful magic in the local monastery."
        menu:
            '“I could tell ye stories for days, ba’who cares?” He chuckles. “I’m just doing my own thing, moving from wall to wall, sleeping where they let me, selling what I can, buying what I need, saving dragons for another day. I used to be a sailor, people called me {color=#f6d6bd}Pyrrhos{/color} because of the, ye know,” he points at the burned skin on his forehead. “B’I’m not one to push a plough or patch ship sails all day long. I don’t care if a corpser eats my bones one day. I’d rather be free for a few years than cage myself in fear for decades.”
            \n\n“And I’m damn good at staying safe, or rather I {i}was{/i} before I landed in this shithole.” He touches the scars on his face. “I haven’t gotten one of these in years, b’it didn’t take two weeks and I almost lost my legs. Spent all my coin in {color=#f6d6bd}Howler’s Dell{/color} for elders’ magic. Not the first time I have an empty pouch, not gonna lie, ba’there’s no coin waiting here. Once I push all the iron to the locals, I’m heading south. Though I won’t ride alone, I’m not making that mistake again.”
            '
            '“I’ve heard no ships can land on this coast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard no ships can land on this coast.”')
                jump ruinedvillage01scavengerscamp01abouthimself02
            'He’s probably lying, but I don’t let him know that I’ve noticed it. “I have another question.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s probably lying, but I don’t let him know that I’ve noticed it. “I have another question.”')
                jump ruinedvillage01scavengerscamp01regularquestions

    label ruinedvillage01scavengerscamp01abouthimself02:
        $ pyrrhos_friendship -= 1
        $ quest_explorepeninsula_description03 = "I heard that some of the locals know ways to move safely through the rocky coasts, so it may be possible to maintain access to the sea after all."
        $ description_galerocks04 = "I heard that the fishers from {color=#f6d6bd}Gale Rocks{/color} know how to move between the coastal rocks."
        $ renpy.notify("Journal updated: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
        menu:
            '“Well,” he tilts his head to the right and gives you a distrustful look. “B’if yer patient and take ya time, ye can get to {color=#f6d6bd}Gale Rocks{/color} from the sea. In a light boat, or a raft, or something that can avoid the rocky teeth. Sure, no hope for a ship, or any trade, ba’with some help, ye can do it. Ba’don’t tell anyone I told ye this.” His tone gets significantly colder. “It’s not something people should talk about.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                jump ruinedvillage01scavengerscamp01aboutironingot01
            'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                pass
            'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutquest
            '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                jump ruinedvillage01scavengerscamp01aboutgettingsick
            '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                jump ruinedvillage01scavengerscamp01abouthimself
            'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                pass
            '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                jump ruinedvillage01scavengerscamp01broughtfood
            '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                jump ruinedvillage01scavengerscamp01aboutgoblins
            '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                jump ruinedvillage01scavengerscamp01aboutundead
            '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
            '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                jump ruinedvillage01scavengerscamp01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                jump ruinedvillage01scavengerscamp01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                jump ruinedvillage01scavengerscamp01aboutasterion
            '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                jump ruinedvillage01scavengerscamp01leavingdell
            '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                jump ruinedvillage01scavengerscamp01leavingspear
            'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                pass
            '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                jump ruinedvillage01scavengerscamp01aboutquestBquestions
            'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                pass
            'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                pass
            'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                pass
            'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                pass
            '“Time for me to leave.”' if quest_escortpyrrhos:
                hide areapicture
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01aboutironingot01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”')
    $ pyrrhos_about_ironingot = 1
    menu:
        'He glances at his crossbow, then scowls at you again, knowing he’s not fast enough. “Come on, roadster. Without it I’ll have nothing to sell once I get south.”
        '
        'I observe him in silence.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe him in silence.')
            $ custom1 = "He rephrases his request a few more times, but seeing no change in your gaze, he finally pauses and clicks his tongue. The candle light dances on his burnt face."
            $ pyrrhos_friendship += 1
            jump ruinedvillage01scavengerscamp01aboutironingot02
        '“Don’t try to play me. You stole it long before you lost your belongings.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t try to play me. You stole it long before you lost your belongings.”')
            $ custom1 = "He raises his voice. “Ay, but {i}I{/i} need it more than some fishers.” He looks at you with contempt, the candle light dances on his burnt face."
            $ pyrrhos_friendship -= 1
            jump ruinedvillage01scavengerscamp01aboutironingot02

    label ruinedvillage01scavengerscamp01aboutironingot02:
        menu:
            '[custom1] “Have mercy. Let me keep it, and I’ll be in ya debt. My thinker is heavier than my muscles, but I know how to use my ballista, and I can help ye on a dangerous trip. This ingot is my only path forward, roadster.”
            '
            '“Give me the iron, scavenger. And stay away from your crossbow.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Give me the iron, scavenger. And stay away from your crossbow.”')
                $ item_ironingot += 1
                $ renpy.notify("You received the iron ingot.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the iron ingot.{/i}')
                $ pyrrhos_friendship -= 5
                $ pyrrhos_gave_ironingot = 1
                menu:
                    'Without another word, he crawls deeper into his tent. You prepare your blade, just in case, but the man gets back with the dark ingot held in both of his hands, painfully looking at it. You take it from him, at first underestimating how heavy it is, but {color=#f6d6bd}Pyrrhos{/color} doesn’t risk taking the opportunity.
                    \n\nYou step back. He doesn’t meet your eyes.
                    '
                    'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                        jump ruinedvillage01scavengerscamp01aboutironingot01
                    'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                        pass
                    'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                        jump ruinedvillage01scavengerscamp01aboutquest
                    '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                        jump ruinedvillage01scavengerscamp01aboutgettingsick
                    '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                        jump ruinedvillage01scavengerscamp01abouthimself
                    'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                        pass
                    '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                        jump ruinedvillage01scavengerscamp01broughtfood
                    '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                        jump ruinedvillage01scavengerscamp01aboutgoblins
                    '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                        jump ruinedvillage01scavengerscamp01aboutundead
                    '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                        jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
                    '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                        jump ruinedvillage01scavengerscamp01aboutruins
                    '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                        jump ruinedvillage01scavengerscamp01aboutbandits
                    '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                        jump ruinedvillage01scavengerscamp01aboutasterion
                    '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                        jump ruinedvillage01scavengerscamp01leavingdell
                    '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                        jump ruinedvillage01scavengerscamp01leavingspear
                    'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                        pass
                    'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                        pass
                    '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                        jump ruinedvillage01scavengerscamp01aboutquestBquestions
                    'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                        pass
                    'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                        pass
                    'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                        pass
                    'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                        pass
                    '“Time for me to leave.”' if quest_escortpyrrhos:
                        hide areapicture
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                        jump ruinedvillageselectarea
            '“Very well. But if you try to leave the peninsula before I collect your debt, I won’t be so kind the next time I find you.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. But if you try to leave the peninsula before I collect your debt, I won’t be so kind the next time I find you.”')
                $ pyrrhos_debt = 1
                $ pyrrhos_friendship += 1
                menu:
                    'He spares you a smirk. “Ye have my word. Take me to a safe place, and I’ll wait there for ya call.”
                    '
                    'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                        jump ruinedvillage01scavengerscamp01aboutironingot01
                    'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                        pass
                    'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                        jump ruinedvillage01scavengerscamp01aboutquest
                    '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                        jump ruinedvillage01scavengerscamp01aboutgettingsick
                    '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                        jump ruinedvillage01scavengerscamp01abouthimself
                    'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                        pass
                    '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                        jump ruinedvillage01scavengerscamp01broughtfood
                    '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                        jump ruinedvillage01scavengerscamp01aboutgoblins
                    '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                        jump ruinedvillage01scavengerscamp01aboutundead
                    '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                        jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
                    '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                        jump ruinedvillage01scavengerscamp01aboutruins
                    '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                        jump ruinedvillage01scavengerscamp01aboutbandits
                    '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                        jump ruinedvillage01scavengerscamp01aboutasterion
                    '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                        jump ruinedvillage01scavengerscamp01leavingdell
                    '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                        jump ruinedvillage01scavengerscamp01leavingspear
                    'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                        pass
                    'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                        pass
                    '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                        jump ruinedvillage01scavengerscamp01aboutquestBquestions
                    'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                        pass
                    'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                        pass
                    'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                        pass
                    'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                        pass
                    '“Time for me to leave.”' if quest_escortpyrrhos:
                        hide areapicture
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                        jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01broughtfood:
    $ pyrrhos_fed += 1
    $ pyrrhos_foodcounter = day
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I brought you some food.”')
    $ item_rations = limit_item_rations(item_rations-1)
    $ renpy.notify("You gave away a food ration.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away a food ration.{/i}')
    menu:
        '“I’m ashamed to accept it,” he answers, but takes your gift before you end your last word. He puts it in a bowl and licks his lips. “Now I can stay here for at least a day more without risking a hunt, or wasting my bolts. But it can’t last for much longer, it sure can’t.”
        '
        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
            jump ruinedvillage01scavengerscamp01aboutironingot01
        'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
            pass
        'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutquest
        '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
            jump ruinedvillage01scavengerscamp01aboutgettingsick
        '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
            jump ruinedvillage01scavengerscamp01abouthimself
        'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
            pass
        '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
            jump ruinedvillage01scavengerscamp01broughtfood
        '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutgoblins
        '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
            jump ruinedvillage01scavengerscamp01aboutundead
        '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
            jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
        '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
            jump ruinedvillage01scavengerscamp01aboutruins
        '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
            jump ruinedvillage01scavengerscamp01aboutbandits
        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
            jump ruinedvillage01scavengerscamp01aboutasterion
        '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
            jump ruinedvillage01scavengerscamp01leavingdell
        '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
            jump ruinedvillage01scavengerscamp01leavingspear
        'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
            pass
        '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
            jump ruinedvillage01scavengerscamp01aboutquestBquestions
        'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
            pass
        'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
            pass
        'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
            pass
        '“Time for me to leave.”' if quest_escortpyrrhos:
            hide areapicture
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
            jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01aboutquestBquestions:
    $ pyrrhos_quest_question2 = 1
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”')
    menu:
        '“I mean... I see ya point, b’I’ve never been there. Can they afford my iron, do they have means to pay for it? I need coins to find a handy bunch that will walk south with me, and I need a new staff, and bolts... I know the village, it’s a nice place, and even has a smithy. Of sorts.”
        '
        '“I had a chance to take a look, though. It’s a large, safe inn. They have enough well-equipped hunters to guide you south. I bet they’ll barter service for iron.”':
            $ pyrrhos_quest_canpelt = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I had a chance to take a look, though. It’s a large, safe inn. They have enough well-equipped hunters to guide you south. I bet they’ll barter service for iron.”')
            $ quest_escortpyrrhos_description02 = "I can also take him to {color=#f6d6bd}Pelt{/color}."
            $ renpy.notify("Journal updated: Escort The Scavenger")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Escort The Scavenger{/i}')
            menu:
                '“Well... It’s a shorter path, I guess, fewer spots to get surrounded by corpsers... If yer sure it’s the best option, fine. I’ll trust a roadster’s judgment.”
                '
                'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
                    jump ruinedvillage01scavengerscamp01aboutironingot01
                'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
                    pass
                'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
                    jump ruinedvillage01scavengerscamp01aboutquest
                '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
                    jump ruinedvillage01scavengerscamp01aboutgettingsick
                '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
                    jump ruinedvillage01scavengerscamp01abouthimself
                'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
                    pass
                '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
                    jump ruinedvillage01scavengerscamp01broughtfood
                '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
                    jump ruinedvillage01scavengerscamp01aboutgoblins
                '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
                    jump ruinedvillage01scavengerscamp01aboutundead
                '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                    jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
                '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
                    jump ruinedvillage01scavengerscamp01aboutruins
                '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                    jump ruinedvillage01scavengerscamp01aboutbandits
                '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
                    jump ruinedvillage01scavengerscamp01aboutasterion
                '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
                    jump ruinedvillage01scavengerscamp01leavingdell
                '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
                    jump ruinedvillage01scavengerscamp01leavingspear
                'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
                    pass
                'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
                    pass
                '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
                    jump ruinedvillage01scavengerscamp01aboutquestBquestions
                'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
                    pass
                'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
                    pass
                'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
                    pass
                'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
                    pass
                '“Time for me to leave.”' if quest_escortpyrrhos:
                    hide areapicture
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
                    jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01aboutgoblins:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do you keep the goblins away?”')
    $ pyrrhos_about_goblins = 1
    menu:
        '“I’ve got a trick or two to keep me safe. A little something that scares them away, even without magic. Ba’tell ye what,” his smile turns into a wide grin. “Help me get out of here and I’m going to share some of it with ye.”
        '
        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
            jump ruinedvillage01scavengerscamp01aboutironingot01
        'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
            pass
        'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutquest
        '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
            jump ruinedvillage01scavengerscamp01aboutgettingsick
        '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
            jump ruinedvillage01scavengerscamp01abouthimself
        'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
            pass
        '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
            jump ruinedvillage01scavengerscamp01broughtfood
        '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutgoblins
        '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
            jump ruinedvillage01scavengerscamp01aboutundead
        '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
            jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
        '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
            jump ruinedvillage01scavengerscamp01aboutruins
        '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
            jump ruinedvillage01scavengerscamp01aboutbandits
        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
            jump ruinedvillage01scavengerscamp01aboutasterion
        '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
            jump ruinedvillage01scavengerscamp01leavingdell
        '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
            jump ruinedvillage01scavengerscamp01leavingspear
        'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
            pass
        '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
            jump ruinedvillage01scavengerscamp01aboutquestBquestions
        'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
            pass
        'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
            pass
        'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
            pass
        '“Time for me to leave.”' if quest_escortpyrrhos:
            hide areapicture
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
            jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01aboutundead:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead around?”')
    $ pyrrhos_about_undead = 1
    if quest_ruins == 1 and not quest_ruins_description01:
        $ quest_ruins_description01 = "I heard that the village was destroyed almost ten years ago."
        $ renpy.notify("Journal updated: The Ruined Village")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
    menu:
        'He nods. “I’ve seen none. People say it’s been less than ten years since the herds came here, b’I don’t know if anyone bothered with raising the pyres. If not, the dead are all roaming in the forest now.” He clicks his tongue with frustration. “It may be that there’s a walker somewhere under the debris, waiting to break through like a dragon in an egg.” He looks straight at you. “Ay, ye’d better not dig.”
        '
        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
            jump ruinedvillage01scavengerscamp01aboutironingot01
        'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
            pass
        'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutquest
        '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
            jump ruinedvillage01scavengerscamp01aboutgettingsick
        '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
            jump ruinedvillage01scavengerscamp01abouthimself
        'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
            pass
        '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
            jump ruinedvillage01scavengerscamp01broughtfood
        '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutgoblins
        '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
            jump ruinedvillage01scavengerscamp01aboutundead
        '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
            jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
        '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
            jump ruinedvillage01scavengerscamp01aboutruins
        '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
            jump ruinedvillage01scavengerscamp01aboutbandits
        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
            jump ruinedvillage01scavengerscamp01aboutasterion
        '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
            jump ruinedvillage01scavengerscamp01leavingdell
        '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
            jump ruinedvillage01scavengerscamp01leavingspear
        'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
            pass
        '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
            jump ruinedvillage01scavengerscamp01aboutquestBquestions
        'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
            pass
        'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
            pass
        'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
            pass
        '“Time for me to leave.”' if quest_escortpyrrhos:
            hide areapicture
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
            jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01aboutthingsleftbehind:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire village? Are there no hidden treasures left?”')
    $ pyrrhos_about_thingsleftbehind += 1
    menu:
        '“You came to the wrong place. Time, moisture, and the damn borers devoured all the loot. I’ve been here for a couple of days now, and all that’s left is this iron I carried here. I was planning to get back here with some hired muscle and clear the collapsed buildings, b’I doubt it’s worth the time and risk.”
        '
        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
            jump ruinedvillage01scavengerscamp01aboutironingot01
        'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
            pass
        'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutquest
        '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
            jump ruinedvillage01scavengerscamp01aboutgettingsick
        '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
            jump ruinedvillage01scavengerscamp01abouthimself
        'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
            pass
        '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
            jump ruinedvillage01scavengerscamp01broughtfood
        '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutgoblins
        '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
            jump ruinedvillage01scavengerscamp01aboutundead
        '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
            jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
        '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
            jump ruinedvillage01scavengerscamp01aboutruins
        '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
            jump ruinedvillage01scavengerscamp01aboutbandits
        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
            jump ruinedvillage01scavengerscamp01aboutasterion
        '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
            jump ruinedvillage01scavengerscamp01leavingdell
        '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
            jump ruinedvillage01scavengerscamp01leavingspear
        'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
            pass
        '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
            jump ruinedvillage01scavengerscamp01aboutquestBquestions
        'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
            pass
        'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
            pass
        'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
            pass
        '“Time for me to leave.”' if quest_escortpyrrhos:
            hide areapicture
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
            jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01aboutruins:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened here?”')
    $ pyrrhos_about_ruins = 1
    menu:
        '“Well, I won’t guess, but I saw many ruins. There’s no treasure and skeletons here, so this place means as much as dirt. Someone was barking too loud, so the beasts broke through and made them quiet again,” he clicks his tongue. “And that’s that. Talking about nature’s fury brings bad luck, don’t ye know?”
        '
        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
            jump ruinedvillage01scavengerscamp01aboutironingot01
        'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
            pass
        'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutquest
        '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
            jump ruinedvillage01scavengerscamp01aboutgettingsick
        '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
            jump ruinedvillage01scavengerscamp01abouthimself
        'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
            pass
        '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
            jump ruinedvillage01scavengerscamp01broughtfood
        '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutgoblins
        '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
            jump ruinedvillage01scavengerscamp01aboutundead
        '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
            jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
        '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
            jump ruinedvillage01scavengerscamp01aboutruins
        '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
            jump ruinedvillage01scavengerscamp01aboutbandits
        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
            jump ruinedvillage01scavengerscamp01aboutasterion
        '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
            jump ruinedvillage01scavengerscamp01leavingdell
        '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
            jump ruinedvillage01scavengerscamp01leavingspear
        'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
            pass
        '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
            jump ruinedvillage01scavengerscamp01aboutquestBquestions
        'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
            pass
        'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
            pass
        'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
            pass
        '“Time for me to leave.”' if quest_escortpyrrhos:
            hide areapicture
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
            jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01aboutbandits:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts nearby?”')
    $ pyrrhos_about_bandits = 1
    menu:
        '“Nah, I think they are in the North, or East. I stuck to the western road and no shell bothered me. Sorry, can’t help ye.”
        '
        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
            jump ruinedvillage01scavengerscamp01aboutironingot01
        'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
            pass
        'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutquest
        '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
            jump ruinedvillage01scavengerscamp01aboutgettingsick
        '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
            jump ruinedvillage01scavengerscamp01abouthimself
        'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
            pass
        '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
            jump ruinedvillage01scavengerscamp01broughtfood
        '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutgoblins
        '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
            jump ruinedvillage01scavengerscamp01aboutundead
        '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
            jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
        '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
            jump ruinedvillage01scavengerscamp01aboutruins
        '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
            jump ruinedvillage01scavengerscamp01aboutbandits
        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
            jump ruinedvillage01scavengerscamp01aboutasterion
        '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
            jump ruinedvillage01scavengerscamp01leavingdell
        '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
            jump ruinedvillage01scavengerscamp01leavingspear
        'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
            pass
        '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
            jump ruinedvillage01scavengerscamp01aboutquestBquestions
        'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
            pass
        'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
            pass
        'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
            pass
        '“Time for me to leave.”' if quest_escortpyrrhos:
            hide areapicture
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
            jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01aboutasterion:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”')
    $ pyrrhos_about_asterion = 1
    $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
    menu:
        '“Ay, I’ve never met him, b’I surely heard this name many times. He vanished long before I got to the coast. At first, people were asking about him. Now they think he’s dead.”
        '
        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
            jump ruinedvillage01scavengerscamp01aboutironingot01
        'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
            pass
        'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutquest
        '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
            jump ruinedvillage01scavengerscamp01aboutgettingsick
        '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
            jump ruinedvillage01scavengerscamp01abouthimself
        'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
            pass
        '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
            jump ruinedvillage01scavengerscamp01broughtfood
        '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutgoblins
        '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
            jump ruinedvillage01scavengerscamp01aboutundead
        '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
            jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
        '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
            jump ruinedvillage01scavengerscamp01aboutruins
        '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
            jump ruinedvillage01scavengerscamp01aboutbandits
        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
            jump ruinedvillage01scavengerscamp01aboutasterion
        '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
            jump ruinedvillage01scavengerscamp01leavingdell
        '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
            jump ruinedvillage01scavengerscamp01leavingspear
        'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
            pass
        '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
            jump ruinedvillage01scavengerscamp01aboutquestBquestions
        'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
            pass
        'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
            pass
        'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
            pass
        '“Time for me to leave.”' if quest_escortpyrrhos:
            hide areapicture
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
            jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01aboutquest:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”')
    menu:
        '“Let me explain first, ay? I was in {color=#f6d6bd}Howler’s Dell{/color}, the closest village to the east and north, and people there are nice, ye know. Not like in {color=#f6d6bd}Old Págos{/color}, they’re all boring and grimmer than a crow. Ba’they cry coin for everything, and damn good coin! I left, wanted to look around the ruins, see if there’s anything left, then move to {color=#f6d6bd}Pelt{/color} and hire the hunters to help me here. No luck, a bunch of griffs jumped my pack bird. I just bought it!” He spits on the floor. “Fast and nimble, b’not brave enough to listen to me when all that screeching and scratching started.”
        \n\n“So, it ran away with my bags. A few fell on the ground and I pulled them here, b’ye see how it is. I won’t travel around with a tent on my back!” He taps the crossbow with his fingers. “I need maybe a day more, ay, just a day, and I’ll have all the iron scrapped from the barrels, so I can move forward. B’I can’t take all my stuff alone, and without me around the apemen are going to break in and steal all my shit.”
        \n\n“I need to stay here, ba’since ye have a horse... Come back tomorrow and help me return to {color=#f6d6bd}Howler’s Dell{/color}, how about it? I just need to know that the road is safe, safe as it can be, I mean.”
        '
        '“What exactly do you want me to do?”' if not pyrrhos_quest_question1:
            $ pyrrhos_quest_question1 = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What exactly do you want me to do?”')
            jump ruinedvillage01scavengerscamp01aboutquestA
        '“Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if not pyrrhos_quest_question2 and pyrrhos_quest_question1 and peltnorth_firsttime and not peltnorth_ban_perm:
            $ pyrrhos_quest_question2 = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”')
            jump ruinedvillage01scavengerscamp01aboutquestB
        '“I don’t work for free.”' if not pyrrhos_quest_question3:
            $ pyrrhos_quest_question3 = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t work for free.”')
            jump ruinedvillage01scavengerscamp01aboutquestC
        '“Fine, it’s a deal. I’m going to escort you.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine, it’s a deal. I’m going to escort you.”')
            jump ruinedvillage01scavengerscamp01regularquestionsv03
        '“I need to think about it.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
            jump ruinedvillage01scavengerscamp01regularquestionsv04

    label ruinedvillage01scavengerscamp01aboutquestA:
        $ quest_escortpyrrhos = 1
        $ quest_escortpyrrhos_description01 = 1
        $ renpy.notify("New entry: Escort The Scavenger")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Escort The Scavenger{/i}')
        menu:
            '“I need ye to make sure there’s no danger hiding on the road, from here to {color=#f6d6bd}Howler’s{/color}. Or rather, I know there is {i}some{/i} danger, b’as long as ye can get there and safely return, I’m sure we can handle some roaming monsters.” He theatrically rubs his hands together. “This ballista has hit more beast skulls than I have fingers, and I’ve {i}never{/i} lost a finger, roadster. Only the toes.”
            \n\nMaybe to prove it, he starts to count on his fingers. “So, see if the road there is clear. Then come here tomorrow, we’ll pack my stuff on ya horse and move out. Ba’don’t come when it’s close to evening, we’re going to need three hours on our feet, and I won’t push through the night. Even sleeping next to an apemen tribe is safer,” he chuckles. “And don’t make me wait for too long! I can wait for a couple of days if I find some food, b’if ye don’t get back, I’ll have to risk it, no matter what.”
            '
            '“What exactly do you want me to do?”' if not pyrrhos_quest_question1:
                $ pyrrhos_quest_question1 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What exactly do you want me to do?”')
                jump ruinedvillage01scavengerscamp01aboutquestA
            '“Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if not pyrrhos_quest_question2 and pyrrhos_quest_question1 and peltnorth_firsttime and not peltnorth_ban_perm:
                $ pyrrhos_quest_question2 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”')
                jump ruinedvillage01scavengerscamp01aboutquestB
            '“I don’t work for free.”' if not pyrrhos_quest_question3:
                $ pyrrhos_quest_question3 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t work for free.”')
                jump ruinedvillage01scavengerscamp01aboutquestC
            '“Fine, it’s a deal. I’m going to escort you.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine, it’s a deal. I’m going to escort you.”')
                jump ruinedvillage01scavengerscamp01regularquestionsv03
            '“I need to think about it.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump ruinedvillage01scavengerscamp01regularquestionsv04

    label ruinedvillage01scavengerscamp01aboutquestB:
        menu:
            '“I mean... I see ya point, b’I’ve never been there. Can they afford my iron, do they have means to pay for it? I need coins to find a handy bunch that will walk south with me, and I need a new staff, and bolts... I know the village, it’s a nice place, and even has a smithy. Of sorts.”
            '
            '“I had a chance to take a look, though. It’s a large inn, a safe one. They seem to be rich and have enough hunters to guide you south. You can use iron to barter.”' if peltnorth_firsttime:
                $ pyrrhos_quest_canpelt = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I had a chance to take a look, though. It’s a large inn, a safe one. They seem to be rich and have enough hunters to guide you south. You can use iron to barter.”')
                jump ruinedvillage01scavengerscamp01aboutquestB2
            '“What exactly do you want me to do?”' if not pyrrhos_quest_question1:
                $ pyrrhos_quest_question1 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What exactly do you want me to do?”')
                jump ruinedvillage01scavengerscamp01aboutquestA
            '“Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if not pyrrhos_quest_question2 and pyrrhos_quest_question1 and peltnorth_firsttime and not peltnorth_ban_perm:
                $ pyrrhos_quest_question2 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”')
                jump ruinedvillage01scavengerscamp01aboutquestB
            '“I don’t work for free.”' if not pyrrhos_quest_question3:
                $ pyrrhos_quest_question3 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t work for free.”')
                jump ruinedvillage01scavengerscamp01aboutquestC
            '“Fine, it’s a deal. I’m going to escort you.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine, it’s a deal. I’m going to escort you.”')
                jump ruinedvillage01scavengerscamp01regularquestionsv03
            '“I need to think about it.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump ruinedvillage01scavengerscamp01regularquestionsv04

    label ruinedvillage01scavengerscamp01aboutquestB2:
        $ quest_escortpyrrhos_description02 = "I can also take him to {color=#f6d6bd}Pelt{/color}."
        $ renpy.notify("Journal updated: Escort The Scavenger")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Escort The Scavenger{/i}')
        menu:
            '“Well... It’s a shorter path, I guess, fewer spots to get surrounded by corpsers... If yer sure it’s the best option, fine. I’ll trust a roadster’s judgment.”
            '
            '“What exactly do you want me to do?”' if not pyrrhos_quest_question1:
                $ pyrrhos_quest_question1 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What exactly do you want me to do?”')
                jump ruinedvillage01scavengerscamp01aboutquestA
            '“Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if not pyrrhos_quest_question2 and pyrrhos_quest_question1 and peltnorth_firsttime and not peltnorth_ban_perm:
                $ pyrrhos_quest_question2 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”')
                jump ruinedvillage01scavengerscamp01aboutquestB
            '“I don’t work for free.”' if not pyrrhos_quest_question3:
                $ pyrrhos_quest_question3 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t work for free.”')
                jump ruinedvillage01scavengerscamp01aboutquestC
            '“Fine, it’s a deal. I’m going to escort you.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine, it’s a deal. I’m going to escort you.”')
                jump ruinedvillage01scavengerscamp01regularquestionsv03
            '“I need to think about it.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump ruinedvillage01scavengerscamp01regularquestionsv04

    label ruinedvillage01scavengerscamp01aboutquestC:
        $ quest_escortpyrrhos_description03 = "For my help, he offers me either dragon bones, or a mixture that “scares apemen away.”"
        menu:
            '“I have ways to pay ye, don’t ye worry. I can give ye dragons, b’I have to sell the iron first, so I’ll need a bit of time, ye see. Five for a short escort would be plenty, I’d say. B’if ye want, I’ll give you a secret jar of mine, a very fine mixture that scares apemen away. Works on pebblers, too.”
            \n\nWhen you ask if all this stench of urine is somehow related to this {i}potion{/i}, he just winks and chuckles.
            '
            '“I’d also like to learn more about the villages you visited.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d also like to learn more about the villages you visited.”')
                jump ruinedvillage01scavengerscamp01aboutquestC2
            '“What exactly do you want me to do?”' if not pyrrhos_quest_question1:
                $ pyrrhos_quest_question1 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What exactly do you want me to do?”')
                jump ruinedvillage01scavengerscamp01aboutquestA
            '“Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if not pyrrhos_quest_question2 and pyrrhos_quest_question1 and peltnorth_firsttime and not peltnorth_ban_perm:
                $ pyrrhos_quest_question2 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”')
                jump ruinedvillage01scavengerscamp01aboutquestB
            '“I don’t work for free.”' if not pyrrhos_quest_question3:
                $ pyrrhos_quest_question3 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t work for free.”')
                jump ruinedvillage01scavengerscamp01aboutquestC
            '“Fine, it’s a deal. I’m going to escort you.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine, it’s a deal. I’m going to escort you.”')
                jump ruinedvillage01scavengerscamp01regularquestionsv03
            '“I need to think about it.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump ruinedvillage01scavengerscamp01regularquestionsv04

    label ruinedvillage01scavengerscamp01aboutquestC2:
        $ description_thais03b = "She hates being asked about the origins of her wealth."
        menu:
            'He seems surprised. “I mean... Ay. Sure. B’I don’t have connections there, ye know. Just my eyes.”
            \n\nHe starts to hum. “Ye know, ye know...” A longer pause. “When ye get to {color=#f6d6bd}Howler’s{/color}, you’ll meet the mayor there, for sure. {color=#f6d6bd}Thais{/color}. And whatever ye do, don’t ask her where she got her coins from, ay? She’s rich, stupid rich, ba’don’t ask her how this happened. Trust me.” He scratches his beard with a mournful look.
            '
            '“What exactly do you want me to do?”' if not pyrrhos_quest_question1:
                $ pyrrhos_quest_question1 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What exactly do you want me to do?”')
                jump ruinedvillage01scavengerscamp01aboutquestA
            '“Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if not pyrrhos_quest_question2 and pyrrhos_quest_question1 and peltnorth_firsttime and not peltnorth_ban_perm:
                $ pyrrhos_quest_question2 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”')
                jump ruinedvillage01scavengerscamp01aboutquestB
            '“I don’t work for free.”' if not pyrrhos_quest_question3:
                $ pyrrhos_quest_question3 = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t work for free.”')
                jump ruinedvillage01scavengerscamp01aboutquestC
            '“Fine, it’s a deal. I’m going to escort you.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine, it’s a deal. I’m going to escort you.”')
                jump ruinedvillage01scavengerscamp01regularquestionsv03
            '“I need to think about it.”' if pyrrhos_quest_question1 == 1 and pyrrhos_quest_question3 == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump ruinedvillage01scavengerscamp01regularquestionsv04

label ruinedvillage01scavengerscamp01:
    if day-pyrrhos_saving_base-pyrrhos_fed < pyrrhos_deathcounter_met and pyrrhos_quest_counter == day:
        jump ruinedvillage01scavengerscamp01regular
    elif day-pyrrhos_saving_base-pyrrhos_fed < pyrrhos_deathcounter_met:
        jump ruinedvillage01scavengerscamp01readytoleave
    else:
        jump ruinedvillage01scavengerscamp01questfailed01

label ruinedvillage01scavengerscamp01regular:
    show areapicture ruinedvillagetent01 at basicfade
    if pyrrhos_firstattitude == "intimidating":
        $ custom1 = ""
    else:
        $ custom1 = " His crossbow is loaded, resting just next to him and aimed at the entrance."
    menu:
        'The entrance to the scavenger’s hideout is open. [pyrrhos_ruinedvillage_fluff][custom1]
        '
        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
            jump ruinedvillage01scavengerscamp01aboutironingot01
        'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
            pass
        'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutquest
        '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
            jump ruinedvillage01scavengerscamp01aboutgettingsick
        '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
            jump ruinedvillage01scavengerscamp01abouthimself
        'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
            pass
        '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
            jump ruinedvillage01scavengerscamp01broughtfood
        '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutgoblins
        '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
            jump ruinedvillage01scavengerscamp01aboutundead
        '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
            jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
        '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
            jump ruinedvillage01scavengerscamp01aboutruins
        '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
            jump ruinedvillage01scavengerscamp01aboutbandits
        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
            jump ruinedvillage01scavengerscamp01aboutasterion
        '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
            jump ruinedvillage01scavengerscamp01leavingdell
        '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
            jump ruinedvillage01scavengerscamp01leavingspear
        'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
            pass
        '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
            jump ruinedvillage01scavengerscamp01aboutquestBquestions
        'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
            pass
        'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
            pass
        'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
            pass
        '“Time for me to leave.”' if quest_escortpyrrhos:
            hide areapicture
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
            jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01readytoleave:
    show areapicture ruinedvillagetent02 at basicfade
    if quarters <= (world_daylength-8):
        $ custom1 = "The man looks tired and his beard is sticky, but he smiles at you. “If yer ready, I’ll start packing the tent. If ye don’t want to wait, start putting the iron on ya mount, it will be quicker. Just say the word and we can leave."
    else:
        $ custom1 = "The man looks tired and his beard is sticky, but he observes you with attention. “A bit late, isn’t it?"
    menu:
        'The entrance to the scavenger’s hideout is open. You see scraps of metal organized in piles, while the old furniture has been dismantled into loose planks and pushed into corners. “Ay, roadster!” [custom1]”
        '
        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude == "intimidating" and not pyrrhos_about_ironingot:
            jump ruinedvillage01scavengerscamp01aboutironingot01
        'I can’t confront him about the iron from Gale Rocks while he keeps the crossbow at his side. (disabled)' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and pyrrhos_firstattitude != "intimidating" and not pyrrhos_about_ironingot:
            pass
        'I should ask him what he wants. “Where do you want to travel to now? And what will you give me for my help?”' if not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutquest
        '“This village makes me sick.”' if (not pyrrhos_about_curse and ruinedvillage_curse_firsttime and not ruinedvillage_curse_gone) or (not pyrrhos_about_curse and ruinedvillage_curse_points >= 2 and not ruinedvillage_curse_gone):
            jump ruinedvillage01scavengerscamp01aboutgettingsick
        '“Tell me about yourself.”' if (not pyrrhos_about_himself) or (pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) >= 5):
            jump ruinedvillage01scavengerscamp01abouthimself
        'He doesn’t trust me enough to tell me about himself. (disabled)' if pyrrhos_about_himself == 1 and (pyrrhos_friendship+appearance_charisma) < 5:
            pass
        '“I brought you some food.”' if pyrrhos_foodcounter != day and item_rations:
            jump ruinedvillage01scavengerscamp01broughtfood
        '“How do you keep the goblins away?”' if not pyrrhos_about_goblins and not quest_escortpyrrhos:
            jump ruinedvillage01scavengerscamp01aboutgoblins
        '“Are you sure there are no undead around?”' if not pyrrhos_about_undead:
            jump ruinedvillage01scavengerscamp01aboutundead
        '“Have you searched the entire village? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
            jump ruinedvillage01scavengerscamp01aboutthingsleftbehind
        '“Do you have any idea what happened here?”' if not pyrrhos_about_ruins:
            jump ruinedvillage01scavengerscamp01aboutruins
        '“I’ve heard about some bandits. Have you seen any hideouts nearby?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
            jump ruinedvillage01scavengerscamp01aboutbandits
        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color}.”' if not pyrrhos_about_asterion:
            jump ruinedvillage01scavengerscamp01aboutasterion
        '“Gather your bags. I’m taking you to {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day and pc_hp > 1:
            jump ruinedvillage01scavengerscamp01leavingdell
        '“Time to head for {color=#f6d6bd}Pelt of the North{/color}.”' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and pc_hp > 1 and not peltnorth_ban_perm:
            jump ruinedvillage01scavengerscamp01leavingspear
        'I’m too tired to protect either of us on the road to Pelt. (Required vitality: 2) (disabled)' if quest_escortpyrrhos == 1 and quarters <= (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day and peltnorth_ban_temp != day and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'I was banned from Pelt of the North. I won’t be able to escort him there. (disabled)' if (peltnorth_ban_temp == day and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day) or (peltnorth_ban_perm and quest_escortpyrrhos == 1 and quarters > (world_daylength-8) and pyrrhos_quest_canpelt and pyrrhos_quest_counter != day):
            pass
        '“Why do you want to go to {color=#f6d6bd}Howler’s Dell{/color}? If you want to go south, we should travel to {color=#f6d6bd}Pelt of the North{/color}.”' if pyrrhos_quest_question1 and pyrrhos_quest_question3 and peltnorth_firsttime and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and not pyrrhos_quest_canpelt:
            jump ruinedvillage01scavengerscamp01aboutquestBquestions
        'I’m too tired to protect either of us on the road to Howler’s Dell. (Required vitality: 2) (disabled)' if pyrrhos_quest_question1 and peltnorth_firsttime and pyrrhos_quest_counter != day and quest_escortpyrrhos == 1 and not peltnorth_ban_perm and pc_hp <= 1:
            pass
        'Without a mount, it’s too dangerous for him to start a journey at such a late hour. (disabled)' if quest_escortpyrrhos == 1 and quarters > (world_daylength-12) and pyrrhos_quest_tohowlersdell == 1 and pyrrhos_quest_counter != day:
            pass
        'To escort him to Howler’s Dell, I need to be sure the road leading there is somewhat safe. (disabled)' if not pyrrhos_quest_tohowlersdell and quest_escortpyrrhos == 1:
            pass
        'I was meant to escort him tomorrow, not sooner. (disabled)' if pyrrhos_quest_counter == day and quest_escortpyrrhos == 1:
            pass
        '“Time for me to leave.”' if quest_escortpyrrhos:
            hide areapicture
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Time for me to leave.”')
            jump ruinedvillageselectarea

label ruinedvillage01scavengerscamp01questfailed01:
    show areapicture ruinedvillagetent03 at basicfade
    $ renpy.notify("Quest completed: Escort The Scavenger")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Escort The Scavenger{/i}')
    $ quest_escortpyrrhos_description06 = "He’s no longer in the ruins, even though he left behind some of his stuff. He was probably finished off by the nearby goblin camp."
    $ description_pyrrhos06 = "He’s no longer in the ruins, even though he left behind some of his stuff. He was probably finished off by the nearby goblin camp."
    $ quest_escortpyrrhos = 3
    $ pyrrhos_dead = 1
    menu:
        'The entrance is wide open. The smell of urine isn’t as vexing, but is now complemented by goblin feces and trails of blood. The tent is torn to pieces, while the scavenger’s tools, clothes, and weapons have either been destroyed or taken away.
        \n\nYou can safely assume that their owner won’t return for them.
        '
        'No point in wasting all this iron. I can put it on {color=#f6d6bd}[horsename]{/color} and sell it somewhere else.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- No point in wasting all this iron. I can put it on {color=#f6d6bd}%s{/color} and sell it somewhere else.' %horsename)
            jump ruinedvillage01scavengerscamp01questfailed02
        'I’m surprised the goblins left behind so much iron, but at least there’s some left for me.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m surprised the goblins left behind so much iron, but at least there’s some left for me.')
            jump ruinedvillage01scavengerscamp01questfailed02
        'It wouldn’t be right to scavenge now. I go somewhere else.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It wouldn’t be right to scavenge now. I go somewhere else.')
            hide areapicture
            jump ruinedvillageselectarea

    label ruinedvillage01scavengerscamp01questfailed02:
        show areapicture ruinedvillagetent03b at basicfade
        $ item_ironscraps += 1
        $ item_crossbowquarrels += 2
        $ renpy.notify("You’ve gathered the iron scraps and two quarrels.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve gathered the iron scraps and two quarrels.{/i}')
        $ quarters += 1
        menu:
            'You walk carefully, avoiding blood and dirt. Some of the iron and steel is touched by rust, but a blacksmith will make good use of them. You use your knife to turn the tent into rags, then wrap them over the roughly edged pieces of your loot, making sure they won’t cut {color=#f6d6bd}[horsename]’s{/color} back during your ride. You find only one other thing of value - two short arrows, made for a crossbow.
            \n\nYou wonder where the scavenger’s shell is.
            '
            'I leave the building.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
                hide areapicture
                jump ruinedvillageselectarea

    label ruinedvillage01scavengerscamp01firsttimedead:
        show areapicture ruinedvillagetent03 at basicfade
        $ pyrrhos_dead = 1
        menu:
            'You step cautiously and take a peek into a cellar-like entrance hall, without any source of light other than the sun that enters through the door. There are dismantled barrels, and a few scraps of iron lying around, all of them looking like a result of human work, not time. You notice no burnt wood, no smell of putridity. The whiff of urine is complemented by goblin feces and trails of blood.
            \n\nYou see a torn to pieces tent and clothes, broken tools, and a crossbow, damaged beyond repair. The road to the upper floor seems to be blocked by the collapsed roof and loose, wooden beams. There are scraps of rusting iron on the ground, detached from now destroyed furniture. Such metal parts can be worth quite a bit.
            \n\nYou can safely assume that their owner won’t return for them.
            '
            'No point in wasting all this iron. I can put it on {color=#f6d6bd}[horsename]{/color} and sell it somewhere else.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- No point in wasting all this iron. I can put it on {color=#f6d6bd}%s{/color} and sell it somewhere else.' %horsename)
                jump ruinedvillage01scavengerscamp01questfailed02alt

        label ruinedvillage01scavengerscamp01questfailed02alt:
            show areapicture ruinedvillagetent03b at basicfade
            $ item_ironscraps += 1
            $ item_crossbowquarrels += 2
            $ renpy.notify("You’ve gathered the iron scraps and two quarrels.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You’ve gathered the iron scraps and two quarrels.{/i}')
            $ quarters += 1
            menu:
                'You walk carefully, avoiding blood and dirt. Some of the iron and steel is touched by rust, but a blacksmith will make good use of them. You use your knife to turn the tent into rags, then wrap them over the roughly edged pieces of your loot, making sure they won’t cut {color=#f6d6bd}[horsename]’s{/color} back during your ride. You find only one other thing of value - two short arrows, made for a crossbow.
                \n\nYou wonder where the owner’s shell is.
                '
                'I leave the building.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
                    hide areapicture
                    jump ruinedvillageselectarea
