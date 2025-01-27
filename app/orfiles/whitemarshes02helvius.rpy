# Helvius - blond, young, strong, large flail, chews herbs, aggressive, arrogant. builder. animal charms, silver head of a moose on his chest.

default helvius_lastdayofvisit = 0
default helvius_about_nomoreundead = 0
default helvius_about_orentius_spared = 0
default helvius_cruel = 0

default helvius_about_whitemarshes = 0
default helvius_about_independence = 0
default helvius_about_wood = 0

default helvius_about_steephouse = 0
default helvius_about_asterion1 = 0
default helvius_about_asterion2 = 0

default helvius_about_undead1 = 0
default helvius_about_undead2 = 0

default helvius_about_bandits1 = 0
default helvius_about_bandits_reputation = 5
default helvius_about_bandits2 = 0
default helvius_about_bandits3 = 0

default helvius_about_plague1 = 0
default helvius_about_plague2 = 0

default helvius_about_missinghunters = 0

default helvius_about_buying = 0
default helvius_shop_points = 0
default helvius_shop_linen_price_base = 0 # either 8 or 10
default helvius_shop_linen_price = 0
default helvius_shop_ironscraps_price = 0
default helvius_shop_ironingot_price = 0
default helvius_shop_pileofbones_price = 0

default helvius_about_cidercask = 0
default helvius_about_cidercask_thyrsus = 0

default helvius_about_bronzerod = 0
default helvius_about_bronzerod_coins = 0
default helvius_about_bronzerod_price = 0

default helvius_about_oldtunnel1 = 0
default helvius_about_oldtunnel_reputation = 8
default helvius_about_oldtunnel2 = 0
default helvius_about_oldtunnel_price = 0
default helvius_about_oldtunnel_paid = 0
default helvius_about_oldtunnel3 = 0

default helvius_about_orentius1 = 0
default helvius_about_orentius2 = 0
default helvius_orentius_helped = 0
default helvius_orentius_threshold = 12

default helvius_about_thaisattack = 0
default helvius_about_womanwithpurse1 = 0
default helvius_about_womanwithpurse2 = 0
default helvius_about_womanwithpurse3 = 0
default helvius_about_womanwithpurse_denied = 0

label whitemarsheshelviusregularALL:
    label whitemarsheshelviusregular01:
        if helvius_shop_points >= 5:
            $ helvius_shop_points -= 5
            $ whitemarshes_reputation += 1
            jump whitemarsheshelviusregular01
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Helvius{/color}.')
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if whitemarshes_nomoreundead and not helvius_about_nomoreundead:
            $ questionpreset = 0
            $ helvius_lastdayofvisit = day
            $ helvius_about_nomoreundead = 1
            if (whitemarshes_nomoreundead+1) < day:
                $ minutes += 5
                $ custom1 = "You find him after a few minutes. He’s overseeing the pyre, making sure the flames are not buried beneath the dead shells. The smell of rotting and burning flesh makes you hesitant about stepping closer, but after someone else nods in your direction, he spares you a disinterested glance and turns away."
            else:
                $ custom1 = "You find him on the top of the wall, helping a few locals place a new brick. You wonder if the construction will ever be finished - the village is now so quiet and empty that you hardly recognize it anymore.\n\n{color=#f6d6bd}Helvius{/color} looks down at you, then turns away."
            menu:
                '[custom1] “You’ve put a lot f’work on me, warden, on all f’us. Get out of my face with your petty troubles.”
                '
                '“You’re scum, {color=#f6d6bd}Helvius{/color}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re scum, {color=#f6d6bd}Helvius{/color}.”')
                    $ custom1 = "He looks at you, moving his lips as if he’s considering spitting on you, but then shrugs. After a quiet moment and a few angry scowls from the other villagers, you walk away."
                    jump whitemarshesrejectedbyhelvius01
                '“You’re still the mayor of this village. Don’t turn away the only roadwarden you have.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re still the mayor of this village. Don’t turn away the only roadwarden you have.”')
                    $ custom1 = "He lets out a joyless chuckle. “You’re the second one this year, may The Wright keep us safe from them. An’ make your end bloody.”\n\nAfter a quiet moment and a few angry scowls from the other villagers, you walk away."
                    jump whitemarshesrejectedbyhelvius01
                'I spare him no more than a shrug.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I spare him no more than a shrug.')
                    $ custom1 = "Your mount welcomes your quick return with a snort, still bothered by the local flies."
                    jump whitemarshesrejectedbyhelvius01
        else:
            $ helvius_lastdayofvisit = day
            $ shop = "helvius"
            $ questionpreset = "helvius1"
            if orentius_spared and not helvius_about_orentius_spared:
                $ helvius_about_orentius_spared = 1
                menu:
                    'He looks down on you, resting his elbows on the haft of his axe and twisting his lips in a mocking smile. “Here again? Odd for you to have so little shame, after you disturbed {color=#f6d6bd}the prophet’s{/color} peace.”
                    '
                    '(helvius1 set)':
                        pass
            elif helvius_about_oldtunnel_paid and helvius_about_oldtunnel_paid <= day and not helvius_about_oldtunnel3:
                $ oldtunnel_inside_undead_defeated = 1
                $ helvius_about_oldtunnel3 = 1
                menu:
                    'You find him sitting on a bench. He stands up, resting his hands on the blade of his poleaxe. “An’ you’re back. The tunnel is cleared, we left {i}most{/i} things inside,” he grunts with amusement.
                    '
                    '(helvius1 set)':
                        pass
            elif thyrsus_about_cidercask_delivered and thyrsus_about_cidercask_delivered+3 <= day and not helvius_about_cidercask_thyrsus:
                $ helvius_about_cidercask_thyrsus = 1
                $ whitemarshes_reputation += 1
                menu:
                    'He welcomes you with a wide grin. “I saw {color=#f6d6bd}Thyrsus{/color}, the other day. An’ your {i}delivery{/i}.” He nods gratefully.
                    '
                    '(helvius1 set)':
                        pass
            else:
                if helvius_lastdayofvisit != day:
                    if whitemarshes_reputation >= 10:
                        $ helvius_lastdayofvisit = day
                        menu:
                            '“Greetings, [pcname]!” He smiles at you, and leans the poleaxe against the nearby wall.
                            '
                            '(helvius1 set)':
                                pass
                    elif whitemarshes_reputation >= 6:
                        $ custom1 = "“Warden,” he welcomes you with a polite nod and keeps the poleaxe at his side."
                    elif whitemarshes_reputation >= 3:
                        $ custom1 = "“Stranger,” he rests the blunt edge of his poleaxe on the ground in front of him."
                    elif whitemarshes_reputation >= 0:
                        $ custom1 = "He welcomes you with a slight nod, then puts his poleaxe across his shoulders."
                    else:
                        $ custom1 = "He rolls his eyes and purses his lips, then puts his poleaxe across his shoulders."
                else:
                    if whitemarshes_reputation >= 5:
                        $ custom1 = "He meets your eyes, waiting for you to speak."
                    else:
                        $ custom1 = "He hardly spares you a glance."
                $ helvius_lastdayofvisit = day
                menu:
                    '[custom1]
                    '
                    '(helvius1 set)':
                        pass

    label whitemarsheshelviusafterinteraction01:
        if helvius_shop_points >= 5:
            $ helvius_shop_points -= 5
            $ whitemarshes_reputation += 1
            jump whitemarsheshelviusafterinteraction01
        if tutorial_selling == 1:
            $ tutorial_selling = 2
        if tutorial_selling2 == 1:
            $ tutorial_selling2 = 2
        $ questionpreset = "helvius1"
        if whitemarshes_reputation >= 10:
            $ custom1 = "“Need any help?”"
        elif whitemarshes_reputation >= 6:
            $ custom1 = "“What else do you need?”"
        elif whitemarshes_reputation >= 3:
            $ custom1 = "He closes his eyes and sighs, waiting for you to speak."
        else:
            $ custom1 = "He sighs loudly, giving you a telling look."
        menu:
            '[custom1]
            '
            '(helvius1 set)':
                pass

