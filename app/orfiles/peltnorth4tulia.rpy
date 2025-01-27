default tulia_pelt_firsttime = 0
default tulia_pelt_dayofvisit = 0
default tulia_pelt_inside = 0
default tulia_pelt_left = 0
default tulia_pelt_needstotalkwithiason = 0
default tulia_peltnorth_fluff = 0
default tulia_peltnorth_fluff_old = 0
default tulia_about_highisland = 0
default tulia_about_highisland_recruited = 0
default tulia_about_highisland_narration = 0
default tulia_highisland_joined = 0
default tulia_about_highisland_recruited_threshold = 9
default tulia_about_troll = 0
default tulia_about_troll_attack = 0
default tulia_about_troll_attack2 = 0
default tulia_about_returntocity = 0
default tulia_about_returntocity_alt = 0
default tulia_about_stillhavingreward = 0
default tulia_about_nonamebandit = 0

label peltnorth01insidetalkingwithtulia01:
    if tulia_pelt_dayofvisit != day:
        $ tulia_pelt_dayofvisit = day
        if tulia_friendship >= 10:
            $ custom1 = "She gives you a radiant smile. “Doing alright?”"
        elif tulia_friendship >= 6:
            $ custom1 = "She smiles and rests her ankle on her knee. “Hi there.”"
        elif tulia_friendship >= 2:
            $ custom1 = "She smiles politely. “Hello again.”"
        elif tulia_friendship >= 0:
            $ custom1 = "She greets you with a nod."
        else:
            $ custom1 = "She meets your eyes, but says nothing."
    else:
        if tulia_friendship >= 5:
            $ custom1 = "She’s relaxed, observing your eyes."
        else:
            $ custom1 = "She’s tense, observing the room."
    jump peltnorth_tulia01regularquestionsafter

label peltnorth_tulia01regularquestions:
    $ custom1 = ""
    $ custom1 = renpy.random.choice(['“What else do you need?”', '“Yes?”', 'She smiles gently.', '“How can I help you?”', '“Go ahead.”', '“Shoot.”'])
    label peltnorth_tulia01regularquestionsafter:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '[custom1]
            '
            '“Summer is almost over. We should soon travel back to the city.”' if not tulia_about_returntocity and not world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Summer is almost over. We should soon travel back to the city.”')
                $ tulia_about_returntocity = 1
                $ custom1 = "She shrugs. “Well, if any city rat is going to criticize me for getting out of here before the end of my {i}watch{/i}, they can jump into the sea, for all I care. I can head back whenever.”"
                jump peltnorth_tulia01regularquestionsafter
            '[[{color=#f6d6bd}Finish your adventure.{/color}] “Are you all packed and ready?”' if tulia_about_returntocity or world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you all packed and ready?”')
                jump peltnorth_tulia01about_returntocity02
            #######
            '“I found {color=#f6d6bd}Asterion{/color}.”' if asterion_found and not quest_asterion_description00goodresult and not quest_asterion_description00lies and not tulia_highisland_joined:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news about {color=#f6d6bd}Asterion{/color}.”')
                jump peltnorth_tulia01asterion_found01
            '“About {color=#f6d6bd}Asterion{/color}...”' if asterion_found and not quest_asterion_description00goodresult and not quest_asterion_description00lies and tulia_highisland_joined:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Asterion{/color}...”')
                jump peltnorth_tulia01asterion_found01_alt
            '(lie) “I found {color=#f6d6bd}Asterion{/color}.”' if not asterion_found and not quest_asterion_description00goodresult and not quest_asterion_description00lies:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Asterion{/color}.”')
                jump peltnorth_tulia01_asterionlie
            'I tell her about {color=#f6d6bd}High Island{/color}. “Want to join my expedition?”' if quest_gatheracrew == 1 and not tulia_about_highisland and not world_endmode and not quest_asterion_description00goodresult and not quest_asterion_description00lies:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell her about {color=#f6d6bd}High Island{/color}. “Want to join my expedition?”')
                jump peltnorth_tulia01asterion_highisland01
            '“I’m still looking for a crew.”' if quest_gatheracrew == 1 and tulia_about_highisland and not tulia_about_highisland_recruited and (tulia_friendship+appearance_charisma) >= tulia_about_highisland_recruited_threshold and not world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m still looking for a crew.”')
                jump peltnorth_tulia01asterion_highisland02
            '“I’m still looking for a crew. It’s an opportunity for you to pay off your debt.”' if quest_gatheracrew == 1 and tulia_about_highisland and not tulia_about_highisland_recruited and tulia_about_bandits_indebt and (tulia_friendship+appearance_charisma) < tulia_about_highisland_recruited_threshold and not world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m still looking for a crew. It’s an opportunity for you to pay off your debt.”')
                jump peltnorth_tulia01asterion_highisland01alt
            'She doesn’t trust me enough to join my crew. (disabled)' if quest_gatheracrew == 1 and tulia_about_highisland and not tulia_about_highisland_recruited and (tulia_friendship+appearance_charisma) < tulia_about_highisland_recruited_threshold and not world_endmode:
                pass
            #######
            '“I’ve been to your camp. It’s as good as gone.”' if militarycamp_destroyed_firsttime and not tulia_about_troll:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to your camp. It’s as good as gone.”')
                $ tulia_about_troll = 1
                $ tulia_friendship += 1
                $ custom1 = "You explain that the broken entrance is in worse shape than she remembers, and that the scavengers are going to have a feast for a few days, if not more. She rubs the top of her head with her entire palm, glancing at two hunters who just entered the room.\n\n“No longer my problem,” she says to herself, but then meets your eyes and lets out a sorrowful chuckle. “Quite a monster we knocked down, wasn’t it?”"
                jump peltnorth_tulia01regularquestionsafter
            '“Tell me about the troll attack.”' if not tulia_about_troll_attack:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about the troll attack.”')
                $ tulia_about_troll_attack = 1
                $ custom1 = "“There isn’t much to say. It came in the early hours, we threw and shot anything we could at it. After it broke through the gate, I had one last arrow left. My {i}subordinate{/i}” her voice is bitter, “gave me time to aim. And now he’s gone.”"
                jump peltnorth_tulia01regularquestionsafter
            '“Did you manage to burn the other soldier?”' if tulia_about_troll_attack and not tulia_about_troll_attack2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you manage to burn the other soldier?”')
                $ tulia_about_troll_attack2 = 1
                $ custom1 = "The sorrow in her eyes makes the shake of her head redundant."
                jump peltnorth_tulia01regularquestionsafter
            ######
            '“Do you still have my reward? Or is it back at the camp?”' if not quest_asterion_description00goodresult and not quest_asterion_description00lies and not tulia_about_stillhavingreward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to your camp. It’s as good as gone.”')
                $ tulia_about_stillhavingreward = 1
                $ custom1 = "After a brief scowl, she looks down and shakes her head, snickering weakly. “I knew you would ask me that. Yeah, it’s all there. I took everything of value with me.”"
                jump peltnorth_tulia01regularquestionsafter
            #######
            '“The priest of {color=#f6d6bd}White Marshes{/color} has agreed to release the dead shells. Problem solved.”' if orentius_convinced and not tulia_about_nomoreundead:
                jump peltnorth_tulia_about_nomoreundead01
            '“The priest of {color=#f6d6bd}White Marshes{/color} is gone, and so are his undead. Problem solved.”' if orentius_banished and not tulia_about_nomoreundead:
                jump peltnorth_tulia_about_nomoreundead02
            '“The village of {color=#f6d6bd}White Marshes{/color} is no more. The North will now struggle with a large group of undead.”' if whitemarshes_destroyed and not tulia_about_nomoreundead:
                jump peltnorth_tulia_about_nomoreundead03
            #######
            '“I found this wax tablet. Do you recognize it?”' if not tulia_about_tablet and item_asteriontablet:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this wax tablet. Do you recognize it?”')
                $ tulia_about_tablet += 1
                jump peltnorth_tulia01tulia_about_tablet01
            #######
            '“Guess what? I met with {color=#f6d6bd}Caius{/color}.”' if foragers_caius_heardabout and foragers_caius_spokento and not tulia_about_caius_spokento:
                jump peltnorth_tulia01tulia_about_caius_spokento01
            #######
            '“Did you ever enter the road leading through the heart of the woods?”' if shortcut_pcknowsabout and not tulia_about_shortcut:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you ever enter the road leading through the heart of the woods?”')
                $ tulia_about_shortcut += 1
                jump peltnorth_tulia01tulia_about_shortcut01
            #######
            '“Do you have any idea about what happened to the ruined village in the west?”' if ruinedvillage_firsttime == 1 and not ruinedvillage_confront_can and not ruinedvillage_truth and not tulia_about_ruinedvillage:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea about what happened to the ruined village in the west?”')
                $ tulia_about_ruinedvillage += 1
                if quest_ruins == 1 and not quest_ruins_description01:
                    $ renpy.notify("Journal updated: The Ruined Village")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                $ quest_ruins_description01 = "I heard that the village was destroyed almost ten years ago."
                jump peltnorth_tulia01tulia_about_ruinedvillage01
            #######
            '“Have you ever encountered the bandits from the north?”' if banditshideout_bandits_pchearedabout and not tulia_about_bandits1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever encountered the bandits from the north?”')
                $ tulia_about_bandits1 += 1
                jump peltnorth_tulia01tulia_about_bandits01
            '“Nice acting, but I spoke with {color=#f6d6bd}Glaucia{/color}. You’re working with her.”' if tulia_about_bandits1 and description_tulia05 and not tulia_about_bandits2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Nice acting, but I spoke with {color=#f6d6bd}Glaucia{/color}. You’re working with her.”')
                $ tulia_about_bandits2 += 1
                jump peltnorth_tulia01tulia_about_bandits02
            '“Come on, now. This is the only pass through {color=#f6d6bd}Hag Hills{/color}. Recently, there was a caravan with tools and spices that was taken by force, to be sold for ransom. {i}Someone{/i} told them to turn east, right into the band’s trap. You want me to believe you bear no responsibility, and saw nothing?”' if tulia_about_bandits2 and glaucia_about_lostmerchants_trail and not tulia_about_bandits3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Come on, now. This is the only pass through {color=#f6d6bd}Hag Hills{/color}. Recently, there was a caravan with tools and spices that was taken by force, to be sold for ransom. {i}Someone{/i} told them to turn east, right into the band’s trap. You want me to believe you bear no responsibility, and saw nothing?”')
                $ tulia_about_bandits3 += 1
                jump peltnorth_tulia01tulia_about_bandits03
            #######
            'I glance at {color=#f6d6bd}the bandit{/color}. “You know him?”' if not tulia_about_nonamebandit and tulia_about_bandits2 and shortcut_bandit_identity and shortcut_darkforest_bandit_inpeltnorth:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at {color=#f6d6bd}the bandit{/color}. “You know him?”')
                $ tulia_about_nonamebandit = 1
                jump peltnorth_tulia01tulia_about_nonamebandit01
            #######
            '“What was your squad’s mission?”' if not tulia_about_hermission:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What was your squad’s mission?”')
                $ tulia_about_hermission += 1
                jump peltnorth_tulia01regularadditionalquestion03
            #######
            'She doesn’t trust me enough to tell me about her squad’s mission. (disabled)' if tulia_about_hermission and not description_tulia04 and (tulia_friendship+appearance_charisma) < 3:
                pass
            #######
            '“About your squad’s mission...”' if tulia_about_hermission and not description_tulia04 and (tulia_friendship+appearance_charisma) >= 3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What was your squad’s mission?”')
                jump peltnorth_tulia01regularadditionalquestion03p02
            #######
            'I head to {color=#f6d6bd}the innkeep{/color}.' if tulia_pelt_needstotalkwithiason and not world_endmode:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to {color=#f6d6bd}the innkeep{/color}.')
                $ can_rest = 0
                $ can_items = 0
                $ tulia_pelt_needstotalkwithiason = 0
                jump peltnorth_tulia_meeting_firsttime03
            'I take another look at the main hall.' if not tulia_pelt_needstotalkwithiason and peltnorth_bonusnpcs > 0 and not world_endmode:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            'I go outside.' if not tulia_pelt_needstotalkwithiason and not world_endmode:
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump leavingthepeltnorth
            'It’s time to leave the peninsula behind. (disabled)' if world_endmode:
                pass

label peltnorth_tulia01tulia_about_tablet01: #“I found this wax tablet. Do you recognize it?”
    menu:
        'She opens it and takes takes a quick glance. “Well, it’s from {color=#f6d6bd}Hovlavan{/color}. {color=#f6d6bd}Asterion{/color} and my lieutenant were the only people I’ve seen with green tablets like this one. And the locals don’t write chronicles.”
        \n\nShe gives it back. “I can’t read. Better look for a priest of The Wright.”
        '
        '“Good call.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Good call.”')
            jump peltnorth_tulia01regularquestions

label peltnorth_tulia01tulia_about_shortcut01: # “Did you ever enter the road leading through the heart of the woods?”
    if quintus_pelt_firsttime and not quintus_pelt_left:
        menu:
            '“Oh, I was advised not to. By {color=#f6d6bd}Quintus{/color}, there,” she nods toward him. “At his gate. He almost begged us not to enter the woods, so we took the longer route.”
            '
            '“I see.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see.”')
                jump peltnorth_tulia01regularquestions
    else:
        menu:
            '“Oh, I was advised not to. Have you seen that huge gate in the west? Made of rocks, very tall? We met a guard there, named... {color=#f6d6bd}Quinton{/color}, maybe? A kind soul, but a bit slow. He almost begged us not to enter the woods, so we took the longer route.”
            '
            '“I see.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see.”')
                jump peltnorth_tulia01regularquestions

label peltnorth_tulia01tulia_about_ruinedvillage01: # “Do you have any idea about what happened to the ruined village in the west?”
    menu:
        '“Nah, there were goblins around the walls, so we never went there. But I was told that the wrath of the herds crushed it... maybe ten years ago? If there were any survivors, they are surely gone by now.”
        '
        '“Maybe they moved to other settlements, or left the peninsula.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe they moved to other settlements, or left the peninsula.”')
            $ custom1 = "“Or they got caught by bandits.”"
            jump peltnorth_tulia01regularquestionsafter

label peltnorth_tulia01tulia_about_banditsALL:
    label peltnorth_tulia01tulia_about_bandits01: # “Have you ever encountered the bandits from the north?”
        menu:
            'She lets out a sad sigh. “So there {i}are{/i} other bandits in the woods after all. If I survive long enough to report to someone, I’ll be sure to mention it.”
            '
            '“Nice acting, but I spoke with {color=#f6d6bd}Glaucia{/color}. You’re working with her.”' if tulia_about_bandits1 and description_tulia05 and not tulia_about_bandits2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Nice acting, but I spoke with {color=#f6d6bd}Glaucia{/color}. You’re working with her.”')
                $ tulia_about_bandits2 += 1
                jump peltnorth_tulia01tulia_about_bandits02
            '“Good idea.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Good idea.”')
                jump peltnorth_tulia01regularquestions
            '“I should learn more about them first.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I should learn more about them first.”')
                $ custom1 = "“Sure... If you can.” She gives you a long stare."
                jump peltnorth_tulia01regularquestions

    label peltnorth_tulia01tulia_about_bandits02:
        menu:
            '{color=#f6d6bd}Tulia{/color} glances at {color=#f6d6bd}the innkeep{/color} and gestures for you to lower your voice.
            '
            '“Come on, now. This is the only pass through {color=#f6d6bd}Hag Hills{/color}. Recently, there was a caravan with tools and spices that was taken by force, to be sold for ransom. {i}Someone{/i} told them to turn east, right into the band’s trap. You want me to believe you bear no responsibility, and saw nothing?”' if tulia_about_bandits2 and glaucia_about_lostmerchants_trail and not tulia_about_bandits3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Come on, now. This is the only pass through {color=#f6d6bd}Hag Hills{/color}. Recently, there was a caravan with tools and spices that was taken by force, to be sold for ransom. {i}Someone{/i} told them to turn east, right into the band’s trap. You want me to believe you bear no responsibility, and saw nothing?”')
                $ tulia_about_bandits3 += 1
                jump peltnorth_tulia01tulia_about_bandits03
            'I give her a grim look, but say nothing.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give her a grim look, but say nothing.')
                jump peltnorth_tulia01regularquestions

    label peltnorth_tulia01tulia_about_bandits03:
        menu:
            '“It’s not so simple,” she drawls out her words. “I wasn’t looking for dragon bones or mead. Without {color=#f6d6bd}Glaucia{/color}, my {i}squad{/i},” she looks around, as if to find her subordinates, “would never have been able to keep the valley passable. On the day of your arrival, she helped us get rid of a griffon that murdered two people this summer alone. Was I afraid of her threats? Sure. But she helped me save lives, too.”
            '
            'I meet her eyes. “You are not some coerced civilian who just happened to help a group of outlaws. People trusted you with their lives, and you betrayed them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I meet her eyes. “You are not some coerced civilian who just happened to help a group of outlaws. People trusted you with their lives, and you betrayed them.”')
                $ tulia_friendship -= 1
                $ custom1 = "She frowns, but her voice is quiet. “Why are you telling me this?”"
                jump peltnorth_tulia01tulia_about_bandits04
            'I nod slowly. “You didn’t have a choice. I carry a share of hard decisions on my shoulders as well.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod slowly. “You didn’t have a choice. I carry a share of hard decisions on my shoulders as well.”')
                $ tulia_friendship += 1
                $ tulia_about_bandits_grateful = 1
                $ custom1 = "She lets out a relieved sigh. “Thank you. For trying to understand.”"
                jump peltnorth_tulia01regularquestionsafter
            'I look away. “How do you think The Wright would respond to your excuses?”' if (pc_faithpoints >= 5 and pc_religion == "theunitedchurch") or (pc_faithpoints >= 6 and pc_religion == "ordersoftruth") or (pc_faithpoints >= 4 and pc_religion == "fellowship"):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look away. “How do you think The Wright would respond to your excuses?”')
                $ pc_faithpoints += 1
                $ custom1 = "She looks down. “It felt like I had no other choice. All I can do is pray for forgiveness.”"
                jump peltnorth_tulia01tulia_about_bandits04

    label peltnorth_tulia01tulia_about_bandits04:
        menu:
            '[custom1]
            '
            '“Once I’m back in the city, I’ll be forced to report this to the commanders. Better think how to justify yourself to the judge.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Once I’m back in the city, I’ll be forced to report this to the commanders. Better think how to justify yourself to the judge.”')
                $ tulia_about_bandits_hopeless = 1
                $ minutes += 5
                $ custom1 = "She taps the hilt of her sword, but gives you no other answer. Her shoulders are tense, and the wider the silence between you grows, the more convinced you are she won’t return to the city after all."
                jump peltnorth_tulia01regularquestionsafter
            '“I’m willing to keep this conversation between us, but not for free. I may need your help in the future. Either somewhere in the peninsula, or back in the city.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m willing to keep this conversation between us, but not for free. I may need your help in the future. Either somewhere in the peninsula, or back in the city.”')
                $ custom1 = "She straightens up, giving you an angry look, and nods briefly. “So this is how it’s going to be. So be it. {i}I’m in your debt{/i},” she says as if it’s a spell, but not without a hint of mockery."
                $ tulia_about_bandits_indebt = 1
                jump peltnorth_tulia01regularquestionsafter
            '(lie) “Your secret is safe with me, but I hope you’ll return the favor. I may need your help in the future.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “Your secret is safe with me, but I need you to return the favor. I may need your help in the future.”')
                $ custom1 = "She straightens up, giving you an angry look, and nods briefly. “So this is how it’s going to be. So be it. {i}I’m in your debt{/i},” she says as if it’s a spell, but not without a hint of mockery."
                $ pc_lies += 2
                $ tulia_about_bandits_indebt = 1
                $ tulia_about_bandits_liedto = 1
                jump peltnorth_tulia01regularquestionsafter

