########################################### HUNTER CABIN
default huntercabin_firsttime = 0
default huntercabin_fluff = ""
default huntercabin_fluff_old = ""
default huntercabin_spider_seen = 0
default huntercabin_inside = 0
default huntercabin_inside_webremoved = 0
default huntercabin_inside_searched = 0

default huntercabin_spider_defeated = 0
default huntercabin_spider_defeated_bybandit = 0
default huntercabin_spider_removed = 0
default huntercabin_spider_pchurt = 0

default huntercabin_spider_smallspiders_killed = 0
default huntercabin_spider_smallspiders_letgo = 0

default huntercabin_listened = 0
default huntercabin_crossbow = 0
default huntercabin_wand = 0
default huntercabin_shield = 0
default huntercabin_noaxe = 0
default huntercabin_restored = 0
default huntercabin_knife = 0

label huntercabin01:
    nvl clear
    $ pc_area = "huntercabin"
    stop music fadeout 4.0
    play nature "audio/ambient/huntercabin01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture huntercabin01 behind spider at basicfade
    label huntercabin_fluffloop:
        $ huntercabin_fluff = renpy.random.choice(['Two pigeons fly off the roof and disappears above the cliff.', 'The nearby flowers are crowded with humming bees.', 'You notice prints of hooves and clawed paws. The pack was fleeing down the road.', 'Termites are climbing the wooden beam that supports the roof. It seems to be their home.', 'A loud roar comes from the west, causing the birds to burst into the sky loudly. From here, you don’t see the battling beasts.'])
        if huntercabin_fluff_old == huntercabin_fluff:
            jump huntercabin_fluffloop
        else:
            $ huntercabin_fluff_old = huntercabin_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if huntercabin_firsttime < 2:
        $ world_known_npcs += 0
        $ world_known_areas += 1
        $ huntercabin_firsttime = 2
        $ stonebridge_unlocked = 1
        $ foragingground_unlocked = 1
        jump huntercabinfirsttime01
    else:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if shortcut_darkforest_bandit_toldabouthuntercabin < day and shortcut_darkforest_bandit_toldabouthuntercabin and not shortcut_darkforest_bandit_killed:
            if not huntercabin_spider_defeated:
                $ huntercabin_spider_defeated = 1
                $ huntercabin_spider_defeated_bybandit = 1
            if not huntercabin_spider_removed:
                $ huntercabin_spider_removed = 1
            if not huntercabin_inside_webremoved:
                $ huntercabin_inside_webremoved = 1
        jump huntercabinregular01

label huntercabinfirsttime01:
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if persistent.deafmode:
        $ deafcustom1 = "The chirping of insects is rarely interrupted by a cackle of a distant bird, and just as often by the thunderous roar of the woodland beasts. The only tracks in sight belong to small critters."
    else:
        $ deafcustom1 = "The only tracks in sight belong to small critters."
    menu:
        '[deafcustom1] The cabin has no window, but a stubborn beast could easily burst in through the old thatch.
        \n\nThe gust of wind doesn’t move the door. A curious ibex observes you from the crag, but flees from your gaze.
        '
        'I check on the cabin.' if not huntercabin_inside:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check on the cabin.')
            $ huntercabin_inside = 1
            jump huntercabin_insidefirsttime01
        'I enter the cabin.' if huntercabin_inside:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cabin.')
            if not huntercabin_spider_defeated:
                jump huntercabin_insidefirsttime01b
            else:
                jump huntercabin_insideregular01

label huntercabinregular01:
    if not huntercabin_noaxe:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
    else:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '[huntercabin_fluff]
        '
        'I check on the cabin.' if not huntercabin_inside:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check on the cabin.')
            $ huntercabin_inside = 1
            jump huntercabin_insidefirsttime01
        'I enter the cabin.' if huntercabin_inside:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cabin.')
            if not huntercabin_spider_defeated:
                jump huntercabin_insidefirsttime01b
            else:
                jump huntercabin_insideregular01
        'I lost my axe during the fight. I should take it back. (disabled)' if huntercabin_noaxe:
            pass

label huntercabin_insidefirsttime01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ minutes += 5
    if quarters < (world_daylength-6):
        $ custom1 = "Its curious eyes are tracking the crickets that jump among the grass blades."
    elif quarters >= (world_daylength-6) and pc_likeshorsename:
        $ custom1 = "It looks around anxiously. You pat its side, but without much conviction. It’s getting dark."
    else:
        $ custom1 = "It looks around anxiously. It’s getting dark."
    menu:
        'You tether {color=#f6d6bd}[horsename]{/color} to the supporting beam. [custom1]
        \n\nYou stretch your limbs, adjust your armor, and reach for the axe.
        '
        'I burst in.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I burst in.')
            jump huntercabin_insidefirsttime02
        'Let’s eavesdrop first.':
            $ huntercabin_listened = 1
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s eavesdrop first.')
            jump huntercabin_insidefirsttime01b

label huntercabin_insidefirsttime01b:
    $ at = 0
    if pc_class == "mage":
        $ at_unlock_spell = 1
        $ manacost = 3
    menu:
        'You sneak toward the door and crouch down. After maybe a minute, a quiet rattle comes from the inside, something similar to the sound of cracking knuckles.
        \n\nYou peek inside and just barely see a small part of the dusty room. A large spider web is spread among the knocked-down furniture.
        '
        'I better grab my wand. [[Cost: {color=#f6d6bd}[manacost]{/color}]' ( condition="at == 'spell'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I better grab my wand.')
            $ at_unlock_spell = 0
            $ huntercabin_wand = 1
            menu:
                'You unwrap the linen sheet and grab the willow wand, still as smooth as on the day you bought it. The pointy, carved twig is thin, but heavy from the injected quicksilver.
                '
                'I walk in and aim at anything that moves.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk in and aim at anything that moves.')
                    jump huntercabin_insidefirsttime02
        'My pneuma is too weak to cast spells in combat. [[Cost: [manacost]] (disabled)] (disabled)' ( condition="at != 'spell' and pc_class == 'mage' and mana < manacost" ):
            pass
        'I may need my crossbow.' if item_crossbow and item_crossbowquarrels:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I may need my crossbow.')
            $ at_unlock_spell = 0
            $ huntercabin_crossbow = 1
            menu:
                'You remove its protective case and plant the stirrup on the ground. You take a deep breath, pull the string until it locks, then load the quarrel.
                '
                'I walk in and aim at anything that moves.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk in and aim at anything that moves.')
                    jump huntercabin_insidefirsttime02
        'I don’t have any quarrels for my crossbow.' if item_crossbow and not item_crossbowquarrels:
            pass
        'I don’t have a crossbow. (disabled)' if not item_crossbow:
            pass
        'I grab my axe and get inside.' if not item_shield:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my axe and get inside.')
            $ at_unlock_spell = 0
            jump huntercabin_insidefirsttime02
        'I grab my axe and raise my shield. Let’s get inside.' if item_shield:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I grab my axe and raise my shield. Let’s get inside.')
            $ at_unlock_spell = 0
            $ huntercabin_shield = 1
            jump huntercabin_insidefirsttime02
        'I should leave.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should leave.')
            $ at_unlock_spell = 0
            jump huntercabinoutsideafterinteraction01

