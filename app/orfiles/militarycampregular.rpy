default militarycamp_fluff = ""
default militarycamp_fluff2 = ""
default militarycamp_fluff2_old = 0
default militarycamp_roast = 0
default militarycamp_destroyed = 0
default militarycamp_destroyed_firsttime = 0
default militarycamp_destroyed_day = 15
default militarycamp_destroyed_firsttime_tulia = 0
default militarycamp_destroyed_firsttime_southerncrossroads = 0

default tulia_about_asterion2 = 0
default tulia_about_asterion3 = 0
default tulia_about_tablet = 0
default tulia_about_nomoreundead = 0
default tulia_about_caius_spokento = 0

default tulia_about_shortcut = 0
default tulia_about_missinghunters = 0
default tulia_about_ruinedvillage = 0

default tulia_about_bandits1 = 0
default tulia_about_bandits2 = 0
default tulia_about_bandits3 = 0
default tulia_about_bandits_grateful = 0
default tulia_about_bandits_hopeless = 0
default tulia_about_bandits_indebt = 0
default tulia_about_bandits_liedto = 0

default tulia_about_asterion_reward = 0

label militarycamp01:
    if day >= militarycamp_destroyed_day:
        stop music fadeout 4.0
        play nature "audio/ambient/shortcutdarkforest01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        jump militarycamp_destroyed01
    $ renpy.music.play("audio/track_18military.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    if day == 1:
        if quarters < (world_daylength-20):
            show areapicture prologuemilitarycampscrap04 at basicfade
        else:
            show areapicture prologuemilitarycampscrap06 at basicfade
    elif day <= 5:
        show areapicture prologuemilitarycampscrap06 at basicfade
    else:
        show areapicture prologuemilitarycampscrap04nofire at basicfade
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ renpy.force_autosave(take_screenshot=False, block=True)
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if day == 1:
        if quarters < (world_daylength-20):
            $ custom1 = "The soldiers are still adding fuel to the pyre. At least the scent is gentler."
        else:
            $ custom1 = "The pyre is no more, the stench barely lingers. The soldiers are preparing bowls of gruel."
        if tulia_friendship >= 2:
            $ custom2 = "{color=#f6d6bd}Tulia{/color} welcomes you with a smile.\n\n“Is everything alright?”"
        else:
            $ custom2 = "{color=#f6d6bd}Tulia{/color} welcomes you with a nod.\n\n“Still alive, I see.”"
        menu:
            '[custom1] [custom2]
            '
            '“I have more questions.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have more questions.”')
                jump militarycamp01regularquestions
    elif day >= (militarycamp_destroyed_day-5) and not militarycamp_roast and pc_food < 4:
        $ militarycamp_roast = 1
        jump militarycamproast01
    else:
        if tulia_friendship >= 2:
            $ custom2 = "{color=#f6d6bd}Tulia{/color} welcomes you with a smile.\n\n“Is everything alright?”"
        else:
            $ custom2 = "{color=#f6d6bd}Tulia{/color} welcomes you with a nod.\n\n“Still alive, I see.”"
        label militarycamp_fluff2loop:
            $ militarycamp_fluff2 = ""
            $ militarycamp_fluff2 = renpy.random.choice(['The soldiers are splitting logs into firewood and stripping a tree trunk of its branches.', 'You hear laughter. The soldiers are practicing with their bows, shooting at a target in some sort of game. The man is mocking his superior in a friendly banter.', 'The soldiers are walking in and out of the camp, carrying large logs to prepare a supply for another pyre.', 'The camp is silent. The soldiers hold their mugs, but don’t even chat, lowering their heads from exhaustion. They seem exhausted.', 'The camp hasn’t changed much since your last visit. The soldiers are cleaning their equipment.', 'You hear the soldiers’ loud discussion as they carry buckets of water.'])
            if militarycamp_fluff2_old == militarycamp_fluff2:
                jump militarycamp_fluff2loop
            else:
                $ militarycamp_fluff2_old = militarycamp_fluff2
        menu:
            '[custom2] [militarycamp_fluff2]
            '
            '“I have more questions.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have more questions.”')
                jump militarycamp01regularquestions

label militarycamproast01ALL:
    label militarycamproast01:
        if (tulia_friendship+appearance_charisma) >= 5:
            menu:
                'Your nose catches the scent long before you reach the gate. A large roasted leg of a runner is hanging above the campfire.
                \n\n{color=#f6d6bd}Tulia{/color} greets you with a smile. “[pcname]! The days are getting colder, huh? Feel free to cut a leg or something from our dinner, we have more than enough to fill ourselves up.”
                '
                'I thank her and start eating the roast.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I thank her and start eating the roast.')
                    jump militarycampeatingroast
                '“I wanted to discuss something.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wanted to discuss something.”')
                    jump militarycamp01regularquestions
        else:
            menu:
                'Your nose catches the scent long before you reach the gate. A large roasted leg of a runner is hanging above the campfire.
                \n\n{color=#f6d6bd}Tulia{/color} welcomes you with a nod. “Hello again. The days are getting colder, huh?”
                '
                '“Any chance I could buy some of your roast?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any chance I could buy some of your roast?”')
                    if (tulia_friendship+appearance_charisma) > 3:
                        jump militarycampbuyingroastfree
                    else:
                        jump militarycampbuyingroast1coin
                '“I wanted to discuss something.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wanted to discuss something.”')
                    jump militarycamp01regularquestions

    label militarycampbuyingroast1coin:
            menu:
                'She gives you a cold look “You can eat as much as you need. For a coin.”
                '
                'I give her a coin and get to the roast.' if coins:
                    $ coins = limit_coins(coins-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give her a coin and get to the roast.')
                    show screen notifyimage( "-1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
                    jump militarycampeatingroast
                'I put a coin on the table and approach the roast.' if coins:
                    $ coins = limit_coins(coins-1)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put a coin on the table and approach the roast.')
                    show screen notifyimage( "-1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
                    jump militarycampeatingroast
                'Looks like I can’t afford it. (disabled)' if coins <= 0:
                    pass
                '“I see. I wanted to discuss something else.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see. I wanted to discuss something else.”')
                    jump militarycamp01regularquestions

    label militarycampbuyingroastfree:
        menu:
            'She waves her hand. “Go ahead, no need to trade. We’ve more than enough.”
            '
            'I thank her and start eating the roast.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I thank her and start eating the roast.')
                jump militarycampeatingroast

    label militarycampeatingroast:
        $ pc_food = limit_pc_food(pc_food+3)
        $ quarters += 1
        show plus3food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 nourishment points.{/i}')
        menu:
            'You take a wooden bowl and tear off pieces of meat. The bird is as juicy as it seemed to be, and you recognize an herbal marinate. The careful cooks left no burnt or undercooked bits. Drops of fat stay on your chin, and you’re tempted to lick your fingers.
            '
            'After the meal, I go to the guards.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- After the meal, I go to the guards.')
                jump militarycamp01regularquestions

