###################### EUDOCIA HOUSE
default eudocia_name = "crafter" # "Eudocia"
default eudocia_friendship = 0
default eudocia_friendship_tierlevel = 10
default eudocia_ban = 0
default eudocia_fluff = ""
default eudocia_fluff_old = ""
default eudocia_inside_fluff = ""
default eudocia_firsttime = 0
default eudocia_inside_firsttime = 0
default eudocia_fluff_inorout = ""
default eudocia_conversation = 0
default eudocia_sleep_available = 0

default eudocia_screaming = 0
default eudocia_screaming2 = ""
default eudocia_heldobject = ""
default eudocia_toldname = 0

default eudocia_image_left = "dark" # "dark" "base"
default eudocia_image_right = "dark" # "dark" "gate" "base"
default eudocia_image_golem01 = 0 # "gate" "turnedback" "turnedleft" "turnedright"
default eudocia_image_golem02 = 0 # "nogolem" "nogolemplusback"
default eudocia_image_eyes = 0 #1

default eudocia_gate_attempt01 = 0
default eudocia_gate_attempt02 = 0
default eudocia_gate_attempt03 = 0
default eudocia_gate_attempt04 = 0
default eudocia_gate_attempt05 = 0

default eudocia_about_closingthegate = ""
default eudocia_about_pens = 0
default eudocia_about_peninsula = 0
default eudocia_about_monks = 0
default eudocia_about_reading = 0
default eudocia_about_asterion = 0
default eudocia_about_asterion_gray = 0
default eudocia_about_asterion_found = 0
default eudocia_about_asterion_cloak = 0
default eudocia_about_asterion_cloak_lied = 0
default eudocia_about_enchanting = 0
default eudocia_about_enchanting_items = 0
default eudocia_about_herself = 0
default eudocia_about_golems = 0 #4
default eudocia_about_golems_gray = 0
default eudocia_about_golems_question1 = 0
default eudocia_about_golems_question2 = 0
default eudocia_about_golems_question3 = 0
default eudocia_about_golems_question4 = 0
default eudocia_about_gargoyle = 0
default eudocia_about_arrow = 0
default eudocia_about_parents = 0
default eudocia_about_plague = 0
default eudocia_about_plague_cured = 0
default eudocia_about_magicsapling = 0
default eudocia_about_chisel = 0
default eudocia_about_sleeping = 0
default eudocia_about_selling = 0
default eudocia_about_spiritrock = 0
default eudocia_about_spiritrock_problem = 0
default eudocia_about_spiritrock_price = 0
default eudocia_about_spiritrock_price_base = 10
default eudocia_about_shortcut = 0
default eudocia_about_highisland = 0
default eudocia_about_missinghunters = 0
default eudocia_about_steephouse = 0
default eudocia_about_steephouse_gray = 0
default eudocia_about_bandits = 0
default eudocia_about_bandits_gray = 0
default eudocia_about_nomoreundead = 0
default eudocia_about_job01 = 0
default eudocia_about_job02 = 0
default eudocia_about_flower_druid = 0
default eudocia_about_flower_refusal = 0
default eudocia_about_flower_refusal_grateful = 0
default eudocia_about_whitemarshes = 0

default eudocia_bronzerod_coinsperrod = 2
default eudocia_bronzerod_debt_paid1 = 0
default eudocia_bronzerod_debt_paid2 = 0
default eudocia_bronzerod_debt = 0
default eudocia_bronzerod_friendship = 0
default eudocia_bronzerod01p01 = 0
default eudocia_bronzerod01p02 = 0
default eudocia_bronzerod01p03 = 0
default eudocia_bronzerod01p04 = 0
default eudocia_bronzerod02p02 = 0
default eudocia_bronzerod02p03 = 0
default eudocia_bronzerod_advance = 0
default eudocia_bronzerod_max = 8
default eudocia_bronzerod_used = 0
default eudocia_bronzerod_installed = 0
default eudocia_bronzerod_installed_paidfor = 0
default eudocia_bronzerod_secondreward = 0

default eudocia_bronzerod_rodin_southerncrossroads = 0
default eudocia_bronzerod_rodin_watchtower = 0
default eudocia_bronzerod_rodin_shortcut = 0
default eudocia_bronzerod_rodin_peltnorth = 0
default eudocia_bronzerod_rodin_druidcave = 0
default eudocia_bronzerod_rodin_westgate = 0
default eudocia_bronzerod_rodin_howlersdell = 0
default eudocia_bronzerod_rodin_whitemarshes = 0
default eudocia_bronzerod_rodin_creeks = 0
default eudocia_bronzerod_rodin_mountainroad = 0
default eudocia_bronzerod_rodin_oldtunnel = 0

default eudocia_about_roadclearing = 0
default eudocia_about_roadclearing_price = 0
default eudocia_about_roadclearing_price_base = 20
default eudocia_about_roadclearing_cleared = 0 # day
default eudocia_about_roadclearing_cleared_seen = 0