label huntercabin_insideregular01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 1
    if huntercabin_spider_defeated and not huntercabin_spider_removed and not huntercabin_restored:
        show spider huntercabin at basicfade
    if not shortcut_darkforest_bandit_leftTOpeltnorth and shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_killed < day and not shortcut_darkforest_bandit_killedspiderpcknows:
        $ shortcut_darkforest_bandit_killedspiderpcknows = 1
        $ huntercabin_restored = 0
        show areapicture huntercabin_inside02 behind spider at basicfade
        menu:
            '{color=#f6d6bd}The man without a name{/color} is no longer here, and neither are his belongings. The floor is covered with stains of blood, scraps of fabric, and overturned furniture.
            '
            'I leave the building.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
                jump huntercabinoutsideafterinteraction01
    elif (shortcut_darkforest_bandit_toldabouthuntercabin+3) < day and shortcut_darkforest_bandit_toldabouthuntercabin and not shortcut_darkforest_bandit_leftthepeninsula and not shortcut_darkforest_bandit_leftTOpeltnorthpcknows and not shortcut_darkforest_bandit_killed:
        $ shortcut_darkforest_bandit_leftTOpeltnorthpcknows = 1
        $ shortcut_darkforest_bandit_leftTOpeltnorth = 1
        $ huntercabin_restored = 1
        show areapicture huntercabin_inside03 behind spider at basicfade
        hide spider
        menu:
            '{color=#f6d6bd}The man without a name{/color} left behind a wooden bowl with a roasted bird wing, fresh berries, hazelnuts, and two wild carrots. All of them untouched.
            '
            'I sit down and enjoy the food.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit down and enjoy the food.')
                $ quarters += 1
                $ pc_food = limit_pc_food(pc_food+2)
                show plus2food at foodchange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 nourishment points.{/i}')
                menu:
                    'The table doesn’t stick to your fingers, so you decide to rest your elbows. The meal is alright - some gruel would go well with it.
                    '
                    'Once I’m done, I leave the building.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- Once I’m done, I leave the building.')
                        jump huntercabinoutsideafterinteraction01
            'It could be poisoned. I throw the bowl outside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It could be poisoned. I throw the bowl outside.')
                $ minutes += 5
                hide spider
                show areapicture huntercabin01 behind spider at basicfade
                menu:
                    'You put on your protective glove and take the meal on the other side of the road, then cast it into the woods, scattering it for the rats and ants.
                    '
                    'I walk away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                        jump huntercabinoutsideafterinteraction01
    elif shortcut_darkforest_bandit_toldabouthuntercabin < day and shortcut_darkforest_bandit_toldabouthuntercabin and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_leftTOpeltnorth and not shortcut_darkforest_bandit_leftthepeninsula:
        $ huntercabin_restored = 1
        show areapicture huntercabin_inside03 behind spider at basicfade
        hide spider
        if not shortcut_darkforest_bandit_huntercabin_firsttime:
            $ shortcut_darkforest_bandit_huntercabin_firsttime = 1
            if huntercabin_spider_seen and not quest_easternpath_description05:
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description05 = "The spider from the cabin is gone."
            if huntercabin_spider_defeated_bybandit:
                $ shortcut_darkforest_bandit_huntercabin_fluff = "You hear the voice of the man whom you encountered in the heart of the forest. He’s standing right in the corner, holding a raised dagger. “Right, looks like we’re both alive,” he lowers his shoulders and clears his throat nervously. “I better memorize the sound of your horse.” He hides the blade. “I got spooked here by a spider, but I took care of it.”"
            else:
                $ shortcut_darkforest_bandit_huntercabin_fluff = "You hear the voice of the man whom you encountered in the heart of the forest. He’s standing right in the corner, holding a raised dagger. “Right, looks like we’re both alive,” he lowers his shoulders and clears his throat nervously. “I better memorize the sound of your horse.” He hides the blade."
        else:
            label shortcut_darkforest_bandit_huntercabin_fluffloop:
                $ shortcut_darkforest_bandit_huntercabin_fluff = renpy.random.choice(['{color=#f6d6bd}The man without a name{/color} is sharpening a curved dagger used for shaving. He doesn’t look at you. “What brings you here?”', '{color=#f6d6bd}The man without a name{/color} is plucking the feathers from a dead pigeon. He doesn’t look at you. “Stranger?”', '{color=#f6d6bd}The man without a name{/color} is washing his gambeson. He doesn’t look at you.', '{color=#f6d6bd}The man without a name{/color} is sitting on the floor, lost in his thoughts. When he glances at you, his eyes are absent.'])
                if shortcut_darkforest_bandit_huntercabin_fluff_old == shortcut_darkforest_bandit_huntercabin_fluff:
                    jump shortcut_darkforest_bandit_huntercabin_fluffloop
                else:
                    $ shortcut_darkforest_bandit_huntercabin_fluff_old = shortcut_darkforest_bandit_huntercabin_fluff
        menu:
            '[shortcut_darkforest_bandit_huntercabin_fluff]
            '
            '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                $ shortcut_darkforest_bandit_about_reward = 1
                jump huntercabin_insidebanditaboutreward01
            '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                $ shortcut_darkforest_bandit_about_corpse = 2
                $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                jump huntercabin_insidebanditaboutcorpse01
            '“Are you planning to stay here for long?”' if not shortcut_darkforest_bandit_about_stayingaround:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                $ shortcut_darkforest_bandit_about_stayingaround = 1
                jump huntercabin_insidebanditaboutstayingaround01
            '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                $ shortcut_darkforest_bandit_about_questions = 1
                jump huntercabin_insidebanditaboutquestions01
            '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump huntercabin_insidebanditconfrontedaboutglauciasquest01
            '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                $ custom1 = "He takes a deep breath and keenly observes your lips."
                jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
            '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump huntercabin_insidebanditconfrontedaboutglauciasquest02
            'I bid farewell to him.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bid farewell to him.')
                jump huntercabinoutsideafterinteraction01
    else:
        if huntercabin_restored:
            show areapicture huntercabin_inside03 behind spider at basicfade
        elif not huntercabin_inside_webremoved:
            show areapicture huntercabin_inside01 behind spider at basicfade
        else:
            show areapicture huntercabin_inside02 behind spider at basicfade
        menu:
            'You step through the threshold.
            '
            'I search the building.' if huntercabin_inside_webremoved and not huntercabin_inside_searched:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the building.')
                $ quarters += 1
                jump huntercabin_insidesearch01
            'I drag the spider carcass away and throw it into the forest.' if not huntercabin_spider_removed:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drag the spider carcass away and throw it into the forest.')
                $ huntercabin_spider_removed = 1
                $ minutes += 5
                jump huntercabinremovingspider01
            'I can’t search the building with this spiderweb around. (disabled)' if not huntercabin_inside_webremoved:
                pass
            'I don’t have much time. I light up a candle and melt the web.' if not huntercabin_inside_webremoved:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have much time. I light up a candle and melt the web.')
                $ minutes += 5
                $ huntercabin_inside_webremoved = 1
                jump huntercabinwebburned01
            'Someone could be interested in such a thick web. I spend an hour or so gathering it.' if not huntercabin_inside_webremoved:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone could be interested in such a thick web. I spend an hour or so gathering it.')
                $ quarters += 4
                $ huntercabin_inside_webremoved = 1
                jump huntercabinwebgathered01
            'I leave the building.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
                jump huntercabinoutsideafterinteraction01

label huntercabinoutsideafterinteraction01:
    if not huntercabin_noaxe:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
    else:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 1
    hide spider
    show areapicture huntercabin01 behind spider at basicfade
    if quarters < (world_daylength-6):
        $ custom1 = "is peacefully grazing on the grass"
    elif quarters >= (world_daylength-6) and pc_likeshorsename:
        $ custom1 = "observes the area nervously. You pat its side, but without much conviction. It’s getting dark"
    else:
        $ custom1 = "observes the area nervously. It’s getting dark"
    menu:
        '{color=#f6d6bd}[horsename]{/color} [custom1].
        '
        'I check on the cabin.' if not huntercabin_inside:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check on the cabin.')
            $ huntercabin_inside = 1
            jump huntercabin_insidefirsttime01
        'I enter the cabin.' if huntercabin_inside:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cabin.')
            if not huntercabin_spider_defeated:
                jump huntercabin_insidefirsttime01b
            else:
                jump huntercabin_insideregular01
        'I lost my axe during the fight. I should take it back. (disabled)' if huntercabin_noaxe:
            pass

label huntercabinwebburned01:
    show areapicture huntercabin_inside02 behind spider at basicfade
    if huntercabin_spider_defeated and not huntercabin_spider_removed:
        show spider huntercabin at basicfade
    if huntercabin_noaxe:
        $ custom1 = "In the meantime, you recover your lost axe."
    else:
        $ custom1 = ""
    $ huntercabin_noaxe = 0
    menu:
        'You unpack a candle and your tinderbox, then sit on the ground and prepare the flint and the linen char cloth. Decades ago, before The Southern Invasion, people used fire strikers made of thick steel, but all you have is a cube-like piece of harsh pyrite. It’s not the best, but enough to make a couple of sparks.
        \n\nHolding the copper candle holder, you approach the spiderwebs. It doesn’t take long - the isolated threads of silk melt as quickly as human hair. And smell just as bad. You remove the strategic spots, letting the web fall on the floor. [custom1]
        \n\nYou notice maybe a dozen defenseless spiderlings. They flee toward the exit, with their speed limited by their tiny legs. They’re smaller than a finger.
        '
        'I trample them with my boot.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I trample them with my boot.')
            jump huntercabinspiderstrampled01
        'They have the right to live.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- They have the right to live.')
            $ achievement_animalssavedpoints += 1
            jump huntercabinspidersescaped01

label huntercabinwebgathered01:
    show areapicture huntercabin_inside02 behind spider at basicfade
    if huntercabin_spider_defeated and not huntercabin_spider_removed:
        show spider huntercabin at basicfade
    if huntercabin_noaxe:
        $ custom1 = "In the meantime, you recover your lost axe."
    else:
        $ custom1 = ""
    $ huntercabin_noaxe = 0
    $ item_spidersilk = 1
    $ renpy.notify("You gathered a spool of spider silk.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gathered a spool of spider silk.{/i}')
    menu:
        'You bring a twig from the outside and use it as a spool. You don’t have much practice and wearing the gloves makes the necessary gestures even more awkward. From time to time the silk breaks, but it shouldn’t be a problem for a tailor - it’s a material for stitching, and wouldn’t be turned into a cloth anyway. [custom1]
        \n\nYou notice maybe a dozen defenseless spiderlings. They flee toward the exit, with their speed limited by their tiny legs. They’re smaller than a finger.
        '
        'I trample them with my boot.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I trample them with my boot.')
            jump huntercabinspiderstrampled01
        'They have the right to live.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- They have the right to live.')
            jump huntercabinspidersescaped01

label huntercabinspiderstrampled01:
    $ huntercabin_spider_smallspiders_killed = 1
    menu:
        'On their death they make a squish.
        '
        'I search the building.' if huntercabin_inside_webremoved and not huntercabin_inside_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the building.')
            $ quarters += 1
            jump huntercabin_insidesearch01
        'I drag the spider carcass away and throw it into the forest.' if not huntercabin_spider_removed:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drag the spider carcass away and throw it into the forest.')
            $ huntercabin_spider_removed = 1
            $ minutes += 5
            jump huntercabinremovingspider01
        'I leave the building.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
            jump huntercabinoutsideafterinteraction01

label huntercabinspidersescaped01:
    $ huntercabin_spider_smallspiders_letgo = 1
    menu:
        'The creatures crawl over the threshold and disappear among the grass blades. It could be the first time they’ve ever been touched by the sun.
        '
        'I search the building.' if huntercabin_inside_webremoved and not huntercabin_inside_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the building.')
            $ quarters += 1
            jump huntercabin_insidesearch01
        'I drag the spider carcass away and throw it into the forest.' if not huntercabin_spider_removed:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drag the spider carcass away and throw it into the forest.')
            $ huntercabin_spider_removed = 1
            $ minutes += 5
            jump huntercabinremovingspider01
        'I leave the building.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
            jump huntercabinoutsideafterinteraction01