label militarycamp01regularquestions:
    $ custom1 = ""
    $ custom1 = renpy.random.choice(['“What else do you need?”', '“Yes?”', 'She smiles gently.', '“How can I help you?”', '“Go ahead.”', '“Shoot.”'])
    label militarycamp01regularquestionsafter:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '[custom1]
            '
            '“I found {color=#f6d6bd}Asterion{/color}.”' if asterion_found and not quest_asterion_description00goodresult:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news about {color=#f6d6bd}Asterion{/color}.”')
                jump militarycamp01aboutasterion01
            #######
            '“The priest of {color=#f6d6bd}White Marshes{/color} has agreed to release the dead shells. Problem solved.”' if orentius_convinced and not tulia_about_nomoreundead:
                jump militarycamptulia_about_nomoreundead01
            '“The priest of {color=#f6d6bd}White Marshes{/color} is gone, and so are his undead. Problem solved.”' if orentius_banished and not tulia_about_nomoreundead:
                jump militarycamptulia_about_nomoreundead02
            '“The village of {color=#f6d6bd}White Marshes{/color} is no more. The North will now struggle with a large group of undead.”' if whitemarshes_destroyed and not tulia_about_nomoreundead:
                jump militarycamptulia_about_nomoreundead03
            #######
            '“I found this wax tablet. Do you recognize it?”' if not tulia_about_tablet and item_asteriontablet:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found this wax tablet. Do you recognize it?”')
                $ tulia_about_tablet += 1
                jump militarycamp01tulia_about_tablet01
            #######
            '“Guess what. I met with {color=#f6d6bd}Caius{/color}.”' if foragers_caius_heardabout and foragers_caius_spokento and not tulia_about_caius_spokento:
                jump militarycamp01tulia_about_caius_spokento01
            #######
            '“Did you ever enter the road leading through the heart of the woods?”' if shortcut_pcknowsabout and not tulia_about_shortcut:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did you ever enter the road leading through the heart of the woods?”')
                $ tulia_about_shortcut += 1
                jump militarycamp01tulia_about_shortcut01
            #######
            '“Were any hunters from the north passing by your camp recently?”' if quest_missinghunters == 1 and not tulia_about_missinghunters:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Were any hunters from the north passing by your camp recently?”')
                $ tulia_about_missinghunters += 1
                jump militarycamp01tulia_about_missinghunters01
            #######
            '“Do you have an idea about what happened to the ruined village in the west?”' if ruinedvillage_firsttime == 1 and not ruinedvillage_confront_can and not ruinedvillage_truth and not tulia_about_ruinedvillage:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have an idea about what happened to the ruined village in the west?”')
                $ tulia_about_ruinedvillage += 1
                if quest_ruins == 1 and not quest_ruins_description01:
                    $ renpy.notify("Journal updated: The Ruined Village")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
                $ quest_ruins_description01 = "I heard that the village was destroyed almost ten years ago."
                jump militarycamp01tulia_about_ruinedvillage01
            #######
            '“Have you ever encountered the bandits from the North?”' if banditshideout_bandits_pchearedabout and not tulia_about_bandits1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever encountered the bandits from the North?”')
                $ tulia_about_bandits1 += 1
                jump militarycamp01tulia_about_bandits01
            '“Nice acting, but I spoke with {color=#f6d6bd}Glaucia{/color}. You’re working with her.”' if tulia_about_bandits1 and description_tulia05 and not tulia_about_bandits2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Nice acting, but I spoke with {color=#f6d6bd}Glaucia{/color}. You’re working with her.”')
                $ tulia_about_bandits2 += 1
                jump militarycamp01tulia_about_bandits02
            '“Come on, now. This is the only pass through {color=#f6d6bd}Hag Hills{/color}. Recently, there’s been a caravan with tools and spices that was taken by force, to be sold for ransom. {i}Someone{/i} told them to turn east, right into the band’s trap. You want me to believe you bear no responsibility, and saw nothing?”' if tulia_about_bandits2 and glaucia_about_lostmerchants_trail and not tulia_about_bandits3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Come on, now. This is the only pass through {color=#f6d6bd}Hag Hills{/color}. Recently, there’s been a caravan with tools and spices that was taken by force, to be sold for ransom. {i}Someone{/i} told them to turn east, right into the band’s trap. You want me to believe you bear no responsibility, and saw nothing?”')
                $ tulia_about_bandits3 += 1
                jump militarycamp01tulia_about_bandits03
            #######
            '“What happened to your squad?”' if not tulia_about_hersquad:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What happened to your squad?”')
                $ tulia_about_hersquad += 1
                jump militarycamp01regularadditionalquestion01
            #######
            '“{color=#f6d6bd}Tulia{/color}, how did you become a lieutenant?”' if not tulia_about_herself:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Tulia{/color}, how did you become a lieutenant?”')
                $ tulia_about_herself += 1
                jump militarycamp01regularadditionalquestion02
            #######
            '“What was your squad’s mission?”' if not tulia_about_hermission:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What was your squad’s mission?”')
                $ tulia_about_hermission += 1
                jump militarycamp01regularadditionalquestion03
            #######
            'She doesn’t trust me enough to tell me about her squad’s mission. (disabled)' if tulia_about_hermission and not description_tulia04 and (tulia_friendship+appearance_charisma) < 3:
                pass
            #######
            '“About your squad’s mission...”' if tulia_about_hermission and not description_tulia04 and (tulia_friendship+appearance_charisma) >= 3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What was your squad’s mission?”')
                jump militarycamp01regularadditionalquestion03p02
            #######
            '“Anything I should know about this camp?”' if not tulia_about_camp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Anything I should know about this camp?”')
                $ tulia_about_camp += 1
                jump militarycamp01regularadditionalquestion04
            #######
            '“Thanks.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thanks.”')
                jump militarycamp01regularnothingelsetodo

label militarycamp01tulia_about_tablet01: #“I found this wax tablet. Do you recognize it?”
    menu:
        'She opens it and takes takes a quick glance. “Well, it’s from {color=#f6d6bd}Hovlavan{/color}. {color=#f6d6bd}Asterion{/color} and my lieutenant were the only people I’ve seen with green tablets like this one. And the locals don’t write chronicles.”
        \n\nShe gives it back. “I can’t read. Better look for a priest of The Wright.”
        '
        '“Good call.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Good call.”')
            jump militarycamp01regularquestions

label militarycamp01tulia_about_shortcut01: # “Did you ever enter the road leading through the heart of the woods?”
    menu:
        '“Oh, we were advised not to. Have you seen this huge gate in the west? Made of rocks, very tall? We’ve met a guard there, named... {color=#f6d6bd}Quinton{/color}, maybe? A kind soul, but a bit slow. He almost begged us not to enter the woods, so we took the longer route.”
        \n\n“That’s where all the settlements are anyway,” her companion chips in. “We didn’t miss much.”
        '
        '“I see.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see.”')
            jump militarycamp01regularquestions

