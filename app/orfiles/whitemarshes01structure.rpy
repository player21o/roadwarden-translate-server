###################### WHITE MARSHES
default whitemarshes_firsttime = 0 # day

default whitemarshes_opposition = 0
default whitemarshes_fluff = ""
default whitemarshes_fluff_old = ""
default whitemarshes_description2 = ""
default whitemarshes_description2_old = ""
default whitemarshes_reputation = 0

default whitemarshes_forestgardenabandoned = 0
default whitemarshes_spying_tried = 0
default whitemarshes_spying_completed = 0

default whitemarshes_observingundead = 0
default whitemarshes_rest_unlocked = 0
default whitemarshes_well = 0

default whitemarshes_valens_firsttime_day = 0
default whitemarshes_valens_firsttime = 0
default whitemarshes_valens_knowspccanread = 0
default whitemarshes_valens_questions1 = 0
default whitemarshes_valens_questions2 = 0
default whitemarshes_valens_questions3 = 0
default whitemarshes_valens_questions4 = 0
default whitemarshes_valens_angry = 0
default whitemarshes_valens_completion_day = 0
default whitemarshes_valens_sellingpoints = 0
default whitemarshes_valens_shop_unlocked = 0 # day
default whitemarshes_valens_shop_firsttime = 0
default whitemarshes_valens_fluff = ""

default whitemarshes_pursewoman = 0
default whitemarshes_pursewoman_talkedto = 0
default whitemarshes_pursewoman_questions1 = 0
default whitemarshes_pursewoman_questions2 = 0
default whitemarshes_pursewoman_questions3 = 0
default whitemarshes_pursewoman_questions4 = 0
default whitemarshes_pursewoman_questions5 = 0
default whitemarshes_pursewoman_coins = 0

default whitemarshes_child = 0
default whitemarshes_child_fluff = ""
default whitemarshes_child_asterion = 0

default whitemarshes_about_matchmaking = 0

label whitemarshes01:
    nvl clear
    $ pc_area = "whitemarshes"
    if not renpy.music.get_playing(channel='music') == "<loop 20.0>audio/dancaineinthedeepwoods_whitemarshes_loop.ogg":
        play music "<loop 20.0>audio/dancaineinthedeepwoods_whitemarshes_loop.ogg" fadeout 1.0 fadein 1.0
    stop nature fadeout 4.0
    label whitemarshes_fluffloop:
        if not whitemarshes_nomoreundead:
            $ whitemarshes_fluff = ""
            $ whitemarshes_fluff = renpy.random.choice(['The village is filled with the unbearable noise of construction, yet the undead laborers take no breaks, don’t gasp for air, don’t stop to look around. The locals avoid them, or scowl at them whenever they get close.', 'Most of the undead are in the fields, but you could swear that one of the skeletons is staring at your axe - you step aside, and the absent gaze of its empty sockets doesn’t move.', 'For a few breaths, you see more undead than locals - they’re gathered at the well, allowing the overseers to inspect their missing limbs.', 'You ride along a trail of blood, which disappears near the well. The locals spread quickly, leaving you with a few guards and many, many more awoken shells.', 'The group that you encountered at the old forest garden is close to the gate. During their training, they use a meatless undead ordered to dodge their attacks.'])
            if whitemarshes_fluff_old == whitemarshes_fluff:
                jump whitemarshes_fluffloop
            else:
                $ whitemarshes_fluff_old = whitemarshes_fluff
        elif (whitemarshes_nomoreundead+1) < day:
            $ whitemarshes_fluff = "The flames in the back of the village are taller than the roofs, and your nostrils are filled with the stench of burnt flesh. The grim scowls of the locals, who are now forced to tame the bogs on their own, are followed by their quick departures."
        else:
            $ whitemarshes_fluff = "Aside from the gatekeepers, you hardly see a soul. A few of the locals come around, making sure no threat has arrived, but no one approaches you. The locals move slowly, yawning and trudging, and the previously loud tools and building materials are now abandoned."
    $ shop = "helvius"
    if not whitemarshes_firsttime:
        $ world_known_npcs += 2
        $ world_known_areas += 1
        $ whitemarshes_firsttime = day
        $ bogcrossroads_unlocked = 1
        $ peatfield_unlocked = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ whitemarshes_child_fluff = ""
        if not pc_firstvillage:
            $ pc_firstvillage = "whitemarshes"
        show areapicture whitemarshes01 at basicfade
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump whitemarshesfirsttime01
    else:
        if quest_readtheletter == 2:
            $ whitemarshes_pursewoman = 1
        if whitemarshes_pursewoman_talkedto:
            $ whitemarshes_pursewoman = 0
        if whitemarshes_nomoreundead:
            $ whitemarshes_pursewoman = 0
        if not whitemarshes_valens_firsttime and not whitemarshes_attacked and not whitemarshes_destroyed:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            show areapicture bogcrossroadstowhitemarshes at basicfade
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ renpy.force_autosave(take_screenshot=True, block=True)
            jump whitemarshes_valens01
        if whitemarshes_valens_firsttime and whitemarshes_valens_firsttime_day+5 <= day and not item_letterwhitemarshes and not whitemarshes_valens_angry and not quest_readtheletter_description01 and not quest_readtheletter_description01alt and not quest_readtheletter_description04:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            show areapicture bogcrossroadstowhitemarshes at basicfade
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ renpy.force_autosave(take_screenshot=True, block=True)
            jump whitemarshes_valens00fail
        if whitemarshes_firsttime < day and not whitemarshes_child:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            show areapicture bogcrossroadstowhitemarshes at basicfade
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ renpy.force_autosave(take_screenshot=True, block=True)
            jump whitemarshes_child01
        else:
            $ can_leave = 1
            if whitemarshes_rest_unlocked:
                $ can_rest = 1
            $ can_items = 1
            show areapicture whitemarshes01 at basicfade
            $ whitemarshes_child_fluff = ""
            with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
            $ renpy.force_autosave(take_screenshot=True, block=True)
            jump whitemarshesregular01