label huntercabin_insidesearch01:
    $ huntercabin_inside_searched = 1
    $ item_crossbowquarrels += 2
    $ renpy.notify("You picked up 2 quarrels.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You picked up 2 quarrels{/i}')
    menu:
        'The chest hides a few old water skins and inedible, stale rations. Among them, however, you find two quarrels for a crossbow.
        \n\nThe bones have no obvious owner, but judging by their age and the lack of skull or human-like hands, you doubt they could be awoken by the fogs. The boots, rugged pants, an old, sticky tunic, and other scraps are cheap, and hide no jewelry. The bowls and mugs are empty.
        '
        'I drag the spider carcass away and throw it into the forest.' if not huntercabin_spider_removed:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drag the spider carcass away and throw it into the forest.')
            $ huntercabin_spider_removed = 1
            $ minutes += 5
            jump huntercabinremovingspider01
        'I leave the building.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
            jump huntercabinoutsideafterinteraction01

label huntercabinremovingspider01:
    if not huntercabin_noaxe:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
    else:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 1
    hide spider
    show areapicture huntercabin01 behind spider at basicfade
    menu:
        'You put on your thick gloves and grab four spider legs at once. The corpse isn’t heavy, so you drag it behind you.
        \n\nYou reach the bushes at the edge of the road, then lift up the entire creature. The more you shake it, the more distracting the twitches of its legs get.
        \n\nYou send it into a tree trunk. It sinks into the thicket, causing a bit of a rustle among the dwellers.
        '
        'I check on the cabin.' if not huntercabin_inside:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check on the cabin.')
            $ huntercabin_inside = 1
            jump huntercabin_insidefirsttime01
        'I enter the cabin.' if huntercabin_inside:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cabin.')
            if not huntercabin_spider_defeated:
                jump huntercabin_insidefirsttime01b
            else:
                jump huntercabin_insideregular01
        'I lost my axe during the fight. I should take it back. (disabled)' if huntercabin_noaxe:
            pass

label huntercabin_insidefirsttime02:
    $ renpy.save("combatsave", extra_info='Combat Auto Save')
    show areapicture huntercabin_inside01 behind spider at basicfade
    if not renpy.music.get_playing(channel='music') == "<loop 32.0>audio/track_15battletheme.ogg":
        play music "<loop 32.0>audio/track_15battletheme.ogg" fadeout 1.0 fadein 1.0
    stop nature fadeout 2.0
    $ huntercabin_spider_seen = 1
    menu:
        'A spider looks at you from the center of the web. Its shell is larger than your head, and the thin legs are longer than your arms. Its countless “hair” blends in with the walls: they’re brown, gray, cream.
        \n\nWhat do you do?
        '
        'Let me think...':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me think...')
            if not tutorial_input:
                $ tutorial_input = 1
            python:
                search = renpy.input("What do you try to do? (example: kick)", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            $ tutorial_input = 2
            jump huntercabinbattle01

label huntercabinbattle01:
    if search == "nothing" or search == "none" or search == "something" or search == "anything" or search == "whatever" or search == " ":
        menu:
            'Are you sure that you don’t want to do anything specific?
            '
            'I try something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump huntercabinbattle01
            'I’m sure.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m sure.')
                label huntercabinbattlewait01:
                    hide areapicture
                    if pc_class == "warrior":
                        $ at_unlock_force = 1
                        $ at = 0
                    if pc_class == "scholar":
                        $ at_unlock_knowledge = 1
                        $ at = 0
                    menu:
                        'The spider doesn’t wait for you. It leans forward silently, shaking the entire web, and you fail to avoid its spit. The sticky ooze hits your eyes, covering them like a glued cloth.
                        '
                        'I drop my weapon and clean my eyes.' ( condition="at != 'force'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop my weapon and clean my eyes.')
                            $ at_unlock_force = 0
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump huntercabinbattleyescleaning01
                        'I don’t have time to clean my eyes. (disabled)' ( condition="at == 'force'" ):
                            pass
                        'I shoot at it blindly.' if huntercabin_crossbow:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shoot at it blindly.')
                            $ at_unlock_force = 0
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump huntercabinbattlshootingcrossbow01
                        'I swing my blade left and right, without pause.' if not huntercabin_crossbow:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I swing my blade left and right, without pause.')
                            $ at_unlock_force = 0
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump huntercabinbattleattackingaxemany01
                        'I wait for the spider to approach me, then dash at it fiercely.' if not huntercabin_crossbow:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for the spider to approach me, then dash at it fiercely.')
                            $ at_unlock_force = 0
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump huntercabinbattleattackingaxesingle01
                        'I drop my crossbow and draw the axe.' if huntercabin_crossbow:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop my crossbow and draw the axe.')
                            $ at_unlock_force = 0
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump huntercabinbattlegrabbingaxe01
                        'I drop my weapon and grab the spider with my bare hands.' ( condition="at != 'knowledge'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop my weapon and grab the spider with my bare hands.')
                            $ at_unlock_force = 0
                            $ at_unlock_knowledge = 0
                            $ at = 0
                            jump huntercabinbattlegrabbing01
                        'I shouldn’t touch the beast at all. (disabled)' ( condition="at == 'knowledge'" ):
                            pass
    elif search == "wait" or search == "stand" or search == "standstill" or search == "staystill" or search == "still" or search == "bestill" or search == "remainstill" or search == "scream" or search == "shout" or search == "yell" or search == "talk":
        jump huntercabinbattlewait01
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
                jump huntercabinbattle01
    elif search == "parry":
        menu:
            'There’s nothing to parry just yet.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump huntercabinbattle01
    elif search == "bite" or search == "chew" or search == "eat" or search == "munch" or search == "hug" or search == "hugit" or search == "eatit" or search == "biteit" or search == "pet" or search == "petit":
        menu:
            '...why though?
            '
            'Just let me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Just let me.')
                jump huntercabinbattlecharge01
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump huntercabinbattle01
    elif search == "spell" or search == "castspell" or search == "usespell" or search == "magicspell" or search == "wand" or search == "magicwand" or search == "blast" or search == "energyblast" or search == "wand" or search == "usewand" or search == "magic" or search == "usemagic" or search == "pneuma" or search == "pneumablast":
        if pc_class == "mage":
            if huntercabin_wand:
                $ huntercabin_spider_defeated = 1
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description05 = "The spider from the cabin is gone."
                $ pc_battlecounter += 1
                $ mana = limit_mana(mana-manacost)
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
                hide areapicture
                menu:
                    'You aim with the wand, while the spider skitters off, shaking the entire web. You release the invisible wave, but fail to avoid the creature’s spit. The sticky ooze hits your eyes, covering them like a glued cloth.
                    \n\nThe sack of flesh smacks the floor. It clicks in agony.
                    \n\nYour eyelids can’t even blink. You hide the wand behind your belt, then sit on the threshold blindly.
                    '
                    'I watch out for my eyes, but act quickly, harshly pulling the ooze.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I watch out for my eyes, but act quickly, harshly pulling the ooze.')
                        jump huntercabinbattleyescleaningfast01
                    'I remove it gently, bit by bit.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove it gently, bit by bit.')
                        jump huntercabinbattleyescleaningslow01
            else:
                menu:
                    'You’ve no time to prepare your amulets.
                    '
                    'I do something else.':
                        python:
                            search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                            search = search.strip().lower().replace(" ", "")
                            if not search:
                                search = "nothing"
                        jump huntercabinbattle01
        else:
            menu:
                'Since when you are a mage?
                '
                'I do something else.':
                    python:
                        search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump huntercabinbattle01
    elif search == "potion" or search == "throwpotion" or search == "usepotion" or search == "throwknife" or search == "throwaknife" or search == "changeweapon" or search == "switchweapons" or search == "takeknife" or search == "takeaknife" or search == "grabknife":
        menu:
            'You’ve no time to prepare a different item.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump huntercabinbattle01
    elif search == "push" or search == "charge" or search == "runatit" or search == "chargeatit" or search == "grabit" or search == "throwit" or search == "pushit" or search == "punchit" or search == "hold" or search == "grasp" or search == "grip" or search == "catch" or search == "squeeze" or search == "clutch" or search == "holdit" or search == "graspit" or search == "gripit" or search == "catchit" or search == "squeezeit" or search == "clutchit" or search == "kick" or search == "kickit" or search == "boot" or search == "punch" or search == "blow" or search == "bash" or search == "touch" or search == "touchit":
        label huntercabinbattlecharge01:
            hide areapicture
            if pc_class == "warrior":
                $ at_unlock_force = 1
                $ at = 0
            if pc_class == "scholar":
                $ at_unlock_knowledge = 1
                $ at = 0
            menu:
                'You rush forward and the spider skitters off, shaking the entire web. You fail to avoid its spit - the sticky ooze hits your eyes, covering them like a glued cloth.
                '
                'I drop my weapon and clean my eyes.' ( condition="at != 'force'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop my weapon and clean my eyes.')
                    $ at_unlock_force = 0
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump huntercabinbattleyescleaning01
                'I don’t have time to clean my eyes. (disabled)' ( condition="at == 'force'" ):
                    pass
                'I shoot at it blindly.' if huntercabin_crossbow:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shoot at it blindly.')
                    $ at_unlock_force = 0
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump huntercabinbattlshootingcrossbow01
                'I swing my blade left and right, without pause.' if not huntercabin_crossbow:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I swing my blade left and right, without pause.')
                    $ at_unlock_force = 0
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump huntercabinbattleattackingaxemany01
                'I wait for the spider to approach me, then dash at it fiercely.' if not huntercabin_crossbow:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for the spider to approach me, then dash at it fiercely.')
                    $ at_unlock_force = 0
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump huntercabinbattleattackingaxesingle01
                'I drop my crossbow and draw the axe.' if huntercabin_crossbow:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop my crossbow and draw the axe.')
                    $ at_unlock_force = 0
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump huntercabinbattlegrabbingaxe01
                'I drop my weapon and grab the spider with my bare hands.' ( condition="at != 'knowledge'" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drop my weapon and grab the spider with my bare hands.')
                    $ at_unlock_force = 0
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump huntercabinbattlegrabbing01
                'I shouldn’t touch the beast at all. (disabled)' ( condition="at == 'knowledge'" ):
                    pass
    elif search == "attack" or search == "attackit" or search == "hitit" or search == "hit" or search == "cutit" or search == "cut" or search == "strikeit" or search == "strike" or search == "useaxe" or search == "axe" or search == "ax" or search == "useax" or search == "slit" or search == "slash" or search == "pierce" or search == "gash" or search == "injure" or search == "hurt" or search == "lacerate" or search == "chop":
        if huntercabin_crossbow:
            menu:
                'You’re holding a crossbow, not an axe. Would you like to shoot the monster?
                '
                'Yes.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Yes.')
                    $ huntercabin_spider_defeated = 1
                    if quest_easternpath == 1 and quest_easternpath_description01:
                        $ renpy.notify("Journal updated: The Eastern Path")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                    $ quest_easternpath_description05 = "The spider from the cabin is gone."
                    $ pc_battlecounter += 1
                    hide areapicture
                    $ item_crossbowquarrels -= 1
                    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                    menu:
                        'You aim, while the spider skitters off, shaking the entire web. You pull the trigger, but fail to avoid the creature’s spit. The sticky ooze hits your eyes, covering them like a glued cloth.
                        \n\nThe sack of flesh smacks the floor. It clicks in agony.
                        \n\nYour eyelids can’t even blink. You drop the crossbow on the floor, then sit on the threshold blindly.
                        '
                        'I watch out for my eyes, but act quickly, harshly pulling the ooze.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I watch out for my eyes, but act quickly, harshly pulling the ooze.')
                            jump huntercabinbattleyescleaningfast01
                        'I remove it gently, bit by bit.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove it gently, bit by bit.')
                            jump huntercabinbattleyescleaningslow01
                'I try something else.':
                    python:
                        search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump huntercabinbattle01
        else:
            jump huntercabinbattlecharge01
    elif search == "fire" or search == "shoot" or search == "crossbow" or search == "shootwithcrossbow" or search == "shootfromcrossbow" or search == "shootit" or search == "shootit" or search == "usecrossbow" or search == "rangeattack":
        if not item_crossbow:
            menu:
                'You don’t possess a crossbow.
                '
                'I try something else.':
                    python:
                        search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump huntercabinbattle01
        elif huntercabin_crossbow:
            $ huntercabin_spider_defeated = 1
            if quest_easternpath == 1 and quest_easternpath_description01:
                $ renpy.notify("Journal updated: The Eastern Path")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
            $ quest_easternpath_description05 = "The spider from the cabin is gone."
            $ pc_battlecounter += 1
            hide areapicture
            $ item_crossbowquarrels -= 1
            $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
            menu:
                'You aim, while the spider skitters off, shaking the entire web. You pull the trigger, but fail to avoid the creature’s spit. The sticky ooze hits your eyes, covering them like a glued cloth.
                \n\nThe sack of flesh smacks the floor. It clicks in agony.
                \n\nYour eyelids can’t even blink. You drop the crossbow on the floor, then sit on the threshold blindly.
                '
                'I watch out for my eyes, but act quickly, harshly pulling the ooze.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I watch out for my eyes, but act quickly, harshly pulling the ooze.')
                    jump huntercabinbattleyescleaningfast01
                'I remove it gently, bit by bit.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove it gently, bit by bit.')
                    jump huntercabinbattleyescleaningslow01
        else:
            menu:
                'You left the crossbow by your saddle. You could instead charge at the monster with your melee weapon.
                '
                'Yes, I attack it with my axe.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Yes, I attack it with my axe.')
                    jump huntercabinbattlecharge01
                'I try something else.':
                    python:
                        search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump huntercabinbattle01
    elif search == "throwaxe" or search == "throwax" or search == "tossaxe" or search == "rangedaxeattack" or search == "tossax" or search == "rangedaxattack" or search == "throwatit" or search == "throwaxeatit" or search == "throwaxatit":
        if huntercabin_crossbow:
            menu:
                'You’re holding a crossbow, not an axe. Would you like to shoot the monster?
                '
                'Yes.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Yes.')
                    $ huntercabin_spider_defeated = 1
                    if quest_easternpath == 1 and quest_easternpath_description01:
                        $ renpy.notify("Journal updated: The Eastern Path")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                    $ quest_easternpath_description05 = "The spider from the cabin is gone."
                    $ pc_battlecounter += 1
                    hide areapicture
                    $ item_crossbowquarrels -= 1
                    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
                    menu:
                        'You aim, while the spider skitters off, shaking the entire web. You pull the trigger, but fail to avoid the creature’s spit. The sticky ooze hits your eyes, covering them like a glued cloth.
                        \n\nThe sack of flesh smacks the floor. It clicks in agony.
                        \n\nYour eyelids can’t even blink. You drop the crossbow on the floor, then sit on the threshold blindly.
                        '
                        'I watch out for my eyes, but act quickly, harshly pulling the ooze.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I watch out for my eyes, but act quickly, harshly pulling the ooze.')
                            jump huntercabinbattleyescleaningfast01
                        'I remove it gently, bit by bit.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove it gently, bit by bit.')
                            jump huntercabinbattleyescleaningslow01
        else:
            if pc_class == "warrior":
                $ huntercabin_spider_defeated = 1
                if quest_easternpath == 1 and quest_easternpath_description01:
                    $ renpy.notify("Journal updated: The Eastern Path")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
                $ quest_easternpath_description05 = "The spider from the cabin is gone."
                $ pc_battlecounter += 1
                hide areapicture
                menu:
                    'You aim, while the spider skitters off, shaking the entire web. You throw the axe, but fail to avoid the creature’s spit. The sticky ooze hits your eyes, covering them like a glued cloth.
                    \n\nThe sack of flesh smacks the floor. It clicks in agony.
                    \n\nYour eyelids can’t even blink. You drop the axe on the floor, then sit on the threshold blindly.
                    '
                    'I watch out for my eyes, but act quickly, harshly pulling the ooze.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I watch out for my eyes, but act quickly, harshly pulling the ooze.')
                        jump huntercabinbattleyescleaningfast01
                    'I remove it gently, bit by bit.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove it gently, bit by bit.')
                        jump huntercabinbattleyescleaningslow01
            else:
                hide areapicture
                if pc_class == "scholar":
                    $ at_unlock_knowledge = 1
                    $ at = 0
                $ huntercabin_noaxe = 1
                menu:
                    'You aim, while the spider skitters off, shaking the entire web. You throw the axe, but fail to avoid the creature’s spit. The sticky ooze hits your eyes, covering them like a glued cloth.
                    \n\nYour blade sinks into the wooden wall.
                    '
                    'I search for my backup knife. It’s better than nothing.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search for my backup knife. It’s better than nothing.')
                        $ at_unlock_force = 0
                        $ at_unlock_knowledge = 0
                        $ at = 0
                        jump huntercabinbattleknife01
                    'I try to grab the spider with my bare hands.' ( condition="at != 'knowledge'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to grab the spider with my bare hands.')
                        $ at_unlock_force = 0
                        $ at_unlock_knowledge = 0
                        $ at = 0
                        jump huntercabinbattlegrabbing01
                    '(I know this is a bad idea.) I try to grab the spider with my bare hands. (disabled)' ( condition="at == 'knowledge'" ):
                        pass
    elif search == "coverface" or search == "cover" or search == "blockattack" or search == "block" or search == "shield" or search == "useshield" or search == "blockshield" or search == "blockwithashield":
        if huntercabin_shield:
            menu:
                'You raise your shield just in time. It gets hit with the monster’s {i}saliva{/i} - it’s sticky like glue, dense, and threads of spider silk stick out of it.
                \n\nThe monster makes a clicking noise and runs at you. The movement of its legs is mesmerizing.
                '
                'My crossbow should do the trick now.' if huntercabin_crossbow:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- My crossbow should do the trick now.')
                    jump huntercabinbattlecrossbowlasthit01
                'My spell should do the trick now.' if huntercabin_wand:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- My spell should do the trick now.')
                    jump huntercabinbattlewandlasthit01
                'It’s desperate, but I have the range advantage. I wait for it to get closer, then strike its head.' if not huntercabin_crossbow:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s desperate, but I have the range advantage. I wait for it to get closer, then strike its head.')
                    jump huntercabinbattleaxelasthit01
        elif item_shield:
            menu:
                'You left your shield with {color=#f6d6bd}[horsename]{/color}. Would you like to cover your face with an arm?
                '
                'Yes.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Yes.')
                    jump huntercabinbattlecoveringfacewithhand
                'I do something else.':
                    python:
                        search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump huntercabinbattle01
        elif search == "shield" or search == "useshield" or search == "useshield" or search == "blockshield" or search == "blockwithashield":
            menu:
                'You don’t own a shield.
                '
                'I do something else.':
                    python:
                        search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump huntercabinbattle01
        else:
            label huntercabinbattlecoveringfacewithhand:
                $ cleanliness = limit_cleanliness(cleanliness-1)
                show minus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
                menu:
                    'Your elbow gets hit with the monster’s {i}saliva{/i} - it’s sticky like glue, dense, and threads of spider silk stick out of it.
                    \n\nThe monster makes a clicking noise and runs at you. The movement of its legs is mesmerizing.
                    '
                    'My crossbow should do the trick now.' if huntercabin_crossbow:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- My crossbow should do the trick now.')
                        jump huntercabinbattlecrossbowlasthit01
                    'My spell should do the trick now.' if huntercabin_wand:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- My spell should do the trick now.')
                        jump huntercabinbattlewandlasthit01
                    'It’s desperate, but I have the range advantage. I wait for it to get closer, then strike its head.' if not huntercabin_crossbow:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s desperate, but I have the range advantage. I wait for it to get closer, then strike its head.')
                        jump huntercabinbattleaxelasthit01
    elif search == "jump" or search == "jumpaway" or search == "jumpaside" or search == "dodge" or search == "dodgeattack" or search == "duck" or search == "leap" or search == "jumpleft" or search == "jumpright" or search == "moveaway" or search == "stepaway" or search == "stepaside" or search == "sideways":
        menu:
            'You jump to the side. The monster’s ball-like {i}saliva{/i}, white and sticky, flies through the door. The monster makes a clicking noise and runs at you. The movement of its legs is mesmerizing.
            '
            'My crossbow should do the trick now.' if huntercabin_crossbow:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My crossbow should do the trick now.')
                jump huntercabinbattlecrossbowlasthit01
            'My spell should do the trick now.' if huntercabin_wand:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- My spell should do the trick now.')
                jump huntercabinbattlewandlasthit01
            'It’s desperate, but I have the range advantage. I wait for it to get closer, then strike its head.' if not huntercabin_crossbow:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s desperate, but I have the range advantage. I wait for it to get closer, then strike its head.')
                jump huntercabinbattleaxelasthit01
    elif search == "runaway" or search == "leave" or search == "escape" or search == "dodge" or search == "flee":
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        hide spider
        show areapicture huntercabin01 behind spider at basicfade
        stop music fadeout 4.0
        play nature "audio/ambient/huntercabin01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        $ huntercabin_wand = 0
        $ huntercabin_crossbow = 0
        $ huntercabin_shield = 0
        menu:
            'You get outside and dash toward {color=#f6d6bd}[horsename]{/color}. For a moment you think that something moved behind your back, but the spider doesn’t follow you.
            '
            'I check on the cabin.' if not huntercabin_inside:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check on the cabin.')
                $ huntercabin_inside = 1
                jump huntercabin_insidefirsttime01
            'I enter the cabin.' if huntercabin_inside:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the cabin.')
                if not huntercabin_spider_defeated:
                    jump huntercabin_insidefirsttime01b
                else:
                    jump huntercabin_insideregular01
    else:
        menu:
            'I don’t know what you mean.
            '
            'I do something else.':
                python:
                    search = renpy.input("What do you try to do?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump huntercabinbattle01

label huntercabinbattleaxelasthit01:
    stop music fadeout 4.0
    play nature "audio/ambient/huntercabin01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture huntercabin_inside01 behind spider at basicfade
    $ huntercabin_spider_defeated = 1
    if quest_easternpath == 1 and quest_easternpath_description01:
        $ renpy.notify("Journal updated: The Eastern Path")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
    $ quest_easternpath_description05 = "The spider from the cabin is gone."
    $ pc_battlecounter += 1
    if huntercabin_spider_defeated and not huntercabin_spider_removed:
        show spider huntercabin at basicfade
    menu:
        'The charging spider can’t escape your confident swipe. Its “shell” breaks and hits the ground. The legs cease to shiver, one by one.
        \n\nThe room is covered with a thick layer of dust. Getting through the web could be risky - a single thread won’t stop you, but a bunch of them could grapple you for good.
        '
        'I search the building.' if huntercabin_inside_webremoved and not huntercabin_inside_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the building.')
            $ quarters += 1
            jump huntercabin_insidesearch01
        'I can’t search the building with this spiderweb around. (disabled)' if not huntercabin_inside_webremoved:
            pass
        'I drag the spider carcass away and throw it into the forest.' if not huntercabin_spider_removed:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drag the spider carcass away and throw it into the forest.')
            $ huntercabin_spider_removed = 1
            $ minutes += 5
            jump huntercabinremovingspider01
        'I don’t have much time. I light up a candle and melt the web.' if not huntercabin_inside_webremoved:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have much time. I light up a candle and melt the web.')
            $ minutes += 5
            $ huntercabin_inside_webremoved = 1
            jump huntercabinwebburned01
        'Someone could be interested in such a thick web. I spend an hour or so gathering it.' if not huntercabin_inside_webremoved:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone could be interested in such a thick web. I spend an hour or so gathering it.')
            $ quarters += 4
            $ huntercabin_inside_webremoved = 1
            jump huntercabinwebgathered01
        'I leave the building.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
            jump huntercabinoutsideafterinteraction01

label huntercabinbattlecrossbowlasthit01:
    stop music fadeout 4.0
    play nature "audio/ambient/huntercabin01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture huntercabin_inside01 behind spider at basicfade
    $ huntercabin_spider_defeated = 1
    if quest_easternpath == 1 and quest_easternpath_description01:
        $ renpy.notify("Journal updated: The Eastern Path")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
    $ quest_easternpath_description05 = "The spider from the cabin is gone."
    $ pc_battlecounter += 1
    if huntercabin_spider_defeated and not huntercabin_spider_removed:
        show spider huntercabin at basicfade
    $ item_crossbowquarrels -= 1
    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
    menu:
        'The quarrel sinks into the creature’s thorax. Its shell breaks and hits the ground. The legs cease to shiver, one by one.
        \n\nThe room is covered with a thick layer of dust. Getting through the web could be risky - a single thread won’t stop you, but a bunch of them could grapple you for good.
        '
        'I search the building.' if huntercabin_inside_webremoved and not huntercabin_inside_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the building.')
            $ quarters += 1
            jump huntercabin_insidesearch01
        'I can’t search the building with this spiderweb around. (disabled)' if not huntercabin_inside_webremoved:
            pass
        'I drag the spider carcass away and throw it into the forest.' if not huntercabin_spider_removed:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drag the spider carcass away and throw it into the forest.')
            $ huntercabin_spider_removed = 1
            $ minutes += 5
            jump huntercabinremovingspider01
        'I don’t have much time. I light up a candle and melt the web.' if not huntercabin_inside_webremoved:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have much time. I light up a candle and melt the web.')
            $ minutes += 5
            $ huntercabin_inside_webremoved = 1
            jump huntercabinwebburned01
        'Someone could be interested in such a thick web. I spend an hour or so gathering it.' if not huntercabin_inside_webremoved:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone could be interested in such a thick web. I spend an hour or so gathering it.')
            $ quarters += 4
            $ huntercabin_inside_webremoved = 1
            jump huntercabinwebgathered01
        'I leave the building.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
            jump huntercabinoutsideafterinteraction01

label huntercabinbattlewandlasthit01:
    stop music fadeout 4.0
    play nature "audio/ambient/huntercabin01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture huntercabin_inside01 behind spider at basicfade
    $ huntercabin_spider_defeated = 1
    if quest_easternpath == 1 and quest_easternpath_description01:
        $ renpy.notify("Journal updated: The Eastern Path")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
    $ quest_easternpath_description05 = "The spider from the cabin is gone."
    $ pc_battlecounter += 1
    if huntercabin_spider_defeated and not huntercabin_spider_removed:
        show spider huntercabin at basicfade
    $ mana = limit_mana(mana-manacost)
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s pneuma.{/i}' %manacost)
    menu:
        'You aim with the wand and release the invisible wave, throwing the spider into the wall with great force. Its “shell” breaks and hits the ground. The legs cease to shiver, one by one.
        \n\nThe room is covered with a thick layer of dust. Getting through the web could be risky - a single thread won’t stop you, but a bunch of them could grapple you for good.
        '
        'I search the building.' if huntercabin_inside_webremoved and not huntercabin_inside_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the building.')
            $ quarters += 1
            jump huntercabin_insidesearch01
        'I can’t search the building with this spiderweb around. (disabled)' if not huntercabin_inside_webremoved:
            pass
        'I drag the spider carcass away and throw it into the forest.' if not huntercabin_spider_removed:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drag the spider carcass away and throw it into the forest.')
            $ huntercabin_spider_removed = 1
            $ minutes += 5
            jump huntercabinremovingspider01
        'I don’t have much time. I light up a candle and melt the web.' if not huntercabin_inside_webremoved:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have much time. I light up a candle and melt the web.')
            $ minutes += 5
            $ huntercabin_inside_webremoved = 1
            jump huntercabinwebburned01
        'Someone could be interested in such a thick web. I spend an hour or so gathering it.' if not huntercabin_inside_webremoved:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone could be interested in such a thick web. I spend an hour or so gathering it.')
            $ quarters += 4
            $ huntercabin_inside_webremoved = 1
            jump huntercabinwebgathered01
        'I leave the building.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
            jump huntercabinoutsideafterinteraction01

label huntercabinbattleyescleaningslow01:
    $ quarters += 3
    show areapicture huntercabin_inside01 behind spider at basicfade
    if huntercabin_spider_defeated and not huntercabin_spider_removed:
        show spider huntercabin at basicfade
    stop music fadeout 4.0
    play nature "audio/ambient/huntercabin01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    $ cleanliness = limit_cleanliness(cleanliness-1)
    show minus1appearance at appearancechange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
    menu:
        'The saliva clings tightly to your skin, but stretching it with your fingers helps. The eyelids are the worst part, but you’re grateful for your reflexes - at least you still have eyes. You get to see the light slowly, then the shapes. The {i}thing{/i} turns out to be gray and white.
        \n\nYou stand up and look around. The room is covered with a thick layer of dust. Getting through the web could be risky - a single thread won’t stop you, but a bunch of them could grapple you for good.
        '
        'I search the building.' if huntercabin_inside_webremoved and not huntercabin_inside_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the building.')
            $ quarters += 1
            jump huntercabin_insidesearch01
        'I can’t search the building with this spiderweb around. (disabled)' if not huntercabin_inside_webremoved:
            pass
        'I drag the spider carcass away and throw it into the forest.' if not huntercabin_spider_removed:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drag the spider carcass away and throw it into the forest.')
            $ huntercabin_spider_removed = 1
            $ minutes += 5
            jump huntercabinremovingspider01
        'I don’t have much time. I light up a candle and melt the web.' if not huntercabin_inside_webremoved:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have much time. I light up a candle and melt the web.')
            $ minutes += 5
            $ huntercabin_inside_webremoved = 1
            jump huntercabinwebburned01
        'Someone could be interested in such a thick web. I spend an hour or so gathering it.' if not huntercabin_inside_webremoved:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone could be interested in such a thick web. I spend an hour or so gathering it.')
            $ quarters += 4
            $ huntercabin_inside_webremoved = 1
            jump huntercabinwebgathered01
        'I leave the building.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
            jump huntercabinoutsideafterinteraction01

label huntercabinbattleyescleaningfast01:
    $ minutes += 5
    show areapicture huntercabin_inside01 behind spider at basicfade
    if huntercabin_spider_defeated and not huntercabin_spider_removed:
        show spider huntercabin at basicfade
    $ pc_hp = limit_pc_hp(pc_hp-1)
    show minus1hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
    $ huntercabin_spider_pchurt += 1
    stop music fadeout 4.0
    play nature "audio/ambient/huntercabin01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    menu:
        'The saliva clings tightly to your skin. You rip it off, suffering after every pull, but the results come quick. You slow down when you get to the eyelids. You’re grateful for your reflexes - at least you still have eyes. You get to see the light slowly, then the shapes. The {i}thing{/i} turns out to be gray and white.
        \n\nYou stand up and look around. The room is covered with a thick layer of dust. Getting through the web could be risky - a single thread won’t stop you, but a bunch of them could grapple you for good.
        '
        'I search the building.' if huntercabin_inside_webremoved and not huntercabin_inside_searched:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search the building.')
            $ quarters += 1
            $ at_unlock_spell = 0
            $ at = 0
            jump huntercabin_insidesearch01
        'I can’t search the building with this spiderweb around. (disabled)' if not huntercabin_inside_webremoved:
            pass
        'I drag the spider carcass away and throw it into the forest.' if not huntercabin_spider_removed:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I drag the spider carcass away and throw it into the forest.')
            $ huntercabin_spider_removed = 1
            $ minutes += 5
            $ at_unlock_spell = 0
            $ at = 0
            jump huntercabinremovingspider01
        'I don’t have much time. I light up a candle and melt the web.' if not huntercabin_inside_webremoved:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have much time. I light up a candle and melt the web.')
            $ minutes += 5
            $ huntercabin_inside_webremoved = 1
            $ at_unlock_spell = 0
            $ at = 0
            jump huntercabinwebburned01
        'Someone could be interested in such a thick web. I spend an hour or so gathering it.' if not huntercabin_inside_webremoved:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone could be interested in such a thick web. I spend an hour or so gathering it.')
            $ quarters += 4
            $ huntercabin_inside_webremoved = 1
            $ at_unlock_spell = 0
            $ at = 0
            jump huntercabinwebgathered01
        'I leave the building.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the building.')
            $ at_unlock_spell = 0
            $ at = 0
            jump huntercabinoutsideafterinteraction01