label peltnorth_tulia01tulia_about_nonamebandit01:
    $ custom1 = "She shrugs. “We never spoke while his boss was around. He used to stand in the shadows, observing the area, but I doubt he’s harmless. You don’t expect me to drag him all the way to the city, do you? I don’t need any more loose tongues there.”"
    jump peltnorth_tulia01regularquestionsafter

label peltnorth_tulia01tulia_about_caius_spokento01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Guess what? I met with {color=#f6d6bd}Caius{/color}.”')
    $ tulia_about_caius_spokento = 1
    $ tulia_friendship += 1
    menu:
        'You mention the tavern and {color=#f6d6bd}Foggy’s{/color} care. {color=#f6d6bd}Tulia{/color} sighs with relief and rests her hands on her sides. “Alive... That’s good to hear, deserter or not. How’s he doing?”
        '
        '“He’s a man of faith now. Kind of.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He’s a man of faith now. Kind of.”')
            $ custom1 = "You vaguely describe what you’ve heard, making her scratch her shaved head. “That’s news to me. I used to know him before he joined the army. Never seemed especially bothered with Wright’s teachings. One time I saw him with that...” She freezes, then lets out a chuckle. “Forget it. I’m glad he’s alright.”"
            jump peltnorth_tulia01regularquestionsafter
        '“He’s insane.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He’s insane.”')
            $ custom1 = "You vaguely describe what you’ve heard, making her shoulders slump. “At least he’s still here... So many things turned against him, and {i}I’m{/i} to blame for it, together with many others. Before he joined the army, he always had something to say. In violent ways, true, but he was a brisk soul. Now he would live on the street, without help or mercy. Good thing he found a new home,” her voice weakens."
            jump peltnorth_tulia01regularquestionsafter
        '“The people around him try to put him to good use. His soul is healing, even if slowly.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The people around him try to put him to good use. His soul is healing, even if slowly.”')
            $ custom1 = "You describe what you’ve seen, making her reach behind her head and take a deep breath. “Guess I ought to be a bit less angry thinking about my squad, though that’s quite a task,” she chuckles. “I’m so glad he found kindness in this land. I wish he didn’t have to look for it, though.”"
            jump peltnorth_tulia01regularquestionsafter

label peltnorth_tulia01regularadditionalquestionALL:
    label peltnorth_tulia01regularadditionalquestion03:
        menu:
            '{color=#f6d6bd}The lieutenant{/color} looks into your eyes. “You know. The usual. Making the roads safe. Keeping people alive.”
            '
            'I explain that it may be important for me to know what they’ve tried to accomplish.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explain that it may be important for me to know what they’ve tried to accomplish.')
                jump peltnorth_tulia01regularadditionalquestion03p02

    label peltnorth_tulia01regularadditionalquestion03p02:
        if tulia_friendship >= 3:
            $ description_tulia04 = "Her squad was meant to find a fitting place for a new outpost."
            menu:
                '“I can’t really tell you... Let’s just say it would be nice to have a {i}reliable{/i} outpost somewhere nearby. A place where you can always find a group of fighters willing to protect you in the name of the law,” she tilts her head back. “Now, if you have any other questions...”
                '
                'I change the topic.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I change the topic.')
                    jump peltnorth_tulia01regularquestions
        else:
            menu:
                '“I can’t really tell you,” you sense no hesitation. “Do you have any other questions?”
                '
                'I change the topic.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I change the topic.')
                    jump peltnorth_tulia01regularquestions

label peltnorth_tulia_about_nomoreundeadALL:
    label peltnorth_tulia_about_nomoreundead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The priest of {color=#f6d6bd}White Marshes{/color} has agreed to release the dead shells. Problem solved.”')
        $ tulia_about_nomoreundead += 1
        $ tulia_friendship += 3
        $ minutes += 5
        menu:
            '“Just like that?” Her voice is close to a shout, and after you explain that it’s quite a bit more complicated, she struggles to listen without assailing you with questions. Finally, you conclude your tale, and {color=#f6d6bd}Tulia{/color} chuckles weakly. “Ah, [pcname], you just made my life much easier. I can now report in {color=#f6d6bd}Hovlavan{/color} that at least {i}some{/i} of the northern struggles won’t require an entire squad to fix them.”
            '
            '“Just don’t omit {i}my{/i} part in this.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just don’t omit {i}my{/i} part in this.”')
                $ custom1 = "“I wouldn’t dare! I’m more than fine with the truth.”"
                jump peltnorth_tulia01regularquestionsafter

    label peltnorth_tulia_about_nomoreundead02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The priest of {color=#f6d6bd}White Marshes{/color} is gone, and so are his undead. Problem solved.”')
        $ tulia_about_nomoreundead += 2
        $ tulia_friendship += 2
        $ minutes += 5
        menu:
            '“Just like that?” Her voice is close to a shout, and after you explain that it’s quite a bit more complicated, she struggles to listen without assailing you with questions. Finally, you conclude your tale, and {color=#f6d6bd}Tulia{/color} sighs with relief. “Well, [pcname], maybe that village won’t be of much value to the city, but at least I can now report in {color=#f6d6bd}Hovlavan{/color} that {i}some{/i} of the northern struggles won’t require an entire squad to fix them. Not the perfect end, sure, but better than the alternatives.”
            '
            '“There was no other way.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There was no other way.”')
                $ custom1 = "“I don’t doubt it. Fanatics can’t be taught to listen.”"
                jump peltnorth_tulia01regularquestionsafter

    label peltnorth_tulia_about_nomoreundead03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The village of {color=#f6d6bd}White Marshes{/color} is no more. The North will now struggle with a large group of undead.”')
        $ tulia_about_nomoreundead += 1
        $ tulia_friendship += 1
        $ minutes += 5
        menu:
            '“How did that happen?” Her voice is close to a shout. “Did the necromancers lose their wits?” You think about the answer, explaining only the most essential parts of what happened. {color=#f6d6bd}Tulia{/color} seeks lies in your eyes, but finally shrugs. “No matter how many times priests tell us that we ought to stay away from dark magic, there’s always someone not willing to listen, ready to hurt everyone around them. Let’s hope that {color=#f6d6bd}Hovlavan{/color} will send a squad or two here before winter.”
            '
            '“Yeah. Let’s.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah. Let’s.”')
                $ custom1 = ""
                jump peltnorth_tulia01regularquestions

###################

