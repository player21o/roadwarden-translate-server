default eudocia_invitation_attempt = 0
default eudocia_invitation_attempt_inprogress = 0
default eudocia_invitation_success = 0

default eudocia_invitation_argument_points = 0
default eudocia_invitation_argument_points_threshold = 25

default eudocia_invitation_argument_monks1 = 0
default eudocia_invitation_argument_monks2 = 0
default eudocia_invitation_argument_asterion = 0
default eudocia_invitation_argument_enchanting = 0
default eudocia_invitation_argument_eudociaflower = 0
default eudocia_invitation_argument_threats = 0
default eudocia_invitation_argument_threats_points = 0
default eudocia_invitation_argument_support = 0

label eudocia_about_invitation00:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe it’s the right time to offer her work in the city.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    menu:
        'You glance at her absent eyes. She has shown you signs of trust, but you won’t convince her with just a smile. The more you’ll learn about the peninsula, the more arguments you’ll have at your disposal.
        '
        'I’m not ready yet.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not ready yet.')
            if pc_area == "eudociahouse":
                $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ questionpreset = "eudocia1"
            menu:
                'She doesn’t interrupt the silence.
                '
                '(eudocia1 set)':
                    pass
        '“I’ve something important to discuss.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve something important to discuss.”')
            jump eudocia_about_invitation01