label huntercabinbattlshootingcrossbow01:
    $ pc_hp = limit_pc_hp(pc_hp-1)
    show minus1hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
    $ huntercabin_spider_pchurt += 1
    if pc_class == "scholar":
        $ at_unlock_knowledge = 1
        $ at = 0
    $ item_crossbowquarrels -= 1
    $ renpy.notify("You’ve got %s quarrels left." %item_crossbowquarrels)
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a quarrel. You’ve got %s quarrels left.{/i}' %item_crossbowquarrels)
    menu:
        'The quarrel hits the wall, followed by the quick {i}steps{/i} of the creature. You step back and put away your weapon. Your calf gets pierced by the spear-sharp leg. Your heart beats faster.
        '
        'I search for my backup knife. It’s better than nothing.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search for my backup knife. It’s better than nothing.')
            $ at_unlock_force = 0
            $ at_unlock_knowledge = 0
            $ at = 0
            $ huntercabin_knife = 1
            menu:
                'You unsheathe the short, one-sided blade, though you can’t say you had much experience using it in combat.
                '
                'I strike the spider down blindly, making as many swings as I can.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I strike the spider down blindly, making as many swings as I can.')
                    $ at_unlock_force = 0
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump huntercabinbattleattackingknifemany01b
                'I wait for the spider to approach me, then dash at it fiercely.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for the spider to approach me, then dash at it fiercely.')
                    $ at_unlock_force = 0
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump huntercabinbattleattackingknifesingle01
        'I try to grab the spider with my bare hands.' ( condition="at != 'knowledge'" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to grab the spider with my bare hands.')
            $ at_unlock_force = 0
            $ at_unlock_knowledge = 0
            $ at = 0
            jump huntercabinbattlegrabbing01
        'I shouldn’t touch the beast at all. (disabled)' ( condition="at == 'knowledge'" ):
            pass
        'I still have my axe. Time to use it.' if not huntercabin_noaxe:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still have my axe. Time to use it.')
            $ at_unlock_force = 0
            $ at_unlock_knowledge = 0
            $ at = 0
            menu:
                'You grab the haft firmly. Thanks to your years of practice, you move to a defensive stance.
                '
                'I strike the spider down blindly, making as many swings as I can.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I strike the spider down blindly, making as many swings as I can.')
                    $ at_unlock_force = 0
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump huntercabinbattleattackingaxemany01b
                'I wait for the spider to approach me, then dash at it fiercely.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for the spider to approach me, then dash at it fiercely.')
                    $ at_unlock_force = 0
                    $ at_unlock_knowledge = 0
                    $ at = 0
                    jump huntercabinbattleattackingaxesingle01
        'I already lost my axe. (disabled)' if huntercabin_noaxe:
            pass