label whitemarshesfirsttime01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ description_whitemarshes01 = "A village of foragers and peat gatherers set among the western bogs."
    menu:
        'The guards let you in without questioning. The entrance, and the wall in general, were recently constructed, though are still not finished - there will soon be yet another gate, allowing for trade and conversations without opening the village to danger.
        \n\nJust like in the fields, the work is divided between the undead, who carry bricks and take care of the most thankless tasks, while the locals cut rocks and spread mortar. The difficult past is still carved in the villagers’ gaunt faces and crude outfits, and their brief glances show little curiosity. A few of them are sharing a meal right next to the well, and the victuals in their baskets consist of green leaves, fruits, eggs, and cuts of roasted meat. The food of foragers.
        \n\nYou’re told to wait here for {color=#f6d6bd}the mayor{/color}. “Don’t roam on your own,” the guard’s voice is harsh, despite the stutter.
        '
        'I tether {color=#f6d6bd}[horsename]{/color} at a small shed.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tether {color=#f6d6bd}%s{/color} at a small shed.' %horsename)
            if bogentrance_dialogue_friendship >= 2:
                $ whitemarshes_reputation += 1
                $ custom1 = "The rider from the forest garden, an’ still in one piece. Not scared f’the bogs, nor our green wall, I see. Ba I still don’t know who you are, stranger."
            elif bogentrance_dialogue_friendship >= 0:
                $ whitemarshes_reputation += 1
                $ custom1 = "The stranger from the forest garden. I canna guess why you wad come here. Who are you, even?"
            else:
                $ whitemarshes_reputation -= 1
                $ custom1 = "You’re that intruder from the forest garden. So our green wall was not nuff to stop you,” he smirks. “Who are you, even?"
            $ helvius_lastdayofvisit = day
            $ description_whitemarshes_helvius01 = "The mayor of the village is known as {color=#f6d6bd}Helvius{/color}."
            menu:
                'The man shows up soon after, with a careless saunter, and he hardly spares you a look, instead staring at your palfrey. “[custom1]”
                \n\nHis stature would be considered {i}average{/i} in most villages, but in comparison to the rest of his tribe, he’s portly, muscular, tall, and with a large, square face. His hands are resting on the shaft of the poleaxe placed across his shoulders, making him seem even larger. His long, straw-colored beard is shabby, and makes his bald head look shiny. You can’t really tell how old he is, though you see no wrinkles.
                \n\nJust like the others, he’s wearing prominent charms, favoring tiny figurines of animals made of bone and wood. Only one of them is hanging from his neck - a silver amulet portraying the head of a moose with large antlers. While valuable, it looks older than the other critters, and quite crude in form.
                '
                'I introduce myself.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I introduce myself.')
                    $ at_activate = 1
                    $ at = 0
                    menu:
                        'He sizes you up. “And I’m {color=#f6d6bd}Helvius{/color}. Who let you in, was it {color=#f6d6bd}Thyrsus{/color}? He’s as much’a gatekeeper as a fly’s {i}a warden{/i} to a piece of shit,” he gives you a telling frown.
                        '
                        ' (disabled)' ( condition="at == 0" ):
                            pass
                        '“I’m not one to badmouth others behind their backs.”' ( condition="at == 'friendly'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “I’m not one to badmouth others behind their backs.”')
                            $ at_activate = 0
                            $ at = 0
                            $ whitemarshes_reputation -= 1
                            $ custom1 = "“Did I ask?” He raises his chin and starts to twist his wrists, spinning his weapon slowly. “No cityfolk will tell us what to think. Take a good look around while you can. {color=#f6d6bd}White Marshes{/color} isn’t for strangers.”"
                            jump whitemarshesfirsttime02
                        '“Who knows,” I half-whisper. “Maybe I got here all by myself, chopped those creepers into a salad?”' ( condition="at == 'playful'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “Who knows,” I half-whisper. “Maybe I got here all by myself, chopped those creepers into a salad?”')
                            $ at_activate = 0
                            $ at = 0
                            $ custom1 = "He stares at you for a good few breaths, until your smile makes him shake his head. “Don’t play a monkey with me. These bogs’ve been our tribe’s home for years, as well’s all the things growing in them. We gave them their shape, an’ we need no cityfolk to push their will upon them.” He starts to twist his wrists, spinning his weapon slowly. “Take a good look around while you can. {color=#f6d6bd}White Marshes{/color} isn’t for strangers.”"
                            jump whitemarshesfirsttime02
                        '“I’m sure he realized I may be of use here.”' ( condition="at == 'distanced'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - “I’m sure he realized I may be of use here.”')
                            $ at_activate = 0
                            $ at = 0
                            $ custom1 = "“Don’t boast, those like you help others when your pouch gets empty, an’ we’ve no need of you here.” He starts to twist his wrists, spinning his weapon slowly. “Take a good look around while you can. {color=#f6d6bd}White Marshes{/color} isn’t for strangers.”"
                            jump whitemarshesfirsttime02
                        'I smile. “Watch your tone.”' ( condition="at == 'intimidating'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - I smile. “Watch your tone.”')
                            $ at_activate = 0
                            $ at = 0
                            $ whitemarshes_reputation += 1
                            if pc_hp >= 3:
                                $ custom1 = "Your eyes meet. His cheek moves as if it’s chewing something, then stops. The man looks away. “Well, you’re in {color=#f6d6bd}White Marshes{/color} now, yet you’ve got no wagons of wares, an’ I’ve no need of you. You can get back on the roads.”"
                            else:
                                $ custom1 = "Your eyes meet. His cheek moves as if it’s chewing something, then stops. You’re the first one to look away, but the man’s tone isn’t as scornful anymore. “Well, you’re in {color=#f6d6bd}White Marshes{/color} now, yet you’ve got no wagons of wares, an’ I’ve no need of you. You can get back on the roads.”"
                            jump whitemarshesfirsttime02
                        'I shrug. “He could tell I won’t hurt you.”' ( condition="at == 'vulnerable'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I shrug. “He could tell I won’t hurt you.”')
                            $ at_activate = 0
                            $ at = 0
                            $ whitemarshes_reputation -= 1
                            if pc_hp >= 3:
                                $ custom1 = "“To me you look like you’ve got nuff muscle behind that fist,” he raises his chin, “but I guess one coward wad recognize another. {i}Welcome{/i} to {color=#f6d6bd}White Marshes{/color}, ba don’t stay for long. You’ve got no wagons of wares, an’ I’ve no need of you. Take a good look around while you can.”"
                            else:
                                $ custom1 = "“I guess one coward wad recognize another,” he raises his chin. “{i}Welcome{/i} to {color=#f6d6bd}White Marshes{/color}, ba don’t stay for long. You’ve got no wagons of wares, an’ I’ve no need of you. Take a good look around while you can.”"
                            jump whitemarshesfirsttime02

    label whitemarshesfirsttime02:
        menu:
            '[custom1]
            \n\nThe turf houses are old, covered with lush grasses and flowers, and you can’t imagine any large family fitting inside such small, one-chambered huts. The alleys are so narrow that only one cart could squeeze through them at once. Your boots have sunk into the mud - the square is covered with deep boot prints. The noise of hammers, shouting, wood splitting, and the shuffling of undead legs pierces through the constant buzzing of insects. {color=#f6d6bd}[horsename]{/color} snorts, hunting down flies with its tail.
            '
            'I notice that there’s only one elder in sight. And he’s observing me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I notice that there’s only one elder in sight. And he’s observing me.')
                $ description_orentius00 = "The priest living in {color=#f6d6bd}White Marshes{/color}, the leader of the local fellowship of The Wright. Known for his necromantic practices."
                $ questionpreset = "helvius1"
                menu:
                    'He’s standing on the top of a wooden platform, by the building that’s unlike any other in the village. His eyes are keen - the left one is dark, the right one is gray, bright. His head and face are shaved, and his simple undyed robe is in even worse shape than the outfits of his tribesfolk.
                    \n\nOnce {color=#f6d6bd}Helvius{/color} realizes what you’re looking at, he lowers his weapon and clears his throat, like a boy caught red-handed. {color=#f6d6bd}The elder{/color} walks away, holding a walking stick with one hand, and touching a wall with the other. “{color=#f6d6bd}Orentius{/color},” says {color=#f6d6bd}the mayor{/color}, “the priest of our fellowship an’ the one who saved our people,” he raises his hand, pointing at the dead shells bustling around the construction site.
                    '
                    '(helvius1 set)':
                        pass

label whitemarshesregular01:
    if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto:
        $ custom2 = "\n\nYou notice a skinny woman with a blue headscarf. She stares at your mount like a wolf at an elk."
    else:
        $ custom2 = ""
    $ can_leave = 1
    if whitemarshes_rest_unlocked:
        $ can_rest = 1
    $ can_items = 1
    menu:
        '[whitemarshes_child_fluff][whitemarshes_fluff][custom2]
        '
        'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
            jump whitemarsheshelviusregular01
        'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_firsttime01
        'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_regular01
        'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
            pass
        'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
            pass
        'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
            $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
            jump whitemarshes_valens02
        'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
            pass
        'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
            jump whitemarshesquest_hiddenpurse01
        'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
            pass
        'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
            jump whitemarshesquest_hiddenpurse02
        'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
            jump whitemarshes_about_matchmaking01
        'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
            jump whitemarshesaskingforroom01
        'I approach the well.' if not whitemarshes_well:
            jump whitemarsheswell01
        'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
            jump whitemarshes_observingundead01

label whitemarshesafterinteraction01:
    if not quest_orentius_thais_description02:
        $ quest_orentius_thais_description02 = "I spent some time in {color=#f6d6bd}White Marshes{/color}. I should report back to Thais."
        if quest_orentius == 1 and quest_orentius_thais_description00 and quest_orentius_thais_description01 and not quest_orentius_thais_description00betrayal:
            $ renpy.notify("Journal updated: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Orentius, the Necromancer{/i}')
    $ can_leave = 1
    if whitemarshes_rest_unlocked:
        $ can_rest = 1
    $ can_items = 1
    if not whitemarshes_nomoreundead:
        $ custom1 = renpy.random.choice(['The locals keep their distance - both from you, and from their undead workers.', 'A sudden shout cuts the sky, but no one pays attention to it. It turns out a small boy got scared by the quiet approach of an awoken shell.', 'The shuffling gait of an undead, still covered with flesh, makes all the other sounds weirdly quiet.', 'A group of children is sitting in a circle, being taught by a teenager how to carve in bone. They’re skinny, and one of them is sobbing.', 'One of the undead workers drops a basket of foraged cranberries and leaves, maybe because its shell is too weak, or maybe because it received a poorly phrased order. It then stays still, waiting for further instructions.', 'You hear a weak moan coming from one of the houses.', 'You notice that all the flies land either on the locals, or on your palfrey - they avoid the awoken shells, without exception.'])
    else:
        $ custom1 = renpy.random.choice(['The locals keep their distance, focused on their overwhelming work.', 'A few young women carry logs of wood, piling them by a wall. They seem exhausted.', 'A group of children is sitting in a circle, being taught by a teenager how to carve in bone. They’re skinny, and one of them is sobbing.', 'A man without legs is sitting above dozens of fruits and mushrooms spread on the ground. He picks them one by one, judging if they should be thrown away.', 'A few farmers try to wash their hands in already dirty water.', 'A few people argue over who’s the “rightful” owner of a basket of purplish leaves and tiny berries. Their scowls warn you to stay out of it.', 'The group that you encountered at the old forest garden is preparing for its next expedition.'])
    if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto:
        $ custom2 = "\n\nYou notice a skinny woman with a blue headscarf. She stares at your mount like a wolf at an elk."
    else:
        $ custom2 = ""
    menu:
        '[custom1][custom2]
        '
        'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
            jump whitemarsheshelviusregular01
        'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_firsttime01
        'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_regular01
        'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
            pass
        'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
            pass
        'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
            $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
            jump whitemarshes_valens02
        'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
            pass
        'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
            jump whitemarshesquest_hiddenpurse01
        'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
            pass
        'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
            jump whitemarshesquest_hiddenpurse02
        'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
            jump whitemarshes_about_matchmaking01
        'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
            jump whitemarshesaskingforroom01
        'I approach the well.' if not whitemarshes_well:
            jump whitemarsheswell01
        'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
            jump whitemarshes_observingundead01

label whitemarshesrejectedbyhelvius01:
    $ can_leave = 1
    if whitemarshes_rest_unlocked:
        $ can_rest = 1
    $ can_items = 1
    menu:
        '[custom1]
        '
        'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
            jump whitemarsheshelviusregular01
        'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_firsttime01
        'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_regular01
        'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
            pass
        'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
            pass
        'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
            $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
            jump whitemarshes_valens02
        'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
            pass
        'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
            jump whitemarshesquest_hiddenpurse01
        'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
            pass
        'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
            jump whitemarshesquest_hiddenpurse02
        'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
            jump whitemarshes_about_matchmaking01
        'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
            jump whitemarshesaskingforroom01
        'I approach the well.' if not whitemarshes_well:
            jump whitemarsheswell01
        'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
            jump whitemarshes_observingundead01

label whitemarshesaftersleep:
    $ can_leave = 1
    if whitemarshes_rest_unlocked:
        $ can_rest = 1
    $ can_items = 1
    if not renpy.music.get_playing(channel='music') == "<loop 20.0>audio/dancaineinthedeepwoods_whitemarshes_loop.ogg":
        play music "<loop 20.0>audio/dancaineinthedeepwoods_whitemarshes_loop.ogg" fadeout 1.0 fadein 1.0
    stop nature fadeout 4.0
    show areapicture whitemarshes01 at basicfade
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ vines_open_sleep = day
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    if not whitemarshes_nomoreundead and not whitemarshes_nomoreundeadfirstsleepdescription:
        $ custom1 = "Even though the village seems to be on its legs, most shells you spot are dead, just as occupied as they were during the night."
    else:
        $ custom1 = "The night watch is heading in to rest, while the day guards are putting on their gambesons. The locals have just started preparing for work, yet they already seem tired. The village is oddly silent."
        if whitemarshes_nomoreundeadfirstsleepdescription == 1:
            $ whitemarshes_nomoreundeadfirstsleepdescription = 0
            jump whitemarshesaftersleepalt
    menu:
        '[custom1]
        '
        'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
            jump whitemarsheshelviusregular01
        'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_firsttime01
        'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_regular01
        'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
            pass
        'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
            pass
        'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
            $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
            jump whitemarshes_valens02
        'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
            pass
        'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
            jump whitemarshesquest_hiddenpurse01
        'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
            pass
        'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
            jump whitemarshesquest_hiddenpurse02
        'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
            jump whitemarshes_about_matchmaking01
        'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
            jump whitemarshesaskingforroom01
        'I approach the well.' if not whitemarshes_well:
            jump whitemarsheswell01
        'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
            jump whitemarshes_observingundead01

    label whitemarshesaftersleepalt:
        $ achievement_pyrepoints += 1
        $ quarters += 4
        $ whitemarshes_nomoreundead = day
        $ orentius_convinced = 1
        $ quest_orentius = 2
        $ can_leave = 1
        if whitemarshes_rest_unlocked:
            $ can_rest = 1
        $ can_items = 1
        if pc_goal == "iwanttoberemembered":
            $ pc_goal_iwanttoberememberedpoints += 2
        if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
            $ renpy.notify("Quest completed: Orentius, the Necromancer.\nJournal updated: %s" %quest_pc_goal_name)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer. Journal updated: %s{/i}' %quest_pc_goal_name)
        else:
            $ renpy.notify("Quest completed: Orentius, the Necromancer")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Orentius, the Necromancer{/i}')
        if thyrsus_orentius_helped:
            $ quest_orentius_thyrsus_description03 = "Thanks to me, {color=#f6d6bd}White Marshes{/color} abandoned their necromantic practices."
        if helvius_orentius_helped:
            $ quest_orentius_helvius_description03 = "Thanks to me, {color=#f6d6bd}White Marshes{/color} abandoned their necromantic practices."
        menu:
            'You wake up to the terrible stench of burning, rotten flesh. Once you leave the shed, you head to {color=#f6d6bd}[horsename]{/color} quickly - it’s sleepy, hugging a corner as it trembles, but you find no wounds on it, nor any issues with your bundles.
            \n\nAs you spend a few minutes to help it relax, you finally realize there are no undead in sight - the pyres beneath their gathered corpses are far away, in the back of the village, but the flames and smoke are visible even from a great distance.
            \n\nThere’s a large group surrounding {color=#f6d6bd}Orentius’{/color} house. The rumor reaches you on its own - soon after the first awoken was touched by fire, the priest collapsed. He now mutters through his visions, but doesn’t wake up.
            '
            'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
                jump whitemarsheshelviusregular01
            'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
                jump whitemarshes_valens_shop_firsttime01
            'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
                jump whitemarshes_valens_shop_regular01
            'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
                pass
            'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
                pass
            'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
                jump whitemarshestryingtospy01
            'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
                $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
                jump whitemarshes_valens02
            'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
                pass
            'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
                jump whitemarshesquest_hiddenpurse01
            'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
                pass
            'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
                jump whitemarshesquest_hiddenpurse02
            'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
                jump whitemarshes_about_matchmaking01
            'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
                jump whitemarshestryingtospy01
            'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
                jump whitemarshesaskingforroom01
            'I approach the well.' if not whitemarshes_well:
                jump whitemarsheswell01
            'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
                jump whitemarshes_observingundead01

label whitemarshesaskingforroom01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ask the guards if there’s a room I could rent for the night.')
    $ whitemarshes_rest_unlocked = 1
    $ can_leave = 1
    if whitemarshes_rest_unlocked:
        $ can_rest = 1
    $ can_items = 1
    $ minutes += 5
    $ renpy.notify("New shelter unlocked.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
    menu:
        '“I guess,” one of them sighs and tells you to wait where you’re standing. After a few minutes, a group of locals approaches a more neglected turf house and starts to empty it. They take out old crates, rags, casks, bricks... Then leave them by the outer wall, at least for now.
        \n\n“T’s an old shed,” explains the guard. “There, you won’t bother anyone. Will be ready before you need it.”
        '
        'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
            jump whitemarsheshelviusregular01
        'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_firsttime01
        'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_regular01
        'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
            pass
        'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
            pass
        'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
            $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
            jump whitemarshes_valens02
        'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
            pass
        'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
            jump whitemarshesquest_hiddenpurse01
        'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
            pass
        'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
            jump whitemarshesquest_hiddenpurse02
        'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
            jump whitemarshes_about_matchmaking01
        'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
            jump whitemarshesaskingforroom01
        'I approach the well.' if not whitemarshes_well:
            jump whitemarsheswell01
        'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
            jump whitemarshes_observingundead01

label whitemarsheswell01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the well.')
    $ can_leave = 1
    if whitemarshes_rest_unlocked:
        $ can_rest = 1
    $ can_items = 1
    $ whitemarshes_well = 1
    menu:
        'The locals observe your hands carefully while you’re drawing the water. After you quench your thirst, you try to wash your face and neck, but one of the older women approaches you quickly, wagging her finger. “We’ve not nuff for this silliness,” she rebukes you. “Water your horse if you {i}have to{/i}, ba we need the rest for ourselves.”
        \n\nThe stern gaze of the other villagers leaves you no room for discussion.
        '
        'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
            jump whitemarsheshelviusregular01
        'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_firsttime01
        'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_regular01
        'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
            pass
        'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
            pass
        'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
            $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
            jump whitemarshes_valens02
        'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
            pass
        'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
            jump whitemarshesquest_hiddenpurse01
        'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
            pass
        'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
            jump whitemarshesquest_hiddenpurse02
        'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
            jump whitemarshes_about_matchmaking01
        'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
            jump whitemarshesaskingforroom01
        'I approach the well.' if not whitemarshes_well:
            jump whitemarsheswell01
        'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
            jump whitemarshes_observingundead01

label whitemarshes_observingundead01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe the undead workers.')
    $ whitemarshes_observingundead = 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ minutes += 5
    $ description_whitemarshes02a = "Quite a few people can give them orders."
    menu:
        'Not being allowed to leave the main square, you observe the shells walking through the gate or helping the builders at the wall. The skeletons are not at all complete - some of them lack a rib, a foot, or a jaw. Many of their bones are cracked or broken, and seem to be connected to each other with nothing at all, as if the pneuma that keeps them moving “knows” which parts should stay firm, and which ones should twist or bend.
        \n\nThose that kept some of their skin and guts don’t smell, rot, or bleed, and make you think of dried meat. It’s as if these scraps of flesh serve no purpose, and seeing how many of these laborers already have great holes in their stomachs, or limbs with revealed bones, it could be that they are just in the middle of the process of becoming like their “naked” counterparts.
        \n\nThe undead loyally fulfill their tasks. So far, you’ve counted five people able to give them orders. Some do so by speaking out loud, while one woman simply looks at a shell, no matter how far it is. The workers, while witless, maintain some sort of carefulness in their actions - they stop when someone gets in their way, and use tools, if they know how, avoiding pointless harm to their shells.
        \n\nThere may be more than fifty creatures spread across and around the village, but you can’t know how many you haven’t seen yet. Many of the fresher undead are elders. Among the skeletons, you spot some that used to belong to children, but none to infants.
        '
        'Maybe such young shells are too difficult a sight even for the locals.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe such young shells are too difficult a sight even for the locals.')
            jump whitemarshesafterinteraction01
        'Maybe they are so different from adult humans that they can’t be awoken.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe they are so different from adult humans that they can’t be awoken.')
            jump whitemarshesafterinteraction01
        'Maybe their shells are too weak to work, or too dumb to listen to orders.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe their shells are too weak to work, or too dumb to listen to orders.')
            jump whitemarshesafterinteraction01

label whitemarshes_about_matchmaking01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I address the guards. “People from the other tribes are looking for spouses.”')
    $ whitemarshes_about_matchmaking = 1
    $ renpy.notify("Journal updated: Matchmaking")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Matchmaking{/i}')
    $ pc_lies += 1
    $ can_leave = 1
    if whitemarshes_rest_unlocked:
        $ can_rest = 1
    $ can_items = 1
    if whitemarshes_nomoreundead:
        $ custom1 = "The taller gatekeeper gives you a long look. “First we need to learn who we are. An’ most of our young members left the village long before your arrival, stranger.”"
    else:
        $ custom1 = "The taller gatekeeper gives you a long look. “We need no matchmaker here. Our youth’s work to do, only then they’re free to go wherever they want.”\n\nAfter you ask if the village is open to invite new dwellers, he snorts. “You think they’re going to move to the {i}village of the dead{/i}? Good joke.”"
    menu:
        '[custom1]
        '
        'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
            jump whitemarsheshelviusregular01
        'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_firsttime01
        'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
            jump whitemarshes_valens_shop_regular01
        'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
            pass
        'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
            pass
        'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
            $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
            jump whitemarshes_valens02
        'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
            pass
        'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
            jump whitemarshesquest_hiddenpurse01
        'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
            pass
        'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
            jump whitemarshesquest_hiddenpurse02
        'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
            jump whitemarshes_about_matchmaking01
        'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
            jump whitemarshestryingtospy01
        'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
            jump whitemarshesaskingforroom01
        'I approach the well.' if not whitemarshes_well:
            jump whitemarsheswell01
        'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
            jump whitemarshes_observingundead01

label whitemarshestryingtospy01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ whitemarshes_spying_tried = 1
    menu:
        'You leave {color=#f6d6bd}[horsename]{/color} at the well and head between the turf houses, but you then hear the heavy steps of one of the armored guards. “What’s this,” he places a hand on your shoulder and turns you around. “Getting homely?”
        '
        '(lie) “I’m just looking around. I have dragon bones to spend, you know.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’m just looking around. I have dragon bones to spend, you know.”')
            $ quest_spyonwhitemarshes_description01a = "The locals won’t let me wander around their village. Maybe I could take a closer look at it when there’s fewer curious eyes."
            $ renpy.notify("Journal updated: Spy on White Marshes")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Spy on White Marshes{/i}')
            $ pc_lies += 1
            $ can_leave = 1
            if whitemarshes_rest_unlocked:
                $ can_rest = 1
            $ can_items = 1
            menu:
                'He stares into your eyes, and you catch a whiff of mint leaves. Finally, he takes his hand back. “Well, we don’t need them, an’ don’t allow strangers to loaf around.” He nods at the gate and makes you follow him. “Stay in sight, warden.”
                '
                'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
                    jump whitemarsheshelviusregular01
                'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
                    jump whitemarshes_valens_shop_firsttime01
                'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
                    jump whitemarshes_valens_shop_regular01
                'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
                    pass
                'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
                    pass
                'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
                    jump whitemarshestryingtospy01
                'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
                    $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
                    jump whitemarshes_valens02
                'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
                    pass
                'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
                    jump whitemarshesquest_hiddenpurse01
                'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
                    pass
                'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
                    jump whitemarshesquest_hiddenpurse02
                'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
                    jump whitemarshes_about_matchmaking01
                'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
                    jump whitemarshestryingtospy01
                'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
                    jump whitemarshesaskingforroom01
                'I approach the well.' if not whitemarshes_well:
                    jump whitemarsheswell01
                'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
                    jump whitemarshes_observingundead01
        '“What’s the problem?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s the problem?”')
            $ whitemarshes_reputation -= 1
            $ quest_spyonwhitemarshes_description01a = "The locals won’t let me wander around their village. Maybe I could take a closer look at it when there’s fewer curious eyes."
            $ renpy.notify("Journal updated: Spy on White Marshes")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Spy on White Marshes{/i}')
            $ can_leave = 1
            if whitemarshes_rest_unlocked:
                $ can_rest = 1
            $ can_items = 1
            menu:
                '“Your nose,” he scoffs. “Don’t loaf around, stranger.” He harshly pulls you toward the gate. “Stick to your beast.” You hear a few onlookers wonder aloud about what you were looking for.
                '
                'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
                    jump whitemarsheshelviusregular01
                'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
                    jump whitemarshes_valens_shop_firsttime01
                'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
                    jump whitemarshes_valens_shop_regular01
                'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
                    pass
                'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
                    pass
                'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
                    jump whitemarshestryingtospy01
                'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
                    $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
                    jump whitemarshes_valens02
                'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
                    pass
                'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
                    jump whitemarshesquest_hiddenpurse01
                'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
                    pass
                'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
                    jump whitemarshesquest_hiddenpurse02
                'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
                    jump whitemarshes_about_matchmaking01
                'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
                    jump whitemarshestryingtospy01
                'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
                    jump whitemarshesaskingforroom01
                'I approach the well.' if not whitemarshes_well:
                    jump whitemarsheswell01
                'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
                    jump whitemarshes_observingundead01
        '“Get your hand off me.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Get your hand off me.”')
            $ quest_spyonwhitemarshes_description01a = "The locals won’t let me wander around their village. Maybe I could take a closer look at it when there’s fewer curious eyes."
            $ renpy.notify("Journal updated: Spy on White Marshes")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Spy on White Marshes{/i}')
            $ can_leave = 1
            if whitemarshes_rest_unlocked:
                $ can_rest = 1
            $ can_items = 1
            menu:
                '“Or what, you’re going to cut it off?” He smirks, but your frown makes him step away. “To the gate, warden. We don’t allow strangers to loaf around.” You consider ignoring his order, but the man’s companions are already on their way. For now, you wander back, speaking with no one.
                '
                'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
                    jump whitemarsheshelviusregular01
                'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
                    jump whitemarshes_valens_shop_firsttime01
                'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
                    jump whitemarshes_valens_shop_regular01
                'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
                    pass
                'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
                    pass
                'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
                    jump whitemarshestryingtospy01
                'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
                    $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
                    jump whitemarshes_valens02
                'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
                    pass
                'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
                    jump whitemarshesquest_hiddenpurse01
                'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
                    pass
                'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
                    jump whitemarshesquest_hiddenpurse02
                'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
                    jump whitemarshes_about_matchmaking01
                'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
                    jump whitemarshestryingtospy01
                'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
                    jump whitemarshesaskingforroom01
                'I approach the well.' if not whitemarshes_well:
                    jump whitemarsheswell01
                'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
                    jump whitemarshes_observingundead01

label whitemarshesquest_hiddenpurseALL:
    label whitemarshesquest_hiddenpurse01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the woman who observes {color=#f6d6bd}%s{/color}.' %horsename)
        $ whitemarshes_pursewoman_talkedto = 1
        $ whitemarshes_pursewoman = 0
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'She moves away, but meets your eyes and makes a smile-like grimace, then leads you behind the empty animal pen, away from the guards’ ears. Her gray hair, mostly covered, is deceiving - she’s no older than thirty, yet her face is marked by insect bites and pustule scars. She takes confident steps, even though she wears muddy footwraps without boots, and a worn, simple skirt. She squeezes the front of her scarf on her chest, shaping it into something like a short, hooded cloak.
            \n\n“A warden, I heard?” She answers your nod by pursing her lips. “I need you to ride somewhere for me.”
            '
            '“Tell me.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me.”')
                menu:
                    '“Far away from here, at the eastern road, the’s an old bridge made f’a single rock,” she doesn’t look away for even a single heartbeat. Her gaunt face is pale, and makes her large, gray eyes look as if someone took their color away. “Beneath it, there’s a rock, and beneath the rock, a purse with {i}my{/i} savings. Bring it to me.”
                    \n\nBefore you mention your reward, she starts to speak faster, giving the men at the gate a nervous glance. “Half of what you’ll find is yours, bring me the rest.”
                    '
                    '“Oh, I already found it.”' if stonebridge_bridge_under:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Oh, I already found it.”')
                        $ custom1 = "She gives you a puzzled look, maybe wondering how to ask what pushed you to dig in the muddy river banks, but after seeing the curious looks of the guards, she leads you behind a turf house, and simply reaches out to you with an open palm."
                        jump whitemarshesquest_hiddenpurse02after
                    '“How much {i}should{/i} be there?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How much {i}should{/i} be there?”')
                        $ custom1 = "“Twenty bones, if that old fool didn’t try to scam me,” she takes a deep breath. “Half f’it’s more than worth the effort.”"
                        jump whitemarshesquest_hiddenpurse01a
                    '“I’d rather ask you a few questions about the village instead.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d rather ask you a few questions about the village instead.”')
                        $ custom1 = "“I’m not risking as much’s a broken nail before you show me the bones,” her clenched fist moves left and right, as if to replace the shake of her head."
                        jump whitemarshesquest_hiddenpurse01a
                    '“And you’re sure it’s {i}yours{/i}?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “And you’re sure it’s {i}yours{/i}?”')
                        $ custom1 = "“Do I look like a treasure hunting madcap? T’s an old payment my client failed to bring me back.”"
                        jump whitemarshesquest_hiddenpurse01a
                    '“Are you in trouble?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you in trouble?”')
                        $ custom1 = "She hesitates a bit too long. “F’course not. Ba a few dragons canna bite, can they?”"
                        jump whitemarshesquest_hiddenpurse01a
                    '“Would {color=#f6d6bd}Helvius{/color} approve of this?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Would {color=#f6d6bd}Helvius{/color} approve of this?”')
                        $ quest_hiddenpurse_description00a = "It seems like it would be better for her to not mention it to {color=#f6d6bd}Helvius{/color}."
                        $ custom1 = "The fingers of her clenched fist turned white. “He doesn’t need to know, so why does that matter?”"
                        jump whitemarshesquest_hiddenpurse01a

    label whitemarshesquest_hiddenpurse01a:
        $ quest_hiddenpurse = 1
        $ renpy.notify("New entry: A Hidden Pouch")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: A Hidden Pouch{/i}')
        $ can_leave = 1
        if whitemarshes_rest_unlocked:
            $ can_rest = 1
        $ can_items = 1
        menu:
            '[custom1] Seeing the curious looks of the guards, she shakes her head and leaves you to yourself as she passes by a flesh-bearing undead.
            '
            'I go to {color=#f6d6bd}Helvius{/color}.' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid != day:
                jump whitemarsheshelviusregular01
            'I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.' if whitemarshes_valens_shop_unlocked and whitemarshes_valens_shop_unlocked < day and not whitemarshes_valens_shop_firsttime:
                jump whitemarshes_valens_shop_firsttime01
            'I approach {color=#f6d6bd}Valens{/color}.' if whitemarshes_valens_shop_firsttime:
                jump whitemarshes_valens_shop_regular01
            'Helvius is barely tolerating my presence here. (disabled)' if helvius_about_nomoreundead:
                pass
            'Helvius is nowhere in sight. (disabled)' if not helvius_about_nomoreundead and helvius_about_oldtunnel_paid == day:
                pass
            'I should take a stroll and learn more about this place, so I can then report back to {color=#f6d6bd}Glaucia{/color}.' if quest_spyonwhitemarshes == 1 and not whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
                jump whitemarshestryingtospy01
            'I should speak with {color=#f6d6bd}Valens{/color}.' if quest_readtheletter == 1 and item_letterwhitemarshes_read:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should speak with {color=#f6d6bd}Valens{/color}.')
                $ custom1 = "He welcomes you with hungry eyes. “Any news, warden?”"
                jump whitemarshes_valens02
            'I still need to get familiar with the letter I got from a local farmer. (disabled)' if quest_readtheletter == 1 and not item_letterwhitemarshes_read:
                pass
            'I approach the woman who observes {color=#f6d6bd}[horsename]{/color}.' if whitemarshes_pursewoman and not whitemarshes_pursewoman_talkedto and not quest_hiddenpurse:
                jump whitemarshesquest_hiddenpurse01
            'I don’t have the pouch I was asked to find. (disabled)' if quest_hiddenpurse == 1 and not stonebridge_bridge_under:
                pass
            'I should tell the woman about her pouch.' if quest_hiddenpurse == 1 and stonebridge_bridge_under:
                jump whitemarshesquest_hiddenpurse02
            'I address the guards. “People from the other tribes are looking for spouses.”' if quest_matchmaking == 1 and not whitemarshes_about_matchmaking:
                jump whitemarshes_about_matchmaking01
            'If I want to spy on this place for Glaucia, I need to do so when no one is watching. (disabled)' if quest_spyonwhitemarshes == 1 and whitemarshes_spying_tried and not whitemarshes_spying_completed and not whitemarshes_nomoreundead:
                jump whitemarshestryingtospy01
            'I ask the guards if there’s a room I could rent for the night.' if not whitemarshes_rest_unlocked:
                jump whitemarshesaskingforroom01
            'I approach the well.' if not whitemarshes_well:
                jump whitemarsheswell01
            'I observe the undead workers.' if not whitemarshes_nomoreundead and not whitemarshes_observingundead:
                jump whitemarshes_observingundead01

    label whitemarshesquest_hiddenpurse02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should tell the woman about her purse.')
        $ custom1 = "She’s just at the edge of the yard, keenly observing you, and as you approach her, she once again leads you further away from the gate - this time behind a turf house. She reaches out to you with an open palm, and speaks quietly. “May The Wright bless you, stranger.”"
        jump whitemarshesquest_hiddenpurse02after

    label whitemarshesquest_hiddenpurse02after:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '[custom1]
            '
            '(lie) “I’m sorry. The pouch was completely rotten, and there were no dragon bones to pick. Just snails.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I’m sorry. The pouch was completely rotten, and there were no dragon bones to pick. Just snails.”')
                $ pc_lies += 1
                $ quest_hiddenpurse = 3
                $ quest_hiddenpurse_description03 = "I decided to lie to her and keep the coin to myself."
                $ renpy.notify("Quest completed: A Hidden Pouch")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: A Hidden Pouch{/i}')
                menu:
                    'She looks at the sky, then to the ground. For two heartbeats, she can’t stop herself from revealing the despair in her eyes, but she then adjusts her headscarf, takes a deep breath, and nods quietly. “Thanks for trying, stranger.”
                    \n\nShe hobbles away, splashing mud with every step.
                    '
                    'I return to my bundles.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to my bundles.')
                        jump whitemarshesafterinteraction01
            '“The pouch was torn and rotten. Here, the only dragon bone I found.”' if coins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The pouch was torn and rotten. Here, the only dragon bone I found.”')
                show screen notifyimage( "-1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 {image=cointest}{/i}')
                $ coins -= 1
                $ quest_hiddenpurse_description02 = "I brought her the news."
                $ quest_hiddenpurse = 2
                $ whitemarshes_reputation += 1
                $ whitemarshes_pursewoman_coins = 1
                $ renpy.notify("Quest completed: A Hidden Pouch")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: A Hidden Pouch{/i}')
                menu:
                    'She looks at the sky, then to the ground. For two heartbeats, she can’t stop herself from revealing the despair in her eyes, but she then adjusts her headscarf, takes a deep breath, and moves her shoulders. “I have not even a fistful of blueberries to thank you, stranger. Ba I’ll tell the rest f’the village you’re a trustworthy messenger, if anyone asks. Hardly anyone does around here.”
                    \n\nShe hobbles away, splashing mud with every step.
                    '
                    'I return to my bundles.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to my bundles.')
                        jump whitemarshesafterinteraction01
            'I already spent the coin I found. (disabled)' if not coins:
                pass
            '(lie) “You were correct. Here, your ten dragon bones.”' if coins >= 10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You were correct. Here, your ten dragon bones.”')
                show screen notifyimage( "-10", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-10 {image=cointest}{/i}')
                $ coins -= 10
                $ pc_lies += 1
                $ quest_hiddenpurse_description02 = "I brought her the news."
                $ quest_hiddenpurse = 2
                $ whitemarshes_pursewoman_coins = 10
                $ renpy.notify("Journal updated: A Hidden Pouch")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: A Hidden Pouch{/i}')
                if helvius_about_womanwithpurse_denied and pc_goal == "iwanttohelp":
                    $ pc_goal_iwanttohelppoints += 1
                $ whitemarshes_opposition = 1
                $ description_thyrsus05 = "He seems to be bothered by the undead of {color=#f6d6bd}White Marshes{/color}."
                menu:
                    'She stares at the coins in silence, holding the tears, then lets out a relieved sigh and shoves the dragons into a small linen sheet, then pushes it behind her jacket, filling the space between her breasts. “I prayed for so long,” she whispers, tying the straps. “An’ thanks to you, I can leave this forsaken place with the next caravan.”
                    \n\nShe flinches and looks around the corner. She speaks quickly.
                    \n\n“I mustn’t be found. I won’t tell what you did for me, but if you have any spark of Wright’s decency in you, speak with {color=#f6d6bd}Thyrsus{/color}, the warlock. He’s the last soul that speaks against {color=#f6d6bd}Orentius{/color}.”
                    \n\nYou hardly understand the last few words. She’s already scurrying away, gesturing for you to head to the gate.
                    '
                    'And so I do.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- And so I do.')
                        jump whitemarshesafterinteraction01
            'I could lie and give her ten dragon bones... But I don’t have that much. (disabled)' if coins < 10:
                pass
            'I apologize. “I just wanted to mention that I’m still working on it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I apologize. “I just wanted to mention that I’m still working on it.”')
                jump whitemarshesafterinteraction01