label militarycamp01tulia_about_missinghunters01: # “Were any hunters from the north passing by your camp recently?”
    menu:
        '“Not from the north... Not from the south!” She lets out a weak chuckle. “I didn’t expect this place to be {i}that{/i} desolate at this time of the year. You’re the only soul we’ve seen in days, unless you count beastfolk.”
        '
        '“Well, it was worth a shot.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, it was worth a shot.”')
            jump militarycamp01regularquestions
        '“Unless they’re from {color=#f6d6bd}Creeks{/color}, I don’t.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Unless they’re from {color=#f6d6bd}Creeks{/color}, I don’t.”')
            $ custom1 = "She smiles. “Well, I didn’t ask them, so there’s always a chance.”"
            $ tulia_friendship += 1
            jump militarycamp01regularquestionsafter

label militarycamp01tulia_about_ruinedvillage01: # “Do you have an idea about what happened to the ruined village in the west?”
    menu:
        '“Nah, there were goblins around the walls, so we never went there. But I was told that the wrath of the herds crushed it... maybe ten years ago?” Her companion agrees with a nod. “If there were any survivors, they are surely gone by now.”
        '
        '“Maybe they moved to other settlements, or left the peninsula.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe they moved to other settlements, or left the peninsula.”')
            $ custom1 = "“Or they got caught by bandits.”"
            jump militarycamp01regularquestionsafter

