default foragers_friendship = 0
default foragers_firsttime = 0
default foragers_greeting_fluff = 0
default foragers_greeting_fluff_old = 0
default foggylake_foragers_lastvisit = 0

default foragers_tzvi_darksecret_unknown = 0

default foragers_about_mushrooms = 0
default foragers_about_rawhide = 0
default foragers_about_missinghunters = 0
default foragers_about_travelers = 0
default foragers_about_rumors = 0
default foragers_about_traps = 0
default foragers_about_furlesswolf = 0

default foragers_caius_heardabout = 0 # foggy_about_militarycamp - vision
default foragers_caius_voice = 0 # foggy_about_militarycamp - vision
default foragers_caius_friendship = 0
default foragers_caius_debate = 0
default foragers_caius_spokento = 0
default foragers_caius_aboutvision = 0
default foragers_caius_aboutvision_gray = 0

default foragers_quest = 0
default foragers_quest_daythreshold = 10
default foragers_quest_reward = 0
default foragers_quest_question01 = 0
default foragers_quest_question02 = 0
default foragers_quest_question03 = 0
default foragers_quest_question04 = 0
default foragers_quest_question05 = 0
default foragers_quest_question06 = 0
default foragers_quest_question07 = 0
default foragers_quest_question08 = 0
default foragers_quest_question09 = 0
default foragers_quest_question10 = 0
default foragers_quest_question_efren = 0
default foragers_quest_message_timer = 0

default foragers_about_gatherthecrew = 0
default foragers_about_gatherthecrew_tzvi_recruited = 0
default foragers_about_gatherthecrew_rejected = 0
default foragers_about_gatherthecrew_price = 0
default tzvi_highisland_joined = 0

label foggylakeforagers01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the foragers.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ foggylake_foragers_lastvisit = day
    if not foragers_firsttime:
        if not foggylake_firsttime_floor:
            $ custom1 = "There’s also {color=#f6d6bd}a third man{/color}. Unlike the rest of the staff, he has an unkempt beard and worn clothes made of blue fabric, patched with scraps of flour sacks. He has only the right hand, though unlike the tavern keeper he has kept the rest of his arm. He’s looking down to examine a trap, but his shoulders are slumped, eyes absent. {color=#f6d6bd}Ilan{/color} doesn’t introduce him."
        else:
            $ custom1 = "There’s also {color=#f6d6bd}the one-handed man{/color} you saw in the attic. Unlike the rest of the staff, he has an unkempt beard and worn clothes made of blue fabric, patched with scraps of flour sacks. He’s looking down to examine a trap, but his shoulders are slumped, eyes absent. {color=#f6d6bd}Ilan{/color} doesn’t introduce him."
        $ foragers_firsttime = 1
        menu:
            'Once {color=#f6d6bd}the man in black fur{/color} hears your steps, he nudges his companion and nods toward you. They put away the old noose traps they were trying to fix, proper for hares and small birds.
            \n\n{color=#f6d6bd}The tall one{/color} spreads his arms, thundering his loud welcome. “A roadwarden, aye? I guess we’re going to see each other a lot. I’m {color=#f6d6bd}Ilan{/color}, and this shortie here is {color=#f6d6bd}Tzvi{/color}.” {color=#f6d6bd}The man in the black fur{/color} looks up, frowning.
            \n\n[custom1]
            '
            '“[pcname]. Nice to meet you.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “%s. Nice to meet you.”' %pcname)
                jump foggylakeforagersintroduction01
            'I greet them with a nod.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I greet them with a nod.')
                jump foggylakeforagersintroduction01
    elif (quest_birdhunting and not foragingground_bird_taken and day > foragingground_quest_timer and quest_birdhunting != 3) or (quest_birdhunting and not foragingground_bird_taken and foragingground_bird_gone and quest_birdhunting != 3):
        $ quest_birdhunting = 3
        $ renpy.notify("Journal updated: Bird Hunting")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bird Hunting{/i}')
        $ quest_birdhunting_description02 = "The bird is nowhere to be found."
        if not foragingground_bird_gone:
            $ achievement_animalssavedpoints += 1
            $ foragingground_bird_gone = 1
        $ questionpreset = "foragers1"
        $ foragers_friendship -= 1
        $ foggylake_foragers_lastvisit = day
        menu:
            '“I just realized,” after every other word {color=#f6d6bd}Ilan{/color} claps the palm of one hand with the dorsal of the other. “The bird we wanted to catch is gone. It returned to the woods, or hwatever.” He waves a hand with resignation, just like his mother tends to do. “So, no more work on our side.”
            '
            '(preset foragers1)':
                pass
    else:
        if not foggylake_foragers_lastvisit:
            $ foggylake_foragers_lastvisit = day
            if foragers_friendship < 1:
                $ foragers_greeting_fluff = "They look away. As you get closer, {color=#f6d6bd}Tzvi{/color} sighs. And {color=#f6d6bd}Ilan{/color} speaks with annoyance. “Aye?”"
            elif foragers_friendship < 5:
                $ foragers_greeting_fluff = "They greet you with a nod. “Hi there, friend,” says {color=#f6d6bd}Ilan{/color}."
            elif foragers_friendship < 10:
                $ foragers_greeting_fluff = "{color=#f6d6bd}Tzvi{/color} smiles toward you. “Come, come, friend. How are you doing?”"
            else:
                $ foragers_greeting_fluff = "They greet you with bright smiles. “Good to see you in one piece, friend,” says {color=#f6d6bd}Ilan{/color}. “Doing good?”"
        else:
            $ foragers_greeting_fluff = renpy.random.choice(['They are chatting about the weather, planning the next couple of hours.', '{color=#f6d6bd}Tzvi{/color} is sitting on the ground, while two others are leaning against the palisade. They glance toward you, but say nothing.', 'They wait for you to speak.', 'One of them tells a story, but stops once you approach them. {color=#f6d6bd}Ilan’s{/color} frowns. “Aye?”', '{color=#f6d6bd}Tzvi{/color} is trying to remove a green mark from his jacket with his own spit.'])
        $ questionpreset = "foragers1"
        menu:
            '[foragers_greeting_fluff]
            '
            '(preset foragers1)':
                pass