label whitemarsheshelviusaboutwhitemarshes01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to learn more about {color=#f6d6bd}White Marshes{/color}.”')
    $ helvius_about_whitemarshes = 1
    $ description_whitemarshes01 = "A village of foragers and peat gatherers set among the western bogs."
    $ questionpreset = "helvius1"
    menu:
        '“Don’t bother, both us an’ yourself. The tribe’s been taming the bogs for five generations, ba the fields,” he moves toward the gate, as if you had no opportunity to see them before, “are from a few seasons ago, thanks to {color=#f6d6bd}Orentius{/color}. We used to live on berries an’ meat, selling peat an’ timber, ba soon we’ll need no outsiders. After all these years of feeding our blood to saurians, leeches, an’ merchants, betta days are coming. {i}We{/i} made them come, an’ we {i}deserve{/i} them,” he fondly wipes his blade with his thumb, then clears his throat. “If The Wright allows.”
        '
        '(helvius1 set)':
            pass

label whitemarsheshelviusaboutgrowingindependent01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So you want to separate yourself from the other settlements.”')
    $ helvius_about_independence = 1
    $ renpy.notify("Journal updated: Explore the Peninsula")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
    $ quest_explorepeninsula_description17b = "The people of {color=#f6d6bd}White Marshes{/color} feel threatened and may attempt to completely seperate themselves from the rest of the peninsula. If that happens, the city merchants will have fewer reasons to invest in a new route."
    $ description_whitemarshes17 = "The locals feel threatened and may attempt to completely seperate themselves from the rest of the peninsula."
    $ questionpreset = "helvius1"
    menu:
        '“The tribes with little iron an’ bones struggle more an’ more. We’re getting ready to welcome plunderers the way they deserve, t’s all. Our palisade wasn’t nuff, all this,” he waves at the wall, and his voice is full of pride, “was built in not even two years, can you believe?”
        \n\nYou glance at a yellowish skeleton that carries two large rocks, each too large for any human to lift on their own.
        '
        '(helvius1 set)':
            pass

label helvius_about_wood01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You used to sell wood, correct?”')
    $ helvius_about_wood = 1
    $ whitemarshes_reputation += 1
    $ questionpreset = "helvius1"
    menu:
        'He nods in approval. “In the old days. Our firewood warmed up all walls an’ toes on this side {color=#f6d6bd}f’Hag Hills{/color}, ba {color=#f6d6bd}Gale Rocks{/color}, in the far north, built its own hamlet for woodcutters, an’ {color=#f6d6bd}Howler’s Dell{/color} grew a fine garden for themselves, just to get by without us. They have oaks, cherries, an’ their own, darker birches. Have no more reason to trade with us, other than peat.”
        \n\nYou glance at the buildings. While they are indeed new, most settlements in the province would view them as crude and cramped.
        '
        '(helvius1 set)':
            pass

label whitemarsheshelviusaboutsteephouse01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The changes and struggles of recent years... Are they related to what happened to the village in the south?”')
    $ helvius_about_steephouse = 1
    $ questionpreset = "helvius1"
    menu:
        'While he stands still, you feel the inquisitive glances of the nearby villagers. “Whatever you’re trying to ask me about,” he says through his clenched teeth, “should stay in your dirty mouth, outsider.”
        '
        '(helvius1 set)':
            pass

label whitemarsheshelviusaboutplagueALL:
    label whitemarsheshelviusaboutplague01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The people of {color=#f6d6bd}Old Págos{/color} are fighting a plague.”')
        $ oldpagos_plague_warnedplaces += 1
        $ helvius_about_plague1 = 1
        $ whitemarshes_reputation += 1
        $ minutes += 5
        $ questionpreset = "helvius1"
        menu:
            '“Fuck,” he looks at the dark clouds and sighs. “Who? Kids, elders?”
            \n\nWhile you speak, the nearby villagers stop their work, and even the undead are told to freeze in place, offering your ears a bit of relief. You answer a lot of questions, making the muddy square even more grim.
            \n\nYou hear someone weeping, and a young woman announcing “t’s not fair, even for them.” {color=#f6d6bd}The mayor{/color} nods in agreement, keeping the axe on his shoulders. “I’ll tell {color=#f6d6bd}Orentius{/color}. From now on, we’ll gather our wood chips and twigs in a shed,” he raises his voice, looking into his tribe’s eyes. “We may’ve nuff for them before winter.”
            '
            '(helvius1 set)':
                pass

    label whitemarsheshelviusaboutplague02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve helped to purge the plague in {color=#f6d6bd}Old Págos{/color}. Maybe with time things will return to normal.”')
        $ whitemarshes_reputation += 1
        $ helvius_about_plague2 = 1
        $ minutes += 5
        $ questionpreset = "helvius1"
        menu:
            '“You did?” He frowns. “An’ how, I ask? Not even {color=#f6d6bd}Orentius{/color} cad help them.”
            \n\nYou start your long tale, but {color=#f6d6bd}the mayor{/color} stops paying attention after just a few minutes, pressing the cold, blunt side of his axe to his cheek. “So some dangerous, pagan spells. Knowing the curses f’the druids, the village may not last till spring. Or maybe {color=#f6d6bd}Thais{/color} is going to collect the debt, now...”
            \n\nWhen he mentions {i}pagans{/i}, you can’t stop yourself from peeking at the loud, undead shells.
            '
            '(helvius1 set)':
                pass

    label whitemarsheshelviusaboutplague02alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The people of {color=#f6d6bd}Old Págos{/color} were suffering from a plague, but I helped them overcome it.”')
        $ whitemarshes_reputation += 1
        $ oldpagos_plague_warnedplaces += 1
        $ helvius_about_plague1 = 1
        $ helvius_about_plague2 = 1
        $ minutes += 5
        $ questionpreset = "helvius1"
        menu:
            '“You did?” He frowns. “An’ how, I ask? We learned about the illness a few days ago, ba not even {color=#f6d6bd}Orentius{/color} cad help them.”
            \n\nYou start your long tale, but {color=#f6d6bd}the mayor{/color} stops paying attention after just a few minutes, pressing the cold, blunt side of his axe to his cheek. “So some dangerous, pagan spells. Knowing the curses f’the druids, the village may not last till spring. Or maybe {color=#f6d6bd}Thais{/color} is going to collect the debt, now...”
            \n\nWhen he mentions {i}pagans{/i}, you can’t stop yourself from peeking at the loud, undead shells.
            '
            '(helvius1 set)':
                pass

label whitemarsheshelviusaboutasterionALL:
    label whitemarsheshelviusaboutasterion01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is {color=#f6d6bd}Asterion{/color} around?”')
        $ helvius_about_asterion1 = 1
        if (whitemarshes_reputation+appearance_charisma) < 3:
            $ questionpreset = "helvius1"
            menu:
                '“Huh? Why wad he be?” You pay attention to his confident stance and strong voice, with its usual hint of disdain, and spot no sign of a lie. “He’s hardly ever been here. I’ve no need of wardens.”
                '
                '(helvius1 set)':
                    pass
        else:
            $ custom1 = "“Huh? Why wad he be?” You pay attention to his confident stance and strong voice, with its usual hint of disdain, and spot no sign of a lie. “He’s hardly ever been here. I’ve no need of wardens.”\n\nYou meet his eyes. “Maybe you don’t. But could there be someone else?” {color=#f6d6bd}Helvius{/color} begins swinging his axe left and right, the heel of the haft now resting in the mud. Trying to recall the past, he makes a puzzled frown.\n\n“Know what? I was told he met with {color=#f6d6bd}our warlock{/color} often, who knows why. Ask him, if you must.”"
            jump whitemarsheshelviusaboutasterion03
        label whitemarsheshelviusaboutasterion02v01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you {i}sure{/i} you have nothing to tell me about {color=#f6d6bd}Asterion{/color}?”')
            $ custom1 = "{color=#f6d6bd}Helvius{/color} begins swinging his axe left and right, the heel of the haft now resting in the mud. Trying to recall the past, he makes a puzzled frown.\n\n“Know what? I was told he met with {color=#f6d6bd}our warlock{/color} often, who knows why. Ask him, if you must.”"
            jump whitemarsheshelviusaboutasterion03
        label whitemarsheshelviusaboutasterion02v02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You say you know nothing about {color=#f6d6bd}Asterion{/color}, but people claim he had strong ties with your tribe.”')
            $ custom1 = "{color=#f6d6bd}Helvius{/color} begins swinging his axe left and right, the heel of the haft now resting in the mud. Trying to recall the past, he makes a puzzled frown.\n\n“Know what? I was told he met with {color=#f6d6bd}our warlock{/color} often, who knows why. Ask him, if you must.”"
            jump whitemarsheshelviusaboutasterion03

    label whitemarsheshelviusaboutasterion03:
        $ helvius_about_asterion2 = 1
        $ questionpreset = "helvius1"
        if not thyrsus_about_asterion2:
            $ renpy.notify("Journal updated: Find the Roadwarden")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
        $ quest_asterion_description17 = "{color=#f6d6bd}Helvius{/color} from {color=#f6d6bd}White Marshes{/color} told me to speak with {color=#f6d6bd}Thyrsus{/color}, the warlock."
        menu:
            '[custom1]
            '
            '(helvius1 set)':
                pass

label whitemarsheshelviusaboutundeadALL:
    label whitemarsheshelviusaboutundead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the undead workers. “They don’t bother you?”')
        $ helvius_about_undead1 = 1
        $ helvius_cruel += 1
        $ questionpreset = "helvius1"
        menu:
            '“I used to listen to stories about them as’a kid,” he nods for you to follow him. “Ba {color=#f6d6bd}Orentius{/color} taught me they’re no dif’rent than boars an’ fire.” He dashes forward and swings his poleaxe, bashing a skeleton’s shoulder. The arm sinks into the mud, while its owner, a bit awkwardly now, keeps trying to climb up a ladder.
            \n\n{color=#f6d6bd}Helvius{/color} bursts into laughter, and the locals look away without a word. “See,” he continues, leading you back to the well, “all you need’s {i}control{/i}. Look there,” he points at a dead shell with remains of flesh on its chest and head. There’s a white-and-brown sparrow sitting on its shoulder, preening its feathers. “Even beasts know they’ve got not a thing to worry about. The awoken are now like they were yesterday, like they were in spring, like they were a year ago. Leave worrying about them to idiots and Unites.”
            '
            '(helvius1 set)':
                pass

    label whitemarsheshelviusaboutundead02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I hear what you say about the awoken, but your tribe used to be strong without them.”')
        $ helvius_about_undead2 = 1
        if not quest_ruins_10yclue13 and quest_ruins == 1 and quest_ruins_description01:
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        $ quest_ruins_10yclue13 = "The people of {color=#f6d6bd}White Marshes{/color} started to isolate themselves."
        $ questionpreset = "helvius1"
        menu:
            '“So what, warden? What was ten years ago, isn’t, an’ what isn’t, doesn’t matter. We needed to trade, yet the others pushed us away. We won’t let them choose for us ever again.”
            '
            '(helvius1 set)':
                pass

label whitemarsheshelviusaboutbanditsALL:
    label whitemarsheshelviusaboutbandits01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Were you recently bothered by any highwaymen?”')
        $ helvius_about_bandits1 = 1
        if (whitemarshes_reputation+appearance_charisma) < helvius_about_bandits_reputation:
            $ questionpreset = "helvius1"
            menu:
                'He reaches for his hair so quickly that it makes you flinch, but then scratches his head gently. “An’ if so? We’d deal with them on our own, without some warden’s {i}help{/i}.”
                '
                '(helvius1 set)':
                    pass
        else:
            $ custom1 = "He reaches for his hair so quickly that it makes you flinch, but then scratches his head gently. “An’ if so? We’d deal with them on our own, without some warden’s {i}help{/i}.”\n\nYou scowl at him, and after a long pause, he sighs. “{color=#f6d6bd}Glaucia’s{/color} angry with us. Took our food an’ tools, beat our foragers, broke our traps. Ba we don’t need a stranger’s guidance.”"
            jump whitemarsheshelviusaboutbandits03

        label whitemarsheshelviusaboutbandits02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We were talking about the highwaymen...”')
            $ custom1 = "After a long pause, he sighs. “{color=#f6d6bd}Glaucia’s{/color} angry with us. Took our food an’ tools, beat our foragers, broke our traps. Ba we don’t need a stranger’s guidance.”"
            jump whitemarsheshelviusaboutbandits03

        label whitemarsheshelviusaboutbandits02alt:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “According to what an old druid told me, the highwaymen bother you much more severely than you led me to believe.”')
            $ custom1 = "“So you’re bothering other people with these questions as well?” He scowls at you, but carries on. “{color=#f6d6bd}Glaucia’s{/color} angry with us. Took our food an’ tools, beat our foragers, broke our traps. Ba we don’t need a stranger’s guidance.”"
            jump whitemarsheshelviusaboutbandits03

    label whitemarsheshelviusaboutbandits03:
        $ helvius_about_bandits2 = 1
        $ banditshideout_villagesasked_aboutattacks += 1
        $ quest_intelforpeltnorth_description03 = "It looks like the bandits have been especially harsh toward {color=#f6d6bd}White Marshes{/color}."
        if quest_intelforpeltnorth == 1:
            $ renpy.notify("Journal updated: Glaucia’s Band")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Glaucia’s Band{/i}')
        $ questionpreset = "helvius1"
        menu:
            '[custom1]
            '
            '(helvius1 set)':
                pass

    label whitemarsheshelviusaboutbandits04:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It would anger {color=#f6d6bd}Glaucia{/color}, but may help me earn his trust. “I know where the highwaymen’s hideout is.”')
        $ helvius_about_bandits3 = 1
        $ minutes += 5
        $ whitemarshes_reputation += 2
        menu:
            'He runs his eyes over your bundles, as if you’re hiding the band there, then frowns. “Well?”
            \n\nYou describe the old hamlet, and the dangerous path leading to it. For a few breaths, you’re not sure if he’s even listening. Then, he points at your chin with his blade.
            \n\n“Why are you telling me this?”
            '
            '“I want your people to prosper.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want your people to prosper.”')
                $ questionpreset = "helvius1"
                menu:
                    '“We don’t need your help,” he scoffs, and raises his chin. “Ba I’m grateful for it. We’ll see if you’re a liar, an’ soon.”
                    '
                    '(helvius1 set)':
                        pass
            '“She needs to be stopped.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She needs to be stopped.”')
                $ questionpreset = "helvius1"
                $ whitemarshes_reputation += 1
                menu:
                    'He nods in agreement. “She’s a hateful spirit, an’ we’ll take her down, once our walls grow tall enough to guard us.”
                    '
                    '(helvius1 set)':
                        pass
            '“My roads don’t need any robbers. I want them to stay clean.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My roads don’t need any robbers. I want them to stay clean.”')
                $ whitemarshes_reputation -= 1
                $ questionpreset = "helvius1"
                menu:
                    'His huff sounds like a snake’s hiss. “{i}Your{/i} roads, outsider? Maybe one day, after ten years or so of washing them clean with your long tongue.” He raises his chin. “Ba I’m grateful for your help. We’ll see if you’re a liar, an’ soon.”
                    '
                    '(helvius1 set)':
                        pass
            '“I just need to speak with {color=#f6d6bd}Orentius{/color}.”' if helvius_about_orentius1 and not orentius_met:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I just need to speak with {color=#f6d6bd}Orentius{/color}.”')
                $ questionpreset = "helvius1"
                menu:
                    'He nods in silence and, for a moment, you don’t see his usual contempt.
                    '
                    '(helvius1 set)':
                        pass

label whitemarsheshelviusaboutmissinghunters01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I seek a few missing hunters from {color=#f6d6bd}Creeks{/color}. Are they here, maybe?”')
    $ helvius_about_missinghunters = 1
    $ quest_missinghunters_daliaknown = 1
    if item_rawhide:
        $ custom1 = " He then points at the rawhide hanging from your bundles. “T’s hers. She’s not coming back, looks so.”"
        $ northernroad_rawhide_owner = 1
    else:
        $ custom1 = ""
    $ questionpreset = "helvius1"
    menu:
        'His voice remains the same, but he squeezes the long haft of his axe. “{color=#f6d6bd}Dalia{/color}, right? Was here, ba many days ago, with questions on howlers an’ cats. Some dumb bet, she told me. Was heading back north.”[custom1]
        '
        '(helvius1 set)':
            pass

    label whitemarsheshelviusaboutmissinghunters02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You mentioned {color=#f6d6bd}Dalia{/color}. Does this rawhide belong to her?”')
        $ northernroad_rawhide_owner = 1
        $ questionpreset = "helvius1"
        menu:
            'He spits on the ground. “T’s hers. She’s not coming back, looks so.”
            '
            '(helvius1 set)':
                pass

label helvius_about_buyingALL:
    label helvius_about_buying01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shall we trade?”')
        $ helvius_about_buying = 1
        menu:
            '“We need what we have, ba I’ll take a look at what you’re bringing, if you seek bones,” he glances at an undead.
            '
            'I nod toward my bundles. “Go ahead.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod toward my bundles. “Go ahead.”')
                jump helvius_about_buying02after

    label helvius_about_buying02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some wares to sell.”')
        jump helvius_about_buying02after

    label helvius_about_buying02after:
        $ thingstosell = 0
        if item_ironscraps:
            $ thingstosell += 1
        if item_linen:
            $ thingstosell += 1
        if item_ironingot:
            $ thingstosell += 1
        if item_pileofbones:
            $ thingstosell += 1
        if item_beholderroot:
            $ thingstosell += 1
        if item_crossbowquarrels:
            $ thingstosell += 1
        if not tutorial_selling:
            $ tutorial_selling = 1
        if thingstosell:
            if not tutorial_selling2:
                $ tutorial_selling2 = 1
        if thingstosell:
            $ shop = "helvius"
            show screen selling()
            if thingstosell == 1:
                $ custom1 = "He points his blade at the only thing that interests him."
            else:
                $ custom1 = "He names a few of your possessions, telling you to keep them at hand."
            menu:
                '[custom1]
                '
                '“Not this time.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not this time.”')
                    hide screen selling
                    jump whitemarsheshelviusafterinteraction01
        else:
            menu:
                'You pull out some items, but he waves them off with his axe. “We’re not adventuring or traveling. Bring me something we cad use around here.”
                '
                'I pack my things.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
                    hide screen selling
                    jump whitemarsheshelviusafterinteraction01

    label whitemarshessellingironscraps:
        $ helvius_shop_ironscraps_price = (8-appearance_price)
        menu:
            'He scratches his chin with his blade, almost catching it with his beard. “{color=#f6d6bd}[helvius_shop_ironscraps_price]{/color}.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the iron scraps.\n+%s" %helvius_shop_ironscraps_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the iron scraps. +%s {image=cointest}{/i}' %helvius_shop_ironscraps_price)
                $ helvius_shop_points += 3
                $ item_ironscraps -= 1
                $ coins += helvius_shop_ironscraps_price
                jump helvius_about_buying03
            '“That’s all.”':
                hide screen selling
                jump whitemarsheshelviusafterinteraction01

    label whitemarshessellingironingot:
        $ helvius_shop_ironingot_price = (22-appearance_price)
        menu:
            'He can’t hide the glint in his eye. He turns his head away, observing your armor. “{color=#f6d6bd}[helvius_shop_ironingot_price]{/color}.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the iron ingot.\n+%s" %helvius_shop_ironingot_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the iron ingot. +%s {image=cointest}{/i}' %helvius_shop_ironingot_price)
                $ helvius_shop_points += 6
                $ item_ironingot -= 1
                $ item_ironingot_sold_whitemarshes = 1
                $ coins += helvius_shop_ironingot_price
                jump helvius_about_buying03
            '“That’s all.”':
                hide screen selling
                jump whitemarsheshelviusafterinteraction01

    label whitemarshessellingquarrels:
        menu:
            '“I’ll pay you for three. With {color=#f6d6bd}one bone{/color}.”
            '
            '“Deal.”' if item_crossbowquarrels >= 3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold 3 quarrels.\n+1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold 3 quarrels. +1 {image=cointest}{/i}')
                $ helvius_shop_points += 1
                $ item_crossbowquarrels -= 3
                $ coins += 1
                jump helvius_about_buying03
            'I only have [item_crossbowquarrels]. (disabled)' if item_crossbowquarrels < 3:
                pass
            '“That’s all.”':
                hide screen selling
                jump whitemarsheshelviusafterinteraction01

    label whitemarshessellingpileofbones:
        $ helvius_shop_pileofbones_price = (20-appearance_price)
        if pc_religion == "pagan":
            $ custom1 = "\n\nYou look into his eyes, and a chill runs down your spine. Something in you tells you only the darkest spirits would smile at such a deal."
        if pc_religion == "ordersoftruth" or pc_religion == "fellowship":
            $ custom1 = "\n\nYou look into his eyes, and a chill runs down your spine, as if you just broke an hourglass in half."
        if pc_religion == "theunitedchurch":
            $ custom1 = "\n\nYou look into his eyes, and a chill runs down your spine. The Church would throw you out for such dark pursuits."
        else:
            $ custom1 = ""
        menu:
            'Staring into the bag, he’s speechless, but finally nods. “Good nuff. {color=#f6d6bd}[helvius_shop_pileofbones_price]{/color}.”[custom1]
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the pile of bones.\n+%s" %helvius_shop_pileofbones_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the pile of bones. +%s {image=cointest}{/i}' %helvius_shop_pileofbones_price)
                $ helvius_shop_points += 10
                if pc_religion == "pagan":
                    $ pc_faithpoints -= 2
                if pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                    $ pc_faithpoints -= 4
                if pc_religion == "theunitedchurch":
                    $ pc_faithpoints -= 5
                $ item_pileofbones -= 1
                $ coins += helvius_shop_pileofbones_price
                jump helvius_about_buying03
            '“That’s all.”':
                hide screen selling
                jump whitemarsheshelviusafterinteraction01

    label whitemarshessellinglinen:
        if not helvius_shop_linen_price_base:
            menu:
                'He touches it with the palm of his hand, and looks at it suspiciously. “Where’s it from?”
                '
                '“{color=#f6d6bd}Howler’s{/color}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Howler’s{/color}.”')
                    $ helvius_shop_linen_price_base = 8
                    $ custom1 = "He spits on the ground, adding just a bit of water to the mud. “"
                    jump whitemarshessellinglinenpart2
                '(lie) “I brought it here from beyond {color=#f6d6bd}Hag Hills{/color}.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I brought it here from beyond {color=#f6d6bd}Hag Hills{/color}.”')
                    $ pc_lies += 1
                    $ helvius_shop_linen_price_base = 10
                    $ custom1 = "He nods. “T’s good fabric, ba not unique. "
                    jump whitemarshessellinglinenpart2
        else:
            if helvius_shop_linen_price_base == 8:
                $ custom1 = "He sighs. “"
            else:
                 $ custom1 = "He scratches his beard. “"
            jump whitemarshessellinglinenpart2

        label whitemarshessellinglinenpart2:
            $ helvius_shop_linen_price = (helvius_shop_linen_price_base-appearance_price)
            menu:
                '[custom1]{color=#f6d6bd}[helvius_shop_linen_price]{/color}.”
                '
                '“Deal.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                    show screen notifyimage( "You sold the stack of linen.\n+%s" %helvius_shop_linen_price, "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the stack of linen. +%s {image=cointest}{/i}' %helvius_shop_linen_price)
                    $ helvius_shop_points += 3
                    $ item_linen -= 1
                    $ coins += helvius_shop_linen_price
                    jump helvius_about_buying03
                '“That’s all.”':
                    hide screen selling
                    jump whitemarsheshelviusafterinteraction01

    label whitemarshessellingbeholderroot:
        menu:
            'He stays away from what he calls “a wicked spell,” but stares at it with fascination. “Mayhap {color=#f6d6bd}Orentius{/color} will make a charm out of it. {color=#f6d6bd}Three bones{/color}.”
            '
            '“Deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal.”')
                show screen notifyimage( "You sold the weird root.\n+3", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold the weird root. +3 {image=cointest}{/i}')
                $ helvius_shop_points += 2
                $ item_beholderroot -= 1
                $ coins += 3
                jump helvius_about_buying03
            '“That’s all.”':
                hide screen selling
                jump whitemarsheshelviusafterinteraction01

    label helvius_about_buying03:
        $ thingstosell = 0
        if item_ironscraps:
            $ thingstosell += 1
        if item_linen:
            $ thingstosell += 1
        if item_ironingot:
            $ thingstosell += 1
        if item_pileofbones:
            $ thingstosell += 1
        if item_beholderroot:
            $ thingstosell += 1
        if item_crossbowquarrels:
            $ thingstosell += 1
        if thingstosell:
            $ shop = "helvius"
            show screen selling()
            if thingstosell == 1:
                $ custom1 = "He points his blade at one more thing."
            else:
                $ custom1 = "He glances at your other possessions."
            menu:
                '[custom1]
                '
                '“Not this time.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not this time.”')
                    hide screen selling
                    jump whitemarsheshelviusafterinteraction01
        else:
            menu:
                '“An’ t’s that,” he steps away.
                '
                'I pack my things.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
                    hide screen selling
                    jump whitemarsheshelviusafterinteraction01

label whitemarsheshelviusaboutcidercaskALL:
    label whitemarsheshelviusaboutcidercask01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have a delivery from {color=#f6d6bd}Foggy{/color}.” I pat the cask strapped to my bundles.')
        menu:
            'With an open mouth, he steps away, looks around, and frowns at a woman who’s scowling at your gesture. “I don’t need it no more, take it out f’our village,” he raises his voice, but can’t hide his hesitation.
            '
            '“Are you saying this out of your own will, or to follow {color=#f6d6bd}Orentius’{/color} orders?”' if description_whitemarshes09:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you saying this out of your own will, or to follow {color=#f6d6bd}Orentius’{/color} orders?”')
                $ custom1 = "Still holding his poleaxe, he tries to make his shoulders seem wider, though it looks more like an awkward shrug. “I’m proud to follow his {i}advice{/i}. Do as I said.”"
                jump whitemarsheshelviusaboutcidercask02
            '“You’re not getting your dragons back.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re not getting your dragons back.”')
                $ custom1 = "“I wouldn’t ask, the path from {color=#f6d6bd}Foggy’s{/color} is long. Take it back to her, or drink it yourself, for all I care.”"
                jump whitemarsheshelviusaboutcidercask02
            '“Then what should I do with it?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then what should I do with it?”')
                $ custom1 = "“Take it back to {color=#f6d6bd}Foggy{/color}, say {i}hi{/i} to her from our tribe, thank her for keeping her side of the deal. Not my problem.”"
                jump whitemarsheshelviusaboutcidercask02
            'I shrug and cover the cask in a sack.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shrug and cover the cask in a sack.')
                $ custom1 = "There’s sadness in his smile, but also relief."
                jump whitemarsheshelviusaboutcidercask02

    label whitemarsheshelviusaboutcidercask02:
        $ helvius_about_cidercask = 1
        $ renpy.notify("Journal updated: Cask of Cider")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Cask of Cider{/i}')
        $ quest_foggy3whitemarshes_description01 = "For whatever reason, {color=#f6d6bd}mayor Helvius{/color} refuses to accept it. Maybe someone else would do so, or I could just bring it back to {color=#f6d6bd}Foggy{/color}."
        $ questionpreset = "helvius1"
        menu:
            '[custom1]
            '
            '(helvius1 set)':
                pass

    label whitemarsheshelviusaboutcidercask03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I lower my voice. “You may want to speak with {color=#f6d6bd}Thyrsus{/color}. I heard he has some {i}hard apples{/i} for you.”')
        $ helvius_about_cidercask_thyrsus = 1
        $ whitemarshes_reputation += 1
        $ questionpreset = "helvius1"
        menu:
            'He doesn’t get it at first, but after a few moments he looks around with a grin, like a kid who just stole a spoonful of honey.
            '
            '(helvius1 set)':
                pass

label helvius_about_recruitahunter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever met {color=#f6d6bd}Cassia{/color}? She’s a warrior from {color=#f6d6bd}Gale Rocks{/color}.”')
    $ quest_recruitahunter_spokento_helvius = 1
    $ quest_recruitahunter_cassia_points += 1
    if quest_recruitahunter_cassia_points >= quest_recruitahunter_cassia_threshold and not quest_recruitahunter_cassia_points_notify2:
        $ quest_recruitahunter_cassia_points_notify2 = 1
        $ quest_recruitahunter_cassia_points_notify1 = 1
        $ renpy.notify("Journal updated: Recruit a Hunter")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
    elif quest_recruitahunter_cassia_points >= 3 and not quest_recruitahunter_cassia_points_notify1:
        $ quest_recruitahunter_cassia_points_notify1 = 1
        $ renpy.notify("Journal updated: Recruit a Hunter")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
    $ questionpreset = "helvius1"
    menu:
        '“Eh? Who?” You repeat your question, but he shrugs. “I know of many great {i}warriors{/i} from her tribe, they’re a disciplined bunch, ba not a single tale about that woman has reached me.”
        '
        '(helvius1 set)':
            pass

label whitemarsheshelviusaboutbronzerodALL:
    label whitemarsheshelviusaboutbronzerod01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Eudocia{/color}, the enchantress, would like to place this rod in your village, somewhere high. Would that be a problem?”')
        $ helvius_about_bronzerod = 1
        menu:
            '“She what? Let me see,” he swings the hollow piece of bronze like a sword made from a branch, then raises it above his head, staring at it with little patience. “a lightning catcher, or a toy... Well,” he gives it back. “Come one day before noon. You’ll go out with the foragers, as’a guard. Work with them for half a day an’ we’ll put it in a tree. Or on a roof, mayhap.”
            '
            'I sigh. “Very well. I’ll do the work.”' if quarters <= (((world_daylength/2)+11)) and pc_hp >= 2:
                jump whitemarsheshelviusaboutbronzerod03work01
            'I’m too tired to join the foragers. (Required vitality: 2) (disabled)' if pc_hp < 2:
                pass
            'It’s too late to start any work now. (disabled)' if quarters > (((world_daylength/2)+11)):
                pass
            '“...Can’t I just pay you?”' if not helvius_about_bronzerod_coins:
                jump whitemarsheshelviusaboutbronzerod02coins
            'I reach for my pouch.' if helvius_about_bronzerod_coins and coins >= helvius_about_bronzerod_price:
                jump whitemarsheshelviusaboutbronzerod03coins
            'I don’t have enough to pay him. (disabled)' if helvius_about_bronzerod_coins and coins < helvius_about_bronzerod_price:
                pass
            '“Maybe another time.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe another time.”')
                jump whitemarsheshelviusafterinteraction01

    label whitemarsheshelviusaboutbronzerod02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About {color=#f6d6bd}Eudocia’s{/color} rod...”')
        if not helvius_about_bronzerod_price:
            menu:
                'He smirks. “Ready to get your hands dirty?”
                '
                'I sigh. “Very well. I’ll do the work.”' if quarters <= (((world_daylength/2)+11)) and pc_hp >= 2:
                    jump whitemarsheshelviusaboutbronzerod03work01
                'I’m too tired to join the foragers. (Required vitality: 2) (disabled)' if pc_hp < 2:
                    pass
                'It’s too late to start any work now. (disabled)' if quarters > (((world_daylength/2)+11)):
                    pass
                '“...Can’t I just pay you?”' if not helvius_about_bronzerod_coins:
                    jump whitemarsheshelviusaboutbronzerod02coins
                'I reach for my pouch.' if helvius_about_bronzerod_coins and coins >= helvius_about_bronzerod_price:
                    jump whitemarsheshelviusaboutbronzerod03coins
                'I don’t have enough to pay him. (disabled)' if helvius_about_bronzerod_coins and coins < helvius_about_bronzerod_price:
                    pass
                '“Maybe another time.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe another time.”')
                    jump whitemarsheshelviusafterinteraction01
        else:
            $ helvius_about_bronzerod_price = (5-appearance_price)
            menu:
                'He holds his laughter. “So, how will it be? Dirty hands, or {color=#f6d6bd}[helvius_about_bronzerod_price]{/color} clean bones?”
                '
                'I sigh. “Very well. I’ll do the work.”' if quarters <= (((world_daylength/2)+11)) and pc_hp >= 2:
                    jump whitemarsheshelviusaboutbronzerod03work01
                'I’m too tired to join the foragers. (Required vitality: 2) (disabled)' if pc_hp < 2:
                    pass
                'It’s too late to start any work now. (disabled)' if quarters > (((world_daylength/2)+11)):
                    pass
                '“...Can’t I just pay you?”' if not helvius_about_bronzerod_coins:
                    jump whitemarsheshelviusaboutbronzerod02coins
                'I reach for my pouch.' if helvius_about_bronzerod_coins and coins >= helvius_about_bronzerod_price:
                    jump whitemarsheshelviusaboutbronzerod03coins
                'I don’t have enough to pay him. (disabled)' if helvius_about_bronzerod_coins and coins < helvius_about_bronzerod_price:
                    pass
                '“Maybe another time.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe another time.”')
                    jump whitemarsheshelviusafterinteraction01

    label whitemarsheshelviusaboutbronzerod02coins:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Can’t I just pay you?”')
        $ helvius_about_bronzerod_price = (5-appearance_price)
        $ helvius_about_bronzerod_coins = 1
        menu:
            'His cackle is like a troll’s grunt. “You value your hours so much? In that case, {color=#f6d6bd}[helvius_about_bronzerod_price]{/color} bones an’ t’s done.”
            '
            'I sigh. “Very well. I’ll do the work.”' if quarters <= (((world_daylength/2)+11)) and pc_hp >= 2:
                jump whitemarsheshelviusaboutbronzerod03work01
            'I’m too tired to join the foragers. (Required vitality: 2) (disabled)' if pc_hp < 2:
                pass
            'It’s too late to start any work now. (disabled)' if quarters > (((world_daylength/2)+11)):
                pass
            '“...Can’t I just pay you?”' if not helvius_about_bronzerod_coins:
                jump whitemarsheshelviusaboutbronzerod02coins
            'I reach for my pouch.' if helvius_about_bronzerod_coins and coins >= helvius_about_bronzerod_price:
                jump whitemarsheshelviusaboutbronzerod03coins
            'I don’t have enough to pay him. (disabled)' if helvius_about_bronzerod_coins and coins < helvius_about_bronzerod_price:
                pass
            '“Maybe another time.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe another time.”')
                jump whitemarsheshelviusafterinteraction01

    label whitemarsheshelviusaboutbronzerod03work01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh. “Very well. I’ll do the work.”')
        show areapicture whitemarshesforaging01 at basicfade
        $ quarters += 16
        $ whitemarshes_reputation += 1
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ cleanliness = limit_cleanliness(cleanliness-3)
        show minus3appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
        $ pc_food = limit_pc_food(pc_food-1)
        show minus1food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
        menu:
            'After half an hour or so, the expedition is ready - six souls, none of them older than forty, and with no undead to assist them. “Too dumb,” the oldest woman explains, “an’ we’ve no overseer with us.” Their accents are heavy, but they rarely address you - for most of the time, they exchange single-word commands, gesturing for you to quiet down whenever you step on a branch.
            \n\nYou spend half a day following the bog paths, but also going deeper into the wilderness. As a group, you manage to scare away the smaller beasts, and your guide claims to lead you around the hunting territories of the larger predators. From time to time, you keep to what looks to you like the most inconvenient trails in sight, yet no one objects. You cross the muds, shallow waters, and ancient, dark game trails, tracking any movement among leaves and grasses.
            \n\nHungry and annoyed by the insects, you go back to {color=#f6d6bd}White Marshes{/color}, carrying baskets and sacks full of mushrooms, berries, herbs, and great leaves - but also a few birds and furry critters.
            '
            'As we head to the village, I follow the guide patiently.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- As we head to the village, I follow the guide patiently.')
                jump whitemarsheshelviusaboutbronzerod03work02
            'I hardly pay any attention to the group. I just look for monsters, that’s all.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I hardly pay any attention to the group. I just look for monsters, that’s all.')
                jump whitemarsheshelviusaboutbronzerod03work02

    label whitemarsheshelviusaboutbronzerod03work02:
        show areapicture whitemarshes01 at basicfade
        menu:
            '{color=#f6d6bd}Helvius{/color} waits for you at the gate, nodding with approval. Two steps away from him, you see a short corpse, bare-boned above its waist, but still wearing pants and carrying scraps of meat on its feet.
            \n\nNot giving you a moment for a breath, {color=#f6d6bd}the mayor{/color} tells you to fetch him a rod. After you do so, he throws it at the undead - bouncing the rod off its head with a thud - and starts to laugh. “Go on, now,” he commands it. “Put it on the tree there, and tie it with a rope.”
            \n\nHis worker bows down to pick up the tools and obediently walks away.
            '
            'I say nothing, and splash my face with water at the well.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I say nothing, and splash my face with water at the well.')
                $ helvius_cruel += 1
                $ custom1 = "It gives you little relief - you’d need bucketfuls of water to wash the bogs off you. The man leaves you behind, amused with the way the undead tries to approach the new challenge. A few times, you hear the dead shell falling from a branch, and the man’s sonorous laughter."
                $ renpy.notify("Journal updated: Bronze Rods")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                $ item_bronzerod -= 1
                $ eudocia_bronzerod_rodin_whitemarshes = 1
                $ eudocia_bronzerod_installed += 1
                if not item_bronzerod:
                    $ renpy.notify("Journal updated: Bronze Rods")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                    if eudocia_bronzerod_installed < 4:
                        $ quest_bronzerod_description07 = "I’ve placed fewer than four rods, but I don’t have any of them left. I should inform {color=#f6d6bd}Eudocia{/color}."
                    elif eudocia_bronzerod_installed < eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                        $ quest_bronzerod_description04 = "I’ve placed some of the rods, but don’t have any of them left. I should collect my reward."
                    elif eudocia_bronzerod_installed >= eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                        $ quest_bronzerod_description05 = "I’ve placed all of the rods. I should collect my reward."
                    else:
                        $ quest_bronzerod_description03 = "I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
                else:
                    if eudocia_bronzerod_installed >= 4:
                        if not quest_bronzerod_description04:
                            $ renpy.notify("Journal updated: Bronze Rods")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                            $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                            $ quest_bronzerod_description02 = 0
                jump whitemarshesrejectedbyhelvius01
            '{image=d6} I grab his shoulder. “We had a deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab his shoulder. “We had a deal.”')
                $ whitemarshes_reputation += 1
                $ helvius_cruel += 1
                if pc_hp <= 2: # fail
                    $ custom1 = "He raises his chin and wrenches himself away easily, yet, at least for a moment, looks at you with a frown, surprised with your resolve. “We’ve no trees inside,” he hisses. “T’s as good’s you can get.”\n\nHe then leaves you behind, amused with the way the undead tries to approach the new challenge. A few times, you hear the dead shell falling from a branch, and the man’s sonorous laughter."
                    $ renpy.notify("Journal updated: Bronze Rods")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                    $ item_bronzerod -= 1
                    $ eudocia_bronzerod_rodin_whitemarshes = 1
                    $ eudocia_bronzerod_installed += 1
                    if not item_bronzerod:
                        $ renpy.notify("Journal updated: Bronze Rods")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                        if eudocia_bronzerod_installed < 4:
                            $ quest_bronzerod_description07 = "I’ve placed fewer than four rods, but I don’t have any of them left. I should inform {color=#f6d6bd}Eudocia{/color}."
                        elif eudocia_bronzerod_installed < eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                            $ quest_bronzerod_description04 = "I’ve placed some of the rods, but don’t have any of them left. I should collect my reward."
                        elif eudocia_bronzerod_installed >= eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                            $ quest_bronzerod_description05 = "I’ve placed all of the rods. I should collect my reward."
                        else:
                            $ quest_bronzerod_description03 = "I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
                    else:
                        if eudocia_bronzerod_installed >= 4:
                            if not quest_bronzerod_description04:
                                $ renpy.notify("Journal updated: Bronze Rods")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                                $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                                $ quest_bronzerod_description02 = 0
                    jump whitemarshesrejectedbyhelvius01
                else: # success
                    $ custom1 = "He gives you a puzzled look and tries to wrench himself away, but your strong grasp doesn’t make it easy. “There are no trees inside, you dumb toad,” he stops suddenly, and, after a long pause, calls for the undead to come back. “I’ll find a tall building.” You let him go and walk back to your bundles, where you quench your thirst."
                    $ renpy.notify("Journal updated: Bronze Rods")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                    $ item_bronzerod -= 1
                    $ eudocia_bronzerod_rodin_whitemarshes = 1
                    $ eudocia_bronzerod_installed += 1
                    if not item_bronzerod:
                        $ renpy.notify("Journal updated: Bronze Rods")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                        if eudocia_bronzerod_installed < 4:
                            $ quest_bronzerod_description07 = "I’ve placed fewer than four rods, but I don’t have any of them left. I should inform {color=#f6d6bd}Eudocia{/color}."
                        elif eudocia_bronzerod_installed < eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                            $ quest_bronzerod_description04 = "I’ve placed some of the rods, but don’t have any of them left. I should collect my reward."
                        elif eudocia_bronzerod_installed >= eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                            $ quest_bronzerod_description05 = "I’ve placed all of the rods. I should collect my reward."
                        else:
                            $ quest_bronzerod_description03 = "I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
                    else:
                        if eudocia_bronzerod_installed >= 4:
                            if not quest_bronzerod_description04:
                                $ renpy.notify("Journal updated: Bronze Rods")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                                $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                                $ quest_bronzerod_description02 = 0
                    jump whitemarshesrejectedbyhelvius01

    label whitemarsheshelviusaboutbronzerod03coins:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I reach for my pouch.')
        show screen notifyimage( "-%s" %helvius_about_bronzerod_price, "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s {image=cointest}{/i}' %helvius_about_bronzerod_price)
        $ helvius_shop_points += 1
        $ coins -= helvius_about_bronzerod_price
        menu:
            'He puts the dragon bones into his own pouch, tells you to give him the rod, and calls for one of the undead workers to come closer. It’s short, bare-boned above its waist, but still wears pants and carries scraps of meat on its feet.
            \n\n{color=#f6d6bd}The mayor{/color} throws the piece of bronze at the undead - bouncing the rod off its head with a thud - and starts to laugh. “Go on, now,” he commands it. “Put it on the tree there, and tie it with a rope.”
            \n\nHe points his finger at a pear tree next to one of the fields, far beyond the village walls. His worker bows down to pick up the tools and obediently walks away.
            '
            'I say nothing.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I say nothing, and splash my face with water at the well.')
                $ quarters += 1
                $ helvius_cruel += 1
                $ custom1 = "The man leaves you behind, amused with the way the undead tries to approach the new challenge. A few times, you hear the dead shell falling from a branch, and the man’s sonorous laughter."
                $ renpy.notify("Journal updated: Bronze Rods")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                $ item_bronzerod -= 1
                $ eudocia_bronzerod_rodin_whitemarshes = 1
                $ eudocia_bronzerod_installed += 1
                if not item_bronzerod:
                    $ renpy.notify("Journal updated: Bronze Rods")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                    if eudocia_bronzerod_installed < 4:
                        $ quest_bronzerod_description07 = "I’ve placed fewer than four rods, but I don’t have any of them left. I should inform {color=#f6d6bd}Eudocia{/color}."
                    elif eudocia_bronzerod_installed < eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                        $ quest_bronzerod_description04 = "I’ve placed some of the rods, but don’t have any of them left. I should collect my reward."
                    elif eudocia_bronzerod_installed >= eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                        $ quest_bronzerod_description05 = "I’ve placed all of the rods. I should collect my reward."
                    else:
                        $ quest_bronzerod_description03 = "I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
                else:
                    if eudocia_bronzerod_installed >= 4:
                        if not quest_bronzerod_description04:
                            $ renpy.notify("Journal updated: Bronze Rods")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                            $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                            $ quest_bronzerod_description02 = 0
                jump whitemarshesrejectedbyhelvius01
            '{image=d6} I grab his shoulder. “We had a deal.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} I grab his shoulder. “We had a deal.”')
                $ quarters += 1
                $ whitemarshes_reputation += 1
                if pc_hp <= 2: # fail
                    $ helvius_cruel += 1
                    $ custom1 = "He raises his chin and wrenches himself away easily, yet, at least for a moment, looks at you with a frown, surprised with your resolve. “We’ve no trees inside,” he hisses. “T’s as good’s you can get.”\n\nHe then leaves you behind, amused with the way the undead tries to approach the new challenge. A few times, you hear the dead shell falling from a branch, and the man’s sonorous laughter."
                    $ renpy.notify("Journal updated: Bronze Rods")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                    $ item_bronzerod -= 1
                    $ eudocia_bronzerod_rodin_whitemarshes = 1
                    $ eudocia_bronzerod_installed += 1
                    if not item_bronzerod:
                        $ renpy.notify("Journal updated: Bronze Rods")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                        if eudocia_bronzerod_installed < 4:
                            $ quest_bronzerod_description07 = "I’ve placed fewer than four rods, but I don’t have any of them left. I should inform {color=#f6d6bd}Eudocia{/color}."
                        elif eudocia_bronzerod_installed < eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                            $ quest_bronzerod_description04 = "I’ve placed some of the rods, but don’t have any of them left. I should collect my reward."
                        elif eudocia_bronzerod_installed >= eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                            $ quest_bronzerod_description05 = "I’ve placed all of the rods. I should collect my reward."
                        else:
                            $ quest_bronzerod_description03 = "I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
                    else:
                        if eudocia_bronzerod_installed >= 4:
                            if not quest_bronzerod_description04:
                                $ renpy.notify("Journal updated: Bronze Rods")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                                $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                                $ quest_bronzerod_description02 = 0
                    jump whitemarshesrejectedbyhelvius01
                else: # success
                    $ custom1 = "He gives you a puzzled look and tries to wrench himself away, but your strong grasp doesn’t make it easy. “There are no trees inside, you dumb toad,” he stops suddenly, and, after a long pause, calls for the undead to come back. “I’ll find a tall building.” You let him go and walk back to your bundles."
                    $ renpy.notify("Journal updated: Bronze Rods")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                    $ item_bronzerod -= 1
                    $ eudocia_bronzerod_rodin_whitemarshes = 1
                    $ eudocia_bronzerod_installed += 1
                    if not item_bronzerod:
                        $ renpy.notify("Journal updated: Bronze Rods")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                        if eudocia_bronzerod_installed < 4:
                            $ quest_bronzerod_description07 = "I’ve placed fewer than four rods, but I don’t have any of them left. I should inform {color=#f6d6bd}Eudocia{/color}."
                        elif eudocia_bronzerod_installed < eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                            $ quest_bronzerod_description04 = "I’ve placed some of the rods, but don’t have any of them left. I should collect my reward."
                        elif eudocia_bronzerod_installed >= eudocia_bronzerod_max and eudocia_bronzerod_rodin_whitemarshes:
                            $ quest_bronzerod_description05 = "I’ve placed all of the rods. I should collect my reward."
                        else:
                            $ quest_bronzerod_description03 = "I’ve placed the rods, but not in {color=#f6d6bd}White Marshes{/color}. Let’s hope {color=#f6d6bd}Eudocia{/color} is going to pay anyway."
                    else:
                        if eudocia_bronzerod_installed >= 4:
                            if not quest_bronzerod_description04:
                                $ renpy.notify("Journal updated: Bronze Rods")
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
                                $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                                $ quest_bronzerod_description02 = 0
                    jump whitemarshesrejectedbyhelvius01