label huntercabinbattlegrabbingaxe01:
    menu:
        'You grab the haft firmly. Thanks to your years of practice, you move to a defensive stance.
        '
        'I strike the spider down blindly, making as many swings as I can.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I strike the spider down blindly, making as many swings as I can.')
            $ at_unlock_force = 0
            $ at_unlock_knowledge = 0
            $ at = 0
            jump huntercabinbattleattackingaxemany01
        'I wait for the spider to approach me, then dash at it fiercely.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for the spider to approach me, then dash at it fiercely.')
            $ at_unlock_force = 0
            $ at_unlock_knowledge = 0
            $ at = 0
            jump huntercabinbattleattackingaxesingle01

label huntercabinbattleattackingaxemany01:
    if pc_hp < 1:
        jump huntercabinbattlelackofhp01
    $ huntercabin_spider_defeated = 1
    if quest_easternpath == 1 and quest_easternpath_description01:
        $ renpy.notify("Journal updated: The Eastern Path")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
    $ quest_easternpath_description05 = "The spider from the cabin is gone."
    $ pc_battlecounter += 1
    $ pc_hp = limit_pc_hp(pc_hp-1)
    show minus1hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
    $ huntercabin_spider_pchurt += 1
    menu:
        'You cut the air at knee height, but somehow the creature reaches your side. Your calf gets pierced by the spear-sharp leg. Your heart beats faster, yet you keep control over your limbs and remain standing.
        \n\nThe next swing lands - the sack of flesh smacks the floor and clicks in agony. You hear only your own heart and the chirping of the insects outside. You’re getting sweaty.
        \n\nYour eyelids can’t even blink. You drop the axe on the floor, then sit on the threshold blindly.
        '
        'I watch out for my eyes, but act quickly, harshly pulling the ooze.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I watch out for my eyes, but act quickly, harshly pulling the ooze.')
            jump huntercabinbattleyescleaningfast01
        'I remove it gently, bit by bit.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove it gently, bit by bit.')
            jump huntercabinbattleyescleaningslow01