label militarycamp01tulia_about_banditsALL: # “Have you ever encountered the bandits from the North?”
    label militarycamp01tulia_about_bandits01: # “Have you ever encountered the bandits from the North?”
        menu:
            'She lets out a sad sigh. “So there {i}are{/i} other bandits in the woods after all.”
            \n\nHer companion hits his forehead with his palm. “This peninsula really hates us. We can’t make a dent in its shell.”
            \n\n{color=#f6d6bd}Tulia{/color} puts a hand on his shoulder, then looks back at you. “Thanks for telling us, roadwarden. If I survive long enough to report to someone, I’ll be sure to mention it.”
            '
            '“Nice acting, but I spoke with {color=#f6d6bd}Glaucia{/color}. You’re working with her.”' if tulia_about_bandits1 and description_tulia05 and not tulia_about_bandits2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Nice acting, but I spoke with {color=#f6d6bd}Glaucia{/color}. You’re working with her.”')
                $ tulia_about_bandits2 += 1
                jump militarycamp01tulia_about_bandits02
            '“Good idea.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Good idea.”')
                jump militarycamp01regularquestions
            '“Maybe I should learn more about them first.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe I should learn more about them first.”')
                $ custom1 = "“Sure... Good luck with that,” {color=#f6d6bd}the man with a bird{/color} chuckles."
                jump militarycamp01regularquestionsafter

    label militarycamp01tulia_about_bandits02:
        menu:
            'While {color=#f6d6bd}Tulia{/color} doesn’t respond right away, her companion spreads his arms like a bear pretending to be larger. “Why would you trust some highwaymen? Whoever this {color=#f6d6bd}Glaucia{/color} is, she tries to sow discord, that’s obvious.”
            '
            '“Come on, now. This is the only pass through {color=#f6d6bd}Hag Hills{/color}. Recently, there’s been a caravan with tools and spices that was taken by force, to be sold for ransom. {i}Someone{/i} told them to turn east, right into the band’s trap. You want me to believe you bear no responsibility, and saw nothing?”' if tulia_about_bandits2 and glaucia_about_lostmerchants_trail and not tulia_about_bandits3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Come on, now. This is the only pass through {color=#f6d6bd}Hag Hills{/color}. Recently, there’s been a caravan with tools and spices that was taken by force, to be sold for ransom. {i}Someone{/i} told them to turn east, right into the band’s trap. You want me to believe you bear no responsibility, and saw nothing?”')
                $ tulia_about_bandits3 += 1
                jump militarycamp01tulia_about_bandits03
            'I give him a grim look, but say nothing.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give him a grim look, but say nothing.')
                jump militarycamp01regularquestions

    label militarycamp01tulia_about_bandits03:
        menu:
            '“It’s not so simple,” she drawls out her words. “I wasn’t looking for dragon bones or mead. Without {color=#f6d6bd}Glaucia{/color}, my {i}squad{/i},” she looks around, as if to find her subordinates, “would never be able to keep the valley passable. On the day of your arrival, she helped us get rid of a griffon that murdered two people this summer alone. Was I afraid of her threats? Sure. But she helped me save lives, too.”
            '
            'I meet her eyes. “You are not some coerced civilian who just happened to help a group of outlaws. People trusted you with their lives, and you betrayed them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I meet her eyes. “You are not some coerced civilian who just happened to help a group of outlaws. People trusted you with their lives, and you betrayed them.”')
                $ tulia_friendship -= 1
                $ custom1 = "She frowns, but her voice is quiet. “Why are you telling me this?”"
                jump militarycamp01tulia_about_bandits04
            'I nod slowly. “You didn’t have a choice. I carry a share of hard decisions on my shoulders as well.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod slowly. “You didn’t have a choice. I carry a share of hard decisions on my shoulders as well.”')
                $ tulia_friendship += 1
                $ tulia_about_bandits_grateful = 1
                $ custom1 = "She lets out a relieved sigh. “Thank you. For trying to understand us.”"
                jump militarycamp01regularquestionsafter
            'I look away. “How do you think The Wright would respond to your excuses?”' if (pc_faithpoints >= 5 and pc_religion == "theunitedchurch") or (pc_faithpoints >= 6 and pc_religion == "ordersoftruth") or (pc_faithpoints >= 4 and pc_religion == "fellowship"):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look away. “How do you think The Wright would respond to your excuses?”')
                $ pc_faithpoints += 1
                $ custom1 = "She looks down. “It felt like I had no other choice. All I can do is pray for forgiveness.”"
                jump militarycamp01tulia_about_bandits04

    label militarycamp01tulia_about_bandits04:
        menu:
            '[custom1]
            '
            '“Once I’m back in the city, I’ll be forced to report this to the commanders. Better think how to justify yourself to the judge.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Once I’m back in the city, I’ll be forced to report this to the commanders. Better think how to justify yourself to the judge.”')
                $ tulia_about_bandits_hopeless = 1
                $ minutes += 5
                $ custom1 = "She taps the hilt of her sword, but gives you no other answer. Her shoulders are tense, and the wider the silence between you grows, the more convinced you are she won’t return to the city after all."
                jump militarycamp01regularquestionsafter
            '“I’m willing to keep this conversation between us, but not for free. I may need your help in the future. Either somewhere in the peninsula, or back in the city.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m willing to keep this conversation between us, but not for free. I may need your help in the future. Either somewhere in the peninsula, or back in the city.”')
                $ custom1 = "She straightens up, giving you an angry look, and nods briefly. “So this is how it’s going to be. So be it. {i}I’m in your debt{/i},” she says as if it’s a spell, but not without a hint of mockery."
                $ tulia_about_bandits_indebt = 1
                jump militarycamp01regularquestionsafter
            '(lie) “Your secret is safe with me, but I hope you’ll return the favor. I may need your help in the future.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “Your secret is safe with me, but I need you to return the favor. I may need your help in the future.”')
                $ custom1 = "She straightens up, giving you an angry look, and nods briefly. “So this is how it’s going to be. So be it. {i}I’m in your debt{/i},” she says as if it’s a spell, but not without a hint of mockery."
                $ pc_lies += 2
                $ tulia_about_bandits_indebt = 1
                $ tulia_about_bandits_liedto = 1
                jump militarycamp01regularquestionsafter