label whitemarsheshelviusaboutoldtunnelALL:
    label whitemarsheshelviusaboutoldtunnel01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could use your tribe’s assistance.” I tell him about the undead roaming in the old tunnel in the north.')
        $ helvius_about_oldtunnel1 = 1
        menu:
            'He scratches the back of his head. “Who do you think we are? We don’t carry traditions of dark spellcasters, we do what we must to survive, an’ on our own. What are you asking me about?”
            '
            '“I was hoping you could get rid of them.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was hoping you could get rid of them.”')
                $ custom1 = "“Even {i}if{/i}, t’s a long an’ risky journey for us. I can’t make any promises.”"
                jump whitemarsheshelviusaboutoldtunnel01a
            '“I expect you can always use more shells around here.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I expect you can always use more shells around here.”')
                $ custom1 = "He bursts into laughter, luring the eyes of the other villagers. “Very true! Ba you speak f’hard magic, I can’t promise anyone here knows it, other than {color=#f6d6bd}Orentius{/color}.”"
                $ helvius_about_oldtunnel_reputation -= 2
                if pc_religion == "ordersoftruth" or pc_religion == "fellowship":
                    $ pc_faithpoints -= 1
                if pc_religion == "theunitedchurch":
                    $ pc_faithpoints -= 2
                jump whitemarsheshelviusaboutoldtunnel01a

    label whitemarsheshelviusaboutoldtunnel01a:
        $ minutes += 78
        if (whitemarshes_reputation+appearance_charisma) < helvius_about_oldtunnel_reputation:
            $ questionpreset = "helvius1"
            menu:
                '[custom1]
                '
                '(helvius1 set)':
                    pass
        else:
            $ custom2 = "\n\nYou look him in the eyes and mention the things you’ve already done for the village. With a grunt, he grabs his axe with both hands, pretending to make a swipe. “So you want me to return the favor? Not for free, stranger. Your {i}kindness{/i} wasn’t asked for, I owe you not a thing. I’ll think about the price in bones. Speak with me once you have some savings.”"
            jump whitemarsheshelviusaboutoldtunnel03

    label whitemarsheshelviusaboutoldtunnel02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know me well enough to realize I’m not trying to lure you into a trap. Help me with the old tunnel.”')
        $ custom1 = "With a grunt, he grabs his axe with both hands, pretending to make a swipe. “So you want me to return the favor? Not for free, stranger. Your {i}kindness{/i} wasn’t asked for, I owe you not a thing. I’ll think about the price in bones. Speak with me once you have some savings.”"
        $ custom2 = ""
        jump whitemarsheshelviusaboutoldtunnel03

    label whitemarsheshelviusaboutoldtunnel02alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Be serious. I sold you a pile of bones. It should be enough to prove my intentions are clear.”')
        $ custom1 = "With a grunt, he grabs his axe with both hands, pretending to make a swipe. “So you want me to return the favor? Not for free, stranger. Your {i}kindness{/i} wasn’t asked for, I owe you not a thing. I’ll think about the price in bones. Speak with me once you have some savings.”"
        $ custom2 = ""
        jump whitemarsheshelviusaboutoldtunnel03

    label whitemarsheshelviusaboutoldtunnel03:
        $ helvius_about_oldtunnel2 = 1
        $ questionpreset = "helvius1"
        menu:
            '[custom1][custom2]
            '
            '(helvius1 set)':
                pass

    label whitemarsheshelviusaboutoldtunnel04:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk the price for clearing the tunnel.”')
        $ helvius_about_oldtunnel_price = (15-(appearance_price*2))
        menu:
            '“Fine,” he sizes you up and raises his chin. “I want [helvius_about_oldtunnel_price] bones, not one less.”
            '
            '“Deal. Take this pouch.”' if coins >= helvius_about_oldtunnel_price:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Deal. Take this pouch.”')
                $ coins -= helvius_about_oldtunnel_price
                $ whitemarshes_reputation += 1
                show screen notifyimage( "-%s" %helvius_about_oldtunnel_price, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s {image=cointest}{/i}' %helvius_about_oldtunnel_price)
                if quarters <= world_daylength-40:
                    $ helvius_about_oldtunnel_paid = day
                    $ custom1 = "He tosses it to one of the guards and raises his voice. “Call the scouts! We’re leaving soon.” He nods toward you. “Stay away from that place for the rest f’the day. You’re not as useless’ I thought, let’s not pierce your head with an unlucky arrow.”\n\nWithout another word, he leaves you by the well and walks through the gate."
                    jump whitemarshesrejectedbyhelvius01
                else:
                    $ helvius_about_oldtunnel_paid = day+1
                    $ questionpreset = "helvius1"
                    menu:
                        'He tosses it to one of the guards and raises his voice. “Call the scouts! We’re leaving tomorrow morning.” He nods toward you. “Tomorrow, stay away from that place. You’re not as useless’ I thought, let’s not pierce your head with an unlucky arrow.”
                        '
                        '(helvius1 set)':
                            pass
            'I can’t afford it. (disabled)' if coins < helvius_about_oldtunnel_price:
                pass
            '“Let me think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me think about it.”')
                jump whitemarsheshelviusafterinteraction01