label huntercabinbattleattackingaxemany01b:
    if pc_hp < 1:
        jump huntercabinbattlelackofhp01
    $ huntercabin_spider_defeated = 1
    if quest_easternpath == 1 and quest_easternpath_description01:
        $ renpy.notify("Journal updated: The Eastern Path")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
    $ quest_easternpath_description05 = "The spider from the cabin is gone."
    $ pc_battlecounter += 1
    $ pc_hp = limit_pc_hp(pc_hp-1)
    show minus1hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
    $ huntercabin_spider_pchurt += 1
    menu:
        'You cut the air at knee height, but somehow the creature reaches your side and strikes you again. You keep control over your limbs and remain standing.
        \n\nThe next swing lands - the sack of flesh smacks the floor and clicks in agony. You hear only your own heart and the chirping of the insects outside. You’re getting sweaty.
        \n\nYour eyelids can’t even blink. You drop the axe on the floor, then sit on the threshold blindly.
        '
        'I watch out for my eyes, but act quickly, harshly pulling the ooze.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I watch out for my eyes, but act quickly, harshly pulling the ooze.')
            jump huntercabinbattleyescleaningfast01
        'I remove it gently, bit by bit.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove it gently, bit by bit.')
            jump huntercabinbattleyescleaningslow01

label huntercabinbattleattackingaxesingle01:
    $ huntercabin_spider_defeated = 1
    if quest_easternpath == 1 and quest_easternpath_description01:
        $ renpy.notify("Journal updated: The Eastern Path")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
    $ quest_easternpath_description05 = "The spider from the cabin is gone."
    $ pc_battlecounter += 1
    menu:
        'The charging spider can’t escape your confident swipe. The sack of flesh smacks the floor and clicks in agony. You hear only your own heart and the chirping of the insects outside. You’re getting sweaty.
        \n\nYour eyelids can’t even blink. You drop the axe on the floor, then sit on the threshold blindly.
        '
        'I watch out for my eyes, but act quickly, harshly pulling the ooze.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I watch out for my eyes, but act quickly, harshly pulling the ooze.')
            jump huntercabinbattleyescleaningfast01
        'I remove it gently, bit by bit.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove it gently, bit by bit.')
            jump huntercabinbattleyescleaningslow01

label huntercabinbattleknifeALL:
    label huntercabinbattleknife01:
        $ huntercabin_knife = 1
        menu:
            'You unsheathe the short, one-sided blade, though you can’t say you had much experience using it in combat.
            '
            'I strike the spider down blindly, making as many swings as I can.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I strike the spider down blindly, making as many swings as I can.')
                $ at_unlock_force = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump huntercabinbattleattackingknifemany01
            'I wait for the spider to approach me, then dash at it fiercely.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for the spider to approach me, then dash at it fiercely.')
                $ at_unlock_force = 0
                $ at_unlock_knowledge = 0
                $ at = 0
                jump huntercabinbattleattackingknifesingle01

    label huntercabinbattleattackingknifemany01:
        if pc_hp < 2:
            jump huntercabinbattlelackofhp01
        $ huntercabin_spider_defeated = 1
        if quest_easternpath == 1 and quest_easternpath_description01:
            $ renpy.notify("Journal updated: The Eastern Path")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
        $ quest_easternpath_description05 = "The spider from the cabin is gone."
        $ pc_battlecounter += 1
        $ pc_hp = limit_pc_hp(pc_hp-2)
        show minus2hp at hpchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
        $ huntercabin_spider_pchurt += 2
        menu:
            'You cut the air at knee height, but somehow the creature reaches your side. Your calf gets pierced by the spear-sharp leg. Your heart beats faster, yet you keep control over your limbs and remain standing.
            \n\nThe next few jabs land, but your hands get in touch with the monster’s hair. Your skin is burning.
            \n\nThe sack of flesh smacks the floor and clicks in agony. You hear only your own heart and the chirping of the insects outside. You’re getting sweaty.
            \n\nYour eyelids can’t even blink. You drop the knife on the floor, then sit on the threshold blindly.
            '
            'I watch out for my eyes, but act quickly, harshly pulling the ooze.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I watch out for my eyes, but act quickly, harshly pulling the ooze.')
                jump huntercabinbattleyescleaningfast01
            'I remove it gently, bit by bit.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove it gently, bit by bit.')
                jump huntercabinbattleyescleaningslow01

    label huntercabinbattleattackingknifemany01b:
        if pc_hp < 2:
            jump huntercabinbattlelackofhp01
        $ huntercabin_spider_defeated = 1
        if quest_easternpath == 1 and quest_easternpath_description01:
            $ renpy.notify("Journal updated: The Eastern Path")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
        $ quest_easternpath_description05 = "The spider from the cabin is gone."
        $ pc_battlecounter += 1
        $ pc_hp = limit_pc_hp(pc_hp-2)
        show minus2hp at hpchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-2 vitality points.{/i}')
        $ huntercabin_spider_pchurt += 2
        menu:
            'You cut the air at knee height, but somehow the creature reaches your side and strikes you again. You keep control over your limbs and remain standing.
            \n\nThe next few jabs land, but your hands get in touch with the monster’s hair. Your skin is burning.
            \n\nThe sack of flesh smacks the floor and clicks in agony. You hear only your own heart and the chirping of the insects outside. You’re getting sweaty.
            \n\nYour eyelids can’t even blink. You drop the knife on the floor, then sit on the threshold blindly.
            '
            'I watch out for my eyes, but act quickly, harshly pulling the ooze.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I watch out for my eyes, but act quickly, harshly pulling the ooze.')
                jump huntercabinbattleyescleaningfast01
            'I remove it gently, bit by bit.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove it gently, bit by bit.')
                jump huntercabinbattleyescleaningslow01

    label huntercabinbattleattackingknifesingle01:
        if pc_hp < 1:
            jump huntercabinbattlelackofhp01
        $ huntercabin_spider_defeated = 1
        if quest_easternpath == 1 and quest_easternpath_description01:
            $ renpy.notify("Journal updated: The Eastern Path")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Eastern Path{/i}')
        $ quest_easternpath_description05 = "The spider from the cabin is gone."
        $ pc_battlecounter += 1
        $ pc_hp = limit_pc_hp(pc_hp-1)
        show minus1hp at hpchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
        $ huntercabin_spider_pchurt += 1
        menu:
            'The charging spider can’t escape your confident jab, but your hands get in touch with the monster’s hair. Your skin is burning.
            \n\nStill, you broke its shell and it clicks in agony. You hear only your own heart and the chirping of the insects outside. You’re getting sweaty.
            \n\nYour eyelids can’t even blink. You drop the knife on the floor, then sit on the threshold blindly.
            '
            'I watch out for my eyes, but act quickly, harshly pulling the ooze.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I watch out for my eyes, but act quickly, harshly pulling the ooze.')
                jump huntercabinbattleyescleaningfast01
            'I remove it gently, bit by bit.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I remove it gently, bit by bit.')
                jump huntercabinbattleyescleaningslow01

