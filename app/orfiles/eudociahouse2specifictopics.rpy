label eudociahouseaboutpensALL:
    label eudociahouseaboutpens01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was asked to deliver the writing quills to the monastery.')
        $ eudocia_about_pens = 1
        $ eudocia_friendship += 1
        $ minutes += 1
        if pc_area == "eudociahouse":
            $ eudocia_fluff_inorout = "She opens one of the heavy doors to her house and you catch a glimpse of a messy bed and a floor covered with clothes. She returns after a minute or so."
        if pc_area == "eudociahouseinside":
            $ eudocia_fluff_inorout = "She stands up with a sigh and moves to the cupboard, then grabs something from the shelf and turns back to you."
        menu:
            '“Then ye’re in luck. They’re ready.”
            \n\n[eudocia_fluff_inorout] “Here.” She opens a small leather case and pulls out the quills, a mix of translucent grays and whites. You step closer and reach out for them, but she keeps holding them.
            \n\n“Why d’ye aid the monks? They’re a rather grim bunch, aren’t they? Some nasty rumors are in the air.” Her grasp is strong, her eyes meet yours briefly.
            '
            '“You’re also working with them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re also working with them.”')
                jump eudociahouseaboutpens02a
            '“I hope they’ll help me find {color=#f6d6bd}Asterion{/color}.”' if not eudocia_about_asterion and quest_asterion == 1 and not asterion_found and not aeli_about_secret_asterion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I hope they’ll help me find {color=#f6d6bd}Asterion{/color}.”')
                $ eudocia_about_asterion = 1
                jump eudociahouseaboutpens02b
            '“It’s just a job.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s just a job.”')
                jump eudociahouseaboutpens02c
            '“What do you mean by {i}rumors{/i}?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you mean by {i}rumors{/i}?”')
                jump eudociahouseaboutpens02d
            '“Everyone has a story. I’m not the one to judge.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Everyone has a story. I’m not the one to judge.”')
                jump eudociahouseaboutpens02e
            '“It’s better to get on people’s good side.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s better to get on people’s good side.”')
                jump eudociahouseaboutpens02a
            '“That’s none of your concern.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s none of your concern.”')
                jump eudociahouseaboutpens02g

    label eudociahouseaboutpens02a:
        menu:
            '“The Northerners have to stick together, but don’t let the outsiders {i}too{/i} close. I may not like my neighbors, but as long as I want to eat aught more than frogs and bark, I need to have them around.”
            \n\nShe stares into your eyes, piercing you with her gray irises.
            \n\n“But ye’re not a prisoner of this place. Ye can come and go, if ye so please.”
            '
            '“Do you feel like a prisoner here?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you feel like a prisoner here?”')
                jump eudociahouseaboutpens02a02
            '“I hope they’ll help me find {color=#f6d6bd}Asterion{/color}.”' if not eudocia_about_asterion and quest_asterion == 1 and not asterion_found and not aeli_about_secret_asterion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I hope they’ll help me find {color=#f6d6bd}Asterion{/color}.”')
                $ eudocia_about_asterion = 1
                jump eudociahouseaboutpens02b
            '“It’s just a job.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s just a job.”')
                jump eudociahouseaboutpens02c
            '“What do you mean by {i}rumors{/i}?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you mean by {i}rumors{/i}?”')
                jump eudociahouseaboutpens02d
            '“Everyone has a story. I’m not the one to judge.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Everyone has a story. I’m not the one to judge.”')
                jump eudociahouseaboutpens02e
            '“That’s none of your concern.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s none of your concern.”')
                jump eudociahouseaboutpens02g

    label eudociahouseaboutpens02a02:
        menu:
            'She looks away.
            '
            '“I hope they’ll help me find {color=#f6d6bd}Asterion{/color}.”' if not eudocia_about_asterion and quest_asterion == 1 and not asterion_found and not aeli_about_secret_asterion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I hope they’ll help me find {color=#f6d6bd}Asterion{/color}.”')
                $ eudocia_about_asterion = 1
                jump eudociahouseaboutpens02b
            '“It’s just a job.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s just a job.”')
                jump eudociahouseaboutpens02c
            '“What do you mean by {i}rumors{/i}?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you mean by {i}rumors{/i}?”')
                jump eudociahouseaboutpens02d
            '“Everyone has a story. I’m not the one to judge.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Everyone has a story. I’m not the one to judge.”')
                jump eudociahouseaboutpens02e
            '“That’s none of your concern.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s none of your concern.”')
                jump eudociahouseaboutpens02g

    label eudociahouseaboutpens02b:
        if pc_area == "eudociahouse":
            $ eudocia_fluff_inorout = "gate"
        if pc_area == "eudociahouseinside":
            $ eudocia_fluff_inorout = "hearth"
        menu:
            '“All this for knowledge? How laudable.” She lets go of the bag and glances at the [eudocia_fluff_inorout]. “But the villages here are full of serpents, be wiser than to trust them. That includes me, of course,” with a smirk, she twirls her hair, “but at least I’ve got no reason to lie to ye.”
            \n\nBefore you respond, she carries on. “Let me tell ye some stuff about {color=#f6d6bd}Asterion{/color}.”
            '
            'I nod.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                $ quest_pensformonastery_description01 = "{color=#f6d6bd}Eudocia{/color} gave me the quills."
                $ renpy.notify("You received the “magic” quills.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the “magic” quills.{/i}')
                $ item_magicpens = 1
                $ custom1 = ""
                jump eudocia_about_asterionsuccess01

    label eudociahouseaboutpens02c:
        $ quest_pensformonastery_description01 = "{color=#f6d6bd}Eudocia{/color} gave me the quills."
        $ item_magicpens = 1
        if pc_area == "eudociahouse":
            $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        if not quest_easternpath:
            $ quest_easternpath = 1
            $ quest_easternpath_description_teaser = "{color=#f6d6bd}Eudocia{/color}, the enchantress, claims that the people from {color=#f6d6bd}Creeks{/color}, a hunting village in the far north, have some issues with maintaining their roads."
            $ renpy.notify("You received the “magic” quills.\nNew entry: Eastern Path")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the “magic” quills. New entry: Eastern Path{/i}')
        else:
            $ renpy.notify("You received the “magic” quills.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the “magic” quills.{/i}')
        $ description_creeks01 = "A village of fishers, hunters, and woodcutters in the far North."
        $ description_creeks03 = "According to {color=#f6d6bd}Eudocia{/color}: “They plan to reclaim the road to the far south of the peninsula. Just smile a lot and they’ll let ye in.”"
        menu:
            'She releases the case and nods. “Fair enough. If ye’re looking for a job, ye may want to reach {color=#f6d6bd}Creeks{/color}, in the north and east. They’re hunters and woodcutters, and plan to reclaim the road to the far south of the peninsula. Just smile a lot and they’ll let ye in.”
            '
            '(eudocia1 set)':
                pass

    label eudociahouseaboutpens02d:
        $ quest_pensformonastery_description01 = "{color=#f6d6bd}Eudocia{/color} gave me the quills."
        $ renpy.notify("You received the “magic” quills.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the “magic” quills.{/i}')
        $ item_magicpens = 1
        $ description_monastery04 = "According to {color=#f6d6bd}Eudocia{/color}, “{color=#f6d6bd}the prelate{/color} crawls in the caves, like a beast in a den.”"
        if pc_area == "eudociahouse":
            $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        menu:
            'She releases the case with a frustrated grimace. “What d’ye mean by {i}what do you mean{/i}?” She’s pretty good at mimicking your accent. “What is it that ye haven’t heard? That the monastery brings sickness and nightmares? That the monks have the village in their bandit grasp? That {color=#f6d6bd}the prelate{/color} crawls in the caves, like a beast in a den?”
            \n\nHer gaze softens when the two of you exchange looks. “I’m just glad they sent ye here. I’d be glad to teach my golems to speak if it would spare me the sight of nasty monastic robes.”
            \n\nYou glance at her own {i}nasty robe{/i}, though she doesn’t even notice it.
            '
            '(eudocia1 set)':
                pass

    label eudociahouseaboutpens02e:
        $ quest_pensformonastery_description01 = "{color=#f6d6bd}Eudocia{/color} gave me the quills."
        $ renpy.notify("You received the “magic” quills.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the “magic” quills.{/i}')
        $ item_magicpens = 1
        # $ eudocia_friendship += 1
        if pc_area == "eudociahouse":
            $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        if not eudocia_about_steephouse:
            $ custom1 = "\n\nShe carries on while you’re attaching the container to your belt. “If it’s the latter,” she says slowly, “don’t ask anyone about the ruins on the southern road, those west from the inn. Those hornets can sting real good.”"
        else:
            $ custom1 = ""
        menu:
            'She releases the case and you catch a glimpse of a smile in her gray eyes. “For ye’re such a truth seeker, or just smart enough to not poke a hornet’s nest? I guess I’ll know soon enough.”[custom1]
            '
            '(eudocia1 set)':
                pass

    label eudociahouseaboutpens02g:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ quest_pensformonastery_description01 = "{color=#f6d6bd}Eudocia{/color} gave me the quills."
        $ renpy.notify("You received the “magic” quills.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the “magic” quills.{/i}')
        $ item_magicpens = 1
        $ questionpreset = "eudocia1"
        menu:
            'She releases the case. “Obviously. But don’t claim that ye also stay away from others’ affairs. Or am I to expect that ye’ve got no questions for me?” Her smirk carries a glimpse of hope.
            '
            '(eudocia1 set)':
                pass

label eudocia_about_asterionALL:
    label eudocia_about_asterion00:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        $ eudocia_about_asterion_gray = 1
        menu:
            '“Nah, he’s not here. Not even a mouse in my shed.” She meets your eyes, yet her gray irises remain absent.
            \n\nHer sigh turns into a snort. “Aught else?”
            '
            '(eudocia1 set)':
                pass

    label eudocia_about_asterion01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if (eudocia_friendship+appearance_charisma) >= 8:
            $ eudocia_about_asterion = 1
            menu:
                'She looks in the distance, holding one arm across her stomach, and twirling her hair with the other. “I should smoke aught. Or at least gather wood. The summer’s almost over.”
                '
                'I ask her again.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask her again.')
                    $ eudocia_friendship -= 1
                    $ custom1 = "She gives you an angry glance. “Don’t hasten me, I’m collecting my thoughts.” For a few breaths, she rubs her left shoulder. “Let me tell ye some stuff about {color=#f6d6bd}Asterion{/color}.”\n\n"
                    jump eudocia_about_asterionsuccess01
                '“I could help you with that.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could help you with that.”')
                    $ eudocia_friendship += 1
                    $ custom1 = "She glances at you, but it takes her a few breaths to answer. “We’ve no time for it, do we now? Wardens never do. Neither do enchanters.” She lets out a long exhale. “Ye’re someone who puts actions first. {color=#f6d6bd}Asterion{/color} was the same. If aught happened to him, don’t let yaself fall too.”\n\n"
                    jump eudocia_about_asterionsuccess01
                'I sit closer to her.' if pc_area == "eudociahouseinside":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit closer to her.')
                    $ eudocia_friendship += 1
                    $ minutes += 5
                    $ custom1 = "Both of you are staring at the wall, letting the minutes go by silently. She finally lets out a sigh, her head resting on her arms, observing the floor. “I’ve collected my thoughts, but I’m not going to repeat myself, so wash your ears.”\n\n"
                    jump eudocia_about_asterionsuccess01
                'I stay silent.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay silent.')
                    $ custom1 = "After a few long breaths, she rubs her left shoulder. Her voice is weaker. “Maybe ye’ll find him after all. And help him, instead of causing him harm.”\n\n"
                    $ minutes += 1
                    jump eudocia_about_asterionsuccess01
        else:
            if pc_area == "eudociahouse":
                $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            $ eudocia_about_asterion_gray = 1
            menu:
                'She raises her chin, challenging your look. “I know not where he may be, but if he {i}wanted{/i} to be found, he’d let us find him.”
                \n\nShe glances at the gate. “Aught else?”
                '
                '(eudocia1 set)':
                    pass

    label eudocia_about_asterionsuccess01:
        $ description_asterion06 = "According to {color=#f6d6bd}Eudocia{/color}, Asterion owns a green cloak, embroidered with black patterns presenting a variety of leaves."
        menu:
            '[custom1]Her description of his appearance matches what you heard from {color=#f6d6bd}Tulia{/color}. “Don’t be deceived by his height,” she adds, “he brought me herbs guarded by a bearfolk, not many could match his spear and bow. In return for his various favors, I shoved pneuma into his cloak, making it as warm and soft as the pelt of a white wolf. Best sleep of my life.” She raises her daydreaming eyes.
            \n\nHer voice grows confident. “If {color=#f6d6bd}Asterion{/color} is still here, I’m sure he still has the cloak. It’s green, has a light hood and embroidered leaves.”
            '
            '“When was the last time you saw him?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “When was the last time you saw him?”')
                $ quest_asterion_description04b = "According to {color=#f6d6bd}Eudocia{/color}, Asterion was preparing for “a great journey.”"
                $ renpy.notify("Journal updated: Find the Roadwarden")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                menu:
                    '“Soon before he vanished. He was anxious, tired. Unkind, but from a heavy heart. He didn’t explain. I didn’t ask.”
                    \n\nHe rested at her place for a few hours, healed himself with magic, and prepared his equipment. She shows a surprising memory for details, but not especially useful ones.
                    \n\n“He told me he was going to start {i}a great journey{/i}, and that he’d bring back many stories. But he was afraid. I know he was.”
                    '
                    '“Did he ask for anything weird before he left? Maybe he wanted something?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he ask for anything weird before he left? Maybe he wanted something?”')
                        $ description_asterion04c = "According to {color=#f6d6bd}Eudocia{/color}, Asterion was looking for a way to “borrow” one of her golems."
                        $ quarters += 1
                        if pc_area == "eudociahouse":
                            $ eudocia_fluff_inorout = "sand"
                        if pc_area == "eudociahouseinside":
                            $ eudocia_fluff_inorout = "dust"
                        if eudocia_bronzerod_used < 5:
                            $ custom1 = "“Oh, that’s not an option. I’ve no way to stay in touch with the sentinels that are far away from here.”"
                        else:
                            $ custom1 = "“Oh, I’ve no way to stay in touch with the sentinels that are far away from here. The rods ye placed help a bit but they also have their limits.”"
                        menu:
                            'She scratches the [eudocia_fluff_inorout] with her foot. “Yes, actually. He wanted to {i}borrow{/i} a golem of mine.”
                            \n\nShe seems to finish her tale, but after seeing your look, she clears her throat.
                            \n\n[custom1]
                            '
                            '“Thank you.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you.”')
                                jump eudociahouseafterquestione
                            '“Do you have any message for him, in case I find him?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any message for him, in case I find him?”')
                                if pc_area == "eudociahouse":
                                    $ can_leave = 1
                                $ can_rest = 1
                                $ can_items = 1
                                $ questionpreset = "eudocia1"
                                menu:
                                    '“Message... Just tell him he still owes me for the cloak. He knows we’re not even. It’s a damn treasure.”
                                    \n\nShe puts on a smile, but her eyes betray her melancholy.
                                    '
                                    '(eudocia1 set)':
                                        pass

    label eudocia_about_asterion_found01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Asterion{/color} is dead.”')
        if pc_area == "eudociahouse":
            $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        $ eudocia_about_asterion_found = 1
        $ eudocia_friendship += 2
        $ minutes += 3
        menu:
            'You describe your expedition, but she pays little attention, observing the ends of her hair. “Just tell me what happened.”
            \n\nYour vague answer is met with a sad, yet accepting smile. “Too bad he chose to die alone.”
            '
            '(eudocia1 set)':
                pass