label eudociahouse01:
    nvl clear
    $ pc_area = "eudociahouse"
    if eudocia_friendship >= 10:
        $ renpy.music.play("audio/track_13eudociahouse02.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    else:
        $ renpy.music.play("audio/track_13eudociahouse01.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    stop nature fadeout 4.0
    if eudocia_image_right != "dark":
        $ eudocia_image_golem01 = renpy.random.choice(['turnedback', 'turnedback', 'turnedleft', 'turnedleft', 'turnedright', 'turnedright', 'none'])
        if eudocia_image_golem01 == "none":
            $ eudocia_image_golem02 = 'nogolemplusback'
        else:
            $ eudocia_image_golem02 = renpy.random.choice([0, 0, 0, 0, 'nogolem'])
    $ eudocia_inside_fluff = renpy.random.choice(['sitting on the stool by the hearth,', 'sitting on the stool, near the cupboard,', 'sitting on the floor, leaning against the bed,', ' leaning against the fur that hangs from the wall,', 'sitting on the floor, surrounded by empty, wooden bowls'])
    $ eudocia_image_eyes = 0
    label eudocia_fluffloop:
        $ eudocia_fluff = renpy.random.choice(['The meadow is so quiet it makes you slow down.', 'White-and-gray birds are sitting on the walls without making a sound, giving you tense looks.', 'You hear heavy steps and the sounds of large objects being dragged around.', 'Only one fly is feasting on the rotting carcass of a snake that’s on the side of the road.', 'A loud roar comes from the north, making your palfrey stop. After a few heartbeats it snorts and moves along.', 'A new spider web is strung between the wall and the gargoyle’s head.', 'There are a few loud ducks on the shore, though they flee after you reach the gargoyle.'])
        if eudocia_fluff_old == eudocia_fluff:
            jump eudocia_fluffloop
        else:
            $ eudocia_fluff_old = huntercabin_fluff
    if quarters >= 40 and quarters < (world_daylength-16):
        $ eudocia_heldobject = renpy.random.choice(['a large, wooden shield in her hands', 'an inkwell placed right in front of her', 'a large rock placed on the floor', 'a brown, thick cape placed on her knees', 'the steel head of a masterful spear in her hands', 'a brand new fishing net lying on the floor'])
    else:
        $ eudocia_heldobject = renpy.random.choice(['a long smoking pipe in her fingers', 'a hot liquid in a wooden bowl in her hands', 'a cold piece of roasted meat on a wooden plate', 'a sharp dagger that she spins in place', 'smoking incense, though she extinguishes it once you show up'])
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ shop = "eudociahouse"
    if not eudocia_firsttime:
        $ world_known_npcs += 1
        $ eudocia_firsttime = 1
        $ world_known_areas += 1
        $ watchtower_unlocked = 1
        jump eudociahousefirsttime01
    elif eudocia_ban:
        jump eudociahousebanned01
    else:
        jump eudociahouseregular01

label eudociahousebanned01:
    $ eudocia_image_right = "dark"
    $ eudocia_image_left = "dark"
    show areapicture eudociahouserightdark behind golem01, golem02, eudocia_image_eyes at basicfade
    $ eudocia_image_golem01 = 0
    $ eudocia_image_golem02 = 0
    $ eudocia_image_eyes = 0
    hide golem01
    hide golem02
    hide eudocia_image_eyes
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'The gargoyle’s eyes shine only briefly. You hear the steps of a golem - it approaches the gate, then stays behind it.
        '
        'No point in staying around. (disabled)':
            pass
        'I don’t have 20 dragon bones. I can’t pay her back. (disabled)' if coins < 20 and quest_bronzerod == 3:
            pass
        'I shout: “I brought your 20 dragon bones. With my apologies.”' if coins >= 20 and quest_bronzerod == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shout: “I brought your coin. With my apologies.”')
            $ eudocia_friendship += 1
            $ custom1 = "“Come, come. Not all is forgotten, but it is forgiven.”"
            label eudociahousebanned02:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                $ eudocia_image_right = "gate"
                show areapicture eudociahouserightgate behind golem01, golem02, eudocia_image_eyes at basicfade
                $ eudocia_image_left = "base"
                $ eudocia_image_golem01 = "gate"
                show golem01 gate at basicfade
                $ eudocia_image_golem02 = "nogolem"
                hide golem02
                $ eudocia_ban = 0
                $ coins -= 20
                $ minutes += 2
                show screen notifyimage( "-20", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-20 {image=cointest}{/i}')
                menu:
                    'The gate opens and the sentinel observes you in silence. After a minute, the enchantress’ feet plod through the yard. {color=#f6d6bd}Eudocia{/color} shows up next to her guard, leans against it, and reaches out to you. You grab your pouch and count down the coins, placing them on her open palm. Finally, she shoves them into her pocket and walks away. [custom1]
                    '
                    'I wait for the golem to get out of my way, then lead {color=#f6d6bd}[horsename]{/color} inside and let it graze on the grass.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for the golem to get out of my way, then lead {color=#f6d6bd}%s{/color} inside and let it graze on the grass.' %horsename)
                        $ eudocia_image_golem01 = "turnedleft" # $ eudocia_image_golem01 = "turnedback"
                        $ eudocia_image_golem02 = "nogolem"
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
                        if eudocia_image_golem02 == "nogolem":
                            show golem02 nogolem_middle at basicfade
                        elif eudocia_image_golem02 == "nogolemplusback":
                            show golem02 nogolemplusback_middle at basicfade
                        else:
                            hide golem02
                        if pc_area == "eudociahouse":
                            $ can_leave = 1
                        else:
                            $ can_leave = 0
                        $ can_rest = 1
                        $ can_items = 1
                        $ questionpreset = "eudocia1"
                        menu:
                            '“Now. What can I do for ye?”
                            '
                            '(eudocia1 set)':
                                pass
        'I shout: “I brought your coin.”' if coins >= 20 and quest_bronzerod == 3:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shout: “I brought your coin.”')
            $ custom1 = "“Come, come. Let’s say we’re even.”"
            jump eudociahousebanned02

label eudociahousefirsttimeALL:
    label eudociahousefirsttime01:
        $ eudocia_image_left = "dark" # "dark" "base"
        $ eudocia_image_right = "dark" # "dark" "gate" "base"
        $ eudocia_image_golem01 = 0
        $ eudocia_image_golem02 = 0
        show areapicture eudociahouseleftdark behind golem01, golem02, eudocia_image_eyes at basicfade
        if eudocia_image_golem02 == "nogolem":
            show golem02 nogolem at basicfade
        elif eudocia_image_golem02 == "nogolemplusback":
            show golem02 nogolemplusback at basicfade
        else:
            hide golem02
        nvl clear
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ renpy.force_autosave(take_screenshot=False, block=True)
        menu:
            'The road leads you downhill, to the edge of a lake. The clearing around the dwelling is quiet, with no crickets, flies, or even toads. The grass is not even knee-high.
            \n\nThere are no signs of a wharf or boats. The wall wasn’t coated, and has already been bitten by winds and rains.
            '
            'I look for an entrance.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for an entrance.')
                show areapicture eudociahouserightdark behind golem01, golem02, eudocia_image_eyes at basicfade
                menu:
                    'Right next to the gate, a gargoyle, or a stone look-alike, kneels on a slab. It’s dark purple, almost black, with yellow, pointy teeth, though its half-open mouth has no tongue, and the creature doesn’t move even an inch. The eyes have been replaced by crystals, red like currant juice.
                    '
                    'I knock on the gate.' if not eudocia_gate_attempt01:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knock on the gate.')
                        $ eudocia_gate_attempt01 = 1
                        jump eudociahousefirsttime02a
                    '“Anyone home?!”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Anyone home?!”')
                        jump eudociahousefirsttime02b
                    'I touch the gargoyle':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I touch the gargoyle.')
                        jump eudociahousefirsttime02c
                    'I push the gate.' if not eudocia_gate_attempt02:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I push the gate.')
                        $ eudocia_gate_attempt02 = 1
                        jump eudociahousefirsttime02d

    label eudociahousefirsttime02a:
        menu:
            'Finding no knocker, you use your fist. There’s no response.
            '
            '“Anyone home?!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Anyone home?!”')
                jump eudociahousefirsttime02b
            'I touch the gargoyle.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I touch the gargoyle.')
                $ eudocia_gate_attempt03 = 1
                jump eudociahousefirsttime02c
            'I push the gate.' if not eudocia_gate_attempt02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I push the gate.')
                $ eudocia_gate_attempt02 = 1
                jump eudociahousefirsttime02d

    label eudociahousefirsttime02d:
        menu:
            'It shakes, but is held by a wooden bar. Soon, another sound comes from the inside - slow, heavy steps.
            '
            'I knock on the gate.' if not eudocia_gate_attempt01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I knock on the gate.')
                $ eudocia_gate_attempt01 = 1
                jump eudociahousefirsttime02a
            '“Anyone home?!”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Anyone home?!”')
                jump eudociahousefirsttime02b
            'I touch the gargoyle.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I touch the gargoyle.')
                jump eudociahousefirsttime02c

    label eudociahousefirsttime02b:
        $ eudocia_screaming = 1
        $ eudocia_image_eyes = 1
        show eudocia_image_eyes 01 at basicfade
        menu:
            'Your voice is welcomed by the screeching of dozens of avian throats. They take off from behind the wall, heading toward the lake. After a few breaths, the {i}eyes{/i} of the gargoyle grow brighter.
            \n\n“What’s with all the ape shouts? Ye lost?” The words are coming from the monster’s mouth, though it remains still. “Stand in front of me, I want to see ya mug.” The drawling voice belongs to a woman, but is lined with unnatural creaking.
            '
            'I step closer.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step closer.')
                $ at_activate = 1
                $ at = 0
                menu:
                    'The eyes don’t rotate, nor blink. “So? Who are ye?”
                    '
                    ' (disabled)' ( condition="at == 0" ):
                        pass
                    '“I’m [pcname], the new roadwarden. I hope you’re having a great day!”' ( condition="at == 'friendly'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (friendly) “I’m %s, the new roadwarden. I hope you’re having a great day!”' %pcname)
                        $ at_activate = 0
                        $ at = 0
                        jump eudociahousefirsttime03friendly
                    '“I must say, as a roadwarden, I’ve seen some disgusting beasts, but you surely have the kindest voice of them all.”' ( condition="at == 'playful'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (playful) “I must say, as a roadwarden, I’ve seen some disgusting beasts, but you surely have the kindest voice of them all.”')
                        $ at_activate = 0
                        $ at = 0
                        jump eudociahousefirsttime03playful
                    '“I’m [pcname], the new roadwarden.”' ( condition="at == 'distanced'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (distanced) “I’m %s, the new roadwarden.”' %pcname)
                        $ at_activate = 0
                        $ at = 0
                        jump eudociahousefirsttime03distanced
                    '“I’m the new roadwarden, and I value my time. Let’s speak face to face.”' ( condition="at == 'intimidating'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (intimidating) “I’m the new roadwarden, and I value my time. Let’s speak face to face.”')
                        $ at_activate = 0
                        $ at = 0
                        jump eudociahousefirsttime03intimidating
                    'I introduce myself. “I’d like to ask you a few questions, if that’s fine with you.”' ( condition="at == 'vulnerable'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (vulnerable) I introduce myself. “I’d like to ask you a few questions, if that’s fine with you.”')
                        $ at_activate = 0
                        $ at = 0
                        jump eudociahousefirsttime03vulnerable

    label eudociahousefirsttime02c:
        $ eudocia_image_eyes = 1
        show eudocia_image_eyes 01 at basicfade
        menu:
            'Your hand seems tiny when placed on the monster’s shoulder, which is coarse and cold like a rock. You consider pushing one of the teeth, but the {i}eyes{/i} of the gargoyle suddenly grow brighter.
            \n\n“What d’ye want? I’m not expecting anyone.” The words are coming from the monster’s mouth, though it remains still. “Stand in front of me, I want to see ya mug.” The drawling voice belongs to a woman, but is lined with unnatural creaking.
            '
            'I step closer.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step closer.')
                $ at_activate = 1
                $ at = 0
                menu:
                    'The eyes don’t rotate, nor blink. “Who are ye?”
                    '
                    ' (disabled)' ( condition="at == 0" ):
                        pass
                    '“I’m [pcname], the new roadwarden. I hope you’re having a great day!”' ( condition="at == 'friendly'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (friendly) “I’m %s, the new roadwarden. I hope you’re having a great day!”' %pcname)
                        $ at_activate = 0
                        $ at = 0
                        jump eudociahousefirsttime03friendly
                    '“I must say, as a roadwarden, I’ve seen some disgusting beasts, but you surely have the kindest voice of them all.”' ( condition="at == 'playful'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (playful) “I must say, as a roadwarden, I’ve seen some disgusting beasts, but you surely have the kindest voice of them all.”')
                        $ at_activate = 0
                        $ at = 0
                        jump eudociahousefirsttime03playful
                    '“I’m [pcname], the new roadwarden.”' ( condition="at == 'distanced'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (distanced) “I’m %s, the new roadwarden.”' %pcname)
                        $ at_activate = 0
                        $ at = 0
                        jump eudociahousefirsttime03distanced
                    '“I’m the new roadwarden, and I value my time. Let’s speak face to face.”' ( condition="at == 'intimidating'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (intimidating) “I’m the new roadwarden, and I value my time. Let’s speak face to face.”')
                        $ at_activate = 0
                        $ at = 0
                        jump eudociahousefirsttime03intimidating
                    'I introduce myself. “I’d like to ask you a few questions, if that’s fine with you.”' ( condition="at == 'vulnerable'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (vulnerable) I introduce myself. “I’d like to ask you a few questions, if that’s fine with you.”')
                        $ at_activate = 0
                        $ at = 0
                        jump eudociahousefirsttime03vulnerable

    label eudociahousefirsttime03friendly: #I’m [pcname], the new roadwarden. I hope you’re having a great day!
        $ eudocia_friendship += 0
        menu:
            'During the long pause, the glow of the gargoyle’s eyes subside. Once they light up again, the voice isn’t much softer.
            \n\n“Well, good to see a new warden. Ye came to pick up some stuff? Ye’re many days too early. Or d’ye even know who I am?”
            '
            '“Oh, but of course.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Oh, but of course.”')
                python:
                    search = renpy.input("What do you call her?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump eudociahousefirsttime04
            '“I don’t, I’m afraid. I’m just getting to know the realm.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t, I’m afraid. I’m just getting to know the realm.”')
                jump eudociahousefirsttime04b

    label eudociahousefirsttime03playful: # I must say, as a roadwarden, I’ve seen some disgusting beasts, but you surely have the kindest voice of them all.
        $ eudocia_friendship -= 1
        menu:
            'During the long pause, the glow of the gargoyle’s eyes subside. Once they light up again, the voice gets even colder.
            \n\n“I don’t know what answer ye’re looking for, so ye’ll get none. D’ye even know who I am?”
            '
            '“Oh, but of course.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Oh, but of course.”')
                python:
                    search = renpy.input("What do you call her?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump eudociahousefirsttime04
            '“I don’t, I’m afraid. I’m just getting to know the realm.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t, I’m afraid. I’m just getting to know the realm.”')
                jump eudociahousefirsttime04b

    label eudociahousefirsttime03distanced: # I’m [pcname], the new roadwarden.
        $ eudocia_friendship += 1
        menu:
            '“I see.” A short pause. “I don’t leave my house often, but I may have a job for a traveler. Ye know who I am, right?”
            '
            '“Naturally.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I do, naturally.”')
                python:
                    search = renpy.input("What do you call her?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump eudociahousefirsttime04
            '“No. I’m just looking around.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t. I’m just getting to know the realm.”')
                jump eudociahousefirsttime04b

    label eudociahousefirsttime03intimidating: # I’m the new roadwarden, and I value my time. Let’s speak face to face.
        $ eudocia_friendship -= 1
        menu:
            'You hear a chuckle. “I’m also a busy soul, stranger, and not one to be ordered around. Ye don’t know where ye are, clearly.”
            '
            '“Yet I do.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Yet I do.”')
                python:
                    search = renpy.input("What do you call her?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump eudociahousefirsttime04
            '“No. Wherever the road takes me, I follow.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “No. Wherever the road takes me, I follow.”')
                jump eudociahousefirsttime04b

    label eudociahousefirsttime03vulnerable: #I introduce myself. “I’d like to ask you a few questions, if that’s fine with you.”
        $ eudocia_friendship -= 1
        menu:
            '“Is that so? My house isn’t a shelter for vagrants, ye need to stay somewhere, go back to the tower. D’ye even know who I am?”
            '
            '“I believe so.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I believe so.”')
                python:
                    search = renpy.input("What do you call her?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                    search = search.strip().lower().replace(" ", "")
                    if not search:
                        search = "nothing"
                jump eudociahousefirsttime04
            '“I don’t, I’m afraid. I’m just getting to know the realm.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t, I’m afraid. I’m just getting to know the realm.”')
                jump eudociahousefirsttime04b

    label eudociahousefirsttime04:
        if search == "eudocia":
            $ eudocia_friendship += 1
            $ eudocia_toldname += 1
            jump eudociahousefirsttime04a
        elif search == "magiccrafter" or search == "magicalcrafter" or search == "magecrafter" or search == "magiccraftsman" or search == "crafter" or search == "mage" or search == "wizard" or search == "sorcerer" or search == "sorceress" or search == "enchanter" or search == "enchantress" or search == "theenchanter" or search == "theenchantress" or search == "antheenchanter" or search == "antheenchantress":
            menu:
                '“Ye for real? Don’t ye know my name?”
                '
                '“I don’t.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t.”')
                    jump eudociahousefirsttime04b
                '“I’m sorry, I’ve never heard it.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sorry, I’ve never heard it.”')
                    jump eudociahousefirsttime04b
                '“It’s...”':
                    python:
                        search = renpy.input("What do you call her?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                        search = search.strip().lower().replace(" ", "")
                        if not search:
                            search = "nothing"
                    jump eudociahousefirsttime04
        #############################
        elif search == "fuck" or search == "sex" or search == "fucker" or search == "idiot" or search == "dumb" or search == "wtf" or search == "shit" or search == "nigger" or search == "nigga" or search == "fag" or search == "bitch" or search == "whore" or search == "cunt":
            python:
                search = renpy.input("...Let’s try this again. What do you call her?", default="", pixel_width=800, exclude="<>?;'][}{,./1234567890!@#$%^&*()-_=+")
                search = search.strip().lower().replace(" ", "")
                if not search:
                    search = "nothing"
            jump eudociahousefirsttime04
        #############################
        else:
            jump eudociahousefirsttime04b

    label eudociahousefirsttime04a:
        if quarters >= 40 and quarters < (world_daylength-16):
            menu:
                'Short pause. “Ye’re disturbing my work. It’s the middle of the day, I need to stay focused.” You hear her deep, annoyed breath. “For a warden, I’ll make this {i}one{/i} exception. But next time, come in the early morning, or soon before the night. Wait where ye are, we’re opening the gate.”
                \n\nThe monster’s eyes darken again. Soon after, you hear heavy steps, and the earth shakes. Something lifts the beam blocking the gate. You realize that your hand is already on the haft of your axe.
                '
                'I try to relax. I’m safe.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to relax. I’m safe.')
                    jump eudociahousefirsttime05
                'One day, such instincts are going to save my life.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- One day, such instincts are going to save my life.')
                    jump eudociahousefirsttime05
        else:
            menu:
                'Short pause. “Well, at least ye’re respecting the hour, instead of interrupting my work. Remember, I meet with people only in the evenings, or the early mornings. Wait where ye are, we’re opening the gate”
                \n\nThe monster’s eyes darken again. Soon after, you hear heavy steps, and the earth shakes. Something lifts the beam blocking the gate. You realize that your hand is already on the haft of your axe.
                '
                'I try to relax. I’m safe.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to relax. I’m safe.')
                    jump eudociahousefirsttime05
                'One day, such instincts are going to save my life.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- One day, such instincts are going to save my life.')
                    jump eudociahousefirsttime05

    label eudociahousefirsttime04b:
        if quarters >= 40 and quarters < (world_daylength-16):
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ eudocia_toldname = 1
            $ eudocia_image_eyes = 0
            hide eudocia_image_eyes
            menu:
                '“So, ye lost ya way, and now ye’re wasting my time.” Long pause. “I’m {color=#f6d6bd}Eudocia{/color}, the only enchantress ye’ll find in this land. And ye’re disturbing my work. I don’t see people in the middle of the day. Return in the early morning, or a few hours before dusk, if ye {i}have to{/i}. Best yet, don’t bother me at all.”
                \n\nThe monster’s eyes darken again. Your mount is ready to ride away.
                '
                'I wait for as long as it takes for her to let me in.' ( condition="quarters < (world_daylength-16)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for as long as it takes for her to let me in.')
                    $ quarters = (world_daylength-16)
                    $ custom1 = "It’s getting colder but, finally, the monster’s eyes glow red."
                    jump eudociahousefirstconversation_wait01
                'I touch the head again.' ( condition="quarters >= (world_daylength-16)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I touch the head again.')
                    $ custom1 = "The monster’s eyes glow red."
                    jump eudociahousefirstconversation_wait01
                'It will make her angry, but I touch the gargoyle’s head. “I’m afraid I have to speak with you {i}right now{/i}.”' ( condition="quarters < (world_daylength-16)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will make her angry, but I touch the gargoyle’s head. “I’m afraid I have to speak with you {i}right now{/i}.”')
                    $ custom1 = "A long pause, until the monster’s eyes glow red."
                    $ eudocia_friendship -= 1
                    jump eudociahousefirstconversation_wait01
        else:
            menu:
                '“So, ye lost ya way, and now ye’re wasting my time. Ye’re lucky I’m not working. Remember, I meet with people only in the evenings, or the early mornings. Wait where ye are, we’re opening the gate.”
                \n\nThe monster’s eyes darken again. Soon after, you hear heavy steps, and the earth shakes. Something lifts the beam blocking the gate. You realize that your hand is already on the haft of your axe.
                '
                'I try to relax. I’m safe.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to relax. I’m safe.')
                    jump eudociahousefirsttime05
                'One day, such instincts are going to save my life.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- One day, such instincts are going to save my life.')
                    jump eudociahousefirsttime05

    label eudociahousefirsttime05:
        $ eudocia_image_eyes = 0
        hide eudocia_image_eyes
        if not eudocia_conversation:
            $ eudocia_conversation = 1
            jump eudociahouseconversationfirsttime01
        else:
            jump eudociahouseconversationregular01

label eudociahouseregular01:
    if eudocia_image_right != "dark":
        $ eudocia_image_right = "base"
    if eudocia_image_left != "dark":
        $ eudocia_image_left = "base"
    if eudocia_image_right == "dark":
        show areapicture eudociahouserightdark behind golem01, golem02, eudocia_image_eyes at basicfade
    if eudocia_image_right == "gate":
        show areapicture eudociahouserightgate behind golem01, golem02, eudocia_image_eyes at basicfade
    if eudocia_image_right == "base":
        show areapicture eudociahouserightbase behind golem01, golem02, eudocia_image_eyes at basicfade
    if eudocia_image_right != "dark":
        if eudocia_image_golem01 == "gate":
            show golem01 gate at basicfade
        elif eudocia_image_golem01 == "turnedback":
            show golem01 turnedback at basicfade
        elif eudocia_image_golem01 == "turnedleft":
            show golem01 turnedleft at basicfade
        elif eudocia_image_golem01 == "turnedright":
            show golem01 turnedright at basicfade
        else:
            hide golem01
    hide golem02
    if eudocia_image_eyes == 1:
        show eudocia_image_eyes 01 at basicfade
    else:
        hide eudocia_image_eyes
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ eudocia_screaming = 0
    $ renpy.force_autosave(take_screenshot=False, block=True)
    if not eudocia_conversation:
        if quarters >= 40 and quarters < (world_daylength-16):
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ eudocia_image_eyes = 0
            hide eudocia_image_eyes
            menu:
                '[eudocia_fluff]
                \n\nYou touch the cold chest. There’s no response.
                '
                'I wait for as long as it takes for her to let me in.' ( condition="quarters < (world_daylength-16)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for as long as it takes for her to let me in.')
                    $ quarters = (world_daylength-16)
                    $ custom1 = "It’s getting colder but, finally, the monster’s eyes glow red."
                    jump eudociahousefirstconversation_wait01
                'It will make her angry, but I touch the gargoyle’s head. “I’m afraid I have to speak with you {i}right now{/i}.”' ( condition="quarters < (world_daylength-16)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will make her angry, but I touch the gargoyle’s head. “I’m afraid I have to speak with you {i}right now{/i}.”')
                    $ custom1 = "A long pause, until the monster’s eyes glow red."
                    $ eudocia_friendship -= 1
                    jump eudociahousefirstconversation_wait01
                'I touch the head again.' ( condition="quarters >= (world_daylength-16)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I touch the head again.')
                    $ custom1 = "The monster’s eyes glow red."
                    jump eudociahousefirstconversation_wait01
        else:
            $ custom1 = "You touch the cold shell. The monster’s eyes glow red."
            label eudociahousefirstconversation_wait01:
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                menu:
                    '[custom1] “Go inside, I’ll be with ye soon.”
                    \n\nThe monster’s eyes darken again. Soon after, you hear heavy steps, and the earth shakes. Something lifts the beam blocking the gate. You realize that your hand is already on the haft of your axe.
                    '
                    'I try to relax. I’m safe.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I try to relax. I’m safe.')
                        jump eudociahousefirsttime05
                    'One day, such instincts are going to save my life.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- One day, such instincts are going to save my life.')
                        jump eudociahousefirsttime05
    elif eudocia_friendship >= eudocia_friendship_tierlevel:
        $ eudocia_image_eyes = 1
        show eudocia_image_eyes 01 at basicfade
        if quarters >= 40 and quarters < (world_daylength-16):
            $ custom1 = "Come inside, I could use a break."
        else:
            $ custom1 = "Come inside, I wouldn’t mind a bit of company."
        menu:
            'You touch the cold shell. The monster’s eyes glow red.
            \n\n“[pcname]! [custom1]”
            \n\nThe golems let you in.
            '
            'I enter the yard.' if eudocia_friendship < eudocia_friendship_tierlevel or not eudocia_inside_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                jump eudociahouseconversationregular01
            'I go straight to the house.' if eudocia_friendship >= eudocia_friendship_tierlevel and eudocia_inside_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go straight to the house.')
                jump eudociahouseconversationregular01
    else:
        if quarters >= 40 and quarters < (world_daylength-16):
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ eudocia_image_eyes = 0
            hide eudocia_image_eyes
            menu:
                '[eudocia_fluff]
                \n\nYou touch the cold chest. There’s no response.
                '
                'I wait for as long as it takes for her to let me in.' ( condition="quarters < (world_daylength-16)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for as long as it takes for her to let me in.')
                    $ custom1 = "It’s getting colder but, finally, the monster’s eyes glow red."
                    $ quarters = (world_daylength-16)
                    label eudociahousefirstconversation_wait02:
                        $ can_leave = 0
                        $ can_rest = 0
                        $ can_items = 0
                        $ eudocia_image_eyes = 1
                        show eudocia_image_eyes 01 at basicfade
                        menu:
                            '[custom1] “Go inside, I’ll be with ye soon.”
                            \n\nThe stone creature lets you in.
                            '
                            'I enter the yard.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                                $ quarters += 1
                                jump eudociahouseconversationregular01
                'I touch the head again.' ( condition="quarters >= (world_daylength-16)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I touch the head again.')
                    $ custom1 = "The monster’s eyes glow red."
                    jump eudociahousefirstconversation_wait02
                'It will make her angry, but I touch the gargoyle’s head. “I’m afraid I have to speak with you {i}right now{/i}.”' ( condition="quarters < (world_daylength-16)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will make her angry, but I touch the gargoyle’s head. “I’m afraid I have to speak with you {i}right now{/i}.”')
                    $ custom1 = "A long pause, until the monster’s eyes glow red."
                    $ eudocia_friendship -= 1
                    jump eudociahousefirstconversation_wait02
        else:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            $ eudocia_image_eyes = 1
            show eudocia_image_eyes 01 at basicfade
            menu:
                '[eudocia_fluff]
                \n\nYou touch the cold shell. The monster’s eyes glow red.
                \n\n“Go inside, I’ll be with ye soon.”
                \n\nThe stone creature lets you in.
                '
                'I enter the yard.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                    $ quarters += 1
                    jump eudociahouseconversationregular01

label eudociahouseconversationfirsttimeALL:
    label eudociahouseconversationfirsttime01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ eudocia_image_right = "gate"
        show areapicture eudociahouserightgate behind golem01, golem02, eudocia_image_eyes at basicfade
        $ eudocia_image_left = "base"
        $ eudocia_image_golem01 = "gate"
        show golem01 gate at basicfade
        $ eudocia_image_golem02 = 0
        hide golem02
        menu:
            'The gate opens violently and rebounds with a loud thud, almost closing again. The creature in front of you is made of floating rocks that appear to be connected, but it’s just an illusion. They could twist and bend in every direction. The eyeless sentinel faces you blankly.
            \n\nYou’ve seen other golems in {color=#f6d6bd}Hovlavan{/color}, endlessly helping with bothersome tasks, but you’ve no idea what makes them move. It lowers its slab-like hands and steps aside, making way for you. Its head rotates, following your steps, but other than that, it’s as motionless as a statue.
            '
            'I enter the yard.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the yard.')
                if not eudocia_screaming:
                    $ eudocia_screaming2 = "A few birds stare at you from the roofs, while many more ignore you. None seem willing to approach the garden patches, despite the growing, though neglected, vegetables."
                else:
                    $ eudocia_screaming2 = "The garden patches, covered with herbs and vegetables, are neglected."
                if not eudocia_toldname:
                    $ eudocia_toldname = "“And here I am. {color=#f6d6bd}Eudocia{/color}, the best and only enchantress in this corner of the world.”"
                else:
                    $ eudocia_toldname = "“We don’t need more salutations. So.”"
                if quarters >= 40 and quarters < (world_daylength-16):
                    $ eudocia_about_closingthegate = "I let ye in this time, but it won’t happen again, not during my work."
                else:
                    $ eudocia_about_closingthegate = "Good that ye came at such an hour, keep it up in the future."
                $ eudocia_image_left = "base"
                $ eudocia_image_golem01 = "turnedback"
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
                if eudocia_image_golem02 == "nogolem":
                    show golem02 nogolem_middle at basicfade
                elif eudocia_image_golem02 == "nogolemplusback":
                    show golem02 nogolemplusback_middle at basicfade
                else:
                    hide golem02
                menu:
                    'The house in front of you has a huge entrance, just large enough for a golem. The building is whitewashed, but the lime is aged and damaged.
                    \n\nThe tools are spread around in no particular order. The rocks resting on the top of the shed resemble the golems. [eudocia_screaming2]
                    \n\nIt’s quiet here.
                    '
                    'I wander about.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wander about.')
                        $ custom5 = "Yer free to look around, but ye won’t find much. I don’t {i}hoard{/i} treasures, I make them."
                        menu:
                            'By city standards, the place is spacious - it could fit a few more houses. The smaller structures look solid, and you spot many tools made of iron and steel. The owner must be wealthy - the labor and building materials must have been worth a sack of dragon bones.
                            \n\nYet the walls are far from safe. Any large monster could burst inside, and the house seems to have no other protection.
                            \n\nFinally, a leaf of the door opens.
                            '
                            'I step closer.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step closer.')
                                jump eudociahouseconversationfirsttime02
                    'I approach the sitting golem.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the sitting golem.')
                        $ custom5 = "No surprise that it caught ya eye, but don’t disturb it, it’s very much awoken and will defend itself. Or me, if it comes to it."
                        if pc_class == "scholar":
                            $ at_unlock_knowledge = 1
                            $ at = 0
                        if quest_studyingthegolems_description01:
                            $ quest_studyingthegolems_description01 = "I asked {color=#f6d6bd}Eudocia{/color} a few things about the golems."
                            $ quest_studyingthegolems_description03 = "I had a chance to take a closer look at one of the golems."
                        else:
                            $ quest_studyingthegolems_description03 = "I had a chance to take a closer look at one of the golems. Maybe I could learn more from its creator."
                        if quest_studyingthegolems == 1:
                            $ renpy.notify("Journal updated: Studying the Golems")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Studying the Golems{/i}')
                        menu:
                            'It seems dead, “inactive,” as cityfolk would call it, but the pneuma still makes its chunks float less than an inch away from one another. It doesn’t react to your presence.
                            \n\nUnlike the previous golem, this one bears engraved signs on its larger rocks. Their meaning is unclear to you, and you can’t tell if they’re a decoration, or carriers of a spell.
                            \n\nA leaf of the doors opens.
                            '
                            'I know these letters.' ( condition="at == 'knowledge'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I know these letters.')
                                $ at_unlock_knowledge = 0
                                $ at = 0
                                $ quest_studyingthegolems_description03b = "I’ve learned that at least some of the golems are covered with inscriptions, possibly enhancing their powers."
                                if quest_studyingthegolems == 1:
                                    $ renpy.notify("Journal updated: Studying the Golems")
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Studying the Golems{/i}')
                                menu:
                                    'The signs represent regular words used in Wright’s Tablets. Their shapes are very old, angular, not adjusted to the softness of a quill.
                                    \n\nThe words read as follows: {i}hunt{/i}, {i}prey{/i}, {i}chase{/i}, {i}meat{/i}, {i}beast{/i}, {i}run{/i}, {i}bring{/i}, {i}wait{/i}, and {i}disguise{/i}.
                                    \n\nThe golem’s owner is standing behind you.
                                    '
                                    'I turn toward them.':
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I turn toward them.')
                                        jump eudociahouseconversationfirsttime02
                            'I step closer.' ( condition="at != 'knowledge'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step closer.')
                                $ at_unlock_knowledge = 0
                                $ at = 0
                                jump eudociahouseconversationfirsttime02

    label eudociahouseconversationfirsttime02:
        menu:
            'The woman is tall and stands upright, with her arms crossed and legs apart. She’s more than thirty, with a face touched by lack of sleep. She gives you a long look, observing your blade, hands, boots, forehead... Everything but your eyes.
            \n\n“I greet ye.” Without the distortion caused by the gargoyle, her strong voice isn’t as disquieting. “[custom5]”
            '
            'I give her a better look.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I give her a better look.')
                $ at_activate = 1
                $ at = 0
                menu:
                    'She’s wearing a long, ragged robe, covered in stains. It used to be blue, but now is unevenly pale. She’s barefoot, with skin covered with dust and dirt. Her dark hair was recently washed, but it’s untidily spread on her shoulders, back, and chest. She wears no jewelry, belt, or buckles.
                    '
                    ' (disabled)' ( condition="at == 0" ):
                        pass
                    '“I’m glad you have a moment to spare. I won’t bother you for long.”' ( condition="at == 'friendly'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (friendly) “I’m glad you have a moment to spare. I won’t bother you for long.”')
                        $ at = 0
                        $ at_activate = 0
                        $ description_eudocia02 = "She doesn’t allow anyone in her house while she works. I should ask her to meet me in the early morning, or a few hours before dusk."
                        $ eudocia_image_golem01 = "turnedleft"
                        show golem01 turnedleft_middle at basicfade
                        $ eudocia_image_right = "base"
                        $ quest_explorepeninsula_description15 = "I met {color=#f6d6bd}Eudocia{/color}, a skilled enchantress who lives near the western road. The guild could benefit from her powerful golems."
                        $ renpy.notify("Journal updated: Explore the Peninsula")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                        menu:
                            'She looks at the ground and drawls out her words. “I sure hope not. I’m not interested in chatter. If ye need to bother me, speak in the tongue of dragons and barter. I don’t serve stew, I don’t offer baths. If ye come here, I better get aught from it.”
                            \n\nShe walks past you and cocks her head toward the golem who let you in. It turns around and shuts the gate. “[eudocia_about_closingthegate] If ye ever come here in the middle of the day, ye’ll stand outside, looking at the doors like an ibex.”
                            \n\n[eudocia_toldname] Her voice remains cold. “Why are ye here?”
                            '
                            '“I was asked to deliver the writing quills to the monastery.”' if quest_pensformonastery == 1 and not eudocia_about_pens:
                                $ eudocia_about_pens = 1
                                jump eudociahouseaboutpens01
                            '“{color=#f6d6bd}Photios{/color} has sent me to buy a {i}spirit rock{/i} for his daughter. He hopes it will enhance {color=#f6d6bd}Phoibe’s{/color} pneuma.”' if not eudocia_about_spiritrock_problem and quest_spiritrock == 1:
                                $ eudocia_about_spiritrock_problem = 1
                                jump eudociaaskedaboutshop01av02
                            '“I’m trying to learn more about the peninsula.”' if not eudocia_about_peninsula:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about the peninsula.”')
                                $ eudocia_about_peninsula = 1
                                jump eudocia_about_peninsula00
                            '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' if quest_asterion == 1 and not asterion_found and not eudocia_about_asterion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
                                jump eudocia_about_asterion00
                            '“I’m looking for a job.”' if not eudocia_about_job01:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a job.”')
                                $ eudocia_about_job01 = 1
                                jump eudocia_about_job00
                            '“I was hoping you could fill an item of mine with pneuma.”' if not eudocia_about_enchanting_items:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was hoping you could fill an item of mine with pneuma.”')
                                $ eudocia_about_enchanting_items = 1
                                jump eudocia_about_enchanting_items01after
                    '“It takes quite a few hours to reach this place. I bet not many people come around.”' ( condition="at == 'playful'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (playful) “It takes quite a few hours to reach this place. I bet not many people come around.”')
                        $ at = 0
                        $ at_activate = 0
                        $ description_eudocia02 = "She doesn’t allow anyone in her house while she works. I should ask her to meet me in the early morning, or a few hours before dusk."
                        $ eudocia_image_golem01 = "turnedleft"
                        show golem01 turnedleft_middle at basicfade
                        $ eudocia_image_right = "base"
                        $ quest_explorepeninsula_description15 = "I met {color=#f6d6bd}Eudocia{/color}, a skilled enchantress who lives near the western road. The guild could benefit from her powerful golems."
                        $ renpy.notify("Journal updated: Explore the Peninsula")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                        $ eudocia_friendship -= 1
                        menu:
                            'She looks at the ground, takes a deep breath, and drawls out her words. “And I avoid their visits. I’m not in the mood for chatter. If ye need to bother me, speak in the tongue of dragons and barter. I don’t serve mead, I don’t offer baths. If ye come here, I better get aught from it.”
                            \n\nShe walks past you and cocks her head toward the golem who let you in. It turns around and shuts the gate. “[eudocia_about_closingthegate] If ye ever come here in the middle of the day, ye’ll stand outside, looking at the doors like an ibex.”
                            \n\n[eudocia_toldname] Her voice gets even harsher. “What d’ye want?”
                            '
                            '“I was asked to deliver the writing quills to the monastery.”' if quest_pensformonastery == 1 and not eudocia_about_pens:
                                $ eudocia_about_pens = 1
                                jump eudociahouseaboutpens01
                            '“{color=#f6d6bd}Photios{/color} has sent me to buy a {i}spirit rock{/i} for his daughter. He hopes it will enhance {color=#f6d6bd}Phoibe’s{/color} pneuma.”' if not eudocia_about_spiritrock_problem and quest_spiritrock == 1:
                                $ eudocia_about_spiritrock_problem = 1
                                jump eudociaaskedaboutshop01av02
                            '“I’m trying to learn more about the peninsula.”' if not eudocia_about_peninsula:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about the peninsula.”')
                                $ eudocia_about_peninsula = 1
                                jump eudocia_about_peninsula00
                            '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' if quest_asterion == 1 and not asterion_found and not eudocia_about_asterion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
                                jump eudocia_about_asterion00
                            '“I’m looking for a job.”' if not eudocia_about_job01:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a job.”')
                                $ eudocia_about_job01 = 1
                                jump eudocia_about_job00
                            '“I was hoping you could fill an item of mine with pneuma.”' if not eudocia_about_enchanting_items:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was hoping you could fill an item of mine with pneuma.”')
                                $ eudocia_about_enchanting_items = 1
                                jump eudocia_about_enchanting_items01after
                    '“Let’s get to it.”' ( condition="at == 'distanced'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (distanced) “Let’s get to it.”')
                        $ at = 0
                        $ at_activate = 0
                        $ description_eudocia02 = "She doesn’t allow anyone in her house while she works. I should ask her to meet me in the early morning, or a few hours before dusk."
                        $ eudocia_image_golem01 = "turnedleft"
                        show golem01 turnedleft_middle at basicfade
                        $ eudocia_image_right = "base"
                        $ quest_explorepeninsula_description15 = "I met {color=#f6d6bd}Eudocia{/color}, a skilled enchantress who lives near the western road. The guild could benefit from her powerful golems."
                        $ renpy.notify("Journal updated: Explore the Peninsula")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                        $ eudocia_friendship += 1
                        menu:
                            'She nods and looks at your ear. You can’t figure out the color of her eyes. Green? “Good. This place is not open to those who don’t use the tongue of dragons and barter, and unlike those from {color=#f6d6bd}Creeks{/color}, idle talk puts me to sleep, or to nightmares, rather. If ye come here, I better get aught from it.”
                            \n\n“For now, let’s not invite a dragon.” She walks past you and cocks her head toward the golem who let you in. It turns around and shuts the gate. “[eudocia_about_closingthegate] If ye ever come here in the middle of the day, ye’ll stand outside, looking at the doors like an ibex.”
                            \n\n[eudocia_toldname] She looks to the sky, her voice remaining bored. “If ye’re here to make a deal, I’m ready to hear ye. But don’t test my patience.”
                            '
                            '“I was asked to deliver the writing quills to the monastery.”' if quest_pensformonastery == 1 and not eudocia_about_pens:
                                $ eudocia_about_pens = 1
                                jump eudociahouseaboutpens01
                            '“{color=#f6d6bd}Photios{/color} has sent me to buy a {i}spirit rock{/i} for his daughter. He hopes it will enhance {color=#f6d6bd}Phoibe’s{/color} pneuma.”' if not eudocia_about_spiritrock_problem and quest_spiritrock == 1:
                                $ eudocia_about_spiritrock_problem = 1
                                jump eudociaaskedaboutshop01av02
                            '“I’m trying to learn more about the peninsula.”' if not eudocia_about_peninsula:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about the peninsula.”')
                                $ eudocia_about_peninsula = 1
                                jump eudocia_about_peninsula00
                            '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' if quest_asterion == 1 and not asterion_found and not eudocia_about_asterion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
                                jump eudocia_about_asterion00
                            '“I’m looking for a job.”' if not eudocia_about_job01:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a job.”')
                                $ eudocia_about_job01 = 1
                                jump eudocia_about_job00
                            '“I was hoping you could fill an item of mine with pneuma.”' if not eudocia_about_enchanting_items:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was hoping you could fill an item of mine with pneuma.”')
                                $ eudocia_about_enchanting_items = 1
                                jump eudocia_about_enchanting_items01after
                    '“Thank you for agreeing to see me.”' ( condition="at == 'vulnerable'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- (vulnerable) “Thank you for agreeing to see me.”')
                        $ at = 0
                        $ at_activate = 0
                        $ description_eudocia02 = "She doesn’t allow anyone in her house while she works. I should ask her to meet me in the early morning, or a few hours before dusk."
                        $ eudocia_image_golem01 = "turnedleft"
                        show golem01 turnedleft_middle at basicfade
                        $ eudocia_image_right = "base"
                        $ quest_explorepeninsula_description15 = "I met {color=#f6d6bd}Eudocia{/color}, a skilled enchantress who lives near the western road. The guild could benefit from her powerful golems."
                        $ renpy.notify("Journal updated: Explore the Peninsula")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                        menu:
                            'She absently stares at your nose. “If ye’re looking for help, ye came to the wrong place. I don’t make sacrifices for others. If ye need to bother me, speak in the tongue of dragons and barter. It’s not a sanctuary, I offer no bed or stew.”
                            \n\nShe walks past you and cocks her head toward the golem who let you in. It turns around and shuts the gate. “[eudocia_about_closingthegate] If ye ever come here in the middle of the day, ye’ll stand outside, looking at the doors like an ibex.”
                            \n\n[eudocia_toldname] Her voice gets cold, harsh. “Why are ye here?”
                            '
                            '“I was asked to deliver the writing quills to the monastery.”' if quest_pensformonastery == 1 and not eudocia_about_pens:
                                $ eudocia_about_pens = 1
                                jump eudociahouseaboutpens01
                            '“{color=#f6d6bd}Photios{/color} has sent me to buy a {i}spirit rock{/i} for his daughter. He hopes it will enhance {color=#f6d6bd}Phoibe’s{/color} pneuma.”' if not eudocia_about_spiritrock_problem and quest_spiritrock == 1:
                                $ eudocia_about_spiritrock_problem = 1
                                jump eudociaaskedaboutshop01av02
                            '“I’m trying to learn more about the peninsula.”' if not eudocia_about_peninsula:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about the peninsula.”')
                                $ eudocia_about_peninsula = 1
                                jump eudocia_about_peninsula00
                            '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' if quest_asterion == 1 and not asterion_found and not eudocia_about_asterion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
                                jump eudocia_about_asterion00
                            '“I’m looking for a job.”' if not eudocia_about_job01:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a job.”')
                                $ eudocia_about_job01 = 1
                                jump eudocia_about_job00
                            '“I was hoping you could fill an item of mine with pneuma.”' if not eudocia_about_enchanting_items:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was hoping you could fill an item of mine with pneuma.”')
                                $ eudocia_about_enchanting_items = 1
                                jump eudocia_about_enchanting_items01after
                    'I don’t say anything.' ( condition="at == 'intimidating'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t say anything.')
                        $ at = 0
                        $ at_activate = 0
                        $ description_eudocia02 = "She doesn’t allow anyone in her house while she works. I should ask her to meet me in the early morning, or a few hours before dusk."
                        $ eudocia_image_golem01 = "turnedleft"
                        show golem01 turnedleft_middle at basicfade
                        $ eudocia_image_right = "base"
                        $ quest_explorepeninsula_description15 = "I met {color=#f6d6bd}Eudocia{/color}, a skilled enchantress who lives near the western road. The guild could benefit from her powerful golems."
                        $ renpy.notify("Journal updated: Explore the Peninsula")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
                        menu:
                            'The two of you exchange a few long looks, but she seems not at all bothered by the silence. Finally, she glances toward her golems and speaks with caution. “If ye come here, I better get aught from it. I speak in the tongue of dragons and barter, and I’m not waiting for strangers.”
                            \n\nShe walks past you and cocks her head toward the golem who let you in. It turns around and shuts the gate. “[eudocia_about_closingthegate] If ye ever come here in the middle of the day, ye’ll stand outside, looking at the doors like an ibex.”
                            \n\n[eudocia_toldname] Her voice remains cold. “Why are ye here?”
                            '
                            '“I was asked to deliver the writing quills to the monastery.”' if quest_pensformonastery == 1 and not eudocia_about_pens:
                                $ eudocia_about_pens = 1
                                jump eudociahouseaboutpens01
                            '“{color=#f6d6bd}Photios{/color} has sent me to buy a {i}spirit rock{/i} for his daughter. He hopes it will enhance {color=#f6d6bd}Phoibe’s{/color} pneuma.”' if not eudocia_about_spiritrock_problem and quest_spiritrock == 1:
                                $ eudocia_about_spiritrock_problem = 1
                                jump eudociaaskedaboutshop01av02
                            '“I’m trying to learn more about the peninsula.”' if not eudocia_about_peninsula:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to learn more about the peninsula.”')
                                $ eudocia_about_peninsula = 1
                                jump eudocia_about_peninsula00
                            '“I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' if quest_asterion == 1 and not asterion_found and not eudocia_about_asterion:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
                                jump eudocia_about_asterion00
                            '“I’m looking for a job.”' if not eudocia_about_job01:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a job.”')
                                $ eudocia_about_job01 = 1
                                jump eudocia_about_job00
                            '“I was hoping you could fill an item of mine with pneuma.”' if not eudocia_about_enchanting_items:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I was hoping you could fill an item of mine with pneuma.”')
                                $ eudocia_about_enchanting_items = 1
                                jump eudocia_about_enchanting_items01after

##########################################

label eudociahouseconversationregular01:
    if eudocia_friendship >= eudocia_friendship_tierlevel:
        if not eudocia_inside_firsttime: #first time in house
            $ eudocia_image_eyes = 0
            $ eudocia_image_left = "base"
            $ eudocia_image_right = "gate"
            show areapicture eudociahousemiddlebase behind golem01, golem02, eudocia_image_eyes at basicfade
            if eudocia_image_golem01 == "turnedback":
                show golem01 turnedback_middle at basicfade
            elif eudocia_image_golem01 == "turnedleft":
                show golem01 turnedleft_middle at basicfade
            elif eudocia_image_golem01 == "turnedright":
                show golem01 turnedright_middle at basicfade
            else:
                hide golem01
            if eudocia_image_golem02 == "nogolem":
                show golem02 nogolem_middle at basicfade
            elif eudocia_image_golem02 == "nogolemplusback":
                show golem02 nogolemplusback_middle at basicfade
            else:
                hide golem02
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            menu:
                'You let {color=#f6d6bd}[horsename]{/color} loose, but no soul shows up to greet you. The door of the house is ajar.
                '
                'I go inside.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go inside.')
                    $ eudocia_inside_firsttime = 1
                    $ pc_area = "eudociahouseinside"
                    jump eudociahouseinsidefirsttime01
        else: #regular in house
            $ pc_area = "eudociahouseinside"
            $ can_leave = 0
            $ can_rest = 1
            $ can_items = 1
            hide golem01
            hide golem02
            hide eudocia_image_eyes
            show areapicture eudociahouseinside01 at basicfade
            $ questionpreset = "eudocia1"
            if eudocia_about_flower_refusal and eudocia_about_flower_refusal < (day-1) and not eudocia_about_flower_refusal_grateful:
                $ eudocia_about_flower_refusal_grateful = 1
                $ eudocia_friendship += 3
                menu:
                    '{color=#f6d6bd}Eudocia’s{/color} welcomes you with a yawn and a blink of her sleepy eyes. “Ye played me dirty with that damn flower,” she growls, but then puts on a gentle smile. “I’ve never slept so much as in the last couple of days... But maybe that’s for the better.”
                    '
                    '(eudocia1 set)':
                        pass
            else:
                menu:
                    '{color=#f6d6bd}Eudocia’s{/color} [eudocia_inside_fluff] and stares at [eudocia_heldobject].
                    '
                    '(eudocia1 set)':
                        pass
    else: # regular, but outside
        $ eudocia_image_eyes = 0
        $ eudocia_image_left = "base"
        $ eudocia_image_right = "gate"
        $ eudocia_image_golem01 = renpy.random.choice(['turnedback', 'turnedleft', 'turnedright'])
        show areapicture eudociahousemiddlebase behind golem01, golem02, eudocia_image_eyes at basicfade
        if eudocia_image_golem01 == "turnedback":
            show golem01 turnedback_middle at basicfade
        elif eudocia_image_golem01 == "turnedleft":
            show golem01 turnedleft_middle at basicfade
        elif eudocia_image_golem01 == "turnedright":
            show golem01 turnedright_middle at basicfade
        else:
            hide golem01
        if eudocia_image_golem02 == "nogolem":
            show golem02 nogolem_middle at basicfade
        elif eudocia_image_golem02 == "nogolemplusback":
            show golem02 nogolemplusback_middle at basicfade
        else:
            hide golem02
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        menu: # regular, but outside
            '{color=#f6d6bd}Eudocia{/color} closes the door behind her. “Ye’re back.”
            '
            '(eudocia1 set)':
                pass

label eudociahouseinsidefirsttime01:
    $ pc_area = "eudociahouseinside"
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    hide golem01
    hide golem02
    hide eudocia_image_eyes
    show areapicture eudociahouseinside02 at basicfade
    menu:
        'The chamber was meant to have only one dweller, but even in {color=#f6d6bd}Hovlavan{/color} it would be seen as outrageously tiny. The air carries the scent of sweat and dirty clothes, but more importantly - smoke. A couple of fish and other pieces of meat are hanging above the hearth, even though there’s no fire left.
        \n\n{color=#f6d6bd}Eudocia{/color} is sitting on the floor, with her back leaning against the wooden step, legs outstretched, feet resting on a wooden pillar. She’s staring intensely at [eudocia_heldobject].
        '
        'I greet her first.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I greet her first.')
            $ custom1 = "She nods, but doesn’t look at you."
            jump eudociahouseinsidefirsttime02
        'I wait for her to say something.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for her to say something.')
            $ custom1 = "She ignores you for a good minute, then glances toward you with a weak smile."
            label eudociahouseinsidefirsttime02:
                if not eudocia_sleep_available:
                    $ eudocia_sleep_available = 1
                    $ renpy.notify("New shelter unlocked.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New shelter unlocked.{/i}')
                menu:
                    '[custom1] “The house is a mess, if it bothers you, complain to the broth I made.” A long pause. “Take a seat, if ye want. It’s getting chilly outside, and ye don’t act like a bandit, so far. If ye need a place to crash, stay in my shed. Just don’t carry any candles inside, I store hay there.”
                    '
                    'I sit down as far away from her as I can, on the stool.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit down as far away from her as I can, on the stool.')
                        $ custom1 = "She puts on a gentle smile."
                        jump eudociahouseinsidefirsttime03
                    'I rest next to her, on the floor.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I rest next to her, on the floor.')
                        $ custom1 = "She nudges you with an elbow. “Just don’t get weird. So, what d’ye want?”"
                        jump eudociahouseinsidefirsttime03
                    'I take place on the wooden step, near the fireplace.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take place on the wooden step, near the fireplace.')
                        $ custom1 = "She spares you only a glance. “So, what brings ye here?”"
                        jump eudociahouseinsidefirsttime03
                    'I sit down on her bed.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit down on her bed.')
                        $ custom1 = "“Just don’t get {i}too{/i} comfortable,” she chuckles without even looking at you."
                        jump eudociahouseinsidefirsttime03
                    'I stay in the entrance.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay in the entrance.')
                        $ custom1 = "“At least close the door. Let’s not invite the autumn inside.”"
                        label eudociahouseinsidefirsttime03:
                            $ can_leave = 0
                            $ can_rest = 1
                            $ can_items = 1
                            $ questionpreset = "eudocia1"
                            menu:
                                '[custom1]
                                '
                                '(eudocia1 set)':
                                    pass

label eudociahouseaftersleep:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ pc_area = "eudociahouse"
    $ eudocia_image_right = "base"
    $ eudocia_image_left = "base"
    $ eudocia_image_golem01 = renpy.random.choice(['turnedback', 'turnedback', 'turnedleft', 'turnedleft', 'turnedright', 'turnedright', 'none'])
    if eudocia_image_golem01 == "none":
        $ eudocia_image_golem02 = 'nogolemplusback'
    else:
        $ eudocia_image_golem02 = renpy.random.choice([0, 0, 0, 0, 'nogolem'])
    show areapicture eudociahousemiddlebase behind golem01, golem02, eudocia_image_eyes at basicfade
    if eudocia_image_golem01 == "turnedback":
        show golem01 turnedback_middle at basicfade
    elif eudocia_image_golem01 == "turnedleft":
        show golem01 turnedleft_middle at basicfade
    elif eudocia_image_golem01 == "turnedright":
        show golem01 turnedright_middle at basicfade
    else:
        hide golem01
    if eudocia_image_golem02 == "nogolem":
        show golem02 nogolem_middle at basicfade
    elif eudocia_image_golem02 == "nogolemplusback":
        show golem02 nogolemplusback_middle at basicfade
    else:
        hide golem02
    $ eudocia_inside_fluff = renpy.random.choice(['sitting on the stool by the hearth,', 'sitting on the stool, near the cupboard,', 'sitting on the floor, leaning against the bed,', ' leaning against the fur that hangs from the wall,', 'sitting on the floor, surrounded by empty, wooden bowls'])
    $ eudocia_image_eyes = 0
    $ eudocia_fluff = renpy.random.choice(['The meadow is so quiet it makes you slow down.', 'White-and-gray birds are sitting on the walls without making a sound, giving you tense looks.', 'You hear heavy steps and the sounds of large objects being dragged around.', 'Only one fly is feasting on the rotting carcass of a snake that’s on the side of the road.', 'A loud roar comes from the north, making your palfrey stop. After a few heartbeats it snorts and moves along.', 'A new spider web is strung between the wall and the gargoyle’s head.', 'There are a few loud ducks on the shore, though they flee after you reach the gargoyle.'])
    if quarters >= 40 and quarters < (world_daylength-16):
        $ eudocia_heldobject = renpy.random.choice(['a large, wooden shield in her hands', 'an inkwell placed right in front of her', 'a large rock placed on the floor', 'a brown, thick cape placed on her knees', 'the steel head of a masterful spear in her hands', 'a brand new fishing net lying on the floor'])
    else:
        $ eudocia_heldobject = renpy.random.choice(['a long smoking pipe in her fingers', 'a hot liquid in a wooden bowl in her hands', 'a cold piece of roasted meat on a wooden plate', 'a sharp dagger that she spins in place', 'smoking incense, though she extinguishes it once you show up'])
    if eudocia_friendship >= 10:
        $ renpy.music.play("audio/track_13eudociahouse02.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    else:
        $ renpy.music.play("audio/track_13eudociahouse01.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if day == 6 or day == 12 or day == 18 or day == 24 or day == 30 or day == 36 or day == 42:
        $ renpy.notify("The days are getting shorter.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}The days are getting shorter.{/i}')
    if eudocia_inside_firsttime:
        menu:
            'You let {color=#f6d6bd}[horsename]{/color} drink outside, then close both of you in the shed. There isn’t much fodder around.
            \n\nThe dragons from the mountains wake you up with their roars, but the heavy steps of the sentinels ease your soul. The yard is carefully patrolled.
            \n\nSome of the hay gets under your clothes, but at least your back doesn’t ache in the morning. You let your palfrey outside.
            '
            'I approach {color=#f6d6bd}Eudocia{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Eudocia{/color}.')
                jump eudociahouseconversationregular01
            'I take a closer look at the golem.' if (not quest_studyingthegolems_description03 and pc_class != "scholar") or (not quest_studyingthegolems_description03b and pc_class == "scholar"):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the golem.')
                jump eudociahousecloserlookatthegolem01
    else:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'You let {color=#f6d6bd}[horsename]{/color} drink outside, then close both of you in the shed. There isn’t much fodder around.
            \n\nThe dragons from the mountains wake you up with their roars, but the heavy steps of the sentinels ease your soul. The yard is carefully patrolled.
            \n\nSome of the hay gets under your clothes, but at least your back doesn’t ache in the morning. You let your palfrey outside.
            \n\nNo soul shows up to greet you. The door of the house is ajar.
            '
            'I go inside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go inside.')
                $ eudocia_inside_firsttime = 1
                $ pc_area = "eudociahouseinside"
                $ can_leave = 0
                $ can_rest = 0
                $ can_items = 0
                hide golem01
                hide golem02
                hide eudocia_image_eyes
                show areapicture eudociahouseinside02 at basicfade
                menu:
                    'The chamber was meant to have only one dweller, but even in {color=#f6d6bd}Hovlavan{/color} it would be seen as outrageously tiny. The air carries the scent of sweat and dirty clothes, but more importantly - smoke. A couple of fish and other pieces of meat are hanging above the hearth, even though there’s no fire left.
                    \n\n{color=#f6d6bd}Eudocia{/color} is sitting on the floor, with her back leaning against the wooden step, legs outstretched, feet resting on a wooden pillar. She’s staring intensely at [eudocia_heldobject].
                    '
                    'I greet her first.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I greet her first.')
                        $ custom1 = "She nods, but doesn’t look at you."
                        jump eudociahouseinsidefirsttime02alt
                    'I wait for her to say something.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for her to say something.')
                        $ custom1 = "She ignores you for a good minute, then glances toward you with a weak smile."
                        label eudociahouseinsidefirsttime02alt:
                            menu:
                                '[custom1] “The house is a mess, if it bothers you, complain to the broth I made.” A long pause. “Take a seat, if ye want.”
                                '
                                'I sit down as far away from her as I can, on the stool.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit down as far away from her as I can, on the stool.')
                                    $ custom1 = "She puts on a gentle smile."
                                    jump eudociahouseinsidefirsttime03alt
                                'I rest next to her, on the floor.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I rest next to her, on the floor.')
                                    $ custom1 = "She nudges you with an elbow. “Just don’t get weird. So, what d’ye want?”"
                                    jump eudociahouseinsidefirsttime03alt
                                'I take place on the wooden step, near the fireplace.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take place on the wooden step, near the fireplace.')
                                    $ custom1 = "She spares you only a glance. “So, what brings ye here?”"
                                    jump eudociahouseinsidefirsttime03alt
                                'I sit down on her bed.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I sit down on her bed.')
                                    $ custom1 = "“Just don’t get {i}too{/i} comfortable,” she chuckles without even looking at you."
                                    jump eudociahouseinsidefirsttime03alt
                                'I stay in the entrance.':
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stay in the entrance.')
                                    $ custom1 = "“At least close the door. Let’s not invite the autumn inside.”"
                                    label eudociahouseinsidefirsttime03alt:
                                        $ can_leave = 0
                                        $ can_rest = 1
                                        $ can_items = 1
                                        $ questionpreset = "eudocia1"
                                        menu:
                                            '[custom1]
                                            '
                                            '(eudocia1 set)':
                                                pass