label whitemarshes_childALL:
    label whitemarshes_child01:
        $ whitemarshes_child = day
        menu:
            'On your way to the village, you see a girl, no older than fifteen, walking through the tall, purple grasses along with a few other youngsters. After she notices your arrival, she runs toward the road, waving to draw your attention.
            '
            'I stop. “Can I help you?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I help you?”')
                jump whitemarshes_child02
            'I wave back, but ride forward.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wave back, but ride forward.')
                $ whitemarshes_child_fluff = "She looks at you with disappointment, but obediently returns to her group. "
                $ can_leave = 1
                if whitemarshes_rest_unlocked:
                    $ can_rest = 1
                $ can_items = 1
                show areapicture whitemarshes01 at basicfade
                jump whitemarshesregular01
            'I ignore her.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ignore her.')
                $ whitemarshes_child_fluff = "Seeing your uninterrupted canter, she turns around. "
                $ can_leave = 1
                if whitemarshes_rest_unlocked:
                    $ can_rest = 1
                $ can_items = 1
                show areapicture whitemarshes01 at basicfade
                jump whitemarshesregular01

    label whitemarshes_child02:
        $ minutes += 5
        menu:
            'It takes her a few more moments to reach you. Her clothes are baggy, appropriately so for her age, but she’s also rather scraggy for a laborer. She carries a slingshot and a simple backpack made of creepers and twigs, filled with green leaves, wild fruits, and a dead squirrel lying on the surface.
            \n\nAfter your question, she gives you a curious glance. “{i}Roadwarden{/i}, parents told me?” Not sure which part of it is a question, you nod in agreement. “Ba what is it that one {i}does{/i}, really? Hunt bounties?”
            '
            '“I mostly patrol the roads and travel between villages. Some roadwardens seek bounties, yes, but I do all sorts of things, whatever’s needed.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I mostly patrol the roads, and travel between villages. Some roadwardens seek bounties, yes, but I do all sorts of things.”')
                $ minutes += 2
                menu:
                    '“Oh, you’re an {i}adventurer{/i}, then?” She makes an odd, displeased grimace, then sneezes and smiles at you.
                    '
                    '“Not really. Adventurers are paid to do odd jobs, but often don’t follow the city laws, nor the local ones. Unlike roadwardens.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not really. Adventurers are paid to do odd jobs, but often don’t follow the city laws, nor the local ones. Unlike roadwardens.”')
                        $ minutes += 2
                        menu:
                            '“Yep, makes sense,” she nods, but looks around with a frown. “So you’re {i}a mercenary{/i}, f’sorts? They {i}do{/i} follow laws, if the pay’s right.”
                            '
                            '“Even less so. Mercenaries follow the {i}rules{/i} of their employers, but they get hired only as fighters. Either as guards, or one-time soldiers - they mostly learn how to fight other humans.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Even less so. Mercenaries follow the {i}rules{/i} of their employers, but they get hired only as fighters. Either as guards, or one-time soldiers - they mostly learn how to fight other humans.”')
                                $ minutes += 2
                                menu:
                                    '“Ba aren’t you {i}a soldier{/i}?” She waves toward her companions, showing them to not worry about her. “You work for the city, right?”
                                    '
                                    '“I do, but I work only with my mount, and answer only to the chieftain. I’ve no lieutenant, and am required to handle many tasks on my own. Securing shelters, for example, or staying alive in the wilderness. I don’t {i}occupy{/i} any specific spot, and am not allowed to collect taxes.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I do, but I work only with my mount, and answer only to the chieftain. I’ve no lieutenant, and am required to handle many tasks on my own. Securing shelters, for example, or staying alive in the wilderness. I don’t {i}occupy{/i} any specific spot, and am not allowed to collect taxes.”')
                                        $ minutes += 2
                                        menu:
                                            'Her tone is confident when she pats her slingshot. “Hear this, then. You’re {i}part-pathfinder-part-adventurer{/i}. The city pays you to cross the woods by yourself, an’ you do odd jobs for your own sake.”
                                            '
                                            '“No, no. Pathfinders don’t patrol the roads, they cross the wilderness and seek game trails that could be widened with tools. And they don’t work alone, beasts are too dangerous. My horse here won’t squeeze through some shrubs, you know?”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No, no. Pathfinders don’t patrol the roads, they cross the wilderness and seek game trails that could be widened with tools. And they don’t work alone, beasts are too dangerous. My horse here won’t squeeze through some shrubs, you know?”')
                                                $ minutes += 2
                                                menu:
                                                    '“Ba you know who {i}does{/i} work alone,” she persists. “{i}Rangers{/i}. Lone spies. You’re pretty much that.”
                                                    '
                                                    '“I mean, you’re close. But rangers are meant to stay hidden, gathering rumors, seeking foes and monsters. They don’t intervene unless directly threatened, and are meant to, above all, bring the news back to their lieutenant, or sabotage enemy troops. I work closely with mayors, and never hide my identity.”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I mean, you’re close. But rangers are meant to stay hidden, gathering rumors, seeking foes and monsters. They don’t intervene unless directly threatened, and are meant to, above all, bring the news back to their lieutenant, or sabotage enemy troops. I work closely with mayors, and never hide my identity.”')
                                                        $ minutes += 2
                                                        menu:
                                                            'She repeats parts of your description quietly, then bursts into laughter. “Now I get it! Ba all these names are a mess, huh?”
                                                            '
                                                            '“I’m impressed you know them at all. There haven’t been many rangers or pathfinders around since the Invasion.”':
                                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m impressed you know them at all. There haven’t been many rangers or pathfinders around since the Invasion.”')
                                                                $ whitemarshes_reputation += 1
                                                                $ whitemarshes_child_asterion = 1
                                                                $ custom1 = "“An’ neither’ve roadwardens,” she shrugs and steps away, trying to silence the loud calls of the other foragers. “One was here before summer, ba found nothing to do here, was just speaking with {color=#f6d6bd}Thyrsus{/color} a lot. You know {color=#f6d6bd}Thyrsus{/color}?” You nod, and she looks back - her fellow foragers are calling her to get back to work. “My ma was a soldier, before she got me. Ba no one tells me much about her, see? City an’ soldiers don’t bother with us no more, so people forgot.”\n\nShe says goodbye with a gentle bow, then runs back to her group."
                                                                jump whitemarshes_child_leaving01
                                                            '“Are you planning to be a traveler, too?”':
                                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to be a traveler, too?”')
                                                                $ whitemarshes_reputation += 1
                                                                $ custom1 = "“Oh, I don’t know,” her slingshot drops again. “I’d like to see the woods, plains, an’ hills, see? Ba there are good days here, too. The sunrise, the icerinks in winter, the mushrooms, the smoked game.” She looks back - her fellow foragers are calling her to get back to work. “Safe travels, roadwarden!”\n\nShe runs back to her group."
                                                                jump whitemarshes_child_leaving01
                                                    '“Listen, I really have no time for this.”':
                                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Listen, I really have no time for this.”')
                                                        $ whitemarshes_child_fluff = "“I... Sorry.” She mutters, and obediently steps away. "
                                                        $ can_leave = 1
                                                        if whitemarshes_rest_unlocked:
                                                            $ can_rest = 1
                                                        $ can_items = 1
                                                        show areapicture whitemarshes01 at basicfade
                                                        jump whitemarshesregular01
                                            '“You figured it out.”':
                                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You figured it out.”')
                                                $ custom1 = "“I did!” She meets your eyes proudly. “I guess there’s a tiny reason to call such a soul {i}a roadwarden{/i}. Safe travels!” She waves to you and runs back to the rest of her group."
                                                jump whitemarshes_child_leaving01
                                    '“You got me there. I guess it’s just a name thing.”':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You got me there. I guess it’s just a name thing.”')
                                        $ custom1 = "“Right?” She meets your eyes proudly. “All cityfolk work for the army, one way or another.” She purses her lips and runs back to the rest of her group."
                                        jump whitemarshes_child_leaving01
                            '“In a way, sure.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “In a way, sure.”')
                                $ custom1 = "“Right?” She meets your eyes proudly. “No soul wad get so far away from the city without bones waiting for them to do so.” She purses her lips and runs back to the rest of her group."
                                jump whitemarshes_child_leaving01
                    '“Close enough.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Close enough.”')
                        $ whitemarshes_child_fluff = "She meets your eyes proudly, purses her lips, and runs back to the rest of her group. "
                        $ can_leave = 1
                        if whitemarshes_rest_unlocked:
                            $ can_rest = 1
                        $ can_items = 1
                        show areapicture whitemarshes01 at basicfade
                        jump whitemarshesregular01
            '“I’m not here to chat. If you have a job for me, speak. Otherwise, I’ll be on my way.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not here to chat. If you have a job for me, speak. Otherwise, I’ll be on my way.”')
                $ whitemarshes_child_fluff = "“I... Sorry.” She mutters, and obediently steps away. "
                $ can_leave = 1
                if whitemarshes_rest_unlocked:
                    $ can_rest = 1
                $ can_items = 1
                show areapicture whitemarshes01 at basicfade
                jump whitemarshesregular01

    label whitemarshes_child_leaving01:
        $ can_leave = 1
        if whitemarshes_rest_unlocked:
            $ can_rest = 1
        $ can_items = 1
        show areapicture whitemarshes01 at basicfade
        menu:
            '[custom1]
            '
            'I ride through the gate.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride through the gate.')
                $ can_leave = 1
                if whitemarshes_rest_unlocked:
                    $ can_rest = 1
                $ can_items = 1
                show areapicture whitemarshes01 at basicfade
                jump whitemarshesregular01