label whitemarsheshelviusaboutthaisconspiracy01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will sabotage {color=#f6d6bd}Thais’{/color} plans, but may help me earn his trust. “You need to strengthen your guards...”')
    $ helvius_about_thaisattack = 1
    $ whitemarshes_reputation += 4
    $ minutes += 5
    menu:
        'You tell him everything you’ve learned from her, though he has little patience and keeps glancing toward {color=#f6d6bd}Orentius’{/color} hut - between his questions, his leg flinches a bit, as if he’s stopping himself from running away.
        \n\n“I don’t know what she did to you that you now go against her,” he breathes heavily, cracking his knuckles and raising his poleaxe, “but we’ll be ready for her. We avoid giving weapons to our {i}workers{/i}, ba t’s time for some changes.”
        \n\nHe tells everyone in sight to prepare for a gathering and selects a few people to spread the news. You, on the other hand, think about {color=#f6d6bd}Thais{/color}. Mentioning what you did may not be the safest idea.
        '
        'I should confess to her.' if not thais_bigmad and not thais_quest_all_cancelled:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should confess to her.')
            $ thais_quest_orentius_betrayal_willadmit = 1
            $ quest_orentius_thais_description03 = 0
            $ quest_orentius_thais_description00betrayal = "I warned the village about {color=#f6d6bd}Thais’{/color} plans. She won’t be able to get in by surprise."
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
            jump whitemarsheshelviusafterinteraction01
        'I’ll keep her in the dark.' if not thais_bigmad and not thais_quest_all_cancelled:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll keep her in the dark.')
            $ quest_orentius_thais_description00betrayal = "I warned the village about {color=#f6d6bd}Thais’{/color} plans. She won’t be able to get in by surprise."
            $ quest_orentius_thais_description03 = 0
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
            jump whitemarsheshelviusafterinteraction01
        'That bridge is already burnt. I don’t need to mention it to her.' if thais_bigmad or thais_quest_all_cancelled:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll keep her in the dark.')
            $ quest_orentius_thais_description00betrayal = "I warned the village about {color=#f6d6bd}Thais’{/color} plans. She won’t be able to get in by surprise."
            $ quest_orentius_thais_description03 = 0
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
            jump whitemarsheshelviusafterinteraction01

label whitemarsheshelviusaboutwomanwithpurseALL:
    label whitemarsheshelviusaboutwomanwithpurse01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I could tell him about the woman that asked me to find her savings...')
        menu:
            'You meet his gaze, both harsh and condescending. You’ve no doubt he won’t take any accusations lightly.
            '
            '“A woman from your village asked me to bring her some lost savings from the east. I thought you should know about this.”' if whitemarshes_pursewoman_coins == 0 or whitemarshes_pursewoman_coins == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A woman from your village asked me to bring her some lost savings from the east. I thought you should know about this.”')
                $ helvius_about_womanwithpurse1 = 1
                $ whitemarshes_reputation += 1
                if quest_hiddenpurse == 1:
                    $ renpy.notify("Quest completed: A Hidden Pouch")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: A Hidden Pouch{/i}')
                $ quest_hiddenpurse = 4
                $ quest_hiddenpurse_description04 = "I told {color=#f6d6bd}Helvius{/color} about her request. She’ll now face consequences."
                $ minutes += 5
                $ questionpreset = "helvius1"
                menu:
                    'He takes a long pause, then tilts his axe. “Tell me what she looks like.”
                    \n\nAfter a brief exchange, he gestures for one of the guards to approach him, and whispers something into his ear. “I’ll speak with her,” he tells you, “ba you’re doing the right thing. She’s in the tribe’s debt, an’ doesn’t deserve the right to leave before she does her part.”
                    '
                    '(helvius1 set)':
                        pass
            '“One of your people wants to leave the village. She asked me to fetch her savings from the east. If you search her possessions, you’ll find the ten dragon bones I gave her.”' if whitemarshes_pursewoman_coins == 10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “One of your people wants to leave the village. She asked me to fetch her savings from the east. If you search her possessions, you’ll find the ten dragon bones I gave her.”')
                $ helvius_about_womanwithpurse3 = 1
                $ whitemarshes_reputation += 2
                $ quest_hiddenpurse = 4
                $ quest_hiddenpurse_description04 = "I told {color=#f6d6bd}Helvius{/color} about her request. She’ll now face consequences."
                $ minutes += 5
                $ questionpreset = "helvius1"
                menu:
                    'He takes a long pause, then tilts his axe. “Tell me what she looks like.”
                    \n\nAfter a brief exchange, he gestures for one of the guards to approach him, and whispers something into his ear. “I’ll speak with her first,” he tells you, “ba you’re doing the right thing. She’s in the tribe’s debt, an’ doesn’t deserve the right to leave before she does her part.”
                    '
                    '(helvius1 set)':
                        pass
            'I don’t want her to suffer any consequences. I try to forget the whole thing.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t want her to suffer any consequences. I try to forget the whole thing.')
                $ helvius_about_womanwithpurse_denied = 1
                if whitemarshes_pursewoman_coins == 10 and pc_goal == "iwanttohelp":
                    $ pc_goal_iwanttohelppoints += 1
                jump whitemarsheshelviusafterinteraction01
            'Maybe if I fulfill her request, I’ll be able to tell him more. (disabled)' if whitemarshes_pursewoman_coins == 0 and quest_hiddenpurse == 1:
                pass
            'I need to think about it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I need to think about it.')
                jump whitemarsheshelviusafterinteraction01

