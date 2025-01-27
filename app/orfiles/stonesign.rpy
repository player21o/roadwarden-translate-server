###################### STONE SIGN / EASTERN WOODLAND EDGE / EASTERN FOREST ENTRANCE
default stonesign_firsttime = 0
default stonesign_firsttime_fluff = ""
default stonesign_fluff = ""
default stonesign_fluff_old = ""
default stonesign_tracks = 0

label stonesign01:
    nvl clear
    $ pc_area = "stonesign"
    stop music fadeout 4.0
    play nature "audio/ambient/stonesign01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture stonesign01 at basicfade
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    label stonesign_fluffloop:
        $ stonesign_fluff = renpy.random.choice(['Three hares cross the road so quickly you barely notice them. Soon after they disappear in the shrubs, a large, spotted cat shows up, trying to catch up with them. It spares you only a glance.', 'You spot fresh claw marks on a nearby tree trunk, as well as a broken branch.', 'You look at the boulder. On its surface, a fresh blood stain holds a few yellow feathers.', 'There are fresh pawprints on the road - a pack of wolves was heading east.', 'On top of a nearby hill, you spot a four-legged dragon chewing on the tree leaves. It completely ignores you, and as you observe its long neck, as thick as a trunk, you can’t imagine a blade that could wound it.'])
        if stonesign_fluff_old == stonesign_fluff:
            jump stonesign_fluffloop
        else:
            $ stonesign_fluff_old = stonesign_fluff
    if not stonesign_firsttime and shortcut_inprogress:
        $ shortcut_inprogress = 0
        $ world_known_areas += 1
        $ stonesign_firsttime = 1
        $ watchtower_unlocked = 1
        jump stonesignfirsttime01fromshortcut
    elif not stonesign_firsttime:
        $ world_known_areas += 1
        $ stonesign_firsttime = 1
        $ watchtower_unlocked = 1
        jump stonesignfirsttime01
    elif shortcut_inprogress:
        $ shortcut_inprogress = 0
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        jump stonesignregular01fromshortcut
    else:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        jump stonesignregular01

