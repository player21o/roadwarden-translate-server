label howlersdell_thaismad00:
    $ thais_afk_cause_betrayal = 2
    $ quarters += 2
    $ thais_super_angry = 1
    if quest_howlerssupport == 1:
        $ quest_howlerssupport = 3
        $ renpy.notify("Quest completed: Support of Howler’s Dell")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Support of Howler’s Dell{/i}')
        $ quest_howlerssupport_description06 = "{color=#f6d6bd}Thais{/color} distrusts me. I won’t be able to negotiate with her."
    if quest_fisherhamlet == 1:
        $ quest_fisherhamlet = 3
    menu:
        'The guard informs you that she needs to look for her, so you sit down on a bench and wait for what feels like an eternity.
        \n\nWhen {color=#f6d6bd}Thais{/color} joins you, she neither says a word of greeting, nor takes a place at the table.
        \n\n“Is our situation not clear enough? I want nothing to do with you, unless it’s {i}essential{/i}.”
        \n\nHe green eyes are filled with disdain, and you notice that her deer-buckle is gone, replaced by a simpler one.
        '
        '“I’m the only traveler you have at hand. You need my services.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m the only traveler you have at hand. You need my services.”')
            $ questionpreset = "thais1"
            menu:
                '“Your arrogance helped you get so far, but you’re soon about to learn no one here {i}needs{/i}. Spit out what you want and leave me the fuck alone.”
                \n\nHer lips are as red as blood.
                '
                '(thais1 preset)':
                    pass
        '“Don’t be childish. Cutting ties with me will only make you lose more.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t be childish. Cutting ties with me will only make you lose more.”')
            $ questionpreset = "thais1"
            menu:
                '“Did I ask you for lessons?” Her lips are as red as blood. “I can trust nothing you are about to tell me. Spit out what you want and leave me the fuck alone.”
                '
                '(thais1 preset)':
                    pass