label huntercabinbattleyescleaning01:
    $ pc_hp = 0
    show minus5hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
    if pc_religion == "pagan":
        show areapicture gameover_alt at basicfade
    else:
        show areapicture gameover at basicfade
    menu:
        'Your right hand reaches the sticky substance, but then you can’t free your fingers. Your nervous twitches make the pain only stronger.
        \n\nThe creature grabs your flesh with its spear-sharp legs, then bites it, not bothered by your clothes. You try to grab it with the other hand, but the spider’s hair makes your skin burn after a single sting.
        \n\nThe last things you remember are your fall and the endless, satisfied clicking.
        \n
        \n\n[pcname]’s soul has left its shell.
        '
        ' Let me replay this area.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this area.')
            stop music fadeout 4.0
            $ renpy.load("combatsave")

label huntercabinbattlegrabbing01:
    $ pc_hp = 0
    show minus5hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
    if pc_religion == "pagan":
        show areapicture gameover_alt at basicfade
    else:
        show areapicture gameover at basicfade
    menu:
        'The spider’s hair makes your skin burn with a single sting. You can’t help but scream. As you raise your hands, the creature grabs your flesh with its spear-sharp legs, then bites it, not bothered by your clothes
        \n\nThe last things you remember are your fall and the endless, satisfied clicking.
        \n
        \n\n[pcname]’s soul has left its shell.
        '
        ' Let me replay this area.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this area.')
            stop music fadeout 4.0
            $ renpy.load("combatsave")

label huntercabinbattlelackofhp01:
    $ pc_hp = 0
    show minus5hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
    if pc_religion == "pagan":
        show areapicture gameover_alt at basicfade
    else:
        show areapicture gameover at basicfade
    menu:
        'Your wounds and exhaustion overwhelm you - you can’t keep up with the beast, and after you miss a few mindless jabs and cuts, the spider grabs your leg, cutting the artery swiftly.
        \n\nThe last things you remember are your fall and the endless, satisfied clicking.
        \n
        \n\n[pcname]’s soul has left its shell.
        '
        ' Let me replay this area.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this area.')
            stop music fadeout 4.0
            $ renpy.load("combatsave")

label huntercabin_insidebanditaboutreward01:
    if not shortcut_darkforest_bandit_confronted:
        $ banditshideout_pcknowswhere = 1
        if (shortcut_darkforest_bandit_friendship+appearance_charisma) > 3:
            $ custom1 = "“It’s not a safe road, but not as scary as people say. You’ll need a hook with a rope to get through. And...” He hesitates. “Don’t meet with {color=#f6d6bd}Glaucia{/color} as a weakling. You’re someone who fights wolves merely because. Stay upright.”"
            $ description_shortcut02 = "I heard that to get to the bandit camp, one needs to own a grappling hook."
        elif (shortcut_darkforest_bandit_friendship+appearance_charisma) > 1:
            $ custom1 = "“It’s not a safe road, but not as scary as people say. You’ll need a hook with a rope to move through it.”"
            $ description_shortcut02 = "I heard that to get to the bandit camp, one needs to own a grappling hook."
        else:
            $ custom1 = "“Go there if you’re brave. Stay away if you’re smart.”"
        menu:
            '“Right, right. You helped me find this place, and I want to be even with you.” He approaches the entrance and looks outside, maybe making sure that you’re not being followed. “You’re going to look for the camp of bandits, stranger. If not now, then another day. You’re merely one of those,” his look is absent, wandering in a different place. “So listen carefully. Head to the middle of the shortcut, to a pile of stones, then turn north. There’s no path in sight, but don’t worry, you’ll find it soon, you will.”
            \n\nHe pauses. [custom1]
            \n\nYou ask him where his knowledge comes from, but there’s anger in his blue eyes. “Don’t try to make an enemy now, stranger. I’m harmless, but not defenseless. And my past will remain merely that. The past.”
            '
            '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                $ shortcut_darkforest_bandit_about_reward = 1
                jump huntercabin_insidebanditaboutreward01
            '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                $ shortcut_darkforest_bandit_about_corpse = 2
                $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                jump huntercabin_insidebanditaboutcorpse01
            '“Are you planning to stay here for long?”' if not shortcut_darkforest_bandit_about_stayingaround:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                $ shortcut_darkforest_bandit_about_stayingaround = 1
                jump huntercabin_insidebanditaboutstayingaround01
            '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                $ shortcut_darkforest_bandit_about_questions = 1
                jump huntercabin_insidebanditaboutquestions01
            '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump huntercabin_insidebanditconfrontedaboutglauciasquest01
            '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                $ custom1 = "He takes a deep breath and keenly observes your lips."
                jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
            '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump huntercabin_insidebanditconfrontedaboutglauciasquest02
            'I bid farewell to him.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bid farewell to him.')
                jump huntercabinoutsideafterinteraction01
    else:
        $ description_glaucia19 = "According to {color=#f6d6bd}the runaway bandit{/color}, “for as long as she’s backed by the council of {color=#f6d6bd}Gale Rocks{/color}, she has a full stomach and warm togs. She won’t hesitate to kill you if she feels threatened by you.”"
        menu:
            'He gives you an embarrassed look. “I wanted to tell you how to reach {color=#f6d6bd}Glaucia{/color}, but you already know all that.” He approaches the entrance and looks outside, maybe making sure that you’re not being followed. “Be wary of her, stranger. You’d need a large squad to threaten her, and for as long as she’s backed by the council of {color=#f6d6bd}Gale Rocks{/color}, she has a full stomach and warm togs. She won’t hesitate to kill you if she feels threatened by you.”
            '
            '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                $ shortcut_darkforest_bandit_about_reward = 1
                jump huntercabin_insidebanditaboutreward01
            '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                $ shortcut_darkforest_bandit_about_corpse = 2
                $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                jump huntercabin_insidebanditaboutcorpse01
            '“Are you planning to stay here for long?”' if not shortcut_darkforest_bandit_about_stayingaround:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                $ shortcut_darkforest_bandit_about_stayingaround = 1
                jump huntercabin_insidebanditaboutstayingaround01
            '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                $ shortcut_darkforest_bandit_about_questions = 1
                jump huntercabin_insidebanditaboutquestions01
            '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump huntercabin_insidebanditconfrontedaboutglauciasquest01
            '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                $ custom1 = "He takes a deep breath and keenly observes your lips."
                jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
            '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump huntercabin_insidebanditconfrontedaboutglauciasquest02
            'I bid farewell to him.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bid farewell to him.')
                jump huntercabinoutsideafterinteraction01

label huntercabin_insidebanditaboutstayingaround01:
    menu:
        '“Nah. Merely enough to rest before I head south. A few days, no more,” his eyes get colder. “But {i}don’t{/i} say a word about me to anyone, stranger. I’m {i}dead{/i} serious.”
        '
        '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
            $ shortcut_darkforest_bandit_about_reward = 1
            jump huntercabin_insidebanditaboutreward01
        '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
            $ shortcut_darkforest_bandit_about_corpse = 2
            $ shortcut_darkforest_furlesswolf_corpseidentity = 1
            jump huntercabin_insidebanditaboutcorpse01
        '“Are you planning to stay here for long?”' if not shortcut_darkforest_bandit_about_stayingaround:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
            $ shortcut_darkforest_bandit_about_stayingaround = 1
            jump huntercabin_insidebanditaboutstayingaround01
        '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
            $ shortcut_darkforest_bandit_about_questions = 1
            jump huntercabin_insidebanditaboutquestions01
        '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
            $ shortcut_darkforest_bandit_confronted = 1
            jump huntercabin_insidebanditconfrontedaboutglauciasquest01
        '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
            $ custom1 = "He takes a deep breath and keenly observes your lips."
            jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
        '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
            $ shortcut_darkforest_bandit_confronted = 1
            jump huntercabin_insidebanditconfrontedaboutglauciasquest02
        'I bid farewell to him.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bid farewell to him.')
            jump huntercabinoutsideafterinteraction01