label eudocia_about_peninsula00:
    $ description_iason05 = "According to {color=#f6d6bd}Eudocia{/color}, he’s “stiff like a broom.”"
    $ description_foggy02 = "According to {color=#f6d6bd}Eudocia{/color}, her place is cheerful and “not as boring as {color=#f6d6bd}Pelt of the North{/color}.”"
    if pc_area == "eudociahouse":
        $ can_leave = 1
    else:
        $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "eudocia1"
    menu:
        'She leans away, frowning. “I can’t even {i}begin{/i} to describe how much I hope yern’t here to exchange gossip. If ye crave it so much, ride south, to {color=#f6d6bd}Pelt of the North{/color}. The keeper is stiff like a broom, but offers a nice room.” She glances at you, but her gray irises remain absent. “Or if ye’d rather visit a {i}cheerful{/i} place, ride north, to {color=#f6d6bd}Foggy Lake{/color}. Or was it {i}Foggy’s Lake{/i}? Whatever, {color=#f6d6bd}Foggy{/color} is the keeper. At least she’s not as boring as the other guy.”
        '
        '(eudocia1 set)':
            pass

label eudocia_about_peninsula01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula.”')
    $ eudocia_about_peninsula = 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ description_iason05 = "According to {color=#f6d6bd}Eudocia{/color}, he’s “stiff like a broom.”"
    $ description_foggy02 = "According to {color=#f6d6bd}Eudocia{/color}, her place is lively and “not as boring as {color=#f6d6bd}Pelt of the North{/color}.”"
    if pc_area == "eudociahouse":
        $ can_leave = 1
    else:
        $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "eudocia1"
    menu:
        '“I’m not selling gossip, nor am I buying it. I’ve my hut, my guards, and my lake. I’m an artisan, not an innkeep. If ye need one, ride south, to {color=#f6d6bd}Pelt of the North{/color}. The keeper is stiff like a broom, but offers a nice room.” Her voice is dripping with annoyance. “Or if ye’d rather visit a {i}cheerful{/i} place, ride north, to {color=#f6d6bd}Foggy Lake{/color}. Or was it {i}Foggy’s Lake{/i}? Whatever, {color=#f6d6bd}Foggy{/color} is the keeper. At least she’s not as boring as the other guy.”
        '
        '(eudocia1 set)':
            pass

label eudocia_about_enchanting_items01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you fill an item of mine with pneuma?”')
    label eudocia_about_enchanting_items01after:
        $ eudocia_about_enchanting_items = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if pc_area == "eudociahouse":
            $ eudocia_fluff_inorout = "She points at her golems."
        if pc_area == "eudociahouseinside":
            $ eudocia_fluff_inorout = "She points at the crossbow on the wall, her boots, and her cauldron."
        menu:
            '“That’s not how this works.” [eudocia_fluff_inorout] Her nails are short and clean, and her hands are soft. “I work all the time, but each item takes me days, sometimes a full season. The tribes bring me things to enchant in the early spring, and collect them a year later. I’ve got to...” She blinks a few times, not sure what to say. Her gray eyes widen. “{i}Imagine{/i} stuff. It takes great focus.”
            \n\nYou mention that you’d generously reward her, but she only shrugs. “Ye don’t plant, ye don’t build. I won’t eat dragon bones. For now, do ya warden duties and come by the end of autumn. Maybe I’ll have time to get something done for ye after the thaws.”
            '
            '“What if I’m in desperate need?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What if I’m in desperate need?”')
                if pc_area == "eudociahouse":
                    $ can_leave = 1
                else:
                    $ can_leave = 0
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "eudocia1"
                menu:
                    'She rolls her eyes. “Ye and everyone else.”
                    '
                    '(eudocia1 set)':
                        pass
            '“I’ll think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                jump eudociahouseafterquestione

label eudocia_about_nomoreundeadALL:
    label eudocia_about_nomoreundead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Great changes are happening in the west. {color=#f6d6bd}White Marshes{/color} is now free of necromancy.”')
        $ eudocia_about_nomoreundead = 1
        label eudocia_about_nomoreundead01post:
            $ eudocia_friendship += 1
            if pc_area == "eudociahouse":
                $ custom1 = "at the clouds"
            else:
                $ custom1 = "at the ceiling"
            $ questionpreset = "eudocia1"
            menu:
                'She starts to twirl her hair and looks first at you, then [custom1]. “I knew about a few empty ones there, but was it really much of an issue? The tribe would burn the corpses once they stopped needing them.”
                \n\nAfter you describe the weight of the situation, she grunts in approval. “I was wrong, then.”
                \n\nSoon after you carry on with your tale, she lowers her head and takes a deep breath. “I’ve heard enough.”
                '
                '(eudocia1 set)':
                    pass

    label eudocia_about_nomoreundead02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The necromancer from {color=#f6d6bd}White Marshes{/color} has been forced to leave the village. The undead are gone.”')
        $ eudocia_about_nomoreundead = 2
        jump eudocia_about_nomoreundead01post

    label eudocia_about_nomoreundead03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m afraid these woods may get much more dangerous soon. I hope your golems are capable of facing undead.”')
        $ eudocia_about_nomoreundead = 3
        $ eudocia_friendship -= 1
        $ questionpreset = "eudocia1"
        menu:
            'She stares at you in silence, waiting for you to go on. You describe the situation briefly and her deep breath turns into a snort. She excuses herself with a wave of her hand. “Another fallen village? Weren’t wardens meant to keep the roads safe?”
            \n\nShe tilts her head back. “All of this really goes against my plans. What to do, what to do...”
            '
            '(eudocia1 set)':
                pass

label eudocia_about_asterion_cloak01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Asterion’s{/color} cloak...”')
    $ eudocia_about_asterion_cloak = 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ eudocia_friendship += 1
    menu:
        'Her eyes narrow as she runs her fingers over the fabric. “The pneuma is still in it. It’s going to keep ye warm. Put it on a rock and it will feel like a pillow.”
        \n\nShe falls silent, rubbing one of the leaves with her thumb, as if to wipe off an invisible stain.
        \n\n“Where did ye find it?”
        '
        '“He sold it to {color=#f6d6bd}Foggy{/color}.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He sold it to {color=#f6d6bd}Foggy{/color}.”')
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            if pc_area == "eudociahouse":
                $ eudocia_fluff_inorout = "ground"
            if pc_area == "eudociahouseinside":
                $ eudocia_fluff_inorout = "floor"
            menu:
                'Your words reach her like a jab. She scratches the [eudocia_fluff_inorout] with her foot, and her shoulders slump. You wait for a few breaths, but she says nothing.
                '
                '(eudocia1 set)':
                    pass
        '(lie) “In the woods, among claw marks, blood, and broken branches. I guess he had to flee.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “In the woods, among claw marks, blood, and broken branches. I guess he had to flee.”')
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            $ pc_lies += 1
            $ questionpreset = "eudocia1"
            $ eudocia_about_asterion_cloak_lied = 1
            menu:
                'She nods. “He wouldn’t abandon such a treasure without a good fight. Good thing you found it first, instead of some goblins.”
                \n\nHer relieved smile reaches even her gray eyes.
                '
                '(eudocia1 set)':
                    pass

label eudocia_about_sleeping01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need a place to rest. Can I spend a night here?”')
    $ eudocia_about_sleeping = 1
    if pc_area == "eudociahouse":
        $ can_leave = 1
    else:
        $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "eudocia1"
    menu:
        'Even though she drawls out her words with frustration, she speaks with ease, as if she’s reciting a memorized speech.
        \n\n“I know how harsh the woods can be, but I don’t offer shelter to travelers. I don’t want to look behind my own shoulder for hours, or use my golems to protect ye. Travel north, or south, look for a tavern or an inn. Ye’ll find a safe hearth there.”
        \n\nShe blinks and crosses her arms. “And we’re both adults. Don’t tell me that I {i}could{/i} bind ye with a rope or take away ya blades. The less I have to touch ye, the better.”
        '
        '(eudocia1 set)':
            pass

    label eudocia_about_sleeping02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s getting late. Can I spend a night in your shed?”')
        $ eudocia_about_sleeping = 1
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ eudocia_sleep_available = 1
        $ renpy.notify("New shelter unlocked.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
        $ questionpreset = "eudocia1"
        menu:
            'She sizes you up, opens her mouth, but then lets out a sigh. “I guess it {i}is{/i} getting chilly outside, and ye don’t act like a bandit, so far. Just don’t carry any candles inside, I store hay there.”
            '
            '(eudocia1 set)':
                pass

label eudocia_about_enchanting01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about enchanting?”')
    $ eudocia_about_enchanting = 1
    $ description_eudocia08 = "According to herself, her magical talents manifested when she was a child, and she doesn’t understand them."
    if pc_area == "eudociahouse":
        $ can_leave = 1
    else:
        $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "eudocia1"
    if pc_area == "eudociahouse":
        $ eudocia_fluff_inorout = "on her hips"
    if pc_area == "eudociahouseinside":
        $ eudocia_fluff_inorout = "on her knee"
    menu:
        'She looks at your hands and starts to twirl her hair. “Naught, really. I don’t know {i}how{/i} I do the stuff I do. As a kid, I put pneuma into my toys. I made my earthen sparrow fly, and my whistle gave a tune without being blown. I practiced for years, but by doing, not by understanding.”
        \n\nShe puts a hand [eudocia_fluff_inorout] and observes her clean nails. “I can’t teach stuff that’s in my fingers, or my eyes, or my breath. It’s just a part of me.”
        '
        '(eudocia1 set)':
            pass

label eudocia_about_herself01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, what’s your story? Why do you live so far from any village?”')
    $ eudocia_about_herself = 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    menu:
        'She looks around. “No.”
        '
        '“Fine.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine.”')
            jump eudociahouseafterquestionb
        '“{i}No{/i} what?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}No{/i} what?”')
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            $ eudocia_friendship -= 1
            menu:
                '“I’m not here to tell ye bedtime stories, or to hear about ya own sad life.”
                \n\nShe lets out a long sigh, trying to limit her frustration. “Back off.”
                '
                '(eudocia1 set)':
                    pass

