# Cephas (the chief - cares after organizing labor, ordering fighters, "the things of today") and Gaiane (the shaman - maintains rituals and is meant to counterbalance the chief, caring for "the things of the past and the future", very young and often high)
default cephasgaiane_available = 0
default cephasgaiane_dayvisit = 0
default cephasgaiane_shop = 0
default cephasgaiane_shop_select = 0 #"dragonhorn"
default cephasgaiane_shop_dragonhorn = 0

default cephasgaiane_about_work = 0 # Inicjuje temat o kontakcie z wioską, można odpowiedzieć na pytanie, dlaczego w ogóle się chce podjąć questa
default cephasgaiane_about_tribe = 0
default cephasgaiane_about_city = 0
default cephasgaiane_about_mountain = 0
default cephasgaiane_about_chiefandshaman = 0

default cephasgaiane_about_notcaring = 0
default cephasgaiane_about_plague = 0
default cephasgaiane_about_necromancers = 0
default cephasgaiane_about_bandits = 0 # Generations come and go, but the woods abide.

default cephasgaiane_about_spiritrock = 0 # (if quest_spiritrock == 1 and galerocks_photios_quest_spiritrock_question_doubt and not cephasgaiane_about_spiritrock)
default cephasgaiane_about_orchard = 0 # if galerocks_fulvia_about_shortcut2 - # "According to {color=#f6d6bd}Fulvia{/color}, it’s possible that the old orchard is still looked after by “{color=#f6d6bd}The Green Mountain Tribe{/color}”."
default cephasgaiane_about_weather = 0
default cephasgaiane_about_steephouse1 = 0 # jeśli się zna prawdę o nim lub szuka prawdy o nim - zmienia pytanie
default cephasgaiane_about_steephouse2 = 0 # jeśli się doprowadziło do upadku Thais
default cephasgaiane_about_asterion1 = 0 # gdy zostaną spytani o Asteriona - quest_reachthepaganvillage_description00b
default cephasgaiane_about_asterion1a = 0
# default cephasgaiane_about_asterion1b = 0
default cephasgaiane_about_asterion2 = 0 # saurian
default cephasgaiane_about_asterion3 = 0 # chief tells where Asterion went
default cephasgaiane_about_asterion4 = 0 # found - jeśli cephasgaiane_about_highisland. “I’ve learned what {color=#f6d6bd}Asterion{/color} was looking for on the island.”

default cephasgaiane_about_highisland_permission = 0
default cephasgaiane_about_highisland = 0
default cephasgaiane_about_highisland_questions_max = 7
default cephasgaiane_about_highisland_questions = 0
default cephasgaiane_about_highisland_question1 = 0 # jak dotrzeć
default cephasgaiane_about_highisland_question2 = 0 # jeśli jak dotrzeć - czemu jest zakaz?
default cephasgaiane_about_highisland_question3 = 0 # historia green mountain
default cephasgaiane_about_highisland_question4 = 0 # dlaczego plemię nie chce odzyskać wyspy
# default cephasgaiane_about_highisland_question5 = 0 # wyjątkowe istoty
default cephasgaiane_about_highisland_question6 = 0 # nietypowe zagrożenia
default cephasgaiane_about_highisland_question7 = 0 # mapa
default cephasgaiane_about_highisland_question8 = 0 # naucz mnie, jak obudzić magiczny posąg
default cephasgaiane_about_unicorns = 0
default greenmountaintribe_asterion_permission_threshold = 5

# some abandoned ideas:
# - czy skarb został tu zachowany przez Green Mountain Tribe, czy może ludzi, którzy nie chcieli zostać w Creeks?
# - kokon z trupem towarzyszki Asteriona - można się dowiedzieć, że tam z nim popłynęła, i zdobyć wsparcie jej rodziny. ( to tego chcą, a nie skarbu! ale żeby ją znaleźć, trzeba zboczyć z drogi?)