label eudocia_about_invitationALL:
    label eudocia_about_invitation01:
        $ eudocia_invitation_attempt = 1
        if pc_area == "eudociahouse":
            $ eudocia_fluff_inorout = "She takes a deep breath and looks at your ear, frowning."
        if pc_area == "eudociahouseinside":
            $ eudocia_fluff_inorout = "She puts her stuff away and looks at your ear, frowning."
        $ at_activate = 1
        $ at = 0
        menu:
            '[eudocia_fluff_inorout] “Are ye taking off ya mask?”
            '
            ' (disabled)' ( condition="at == 0" ):
                pass
            'I smile. “I’ve a good offer for you.”' ( condition="at == 'friendly'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - I smile. “I’ve a good offer for you.”')
                $ custom1 = "“Good for {i}someone{/i}, but my soul has neither great needs, nor appetite.” An awkward pause. “Take a walk with me. I want to stretch my legs.”"
                $ eudocia_friendship += 0
                jump eudocia_about_invitation02
            '“It’s getting cold. I’d rather keep my clothes on.”' ( condition="at == 'playful'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “It’s getting cold. I’d rather keep my clothes on.”')
                $ custom1 = "Her grimace of disgust makes you move away. “Don’t even try it. And just in case, take a walk with me. Just so ye don’t get {i}too{/i} comfortable.”"
                $ eudocia_friendship -= 1
                jump eudocia_about_invitation02
            '“I simply think it’s a good moment to have an honest conversation about our shared efforts.”' ( condition="at == 'distanced'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “I simply think it’s a good moment to have an honest conversation about our shared efforts.”')
                $ custom1 = "“It may be,” she says slowly, “and I guess it means ye’re leaving soon. Come, take a walk with me."
                $ eudocia_friendship += 1
                jump eudocia_about_invitation02
            '“I don’t have much time left. Use your opportunity while you have it.”' ( condition="at == 'intimidating'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “I don’t have much time left. Use your opportunity while you have it.”')
                $ custom1 = "“Ye speak as if ye’re doing me a favor, but my soul has neither great needs, nor appetite.” An awkward pause. “Take a walk with me. I want to stretch my legs.”"
                $ eudocia_friendship += 0
                jump eudocia_about_invitation02
            '“As much as one can.”' ( condition="at == 'vulnerable'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - “As much as one can.”')
                $ custom1 = "“I doubt it. {i}I{/i}, for example, have got no trouble speaking to ye as I would to myself. I don’t say {i}everything{/i}, maybe, but my tongue is honest.”\n\nAn awkward pause. “Take a walk with me. I’m sick of these walls.”"
                $ eudocia_friendship -= 1
                jump eudocia_about_invitation02

    label eudocia_about_invitation02:
        $ at_activate = 0
        $ at = 0
        menu:
            '[custom1]
            '
            'While we’re heading toward the gate, I tell her about my deal with the guild.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- While we’re heading outside, I tell her about my deal with the guild.')
                jump eudocia_about_invitation_arguments01

label eudocia_about_invitation_argumentsALL:
    label eudocia_about_invitation_arguments01:
        $ pc_area = "eudociahouse"
        $ eudocia_invitation_attempt_inprogress = 1
        hide golem01
        hide golem02
        hide eudocia_image_eyes
        if eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            show areapicture watchtowertoeudocia2_fixed at basicfade
        else:
            show areapicture watchtowertoeudocia2 at basicfade
        $ minutes += 5
        $ questionpreset = "eudocia2"
        stop music fadeout 4.0
        play nature "audio/ambient/eudociadiscussionlake01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        menu:
            'You mention the merchants, the officials, and the high status of the enchanters among the cityfolk. She lets you speak without interruption, observing the surroundings. Still barefoot and with a worn robe, she looks like a cook in an herbal garden.
            \n\nYou approach the pond and she takes a deep breath. The geese in the distance are as gray as her irises. “We’re just in time, the air is still fresh,” her tone is hard to decipher, and she keeps taking long pauses. “I’ve built so much, and over so many years. Now ye want me to tie myself to some coin holders? Or even worse, to leave all this,” she waves toward her residence, “behind?”
            '
            '(eudocia2 set)':
                pass

    label eudocia_about_invitation_arguments_monksALL:
        label eudocia_about_invitation_arguments_monks01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you be sure {color=#f6d6bd}the monks{/color} won’t turn their neighbors against you?”')
            $ eudocia_invitation_argument_monks1 = 1
            $ eudocia_invitation_argument_points += 2
            $ eudocia_about_monks = 1
            $ minutes += 2
            $ questionpreset = "eudocia2"
            menu:
                'She cocks her head to the side. “So far, they’ve done naught to hurt me. I went as far away from them as I could have. I bother no one.”
                '
                '(eudocia2 set)':
                    pass

        label eudocia_about_invitation_arguments_monks02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yet {color=#f6d6bd}Aeli{/color} is already scheming against you. He wanted me to spy on your golems, find their weaknesses.”')
            $ eudocia_invitation_argument_monks2 = 1
            $ monastery_betrayal_done = 1
            $ eudocia_invitation_argument_points += 5
            menu:
                'Her voice cracks. “Did ye?”
                '
                '“In a way.”' if aeli_golems_clues_counter and not quest_studyingthegolems_description06:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “In a way.”')
                    $ custom1 = "She turns away, leading you further up the bank."
                    $ eudocia_friendship -= 1
                    jump eudocia_about_invitation_arguments_monks03
                '(lie) “Of course not.”' if aeli_golems_clues_counter and not quest_studyingthegolems_description06:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “Of course not.”')
                    $ custom1 = "She sizes you up, then looks at the clouds and takes a step back. The hint of gratitude in her eyes is hidden beneath the sorrow."
                    $ pc_lies += 1
                    jump eudocia_about_invitation_arguments_monks03
                '“Yes.”' if quest_studyingthegolems_description06:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yes.”')
                    $ custom1 = "She turns away, leading you further up the bank."
                    $ eudocia_friendship -= 1
                    jump eudocia_about_invitation_arguments_monks03
                '(lie) “No.”' if quest_studyingthegolems_description06:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “No.”')
                    $ custom1 = "She sizes you up, then looks at the clouds and takes a step back. The hint of gratitude in her eyes is hidden beneath the sorrow."
                    $ pc_lies += 2
                    jump eudocia_about_invitation_arguments_monks03
                '“I told him nothing.”' if not aeli_golems_clues_counter:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I told him nothing.”')
                    $ custom1 = "She sizes you up, then looks at the clouds and takes a step back. The hint of gratitude in her eyes is hidden beneath the sorrow."
                    jump eudocia_about_invitation_arguments_monks03

        label eudocia_about_invitation_arguments_monks03:
            $ questionpreset = "eudocia2"
            $ minutes += 1
            menu:
                '[custom1]
                '
                '(eudocia2 set)':
                    pass

    label eudocia_about_invitation_arguments_asterion01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know how easy it is to suddenly disappear in this land. Just think about {color=#f6d6bd}Asterion{/color}.”')
        $ eudocia_invitation_argument_asterion = 1
        $ minutes += 1
        $ questionpreset = "eudocia2"
        if eudocia_about_asterion_found:
            $ custom1 = "“I’d rather not,” she rubs her arms above her elbows, as if to warm herself up. “I’m just glad ye were able to find him, that’s all.”"
            if eudocia_about_asterion_cloak_lied:
                $ eudocia_invitation_argument_points += 6
            elif eudocia_about_asterion_cloak:
                $ eudocia_invitation_argument_points += 5
            else:
                $ eudocia_invitation_argument_points += 4
        else:
            $ custom1 = "“I’d rather not,” she rubs her arms above her elbows, as if to warm herself up. “I just hope he’s alright.”"
            if eudocia_about_asterion_cloak_lied:
                $ eudocia_invitation_argument_points += 4
            elif eudocia_about_asterion_cloak:
                $ eudocia_invitation_argument_points += 3
            else:
                $ eudocia_invitation_argument_points += 2
        menu:
            '[custom1]
            '
            '(eudocia2 set)':
                pass

    label eudocia_about_invitation_arguments_enchanting01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know best how much you’ve learned since the day you enchanted that old chisel. In the city, you could speak with other masters, learn how to read scrolls. You’d unlock your potential.”')
        $ eudocia_invitation_argument_enchanting = 1
        $ minutes += 2
        if pc_class == "warrior":
            $ custom1 = "As a soul trained in the blade, you keep your story vague, free of names and places. You describe the golemic limbs aiding workers, candles that last for days, helmets that help sailors talk during storms. She observes the birds flying toward the eastern mountains, listening carefully."
            $ eudocia_invitation_argument_points += 3
        if pc_class == "mage":
            $ custom1 = "You may not know many details about her style of magic, but you’ve met a few respected spellcasters in the city. You mention their comfortable houses, as well as the golemic limbs aiding workers, candles that last for days, helmets that help sailors talk during storms. She observes the birds flying toward the eastern mountains, listening carefully."
            $ eudocia_invitation_argument_points += 4
        if pc_class == "scholar":
            $ custom1 = "Using bits of knowledge you’ve read in the old codices, you mention a few respected enchanters working in the city, as well as their unique interest in magic that helps the fishers and wall builders. You mention the golemic limbs aiding workers, candles that last for days, helmets that help sailors talk during storms. She observes the birds flying toward the eastern mountains, listening carefully."
            $ eudocia_invitation_argument_points += 5
        $ questionpreset = "eudocia2"
        menu:
            '[custom1]
            \n\n“{i}Other masters{/i},” she tastes your words as she repeats them. “I haven’t needed them so far, but...” She doesn’t finish, instead giving you a kind smile.
            '
            '(eudocia2 set)':
                pass

    label eudocia_about_invitation_arguments_eudociaflower00:
        label eudocia_about_invitation_arguments_eudociaflower01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “In {color=#f6d6bd}Hovlavan{/color}, you’d find all the snake bait you need. As well as other entertainments.”')
            $ eudocia_invitation_argument_eudociaflower = 1
            $ eudocia_invitation_argument_points += 2
            $ minutes += 1
            $ questionpreset = "eudocia2"
            menu:
                'She flinches. “It’s not like I smoke it every day,” she picks a reed growing by the bank, examines it for a bit, then throws it into the water. “But I admit finding the flowers isn’t easy.”
                '
                '(eudocia2 set)':
                    pass

        label eudocia_about_invitation_arguments_eudociaflower02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “In {color=#f6d6bd}Hovlavan{/color}, there are countless things to do. Enough to distract you from snake bait.”')
            $ eudocia_invitation_argument_eudociaflower = 1
            $ eudocia_invitation_argument_points += 3
            $ minutes += 1
            $ questionpreset = "eudocia2"
            menu:
                'She flinches, then reaches for the ends of her hair. Her fingers are shaking slightly, and once she realizes you’ve noticed them, she picks up her pace.
                '
                '(eudocia2 set)':
                    pass

    label eudocia_about_invitation_arguments_threats01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The peninsula is a dangerous place, with little help to offer. I know that better than anyone.”')
        $ eudocia_invitation_argument_threats = 1
        if ruinedvillage_truth:
            $ eudocia_invitation_argument_threats_points += 3
            $ custom1 = ", the destruction of {color=#f6d6bd}Steep House{/color}"
        elif ruinedvillage_confront_can:
            $ eudocia_invitation_argument_threats_points += 2
            $ custom1 = ", the collapse of the southern village"
        elif ruinedvillage_firsttime:
            $ eudocia_invitation_argument_threats_points += 1
            $ custom1 = ", the destroyed village by the southern road"
        else:
            $ custom1 = ""
        if whitemarshes_destroyed:
            $ eudocia_invitation_argument_threats_points += 3
            $ custom2 = ", the undead roaming the bogs"
        elif whitemarshes_firsttime and not whitemarshes_nomoreundead:
            $ eudocia_invitation_argument_threats_points += 1
            $ custom2 = ", the undead of {color=#f6d6bd}White Marshes{/color}"
        else:
            $ custom2 = ", the rumors about the undead"
        if militarycamp_destroyed:
            $ eudocia_invitation_argument_threats_points += 2
            $ custom3 = ", the troll from the old camp in {color=#f6d6bd}Hag Hills{/color}"
        else:
            $ custom3 = ""
        if eudocia_about_plague_cured:
            $ eudocia_invitation_argument_threats_points += 2
            $ custom4 = ", the plague"
        elif eudocia_about_plague:
            $ eudocia_invitation_argument_threats_points += 3
            $ custom4 = ", the plague"
        else:
            $ custom4 = ""
        if quest_missinghunters_description01:
            $ eudocia_invitation_argument_threats_points += 2
            $ custom5 = ", the fate of the missing hunters"
        elif quest_missinghunters:
            $ eudocia_invitation_argument_threats_points += 1
            $ custom5 = ", the missing hunters"
        else:
            $ custom5 = ""
        if eudocia_about_bandits:
            $ eudocia_invitation_argument_threats_points += 3
            $ custom6 = ", her own fear of the bandits"
        elif banditshideout_firsttime:
            $ eudocia_invitation_argument_threats_points += 2
            $ custom6 = ", {color=#f6d6bd}Glaucia’s{/color} band"
        elif quest_lostmerchants:
            $ eudocia_invitation_argument_threats_points += 2
            $ custom6 = ", the lost merchants"
        elif banditshideout_bandits_pchearedabout:
            $ eudocia_invitation_argument_threats_points += 1
            $ custom6 = ", the local bandits"
        else:
            $ custom6 = ""
        $ questionpreset = "eudocia2"
        if eudocia_invitation_argument_threats_points >= 12:
            $ custom7 = ". Her shoulders slump. “I know the outside world outgrows me. Why can’t it just stay away?”"
            $ minutes += 4
        elif eudocia_invitation_argument_threats_points >= 7:
            $ custom7 = ". She hesitates still. “I guess I ought to trust ye on this one.”"
            $ minutes += 3
        elif eudocia_invitation_argument_threats_points >= 4:
            $ custom7 = ", but she’s far from convinced. “The wilderness is there, and I’m here. I’ve got my golems to guard me.”"
            $ minutes += 2
        else:
            $ custom7 = ", but she’s hardly impressed. “The wilderness is there, and I’m here. I’ve got my golems to guard me.”"
            $ minutes += 2
        $ eudocia_invitation_argument_points += (eudocia_invitation_argument_threats_points/2)
        menu:
            'You mention the monsters you’ve encountered[custom1][custom2][custom3][custom4][custom5][custom6][custom7]
            '
            '(eudocia2 set)':
                pass

    label eudocia_about_invitation_arguments_support01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The cityfolk will start negotiations with the tribes as well. You don’t have to be left out.”')
        $ eudocia_invitation_argument_support = 1
        $ eudocia_friendship -= 1
        if quest_creekssupport == 2:
            $ eudocia_invitation_argument_points += 2
        if quest_galerockssupport == 2:
            $ eudocia_invitation_argument_points += 2
        if quest_howlerssupport == 2:
            $ eudocia_invitation_argument_points += 1
        if quest_oldpagossupport == 2:
            $ eudocia_invitation_argument_points += 2
        if quest_monasterysupport == 2:
            $ eudocia_invitation_argument_points += 1
        $ minutes += 2
        $ questionpreset = "eudocia2"
        menu:
            'You’re close to the crag behind the residence, observing the heavy golem that’s lifting large boulders and moving them aside. So far, it has formed a small pile of rocks that resemble its own limbs.
            \n\nYou describe the support you’ve already gathered, as well as your further plans. “I can either face the avalanche, or wait for it to bury me,” she summarizes, then lowers her voice. “No one is going to honor my own will.”
            '
            '(eudocia2 set)':
                pass

label eudocia_about_invitation_conclusionALL:
    label eudocia_about_invitation_conclusion01:
        $ questionpreset = 0
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s your decision?”')
        if (eudocia_friendship+appearance_charisma+eudocia_invitation_argument_points) < eudocia_invitation_argument_points_threshold:
            menu:
                'You answer a few more questions about the city, but her doubts only grow. “So all I’ve got is ya word, and the unspoken plans of ya puppeteers.”
                \n\nFor a few more breaths, you listen to the branches and grass trampled by your feet. Finally, {color=#f6d6bd}Eudocia{/color} looks in the distance, and gestures for you to follow her back to the gate.
                \n\n“I can’t agree to this, [pcname]. This is my home, my {i}real{/i} home.”
                '
                '“I see.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I see.”')
                    $ custom1 = ""
                    jump eudocia_about_invitation_conclusion02
                '“Anything I can do to make you reconsider?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Anything I can do to make you reconsider?”')
                    $ custom1 = "“I... I’ll let ye know,” she starts, but then speeds up her walking. Her eyes are wandering nervously, as if she’s looking for a way to flee.\n\n"
                    jump eudocia_about_invitation_conclusion02
                '“I hope you won’t regret this.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I hope you won’t regret this.”')
                    $ custom1 = "“We may never know,” she drawls out her words. “I’ll solve the real issues once they reach my very walls.”\n\n"
                    label eudocia_about_invitation_conclusion02:
                        $ eudocia_image_left = "base"
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
                        $ eudocia_image_golem02 = "nogolem"
                        if eudocia_image_golem02 == "nogolem":
                            show golem02 nogolem_middle at basicfade
                        elif eudocia_image_golem02 == "nogolemplusback":
                            show golem02 nogolemplusback_middle at basicfade
                        else:
                            hide golem02
                        $ eudocia_invitation_attempt_inprogress = 0
                        stop nature fadeout 4.0
                        if eudocia_friendship >= 10:
                            $ renpy.music.play("audio/track_13eudociahouse02.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
                        else:
                            $ renpy.music.play("audio/track_13eudociahouse01.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
                        $ quest_explorepeninsula_description15c = "{color=#f6d6bd}Eudocia{/color} refused to start talks with the merchants."
                        $ renpy.notify("Journal updated: Explore the Peninsula")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                        if pc_area == "eudociahouse":
                            $ can_leave = 1
                        $ can_rest = 1
                        $ can_items = 1
                        $ minutes += 3
                        $ questionpreset = "eudocia1"
                        menu:
                            '[custom1]You reach the front yard, greeted by {color=#f6d6bd}[horsename]’s{/color} curious snort. {color=#f6d6bd}The enchantress{/color} heads toward her house, but stops herself from opening the door.
                            '
                            '(eudocia1 set)':
                                pass
        else:
            $ eudocia_invitation_success = 1
            menu:
                'You answer a few more questions about the city, and her doubtful glances are slowly replaced with polite nods. “So all I have is ya word for now, but that’s better than naught.”
                \n\nFor a few more breaths, you listen to the branches and grass trampled by your feet. Finally, {color=#f6d6bd}Eudocia{/color} looks in the distance, and gestures for you to follow her back to the gate.
                \n\n“I’ll speak with ya puppeteers. And I’ve got a little gift for them.”
                '
                '“A gift?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A gift?”')
                    $ custom1 = "“A sign of good will,” she waves it off. “Let me gather my thoughts.”"
                    jump eudocia_about_invitation_conclusion03
                '“I’m no one’s puppet.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m no one’s puppet.”')
                    $ custom1 = "Her snort is followed by silence."
                    label eudocia_about_invitation_conclusion03:
                        $ eudocia_image_left = "base"
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
                        $ eudocia_image_golem02 = "nogolem"
                        if eudocia_image_golem02 == "nogolem":
                            show golem02 nogolem_middle at basicfade
                        elif eudocia_image_golem02 == "nogolemplusback":
                            show golem02 nogolemplusback_middle at basicfade
                        else:
                            hide golem02
                        $ eudocia_invitation_attempt_inprogress = 0
                        stop nature fadeout 4.0
                        if eudocia_friendship >= 10:
                            $ renpy.music.play("audio/track_13eudociahouse02.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
                        else:
                            $ renpy.music.play("audio/track_13eudociahouse01.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
                        $ minutes += 5
                        menu:
                            '[custom1]
                            \n\nYou reach the front yard, greeted by {color=#f6d6bd}[horsename]’s{/color} curious snort. {color=#f6d6bd}The enchantress{/color} enters her house briefly, and brings you what looks like a plank made of rock shards.
                            \n\n“Tell them I made this ten years ago. It should be enough to convince them my golems are real.”
                            '
                            '“But what is it?”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But what is it?”')
                                menu:
                                    '“Well,” she invites you to stretch out your hand, then grabs your fingers with her own. Her touch is cold. “A keepsake from the time I needed to build my first sentinel.”
                                    \n\nThe rocks clench to your skin, from your wrist to your shoulder, like a sleeve. Your arm gets slightly heavier, but the sensation fades away.
                                    \n\n“Don’t shake anyone’s hand while wearing this,” her words carry both pride and melancholy. “It takes time to get used to my spell’s strength. To take it off, just give it a rapid pull here,” she grabs it close to your shoulder, and The Golem Glove falls away. Even though the rocks aren’t connected to each other in any visible way, they keep their general shape. “As long as ye don’t push any of the parts too fiercely, the pneuma will hold.”
                                    '
                                    '“Should I hide it in my bags?”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Should I hide it in my bags?”')
                                        $ custom1 = "“Nah, it will help ye more if ye use it. Keep it close in the woods - ya punches will surprise ye.”"
                                        jump eudocia_about_invitation_conclusion04
                                    '“Can I use it in combat?”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I use it in combat?”')
                                        $ custom1 = "“Ye better,” a brief chuckle. “Ya punches will surprise ye, and we need ye back in the city, and safe.”"
                                        jump eudocia_about_invitation_conclusion04
                                    '“Thank you for your trust, {color=#f6d6bd}Eudocia{/color}.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Thank you for your trust, {color=#f6d6bd}Eudocia{/color}.”')
                                        $ eudocia_friendship += 1
                                        $ custom1 = "After she meets your eyes, her bewilderment gives way to a warm smile."
                                        label eudocia_about_invitation_conclusion04:
                                            $ item_golemglove = 1
                                            $ quest_explorepeninsula_description15a = "{color=#f6d6bd}Eudocia{/color} has agreed to talk with the merchants. I need to take her Golem Glove to the city."
                                            $ renpy.notify("Journal updated: Explore the Peninsula.\nYou received The Golem Glove.")
                                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula. You received The Golem Glove.{/i}')
                                            if pc_area == "eudociahouse":
                                                $ can_leave = 1
                                            $ can_rest = 1
                                            $ can_items = 1
                                            $ minutes += 1
                                            $ questionpreset = "eudocia1"
                                            menu:
                                                '[custom1]
                                                '
                                                '(eudocia1 set)':
                                                    pass