label whitemarsheshelviusaboutorentiusALL:
    label helvius_about_orentius101:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like to speak with {color=#f6d6bd}Orentius{/color}.”')
        $ helvius_about_orentius1 = 1
        menu:
            'As he straightens up, the moose head on his chest bounces enthusiastically. “You an’ many others, ba he’s swamped by his work, an’ we’ve nuff threats in the shadows already. If he decides you’re trustworthy, he {i}may{/i} speak with you {i}once{/i}, ba why would I even ask him?”
            '
            '“I need his guidance.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need his guidance.”')
                $ whitemarshes_reputation += 0
                $ custom1 = "“Then seek fortune tellers an’ scholars,” he scoffs. “We’ve our own struggles to solve before we start leading outsiders.”"
                jump helvius_about_orentius102
            '“I want to hear Wright’s will.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to hear Wright’s will.”')
                $ whitemarshes_reputation += 1
                $ custom1 = "“You’re at the right place, but at the wrong time. One day, all provinces f’The Land will learn what was revealed to {color=#f6d6bd}the prophet{/color},” he spreads his arms, holding the poleaxe like a staff. “Ride away, to the villages, to the city. You will all hear Wright’s words soon enough.”"
                jump helvius_about_orentius102
            '“I must convince him that these undead ought to burn on a pyre.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I must convince him that these undead ought to burn on a pyre.”')
                $ whitemarshes_reputation -= 1
                $ custom1 = "“An’ who made {i}you{/i} a judge f’this? Some old leeches, straight from the city’s down mattresses?” He puts his axe on his shoulders. “We need no outsiders to teach {i}us{/i}.”"
                jump helvius_about_orentius102
            '“I just want to meet him. He sounds like an unusual soul.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I just want to meet him. He sounds like an unusual soul.”')
                $ whitemarshes_reputation -= 1
                $ custom1 = "“We aren’t here to amuse your {i}nosiness{/i},” he raises his chin. “Ride to that {i}city{/i} f’yours and ask sailors to tell you stories,” his voice is dripping with disdain."
                jump helvius_about_orentius102

    label helvius_about_orentius102:
        if not quest_orentius:
            $ quest_orentius = 1
            $ renpy.notify("New entry: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Orentius, the Necromancer{/i}')
        else:
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
        $ quest_orentius_helvius_description01 = "{color=#f6d6bd}Helvius{/color} will agree to introduce me to {color=#f6d6bd}Orentius{/color} if he decides I have proven myself to be a trustworthy ally of his tribe."
        $ quest_orentius_thais_description02 = "I spoke with {color=#f6d6bd}Helvius{/color} about meeting with {color=#f6d6bd}Orentius{/color}. I should report back to Thais."
        $ questionpreset = "helvius1"
        menu:
            '[custom1]
            '
            '(helvius1 set)':
                pass

    label whitemarsheshelviusaboutaboutorentius201:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you really think I’m not trustworthy enough to speak with {color=#f6d6bd}Orentius{/color}?”')
        $ quest_orentius_helvius_description02 = "Once I’m ready, I should tell {color=#f6d6bd}Helvius{/color} to introduce me to {color=#f6d6bd}Orentius{/color}. It’s going to be my only opportunity to speak with him, so I should be sure I know what I’m doing."
        $ helvius_about_orentius2 = 1
        $ renpy.notify("Journal updated: Orentius, the Necromancer")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
        $ questionpreset = "helvius1"
        menu:
            '“F’course,” he grunts without thinking twice. “Ba I passed to him all the news you brought us, an’ he grew curious about you. Ask me one evening, you’ll have your chance. Ba {i}the only{/i} chance, you hear me? You carry a strange air with you, outsider, we’ll keep our eyes open.”
            '
            '(helvius1 set)':
                pass

    label helvius_about_orentius202:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to meet with him now.”')
        show areapicture whitemarshes01night at basicfade
        $ helvius_orentius_helped = 1
        $ orentius_dagger = 0
        menu:
            'In silence, he tells you to take off your cloak, and gestures for the guards to approach you. The light of a torch makes you squint your eyes. “We’re going to {color=#f6d6bd}Orentius{/color},” he explains, and they ask no questions - they grasp your hands, take away your axe, and start to squeeze you around the belt, armpits, even the groin. A young woman reaches for your boots and lets out a triumphant grunt upon finding your dagger, then tosses it in with your other blades.
            \n\n“Ready,” she announces and shoves your things into a sack, which she then puts onto your saddle. {color=#f6d6bd}Helvius{/color} looks into your eyes, holding the silver moose head with his fingers, as if to add import to his words. “Don’t be a monkey in there,” he growls. “We’ll wait just outside the door.”
            '
            'I let them lead me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let them lead me.')
                $ minutes += 5
                jump whitemarshesorentius01