label peltnorth_tulia01asterion_found01ALL:
    label peltnorth_tulia01asterion_found01:
        $ quarters += 2
        menu:
            '{color=#f6d6bd}Tulia{/color} doesn’t interrupt you, nodding as she keenly listens to your tale about clues and rumors, the old tribes, and the awakened corpse.
            \n\nShe ponders for a bit, looking at the oven. “So, what do you make of it? Not the brightest death I could wish for someone.”
            '
            '“He knew the danger, but took the risk anyway. A fair end to his journey.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He knew the danger, but took the risk anyway. A fair end to his journey.”')
                menu:
                    '“You two had this in common. {i}I{/i} wouldn’t travel to a wild island.” Her smile turns into a chuckle. “You’re lucky to still be here!”
                    '
                    '“Risk-taking is the only way to get somewhere in life.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Risk-taking is the only way to get somewhere in life.”')
                        $ asterion_found_pcthought = "readyforanadventure"
                        jump peltnorth_tulia01_2pcfoundhimaa
                    '“Yeah... From now on, I’ll stay on the roads.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah... From now on, I’ll stay on the roads.”')
                        $ asterion_found_pcthought = "readytoplayitsafe"
                        jump peltnorth_tulia01_2pcfoundhimab
                    'I smirk. “Says the gal who spent half a year in this shithole.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smirk. “Says the gal who spent half a year in this shithole.”')
                        menu:
                            '“Ha, I know!” Her laughter starts strong, but is cut off by a harsh cough. “I trusted my group too much, but that’s still a safer bet than risking your head.”
                            '
                            '“Risk-taking is the only way to get somewhere in life.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Risk-taking is the only way to get somewhere in life.”')
                                $ asterion_found_pcthought = "readyforanadventure"
                                label peltnorth_tulia01_2pcfoundhimaa: #“Risk-taking is the only way to get somewhere in life.”
                                    menu:
                                        '“Spoken like a true adventurer,” she scratches the back of her head. Her hair has started to show. “And you’re not going to stay here for long. A roadwarden who wants to stay alive needs to know how to say {i}no{/i} to their ambitions... Yet I bet that once you get used to these roads, you’ll get bored of them.”
                                        '
                                        '“Well, that’s surely possible.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, that’s surely possible.”')
                                            jump peltnorth_tulia01_03gettingreward
                            '“Yeah... From now on, I’ll stay on the roads.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah... From now on, I’ll stay on the roads.”')
                                $ asterion_found_pcthought = "readytoplayitsafe"
                                label peltnorth_tulia01_2pcfoundhimab: #“Yeah. That was pretty damn stupid of me. From now on, I’ll stay on the roads.”
                                    menu:
                                        '“Well, at least your bravery didn’t go to waste! {color=#f6d6bd}Asterion’s{/color} family won’t be happy to hear the news, but they’ll be able to move on now. Good job, it would be a waste to lose your potential. Better take care of yourself.”
                                        '
                                        '“That’s the plan.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the plan.”')
                                            jump peltnorth_tulia01_03gettingreward
            '“He bit off more than he could chew. Now his kids will face the consequences.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He bit off more than he could chew. Now his kids will face the consequences.”')
                menu:
                    '“My thoughts exactly. Did he do all this for his own ambitions, or to help his family?” She scratches the back of her head. Her hair has started to show. “Still, he made a mistake.”
                    '
                    '“Well, not necessarily. We can’t judge the decision on the outcome alone. He might have had a good reason to think it would all play out as he intended.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, not necessarily. We can’t judge the decision on the outcome alone. He might have had a good reason to think it would all play out as he intended.”')
                        $ asterion_found_pcthought = "believeshewasrational"
                        menu:
                            '“You {i}may{/i} be right. Even healthy thoughts lead us to suffering.”
                            '
                            '“Exactly.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Exactly.”')
                                jump peltnorth_tulia01_03gettingreward
                    '“And I almost repeated it. I’ll try to play it safe, from now on.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And I almost repeated it. I’ll try to play it safe, from now on.”')
                        $ asterion_found_pcthought = "readytoplayitsafe"
                        menu:
                            '“Well, at least {i}your{/i} bravery didn’t go to waste! {color=#f6d6bd}Asterion’s{/color} family won’t be happy to hear the news, but thanks to you, they can start to heal. Now we need {i}you{/i} to take care of yourself. You’ve got potential.”
                            '
                            '“That’s the plan.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the plan.”')
                                jump peltnorth_tulia01_03gettingreward
            '“I don’t know what to think. I’d like to know his perspective.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t know what to think. I’d like to know his perspective.”')
                menu:
                    'She sighs. “Well, we can’t read his soul. Let it go, it’s in the past now.”
                    '
                    '“His death seems so... pointless, now.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “His death seems so... pointless, now.”')
                        $ asterion_found_pcthought = "annoyedwithunsolvedmystery"
                        menu:
                            'Her sad eyes betray her nonchalant voice. “The Wright and nature take us without a reason.”
                            '
                            '“I guess.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I guess.”')
                                jump peltnorth_tulia01_03gettingreward
                    '“You’re right. I’ll be fine.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re right. I’ll be fine.”')
                        $ asterion_found_pcthought = "readytoletthemysterygo"
                        menu:
                            '“{color=#f6d6bd}Asterion’s{/color} family won’t be happy to hear the news, but thanks to you, they can start to heal. Now we need {i}you{/i} to take care of yourself. You’ve got potential.”
                            '
                            '“That’s the plan.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the plan.”')
                                jump peltnorth_tulia01_03gettingreward
            '“He made a mistake, that’s all. It has nothing to do with me.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He made a mistake, that’s all. It has nothing to do with me.”')
                menu:
                    '“Just another job for you, isn’t it?”
                    '
                    '“That’s right.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s right.”')
                        $ asterion_found_pcthought = "doesntcareatall"
                        jump peltnorth_tulia01_03gettingreward
                    '“And just another dead traveler.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And just another dead traveler.”')
                        $ asterion_found_pcthought = "doesntcareatall"
                        menu:
                            '“Well, won’t argue with that,” she rests her hand on the hilt of her sword. “Though I doubt his family will share your sentiment.”
                            '
                            '“Fair enough.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fair enough.”')
                                jump peltnorth_tulia01_03gettingreward
            '“Honestly? I may end up the same way.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Honestly? I may end up the same way.”')
                menu:
                    'She scratches the back of her head. Her hair has started to show. “How come?”
                    '
                    '“He spent his time in constant pursuit, everywhere a stranger, barely a pawn maneuvering between the intrigues of others. I bet he tried to squeeze as much from every moment as he could, facing guilt whenever he took a day off. A soul lost in calculations and dreams, free, but never present, lacking balance. No wonder he pushed himself so much that he finally broke. We are sitting at a feast of options, but with every meal tasting like dust, making us only more hungry.” (disabled)':
                        pass
                    '“Oh, I’m just thinking out loud.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Oh, I’m just thinking out loud.”')
                        $ asterion_found_pcthought = "pchasseriousdoubts"
                        jump peltnorth_tulia01_03gettingreward

    label peltnorth_tulia01_03gettingreward:
        menu:
            'She stretches out, heads upstairs, and brings you a few items. There’s enough of them to make her stumble, but she covers her embarrassment with a chuckle. “Well, this is my part of the deal!”
            \n\nShe rests two weapons against the table. You remove the cloth wrapped around the spear’s head - it’s sharp, made of steel. The shaft is made of thick oak - {color=#f6d6bd}Asterion{/color} must have had pretty large hands - and is partially covered with linen cord and leather straps, intended to support one’s grip.
            \n\nThe bow is currently unstrung, but it would be about five feet long. The polished red oak shines in the light. You wonder if you’re too old to learn how to shoot such a weapon.
            '
            'I look at the things on the table.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the things on the table.')
                $ item_asterionbow = 1
                $ item_asterionspear = 1
                $ item_asterionpurse = 1
                $ item_asterionwine = 1
                $ item_smallhealingpotion += 3
                if pc_class == "scholar":
                    $ custom1 = "There are two letters engraved on its surface: “NB.”"
                else:
                    $ custom1 = "There are two letters engraved on its surface, unknown to you."
                menu:
                    'The leather pouch must be decades old. You shake it - there’s a few bones inside, but also something made of metal.
                    \n\nYou reach for the earthenware bottles. Three of them are very similar to each other, as small as your fist, and all are sealed with wax, though the tiny sticks in them will enable swift opening. {color=#f6d6bd}Tulia{/color} explains that they contain small amounts of a healing concoction.
                    \n\nThe last bottle is much larger. [custom1]
                    \n\n{color=#f6d6bd}The soldier{/color} has no idea what it is.
                    '
                    'Finding space for it all among my bundles won’t be easy.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Finding space for it all among my bundles won’t be easy.')
                        if quest_asterion_description00lies:
                            jump peltnorth_tulia01_03gettingreward_lie
                        else:
                            jump peltnorth_tulia01_questfinishedcongrats

    label peltnorth_tulia01_questfinishedcongrats:
        $ quest_asterion = 2
        $ renpy.notify("Quest completed: Find the Roadwarden\nYou received Asterion’s equipment.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Find the Roadwarden. You received Asterion’s equipment.{/i}')
        $ quest_asterion_description00goodresult = "I collected my reward from {color=#f6d6bd}Tulia{/color}."
        $ can_leave = 1
        if peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day:
            $ can_rest = 1
        else:
            $ can_rest = 0
        $ can_items = 1
        if quarters <= (world_daylength-5):
            show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
        else:
            show areapicture peltnorth01 at basicfade behind peltnorthbronzerod
        if eudocia_bronzerod_rodin_peltnorth:
            show peltnorthbronzerod at basicfade
        if tutorial_selling == 1:
            $ tutorial_selling = 2
        if tutorial_selling2 == 1:
            $ tutorial_selling2 = 2
        if quarters >= 32 and quarters < (world_daylength-12):
            $ peltnorth_armorer_description = "You hear the sounds of work coming from the armorer’s workshop."
        else:
            $ peltnorth_armorer_description = "At this hour, the armorer’s workshop is closed."
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level1 and not iason_friendship_moneybonus_level1_given:
            $ iason_friendship_moneybonus_level1_given = 1
            $ dalit_friendship += 1
            $ iason_friendship += 1
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level2 and not iason_friendship_moneybonus_level2_given:
            $ iason_friendship_moneybonus_level2_given = 1
            $ dalit_friendship += 2
            $ iason_friendship += 2
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level3 and not iason_friendship_moneybonus_level3_given:
            $ iason_friendship_moneybonus_level3_given = 1
            $ dalit_friendship += 3
            $ iason_friendship += 3
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level4 and not iason_friendship_moneybonus_level4_given:
            $ iason_friendship_moneybonus_level4_given = 1
            $ dalit_friendship += 4
            $ iason_friendship += 4
        if iason_friendship_moneybonus_points >= iason_friendship_moneybonus_level5 and not iason_friendship_moneybonus_level5_given:
            $ iason_friendship_moneybonus_level5_given = 1
            $ dalit_friendship += 5
            $ iason_friendship += 5
        if tutorial_selling == 1:
            $ tutorial_selling = 2
        if tutorial_selling2 == 1:
            $ tutorial_selling2 = 2
        if world_endmode:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            menu:
                '{color=#f6d6bd}[horsename]{/color} spares you a glance as you reach toward your bundles, but then returns to its nap.
                \n\nYou take a deep breath. You could have taken the easy way out, but you didn’t. Your back, buttocks, and legs are aching from the long journey. The first night you spent on the peninsula feels like a lifetime ago.
                \n\nYet you’re still here. And who knows - maybe even rich.
                '
                'I go back to {color=#f6d6bd}Tulia{/color}.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to {color=#f6d6bd}Tulia{/color}.')
                    show areapicture peltnorth01inside at basicfade
                    hide peltnorthbronzerod
                    jump peltnorth_tulia01regularquestions
        else:
            menu:
                '{color=#f6d6bd}[horsename]{/color} spares you a glance as you reach toward your bundles, but then returns to its nap.
                \n\nYou take a deep breath. You could have taken the easy way out, but you didn’t. Your back, buttocks, and legs are aching from the long journey. The first night you spent on the peninsula feels like a lifetime ago.
                \n\nYet you’re still here. And who knows - maybe even rich.
                '
                'I go back to the inn.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the inn.')
                    jump peltnorth01inside
                'I approach the guards.' ( condition="quarters < (world_daylength-4)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the guards.')
                    if dalit_firsttime:
                        jump peltnorthtalkingwithguards01
                    else:
                        $ dalit_firsttime = 1
                        jump dalit_firsttime01
                'The guards are currently on watch. They won’t talk with me. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
                    pass
                'I head to the armorer.' ( condition="quarters >= 32 and quarters < (world_daylength-12)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the armorer.')
                    if peltnorth_armorer_firsttime:
                        jump peltnorthtalkingwitharmorer01
                    else:
                        $ peltnorth_armorer_firsttime = 1
                        jump peltnorthtalkingwitharmorerfirsttime01
                'The armorer is nowhere in sight. (disabled)' ( condition="quarters < 32 or quarters >= (world_daylength-12)" ):
                    pass
                'I go to the well.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the well.')
                    jump peltnorthwell01
                'I should go outside and forage for berries.' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters <= (world_daylength-4) and not item_peltnorthberries" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should to outside and forage for berries.')
                    jump peltnorthleftoversquestforberries02
                'It’s too dark to gather the berries right now. (disabled)' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters > (world_daylength-4) and not item_peltnorthberries" ):
                    pass
                'I shouldn’t try to gather the berries without the hook. (disabled)' ( condition="iason_food_berries == 1 and not item_peltnorthberrytools and not item_peltnorthberries" ):
                    pass

    label peltnorth_tulia01asterion_found01_alt:
        menu:
            'She ponders for a bit, looking at the oven. “So, what do you make of it? Not the brightest death I could wish for someone.”
            '
            '“He knew the danger, but took the risk anyway. A fair end to his journey.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He knew the danger, but took the risk anyway. A fair end to his journey.”')
                menu:
                    '“You two had this in common. I can’t believe I joined you on a wild island.” Her smile turns into a chuckle. “We’re lucky to still be here!”
                    '
                    '“Risk-taking is the only way to get somewhere in life.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Risk-taking is the only way to get somewhere in life.”')
                        $ asterion_found_pcthought = "readyforanadventure"
                        jump peltnorth_tulia01_2pcfoundhimaa_alt
                    '“Yeah... From now on, I’ll stay on the roads.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah... From now on, I’ll stay on the roads.”')
                        $ asterion_found_pcthought = "readytoplayitsafe"
                        jump peltnorth_tulia01_2pcfoundhimab_alt
                    'I smirk. “Says the gal who spent half a year in this shithole.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smirk. “Says the gal who spent half a year in this shithole.”')
                        menu:
                            '“Ha, I know!” Her laughter starts strong, but is cut off by a harsh cough. “I trusted my group too much, but that’s still a safer bet than risking your head.”
                            '
                            '“Risk-taking is the only way to get somewhere in life.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Risk-taking is the only way to get somewhere in life.”')
                                $ asterion_found_pcthought = "readyforanadventure"
                                label peltnorth_tulia01_2pcfoundhimaa_alt: #“Risk-taking is the only way to get somewhere in life.”
                                    menu:
                                        '“Spoken like a true adventurer,” she scratches the back of her head. Her hair has started to show. “And you’re not going to stay here for long. A roadwarden who wants to stay alive needs to know how to say {i}no{/i} to their ambitions... Yet I bet that once you get used to these roads, you’ll get bored of them.”
                                        '
                                        '“Well, that’s surely possible.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, that’s surely possible.”')
                                            jump peltnorth_tulia01_03gettingreward
                            '“Yeah... From now on, I’ll stay on the roads.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah... From now on, I’ll stay on the roads.”')
                                $ asterion_found_pcthought = "readytoplayitsafe"
                                label peltnorth_tulia01_2pcfoundhimab_alt: #“Yeah. That was pretty damn stupid of me. From now on, I’ll stay on the roads.”
                                    menu:
                                        '“Well, at least your bravery didn’t go to waste! {color=#f6d6bd}Asterion’s{/color} family won’t be happy to hear the news, but they’ll be able to move on now. Good job, it would be a waste to lose your potential. Better take care of yourself.”
                                        '
                                        '“That’s the plan.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the plan.”')
                                            jump peltnorth_tulia01_03gettingreward
            '“He bit off more than he could chew. Now his kids will face the consequences.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He bit off more than he could chew. Now his kids will face the consequences.”')
                menu:
                    '“My thoughts exactly. Did he do all this for his own ambitions, or to help his family?” She scratches the back of her head. Her hair has started to show. “Still, he made a mistake.”
                    '
                    '“Well, not necessarily. We can’t judge the decision on the outcome alone. He might have had a good reason to think it would all play out as he intended.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, not necessarily. We can’t judge the decision on the outcome alone. He might have had a good reason to think it would all play out as he intended.”')
                        $ asterion_found_pcthought = "believeshewasrational"
                        menu:
                            '“You {i}may{/i} be right. Even healthy thoughts lead us to suffering.”
                            '
                            '“Exactly.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Exactly.”')
                                jump peltnorth_tulia01_03gettingreward
                    '“And I almost repeated it. I’ll try to play it safe, from now on.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And I almost repeated it. I’ll try to play it safe, from now on.”')
                        $ asterion_found_pcthought = "readytoplayitsafe"
                        menu:
                            '“Well, at least {i}your{/i} bravery didn’t go to waste! {color=#f6d6bd}Asterion’s{/color} family won’t be happy to hear the news, but thanks to you, they can start to heal. Now we need {i}you{/i} to take care of yourself. You’ve got potential.”
                            '
                            '“That’s the plan.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the plan.”')
                                jump peltnorth_tulia01_03gettingreward
            '“I don’t know what to think. I’d like to know his perspective.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t know what to think. I’d like to know his perspective.”')
                menu:
                    'She sighs. “Well, we can’t read his soul. Let it go, it’s in the past now.”
                    '
                    '“His death seems so... pointless, now.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “His death seems so... pointless, now.”')
                        $ asterion_found_pcthought = "annoyedwithunsolvedmystery"
                        menu:
                            'Her sad eyes betray her nonchalant voice. “The Wright and nature take us without a reason.”
                            '
                            '“I guess.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I guess.”')
                                jump peltnorth_tulia01_03gettingreward
                    '“You’re right. I’ll be fine.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re right. I’ll be fine.”')
                        $ asterion_found_pcthought = "readytoletthemysterygo"
                        menu:
                            '“{color=#f6d6bd}Asterion’s{/color} family won’t be happy to hear the news, but thanks to you, they can start to heal. Now we need {i}you{/i} to take care of yourself. You’ve got potential.”
                            '
                            '“That’s the plan.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the plan.”')
                                jump peltnorth_tulia01_03gettingreward
            '“He made a mistake, that’s all. It has nothing to do with me.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He made a mistake, that’s all. It has nothing to do with me.”')
                menu:
                    '“Just another job for you, isn’t it?”
                    '
                    '“That’s right.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s right.”')
                        $ asterion_found_pcthought = "doesntcareatall"
                        jump peltnorth_tulia01_03gettingreward
                    '“And just another dead traveler.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And just another dead traveler.”')
                        $ asterion_found_pcthought = "doesntcareatall"
                        menu:
                            '“Well, won’t argue with that,” she rests her hand on the hilt of her sword. “Though I doubt his family will share your sentiment.”
                            '
                            '“Fair enough.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fair enough.”')
                                jump peltnorth_tulia01_03gettingreward
            '“Honestly? I may end up the same way.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Honestly? I may end up the same way.”')
                menu:
                    'She scratches the back of her head. Her hair has started to show. “How come?”
                    '
                    '“He spent his time in constant pursuit, everywhere a stranger, barely a pawn maneuvering between the intrigues of others. I bet he tried to squeeze as much from every moment as he could, facing guilt whenever he took a day off. A soul lost in calculations and dreams, free, but never present, lacking balance. No wonder he pushed himself so much that he finally broke. We are sitting at a feast of options, but with every meal tasting like dust, making us only more hungry.” (disabled)':
                        pass
                    '“Oh, I’m just thinking out loud.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Oh, I’m just thinking out loud.”')
                        $ asterion_found_pcthought = "pchasseriousdoubts"
                        jump peltnorth_tulia01_03gettingreward