label greenmountaintribechieffirsttime01:
    $ cephasgaiane_dayvisit = day
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ shop = "greenmountaintribechief"
    show areapicture greenmountaintribecave01 at basicfade
    menu:
        'The simple huts are short enough for you to see their hide-covered roofs from above, and as you look at the ceiling, there’s no water dripping on them. They don’t offer much privacy, either - even if the entrances were covered with a curtain, the gaps between the bones let you peek inside. It’s as if they one day collapsed here from the surface, losing their purpose, but remaining as a relic of the old way of living.
        \n\nWhile the huts are only filled with furs and a few pieces of clothing, the chamber is far from empty. A few women, some of them very young, some in their thirties or forties, are sitting around the campfire, feeding infants or playing with toddlers. There’s a man stretching a piece of leather on a tanning rack, and you hear splashes of water coming from a corner.
        \n\nWhen your eyes land on two people sitting in a circle of wooden stumps, their gaze makes your destination clear.
        '
        'I step closer.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step closer.')
            menu:
                'They are sitting a few steps away from one another, and as you’re invited to sit down, the three of you form a triangle. The air is heavy, but you smell no sweat or dirt, and aside from the crying child and echoes of distant play and conversations, the dancing lights and crackling wood are no less cozy than an inn in the evening.
                \n\n{color=#f6d6bd}The man in his fifties{/color} is leaning forward, resting his elbows on his thighs, more like a tired guard than a distinguished ruler. He’s dressed just as heavily as the people you saw on the surface, but the fabric of his clothes is so dark-blue that it’s almost black. He’s barefoot, and you wonder if that’s enough to not make him sweat under the layers of wool. His helmet, shield, and sword are resting on the ground. His long gray hair freely surrounds his face, which is covered with wrinkles and scars. Some beast was lucky enough to leave a mark deeper than that - the man’s nose is missing, leaving a disfigured hole.
                \n\n{color=#f6d6bd}The woman could be twenty-five{/color}, and has absent eyes that are roving over your outfit, equipment, face, and hands. She’s dressed much more humbly than the man - her tunic and pants are undyed and short enough to reveal her calves and forearms. She has unevenly cut short black hair, and a yellow kerchief that’s hanging from her neck, lazily thrown over her back. Her legs are stretched out in front of her, resting on the heels of her sandals and swaying left and right, spread just above an unfolded sack, covered with gemstones, pebbles, and animal bones. She keeps her hands on the nearest trunk, desperate for something to support her back.
                \n\nBoth of them are unusually pale, but the woman looks almost sick.
                '
                'I introduce myself.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I introduce myself.')
                    if pc_religion == "pagan":
                        $ custom1 = "You speak in the Old Speech, and the man smiles. “Let’s use t’ City Tongue from now on. Our shaman,” he looks at the young person in a light outfit, “I t’owt her what I knew, but we bot’ need to practice.” "
                    else:
                        $ custom1 = "“We’ve heard ‘at you know nawt of our tongue,” starts the elder with a firm look, “but I’ve talked wit’ t’ cityfolk more ‘tan I wanted. And our shaman,” he looks at the young person in a light outfit, “I t’owt her what I knew, but knows little of t’ way you sound. Let her practice.”"
                    menu:
                        '[custom1]
                        \n\nShe frowns and waves her hand in front of her nose, as if there’s a fly there. “Hello,” her voice is both delicate and annoyed. “Shaman {color=#f6d6bd}Gaiane{/color},” she struggles to utter.
                        \n\nThe man stares at you, speaking more confidently, and with a greater familiarity of the sounds he uses. “And I’m {color=#f6d6bd}Cephas{/color}, t’ chief of {color=#f6d6bd}T’ Tribe of T’ Green Mountain{/color}. Your gift bowt you our time, but we’ve busy lives.”
                        '
                        'I try to get used to their dialect.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to get used to their dialect.')
                            $ at_activate = 1
                            $ at = 0
                            menu:
                                '“Who sends you, [pcname]?”
                                '
                                ' (disabled)' ( condition="at == 0" ):
                                    pass
                                'I speak softly. “No one. As a roadwarden, I wanted to be sure you don’t need my help.”' ( condition="at == 'friendly'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - I speak softly. “No one. As a roadwarden, I wanted to be sure you don’t need my help.”')
                                    $ at_activate = 0
                                    $ at = 0
                                    $ cephasgaiane_about_work = 1
                                    $ custom2 = "{color=#f6d6bd}Cephas’{/color} voice grows colder. “Do we look as if we need one’s help? Do you see cracks in our walls ‘at can’t be sealed wit’out your blood, or monsters you can sing to sleep?”\n\n{color=#f6d6bd}Gaiane{/color} reaches for two green gems and puts them on the edge of the fabric, side by side. “Don’t get angry,” her voice is close to a whisper, and seems to ease {color=#f6d6bd}the ire in the chief’s{/color} gaze right away. When she looks at you, she keeps her hands in front of her, palms up. “Does your soul speak of pride, or of care? Can’t see it. But we’re good as is, and ask you to trust our mout’s to ask for us, if we need ‘em to.”"
                                    $ greenmountaintribe_secondattitude = "friendly"
                                    $ greenmountaintribe_reputation -= 1
                                    jump greenmountaintribechieffirsttime02
                                'I smile. “My curiosity.”' ( condition="at == 'playful'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - I smile. “My curiosity.”')
                                    $ at_activate = 0
                                    $ at = 0
                                    $ custom2 = "{color=#f6d6bd}Gaiane{/color} chuckles, and moves one of the orange gems with her foot. “Firm like a topaz, to take you so far. Ask, and we’ll speak.”"
                                    $ greenmountaintribe_secondattitude = "playful"
                                    jump greenmountaintribechieffirsttime02
                                'I look them in the eyes. “I represent the interests of the city of {color=#f6d6bd}Hovlavan{/color}, as well as its merchant guild.”' ( condition="at == 'distanced'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - I look them in the eyes. “I represent the interests of the city of {color=#f6d6bd}Hovlavan{/color}, as well as its merchant guild.”')
                                    $ at_activate = 0
                                    $ at = 0
                                    $ custom2 = "“And we seek no trade or ties to t’ city, its traders, or soldiers, or priests,” {color=#f6d6bd}Cephas’{/color} voice is strict, though {color=#f6d6bd}Gaiane{/color} tries to ease the tension with her gentle whisper. “Speak like t’ cityfolk,” she looks you in the eyes, “and our mout’s will be of our tribe. But be a soul, and we,” she reaches for two dark-red gems, and places them on each end of a small bone, “will be souls, too.”"
                                    $ greenmountaintribe_secondattitude = "distanced"
                                    jump greenmountaintribechieffirsttime02
                                'I say a soundless curse. “Why do you care? Getting here, sweat, and dragon bones. I {i}deserve{/i} to speak with you.”' ( condition="at == 'intimidating'" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I say a soundless curse. “Why do you care? Getting here, sweat, and dragon bones. I {i}deserve{/i} to speak with you.”')
                                    $ at_activate = 0
                                    $ at = 0
                                    $ custom2 = "They exchange looks, with {color=#f6d6bd}Gaiane{/color} seemingly not being sure what you just said, but after seeing {color=#f6d6bd}Cephas’{/color} nod, she speaks to you a bit too gently, as if she’s addressing a child in a tantrum, staring into your eyes. “‘Ten speak, and we’ll listen.” She reaches to one of the red gems below her, and places it between two tiny bones."
                                    $ greenmountaintribe_secondattitude = "intimidating"
                                    $ greenmountaintribe_reputation -= 1
                                    jump greenmountaintribechieffirsttime02
                                'I think about the words of the old druid. “I’m a freedom seeker, a friend of the speakers of the forest.”' ( condition="at == 'vulnerable' and description_greenmountaintribe03" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I think about the words of the old druid. “I’m a freedom seeker, a friend of the speakers of the forest.”')
                                    $ at_activate = 0
                                    $ at = 0
                                    $ custom2 = "He straightens up, giving you a serious look. “‘Ten sit down with us and rest, for we’ve all found our freedom here.” The shaman gives you both puzzled looks, but says nothing. “May t’ {i}freedom seeker{/i} be free of hunger and welcomed,” he says to her, then addresses the women sitting at the fire in the Old Speech.\n\nSoon after you sit down, an aromatic bowl of stew lands in your hands, warming them up. {color=#f6d6bd}The chief and the shaman{/color} also receive very small servings, accompanying you. Once the bowls are taken away, the gentle voice of {color=#f6d6bd}Gaiane{/color} breaks the silence. “Can’t move mountains for you, but we listen, and share.” She reaches for a few gems in various colors, and puts them into a single row."
                                    $ quarters += 1
                                    $ pc_food = limit_pc_food(pc_food+2)
                                    show plus2food at foodchange onlayer myoverlay
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
                                    $ greenmountaintribe_secondattitude = "vulnerable"
                                    $ greenmountaintribe_reputation += 2
                                    jump greenmountaintribechieffirsttime02
                                'For a moment I’m silent, then look at the ground. “No one sent me. I need help.”' ( condition="at == 'vulnerable' and not description_greenmountaintribe03" ):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - For a moment I’m silent, then look at the ground. “No one sent me. I need help.”')
                                    $ at_activate = 0
                                    $ at = 0
                                    $ custom2 = "They look at you carefully. “Can’t move mountains for you,” {color=#f6d6bd}Gaiane’s{/color} voice is warm. “But we listen, and share.” She reaches for a few gems in various colors, and puts them into a single row."
                                    $ greenmountaintribe_secondattitude = "vulnerable"
                                    $ greenmountaintribe_reputation += 1
                                    jump greenmountaintribechieffirsttime02

    label greenmountaintribechieffirsttime02:
        $ questionpreset = "cephasgaiane1"
        if quest_reachthepaganvillage == 1:
            $ renpy.notify("Quest completed: The Hidden Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Hidden Village{/i}')
        $ quest_reachthepaganvillage = 2
        menu:
            '[custom2]
            '
            '(cephasgaiane1 set)':
                pass

label greenmountaintribechiefregular01:
    show areapicture greenmountaintribecave01 at basicfade
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ shop = "greenmountaintribechief"
    if cephasgaiane_dayvisit == day:
        jump greenmountaintribechiefafterinteraction01
    else:
        $ cephasgaiane_dayvisit = day
        $ questionpreset = "cephasgaiane1"
        menu:
            '[greenmountaintribe_cave_fluff]
            '
            '(cephasgaiane1 set)':
                pass

label greenmountaintribechiefafterinteraction01:
    hide screen selling
    $ questionpreset = "cephasgaiane1"
    $ custom1 = renpy.random.choice(['You sit in silence, until a group of kids runs through the chamber, shouting at each other. Once they notice you, they leave quietly, {color=#f6d6bd}Gaiane{/color} smiling after them.', 'A guard enters the chamber to whisper something to {color=#f6d6bd}Cephas{/color}, then leaves quickly.', '{color=#f6d6bd}Gaiane{/color} studies the gems and pebbles spread before her.', 'A few young people come in through the entrance behind your back, observing you and whispering to each other, then disappear once you and {color=#f6d6bd}Cephas{/color} look in their direction.', 'The cry of a child echoes through the tunnels, followed by the calming chatter of an elder.'])
    menu:
        '[custom1]
        '
        '(cephasgaiane1 set)':
            pass

label cephasgaiane_about_tribeALL:
    label cephasgaiane_about_tribe01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about your village.”')
        $ cephasgaiane_about_tribe = 1
        $ questionpreset = "cephasgaiane1"
        if quest_explorepeninsula == 1:
            $ renpy.notify("Journal updated: Explore the Peninsula")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
        $ quest_explorepeninsula_description20 = "From what I’ve learned in {color=#f6d6bd}The Tribe of The Green Mountain{/color}, they will never be open to negotiating with the city."
        menu:
            '{color=#f6d6bd}The shaman{/color} leans forward, smiling. The fire plays with her shadow. “And how? In {i}your{/i} tongue? Wit’out crossing our tunnels, or plowing our fields, or battling t’ snow cats, or making a cup bowl wit’ our elders?” She gestures for you to take a glance at the huts, the spears, and the rocks beneath her. “We’ve our own seasons, trades, and legends. Spirits guide us t’rough dreams and t’unders. Children learn stories older ‘tan emperors.”
            \n\nAs she grows more passionate with every word, {color=#f6d6bd}the chief{/color} observes her with a smile. He reaches for his sword, observing the dark scabbard covered with a fancy pattern of squares. “If we were a tribe of T’ Ten cities, you’d like to hear ‘at we dig for ore, grow crops, hunt. We lack some t’ings, we have ot’ers in abundance, but we accept what we get, and won’t open our gates to no merchants. Or blood we can’t trust.”
            '
            '(cephasgaiane1 set)':
                pass

    label cephasgaiane_about_chiefandshaman01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Who’s the decision maker in the village? The chief, or the shaman?”')
        $ cephasgaiane_about_chiefandshaman = 1
        $ questionpreset = "cephasgaiane1"
        menu:
            '“T’ village decides for t’ village,” {color=#f6d6bd}Cephas{/color} smiles. “In {color=#f6d6bd}T’ Tribe{/color} a chief worries about t’ ‘tings of today, and a shaman about t’ ‘tings of ‘t past and tomorrow.”
            \n\n{color=#f6d6bd}Gaiane{/color} looks at him with respect. “For ‘tere are harvests of ‘tis season,” she says solemnly, “but taste like ashes wit’out memories and hopes.” She points at the bones and pebbles beneath her, as if they’re meant to explain it all.
            \n\nA quiet tune plays from the opposite end of the chamber in an attempt to calm a crying child.
            '
            '(cephasgaiane1 set)':
                pass

    label cephasgaiane_about_work01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I help you with anything, as a roadwarden?”')
        $ cephasgaiane_about_work = 1
        $ questionpreset = "cephasgaiane1"
        menu:
            '“Do we look as if we need one’s help? Do you see cracks in our walls ‘at can’t be sealed wit’out your blood, or monsters you can sing to sleep?”
            \n\n{color=#f6d6bd}Gaiane{/color} reaches for two green gems and places them on the edge of the fabric, side by side. “Don’t get angry,” her voice is close to a whisper, and seems to ease the ire in {color=#f6d6bd}the chief’s{/color} gaze right away. When she looks at you, she keeps her hands in front of her, palms up. “Does your soul speak of pride, or of care? Can’t see it. But we’re good as is, and ask you to trust our mout’s to ask for us, if we need ‘em to.”"
            '
            '(cephasgaiane1 set)':
                pass

    label cephasgaiane_about_city01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you think about {color=#f6d6bd}Hovlavan{/color}?”')
        $ cephasgaiane_about_city = 1
        if cephasgaiane_about_mountain:
            $ description_highisland05 = "In distant times, it used to be a home to {color=#f6d6bd}The Tribe of The Green Mountain{/color}, who were then pushed away by {color=#f6d6bd}Hovlavan’s{/color} army."
            $ description_greenmountaintribe10 = "The Tribe used to thrive on {color=#f6d6bd}High Island{/color}, but they were thrown out from the original {color=#f6d6bd}Green Mountain{/color} - the volcano - by the corsairs of {color=#f6d6bd}Hovlavan{/color} when they refused to join the city."
        $ description_greenmountaintribe07 = "They try to stay away from the cityfolk, afraid of persecution from the hands of The United Church."
        $ questionpreset = "cephasgaiane1"
        menu:
            '“We don’t,” {color=#f6d6bd}Cephas’{/color} voice is cold, and when {color=#f6d6bd}Gaiane{/color} chips in, she hands you a soft, though heavy pouch. Inside, you find a collection of dozens of red crystals, each one smaller than a game die. “T’ city’s corsairs pillaged our homeland for years, saying ‘ey would stop once we’d agree to pay t’ yearly tribute. ‘Ey murdered us and torched our harbors and crops, for we held t’ island before ‘em, and prayed to different spirits.”
            \n\nYou return the pouch, and ask what’s the meaning behind it. “T’ shamans of old made a tomb wit’ one rock for every soul lost to T’ Ten Cities. ‘Ey browt ‘em here, to help us remember.”
            '
            '(cephasgaiane1 set)':
                pass

    label cephasgaiane_about_mountain01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I expected this mountain to be a bit more... {i}green{/i}.”')
        $ cephasgaiane_about_mountain = 1
        $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
        if cephasgaiane_about_city:
            $ description_highisland05 = "In distant times, it used to be a home to {color=#f6d6bd}The Tribe of The Green Mountain{/color}, who were then pushed away by {color=#f6d6bd}Hovlavan’s{/color} army."
            $ description_greenmountaintribe10 = "The Tribe used to thrive on {color=#f6d6bd}High Island{/color}, but they were thrown out from the original {color=#f6d6bd}Green Mountain{/color} - the volcano - by the corsairs of {color=#f6d6bd}Hovlavan{/color} when they refused to join the city."
        $ questionpreset = "cephasgaiane1"
        menu:
            '“We are {i}of{/i} it, but not {i}on{/i} it.” {color=#f6d6bd}Cephas{/color} glances at the flames. “T’ Green Mountain is on {color=#f6d6bd}High Island{/color}.”
            \n\n{color=#f6d6bd}Gaiane’s{/color} voice becomes melodic, even though she pauses when she says a few of the more unique words out loud. “T’ volcano in t’ very center. Around it, our fields were growing like ‘ey could in no ot’er soil of t’ nort’. Every few lifespans, lava turns to ashes t’ woods ‘at it feeds, but ‘tese ashes give birt’ to t’ sweetest fruits and heaviest grain.”
            '
            '(cephasgaiane1 set)':
                pass

label cephasgaiane_about_asterionALL:
    label cephasgaiane_about_asterion101:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to find {color=#f6d6bd}Asterion{/color}.”')
        $ cephasgaiane_about_asterion1 = 1
        $ questionpreset = "cephasgaiane1"
        menu:
            '“He was here, and a few times,” with every word, {color=#f6d6bd}Cephas’{/color} voice gets quieter, as if he’s not sure how to continue. “We helped him, for he gave us a grand promise, and a sign of his trustwort’iness. Browt back a soul t’owt to be lost in t’ woods. But it’s been almost a season since we saw him.”
            '
            '(cephasgaiane1 set)':
                pass

    label cephasgaiane_about_asterion101a:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What kind of person is {color=#f6d6bd}Asterion{/color}?”')
        $ cephasgaiane_about_asterion1a = 1
        $ questionpreset = "cephasgaiane1"
        $ description_asterion15 = "According to {color=#f6d6bd}Gaiane{/color}, Asterion is “a shell lost on its pat’ to nowhere, a soul torn by its dreams, a word spoken to no one.”"
        menu:
            '“A shell lost on its pat’ to nowhere,” {color=#f6d6bd}Gaiane{/color} stares into your eyes, “a soul torn by its dreams, a word spoken to no one.”
            \n\n{color=#f6d6bd}The chief{/color} frowns, but doesn’t add anything.
            '
            '(cephasgaiane1 set)':
                pass

    label cephasgaiane_about_asterion201:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That saurian I saw outside... It used to belong to {color=#f6d6bd}Asterion{/color}, am I right?”')
        $ quest_asterion_description07 = "I found Asterion’s saurian with {color=#f6d6bd}The Tribe of The Green Mountain{/color}. It’s larger than a horse, dark green, though the edges of its limbs, tail, and eyebrows are red-and-orange."
        $ description_asterion08 = "I found Asterion’s saurian with {color=#f6d6bd}The Tribe of The Green Mountain{/color}. It’s larger than a horse, dark green, though the edges of its limbs, tail, and eyebrows are red-and-orange."
        $ cephasgaiane_about_asterion2 = 1
        $ cephasgaiane_about_unicorns = 1
        $ asterion_highisland_clues += 1
        $ questionpreset = "cephasgaiane1"
        menu:
            '“‘At’s correct,” {color=#f6d6bd}Cephas’{/color} approving eyes contrast with the threatening look of his “nose,” and his voice is warm. “Where he was heading, ‘ere was no place for a beast ‘at doesn’t swim well, so he asked us to look after it. And also, he was afraid of t’ unicorns.”
            \n\nAfter you mention that you doubt having fewer teeth would help someone deal with such a monster, {color=#f6d6bd}Gaiane{/color} chuckles, then bites her lower lip, showing her unusually long canines. “You’d like to cut t’ skin of a spirit of havoc? Cityfolk ‘tink t’ unicorns are but a battering ram, yet ‘ey are ‘eir own soulcarriers, led by judgment, not anger. ‘Ey eat grass and shoots, not flesh, and when not wit’ calves, listen to t’ kind tales and prayers.”
            \n\n{color=#f6d6bd}The chief{/color} nods. “It was wise of him to not take wit’ him a bloodt’irsty saurian. It won’t learn when to bow, for it trusts only its own muscles and fear.”
            '
            '(cephasgaiane1 set)':
                pass

    label cephasgaiane_about_asterion301:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But where did {color=#f6d6bd}Asterion{/color} go?”')
        $ cephasgaiane_about_asterion3 = 1
        if (greenmountaintribe_reputation+(appearance_charisma/2)) < greenmountaintribe_asterion_permission_threshold-1:
            $ questionpreset = "cephasgaiane1"
            menu:
                '{color=#f6d6bd}Cephas{/color} runs his stern eyes over you. “To a place ‘at doesn’t need yet anot’er cityfolk.”
                '
                '(cephasgaiane1 set)':
                    pass
        else:
            $ cephasgaiane_about_asterion3 = 2
            $ cephasgaiane_about_mountain = 1
            $ asterion_highisland_knowsabout = 1
            $ asterion_highisland_clues += 5
            $ quest_asterion_description13 = "{color=#f6d6bd}Cephas and Gaiane{/color} told me that {color=#f6d6bd}Asterion{/color} was meant to examine the state of the ruins and the caves that can be found on the island’s volcano, and to bring news about them to the Tribe."
            $ description_highisland05 = "In distant times, it used to be a home to {color=#f6d6bd}The Tribe of The Green Mountain{/color}, who were then pushed away by {color=#f6d6bd}Hovlavan’s{/color} army."
            $ description_greenmountaintribe10 = "The Tribe used to thrive on {color=#f6d6bd}High Island{/color}, but they were thrown out from the original {color=#f6d6bd}Green Mountain{/color} - the volcano - by the corsairs of {color=#f6d6bd}Hovlavan{/color} when they refused to join the city."
            $ renpy.notify("Journal updated: Find the Roadwarden")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Journal updated: Find the Roadwarden')
            $ questionpreset = "cephasgaiane1"
            menu:
                '{color=#f6d6bd}Cephas{/color} runs his stern eyes over you. “To a place ‘at doesn’t need yet anot’er cityfolk. Our old home, {color=#f6d6bd}High Island{/color}. T’ place we lost to t’ dragons of {color=#f6d6bd}Hovlavan{/color}, and where we will return once t’ cities fall.”
                \n\n“To {color=#f6d6bd}T’ Green Mountain{/color},” {color=#f6d6bd}Gaiane{/color} adds with an excited whisper.
                \n\nWhen asked about the reason why the roadwarden wanted to reach this place at all, {color=#f6d6bd}the shaman{/color} struggles with finding the right words. “He believed ‘ere was a... key to his answers ‘tere. A link between t’ homes of our Tribe, and the oldest streets of {color=#f6d6bd}Hovlavan{/color}, one’s so old they are deep beneath ‘tose you know of.”
                \n\n“I care not for any of ‘at,” {color=#f6d6bd}the chief{/color} interrupts her. “We agreed to help him get to t’ caves carved in t’ volcano, in t’ heart of our homeland, for he was meant to share wit’ us whatever he sees, or learns. Now he’s lost.”
                '
                '(cephasgaiane1 set)':
                    pass
        label cephasgaiane_about_asterion302:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I {i}need{/i} to learn where {color=#f6d6bd}Asterion{/color} went.”')
            $ cephasgaiane_about_asterion3 = 2
            $ cephasgaiane_about_mountain = 1
            $ asterion_highisland_knowsabout = 1
            $ asterion_highisland_clues += 5
            $ description_highisland05 = "In distant times, it used to be a home to {color=#f6d6bd}The Tribe of The Green Mountain{/color}, who were then pushed away by {color=#f6d6bd}Hovlavan’s{/color} army."
            $ quest_asterion_description13 = "{color=#f6d6bd}Cephas and Gaiane{/color} told me that {color=#f6d6bd}Asterion{/color} was meant to examine the state of the ruins and the caves that can be found on the island’s volcano, and to bring news about them to the Tribe."
            $ description_greenmountaintribe10 = "The Tribe used to thrive on {color=#f6d6bd}High Island{/color}, but they were thrown out from the original {color=#f6d6bd}Green Mountain{/color} - the volcano - by the corsairs of {color=#f6d6bd}Hovlavan{/color} when they refused to join the city."
            $ renpy.notify("Journal updated: Find the Roadwarden")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Journal updated: Find the Roadwarden')
            $ questionpreset = "cephasgaiane1"
            menu:
                '{color=#f6d6bd}Cephas{/color} runs his stern eyes over you. “To a place ‘at doesn’t need yet anot’er cityfolk. Our old home, {color=#f6d6bd}High Island{/color}. T’ place we lost to t’ dragons of {color=#f6d6bd}Hovlavan{/color}, and where we will return once t’ cities fall.”
                \n\n“To {color=#f6d6bd}T’ Green Mountain{/color},” {color=#f6d6bd}Gaiane{/color} adds with an excited whisper.
                \n\nWhen asked about the reason why the roadwarden wanted to reach this place at all, {color=#f6d6bd}the shaman{/color} struggles with finding the right words. “He believed ‘ere was a... key to his answers ‘tere. A link between t’ homes of our Tribe, and the oldest streets of {color=#f6d6bd}Hovlavan{/color}, one’s so old they are deep beneath ‘tose you know of.”
                \n\n“I care not for any of ‘at,” {color=#f6d6bd}the chief{/color} interrupts her. “We agreed to help him get to t’ caves carved in t’ volcano, in t’ heart of our homeland, for he was meant to share wit’ us whatever he sees, or learns. Now he’s lost.”
                '
                '(cephasgaiane1 set)':
                    pass

    label cephasgaiane_about_asterion401:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring you news of what I saw on {color=#f6d6bd}High Island{/color}.”')
        $ cephasgaiane_about_asterion4 = 1
        $ greenmountaintribe_reputation += 2
        $ quarters += 2
        $ questionpreset = 0
        menu:
            'Sharing the story of your journey takes you a long time. You get many questions from both of the leaders, and some of the more nuanced descriptions use words that are not known to them. Finally, you describe the cave, and {color=#f6d6bd}Asterion’s{/color} {i}treasure{/i}.
            \n\n{color=#f6d6bd}Gaiane{/color} looks at the rocks below her. {color=#f6d6bd}Cephas{/color} speaks in her direction, with disappointment flowing through every sound. “So after all, he was yet anot’er shell lusting after wealt’.”
            \n\nYou flinch when he reaches for his sword, but he uses it as a support for his crossed arms. “{color=#f6d6bd}Asterion{/color} is yet anot’er sign ‘at t’ cityfolk haven’t changed. Yet so far, you’ve shown us not’ing but kindness. Why have you returned to us wit’ ‘is tale, [pcname]?”
            '
            '“Maybe you could show your gratitude by, let’s say, offering me the {i}dragon horn{/i}.”' if cephasgaiane_shop and not cephasgaiane_shop_dragonhorn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe you could show your gratitude by, let’s say, offering me the {i}dragon horn{/i}.”')
                $ renpy.notify("You received the dragon horn.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the dragon horn.{/i}')
                $ item_dragonhorn = 1
                $ cephasgaiane_shop_dragonhorn = 1
                $ questsupportofthegreenmountaintribereward = "horn"
                $ questionpreset = "cephasgaiane1"
                $ quest_greenmountainsupport = 3
                menu:
                    'He smirks, then bites his bottom lip. “You crossed t’ roads and settlements of t’ peninsula, reached our village, touched {color=#f6d6bd}High Island{/color} with your feet, avoiding all ‘tese beasts... and you still seek new {i}toys{/i}?” Seeing your nod, he bursts into laughter, amplified by the echo. “Very well! I’ll ask someone to carry it to your saddles.”
                    '
                    '(cephasgaiane1 set)':
                        pass
            '“I need to speak with you about {color=#f6d6bd}Hovlavan{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to speak with you about {color=#f6d6bd}Hovlavan{/color}.”')
                $ quarters += 1
                $ questsupportofthegreenmountaintribereward = "support"
                menu:
                    'He pierces you with his cold eyes. “‘En speak.”
                    \n\nYou share the sparse information you possess. The possible arrival of the messengers, the negotiations with the settlements, the states of the roads. “If everything goes according to the officials’ plans,” you conclude, “you have no way of stopping the days of merchants and soldiers. I ask you not to change your way of life, but to agree to meet with whoever the city sends here, and to reject them with your words, not violence.”
                    \n\nThe long pause is broken by {color=#f6d6bd}Gaiane{/color}. “[pcname], apologies, but wait outside.” She speaks gently, but with a hint of melancholy. “We need to talk as a chief and a shaman, for t’ tribe’s soul is in danger.”
                    '
                    'I step out of the chamber.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step out of the chamber.')
                        $ quarters += 1
                        $ quest_greenmountainsupport = 2
                        $ renpy.notify("Quest Completed: The Support of The Tribe of The Green Mountain")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest Completed: The Support of The Tribe of The Green Mountain{/i}')
                        menu:
                            'You’re the only person who does so, and even as you hear the raised voices of the leaders, they are freely heard by all of the nearby tribesfolk. The thick Old Speech accent and distorting echo don’t allow you to catch so much as a word, but the tense atmosphere is palpable.
                            \n\nFinally, you’re asked to return to the room, and as you sit down, {color=#f6d6bd}Cephas{/color} looks you in the eyes, holding his helmet. “We will never get along wit’ ‘ose who led to our fall,” his voice got hoarse. “But let ‘em know who we are, ‘at we’re ready to tell ‘em where our lands start, so ‘ey know to avoid ‘em.”
                            '
                            '“That’s all I’m asking for.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s all I’m asking for.”')
                                if pc_goal == "iwantstatus":
                                    $ pc_goal_iwantstatuspoints += 1
                                if quest_pc_goal == 1 and pc_goal == "iwantstatus":
                                    $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                                $ questionpreset = "cephasgaiane1"
                                menu:
                                    '{color=#f6d6bd}Gaiane{/color} nods, but her eyes are absent, and her hands are clenched around dozens of small, red crystals.
                                    '
                                    '(cephasgaiane1 set)':
                                        pass
            '“I just wanted to tell you the truth. Not all cityfolk are cunning goblins.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I just wanted to tell you the truth. Not all cityfolk are cunning goblins.”')
                $ questsupportofthegreenmountaintribereward = "friendship"
                $ quest_greenmountainsupport = 3
                $ greenmountaintribe_reputation += 1
                $ questionpreset = "cephasgaiane1"
                menu:
                    '{color=#f6d6bd}Gaiane{/color} takes a deep breath, then stretches her legs out and looks at you kindly. “Your trut’ and tales are of great value, and if you come here after winter, we’ll show you honesty and a safe roof as well.”
                    '
                    '(cephasgaiane1 set)':
                        pass

label cephasgaiane_about_spiritrock01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will be difficult to explain this, but I want to learn what they think about {color=#f6d6bd}Phoibe’s{/color} situation.')
    $ cephasgaiane_about_spiritrock = 1
    $ minutes += 10
    $ questionpreset = "cephasgaiane1"
    menu:
        'While it turns out that the leaders are quite familiar with {i}spirit rocks{/i}, {color=#f6d6bd}the shaman{/color} is hesitant to judge if they can be used in the way described by {color=#f6d6bd}Photios{/color}. “In t’ tales I carry, t’ strengt’ of pneuma shapes t’ same way t’ muscles of a shell does. ‘Tere were heroes born as weaklings, as ‘tere were ones wit’ little breat’. And ‘tese souls risked ‘teir lives to learn, wondering far and deep, finding sages and amulets. But as ‘tere are no stories of an armless woman who grew to be a hunter, ‘tere are also none of a spell-less man who mastered magic.”
        '
        '(cephasgaiane1 set)':
            pass

label cephasgaiane_about_plague01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Old Págos{/color}, the village on the opposite side of the peninsula, was attacked by a plague.”')
    $ cephasgaiane_about_plague = 1
    $ custom1 = "{color=#f6d6bd}Cephas{/color} glances at the puzzled {color=#f6d6bd}shaman{/color} and says a word in the Old Speech, causing her to gasp and switch the positions of a few bones. He then looks at you. “Terrible, but we can do not’ing. They have to endure it, and we’ll not risk breat’ing their air.”"
    jump cephasgaiane_about_notcaring01

    label cephasgaiane_about_necromancers01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you heard about the necromancers living in the far west?”')
        $ cephasgaiane_about_necromancers = 1
        $ custom1 = "“Our...” {color=#f6d6bd}Cephas{/color} hesitates, selecting the word carefully. “{i}Scouts{/i} saw the awoken, yes. But ‘ey won’t reach us, and we’ll not die purging ‘em.”"
        jump cephasgaiane_about_notcaring01

    label cephasgaiane_about_bandits01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The roads in the west grow more dangerous as they struggle with bandits.”')
        $ cephasgaiane_about_bandits = 1
        $ custom1 = "“Our...” {color=#f6d6bd}Cephas{/color} hesitates, selecting the word carefully. “{i}Scouts{/i} saw their deeds, yes. But ‘ey won’t reach us, and we’ve not’ing to gain from fighting ‘em.”"
        jump cephasgaiane_about_notcaring01

    label cephasgaiane_about_steephouse01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about the ruins of the village at the southern road.”')
        $ custom1 = "“We took no part in its collapse,” {color=#f6d6bd}Cephas{/color} speaks slowly, shaking his head as he glances at {color=#f6d6bd}the shaman{/color}. “But to avoid war, we promised not to speak of it.”"
        jump cephasgaiane_about_notcaring01

    label cephasgaiane_about_notcaring01:
        $ cephasgaiane_about_notcaring = 1
        $ cephasgaiane_about_steephouse1 = 1
        $ oldpagos_plague_warnedplaces += 1
        $ questionpreset = "cephasgaiane1"
        $ description_greenmountaintribe06 = "According to {color=#f6d6bd}Gaiane{/color}, they cut off contact with the other villages ten years ago."
        $ quest_ruins_10yclue06 = "{color=#f6d6bd}The Tribe of The Green Mountain{/color} cut off contact with the other villages."
        menu:
            '[custom1]
            \n\n{color=#f6d6bd}Gaiane{/color} nods in agreement, even though there’s a sadness to her voice. “Souls and tribes come and go, but t’ woods abide. For ten years now, we have let the lowlanders keep to ‘temselves.”
            '
            '(cephasgaiane1 set)':
                pass

label cephasgaiane_about_steephouse201:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I confronted {color=#f6d6bd}Thais{/color} about {color=#f6d6bd}Steep House{/color}. Her village will soon be under new leadership.”')
    $ cephasgaiane_about_steephouse2 = 1
    $ greenmountaintribe_reputation += 2
    $ questionpreset = "cephasgaiane1"
    menu:
        'They look at you in silence. “To me, {color=#f6d6bd}‘Tais{/color} is only a story,” {color=#f6d6bd}Gaiane{/color} speaks carefully, “t’ story not of a leader, but of a tyrant.”
        \n\n“My cousin lost his life in {color=#f6d6bd}Steep House{/color}, fell in love with a young druidess,” {color=#f6d6bd}Cephas{/color} looks at you with a sinister grin, or maybe his scars make you see it that way. “He did not’ing wrong, lived ‘tere and cut stones. {color=#f6d6bd}‘Tais’{/color} beasts were always loud, and just like the real howlers, they owt to hang from a branch.”
        \n\n{color=#f6d6bd}Gaiane{/color} scowls at him, and even though she may be younger than half his age, he suddenly seems much smaller, crossing his arms. “You’re a good soul to make ‘tis happen,” she looks at you again, now holding a small, green gem. “Wit’ {i}her{/i} as a chief, we were waiting for t’ wrat’ of t’ herds to fall upon ‘em.”
        '
        '(cephasgaiane1 set)':
            pass

label cephasgaiane_about_orchard01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wonder... Is it true that you still maintain the old orchard at the heart of the woods?”')
    $ cephasgaiane_about_orchard = 1
    $ questionpreset = "cephasgaiane1"
    menu:
        '“I know t’ place,” {color=#f6d6bd}the chief{/color} glances at the surprised {color=#f6d6bd}shaman{/color}, then scowls at you like a kid caught in the act. He puts his right foot on his helmet, so that his arm can now point at your chest without leaving its comfortable support. “Our hunters and scouts have t’ right to do as ‘ey please. No one is forbidden to leave our village, or to talk wit’ t’ lowlanders. Someone used to love ‘tis place, before we saw t’ northern tribes for what ‘ey are. ‘At’s all ‘tere is to it.”
        '
        '(cephasgaiane1 set)':
            pass

##########################
label cephasgaiane_about_highislandALL:
    label cephasgaiane_about_highisland01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can we talk about {color=#f6d6bd}High Island{/color}?”')
        $ cephasgaiane_about_highisland = 1
        $ questionpreset = "cephasgaiane2"
        menu:
            '“We can, but no soul of our tribe has been ‘ere in generations,” even a gentle frown changes {color=#f6d6bd}the chief’s{/color} scarred face greatly. “We won’t return ‘tere while t’ cities remain a t’reat.”
            '
            '(cephasgaiane2 set)':
                pass

    label cephasgaiane_about_highisland02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have more questions about {color=#f6d6bd}High Island{/color}.”')
        $ questionpreset = "cephasgaiane2"
        menu:
            '“Ask.”
            '
            '(cephasgaiane2 set)':
                pass

    label cephasgaiane_about_highisland_question101:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How can I get there?”')
        if (greenmountaintribe_reputation+(appearance_charisma/2)) < greenmountaintribe_asterion_permission_threshold:
            $ cephasgaiane_about_highisland_question1 = 1
            $ questionpreset = "cephasgaiane2"
            menu:
                '{color=#f6d6bd}The chief{/color} answers slowly, with a night-cold voice. “We’ll cut any limb ‘at so much as touches our homeland.”
                '
                '(cephasgaiane2 set)':
                    pass
        else:
            $ cephasgaiane_about_highisland_question1 = 2
            $ cephasgaiane_about_highisland_permission = 1
            $ cephasgaiane_about_highisland_questions += 1
            $ highisland_howtoreach_pcknows = 1
            $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
            $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
            $ description_highisland03 = "The only way to get to the surface of the island is to reach it during nighttime."
            $ description_highisland08a = "According to {color=#f6d6bd}Gaiane{/color}, I need to reach the “northern” waterfall."
            $ questionpreset = "cephasgaiane2"
            menu:
                '“Don’t you know T’ Tribe cuts any limb ‘at so much as touches our homeland?” {color=#f6d6bd}The chief{/color} observes your hands while rubbing his own, dried and covered with scars. “You want it to turn into a pyre for radardens?”
                \n\n{color=#f6d6bd}The shaman’s{/color} quiet voice is like a touch of dew. “If you land ‘tere, bring us {color=#f6d6bd}Asterion{/color}, or your own tale, [pcname]. Or we’ll not forgive you.” Her tone carries no question, no request.
                \n\nShe then gets off the stool, crouches above the fabric, and grabs a few small bones. She arranges them into a curved line. “T’ coast of {color=#f6d6bd}High Island{/color}, as tall as a ship,” she doesn’t look at you. “Here is nort’,” she marks it with a white pebble, “closer to {color=#f6d6bd}Gale Rocks{/color},” a red rock, far away from the island. “Swim here, to t’ nort’ern waterfall,” her hands return to the island, placing a blue gem in what seems to be a corner.
                \n\nWhen she meets your eyes, her voice starts to quicken, heedless of stumbling over words. “‘At waterfall hides a cave, an old harbor. Boat can’t land ‘tere wit’out t’ high tide of t’ night.”
                \n\nJust in case, you ask her to repeat, so you can memorize it, and {color=#f6d6bd}Cephas{/color} helps to summarize it.
                '
                '(cephasgaiane2 set)':
                    pass
        label cephasgaiane_about_highisland_question102:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I {i}need{/i} to reach that place.”')
            $ cephasgaiane_about_highisland_question1 = 2
            $ cephasgaiane_about_highisland_permission = 1
            $ cephasgaiane_about_highisland_questions += 1
            $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
            $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
            $ description_highisland03 = "The only way to get to the surface of the island is to reach it during nighttime."
            $ description_highisland08a = "According to {color=#f6d6bd}Gaiane{/color}, I need to reach the “northern” waterfall."
            $ highisland_howtoreach_pcknows = 1
            $ questionpreset = "cephasgaiane2"
            menu:
                '{color=#f6d6bd}The chief{/color} observes your hands while rubbing his own, dried and covered with scars. “You want it to turn into a pyre for radardens?”
                \n\n{color=#f6d6bd}The shaman’s{/color} quiet voice is like a touch of dew. “If you land ‘tere, bring us {color=#f6d6bd}Asterion{/color}, or your own tale, [pcname]. Or we’ll not forgive you.” Her tone carries no question, no request.
                \n\nShe then gets off the stool, crouches above the fabric, and grabs a few small bones. She arranges them into a curved line. “T’ coast of {color=#f6d6bd}High Island{/color}, as tall as a ship,” she doesn’t look at you. “Here is nort’,” she marks it with a white pebble, “closer to {color=#f6d6bd}Gale Rocks{/color},” a red rock, far away from the island. “Swim here, to t’ nort’ern waterfall,” her hands return to the island, placing a blue gem in what seems to be a corner.
                \n\nWhen she meets your eyes, her voice starts to quicken, heedless of stumbling over words. “‘At waterfall hides a cave, an old harbor. Boat can’t land ‘tere wit’out t’ high tide of t’ night.”
                \n\nJust in case, you ask her to repeat, so you can memorize it, and {color=#f6d6bd}Cephas{/color} helps to summarize it.
                '
                '(cephasgaiane2 set)':
                    pass

    label cephasgaiane_about_highisland_question101alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Would it matter to you if I were to land there?”')
        if (greenmountaintribe_reputation+(appearance_charisma/2)) < greenmountaintribe_asterion_permission_threshold:
            $ cephasgaiane_about_highisland_question1 = 1
            $ questionpreset = "cephasgaiane2"
            menu:
                '{color=#f6d6bd}The chief{/color} answers slowly, with a night-cold voice. “We’ll cut any limb ‘at so much as touches our homeland.”
                '
                '(cephasgaiane2 set)':
                    pass
        else:
            $ cephasgaiane_about_highisland_question1 = 2
            $ cephasgaiane_about_highisland_permission = 1
            $ cephasgaiane_about_highisland_questions += 1
            $ highisland_howtoreach_pcknows = 1
            $ questionpreset = "cephasgaiane2"
            menu:
                '“Don’t you know T’ Tribe cuts any limb ‘at so much as touches our homeland?” {color=#f6d6bd}The chief{/color} observes your hands while rubbing his own, dried and covered with scars. “You want it to turn into a pyre for radardens?”
                \n\n{color=#f6d6bd}The shaman’s{/color} quiet voice is like a touch of dew. “If you land ‘tere, bring us {color=#f6d6bd}Asterion{/color}, or your own tale, [pcname]. Or we’ll not forgive you.” Her tone carries no question, no request.
                '
                '(cephasgaiane2 set)':
                    pass
        label cephasgaiane_about_highisland_question102alt:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I would still appreciate your permission to search the island.”')
            $ cephasgaiane_about_highisland_question1 = 2
            $ cephasgaiane_about_highisland_permission = 1
            $ cephasgaiane_about_highisland_questions += 1
            $ highisland_howtoreach_pcknows = 1
            $ questionpreset = "cephasgaiane2"
            menu:
                '{color=#f6d6bd}The chief{/color} observes your hands while rubbing his own, dried and covered with scars. “You want it to turn into a pyre for radardens?”
                \n\n{color=#f6d6bd}The shaman’s{/color} quiet voice is like a touch of dew. “If you land ‘tere, bring us {color=#f6d6bd}Asterion{/color}, or your own tale, [pcname]. Or we’ll not forgive you.” Her tone carries no question, no request.
                '
                '(cephasgaiane2 set)':
                    pass

    label cephasgaiane_about_highisland_question201:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why don’t you want anyone to land there?”')
        $ cephasgaiane_about_highisland_questions += 1
        $ cephasgaiane_about_highisland_question2 = 1
        $ questionpreset = "cephasgaiane2"
        menu:
            '“What good could it bring us?” {color=#f6d6bd}The chief{/color} leans back, as if there’s nothing to talk about. After a few breaths, {color=#f6d6bd}the shaman{/color} chips in.
            \n\n“We’ll enter t’ island like a traveler returning to ‘eir bed. Eyes of t’ cityfolk see not our homeland, but ‘eir failed search for iron. Eyes of t’ ot’er tribes see our lost treasure not as our soil, sky, and rains, but only as belongings to grab and sell. Our friends help us keep an eye on t’ island, and if anyone breaks our rule, we’ll be ready to swim ‘tere, and stop ‘eir greed. But it’s no longer a home to any human soul.”
            '
            '(cephasgaiane2 set)':
                pass

    label cephasgaiane_about_highisland_question301:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s the story of the island?”')
        $ cephasgaiane_about_highisland_questions += 1
        $ cephasgaiane_about_highisland_question3 = 1
        $ quarters += 1
        $ questionpreset = "cephasgaiane2"
        # remember to update the journal
        menu:
            '{color=#f6d6bd}Gaiane{/color} smiles and starts to speak in the Old Speech, as if she’s repeating the same tale for the hundredth time, then chuckles. Once she shifts to the City Tongue, she struggles at some points, but {color=#f6d6bd}Cephas{/color} provides her with words and phrases, or fills the gaps on his own.
            \n\nThe Green Mountain, the life-giving volcano in the center of the island, has been home to the Tribe for longer than anyone can remember, “as we’re older ‘tan any of T’ Ten Cities” - though you doubt there are any ways to verify such a claim. {color=#f6d6bd}The shaman{/color} spends a good few minutes describing the days of her ancestors - through hardship, they managed to tame enough land to grow vegetables, and made a great chunk of the island their forest garden. After finding the iron and copper veins, they had enough tools and weapons to save their offspring from back-breaking labor. She’s also eager to describe the deeds of many families and heroes, and the unique herbs with their “beautiful names”, but {color=#f6d6bd}the chief{/color} asks her to move on.
            \n\nFor most of its existence, {color=#f6d6bd}Hovlavan{/color} avoided the island, finding hardship in getting close to it, and since “the pagans” were reluctant to accept dragon bones, the merchants saw little value in their wares. However, once the tribes of the peninsula noticed the growing supply of alloys used by the islandfolk and their fishers, the news reached the city.
            \n\nA little more than two hundred years ago, the officials tried to negotiate a new trade deal with the locals, but to no avail. Finally, they allowed the corsairs to start their usual efforts, putting to use the growing height of their ships. At first, they harrassed the fishers, then landed on the island itself. The Tribe was ready to fight for what was theirs, but the cruelty they faced outmatched them. The kidnappings made the locals afraid to leave their walls, and then the raids enslaved whole hamlets, or burned many crucial structures.
            \n\nUsing traps and their knowledge of the terrain, The Tribe managed to kill more than they lost, but the corsair ships kept coming, always led by new, yet even more experienced captains. After a few bloody battles, the forest fires started, and the locals understood they had little time before the wrath of the herds would trample them to death.
            \n\n“We are t’ eight’ generation of T’ Tribe living here, so close to t’ coast, yet so far from it,” she ends her tale. “Taming t’ new grounds was harsh, and once t’ first children born in ‘tese tunnels started breat’ing, only a fift’ of T’ Tribe was still here to welcome ‘em.”
            '
            '(cephasgaiane2 set)':
                pass

    label cephasgaiane_about_highisland_question401:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why won’t your tribe try to reclaim the island?”')
        $ cephasgaiane_about_highisland_questions += 1
        $ cephasgaiane_about_highisland_question4 = 1
        $ questionpreset = "cephasgaiane2"
        menu:
            '“T’ root of our torment survived t’ plague, t’ invasion, and disasters now known only to t’ oldest tales,” {color=#f6d6bd}Gaiane{/color} grabs a few small bones from the fabric beneath her and starts to roll them between the palms of her hands. “We have no strengt’ to fight it, no hope to defeat it. But we can wait in humbleness, and hope t’ spirits will turn ‘eir face away once our enemies come to ‘em for help.”
            \n\n{color=#f6d6bd}Cephas{/color} rests a hand on his side. “Returning would anger the herds, and cost us dearly. Yet after one, two generations, once our walls and children grow strong,” he looks at an infant being fed by the fire, “t’ corsairs will once again bring torches and chains, for ‘eir {i}Wright{/i} allows ‘em to murder freely.” He utters the soulcarrier’s name with disgust. “Leading our Tribe to ‘eir homeland is t’ dream of every chief and every shaman, but it’s a dream of t’ prideful.”
            '
            '(cephasgaiane2 set)':
                pass

    label cephasgaiane_about_highisland_question601:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is the island dangerous?”')
        $ cephasgaiane_about_highisland_questions += 1
        $ cephasgaiane_about_highisland_question6 = 1
        $ questionpreset = "cephasgaiane2"
        menu:
            '{color=#f6d6bd}Cephas{/color} shrugs. “As dangerous as t’ wildest woods and hills. Its roads are no more, and spiders and apemen now live in our houses. T’ cityfolk who tried to take our lands may still be ‘tere, walking shells wit’out souls, but after so much time, ‘ey likely went after blood on t’ mainland.”
            '
            '(cephasgaiane2 set)':
                pass

    label cephasgaiane_about_highisland_question701:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is there something that could help me explore the island?”')
        $ cephasgaiane_about_highisland_questions += 1
        $ cephasgaiane_about_highisland_question7 = 1
        if quest_sleepinggiant == 1 or quest_sleepinggiant == 2:
            $ renpy.notify("Journal updated: The Sleeping Giant")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Sleeping Giant{/i}')
        $ quest_sleepinggiant_description00a = "I could put some time into learning more about the statue of a giant, and learn the “map” it hides."
        $ questionpreset = "cephasgaiane2"
        menu:
            '“T’ second generation ‘at lived on ‘tis mountain knew it would one day forget its homeland,” {color=#f6d6bd}Gaiane{/color} pauses, observing a young woman adding wood to the fire. “‘Ey built t’ statue of a spirit ‘at protected us from t’ flames of {color=#f6d6bd}T’ Green Mountain{/color}, T’ Sleeping Giant. ‘Ey still hold t’ key to t’ island.”
            \n\n“The {i}key{/i},” you repeat, and {color=#f6d6bd}Cephas{/color} tilts his head. “A {i}map{/i}, I’d say.”
            '
            '(cephasgaiane2 set)':
                pass

    label cephasgaiane_about_highisland_question801:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve time now. Teach me what I need to know about this statue.”')
        $ cephasgaiane_about_highisland_questions += 1
        $ cephasgaiane_about_highisland_question8 = 1
        if giantstatue_pray_knows:
            $ minutes += 5
            $ custom1 = "While your knowledge of the prayer sparks some questions, {color=#f6d6bd}the chief and the shaman{/color} accept it quickly, even commend you for it. They move on to the explanation of the signs that the statue hides."
        else:
            if pc_religion == "pagan":
                $ custom1 = "“Stand in front of it, kneel, bow your head,” starts {color=#f6d6bd}Gaiane{/color}, with a tone of the grandparent instructing a child how to say “thank you”.\n\n“Say ‘tese words at least ten times.” She utters words in the Old Speech for a while, though her thick accent leaves you unsure about parts of it. She then gives you a warm smile, and repeats much slower. “{i}Oh, the spirits and our giantfathers, be with our paths, and not in thunders. The night is here, and we are but a shadow. The shining stones are falling in the grass, the apescreams of our mouths are weak and short. We come from a flame, and vanish in the fog - and we taste life, to the last breath.{/i}”\n\nYou then spend a couple of minutes repeating her words and mimicking her accent. It’s not too hard to memorize it - the rhythm makes it more of a poem than a speech.\n\nFinally, {color=#f6d6bd}the chief and the shaman{/color} move on to the “shining lights” which the statue will reveal."
                $ quarters += 1
            else:
                $ custom1 = "“Stand in front of it, kneel, bow your head,” starts {color=#f6d6bd}Gaiane{/color}, with the tone of a grandparent instructing a child how to say “thank you”.\n\n“Say ‘tese words at least ten times.” She utters words in the Old Speech for a while, then gives you a warm smile. “Oh, t’ spirits and t’ giantfathers, be with our paths, and not in t’unders. T’ night is here, and we are but a shadow. T’ gems are falling in t’ grass, t’ ape sounds of our mout’s are weak and short. We come from a flame, and vanish in t’ fog - and we taste life, to t’ last breat’.”\n\nYou then spend a good couple of minutes repeating the words in her thick accent, not always knowing when one of them ends and another begins. But the longer you repeat the prayer, the easier it is for you to get into the rhythm and notice that the words are more of a poem than a speech.\n\nFinally, {color=#f6d6bd}the chief and the shaman{/color} move on to the “shining lights” which the statue will reveal."
                $ quarters += 2
        $ giantstatue_pray_knows = 1
        $ giantstatue_pray_map_meaning = 1
        $ description_highisland15 = "{color=#f6d6bd}Cephas{/color} described the meaning of the map of The Sleeping Giant as follows: “T’ great green light in t’ center is {color=#f6d6bd}T’ Green Mountain{/color}, and t’ great blue one next to it - t’ home of T’ Tribe. T’ others mark buildings. T’ dim ones were lost even before t’ days of t’ corsairs. We abandoned t’ brighter ones only eight generations ago. Blue lights stand for hamlets. White - camps and dolmens. Yellow - watchtowers. T’ orange... Are different, as ‘ey mean the lairs of t’ greatest beasts.”"
        if pc_class == "scholar":
            $ custom2 = "of writing everything down"
        else:
            $ custom2 = "of making sure you’ve memorized everything"
        $ questionpreset = "cephasgaiane2"
        menu:
            '[custom1] “T’ great green light in t’ center is {color=#f6d6bd}T’ Green Mountain{/color}, and t’ great blue one next to it - t’ home of T’ Tribe,” {color=#f6d6bd}Cephas{/color} explains. “T’ others mark buildings. T’ dim ones were lost even before t’ days of the corsairs. We abandoned t’ brighter ones only eight generations ago. Blue lights stand for hamlets. White - camps and dolmens. Yellow - watchtowers. T’ orange...” He pauses. “Are different, as ‘ey mean the lairs of t’ greatest beasts.”
            \n\nAfter a few more minutes [custom2], you need a momentary break, as the heavy air is giving you a headache.
            '
            '(cephasgaiane2 set)':
                pass

    label cephasgaiane_about_highisland_question801alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Actually, I was already able to awaken the statue. But I’m not sure how to understand it.”')
        $ cephasgaiane_about_highisland_questions += 1
        $ cephasgaiane_about_highisland_question8 = 1
        $ minutes += 5
        $ giantstatue_pray_knows = 1
        $ giantstatue_pray_map_meaning = 1
        $ description_highisland15 = "{color=#f6d6bd}Cephas{/color} described the meaning of the map of The Sleeping Giant as follows: “T’ great green light in t’ center is {color=#f6d6bd}T’ Green Mountain{/color}, and t’ great blue one next to it - t’ home of T’ Tribe. T’ others mark buildings. T’ dim ones were lost even before t’ days of t’ corsairs. We abandoned t’ brighter ones only eight generations ago. Blue lights stand for hamlets. White - camps and dolmens. Yellow - watchtowers. T’ orange... Are different, as ‘ey mean the lairs of t’ greatest beasts.”"
        if pc_class == "scholar":
            $ custom2 = "of writing everything down"
        else:
            $ custom2 = "of making sure you’ve memorized everything"
        $ questionpreset = "cephasgaiane2"
        menu:
            'While your deed sparks some questions, {color=#f6d6bd}the chief and the shaman{/color} accept it quickly, even commend you for it. “T’ great green light in t’ center is {color=#f6d6bd}T’ Green Mountain{/color}, and t’ great blue one next to it - t’ home of T’ Tribe,” {color=#f6d6bd}Cephas{/color} explains. “T’ others mark buildings. T’ dim ones were lost even before t’ days of the corsairs. We abandoned t’ brighter ones only eight generations ago. Blue lights stand for hamlets. White - camps and dolmens. Yellow - watchtowers. T’ orange...” He pauses. “Are different, as ‘ey mean the lairs of t’ greatest beasts.”
            \n\nAfter a few more minutes [custom2], you’re ready to change the topic.
            '
            '(cephasgaiane2 set)':
                pass

##########################
label cephasgaiane_shop01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The roads are dangerous. Do you have any useful equipment to sell?”')
    $ questionpreset = 0
    $ cephasgaiane_shop = 1
    $ renpy.notify("New trader unlocked.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
    if pc_religion == "pagan":
        $ custom1 = "“{i}We have more horns than we need,{/i}” {color=#f6d6bd}the shaman{/color} chips in, and after a bit of a pause, {color=#f6d6bd}Cephas{/color} agrees."
    else:
        $ custom1 = "“We have...” {color=#f6d6bd}The shaman{/color} chips in, but then pauses, frowning. She says something in the Old Speech, and {color=#f6d6bd}Cephas{/color} nods. “You mean {i}horns{/i},” he says, then looks at you again."
    menu:
        '{color=#f6d6bd}The chief{/color} scoffs. “Why, do {i}you{/i} have somet’ing we may want? We don’t have dragon bones, don’t trade, and we need what we have.”
        \n\n[custom1] “We could barter for it. Our guards and scouts use the horns of many beasts, but ‘tere’s one type we don’t use any more.”
        \n\n“T’ war horn,” {color=#f6d6bd}Gaiane{/color} adds ominously, “roars like a dragon.”
        \n\n{color=#f6d6bd}The chief{/color} smirks. “‘At’s right. Most beasts flee when ‘ey hear it. But can’t show you how it sounds here, we’d go deaf.”
        '
        '“Can I at least see it?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I at least see it?”')
            show screen shopscreen with dissolve
            jump greenmountaintribechiefaftertrading01

    label greenmountaintribechiefaftertrading01:
        $ questionpreset = "cephasgaiane1"
        menu:
            'After a moment, someone brings you the horn.
            '
            '(cephasgaiane1 set)':
                pass

    label cephasgaiane_shop02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s barter.”')
        show screen shopscreen with dissolve
        $ questionpreset = "cephasgaiane1"
        menu:
            'After a moment, someone brings you the horn.
            '
            '(cephasgaiane1 set)':
                pass

    label cephasgaiane_shop_freegift01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to offer you a gift, as a sign of my good will.”')
        $ cephasgaiane_shop_select = "freegift"
        $ shop = "greenmountaintribechief"
        $ questionpreset = 0
        show screen selling()
        menu:
            'They exchange looks.
            '
            '“Just give me a moment to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just give me a moment to think about it.”')
                jump greenmountaintribechiefafterinteraction01

    label greenmountaintribechiefaftertrading02:
        #if cephasgaiane_shop_select == "dragonhorn":
        #    $ custom1 = ""
        $ cephasgaiane_shop_select = 0
        $ quarters += 1
        hide screen selling
        $ questionpreset = "cephasgaiane1"
        menu:
            'Finishing the transaction takes a good few minutes since you have to get to {color=#f6d6bd}[horsename]{/color}, show {color=#f6d6bd}Cephas{/color} what you have - {color=#f6d6bd}Gaiane{/color} refused to join you - then return to the cave. Once {color=#f6d6bd}the saurian rider{/color} takes your gift, the other locals discuss their new possession enthusiastically.
            '
            '(cephasgaiane1 set)':
                pass

    label greenmountaintribechiefbarteringfordragonhorn01:
        $ cephasgaiane_shop_select = "dragonhorn"
        $ shop = "greenmountaintribechief"
        $ questionpreset = 0
        show screen selling()
        menu:
            'You look at the horn, thinking of the things you could offer to the tribe.
            '
            '“Maybe another time.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe another time.”')
                jump greenmountaintribechiefafterinteraction01

    label greenmountaintribechiefsellingsealskin:
        $ questionpreset = 0
        menu:
            '“We’ve enough pelts,” starts {color=#f6d6bd}Cephas{/color}, but {color=#f6d6bd}Gaiane’s{/color} eyes widen. “You sure you have it? Seals are of great value to our tales, ‘eir skins are what we used to wear... {i}Many{/i} years ago.” She looks at {color=#f6d6bd}the chief{/color}. “We should hang it on a wall of...” She whispers a word in the Old Speech, and you don’t catch it. Finally, he agrees.
            '
            '“You can see it outside.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can see it outside.”')
                if cephasgaiane_shop_select == "dragonhorn":
                    $ renpy.notify("You traded the sealskin\nfor the dragon horn.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You traded the sealskin for the dragon horn.{/i}')
                    $ item_dragonhorn = 1
                    $ cephasgaiane_shop_dragonhorn = 1
                elif cephasgaiane_shop_select == "freegift":
                    $ renpy.notify("You gave away the sealskin.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the sealskin.{/i}')
                $ item_sealskin = 0
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribechiefaftertrading02
            '“I need to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump greenmountaintribechiefafterinteraction01

    label greenmountaintribechiefsellingbeholderroot:
        $ questionpreset = 0
        menu:
            '{color=#f6d6bd}Cephas{/color} frowns. “We’ve known for years ‘at {color=#f6d6bd}Howler’s{/color} breat’s in dark pneuma. May you study such a root, shaman?” They exchange looks, and while she seems a bit smaller ever since you described the twisted root, she sighs. “Can try.”
            '
            '“You can see it outside.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can see it outside.”')
                if cephasgaiane_shop_select == "dragonhorn":
                    $ renpy.notify("You traded the weird root\nfor the dragon horn.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You traded the weird root for the dragon horn.{/i}')
                    $ item_dragonhorn = 1
                    $ cephasgaiane_shop_dragonhorn = 1
                elif cephasgaiane_shop_select == "freegift":
                    $ renpy.notify("You gave away the weird root.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the weird root.{/i}')
                $ item_beholderroot = 0
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribechiefaftertrading02
            '“I need to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump greenmountaintribechiefafterinteraction01

    label greenmountaintribechiefsellingaxe02:
        $ questionpreset = 0
        if cephasgaiane_shop_select == "dragonhorn":
           $ custom1 = " a loud horn"
        else:
           $ custom1 = " our smiles"
        menu:
            '“We need no more blades,” starts {color=#f6d6bd}Gaiane{/color}, but {color=#f6d6bd}Cephas{/color} gestures for her to wait. “Let me take a look. Bronze lasts for lifetimes, it’s a gem well wort’[custom1].”
            \n\nShe rolls her eyes, but says nothing.
            '
            '“Come outside, then.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Come outside, then.”')
                if cephasgaiane_shop_select == "dragonhorn":
                    $ renpy.notify("You traded the bronze axe\nfor the dragon horn.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You traded the bronze axe for the dragon horn.{/i}')
                    $ item_dragonhorn = 1
                    $ cephasgaiane_shop_dragonhorn = 1
                elif cephasgaiane_shop_select == "freegift":
                    $ renpy.notify("You gave away the bronze axe.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the bronze axe.{/i}')
                $ item_axe02alt = 0
                $ item_axehead = 0
                $ item_axeset = 0
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribechiefaftertrading02
            '“I need to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump greenmountaintribechiefafterinteraction01

    label greenmountaintribechiefsellingaxe03:
        $ questionpreset = 0
        if cephasgaiane_shop_select == "dragonhorn":
           $ custom1 = " a loud horn"
        else:
           $ custom1 = " our smiles"
        menu:
            '“We need no more blades,” starts {color=#f6d6bd}Gaiane{/color}, but {color=#f6d6bd}Cephas{/color} gestures for her to wait. “Let me take a look. If t’ radarden describes it rightly, a weapon such as ‘tis is a gem well wort’[custom1].”
            \n\nShe rolls her eyes, but says nothing.
            '
            '“You can see it outside.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can see it outside.”')
                if cephasgaiane_shop_select == "dragonhorn":
                    $ renpy.notify("You traded the battle axe\nfor the dragon horn.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You traded the battle axe for the dragon horn.{/i}')
                    $ item_dragonhorn = 1
                    $ cephasgaiane_shop_dragonhorn = 1
                elif cephasgaiane_shop_select == "freegift":
                    $ renpy.notify("You gave away the battle axe.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the battle axe.{/i}')
                $ item_axe03 = 0
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribechiefaftertrading02
            '“I need to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump greenmountaintribechiefafterinteraction01

    label greenmountaintribechiefsellingcidercask:
        $ questionpreset = 0
        menu:
            'Since {i}cider{/i} is an unknown word in the tribe, you describe it as {i}sweet apple beer{/i}, and warn them that it won’t stay fresh for long. “We could open it after the harvest,” says {color=#f6d6bd}the chief{/color}, and {color=#f6d6bd}the shaman{/color} smiles in agreement. “Someone young may get inspired.”
            '
            '“You can see it outside.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can see it outside.”')
                if cephasgaiane_shop_select == "dragonhorn":
                    $ renpy.notify("You traded the cider cask\nfor the dragon horn.")
                    $ item_dragonhorn = 1
                    $ cephasgaiane_shop_dragonhorn = 1
                    if quest_foggy3whitemarshes == 1:
                        $ quest_foggy3whitemarshes_description07 = "I sold the cask outside of {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Foggy{/color} won’t learn about it."
                        $ renpy.notify("Journal updated: Cask of Cider\nYou traded the cask of cider\nfor the dragon horn.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Cask of Cider. You traded the cask of cider for the dragon horn.{/i}')
                    else:
                        $ renpy.notify("You traded the cask of cider\nfor the dragon horn.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You traded the cask of cider for the dragon horn.{/i}')
                elif cephasgaiane_shop_select == "freegift":
                    $ renpy.notify("You gave away the cider cask.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the cider cask.{/i}')
                    if quest_foggy3whitemarshes == 1:
                        $ quest_foggy3whitemarshes_description07 = "I sold the cask outside of {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Foggy{/color} won’t learn about it."
                        $ renpy.notify("Journal updated: Cask of Cider\nYou traded the cask of cider\nfor the dragon horn.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Cask of Cider. You traded the cask of cider for the dragon horn.{/i}')
                    else:
                        $ renpy.notify("You traded the cask of cider\nfor the dragon horn.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You traded the cask of cider for the dragon horn.{/i}')
                $ item_cidercask = 0
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribechiefaftertrading02
            '“I need to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump greenmountaintribechiefafterinteraction01

    label greenmountaintribechiefsellingironingot:
        $ questionpreset = 0
        menu:
            'Bored, {color=#f6d6bd}Gaiane{/color} speaks to {color=#f6d6bd}the chief{/color}. “We need?” He chuckles. “Always. But we’ve got iron already, unlike good steel. I need to take a look, first.”
            '
            '“Let’s go and see it, then.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s go and see it, then.”')
                if cephasgaiane_shop_select == "dragonhorn":
                    $ renpy.notify("You traded the iron ingot\nfor the dragon horn.")
                    $ item_dragonhorn = 1
                    $ cephasgaiane_shop_dragonhorn = 1
                elif cephasgaiane_shop_select == "freegift":
                    $ renpy.notify("You gave away the iron ingot.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the iron ingot.{/i}')
                $ item_ironingot_sold_greenmountain = 1
                $ item_ironingot = 0
                $ greenmountaintribe_reputation += 1
                jump greenmountaintribechiefaftertrading02
            '“I need to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump greenmountaintribechiefafterinteraction01

    label greenmountaintribechiefssellingspices:
        $ questionpreset = 0
        menu:
            '{color=#f6d6bd}Gaiane{/color} looks at you with widened eyes, moving her legs as if she wants to stand up right away. “For medicine!”
            \n\n{color=#f6d6bd}Cephas{/color} chuckles. “You mean {i}for t’ cooks{/i}, I t’ink, but we’ll split. Let me smell some of it, [pcname].”
            '
            '“Let’s go, then.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s go, then.”')
                if cephasgaiane_shop_select == "dragonhorn":
                    $ renpy.notify("You traded the spices\nfor the dragon horn.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You traded the spices for the dragon horn.{/i}')
                    $ item_dragonhorn = 1
                    $ cephasgaiane_shop_dragonhorn = 1
                elif cephasgaiane_shop_select == "freegift":
                    $ renpy.notify("You gave away the spices.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away the spices.{/i}')
                $ item_spices = 0
                $ greenmountaintribe_reputation += 2
                jump greenmountaintribechiefaftertrading02
            '“I need to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump greenmountaintribechiefafterinteraction01

    label greenmountaintribechiefssellingasterionscloak:
        $ questionpreset = 0
        menu:
            'Met with disbelief, you describe the cloak’s powers, and {color=#f6d6bd}Gaiane{/color} covers her mouth, looking at {color=#f6d6bd}the chief{/color}. “For t’ elders, and t’ watch, and t’ climbers!” His nod is thoughtful.
            '
            '“Let’s go and see it, then.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s go and see it, then.”')
                if cephasgaiane_shop_select == "dragonhorn":
                    $ renpy.notify("You traded Asterion’s cloak\nfor the dragon horn.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You traded Asterion’s cloak for the dragon horn.{/i}')
                    $ item_dragonhorn = 1
                    $ cephasgaiane_shop_dragonhorn = 1
                elif cephasgaiane_shop_select == "freegift":
                    $ renpy.notify("You gave away Asterion’s cloak.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away Asterion’s cloak.{/i}')
                $ item_asterioncloak = 0
                $ greenmountaintribe_reputation += 2
                jump greenmountaintribechiefaftertrading02
            '“I need to think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about it.”')
                jump greenmountaintribechiefafterinteraction01