label howlersdell_thaismad01:
    $ minutes += 20
    $ questionpreset = "thais1"
    menu:
        'The guard informs you that she needs to look for her, so you stand around and wait for what feels like eternity.
        \n\nWhen {color=#f6d6bd}Thais{/color} joins you, she neither says a word, nor takes a seat.
        '
        '(thais1 preset)':
            pass

label howlersdell_thaismad02:
    $ questionpreset = "thais1"
    menu:
        '{color=#f6d6bd}Thais{/color} gives you a scornful glance.
        '
        '(thais1 preset)':
            pass

label howlersdellthaisafterquestionsBIGMAD:
    $ questionpreset = "thais1"
    $ custom1 = renpy.random.choice(['She struggles to hide the hatred in her eyes.', 'She looks around, ignoring your presence.', '“Are you done?”'])
    menu:
        '[custom1]
        '
        '(thais1 preset)':
            pass

label howlersdellquestionsgolems01fail:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know {color=#f6d6bd}Eudocia{/color}, the enchantress? I’d like to hang this rod on a watchtower for her.”')
    $ thais_about_golemsrods = 1
    $ thais_about_bronzerod_allowed = -1
    $ questionpreset = "thais1"
    menu:
        'She scoffs. “Don’t be stupid. And if any of us finds such a thing in our woods, you’ll pay a price for breaking our laws.”
        '
        '(thais1 preset)':
            pass

label howlersdellquestionsplague01fail:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring sad news from {color=#f6d6bd}Old Págos{/color}. The villagers were stricken by a plague.”')
    $ thais_about_plague = 1
    $ howlersdell_elpis_firsttime_theywant = 1
    $ howlersdell_reputation += 1
    $ oldpagos_plague_warnedplaces += 1
    $ questionpreset = "thais1"
    menu:
        'She gives you a long, doubtful look, then calls a guard with a gesture. “Tell the others to gather by {color=#f6d6bd}Ape Ale{/color},” she tells her, then looks back into your eyes. “I’ll pass them the news once we’re done here. I can’t heal illnesses - speak with {color=#f6d6bd}the druids{/color}, if you must.”
        \n\nThe guard returns, and {color=#f6d6bd}the mayor{/color} sends her away again: “Warn {color=#f6d6bd}Elpis{/color}. She must speak with [pcname] soon.”
        '
        '(thais1 preset)':
            pass

label howlersdellquestionsbanditsMADALL:
    label howlersdellquestionsbanditsMAD01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was in Pelt of the North. The innkeeper feels uneasy about Glaucia’s band.”')
        $ thais_about_banditband = 1
        $ questionpreset = 0
        menu:
            'When you mention the “raids” on the northern villages, her eyes narrow. “Are you sure? It’s the first I’m hearing of it. {color=#f6d6bd}Glaucia{/color} has been around since years back, but she’s not much of a nuisance.”
            '
            '“I’m just a messenger. He’s asking for you to join forces with him.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m just a messenger. He’s asking for you to join forces with him.”')
                menu:
                    '“Well, I can’t give you my answer. I won’t ask our hunters to endanger their lives in the pursuit of some gossip.”
                    '
                    '“I could ask around, learn something more.”' if (banditshideout_villagesasked_aboutattacks < 3 and not whitemarshes_attacked) and not (banditshideout_villagesasked_aboutattacks == 2 and druidcave_druid_about_bandits1 and not helvius_about_bandits2):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could ask around, learn something more.”')
                        $ quest_intelforpeltnorth_description04 = "{color=#f6d6bd}Thais{/color} won’t answer my question until I learn more about the “raids” from the northern villages - {color=#f6d6bd}White Marshes{/color}, {color=#f6d6bd}Gale Rocks{/color}, and {color=#f6d6bd}Creeks{/color}."
                        $ renpy.notify("Journal updated: Glaucia’s Band")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
                        menu:
                            'She sighs. “There are only three villages in the North. {color=#f6d6bd}White Marshes{/color}, {color=#f6d6bd}Gale Rocks{/color}, and {color=#f6d6bd}Creeks{/color}. Bring me news from those places and you will get my answer.”
                            '
                            '“I’m paid for passing the message from here to {color=#f6d6bd}Pelt of the North{/color}. Asking me to ride for you through half of the peninsula and back is a different deal entirely.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m paid for passing the message from here to {color=#f6d6bd}Pelt of the North{/color}. Asking me to ride for you through half of the peninsula and back is a different deal entirely.”')
                                menu:
                                    'She observes you carefully. “Are you trying to anger me, you piece of shit?”
                                    '
                                    '“Forget it.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Forget it, you piece of shit.”')
                                        jump howlersdellthaisafterquestions
                            '“I can do that.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can do that.”')
                                jump howlersdellthaisafterquestions
                    '“From what I’ve heard, the only place bothered by raids is {color=#f6d6bd}White Marshes{/color}. The people from {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Creeks{/color} have faced no issues.”' if (banditshideout_villagesasked_aboutattacks >= 3) or (banditshideout_villagesasked_aboutattacks == 2 and not helvius_about_bandits2 and druidcave_druid_about_bandits1):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “From what I’ve heard, the only place bothered by raids is {color=#f6d6bd}White Marshes{/color}. The people from {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Creeks{/color} have faced no issues.”')
                        $ quest_intelforpeltnorth_description04 = "{color=#f6d6bd}Thais{/color} won’t answer my question until I learn more about the “raids” from the northern villages - {color=#f6d6bd}White Marshes{/color}, {color=#f6d6bd}Gale Rocks{/color}, and {color=#f6d6bd}Creeks{/color}."
                        jump howlersdellquestionsbanditsMAD202
                    '“I don’t have time for this. Should I tell {color=#f6d6bd}the innkeep{/color} that you’re not interested in collaboration?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have time for this. Should I tell {color=#f6d6bd}the innkeep{/color} that you’re not interested in collaboration?”')
                        $ quest_intelforpeltnorth_description05 = "{color=#f6d6bd}Thais{/color} has decided to reject the collaboration. I should bring the news to the innkeeper."
                        $ renpy.notify("Journal updated: Glaucia’s Band")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
                        $ questionpreset = "thais1"
                        menu:
                            'She raises her chin. “I guess you should.”
                            '
                            '(thais1 preset)':
                                pass

    label howlersdellquestionsbanditsMAD201:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring news about {color=#f6d6bd}Glaucia’s{/color} band.”')
        $ thais_about_banditband2 = 1
        $ questionpreset = 0
        menu:
            '“And?”
            '
            '“The only place bothered by raids is {color=#f6d6bd}White Marshes{/color}. The people from {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Creeks{/color} have faced no issues.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The only place bothered by raids is {color=#f6d6bd}White Marshes{/color}. The people from {color=#f6d6bd}Gale Rocks{/color} and {color=#f6d6bd}Creeks{/color} have faced no issues.”')
                jump howlersdellquestionsbanditsMAD202

    label howlersdellquestionsbanditsMAD202:
        $ quest_intelforpeltnorth_description06 = "I brought the news to {color=#f6d6bd}Thais{/color}, but she has decided to reject the invitation. I should return to the innkeeper."
        $ renpy.notify("Journal updated: Glaucia’s Band")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
        menu:
            'She crosses her arms. “If {color=#f6d6bd}Glaucia{/color} is eager to bother with the poorest settlement in the north, especially one filled with awoken, it must be personal for her. We have no reason to stand in the middle of it.”
            \n\nShe adjusts her cape, then stares into your eyes. Her voice is solemn. “{i}As the mayor of {color=#f6d6bd}Howler’s Dell{/color}, I appreciate your concern, but I don’t share your apprehension. The guards of our village will stay on our walls. Be sure to come see us soon, we would gladly share a lamb and tale with you.{/i}”
            '
            '“Very well. I’ll pass it to him.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. I’ll pass it to him.”')
                jump howlersdellthaisafterquestions