label militarycamp01regularadditionalquestion01:
    $ foragers_caius_heardabout += 1
    menu:
        '{color=#f6d6bd}The man{/color} shrugs. “Bandits happened. And monsters.”
        \n\n“A {i}strong{/i} band, though,” {color=#f6d6bd}his companion{/color} chips in. “When we got to the peninsula in spring, we saw some people living in this camp. The old lieutenant decided to avoid it, and look for an inn. We had to travel through the night for a bit,” {color=#f6d6bd}the bearded soldier{/color} scoffs and crosses his arms, but she carries on. “If he had decided otherwise, we would all have died that day. {color=#f6d6bd}The innkeeper{/color} explained that the camp is a trap, that the armed ones pretend to be soldiers. Stay there at night, lose everything you have.”
        '
        '“Sounds like slave hunters.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What did they do with those who came? Murdered them in their sleep?”')
            menu:
                '{color=#f6d6bd}Tulia{/color} sighs. “Very much so. They killed some, and took others away, who knows where. They were letting the northerners go, hoping to avoid their wrath.”
                \n\n“It kind of worked,” adds {color=#f6d6bd}the soldier{/color}. “We asked them for help, but they refused. We had to clear the entire camp on our own, and that’s why three of our people died.”
                \n\n“Don’t exaggerate, it’s not like the lieutenant didn’t make a mistake. He wanted to get rid of them and take over their camp, but we didn’t know our enemy well enough. We were outnumbered, and they had an ice mage among them.” She looks at you. “At least we cleared the road. Saved lives.”
                '
                '“You mentioned monsters as well?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You mentioned monsters as well?”')
                    menu:
                        '“Nothing that would surprise you. Those of us who survived the skirmish were young. Too inexperienced to spend a summer in this place without a good leader, and they didn’t trust me. One of them got caught by a treant. Another one ignored my orders to perform some sort of a ritual hunt, so a werebear tore her to pieces. The last one tried to act tough, didn’t tell us that he had cut his hand while cleaning his gambeson,” she lets out a ghastly chuckle. “We had to cut it off, and he was so ashamed that decided to walk north, find a new life, disappear. Idiot.”
                        \n\n“What a colorful journey,” {color=#f6d6bd}the soldier{/color} whistles a sad melody.
                        '
                        '“You’ve made this place safer.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’ve made this place safer.”')
                            menu:
                                '“Barely.” {color=#f6d6bd}Tulia{/color} seems tired. “And who knows if it was worth the lives and effort.”
                                '
                                '“Sure.”':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure.”')
                                    jump militarycamp01regularquestions
                        'I stay silent.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay silent.')
                            jump militarycamp01regularquestions

label militarycamp01tulia_about_caius_spokento01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Guess what. I met with {color=#f6d6bd}Caius{/color}.”')
    $ tulia_friendship += 1
    $ tulia_about_caius_spokento = 1
    menu:
        'You mention the tavern and {color=#f6d6bd}Foggy’s{/color} care. {color=#f6d6bd}Tulia{/color} sighs with relief and rests her hands on her sides. “Alive... That’s good to hear, deserter or not. How’s he doing?”
        '
        '“He’s a man of faith now. Kind of.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He’s a man of faith now. Kind of.”')
            $ custom1 = "You vaguely describe what you’ve heard, making her scratch her shaved head. “That’s news to me. I used to know him before he joined the army. Never seemed especially bothered with Wright’s teachings. One time I saw him with that...” She freezes, then lets out a chuckle. “Forget it. I’m glad he’s alright.”"
            jump militarycamp01regularquestionsafter
        '“He’s insane.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He’s insane.”')
            $ custom1 = "You vaguely describe what you’ve heard, making her shoulders slump. “At least he’s still here... So many things turned against him, and {i}I’m{/i} to blame for it, together with many others. Before he joined the army, he always had something to say. In violent ways, true, but was a brisk soul. Now he would live on the street, without help or mercy. Good thing he found a new home,” her voice weakens."
            jump militarycamp01regularquestionsafter
        '“The people around him try to put him to good use. His soul is healing, even if slowly.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The people around him try to put him to good use. His soul is healing, even if slowly.”')
            $ custom1 = "You describe what you’ve seen, making her reach behind her head and take a deep breath. “Guess I ought to be a bit less angry thinking about my squad, though that’s quite a request,” she chuckles. “I’m so glad he found kindness in this land. I wish he didn’t have to look for it, though.”"
            jump militarycamp01regularquestionsafter

label militarycamp01regularadditionalquestion02:
    menu:
        '“That’s not much of a story, honestly,” she looks at her hand, which is currently resting on her hilt. “In the city there’s a strict order of, what should I call it?” She exchanges looks with her companion, but he can’t help her. “Well, {i}leadership succession{/i}, I guess. {color=#f6d6bd}Hovlavan{/color} chief selects commanders, those select lieutenants, and those put their soldiers in order of priority. If a lieutenant dies, they get replaced by the next soldier in line.”
        '
        '“So you were his successor?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you were his successor?”')
            jump militarycamp01regularadditionalquestion02p02

    label militarycamp01regularadditionalquestion02p02:
        menu:
            '“Nah, not exactly. When we fought the bandits, our lieutenant was hit by a slingshot. His boyfriend jumped to help him, but failed to protect either of them from a spell. It was like a ball of ice that hung above them and exploded, piercing their heads, completely avoiding their shield. Really unpleasant.”
            \n\nShe pauses.
            '
            '“And you were the third one in line, is that right?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And you were the third one in line, is that right?”')
                jump militarycamp01regularadditionalquestion02p03
            '“Jumping in like that to save a man in the middle of an attack... Doesn’t sound like a wise decision.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Jumping in like that to save a man in the middle of an attack... Doesn’t sound like a wise decision.”')
                jump militarycamp01regularadditionalquestion02p03b

    label militarycamp01regularadditionalquestion02p03b:
        menu:
            '“I agree, but so what? He’s dead, I doubt he’s going to learn much from scolding.”
            '
            '“And you were the third one in line, is that right?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And you were the third one in line, is that right?”')
                jump militarycamp01regularadditionalquestion02p03

    label militarycamp01regularadditionalquestion02p03:
        $ description_tulia02 = "She didn’t expect to become a lieutenant and most members of her squad are already dead."
        menu:
            '“Basically, yeah,” she says without enthusiasm. “I didn’t plan to become a leader, though. I’ll get demoted once we return to the city. I prefer to follow anyway.”
            '
            'After another pause, I decide it’s a good moment to change the topic.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- After another pause, I decide it’s a good moment to change the topic.')
                jump militarycamp01regularquestions