label eudocia_about_plagueALL:
    label eudocia_about_plague01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news from the East. {color=#f6d6bd}Old Págos{/color} is facing a grave plague.”')
        jump eudocia_about_plague01after
    label eudocia_about_plague01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news from the East. {color=#f6d6bd}Old Págos{/color} has faced a grave plague.”')
        jump eudocia_about_plague01after
    label eudocia_about_plague01after:
        $ eudocia_about_plague = 1
        $ oldpagos_plague_warnedplaces += 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'She stands still. “Come... Come again?”
            \n\nWhile you describe the symptoms, she starts to fidget, and finally interrupts you.
            \n\n“Cut it! Have ye heard aught about {color=#f6d6bd}Eulalia{/color} and {color=#f6d6bd}Ireneus{/color}? They’re about 50, 55. A mason and a sculptor. Her eyes are getting bad, he has a limp.”
            '
            '“I never entered the gate.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I never entered the gate.”')
                $ questionpreset = "eudocia1"
                if pc_area == "eudociahouse":
                    $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    'She rubs her arms above her elbows, as if to warm herself up.
                    \n\n“If ye ever ride there again...” She meets your eyes. “Ask around, please. I need to know.”
                    '
                    '(eudocia1 set)':
                        pass

    label eudociaaskedaboutparents01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news about {color=#f6d6bd}your parents{/color}.”')
        $ eudocia_about_parents = 1
        $ eudocia_friendship += 1
        $ pc_goal_iwanttohelppoints += 1
        $ eudocia_about_spiritrock_price_base -= 2
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'She takes a deep breath. “Tell me.”
            '
            '“I’m afraid they didn’t make it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m afraid they didn’t make it.”')
                jump eudociaaskedaboutparents01a
            '“I’m so sorry, {color=#f6d6bd}Eudocia{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m so sorry, {color=#f6d6bd}Eudocia.{/color}.”')
                jump eudociaaskedaboutparents01a
            '“They’re gone.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They’re gone.”')
                jump eudociaaskedaboutparents01a

    label eudociaaskedaboutparents01a:
        menu:
            'She closes her eyes. “I...” Her voice becomes absent. “Back to trade, then. I’m going to lower the price of my spirit rocks for ye. By two dragons. I think that’s fair.”
            \n\nShe opens her gray eyes and you notice the tears. Her voice is shaking. “I need... a moment.”
            '
            '“If it’s any consolation... The plague itself is no more.”' if oldpagos_cured:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If it’s any consolation... The plague itself is no more.”')
                $ eudocia_about_plague_cured = 1
                $ eudocia_friendship += 1
                menu:
                    'You tell her about your deeds, but she stares into the distance without so much as a gesture, and doesn’t ask you a single question. It takes her a minute to form a few words. “So there was no hope for them... But now it’s there for others. Thank ye.”
                    '
                    '“I should brush my horse.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I should brush my horse.”')
                        $ eudocia_friendship += 1
                        jump eudociaaskedaboutparents02a
                    '“I need to ride somewhere else. I’ll see you later.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to ride somewhere else. I’ll see you later.”')
                        jump eudociaaskedaboutparents02b
                    '“I’m afraid I need to ask you some other questions. Time is relentless.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m afraid I need to ask you some other questions. Time is relentless.”')
                        $ eudocia_friendship -= 1
                        jump eudociaaskedaboutparents02c
            '“Definitely. I’ll brush my horse.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Definitely. I’ll brush my horse.”')
                $ eudocia_friendship += 1
                jump eudociaaskedaboutparents02a
            '“It’s time for me to leave. I’ll see you later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s time for me to leave. I’ll see you later.”')
                jump eudociaaskedaboutparents02b
            '“I’m afraid I need to ask you some other questions. Time is relentless.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m afraid I need to ask you some other questions. Time is relentless.”')
                $ eudocia_friendship -= 1
                jump eudociaaskedaboutparents02c

    label eudociaaskedaboutparents02a:
        if not quest_studyingthegolems_description03 or (not quest_studyingthegolems_description03b and pc_class == "scholar"):
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            if pc_class == "scholar":
                $ at_unlock_knowledge = 1
                $ at = 0
            if quest_studyingthegolems_description01:
                $ quest_studyingthegolems_description01 = "I asked {color=#f6d6bd}Eudocia{/color} a few things about the golems."
                $ quest_studyingthegolems_description03 = "I had a chance to take a closer look at one of the golems."
            else:
                $ quest_studyingthegolems_description03 = "I had a chance to take a closer look at one of the golems. Maybe I could learn more from its creator."
            if quest_studyingthegolems == 1:
                $ renpy.notify("Journal updated: Studying the Golems")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Studying the Golems{/i}')
            menu:
                'Once you’re alone, you’ve an opportunity to take a closer look at the nearby golem.
                \n\nIt seems dead, “inactive,” as cityfolk would call it, but the pneuma still makes its chunks float less than an inch away from one another. It doesn’t react to your presence.
                \n\nUnlike the gatekeeper, it bears engraved signs on its larger rocks. Their meaning is unclear to you, and you can’t tell if they’re a decoration, or carriers of a spell.
                '
                'I know these letters.' ( condition="at == 'knowledge'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I know these letters.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    if quest_studyingthegolems == 1:
                        $ renpy.notify("Journal updated: Studying the Golems")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Studying the Golems{/i}')
                    $ quest_studyingthegolems_description03b = "I’ve learned that at least some of the golems are covered with inscriptions, possibly enhancing their powers."
                    menu:
                        'The signs represent regular words used in Wright’s Tablets. Their shapes are very old, angular, not adjusted to the softness of a quill.
                        \n\nThe words read as follows: {i}hunt{/i}, {i}prey{/i}, {i}chase{/i}, {i}meat{/i}, {i}beast{/i}, {i}run{/i}, {i}bring{/i}, {i}wait{/i}, and {i}disguise{/i}.
                        '
                        'I step away.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump eudociahouseonthesquare01afterparentsdead
                'I step away.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump eudociahouseonthesquare01afterparentsdead
        else:
            label eudociahouseonthesquare01afterparentsdead:
                $ questionpreset = "eudocia1"
                if pc_area == "eudociahouse":
                    $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ quarters += 4
                menu:
                    'You use this hour to rest from riding. You exercise for a bit, practice combat stances with your axe, then brush {color=#f6d6bd}[horsename]{/color}, which then gladly takes a nap.
                    \n\nWhen {color=#f6d6bd}Eudocia{/color} leaves her house, she crouches by a bucket of water and washes her face. Once she straightens up and turns toward you, there’s a shadow of a smile on her lips. “I’m glad ye stayed around, but I’ll be fine. Is there aught I can do for ye?”
                    '
                    '(eudocia1 set)':
                        pass
    label eudociaaskedaboutparents02b:
        $ travel_destination = "watchtower"
        menu:
            'She nods and returns to her house. You climb into the saddle.
            '
            'I ride away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride away.')
                jump finaldestinationaftertraveldescription
    label eudociaaskedaboutparents02c:
        $ questionpreset = "eudocia1"
        if pc_area == "eudociahouse":
            $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'She wipes her face on her sleeve, then nods, crosses her arms, and gives you a chilling look.
            '
            '(eudocia1 set)':
                pass

label eudociaaskedabouthealedplague01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You should know... The plague of {color=#f6d6bd}Old Págos{/color} is no more.”')
    $ eudocia_about_plague_cured = 1
    $ eudocia_friendship += 1
    $ questionpreset = "eudocia1"
    if pc_area == "eudociahouse":
        $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'You tell her about your deeds, but she stares into the distance without so much as a gesture, and doesn’t ask you a single question. It takes her a minute to form a few words. “So there was no hope for them... But now it’s there for others. Thank ye.”
        '
        '(eudocia1 set)':
            pass

label eudociaaskedaboutchiselALL:
    label eudociaaskedaboutchisel01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show her the chisel from {color=#f6d6bd}Old Págos{/color}. “It used to belong to a sculptor... Do you recognize it?”')
        $ eudocia_friendship += 2
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ eudocia_about_chisel = 1
        menu:
            'A sad grimace cuts through her face as she rubs her arms. After a few breaths, she holds out her open palm.
            '
            'I give her the chisel.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give her the chisel.')
                if pc_area == "eudociahouseinside":
                    $ pc_area = "eudociahouse"
                    show areapicture eudociahousemiddlebase behind golem01, golem02, eudocia_image_eyes at basicfade
                    $ eudocia_image_golem01 = renpy.random.choice(['turnedback', 'turnedleft', 'turnedright'])
                    if eudocia_image_golem01 == "turnedback":
                        show golem01 turnedback_middle at basicfade
                    elif eudocia_image_golem01 == "turnedleft":
                        show golem01 turnedleft_middle at basicfade
                    elif eudocia_image_golem01 == "turnedright":
                        show golem01 turnedright_middle at basicfade
                    else:
                        hide golem01
                    if eudocia_image_golem02 == "nogolem":
                        show golem02 nogolem_middle at basicfade
                    elif eudocia_image_golem02 == "nogolemplusback":
                        show golem02 nogolemplusback_middle at basicfade
                    else:
                        hide golem02
                menu:
                    'She stands upright in the center of the yard, with feet spread apart, arms stretched out, and the chisel placed in her right hand. After a few heartbeats, the steel rod floats in the air, maybe two feet away from her face, rotating slowly, rising up, and descending, like a stick on a pond’s surface.
                    \n\nHer gray eyes are tender, her voice is close to a whisper. “As a kid, I made a few toys that moved on their own, but they lasted no longer than a single afternoon. A spoon that made all stuff taste sweet, until it melted. One candle that shined, one that gave out a green light, but they also turned into stumps.”
                    \n\n{color=#f6d6bd}Eudocia’s{/color} long, dark hair is now waving around her, but there’s no wind. “I wanted to make aught that would last, with no end. I was twelve, such an {i}adult{/i} soul.” She lets out a chuckle. “So I turned my back on my toys, and took my father’s old, favorite tool. It was always in the shed, for he was afraid it would wear away.”
                    '
                    '“I heard that he was using it to the very end.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I heard that he was using it to the very end.”')
                        $ custom1 = "“I can see that!” Her brief laughter adds strength to her voice."
                        label eudociaaskedaboutchisel02:
                            menu:
                                '[custom1] “The stitches I used to hold the pneuma inside are dwindling. I’ll restore them in no time.”
                                \n\nShe grabs the chisel swiftly. Her hair falls on her shoulders, her eyes now focused, as if she’s an artisan solving a puzzle.
                                \n\n“But why keep it the same? A new owner could put it to new use.”
                                '
                                '“What do you mean?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you mean?”')
                                    jump eudociaaskedaboutchisel03
                    'I don’t interrupt her.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t interrupt her.')
                        $ custom1 = "With a playful smile, she rotates it faster."
                        jump eudociaaskedaboutchisel02

    label eudociaaskedaboutchisel03:
        menu:
            '“Currently, the chisel {i}adapts{/i} to the surface it touches. When used against glass, it makes powerful hits gentler. When against stone, it strengthens them... Ye get the idea.” She points at you with the tool and puts her weight on her left leg. “I’ll remove these limitations, make it so that it will simply enhance any strike made with it. A weapon, well, against rocks. A {i}tool of destruction{/i}.”
            \n\nShe looks up and starts to laugh at her own joke. Her relaxed shell makes her look like a different soul.
            '
            '“Sounds useful indeed.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sounds useful indeed.”')
                $ quarters += 2
                menu:
                    'She returns to her previous position. “Better go ahead and find aught to do. I’m not a kid anymore, but it may still take me a while.”
                    \n\nThe chisel floats again, carefully examined by the enchantress. You find yourself a wooden block and sit down. You inspect your clothes, especially the cloak, and take a look at your blade.
                    \n\nFinally, the enchantress stands still, holding her new creation in one hand, and scratching her chin with the other. You gather your stuff and approach her, but she doesn’t look at you.
                    '
                    '“Something wrong?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Something wrong?”')
                        $ item_magicchisel = 2
                        $ renpy.notify("You received the tool of destruction.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the tool of destruction.{/i}')
                        menu:
                            '“No, not at all. I’m just surprised.” She hands it back to you. “I didn’t expect that my past intuition was this sharp, I thought it would take me {i}much{/i} longer. Well, go ahead, test it. Maybe there?” She points at the wall behind her house.
                            \n\nThe chisel is just as warm as it was when you received it in {color=#f6d6bd}Old Págos{/color}, but now it quivers gently, as if it’s barely confining its power.
                            \n\nYou press it against one of the larger bricks, then hit it with the blunt side of your axe. The rock moves by about two inches, with a pattern of cracks that resembles broken glass. After your next strike, it falls out of the wall, leaving behind only a cloud of dust.
                            '
                            'Shocked, I step back.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Shocked, I step back.')
                                jump eudociaaskedaboutchisel06
                            'Excellent.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Excellent.')
                                label eudociaaskedaboutchisel06:
                                    $ can_leave = 1
                                    $ can_rest = 1
                                    $ can_items = 1
                                    $ questionpreset = "eudocia1"
                                    menu:
                                        '{color=#f6d6bd}Eudocia{/color} welcomes your return with a confident smile. “Pretty good, huh? Thanks to you, I finished what I left behind many years ago.” She takes a deep breath. “Let me know if ye need aught else.”
                                        '
                                        '(eudocia1 set)':
                                            pass