label foggylakeforagersintroductionALL:
    label foggylakeforagersintroduction01:
        if item_wingedhourglass_worn:
            $ foragers_caius_voice = 1
            menu:
                '{color=#f6d6bd}Tzvi{/color} stares at the hourglass hanging from your neck. “Hwat’s with the wings?” His grating voice is uniquely inquisitive. “Are you a missionary?”
                '
                'I laugh. “Not at all. Many people wear these in {color=#f6d6bd}Hovlavan{/color}.”' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I laugh. “Not at all. Many people wear these in {color=#f6d6bd}Hovlavan{/color}.”')
                    menu:
                        'He frowns. “So you’re just wearing it, for no reason?”
                        '
                        '“Yeah. It’s just a trinket.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah. It’s just a trinket.”')
                            jump foggylakeforagersintroduction01caiusargument01
                        '“I’m expressing my beliefs, sure, but I don’t try to convert anyone.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m expressing my beliefs, sure, but I don’t try to convert anyone.”')
                            jump foggylakeforagersintroduction01caiusargument02
                '“If anyone asks about my faith, I’ll say what I know, but I’m not a priest.”' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If anyone asks about my faith, I’ll say what I know, but I’m not a priest.”')
                    $ foragers_caius_friendship += 2
                    $ foragers_friendship += 0
                    $ pc_faithpoints_opportunities += 1
                    $ pc_faithpoints += 2
                    menu:
                        '“Is that so,” his growling voice gets much colder, but {color=#f6d6bd}Ilan{/color} clears his throat and chips in. “You may want to take it off hwile you’re not in the city. You won’t find many allies in the North, other than {color=#f6d6bd}Old Págos{/color} and {color=#f6d6bd}Gale Rocks{/color}. Folks around here have their own traditions.”
                        \n\n{color=#f6d6bd}The third man{/color} looks at you with smiling eyes - his lips are completely covered by the beard. “You’re brave,” he whispers, “traveling in The Land of the Beasts, but showing to all that you’re not one of them. Beasts, I mean.” {color=#f6d6bd}Tzvi{/color} scoffs loudly, but the man goes on. “We stand where the others bow down, for we’re ready to bring good deeds with us.” He has the accent of the cityfolk. Same as yours.
                        '
                        'I smile back at him.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile back at him.')
                            $ foragers_caius_friendship += 1
                            $ foragers_friendship -= 1
                            $ custom2 = "“Be at peace, roadwarden,” he says with a smile and reaches for another trap. His gestures are quicker and more confident.\n\n{color=#f6d6bd}Tzvi{/color} looks at you both in silence, and once {color=#f6d6bd}Ilan{/color} speaks, you notice his fake smile."
                            jump foggylakeforagersintroduction03
                        'I just stare at him. I don’t want the others to think I see them as “beasts”.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I just stare at him. I don’t want the others to think I see them as “beasts”.')
                            $ custom2 = "After a few breaths, he reaches for another trap, and is now a bit more awake.\n\n“Aye, don’t bother with him. He sometimes has such {i}moments{/i},” {color=#f6d6bd}Ilan{/color} shrugs."
                            jump foggylakeforagersintroduction03
                        'I cross my arms. “I do what I can, but I see all good souls as my allies.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cross my arms. “I do what I can, but I see all good souls as my allies.”')
                            $ foragers_caius_friendship -= 1
                            $ foragers_friendship += 1
                            $ custom2 = "Taken by surprise, he lowers his head. “You ain’t ready for the path of thorns and claws.” He reaches for another trap, though his gestures are even slower than before. After a short pause, {color=#f6d6bd}Ilan{/color} smiles."
                            jump foggylakeforagersintroduction03
                '“I’m expressing my beliefs, sure, but I don’t try to convert anyone.”' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m expressing my beliefs, sure, but I don’t try to convert anyone.”')
                    $ foragers_caius_friendship += 1
                    $ foragers_friendship += 1
                    $ pc_faithpoints_opportunities += 1
                    $ pc_faithpoints += 1
                    label foggylakeforagersintroduction01caiusargument02:
                        if (pc_class == "scholar" and pc_religion == "theunitedchurch") or (pc_class == "scholar" and pc_religion == "ordersoftruth") or (pc_class == "scholar" and pc_religion == "fellowship"):
                            $ at_unlock_knowledge = 1
                            $ at = 0
                        menu:
                            '“Is that so,” he growls, but his eyes soften. {color=#f6d6bd}Ilan{/color} puts on an unconvinced smile. “You may want to take it off hwile you’re not in the city. You won’t find many allies in the North, other than {color=#f6d6bd}Old Págos{/color} and {color=#f6d6bd}Gale Rocks{/color}. Folks around here have their own traditions.”
                            \n\n{color=#f6d6bd}The third man{/color} gives you a curious glance. “You’re brave to wear the blessed sign,” he whispers, “but The Wright needs souls willing to fight in their name.” {color=#f6d6bd}Tzvi{/color} rolls his eyes, but the man goes on. “The pagans look at us, judge our lips and hands. We ought to be brave, don’t throw away your salvation. Think of what The Tribe of The Southern Valley did centuries ago, when they hid their hourglasses to buy ibexes from The Ice Clan.”
                            \n\nHe has the accent of the cityfolk. Same as yours.
                            '
                            'I can turn this around. “The Tribe did so for a good reason. Don’t you remember? They were fighting for survival.”' ( condition="at == 'knowledge'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can turn this around. “The Tribe did so for a good reason. Don’t you remember? They were fighting for survival.”')
                                $ at_unlock_knowledge = 0
                                $ at = 0
                                menu:
                                    '“One-fifth of them died just a year later! If they had kept their trust, Wright’s mercy would have saved them all.”
                                    '
                                    '“...Or none of them. The Wright saves those they choose, our prayers mean little.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Or none of them. The Wright saves who they choose, not who we want them to save.”')
                                        menu:
                                            'He shakes his head, his beard is like a sweeping broom. “They’d tainted their souls, lost their purpose. They dies for a reason, like all of us.”
                                            '
                                            '“You don’t know Wright’s Tablets. It is written: {i}There was great sadness among The Wright and their tribes, for Zev had burnt before his time.{/i}”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t know Wright’s Tablets. It is written: {i}There was great sadness among The Wright and their tribes, for Zev had burnt before his time.{/i}”')
                                                $ foragers_caius_debate = 1
                                                $ foragers_caius_friendship += 3
                                                $ pc_faithpoints += 3
                                                $ custom2 = "“How dare you...” He raises his arms and shakes his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“I may not know them as much as I should. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                jump foggylakeforagersintroduction03
                                            '“If you were truly thinking that, you would not hide behind the walls. Instead, you’d let The Wright decide when to take you away.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you were truly thinking that, you would not hide behind the walls. Instead, you’d let The Wright decide when to take you away.”')
                                                $ foragers_caius_debate = 1
                                                $ foragers_caius_friendship += 3
                                                $ pc_faithpoints += 3
                                                $ custom2 = "He freezes, giving you a puzzled look. He raises his arms, shaking his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“I may sometimes get lost. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                jump foggylakeforagersintroduction03
                                            '“You tread on dangerous ground. Or would you say the same to parents of ill children?”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You tread on dangerous ground. Or would you say the same to parents of ill children?”')
                                                $ foragers_caius_debate = 1
                                                $ foragers_caius_friendship += 3
                                                $ pc_faithpoints += 3
                                                $ custom2 = "He freezes with a terrified grimace. His eyes mist over at your harsh look. He then raises his arms, shaking his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, some souls ought not to hear my words. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                jump foggylakeforagersintroduction03
                                    '“Wright’s Tablets don’t mention it was a punishment of any sort. It’s more likely they were lucky to even get that far, considering their situation.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Wright’s Tablets don’t mention it was a punishment of any sort. It’s more likely they were lucky to even get that far, considering their situation.”')
                                        menu:
                                            'He raises his chin. “Their {i}situation{/i} was their own doing. They were weak in faith, seeking help among the pagan tribes. If it had not been for their broken paths and betrayals, they would not have been pushed into such a rough path.”
                                            '
                                            'I look at him in disbelief. “It was the Tribe of The {i}Western{/i} Valley that was punished for their wrongdoings. It’s a completely different story, about feeding the beastfolk with human blood.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at him in disbelief. “It was the Tribe of The {i}Western{/i} Valley that was punished for their wrongdoings. It’s a completely different story, about feeding the beastfolk with human blood.”')
                                                $ foragers_caius_debate = 1
                                                $ foragers_caius_friendship += 3
                                                $ pc_faithpoints += 3
                                                $ custom2 = "“How dare you...” He raises his arms and shakes his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, I may not know The Tablets as much as I should. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                jump foggylakeforagersintroduction03
                                            '“That’s not what’s said in Wright’s Tablets. Their story starts with the description of the long winter, and the fire that took away their supplies. They made mistakes, but none of them were grave.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s not what’s said in Wright’s Tablets. Their story starts with the description of the long winter, and the fire that took away their supplies. They made mistakes, but none of them were grave.”')
                                                $ foragers_caius_debate = 1
                                                $ foragers_caius_friendship += 3
                                                $ pc_faithpoints += 3
                                                $ custom2 = "He frowns in disbelief and mentions a few of their sins, but you remind him that they all occurred {i}after{/i} the events you’re discussing. He finally raises his arms, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, I may not know The Tablets as much as I should. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                jump foggylakeforagersintroduction03
                                            '“You attribute to them misdeeds based on their struggles, but it’s just as likely their land was simply harsh. None of us deserves every bad thing that happens, nor every good thing. Think of emperor Adir’s childhood.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You attribute to them misdeeds based on their struggles, but it’s just as likely their land was simply harsh. None of us deserves every bad thing that happens, nor every good thing. Think of emperor Adir’s childhood.”')
                                                $ foragers_caius_debate = 1
                                                $ foragers_caius_friendship += 3
                                                $ pc_faithpoints += 3
                                                $ custom2 = "He freezes with a terrified grimace. His eyes mist over at your harsh look. He then raises his arms, shaking his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, I may be lost in my thoughts. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                    '“You know that’s impossible. The Wright promised they would never use the wrath of the herds against us.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know that’s impossible. The Wright promised they would never use the wrath of the herds against us.”')
                                        menu:
                                            'He shudders, but then takes the stance of a preacher. “The Wright may not have ordered the beasts to charge at them, but they didn’t defend them either! Their hand was just, and knew that nothing good may come of that tribe!”
                                            '
                                            '“You contradict the lessons of many tales. All sorts of heroes and leaders used to be good-for-nothings until Wright’s calling inspired them to change their paths. It wasn’t a reward, it was an encouragement.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You contradict the lessons of many tales. All sorts of heroes and leaders used to be good-for-nothings until Wright’s calling inspired them to change their paths. It wasn’t a reward, it was an encouragement.”')
                                                $ foragers_caius_debate = 1
                                                $ foragers_caius_friendship += 3
                                                $ pc_faithpoints += 3
                                                $ custom2 = "He freezes with a terrified grimace. His eyes mist over at your harsh look. He then raises his arms, shaking his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, I may be lost in my thoughts. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                            '“Don’t you remember the story of Hila? She was a part of their tribe, yet brought a lot of good to thousands of souls. And it happened {i}while{/i} they were struggling, not after that.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you remember the story of Hila? She was a part of their tribe, yet brought a lot of good to thousands of souls. And it happened {i}while{/i} they were struggling, not after that.”')
                                                $ foragers_caius_debate = 1
                                                $ foragers_caius_friendship += 3
                                                $ pc_faithpoints += 3
                                                $ custom2 = "With a puzzled frown he looks at his companions, but they spare him nothing more than a shrug. You explain that Hila was a heroine who got rid of the unicorns in The Growing Mountains, and the man’s eyes widen. He raises his arms and shakes his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, my knowledge of The Tablets is not as deep as it should be. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                jump foggylakeforagersintroduction03
                                            '“And what else, should The Wright throw the entire tribe into a snake pit and say {i}it wasn’t me, the snakes did it{/i}? You make them look like a petty brat, or a coward who can’t follow their own rules.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what else, should The Wright throw the entire tribe into a snake pit and say {i}it wasn’t me, the snakes did it{/i}? You make them look like a petty brat, or a coward who can’t follow their own rules.”')
                                                $ foragers_caius_debate = 1
                                                $ foragers_caius_friendship += 3
                                                $ pc_faithpoints += 3
                                                $ custom2 = "“How dare you...” He raises his arms and shakes his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, I may be injust in my words. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                jump foggylakeforagersintroduction03
                            '“If it happens, it happens.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If it happens, it happens.”')
                                $ foragers_caius_friendship += 1
                                $ foragers_friendship -= 1
                                $ custom2 = "“Be at peace, roadwarden,” he says with a smile and reaches for another trap. His gestures are quicker and more confident.\n\n{color=#f6d6bd}Tzvi{/color} looks at you both in silence, and once {color=#f6d6bd}Ilan{/color} speaks, you notice his fake smile."
                                $ at_unlock_knowledge = 0
                                $ at = 0
                                jump foggylakeforagersintroduction03
                            '“I’m not knowledgable enough to claim Wright’s truth. I’ll leave it to others.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not knowledgable enough to claim Wright’s truth. I’ll leave it to others.”')
                                $ custom2 = "He takes a long pause, then gives you a cheerful glance, with a smile hidden in his beard. “You can judge your talents, and I envy you... But keep your soul open. The Wright’s call can turn us into eternal tools, making us bend the realms to their will.” He reaches for another trap, his gestures are quicker and more confident.\n\nThe other men look at each other until {color=#f6d6bd}Ilan{/color} shrugs and nods toward you."
                                $ foragers_caius_friendship += 1
                                $ at_unlock_knowledge = 0
                                $ at = 0
                                jump foggylakeforagersintroduction03
                            '“I guess we disagree.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I guess we disagree.”')
                                $ foragers_friendship += 1
                                $ custom2 = "Taken by surprise, he lowers his head. “You ain’t ready for the path of thorns and claws.” He reaches for another trap, though his gestures are even slower than before. After a short pause, {color=#f6d6bd}Ilan{/color} smiles."
                                $ at_unlock_knowledge = 0
                                $ at = 0
                                jump foggylakeforagersintroduction03
                '“It’s just a trinket.”':
                    label foggylakeforagersintroduction01caiusargument01:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s just a trinket.”')
                        $ foragers_caius_friendship -= 1
                        $ foragers_friendship += 1
                        if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                            $ pc_faithpoints_opportunities += 1
                            $ pc_faithpoints -= 2
                        menu:
                            '“I see,” he growls, but his eyes soften. {color=#f6d6bd}Ilan{/color} puts on a cheerful smile. “Steel has a good shine to it, friend. In our home we wear bones and tusks. Gold is pretty, too, but we have none.”
                            \n\n{color=#f6d6bd}The third man{/color} still avoids your eyes, but lets out a whisper: “Coward.” The other two look toward him.
                            '
                            'I ignore him. “Maybe traders will bring you some.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ignore him. “Maybe traders will bring you some.”')
                                $ foragers_friendship += 1
                                $ custom2 = "{color=#f6d6bd}Ilan{/color} clasps his hands together and meets your eyes, turning his back on the silent man. “I hope so! The more they bring, the prettier our folks will get.”"
                                jump foggylakeforagersintroduction03
                            '“What do you mean by that?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you mean by that?”')
                                if (pc_class == "scholar" and pc_religion == "theunitedchurch") or (pc_class == "scholar" and pc_religion == "ordersoftruth") or (pc_class == "scholar" and pc_religion == "fellowship"):
                                    $ at_unlock_knowledge = 1
                                    $ at = 0
                                menu:
                                    'He puts away the trap, though still stares at it. “Once someone pushes against The Wright, the one who rules you and guides you, you can’t even stay on your feet? You throw away your salvation The Tribe of The Southern Valley did centuries ago, when they hid their hourglasses to buy ibexes from The Ice Clan.” He looks at you with widely opened eyes, consumed by zeal. “Coward!”
                                    \n\nHe has the accent of the cityfolk. Same as yours.
                                    '
                                    'I can turn this around. “The Tribe did so for a good reason. Don’t you remember? They were fighting for survival.”' ( condition="at == 'knowledge'" ):
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I can turn this around. “The Tribe did so for a good reason. Don’t you remember? They were fighting for survival.”')
                                        $ at_unlock_knowledge = 0
                                        $ at = 0
                                        menu:
                                            '“One-fifth of them died just a year later! If they had kept their trust, Wright’s mercy would have saved them all.”
                                            '
                                            '“...Or none of them. The Wright saves those they choose, our prayers mean little.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Or none of them. The Wright saves who they choose, not who we want them to save.”')
                                                menu:
                                                    'He shakes his head, his beard is like a sweeping broom. “They’d tainted their souls, lost their purpose. They dies for a reason, like all of us.”
                                                    '
                                                    '“You don’t know Wright’s Tablets. It is written: {i}There was great sadness among The Wright and their tribes, for Zev had burnt before his time.{/i}”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t know Wright’s Tablets. It is written: {i}There was great sadness among The Wright and their tribes, for Zev had burnt before his time.{/i}”')
                                                        $ foragers_caius_debate = 1
                                                        $ foragers_caius_friendship += 3
                                                        $ pc_faithpoints += 3
                                                        $ custom2 = "“How dare you...” He raises his arms and shakes his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“I may not know them as much as I should. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                        jump foggylakeforagersintroduction03
                                                    '“If you were truly thinking that, you would not hide behind the walls. Instead, you’d let The Wright decide when to take you away.”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you were truly thinking that, you would not hide behind the walls. Instead, you’d let The Wright decide when to take you away.”')
                                                        $ foragers_caius_debate = 1
                                                        $ foragers_caius_friendship += 3
                                                        $ pc_faithpoints += 3
                                                        $ custom2 = "He freezes, giving you a puzzled look. He raises his arms, shaking his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“I may sometimes get lost. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                        jump foggylakeforagersintroduction03
                                                    '“You tread on dangerous ground. Or would you say the same to parents of ill children?”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You tread on dangerous ground. Or would you say the same to parents of ill children?”')
                                                        $ foragers_caius_debate = 1
                                                        $ foragers_caius_friendship += 3
                                                        $ pc_faithpoints += 3
                                                        $ custom2 = "He freezes with a terrified grimace. His eyes mist over at your harsh look. He then raises his arms, shaking his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, some souls ought not to hear my words. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                        jump foggylakeforagersintroduction03
                                            '“Wright’s Tablets don’t mention it was a punishment of any sort. It’s more likely they were lucky to even get that far, considering their situation.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Wright’s Tablets don’t mention it was a punishment of any sort. It’s more likely they were lucky to even get that far, considering their situation.”')
                                                menu:
                                                    'He raises his chin. “Their {i}situation{/i} was their own doing. They were weak in faith, and they were seeking help among the pagan tribes. If it had not been for their broken paths and betrayals, they would have not been pushed into such a fate.”
                                                    '
                                                    'I look at him in disbelief. “It was the Tribe of The {i}Western{/i} Valley that’s been punished for their wrongdoings. It’s a completely different story, about the human blood given away to beastfolk.”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at him in disbelief. “It was the Tribe of The {i}Western{/i} Valley that was punished for their wrongdoings. It’s a completely different story, about feeding the beastfolk with human blood.”')
                                                        $ foragers_caius_debate = 1
                                                        $ foragers_caius_friendship += 3
                                                        $ pc_faithpoints += 3
                                                        $ custom2 = "“How dare you...” He raises his arms and shakes his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, I may not know The Tablets as much as I should. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                        jump foggylakeforagersintroduction03
                                                    '“That’s not what’s said in Wright’s Tablets. Their story starts with the description of the long winter, and the fire that took away their supplies. They made mistakes, but none of them were grave.”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s not what’s said in Wright’s Tablets. Their story starts with the description of the long winter, and the fire that took away their supplies. They made mistakes, but none of them were grave.”')
                                                        $ foragers_caius_debate = 1
                                                        $ foragers_caius_friendship += 3
                                                        $ pc_faithpoints += 3
                                                        $ custom2 = "He frowns in disbelief and mentions a few of their sins, but you remind him that they all occurred {i}after{/i} the events you’re discussing. He finally raises his arms, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, I may not know The Tablets as much as I should. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                        jump foggylakeforagersintroduction03
                                                    '“You attribute to them misdeeds based on their struggles, but it’s just as likely their land was simply harsh. None of us deserves every bad thing that happens, nor every good thing. Think of emperor Adir’s childhood.”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You attribute to them misdeeds based on their struggles, but it’s just as likely their land was simply harsh. None of us deserves every bad thing that happens, nor every good thing. Think of emperor Adir’s childhood.”')
                                                        $ foragers_caius_debate = 1
                                                        $ foragers_caius_friendship += 3
                                                        $ pc_faithpoints += 3
                                                        $ custom2 = "He freezes with a terrified grimace. His eyes mist over at your harsh look. He then raises his arms, shaking his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, I may be lost in my thoughts. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                            '“You know that’s impossible. The Wright promised they would never use the wrath of the herds against us.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know that’s impossible. The Wright promised they would never use the wrath of the herds against us.”')
                                                menu:
                                                    'He shudders, but then takes the stance of a preacher. “The Wright may not have ordered the beasts to charge at them, but they didn’t defend them either! Their hand was just, and knew that nothing good may come of that tribe!”
                                                    '
                                                    '“You contradict the lessons of many tales. All sorts of heroes and leaders used to be good-for-nothings until Wright’s calling inspired them to change their paths. It wasn’t a reward, it was an encouragement.”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You contradict the lessons of many tales. All sorts of heroes and leaders used to be good-for-nothings until Wright’s calling inspired them to change their paths. It wasn’t a reward, it was an encouragement.”')
                                                        $ foragers_caius_debate = 1
                                                        $ foragers_caius_friendship += 3
                                                        $ pc_faithpoints += 3
                                                        $ custom2 = "He freezes with a terrified grimace. His eyes mist over at your harsh look. He then raises his arms, shaking his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, I may be lost in my thoughts. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                    '“Don’t you remember the story of Hila? She was a part of their tribe, yet brought a lot of good to thousands of souls. And it happened {i}while{/i} they were struggling, not after that.”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you remember the story of Hila? She was a part of their tribe, yet brought a lot of good to thousands of souls. And it happened {i}while{/i} they were struggling, not after that.”')
                                                        $ foragers_caius_debate = 1
                                                        $ foragers_caius_friendship += 3
                                                        $ pc_faithpoints += 3
                                                        $ custom2 = "With a puzzled frown he looks at his companions, but they spare him nothing more than a shrug. You explain that Hila was a heroine who got rid of the unicorns in The Growing Mountains, and the man’s eyes widen. He raises his arms and shakes his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, my knowledge of The Tablets is not as deep as it should be. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                        jump foggylakeforagersintroduction03
                                                    '“And what else, should The Wright throw the entire tribe into a snake pit and say {i}it wasn’t me, the snakes did it{/i}? You make them look like a petty brat, or a coward who can’t follow their own rules.”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And what else, should The Wright throw the entire tribe into a snake pit and say {i}it wasn’t me, the snakes did it{/i}? You make them look like a petty brat, or a coward who can’t follow their own rules.”')
                                                        $ foragers_caius_debate = 1
                                                        $ foragers_caius_friendship += 3
                                                        $ pc_faithpoints += 3
                                                        $ custom2 = "“How dare you...” He raises his arms and shakes his fist, but once he notices his stump, he hides it in the palm of his hand. He looks at the ground.\n\n“True, I may be injust in my words. But I {i}do{/i} know that The Wright punishes the weak, the arrogant, the crooked.” As the leaves rustle, you barely recognize his words. “I do apologize, traveler. I’m too eager to judge.” He takes a step back and sits down by the palisade, without even looking at the traps.\n\nAfter a few heartbeats, {color=#f6d6bd}Ilan{/color} breaks the awkward pause. His amused voice scares away a bird."
                                                        jump foggylakeforagersintroduction03
                                    '“It’s just a necklace, you lunatic.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s just a necklace, you lunatic.”')
                                        $ foragers_caius_friendship -= 1
                                        if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                                            $ pc_faithpoints -= 1
                                        $ custom2 = "The trap falls on the ground. He reaches for it with a shaking hand. “If that’s what you think, you stain your own soul by wearing what doesn’t belong to you. One day you’ll pay for it, as {i}all{/i} evildoers do.”\n\nAfter an awkward pause, {color=#f6d6bd}Ilan{/color} puts on an awkward smile."
                                        $ at_unlock_knowledge = 0
                                        $ at = 0
                                        jump foggylakeforagersintroduction03
                                    '“You know nothing about me. Save your judgments for those who seek it.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know nothing about me. Save your judgments for those who seek it.”')
                                        $ foragers_caius_friendship -= 1
                                        $ custom2 = "He turns away. He reaches for another trap, but his gestures are even slower than before. After a short pause, {color=#f6d6bd}Ilan{/color} nods toward you."
                                        $ at_unlock_knowledge = 0
                                        $ at = 0
                                        jump foggylakeforagersintroduction03
                                    'I repentantly bow my head.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I repentantly bow my head.')
                                        $ custom2 = "An awkward pause goes on. “Pray for bravery,” he finally says. “We all need more of it.”\n\nAfter you raise your head, you meet {color=#f6d6bd}Ilan’s{/color} amused look."
                                        $ at_unlock_knowledge = 0
                                        $ at = 0
                                        jump foggylakeforagersintroduction03
                            '“Nothing cowardly in speaking the truth.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Nothing cowardly in speaking the truth.”')
                                if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                                    $ pc_faithpoints -= 1
                                $ custom2 = "He turns away and reaches for another trap, with shoulders even more slumped than before. {color=#f6d6bd}Ilan{/color} sighs."
                                jump foggylakeforagersintroduction03
        else:
            $ custom2 = "{color=#f6d6bd}Ilan{/color} smiles."
            jump foggylakeforagersintroduction03

    label foggylakeforagersintroduction03:
        menu:
            '[custom2] “Were you at {color=#f6d6bd}Pelt of the North{/color} yet, friend?” He blushes. “How is {color=#f6d6bd}Dalit{/color} doing?”
            '
            '“I haven’t been there yet.”' if not peltnorth_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I haven’t been there yet.”')
                $ questionpreset = "foragers1"
                $ dalit_name = "Dalit"
                $ description_iason07 = "According to {color=#f6d6bd}Ilan{/color}, he was in need of hard drinks and healing potions."
                $ description_dalit03 = "According to {color=#f6d6bd}Ilan{/color}, she’s a playful girl who always looks for entertainment."
                $ description_dalit04 = "According to {color=#f6d6bd}Ilan{/color}, she loves to tell stories about the monsters she’s faced."
                menu:
                    '“Ah, bummer! It’s on the southern road. They’re kind to travelers, these hunters, wanted to buy hard drinks and healing potions from us. The innkeep is their boss, but just wait before you meet {color=#f6d6bd}Dalit{/color}! She played dice with us for a good hour, and knows all sorts of tales about monsters, and her smile... Must be really bored, that one!” His smile turns into a grin. “Better say {i}hi{/i} to her for us!”
                    \n\n{color=#f6d6bd}Tzvi{/color} adjusts his black cloak. “Our traps won’t fix themselves. Hwat brings you to us?” {color=#f6d6bd}Ilan{/color} frowns at this interruption, but says nothing.
                    '
                    '(preset foragers1)':
                        pass
            '(lie) “I haven’t been there yet.”' if peltnorth_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I haven’t been there yet.”')
                $ questionpreset = "foragers1"
                $ pc_lies += 1
                $ dalit_name = "Dalit"
                $ description_iason07 = "According to {color=#f6d6bd}Ilan{/color}, he was in need of hard drinks and healing potions."
                $ description_dalit03 = "According to {color=#f6d6bd}Ilan{/color}, she’s a playful girl who always looks for entertainment."
                $ description_dalit04 = "According to {color=#f6d6bd}Ilan{/color}, she loves to tell stories about the monsters she’s faced."
                menu:
                    '“Ah, bummer! It’s on the southern road. They’re kind to travelers, these hunters, wanted to buy hard drinks and healing potions from us. The innkeep is their boss, but just wait before you meet {color=#f6d6bd}Dalit{/color}! She played dice with us for a good hour, and knows all sorts of tales about monsters, and her smile... Must be really bored, that one!” His smile turns into a grin. “Better say {i}hi{/i} to her for us!”
                    \n\n{color=#f6d6bd}Tzvi{/color} adjusts his black cloak. “Our traps won’t fix themselves. Hwat brings you to us?” {color=#f6d6bd}Ilan{/color} frowns at this interruption, but says nothing.
                    '
                    '(preset foragers1)':
                        pass
            '(lie) “She’s fine. Just doing her thing, you know.”' if not dalit_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “She’s fine. Just doing her thing, you know.”')
                $ questionpreset = "foragers1"
                $ pc_lies += 1
                $ foragers_friendship += 1
                $ description_iason07 = "According to {color=#f6d6bd}Ilan{/color}, he was in need of hard drinks and healing potions."
                menu:
                    'Seeing you don’t plan to carry on, he gives you an awkward smile. “I bet! She’s always so bored, that one!” His smile turns into a grin. “Better say {i}hi{/i} to her for us! Her boss was looking for hard drinks and healing potions, I wish I could have helped her.” He glances at his companion, who’s currently observing a column of ants running alongside the palisade. “They were offering good prices! And she was really good at dice...”
                    \n\n{color=#f6d6bd}Tzvi{/color} adjusts his black cloak. “Our traps won’t fix themselves. Hwat brings you to us?” {color=#f6d6bd}Ilan{/color} frowns at this interruption, but says nothing.
                    '
                    '(preset foragers1)':
                        pass
            '“She’s well. Seems to keep the whole crew together.”' if dalit_firsttime and dalit_name == "Dalit":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She’s well. Seems to keep the whole crew together.”')
                $ questionpreset = "foragers1"
                $ foragers_friendship += 2
                $ description_iason07 = "According to {color=#f6d6bd}Ilan{/color}, he was in need of hard drinks and healing potions."
                $ description_dalit04 = "According to {color=#f6d6bd}Ilan{/color}, she loves to tell stories about the monsters she’s faced."
                menu:
                    'His voice gets drowsy. “Her soul is young, but {i}everyone{/i} listens when she speaks. She’s always so bored, that one!” His smile turns into a grin. “Better say {i}hi{/i} to her for us! Her boss was looking for hard drinks and healing potions, I wish I could have helped her.” He glances at his companion, who’s currently observing a column of ants running alongside the palisade. “They were offering good prices! And she was really good at dice, and told us about so many monsters...”
                    \n\n{color=#f6d6bd}Tzvi{/color} adjusts his black cloak. “Our traps won’t fix themselves. Hwat brings you to us?” {color=#f6d6bd}Ilan{/color} frowns at this interruption, but says nothing.
                    '
                    '(preset foragers1)':
                        pass
            '“Is that the one with yellow armor? She’s well. Seems to keep the whole crew together.”' if dalit_firsttime and dalit_name != "Dalit":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is that the one with a yellow armor? She’s well. Seems to keep the whole crew together.”')
                $ dalit_name = "Dalit"
                $ questionpreset = "foragers1"
                $ foragers_friendship +=2
                $ description_iason07 = "According to {color=#f6d6bd}Ilan{/color}, he was in need of hard drinks and healing potions."
                $ description_dalit04 = "According to {color=#f6d6bd}Ilan{/color}, she loves to tell stories about the monsters she’s faced."
                menu:
                    '“That’s her! A lively color, aye? Yellow?” He smiles, but you catch a hint of envy in his voice. “Better say {i}hi{/i} to her for us! Her boss was looking for hard drinks and healing potions, I wish I could have helped her.” He glances at his companion, who’s currently observing a column of ants running alongside the palisade. “They were offering good prices! And she was really good at dice, and told us about so many monsters...”
                    \n\n{color=#f6d6bd}Tzvi{/color} adjusts his black cloak. “Our traps won’t fix themselves. Hwat brings you to us?” {color=#f6d6bd}Ilan{/color} frowns at this interruption, but says nothing.
                    '
                    '(preset foragers1)':
                        pass
            '“I didn’t speak with the hunters all that much.”' if peltnorth_firsttime and not dalit_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t speak with the hunters all that much.”')
                $ questionpreset = "foragers1"
                $ dalit_name = "Dalit"
                $ description_dalit03 = "According to {color=#f6d6bd}Ilan{/color}, she’s a playful girl who always looks for entertainment."
                $ description_dalit04 = "According to {color=#f6d6bd}Ilan{/color}, she loves to tell stories about the monsters she’s faced."
                menu:
                    '“Ah, bummer! You missed on a {i}great{/i} company. They’re kind to travelers, these hunters, wanted to buy hard drinks and healing potions from us. The innkeep is their boss, but just wait before you meet {color=#f6d6bd}Dalit{/color}! She played dice with us for a good hour, and knows all sorts of tales about monsters, and her smile... Must be really bored, that one!” His smile turns into a grin. “Better say {i}hi{/i} to her for us!”
                    \n\n{color=#f6d6bd}Tzvi{/color} adjusts his black cloak. “Our traps won’t fix themselves. Hwat brings you to us?” {color=#f6d6bd}Ilan{/color} frowns at this interruption, but says nothing.
                    '
                    '(preset foragers1)':
                        pass

label foggylakereforagersafterinteraction01:
    $ questionpreset = "foragers1"
    menu:
        '“Let us know if we can be of help, aye?”
        '
        '(preset foragers1)':
            pass

label foggylakeforagersregularquestionsaboutworkALL:
    label foggylakeforagersregularquestionsaboutwork01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your plan? I could use some work.”')
        $ foragers_quest = 1
        if day > foragingground_quest_timer or foragingground_bird_gone:
            $ foragingground_bird_gone = 1
            $ questionpreset = "foragers1"
            menu:
                '“Nah, we have none.” {color=#f6d6bd}Tzvi{/color} shrugs.
                \n\n“You’re a bit late, friend,” adds {color=#f6d6bd}Ilan{/color}. “We were hoping to catch that large bird, one that used to roam in the valley south of here, but it’s gone, looks like. No more hunting for us.”
                '
                '(preset foragers1)':
                    pass
        elif day >= foragers_quest_daythreshold:
            if day+1 == foragingground_quest_timer:
                $ foragingground_quest_timer = (foragingground_quest_timer+2)
            menu:
                '{color=#f6d6bd}Tzvi{/color} nods, {color=#f6d6bd}Ilan’s{/color} voice gets even louder. “Glad to hear that! There’s hardly any fruits left around here, and even fewer mushrooms, so we’re planning to do some bird catching, and soon! A hunt without killing. Hwat do you say?”
                '
                '“Why would you need my help with birds? Don’t you just let them walk into traps?”' if not foragers_quest_question01:
                    jump foggylakeforagersregularquestionsaboutwork01questions01
                '“How much do you pay?”' if not foragers_quest_question07:
                    jump foggylakeforagersregularquestionsaboutwork01questions07
                '“I can’t leave my horse behind.”' if not foragers_quest_question08:
                    jump foggylakeforagersregularquestionsaboutwork01questions08
                '“What’s your plan, exactly?”' if foragers_quest_question01 and not foragers_quest_question02:
                    jump foggylakeforagersregularquestionsaboutwork01questions02
                '“I feel like I could use better equipment.”' if foragers_quest_question02 and not foragers_quest_question03:
                    jump foggylakeforagersregularquestionsaboutwork01questions03
                '“This all sounds {i}really{/i} dangerous.”' if foragers_quest_question02 and not foragers_quest_question09:
                    jump foggylakeforagersregularquestionsaboutwork01questions09
                '“You’re putting me in front of a large beast for just five dragons? That’s bullshit.”' if foragers_quest_question09 and foragers_quest_question07 and not foragers_quest_question05:
                    jump foggylakeforagersregularquestionsaboutwork01questions05
                '“What are you going to do with your catch?”' if foragers_quest_question01 and not foragers_quest_question06:
                    jump foggylakeforagersregularquestionsaboutwork01questions06
                '“Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”' if foragers_quest_question06 and not foragers_quest_question10 and not creeks_reasonstojoin_creeksaboutlackingmeat:
                    jump foggylakeforagersregularquestionsaboutwork01questions10
                '“Fine. I’ll tell you once I’m ready to go.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day >= foragers_quest_daythreshold:
                    jump foggylakeforagersregularquestionsaboutwork01all
                '“Fine. I’ll be back in [custom6] days, or soon after that.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day < foragers_quest_daythreshold:
                    jump foggylakeforagersregularquestionsaboutwork01allalt
        else:
            $ quest_birdhunting_description01 = 1
            $ custom6 = (foragers_quest_daythreshold-day)
            menu:
                '{color=#f6d6bd}Tzvi{/color} nods, and {color=#f6d6bd}Ilan’s{/color} voice gets even louder. “Glad to hear that! There’s hardly any fruits left around here, and even fewer mushrooms, so we’re planning to do some bird catching, a hunt without killing. Maybe not today, but in [custom6] days, maybe a bit later. Hwat do you say?”
                '
                '“Why would you need my help with birds? Don’t you just let them walk into traps?”' if not foragers_quest_question01:
                    jump foggylakeforagersregularquestionsaboutwork01questions01
                '“How much do you pay?”' if not foragers_quest_question07:
                    jump foggylakeforagersregularquestionsaboutwork01questions07
                '“I can’t leave my horse behind.”' if not foragers_quest_question08:
                    jump foggylakeforagersregularquestionsaboutwork01questions08
                '“What’s your plan, exactly?”' if foragers_quest_question01 and not foragers_quest_question02:
                    jump foggylakeforagersregularquestionsaboutwork01questions02
                '“I feel like I could use better equipment.”' if foragers_quest_question02 and not foragers_quest_question03:
                    jump foggylakeforagersregularquestionsaboutwork01questions03
                '“This all sounds {i}really{/i} dangerous.”' if foragers_quest_question02 and not foragers_quest_question09:
                    jump foggylakeforagersregularquestionsaboutwork01questions09
                '“You’re putting me in front of a large beast for just five dragons? That’s bullshit.”' if foragers_quest_question09 and foragers_quest_question07 and not foragers_quest_question05:
                    jump foggylakeforagersregularquestionsaboutwork01questions05
                '“What are you going to do with your catch?”' if foragers_quest_question01 and not foragers_quest_question06:
                    jump foggylakeforagersregularquestionsaboutwork01questions06
                '“Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”' if foragers_quest_question06 and not foragers_quest_question10 and not creeks_reasonstojoin_creeksaboutlackingmeat:
                    jump foggylakeforagersregularquestionsaboutwork01questions10
                '“Fine. I’ll tell you once I’m ready to go.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day >= foragers_quest_daythreshold:
                    jump foggylakeforagersregularquestionsaboutwork01all
                '“Fine. I’ll be back in [custom6] days, or soon after that.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day < foragers_quest_daythreshold:
                    jump foggylakeforagersregularquestionsaboutwork01allalt

    label foggylakeforagersregularquestionsaboutwork01questions01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why would you need my help with birds? Don’t you just let them walk into traps?”')
        $ foragers_quest_question01 = 1
        if not foragers_caius_voice:
            $ foragers_caius_voice = 1
            $ custom1 = " He has the accent of the cityfolk. Same as yours."
        else:
            $ custom1 = ""
        menu:
            '{color=#f6d6bd}Ilan{/color} glances at the cords used for snares. “These won’t do. We want to catch a runner, this big,” he raises his muscular arm and stops it maybe a foot above his head. “And bring it here, alive. We want its meat for later.”
            \n\n{color=#f6d6bd}The man with one hand{/color} interrupts him. His voice is weak, but disdainful. “Beasts ought to be dealt with, not tamed. Bonding with monsters brings only death.” [custom1]
            \n\n“Will bring us full bellies in winter,” squawks {color=#f6d6bd}Tzvi{/color}.
            '
            '“Why would you need my help with birds? Don’t you just let them walk into traps?”' if not foragers_quest_question01:
                jump foggylakeforagersregularquestionsaboutwork01questions01
            '“How much do you pay?”' if not foragers_quest_question07:
                jump foggylakeforagersregularquestionsaboutwork01questions07
            '“I can’t leave my horse behind.”' if not foragers_quest_question08:
                jump foggylakeforagersregularquestionsaboutwork01questions08
            '“What’s your plan, exactly?”' if foragers_quest_question01 and not foragers_quest_question02:
                jump foggylakeforagersregularquestionsaboutwork01questions02
            '“I feel like I could use better equipment.”' if foragers_quest_question02 and not foragers_quest_question03:
                jump foggylakeforagersregularquestionsaboutwork01questions03
            '“This all sounds {i}really{/i} dangerous.”' if foragers_quest_question02 and not foragers_quest_question09:
                jump foggylakeforagersregularquestionsaboutwork01questions09
            '“You’re putting me in front of a large beast for just five dragons? That’s bullshit.”' if foragers_quest_question09 and foragers_quest_question07 and not foragers_quest_question05:
                jump foggylakeforagersregularquestionsaboutwork01questions05
            '“What are you going to do with your catch?”' if foragers_quest_question01 and not foragers_quest_question06:
                jump foggylakeforagersregularquestionsaboutwork01questions06
            '“Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”' if foragers_quest_question06 and not foragers_quest_question10 and not creeks_reasonstojoin_creeksaboutlackingmeat:
                jump foggylakeforagersregularquestionsaboutwork01questions10
            '“Fine. I’ll tell you once I’m ready to go.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day >= foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01all
            '“Fine. I’ll be back in [custom6] days, or soon after that.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day < foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01allalt

    label foggylakeforagersregularquestionsaboutwork01questions02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your plan, exactly?”')
        $ foragers_quest_question02 = 1
        menu:
            '{color=#f6d6bd}Ilan{/color} grabs a rope and shakes it in front of you. “We’ll catch its neck. Your part would be to keep it from running. Don’t hurt it, just make it busy enough for us to surround it.”
            '
            '“Why would you need my help with birds? Don’t you just let them walk into traps?”' if not foragers_quest_question01:
                jump foggylakeforagersregularquestionsaboutwork01questions01
            '“How much do you pay?”' if not foragers_quest_question07:
                jump foggylakeforagersregularquestionsaboutwork01questions07
            '“I can’t leave my horse behind.”' if not foragers_quest_question08:
                jump foggylakeforagersregularquestionsaboutwork01questions08
            '“What’s your plan, exactly?”' if foragers_quest_question01 and not foragers_quest_question02:
                jump foggylakeforagersregularquestionsaboutwork01questions02
            '“I feel like I could use better equipment.”' if foragers_quest_question02 and not foragers_quest_question03:
                jump foggylakeforagersregularquestionsaboutwork01questions03
            '“This all sounds {i}really{/i} dangerous.”' if foragers_quest_question02 and not foragers_quest_question09:
                jump foggylakeforagersregularquestionsaboutwork01questions09
            '“You’re putting me in front of a large beast for just five dragons? That’s bullshit.”' if foragers_quest_question09 and foragers_quest_question07 and not foragers_quest_question05:
                jump foggylakeforagersregularquestionsaboutwork01questions05
            '“What are you going to do with your catch?”' if foragers_quest_question01 and not foragers_quest_question06:
                jump foggylakeforagersregularquestionsaboutwork01questions06
            '“Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”' if foragers_quest_question06 and not foragers_quest_question10 and not creeks_reasonstojoin_creeksaboutlackingmeat:
                jump foggylakeforagersregularquestionsaboutwork01questions10
            '“Fine. I’ll tell you once I’m ready to go.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day >= foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01all
            '“Fine. I’ll be back in [custom6] days, or soon after that.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day < foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01allalt

    label foggylakeforagersregularquestionsaboutwork01questions03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I feel like I could use better equipment.”')
        $ foragers_quest_question03 = 1
        $ description_akakios05 = "According to {color=#f6d6bd}Ilan{/color}, he’s “all ‘bout trade, not much for idle talk.”"
        menu:
            '“Well, you shouldn’t {i}need{/i} weapons for it, friend, but you may look for something worthhwile in {color=#f6d6bd}Howler’s Dell{/color}.” {color=#f6d6bd}Ilan{/color} points west. “{color=#f6d6bd}Akakios{/color} is all ‘bout trade, not much for idle talk, but he sells things for all his folks.”
            '
            '“Why would you need my help with birds? Don’t you just let them walk into traps?”' if not foragers_quest_question01:
                jump foggylakeforagersregularquestionsaboutwork01questions01
            '“How much do you pay?”' if not foragers_quest_question07:
                jump foggylakeforagersregularquestionsaboutwork01questions07
            '“I can’t leave my horse behind.”' if not foragers_quest_question08:
                jump foggylakeforagersregularquestionsaboutwork01questions08
            '“What’s your plan, exactly?”' if foragers_quest_question01 and not foragers_quest_question02:
                jump foggylakeforagersregularquestionsaboutwork01questions02
            '“I feel like I could use better equipment.”' if foragers_quest_question02 and not foragers_quest_question03:
                jump foggylakeforagersregularquestionsaboutwork01questions03
            '“This all sounds {i}really{/i} dangerous.”' if foragers_quest_question02 and not foragers_quest_question09:
                jump foggylakeforagersregularquestionsaboutwork01questions09
            '“You’re putting me in front of a large beast for just five dragons? That’s bullshit.”' if foragers_quest_question09 and foragers_quest_question07 and not foragers_quest_question05:
                jump foggylakeforagersregularquestionsaboutwork01questions05
            '“What are you going to do with your catch?”' if foragers_quest_question01 and not foragers_quest_question06:
                jump foggylakeforagersregularquestionsaboutwork01questions06
            '“Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”' if foragers_quest_question06 and not foragers_quest_question10 and not creeks_reasonstojoin_creeksaboutlackingmeat:
                jump foggylakeforagersregularquestionsaboutwork01questions10
            '“Fine. I’ll tell you once I’m ready to go.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day >= foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01all
            '“Fine. I’ll be back in [custom6] days, or soon after that.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day < foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01allalt

    label foggylakeforagersregularquestionsaboutwork01questions05:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re putting me in front of a large beast for just five dragons? That’s bullshit.”')
        $ foragers_quest_question05 = 1
        $ foragers_quest_reward = 1
        menu:
            'You haggle for a bit. While {color=#f6d6bd}Ilan{/color} gets easily convinced, it’s {color=#f6d6bd}Tzvi{/color} who cuts your conversation short. Even if his voice is croaky, it’s also firm. “You’ll get eight. Ask for more and we’ll do better buying food in {color=#f6d6bd}Howler’s{/color}.”
            '
            '“Why would you need my help with birds? Don’t you just let them walk into traps?”' if not foragers_quest_question01:
                jump foggylakeforagersregularquestionsaboutwork01questions01
            '“How much do you pay?”' if not foragers_quest_question07:
                jump foggylakeforagersregularquestionsaboutwork01questions07
            '“I can’t leave my horse behind.”' if not foragers_quest_question08:
                jump foggylakeforagersregularquestionsaboutwork01questions08
            '“What’s your plan, exactly?”' if foragers_quest_question01 and not foragers_quest_question02:
                jump foggylakeforagersregularquestionsaboutwork01questions02
            '“I feel like I could use better equipment.”' if foragers_quest_question02 and not foragers_quest_question03:
                jump foggylakeforagersregularquestionsaboutwork01questions03
            '“This all sounds {i}really{/i} dangerous.”' if foragers_quest_question02 and not foragers_quest_question09:
                jump foggylakeforagersregularquestionsaboutwork01questions09
            '“You’re putting me in front of a large beast for just five dragons? That’s bullshit.”' if foragers_quest_question09 and foragers_quest_question07 and not foragers_quest_question05:
                jump foggylakeforagersregularquestionsaboutwork01questions05
            '“What are you going to do with your catch?”' if foragers_quest_question01 and not foragers_quest_question06:
                jump foggylakeforagersregularquestionsaboutwork01questions06
            '“Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”' if foragers_quest_question06 and not foragers_quest_question10 and not creeks_reasonstojoin_creeksaboutlackingmeat:
                jump foggylakeforagersregularquestionsaboutwork01questions10
            '“Fine. I’ll tell you once I’m ready to go.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day >= foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01all
            '“Fine. I’ll be back in [custom6] days, or soon after that.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day < foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01allalt

    label foggylakeforagersregularquestionsaboutwork01questions06:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What are you going to do with the bird once we catch it?”')
        $ foragers_quest_question06 = 1
        menu:
            '“We’ll tether it to the palisade for a day or two, then take it to {color=#f6d6bd}Creeks{/color}. Our tribesfolk have enough space to look after it through autumn. Maybe it’ll drop a few eggs? Even if not, it’s fresh food.”
            '
            '“Why would you need my help with birds? Don’t you just let them walk into traps?”' if not foragers_quest_question01:
                jump foggylakeforagersregularquestionsaboutwork01questions01
            '“How much do you pay?”' if not foragers_quest_question07:
                jump foggylakeforagersregularquestionsaboutwork01questions07
            '“I can’t leave my horse behind.”' if not foragers_quest_question08:
                jump foggylakeforagersregularquestionsaboutwork01questions08
            '“What’s your plan, exactly?”' if foragers_quest_question01 and not foragers_quest_question02:
                jump foggylakeforagersregularquestionsaboutwork01questions02
            '“I feel like I could use better equipment.”' if foragers_quest_question02 and not foragers_quest_question03:
                jump foggylakeforagersregularquestionsaboutwork01questions03
            '“This all sounds {i}really{/i} dangerous.”' if foragers_quest_question02 and not foragers_quest_question09:
                jump foggylakeforagersregularquestionsaboutwork01questions09
            '“You’re putting me in front of a large beast for just five dragons? That’s bullshit.”' if foragers_quest_question09 and foragers_quest_question07 and not foragers_quest_question05:
                jump foggylakeforagersregularquestionsaboutwork01questions05
            '“What are you going to do with your catch?”' if foragers_quest_question01 and not foragers_quest_question06:
                jump foggylakeforagersregularquestionsaboutwork01questions06
            '“Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”' if foragers_quest_question06 and not foragers_quest_question10 and not creeks_reasonstojoin_creeksaboutlackingmeat:
                jump foggylakeforagersregularquestionsaboutwork01questions10
            '“Fine. I’ll tell you once I’m ready to go.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day >= foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01all
            '“Fine. I’ll be back in [custom6] days, or soon after that.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day < foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01allalt

    label foggylakeforagersregularquestionsaboutwork01questions07:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How much do you pay?”')
        $ foragers_quest_question07 = 1
        menu:
            '“I mean, it may be a scary trip, but it won’t take that long.” {color=#f6d6bd}Ilan{/color} shrugs. “Just show up here at noon or before it, we’ll be back in a few hours. You’ll get five dragons, two if the bird dies. That’s a good price for one afternoon, aye?”
            '
            '“Why would you need my help with birds? Don’t you just let them walk into traps?”' if not foragers_quest_question01:
                jump foggylakeforagersregularquestionsaboutwork01questions01
            '“How much do you pay?”' if not foragers_quest_question07:
                jump foggylakeforagersregularquestionsaboutwork01questions07
            '“I can’t leave my horse behind.”' if not foragers_quest_question08:
                jump foggylakeforagersregularquestionsaboutwork01questions08
            '“What’s your plan, exactly?”' if foragers_quest_question01 and not foragers_quest_question02:
                jump foggylakeforagersregularquestionsaboutwork01questions02
            '“I feel like I could use better equipment.”' if foragers_quest_question02 and not foragers_quest_question03:
                jump foggylakeforagersregularquestionsaboutwork01questions03
            '“This all sounds {i}really{/i} dangerous.”' if foragers_quest_question02 and not foragers_quest_question09:
                jump foggylakeforagersregularquestionsaboutwork01questions09
            '“You’re putting me in front of a large beast for just five dragons? That’s bullshit.”' if foragers_quest_question09 and foragers_quest_question07 and not foragers_quest_question05:
                jump foggylakeforagersregularquestionsaboutwork01questions05
            '“What are you going to do with your catch?”' if foragers_quest_question01 and not foragers_quest_question06:
                jump foggylakeforagersregularquestionsaboutwork01questions06
            '“Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”' if foragers_quest_question06 and not foragers_quest_question10 and not creeks_reasonstojoin_creeksaboutlackingmeat:
                jump foggylakeforagersregularquestionsaboutwork01questions10
            '“Fine. I’ll tell you once I’m ready to go.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day >= foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01all
            '“Fine. I’ll be back in [custom6] days, or soon after that.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day < foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01allalt

    label foggylakeforagersregularquestionsaboutwork01questions08:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t leave my horse behind.”')
        $ foragers_quest_question08 = 1
        menu:
            '“Oh, I wouldn’t worry ‘bout it,” {color=#f6d6bd}Ilan{/color} waves a hand, just like his mother. “The idiot will take care of it.”
            \n\n{color=#f6d6bd}The one-handed man{/color} starts to object, but a harsh “shut up” from {color=#f6d6bd}Tzvi{/color} makes him sigh. His shoulders sag. {color=#f6d6bd}Ilan{/color} goes on: “He’s a loony, and would stumble over his own feet on a trip, but does hwat he needs when told to. And you know he won’t steal it, he {i}hates{/i} animals.”
            '
            '“Why would you need my help with birds? Don’t you just let them walk into traps?”' if not foragers_quest_question01:
                jump foggylakeforagersregularquestionsaboutwork01questions01
            '“How much do you pay?”' if not foragers_quest_question07:
                jump foggylakeforagersregularquestionsaboutwork01questions07
            '“I can’t leave my horse behind.”' if not foragers_quest_question08:
                jump foggylakeforagersregularquestionsaboutwork01questions08
            '“What’s your plan, exactly?”' if foragers_quest_question01 and not foragers_quest_question02:
                jump foggylakeforagersregularquestionsaboutwork01questions02
            '“I feel like I could use better equipment.”' if foragers_quest_question02 and not foragers_quest_question03:
                jump foggylakeforagersregularquestionsaboutwork01questions03
            '“This all sounds {i}really{/i} dangerous.”' if foragers_quest_question02 and not foragers_quest_question09:
                jump foggylakeforagersregularquestionsaboutwork01questions09
            '“You’re putting me in front of a large beast for just five dragons? That’s bullshit.”' if foragers_quest_question09 and foragers_quest_question07 and not foragers_quest_question05:
                jump foggylakeforagersregularquestionsaboutwork01questions05
            '“What are you going to do with your catch?”' if foragers_quest_question01 and not foragers_quest_question06:
                jump foggylakeforagersregularquestionsaboutwork01questions06
            '“Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”' if foragers_quest_question06 and not foragers_quest_question10 and not creeks_reasonstojoin_creeksaboutlackingmeat:
                jump foggylakeforagersregularquestionsaboutwork01questions10
            '“Fine. I’ll tell you once I’m ready to go.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day >= foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01all
            '“Fine. I’ll be back in [custom6] days, or soon after that.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day < foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01allalt

    label foggylakeforagersregularquestionsaboutwork01questions09:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “This all sounds {i}really{/i} dangerous.”')
        $ foragers_quest_question09 = 1
        menu:
            '“That’s hwy we want {i}you{/i} to do the rough part,” {color=#f6d6bd}Tzvi{/color} smirks. “We’re just foragers. A roadwarden knows how to fight, aye? At least it’s on its own, without its... {i}flock{/i}?”
            '
            '“Why would you need my help with birds? Don’t you just let them walk into traps?”' if not foragers_quest_question01:
                jump foggylakeforagersregularquestionsaboutwork01questions01
            '“How much do you pay?”' if not foragers_quest_question07:
                jump foggylakeforagersregularquestionsaboutwork01questions07
            '“I can’t leave my horse behind.”' if not foragers_quest_question08:
                jump foggylakeforagersregularquestionsaboutwork01questions08
            '“What’s your plan, exactly?”' if foragers_quest_question01 and not foragers_quest_question02:
                jump foggylakeforagersregularquestionsaboutwork01questions02
            '“I feel like I could use better equipment.”' if foragers_quest_question02 and not foragers_quest_question03:
                jump foggylakeforagersregularquestionsaboutwork01questions03
            '“This all sounds {i}really{/i} dangerous.”' if foragers_quest_question02 and not foragers_quest_question09:
                jump foggylakeforagersregularquestionsaboutwork01questions09
            '“You’re putting me in front of a large beast for just five dragons? That’s bullshit.”' if foragers_quest_question09 and foragers_quest_question07 and not foragers_quest_question05:
                jump foggylakeforagersregularquestionsaboutwork01questions05
            '“What are you going to do with your catch?”' if foragers_quest_question01 and not foragers_quest_question06:
                jump foggylakeforagersregularquestionsaboutwork01questions06
            '“Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”' if foragers_quest_question06 and not foragers_quest_question10 and not creeks_reasonstojoin_creeksaboutlackingmeat:
                jump foggylakeforagersregularquestionsaboutwork01questions10
            '“Fine. I’ll tell you once I’m ready to go.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day >= foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01all
            '“Fine. I’ll be back in [custom6] days, or soon after that.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day < foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01allalt

    label foggylakeforagersregularquestionsaboutwork01questions10:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”')
        $ foragers_quest_question10 = 1
        $ creeks_reasonstojoin_creeksaboutlackingmeat = 1
        menu:
            'They exchange looks. “Maybe,” admits {color=#f6d6bd}Tzvi{/color}. “But not big enough to make us pay you more.”
            '
            '“Why would you need my help with birds? Don’t you just let them walk into traps?”' if not foragers_quest_question01:
                jump foggylakeforagersregularquestionsaboutwork01questions01
            '“How much do you pay?”' if not foragers_quest_question07:
                jump foggylakeforagersregularquestionsaboutwork01questions07
            '“I can’t leave my horse behind.”' if not foragers_quest_question08:
                jump foggylakeforagersregularquestionsaboutwork01questions08
            '“What’s your plan, exactly?”' if foragers_quest_question01 and not foragers_quest_question02:
                jump foggylakeforagersregularquestionsaboutwork01questions02
            '“I feel like I could use better equipment.”' if foragers_quest_question02 and not foragers_quest_question03:
                jump foggylakeforagersregularquestionsaboutwork01questions03
            '“This all sounds {i}really{/i} dangerous.”' if foragers_quest_question02 and not foragers_quest_question09:
                jump foggylakeforagersregularquestionsaboutwork01questions09
            '“You’re putting me in front of a large beast for just five dragons? That’s bullshit.”' if foragers_quest_question09 and foragers_quest_question07 and not foragers_quest_question05:
                jump foggylakeforagersregularquestionsaboutwork01questions05
            '“What are you going to do with your catch?”' if foragers_quest_question01 and not foragers_quest_question06:
                jump foggylakeforagersregularquestionsaboutwork01questions06
            '“Is there a problem with supplies in {color=#f6d6bd}Creeks{/color}?”' if foragers_quest_question06 and not foragers_quest_question10 and not creeks_reasonstojoin_creeksaboutlackingmeat:
                jump foggylakeforagersregularquestionsaboutwork01questions10
            '“Fine. I’ll tell you once I’m ready to go.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day >= foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01all
            '“Fine. I’ll be back in [custom6] days, or soon after that.”' if foragers_quest_question01 and foragers_quest_question08 and foragers_quest_question07 and day < foragers_quest_daythreshold:
                jump foggylakeforagersregularquestionsaboutwork01allalt

    label foggylakeforagersregularquestionsaboutwork01all:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I’ll tell you once I’m ready to go.”')
        $ quest_birdhunting = 1
        $ renpy.notify("New entry: Bird Hunting")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Bird Hunting{/i}')
        $ questionpreset = "foragers1"
        menu:
            '{color=#f6d6bd}Ilan{/color} grins. “Do so! But don’t make us wait for too long, the runner may walk away any day now. Just come before afternoon.”
            '
            '(preset foragers1)':
                pass

    label foggylakeforagersregularquestionsaboutwork01allalt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I’ll be back in %s days, or soon after that.”' %custom6)
        $ quest_birdhunting = 1
        $ renpy.notify("New entry: Bird Hunting")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Bird Hunting{/i}')
        $ questionpreset = "foragers1"
        menu:
            '{color=#f6d6bd}Ilan{/color} grins. “Do so! We still need to prepare, and you better do so as well, but don’t make us wait for long, let’s not test the bird’s patience. Just come one day before afternoon.”
            '
            '(preset foragers1)':
                pass

label foggylakeforagersregularquestionsaboutwork02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have everything I need. Let’s hunt while it’s still early.”')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ foragingground_foragers_toforagingground = 1
    menu:
        '{color=#f6d6bd}Ilan{/color} clasps his hands. “Then we’re going! Idiot, take care of the horse,” he nods toward {color=#f6d6bd}the man with one hand{/color}.
        \n\n{color=#f6d6bd}Ilan{/color} puts proudly a rope and a bag on his shoulders, while {color=#f6d6bd}Tzvi{/color} shoves everything under his black cloak. They gather by the gate and mock their companion as he toddles toward the lake with an empty bucket.
        '
        'I grab whatever may be of use from my bags and leave the yard.' if not pc_likeshorsename:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab whatever may be of use from my bags and leave the yard.')
            $ travel_destination = "wanderer"
            $ quarters += 1
            jump finaldestinationafterevent
        'I grab whatever may be of use from my bags and scratch {color=#f6d6bd}[horsename]’s{/color} neck.' if pc_likeshorsename:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab whatever may be of use from my bags and scratch {color=#f6d6bd}%s’s{/color}neck.' %horsename)
            $ travel_destination = "wanderer"
            $ quarters += 1
            jump finaldestinationafterevent

label foggylakereturningwiththebird01:
    if foragingground_bird_taken == 1: # taken
        $ quest_birdhunting_description06 = "I was asked to bring the news about the creature to {color=#f6d6bd}Creeks{/color} in a day or so."
        $ quest_birdhunting_description05 = "The trip was a success. I received my reward."
        $ foragers_quest_message_timer = day
        if foragers_quest_reward:
            $ coins += 8
            show screen notifyimage( "Journal updated: Bird Hunt.\n+8", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bird Hunt. +8 {image=cointest}{/i}')
        else:
            $ coins += 5
            show screen notifyimage( "Journal updated: Bird Hunt.\n+5", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bird Hunt. +5 {image=cointest}{/i}')
        $ can_leave = 1
        if foggy_about_shelter == 1:
            $ can_rest = 1
        else:
            $ can_rest = 0
        $ can_items = 1
        $ foggylake_horsename_fluff = renpy.random.choice(['enjoying some fresh grass', 'napping', 'observing the movement on the lake', 'around slowly moving, as far as its cord allows it', 'pawing the ground', 'fighting off some flies with its tail', 'lazily looking around', 'drinking from the lake'])
        menu:
            '{color=#f6d6bd}Foggy{/color} observes you from the top of the stairs, with the hand resting on her stomach. “Well done, dears,” she grins at the sight of the runner. “Tether it close to the water. Love,” she looks at you, “be nice and head to {color=#f6d6bd}Creeks{/color} today or tomorrow, will you? Tell {color=#f6d6bd}Efren{/color} we’re coming, and to give you a bone for the message.” She glances at {color=#f6d6bd}the man with one hand{/color} as he scowls at the beast. Before she enters the door, she smiles at her son. “Once you’re done, wash your hands and come for dinner. Tell me everything.”
            \n\nTethering the creature to a beam takes you a few minutes. {color=#f6d6bd}Ilan’s{/color} gasping for air, leaning on his knees, and while {color=#f6d6bd}Tzvi{/color} keeps his posture straight, his red face betrays him. “Well,” says {color=#f6d6bd}the tall man{/color}, “I have your dragons here. Thanks for your work, friend.” The ring-shaped bones are covered in his sweat.
            \n\n{color=#f6d6bd}[horsename]{/color} is [foggylake_horsename_fluff].
            '
            'I enter the tavern.':
                jump foggylakeinside01
            'I approach the foragers.' ( condition="(quarters < (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters < (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters < (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters < (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters < (world_daylength-4) and quest_birdhunting == 1) or (quarters < (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters < (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and not foragers_about_travelers) or (quarters < (world_daylength-4) and not foragers_about_rumors) or (quarters < (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters < (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                jump foggylakeforagers01
            'I have nothing to say to the foragers. (disabled)' ( condition="not (quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) and not (quest_missinghunters == 1 and not foragers_about_missinghunters) and not (oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) and not (not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) and not (quest_birdhunting == 1) and not (foragers_caius_heardabout and not foragers_caius_spokento) and not (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) and not (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) and not (not foragers_about_travelers) and not (not foragers_about_rumors) and not (ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) and not (not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                pass
            'The foragers are preparing for the night. (disabled)' ( condition="(quarters >= (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters >= (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters >= (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters >= (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters >= (world_daylength-4) and quest_birdhunting == 1) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters >= (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and not foragers_about_travelers) or (quarters >= (world_daylength-4) and not foragers_about_rumors) or (quarters >= (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters >= (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                pass
            'I could wash myself in the lake.' if not foggylake_bath:
                jump foggylakelake01
    elif foragingground_bird_taken == 2: # killed
        $ coins += 2
        show screen notifyimage( "Quest completed: Bird Hunt.\n+2", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bird Hunt. +2 {image=cointest}{/i}')
        $ quest_birdhunting_description04 = "The trip was a partial success. The bird died in the process, but at least we’ve got its meat."
        $ quest_birdhunting = 2
        $ can_leave = 1
        if foggy_about_shelter == 1:
            $ can_rest = 1
        else:
            $ can_rest = 0
        $ can_items = 1
        $ foggylake_horsename_fluff = renpy.random.choice(['enjoying some fresh grass', 'napping', 'observing the movement on the lake', 'around slowly moving, as far as its cord allows it', 'pawing the ground', 'fighting off some flies with its tail', 'lazily looking around', 'drinking from the lake'])
        menu:
            '{color=#f6d6bd}Foggy{/color} observes you from the top of the stairs, with the hand resting on her stomach. At the sight of the dead runner, she makes a fist, cracking her knuckles. “Didn’t work, aye? Drop it somehwere, wash your hands, and come to eat.” During this invitation, she doesn’t look at you. “We’ll deplume it soon, and {color=#f6d6bd}Caius{/color},” she looks at the one handed man, who observes the dead animal with a wide grin. “Be a dear and cut the wood. We have a lot of cooking ahead.” She enters the door.
            \n\nYou hear the soft thud of the corpse hitting the ground. {color=#f6d6bd}Ilan’s{/color} gasping for air, leaning on his knees, and while {color=#f6d6bd}Tzvi{/color} keeps his posture straight, his red face betrays him. “Well,” says {color=#f6d6bd}the tall man{/color}, “I have your dragons here. Two for the dead one, like we said. Thanks for the effort, friend.” The ring-shaped bones are covered in his sweat.
            \n\n{color=#f6d6bd}[horsename]{/color} is [foggylake_horsename_fluff].
            '
            'I enter the tavern.':
                jump foggylakeinside01
            'I approach the foragers.' ( condition="(quarters < (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters < (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters < (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters < (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters < (world_daylength-4) and quest_birdhunting == 1) or (quarters < (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters < (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and not foragers_about_travelers) or (quarters < (world_daylength-4) and not foragers_about_rumors) or (quarters < (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters < (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                jump foggylakeforagers01
            'I have nothing to say to the foragers. (disabled)' ( condition="not (quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) and not (quest_missinghunters == 1 and not foragers_about_missinghunters) and not (oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) and not (not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) and not (quest_birdhunting == 1) and not (foragers_caius_heardabout and not foragers_caius_spokento) and not (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) and not (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) and not (not foragers_about_travelers) and not (not foragers_about_rumors) and not (ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) and not (not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                pass
            'The foragers are preparing for the night. (disabled)' ( condition="(quarters >= (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters >= (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters >= (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters >= (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters >= (world_daylength-4) and quest_birdhunting == 1) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters >= (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and not foragers_about_travelers) or (quarters >= (world_daylength-4) and not foragers_about_rumors) or (quarters >= (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters >= (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                pass
            'I could wash myself in the lake.' if not foggylake_bath:
                jump foggylakelake01
    else: # escaped
        $ quest_birdhunting_description03 = "The trip was a failure. The bird managed to run away."
        $ quest_birdhunting = 3
        $ renpy.notify("Quest completed: Bird Hunt")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Bird Hunt{/i}')
        $ can_leave = 1
        if foggy_about_shelter == 1:
            $ can_rest = 1
        else:
            $ can_rest = 0
        $ can_items = 1
        $ foggylake_horsename_fluff = renpy.random.choice(['enjoying some fresh grass', 'napping', 'observing the movement on the lake', 'around slowly moving, as far as its cord allows it', 'pawing the ground', 'fighting off some flies with its tail', 'lazily looking around', 'drinking from the lake'])
        menu:
            '{color=#f6d6bd}Foggy{/color} observes you from the top of the stairs, with the hand resting on her stomach. She runs her eyes over {color=#f6d6bd}Ilan{/color}, but he waves off her wordless question. “It ran away, we lacked one more soul.”
            \n\n“At least you’re safe,” she sighs. “Wash your hands, the dinner is almost ready.” She enters the open door, while the men walk away in silence.
            \n\n{color=#f6d6bd}[horsename]{/color} is [foggylake_horsename_fluff].
            '
            'I enter the tavern.':
                jump foggylakeinside01
            'I approach the foragers.' ( condition="(quarters < (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters < (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters < (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters < (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters < (world_daylength-4) and quest_birdhunting == 1) or (quarters < (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters < (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and not foragers_about_travelers) or (quarters < (world_daylength-4) and not foragers_about_rumors) or (quarters < (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters < (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                jump foggylakeforagers01
            'I have nothing to say to the foragers. (disabled)' ( condition="not (quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) and not (quest_missinghunters == 1 and not foragers_about_missinghunters) and not (oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) and not (not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) and not (quest_birdhunting == 1) and not (foragers_caius_heardabout and not foragers_caius_spokento) and not (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) and not (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) and not (not foragers_about_travelers) and not (not foragers_about_rumors) and not (ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) and not (not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                pass
            'The foragers are preparing for the night. (disabled)' ( condition="(quarters >= (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters >= (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters >= (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters >= (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters >= (world_daylength-4) and quest_birdhunting == 1) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters >= (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and not foragers_about_travelers) or (quarters >= (world_daylength-4) and not foragers_about_rumors) or (quarters >= (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters >= (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
                pass
            'I could wash myself in the lake.' if not foggylake_bath:
                jump foggylakelake01

label foragers_about_rawhide01:
    $ can_leave = 1
    if foggy_about_shelter == 1:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    if not foragers_firsttime:
        $ custom1 = "{color=#f6d6bd}the large forager{/color}"
    else:
        $ custom1 = "{color=#f6d6bd}Ilan{/color}"
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        'Once you get on the ground, [custom1] points at the old rawhide you’re carrying by your saddle. “Looking for a blanket, friend? You’ll find one, clean and all, in {color=#f6d6bd}Creeks{/color}. This one will get smelly soon.”
        \n\n[foggylake_fluff_outside]
        '
        'I enter the tavern.':
            jump foggylakeinside01
        'I approach the foragers.' ( condition="(quarters < (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters < (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters < (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters < (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters < (world_daylength-4) and quest_birdhunting == 1) or (quarters < (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters < (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and not foragers_about_travelers) or (quarters < (world_daylength-4) and not foragers_about_rumors) or (quarters < (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters < (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            jump foggylakeforagers01
        'I have nothing to say to the foragers. (disabled)' ( condition="not (quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) and not (quest_missinghunters == 1 and not foragers_about_missinghunters) and not (oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) and not (not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) and not (quest_birdhunting == 1) and not (foragers_caius_heardabout and not foragers_caius_spokento) and not (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) and not (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) and not (not foragers_about_travelers) and not (not foragers_about_rumors) and not (ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) and not (not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            pass
        'The foragers are preparing for the night. (disabled)' ( condition="(quarters >= (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters >= (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters >= (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters >= (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters >= (world_daylength-4) and quest_birdhunting == 1) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters >= (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and not foragers_about_travelers) or (quarters >= (world_daylength-4) and not foragers_about_rumors) or (quarters >= (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters >= (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            pass
        'I could wash myself in the lake.' if not foggylake_bath:
            jump foggylakelake01

label foggy_about_missinghunters_dayreported01:
    $ can_leave = 1
    if foggy_about_shelter == 1:
        $ can_rest = 1
    else:
        $ can_rest = 0
    $ can_items = 1
    if not foragers_firsttime:
        $ custom1 = "{color=#f6d6bd}The large forager{/color}"
    else:
        $ custom1 = "{color=#f6d6bd}Ilan{/color}"
    if not foragers_firsttime:
        $ custom2 = "{color=#f6d6bd}the other man{/color}"
    else:
        $ custom2 = "{color=#f6d6bd}Tvi{/color}"
    $ foggylake_inside_lastvisit = 1
    $ foggy_food_meals_available += 1
    $ foggy_friendship += 1
    $ foragers_friendship += 1
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        'You look around from the saddle. [custom1] is crouching by the palisade, with red eyes and clasped fingers, while [custom2] is by his side, observing the spread feathers. You get on the ground and {color=#f6d6bd}Foggy{/color} shows up in the tavern’s entrance. “We’ve heard the news of the hunters, love. We lost our friends, but now we can start to heal. Come when you’re done here, I’ll have dinner ready.”
        \n\n[foggylake_fluff_outside]
        '
        'I enter the tavern.':
            jump foggylakeinside01
        'I approach the foragers.' ( condition="(quarters < (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters < (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters < (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters < (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters < (world_daylength-4) and quest_birdhunting == 1) or (quarters < (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters < (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters < (world_daylength-4) and not foragers_about_travelers) or (quarters < (world_daylength-4) and not foragers_about_rumors) or (quarters < (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters < (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            jump foggylakeforagers01
        'I have nothing to say to the foragers. (disabled)' ( condition="not (quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) and not (quest_missinghunters == 1 and not foragers_about_missinghunters) and not (oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) and not (not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) and not (quest_birdhunting == 1) and not (foragers_caius_heardabout and not foragers_caius_spokento) and not (foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) and not (foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) and not (not foragers_about_travelers) and not (not foragers_about_rumors) and not (ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) and not (not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            pass
        'The foragers are preparing for the night. (disabled)' ( condition="(quarters >= (world_daylength-4) and quest_asterion == 1 and quest_gatheracrew == 1 and not asterion_found and not foragers_about_gatherthecrew_tzvi_recruited and not foragers_about_gatherthecrew_rejected) or (quarters >= (world_daylength-4) and quest_missinghunters == 1 and not foragers_about_missinghunters) or (quarters >= (world_daylength-4) and oldtunnel_inside_undead_seen and not oldtunnel_inside_undead_pursuit and not oldtunnel_inside_undead_defeated and not oldtunnel_exploration_knowledge and not foragers_about_traps) or (quarters >= (world_daylength-4) and not foragers_quest and not day > foragingground_quest_timer and not foragingground_bird_gone) or (quarters >= (world_daylength-4) and quest_birdhunting == 1) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and not foragers_caius_spokento) or (quarters >= (world_daylength-4) and foggy_about_militarycamp and not foragers_caius_heardabout and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and foragers_caius_heardabout and foragers_caius_spokento and not foragers_caius_aboutvision) or (quarters >= (world_daylength-4) and not foragers_about_travelers) or (quarters >= (world_daylength-4) and not foragers_about_rumors) or (quarters >= (world_daylength-4) and ruinedshelter_mushrooms and not foggy_about_mushroomsinruinedshelter and not foragers_about_mushrooms) or (quarters >= (world_daylength-4) and not quest_recruitahunter_spokento_foragers and quest_recruitahunter == 1 and not quest_recruitahunter_dalit_about_erastos_completed)" ):
            pass
        'I could wash myself in the lake.' if not foggylake_bath:
            jump foggylakelake01

label foggylakeforagersregularquestionsabouttravelers01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you often have travelers here?”')
    $ foragers_about_travelers = 1
    $ questionpreset = "foragers1"
    menu:
        '{color=#f6d6bd}Ilan’s{/color} voice is like thunder. “Nah. You may very well be the last one this season. Sometimes a group of adventurers, who knows hwy, and southern traders in spring and autumn. Most of our visitors are from the villages, usually {color=#f6d6bd}Creeks{/color} and {color=#f6d6bd}Gale Rocks{/color}. They leave goods at our place, or just outside, and my ma barters in their name with the others. I mean, rocks, timber, furs, and barrelled fish can wait a few days.”
        '
        '(preset foragers1)':
            pass

label foggylakeforagersregularquestionsaboutpeninsula01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about the peninsula?”')
    $ foragers_about_rumors = 1
    $ minutes += 5
    $ questionpreset = "foragers1"
    $ description_akakios04 = "According to {color=#f6d6bd}Ilan{/color}, he doesn’t care about chit-chat and gets straight to the point."
    menu:
        '{color=#f6d6bd}Tzvi{/color} lets out a sigh. “Not much to see here, aye? Trees, rocks, ponds. I’ve never been in {color=#f6d6bd}Howler’s{/color},” he starts, but then {color=#f6d6bd}Ilan{/color} chips in. “I have, a couple of times. A nice place, kind folks. Lots of grain. They have but one trader, {color=#f6d6bd}Akakios{/color}. He pays poorly, but at least doesn’t waste one’s time, gets straight to the point, see?” He thinks for a bit. “And they’re all so tall! Twice as tall as he is,” he points at {color=#f6d6bd}Tzvi{/color}, who frowns and squeaks back at him. “Bullshit.”
        \n\nYou gossip for the next few minutes, but the things they share with you are of little use. They end up saying that you should talk with {color=#f6d6bd}Foggy{/color} instead. “She used to travel a lot, and speaks with every visitor.”
        '
        '(preset foragers1)':
            pass

label foggylakeforagersaboutmushrooms01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I saw a lot of mushrooms at the ruined shelter in the west. A lot of bugs, too.”')
    $ foragers_about_mushrooms += 1
    $ foggy_friendship += 1
    $ foragers_friendship += 1
    $ questionpreset = "foragers1"
    menu:
        'You describe them, struggling with naming the shapes and colors, but the foragers decipher your attempts with ease. {color=#f6d6bd}Ilan{/color} looks at the clouds, nodding with a smile. “Should still be warm enough to dry them, thanks. We’ll get there soon.”
        '
        '(preset foragers1)':
            pass

label foggylakeforagersregularquestionsaboutefrenandhunt01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A little wolf told me you didn’t ask any of the hunters to go with you.”')
    $ foragers_quest_question_efren += 1
    $ creeks_reasonstojoin_beastattacks += 1
    $ creeks_reasonstojoin_creeksaboutlackingmeat += 1
    $ foragers_friendship += 1
    $ questionpreset = "foragers1"
    menu:
        '{color=#f6d6bd}The shorter man{/color} steps away. “Who cares? It’s us who put dragons on the table.”
        \n\n{color=#f6d6bd}His larger companion{/color} blushes slightly. “It’s nothing, really... The days are getting colder, so the beasts are getting busy, and some of our friends are already missing. I’d rather pay a stranger to shield us from our prey than put our tribesfolk at risk. You know how it is, friend.”
        '
        '(preset foragers1)':
            pass

label foggylakeforagersregularquestionsaboutmissinghunters01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Admon{/color}, {color=#f6d6bd}Dalia{/color}, and {color=#f6d6bd}Vaschel{/color} didn’t return from their hunting trip. Did they share any plans with you?”')
    $ foragers_about_missinghunters = 1
    $ minutes += 2
    $ questionpreset = "foragers1"
    menu:
        '“Hwy would they,” growls {color=#f6d6bd}Tzvi{/color}. “The don’t waste our time, we don’t bother with theirs.”
        \n\n{color=#f6d6bd}Ilan’s{/color} eyes are a bit warmer. “{color=#f6d6bd}Efren{/color} already asked us. They ate there, on the stairs, then left, days ago. They didn’t want to get in each other’s way, so they planned to spread, that’s all I know.” Seeing your look, he spreads his arms in an awkward shrug. “They were laughing, eating, all confident and strong. I didn’t know they would disappear.”
        \n\nYou consider his words when {color=#f6d6bd}the shorter man{/color} starts to snap his fingers. “Wait, wait, wait, I heard one thing. Something ‘bout, yeah, that they {i}won’t{/i} go north, because of the {i}dark magic{/i} in the tunnel.”
        \n\n“Then it’s smart of them,” concludes {color=#f6d6bd}Ilan{/color} with a humble smile. “Better than nothing, aye? I’m sure they’re fine.”
        '
        '(preset foragers1)':
            pass

label foggylakeforagersregularquestionsabouttraps01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know this and that about traps. Can you teach me how to build them?”')
    $ foragers_about_traps = 1
    $ questionpreset = "foragers1"
    menu:
        '“Hwy, you’re catching a hare, or a stoat?” When you explain what you’ve seen in the tunnel, {color=#f6d6bd}Ilan{/color} looks around. “Oh dear,” he whispers. “You better look for some big traps. Asks {color=#f6d6bd}Efren{/color}, maybe. From {color=#f6d6bd}Creeks{/color}. He’s a {i}real{/i} hunter.”
        '
        '(preset foragers1)':
            pass

label foggylakeforagersregularquestionsabouttulia01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn toward the one without a hand. “Do you know {color=#f6d6bd}Tulia{/color}?”')
    $ foragers_caius_spokento = day
    if not foragers_caius_voice:
        $ foragers_caius_voice = 1
        $ custom1 = " He has the accent of the cityfolk. Same as yours."
    else:
        $ custom1 = ""
    $ foragers_caius_friendship += 1
    menu:
        'The man gives you a surprised glance, but then looks down and crosses his arms, holding his hand under his shoulder. “I’m a new man now. There’s nothing that ties me to the army.”[custom1]
        '
        '“You’ve crossed a great part of this land, greater than most. Have you seen anything unusual?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ve crossed a great part of this land, greater than most. Have you seen anything unusual?”')
            menu:
                'He takes a deep breath, his voice is close to a whisper. “There’s fog in my soul. I was on the eastern road, hungry and sick, praying for The Wright to send its beasts on me and save me from the pains of living. I remember the touch of fur, and the breath on my neck, the claws pinning me to the ground. I was waiting with my eyes closed, then I woke up in the middle of the night, still feeling. I got back on my feet, walking until I reached the lights of this tavern, without so much as a bruise. {color=#f6d6bd}Foggy{/color} may have no faith in her heart, but The Wright used her kindness to give me a second chance.”
                \n\n{color=#f6d6bd}Ilan{/color} frowns at the man’s words, and there’s cautiousness in his voice. “He may be crazy, but it’s true he came here after midnight, raving. Maybe the monsters don’t like his scent.”
                '
                '“So you forgot everything?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you forgot everything?”')
                    $ description_shortcut06 = "According to {color=#f6d6bd}Ilan{/color}, it’s a bad idea to enter the woods without a crossbow."
                    $ foragers_about_furlesswolf = 1
                    $ questionpreset = "foragers1"
                    menu:
                        'He hides his stump in the palm of his hand and curls up. “I’ve seen a dragon eating a tree, an ape that tore away the head of a monstrous cat, and a wolf without fur that was as quick as a lightning. Now leave me alone, evil spirit. Let my shame rest.”
                        \n\nHe’s shaking. “Let him be, aye?” {color=#f6d6bd}Tzvi{/color} grunts at you. “Nothing wrong ‘bout a man trying to forget.”
                        \n\n{color=#f6d6bd}Ilan{/color} rubs his chin. “A furless wolf, friend? I’ve heard about one, our tribesfolk saw it in the heart of the woods. A nasty beast, let’s hope it won’t find a mate for breeding. It charges at you like a runner, and jumps right at your throat,” he touches his neck, “so even the hunters stay away from it. Too bad we’ve no crossbows,” he raises his wooden club. “Aye, better to avoid the deep woods without one.”
                        '
                        '(preset foragers1)':
                            pass

label foggylakeforagersregularquestionsaboutvisions01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, {color=#f6d6bd}Caius{/color}. Your boss told me you have some sort of visions.”')
    if not foragers_caius_voice:
        $ foragers_caius_voice = 1
        $ custom1 = " He has the accent of the cityfolk. Same as yours."
    else:
        $ custom1 = ""
    if foragers_caius_friendship > 0:
        $ foragers_caius_aboutvision = 1
        menu:
            'He meets your eyes and straightens up, reaching out to you with his dirty hand.
            '
            'I allow him.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I allow him.')
                $ custom2 = "It rests on your shoulders, light like a bird. Your nose tells you that he hasn’t washed in quite a few days."
                label foggylakeforagersregularquestionsaboutvisions02:
                    menu:
                        '[custom2] [custom1]
                        \n\n“The Wright hears the prayers of the people. I mean, of The Ten Cities! All the tribes, and the empress, and priests, merchants, farmers... We thought things were lost, the glory behind us! Punished by humiliation for our weak hearts,” he starts to shake his stump a foot away from your face, “but there’s hope!”
                        \n\nHis voice gets stronger with every heartbeat, and a wide smile shows up under his beard. “The Wright’s test is behind us, and we, the sinners, have failed it! Now are the days of atonement, and of The New Cities, with New Tribes and The Cleansed Land! We, you know, you know! Have to {i}fix{/i} ourselves, change what we can, weed out our sins and bring fresh hearts to the Holiest Soul Carrier, and let them guide us anew, with new Tablets and prayers, and a new church... The Only Church! Yes!”
                        \n\nHe steps in place, bursting with excitement. “All the rivers will flow as one wave, and The New Cities, The Reborn City, will wipe out the {i}barbarians{/i},” he spits on the ground, “and send them back into their chains!” He points his hand south. “We will come through the ashes, reborn into a power greater than any fortress, than a thousand dragons, than all the ships and armies!”
                        \n\nHe steps back, lowering his head. “I, the humble servant, was granted this vision.”
                        '
                        'I nod enthusiastically. “That’s great news!”' if pc_religion == "pagan" or pc_religion == "none" or pc_religion == "unknown":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod enthusiastically. “That’s great news!”')
                            $ foragers_caius_friendship += 1
                            $ questionpreset = "foragers1"
                            menu:
                                'He turns away from you and approaches the wall. “Take this word and carry it in your heart, and on your lips. Be a part of the wave that swallows the faithless.”
                                \n\n{color=#f6d6bd}Tzvi{/color} presses a clenched fist to his lips, stopping himself from laughter, while {color=#f6d6bd}Ilan{/color} looks at the prophet with concern. “Don’t encourage him, friend. It’s not right.”
                                '
                                '(preset foragers1)':
                                    pass
                        '(lie) I nod enthusiastically. “That’s great news!”' if pc_religion == "pagan" or pc_religion == "none" or pc_religion == "unknown":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) I nod enthusiastically. “That’s great news!”')
                            $ foragers_caius_friendship += 1
                            $ pc_lies += 1
                            $ questionpreset = "foragers1"
                            menu:
                                'He turns away from you and approaches the wall. “Take this word and carry it in your heart, and on your lips. Be a part of the wave that swallows the faithless.”
                                \n\n{color=#f6d6bd}Tzvi{/color} presses a clenched fist to his lips, stopping himself from laughter, while {color=#f6d6bd}Ilan{/color} looks at the prophet with concern. “Don’t encourage him, friend. It’s not right.”
                                '
                                '(preset foragers1)':
                                    pass
                        'I nod enthusiastically. “So be it!”' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod enthusiastically. “That’s great news!”')
                            $ foragers_caius_friendship += 1
                            $ pc_faithpoints += 1
                            $ questionpreset = "foragers1"
                            menu:
                                'He turns away from you and approaches the wall. “Take this word and carry it in your heart, and on your lips. Be a part of the wave that swallows the faithless.”
                                \n\n{color=#f6d6bd}Tzvi{/color} presses a clenched fist to his lips, stopping himself from laughter, while {color=#f6d6bd}Ilan{/color} looks at the prophet with concern. “Don’t encourage him, friend. It’s not right.”
                                '
                                '(preset foragers1)':
                                    pass
                        '(lie) I nod enthusiastically. “So be it!”' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) I nod enthusiastically. “That’s great news!”')
                            $ foragers_caius_friendship += 1
                            $ pc_lies += 1
                            $ questionpreset = "foragers1"
                            menu:
                                'He turns away from you and approaches the wall. “Take this word and carry it in your heart, and on your lips. Be a part of the wave that swallows the faithless.”
                                \n\n{color=#f6d6bd}Tzvi{/color} presses a clenched fist to his lips, stopping himself from laughter, while {color=#f6d6bd}Ilan{/color} looks at the prophet with concern. “Don’t encourage him, friend. It’s not right.”
                                '
                                '(preset foragers1)':
                                    pass
                        'I nod. “I see.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “I see.”')
                            $ questionpreset = "foragers1"
                            menu:
                                'He gives you a harsh glance, then walks away, nodding and raising his voice. “Open your heart, or the wave will take you, too.”
                                \n\n{color=#f6d6bd}Tzvi{/color} presses a clenched fist to his lips, stopping himself from laughter, while {color=#f6d6bd}Ilan{/color} looks at the prophet with concern. “Don’t push him any longer, friend. He told you all that is already.”
                                '
                                '(preset foragers1)':
                                    pass
                        '“...You’re insane.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...You’re insane.”')
                            $ foragers_caius_friendship -= 1
                            $ questionpreset = "foragers1"
                            menu:
                                'He points at you with his stump. “The wave is going to take you too, roadwarden. You will drown in what’s to come.” He turns away from you and approaches the wall, crossing his arm.
                                \n\n{color=#f6d6bd}Tzvi{/color} presses a clenched fist to his lips, stopping himself from laughter, while {color=#f6d6bd}Ilan{/color} looks at the prophet with concern. “Don’t upset him, friend. He’ll have nightmares again.”
                                '
                                '(preset foragers1)':
                                    pass
            'I step away. “It’s fine. Just tell me.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away. “It’s fine. Just tell me.”')
                $ custom2 = "He grabs the empty air in front of your shoulder and after a pause, he draws invisible shapes with his arms."
                jump foggylakeforagersregularquestionsaboutvisions02
    else:
        $ foragers_caius_aboutvision_gray = 1
        $ questionpreset = "foragers1"
        menu:
            'He raises his head, frowning. “More mockery? Stay away from me, stranger. I have nothing to tell you.” [custom1]
            '
            '(preset foragers1)':
                pass

label foggylakeforagersregularquestionsaboutgatherthecrewALL:
    label foggylakeforagersregularquestionsaboutgatherthecrew01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a few souls willing to explore {color=#f6d6bd}High Island{/color} with me.”')
        $ foragers_about_gatherthecrew = 1
        menu:
            '“Stupid or hwat?” {color=#f6d6bd}Ilan{/color} bursts into laughter. “There are easier ways to seek death, and dragons aren’t worth that shit.”
            \n\n{color=#f6d6bd}Tzvi{/color}, however, gives you a long look. “Hwy?” You mention briefly your search for {color=#f6d6bd}Asterion{/color}. “Sounds like a waste of effort,” he adjusts his cloak, “but I’ll do it. For a fair pay. I’m good with knives, sneaking by, and making small things out of wood.”
            \n\n{color=#f6d6bd}The tall forager{/color} straightens up and looks his companion in the eyes, demanding explanation, but {color=#f6d6bd}the man in black fur{/color} waves it off. “I’m bored of the inn, and I’d hate spending another winter in {color=#f6d6bd}Creeks{/color}.” His voice carries a hint of an apology. “Aye, we need no dragons here. But I’d take them south, behind {color=#f6d6bd}Hags{/color}.”
            \n\nThe distance between them grows with every breath.
            '
            '“What’s your price?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your price?”')
                label foggylakeforagersregularquestionsaboutgatherthecrew03:
                    if quest_birdhunting_description05:
                        $ foragers_about_gatherthecrew_price = 20
                        $ custom1 = "“You did well during our hunt, so I assume you know hwat you’re doing."
                    elif quest_birdhunting_description04:
                        $ foragers_about_gatherthecrew_price = 25
                        $ custom1 = "“You didn’t do too bad during our hunt, so I assume you know hwat you’re doing."
                    elif quest_birdhunting_description03:
                        $ foragers_about_gatherthecrew_price = 30
                        $ custom1 = "“You didn’t do so well during our hunt, but at least you got out of it in one piece."
                    elif quest_birdhunting == 3:
                        $ foragers_about_gatherthecrew_price = 40
                        $ custom1 = "“You failed to help us in our hunt, so I don’t know if you’re to be trusted."
                    elif day > foragingground_quest_timer or foragingground_bird_gone:
                        $ foragers_about_gatherthecrew_price = 40
                        $ custom1 = "“I don’t know how well you’ll handle yourself in the wilderness, too bad we couldn’t hunt together."
                    else:
                        $ foragers_about_gatherthecrew_price = 35
                        $ custom1 = "“I don’t know how well you’ll handle yourself in the wilderness, so first I’d rather go out on a hunt together with you."
                    $ foragers_about_gatherthecrew_price -= foragers_friendship
                    if foggy_friendship <= 0:
                        $ foragers_about_gatherthecrew_price += 1
                    elif foggy_friendship < 5:
                        $ foragers_about_gatherthecrew_price += 0
                    elif foggy_friendship < 10:
                        $ foragers_about_gatherthecrew_price -= 1
                    elif foggy_friendship < 15:
                        $ foragers_about_gatherthecrew_price -= 2
                    elif foggy_friendship < 20:
                        $ foragers_about_gatherthecrew_price -= 3
                    else:
                        $ foragers_about_gatherthecrew_price -= 4
                    if creeks_reputation <= 0:
                        $ foragers_about_gatherthecrew_price += 1
                    elif creeks_reputation < 5:
                        $ foragers_about_gatherthecrew_price += 0
                    elif creeks_reputation < 10:
                        $ foragers_about_gatherthecrew_price -= 1
                    elif creeks_reputation < 15:
                        $ foragers_about_gatherthecrew_price -= 2
                    elif creeks_reputation < 20:
                        $ foragers_about_gatherthecrew_price -= 3
                    else:
                        $ foragers_about_gatherthecrew_price -= 4
                    $ foragers_about_gatherthecrew_price += appearance_price
                    if armor >= 4:
                        $ foragers_about_gatherthecrew_price -= 1
                    if item_axe03 or item_crossbow:
                        $ foragers_about_gatherthecrew_price -= 1
                    if foragers_about_gatherthecrew_price < 10:
                        $ foragers_about_gatherthecrew_price = 10
                        $ custom6 = "I won’t work for less, ever."
                    else:
                        $ custom6 = "Maybe a bit less in the future, if I see you’re useful for our tribesfolk and you can handle yourself."
                    menu:
                        '[custom1] {color=#f6d6bd}[foragers_about_gatherthecrew_price]{/color} dragons. [custom6] I’m good at sneaking. Even better at stabbing things. And I move well. Climb. Crawl.”
                        '
                        '“Very well. Take this and be ready to leave soon.”' if coins >= foragers_about_gatherthecrew_price:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. Take this and be ready to leave soon.”')
                            show screen notifyimage( "-%s" %foragers_about_gatherthecrew_price, "gui/coin2.png")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s {image=cointest}{/i}' %foragers_about_gatherthecrew_price)
                            $ coins -= foragers_about_gatherthecrew_price
                            $ foragers_about_gatherthecrew_tzvi_recruited = 1
                            $ questionpreset = "foragers1"
                            menu:
                                '“Easy. I always have by my side hwat I’m going to take, anyway,” he takes your pouch and gives you a wide smile. {color=#f6d6bd}Ilan{/color} observes the lake, his lips are shaking.
                                '
                                '(preset foragers1)':
                                    pass
                        'I can’t afford his services. (disabled)' if coins < foragers_about_gatherthecrew_price:
                            pass
                        '“I’ll let you know.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll let you know.”')
                            $ questionpreset = "foragers1"
                            menu:
                                'He spares you an annoyed grimace and avoids {color=#f6d6bd}Ilan’s{/color} gaze.
                                '
                                '(preset foragers1)':
                                    pass

    label foggylakeforagersregularquestionsaboutgatherthecrew02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s discuss the price, {color=#f6d6bd}Tzvi{/color}.”')
        jump foggylakeforagersregularquestionsaboutgatherthecrew03

label foragers_about_recruitahunter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever met {color=#f6d6bd}Erastos{/color}, the trapper?”')
    $ quest_recruitahunter_spokento_foragers = 1
    $ questionpreset = "foragers1"
    menu:
        'They exchange looks as {color=#f6d6bd}Tzvi{/color} adjusts his dark cloak. “We don’t hunt all that much, just catch birds and so on. Hwy don’t you try in {color=#f6d6bd}Creeks{/color}?”
        '
        '(preset foragers1)':
            pass