label peltnorth_tulia01_asterionlieALL:
    label peltnorth_tulia01_asterionlie:
        $ quest_asterion_description00lies = "I wasn’t able to find {color=#f6d6bd}Asterion{/color} on time, but I lied to {color=#f6d6bd}Tulia{/color} to get my reward."
        $ pc_lies += 2
        menu:
            'She flashes you a wide smile.
            '
            '(lie) “He’s dead. Devoured by monsters during a routine patrol.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “He’s dead. Devoured by monsters during a routine patrol.”')
                $ asterion_lie = "monsters"
                menu:
                    'She nods. “Yet another soul strangled by the woods. What sort of creature caught him?”
                    \n\nYou share a simple story about a lonely stranger assaulted by a pack of wolves, torn to pieces and dragged away from the main road. You describe the broken spear, the rusty mail, the pants which surely belonged to a shell of short stature. {color=#f6d6bd}Tulia{/color} listens patiently, without delving into details.
                    '
                    '“It was nothing more than an accident.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It was nothing more than an accident.”')
                        jump peltnorth_tulia01_03gettingreward
            '(lie) “He was murdered by unknown highwaymen. They left the peninsula soon after.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “He was murdered by unknown highwaymen. They left the peninsula soon after.”')
                $ asterion_lie = "bandits"
                menu:
                    'She sighs. “They had enough guts to rob a roadwarden... I’m lucky they didn’t come after me as well. Any clues who they are?”
                    \n\nYou do your best to describe a mediocre group of vagabonds who at one point tried to sell mail and a spear to the locals. Since that day, {color=#f6d6bd}Asterion{/color} hasn’t been seen, dead or alive. {color=#f6d6bd}Tulia{/color} listens patiently, without delving into details.
                    '
                    '“They won’t face justice anytime soon.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “They won’t face justice anytime soon.”')
                        jump peltnorth_tulia01_03gettingreward
            '(lie) “He lives in solitude, in a place I’m not allowed to reveal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “He lives in solitude, in a place I’m not allowed to reveal.”')
                $ asterion_lie = "solitude"
                menu:
                    'Her eyes widen. “Is he mad?”
                    \n\nYou lean into that explanation. According to your tale, the roadwarden sees himself as choking on his own greed and remorse. He’s not easy to find, feeding on berries, frogs, and roots, surrounded by traps. He contemplates nature and the tangled paths of human souls.
                    \n\nShe narrows her eyes, but listens patiently, giving you occasional nods.
                    '
                    '“He had {i}a vision{/i} and won’t allow anyone else to find him. I’d bet the path I took is already blocked.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He had {i}a vision{/i} and won’t allow anyone else to find him. I’d bet the path I took is already blocked.”')
                        jump peltnorth_tulia01_03gettingreward

    label peltnorth_tulia01_03gettingreward_lie:
        $ renpy.notify("You received Asterion’s equipment.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received Asterion’s equipment.{/i}')
        if quarters <= (world_daylength-5):
            show areapicture peltnorth01gateopen at basicfade behind peltnorthbronzerod
        else:
            show areapicture peltnorth01 at basicfade behind peltnorthbronzerod
        if eudocia_bronzerod_rodin_peltnorth:
            show peltnorthbronzerod at basicfade
        if quarters >= 32 and quarters < (world_daylength-12):
            $ peltnorth_armorer_description = "You hear the sounds of work coming from the armorer’s workshop."
        else:
            $ peltnorth_armorer_description = "At this hour, the armorer’s workshop is closed."
        menu:
            '{color=#f6d6bd}[horsename]{/color} is swishing its tail anxiously, looking around. You move your bundles and take a deep breath. You could still look for {color=#f6d6bd}Asterion{/color}, but it’s unlikely you’ll find additional payment. Maybe the officials would appreciate the truth.
            '
            'I want to know what happened to him. I won’t give up on my quest.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to know what happened to him. I won’t give up on my quest.')
                jump leavingthepeltnorth02
            'He may need my help. I still need to find him.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He may need my help. I still need to find him.')
                jump leavingthepeltnorth02
            'Without the reward, I won’t bother. Time to let it go.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Without the reward, I won’t bother. Time to let it go.')
                $ renpy.notify("Quest completed: Find the Roadwarden")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Find the Roadwarden{/i}')
                $ quest_asterion = 3
                if quest_gatheracrew == 1:
                    $ quest_gatheracrew = 3
                $ quest_asterion_description00gaveup = "I’ve decided to give up on this quest."
                jump leavingthepeltnorth02