label eudociaaskedaboutshopALL:
    label eudociaaskedaboutshop01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have anything interesting to sell?”')
        $ eudocia_about_selling = 1
        $ renpy.notify("New trader unlocked.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if pc_area == "eudociahouse":
            $ eudocia_fluff_inorout = "house"
        if pc_area == "eudociahouseinside":
            $ eudocia_fluff_inorout = "closet"
        $ eudocia_about_spiritrock_price = (eudocia_about_spiritrock_price_base+appearance_price)
        menu:
            '“Well, I’m not a trader. I do the stuff people ask me about, and they’re not for sale.” She glances at the [eudocia_fluff_inorout], then toward a pocket at her hips. “There’s but one tool that I’m willing to part with, for [eudocia_about_spiritrock_price] bones, but it’s for spell casters only.”
            \n\nShe reaches out to you. On her open palm you see a flat, small pebble, bluish, but in no way unusual.
            \n\n“Ye put it in ya mouth and press it to ya palate. No chewing,” she smirks. “If ye’re a sorcerer, it will restore ya pneuma.”
            '
            'I can’t afford it. (disabled)' if coins < eudocia_about_spiritrock_price:
                pass
            '“I’ll take it. Here are the dragons.”' if coins >= eudocia_about_spiritrock_price:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take it. Here are the dragons.”')
                $ item_spiritrock += 1
                $ coins -= eudocia_about_spiritrock_price
                show screen notifyimage( "You bought a spirit rock.\n-%s" %eudocia_about_spiritrock_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought a spirit rock. -%s {image=cointest}{/i}' %eudocia_about_spiritrock_price)
                jump eudociahouseafterquestiong
            '“What if it’s used by someone who still has pneuma in them? Or can’t use magic?”' if not eudocia_about_spiritrock_problem:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What if it’s used by someone who still has pneuma in them? Or can’t use magic?”')
                $ eudocia_about_spiritrock_problem = 1
                jump eudociaaskedaboutshop01a
            '“Why a pebble? Wouldn’t a potion be easier to use?”' if not eudocia_about_spiritrock:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why a pebble? Wouldn’t a potion be easier to use?”')
                $ eudocia_about_spiritrock = 1
                jump eudociaaskedaboutshop01b
            '“I’ll think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                jump eudociahouseafterquestione

    label eudociaaskedaboutshop01a:
        menu:
            '“Oh. Ye don’t want to do that,” she grabs the ends of her hair. “It will boil ya blood and rip ya skin apart. Each shell is like a bottle for pneuma, it has its limits. Ye can train to contain more of it, like I’ve been doing for more than twenty years now, but there’s no {i}magical rock{/i} that’s going to do it for ye.”
            '
            'I can’t afford it. (disabled)' if coins < eudocia_about_spiritrock_price:
                pass
            '“I’ll take it. Here are the dragons.”' if coins >= eudocia_about_spiritrock_price:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take it. Here are the dragons.”')
                $ item_spiritrock += 1
                $ coins -= eudocia_about_spiritrock_price
                show screen notifyimage( "You bought a spirit rock.\n-%s" %eudocia_about_spiritrock_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought a spirit rock. -%s {image=cointest}{/i}' %eudocia_about_spiritrock_price)
                jump eudociahouseafterquestiong
            '“What if it’s used by someone who still has pneuma in them? Or can’t use magic?”' if not eudocia_about_spiritrock_problem:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What if it’s used by someone who still has pneuma in them? Or can’t use magic?”')
                $ eudocia_about_spiritrock_problem = 1
                jump eudociaaskedaboutshop01a
            '“Why a pebble? Wouldn’t a potion be easier to use?”' if not eudocia_about_spiritrock:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why a pebble? Wouldn’t a potion be easier to use?”')
                $ eudocia_about_spiritrock = 1
                jump eudociaaskedaboutshop01b
            '“I’ll think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                jump eudociahouseafterquestione

    label eudociaaskedaboutshop01b:
        menu:
            '“Do I smell of smoke and mushrooms? I’m not going to play around with flasks and alembics.” She shakes the rock. “This one won’t break, won’t scatter, won’t spoil. Perfect for a traveler, or any buyer, really.”
            \n\nShe steps away and adjusts her dirty robe. “It works, and it won’t hurt ye, if ye’re smart with it. It’s a lifesaver.”
            '
            'I can’t afford it. (disabled)' if coins < eudocia_about_spiritrock_price:
                pass
            '“I’ll take it. Here are the dragons.”' if coins >= eudocia_about_spiritrock_price:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take it. Here are the dragons.”')
                $ item_spiritrock += 1
                $ coins -= eudocia_about_spiritrock_price
                show screen notifyimage( "You bought a spirit rock.\n-%s" %eudocia_about_spiritrock_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought a spirit rock. -%s {image=cointest}{/i}' %eudocia_about_spiritrock_price)
                jump eudociahouseafterquestiong
            '“What if it’s used by someone who still has pneuma in them? Or can’t use magic?”' if not eudocia_about_spiritrock_problem:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What if it’s used by someone who still has pneuma in them? Or can’t use magic?”')
                $ eudocia_about_spiritrock_problem = 1
                jump eudociaaskedaboutshop01a
            '“Why a pebble? Wouldn’t a potion be easier to use?”' if not eudocia_about_spiritrock:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why a pebble? Wouldn’t a potion be easier to use?”')
                $ eudocia_about_spiritrock = 1
                jump eudociaaskedaboutshop01b
            '“I’ll think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                jump eudociahouseafterquestione

    label eudociaaskedaboutshop02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s trade.”')
        show screen shopscreen with dissolve
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        menu:
            'You discuss the price.
            '
            '(eudocia1 set)':
                pass

label eudociaaskedaboutshop01av02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Photios{/color} has sent me to buy a {i}spirit rock{/i} for his daughter. He hopes it will enhance {color=#f6d6bd}Phoibe’s{/color} pneuma.”')
    $ eudocia_about_spiritrock_problem = 1
    $ questionpreset = "eudocia1"
    menu:
        '“Oh. Ye don’t want to try that,” she grabs the ends of her hair. “It would boil her blood and rip her skin apart. Each shell is like a bottle for pneuma, it has its limits. Ye can train to contain more of it, like I’ve been doing for more than twenty years now, but there’s no {i}magical rock{/i} that’s going to do it for ye. But if ye want, I can still sell it to ye.”
        '
        '(eudocia1 set)':
            pass

label eudocia_about_golemsALL:
    label eudocia_about_golems01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about your golems.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if pc_area == "eudociahouse":
            $ eudocia_fluff_inorout = "She walks around the closest sentinel and observes it like a farmer would a donkey before a purchase."
        if pc_area == "eudociahouseinside":
            $ eudocia_fluff_inorout = "She stands up with a sigh and opens a door, then summons the closest sentinel with a single gesture."
        menu:
            '[eudocia_fluff_inorout] “Isn’t it clear what they are? Furniture that walks and works. They carry rocks and logs, hunt, kind of, and protect this place while I rest. What else is there to say?”
            '
            '“Do they talk?”' if not eudocia_about_golems_question1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do they talk?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question1 = 1
                jump eudocia_about_golems01a
            '“How do you make one?”' if not eudocia_about_golems_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do you make one?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question2 = 1
                jump eudocia_about_golems01b
            '“Is it for sale?”' if not eudocia_about_golems_question3: #########if quest_bronzerod != 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is it for sale?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question3 = 1
                jump eudocia_about_golems01c
            '“It’s so loud when it walks... Don’t monsters react to its presence?”' if not eudocia_about_golems_question4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s so loud when it walks... Don’t monsters react to its presence?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question4 = 1
                jump eudocia_about_golems01d
            '“Let’s change the topic.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s change the topic.”')
                if eudocia_about_golems >= 4:
                    jump eudociahouseafterquestioncgolem
                else:
                    jump eudociahouseafterquestionc

    label eudocia_about_golems01a: #Do they talk?
        menu:
            '{color=#f6d6bd}Eudocia{/color} still moves her lips, but her words are coming from the stone creature, which doesn’t move an inch. “No more than the gargoyle ye’ve seen.” The voice is deep, distorted by an echo. “They don’t need meat or bones and listen to my commands, but have no understanding of what’s happening around them. To create a sentient creature, ye’d need a human shell, and a whole lot of necromancy.” The golem raises its hands and shows you its {i}palms{/i}. “And I’m not going to touch that.”
            \n\nShe then mentions that her creation isn’t much of a messenger - it needs to remain close to her. “Just look at it.” The golem covers its nonexistent mouth. “It has no eyes, snout, ears... Seeing the world through its head is like putting ya eyeball into a rose bush. It takes pneuma, and the further away it is, the more exhausting it gets.”
            '
            '“Do they talk?”' if not eudocia_about_golems_question1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do they talk?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question1 = 1
                jump eudocia_about_golems01a
            '“How do you make one?”' if not eudocia_about_golems_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do you make one?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question2 = 1
                jump eudocia_about_golems01b
            '“Is it for sale?”' if not eudocia_about_golems_question3: #########if quest_bronzerod != 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is it for sale?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question3 = 1
                jump eudocia_about_golems01c
            '“It’s so loud when it walks... Don’t monsters react to its presence?”' if not eudocia_about_golems_question4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s so loud when it walks... Don’t monsters react to its presence?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question4 = 1
                jump eudocia_about_golems01d
            '“Let’s change the topic.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s change the topic.”')
                if eudocia_about_golems >= 4:
                    jump eudociahouseafterquestioncgolem
                else:
                    jump eudociahouseafterquestionc

    label eudocia_about_golems01b: #“How do you make one?”
        menu:
            '“I fill each rock with pneuma, bind them together...” She pauses, then waves it off. “Ye won’t build one anyway. Like alchemists, enchanters have their own secrets, but I’ve got no way of sharing my talents with others.”
            '
            '“Do they talk?”' if not eudocia_about_golems_question1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do they talk?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question1 = 1
                jump eudocia_about_golems01a
            '“How do you make one?”' if not eudocia_about_golems_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do you make one?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question2 = 1
                jump eudocia_about_golems01b
            '“Is it for sale?”' if not eudocia_about_golems_question3: #########if quest_bronzerod != 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is it for sale?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question3 = 1
                jump eudocia_about_golems01c
            '“It’s so loud when it walks... Don’t monsters react to its presence?”' if not eudocia_about_golems_question4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s so loud when it walks... Don’t monsters react to its presence?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question4 = 1
                jump eudocia_about_golems01d
            '“Let’s change the topic.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s change the topic.”')
                if eudocia_about_golems >= 4:
                    jump eudociahouseafterquestioncgolem
                else:
                    jump eudociahouseafterquestionc

    label eudocia_about_golems01c: #Is it for sale?
        $ minutes += 5
        menu:
            '“One day, or so I hope.” She points at a golem’s hand. “One wrong order and it’ll tear ya head away, or kick over a house. It won’t ever be {i}safe{/i}, but the dead make for bad customers. And I won’t be blamed for others’ stupidity.”
            \n\nHer further answers come in greater detail, but they’re rather complex. From what you understand, she plans to invent a set of very specific commands that could be quickly learned, then bind them to a wand, binding it to the creature.
            \n\n“I’m still not sure if it’s the safest solution. If a wand was taken by a reaver... Stuff could get ugly.”
            '
            '“Do they talk?”' if not eudocia_about_golems_question1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do they talk?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question1 = 1
                jump eudocia_about_golems01a
            '“How do you make one?”' if not eudocia_about_golems_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do you make one?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question2 = 1
                jump eudocia_about_golems01b
            '“Is it for sale?”' if not eudocia_about_golems_question3: #########if quest_bronzerod != 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is it for sale?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question3 = 1
                jump eudocia_about_golems01c
            '“It’s so loud when it walks... Don’t monsters react to its presence?”' if not eudocia_about_golems_question4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s so loud when it walks... Don’t monsters react to its presence?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question4 = 1
                jump eudocia_about_golems01d
            '“Let’s change the topic.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s change the topic.”')
                if eudocia_about_golems >= 4:
                    jump eudociahouseafterquestioncgolem
                else:
                    jump eudociahouseafterquestionc

    label eudocia_about_golems01d: #Don’t monsters react to its presence? It walks so loudly.
        menu:
            'She lets out a chuckle. “They flee from them as they would from trolls. They can’t stalk their prey, or jump on them from a bush, but when they don’t move for long, beasts take them for rocks. It’s not like they need to breathe. It just sits still, waiting for a roe-deer to get close...”
            \n\nThe golem’s eye suddenly gets brighter. It jumps forward and punches the air. It lands with the sound of thunder. “That’s why I need them to be so large,” the enchantress explains. “I can’t give them {i}muscles{/i}, the speed I give them is pure pneuma. Being firm and heavy helps.”
            \n\nShe disregards your mention of the wrath of the herds. “True, I make more mess than most humans would, but that’s one of the reasons why I stay away from the villages. Being all alone, I give the beasts time to get used to my walls. And my sentinels know to stay away from unicorns and pebblers.”
            '
            '“Do they talk?”' if not eudocia_about_golems_question1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do they talk?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question1 = 1
                jump eudocia_about_golems01a
            '“How do you make one?”' if not eudocia_about_golems_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do you make one?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question2 = 1
                jump eudocia_about_golems01b
            '“Is it for sale?”' if not eudocia_about_golems_question3: #########if quest_bronzerod != 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is it for sale?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question3 = 1
                jump eudocia_about_golems01c
            '“It’s so loud when it walks... Don’t monsters react to its presence?”' if not eudocia_about_golems_question4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s so loud when it walks... Don’t monsters react to its presence?”')
                $ eudocia_about_golems += 1
                $ eudocia_about_golems_question4 = 1
                jump eudocia_about_golems01d
            '“Let’s change the topic.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s change the topic.”')
                if eudocia_about_golems >= 4:
                    jump eudociahouseafterquestioncgolem
                else:
                    jump eudociahouseafterquestionc