label whitemarshes_valensALL:
    label whitemarshes_valens01:
        $ whitemarshes_valens_firsttime = 1
        $ whitemarshes_valens_firsttime_day = day
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'As you ride past the fields, one of the local farmers enters the road, gesturing for you to stop. He’s holding a rusty sickle and carries a basket on his back, filled with various weeds and a sharped club. His patched, worn tunic is neglected, but fitting for a farmer. The lean years left his face skinny and his teeth crooked, but his sad eyes hold heartwarming kindness.
            \n\n“Hi there, warden,” he has a thick, local accent. “I’ve been wondering just now, the’s a small matter, you see... Do you know how to read?”
            '
            '“I used to be a scholar.”' if pc_class == "scholar":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I used to be a scholar.”')
                $ whitemarshes_valens_knowspccanread = 1
                $ quest_readtheletter = 1
                $ item_letterwhitemarshes = 1
                $ item_letterwhitemarshes_read = 1
                $ renpy.notify("New entry: Read The Letter.\nYou received the bone tablet.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Read The Letter. You received the bone tablet.{/i}')
                menu:
                    '“Fantastic!” He gives you a radiant smile. “Give me a few moments?” Without waiting for your response, he runs to the village, and returns to you with a small sack in his hands.
                    \n\n“How about you take a look at it?” He unwraps the package and reveals a large wax tablet made of bone. “T’s a letter from someone I care about, ba I’m not sure what it says. I’ll give you a coin once you read it for me!”
                    \n\nYou take the tablet from his open palm. It’s fancy, unlike the wooden ones. On its back you find an engraving portraying a large, furry beast. “Made f’a troll’s hip,” {color=#f6d6bd}the farmer{/color} says proudly.
                    \n\nYou examine the confident, deep signs written in the wax. The letter is short {i}{color=#f6d6bd}Valens{/color}{/i}, it starts, {i}I couldn’t bear another day in this nightmarish village. But now I don’t have to - I’ve met another soul during my hunting trip south. We will start a new family, goodbye.{/i} No signature.
                    \n\nThe man is walking in place, waiting for you to speak.
                    '
                    '“Why do you need my help?”' if not whitemarshes_valens_questions1 and whitemarshes_valens_firsttime == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why do you need my help?”')
                        $ whitemarshes_valens_questions1 = 1
                        $ quest_readtheletter_description00a = "He told me I could find help among followers of The Wright."
                        $ custom1 = "He frowns as if the answer is obvious. “No merchants come here these days, an’ no missionaries. An’ we don’t need to read around here.”"
                        jump whitemarshes_valens02
                    '“But you do have a priest in the village.”' if whitemarshes_valens_questions1 and not whitemarshes_valens_questions2 and whitemarshes_valens_firsttime == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But you do have a priest in the village.”')
                        $ whitemarshes_valens_questions2 = 1
                        $ custom1 = "He looks at the gate, as if he just realized you’re right. “I asked him,” his tone is cold, “ba he was no help. Said {i}the letters are blurry{/i}. They look fine to me!”"
                        jump whitemarshes_valens02
                    '“That’s a pretty tablet.”' if not whitemarshes_valens_questions3 and whitemarshes_valens_firsttime == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s a pretty tablet.”')
                        $ whitemarshes_valens_questions3 = 1
                        $ custom1 = "He puts his hands on his sides, his smile is filled with pride. “Did it myself! With cold nights an’ little iron, takes thinking to keep your hands busy!”"
                        jump whitemarshes_valens02
                    '“I know what’s in the letter.”' if item_letterwhitemarshes_read:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know what’s in the letter.”')
                        jump whitemarshes_valens03
                    '(lie) “There are some letters here I can’t decipher. I better consult them with someone.”' if whitemarshes_valens_knowspccanread and whitemarshes_valens_firsttime == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “There are some letters here I can’t decipher. I better consult them with someone.”')
                        $ whitemarshes_valens_firsttime = 2
                        $ pc_lies += 1
                        $ minutes += 5
                        if travel_destination == "whitemarshes":
                            menu:
                                'His disappointed sigh says it all. “Good thing you’re a rider,” he steps away. “I’ll wait for you with the coin I promised!”
                                '
                                'I ride through the gate.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride through the gate.')
                                    $ can_leave = 1
                                    if whitemarshes_rest_unlocked:
                                        $ can_rest = 1
                                    $ can_items = 1
                                    show areapicture whitemarshes01 at basicfade
                                    jump whitemarshesregular01
                        else:
                            $ can_leave = 1
                            if whitemarshes_rest_unlocked:
                                $ can_rest = 1
                            $ can_items = 1
                            menu:
                                'His disappointed sigh says it all. “Good thing you’re a rider,” he steps away, clearing the path. “I’ll wait for you with the coin I promised!”
                                '
                                'I’m ready for the further journey. (disabled)':
                                    pass
                    '“Fine. I’ll see you soon.”' if not whitemarshes_valens_knowspccanread and whitemarshes_valens_firsttime == 1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I’ll see you soon.”')
                        $ minutes += 5
                        if travel_destination == "whitemarshes":
                            menu:
                                'He waves to you and steps away, clearing the path. “I’ll wait for you with the coin I promised!”
                                '
                                'I ride through the gate.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride through the gate.')
                                    $ can_leave = 1
                                    if whitemarshes_rest_unlocked:
                                        $ can_rest = 1
                                    $ can_items = 1
                                    show areapicture whitemarshes01 at basicfade
                                    jump whitemarshesregular01
                        else:
                            $ can_leave = 1
                            if whitemarshes_rest_unlocked:
                                $ can_rest = 1
                            $ can_items = 1
                            menu:
                                'He waves to you and steps away, clearing the path. “I’ll wait for you with the coin I promised!”
                                '
                                'I’m ready for the further journey. (disabled)':
                                    pass
                    '“I’ll see you soon.”' if whitemarshes_valens_firsttime == 2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll see you soon.”')
                        jump whitemarshesafterinteraction01
            '“I don’t, I’m afraid.”' if pc_class != "scholar":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t, I’m afraid.”')
                jump whitemarshes_valens01a
            '“No.”' if pc_class != "scholar":
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No.”')
                label whitemarshes_valens01a:
                    $ quest_readtheletter = 1
                    $ item_letterwhitemarshes = 1
                    $ renpy.notify("New entry: Read The Letter.\nYou received the bone tablet.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Read The Letter. You received the bone tablet.{/i}')
                    menu:
                        '“I see,” he gives you a sad smile, “ba still... you’ve a horse, I mean?” He raises his eyes, as if to make it clear he’s aware that you’re sitting in a saddle. “It is... You ride places! Give me a few moments?” Without waiting for your response, he runs to the village, and returns to you with a small sack in his hands.
                        \n\n“How about you take it to someone smart?” He unwraps the package and reveals a large wax tablet made of bone. “T’s a letter from someone I care about, ba I’m not sure what it says. I’ll give you a coin once you read it for me!”
                        \n\nYou take the tablet from his open palm. It’s fancy, unlike the wooden ones. On its back you find an engraving portraying a large, furry beast. “Made f’a troll’s hip,” {color=#f6d6bd}the farmer{/color} says proudly.
                        '
                        '“Why do you need my help?”' if not whitemarshes_valens_questions1 and whitemarshes_valens_firsttime == 1:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why do you need my help?”')
                            $ whitemarshes_valens_questions1 = 1
                            $ quest_readtheletter_description00a = "He told me I could find help among followers of The Wright."
                            $ custom1 = "He frowns as if the answer is obvious. “No merchants come here these days, an’ no missionaries. An’ we don’t need to read around here.”"
                            jump whitemarshes_valens02
                        '“But you do have a priest in the village.”' if whitemarshes_valens_questions1 and not whitemarshes_valens_questions2 and whitemarshes_valens_firsttime == 1:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But you do have a priest in the village.”')
                            $ whitemarshes_valens_questions2 = 1
                            $ custom1 = "He looks at the gate, as if he just realized you’re right. “I asked him,” his tone is cold, “ba he was no help. Said {i}the letters are blurry{/i}. They look fine to me!”"
                            jump whitemarshes_valens02
                        '“That’s a pretty tablet.”' if not whitemarshes_valens_questions3 and whitemarshes_valens_firsttime == 1:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s a pretty tablet.”')
                            $ whitemarshes_valens_questions3 = 1
                            $ custom1 = "He puts his hands on his sides, his smile is filled with pride. “Did it myself! With cold nights an’ little iron, takes thinking to keep your hands busy!”"
                            jump whitemarshes_valens02
                        '“I know what’s in the letter.”' if item_letterwhitemarshes_read:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know what’s in the letter.”')
                            jump whitemarshes_valens03
                        '(lie) “There are some letters here I can’t decipher. I better consult them with someone.”' if whitemarshes_valens_knowspccanread and whitemarshes_valens_firsttime == 1:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “There are some letters here I can’t decipher. I better consult them with someone.”')
                            $ whitemarshes_valens_firsttime = 2
                            $ pc_lies += 1
                            $ minutes += 5
                            if travel_destination == "whitemarshes":
                                menu:
                                    'His disappointed sigh says it all. “Good thing you’re a rider,” he steps away. “I’ll wait for you with the coin I promised!”
                                    '
                                    'I ride through the gate.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride through the gate.')
                                        $ can_leave = 1
                                        if whitemarshes_rest_unlocked:
                                            $ can_rest = 1
                                        $ can_items = 1
                                        show areapicture whitemarshes01 at basicfade
                                        jump whitemarshesregular01
                            else:
                                $ can_leave = 1
                                if whitemarshes_rest_unlocked:
                                    $ can_rest = 1
                                $ can_items = 1
                                menu:
                                    'His disappointed sigh says it all. “Good thing you’re a rider,” he steps away, clearing the path. “I’ll wait for you with the coin I promised!”
                                    '
                                    'I’m ready for the further journey. (disabled)':
                                        pass
                        '“Fine. I’ll see you soon.”' if not whitemarshes_valens_knowspccanread and whitemarshes_valens_firsttime == 1:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I’ll see you soon.”')
                            $ minutes += 5
                            if travel_destination == "whitemarshes":
                                menu:
                                    'He waves to you and steps away, clearing the path. “I’ll wait for you with the coin I promised!”
                                    '
                                    'I ride through the gate.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride through the gate.')
                                        $ can_leave = 1
                                        if whitemarshes_rest_unlocked:
                                            $ can_rest = 1
                                        $ can_items = 1
                                        show areapicture whitemarshes01 at basicfade
                                        jump whitemarshesregular01
                            else:
                                $ can_leave = 1
                                if whitemarshes_rest_unlocked:
                                    $ can_rest = 1
                                $ can_items = 1
                                menu:
                                    'He waves to you and steps away, clearing the path. “I’ll wait for you with the coin I promised!”
                                    '
                                    'I’m ready for the further journey. (disabled)':
                                        pass
                        '“I’ll see you soon.”' if whitemarshes_valens_firsttime == 2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll see you soon.”')
                            jump whitemarshesafterinteraction01

    label whitemarshes_valens02:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '[custom1]
            '
            '“Why do you need my help?”' if not whitemarshes_valens_questions1 and whitemarshes_valens_firsttime == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why do you need my help?”')
                $ whitemarshes_valens_questions1 = 1
                $ quest_readtheletter_description00a = "He told me I could find help among followers of The Wright."
                $ custom1 = "He frowns as if the answer is obvious. “No merchants come here these days, an’ no missionaries. An’ we don’t need to read around here.”"
                jump whitemarshes_valens02
            '“But you do have a priest in the village.”' if whitemarshes_valens_questions1 and not whitemarshes_valens_questions2 and whitemarshes_valens_firsttime == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But you do have a priest in the village.”')
                $ whitemarshes_valens_questions2 = 1
                $ custom1 = "He looks at the gate, as if he just realized you’re right. “I asked him,” his tone is cold, “ba he was no help. Said {i}the letters are blurry{/i}. They look fine to me!”"
                jump whitemarshes_valens02
            '“That’s a pretty tablet.”' if not whitemarshes_valens_questions3 and whitemarshes_valens_firsttime == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s a pretty tablet.”')
                $ whitemarshes_valens_questions3 = 1
                $ custom1 = "He puts his hands on his sides, his smile is filled with pride. “Did it myself! With cold nights an’ little iron, takes thinking to keep your hands busy!”"
                jump whitemarshes_valens02
            '“I know what’s in the letter.”' if item_letterwhitemarshes_read:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know what’s in the letter.”')
                jump whitemarshes_valens03
            '(lie) “There are some letters here I can’t decipher. I better consult them with someone.”' if whitemarshes_valens_knowspccanread and whitemarshes_valens_firsttime == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “There are some letters here I can’t decipher. I better consult them with someone.”')
                $ whitemarshes_valens_firsttime = 2
                $ pc_lies += 1
                $ minutes += 5
                if travel_destination == "whitemarshes":
                    menu:
                        'His disappointed sigh says it all. “Good thing you’re a rider,” he steps away. “I’ll wait for you with the coin I promised!”
                        '
                        'I ride through the gate.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride through the gate.')
                            $ can_leave = 1
                            if whitemarshes_rest_unlocked:
                                $ can_rest = 1
                            $ can_items = 1
                            show areapicture whitemarshes01 at basicfade
                            jump whitemarshesregular01
                else:
                    $ can_leave = 1
                    if whitemarshes_rest_unlocked:
                        $ can_rest = 1
                    $ can_items = 1
                    menu:
                        'His disappointed sigh says it all. “Good thing you’re a rider,” he steps away, clearing the path. “I’ll wait for you with the coin I promised!”
                        '
                        'I’m ready for the further journey. (disabled)':
                            pass
            '“Fine. I’ll see you soon.”' if not whitemarshes_valens_knowspccanread and whitemarshes_valens_firsttime == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. I’ll see you soon.”')
                $ minutes += 5
                if travel_destination == "whitemarshes":
                    menu:
                        'He waves to you and steps away, clearing the path. “I’ll wait for you with the coin I promised!”
                        '
                        'I ride through the gate.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride through the gate.')
                            $ can_leave = 1
                            if whitemarshes_rest_unlocked:
                                $ can_rest = 1
                            $ can_items = 1
                            show areapicture whitemarshes01 at basicfade
                            jump whitemarshesregular01
                else:
                    $ can_leave = 1
                    if whitemarshes_rest_unlocked:
                        $ can_rest = 1
                    $ can_items = 1
                    menu:
                        'He waves to you and steps away, clearing the path. “I’ll wait for you with the coin I promised!”
                        '
                        'I’m ready for the further journey. (disabled)':
                            pass
            '“I’ll see you soon.”' if whitemarshes_valens_firsttime == 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll see you soon.”')
                jump whitemarshesafterinteraction01

    label whitemarshes_valens03:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'He puts a hand on his forehead. You can’t tell if it’s a sign of relief, or tension.
            '
            '“It’s a long story. The letter says one thing, but I spoke with the innkeep at the southern inn...”' if iason_about_valens:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s a long story. The letter says one thing, but I spoke with the innkeep at the southern inn...”')
                $ quest_readtheletter_description04 = 1
                $ quest_readtheletter_description01 = "I brought him the news and received my reward."
                if pc_goal == "iwanttohelp":
                    $ pc_goal_iwanttohelppoints += 2
                $ whitemarshes_reputation += 2
                $ orentius_friendship += 1
                $ minutes += 5
                $ description_orentius11 = "According to {color=#f6d6bd}Valens{/color}, he “always asks to be heard”."
                $ custom1 = "He opens and closes his mouth repeatedly, observing you in silence. “That idiot,” he tries to stop his tears. “How cad he not see his pride ate his ties? An’ without asking me, as if I were to throw him into the dirt?” He looks toward the hut on the platform. “I guess {color=#f6d6bd}Orentius{/color} knew my husband canna be trusted. He always asks {i}to be heard{/i}, mayhap I...” He lets out a sigh, his shaking hands offer you the reward."
                jump whitemarshes_valens04
            '(lie) “The letters are too distorted. No one could read what’s in here.”' if not iason_about_valens:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “The letters are too distorted. No one could read what’s in here.”')
                $ quest_readtheletter_description01alt = "I lied to him about the contents and received my reward."
                $ pc_lies += 1
                if pc_goal == "iwanttohelp":
                    $ pc_goal_iwanttohelppoints += 1
                $ whitemarshes_reputation += 1
                $ orentius_friendship += 1
                $ minutes += 5
                $ custom1 = "He grabs the upper part of his nose, squeezing it while he starts to sob. “So I’ll never know. I should’ve listen to {color=#f6d6bd}Orentius{/color}, just forget about him...” His shaking hands offer you the reward, and you look at the nearest guard. He gives you a polite nod."
                jump whitemarshes_valens04
            'I repeat to him his husband’s words.' if not iason_about_valens:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I repeat to him his husband’s words.')
                $ quest_readtheletter_description01 = "I brought him the news and received my reward."
                if pc_goal == "iwanttohelp":
                    $ pc_goal_iwanttohelppoints += 1
                $ whitemarshes_reputation += 1
                $ orentius_friendship -= 2
                $ minutes += 5
                $ description_orentius11 = "According to {color=#f6d6bd}Valens{/color}, he “always asks to be heard”."
                $ custom1 = "At first he freezes, then gives a hateful look toward {color=#f6d6bd}Orentius’{/color} hut. “He knew what this piece of shit did,” he growls. “He always asks {i}to be heard{/i}, only to spread lies. Why do I need to find a stranger to hear the truth, for once in my life?” His eyes get gentler once he looks at you, but you notice the tears in his eyes. His shaking hands offer you the reward."
                jump whitemarshes_valens04

    label whitemarshes_valens04:
        $ whitemarshes_valens_completion_day = day
        $ coins += 1
        show screen notifyimage( "+1", "gui/coin2.png")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 {image=cointest}{/i}')
        if whitemarshes_valens_firsttime == 1:
            $ custom2 = "“Now, about the tablet..."
        else:
            $ custom2 = "“You still’ve the tablet?”"
        menu:
            '[custom1] [custom2]
            '
            '“Here you go.”' if item_letterwhitemarshes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here you go.”')
                $ item_letterwhitemarshes = 2
                $ renpy.notify("You received the bone stylus.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the bone stylus.{/i}')
                menu:
                    '“I don’t want it,” he steps away. “You know what? Take this,” he pulls out a bone stylus that perfectly matches the colors of the tablet. “Together, they will buy you a few meals at a trader’s stall. Good luck, warden.”
                    '
                    '“Farewell.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                        $ quest_readtheletter = 2
                        $ renpy.notify("Quest completed: Read The Letter")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Read The Letter{/i}')
                        $ whitemarshes_pursewoman = 1
                        $ whitemarshes_valens_shop_unlocked = day
                        show areapicture whitemarshes01 at basicfade
                        jump whitemarshesafterinteraction01
            '(lie) “I don’t have it anymore.”' if item_letterwhitemarshes and whitemarshes_valens_firsttime >= 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “I don’t have it anymore.”')
                $ pc_lies += 1
                $ whitemarshes_reputation -= 1
                menu:
                    'He narrows his eyes, as if the last shard of trust just escaped his heart. “You don’t say? I didn’t want it back anyway.” He turns away and spares you but a short wave of his hand.
                    '
                    '“Farewell.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                        $ quest_readtheletter = 2
                        $ renpy.notify("Quest completed: Read The Letter")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Read The Letter{/i}')
                        $ whitemarshes_pursewoman = 1
                        show areapicture whitemarshes01 at basicfade
                        jump whitemarshesafterinteraction01
            '“I don’t have it anymore.”' if not item_letterwhitemarshes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t have it anymore.”')
                $ whitemarshes_reputation -= 1
                menu:
                    'He narrows his eyes, as if the last shard of trust just escaped his heart. “You don’t say? I didn’t want it back anyway.” He turns away and spares you but a short wave of his hand.
                    '
                    '“Farewell.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                        $ quest_readtheletter = 2
                        $ renpy.notify("Quest completed: Read The Letter")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Read The Letter{/i}')
                        $ whitemarshes_pursewoman = 1
                        show areapicture whitemarshes01 at basicfade
                        jump whitemarshesafterinteraction01

    label whitemarshes_valens00fail:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'Before you reach the gate, {color=#f6d6bd}the farmer{/color} once again cuts your path, angrily shaking his sickle. “Warden! I was thinking... Takes you oddly long to read this little letter.”
            '
            '“I managed to learn what it says.”' if item_letterwhitemarshes_read:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I managed to learn what it says.”')
                jump whitemarshes_valens03
            '“I don’t have your tablet anymore.”' if not item_letterwhitemarshes_read:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I managed to learn what’s in the letter.”')
                $ whitemarshes_reputation -= 2
                $ whitemarshes_valens_angry = 1
                menu:
                    '“You serious?” He narrows his eyes. Soon after, you see him speaking with the guards, and while they don’t approach you, their distrustful glances make it clear your deed won’t be ignored.
                    '
                    'I walk away.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I walk away.')
                        show areapicture whitemarshes01 at basicfade
                        jump whitemarshesafterinteraction01