label peltnorth_tulia01asterion_highislandALL:
    label peltnorth_tulia01asterion_highisland01:
        $ tulia_about_highisland = 1
        $ minutes += 5
        if tulia_about_bandits_indebt:
            $ tulia_about_highisland_recruited = 1
            menu:
                'She breathes deeply, and her eyes are cold. “After all, I {i}owe{/i} you one. But I hope you know better than to hunt beasts there.”
                '
                '“I’ll stop by when I need you.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll stop by when I need you.”')
                    $ custom1 = "“If you must.”"
                    jump peltnorth_tulia01regularquestionsafter
        else:
            menu:
                'She gives you a long look. “I mostly forgot about {color=#f6d6bd}Asterion{/color}. And I’ve had my share of beasts already.”
                '
                '“The officials would appreciate your report from the island.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The officials would appreciate your report from the island.”')
                    $ custom1 = "“They can shove it,” she leans away. “Unless they’re going to send me to a village with tall walls, I’m about to quit.”\n\n"
                    jump peltnorth_tulia01asterion_highisland01a
                '“Your help may save his life.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your help may save his life.”')
                    $ tulia_friendship += 1
                    $ custom1 = "She sighs, then starts to rub her temples. “I guess.” "
                    jump peltnorth_tulia01asterion_highisland01a
                '“You’re missing out on a real adventure. We may find a treasure, or ancient ruins.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re missing out on a real adventure. We may find a treasure, or ancient ruins.”')
                    $ custom1 = "“Adventures are overrated,” she leans away, “and from my experience, they give you more scars than meals.”\n\n"
                    jump peltnorth_tulia01asterion_highisland01a
                '“You’ve got anything better to do?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ve got anything better to do?”')
                    $ tulia_friendship -= 1
                    $ custom1 = "“{i}Not dying{/i} is high on my list,” she raises her chin, and her eyes turn cold. “Be so kind as to keep yourself in one piece as well so we can keep each other safe on our way to the city.”\n\n"
                    jump peltnorth_tulia01asterion_highisland01a

    label peltnorth_tulia01asterion_highisland01alt:
        $ tulia_about_highisland_recruited = 1
        menu:
            'She breathes deeply, and her eyes are cold. “Fine. But I hope you know better than to hunt beasts there.”
            '
            '“I’ll stop by when I need you.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll stop by when I need you.”')
                $ custom1 = "“If you must.”"
                jump peltnorth_tulia01regularquestionsafter

    label peltnorth_tulia01asterion_highisland01a:
        if (tulia_friendship+appearance_charisma) >= tulia_about_highisland_recruited_threshold:
            label peltnorth_tulia01asterion_highisland03:
                $ tulia_about_highisland_recruited = 1
                menu:
                    '[custom1]A long pause. “Fine, fine. I don’t know if you’re trustworthy, but you’re capable, that’s for sure. Count me in.”
                    '
                    '“Thanks, {color=#f6d6bd}Tulia{/color}.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks, {color=#f6d6bd}Tulia{/color}.”')
                        $ custom1 = "She playfully hits your shoulder, then gives you a gentle smile. “You’re welcome.”"
                        jump peltnorth_tulia01regularquestionsafter
                    '“I’ll stop by when I need you.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll stop by when I need you.”')
                        $ custom1 = "“I’ll be ready.”"
                        jump peltnorth_tulia01regularquestionsafter
        else:
            menu:
                '[custom1]A short pause. “I can’t do it. Are you really this sick of the roads? I don’t plan to give you a palace made of dragon bones, you know.”
                '
                '“Summer is almost over. We should soon travel back to the city.”' if not tulia_about_returntocity and not world_endmode:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Summer is almost over. We should soon travel back to the city.”')
                    $ tulia_about_returntocity = 1
                    $ custom1 = "She shrugs. “Well, if any city rat is going to criticize me for getting out of here before the end of my {i}watch{/i}, they can jump into the sea, for all I care. I can head back whenever.”"
                    jump peltnorth_tulia01regularquestionsafter
                '[[{color=#f6d6bd}Finish your adventure.{/color}] “Are you all packed and ready?”' if tulia_about_returntocity or world_endmode:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you all packed and ready?”')
                    jump peltnorth_tulia01about_returntocity02
                #######
                '“I found {color=#f6d6bd}Asterion{/color}.”' if asterion_found and not quest_asterion_description00goodresult and not quest_asterion_description00lies and not tulia_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news about {color=#f6d6bd}Asterion{/color}.”')
                    jump peltnorth_tulia01asterion_found01
                '“About {color=#f6d6bd}Asterion{/color}...”' if asterion_found and not quest_asterion_description00goodresult and not quest_asterion_description00lies and tulia_highisland_joined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Asterion{/color}...”')
                    jump peltnorth_tulia01asterion_found01_alt
                '(lie) “I found {color=#f6d6bd}Asterion{/color}.”' if not asterion_found and not quest_asterion_description00goodresult and not quest_asterion_description00lies:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Asterion{/color}.”')
                    jump peltnorth_tulia01_asterionlie
                'I tell her about {color=#f6d6bd}High Island{/color}. “Want to join my expedition?”' if quest_gatheracrew == 1 and not tulia_about_highisland and not world_endmode and not quest_asterion_description00goodresult and not quest_asterion_description00lies:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell her about {color=#f6d6bd}High Island{/color}. “Want to join my expedition?”')
                    jump peltnorth_tulia01asterion_highisland01
                '“I’m still looking for a crew.”' if quest_gatheracrew == 1 and tulia_about_highisland and not tulia_about_highisland_recruited and (tulia_friendship+appearance_charisma) >= tulia_about_highisland_recruited_threshold and not world_endmode:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m still looking for a crew.”')
                    jump peltnorth_tulia01asterion_highisland02
                '“I’m still looking for a crew. It’s an opportunity for you to pay off your debt.”' if quest_gatheracrew == 1 and tulia_about_highisland and not tulia_about_highisland_recruited and tulia_about_bandits_indebt and (tulia_friendship+appearance_charisma) < tulia_about_highisland_recruited_threshold and not world_endmode:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m still looking for a crew. It’s an opportunity for you to pay off your debt.”')
                    jump peltnorth_tulia01asterion_highisland01alt
                'She doesn’t trust me enough to join my crew. (disabled)' if quest_gatheracrew == 1 and tulia_about_highisland and not tulia_about_highisland_recruited and (tulia_friendship+appearance_charisma) < tulia_about_highisland_recruited_threshold and not world_endmode:
                    pass
                #######
                '“I’ve been to your camp. It’s as good as gone.”' if militarycamp_destroyed_firsttime and not tulia_about_troll:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to your camp. It’s as good as gone.”')
                    $ tulia_about_troll = 1
                    $ tulia_friendship += 1
                    $ custom1 = "You explain that the broken entrance is in worse shape than she remembers, and that the scavengers are going to have a feast for a few days, if not more. She rubs the top of her head with her entire palm, glancing at two hunters who just entered the room.\n\n“No longer my problem,” she says to herself, but then meets your eyes and lets out a sorrowful chuckle. “Quite a monster we knocked down, wasn’t it?”"
                    jump peltnorth_tulia01regularquestionsafter
                '“Tell me about the troll attack.”' if not tulia_about_troll_attack:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about the troll attack.”')
                    $ tulia_about_troll_attack = 1
                    $ custom1 = "“There isn’t much to say. It came in the early hours, we threw and shot anything we could at it. After it broke through the gate, I had one last arrow left. My {i}subordinate{/i}” her voice is bitter, “gave me time to aim. And now he’s gone.”"
                    jump peltnorth_tulia01regularquestionsafter
                '“Did you manage to burn the other soldier?”' if tulia_about_troll_attack and not tulia_about_troll_attack2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you manage to burn the other soldier?”')
                    $ tulia_about_troll_attack2 = 1
                    $ custom1 = "The sorrow in her eyes makes the shake of her head redundant."
                    jump peltnorth_tulia01regularquestionsafter
                ######
                '“Do you still have my reward? Or is it back at the camp?”' if not quest_asterion_description00goodresult and not quest_asterion_description00lies and not tulia_about_stillhavingreward:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to your camp. It’s as good as gone.”')
                    $ tulia_about_stillhavingreward = 1
                    $ custom1 = "After a brief scowl, she looks down and shakes her head, snickering weakly. “I knew you would ask me that. Yeah, it’s all there. I took everything of value with me.”"
                    jump peltnorth_tulia01regularquestionsafter
                #######
                '“The priest of {color=#f6d6bd}White Marshes{/color} has agreed to release the dead shells. Problem solved.”' if orentius_convinced and not tulia_about_nomoreundead:
                    jump peltnorth_tulia_about_nomoreundead01
                '“The priest of {color=#f6d6bd}White Marshes{/color} is gone, and so are his undead. Problem solved.”' if orentius_banished and not tulia_about_nomoreundead:
                    jump peltnorth_tulia_about_nomoreundead02
                '“The village of {color=#f6d6bd}White Marshes{/color} is no more. The North will now struggle with a large group of undead.”' if whitemarshes_destroyed and not tulia_about_nomoreundead:
                    jump peltnorth_tulia_about_nomoreundead03
                #######
                '“I found this wax tablet. Do you recognize it?”' if not tulia_about_tablet and item_asteriontablet:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this wax tablet. Do you recognize it?”')
                    $ tulia_about_tablet += 1
                    jump peltnorth_tulia01tulia_about_tablet01
                #######
                '“Guess what? I met with {color=#f6d6bd}Caius{/color}.”' if foragers_caius_heardabout and foragers_caius_spokento and not tulia_about_caius_spokento:
                    jump peltnorth_tulia01tulia_about_caius_spokento01
                #######
                '“Did you ever enter the road leading through the heart of the woods?”' if shortcut_pcknowsabout and not tulia_about_shortcut:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you ever enter the road leading through the heart of the woods?”')
                    $ tulia_about_shortcut += 1
                    jump peltnorth_tulia01tulia_about_shortcut01
                #######
                '“Do you have any idea about what happened to the ruined village in the west?”' if ruinedvillage_firsttime == 1 and not ruinedvillage_confront_can and not ruinedvillage_truth and not tulia_about_ruinedvillage:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea about what happened to the ruined village in the west?”')
                    $ tulia_about_ruinedvillage += 1
                    if quest_ruins == 1 and not quest_ruins_description01:
                        $ renpy.notify("Journal updated: The Ruined Village")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                    $ quest_ruins_description01 = "I heard that the village was destroyed almost ten years ago."
                    jump peltnorth_tulia01tulia_about_ruinedvillage01
                #######
                '“Have you ever encountered the bandits from the north?”' if banditshideout_bandits_pchearedabout and not tulia_about_bandits1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever encountered the bandits from the north?”')
                    $ tulia_about_bandits1 += 1
                    jump peltnorth_tulia01tulia_about_bandits01
                '“Nice acting, but I spoke with {color=#f6d6bd}Glaucia{/color}. You’re working with her.”' if tulia_about_bandits1 and description_tulia05 and not tulia_about_bandits2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Nice acting, but I spoke with {color=#f6d6bd}Glaucia{/color}. You’re working with her.”')
                    $ tulia_about_bandits2 += 1
                    jump peltnorth_tulia01tulia_about_bandits02
                '“Come on, now. This is the only pass through {color=#f6d6bd}Hag Hills{/color}. Recently, there was a caravan with tools and spices that was taken by force, to be sold for ransom. {i}Someone{/i} told them to turn east, right into the band’s trap. You want me to believe you bear no responsibility, and saw nothing?”' if tulia_about_bandits2 and glaucia_about_lostmerchants_trail and not tulia_about_bandits3:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Come on, now. This is the only pass through {color=#f6d6bd}Hag Hills{/color}. Recently, there was a caravan with tools and spices that was taken by force, to be sold for ransom. {i}Someone{/i} told them to turn east, right into the band’s trap. You want me to believe you bear no responsibility, and saw nothing?”')
                    $ tulia_about_bandits3 += 1
                    jump peltnorth_tulia01tulia_about_bandits03
                #######
                'I glance at {color=#f6d6bd}the bandit{/color}. “You know him?”' if not tulia_about_nonamebandit and tulia_about_bandits2 and shortcut_bandit_identity and shortcut_darkforest_bandit_inpeltnorth:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at {color=#f6d6bd}the bandit{/color}. “You know him?”')
                    $ tulia_about_nonamebandit = 1
                    jump peltnorth_tulia01tulia_about_nonamebandit01
                #######
                '“What was your squad’s mission?”' if not tulia_about_hermission:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What was your squad’s mission?”')
                    $ tulia_about_hermission += 1
                    jump peltnorth_tulia01regularadditionalquestion03
                #######
                'She doesn’t trust me enough to tell me about her squad’s mission. (disabled)' if tulia_about_hermission and not description_tulia04 and (tulia_friendship+appearance_charisma) < 3:
                    pass
                #######
                '“About your squad’s mission...”' if tulia_about_hermission and not description_tulia04 and (tulia_friendship+appearance_charisma) >= 3:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What was your squad’s mission?”')
                    jump peltnorth_tulia01regularadditionalquestion03p02
                #######
                'I head to {color=#f6d6bd}the innkeep{/color}.' if tulia_pelt_needstotalkwithiason and not world_endmode:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to {color=#f6d6bd}the innkeep{/color}.')
                    $ can_rest = 0
                    $ can_items = 0
                    $ tulia_pelt_needstotalkwithiason = 0
                    jump peltnorth_tulia_meeting_firsttime03
                'I take another look at the main hall.' if not tulia_pelt_needstotalkwithiason and peltnorth_bonusnpcs > 0 and not world_endmode:
                    $ can_rest = 0
                    $ can_leave = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                    jump peltnorth01insidechoosenpc
                'I go outside.' if not tulia_pelt_needstotalkwithiason and not world_endmode:
                    $ can_rest = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                    jump leavingthepeltnorth
                'It’s time to leave the peninsula behind. (disabled)' if world_endmode:
                    pass

    label peltnorth_tulia01asterion_highisland02:
        $ custom1 = ""
        jump peltnorth_tulia01asterion_highisland03

label peltnorth_tulia01about_returntocity02:
    $ tulia_about_returntocity = 1
    if quarters <= (((world_daylength/2)+11)+4):
        $ custom1 = "You look outside. It’s early enough for you to reach the settlements on the other side of {color=#f6d6bd}Hag Hills{/color}."
    else:
        $ custom1 = "You look outside. It’s too late to ride to the other side of {color=#f6d6bd}Hag Hills{/color}, but you could leave first thing in the morning."
    menu:
        'She rests her hands on her knees, then straightens up. “I am if you are.”
        \n\n[custom1]
        '
        'I keep staring at the exit. There may be another way.' if (not tulia_about_returntocity_alt and quest_ruins_choice == "thais_alliance") or (not tulia_about_returntocity_alt and pc_goal_iwantnewlife_creeks) or (not tulia_about_returntocity_alt and pc_goal_iwantnewlife_monastery) or (not tulia_about_returntocity_alt and glaucia_invitingtojoin) or (not tulia_about_returntocity_alt and pc_goal_iwantnewlife_galerocks):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I keep staring at the exit. There may be another way.')
            jump peltnorth_tulia01about_returntocity03
        '“Let’s introduce you to {color=#f6d6bd}[horsename]{/color}. You’re going to spend a lot of time together.”' if pc_likeshorsename:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s introduce you to {color=#f6d6bd}%s{/color}. You’re going to spend a lot of time together.”' %horsename)
            jump hovlavan_road01
        '“Let’s take your bundles outside.”' if not pc_likeshorsename:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s take your bundles outside.”')
            jump hovlavan_road01
        'I nod to her. “I’m not going to join you.”' if tulia_about_returntocity_alt:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to her. “I’m not going to join you.”')
            jump peltnorth_tulia01about_returntocity04
        'Maybe later.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe later.')
            jump peltnorth_tulia01regularquestions
        'With no tribe willing to allow me to stay with them, all I’ve got left is to head back to the city. (disabled)' if not (not tulia_about_returntocity_alt and quest_ruins_choice == "thais_alliance") and not (not tulia_about_returntocity_alt and pc_goal_iwantnewlife_creeks) and not (not tulia_about_returntocity_alt and pc_goal_iwantnewlife_monastery) and not (not tulia_about_returntocity_alt and glaucia_invitingtojoin) and not (not tulia_about_returntocity_alt and pc_goal_iwantnewlife_galerocks):
            pass


    label peltnorth_tulia01about_returntocity03:
        $ tulia_about_returntocity_alt = 1
        menu:
            'There’s only a few steps between you and the door, and a few more between it and {color=#f6d6bd}[horsename]{/color}. You can already tell what birds would be sitting on the top of the wall, what rumors you’d hear from the guards, what smells would hit you no matter which direction you’d travel. 
            \n\nYou {i}could{/i} just walk away. Let the merchants handle things on their own.
            '
            'It would be a betrayal.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It would be a betrayal.')
                menu:
                    'You’re not representing the army, at least not officially, so you wouldn’t get labeled as a deserter.
                    \n\nStill, you’d sabotage everything you’ve done for the city. You could never return home, and once the guild learns of your presence here, you can expect they’d put a bounty on your head. But if your stance in the North is strong enough, the locals could protect you from the guild’s wrath.
                    '
                    'Would the locals even accept me?':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Would the locals even accept me?')
                        $ custom1 = ""
                        $ custom2 = ""
                        $ custom3 = ""
                        $ custom4 = ""
                        $ custom5 = ""
                        $ custom6 = ""
                        $ custom7 = ""
                        $ custom8 = ""
                        $ custom9 = ""
                        $ custom10 = ""
                        if quest_ruins_choice == "thais_defeated":
                            $ custom1 = "As {color=#f6d6bd}Thais{/color} is awaiting her trial, you doubt that the rest of her neighbors would be too keen on negotiating with the cityfolk. Despite their mixed feelings toward you, you’d likely stay on their good side."
                        elif (quest_ruins_choice == "thais_alliance" and item_thaisletter_opened) or (quest_ruins_choice == "thais_alliance" and item_thaisletter):
                            $ custom1 = "Your alliance with {color=#f6d6bd}Thais{/color} may help you avoid her anger, but knowing her plans in regards to the city, you doubt she’s going to be too happy about your sudden change of mind."
                        elif quest_ruins_choice == "thais_alliance":
                            $ custom1 = "Your alliance with {color=#f6d6bd}Thais{/color} may help you convince her to keep you around, though you’re not sure how much of an asset to her you’d be without the guild’s backing."
                        elif item_thaisletter_opened or item_thaisletter:
                            if quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                                $ custom1 = "Considering your recent conflict with {color=#f6d6bd}Thais{/color}, she may not be too eager to forgive you for failing to deliver her letter to the members of the guild. You’ll likely have to stay away from {color=#f6d6bd}Howler’s{/color}, unless you have no other choice."
                            else:
                                $ custom1 = "You were meant to deliver {color=#f6d6bd}Thais’{/color} letter to the members of the guild, but you don’t expect her ire to last for more than a few seasons."
                        elif quest_ruins_choice == "thais_won" or quest_ruins_choice == "thais_alliance_fail":
                            $ custom1 = "Considering your recent conflict with {color=#f6d6bd}Thais{/color}, you’ll likely have to stay away from {color=#f6d6bd}Howler’s{/color}, unless you have no other choice. Without the city’s backing to protect you, she’d be free to punish you however she wants."
                        elif howlersdell_firsttime:
                            $ custom1 = "You don’t expect to find much support from the people of {color=#f6d6bd}Howler’s Dell{/color}."
                        else:
                            $ custom1 = ""
                        if pc_goal_iwantnewlife_monastery:
                            $ custom2 = "You were promised a spot in {color=#f6d6bd}the monastery{/color}, if you were to seek it. You’ll likely stay on the monks’ good side, no matter what you decide."
                        elif quest_oldpagossupport == 2:
                            $ custom2 = "The people of {color=#f6d6bd}Old Págos{/color} expect you to represent their cause in the city, but seeing their own hesitancy, you assume they would accept your call."
                        elif quest_healingtheplague == 2:
                            $ custom2 = "The people of {color=#f6d6bd}Old Págos{/color} will likely accept your presence. Your heroic deeds won’t be easily forgotten."
                        elif monastery_firsttime:
                            $ custom2 = "You don’t expect the monks to care much about your presence."
                        elif oldpagos_firsttime:
                            $ custom2 = "You don’t expect the people of {color=#f6d6bd}Old Págos{/color} to care much about your presence."
                        else:
                            $ custom2 = ""
                        if custom1 != "" and custom2 != "":
                            $ custom6 = "\n\n"
                        if pc_goal_iwantnewlife_creeks and quest_creekssupport == 2:
                            $ custom3 = "Knowing how the tribe of {color=#f6d6bd}Creeks{/color} reacted to the results of their vote, you’re sure they’ll be relieved to see your quick return."
                        elif quest_creekssupport == 2:
                            $ custom3 = "Knowing how the tribe of {color=#f6d6bd}Creeks{/color} reacted to the results of their vote, you may be able to bring them to your side, despite abandoning your responsibilities."
                        elif pc_goal_iwantnewlife_creeks:
                            $ custom3 = "Since you were already invited to stay with the tribe of {color=#f6d6bd}Creeks{/color}, you’re sure they’ll be happy to see your quick return."
                        elif quest_creekssupport == 3:
                            $ custom3 = "Since the tribe of {color=#f6d6bd}Creeks{/color} doesn’t care much about collaborating with the city in the first place, you doubt they’re going to be bothered by your return."
                        elif creeks_firsttime:
                            $ custom3 = "You don’t expect to find much support in {color=#f6d6bd}Creeks{/color}."
                        else:
                            $ custom3 = ""
                        if (custom2 != "" and custom3 != "") or (custom1 != "" and custom2 == "" and custom3 != ""):
                            $ custom7 = "\n\n"
                        if pc_goal_iwantnewlife_galerocks and quest_galerockssupport == 2:
                            $ custom4 = "After the effort you put into convincing the council of {color=#f6d6bd}Gale Rocks{/color} to begin the negotiations with {color=#f6d6bd}Hovlavan{/color}, you’ll surely be met with some surprised glances at the village, but considering the recent trust they’ve shown you, you should be able to explain yourself."
                        elif quest_galerockssupport == 2:
                            $ custom4 = "After the effort you put into convincing the council of {color=#f6d6bd}Gale Rocks{/color} to begin the negotiations with {color=#f6d6bd}Hovlavan{/color}, you’ll surely be met with some surprised glances at the village."
                        elif pc_goal_iwantnewlife_galerocks:
                            $ custom4 = "After the recent invitation you received from the council of {color=#f6d6bd}Gale Rocks{/color}, you expect them to take you back with no questions asked."
                        elif quest_galerockssupport == 3 or quest_galerockssupport == 4:
                            $ custom3 = "As the council of {color=#f6d6bd}Gale Rocks{/color} have closed their village to the city’s influence, you may struggle to convince them to work with an outsider."
                        elif galerocks_firsttime:
                            $ custom4 = "The people of {color=#f6d6bd}Gale Rocks{/color} don’t seem too interested in working with an outsider."
                        else:
                            $ custom4 = ""
                        if (custom3 != "" and custom4 != "") or (custom1 != "" and custom2 == "" and custom3 == "" and custom4 != "") or (custom2 != "" and custom3 == "" and custom4 != ""):
                            $ custom8 = "\n\n"
                        if glaucia_invitingtojoin:
                            $ custom5 = "If nothing else, you were invited to join {color=#f6d6bd}Glaucia{/color}. Her band may be crude, but your presence there could point them in a less harmful direction."
                        elif glaucia_about_galerocksdecision_liedto:
                            $ custom5 = "Remembering the lie you sold to {color=#f6d6bd}Glaucia{/color}, staying around {i}her{/i} woods may get a bit risky."
                        else:
                            $ custom5 = ""
                        if (custom4 != "" and custom5 != "") or (custom1 != "" and custom2 == "" and custom3 == "" and custom4 == "" and custom5 != "") or (custom2 != "" and custom3 == "" and custom4 == "" and custom5 != "") or (custom3 != "" and custom4 == "" and custom5 != ""):
                            $ custom9 = "\n\n"
                        menu:
                            '[custom1][custom6][custom2][custom7][custom3][custom8][custom4][custom9][custom5]
                            '
                            'I was meant to take my savings back to the city, help my sibling...' if pc_goal == "ineedmoney":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to take my savings back to the city, help my sibling...')
                                if coins >= 200 or (pc_goal_lost100coins and coins >= 100) or (pc_goal_lost100coins and item_asterionwine and item_asterionwine_pcknows_2) or (coins >= 100 and item_asterionwine and item_asterionwine_pcknows_2):
                                    $ custom1 = "The tremendous wealth you’ve gathered should be just enough to support the one you were meant to save.\n\n{color=#f6d6bd}Tulia{/color} shoots you an impatient look. You could escort her close to the city gates so that she can bring the soul you care about to you. And if the soldier were to ask you for something in return... You could spare her some pieces of extra equipment. It should be enough."
                                elif pc_goal_lost100coins or coins >= 100 or (item_asterionwine and item_asterionwine_pcknows_2):
                                    $ custom1 = "Without the pay you were meant to get from the guild, you can’t gather enough on your own. But maybe you could bring the soul you care about here, to be together with you?\n\n{color=#f6d6bd}Tulia{/color} shoots you an impatient look. You could escort her close to the city gates so that she can bring the soul you care about to you. And if the soldier were to ask you for something in return... You could spare her some pieces of extra equipment. It should be enough."
                                else:
                                    $ custom1 = "Even with the pay you were promised by the city officials, what you’ve gathered so far won’t be enough to help you. You may just as well stay here, seek luck. Maybe look for a treasure.\n\n{color=#f6d6bd}Tulia{/color} looks tired. Beaten."
                                jump peltnorth_tulia01about_returntocity03_after
                            'I came here to become rich...' if pc_goal == "iwantmoney":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I came here to become rich...')
                                if pc_goal_lost100coins or coins >= 100 or (item_asterionwine and item_asterionwine_pcknows_2):
                                    $ custom1 = "While your savings may be major, you doubt you’ll find a place in the North that would truly allow you to invest them. If you were to stay, you’d sooner be forced to buy yourself a new mount, than be allowed to spend your days idly.\n\n{color=#f6d6bd}Tulia{/color} looks tired. Beaten. Staying here would mean abandoning your dream."
                                else:
                                    $ custom1 = "Your savings are not exactly impressive, but even if they were, you doubt you’d find a place in the North that would truly allow you to invest them. If you were to stay, you’d sooner be forced to buy yourself a new mount, than be allowed to spend your days idly.\n\n{color=#f6d6bd}Tulia{/color} looks tired. Beaten. Staying here would mean abandoning your dream."
                                jump peltnorth_tulia01about_returntocity03_after
                            'I was meant to become a hero...' if pc_goal == "iwanttoberemembered":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to become a hero...')
                                if quest_pc_goal == 2:
                                    $ custom1 = "You won’t find many opportunities to prove yourself back in the city. You could master your trade here, then maybe join a group of adventurers. Start another journey.\n\n{color=#f6d6bd}Tulia{/color} shoots you an encouraging look."
                                else:
                                    $ custom1 = "So far, you haven’t had much luck, but you know the North hides dark secrets for you to unravel - you can feel it.\n\n{color=#f6d6bd}Tulia{/color} looks exhausted. She may not be ready - but you are."
                                jump peltnorth_tulia01about_returntocity03_after
                            'I was meant to help people...' if pc_goal == "iwanttohelp":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to help people...')
                                if quest_pc_goal == 2:
                                    $ custom1 = "The roads need you more than the safe city walls. Or you could master your trade here, then maybe join a group of adventurers. Start another journey.\n\n{color=#f6d6bd}Tulia{/color} shoots you an encouraging look."
                                else:
                                    $ custom1 = "So far, you haven’t had much luck, but you know the North hides more desperate souls - you can feel it.\n\n{color=#f6d6bd}Tulia{/color} looks exhausted. She may not be ready - but you are."
                                jump peltnorth_tulia01about_returntocity03_after
                            'I wanted to start a new life...' if pc_goal == "iwanttostartanewlife":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wanted to start a new life...')
                                if quest_pc_goal == 2:
                                    $ custom1 = "Why not accept an invitation you received? Here, away from the cage of the city, you could take a deep breath.\n\n{color=#f6d6bd}Tulia{/color} shoots you an encouraging look."
                                elif quest_ruins_choice == "thais_alliance" or pc_goal_iwantnewlife_creeks or pc_goal_iwantnewlife_monastery or glaucia_invitingtojoin or pc_goal_iwantnewlife_galerocks:
                                    $ custom1 = "Why not accept an invitation you received? Here, away from the cage of the city, you could take a deep breath.\n\n{color=#f6d6bd}Tulia{/color} shoots you an encouraging look."
                                else:
                                    $ custom1 = "But so far, no one seems ready to take you in. You’d be forced to stay in the saddle, resting at inns, never a neighbor.\n\n{color=#f6d6bd}Tulia{/color} looks exhausted. Beaten."
                                jump peltnorth_tulia01about_returntocity03_after
                            'I shake my head. I was meant to gain influence...' if pc_goal == "iwantstatus":
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake my head. I was meant to gain influence...')
                                if quest_pc_goal == 2:
                                    $ custom1 = "Your reputation in the North would take quite a hit if you were to cut yourself free from the protection of the guild, but you could still pull a few strings among the local mayors and elders. Behind the city walls, you could get a slice of the pie. Here - it’s waiting for you.\n\n{color=#f6d6bd}Tulia{/color} shoots you an encouraging look."
                                else:
                                    $ custom1 = "Your reputation in the North would take quite a hit if you were to cut yourself free from the protection of the guild, and it’s not like you have enough strings to pull on your own..\n\n{color=#f6d6bd}Tulia{/color} looks tired. Beaten. Staying here would mean abandoning your dream."
                                label peltnorth_tulia01about_returntocity03_after:
                                    menu:
                                        '[custom1]
                                        '
                                        '“Let’s introduce you to {color=#f6d6bd}[horsename]{/color}. You’re going to spend a lot of time together.”' if pc_likeshorsename:
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s introduce you to {color=#f6d6bd}%s{/color}. You’re going to spend a lot of time together.”' %horsename)
                                            jump hovlavan_road01
                                        '“Let’s take your bundles outside.”' if not pc_likeshorsename:
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s take your bundles outside.”')
                                            jump hovlavan_road01
                                        'I nod to her. “I’m not going to join you.”' if tulia_about_returntocity_alt:
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod to her. “I’m not going to join you.”')
                                            jump peltnorth_tulia01about_returntocity04
                                        'Maybe later.':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe later.')
                                            jump peltnorth_tulia01regularquestions


    label peltnorth_tulia01about_returntocity04:
        menu:
            '“What’s that supposed to mean?” Her voice remains firm, even when it’s low.
            \n\nYou start to explain yourself, but quickly realize it’s not easy to put your soul into words.
            '
            '“I can’t forgive the cityfolk for the way they’ve treated the people I care about.”' if pc_goal == "ineedmoney":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can’t forgive the cityfolk  for the way they’ve treated the people I care about.”')
                $ custom1 = "The tips of her fingers squeeze the hilt of her sword. A long, understanding pause. “A risky move, but...” She doesn’t end her thought. “Well, I still need to report this to my commander. If I can reach him in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b
            '“Trading in the city would bring me no comfort. I’d rather ask the tribes to spare me a room, and let me work among them.”' if pc_goal == "iwantmoney":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Trading in the city would bring me no comfort. I’d rather ask the tribes to spare me a room, and let me work among them.”')
                $ custom1 = "She frowns, as if calculating something, but ends up with a disapproving sigh. “Without the guilds’ caravans, these roads will dwindle - sooner or later. You’ll end up as beast fodder.” With each word, her tone loses conviction. “And I still need to report this to my commander. If I can reach him in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b
            '“I’m going to build my legend here. I don’t need the guild for that.”' if pc_goal == "iwanttoberemembered":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to build my legend here. I don’t need the guild for that.”')
                $ custom1 = "She frowns, trying to find a hint of a joke in your eyes, then forms an annoyed grimace. “You won’t find many bards in these lands,” she states simply. “And I still need to report this to my commander. If I can reach him in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b
            '“I’m needed here. I can change this place for the better - and without the guild’s chains.”' if pc_goal == "iwanttohelp":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m needed here. I can change this place for the better - and without the guild’s chains.”')
                $ custom1 = "“Are you sure your help will be welcome here? We are strangers here.” Her lips are dry. “There are many more tribes, and many more threats. You won’t save everyone.” She straightens up. “And I still need to report this to my commander. If I can reach him in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b
            '“I’ll find freedom here. A new chance.”' if pc_goal == "iwanttostartanewlife":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll find freedom here. A new chance.”')
                $ custom1 = "The tips of her fingers squeeze the hilt of her sword. A long, understanding pause. “A risky bet, but...” She doesn’t end her thought. “Well, I still need to report this to my commander. If I can reach him in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b
            '“I’d rather be the master here than a puppet in the guild.”' if pc_goal == "iwantstatus":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d rather be the master here than a puppet in the guild.”')
                $ custom1 = "She frowns, rubbing the back of her head. Her hair is like a boar’s bristles. “You’re playing a dangerous game, and the merchants don’t share their toys. Better travel with a loaded crossbow.” A long pause. “I need to report this to them, and to my commander. If I can reach the gates in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b
            '“I don’t want {color=#f6d6bd}Hovlavan{/color} to break this place. The tribes should shape their path on their own.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t want {color=#f6d6bd}Hovlavan{/color} to break this place. The tribes should shape their path on their own.”')
                $ custom1 = "She frowns, rubbing the back of her head. Her hair is like a boar’s bristles. “Then you’re taking away a meal from a very hungry bear. Better travel with a loaded crossbow - the merchants won’t take your deeds kindly.” A long pause. “And I need to report this to them, and to my commander. If I can reach the gates in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b
            '“I’ve grown attached to the people here. More than I have to anyone in the city.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve grown attached to the people here. More than I have to anyone in the city.”')
                $ custom1 = "A strange sadness crosses her eyes. “I see,” she mumbles before a long pause. “Fine. But I still need to report this to my commander. If I can reach him in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b
            '“I have some unfinished business here. And opportunities to pursue.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some unfinished business here. And opportunities to pursue.”')
                $ custom1 = "Her dry lips form a smirk. “You know this place will only get worse with fall and winter, right? May want to think this through again.” After seeing your resolute gaze, she lets out a sigh. “I still need to report this to my commander. If I can reach him in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b
            '“Living here feels more... real. The people are crude. The threats are out in the open. Each meal is different. One’s worth isn’t measured with coins.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Living here feels more... real. The people are crude. The threats are out in the open. Each meal is different. One’s worth isn’t measured with coins.”')
                $ custom1 = "She frowns, rubbing the back of her head. Her hair is like a boar’s bristles. “If that’s what you think. To me, real is what I touch, what I see. Everything I do. No matter the streets or the wilderness, I can’t escape the ills of a soul.” A long pause. “I need to report this to my commander. If I can reach him in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b
            '“Haven’t you seen how well I’ve been doing for myself here? Being a roadwarden is easy.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Haven’t you seen how well I’ve been doing for myself here? Being a roadwarden is easy.”')
                $ custom1 = "Her dry lips let out a sigh. “I guess insanity won’t be much of a hindrance for you. But I still need to report this to my commander. If I can reach him in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b
            'I say nothing.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I say nothing.')
                $ custom1 = "You exchange looks. She opens her dry lips, but finally nods with resignation. “I need to report this to my commander. If I can reach him in one piece, through these roads.”"
                jump peltnorth_tulia01about_returntocity04b


    label peltnorth_tulia01about_returntocity04b:
        if pc_goal == "ineedmoney":
            menu:
                '[custom1]
                '
                '“I’ll help you reach the inn, the one nearest to the city. But in return I need your help.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll help you reach the inn, the one nearest to the city. But in return I need your help.”')
                    if item_elkfur:
                        $ item_elkfur = 0
                        $ renpy.notify("You gave away the elk fur.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the elk fur.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the elk fur. It may be heavy, but she can sell it even on the way. “And where are you going to stay next?”"
                    elif item_sealskin:
                        $ item_sealskin = 0
                        $ renpy.notify("You lost sealskin.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away sealskin.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the sealskin. It may be heavy, but she can sell it even on the way. “And where are you going to stay next?”"
                    elif item_linen:
                        $ item_linen = 0
                        $ renpy.notify("You gave away the stack of linen.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the stack of linen.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the stack of linen. It may be heavy, but she can sell it even on the way. “And where are you going to stay next?”"
                    elif item_spices:
                        $ item_spices = 0
                        $ renpy.notify("You gave away the sack of spices.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the sack of spices.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the sack of spices. It should be worth quite a bit at the city stalls. “And where are you going to stay next?”"
                    elif item_ironingot:
                        $ item_ironingot = 0
                        $ renpy.notify("You gave away the iron ingot.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the iron ingot.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the iron ingot. It may be heavy, but she can sell it even on the way. “And where are you going to stay next?”"
                    elif item_magicchisel == 1:
                        $ item_magicchisel = 0
                        $ renpy.notify("You gave away the magic chisel.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the magic chisel.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the magic chisel. It should be worth quite a bit at the city stalls. “And where are you going to stay next?”"
                    elif item_magicchisel == 2:
                        $ item_magicchisel = 0
                        $ renpy.notify("You gave away The Tool of Destruction.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away The Tool of Destruction.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts The Tool of Destruction. Its purpose doesn’t take much explaining, and it should be worth quite a bit at the city stalls. “And where are you going to stay next?”"
                    elif item_cidercask:
                        $ item_cidercask = 0
                        $ renpy.notify("You gave away the cask of cider.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the cask of cider.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the cask of cider. It may be heavy, but she can sell it even on the way. “And where are you going to stay next?”"
                    elif item_asterioncloak:
                        $ item_asterioncloak = 0
                        $ renpy.notify("You gave away Asterion’s cloak.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away Asterion’s cloak.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts Asterion’s cloak. Not only is it valuable, it could help her on her journey. “And where are you going to stay next?”"
                    elif item_asterionbow:
                        $ item_asterionbow = 0
                        $ renpy.notify("You gave away Asterion’s bow.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away Asterion’s bow.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts Asterion’s bow. Not only is it valuable, it could help her on her journey. “And where are you going to stay next?”"
                    elif item_asterionspear:
                        $ item_asterionspear = 0
                        $ renpy.notify("You gave away Asterion’s spear.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away Asterion’s spear.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts Asterion’s spear. Not only is it valuable, it could help her on her journey. “And where are you going to stay next?”"
                    elif item_spiritrock >= 2:
                        $ item_spiritrock -= 2
                        $ renpy.notify("You gave away two spirit rocks.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away two spirit rocks.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts two spirit rocks. They should be worth quite a bit at the city stalls. “And where are you going to stay next?”"
                    elif item_mountainroadspear:
                        $ item_mountainroadspear = 0
                        $ renpy.notify("You gave away the spear.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the spear.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the spear you found in the mountains. Not only is it valuable, it could help her on her journey. “And where are you going to stay next?”"
                    elif item_axe02alt or item_axehead or item_axeset:
                        $ item_axe02alt = 0
                        $ item_axehead = 0
                        $ item_axeset = 0
                        $ renpy.notify("You gave away the bronze axe.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the bronze axe.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the bronze axe you found. Not only is it valuable, it could help her on her journey. “And where are you going to stay next?”"
                    elif item_golemglove:
                        $ item_golemglove = 0
                        $ renpy.notify("You gave away the golem glove.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the golem glove.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the golem glove. Not only is it valuable, it could help her on her journey. “And where are you going to stay next?”"
                    elif item_fancyclothes:
                        $ item_fancyclothes = 0
                        $ renpy.notify("You gave away your fancy clothes.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away your fancy clothes.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts your set of fancy clothes. They may be heavy, but should be worth quite a bit at the city stalls. “And where are you going to stay next?”"
                    elif item_axe03:
                        $ item_axe03 = 0
                        $ renpy.notify("You gave away the battle axe.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the battle axe.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the battle axe you bought. Not only is it valuable, it could help her on her journey. “And where are you going to stay next?”"
                    elif item_crossbow:
                        $ item_crossbow = 0
                        $ renpy.notify("You gave away the crossbow.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the crossbow.{/i}')
                        $ custom2 = "After a bit of negotiating, she accepts the crossbow. Not only is it valuable, it could help her on her journey. “And where are you going to stay next?”"
                    else:
                        $ renpy.notify("You gave away some odds and ends.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away some odds and ends.{/i}')
                        $ custom2 = "After a bit of negotiating, you’re forced to offer her various odds and ends, shoving them into a sack. She sighs. “So, where are you going to stay next?”"
                    $ anti_epilogue_village_tulia_fate = "city"
                    menu:
                        'You reveal the true reason why you’re here and explain your plan. Once you reach {color=#f6d6bd}Hovlavan’s{/color} proximity, {color=#f6d6bd}Tulia{/color} will bring your sibling to you - stealthily. In return, she’s going to get a piece of your equipment, and mention in her report that you’re yet another {i}lost{/i} roadwarden. [custom2]
                        '
                        '“{color=#f6d6bd}Creeks{/color} is a lovely place.”' if pc_goal_iwantnewlife_creeks:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Creeks{/color} is a lovely place.”')
                            $ custom1 = "“Is it? I’ve heard it’s as good as doomed to the first beast attack, so I hope the kind hearts are enough to make it stand on its own.”"
                            $ anti_epilogue_village_selected = "creeks"
                            jump peltnorth_tulia01about_returntocity04_tuliatocitywithpc
                        '“{color=#f6d6bd}Gale Rocks{/color} is as far away from the city as I can get.”' if pc_goal_iwantnewlife_galerocks:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Gale Rocks{/color} is as far away from the city as I can get.”')
                            $ custom1 = "“And its stronghold is not to be undersold, I reckon.”"
                            $ anti_epilogue_village_selected = "galerocks"
                            jump peltnorth_tulia01about_returntocity04_tuliatocitywithpc
                        '“No threats can reach me at {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_ruins_choice == "thais_alliance":
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No threats can reach me at {color=#f6d6bd}Howler’s Dell{/color}.”')
                            $ custom1 = "“Other than the wrath of the herds, you mean.”"
                            $ anti_epilogue_village_selected = "howlers"
                            jump peltnorth_tulia01about_returntocity04_tuliatocitywithpc
                        '“I’ll ask the prelate of {color=#f6d6bd}the monastery{/color} to forgive me and take me in.”' if pc_goal_iwantnewlife_monastery:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll ask the prelate of {color=#f6d6bd}the monastery{/color} to forgive me and take me in.”')
                            $ custom1 = "“There’s a {i}prelate{/i}?” Her voice displays no curiosity."
                            $ anti_epilogue_village_selected = "monastery"
                            jump peltnorth_tulia01about_returntocity04_tuliatocitywithpc
                        '“I’m joining {color=#f6d6bd}Glaucia’s{/color} band. Time for me to taste some real freedom.”' if glaucia_invitingtojoin:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m joining {color=#f6d6bd}Glaucia’s{/color} band. Time for me to taste some real freedom.”')
                            $ custom1 = "She freezes for a moment, as if expecting a strike, but then whispers. “Then be on your watch. Don’t ignore how heavy her boots can get.”"
                            $ anti_epilogue_village_selected = "bandits"
                            jump peltnorth_tulia01about_returntocity04_tuliatocitywithpc
                        '“I’m going to stick to the roads. Travel between the settlements, help them connect to the tribes south of {color=#f6d6bd}Hag Hills{/color}.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to stick to the roads. Travel between the settlements, help them connect to the tribes south of {color=#f6d6bd}Hag Hills{/color}.”')
                            $ custom1 = "“As long as you don’t pretend you’re an {i}official{/i} warden, you should be fine. For the next few seasons you have left before the beasts catch you.”"
                            $ anti_epilogue_village_selected = "travel"
                            label peltnorth_tulia01about_returntocity04_tuliatocitywithpc:
                                if quarters <= (((world_daylength/2)+11)+4):
                                    if tulia_friendship >= (tulia_about_highisland_recruited_threshold/2):
                                        $ custom2 = "She grabs her sack of sparse belongings and approaches the counter to pay her dues. “Then let’s get to it, friend.”\n\nThe innkeep nods to you politely, but keeps his thoughts to himself."
                                    else:
                                        $ custom2 = "She grabs her sack of sparse belongings and approaches the counter to pay her dues. Then let’s get to it.”\n\nThe innkeep nods to you politely, but keeps his thoughts to himself."
                                    menu:
                                        '[custom1] [custom2]
                                        '
                                        '“Let’s introduce you to {color=#f6d6bd}[horsename]{/color}. You’re going to spend a lot of time together.”' if pc_likeshorsename:
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s introduce you to {color=#f6d6bd}%s{/color}. You’re going to spend a lot of time together.”' %horsename)
                                            jump anti_hovlavan01
                                        '“Let’s take your bundles outside.”' if not pc_likeshorsename:
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s take your bundles outside.”')
                                            jump anti_hovlavan01
                                else:
                                    if tulia_friendship >= (tulia_about_highisland_recruited_threshold/2):
                                        $ custom2 = "She looks at the darkening sky. “It’s too late to leave today, but since we’ve got an evening to spare... Want to have a proper drink, now that you’re a free soul?”"
                                        menu:
                                            '[custom1] [custom2]
                                            '
                                            '“Definitely. I’ve gathered quite a few stories during my patrols.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Definitely. I’ve gathered quite a few stories during my patrols.”')
                                                jump anti_hovlavan01
                                            '“Let’s keep our heads fresh for tomorrow. The leaves are starting to turn yellow.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s keep our heads fresh for tomorrow. The leaves are starting to turn yellow.')
                                                jump anti_hovlavan01
                                    else:
                                        $ custom2 = "She looks at the darkening sky. “It’s too late to leave today, but that means we can get some proper rest before the journey.” She leaves you with a hollow nod, then places a dragon bone on the counter, asking for a mug of ale."
                                        menu:
                                            '[custom1] [custom2]
                                            '
                                            'I too approach the innkeep. Let’s see if he’s got any work for me.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I too approach the innkeep. Let’s see if he’s got any work for me.')
                                                jump anti_hovlavan01
                                            'I head outside. If I prepare myself now, we can leave right after dawn.':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head outside. If I prepare myself now, we can leave right after dawn.')
                                                jump anti_hovlavan01
        else:
            menu:
                '[custom1]
                '
                '“I’d compensate you for... {i}strategic{/i} silence.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d compensate you for... {i}strategic{/i} silence.”')
                    $ custom1 = "You explain which parts of her report she needs to omit, and suggest a few pieces of information she could add instead - most of them portraying the North as a dangerous place, one that lost not one, but two wardens in recent months.\n\nAfter a few minutes, she taps on the nearest table. “Show me something that’s worth it.”"
                    jump peltnorth_tulia01about_returntocity04_tuliatocityalone
                '“Or you could stick around. What’s waiting for you back home?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Or you could stick around. What’s waiting for you back home?”')
                    if tulia_friendship >= tulia_about_highisland_recruited_threshold or (tulia_about_bandits_grateful and tulia_friendship >= (tulia_about_highisland_recruited_threshold-2)):
                        $ custom1 = "“Stick around? Doing...” She glances at the innkeep, then at you again. “Give me a moment.”\n\nShe falls silent, lost in her thoughts. Finally, she grabs her sword, as if to draw courage from it. “No one in the city is going to care about my efforts here, are they? If anything, they’d {i}reprimand{/i} me, first. My name carries no value. I could just throw it away.”\n\nHer tone gets warmer. “And what are your plans, now?”"
                        $ custom2 = ""
                        $ anti_epilogue_village_tulia_fate = "pelt"
                        jump peltnorth_tulia01about_returntocity04_tuliainpelt
                    else:
                        menu:
                            '“Stick around? Doing...” She glances at the innkeep, then at you again. “Give me a moment.”\n\nShe falls silent, lost in her thoughts. Finally, she lets out a weak chuckle. “I honestly doubt I could escape my responsibilities just like that. I did a decent job here, and if the army decides otherwise, at least I won’t flee like a coward.” You seek a rebuke in her eyes, but her words target herself more than you.
                            '
                            '“Then I can compensate you for... {i}strategic{/i} silence.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then I can compensate you for... {i}strategic{/i} silence.”')
                                $ custom1 = "You explain which parts of her report she needs to omit, and suggest a few pieces of information she could add instead - most of them portraying the North as a dangerous place, one that lost not one, but two wardens in recent months.\n\nAfter a few minutes, she taps on the nearest table. “Show me something that’s worth it.”"
                                jump peltnorth_tulia01about_returntocity04_tuliatocityalone


    label peltnorth_tulia01about_returntocity04_tuliainpelt:
        menu:
            '[custom1]
            '
            '“{color=#f6d6bd}Creeks{/color} is a lovely place.”' if pc_goal_iwantnewlife_creeks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Creeks{/color} is a lovely place.”')
                $ custom1 = "“Is it? I’ve heard it’s as good as doomed to the first beast attack, so I hope the kind hearts are enough to make it stand on its own.”"
                $ anti_epilogue_village_selected = "creeks"
                jump peltnorth_tulia01about_returntocity04_tuliainpelt2
            '“{color=#f6d6bd}Gale Rocks{/color} is as far away from the city as I can get.”' if pc_goal_iwantnewlife_galerocks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Gale Rocks{/color} is as far away from the city as I can get.”')
                $ custom1 = "“And its stronghold is not to be undersold, I reckon.”"
                $ anti_epilogue_village_selected = "galerocks"
                jump peltnorth_tulia01about_returntocity04_tuliainpelt2
            '“No threats can reach me at {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_ruins_choice == "thais_alliance":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No threats can reach me at {color=#f6d6bd}Howler’s Dell{/color}.”')
                $ custom1 = "“Other than the wrath of the herds, you mean.”"
                $ anti_epilogue_village_selected = "howlers"
                jump peltnorth_tulia01about_returntocity04_tuliainpelt2
            '“I’ll ask the prelate of {color=#f6d6bd}the monastery{/color} to forgive me and take me in.”' if pc_goal_iwantnewlife_monastery:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll ask the prelate of {color=#f6d6bd}the monastery{/color} to forgive me and take me in.”')
                $ custom1 = "“There’s a {i}prelate{/i}?” Her voice displays no curiosity."
                $ anti_epilogue_village_selected = "monastery"
                jump peltnorth_tulia01about_returntocity04_tuliainpelt2
            '“I’m joining {color=#f6d6bd}Glaucia’s{/color} band. Time for me to taste some real freedom.”' if glaucia_invitingtojoin:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m joining {color=#f6d6bd}Glaucia’s{/color} band. Time for me to taste some real freedom.”')
                $ anti_epilogue_village_tulia_fate = "bandits"
                $ custom1 = "She freezes for a moment, as if expecting a strike, but then whispers. “Her boots can get a bit too heavy, friend but... Maybe we should talk with her together.”"
                $ anti_epilogue_village_selected = "bandits"
                jump peltnorth_tulia01about_returntocity04_tuliainpelt2
            '“I’m going to stick to the roads. Travel between the settlements, help them connect to the tribes south of {color=#f6d6bd}Hag Hills{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to stick to the roads. Travel between the settlements, help them connect to the tribes south of {color=#f6d6bd}Hag Hills{/color}.”')
                $ custom1 = "“As long as you don’t pretend you’re an {i}official{/i} warden, you should be fine. For the next few seasons you have left before the beasts catch you.”"
                $ anti_epilogue_village_selected = "travel"
                label peltnorth_tulia01about_returntocity04_tuliainpelt2:
                    if quarters <= (((world_daylength/2)+11)+4):
                        if anti_epilogue_village_selected != "bandits":
                            $ custom2 = "She grabs her sack of sparse belongings and approaches the counter to pay her dues while still looking at you. “I guess I’ll see you around.”\n\nThe innkeep nods to you politely, but keeps his thoughts to himself."
                            menu:
                                '[custom1] [custom2]
                                '
                                'I approach him too. Let’s see if he’s got any work for me.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach him too. Let’s see if he’s got any work for me.')
                                    jump anti_hovlavan01
                                'I head outside. No time to waste - I’ve got a lot of talking to do the next few days.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head outside. No time to waste - I’ve got a lot of talking to do the next few days.')
                                    jump anti_hovlavan01
                        else:
                            $ custom2 = "She grabs her sack of sparse belongings and approaches the counter to pay her dues while still looking at you. “How about we go to her right away?”\n\nThe innkeep nods to you politely, but keeps his thoughts to himself."
                            menu:
                                '[custom1] [custom2]
                                '
                                '“We should. We’ve got a lot of explaining to do.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We should. We’ve got a lot of explaining to do.”')
                                    jump anti_hovlavan01
                    else:
                        $ custom2 = "She looks at the darkening sky. “It’s too late to leave today, but since we’ve got an evening to spare... Want to have a proper drink, now that we’re free souls?”"
                        menu:
                            '[custom1] [custom2]
                            '
                            '“Definitely. I’ve gathered quite a few stories during my patrols.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Definitely. I’ve gathered quite a few stories during my patrols.”')
                                jump anti_hovlavan01
                            '“I’ve got no time to waste, and a lot of talking to do the next few days.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve got no time to waste, and a lot of talking to do the next few days.”')
                                jump anti_hovlavan01


    label peltnorth_tulia01about_returntocity04_tuliatocityalone:
        if item_elkfur:
            $ item_elkfur = 0
            $ renpy.notify("You gave away the elk fur.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the elk fur.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the elk fur. It may be heavy, but she can sell it on the way. “And what are your plans, now?”"
        elif item_sealskin:
            $ item_sealskin = 0
            $ renpy.notify("You lost sealskin.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away sealskin.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the sealskin. It may be heavy, but she can sell it on the way. “And what are your plans, now?”"
        elif item_linen:
            $ item_linen = 0
            $ renpy.notify("You gave away the stack of linen.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the stack of linen.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the stack of linen. It may be heavy, but she can sell it on the way. “And what are your plans, now?”"
        elif item_spices:
            $ item_spices = 0
            $ renpy.notify("You gave away the sack of spices.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the sack of spices.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the sack of spices. It should be worth quite a bit at the city stalls. “And what are your plans, now?”"
        elif item_ironingot:
            $ item_ironingot = 0
            $ renpy.notify("You gave away the iron ingot.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the iron ingot.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the iron ingot. It may be heavy, but she can sell it on the way. “And what are your plans, now?”"
        elif item_magicchisel == 1:
            $ item_magicchisel = 0
            $ renpy.notify("You gave away the magic chisel.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the magic chisel.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the magic chisel. It should be worth quite a bit at the city stalls. “And what are your plans, now?”"
        elif item_magicchisel == 2:
            $ item_magicchisel = 0
            $ renpy.notify("You gave away The Tool of Destruction.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away The Tool of Destruction.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts The Tool of Destruction. Its purpose doesn’t take much explaining, and it should be worth quite a bit at the city stalls. “And what are your plans, now?”"
        elif item_cidercask:
            $ item_cidercask = 0
            $ renpy.notify("You gave away the cask of cider.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the cask of cider.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the cask of cider. It may be heavy, but she can sell it on the way. “And what are your plans, now?”"
        elif item_asterioncloak:
            $ item_asterioncloak = 0
            $ renpy.notify("You gave away Asterion’s cloak.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away Asterion’s cloak.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts Asterion’s cloak. Not only is it valuable, it could help her on her journey. “And what are your plans, now?”"
        elif item_asterionbow:
            $ item_asterionbow = 0
            $ renpy.notify("You gave away Asterion’s bow.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away Asterion’s bow.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts Asterion’s bow. Not only is it valuable, it could help her on her journey. “And what are your plans, now?”"
        elif item_asterionspear:
            $ item_asterionspear = 0
            $ renpy.notify("You gave away Asterion’s spear.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away Asterion’s spear.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts Asterion’s spear. Not only is it valuable, it could help her on her journey. “And what are your plans, now?”"
        elif item_spiritrock >= 2:
            $ item_spiritrock -= 2
            $ renpy.notify("You gave away two spirit rocks.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away two spirit rocks.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts two spirit rocks. They should be worth quite a bit at the city stalls. “And what are your plans, now?”"
        elif item_mountainroadspear:
            $ item_mountainroadspear = 0
            $ renpy.notify("You gave away the spear.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the spear.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the spear you found in the mountains. Not only is it valuable, it could help her on her journey. “And what are your plans, now?”"
        elif item_axe02alt or item_axehead or item_axeset:
            $ item_axe02alt = 0
            $ item_axehead = 0
            $ item_axeset = 0
            $ renpy.notify("You gave away the bronze axe.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the bronze axe.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the bronze axe you found. Not only is it valuable, it could help her on her journey. “And what are your plans, now?”"
        elif item_golemglove:
            $ item_golemglove = 0
            $ renpy.notify("You gave away the golem glove.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the golem glove.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the golem glove. Not only is it valuable, it could help her on her journey. “And what are your plans, now?”"
        elif item_fancyclothes:
            $ item_fancyclothes = 0
            $ renpy.notify("You gave away your fancy clothes.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away your fancy clothes.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts your set of fancy clothes. They may be heavy, but should be worth quite a bit at the city stalls. “And what are your plans, now?”"
        elif item_axe03:
            $ item_axe03 = 0
            $ renpy.notify("You gave away the battle axe.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the battle axe.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the battle axe you bought. Not only is it valuable, it could help her on her journey. “And what are your plans, now?”"
        elif item_crossbow:
            $ item_crossbow = 0
            $ renpy.notify("You gave away the crossbow.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the crossbow.{/i}')
            $ custom2 = "After a bit of negotiating, she accepts the crossbow. Not only is it valuable, it could help her on her journey. “And what are your plans, now?”"
        else:
            $ renpy.notify("You gave away some odds and ends.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away some odds and ends.{/i}')
            $ custom2 = "After a bit of negotiating, you’re forced to offer her various odds and ends, shoving them into a sack. She sighs. “So, what are your plans, now?”"
        $ anti_epilogue_village_tulia_fate = "city"
        menu:
            '[custom1] [custom2]
            '
            '“{color=#f6d6bd}Creeks{/color} is a lovely place.”' if pc_goal_iwantnewlife_creeks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Creeks{/color} is a lovely place.”')
                $ custom1 = "“Is it? I’ve heard it’s as good as doomed to the first beast attack, so I hope the kind hearts are enough to make it stand on its own.”"
                $ anti_epilogue_village_selected = "creeks"
                jump peltnorth_tulia01about_returntocity04_tuliatocityalone2
            '“{color=#f6d6bd}Gale Rocks{/color} is as far away from the city as I can get.”' if pc_goal_iwantnewlife_galerocks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Gale Rocks{/color} is as far away from the city as I can get.”')
                $ custom1 = "“And its stronghold is not to be undersold, I reckon.”"
                $ anti_epilogue_village_selected = "galerocks"
                jump peltnorth_tulia01about_returntocity04_tuliatocityalone2
            '“No threats can reach me at {color=#f6d6bd}Howler’s Dell{/color}.”' if quest_ruins_choice == "thais_alliance":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No threats can reach me at {color=#f6d6bd}Howler’s Dell{/color}.”')
                $ custom1 = "“Other than the wrath of the herds, you mean.”"
                $ anti_epilogue_village_selected = "howlers"
                jump peltnorth_tulia01about_returntocity04_tuliatocityalone2
            '“I’ll ask the prelate of {color=#f6d6bd}the monastery{/color} to forgive me and take me in.”' if pc_goal_iwantnewlife_monastery:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll ask the prelate of {color=#f6d6bd}the monastery{/color} to forgive me and take me in.”')
                $ custom1 = "“There’s a {i}prelate{/i}?” Her voice displays no curiosity."
                $ anti_epilogue_village_selected = "monastery"
                jump peltnorth_tulia01about_returntocity04_tuliatocityalone2
            '“I’m joining {color=#f6d6bd}Glaucia’s{/color} band. Time for me to taste some real freedom.”' if glaucia_invitingtojoin:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m joining {color=#f6d6bd}Glaucia’s{/color} band. Time for me to taste some real freedom.”')
                $ custom1 = "She freezes for a moment, as if expecting a strike, but then whispers. “Then be on your watch. Don’t ignore how heavy her boots can get.”"
                $ anti_epilogue_village_selected = "bandits"
                jump peltnorth_tulia01about_returntocity04_tuliatocityalone2
            '“I’m going to stick to the roads. Travel between the settlements, help them connect to the tribes south of {color=#f6d6bd}Hag Hills{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to stick to the roads. Travel between the settlements, help them connect to the tribes south of {color=#f6d6bd}Hag Hills{/color}.”')
                $ custom1 = "“As long as you don’t pretend you’re an {i}official{/i} warden, you should be fine. For the next few seasons you have left before the beasts catch you.”"
                $ anti_epilogue_village_selected = "travel"
                label peltnorth_tulia01about_returntocity04_tuliatocityalone2:
                    if quarters <= (((world_daylength/2)+11)+4):
                        if tulia_friendship >= (tulia_about_highisland_recruited_threshold/2):
                            $ custom2 = "She grabs her sack of sparse belongings and approaches the counter to pay her dues, then heads outside. “Safe travels, friend.”\n\nThe innkeep nods to you politely, but keeps his thoughts to himself."
                        else:
                            $ custom2 = "She grabs her sack of sparse belongings and approaches the counter to pay her dues, then heads outside. “Safe travels.”\n\nThe innkeep nods to you politely, but keeps his thoughts to himself."
                        menu:
                            '[custom1] [custom2]
                            '
                            'I approach him too. Let’s see if he’s got any work for me.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach him too. Let’s see if he’s got any work for me.')
                                jump anti_hovlavan01
                            'I head outside. No time to waste - I’ve got a lot of talking to do the next few days.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head outside. No time to waste - I’ve got a lot of talking to do the next few days.')
                                jump anti_hovlavan01
                    else:
                        if tulia_friendship >= (tulia_about_highisland_recruited_threshold/2):
                            $ custom2 = "She looks at the darkening sky. “It’s too late to leave today, but since we’ve got an evening to spare... Want to have a proper drink, now that you’re a free soul?”"
                            menu:
                                '[custom1] [custom2]
                                '
                                '“Definitely. I’ve gathered quite a few stories during my patrols.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Definitely. I’ve gathered quite a few stories during my patrols.”')
                                    jump anti_hovlavan01
                                '“I’ve got no time to waste, and a lot of talking to do the next few days.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve got no time to waste, and a lot of talking to do the next few days.”')
                                    jump anti_hovlavan01
                        else:
                            $ custom2 = "She looks at the darkening sky. “It’s too late to leave today, but I guess I can get some proper rest before the journey. Safe travels to you,” she leaves you with a hollow nod, then places a dragon bone on the counter, asking for a mug of ale."
                            menu:
                                '[custom1] [custom2]
                                '
                                'I too approach the innkeep. Let’s see if he’s got any work for me.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I too approach the innkeep. Let’s see if he’s got any work for me.')
                                    jump anti_hovlavan01
                                'I head outside. No time to waste - I’ve got a lot of talking to do the next few days.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head outside. No time to waste - I’ve got a lot of talking to do the next few days.')
                                    jump anti_hovlavan01

label peltnorth_tulia_meeting01:
    if peltnorth_ban_perm_past:
        $ custom1 = "but even though they give you suspicious looks, they don’t stop you from crossing the open gate"
    else:
        $ custom1 = "looking at you as if you’re bringing them answers"
    menu:
        'The yard is stained with coughed-up blood, the trail leading into the building. The hunters are tense, with weapons at hand, [custom1].
        \n\nYou’re approached by {color=#f6d6bd}[dalit_name]{/color}. “You heard? {color=#f6d6bd}The lieutenant{/color} from {color=#f6d6bd}Hag Hills{/color} fled from her camp - she would be dead without our potions.”
        '
        '“What happened?”' if not militarycamp_destroyed_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What happened?”')
            menu:
                '“A troll,” there’s a hint of shame in her voice. “She says she stopped it, but not before it tore the other soldier to pieces. Better speak with her.”
                '
                'I enter the building.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the building.')
                    jump peltnorth_tulia_meeting02
        '“She’s the one who killed the troll?”' if militarycamp_destroyed_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She’s the one who killed the troll?”')
            $ dalit_friendship += 1
            menu:
                'Her eyes widen. “So she wasn’t lying. Tough soul, that one. Did you get the beast’s tusks?”
                \n\nYou explain that getting through the scavengers won’t be so easy, and she puffs her cheeks briefly. “It may be time to give up on the camp completely. No one is going to maintain this road any longer, not with all the other soldiers dead. The bad news will spread.”
                '
                'I nod and enter the building.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and enter the building.')
                    label peltnorth_tulia_meeting02:
                        show areapicture peltnorth01inside at basicfade
                        hide peltnorthbronzerod
                        $ minutes += 5
                        if tulia_friendship >= 5:
                            $ custom1 = "Her smile is empty."
                        elif tulia_friendship >= 2:
                            $ custom1 = "Her grunt is hesitant."
                        else:
                            $ custom1 = "She lets out a sigh."
                        menu:
                            '{color=#f6d6bd}The innkeep{/color} greets you with a nod, then his eyes lead you to the bench in the corner. {color=#f6d6bd}Tulia{/color} is sitting with her head resting against the wall, breathing heavily, with clean bandages on her neck, arm, and leg. Next to her are three small bottles, all of them open, but your nose catches no scent of ale. Her gambeson is on the floor, now more of a rag than armor.
                            \n\nAs you sit down next to her on a stool, she opens one eye, then another. [custom1]
                            '
                            '“Tell me about the attack.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about the attack.”')
                                $ tulia_about_troll_attack = 1
                                $ custom1 = "“There isn’t much to say. It came in the early hours, we threw and shot anything we could at it. After it broke through the gate, I had one last arrow left. My {i}subordinate{/i}” her voice is bitter, “gave me time to aim. And now he’s gone.”"
                                jump peltnorth_tulia01regularquestionsafter
                            '“Do you need my help?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you need my help?”')
                                $ tulia_friendship += 1
                                $ custom1 = "“I know how I look, but pneuma is already flowing in my blood. I’m good.”"
                                jump peltnorth_tulia01regularquestionsafter
                            '“What will you do next?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will you do next?”')
                                $ tulia_about_returntocity = 1
                                $ custom1 = "She shrugs. “Well, if any city rat is going to criticize me for getting out of here before the end of my {i}watch{/i}, they can jump into the sea, for all I care. I can head back to the city whenever you’re ready.”"
                                jump peltnorth_tulia01regularquestionsafter
                            '“I’ve been to your camp. It’s as good as gone.”' if militarycamp_destroyed_firsttime and not tulia_about_troll:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to your camp. It’s as good as gone.”')
                                $ tulia_about_troll = 1
                                $ tulia_friendship += 1
                                $ custom1 = "You explain that the broken entrance is in worse shape than she remembers, and that the scavengers are going to have a feast for a few days, if not more. She rubs the top of her head with her entire palm, glancing at two hunters who just entered the room.\n\n“No longer my problem,” she says to herself, but then meets your eyes and lets out a sorrowful chuckle. “Quite a monster we knocked down, wasn’t it?”"
                                jump peltnorth_tulia01regularquestionsafter

label peltnorth_tulia_meeting_firsttimeALL:
    label peltnorth_tulia_meeting_firsttime01:
        $ dalit_about_tulia = 1
        $ tulia_pelt_needstotalkwithiason = 1
        menu:
            'Inns like this one fit the regions traveled by merchants, but you wouldn’t expect a place of this size in a forsaken peninsula. The stone and lumber must have been transported from far away, and the workers, guarded by expensive mercenaries, surely lived for many seasons in a primitive hamlet, subsisting on salted supplies.
            \n\nThe yard is stained with coughed-up blood, the trail leading into the building. The guards are tense, with weapons at hand, looking at you as if you’re bringing them answers.
            \n\nYou’re approached by {color=#f6d6bd}a woman in yellow armor{/color}. “You’re that roadwarden, correct? {color=#f6d6bd}The lieutenant{/color} from {color=#f6d6bd}Hag Hills{/color} fled from her camp - she would be dead without our potions.” She has long, curly, disorderly red hair, pointing in every possible direction. This combination of colors doesn’t work at all - in the woods, one would have to shout to draw this much attention.
            '
            '“What happened?”' if not militarycamp_destroyed_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What happened?”')
                menu:
                    '“A troll,” there’s a hint of shame in her voice. “She says she stopped it, but not before it tore the other soldier to pieces. Better speak with her.”
                    \n\nHer voice is young and strong, with an accent that reminds you of the villages spread around {color=#f6d6bd}Hovlavan{/color}. Her eyes keep running toward {color=#f6d6bd}[horsename]{/color}, though both her and the rest of the crew stay away from it.
                    '
                    'I lead it to the tethering post, then enter the building.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead it to the tethering post, then enter the building.')
                        jump peltnorth_tulia_meeting_firsttime02
            '“She’s the one who killed the troll?”' if militarycamp_destroyed_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She’s the one who killed the troll?”')
                $ dalit_friendship += 1
                menu:
                    'Her eyes widen. “So she wasn’t lying. Tough soul, that one. Did you get the beast’s tusks?”
                    \n\nYou explain that getting through the scavengers won’t be so easy, and she puffs her cheeks briefly. “It may be time to give up on the camp completely. No one is going to maintain this road any longer, not with all the other soldiers dead. The bad news will spread.”
                    \n\nHer voice is young and strong, with an accent that reminds you of the villages spread around {color=#f6d6bd}Hovlavan{/color}. Her eyes keep running toward {color=#f6d6bd}[horsename]{/color}, though both her and the rest of the crew stay away from it.
                    '
                    'I lead it to the tethering post, then enter the building.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lead it to the tethering post, then enter the building.')
                        label peltnorth_tulia_meeting_firsttime02:
                            $ shop = "peltnorth"
                            $ renpy.notify("New shelter unlocked.")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
                            $ peltnorth_resting = 1
                            show areapicture peltnorth01inside at basicfade
                            hide peltnorthbronzerod
                            $ minutes += 5
                            if tulia_friendship >= 5:
                                $ custom1 = "Her smile is empty."
                            elif tulia_friendship >= 2:
                                $ custom1 = "Her grunt is hesitant."
                            else:
                                $ custom1 = "She lets out a sigh."
                            $ iason_stance = "behindcounter"
                            if quarters < 36:
                                $ peltnorthroomdescription = "The locked windows make the air stuffy, and the weak fire in the stove hardly lightens up the hall."
                            elif quarters < 48:
                                $ peltnorthroomdescription = "Only some of the windows are open, revealing the dust dancing in the sunbeams. The air is a bit stuffy."
                            elif quarters < (world_daylength-60):
                                $ peltnorthroomdescription = "The windows are open, but the heat of the burning stove warms you."
                            elif quarters < world_daylength:
                                $ peltnorthroomdescription = "The open windows fill the hall with refreshing air and the sounds of conversations."
                            else:
                                $ peltnorthroomdescription = "The locked windows make the air stuffy, and both the counter and the tables are lit with candles."
                            menu:
                                '[peltnorthroomdescription] {color=#f6d6bd}The muscular innkeep{/color} greets you from behind the counter, then his eyes lead you to the bench in the corner. {color=#f6d6bd}Tulia{/color} is sitting with her head resting against the wall, breathing heavily, with clean bandages on her neck, arm, and leg. Next to her are three small bottles, all of them open, but your nose catches no scent of ale. Her gambeson is on the floor, now more of a rag than armor.
                                \n\nAs you sit down next to her on a stool, she opens one eye, then another. [custom1]
                                '
                                '“Tell me about the attack.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about the attack.”')
                                    $ tulia_about_troll_attack = 1
                                    $ custom1 = "“There isn’t much to say. It came in the early hours, we threw and shot anything we could at it. After it broke through the gate, I had one last arrow left. My {i}subordinate{/i}” her voice is bitter, “gave me time to aim. And now he’s gone.”"
                                    jump peltnorth_tulia01regularquestionsafter
                                '“Do you need my help?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you need my help?”')
                                    $ tulia_friendship += 1
                                    $ custom1 = "“I know how I look, but pneuma is already flowing in my blood. I’m good.”"
                                    jump peltnorth_tulia01regularquestionsafter
                                '“What will you do next?”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What will you do next?”')
                                    $ tulia_about_returntocity = 1
                                    $ custom1 = "She shrugs. “Well, if any city rat is going to criticize me for getting out of here before the end of my {i}watch{/i}, they can jump into the sea, for all I care. I can head back to the city whenever you’re ready.”"
                                    jump peltnorth_tulia01regularquestionsafter
                                '“I’ve been to your camp. It’s as good as gone.”' if militarycamp_destroyed_firsttime and not tulia_about_troll:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve been to your camp. It’s as good as gone.”')
                                    $ tulia_about_troll = 1
                                    $ tulia_friendship += 1
                                    $ custom1 = "You explain that the broken entrance is in worse shape than she remembers, and that the scavengers are going to have a feast for a few days, if not more. She rubs the top of her head with her entire palm, glancing at two hunters who just entered the room.\n\n“No longer my problem,” she says to herself, but then meets your eyes and lets out a sorrowful chuckle. “Quite a monster we knocked down, wasn’t it?”"
                                    jump peltnorth_tulia01regularquestionsafter

    label peltnorth_tulia_meeting_firsttime03:
        $ at_activate = 1
        $ at = 0
        menu:
            'The planks let out a creak after every step you make. “Rough day, ain’t it? Let’s hope the troll marches won’t be a seasonal thing,” the man’s voice is deep and soft, with a city-like accent. He observes you with keen attention, yet avoids your eyes.
            \n\nHis skin is dark, almost purple, rare even among The Southern Tribes, and his hair is naturally blueish. His clothes are quite fancy for manual labor - the elegant tunic wouldn’t stand out in the city square.
            \n\n“Just so you know, my {color=#f6d6bd}Pelt{/color} doesn’t belong to {color=#f6d6bd}Hovlavan{/color}. You can sleep on the floor if you wish so, but if you want a bed or a meal, you have to pay. We may have some leftovers from dinner, but I’d need to check.”
            '
            ' (disabled)' ( condition="at == 0" ):
                pass
            '“Thanks, I’d appreciate it. I see you know how to make friends with a roadwarden.”' ( condition="at == 'friendly'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “Thanks, I’d appreciate it. I see you know how to make friends with a roadwarden.”')
                $ at_activate = 0
                $ at = 0
                $ iason_friendship -= 1
                menu:
                    'He meets your eyes with a puzzled look, then grabs a wet cloth and starts to wipe down the shelves. From time to time, your conversation is interrupted by splashes of dirty water in the wooden bucket.
                    \n\n“Well, nothing is truly free. I have work for a soul of the road, but I don’t need a new mouth to babble.” He speaks slowly, yet clearly. “Maybe you’ll help me with a worrying thought I have, instead?”
                    '
                    '“Which is?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Which is?”')
                        jump peltnorth_tulia_meeting_firsttime04
            '“Well! I could help you with all that you have left, if you need me to!”' ( condition="at == 'playful'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “Well! I could help you with all that you have left, if you need me to!”')
                $ at_activate = 0
                $ at = 0
                $ iason_friendship -= 2
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "iason1"
                menu:
                    'He sighs, grabs a wet cloth, and starts to wipe down the shelves. From time to time, your conversation is interrupted by splashes of dirty water in the wooden bucket.
                    \n\n“You’re already giving me second thoughts,” he speaks slowly, yet clearly. “What do you want?”
                    '
                    '(iason1 set)':
                        pass
            '“I won’t stay here for long.” I introduce myself.' ( condition="at == 'distanced'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “I won’t stay here for long.” I introduce myself.')
                $ at_activate = 0
                $ at = 0
                $ iason_friendship += 1
                menu:
                    'He nods and fills two mugs with water, then offers you one of them.
                    \n\n“I’m glad to see someone willing to take {color=#f6d6bd}Asterion’s{/color} place. Even my crew here hits the road only if they need to see the healers of {color=#f6d6bd}Howler’s Dell{/color}, and they’re more than resourceful. A roadwarden is always going to find work here, in the North. Though maybe not on the eastern road.”
                    \n\nHe takes a mouthful of water and drinks it with a pleased sigh.
                    \n\n“Would you like to help me with a worrying thought I have?” For a brief moment, he meets your eyes.
                    '
                    '“Which is?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Which is?”')
                        jump peltnorth_tulia_meeting_firsttime04
            '“I’m not here to beg for food. I’m looking for answers.”' ( condition="at == 'intimidating'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “I’m not here to beg for food. I’m looking for answers.”')
                $ at_activate = 0
                $ at = 0
                $ can_rest = 1
                $ can_items = 1
                $ questionpreset = "iason1"
                menu:
                    'He sighs, grabs a wet cloth, and starts to wipe down the shelves. From time to time, your hear splashes of dirty water in the wooden bucket.
                    '
                    '(iason1 set)':
                        pass
            '“Thanks. It’s not easy to get food on the road.”' ( condition="at == 'vulnerable'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “Thanks. It’s not easy to get food on the road.”')
                $ at_activate = 0
                $ at = 0
                menu:
                    'He meets your eyes with a frown, then grabs a wet cloth and starts to wipe down the shelves. From time to time, your conversation is interrupted by splashes of dirty water in the wooden bucket.
                    \n\n“Just don’t get used to it. Coins aren’t worth much here, in the North, surely less than work. And there are days of hunger,” he speaks slowly, yet clearly. “You won’t fill your stomach with words alone, but maybe you’ll help me with a worrying thought I have?”
                    '
                    '“Which is?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Which is?”')
                        jump peltnorth_tulia_meeting_firsttime04