label militarycamp01regularadditionalquestion03:
    menu:
        '{color=#f6d6bd}The lieutenant{/color} looks into your eyes. “You know. The usual. Making the roads safe. Keeping people alive.”
        '
        'I explain that it may be important for me to know what they’ve tried to accomplish.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I explain that it may be important for me to know what they’ve tried to accomplish.')
            jump militarycamp01regularadditionalquestion03p02

    label militarycamp01regularadditionalquestion03p02:
        if tulia_friendship >= 3:
            $ description_tulia04 = "Her squad was meant to find a fitting place for a new outpost."
            menu:
                '“I can’t really tell you... Let’s just say it would be nice to have a {i}reliable{/i} outpost somewhere nearby. A place where you can always find a group of fighters willing to protect you in the name of the law,” she tilts her head back. “Now, if you have any other questions...”
                '
                'I change the topic.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I change the topic.')
                    jump militarycamp01regularquestions
        else:
            menu:
                '“I can’t really tell you,” you sense no hesitation. “Do you have any other questions?”
                '
                'I change the topic.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I change the topic.')
                    jump militarycamp01regularquestions

label militarycamp01regularadditionalquestion04:
    menu:
        'The story is brief. Some merchants built the camp to have an extra stop for mules and donkeys, just between the inn and the southern villages. There’s plenty of grass here, and a pond nearby.
        \n\nWhen the peninsula grew more dangerous, the camp stood abandoned, from time to time serving as a shelter for travelers. The bandits came here in spring, further paralyzing the exchange of information between the northern and southern settlements.
        \n\nSince these highwaymen are no more, the situation may reverse. Time will tell.
        '
        '{color=#f6d6bd}Hovlavan{/color} would need more people who’d be willing to get rid of the local threats.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {color=#f6d6bd}Hovlavan{/color} would need more people who’d be willing to get rid of the local threats.')
            jump militarycamp01regularquestions

label militarycamptulia_about_nomoreundeadALL:
    label militarycamptulia_about_nomoreundead01:
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
                jump militarycamp01regularquestionsafter

    label militarycamptulia_about_nomoreundead02:
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
                jump militarycamp01regularquestionsafter

    label militarycamptulia_about_nomoreundead03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The village of {color=#f6d6bd}White Marshes{/color} is no more. The North will now struggle with a large group of undead.”')
        $ tulia_about_nomoreundead += 1
        $ tulia_friendship += 1
        $ minutes += 5
        menu:
            '“How did that happen?” Her voice is close to a shout. “Did the necromancers lose their wits?” You think about the answer, explaining only the most essential parts of what happened. {color=#f6d6bd}Tulia{/color} seeks lies in your eyes, but finally shrugs. “No matter how many times priests tell us that we ought to stay away from dark magic, there’s always someone not willing to listen, but ready to hurt everyone around them. Let’s hope that {color=#f6d6bd}Hovlavan{/color} will send here a squad or two before winter.”
            '
            '“Yeah. Let’s.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah. Let’s.”')
                jump militarycamp01regularquestions