label eudociahousecloserlookatthegolem01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if pc_class == "scholar":
        $ at_unlock_knowledge = 1
        $ at = 0
    if quest_studyingthegolems_description01:
        $ quest_studyingthegolems_description01 = "I asked {color=#f6d6bd}Eudocia{/color} a few things about the golems."
        $ quest_studyingthegolems_description03 = "I had a chance to take a closer look at one of the golems."
    else:
        $ quest_studyingthegolems_description03 = "I had a chance to take a closer look at one of the golems. Maybe I could learn more from its creator."
    if quest_studyingthegolems == 1:
        $ renpy.notify("Journal updated: Studying the Golems")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Studying the Golems{/i}')
    menu:
        'It seems dead, “inactive,” as cityfolk would call it, but the pneuma still makes its chunks float less than an inch away from one another. It doesn’t react to your presence.
        \n\nUnlike the gatekeeper, this golem bears engraved signs on its larger rocks. Their meaning is unclear to you, and you can’t tell if they’re a decoration, or carriers of a spell.
        '
        'I know these letters.' ( condition="at == 'knowledge'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I know these letters.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump eudociahousecloserlookatthegolem01b
        'I step away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump eudociahouseonthesquare01

label eudociahousecloserlookatthegolem01b:
    if quest_studyingthegolems == 1:
        $ renpy.notify("Journal updated: Studying the Golems")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Studying the Golems{/i}')
    $ quest_studyingthegolems_description03b = "I’ve learned that at least some of the golems are covered with inscriptions, possibly enhancing their powers."
    menu:
        'The signs represent regular words used in Wright’s Tablets. Their shapes are very old, angular, not adjusted to the softness of a quill.
        \n\nThe words read as follows: {i}hunt{/i}, {i}prey{/i}, {i}chase{/i}, {i}meat{/i}, {i}beast{/i}, {i}run{/i}, {i}bring{/i}, {i}wait{/i}, and {i}disguise{/i}.
        '
        'I step away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
            $ at_unlock_knowledge = 0
            $ at = 0
            jump eudociahouseonthesquare01

label eudociaaskedaboutgolemwords01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I saw some words on your golems. What do they mean?”')
    label eudociaaskedaboutgolemwords02:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        if (eudocia_friendship+appearance_charisma) < 6:
            $ eudocia_about_golems_gray = 1
            menu:
                'She looks at your right elbow. “It’s naught, warden. Decorations.”
                '
                '(eudocia1 set)':
                    pass
        else:
            if quest_studyingthegolems == 1:
                $ renpy.notify("Journal updated: Studying the Golems")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Studying the Golems{/i}')
            $ quest_studyingthegolems_description03b = "I’ve learned that at least some of the golems are covered with inscriptions, possibly enhancing their powers."
            menu:
                'She thinks for a bit, then meets your eyes. “They hold my spells. Each one means aught different. {i}Look{/i}. {i}Chase{/i}. {i}Beast{/i}. {i}Run{/i}. The golems are meant to hunt, and I hope that if aught happens to them, I’ll have an option to put these enhanced rocks into other shells.”
                \n\nShe twirls her hair. “A nice little trick, though I’m not sure it works. I plan to use a few more words, like {i}dig{/i}, or {i}lumber{/i}.”
                '
                '(eudocia1 set)':
                    pass

    label eudociaaskedaboutgolemwords01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the words on your golems...”')
        jump eudociaaskedaboutgolemwords02

label eudociaaskedaboutreading01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Since you have writings on your golems... Could you read some things for me?”')
    if pc_area == "eudociahouse":
        $ can_leave = 1
    else:
        $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "eudocia1"
    $ eudocia_about_reading = 1
    $ description_monastery05 = "I heard that I can ask the monks to read any piece of writing I struggle with."
    menu:
        'Her eyes widen, but she then smiles. “Ye got it wrong. I ask others to write down the words I need, together with pictures, and I then copy them. Ye could go to,” she lets out a sigh, “the monastery, in the far mountains.”
        '
        '(eudocia1 set)':
            pass

label eudocia_about_arrow01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Surely you’ve filled some arrows with pneuma before? Any ideas where this is from?” I show her the one that I found near the fallen tree.')
    $ eudocia_about_arrow = 1
    if pc_area == "eudociahouse":
        $ can_leave = 1
    else:
        $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "eudocia1"
    menu:
        '“Why, are ye tracing a murderer?” She smirks, but then grabs the arrow and takes a quick look. “Black and orange... I don’t know much about wood, but I recognize these feathers. The people of {color=#f6d6bd}Gale Rocks{/color} breed such pheasants.”
        \n\nShe gives it back. “It’s in the far North, close to the coast.”
        '
        '(eudocia1 set)':
            pass

label eudociaaskedaboutmagicsapling01:
    $ eudocia_about_magicsapling = 1
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found a barren field that may be affected by a curse. Do you have anything I could use to see if I’m right?”')
    $ minutes += 5
    if pc_area == "eudociahouseinside":
        $ pc_area = "eudociahouse"
        show areapicture eudociahousemiddlebase behind golem01, golem02, eudocia_image_eyes at basicfade
        $ eudocia_image_golem01 = renpy.random.choice(['turnedback', 'turnedleft', 'turnedright'])
        if eudocia_image_golem01 == "turnedback":
            show golem01 turnedback_middle at basicfade
        elif eudocia_image_golem01 == "turnedleft":
            show golem01 turnedleft_middle at basicfade
        elif eudocia_image_golem01 == "turnedright":
            show golem01 turnedright_middle at basicfade
        else:
            hide golem01
        if eudocia_image_golem02 == "nogolem":
            show golem02 nogolem_middle at basicfade
        elif eudocia_image_golem02 == "nogolemplusback":
            show golem02 nogolemplusback_middle at basicfade
        else:
            hide golem02
    menu:
        '“A cursed field? Where did ye found this stuff?” As you explain briefly, she observes your boots. “I know the place, but...” She steps away and approaches the garden patch by her house. She observes it for a moment, then kneels down, paying no attention to her robe, and reaches for a wooden spade.
        \n\nWhat she digs out looks like a tree sapling with two leaves that are as large as a hand and a thin, elastic stalk. It’s shorter than your head. “Would ye look at that! Still green. Give me two dragons and I’ll put it in a bag with soil. It should survive at least a couple of days.”
        '
        '“How does it work?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How does it work?”')
            menu:
                'She straightens up. “Well, ye plant it, of course. Wait for half an hour and ye’ll see. If it grows an inch...” She frowns, raises the plant to her eyes, and grunts. “Forget it. If it bursts into bloom, the soil is enchanted. If it withers, it’s cursed. Stays the same? No pneuma.”
                \n\nShe lowers it again. “Just be careful {i}when{/i} ye do it. It loves fogs.”
                '
                '“So it’s a plant that {i}grows{/i} by magic?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So it’s a plant that {i}grows{/i} by magic?”')
                    menu:
                        '“...Yes. And it costs two dragons.”
                        '
                        '“Why do you even have such a thing? Are there many magic fields around?”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why do you even have such a thing? Are there many magic fields around?”')
                            menu:
                                '“What? No.” She snorts. “But these plants are the only stuff I can think of right now. I’m trying to make a plant that grows without sunlight, using just water, soil, and pneuma. I’ll know I’m there once it starts to bear fruit.” She glances at your nose. “I swear, don’t even mention mushrooms.”
                                \n\nYou ask her about the purpose of all this, but she just plays with her hair and looks toward the gate. “Just a... hobby of mine.”
                                '
                                'I can’t afford it. (disabled)' if coins < 2:
                                    pass
                                '“I’ll take it. Here are the dragons.”' if coins >= 2:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take it. Here are the dragons.”')
                                    $ item_magicalsapling += 1
                                    $ coins -= 2
                                    show screen notifyimage( "You bought the sapling. -2", "gui/coin2.png")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought the sapling. -2 {image=cointest}{/i}')
                                    jump eudociahouseafterquestiong2
                                '“I’ll think about it.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                                    jump eudociahouseafterquestione
                        'I can’t afford it. (disabled)' if coins < 2:
                            pass
                        '“I’ll take it. Here are the dragons.”' if coins >= 2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take it. Here are the dragons.”')
                            $ item_magicalsapling += 1
                            $ coins -= 2
                            show screen notifyimage( "You bought the sapling. -2", "gui/coin2.png")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought the sapling. -2 {image=cointest}{/i}')
                            jump eudociahouseafterquestiong2
                        '“I’ll think about it.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                            jump eudociahouseafterquestione