label stonesignfirsttime01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown" or pc_religion == "pagan":
        $ pc_faithpoints_opportunities += 1
    if persistent.deafmode:
        $ deafcustom1 = " and fields inhabited by gurgling aurochs. The birds are loud, and you’ve never heard some of their songs before."
    else:
        $ deafcustom1 = ""
    menu:
        'The path leads downward, through the hills[deafcustom1]. The forest gets thicker, and the signs of human touch are rare - the lone, large boulder surely draws attention. You can’t guess its age, but the paths around suggest it was passed plenty of times already.
        \n\nYou stop {color=#f6d6bd}[horsename]{/color} to take a closer look. The remains of red paint are covering the eastern side. It’s the same message as the one you saw at the southern crossroads. “Don’t enter. Danger ahead.”
        \n\nYou look down the dark road, and hear the distant roar of a dragon.
        '
        'I ask The Wright for protection.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask The Wright for protection.')
            $ pc_faithpoints += 1
            $ custom1 = "You look at the blue sky, take a deep breath, then start humming an old tune. You don’t remember the words, but they tell the story of Sela, a brave soul from Wright’s Tablets, betrayed by his fellow warriors, abandoned in the wilderness, with no weapons to protect himself. Thanks to Wright’s inspiration, he realized that a lizard’s bone, the only thing left from his last meal, could be broken, sharpened, and used as the head of a spear. Thus, he managed to defeat a large cat, and returned to his family.\n\nThe road gets a bit brighter."
            jump stonesignfirsttime02
        'I think of a protective spell of my ancestors.' if pc_religion == "pagan" or pc_religion == "unknown":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think of a protective spell of my ancestors.')
            $ quarters += 1
            $ pc_faithpoints += 1
            $ custom1 = "You get on the ground and gather a couple of leaves, a fistful of soil, a stone, a bunch of berries, blades of grass, a mushroom... You make a “ball of the forest” and throw it as far away as you can, marking the road ahead. It {i}should{/i} keep monsters away."
            jump stonesignfirsttime02
        'I’m not ready to enter the heart of the forest.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m not ready to enter the heart of the forest.')
            $ custom1 = "You take a look at your bundles, mount, and weapons, then think about the beasts of the woods... You may not be able to outrun them."
            jump stonesignfirsttime02
        'I scratch {color=#f6d6bd}[horsename]’s{/color} neck. I’m ready.' if pc_likeshorsename:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I scratch {color=#f6d6bd}%s’s{/color} neck. I’m ready.' %horsename)
            $ custom1 = "You can’t help but smile. Your palfrey’s nicker brings you comfort. No matter how dark it’s going to get, the sky above your heads is bright and blue."
            jump stonesignfirsttime02
        'I crack my knuckles. I’m ready.' if not pc_likeshorsename:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I crack my knuckles. I’m ready.')
            $ custom1 = "You take another look at your equipment. It’s not much, but it got you so far. What matters is that you know how to use it."
            jump stonesignfirsttime02

    label stonesignfirsttime02:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '[custom1]
            '
            'I search for the tracks I found at the watchtower.' if watchtower_tracks and not stonesign_tracks and not shortcut_cairn_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search for the tracks I found at the watchtower.')
                jump stonesign_tracks01
            'Entering the forest this late is going to be my death. (disabled)' ( condition="quarters > (world_daylength-12)" ):
                pass
            'I travel as far {color=#f6d6bd}west{/color} as I can.' ( condition="not westgate_firsttime and quarters <= (world_daylength-12)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel as far {color=#f6d6bd}west{/color} as I can.')
                $ questionpreset = 0
                $ shortcut_inprogress = 1
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "westgate"
                jump shortcut01
            'I travel to the {color=#f6d6bd}gate in the west{/color}.' ( condition="westgate_firsttime and quarters <= (world_daylength-12)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel to the {color=#f6d6bd}gate in the west{/color}')
                $ questionpreset = 0
                $ shortcut_inprogress = 1
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "westgate"
                jump shortcut01
            'I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.' ( condition="shortcut_cairn_firsttime and quarters <= (world_daylength-12)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.')
                $ questionpreset = 0
                $ shortcut_inprogress = 1
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "cairn"
                jump shortcut01
            'I return to {color=#f6d6bd}the bandits’ hideout{/color}.' ( condition="banditshideout_firsttime and not banditshideout_banned and quarters <= (world_daylength-12)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the bandits’ hideout{/color}.')
                $ questionpreset = 0
                $ shortcut_inprogress = 1
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "hideout"
                jump shortcut01

label stonesignregular01:
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '[stonesign_fluff]
        '
        'I search for the tracks I found at the watchtower.' if watchtower_tracks and not stonesign_tracks and not shortcut_cairn_tracks:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search for the tracks I found at the watchtower.')
            jump stonesign_tracks01
        'Entering the forest this late is going to be my death. (disabled)' ( condition="quarters > (world_daylength-12)" ):
            pass
        'I travel as far {color=#f6d6bd}west{/color} as I can.' ( condition="not westgate_firsttime and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel as far {color=#f6d6bd}west{/color} as I can.')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "westgate"
            jump shortcut01
        'I travel to the {color=#f6d6bd}gate in the west{/color}.' ( condition="westgate_firsttime and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel to the {color=#f6d6bd}gate in the west{/color}')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "westgate"
            jump shortcut01
        'I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.' ( condition="shortcut_cairn_firsttime and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "cairn"
            jump shortcut01
        'I return to {color=#f6d6bd}the bandits’ hideout{/color}.' ( condition="banditshideout_firsttime and not banditshideout_banned and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the bandits’ hideout{/color}.')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "hideout"
            jump shortcut01

label stonesignregular01fromshortcut:
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'You leave the dark woods behind. [stonesign_fluff]
        '
        'I search for the tracks I found at the watchtower.' if watchtower_tracks and not stonesign_tracks and not shortcut_cairn_tracks:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search for the tracks I found at the watchtower.')
            jump stonesign_tracks01
        'Entering the forest this late is going to be my death. (disabled)' ( condition="quarters > (world_daylength-12)" ):
            pass
        'I travel as far {color=#f6d6bd}west{/color} as I can.' ( condition="not westgate_firsttime and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel as far {color=#f6d6bd}west{/color} as I can.')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "westgate"
            jump shortcut01
        'I travel to the {color=#f6d6bd}gate in the west{/color}.' ( condition="westgate_firsttime and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel to the {color=#f6d6bd}gate in the west{/color}')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "westgate"
            jump shortcut01
        'I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.' ( condition="shortcut_cairn_firsttime and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "cairn"
            jump shortcut01
        'I return to {color=#f6d6bd}the bandits’ hideout{/color}.' ( condition="banditshideout_firsttime and not banditshideout_banned and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the bandits’ hideout{/color}.')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "hideout"
            jump shortcut01

label stonesignfirsttime01fromshortcut:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown" or pc_religion == "pagan":
        $ pc_faithpoints_opportunities += 1
    menu:
        'The path leads you uphill. The trees are getting sparser and smaller, and more sunlight touches the ground.
        \n\nThe signs of human touch are rare - the lone, large boulder surely draws attention. You can’t guess its age, but the paths around suggest it was passed plenty of times already. The remains of red paint are covering the eastern side. It’s the same message as the one you saw at the southern crossroads. “Don’t enter. Danger ahead.”
        \n\nYou look behind you.
        '
        'I thank The Wright for protecting me.' if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I thank The Wright for protecting me.')
            $ custom1 = "You bow your head, but as you think of words of prayer, you’re beset by the memories of blood and eyes. You look around whenever you hear a rustle. Even your breath gets faster. You shake your head and grasp the reins firmly."
            $ pc_faithpoints += 1
            jump stonesignfullroad02
        'I thank my ancestors for keeping my senses sharp.' if pc_religion == "unknown" or pc_religion == "pagan":
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I thank my ancestors for keeping my senses sharp.')
            $ pc_faithpoints += 1
            $ custom1 = "You try to repeat the short ritual - one should clasp their hands, then touch the eyes... Or was it a nose? You start gesturing, hoping that the muscles will lead you through the confusion, but this only distracts you further. You’re beset by the memories of blood and eyes. You look around whenever you hear a rustle. Even your breath gets faster. You shake your head and grasp the reins firmly."
            jump stonesignfullroad02
        'I pat {color=#f6d6bd}[horsename]{/color}. It did well.' if pc_likeshorsename:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pat {color=#f6d6bd}%s{/color}. It did well.' %horsename)
            $ custom1 = "Your palfrey snorts and tosses its head, pinning its scared ears back. You’d like to tell it that you’re proud and grateful, but even if it could understand you, it wouldn’t listen."
            jump stonesignfullroad02
        'I sigh with relief. Who cares about signs - I made it.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh with relief. Who cares about signs - I made it.')
            $ custom1 = "You smile, then chuckle nervously, and finally break out in laughter. Your palfrey welcomes your voice with an annoyed snort. It moves forward without waiting for your order."
            jump stonesignfullroad02
        'I deserve rest in a good bed after that.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sigh with relief. I deserve a good bed after that.')
            $ custom1 = "Your arms and legs get heavier. You keep an eye on the road, and tell your palfrey to move along."
            jump stonesignfullroad02

    label stonesignfullroad02:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '[custom1]
            '
            'I search for the tracks I found at the watchtower.' if watchtower_tracks and not stonesign_tracks and not shortcut_cairn_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search for the tracks I found at the watchtower.')
                jump stonesign_tracks01
            'Entering the forest this late is going to be my death. (disabled)' ( condition="quarters > (world_daylength-12)" ):
                pass
            'I travel as far {color=#f6d6bd}west{/color} as I can.' ( condition="not westgate_firsttime and quarters <= (world_daylength-12)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel as far {color=#f6d6bd}west{/color} as I can.')
                $ questionpreset = 0
                $ shortcut_inprogress = 1
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "westgate"
                jump shortcut01
            'I travel to the {color=#f6d6bd}gate in the west{/color}.' ( condition="westgate_firsttime and quarters <= (world_daylength-12)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel to the {color=#f6d6bd}gate in the west{/color}')
                $ questionpreset = 0
                $ shortcut_inprogress = 1
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "westgate"
                jump shortcut01
            'I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.' ( condition="shortcut_cairn_firsttime and quarters <= (world_daylength-12)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.')
                $ questionpreset = 0
                $ shortcut_inprogress = 1
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "cairn"
                jump shortcut01
            'I return to {color=#f6d6bd}the bandits’ hideout{/color}.' ( condition="banditshideout_firsttime and not banditshideout_banned and quarters <= (world_daylength-12)" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the bandits’ hideout{/color}.')
                $ questionpreset = 0
                $ shortcut_inprogress = 1
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "hideout"
                jump shortcut01

label stonesign_tracks01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ stonesign_tracks = 1
    if quest_fallentree == 1:
        $ renpy.notify("Journal updated: Fallen Tree")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Fallen Tree{/i}')
    $ quest_fallentree_description02 = "Whoever was present at the wagon, was then passing by the abandoned watchtower, then entered the heart of the woods."
    menu:
        'The hard heels can’t be mistaken, and the travelers didn’t mask their steps. They passed the rock from both sides, heading deeper into the forest.
        '
        'I search for the tracks I found at the watchtower.' if watchtower_tracks and not stonesign_tracks and not shortcut_cairn_tracks:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I search for the tracks I found at the watchtower.')
            jump stonesign_tracks01
        'Entering the forest this late is going to be my death. (disabled)' ( condition="quarters > (world_daylength-12)" ):
            pass
        'I travel as far {color=#f6d6bd}west{/color} as I can.' ( condition="not westgate_firsttime and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel as far {color=#f6d6bd}west{/color} as I can.')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "westgate"
            jump shortcut01
        'I travel to the {color=#f6d6bd}gate in the west{/color}.' ( condition="westgate_firsttime and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel to the {color=#f6d6bd}gate in the west{/color}')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "westgate"
            jump shortcut01
        'I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.' ( condition="shortcut_cairn_firsttime and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "cairn"
            jump shortcut01
        'I return to {color=#f6d6bd}the bandits’ hideout{/color}.' ( condition="banditshideout_firsttime and not banditshideout_banned and quarters <= (world_daylength-12)" ):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the bandits’ hideout{/color}.')
            $ questionpreset = 0
            $ shortcut_inprogress = 1
            $ shortcut_traveled += 1
            $ travel_destination_shortcut = "hideout"
            jump shortcut01