label militarycamp01aboutasterion01ALL:
    label militarycamp01aboutasterion01:
        $ quarters += 2
        menu:
            '{color=#f6d6bd}Tulia{/color} rubs her hands. “Surprise me.”
            \n\nYou both sit down at the table, with the other soldier standing nearby, listening to your tale about clues and rumors, the old tribes, and the awakened corpse.
            \n\n{color=#f6d6bd}Tulia{/color} doesn’t interrupt you, nodding as she’s keenly observing your gestures.
            \n\nShe ponders for a bit, looking at the gate. “So, what do you make of it? Not the brightest death I could wish for someone.”
            '
            '“He knew the danger, but took the risk anyway. A fair end to his journey.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He knew the danger, but took the risk anyway. A fair end to his journey.”')
                menu:
                    '“You two had this in common. {i}I{/i} wouldn’t travel to a wild island.” Her smile turns into a chuckle. “You’re lucky to still be here!”
                    '
                    '“That’s the only way to get somewhere in life.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the only way to get somewhere in life.”')
                        $ asterion_found_pcthought = "readyforanadventure"
                        jump militarycamp01tuliaaboutasterion2pcfoundhimaa
                    '“Yeah... From now on, I’ll stay on the roads.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah... From now on, I’ll stay on the roads.”')
                        $ asterion_found_pcthought = "readytoplayitsafe"
                        jump militarycamp01tuliaaboutasterion2pcfoundhimab
                    'I smirk. “Says the gal who spent half a year in this shithole.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smirk. “Says the gal who spent half a year in this shithole.”')
                        menu:
                            '“Ha, I know!” Her laughter starts strong, but gets cut by a harsh cough. “I trusted my group too much, but that’s still a safer bet than risking your head.”
                            '
                            '“That’s the only way to get somewhere in life.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the only way to get somewhere in life.”')
                                $ asterion_found_pcthought = "readyforanadventure"
                                label militarycamp01tuliaaboutasterion2pcfoundhimaa: #“That’s the only way to get somewhere in life.”
                                    menu:
                                        '“Spoken like a true adventurer,” she scratches the back of her head. Her hair has started to show. “And you’re not going to stay here for long. A roadwarden who wants to stay alive needs to know how to say {i}no{/i} to their ambitions... Yet I bet that once you get used to these roads, you’ll get bored of them.”
                                        '
                                        '“Well, that’s surely possible.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Well, that’s surely possible.”')
                                            jump militarycamp01tuliaaboutasterion03gettingreward
                            '“Yeah... From now on, I’ll stay on the roads.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yeah... From now on, I’ll stay on the roads.”')
                                $ asterion_found_pcthought = "readytoplayitsafe"
                                label militarycamp01tuliaaboutasterion2pcfoundhimab: #“Yeah. That was pretty damn stupid of me. From now on, I’ll stay on the roads.”
                                    menu:
                                        '“Well, at least your bravery didn’t go to waste! {color=#f6d6bd}Asterion’s{/color} family won’t be happy to hear the news, but they’ll be able to move on now. Good job, it would be a waste to lose your potential. Better take care of yourself.”
                                        '
                                        '“That’s the plan.”':
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the plan.”')
                                            jump militarycamp01tuliaaboutasterion03gettingreward
            '“He was biting off more than he could chew. Now his kids will face the consequences.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He was biting off more than he could chew. Now his kids will face the consequences.”')
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
                                jump militarycamp01tuliaaboutasterion03gettingreward
                    '“And I almost repeated it. I’ll try to play it safe, from now on.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And I almost repeated it. I’ll try to play it safe, from now on.”')
                        $ asterion_found_pcthought = "readytoplayitsafe"
                        menu:
                            '“Well, at least {i}your{/i} bravery didn’t go to waste! {color=#f6d6bd}Asterion’s{/color} family won’t be happy to hear the news, but thanks to you, they can start to heal. Now we need {i}you{/i} to take care of yourself. You’ve got potential.”
                            '
                            '“That’s the plan.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the plan.”')
                                jump militarycamp01tuliaaboutasterion03gettingreward
            '“I don’t know what to think. I’d like to learn his own perspective.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t know what to think. I’d like to learn his own perspective.”')
                menu:
                    'She sighs. “Well, we won’t read his soul. Let it go, it’s in the past now.”
                    '
                    '“His death seems so... pointless, now.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “His death seems so... pointless, now.”')
                        $ asterion_found_pcthought = "annoyedwithunsolvedmystery"
                        menu:
                            'Her sad eyes betray her nonchalant voice. “The Wright and nature take us without a reason.”
                            '
                            '“I guess.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I guess.”')
                                jump militarycamp01tuliaaboutasterion03gettingreward
                    '“You’re right. I’ll be fine.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re right. I’ll be fine.”')
                        $ asterion_found_pcthought = "readytoletthemysterygo"
                        menu:
                            '“{color=#f6d6bd}Asterion’s{/color} family won’t be happy to hear the news, but thanks to you, they can start to heal. Now we need {i}you{/i} to take care of yourself. You’ve got potential.”
                            '
                            '“That’s the plan.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s the plan.”')
                                jump militarycamp01tuliaaboutasterion03gettingreward
            '“He made a mistake, that’s all. It has nothing to do with me.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “He made a mistake, that’s all. It has nothing to do with me.”')
                menu:
                    '“Just another job for you, isn’t it?”
                    '
                    '“That’s right.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s right.”')
                        $ asterion_found_pcthought = "doesntcareatall"
                        jump militarycamp01tuliaaboutasterion03gettingreward
                    '“And just another dead traveler.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And just another dead traveler.”')
                        $ asterion_found_pcthought = "doesntcareatall"
                        menu:
                            '“Well, won’t argue with that,” she rests her hand on the hilt of her sword. “I doubt his family will share your sentiment.”
                            '
                            '“Fair enough.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fair enough.”')
                                jump militarycamp01tuliaaboutasterion03gettingreward
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
                        jump militarycamp01tuliaaboutasterion03gettingreward

    label militarycamp01tuliaaboutasterion03gettingreward:
        menu:
            'She stretches out, heads for her tent, and brings you a few items. There’s enough of them to make her stumble, but she covers her embarrassment with a chuckle. “Well, this is my part of the deal!”
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
                        $ renpy.notify("Quest completed: Find the Roadwarden\nYou received Asterion’s equipment.")
                        $ quest_asterion = 2
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Find the Roadwarden. You received Asterion’s equipment.{/i}')
                        $ quest_asterion_description00goodresult = "I collected my reward from {color=#f6d6bd}Tulia{/color}."
                        menu:
                            '{color=#f6d6bd}[horsename]{/color} spares you a glance as you reach toward your bundles, but then returns to its nap.
                            \n\nYou take a deep breath. You could have taken the easy way out, but you didn’t. Your back, buttocks, and legs are aching from the long journey. The first night you spent on the peninsula could be a lifetime ago.
                            \n\nYet you’re still here. And who knows - maybe even rich.
                            '
                            'I return to {color=#f6d6bd}Tulia{/color}.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}Tulia{/color}.')
                                jump militarycamp01regularquestions

##################

label prolcamp01regularaftersleeping:
    $ militarycamp_fluff = renpy.random.choice(['A monkey, not larger than your head, with brown and yellow fur, is running on the beams of the wall, but disappears once it notices your gaze.', 'You see a gray hawk soaring through the blue sky. It’s so far from you that you struggle to estimate its size.', 'A green field mouse is foraging in the grass, unaware that you’ve noticed it.'])
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.music.play("audio/track_18military.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    if day == 1:
        if quarters < (world_daylength-20):
            show areapicture prologuemilitarycampscrap04 at basicfade
        else:
            show areapicture prologuemilitarycampscrap06 at basicfade
    elif day <= 5:
        show areapicture prologuemilitarycampscrap06 at basicfade
    else:
        show areapicture prologuemilitarycampscrap04nofire at basicfade
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    menu:
        'Your back begs you to stand up. [militarycamp_fluff] You prepare {color=#f6d6bd}[horsename]{/color} for the journey ahead.
        '
        'I approach {color=#f6d6bd}Tulia{/color}.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Tulia{/color}.')
            jump militarycamp01regularquestions
        'I approach the barrel with water.':
            jump militarycampbath01
        # 'I won’t get much cleaner at the barrel. (disabled)' if (cleanliness_equipment < 3 and cleanliness > 0) or (cleanliness_equipment >= 3 and cleanliness > 1):
        #     pass
        'I’m ready to go. (disabled)':
            pass