label huntercabin_insidebanditaboutcorpse01:
    $ quest_missinghunters_vaschelfound = 1
    $ quest_missinghunters_vaschelknown = 1
    menu:
        '“Let me think... It wasn’t in all that good shape, quite slaughtered, you see. It was a male, I saw them before, name was {color=#f6d6bd}Vaschel{/color}. Darker than me, black hair, this tall,” he raises his hand to estimate the person’s size. “Was wearing leather, brown and green, them people at {color=#f6d6bd}Creeks{/color} wear such things all the time. He had scraps of his face, he did, and here,” he points to his left ear, “he had an animal bone, an earling.”
        '
        '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
            $ shortcut_darkforest_bandit_about_reward = 1
            jump huntercabin_insidebanditaboutreward01
        '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
            $ shortcut_darkforest_bandit_about_corpse = 2
            $ shortcut_darkforest_furlesswolf_corpseidentity = 1
            jump huntercabin_insidebanditaboutcorpse01
        '“Are you planning to stay here for long?”' if not shortcut_darkforest_bandit_about_stayingaround:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
            $ shortcut_darkforest_bandit_about_stayingaround = 1
            jump huntercabin_insidebanditaboutstayingaround01
        '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
            $ shortcut_darkforest_bandit_about_questions = 1
            jump huntercabin_insidebanditaboutquestions01
        '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
            $ shortcut_darkforest_bandit_confronted = 1
            jump huntercabin_insidebanditconfrontedaboutglauciasquest01
        '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
            $ custom1 = "He takes a deep breath and keenly observes your lips."
            jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
        '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
            $ shortcut_darkforest_bandit_confronted = 1
            jump huntercabin_insidebanditconfrontedaboutglauciasquest02
        'I bid farewell to him.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bid farewell to him.')
            jump huntercabinoutsideafterinteraction01

label huntercabin_insidebanditaboutquestions01:
    menu:
        'He shrugs. “I don’t care. I’ve no reason to amuse you. And I’ve made a pledge to keep things to myself.”
        '
        '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
            $ shortcut_darkforest_bandit_about_reward = 1
            jump huntercabin_insidebanditaboutreward01
        '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
            $ shortcut_darkforest_bandit_about_corpse = 2
            $ shortcut_darkforest_furlesswolf_corpseidentity = 1
            jump huntercabin_insidebanditaboutcorpse01
        '“Are you planning to stay here for long?”' if not shortcut_darkforest_bandit_about_stayingaround:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
            $ shortcut_darkforest_bandit_about_stayingaround = 1
            jump huntercabin_insidebanditaboutstayingaround01
        '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
            $ shortcut_darkforest_bandit_about_questions = 1
            jump huntercabin_insidebanditaboutquestions01
        '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
            $ shortcut_darkforest_bandit_confronted = 1
            jump huntercabin_insidebanditconfrontedaboutglauciasquest01
        '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
            $ custom1 = "He takes a deep breath and keenly observes your lips."
            jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
        '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
            $ shortcut_darkforest_bandit_confronted = 1
            jump huntercabin_insidebanditconfrontedaboutglauciasquest02
        'I bid farewell to him.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bid farewell to him.')
            jump huntercabinoutsideafterinteraction01

label huntercabin_insidebanditconfrontedaboutglauciasquestALL:
    label huntercabin_insidebanditconfrontedaboutglauciasquest01:
        $ shortcut_bandit_identity = 1
        menu:
            'His breath gets heavier, and after you notice his hand reaching for something behind his back, he drops a dagger and raises his arms. “Please. She’ll kill me.”
            '
            '“Tell me your story.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me your story.”')
                $ custom1 = "“There ain’t much of one. Wanted to be a free soul, hunt beasts, maybe take away a little something from what merchants keep in their lake-deep pockets. But {color=#f6d6bd}Glaucia’s{/color} obsessed with {color=#f6d6bd}White Marshes{/color} and their {i}awoken{/i}. She told me my day is coming, that it’s time to do my share of {i}work{/i}. But I won’t murder in her name, I won’t.” With every word, he speaks a bit quicker, and ends his tale with a flinch, as if a bad memory just pinched his ear."
                jump huntercabin_insidebanditconfrontedaboutglauciasquest01past

    label huntercabin_insidebanditconfrontedaboutglauciasquest01past:
        menu:
            '[custom1]
            '
            '“Just give me the things you stole from her. I’ll try to convince her to forget about all this.”' if glaucia_about_runaway_bonusquestion6 and not shortcut_darkforest_bandit_confronted_question1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just give me the things you stole from her. I’ll try to convince her to forget about all this.”')
                $ custom1 = "“I... don’t have it,” he looks away. “I got all them powder soggy. I tried to then use it to torch some wood, but that was {i}not{/i} a good idea.”"
                $ shortcut_darkforest_bandit_confronted_question1 = 1
                jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
            '“Can I be sure you won’t just look for another band once you cross {color=#f6d6bd}Hag Hills{/color}?”' if not shortcut_darkforest_bandit_confronted_question3:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I be sure you won’t just look for another band once you cross {color=#f6d6bd}Hag Hills{/color}?”')
                $ custom1 = "“I don’t know much about the lands in the south, but they can’t be as bad as they are here,” you consider refuting his statement, but he carries on. “I may stay at a few inns, and get to {color=#f6d6bd}Hovlavan{/color} before winter with a heavy pouch. I have skills,” he spares you a charming smirk, “that I could put there to hire.”"
                $ shortcut_darkforest_bandit_confronted_question3 = 1
                jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
            '“What are those {i}skills{/i} of yours?”' if shortcut_darkforest_bandit_confronted_question4 and not shortcut_darkforest_bandit_confronted_question4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What are those {i}skills{/i} of yours?”')
                $ custom1 = "“Quick legs, fast hands, a healthy back... Oh, and I can blend in with shadows, if I’m rested.” Seeing your frown, he gives you a dishonest smile, but his eyes are as tense as his teeth are white. “You didn’t think I was staying around for so long all playing fair, did you? I don’t care who’s going to hire me. Priests, merchants, officials, even adventurers. They’ll sure pay me better than {color=#f6d6bd}Glaucia{/color} did.”"
                $ shortcut_darkforest_bandit_confronted_question4 = 1
                jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
            '“Helping you may turn out to be costly. What can you give me in return?”' if not shortcut_darkforest_bandit_confronted_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Helping you may turn out to be costly. What can you give me in return?”')
                $ custom1 = "He falls quiet. He glances at his knife, which is made of fine steel, but has a rather simple handle. “I’m broke,” he pouches his lips, “but you may need my help, one day. I could help you get to a dangerous place, even fight beasts for you. And then, maybe I’ll join you on your ride to the city, alright? I’ll soon leave for {color=#f6d6bd}Pelt{/color}, you’ll find me there, if not here.”"
                $ shortcut_darkforest_bandit_confronted_question2 = 1
                $ shortcut_darkforest_bandit_about_stayingaround = 1
                jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
            '“Very well. I’ll cover for you for {color=#f6d6bd}Glaucia{/color}. Wait for me here or at {color=#f6d6bd}Pelt{/color} until the end of summer.”' if shortcut_darkforest_bandit_confronted_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. I’ll cover for you for {color=#f6d6bd}Glaucia{/color}. Wait for me here or at {color=#f6d6bd}Pelt{/color} until the end of summer.”')
                label huntercabin_insidebanditconfrontedaboutglauciasquest02:
                    $ shortcut_darkforest_bandit_promisedtocoverforhim = 1
                    $ pc_goal_iwanttohelppoints += 1
                    $ description_glaucia20 = "According to {color=#f6d6bd}the runaway bandit{/color}, “her gratitude goes only as far as it takes to spare one’s life. She thinks she’s saving the innocent and punishing the monsters, so in her view it’s {i}us{/i} who should be grateful to {i}her{/i}.”"
                    menu:
                        '“You won’t regret this,” he gives you a grateful nod. “Her gratitude goes only as far as it takes to spare one’s life. She thinks she’s saving the innocent and punishing the monsters, so in her view it’s {i}us{/i} who should be grateful to {i}her{/i}.”
                        '
                        '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                            $ shortcut_darkforest_bandit_about_reward = 1
                            jump huntercabin_insidebanditaboutreward01
                        '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                            $ shortcut_darkforest_bandit_about_corpse = 2
                            $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                            jump huntercabin_insidebanditaboutcorpse01
                        '“Are you planning to stay here for long?”' if not shortcut_darkforest_bandit_about_stayingaround:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                            $ shortcut_darkforest_bandit_about_stayingaround = 1
                            jump huntercabin_insidebanditaboutstayingaround01
                        '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                            $ shortcut_darkforest_bandit_about_questions = 1
                            jump huntercabin_insidebanditaboutquestions01
                        '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                            $ shortcut_darkforest_bandit_confronted = 1
                            jump huntercabin_insidebanditconfrontedaboutglauciasquest01
                        '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                            $ custom1 = "He takes a deep breath and keenly observes your lips."
                            jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
                        '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                            $ shortcut_darkforest_bandit_confronted = 1
                            jump huntercabin_insidebanditconfrontedaboutglauciasquest02
                        'I bid farewell to him.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bid farewell to him.')
                            jump huntercabinoutsideafterinteraction01
            '“I want nothing to do with a bandit, but I’m not going to use your life as a ware to sell. Just leave the peninsula, and right now.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want nothing to do with a bandit, but I’m not going to use your life as a ware to sell. Just leave the peninsula, and right now.”')
                $ shortcut_darkforest_bandit_leftthepeninsula = 1
                menu:
                    'He gives you a long look, then, without a word, grabs his sparse belongings. For a few breaths, you see him heading south, but then he enters a darker part of the road - and seems to vanish in thin air.
                    '
                    'I go outside.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                        jump huntercabinoutsideafterinteraction01
            '“I need to think about all this.”' if shortcut_darkforest_bandit_confronted_question2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about all this.”')
                menu:
                    '“Don’t play with me, stranger,” he growls. “I’m not going to sit around and wait for your mercy without end.”
                    '
                    '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                        $ shortcut_darkforest_bandit_about_reward = 1
                        jump huntercabin_insidebanditaboutreward01
                    '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                        $ shortcut_darkforest_bandit_about_corpse = 2
                        $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                        jump huntercabin_insidebanditaboutcorpse01
                    '“Are you planning to stay here for long?”' if not shortcut_darkforest_bandit_about_stayingaround:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                        $ shortcut_darkforest_bandit_about_stayingaround = 1
                        jump huntercabin_insidebanditaboutstayingaround01
                    '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                        $ shortcut_darkforest_bandit_about_questions = 1
                        jump huntercabin_insidebanditaboutquestions01
                    '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                        $ shortcut_darkforest_bandit_confronted = 1
                        jump huntercabin_insidebanditconfrontedaboutglauciasquest01
                    '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                        $ custom1 = "He takes a deep breath and keenly observes your lips."
                        jump huntercabin_insidebanditconfrontedaboutglauciasquest01past
                    '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                        $ shortcut_darkforest_bandit_confronted = 1
                        jump huntercabin_insidebanditconfrontedaboutglauciasquest02
                    'I bid farewell to him.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I bid farewell to him.')
                        jump huntercabinoutsideafterinteraction01