label whitemarshes_valens_shopALL:
    label whitemarshes_valens_shop_firsttime01:
        $ whitemarshes_valens_shop_firsttime = 1
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I notice {color=#f6d6bd}Valens{/color} standing next to a shed. I’ll say {i}hi{/i} to him.')
        menu:
            'He’s moving small packages, bringing order to some neglected shelves. His eyes are red from crying, but he greets you with a strong voice and a polite smile. This time, he’s wearing a decent, blue tunic.
            \n\n“Back with us, [pcname]? The’s been long time since I saw some visiting our home as often as you do.”
            '
            '“It’s not so bad here.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s not so bad here.”')
                $ custom1 = "“You’ven’t seen the worst of it,” he chuckles. “Me, I’m looking after our grain and dried meat before fall comes. Thanks to...” He draws in the air and lowers his voice. “{color=#f6d6bd}Orentius’{/color} {i}help{/i}, we’ve more food than in many years, ba now we need to figure out what goes to our bellies, what back to the soil.”"
                $ whitemarshes_valens_sellingpoints += 10
                jump whitemarshes_valens_shop_firsttime02
            '“That’s how my job works. I go where others don’t.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That’s how my job works. I go where others don’t.”')
                $ custom1 = "He gives you a long look, as if he’s not sure if it’s meant to be an insult, then turns back to the bags. “I’m looking after our grain and dried meat before fall comes. Thanks to...” He draws in the air and lowers his voice. “{color=#f6d6bd}Orentius’{/color} {i}help{/i}, we’ve more food than in many years, ba now we need to figure out what goes to our bellies, what back to the soil.”"
                $ whitemarshes_valens_sellingpoints += 5
                label whitemarshes_valens_shop_firsttime02:
                    menu:
                        '[custom1]
                        '
                        '“I may have some supplies I could spare. Want to take a look?”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I may have some supplies I could spare. Want to take a look?”')
                            jump whitemarshes_valens_shop_selling01

    label whitemarshes_valens_shop_regular01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Valens{/color}.')
        $ whitemarshes_valens_fluff = renpy.random.choice(['“Good day, warden.”', '“Here to trade?”', 'He offers you a nut.', '“The days are getting colder.”'])
        menu:
            '[whitemarshes_valens_fluff]
            '
            '{image=cointest} “I have some supplies I don’t need.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I have some supplies I don’t need.”')
                jump whitemarshes_valens_shop_selling01
            '“I spoke with the innkeep from {color=#f6d6bd}Pelt{/color}, and he has some news about your husband...”' if iason_about_valens and quest_readtheletter_description01 and not quest_readtheletter_description01alt and not quest_readtheletter_description04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spoke with the innkeep from {color=#f6d6bd}Pelt{/color}, and he has some news about your husband...”')
                jump whitemarshes_valens_shop_spouseupdate01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump whitemarshesafterinteraction01

    label whitemarshes_valens_shop_selling01:
        show screen shopscreen with dissolve
        menu:
            'He asks you to put everything on the table.
            '
            '{image=cointest} “I have some supplies I don’t need.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I have some supplies I don’t need.”')
                jump whitemarshes_valens_shop_selling01
            '“I spoke with the innkeep from {color=#f6d6bd}Pelt{/color}, and he has some news about your husband...”' if iason_about_valens and quest_readtheletter_description01 and not quest_readtheletter_description01alt and not quest_readtheletter_description04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spoke with the innkeep from {color=#f6d6bd}Pelt{/color}, and he has some news about your husband...”')
                jump whitemarshes_valens_shop_spouseupdate01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump whitemarshesafterinteraction01

    label whitemarshes_valens_aftertrading01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if whitemarshes_valens_sellingpoints >= 40:
            $ whitemarshes_valens_sellingpoints -= 40
            $ whitemarshes_reputation += 2
            $ whitemarshes_valens_fluff = '“I’m s’prised you carried so much with you all the way here!” He lets out a chuckle.'
        elif whitemarshes_valens_sellingpoints >= 20:
            $ whitemarshes_valens_sellingpoints -= 20
            $ whitemarshes_reputation += 1
            $ whitemarshes_valens_fluff = '“Thanks, I’ll put them to good use.”'
        else:
            $ whitemarshes_valens_fluff = '“Mayhap another time.”'
        menu:
            '[whitemarshes_valens_fluff]
            '
            '{image=cointest} “I have some supplies I don’t need.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I have some supplies I don’t need.”')
                jump whitemarshes_valens_shop_selling01
            '“I spoke with the innkeep from {color=#f6d6bd}Pelt{/color}, and he has some news about your husband...”' if iason_about_valens and quest_readtheletter_description01 and not quest_readtheletter_description01alt and not quest_readtheletter_description04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spoke with the innkeep from {color=#f6d6bd}Pelt{/color}, and he has some news about your husband...”')
                jump whitemarshes_valens_shop_spouseupdate01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump whitemarshesafterinteraction01

    label whitemarshes_valens_shop_spouseupdate01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s a long story. The letter says one thing, but I spoke with the innkeep at the southern inn...”')
        $ quest_readtheletter_description04 = 1
        if pc_goal == "iwanttohelp":
            $ pc_goal_iwanttohelppoints += 1
        $ whitemarshes_reputation += 1
        $ orentius_friendship += 3
        $ minutes += 5
        menu:
            'He opens and closes his mouth repeatedly, observing you in silence. “That idiot,” he tries to stop his tears. “How cad he not see his pride ate his ties? An’ without asking me, as if I were to throw him into the dirt?” He looks toward the hut on the platform. “I guess {color=#f6d6bd}Orentius{/color} knew my husband canna be trusted. Mayhap I...” He lets out a sigh. “Thank you for telling me, [pcname].”
            '
            '{image=cointest} “I have some supplies I don’t need.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I have some supplies I don’t need.”')
                jump whitemarshes_valens_shop_selling01
            '“I spoke with the innkeep from {color=#f6d6bd}Pelt{/color}, and he has some news about your husband...”' if iason_about_valens and quest_readtheletter_description01 and not quest_readtheletter_description01alt and not quest_readtheletter_description04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I spoke with the innkeep from {color=#f6d6bd}Pelt{/color}, and he has some news about your husband...”')
                jump whitemarshes_valens_shop_spouseupdate01
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump whitemarshesafterinteraction01