label militarycamp01regularnothingelsetodo:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if quarters >= (world_daylength-4):
        menu:
            'You’re ready to prepare your sleeping spot.
            '
            'I approach {color=#f6d6bd}Tulia{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Tulia{/color}.')
                jump militarycamp01regularquestions
            'I approach the barrel with water.':
                jump militarycampbath01
            # 'I won’t get much cleaner at the barrel. (disabled)' if (cleanliness_equipment < 3 and cleanliness > 0) or (cleanliness_equipment >= 3 and cleanliness > 1):
            #     pass
            'It’s time to sleep. (disabled)':
                pass
    else:
        menu:
            'You’re ready for the further journey.
            '
            'I approach {color=#f6d6bd}Tulia{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Tulia{/color}.')
                jump militarycamp01regularquestions
            'I approach the barrel with water.':
                jump militarycampbath01
            # 'I won’t get much cleaner at the barrel. (disabled)' if (cleanliness_equipment < 3 and cleanliness > 0) or (cleanliness_equipment >= 3 and cleanliness > 1):
            #     pass
            'I’m ready to go. (disabled)':
                pass

label militarycampbath01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the barrel with water.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if cleanliness_equipment <= 0:
        $ custom1 = "{color=#6a6a6a}You need at least 2 pieces of bathing equipment to get more out of this place.{/color}"
        $ custom2 = ""
    elif cleanliness_equipment == 1:
        if item_soap:
            $ custom1 = "The oak-ash soap you own is not enough to help you get cleaner."
        elif item_teethset:
            $ custom1 = "The teeth set you own is not enough to help you get cleaner."
        elif item_perfume:
            $ custom1 = "The perfume you own is not enough to help you get cleaner."
        $ custom2 = "\n\n{color=#6a6a6a}You need 2 pieces of bathing equipment to get more out of this place.{/color}"
    elif cleanliness_equipment == 2:
        if item_soap and item_teethset:
            $ custom1 = "The oak-ash soap and the teeth set you own can help you get cleaner."
        elif item_soap and item_perfume:
            $ custom1 = "The oak-ash soap and the perfume you own can help you get cleaner."
        elif item_teethset and item_perfume:
            $ custom1 = "The teeth set and the perfume you own can help you get cleaner."
        $ custom2 = "\n\n{color=#6a6a6a}This spot is already as helpful as it can get.{/color}"
    elif cleanliness_equipment >= 3:
        $ custom1 = "The oak-ash soap, the teeth set, and the perfume you own can help you get cleaner."
        $ custom2 = "\n\n{color=#6a6a6a}This spot is already as helpful as it can get.{/color}"
    menu:
        'The barrel was recently refilled by the soldiers. You fish out the few drifting insects.
        \n\n[custom1][custom2]
        '
        'I wash my hands, face, and neck.' if (cleanliness < 1 and cleanliness_equipment < 2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my hands, face, and neck.')
            jump militarycampbath02
        'I wash my shell.' if (cleanliness < 2 and cleanliness_equipment >= 2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
            jump militarycampbath02
        'I won’t get any cleaner here. (disabled)' if cleanliness == 2:
            pass
        'I’m as clean as I can get. (disabled)' if cleanliness == 3:
            pass
        'I step away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
            jump militarycamp01regularnothingelsetodo

    label militarycampbath02:
        if not cleanliness:
            if cleanliness_equipment >= 2:
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness+2)
                show plus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 appearance points.{/i}')
            else:
                $ minutes += 10
                $ cleanliness = limit_cleanliness(cleanliness+1)
                show plus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance points.{/i}')
        elif cleanliness == 1:
            $ minutes += 10
            $ cleanliness = limit_cleanliness(cleanliness+1)
            show plus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        menu:
            'You draw water with your hands to splash your skin.
            '
            'I wash my hands, face, and neck.' if (cleanliness < 1 and cleanliness_equipment < 2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my hands, face, and neck.')
                jump militarycampbath02
            'I wash my shell.' if (cleanliness < 2 and cleanliness_equipment >= 2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
                jump militarycampbath02
            'I won’t get any cleaner here. (disabled)' if cleanliness == 2:
                pass
            'I’m as clean as I can get. (disabled)' if cleanliness == 3:
                pass
            'I step away.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump militarycamp01regularnothingelsetodo

label militarycamp_destroyedALL:
    label militarycamp_destroyed01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show areapicture militarycamptosoutherncrossroads at basicfade
        menu:
            'The road is covered with paw prints. From time to time you spot blood stains, spit out by someone with deep wounds. The black carrion eaters are circling ahead, above the camp.
            '
            'I may need to turn around.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may need to turn around.')
                show areapicture prologuemilitarycampdestroyed01 at basicfade
                $ militarycamp_destroyed = 1
                $ militarycamp_destroyed_firsttime = 1
                if militarycamp_destroyed_firsttime_tulia:
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                menu:
                    'You don’t reach the walls. The carcass is serving as a feast to birds and dragonlings, a few of which are resting on the ground, waiting for the next wave of hunger. One of them gets back on its paws, giving you a warning stare.
                    \n\nThe path of the troll’s charge is marked with broken arrows and puddles of blood. The soldiers fought bravely, but the camp will be of no use until someone arrives here with a wagon of timber.
                    '
                    'I better ride to the inn.' if world_endmode:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better ride to the inn.')
                        $ travel_destination = "peltnorth"
                        jump finaldestinationafterevent
                    'Maybe the trail west will lead me to any survivors.' if not militarycamp_destroyed_firsttime_tulia and not world_endmode:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe the trail west will lead me to any survivors.')
                        $ travel_destination = "peltnorth"
                        jump finaldestinationafterevent
                    'Time to get out of here. (disabled)' if militarycamp_destroyed_firsttime_tulia:
                        pass