label eudociaaskedaboutthedistrustofmonks01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spoke with {color=#f6d6bd}the monks{/color}. They’re quite afraid of you.”')
    if pc_area == "eudociahouse":
        $ can_leave = 1
    else:
        $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "eudocia1"
    $ eudocia_about_monks = 1
    $ eudocia_friendship += 1
    $ minutes += 5
    menu:
        '“Are they, now,” she meets your eyes. “What did they tell ye?” As you recollect your memories, she patiently listens to your tale, staring into the distance with her arms crossed.
        \n\n“So that’s how they see me now. A beast spending every breath to hurt them. Yet they still ask me to put spells in their tools.” She remains still, moving only her lips, drawling out every word. “All it took was for me to move on, to leave {i}them{/i} behind. They call themselves {i}pacifists{/i}, {i}unlike blood-shedding Unites{/i}, they say, yet forced my tribe to work for them, from their birth to the pyre? It’s the same sickness of the soul, {i}believing{/i} that ye see the truth, that all other souls are blind.”
        \n\nWhen she realizes that her voice is getting close to a shout, she falls silent.
        '
        '(eudocia1 set)':
            pass

label eudociaaskedaboutshortcut01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever been to the shortcut?”')
    $ eudocia_about_shortcut = 1
    if pc_area == "eudociahouse":
        $ can_leave = 1
    else:
        $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "eudocia1"
    $ description_shortcut08 = "According to {color=#f6d6bd}Eudocia{/color}, the best way to deal with the monkeys in the far west is to ignore them, so that they get used to one’s sight."
    menu:
        '“Only once,” she admits slowly, “and it’s not a good memory.”
        \n\nHer brief tale is rather vague. She once had to use her golems to travel {i}to the other side{/i}, seeking a remedy for her stomachache. “The beasts were afraid of the noise they make,” she points at the massive stone legs of her creations, “but the monkeys in the far west were too dumb even for that. They kept throwing things at us, even {i}poop{/i},” she pauses, making a disgusted grimace. “We couldn’t reach them, or scare them away.”
        \n\nYou ask what happened next, but she crosses her arms. “Eh. I was told it’s better to ignore them, let them get used to one’s sight. But my stomach was better already, so we just took the long way back.”
        '
        '(eudocia1 set)':
            pass

label eudociaaskedabouthighisland01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever heard about {color=#f6d6bd}High Island{/color}?”')
    $ eudocia_about_highisland = 1
    if pc_area == "eudociahouse":
        $ can_leave = 1
    else:
        $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "eudocia1"
    $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
    $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
    menu:
        '“But of course,” she says right away, but then leans away and glances at your boots. “Though... I didn’t pay much attention to the monks’ tales.” She brushes her dark hair with her fingers, asking you to give her a moment.
        \n\nShe doesn’t share much with you. {color=#f6d6bd}High Island{/color} is the largest island that’s somewhat close to the coast, but its huge volcano makes it a worrying sight. It may be covered with green forests and hills, but no tribe aspires to claim it.
        \n\n“You may want to ask {color=#f6d6bd}Foggy{/color}. She loves tales of weird places.”
        '
        '(eudocia1 set)':
            pass

label eudociaaskedaboutsteephousALL:
    label eudociaaskedaboutsteephouse01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You left {color=#f6d6bd}Old Págos{/color} during the same time when the village in the south collapsed. What happened?”')
        $ questionpreset = "eudocia1"
        $ eudocia_about_steephouse_gray = 1
        if not (eudocia_friendship+appearance_charisma) >= 8 or not eudocia_about_parents:
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            menu:
                'She opens her mouth, then closes it slowly, piercing you with her gray eyes. “I shouldn’t share these grim tales with outsiders. It would give me nothing, and may hurt many Northerners.”
                '
                '(eudocia1 set)':
                    pass
        else:
            jump eudociaaskedaboutsteephouse03

    label eudociaaskedaboutsteephouse02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I helped you, {color=#f6d6bd}Eudocia{/color}, and you can see I’m not a scoundrel. What happened to the village in the south?”')
        label eudociaaskedaboutsteephouse03:
            $ ruinedvillage_name = "Steep House"
            $ description_tertia03 = "According to {color=#f6d6bd}Eudocia{/color}, it’s easier to convince {color=#f6d6bd}Tertia{/color} with a winged hourglass on one’s neck."
            $ eudocia_about_steephouse = 1
            $ minutes += 3
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            if pc_area == "eudociahouse":
                $ eudocia_fluff_inorout = "She looks at the closest golem, then at the tools, and finally at her clean fingernails."
            if pc_area == "eudociahouseinside":
                $ eudocia_fluff_inorout = "She looks at the hearth, then at the crossbow, and finally at her clean fingernails."
            $ questionpreset = "eudocia1"
            menu:
                '“I’m no longer a part of the Northern tribes, I shouldn’t speak in their name.” [eudocia_fluff_inorout] “When ye’re at {color=#f6d6bd}Old Págos{/color}, who speaks with ye?”
                \n\nAfter you mention {color=#f6d6bd}Tertia{/color}, she drawls out her words. “If ye have an hourglass, ye may want to wear it. It’ll be easier to {i}convince{/i} her.” After a long pause you start to look around, and only then does she find the right words. “And... Is she healthy? I haven’t talked with her in many years.”
                \n\nYou admit that your conversations don’t give you the full picture, so all you can do is describe the confidence of her voice, and that the tribe seems to trust her. “I’m happy for her,” she says with an absent voice.
                \n\nYour exchange looks. “It may have little meaning now, but tell her as follows: {i}The warden ought to know about {color=#f6d6bd}Steep House{/color}, {color=#f6d6bd}Little Otter{/color}{/i}.” She looks away, blushing. “She’ll know it’s from me.”
                '
                '(eudocia1 set)':
                    pass

label eudociaaskedaboutbanditsALL:
    label eudociaaskedaboutbandits01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Don’t they bother you?”')
        $ questionpreset = "eudocia1"
        $ eudocia_about_bandits_gray = 1
        if (eudocia_friendship+appearance_charisma) < 6:
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            menu:
                'She puts her hands on her sides and straightens up, displaying her unusual height. “Is this another sick game of hers? If so, tell her I’m not interested either in her head, or her offers.” You notice the sudden movement of her golem.
                '
                '(eudocia1 set)':
                    pass
        else:
            $ custom1 = "“They don’t attack me, but {color=#f6d6bd}Glaucia{/color} is fucking terrifying."
            jump eudociaaskedaboutbandits03

    label eudociaaskedaboutbandits02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You seem to be afraid of the bandits, {color=#f6d6bd}Eudocia{/color}.”')
        $ custom1 = "“I’m not {i}afraid{/i}, {color=#f6d6bd}Glaucia{/color} is fucking terrifying."
        label eudociaaskedaboutbandits03:
            $ eudocia_about_bandits = 1
            $ banditshideout_knowsaboutlumberjackcamp_knowsbanditsareinlumberjackcamp = 1
            $ description_glaucia04 = "{color=#f6d6bd}Eudocia{/color} is afraid of her. “She can’t be reasoned with - if she doesn’t feel threatened, one can only ask her for mercy.”"
            $ description_bandits03 = "According to {color=#f6d6bd}Eudocia{/color}, they may be staying at an old lumberjack camp, though she doesn’t know where it is."
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            menu:
                'She glances at the gate. [custom1] Here’s a little tip, and engrave it on ya soul: she {i}can’t{/i} be reasoned with. If ye’re strong, threaten her, if weak... Ask her for mercy, I guess. She wanted to work with me, but I need no Wright to know her soul is wicked.”
                \n\nShe takes a step toward you. “I {i}think{/i} they’re somewhere in the deep woods. I don’t know much about these lands, I’ve got other stuff to worry about. There’s only one place that I know of that could keep an entire band - an old lumberjack camp. But you won’t reach it through any of the main roads, so...”
                \n\nShe steps back. “That’s that.”
                '
                '(eudocia1 set)':
                    pass

label eudocia_about_whitemarshes01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Why did you ask me to place a rod in {color=#f6d6bd}White Marshes{/color} specifically? Is it because of the undead?”')
    $ eudocia_about_whitemarshes = 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if pc_area == "eudociahouseinside":
        $ custom1 = "scratches her foot, then points at the door"
    else:
        $ custom1 = "scratches the ground with her foot, then points at her golem"
    menu:
        '“I... No, why?” she [custom1]. “I still need to do a bit of work with the sentinels, but I hope to offer one to them, maybe in the spring. It could replace ten, twenty humans. The villagers may not have much food {i}right now{/i}, but I know how to be patient.”
        '
        '“You’re willing to make deals with necromancers?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re willing to make deals with necromancers?”')
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            menu:
                '“And why not? Would you want me to build a chapel next? I don’t judge those I don’t know well. These lands are harsh, I’m sure the tribe from {color=#f6d6bd}Marshes{/color} is doing what it feels is necessary. Maybe my sentinels could help them part with the empty ones?”
                '
                '(eudocia1 set)':
                    pass
        '“They have quite a bunch of awoken corpses, you know.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They have quite a bunch of awoken corpses, you know.”')
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            menu:
                '“Erm,” she moves her hair behind her shoulder. “All I can do is hope they know when to stop.”
                '
                '(eudocia1 set)':
                    pass
        '“That’s very... Pragmatic of you.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s very... Pragmatic of you.”')
            $ eudocia_friendship += 1
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            menu:
                '“What can I say?” She brushes her long hair with her fingers. “I’d rather be safe than sacred.”
                '
                '(eudocia1 set)':
                    pass

label eudocia_about_gargoyle01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s with the gargoyle?”')
    $ eudocia_about_gargoyle = 1
    if pc_area == "eudociahouse":
        $ can_leave = 1
    else:
        $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "eudocia1"
    menu:
        '“Can’t an enchantress show off her trophy?” She gives you a proud smile. “My sentinels took it down years ago. The tribe of {color=#f6d6bd}Old Págos{/color} is fond of statues, so I have my own, like in the old days, long before monks came to the North.”
        \n\nSeeing your puzzled look, she twirls her hair. “A dead gargoyle on the road, or by a village gate, was meant to scare off evil spirits. I don’t know about that, but its sight sure taught the local beasts who they’re dealing with.”
        '
        '(eudocia1 set)':
            pass

label eudocia_about_jobALL:
    label eudocia_about_job00:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a job.”')
        $ eudocia_about_job01 = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if whitemarshes_nomoreundead or whitemarshes_destroyed or whitemarshes_attacked:
            $ quest_bronzerod = 4
            menu:
                'She stands still for a moment, then stares into the distance with her gray, absent irises. “I’ve got some stuff that could use another hand. Ye up for some danger, if it comes to it?” You nod and ask what sort of creature is bothering her. “Nah, I meant riding and climbing. If ye can do this without grabbing that axe of yas, perfect. Now, give me a moment.”
                \n\nShe opens one of the heavy doors to her house and you catch a glimpse of a messy bed and a floor covered with clothes. After a minute, she shows up with a large sack filled with rods made of smooth, clean bronze.
                \n\n“Here’s the gist of it. I need ye to get to eight spots across the peninsula and place these rods on them. High buildings, trees, mountainsides. I don’t really travel much,” she lets out a confident chuckle, “so I can’t hold ya hand. I {i}need{/i} one of them in {color=#f6d6bd}White Marshes{/color}, in the wetlands far west of here.”
                '
                '“Huh, about that...”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Huh, about that...”')
                    if pc_area == "eudociahouse":
                        $ can_leave = 1
                    else:
                        $ can_leave = 0
                    $ can_rest = 1
                    $ can_items = 1
                    $ questionpreset = "eudocia1"
                    if orentius_convinced or orentius_banished:
                        $ eudocia_about_nomoreundead = 1
                        $ eudocia_friendship += 1
                        if pc_area == "eudociahouse":
                            $ custom1 = "at the clouds"
                        else:
                            $ custom1 = "at the ceiling"
                        $ questionpreset = "eudocia1"
                        menu:
                            'She starts to twirl her hair and looks first at you, then [custom1]. “I knew about a few empty ones there, but was it really much of an issue? The tribe would burn the corpses once they stopped needing them.”
                            \n\nAfter you describe the weight of the situation, she grunts in approval. “I was wrong, then.”
                            \n\nSoon after you carry on with your tale, she lowers her head and takes a deep breath. “I’ve heard enough. All I care about now is that {color=#f6d6bd}the mayor{/color} won’t allow you to place a rod. I’ve no task for you after all.”
                            '
                            '(eudocia1 set)':
                                pass
                    elif whitemarshes_attacked:
                        $ eudocia_about_nomoreundead = 3
                        $ eudocia_friendship -= 1
                        $ questionpreset = "eudocia1"
                        menu:
                            'You describe the situation briefly and her deep breath turns into a snort. She excuses herself with a wave of her hand. “So you attacked the village? Weren’t wardens meant to keep the roads safe?”
                            \n\nShe tilts her head back with annoyance. “All of this really goes against my plans. What to do, what to do... Well, I’ve no task for you after all.”
                            '
                            '(eudocia1 set)':
                                pass
                    elif whitemarshes_destroyed:
                        $ eudocia_about_nomoreundead = 3
                        $ eudocia_friendship -= 1
                        $ questionpreset = "eudocia1"
                        menu:

                            'You describe the situation briefly and her deep breath turns into a snort. She excuses herself with a wave of her hand. “Another fallen village? Weren’t wardens meant to keep the roads safe?”
                            \n\nShe tilts her head back with annoyance. “All of this really goes against my plans. What to do, what to do... Well, I’ve no task for you after all.”
                            '
                            '(eudocia1 set)':
                                pass
        else:
            $ quest_bronzerod = 1
            $ item_bronzerod = eudocia_bronzerod_max
            $ renpy.notify("New entry: Bronze Rods")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Bronze Rods{/i}')
            menu:
                'She stands still for a moment, then stares into the distance with her gray, absent irises. “I’ve got some stuff that could use another hand. Ye up for some danger, if it comes to it?” You nod and ask what sort of creature is bothering her. “Nah, I meant riding and climbing. If ye can do this without grabbing that axe of yas, perfect. Now, give me a moment.”
                \n\nShe opens one of the heavy doors to her house and you catch a glimpse of a messy bed and a floor covered with clothes. After a minute, she shows up with a large sack filled with rods made of smooth, clean bronze.
                \n\n“Here’s the gist of it. I need ye to get to eight spots across the peninsula. High buildings, trees, mountainsides. I don’t really travel much,” she lets out a confident chuckle, “so I can’t hold ya hand. I {i}need{/i} one of them in {color=#f6d6bd}White Marshes{/color}, in the wetlands far west of here. Other than that, ye need to keep ya eyes open.”
                \n\nShe takes one of the rods. “Once ye reach a good spot, place one of these as high as ye can. I’ll pay ye in dragons. Two for each one, but place at least four before ye come to see me. I need as many of them out there as possible.”
                '
                '“So far so good. What are they for?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So far so good. What are they for?”')
                    jump eudocia_about_job02

    label eudocia_about_job01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a job.”')
        $ eudocia_about_job01 = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if eudocia_about_nomoreundead:
            $ quest_bronzerod = 4
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            menu:
                '“And I’ve none for ye. Not after all the things ye’ve done in {color=#f6d6bd}White Marshes{/color}.”
                '
                '(eudocia1 set)':
                    pass
        elif whitemarshes_nomoreundead or whitemarshes_destroyed or whitemarshes_attacked:
            $ quest_bronzerod = 4
            menu:
                'She stands still for a moment, then cocks her head to the side. “I’ve got some stuff that could use another hand. Ye up for some danger, if it comes to it?” You nod and ask what sort of creature is bothering her. “Nah, I meant riding and climbing. If ye can do it without grabbing that axe of yas, fine. Now, give me a moment.”
                \n\nShe opens one of the heavy doors to her house and you catch a glimpse of a messy bed and a floor covered with clothes. After a minute, she shows up with a large sack filled with rods made of smooth, clean bronze.
                \n\n“Here’s the gist of it. I need ye to get to eight spots across the peninsula and place these rods on them. High buildings, trees, mountainsides. I don’t really travel much,” she lets out a confident chuckle, “so I can’t hold ya hand. I {i}need{/i} one of them in {color=#f6d6bd}White Marshes{/color}, in the wetlands far west of here.”
                '
                '“Huh, about that...”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Huh, about that...”')
                    if pc_area == "eudociahouse":
                        $ can_leave = 1
                    else:
                        $ can_leave = 0
                    $ can_rest = 1
                    $ can_items = 1
                    $ questionpreset = "eudocia1"
                    if orentius_convinced or orentius_banished:
                        $ eudocia_about_nomoreundead = 1
                        $ eudocia_friendship += 1
                        if pc_area == "eudociahouse":
                            $ custom1 = "at the clouds"
                        else:
                            $ custom1 = "at the ceiling"
                        $ questionpreset = "eudocia1"
                        menu:
                            'She starts to twirl her hair and looks first at you, then [custom1]. “I knew about a few empty ones there, but was it really much of an issue? The tribe would burn the corpses once they stopped needing them.”
                            \n\nAfter you describe the weight of the situation, she grunts in approval. “I was wrong, then.”
                            \n\nSoon after you carry on with your tale, she lowers her head and takes a deep breath. “I’ve heard enough. All I care about now is that {color=#f6d6bd}the mayor{/color} won’t allow you to place a rod. I’ve no task for you after all.”
                            '
                            '(eudocia1 set)':
                                pass
                    elif whitemarshes_attacked:
                        $ eudocia_about_nomoreundead = 3
                        $ eudocia_friendship -= 1
                        $ questionpreset = "eudocia1"
                        menu:
                            'You describe the situation briefly and her deep breath turns into a snort. She excuses herself with a wave of her hand. “So you attacked the village? Weren’t wardens meant to keep the roads safe?”
                            \n\nShe tilts her head back with annoyance. “All of this really goes against my plans. What to do, what to do... Well, I’ve no task for you after all.”
                            '
                            '(eudocia1 set)':
                                pass
                    elif whitemarshes_destroyed:
                        $ eudocia_about_nomoreundead = 3
                        $ eudocia_friendship -= 1
                        $ questionpreset = "eudocia1"
                        menu:
                            'You describe the situation briefly and her deep breath turns into a snort. She excuses herself with a wave of her hand. “Another fallen village? Weren’t wardens meant to keep the roads safe?”
                            \n\nShe tilts her head back with annoyance. “All of this really goes against my plans. What to do, what to do... Well, I’ve no task for you after all.”
                            '
                            '(eudocia1 set)':
                                pass
        else:
            $ quest_bronzerod = 1
            $ item_bronzerod = eudocia_bronzerod_max
            $ renpy.notify("New entry: Bronze Rods")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Bronze Rods{/i}')
            menu:
                'She stands still for a moment, then cocks her head to the side. “I’ve got some stuff that could use another hand. Ye up for some danger, if it comes to it?” You nod and ask what sort of creature is bothering her. “Nah, I meant riding and climbing. If ye can do it without grabbing that axe of yas, fine. Now, give me a moment.”
                \n\nShe opens one of the heavy doors to her house and you catch a glimpse of a messy bed and a floor covered with clothes. After a minute, she shows up with a large sack filled with rods made of smooth, clean bronze.
                \n\n“Here’s the gist of it. I need ye to get to eight spots across the peninsula. High buildings, trees, mountainsides. I don’t really travel much,” she lets out a confident chuckle, “so I can’t hold ya hand. I {i}need{/i} one of them in {color=#f6d6bd}White Marshes{/color}, in the wetlands far west of here. Other than that, ye need to keep ya eyes open.”
                \n\nShe takes one of the rods. “Once ye reach a good spot, place one of these as high as ye can. I’ll pay ye in dragons. Two for each one, but place at least four before ye come to see me. I need as many of them out there as possible.”
                '
                '“So far so good. What are they for?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So far so good. What are they for?”')
                    jump eudocia_about_job02

    label eudocia_about_job02:
        menu:
            '“Well, there’s magic in them, as ye can imagine.” You weigh a rod in your hand. Even though it’s more than two feet long, it’s light, empty inside - you could bend it on your knee. The bag also contains a long hemp cord and a scrap of cloth.
            \n\n“If I were to send my golems away, let’s say a mile or two from here, they’d stop moving at all, waiting for me to show up.” She approaches the nearest sentinel and touches its {i}chest{/i}. “They carry similar rods inside, so the plan is to give my orders better {i}range{/i}, so to speak. I’m tired of depending on hirelings, especially since they no longer stop by.”
            \n\nShe leans against the golem, with her arms crossed. “Questions?”
            '
            '“How much time do I have?”' if not eudocia_bronzerod01p01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How much time do I have?”')
                $ eudocia_bronzerod01p01 = 1
                jump eudocia_bronzerod01p01
            '“Some of the locals may not be happy with me putting bronze rods on their rooftops.”' if not eudocia_bronzerod01p02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Some of the locals not be happy with me putting bronze rods on their rooftops.”')
                $ eudocia_bronzerod01p02 = 1
                jump eudocia_bronzerod01p02
            '{image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”' if eudocia_bronzerod01p02 and not eudocia_bronzerod01p03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”')
                $ eudocia_bronzerod01p03 = 1
                jump eudocia_bronzerod01p03
            '“...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”' if not eudocia_bronzerod01p04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”')
                $ eudocia_bronzerod01p04 = 1
                jump eudocia_bronzerod01p04
            '“We have a deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                jump eudociahouseafterquestionf

    label eudocia_bronzerod01p01:
        menu:
            '“Oh, don’t worry about it.” She dusts off the golem’s arm. “Let’s say... Before the leaves turn yellow?”
            '
            '“How much time do I have?”' if not eudocia_bronzerod01p01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How much time do I have?”')
                $ eudocia_bronzerod01p01 = 1
                jump eudocia_bronzerod01p01
            '“Some of the locals may not be happy with me putting bronze rods on their rooftops.”' if not eudocia_bronzerod01p02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Some of the locals not be happy with me putting bronze rods on their rooftops.”')
                $ eudocia_bronzerod01p02 = 1
                jump eudocia_bronzerod01p02
            '{image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”' if eudocia_bronzerod01p02 and not eudocia_bronzerod01p03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”')
                $ eudocia_bronzerod01p03 = 1
                jump eudocia_bronzerod01p03
            '“...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”' if not eudocia_bronzerod01p04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”')
                $ eudocia_bronzerod01p04 = 1
                jump eudocia_bronzerod01p04
            '“We have a deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                jump eudociahouseafterquestionf

    label eudocia_bronzerod01p02:
        menu:
            'She gives you a puzzled look. “Wardens do have their ways to get on people’s good side, correct?”
            '
            '“How much time do I have?”' if not eudocia_bronzerod01p01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How much time do I have?”')
                $ eudocia_bronzerod01p01 = 1
                jump eudocia_bronzerod01p01
            '“Some of the locals may not be happy with me putting bronze rods on their rooftops.”' if not eudocia_bronzerod01p02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Some of the locals not be happy with me putting bronze rods on their rooftops.”')
                $ eudocia_bronzerod01p02 = 1
                jump eudocia_bronzerod01p02
            '{image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”' if eudocia_bronzerod01p02 and not eudocia_bronzerod01p03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”')
                $ eudocia_bronzerod01p03 = 1
                jump eudocia_bronzerod01p03
            '“...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”' if not eudocia_bronzerod01p04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”')
                $ eudocia_bronzerod01p04 = 1
                jump eudocia_bronzerod01p04
            '“We have a deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                jump eudociahouseafterquestionf

    label eudocia_bronzerod01p03:
        $ quarters += 1
        if (eudocia_friendship+appearance_charisma) > 1:
            $ eudocia_bronzerod_coinsperrod = 3
            menu:
                'You haggle for a bit and you notice a moment of weakness. As you insist on even more, she starts to twirl her hair.
                \n\n“Fine, three for each. It’s over twenty in total, so show some decency and don’t make me wait longer than necessary. If ye do all eight rods, I {i}may{/i} give ye aught else.”
                '
                '“How much time do I have?”' if not eudocia_bronzerod01p01:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How much time do I have?”')
                    $ eudocia_bronzerod01p01 = 1
                    jump eudocia_bronzerod01p01
                '“Some of the locals may not be happy with me putting bronze rods on their rooftops.”' if not eudocia_bronzerod01p02:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Some of the locals not be happy with me putting bronze rods on their rooftops.”')
                    $ eudocia_bronzerod01p02 = 1
                    jump eudocia_bronzerod01p02
                '{image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”' if eudocia_bronzerod01p02 and not eudocia_bronzerod01p03:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”')
                    $ eudocia_bronzerod01p03 = 1
                    jump eudocia_bronzerod01p03
                '“...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”' if not eudocia_bronzerod01p04:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”')
                    $ eudocia_bronzerod01p04 = 1
                    jump eudocia_bronzerod01p04
                '“We have a deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                    jump eudociahouseafterquestionf
        else:
            menu:
                'You haggle for a bit, but her distrust is like a wall. She waves your arguments off.
                \n\n“I’m not a merchant, I don’t gather coins for the thrill of it. I’m putting almost twenty dragons on the table here, should be enough. Do all eight rods and I {i}may{/i} prepare aught else for ye.”
                '
                '“How much time do I have?”' if not eudocia_bronzerod01p01:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How much time do I have?”')
                    $ eudocia_bronzerod01p01 = 1
                    jump eudocia_bronzerod01p01
                '“Some of the locals may not be happy with me putting bronze rods on their rooftops.”' if not eudocia_bronzerod01p02:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Some of the locals not be happy with me putting bronze rods on their rooftops.”')
                    $ eudocia_bronzerod01p02 = 1
                    jump eudocia_bronzerod01p02
                '{image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”' if eudocia_bronzerod01p02 and not eudocia_bronzerod01p03:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”')
                    $ eudocia_bronzerod01p03 = 1
                    jump eudocia_bronzerod01p03
                '“...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”' if not eudocia_bronzerod01p04:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”')
                    $ eudocia_bronzerod01p04 = 1
                    jump eudocia_bronzerod01p04
                '“We have a deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                    jump eudociahouseafterquestionf

    label eudocia_bronzerod01p04:
        $ eudocia_friendship -= 1
        menu:
            'Her gray eyes give you a long, disquieting look. You could swear it’s getting colder here.
            \n\n“I won’t ask for ya trust and I don’t need it. Either help me, or leave the rods and do ya own stuff.”
            '
            '“How much time do I have?”' if not eudocia_bronzerod01p01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How much time do I have?”')
                $ eudocia_bronzerod01p01 = 1
                jump eudocia_bronzerod01p01
            '“Some of the locals may not be happy with me putting bronze rods on their rooftops.”' if not eudocia_bronzerod01p02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Some of the locals not be happy with me putting bronze rods on their rooftops.”')
                $ eudocia_bronzerod01p02 = 1
                jump eudocia_bronzerod01p02
            '{image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”' if eudocia_bronzerod01p02 and not eudocia_bronzerod01p03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} “I may be forced to pull some strings to get it done. Two dragon bones won’t be enough.”')
                $ eudocia_bronzerod01p03 = 1
                jump eudocia_bronzerod01p03
            '“...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”' if not eudocia_bronzerod01p04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...and I can be sure that you’ve no plans to raid the villages with an army of unstoppable sentinels, right?”')
                $ eudocia_bronzerod01p04 = 1
                jump eudocia_bronzerod01p04
            '“We have a deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We have a deal.”')
                jump eudociahouseafterquestionf

label eudocia_about_job01rewardALL:
    label eudocia_about_job01rewardsuccess01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to collect my reward for the bronze rods.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ eudocia_bronzerod_debt = (eudocia_bronzerod_installed*eudocia_bronzerod_coinsperrod)-eudocia_bronzerod_debt_paid1
        $ eudocia_bronzerod_debt_paid1 = eudocia_bronzerod_debt_paid1+eudocia_bronzerod_debt
        if eudocia_bronzerod_installed == 4:
            $ eudocia_friendship -= eudocia_bronzerod_friendship
            $ eudocia_friendship += 2
            $ eudocia_bronzerod_friendship = 2
            $ eudocia_bronzerod_installed_paidfor = 4
        elif eudocia_bronzerod_installed == 5:
            $ eudocia_friendship -= eudocia_bronzerod_friendship
            $ eudocia_friendship += 2
            $ eudocia_bronzerod_friendship = 2
            $ eudocia_bronzerod_installed_paidfor = 5
        elif eudocia_bronzerod_installed == 6:
            $ eudocia_friendship -= eudocia_bronzerod_friendship
            $ eudocia_friendship += 3
            $ eudocia_bronzerod_friendship = 3
            $ eudocia_bronzerod_installed_paidfor = 6
        elif eudocia_bronzerod_installed == 7:
            $ eudocia_friendship -= eudocia_bronzerod_friendship
            $ eudocia_friendship += 3
            $ eudocia_bronzerod_friendship = 3
            $ eudocia_bronzerod_installed_paidfor = 7
        else:
            $ eudocia_friendship -= eudocia_bronzerod_friendship
            $ eudocia_friendship += 4
            $ eudocia_bronzerod_friendship = 4
            $ eudocia_bronzerod_installed_paidfor = 8
        if eudocia_bronzerod_debt > 0:
            $ coins += eudocia_bronzerod_debt
            show screen notifyimage( "+%s" %eudocia_bronzerod_debt, "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+%s {image=cointest}{/i}' %eudocia_bronzerod_debt)
            menu:
                '{color=#f6d6bd}Eudocia{/color} wipes her hands on her robe, puts one into her pocket, and waits for you to describe the locations where you’ve placed the rods. She asks you for a few details, then thinks aloud. “Let’s see... [eudocia_bronzerod_installed] rods in total, so that would be... Here ye go.”
                '
                '“I guess we’re done here.”' if not item_bronzerod:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I guess we’re done here.”')
                    if eudocia_bronzerod_installed < eudocia_bronzerod_max:
                        if pc_goal == "iwanttohelp":
                            $ pc_goal_iwanttohelppoints += 1
                        $ custom1 = "I wish ye had better luck, but each step helps me. Such a journey would take me weeks. Or it wouldn’t, for I wouldn’t try it."
                    else:
                        $ eudocia_about_spiritrock_price_base -= 2
                        if pc_goal == "iwanttohelp":
                            $ pc_goal_iwanttohelppoints += 2
                        $ custom1 = "Fantastic. As a bonus reward for placing all of the rods, you can buy my {i}spirit rocks{/i} cheaper. Such a journey would take me weeks. Or it wouldn’t, for I wouldn’t try it."
                    jump eudocia_about_job01rewardsuccess03
                'I pull out my pouch.' if item_bronzerod:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pull out my pouch.')
                    if pc_area == "eudociahouse":
                        $ can_leave = 1
                    else:
                        $ can_leave = 0
                    $ can_rest = 1
                    $ can_items = 1
                    $ questionpreset = "eudocia1"
                    menu:
                        '“Great, great. Keep it up.”
                        '
                        '(eudocia1 set)':
                            pass
        elif not item_bronzerod:
            $ quest_bronzerod = 2
            $ quest_bronzerod_description06 = "I’ve collected my reward."
            $ renpy.notify("Quest completed: Bronze Rods")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bronze Rods{/i}')
            if pc_goal == "iwanttohelp":
                $ pc_goal_iwanttohelppoints += 1
            if pc_area == "eudociahouse":
                $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            menu:
                '“I already paid ye, and I can {i}sense{/i} that no new rods have been placed.”
                \n\nOnce you explain that you’ve lost the other rods, she nods. “I wish ye had better luck, but each step helps me. Such a journey would take me weeks. Or it wouldn’t, for I wouldn’t try it.” She chuckles, but as she twirls her hair, her eyes grow absent again.
                '
                '(eudocia1 set)':
                    pass
        else:
            if pc_area == "eudociahouse":
                $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            menu:
                '“I already paid ye, and I can {i}sense{/i} that no new rods have been placed.”
                '
                '(eudocia1 set)':
                    pass

    label eudocia_about_job01rewardsuccess03:
        $ quest_bronzerod = 2
        $ quest_bronzerod_description06 = "I’ve collected my reward."
        $ renpy.notify("Quest completed: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bronze Rods{/i}')
        if pc_area == "eudociahouse":
            $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        if pc_goal == "iwanttohelp":
            $ pc_goal_iwanttohelppoints += 1
        menu:
            '“It looks so, it looks so. Thanks, [pcname]. [custom1]” She chuckles, but as she twirls her hair, her eyes grow absent again.
            '
            '(eudocia1 set)':
                pass

    label eudocia_about_job01rewardfailure01nomarshes:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I won’t finish the job.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ eudocia_bronzerod_debt = (eudocia_bronzerod_installed*eudocia_bronzerod_coinsperrod)/2
        if eudocia_about_nomoreundead == 1 or eudocia_about_nomoreundead == 2:
            $ custom1 = "Ye burnt an army of undead, yet haven’t found a way to place one rod in {color=#f6d6bd}White Marshes{/color}?"
        elif eudocia_about_nomoreundead == 3:
            $ custom1 = "Ye threw the bogs into chaos, yet haven’t found a way to place one rod in {color=#f6d6bd}White Marshes{/color}?"
        else:
            $ custom1 = "All this and ye haven’t found a way to place one in {color=#f6d6bd}White Marshes{/color}?"
        menu:
            'She looks into the now-empty sack. Her voice is on the verge of shouting. “Are ye serious? [custom1]”
            \n\nShe walks away, looking up. Her gray eyes are on the edge of fury. “Fine, whatever. I’ll pay ye half. I need the rest to order new rods.”
            '
            'I nod.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod.')
                jump eudocia_about_job01rewardfailure02a
            '“Let’s even things out. Keep your dragons.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s even things out. Keep your dragons.”')
                jump eudocia_about_job01rewardfailure02b

    label eudocia_about_job01rewardfailure01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I won’t finish the job.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ eudocia_bronzerod_debt = (eudocia_bronzerod_installed*eudocia_bronzerod_coinsperrod)
        if eudocia_about_nomoreundead == 1 or eudocia_about_nomoreundead == 2:
            $ custom1 = " before ye made {color=#f6d6bd}the mayor{/color} angry at ye"
        elif eudocia_about_nomoreundead == 3:
            $ custom1 = " before ye threw it into chaos"
        else:
            $ custom1 = ""
        menu:
            'She looks into the now-empty sack. Her voice is on the verge of shouting. “Are ye serious? Ye haven’t even placed four of them? Did ye {i}at least{/i} leave one in {color=#f6d6bd}White Marshes{/color}[custom1]?”
            '
            '“I did.”' if eudocia_bronzerod_rodin_whitemarshes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I did.”')
                jump eudocia_about_job01rewardfailure02
            '“I didn’t.”' if not eudocia_bronzerod_rodin_whitemarshes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t.”')
                jump eudocia_about_job01rewardfailure03ban

    label eudocia_about_job01rewardfailure02:
        menu:
            'She walks away with crossed arms, looking up. Her eyes are on the edge of fury. “Fine, better than naught. But I’ve got no clue where to find new rods. One step forward, two steps back.”
            '
            'I don’t say anything.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t say anything.')
                jump eudocia_about_job01rewardfailure02a
            '“In that case, let’s even things out. Keep your dragons.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “In that case, let’s even things out. Keep your dragons.”')
                jump eudocia_about_job01rewardfailure02b

    label eudocia_about_job01rewardfailure02a:
        $ coins += eudocia_bronzerod_debt
        show screen notifyimage( "Quest completed: Bronze Rods.\n+%s" %eudocia_bronzerod_debt, "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bronze Rods. +%s {image=cointest}{/i}' %eudocia_bronzerod_debt)
        $ quest_bronzerod = 3
        $ quest_bronzerod_description08 = "I’ve informed {color=#f6d6bd}Eudocia{/color} about my failure. She wasn’t happy, but I’ve collected my reward."
        $ questionpreset = "eudocia1"
        menu:
            'She reaches into her pocket and you tell her about the rods you placed. She hands you the dragon bones and steps away, avoiding your eyes.
            '
            '(eudocia1 set)':
                pass

    label eudocia_about_job01rewardfailure02b:
        menu:
            'Her long gaze is penetrating. “Is that an apology?”
            '
            '“Exactly.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Exactly.”')
                $ quest_bronzerod = 2
                $ quest_bronzerod_description08 = "I’ve informed {color=#f6d6bd}Eudocia{/color} about my failure. She wasn’t happy."
                $ renpy.notify("Quest completed: Bronze Rods")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bronze Rods{/i}')
                $ eudocia_friendship += 2
                if pc_area == "eudociahouse":
                    $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "eudocia1"
                menu:
                    '“I accept,” she nods, “but no more fuck ups.”
                    \n\nOnce you’re done talking about the rods you placed, she puts a hand on her hip and leans to the side, tapping her fingers.
                    '
                    '(eudocia1 set)':
                        pass
            '“It’s a promise. I’ll do better next time.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s a promise I’ll do better next time.”')
                $ quest_bronzerod = 2
                $ quest_bronzerod_description08 = "I’ve informed {color=#f6d6bd}Eudocia{/color} about my failure. She wasn’t happy."
                $ eudocia_friendship += 1
                $ renpy.notify("Quest completed: Bronze Rods")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bronze Rods{/i}')
                if pc_area == "eudociahouse":
                    $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "eudocia1"
                menu:
                    '“We’ll see. Next time, at least admit your fuck up.”
                    \n\nOnce you’re done talking about the rods you placed, she puts a hand on her hip and leans to the side, tapping her fingers.
                    '
                    '(eudocia1 set)':
                        pass

    label eudocia_about_job01rewardfailure03ban:
        $ quest_bronzerod = 3
        $ quest_bronzerod_description08 = "I’ve informed {color=#f6d6bd}Eudocia{/color} about my failure. She wasn’t happy."
        $ renpy.notify("Quest completed: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bronze Rods{/i}')
        $ eudocia_ban = 1
        $ travel_destination = "watchtower"
        menu:
            '“Unbelievable,” she grabs her hair and pulls, shaking her fist and breathing heavily. “What are ye even good for? Eating troll shit? I’m not giving ye a single bone. Go into the fogs before...”
            \n\nThe closest golem turns in place and jumps toward you like a thunderous rockslide. {color=#f6d6bd}Eudocia’s{/color} voice gets deeper, distorted by an echo as it comes from the stone creature itself. “Pack ya bags! The next time I see ye, ye better have my {color=#f6d6bd}twenty dragons{/color}. Ye won’t shirk it off!”
            \n\n{color=#f6d6bd}[horsename]{/color} trots toward the gate without waiting for your order.
            '
            'Let’s get out of her sight.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s get out of her sight.')
                jump finaldestinationaftertraveldescription

label eudocia_about_jobnumber2ALL:
    label eudocia_about_jobnumber201a:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you need help with anything else?”')
        $ eudocia_about_job02 = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ quest_eudociaflower = 1
        $ renpy.notify("New entry: Flowers for Eudocia")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Flowers for Eudocia{/i}')
        menu:
            'Her lips form a shadow of a smile. “I do, but it won’t be as much of an {i}ordeal{/i}. Just a simple errand.”
            \n\nShe moves closer and pulls out a dry flower petal from her pocket. “See, it’s like an orange tulip, but has much larger leaves. It’s called snake bait. Bring me one or two, freshly picked, I’ll pay ye five dragons. Fair enough?”
            '
            '“{i}Five{/i}? What do you need it for?”' if not eudocia_bronzerod02p02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}Five{/i}? What do you need it for?”')
                $ eudocia_bronzerod02p02 = 1
                jump eudocia_about_jobnumber202
            '“Any tips where I can find it?”' if not eudocia_bronzerod02p03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips where I can find it?”')
                $ eudocia_bronzerod02p03 = 1
                jump eudocia_about_jobnumber203
            '“Weirdly enough, I already have the herb with me.”' if item_snakebait:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Weirdly enough, I already have the herb with me.”')
                jump eudociahousepchasflower01
            '“Deal.”' if not item_snakebait:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                jump eudociahouseafterquestione

    label eudocia_about_jobnumber202:
        menu:
            '“I simply {i}want{/i} it.” Her voice gets colder. “These flowers are hard to find. I’d pay five dragons for them any day.”
            \n\nYou start to ask another question, but she warns you with a scowl. “That’s all ye need to know.”
            '
            '“{i}Five{/i}? What do you need it for?”' if not eudocia_bronzerod02p02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}Five{/i}? What do you need it for?”')
                $ eudocia_bronzerod02p02 = 1
                jump eudocia_about_jobnumber202
            '“Any tips where I can find it?”' if not eudocia_bronzerod02p03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips where I can find it?”')
                $ eudocia_bronzerod02p03 = 1
                jump eudocia_about_jobnumber203
            '“Weirdly enough, I already have the herb with me.”' if item_snakebait:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Weirdly enough, I already have the herb with me.”')
                jump eudociahousepchasflower01
            '“Deal.”' if not item_snakebait:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                jump eudociahouseafterquestione

    label eudocia_about_jobnumber203:
        $ quest_eudociaflower_description01 = "According to {color=#f6d6bd}Eudocia{/color}, the flowers can be found in shadowy meadows that grow in deep forests."
        $ renpy.notify("Journal updated: Flowers for Eudocia")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Flowers for Eudocia{/i}')
        menu:
            '“That’s the hard part. Ye can try in the western villages, or in the deep woods. They need light, so not in caves, but stay in shadows, so below trees. Edges of meadows, would be my guess. Or maybe ye’ll find one just by the main road? Keep your eyes open.”
            '
            '“{i}Five{/i}? What do you need it for?”' if not eudocia_bronzerod02p02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}Five{/i}? What do you need it for?”')
                $ eudocia_bronzerod02p02 = 1
                jump eudocia_about_jobnumber202
            '“Any tips where I can find it?”' if not eudocia_bronzerod02p03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any tips where I can find it?”')
                $ eudocia_bronzerod02p03 = 1
                jump eudocia_about_jobnumber203
            '“Weirdly enough, I already have the herb with me.”' if item_snakebait:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Weirdly enough, I already have the herb with me.”')
                jump eudociahousepchasflower01
            '“Deal.”' if not item_snakebait:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                jump eudociahouseafterquestione

    label eudocia_about_jobnumber201b:
        if pc_area == "eudociahouse":
            $ eudocia_fluff_inorout = "She crosses her arms."
        if pc_area == "eudociahouseinside":
            $ eudocia_fluff_inorout = "She reaches for her pipe."
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ eudocia_about_job02 = 1
        $ questionpreset = "eudocia1"
        menu:
            '[eudocia_fluff_inorout] “Nah. Not ya help.”
            '
            '(eudocia1 set)':
                pass

label eudociahousepchasflowerALL:
    label eudociahousepchasflower01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I brought you flowers.”')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ eudocia_friendship += 1
        menu:
            'Her eyes widen as she moves closer to you. “And I’ve got your dragons. Here.”
            \n\nHer outstretched hand is shaking.
            '
            '“...How about eight?”':
                label eudociahousepchasflower01a:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...How about eight?”')
                    menu:
                        'Her eyes are piercing through your skull.
                        '
                        '“Forget it. Here, take them.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it. Here, take them.”')
                            jump eudociahousereward01positive5
                        '(lie) “Turns out, a lot of people want them. I could get ten or more, but I’d rather keep my word.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “Turns out, a lot of people want them. I could get ten or more, but I’d rather keep my word.”')
                            $ pc_lies += 1
                            jump eudociahousereward02neutral8
            '“They aren’t good for you, you know.”' if pc_class == "scholar" or item_snakebait_truth:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They aren’t good for you, you know.”')
                menu:
                    '“Ye’ve got no reason to worry. We had a deal, [pcname].”
                    \n\nHer bottom lip is shaking - the hunger in her gray eyes makes you lean away.
                    '
                    '“So be it. Here you go. Just as we agreed.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So be it. Here you go. Just as we agreed.”')
                        jump eudociahousereward01positive5
                    '“...How about eight?”':
                        jump eudociahousepchasflower01a
                    '“I’m not going to sell them to you.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not going to sell them to you.”')
                        $ eudocia_friendship -= 1
                        $ eudocia_about_flower_refusal = day
                        $ pc_goal_iwanttohelppoints += 1
                        jump eudociahousereward02negative0
                    '“I’m sorry, but I can’t. I’m not going to hurt you for coin.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sorry, but I can’t. I’m not going to hurt you for coin.”')
                        $ eudocia_friendship += 0
                        $ eudocia_about_flower_refusal = day
                        $ pc_goal_iwanttohelppoints += 1
                        jump eudociahousereward02negative0
            '“Here you go.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here you go.”')
                jump eudociahousereward01positive5

    label eudociahousereward01positive5:
        $ quest_eudociaflower_description03 = "I received my reward."
        show screen notifyimage( "Journal updated: Flowers for Eudocia.\n+5", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Flowers for Eudocia. +5 {image=cointest}{/i}')
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ quest_eudociaflower = 2
        $ eudocia_friendship += 2
        $ coins += 5
        $ item_snakebait -= 1
        $ questionpreset = "eudocia1"
        menu:
            '“Fine job, fine job,” she says quietly, examining the petals carefully.
            '
            '(eudocia1 set)':
                pass

    label eudociahousereward02neutral8:
        $ quest_eudociaflower_description03 = "I received my reward."
        show screen notifyimage( "Journal updated: Flowers for Eudocia.\n+8", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Flowers for Eudocia. +8 {image=cointest}{/i}')
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ quest_eudociaflower = 2
        $ eudocia_friendship += 0
        $ coins += 8
        $ item_snakebait -= 1
        $ questionpreset = "eudocia1"
        menu:
            'Her shoulders slump, and her voice gets close to a whisper. “Fine.”
            \n\nShe examines the petals carefully, avoiding your look.
            '
            '(eudocia1 set)':
                pass

    label eudociahousereward02negative0:
        $ quest_eudociaflower_description04 = "I called off our deal."
        if pc_goal == "iwanttohelp":
            $ pc_goal_iwanttohelppoints += 1
        $ renpy.notify("Quest completed: Flowers for Eudocia")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Flowers for Eudocia{/i}')
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ quest_eudociaflower = 3
        $ eudocia_friendship -= 1
        $ questionpreset = "eudocia1"
        menu:
            'She looks away. A strand of hair hides her angry gray eyes.
            '
            '(eudocia1 set)':
                pass

label eudociaaskedaboutmissinghunters01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A few hunters recently left {color=#f6d6bd}Creeks{/color}, and haven’t returned so far. {color=#f6d6bd}Dalia{/color}, {color=#f6d6bd}Admon{/color}, {color=#f6d6bd}Vaschel{/color}. Have you met them?”')
    if pc_area == "eudociahouse":
        $ can_leave = 1
    else:
        $ can_leave = 0
    $ can_rest = 1
    $ can_items = 1
    $ eudocia_about_missinghunters = 1
    $ questionpreset = "eudocia1"
    menu:
        '“{color=#f6d6bd}Admon{/color}... He was here, alright. Asked me about the lands east of the stone bridge in the north, but I couldn’t help him much. Those lands are better left to...” She pauses, then waves it off.
        '
        '(eudocia1 set)':
            pass

label eudocia_about_roadclearingALL:
    label eudocia_about_roadclearing01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The roads around the watchtower are in terrible shape. Why don’t your golems look after them?”')
        $ eudocia_about_roadclearing = 1
        menu:
            '“Why would I bother?” You expect her to continue, but her question is earnest.
            '
            '“The paths are getting overgrown. Soon, getting to the other villages will be close to impossible.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The paths are getting overgrown. Soon, getting to the other villages will be close to impossible.”')
                menu:
                    'She twirls her hair, looking in the direction of the tower. “It may be for the better,” she starts listlessly, then shakes her head gently. “Ye may be right. I hoped the trail would take care of itself, with traders and all, but the years are getting emptier. Still, I need my {i}workers{/i} to seek food, and to guard my walls.” She speaks mostly to herself.
                    '
                    '“I could bring you some rations in return.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could bring you some rations in return.”')
                        $ eudocia_about_roadclearing_price = (eudocia_about_roadclearing_price_base+appearance_price-(eudocia_bronzerod_installed_paidfor*2))
                        if eudocia_about_roadclearing_price <= 4:
                            $ eudocia_friendship += 1
                            if pc_area == "eudociahouse":
                                $ can_leave = 1
                            else:
                                $ can_leave = 0
                            $ can_rest = 1
                            $ can_items = 1
                            $ eudocia_about_missinghunters = 1
                            $ questionpreset = "eudocia1"
                            $ eudocia_about_roadclearing_cleared = day
                            menu:
                                'She glances into your eyes. “Ye’ve already done a lot for me, and with so many rods placed around the peninsula, sending the golems into the woods won’t be too much of a cost. I’ll give one of them new orders before I go to sleep.”
                                '
                                '(eudocia1 set)':
                                    pass
                        else:
                            menu:
                                'She observes your boots, then crosses her arms. “The more bronze rods there are spread across the peninsula, the easier it is for me to send the golems into the woods. For now, let’s say {color=#f6d6bd}[eudocia_about_roadclearing_price]{/color} rations. I guess gentler roads will get me more food anyway, so I don’t need ye to bring me any barrels.”
                                '
                                '“Fine. Where should I put all this?”' if item_rations >= eudocia_about_roadclearing_price:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. Where should I put all this?”')
                                    jump eudocia_about_roadclearing03
                                'I can’t afford it. (disabled)' if item_rations < eudocia_about_roadclearing_price:
                                    pass
                                '“I’ll think about it.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                                    jump eudociahouseafterquestionc

    label eudocia_about_roadclearing02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Let’s talk about clearing the roads.”')
        $ eudocia_about_roadclearing_price = (eudocia_about_roadclearing_price_base+appearance_price-(eudocia_bronzerod_installed_paidfor*2))
        if eudocia_about_roadclearing_price <= 4:
            $ eudocia_friendship += 1
            if pc_area == "eudociahouse":
                $ can_leave = 1
            else:
                $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            $ eudocia_about_missinghunters = 1
            $ questionpreset = "eudocia1"
            $ eudocia_about_roadclearing_cleared = day
            menu:
                'She glances into your eyes. “Ye’ve already done a lot for me, and with so many rods placed around the peninsula, sending the golems into the woods won’t be too much of a cost. I’ll give one of them new orders before I go to sleep.”
                '
                '(eudocia1 set)':
                    pass
        else:
            menu:
                '“{color=#f6d6bd}[eudocia_about_roadclearing_price]{/color} food rations would be fair.”
                '
                '“Fine. Where should I put all this?”' if item_rations >= eudocia_about_roadclearing_price:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. Where should I put all this?”')
                    jump eudocia_about_roadclearing03
                'I can’t afford it. (disabled)' if item_rations < eudocia_about_roadclearing_price:
                    pass
                '“I’ll think about it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                    jump eudociahouseafterquestionc

    label eudocia_about_roadclearing03:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ eudocia_about_missinghunters = 1
        $ questionpreset = "eudocia1"
        $ eudocia_about_roadclearing_cleared = day
        $ item_rations -= eudocia_about_roadclearing_price
        $ renpy.notify("You gave away %s food rations." %eudocia_about_roadclearing_price)
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away %s food rations.{/i}' %eudocia_about_roadclearing_price)
        $ eudocia_friendship += 1
        menu:
            'She makes a vague gesture toward the nearest stool. “I’ll give a golem new orders before I go to sleep.”
            '
            '(eudocia1 set)':
                pass