label eudociahouseafterquestionALL:
    label eudociahouseafterquestion:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        menu:
            '“Can’t stop ye now.”
            '
            '(eudocia1 set)':
                pass

    label eudociahouseafterquestionb:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        menu:
            'She stares in the distance.
            '
            '(eudocia1 set)':
                pass

    label eudociahouseafterquestionc:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        menu:
            '“I’m listening.”
            '
            '(eudocia1 set)':
                pass

    label eudociahouseafterquestioncgolem:
        if quest_studyingthegolems_description03:
            $ quest_studyingthegolems_description01 = "I asked {color=#f6d6bd}Eudocia{/color} a few things about the golems."
            $ quest_studyingthegolems_description03 = "I had a chance to take a closer look at one of the golems."
        else:
            $ quest_studyingthegolems_description01 = "I asked Eudocia a few things about the golems, but I could still take a closer look at them on my own."
        if quest_studyingthegolems == 1:
            $ renpy.notify("Journal updated: Studying the Golems")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Studying the Golems{/i}')
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        $ quarters += 1
        menu:
            'Her lips form a smile. “If anyone asks ye about them, don’t spare good words. They’re things of wonder, my greatest enchantment.”
            '
            '(eudocia1 set)':
                pass

    label eudociahouseafterquestiond:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        menu:
            '“Go ahead.”
            '
            '(eudocia1 set)':
                pass

    label eudociahouseafterquestione:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        menu:
            '“Need aught else?”
            '
            '(eudocia1 set)':
                pass

    label eudociahouseafterquestionf:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        menu:
            'She avoids your eyes. “Great. Just don’t die on the road, this bronze cost me many favors. And be sure to leave one of the rods in {color=#f6d6bd}White Marshes{/color}.”
            '
            '(eudocia1 set)':
                pass

    label eudociahouseafterquestiong:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        menu:
            '“Good, good.”
            '
            '(eudocia1 set)':
                pass

    label eudociahouseafterquestiong2:
        if pc_area == "eudociahouse":
            $ can_leave = 1
        else:
            $ can_leave = 0
        $ can_rest = 1
        $ can_items = 1
        $ questionpreset = "eudocia1"
        menu:
            'She lets out a satisfied grunt.
            '
            '(eudocia1 set)':
                pass

label eudociahouseonthesquare01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ pc_area = "eudociahouse"
    $ eudocia_image_right = "base"
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
    if eudocia_image_golem02 == "nogolem":
        show golem02 nogolem_middle at basicfade
    elif eudocia_image_golem02 == "nogolemplusback":
        show golem02 nogolemplusback_middle at basicfade
    else:
        hide golem02
    $ custom1 = renpy.random.choice(['is napping', 'is grazing on the grass', 'welcomes you with a snort', 'is pawing the ground', 'gives the golem curious glances'])
    menu:
        'You take a couple of deep breaths. {color=#f6d6bd}[horsename]{/color} [custom1].
        '
        'I approach {color=#f6d6bd}Eudocia{/color}.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach {color=#f6d6bd}Eudocia{/color}.')
            jump eudociahouseconversationregular01
        'I take a closer look at the golem.' if (not quest_studyingthegolems_description03 and pc_class != "scholar") or (not quest_studyingthegolems_description03b and pc_class == "scholar"):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a closer look at the golem.')
            jump eudociahousecloserlookatthegolem01
