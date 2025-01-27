###################### Beholder
default beholder_firsttime = 0
default beholder_fluff_tree = ""
default beholder_fluff = ""
default beholder_fluff_old = ""
default beholder_name_known = 0

default beholder_altar_seen = 0
default beholder_altar_amulet = 0
default beholder_altar_awakened = 0
default beholder_altar_awakened_threshold = 24
default beholder_altar_blocked = 0
default beholder_altar_feeding_firstday = 0 #day
default beholder_altar_feeding_lastday = 0 #day

default beholder_water_seen = 0
default beholder_cutroot = 0
default beholder_cutroot_blocked = 0

default beholder_fruit = 0 # 0 - 1 - 2
default beholder_fruit_truth = 0
default beholder_fruit_interaction = 0

default beholder_caneat_blood = 0
default beholder_caneat_magic = 0
default beholder_caneat_items = 0
default beholder_caneat_bronzerod = 0

default beholder_branch = 0
default beholder_oceannecklace = 0
default beholder_destroyed = 0
default beholder_pileofbones = 0
default beholder_arrow = 0
default beholder_thyrsusgift = 0

label beholder01:
    $ renpy.music.play("audio/track_12beholder.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    if not beholder_fruit:
        play nature "audio/ambient/beholder01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    else:
        play nature "audio/ambient/beholder02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    nvl clear
    if not beholder_altar_awakened:
        show areapicture beholder01 at basicfade behind beholdercut
        $ beholder_fluff_tree = "The tree is perfectly still and hasn’t changed a bit since the first time you saw it."
    elif (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The wind is moving the branches gently."
        show areapicture beholder02 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
        show areapicture beholder03 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
        show areapicture beholder04 at basicfade behind beholdercut
    elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
        $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. You also see more roots breaking through the water’s surface."
        show areapicture beholder05 at basicfade behind beholdercut
    elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
        $ beholder_fluff_tree = "The tree is much taller and stronger, and it has grown a weird, pale fruit. However, it doesn’t move anymore."
        show areapicture beholder06 at basicfade behind beholdercut
    else:
        $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
        if beholder_branch:
            show areapicture beholder07b at basicfade behind beholdercut
        else:
            show areapicture beholder07 at basicfade behind beholdercut
    if beholder_cutroot:
        show beholdercut 01 at basicfade
    label beholder_fluffloop:
        $ beholder_fluff = ""
        $ beholder_fluff = renpy.random.choice(['A large, black-and-green bird is sitting on the altar. When you get closer, it spreads its wings and flies away.', 'The smell of the water hasn’t changed a bit, but the cold breeze brings refreshing air from the meadows.', 'You think you see a moving root, but as you observe it, it lies still.', 'The bubbles are breaking through the water’s surface, but you can’t get close enough to identify their source.', 'You hear the sound of a small creature jumping into the water.'])
        if beholder_fluff_old == beholder_fluff:
            jump beholder_fluffloop
        else:
            $ beholder_fluff_old = beholder_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if not beholder_firsttime:
        $ beholder_firsttime = 1
        $ world_known_areas += 1
        $ ruinedvillage_unlocked = 1
        $ druidcave_unlocked = 1
        $ howlersdell_unlocked = 1
        if ruinedvillage_firsttime and beholder_firsttime and howlersdell_firsttime:
            $ pyrrhos_quest_tohowlersdell = 1
        jump beholderfirsttime01
    else:
        jump beholderregular01

label beholderfirsttime01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ pc_faithpoints_opportunities += 1
    if howlersdell_firsttime:
        $ custom1 = "You think about the tree you saw in the square of {color=#f6d6bd}Howler’s Dell{/color}, but which was much smaller."
    else:
        $ custom1 = ""
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
        $ pc_faithpoints_opportunities += 1
    menu:
        'This... plant shouldn’t be alive, not without leaves. It doesn’t resemble the other trees of the wetlands. It’s something else. [custom1]
        \n\nYou get off your horse and prepare your axe. The water is filled with dirt and dead plants, and it smells like an old corpse. The roots are spreading far, breaking through the water’s surface. You don’t see any saurians in the grasses or on the shore.
        \n\nYou approach the table-like altar made of three limestone slabs. Were these rocks originally as formless as they are now, or was there a point in time, centuries ago, when they were precisely shaped and decorated by masters of artistry? There’s no way to tell.
        \n\n{color=#f6d6bd}[horsename]{/color} is peacefully observing the dark grass and slapping flies with its tail. Whatever it is that you feel in the air, it’s clear that your companion sees this place through very different eyes.
        '
        'I smile and scratch the bottom of its neck. “Go ahead. I’ll look around for just a moment.”' if pc_likeshorsename:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile and scratch the bottom of its neck. “Go ahead. I’ll look around for just a moment.”')
            jump beholderafterinteraction
        'I encourage it to graze while I look around.' if not pc_likeshorsename:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I encourage it to graze while I look around.')
            jump beholderafterinteraction
        'I know there are dark forces hidden in here. I ask The Wright for a vigilant eye and a bright soul.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I know there are dark forces hidden in here. I ask The Wright for a vigilant eye and a bright soul.')
            $ pc_faithpoints += 1
            jump beholderfirsttime01a
        'There must be a strong spirit hidden in this tree. Maybe I should bring it a gift.' if pc_religion == "pagan" or pc_religion == "unknown":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- There must be a strong spirit hidden in this tree. Maybe I should bring it a gift.')
            jump beholderfirsttime01b

label beholderfirsttime01a:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'You bow your head, trying to imagine an appropriate ritual. Whenever you start a thought, it runs away, to the sounds of insects, visions of predators, smells of the muddy water.
        \n\nYou rub your hands, focusing on what’s in your grasp, collecting your wits slowly. It takes a few moments, but you start breathing without sensing the stench. You arrange all the chaotic images into a cohesive utterance. Your prayer is brief, but once it’s done, you feel prepared.
        '
        'I approach the altar.':
            if beholder_altar_seen:
                jump beholderaltar01
            else:
                jump beholderaltarfirsttime01
        'I look into the water.' if not beholder_water_seen:
            jump beholderwater01
        'I take a closer look at the roots.' if not beholder_cutroot and not beholder_cutroot_blocked and beholder_water_seen:
            jump beholderroots01

label beholderfirsttime01b:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'You’ve never seen a soul carrier like this one, but you find a comforting glory in its haunting form. You see it as a part of the natural order, an incarnation of death. For many cityfolk, the only acceptable wilderness includes wild game, flowers, and birch sap. But you know the value of balance, the cycle of all things.
        \n\nYou wonder what sort of offerings people bring here. You doubt that an altar like this one could play only a ceremonial function. Animals, maybe?
        '
        'I approach the altar.':
            if beholder_altar_seen:
                jump beholderaltar01
            else:
                jump beholderaltarfirsttime01
        'I look into the water.' if not beholder_water_seen:
            jump beholderwater01
        'I take a closer look at the roots.' if not beholder_cutroot and not beholder_cutroot_blocked and beholder_water_seen:
            jump beholderroots01

label beholderregular01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'You reach the crossroads. [beholder_fluff_tree] [beholder_fluff]
        '
        'I approach the altar.':
            if beholder_altar_seen:
                jump beholderaltar01
            else:
                jump beholderaltarfirsttime01
        'I look into the water.' if not beholder_water_seen:
            jump beholderwater01
        'I take a closer look at the roots.' if not beholder_cutroot and not beholder_cutroot_blocked and beholder_water_seen:
            jump beholderroots01

label beholderafterinteraction:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'You don’t see any creatures, nor humans.
        '
        'I approach the altar.':
            if beholder_altar_seen:
                jump beholderaltar01
            else:
                jump beholderaltarfirsttime01
        'I look into the water.' if not beholder_water_seen:
            jump beholderwater01
        'I take a closer look at the roots.' if not beholder_cutroot and not beholder_cutroot_blocked and beholder_water_seen:
            jump beholderroots01

label beholderweirdfruit01:
    $ renpy.music.play("audio/track_05dolmen.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    menu:
        'It appeared in just a couple of moments, transforming from a button-sized sphere into a large fruit. While its shape and size resemble an apple, it’s also pale, entwining the whites and grays of bone. It’s divided into a number of slices, like an expensive toy made of marble.
        \n\nThe tree is now larger, taller, but becomes silent once motionless, sated in its hunger.
        \n\nYour farewell gift is waiting for you.
        '
        'I spend an hour or so making the tools that will allow me to pick the fruit from where I am.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I spend an hour or so making the tools that will allow me to pick the fruit from where I am.')
            $ quarters += 5
            $ item_magicfruit = 1
            $ beholder_fruit = 2
            $ renpy.notify("You gained a weird fruit.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gained a weird fruit.{/i}')
            jump beholderweirdfruit01a
        'I undress and enter the water.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I undress and enter the water.')
            $ quarters += 1
            $ item_magicfruit = 1
            $ beholder_fruit = 2
            $ renpy.notify("You gained a weird fruit.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gained a weird fruit.{/i}')
            jump beholderweirdfruit01b

label beholderweirdfruit01a:
    $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
    show areapicture beholder07 at basicfade behind beholdercut
    menu:
        'You look for two long branches in the required shapes. At first you make a curved “hook,” then a net-like piece of cloth spread between two sub-branches. The plan is simple - pull the fruit with the former, then catch it with the latter. You practice it on an imaginary branch a couple of times, until you feel ready.
        \n\nAll it takes is a single pull. It’s hard like bone, smooth like polished granite. And just as cold.
        \n\nYou look at the tree, but nothing else grabs your attention.
        '
        'I put the tools away and hide the fruit in a sack.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I put the tools away and hide the fruit in a sack.')
            $ quest_swampaltar_description04 = "The tree has answered my sacrifice with a weird, bone-like fruit. I don’t think it will grow anymore in the near future."
            $ quest_swampaltar = 2
            $ renpy.notify("Quest completed: Swamp Altar")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
            if not beholder_fruit:
                play nature "audio/ambient/beholder01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            else:
                play nature "audio/ambient/beholder02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            jump beholderafterinteraction

label beholderweirdfruit01b:
    $ beholder_branch = 1
    $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
    show areapicture beholder07b at basicfade behind beholdercut
    $ cleanliness = limit_cleanliness(cleanliness-3)
    show minus3appearance at appearancechange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 appearance points.{/i}')
    menu:
        'You take off your clothes and step into the warm, bubbling fluid, surrounded by the stench of dead shells. The water is shallow, but your feet don’t land only on mud - with every step, you touch tree roots of various sizes, thicker than a spider web, covered with just a thin layer of dirt.
        \n\nThe bough begins to lower itself, greeting your presence. All it takes is a gentle pull - the fruit is hard like bone, smooth like polished granite. And just as cold.
        \n\nYou look at the tree, but nothing else grabs your attention. You’re wet, smelly, and the wind is almost painful.
        '
        'I return to my clothes, hide the fruit in a sack, rinse my shell with clean water, and get dressed.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to my clothes, hide the fruit in a sack, rinse my shell with clean water, and get dressed.')
            $ quest_swampaltar_description04 = "The tree has answered my sacrifice with a weird, bone-like fruit. I don’t think it will grow anymore in the near future."
            $ quest_swampaltar = 2
            $ renpy.notify("Quest completed: Swamp Altar")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
            if not beholder_fruit:
                play nature "audio/ambient/beholder01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            else:
                play nature "audio/ambient/beholder02.ogg" fadeout 2.0 fadein 5.0 volume 1.0
            jump beholderafterinteraction

label beholderwater01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look into the water.')
    $ beholder_water_seen = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'You step cautiously. Without knowing how deep it gets, you have to consider that a saurian could be camouflaged in the mud, waiting for a victim to get near. Since you don’t plan to kneel down and drink, you’re hoping to dodge a potential strike.
        \n\nOnce you get closer, you start breathing again. While the water is dirty, it’s also shallow. You see the vegetation, swimming insects, and even small fish. All of them stay away from the tree roots, which look like a spider web covering the bottom of the pond.
        \n\nAside from that, you don’t see anything that would catch your attention.
        '
        'I approach the altar.':
            if beholder_altar_seen:
                jump beholderaltar01
            else:
                jump beholderaltarfirsttime01
        'I take a closer look at the roots.' if not beholder_cutroot and not beholder_cutroot_blocked and beholder_water_seen:
            jump beholderroots01

label beholderroots01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the roots.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    menu:
        'You kneel in front of one that’s lying on the shore. It’s brown, covered with hair that resembles that on your arm.
        \n\nWhen you touch it, it’s moist, soft, and warmer than you’d expect.
        '
        'I do something with it.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I do something with it.')
            if not tutorial_input:
                $ tutorial_input = 1
                $ tutorial_input_roots = 1
            python:
                search = renpy.input("What do you try to do? (example: kick)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            $ tutorial_input = 2
            $ tutorial_input_roots = 0
            jump interactrootbeholder
        'I stand up.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
            jump beholderafterinteraction

label interactrootbeholder:
    if search == "nothing" or search == "none" or search == "something" or search == "anything" or search == "whatever" or search == " " or search == "":
        menu:
            'And you do nothing.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    elif search == "fuck" or search == "sex" or search == "wtf" or search == "shit" or search == "nigger" or search == "nigga" or search == "fag":
        menu:
            'Grow up.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    elif search == "cut" or search == "slit" or search == "slash" or search == "pierce" or search == "gash" or search == "injure" or search == "hurt" or search == "lacerate" or search == "knife" or search == "stab":
        if pc_religion == "pagan":
            $ custom1 = ", but you doubt your ancestors would approve of it"
        else:
            $ custom1 = ""
        menu:
            'You pull out your knife, then stop in place. You can’t tell what the results of {i}wounding{/i} the tree would be[custom1].
            '
            'I make the cut.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make the cut.')
                if pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                    $ pc_faithpoints -= 1
                $ beholder_cutroot = day
                $ beholder_altar_awakened_threshold += 2
                show beholdercut 01 at basicfade
                $ quarters += 1
                $ item_beholderroot = 1
                $ renpy.notify("You pick up the root.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You pick up the root.{/i}')
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                menu:
                    'The cut is swift, but the nimble root is difficult to hold. It backs down into the water, pulled by the rest of the creature, leaving trail or red bubbles and mud. The water quiets down a few minutes later.
                    \n\nA chunk of the root is still in your fingers, so you move it into a jar from your bundles. Your hand is now covered with a red, sticky {i}goo{/i}, smelling like rusty nails and sweet fruits mixed with beer. You reach for a water skin and wash the plant’s juices from your skin.
                    '
                    'I walk away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                        jump beholderafterinteraction
            'I better spare it.' if pc_religion != "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better spare it.')
                $ beholder_cutroot_blocked = 1
                $ achievement_animalssavedpoints += 1
                jump beholderafterinteraction
            'I ought to spare it.' if pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ought to spare it.')
                $ beholder_cutroot_blocked = 1
                $ achievement_animalssavedpoints += 1
                $ pc_faithpoints_opportunities += 1
                $ pc_faithpoints += 1
                jump beholderafterinteraction
    elif search == "cutoff" or search == "cutthrough" or search == "cutaway" or search == "chopoff" or search == "chop" or search == "axe" or search == "ax" or search == "attack":
        if pc_religion == "pagan":
            $ custom1 = ", but you doubt your ancestors would approve of it"
        else:
            $ custom1 = ""
        menu:
            'You pull out your axe, then stop in place. You can’t tell what the results of {i}wounding{/i} the tree would be[custom1].
            '
            'I make the cut.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make the cut.')
                if pc_religion == "pagan":
                    $ pc_faithpoints_opportunities += 1
                    $ pc_faithpoints -= 1
                $ beholder_cutroot = day
                $ beholder_altar_awakened_threshold += 2
                show beholdercut 01 at basicfade
                $ item_beholderroot = 1
                $ renpy.notify("You pick up the root.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You pick up the root.{/i}')
                menu:
                    'You stand above the root like you are about to split firewood. The swing is accurate, but the nimble root backs down into the water, pulled by the rest of the creature, leaving trail or red bubbles and mud
                    \n\nA chunk of the root is still in your fingers, so you move it into a jar from your bundles. The axe is now covered with a red, sticky {i}goo{/i}, smelling like rusty nails and sweet fruits mixed with beer. You reach for a water skin and wash the blade from the plant’s juices.
                    '
                    'I walk away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                        jump beholderafterinteraction
            'I better spare it.' if pc_religion != "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better spare it.')
                $ beholder_cutroot_blocked = 1
                $ achievement_animalssavedpoints += 1
                jump beholderafterinteraction
            'I ought to spare it.' if pc_religion == "pagan":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ought to spare it.')
                $ beholder_cutroot_blocked = 1
                $ achievement_animalssavedpoints += 1
                $ pc_faithpoints_opportunities += 1
                $ pc_faithpoints += 1
                jump beholderafterinteraction
    elif search == "bite" or search == "chew" or search == "eat" or search == "munch":
        menu:
            '...The scent of decaying water is now especially repellent. You bite into the warm root and start chewing it, but with no results. It’s flexible and stretchy, and you can’t hurt it with something so blunt.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    elif search == "touch" or search == "pat" or search == "poke":
        menu:
            'The root is moist, soft, and weirdly warm.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    elif search == "kick" or search == "kickit" or search == "boot" or search == "hit" or search == "punch" or search == "blow" or search == "bash" or search == "crush" or search == "squash" or search == "stand" or search == "standon" or search == "fist" or search == "strike":
        menu:
            'The root is flexible and stretchy, your blunt hits sink into it like it’s a pillow. Whenever you lean away, it returns to its original shape.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    elif search == "push" or search == "push in" or search == "nudge":
        menu:
            'The root doesn’t resist your touch and you can easily bend it. You try to push it into the water, but with no effect - whenever you let it go, it returns to its original position.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    elif search == "hold" or search == "grasp" or search == "grip" or search == "catch" or search == "squeeze" or search == "clutch" or search == "bend":
        menu:
            'The root doesn’t resist your touch and you can easily bend it. You hold it tightly and your hands sink into it like it’s a soft pillow. You feel its warmth, but when you hold it for a fair bit, you notice a gentle itching on your skin.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    elif search == "pull" or search == "tug" or search == "draw" or search == "stretch":
        menu:
            'The root doesn’t resist your touch and you can easily bend it. You hold it tightly and your hands sink into it like it’s a soft pillow. You feel its warmth.
            \n\nYou start to pull, but with little to no effect, no matter how much strength you put into it. It’s firmly held by something in the water, probably covered by the swamp’s floor.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    elif search == "hug" or search == "cuddle":
        menu:
            '...I mean, it’s really dirty and disgusting.
            '
            'So what?':
                $ search = "realhug"
                jump interactrootbeholder
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    elif search == "realhug":
        menu:
            'The root is soft and doesn’t resist your touch. You hold it tightly, even though its smell is not far off from the stench of water from which it sticks out. While your gambeson keeps it away, you can still feel its warmth, or maybe it’s just a trick of your imagination. After a couple of moments, it doesn’t look like it’s trying to hurt you, but you feel a... pulse, of sorts.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    elif search == "kiss" or search == "lick":
        menu:
            '...?
            '
            'Like I said.':
                $ search = "realkiss"
                jump interactrootbeholder
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    elif search == "realkiss":
        menu:
            'The root is soft and doesn’t resist your touch. Its smell is not far off from the stench of water from which it sticks out. You feel its warmth, or maybe it’s just a trick of your imagination. After a couple of moments, your lips start to itch.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction
    else:
        menu:
            'Either you can’t do that, or I don’t understand you.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactrootbeholder
            'I stand up.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                jump beholderafterinteraction

label beholderaltarfirsttime01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the altar.')
    $ beholder_altar_seen = 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ quest_swampaltar = 1
    $ renpy.notify("New entry: Swamp Altar")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Swamp Altar{/i}')
    $ at = 0
    if pc_class == "mage" and not beholder_altar_amulet and not beholder_caneat_magic:
        $ at_unlock_spell = 1
        $ manacost = 1
    menu:
        'There’s clumped dirt in the uneven nicks, fused by years of winds and rains. The bottom surface of the table is dusty, but you don’t find any spiderwebs or mold, even though it’s a perfect spot for them.
        \n\nThe tree roots cling to the altar in many spots. They’re firmly attached - you struggle to move them even by an inch.
        \n\nThe cream-colored limestone is cold and smooth.
        '
        'I use an amulet to detect if there’s any magic hidden in the altar. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and mana >= manacost" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use an amulet to detect if there’s any magic hidden in the altar.')
            $ at = 0
            $ at_unlock_spell = 0
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Lost %s pneuma.{/i}' %manacost)
            $ beholder_altar_amulet = 1
            jump beholderaltarusingamulet01
        'I lack pneuma to look for magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
            pass
        'I try to make an offering.':
            $ at = 0
            $ at_unlock_spell = 0
            if not tutorial_input:
                $ tutorial_input = 1
            python:
                search = renpy.input("What is your sacrifice? (example: food)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            $ tutorial_input = 2
            jump interactaltarbeholder
        'I walk away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
            $ at = 0
            $ at_unlock_spell = 0
            jump beholderafterinteraction

label beholderaltarusingamulet01:
    $ quarters += 1
    menu:
        'You unpack the wooden spheres, pleasantly smooth and light. The entire set fits in the palm of your hand.
        \n\nYou place them in various spots - on the altar, next to the roots beneath it, and a few steps away, on the boulder. You begin the ritual, after which all you can do is wait. You go for a walk with {color=#f6d6bd}[horsename]{/color}, making sure there are no monsters in your vicinity.
        \n\nWhen you return to collect your amulets, only the one placed on the rock hasn’t changed its temperature. The others are cold. The closer they are to the tree roots, the cooler they are, almost painfully so.
        \n\nThis is not what was supposed to happen. If the objects are filled with magic, the spheres get warmer. If not, they stay in their original state. But this? You’ve never seen such a reaction.
        '
        'I try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction

label beholderaltar01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the altar.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ at = 0
    if pc_class == "mage" and not beholder_altar_amulet and not beholder_caneat_magic:
        $ at_unlock_spell = 1
        $ manacost = 1
    $ beholder_altar_open = 0
    if not beholder_fruit:
        if pc_class == "mage":
            if not beholder_caneat_blood or not beholder_caneat_items or not beholder_caneat_magic:
                $ beholder_altar_open = 1
        else:
            if not beholder_caneat_blood or not beholder_caneat_items:
                $ beholder_altar_open = 1
    menu:
        'The cream-colored limestone is cold and smooth. [beholder_fluff_tree]
        '
        'I use an amulet to detect if there’s any magic hidden in the altar. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell' and mana >= manacost" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I use an amulet to detect if there’s any magic hidden in the altar.')
            $ at = 0
            $ at_unlock_spell = 0
            $ mana = limit_mana(mana-manacost)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Lost %s pneuma.{/i}' %manacost)
            $ beholder_altar_amulet = 1
            jump beholderaltarusingamulet01
        'I lack pneuma to look for magic. [[Cost: [manacost]] (disabled)' ( condition="at_unlock_spell == 1 and mana < manacost" ):
            pass
        'I make an offering.' if beholder_altar_open:
            $ at = 0
            $ at_unlock_spell = 0
            if not tutorial_input:
                $ tutorial_input = 1
            python:
                search = renpy.input("What is your sacrifice? (example: food)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            $ tutorial_input = 2
            jump interactaltarbeholder
        'I offer my blood.' ( condition="beholder_caneat_blood and pc_hp and not beholder_fruit" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer my blood.')
            $ at = 0
            $ at_unlock_spell = 0
            jump beholderaltarblooddonation
        'I’m too weak to offer my blood. (Required vitality: 1) (disabled)' ( condition="beholder_caneat_blood and not pc_hp and not beholder_fruit" ):
            pass
        'I offer a magical item.' if beholder_caneat_items or item_casket:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer a magical item.')
            $ at = 0
            $ at_unlock_spell = 0
            jump beholderaltaritemdonation
        'I offer my magical power. [[Cost: {color=#f6d6bd}3{/color} or more]' ( condition="beholder_caneat_magic and pc_class == 'mage' and mana >= 3 and not beholder_fruit" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I offer my magical power.')
            $ at = 0
            $ at_unlock_spell = 0
            jump beholderaltarmagicdonation
        'There’s no pneuma left in me. I can’t sacrifice it. [[Cost: 3 or more] (disabled)' ( condition="beholder_caneat_magic and pc_class == 'mage' and mana < 3 and not beholder_fruit" ):
            pass
        'I walk away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
            $ at = 0
            $ at_unlock_spell = 0
            jump beholderafterinteraction

label beholderaltarblooddonation:
    if not beholder_caneat_blood:
        menu:
            '...
            \n\nHow much?
            '
            'Just a couple of drops from the tip of my finger.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Just a couple of drops from the tip of my finger.')
                jump beholderaltarblooddonationdroplets
            'I make a slight cut on the palm of my hand. It will only hurt a little.' ( condition="pc_hp >= 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make a slight cut on the palm of my hand. It will only hurt a little.')
                $ beholder_caneat_blood = 1
                if not beholder_altar_feeding_firstday:
                    $ beholder_altar_feeding_firstday = day
                $ beholder_altar_feeding_lastday = day
                $ beholder_altar_awakened += 2
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                jump beholderaltarblooddonationfirsttime
            'I make a deep cut.' ( condition="pc_hp >= 2" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make a deep cut.')
                $ beholder_caneat_blood = 1
                if not beholder_altar_feeding_firstday:
                    $ beholder_altar_feeding_firstday = day
                $ beholder_altar_feeding_lastday = day
                $ beholder_altar_awakened += 4
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                jump beholderaltarblooddonationfirsttime
            'I clench my teeth and hurt myself quite a bit.' ( condition="pc_hp >= 3" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clench my teeth and hurt myself quite a bit.')
                $ beholder_caneat_blood = 1
                if not beholder_altar_feeding_firstday:
                    $ beholder_altar_feeding_firstday = day
                $ beholder_altar_feeding_lastday = day
                $ beholder_altar_awakened += 6
                $ pc_hp = limit_pc_hp(pc_hp-3)
                show minus3hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                jump beholderaltarblooddonationfirsttime
            'As much as I can before I faint.' ( condition="pc_hp >= 4" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- As much as I can before I faint.')
                $ beholder_caneat_blood = 1
                if not beholder_altar_feeding_firstday:
                    $ beholder_altar_feeding_firstday = day
                $ beholder_altar_feeding_lastday = day
                $ pc_hp = limit_pc_hp(pc_hp-4)
                show minus4hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
                $ beholder_altar_awakened += 9
                jump beholderaltarblooddonationfirsttime
            'I can’t offer any more in my current state. (disabled)' ( condition="pc_hp < 4" ):
                pass
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    else:
        menu:
            'How much blood do you sacrifice?
            '
            'I make a slight cut on the palm of my hand. It will only hurt a little.' ( condition="pc_hp >= 1" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make a slight cut on the palm of my hand. It will only hurt a little.')
                $ beholder_altar_feeding_lastday = day
                $ beholder_altar_awakened += 2
                $ pc_hp = limit_pc_hp(pc_hp-1)
                show minus1hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
                jump beholderaltarblooddonationmoretimes
            'I make a deep cut.' ( condition="pc_hp >= 2" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make a deep cut.')
                $ beholder_altar_feeding_lastday = day
                $ beholder_altar_awakened += 4
                $ pc_hp = limit_pc_hp(pc_hp-2)
                show minus2hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
                jump beholderaltarblooddonationmoretimes
            'I clench my teeth and hurt myself quite a bit.' ( condition="pc_hp >= 3" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clench my teeth and hurt myself quite a bit.')
                $ beholder_altar_feeding_lastday = day
                $ beholder_altar_awakened += 6
                $ pc_hp = limit_pc_hp(pc_hp-3)
                show minus3hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
                jump beholderaltarblooddonationmoretimes
            'As much as I can before I faint.' ( condition="pc_hp >= 4" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- As much as I can before I faint.')
                $ beholder_altar_feeding_lastday = day
                $ pc_hp = limit_pc_hp(pc_hp-4)
                show minus4hp at hpchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
                $ beholder_altar_awakened += 9
                jump beholderaltarblooddonationmoretimes
            'I can’t offer any more in my current state. (disabled)' ( condition="pc_hp < 4" ):
                pass
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction

label beholderaltarblooddonationdroplets:
    menu:
        'You jab a finger with your knife. The blood flows slowly and you pay close attention to the moment when it falls on the altar’s surface.
        \n\nEach drop splashes in all directions, then disappears. You see no trace of them.
        '
        'I make a slight cut on the palm of my hand. It will only hurt a little.' ( condition="pc_hp >= 1" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make a slight cut on the palm of my hand. It will only hurt a little.')
            $ beholder_caneat_blood = 1
            if not beholder_altar_feeding_firstday:
                $ beholder_altar_feeding_firstday = day
            $ beholder_altar_feeding_lastday = day
            $ beholder_altar_awakened += 2
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            jump beholderaltarblooddonationfirsttime
        'I make a deep cut.' ( condition="pc_hp >= 2" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I make a deep cut.')
            $ beholder_caneat_blood = 1
            if not beholder_altar_feeding_firstday:
                $ beholder_altar_feeding_firstday = day
            $ beholder_altar_feeding_lastday = day
            $ beholder_altar_awakened += 4
            $ pc_hp = limit_pc_hp(pc_hp-2)
            show minus2hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
            jump beholderaltarblooddonationfirsttime
        'I clench my teeth and hurt myself quite a bit.' ( condition="pc_hp >= 3" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I clench my teeth and hurt myself quite a bit.')
            $ beholder_caneat_blood = 1
            if not beholder_altar_feeding_firstday:
                $ beholder_altar_feeding_firstday = day
            $ beholder_altar_feeding_lastday = day
            $ beholder_altar_awakened += 6
            $ pc_hp = limit_pc_hp(pc_hp-3)
            show minus3hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-3 vitality points.{/i}')
            jump beholderaltarblooddonationfirsttime
        'As much as I can before I faint.' ( condition="pc_hp >= 4" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- As much as I can before I faint.')
            $ beholder_caneat_blood = 1
            if not beholder_altar_feeding_firstday:
                $ beholder_altar_feeding_firstday = day
            $ beholder_altar_feeding_lastday = day
            $ pc_hp = limit_pc_hp(pc_hp-4)
            show minus4hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-4 vitality points.{/i}')
            $ beholder_altar_awakened += 9
            jump beholderaltarblooddonationfirsttime
        'I can’t offer any more in my current state. (disabled)' ( condition="pc_hp < 4" ):
            pass
        'I try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction

label beholderaltarblooddonationfirsttime:
    $ renpy.notify("Journal updated: Swamp Altar")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
    $ quest_swampaltar_description01 = "The tree reacts when I “feed” it with human blood."
    if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The wind is moving the branches gently."
        show areapicture beholder02 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
        show areapicture beholder03 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
        show areapicture beholder04 at basicfade behind beholdercut
    elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
        $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. You also see more roots breaking through the water’s surface."
        show areapicture beholder05 at basicfade behind beholdercut
    elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
        $ beholder_fruit = 1
        $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
        show areapicture beholder06 at basicfade behind beholdercut
    else:
        $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
        if beholder_branch:
            show areapicture beholder07b at basicfade behind beholdercut
        else:
            show areapicture beholder07 at basicfade behind beholdercut
    menu:
        'Your blood spills on the altar and sinks into it before it gets to the edge. The tree greets your offering with the sound of moving, stretching branches.
        \n\nYou try to ignore the pain and prepare water and bandages to take care of the wound.
        '
        'I try something else.' if beholder_fruit != 1:
            jump beholderaltar01
        'I walk away.' if beholder_fruit != 1:
            jump beholderafterinteraction
        'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
            jump beholderweirdfruit01

label beholderaltarblooddonationmoretimes:
    if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The wind is moving the branches gently."
        show areapicture beholder02 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
        show areapicture beholder03 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
        show areapicture beholder04 at basicfade behind beholdercut
    elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
        $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
        show areapicture beholder05 at basicfade behind beholdercut
    elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
        $ beholder_fruit = 1
        $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
        show areapicture beholder06 at basicfade behind beholdercut
    else:
        $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
        if beholder_branch:
            show areapicture beholder07b at basicfade behind beholdercut
        else:
            show areapicture beholder07 at basicfade behind beholdercut
    menu:
        'Your blood spills on the altar and sinks into it before it gets to the edges. The sound of moving, stretching branches occurs almost immediately.
        '
        'I try something else.' if beholder_fruit != 1:
            jump beholderaltar01
        'I walk away.' if beholder_fruit != 1:
            jump beholderafterinteraction
        'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
            jump beholderweirdfruit01

label beholderaltarmagicdonation:
    if not beholder_caneat_magic:
        menu:
            'You don’t know a spell that could transfer your pneuma toward another object. It would require the knowledge and experience of an enchanter.
            \n\nHowever, you {i}could{/i} strike the altar with a major part of the pneuma that’s left in you. Your shell won’t be impacted in the process.
            \n\nAlso, this power is usually a bit... Dangerous toward its targets.
            '
            'I risk it. [[Cost: {color=#f6d6bd}3{/color}]' ( condition="mana >= 3" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I risk it. [[Cost: {color=#f6d6bd}3{/color}]')
                $ manacost = 3
                jump beholderaltarmagicdonationfirsttime
            'I’ll give it everything I have. [[Cost: {color=#f6d6bd}5{/color}]' ( condition="mana >= 5" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll give it everything I have. [[Cost: {color=#f6d6bd}5{/color}]')
                $ manacost = 5
                jump beholderaltarmagicdonationfirsttime
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    else:
        menu:
            'You prepare your wand.
            '
            'I’m ready for it. [[Cost: {color=#f6d6bd}3{/color}]' ( condition="mana >= 3" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m ready for it. [[Cost: {color=#f6d6bd}3{/color}]')
                $ manacost = 3
                jump beholderaltarmagicdonationmoretimes
            'I’ll give it everything I have. [[Cost: {color=#f6d6bd}5{/color}]' ( condition="mana >= 5" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll give it everything I have. [[Cost: {color=#f6d6bd}5{/color}]')
                $ manacost = 5
                jump beholderaltarmagicdonationmoretimes
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction

label beholderaltarmagicdonationfirsttime:
    $ beholder_caneat_magic = 1
    menu:
        'You unwrap the linen sheet and grab the willow wand, still as smooth as on the day you bought it. The pointy, carved twig is thin, but heavy from the injected quicksilver.
        \n\nYou raise it as if you are about to stab the air with a dagger, then make a swipe.
        '
        'Let’s hope it works.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s hope it works.')
            jump beholderaltarmagicdonationmoretimes

label beholderaltarmagicdonationmoretimes:
    if manacost == 3:
        $ beholder_altar_awakened += 4
    else:
        $ beholder_altar_awakened += 8
    $ mana = limit_mana(mana-manacost)
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Lost %s pneuma.{/i}' %manacost)
    if not beholder_altar_feeding_firstday:
        $ beholder_altar_feeding_firstday = day
    $ beholder_altar_feeding_lastday = day
    if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The wind is moving the branches gently."
        show areapicture beholder02 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
        show areapicture beholder03 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
        show areapicture beholder04 at basicfade behind beholdercut
    elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
        $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
        show areapicture beholder05 at basicfade behind beholdercut
    elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
        $ beholder_fruit = 1
        $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
        show areapicture beholder06 at basicfade behind beholdercut
    else:
        $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
        if beholder_branch:
            show areapicture beholder07b at basicfade behind beholdercut
        else:
            show areapicture beholder07 at basicfade behind beholdercut
    menu:
        'The tree greets your offering with the sound of moving, stretching branches.
        '
        'I try something else.' if beholder_fruit != 1:
            if not quest_swampaltar_description02:
                $ quest_swampaltar_description02 = "The altar is responding to magical powers. I can use my pneuma as a sacrifice, but it will temporarily make me unable to use any more spells."
                $ renpy.notify("Journal updated: Swamp Altar")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
            jump beholderaltar01
        'I walk away.' if beholder_fruit != 1:
            if not quest_swampaltar_description02:
                $ quest_swampaltar_description02 = "The altar is responding to magical powers. I can use my pneuma as a sacrifice, but it will temporarily make me unable to use any more spells."
                $ renpy.notify("Journal updated: Swamp Altar")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
            jump beholderafterinteraction
        'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
            jump beholderweirdfruit01

label beholderaltaritemdonation:
    menu:
        'Which item would you like to sacrifice?
        '
        'The cursed coins.' if item_casket:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The cursed coins.')
            jump altardonatingmagicitemcasket
        'A spirit rock.' if item_spiritrock:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- A spirit rock.')
            jump altardonatingmagicitemspiritrock
        'The potion I found in the dolmen.' if item_potiondolmen:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The potion I found in the dolmen.')
            jump altardonatingmagicitempotiondolmen
        'A small healing potion.' if item_smallhealingpotion:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- A small healing potion.')
            jump altardonatingmagicitemsmallhealingpotion
        'One of my healing potions.' if item_generichealingpotion:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- One of my healing potions.')
            jump altardonatingmagicitemgenerichealingpotion
        'A share of my sharpening poison.' if item_sharpeningpotion >= 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- One of my healing potions.')
            jump altardonatingmagicitemsharpeningpotion
        'My sharpening poison.' if item_sharpeningpotion == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- My sharpening poison.')
            jump altardonatingmagicitemsharpeningpotion
        'The magic quills I’m carrying for {color=#f6d6bd}the monks{/color}.' if item_magicpens:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The magic quills I’m carrying for {color=#f6d6bd}the monks{/color}.')
            jump altardonatingmagicitemmagicpens
        'A bronze rod that I got from {color=#f6d6bd}Eudocia{/color}.' if item_bronzerod:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- A bronze rod that I got from {color=#f6d6bd}Eudocia{/color}.')
            $ beholder_caneat_bronzerod = 1
            jump altardonatingmagicitembronzerod
        'Asterion’s cloak.' if item_asterioncloak:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Asterion’s cloak.')
            jump altardonatingmagicitemasterioncloak
        'The magic chisel.' if item_magicchisel == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The magic chisel.')
            jump altardonatingmagicitemmagicchisel
        'The Tool of Destruction.' if item_magicchisel == 2:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The Tool of Destruction.')
            jump altardonatingmagicitemmagicchisel
        'The Golem Glove.' if item_golemglove:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The Golem Glove.')
            jump altardonatingmagicitemgolemglove
        'The dragon horn.' if item_dragonhorn:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The dragon horn.')
            jump altardonatingmagicitemdragonhorn
        'The blinding powder.' if item_blindingpowder:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The blinding powder.')
            jump altardonatingmagicitemblindingpowder
        'The withering dust.' if item_witheringdust:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The withering dust.')
            jump altardonatingmagicitemwitheringdust
        'I try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction

label interactaltarbeholder:
    ###################################### Does nothing / Easter eggs
    if search == "nothing" or search == "none":
        menu:
            'And you give nothing.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    elif search == "item" or search == "anitem" or search == "something" or search == "anything" or search == "whatever" or search == "magical item" or search == "armor" or search == "weapon" or search == "trinket" or search == "treasure" or search == "object" or search == "stuff" or search == "cloth" or search == "things" or search == "thing" or search == "plant" or search == "fur" or search == "trophy" or search == "furs" or search == "skin" or search == "skins" or search == "claw" or search == "claws" or search == "tusk" or search == "tooth" or search == "teeth" or search == "keys" or search == "key" or search == "potion" or search == "magicitem" or search == "healingpotion" or search == "healingelixir" or search == "magicstone" or search == "potionfrommonastery":
        menu:
            'You need to be more specific.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    elif search == "rock" or search == "rocks" or search == "stone" or search == "stones" or search == "pebble" or search == "pebbles" or search == "ground" or search == "dirt" or search == "earth":
        menu:
            'You place a couple of regular rocks on the altar, but it doesn’t look like it does anything.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    elif search == "water" or search == "drink":
        menu:
            'You pour out both clean water and some of the smelly liquid from the swamp, but in both cases nothing occurs.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    elif search == "branch" or search == "stick" or search == "branches" or search == "flower" or search == "flowers" or search == "grass" or search == "bough" or search == "mushroom" or search == "mushrooms" or search == "fungi" or search == "leaf" or search == "leaves" or search == "herb" or search == "herbs" or search == "plants":
        menu:
            'You place a couple of plants of all types and sizes, but none of them seems to do anything.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    elif search == "foodrations" or search == "rations" or search == "fruit" or search == "fruits" or search == "ration" or search == "foodration" or search == "vegetable" or search == "vegetables" or search == "vegetables" or search == "abucketfulofberries" or search == "bucketfulofberries" or search == "abucketfulberries" or search == "berries" or search == "greens" or search == "food" or search == "meal":
        menu:
            'You place any type of food you can find in your sacks or on the nearby plants, but none of them seem to make any difference.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    elif search == "spit" or search == "saliva":
        menu:
            'You spit on the altar, but nothing happens.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    elif search == "piss" or search == "urine" or search == "shit" or search == "feces" or search == "faeces" or search == "excrement" or search == "filth" or search == "dung":
        menu:
            '...Nothing happens.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    elif search == "hair":
        menu:
            'You pull out a hair of yours and put it on the altar, but you don’t see any change.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    elif search == "myself" or search == "myshell" or search == "mybody" or search == "mylife" or search == "hand" or search == "life" or search == "self" or search == "shell" or search == "body" or search == "life":
        menu:
            'You put your hand on the altar, but you don’t see any reaction.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    ####################################### Magic and blood
    elif search == "blood" or search == "myblood" or search == "theblood":
        if beholder_fruit:
            jump beholderaltarblooddonationnotneeded
        else:
            jump beholderaltarblooddonation
    elif search == "magic" or search == "mymagic" or search == "power" or search == "mypower" or search == "myenergy" or search == "magicalenergy" or search == "energy" or search == "spell" or search == "mana" or search == "spirit" or search == "soul" or search == "myspirit" or search == "mysoul" or search == "pneuma" or search == "mypneuma" or search == "psyche" or search == "mypsyche":
        $ manacost = 3
        if pc_class != "mage":
            menu:
                'While all humans have some amount of pneuma inside them, you don’t know how to channel it. It would take an experienced spellcaster.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        elif mana < manacost:
            menu:
                'You feel like there’s almost no pneuma left in your shell. You can’t try to cast a spell. [[Cost: {color=#f6d6bd}[manacost]{/color}]
                '
                'I make a different offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            if beholder_fruit:
                jump beholderaltarmagicdonationnotneeded
            else:
                jump beholderaltarmagicdonation
    ########################################### Real items that do nothing
    elif search == "antlers" or search == "theantlers" or search == "theantlers" or search == "antlers" or search == "thesetofantlers" or search == "thesetofantlers" or search == "thesetantlers" or search == "antlersset" or search == "antlerset":
        if item_antlers:
            menu:
                'You put the set of antlers on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "asterionbow" or search == "asterionsbow" or search == "theasterionsbow" or search == "theasterionbow":
        if item_asterionbow:
            menu:
                'You put the bow on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "asterionspear" or search == "asterionsspear" or search == "theasterionsspear" or search == "theasterionspear":
        if item_asterionspear:
            menu:
                'You put the spear on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "aspear" or search == "mountainroadspear" or search == "aspear" or search == "spear":
        if item_asterionspear or item_mountainroadspear:
            menu:
                'You put the spear on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "asterionpurse" or search == "asterionspurse" or search == "asterionbag" or search == "theasterionspurse" or search == "theasterionpurse" or search == "theasterionsbag" or search == "theasterionpouch" or search == "asterionpouch" or search == "asterionspouch" or search == "theasterionspouch" or search == "theasterionpouch":
        if item_asterionpurse:
            menu:
                'You put the pouch on the altar. It vibrates a bit.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "arrow" or search == "thearrow" or search == "thesimplearrow" or search == "anarrow" or search == "asimplearrow" or search == "aarrow" or search == "abasicarrow" or search == "humanarrow" or search == "thehumanarrow" or search == "ahumanarrow":
        if item_arrow:
            if not beholder_arrow:
                $ beholder_arrow = 1
                if beholder_thyrsusgift:
                    $ beholder_altar_awakened += 1
                menu:
                    'You put the arrow on the altar and its feathers get slightly darker, but after another breath, no more changes occur. You try to repeat this action, but to no avail.
                    '
                    'I make an offering.':
                        python:
                            search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump interactaltarbeholder
                    'I try something else.':
                        jump beholderaltar01
                    'I walk away.':
                        jump beholderafterinteraction
            else:
                menu:
                    'You put the arrow on the altar, but nothing happens.
                    '
                    'I make an offering.':
                        python:
                            search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump interactaltarbeholder
                    'I try something else.':
                        jump beholderaltar01
                    'I walk away.':
                        jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "thyrsusgift" or search == "thyrsussgift" or search == "giftforparents" or search == "giftforthyrsusparents" or search == "giftparents" or search == "thyrsusbelongings" or search == "thyrsusbelonging" or search == "thyrsuschildhood" or search == "thyrsustoys" or search == "toy" or search == "toys" or search == "doll" or search == "athyrsusgift" or search == "athyrsussgift" or search == "agiftforparents" or search == "agiftforthyrsusparents" or search == "agiftparents" or search == "athyrsusbelongings" or search == "athyrsusbelonging" or search == "athyrsuschildhood" or search == "athyrsustoys" or search == "atoy" or search == "atoys" or search == "adoll" or search == "thethyrsusgift" or search == "thethyrsussgift" or search == "thegiftforparents" or search == "thegiftforthyrsusparents" or search == "thegiftparents" or search == "thethyrsusbelongings" or search == "thethyrsusbelonging" or search == "thethyrsuschildhood" or search == "thethyrsustoys" or search == "thetoy" or search == "thetoys" or search == "thedoll":
        if item_thyrsusgift:
            if not beholder_thyrsusgift:
                $ beholder_thyrsusgift = 1
                if beholder_arrow:
                    $ beholder_altar_awakened += 1
                menu:
                    'You put {color=#f6d6bd}Thyrsus’{/color} toys on the altar, and while their edges get a bit darker, letting out a scent of smoke, they soon remain idly.
                    '
                    'I make an offering.':
                        python:
                            search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump interactaltarbeholder
                    'I try something else.':
                        jump beholderaltar01
                    'I walk away.':
                        jump beholderafterinteraction
            else:
                menu:
                    'You put {color=#f6d6bd}Thyrsus’{/color} toys on the altar, but nothing happens.
                    '
                    'I make an offering.':
                        python:
                            search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump interactaltarbeholder
                    'I try something else.':
                        jump beholderaltar01
                    'I walk away.':
                        jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "asimplebattleaxe" or search == "thesimplebattleaxe" or search == "simplebattleaxe" or search == "battleaxe" or search == "axe" or search == "wellcraftedbattleaxe" or search == "craftedbattleaxe" or search == "myaxe" or search == "ax" or search == "myax" or search == "simpleax" or search == "battleax" or search == "knife" or search == "dagger" or search == "thebattleaxe" or search == "theaxe" or search == "thewellcraftedbattleaxe" or search == "thecraftedbattleaxe" or search == "asimplebattleax" or search == "thesimplebattleax" or search == "simplebattleax" or search == "battleax" or search == "ax" or search == "wellcraftedbattleax" or search == "craftedbattleax" or search == "myax" or search == "ax" or search == "myax" or search == "simpleax" or search == "battleax" or search == "knife" or search == "dagger" or search == "thebattleax" or search == "theax" or search == "thewellcraftedbattleax" or search == "thecraftedbattleax":
        if item_axe01 or item_axe02:
            menu:
                'You put your weapon on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "axe02alt" or search == "axehead" or search == "axeset" or search == "bronzeaxe" or search == "bronzebattleaxe" or search == "bronzeblade" or search == "craftedbattleaxe" or search == "abronzeaxehead" or search == "bronzeaxeset" or search == "axehead" or search == "anaxeheadwithahandle" or search == "axeheadwithahandle" or search == "axeheadwithhandle" or search == "abronzeax" or search == "thebronzeax" or search == "bronzeax" or search == "bronzebattleax" or search == "abronzeaxhead" or search == "bronzeaxset" or search == "axhead" or search == "anaxheadwithahandle" or search == "axheadwithahandle" or search == "axheadwithhandle" or search == "an axe head with handle" or search == "anaxeheadwithhandle":
        if item_axe01 or item_axe02:
            menu:
                'You put the bronze blade on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "savings" or search == "yoursaving" or search == "yoursavings" or search == "mysaving" or search == "mysavings" or search == "thesavings" or search == "100coin" or search == "100coins" or search == "100dragonbones" or search == "100bones":
        if pc_goal_lost100coins:
            menu:
                'You put the heavy box on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "aweirdroot" or search == "weirdroot" or search == "theweirdroot" or search == "abeholderroot" or search == "beholderroot" or search == "thebeholderroot":
        if item_beholderroot:
            menu:
                'You put the tree’s root on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "bugrepellent" or search == "aherbalbugrepellent" or search == "theherbalbugrepellent" or search == "herbalbugrepellent" or search == "bugpoison" or search == "bugrepellent" or search == "aherbalbugrepellent" or search == "theherbalbugrepellent" or search == "herbalbugrepellent" or search == "bugpoison":
        if item_bugrepellent:
            menu:
                'You put the herbal ointment on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "astingointment" or search == "astingointment" or search == "thestingointment" or search == "thestingointment" or search == "stingointment" or search == "stingointment":
        if item_stingointment:
            menu:
                'You put the herbal ointment on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "cidercask" or search == "acaskofcider" or search == "thecaskofcider" or search == "cidercask" or search == "cask" or search == "caskofcider" or search == "caskcider" or search == "caskcider" or search == "ciderbarrel" or search == "abarrelofcider" or search == "thebarrelofcider" or search == "ciderbarrel" or search == "barrel" or search == "barrelofcider" or search == "barrelcider" or search == "barrelcider" or search == "cider" or search == "acider" or search == "thecider":
        if item_cidercask:
            menu:
                'You put the cask of cider on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "crossbow" or search == "mycrossbow" or search == "ballista" or search == "acrossbow" or search == "thecrossbow" or search == "theballista" or search == "aballista":
        if item_crossbow:
            menu:
                'You put your crossbow on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "empressfish" or search == "anempressfish" or search == "theempressfish" or search == "empressfish" or search == "empresscarp" or search == "anempresscarp" or search == "theempresscarp" or search == "empresscarp":
        if item_empresscarp:
            menu:
                'You put the bucket with an empress carp on the altar. There are no signs of panic coming from the inside.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "fancyoutfit" or search == "thefancyoutfit" or search == "afancyoutfit" or search == "fancyclothes" or search == "thefancyclothes" or search == "afancyclothes" or search == "fancytunic" or search == "afancytunic" or search == "thefancytunic" or search == "fancyrobe" or search == "afancyrobe" or search == "thefancyrobe" or search == "fancydress" or search == "afancydress" or search == "thefancydress":
        if item_fancyclothes:
            menu:
                'You put your fancy outfit on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "fish" or search == "afish" or search == "thefish" or search == "fishes" or search == "rawfishes" or search == "rawfish" or search == "cookedfishes" or search == "cookedfish":
        if item_rawfishtotalnumber or item_cookedfish:
            menu:
                'You put a fish on the altar. It’s now a bit dirty.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "fishtrap" or search == "afishtrap" or search == "thefishtrap" or search == "fishingtrap" or search == "fishbasket" or search == "fishingbasket":
        if item_fishtrap:
            menu:
                'You put the fish trap on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "aboxfromthedolmen" or search == "boxfromthedolmen" or search == "box" or search == "dolmenbox" or search == "boxdolmen":
        if item_boxfromdolmen:
            menu:
                'You put the box from the dolmen on the altar. Once you take it back, it’s shaking a bit.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "aberrypickinghook" or search == "berrypickinghook" or search == "pickinghook" or search == "hook" or search == "toolsforberrypicking" or search == "toolsberrypicking":
        if item_peltnorthberrytools:
            menu:
                'You put the berry picking hook on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "thebonebuckle" or search == "abonebuckle" or search == "bonebuckle" or search == "buckle" or search == "thebuckle" or search == "abuckle" or search == "thedecorativebuckle" or search == "adecorativebuckle" or search == "decorativebuckle" or search == "thedecoratedbuckle" or search == "adecoratedbuckle" or search == "decoratedbuckle" or search == "theboarbuckle" or search == "aboarbuckle" or search == "boarbuckle":
        if item_boneebuckle:
            menu:
                'You put the boar buckle on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "theboneearring" or search == "aboneearring" or search == "boneearring" or search == "earring":
        if item_boneearring:
            menu:
                'You put the earring on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "thebonering" or search == "abonering" or search == "bonering" or search == "ring":
        if item_bonering:
            menu:
                'You put the ring on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "brokenknife" or search == "abrokenknife" or search == "thebrokenknife" or search == "knifehandle" or search == "theknifehandle" or search == "aknifehandle" or search == "bone knifehandle" or search == "knifeshandle" or search == "knifehandle":
        if item_brokenknife:
            menu:
                'You put the knife handle on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "chicken" or search == "chickenroast" or search == "roastchicken" or search == "roastedchicken" or search == "chickenmeat" or search == "achicken" or search == "thechicken" or search == "thechickenroast" or search == "theroastchicken" or search == "achickenroast" or search == "aroastchicken" or search == "theroastedchicken" or search == "aroastedchicken":
        if item_chicken:
            menu:
                'You put the dead stoat on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "cidercask" or search == "caskcider" or search == "caskofcider" or search == "acaskofcider" or search == "thecaskofcider" or search == "barrelofcider" or search == "abarrelofcider" or search == "thebarrelofcider" or search == "barrelcider" or search == "ciderbarrel":
        if item_cidercask:
            menu:
                'You put the cask of cider on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "alantern" or search == "lantern" or search == "thelantern" or search == "lamp" or search == "alamp" or search == "thelamp":
        if item_lantern:
            menu:
                'You put the lantern on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "pebblersclaw" or search == "pebblerclaw" or search == "thepebblersclaw" or search == "thepebblerclaw" or search == "apebblersclaw" or search == "apebblerclaw" or search == "pebbler":
        if item_peltnorthberryclaw:
            menu:
                'You put the pebbler’s claw on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "acloakwithahood" or search == "cloakwithahood" or search == "acloakwithhood" or search == "cloakwithhood" or search == "cloakhood" or search == "thecloak" or search == "thehood" or search == "acloak" or search == "ahood":
        menu:
            'You put your cloak on the altar, but nothing happens.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    elif search == "gambesonrepairset" or search == "thegambesonrepairset" or search == "agambesonrepairset" or search == "gambesontools" or search == "thegambesontools" or search == "agambesontools" or search == "gambesonset" or search == "thegambesonset" or search == "agambesonset" or search == "gambesonkit" or search == "thegambesonkit" or search == "agambesonkit" or search == "armorkit" or search == "thearmorkit" or search == "anarmorkit":
        if item_gambesonrepairset:
            menu:
                'You put your tools on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "paintedsign" or search == "thepaintedsign" or search == "apaintedsign" or search == "sign" or search == "thesign" or search == "asign" or search == "signpost" or search == "thesignpost" or search == "asignpost" or search == "post" or search == "thepost" or search == "apost" or search == "plank" or search == "theplank" or search == "aplank":
        if item_signpost:
            menu:
                'You put the painted plank on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "sewingkit" or search == "thesewingkit" or search == "asewingkit" or search == "sewkit" or search == "thesewkit" or search == "asewkit" or search == "clotheskit" or search == "theclotheskit" or search == "aclotheskit" or search == "clothesrepairkit" or search == "theclothesrepairkit" or search == "aclothesrepairkit":
        if item_sewingkit:
            menu:
                'You put your sewing kit on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "apursewithcoins" or search == "pursewithcoins" or search == "apurse" or search == "purse" or search == "coins" or search == "coin" or search == "money" or search == "acoin" or search == "dragon" or search == "dragons" or search == "dragonbones" or search == "dragoncoins" or search == "apouchwithcoins" or search == "pouchwithcoins" or search == "apouch" or search == "pouch":
        if coins:
            menu:
                'You put both your pouch and the coins on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            menu:
                'You don’t have a single coin left, but you put your empty pouch on the altar. Nothing seems to happen.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
    elif search == "elkfur" or search == "elk" or search == "elksfur" or search == "furofelk" or search == "theelkfur" or search == "theelk" or search == "theelksfur" or search == "aelkfur" or search == "aelk" or search == "aelksfur" or search == "anelkfur" or search == "anelk" or search == "anelksfur":
        if item_elkfur:
            menu:
                'You put the fur on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "harefur" or search == "hare" or search == "haresfur" or search == "furofhare" or search == "theharefur" or search == "thehare" or search == "theharesfur" or search == "aharefur" or search == "ahare" or search == "aharesfur" or search == "anharefur" or search == "anhare" or search == "anharesfur" or search == "harepelt" or search == "harespelt" or search == "peltofhare" or search == "theharepelt" or search == "theharespelt" or search == "aharepelt" or search == "aharespelt" or search == "anharepelt" or search == "anharespelt":
        if item_harepelt:
            menu:
                'You put the pelt on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "sealfur" or search == "seal" or search == "sealsfur" or search == "furofseal" or search == "sealskin" or search == "sealpelt" or search == "thesealfur" or search == "theseal" or search == "thesealsfur" or search == "thefurofseal" or search == "thesealskin" or search == "thesealpelt" or search == "asealfur" or search == "aseal" or search == "asealsfur" or search == "afurofseal" or search == "asealskin" or search == "asealpelt" or search == "seal":
        if item_sealskin:
            menu:
                'You put the pelt on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "blanket" or search == "rawhide" or search == "rawhide" or search == "therawhide" or search == "therawhide" or search == "arawhide" or search == "lostrawhide":
        if item_rawhide:
            menu:
                'You put the rawhide on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "fishnecklace" or search == "theoceannecklace" or search == "anoceannecklace" or search == "oceannecklace" or search == "shellnecklace" or search == "sharknecklace" or search == "seashellnecklace" or search == "oceannecklace" or search == "fishscalesnecklace" or search == "scalenecklace" or search == "hamletnecklace" or search == "abandonedhamletnecklace" or search == "necklacefromhamlet":
        if item_oceannecklace:
            if not beholder_oceannecklace:
                $ beholder_altar_awakened += 1
                $ beholder_oceannecklace = 1
                menu:
                    'You put the necklace on the altar. For a few heartbeats you hear a silent whistling and the seashell cracks slightly. Nothing else happens.
                    '
                    'I make an offering.':
                        python:
                            search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump interactaltarbeholder
                    'I try something else.':
                        jump beholderaltar01
                    'I walk away.':
                        jump beholderafterinteraction
            else:
                menu:
                    'You put the necklace on the altar, but nothing happens.
                    '
                    'I make an offering.':
                        python:
                            search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump interactaltarbeholder
                    'I try something else.':
                        jump beholderaltar01
                    'I walk away.':
                        jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "aworngambeson" or search == "worngambeson" or search == "adecentgambeson" or search == "decentgambeson" or search == "afinegambeson" or search == "finegambeson" or search == "gambeson" or search == "goodgambeson" or search == "armor" or search == "strengthenedgambeson" or search == "astrengthenedgambeson" or search == "thestrengthenedgambeson":
        menu:
            'You put your armor on the altar, but nothing happens.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction
    elif search == "griffonegg" or search == "eggofgriffon" or search == "egggriffon" or search == "griffinegg" or search == "eggofgriffin" or search == "egggriffin" or search == "griffegg" or search == "eggofgriff" or search == "egggriff" or search == "deadegg" or search == "thegriffonegg" or search == "theeggofgriffon" or search == "theegggriffon" or search == "thegriffinegg" or search == "theeggofgriffin" or search == "theegggriffin" or search == "thegriffegg" or search == "theeggofgriff" or search == "theegggriff" or search == "thedeadegg" or search == "agriffonegg" or search == "aeggofgriffon" or search == "aegggriffon" or search == "agriffinegg" or search == "aeggofgriffin" or search == "aegggriffin" or search == "agriffegg" or search == "aeggofgriff" or search == "aegggriff" or search == "adeadegg":
        if item_griffonegg:
            menu:
                'You put the egg on the altar. It keeps rolling over.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "trollurine" or search == "trollsurine" or search == "atrollurine" or search == "atrollsurine" or search == "thetrollsurine" or search == "thetrollurine" or search == "ajaroftrollsurine" or search == "jaroftrollsurine" or search == "ajarofurine" or search == "jarofurine" or search == "goblinrepellent":
        if item_trollurine:
            menu:
                'You put the jar of troll’s urine on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "horse" or search == "myhorse" or search == "mount" or search == "palfrey" or search == "thehorse" or search == "themount" or search == "thepalfrey" or search == "ahorse" or search == "amount" or search == "apalfrey" or search == horsename_reduced:
        if item_horse:
            menu:
                '...{color=#f6d6bd}[horsename]{/color} is too large.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "ironscraps" or search == "iron" or search == "steelscraps" or search == "steel" or search == "metalscraps" or search == "theironscraps" or search == "theiron" or search == "thesteelscraps" or search == "thesteel" or search == "themetalscraps" or search == "aironscraps" or search == "airon" or search == "asteelscraps" or search == "asteel" or search == "ametalscraps":
        if item_ironscraps:
            menu:
                'You put a bunch of iron scraps on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "ironingot" or search == "steelingot" or search == "metalingot" or search == "theironingot" or search == "thesteelingot" or search == "themetalingot" or search == "aironingot" or search == "asteelingot" or search == "ametalingot":
        if item_ironingot:
            menu:
                'You put a bunch of iron ingot on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "goblinspear" or search == "goblinspear" or search == "speargoblin" or search == "goblinsspear" or search == "aspearofagoblin" or search == "thespearofagoblin" or search == "agoblinspear" or search == "thegoblinspear":
        if item_goblinspear:
            menu:
                'You put the goblin spear on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "trapdoorkey" or search == "dolmenkey" or search == "smallchapelkey" or search == "chapelkey" or search == "thetrapdoorkey" or search == "thedolmenkey" or search == "thechapelkey" or search == "atrapdoorkey" or search == "adolmenkey" or search == "achapelkey":
        if item_trapdoorkeydolmen:
            menu:
                'You place the key on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "asterionkey" or search == "asterionskey" or search == "theasterionkey" or search == "theasterionskey" or search == "anasterionkey" or search == "anasterionskey" or search == "aasterionkey" or search == "aasterionskey":
        if item_asterionkey:
            menu:
                'You place the key on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "largebronzekey" or search == "hugebronzekey" or search == "bronzekey" or search == "tunnelkey" or search == "oldtunnelkey" or search == "bronzegatekey" or search == "gatekey" or search == "thelargebronzekey" or search == "thehugebronzekey" or search == "thebronzekey" or search == "thetunnelkey" or search == "theoldtunnelkey" or search == "thebronzegatekey" or search == "thegatekey" or search == "alargebronzekey" or search == "ahugebronzekey" or search == "abronzekey" or search == "atunnelkey" or search == "aoldtunnelkey" or search == "abronzegatekey" or search == "agatekey":
        if item_oldtunnelkey:
            menu:
                'You place the key on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "smallkey" or search == "ironkey" or search == "storerroomkey":
        if item_oldtunnesmallkey:
            menu:
                'You place the key on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "watchtowerkey" or search == "keytowatchtower" or search == "thewatchtowerkey" or search == "thekeytowatchtower" or search == "awatchtowerkey" or search == "akeytowatchtower":
        if item_watchtowerkey:
            menu:
                'You place the key on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "beachkey" or search == "piershedkey" or search == "shedkey" or search == "keytotheshed" or search == "awatchtowerkey" or search == "akeytowatchtower":
        if item_piershedkey:
            menu:
                'You place the key on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "magicalamulets" or search == "myamulets" or search == "amulets" or search == "mageamulets" or search == "themagicalamulets" or search == "themyamulets" or search == "themageamulets" or search == "amagicalamulets" or search == "amyamulets" or search == "amageamulets":
        if item_mageamulets:
            menu:
                'Without the amulets, you won’t be able to reliably use magic. It’s too much of a risk.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "aweirdfruit" or search == "theweirdfruit" or search == "weirdfruit" or search == "themagicfruit" or search == "amagicfruit" or search == "magicfruit" or search == "magicalfruit" or search == "magicfruit" or search == "theseed":
        if item_magicfruit:
            menu:
                'You put the bone-like fruit back on the altar, but the tree doesn’t react.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "arope" or search == "rope" or search == "therope":
        if item_rope:
            menu:
                'You place the rope on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "asetofsauriansclaws" or search == "setofsauriansclaws" or search == "saurianclaws" or search == "sauriansclaw" or search == "saurianclaw" or search == "sauriansclaws" or search == "asetofdragonlingsclaws" or search == "setofdragonlingsclaws" or search == "dragonlingclaws" or search == "dragonlingsclaw" or search == "dragonlingclaw" or search == "dragonlingsclaws" or search == "thesetofsauriansclaws" or search == "thesetofsauriansclaws" or search == "thesaurianclaws" or search == "thesauriansclaw" or search == "thesaurianclaw" or search == "thesauriansclaws" or search == "theasetofdragonlingsclaws" or search == "thesetofdragonlingsclaws" or search == "thedragonlingclaws" or search == "thedragonlingsclaw" or search == "thedragonlingclaw" or search == "thedragonlingsclaws" or search == "asetofsauriansclaws" or search == "asaurianclaws" or search == "asauriansclaw" or search == "asaurianclaw" or search == "asauriansclaws" or search == "aasetofdragonlingsclaws" or search == "asetofdragonlingsclaws" or search == "adragonlingclaws" or search == "adragonlingsclaw" or search == "adragonlingclaw" or search == "adragonlingsclaws":
        if item_dragonlingclaws:
            menu:
                'You place the saurian’s claws on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "saurianspaw" or search == "saurianspaw" or search == "saurianpaw" or search == "saurianfingers" or search == "sauriansfingers" or search == "dragonlingspaw" or search == "dragonlingspaw" or search == "dragonlingpaw" or search == "dragonlingfingers" or search == "dragonlingsfingers" or search == "thesaurianspaw" or search == "thesaurianspaw" or search == "thesaurianpaw" or search == "thesaurianfingers" or search == "thesauriansfingers" or search == "thedragonlingspaw" or search == "thedragonlingspaw" or search == "thedragonlingpaw" or search == "thedragonlingfingers" or search == "thedragonlingsfingers" or search == "asaurianspaw" or search == "asaurianspaw" or search == "asaurianpaw" or search == "asaurianfingers" or search == "asauriansfingers" or search == "adragonlingspaw" or search == "adragonlingspaw" or search == "adragonlingpaw" or search == "adragonlingfingers" or search == "adragonlingsfingers":
        if item_dragonlingpaw:
            menu:
                'You place the dragonling’s paw on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "spices" or search == "sackofspices" or search == "thesacksofspices" or search == "sakcsofspices" or search == "spice" or search == "spiceset" or search == "spicesack":
        if item_spices:
            menu:
                'You put the spices on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "myherbs" or search == "asetofherbs" or search == "theasetofherbs" or search == "setofherbs" or search == "scholarherbs":
        if item_scholarherbs:
            menu:
                'You place your set of herbs on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "snakebait" or search == "eudociaflower" or search == "eudociasflower" or search == "serpentbait" or search == "thesnakebait" or search == "theeudociaflower" or search == "theeudociasflower" or search == "theserpentbait" or search == "asnakebait" or search == "aeudociaflower" or search == "aeudociasflower" or search == "aserpentbait":
        if item_snakebait:
            menu:
                'You put the flower on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "writinginstruments" or search == "writing" or search == "waxtablet" or search == "stylus" or search == "parchment" or search == "parchments" or search == "ink" or search == "mywritinginstruments" or search == "thewritinginstruments" or search == "thewriting" or search == "thewaxtablet" or search == "thestylus" or search == "theparchment" or search == "theparchments" or search == "theink" or search == "awritinginstruments" or search == "awriting" or search == "awaxtablet" or search == "astylus" or search == "aparchment" or search == "aparchments" or search == "anink":
        if item_writinginstruments:
            menu:
                'You place your set of writing instruments on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "wine" or search == "asterionswine" or search == "asterionsbottle" or search == "nightsbane" or search == "asterionswine" or search == "asterionsbottle" or search == "asterionwine" or search == "asterionbottle" or search == "nightbane" or search == "banenight" or search == "bane" or search == "expensivewine" or search == "thewine" or search == "theasterionswine" or search == "theasterionsbottle" or search == "thenightsbane" or search == "theasterionswine" or search == "theasterionsbottle" or search == "theasterionwine" or search == "theasterionbottle" or search == "thenightbane" or search == "thebanenight" or search == "thebane" or search == "theexpensivewine":
        if item_asterionwine:
            menu:
                'You put the bottle on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "spidersilk" or search == "spiderssilk" or search == "spiderweb" or search == "web" or search == "silk" or search == "thespidersilk" or search == "thespiderssilk" or search == "thespiderweb" or search == "theweb" or search == "thesilk" or search == "aspidersilk" or search == "aspiderssilk" or search == "aspiderweb" or search == "aweb" or search == "asilk":
        if item_spidersilk:
            menu:
                'You put the threads of spider silk on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    # elif search == "spidervenom" or search == "spidersvenom" or search == "thespidervenom" or search == "thespidersvenom":
    #     if item_spidervenom:
    #         menu:
    #             'You put the flask of spider venom on the altar, but nothing happens.
    #             '
    #             'I make an offering.':
    #                 python:
    #                     search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
    #                     search = search.strip().lower().replace(" ", "")
    #                     if not search:
    #                         search = "nothing"
    #                 jump interactaltarbeholder
    #             'I try something else.':
    #                 jump beholderaltar01
    #             'I walk away.':
    #                 jump beholderafterinteraction
    #     else:
    #         $ search = "zzz"
    #         jump interactaltarbeholder
    elif search == "shield" or search == "ashield" or search == "theshield" or search == "myshield":
        if item_shield:
            menu:
                'You put the shield on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "furlesswolf" or search == "furlesswolftrophy" or search == "thefurlesswolf" or search == "thefurlesswolftrophy" or search == "aheadofabeast" or search == "headofabeast" or search == "headofbeast" or search == "headbeast" or search == "beasthead" or search == "aheadofawolf" or search == "headofawolf" or search == "headofwolf" or search == "headwolf" or search == "wolfhead" or search == "wolftrophy":
        if item_furlesswolftrophy:
            menu:
                'You put the beast’s head on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "stoat" or search == "thedeadstoat" or search == "deadstoat" or search == "adeadstoat" or search == "stoatcarcass" or search == "stoatbody" or search == "stoatshell":
        if item_stoat:
            menu:
                'You put the dead stoat on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "boartusks" or search == "boartusk" or search == "boartusks" or search == "theboartusks" or search == "aboartusk" or search == "tusksboar" or search == "tusksofaboar" or search == "deadboar":
        if item_boartusks:
            menu:
                'You put the tusks of the boar on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "bonehook" or search == "bonehook" or search == "hookbones" or search == "boneshook" or search == "abonehook" or search == "thebonehook":
        if item_bonehook:
            menu:
                'You put the bone hook on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "crossbowquarrels" or search == "crossbowquarrels" or search == "thecrossbowquarrels" or search == "acrossbowquarrel" or search == "crossbowquarrel" or search == "quarrel" or search == "quarrels":
        if item_crossbowquarrels:
            menu:
                'You put a quarrel on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "ghoulblood" or search == "ghoulsblood" or search == "corpseeaterblood" or search == "corpseeatersblood" or search == "corpseeater" or search == "theghoulblood" or search == "theghoulsblood" or search == "thecorpseeaterblood" or search == "thecorpseeatersblood" or search == "thecorpseeater" or search == "aghoulblood" or search == "aghoulsblood" or search == "acorpseeaterblood" or search == "acorpseeatersblood" or search == "acorpseeater":
        if item_ghoulblood:
            menu:
                'You put the flask of corpse eater’s blood on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "marshbule" or search == "marshbules" or search == "amarshbule" or search == "themarshbules" or search == "fistfulofmarshbules":
        if item_marshbules:
            menu:
                'You put a few marshbules on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "bogmushroom" or search == "bogfriend" or search == "abogfriend" or search == "thebogfriend":
        if item_bogfriend:
            menu:
                'You put the bogfriend on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "basalt" or search == "basaltrock" or search == "powderedbasalt" or search == "powderedrock" or search == "abasalt" or search == "abasaltrock" or search == "apowderedbasalt" or search == "apowderedrock" or search == "thebasalt" or search == "thebasaltrock" or search == "thepowderedbasalt" or search == "thepowderedrock":
        if item_powderedrock or item_rocktobepowdered:
            menu:
                'You put the basalt on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "rareherbs" or search == "forestherbs" or search == "therareherbs" or search == "theforestherbs" or search == "acollectionofherbs":
        if item_shortcutherbs:
            menu:
                'You put the herbs on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "driftwood" or search == "thedriftwood" or search == "adriftwood":
        if item_driftwood:
            menu:
                'You put a piece of driftwood on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "cursedsoil" or search == "jarofcursedsoil" or search == "jarcursedsoil" or search == "thecursedsoil" or search == "thejarofcursedsoil" or search == "thejarcursedsoil" or search == "acursedsoil" or search == "ajarofcursedsoil" or search == "ajarcursedsoil":
        $ beholder_caneat_items = 1
        if item_cursedsoil:
            menu:
                'You open the jar and sprinkle some of the soil on the altar. The specks instantly get darker, but as you consider how little pneuma can be held by them, you realize you would have to bring here many carts of dirt to gather power comparable with a single magical potion.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "blackwoundwort" or search == "woundwort" or search == "theblackwoundwort" or search == "thewoundwort" or search == "ablackwoundwort" or search == "awoundwort":
        if item_blackwoundwort:
            menu:
                'You put the black woundwort on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "linen" or search == "linencloth" or search == "sheetsoflinencloth" or search == "astackoflinenfabric" or search == "stackoflinenfabric" or search == "stacklinenfabric" or search == "linenfabric" or search == "stackoffabric" or search == "stacklinen":
        if item_linen:
            menu:
                'You put the sheets of linen on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "awingedhourglass" or search == "wingedhourglass" or search == "thewingedhourglass" or search == "winged" or search == "wings" or search == "hourglass":
        if item_wingedhourglass:
            menu:
                'You place your winged hourglass on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "thaisletter" or search == "letterthais":
        if item_thaisletter or item_thaisletter_opened:
            menu:
                'You place the scroll on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "thetroll-bonetablet" or search == "thetrollbonetablet" or search == "troll-bonetablet" or search == "trollbonetablet" or search == "trollbone" or search == "trolltablet":
        if item_letterwhitemarshes:
            menu:
                'You place the troll-bone tablet on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    #################################### MAGICAL ITEMS
    elif search == "humanbones" or search == "humanbone" or search == "thehumanbones" or search == "ahumanbones" or search == "thehumanbone" or search == "pileofbones" or search == "pilesofbones" or search == "thepileofbones" or search == "stackofbones" or search == "stacksofbones" or search == "creeksbones" or search == "huntressbones":
        if item_pileofbones and not beholder_pileofbones:
            $ beholder_altar_awakened += 1
            $ beholder_pileofbones = 1
            menu:
                'You put the bones of a huntress on the altar. A few of them crack slightly, others get a tiny bit more yellow, and you think you hear the sound of a moving branch... But other than that, nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        elif item_pileofbones:
            menu:
                'You put the bones of a huntress on the altar, but nothing happens.
                '
                'I make an offering.':
                    python:
                        search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump interactaltarbeholder
                'I try something else.':
                    jump beholderaltar01
                'I walk away.':
                    jump beholderafterinteraction
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "abottlefromthedolmen" or search == "bottlefromthedolmen" or search == "bottlefromdolmen" or search == "bottlefromchapel" or search == "apotionfromthedolmen" or search == "potion fromthedolmen" or search == "potiondolmen" or search == "dolmenpotion" or search == "potiondolmen":
        if item_potiondolmen:
            jump altardonatingmagicitempotiondolmen
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "afreshhealingpotion" or search == "freshhealingpotion" or search == "newhealingpotion" or search == "anewhealingpotion" or search == "ahealingpotionfromthemonastery" or search == "ahealingpotionfrommonastery" or search == "healingpotionfrommonastery" or search == "ahealingpotionfromthemonastery":
        if item_generichealingpotion:
            jump altardonatingmagicitemgenerichealingpotion
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "asterionspotion" or search == "asterionpotion" or search == "asterionpotions" or search == "asterionspotions" or search == "theasterionpotion" or search == "aasterionpotion" or search == "asmallhealingpotion" or search == "smallhealingpotion" or search == "smallhealingpotions" or search == "atinyhealingpotion" or search == "tinyhealingpotion" or search == "tinyhealingpotions":
        if item_smallhealingpotion:
            jump altardonatingmagicitemsmallhealingpotion
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "sharpeningpoison" or search == "asharpeningpoison" or search == "thesharpeningpoison" or search == "sharpeningpoisons" or search == "sharpeningpotion" or search == "asharpeningpotion" or search == "thesharpeningpotion" or search == "sharpeningpotions" or search == "sharppoison" or search == "sharppotion" or search == "sharpdust" or search == "sharppowder":
        if item_sharpeningpotion:
            jump altardonatingmagicitemsharpeningpotion
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "magicpens" or search == "magicalpens" or search == "eudociapens" or search == "monkpens" or search == "monasterypens" or search == "magicquills" or search == "magicalquills" or search == "eudociaquills" or search == "monkquills" or search == "monasteryquills" or search == "magicalquill" or search == "eudociaquill" or search == "monkquill" or search == "monasteryquill" or search == "themagicpens" or search == "themagicalpens" or search == "theeudociapens" or search == "themonkpens" or search == "themonasterypens" or search == "themagicquills" or search == "themagicalquills" or search == "theeudociaquills" or search == "themonkquills" or search == "themonasteryquills" or search == "themagicalquill" or search == "theeudociaquill" or search == "themonkquill" or search == "themonasteryquill":
        if item_magicpens:
            jump altardonatingmagicitemmagicpens
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "bronzerod" or search == "bronzerods" or search == "golemwands" or search == "bronzerod" or search == "bronzerod" or search == "antennae" or search == "bronzerod" or search == "bronzerod" or search == "eudociasrods" or search == "eudociasrod" or search == "thebronzerod" or search == "thebronzerods" or search == "thegolemwands" or search == "thebronzerod" or search == "thebronzerod" or search == "abronzerod" or search == "abronzerods" or search == "agolemwands" or search == "abronzerod" or search == "abronzerod":
        if item_bronzerod:
            jump altardonatingmagicitembronzerod
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "cursedcoins" or search == "thecursedcoins" or search == "cursedcoin" or search == "acasketofcoins" or search == "casketofcoins" or search == "casketcoins" or search == "acasketofcoin" or search == "casketofcoin" or search == "casketcoin" or search == "acaskofcoins" or search == "caskofcoins" or search == "caskcoins" or search == "aboxofcoins" or search == "boxofcoins" or search == "boxcoins" or search == "navicabox" or search == "navicacoins" or search == "navicaitem" or search == "navicacurse":
        if item_casket:
            jump altardonatingmagicitemcasket
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "energystone" or search == "battery" or search == "magicalstone" or search == "manastone" or search == "spiritstone" or search == "soulstone" or search == "psychestone" or search == "pneumastone" or search == "thespiritstone" or search == "aspiritstone" or search == "energyrock" or search == "battery" or search == "magicalrock" or search == "manarock" or search == "spiritrock" or search == "soulrock" or search == "psycherock" or search == "pneumarock" or search == "thespiritrock" or search == "aspiritrock":
        if item_spiritrock:
            jump altardonatingmagicitemspiritrock
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "asterioncloak" or search == "asterionscloak" or search == "theasterioncloak" or search == "magicalcloak" or search == "magiccloak":
        if item_asterioncloak:
            jump altardonatingmagicitemasterioncloak
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "magicchisel" or search == "magicalchisel" or search == "themagicchisel" or search == "thechisel" or search == "achisel" or search == "chisel" or search == "thetoolofdestruction" or search == "toolofdestruction" or search == "tooldestruction" or search == "destructiontool" or search == "toolofdoom":
        if item_magicchisel:
            jump altardonatingmagicitemmagicchisel
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "golemglove" or search == "thegolemglove" or search == "thegolemhand" or search == "golemhand" or search == "eudociaglove" or search == "eudociasglove" or search == "rockglove" or search == "therockglove" or search == "stoneglove" or search == "thestoneglove":
        if item_golemglove:
            jump altardonatingmagicitemgolemglove
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "dragonhorn" or search == "thedragonhorn" or search == "adragonhorn" or search == "battlehorn" or search == "warhorn" or search == "thebattlehorn" or search == "thewarhorn" or search == "abattlehorn" or search == "awarhorn":
        if item_magicchisel:
            jump altardonatingmagicitemdragonhorn
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "plantacid" or search == "plantpoison" or search == "thewitheringdust" or search == "witheringdust" or search == "thewitheringdust" or search == "thewithering" or search == "awitheringdust" or search == "awithering":
        if item_witheringdust:
            jump altardonatingmagicitemwitheringdust
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    elif search == "blindingdust" or search == "blindingpowder" or search == "theblindingdust" or search == "theblindingpowder" or search == "ablindingdust" or search == "ablindingpowder" or search == "blinding":
        if item_blindingpowder:
            jump altardonatingmagicitemblindingpowder
        else:
            $ search = "zzz"
            jump interactaltarbeholder
    ####################################
    else:
        menu:
            'You either can’t do that, or you don’t possess such an item.
            '
            'I make an offering.':
                python:
                    search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump interactaltarbeholder
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction

label interactaltarbeholder_bug:
    menu:
        'You either can’t do that, or you don’t possess such an item.
        '
        'I make an offering.':
            python:
                search = renpy.input("What is your sacrifice?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            jump interactaltarbeholder
        'I try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction

label altardonatingmagicitempotiondolmen:
    menu:
        'You put the bottle on the altar and after a couple of breaths it starts to shake. Maybe you should pour out its contents.
        '
        'I spill the liquid on the altar.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I spill the liquid on the altar.')
            jump altardonatingmagicitempotiondolmen02
        'I take it back and try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction
label altardonatingmagicitempotiondolmen02:
    $ renpy.notify("You lost the potion.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a potion.{/i}')
    $ item_potiondolmen = 0
    $ quest_healingpotion_description04 = "I have lost the potion. I should speak with the merchant."
    if not beholder_altar_feeding_firstday:
        $ beholder_altar_feeding_firstday = day
    $ beholder_altar_feeding_lastday = day
    $ beholder_altar_awakened += 6
    if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The wind is moving the branches gently."
        show areapicture beholder02 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
        show areapicture beholder03 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
        show areapicture beholder04 at basicfade behind beholdercut
    elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
        $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
        show areapicture beholder05 at basicfade behind beholdercut
    elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
        $ beholder_fruit = 1
        $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
        show areapicture beholder06 at basicfade behind beholdercut
    else:
        $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
        if beholder_branch:
            show areapicture beholder07b at basicfade behind beholdercut
        else:
            show areapicture beholder07 at basicfade behind beholdercut
    menu:
        'The potion covers the altar, filling the air with the sweet smell of fruits and honey. The liquid sinks into the table before it gets to the edges.
        \n\nThe tree greets your offering with the sound of moving, stretching branches.
        '
        'I try something else.' if beholder_fruit != 1:
            if not beholder_caneat_items:
                $ beholder_caneat_items = 1
                $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                $ renpy.notify("Journal updated: Swamp Altar")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
            jump beholderaltar01
        'I walk away.' if beholder_fruit != 1:
            if not beholder_caneat_items:
                $ beholder_caneat_items = 1
                $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                $ renpy.notify("Journal updated: Swamp Altar")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
            jump beholderafterinteraction
        'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
            if not beholder_caneat_items:
                $ beholder_caneat_items = 1
                $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                $ renpy.notify("Journal updated: Swamp Altar")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
            jump beholderweirdfruit01

label altardonatingmagicitemgenerichealingpotion:
    menu:
        'You put the bottle on the altar and after a couple of breaths it starts to shake. Maybe you should pour out its contents.
        '
        'I spill the liquid on the altar.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I spill the liquid on the altar.')
            jump altardonatingmagicitemgenerichealingpotion02
        'I take it back and try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction
    label altardonatingmagicitemgenerichealingpotion02:
        $ renpy.notify("You lost a potion.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a potion.{/i}')
        $ item_generichealingpotion -= 1
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        $ beholder_altar_awakened += 6
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'The potion covers the altar, filling the air with the sweet smell of fruits and honey. The liquid sinks into the table before it gets to the edges.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderweirdfruit01

label altardonatingmagicitemsmallhealingpotion:
    menu:
        'You put the bottle on the altar and after a couple of breaths it starts to shake. Maybe you should pour out its contents.
        '
        'I spill the liquid on the altar.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I spill the liquid on the altar.')
            jump altardonatingmagicitemsmallhealingpotion02
        'I take it back and try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction
    label altardonatingmagicitemsmallhealingpotion02:
        $ renpy.notify("You lost a potion.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a potion.{/i}')
        $ item_smallhealingpotion -= 1
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        $ beholder_altar_awakened += 2
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'The potion covers the altar, filling the air with the sweet smell of exotic herbs. The liquid sinks into the table before it gets to the edges.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderweirdfruit01

label altardonatingmagicitemsharpeningpotion:
    menu:
        'You reach for the powder. As you move the bowl toward the altar, it starts to shake.
        '
        'I spread it on the altar.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I spill the liquid on the altar.')
            jump altardonatingmagicitemsharpeningpotion02
        'I take it back and try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction
    label altardonatingmagicitemsharpeningpotion02:
        $ renpy.notify("You lost a portion of the sharpening poison.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a portion of the sharpening poison.{/i}')
        $ item_sharpeningpotion -= 1
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        $ beholder_altar_awakened += 2
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'The dust bursts into a blue flame - but only for a heartbeat. It turns gray and stays warm for another minute.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderweirdfruit01

label altardonatingmagicitemmagicpens:
    menu:
        'As you move the quills toward the altar, you hear a gentle hiss.
        '
        'I place them anyway.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I place them anyway.')
            jump altardonatingmagicitemmagicpens
        'I take it back and try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction
    label altardonatingmagicitemmagicpens02:
        $ renpy.notify("You lost the quills.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the quills.{/i}')
        $ quest_pensformonastery_description02 = "I used the quills on the altar, feeding the mysterious tree with them. While it worked, they were completely destroyed in the process."
        $ item_magicpens -= 1
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        $ beholder_altar_awakened += 2
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'The quills sizzle and turn black and twisted, even though you don’t notice any sort of smoke.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderweirdfruit01

label altardonatingmagicitemcasket:
    $ item_casket = 0
    $ renpy.notify("You lost the casket.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the casket.{/i}')
    $ minutes += 1
    if pc_religion == "pagan":
        $ pc_faithpoints_opportunities += 1
    menu:
        'You open the box and pour out the coins onto the altar. You wait for a few good breaths - nothing seems to happen.
        '
        'I was meant to make sure no one is going to use these coins. I throw them into the smelly water.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I was meant to make sure no one is going to use these coins. I throw them into the smelly water.')
            $ quest_cursedcoins_description04 = 1 #1 - "I got rid of the coins for good. I should return to {color=#f6d6bd}Navica{/color}."
            if pc_religion != "pagan":
                $ custom1 = "The ring-shaped coins make brief splashes on impact, then sink slowly."
            else:
                $ pc_faithpoints += 1
                $ custom1 = "The ring-shaped coins make brief splashes on impact, then sink slowly. You think about your ancestors - it feels like you just took part in an ancient ritual."
            $ renpy.notify("Journal updated: The Cursed Coins.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Cursed Coins.{/i}')
            jump altardonatingmagicitemcasket02
        'I did my part. I’ll keep the coins for myself and will later lie to {color=#f6d6bd}Navica{/color} about them.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I did my part. I’ll keep the coins for myself and will later lie to {color=#f6d6bd}Navica{/color} about them.')
            $ quest_cursedcoins_description03 = 1 #1 - "I did as she asked, but the coins seem fine. I kept them to myself, and should now return to {color=#f6d6bd}Navica{/color}."
            $ coins += 15
            if pc_religion != "pagan":
                $ custom1 = "They rattle exactly the same as any other dragon bone. The casket will serve you as a container for a fragile bottle."
            else:
                $ pc_faithpoints -= 1
                $ custom1 = "They rattle exactly the same as any other dragon bone, even though you get the feeling of abandoning a sacred ritual. The casket will serve you as a container for a fragile bottle."
            show screen notifyimage( "Journal updated: The Cursed Coins.\n+15", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Cursed Coins. +15 {image=cointest}{/i}')
            jump altardonatingmagicitemcasket02
        'I add the coins to my own pouch and forget about this whole ordeal':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I add the coins to my own pouch and forget about this whole ordeal')
            $ quest_cursedcoins_description02 = 1 #1 - "I decided to keep the coins to myself, and to forget about the whole thing."
            $ coins += 15
            if pc_religion != "pagan":
                $ custom1 = "They rattle exactly the same as any other dragon bone. The casket will serve you as a container for a fragile bottle."
            else:
                $ pc_faithpoints -= 1
                $ custom1 = "They rattle exactly the same as any other dragon bone, even though you get the feeling of abandoning a sacred ritual. The casket will serve you as a container for a fragile bottle."
            $ quest_cursedcoins = 3
            show screen notifyimage( "Quest completed: The Cursed Coins.\n+15", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Cursed Coins. +15 {image=cointest}{/i}')
            label altardonatingmagicitemcasket02:
                menu:
                    '[custom1]
                    '
                    'I try something else.':
                        jump beholderaltar01
                    'I walk away.':
                        jump beholderafterinteraction

label altardonatingmagicitembronzerod:
    if not beholder_caneat_bronzerod:
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        $ beholder_altar_awakened += 1
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        $ item_bronzerod -= 1
        menu:
            'You put one of the rods on the altar and it suddenly starts to corrode, even though bronze hardly ever does so. Not only does it become green, it turns into dust.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                jump beholderweirdfruit01
    else:
        menu:
            'How many rods do you wish to sacrifice?
            '
            'One.' if item_bronzerod >= 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- One.')
                $ beholder_altar_awakened += 1
                $ item_bronzerod -= 1
                jump altardonatingmagicitembronzerod02a
            'Two.' if item_bronzerod >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Two.')
                $ beholder_altar_awakened += 2
                $ item_bronzerod -= 2
                jump altardonatingmagicitembronzerod02
            'Three.' if item_bronzerod >= 3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Three.')
                $ beholder_altar_awakened += 3
                $ item_bronzerod -= 3
                jump altardonatingmagicitembronzerod02
            'Four.' if item_bronzerod > 4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Four.')
                $ beholder_altar_awakened += 4
                $ item_bronzerod -= 4
                jump altardonatingmagicitembronzerod02
            'Five.' if item_bronzerod > 5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Five.')
                $ beholder_altar_awakened += 5
                $ item_bronzerod -= 5
                jump altardonatingmagicitembronzerod02
            '...all of them.' if item_bronzerod > 5:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- ...all of them.')
                $ beholder_altar_awakened += item_bronzerod
                $ item_bronzerod = 0
                jump altardonatingmagicitembronzerod02
            'I try something else.':
                jump beholderaltar01
            'I walk away.':
                jump beholderafterinteraction

    label altardonatingmagicitembronzerod02:
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
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'You put the rods on the altar and they suddenly start to corrode, even though bronze hardly ever does so. Not only do they become green, they turn into dust.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                jump beholderweirdfruit01

    label altardonatingmagicitembronzerod02a:
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'You put one of the rods on the altar and it suddenly starts to corrode, even though bronze hardly ever does so. Not only does it become green, it turns into dust.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                jump beholderweirdfruit01

label altardonatingmagicitemspiritrock:
    $ renpy.notify("You lost a spirit rock.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a spirit rock.{/i}')
    $ item_spiritrock -= 1
    if not beholder_altar_feeding_firstday:
        $ beholder_altar_feeding_firstday = day
    $ beholder_altar_feeding_lastday = day
    $ beholder_altar_awakened += 6
    if beholder_altar_awakened <= 2:
        $ beholder_fluff_tree = "The wind is moving the branches gently."
    if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The wind is moving the branches gently."
        show areapicture beholder02 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
        show areapicture beholder03 at basicfade behind beholdercut
    elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
        $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
        show areapicture beholder04 at basicfade behind beholdercut
    elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
        $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
        show areapicture beholder05 at basicfade behind beholdercut
    elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
        $ beholder_fruit = 1
        $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
        show areapicture beholder06 at basicfade behind beholdercut
    else:
        $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
        if beholder_branch:
            show areapicture beholder07b at basicfade behind beholdercut
        else:
            show areapicture beholder07 at basicfade behind beholdercut
    menu:
        'As soon as you lay it on the stone slab, the pebble hisses for less than a single breath, then shatters into dozens of tiny rocks, not much larger than grains of sand.
        \n\nThe tree greets your offering with the sound of moving, stretching branches.
        '
        'I try something else.' if beholder_fruit != 1:
            if not beholder_caneat_items:
                $ beholder_caneat_items = 1
                $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                $ renpy.notify("Journal updated: Swamp Altar")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
            jump beholderaltar01
        'I walk away.' if beholder_fruit != 1:
            if not beholder_caneat_items:
                $ beholder_caneat_items = 1
                $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                $ renpy.notify("Journal updated: Swamp Altar")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
            jump beholderafterinteraction
        'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
            jump beholderweirdfruit01

label altardonatingmagicitemasterioncloak:
    menu:
        'You grab Asterion’s cloak and as you gaze at the leaf-shaped decorations, you reflect on the potential worth of this delicate piece of clothing.
        '
        'I still do this.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still do this.')
            jump altardonatingmagicitemasterioncloak02
        'I take it back and try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction
    label altardonatingmagicitemasterioncloak02:
        $ renpy.notify("You lost Asterion’s cloak.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost Asterion’s cloak.{/i}')
        $ item_asterioncloak = 0
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        $ beholder_altar_awakened += 12
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'You place the cloak on the altar and, after a brief sizzling, the entire fabric bursts into green, blue, and purple flames. You step away, but after a couple of breaths, it’s already over. You see only dust.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                jump beholderweirdfruit01

label altardonatingmagicitemmagicchisel:
    menu:
        'As you bring the chisel closer to the altar, its trembling are much more noticeable. Your hand gets uncomfortably warm.
        '
        'I drop it on the altar.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop it on the altar.')
            jump altardonatingmagicitemaltardonatingmagicitemmagicchisel02
        'I take it back and try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction
    label altardonatingmagicitemaltardonatingmagicitemmagicchisel02:
        if item_magicchisel == 2:
            $ beholder_altar_awakened += 12
            $ renpy.notify("You lost The Tool of Destruction.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost The Tool of Destruction.{/i}')
        elif item_magicchisel == 1:
            $ beholder_altar_awakened += 8
            $ renpy.notify("You lost the magic chisel.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the magic chisel.{/i}')
        $ item_magicchisel = 0
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'The chisel starts to shake, jumping on the stone like a fish in pain. In less than a minute it turns orange, then red, and you consider pushing it away with a stick, before it covers the altar with melted iron, then turns into dark dust.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                jump beholderweirdfruit01

label altardonatingmagicitemdragonhorn:
    menu:
        'As you move the horn closer to the altar, it makes a gentle, weak whine. Your hand gets uncomfortably warm.
        '
        'I drop it on the altar.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop it on the altar.')
            jump altardonatingmagicitemdragonhorn02
        'I take it back and try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction
    label altardonatingmagicitemdragonhorn02:
        $ beholder_altar_awakened += 8
        $ item_dragonhorn = 0
        $ renpy.notify("You lost the dragon horn.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the dragon horn.{/i}')
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'It starts to shake. The hoops turn orange, then red, then they break. The horn soon follows, turning into a small pile of glassy shards.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                jump beholderweirdfruit01

label altardonatingmagicitemgolemglove:
    menu:
        'As you move the glove closer to the altar, its rocks are pressing against each other, like a pack of terrified goblins.
        '
        'I drop it on the altar.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop it on the altar.')
            jump altardonatingmagicitemgolemglove02
        'I take it back and try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction
    label altardonatingmagicitemgolemglove02:
        $ beholder_altar_awakened += 10
        $ item_golemglove = 0
        $ renpy.notify("You lost The Golem Glove.\nJournal updated: Explore the Peninsula")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost The Golem Glove. Journal updated: Explore the Peninsula{/i}')
        $ quest_explorepeninsula_description15b = "I sacrificed The Golem Glove. The officials will have to trust my word."
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'The rocks get warm and start to crack, letting out weak hiss. After a few breaths, all that’s left of the golem hand is a pile of dust.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                jump beholderweirdfruit01

label altardonatingmagicitemwitheringdust:
    menu:
        'You raise the bag in front of you, and realize that if anything happens to it, you may not ever get a new supply of the withering dust.
        '
        'Yes.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Yes.')
            jump altardonatingmagicitemwitheringdust02
        'I take it back and try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction
    label altardonatingmagicitemwitheringdust02:
        $ item_witheringdust -= 1
        $ renpy.notify("You lost the withering dust.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the withering dust.{/i}')
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        $ beholder_altar_awakened += 3
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'You spread the magical mixture on the altar, and as soon as it hits the stone, it starts to sizzle and turn into ash.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                jump beholderweirdfruit01

label altardonatingmagicitemblindingpowder:
    menu:
        'You raise the satchel in front of you, and realize that if anything happens to it, you may not ever get a new supply of the blinding powder.
        '
        'Yes.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Yes.')
            jump altardonatingmagicitemblindingpowder02
        'I take it back and try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction
    label altardonatingmagicitemblindingpowder02:
        $ item_blindingpowder -= 1
        $ renpy.notify("You lost the blinding powder.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the blinding powder.{/i}')
        if not beholder_altar_feeding_firstday:
            $ beholder_altar_feeding_firstday = day
        $ beholder_altar_feeding_lastday = day
        $ beholder_altar_awakened += 10
        if beholder_altar_awakened <= 2:
            $ beholder_fluff_tree = "The wind is moving the branches gently."
        if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The wind is moving the branches gently."
            show areapicture beholder02 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
            show areapicture beholder03 at basicfade behind beholdercut
        elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
            $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
            show areapicture beholder04 at basicfade behind beholdercut
        elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
            $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
            show areapicture beholder05 at basicfade behind beholdercut
        elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
            $ beholder_fruit = 1
            $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
            show areapicture beholder06 at basicfade behind beholdercut
        else:
            $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
            if beholder_branch:
                show areapicture beholder07b at basicfade behind beholdercut
            else:
                show areapicture beholder07 at basicfade behind beholdercut
        menu:
            'You spread the magical mixture on the altar, and as soon as it hits the stone, it starts to sizzle and turn black.
            \n\nThe tree greets your offering with the sound of moving, stretching branches.
            '
            'I try something else.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderaltar01
            'I walk away.' if beholder_fruit != 1:
                if not beholder_caneat_items:
                    $ beholder_caneat_items = 1
                    $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
                    $ renpy.notify("Journal updated: Swamp Altar")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
                jump beholderafterinteraction
            'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
                jump beholderweirdfruit01

label beholderaltarblooddonationnotneeded:
    menu:
        'The tree is already fully grown. There is no need to spill more blood.
        '
        'I try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction

label beholderaltarmagicdonationnotneeded:
    menu:
        'The tree is already fully grown. There is no need to exhaust your pneuma.
        '
        'I try something else.':
            jump beholderaltar01
        'I walk away.':
            jump beholderafterinteraction

#### SACRIFICING A MAGICAL ITEM, TEMPLATE
# label altardonatingmagicitemNAMEOFTHEITEM:
# menu:
#     'FLUFF THAT IS MEANT TO MAKE SURE THAT THE PLAYER REALY WANTS TO DO IT
#     '
#     'Yes.':
#         $ narrator.add_history(kind='nvl', who=narrator.name, what='- Yes.')
#         jump altardonatingmagicitemNAMEOFTHEITEM02
#     'I take it back and try something else.':
#         jump beholderaltar01
#     'I walk away.':
#         jump beholderafterinteraction
# label altardonatingmagicitemNAMEOFTHEITEM02:
# $ item_ITEM -= 1
# $ renpy.notify("You lost the NAME OF THE ITEM.")
# $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost the NAME OF THE ITEM.{/i}')
# if not beholder_altar_feeding_firstday:
#     $ beholder_altar_feeding_firstday = day
# $ beholder_altar_feeding_lastday = day
# $ beholder_altar_awakened += X
# if beholder_altar_awakened <= 2:
#     $ beholder_fluff_tree = "The wind is moving the branches gently."
# if (beholder_altar_awakened <= 6 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 5 and difficultypick_advanced_questseasier):
#     $ beholder_fluff_tree = "The wind is moving the branches gently."
#     show areapicture beholder02 at basicfade behind beholdercut
# elif (beholder_altar_awakened <= 12 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 10 and difficultypick_advanced_questseasier):
#     $ beholder_fluff_tree = "The tree is moving slowly and some of the branches are now visibly longer."
#     show areapicture beholder03 at basicfade behind beholdercut
# elif (beholder_altar_awakened <= 18 and not difficultypick_advanced_questseasier) or (beholder_altar_awakened <= 15 and difficultypick_advanced_questseasier):
#     $ beholder_fluff_tree = "The tree branches and roots are moving slowly, in a way that can’t be justified solely by the wind."
#     show areapicture beholder04 at basicfade behind beholdercut
# elif beholder_altar_awakened <= beholder_altar_awakened_threshold:
#     $ beholder_fluff_tree = "The tree branches are now much longer and they keep swinging gently. More and more roots break through the water surface."
#     show areapicture beholder05 at basicfade behind beholdercut
# elif beholder_altar_awakened > beholder_altar_awakened_threshold and not beholder_fruit:
#     $ beholder_fruit = 1
#     $ beholder_fluff_tree = "The tree is now visibly taller and it has grown a weird, pale fruit. However, it doesn’t move anymore."
#     show areapicture beholder06 at basicfade behind beholdercut
# else:
#     $ beholder_fluff_tree = "The tree is now visibly taller and wider, but it doesn’t move anymore."
#     if beholder_branch:
#         show areapicture beholder07b at basicfade behind beholdercut
#     else:
#         show areapicture beholder07 at basicfade behind beholdercut
# menu:
#     'XX
#     \n\nThe tree greets your offering with the sound of moving, stretching branches.
#     '
#     'I try something else.' if beholder_fruit != 1:
#         if not beholder_caneat_items:
#             $ beholder_caneat_items = 1
#             $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
#             $ renpy.notify("Journal updated: Swamp Altar")
#             $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
#         jump beholderaltar01
#     'I walk away.' if beholder_fruit != 1:
#         if not beholder_caneat_items:
#             $ beholder_caneat_items = 1
#             $ quest_swampaltar_description03 = "The tree can “drain” magical power from various items, which results in their destruction."
#             $ renpy.notify("Journal updated: Swamp Altar")
#             $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Swamp Altar{/i}')
#         jump beholderafterinteraction
#     'I approach the weird fruit that has suddenly appeared.' if beholder_fruit == 1:
#         $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the weird fruit that has suddenly appeared.')
#         jump beholderweirdfruit01
