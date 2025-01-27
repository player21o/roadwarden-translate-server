###################### West Gate - Quintus
# Quintus - bardzo zestresowany, zdeterminowany, by utrzymać służbę, nie wie za wiele, ale poszukuje rozrywki, śmieje się nerwowo, niewyspany, okaleczony - świeże rany na twarzy, bandaż na głowie, hoarse voice, kuleje (he limps - bo temporary) scratches the bandage on his cheek.

default westgate_firsttime = 0
default westgate_open = 0
default quintus_alive = 1
default quintus_attitude = 0
default quintus_left_gate = 0
default quintus_left_gate_about = 0
default quintus_left_gate_points = 0
default quintus_left_gate_points_threshold = 25
default quintus_left_gate_points_argument_nomoreundead = 0
default quintus_left_gate_points_argument_glauciadefeated = 0
default quintus_left_gate_points_argument_shortcut = 0
default quintus_left_gate_points_argument_food = 0
default quintus_left_gate_points_argument_iason = 0
default quintus_left_gate_points_argument_iason_about = 0
default quintus_left_gate_points_argument_coins = 0
default quintus_left_gate_points_argument_coins_threshold = 0
default quintus_left_gate_points_argument_oldpagoshelp = 0

default quintus_about_highisland_recruitment = 0
default quintus_about_highisland_recruitment_done = 0
default quintus_highisland_joined = 0

default westgate_fluff = ""
default westgate_fluff2 = ""
default westgate_fluff3 = ""

default quintus_friendship = 0
default quintus_about_gate = 0
default quintus_about_bronzerod = 0 # 1 - spytany, ale nie dostał jedzenia. 2 - dostał jedzenie.

default quintus_food_delivered_amount = 0
default quintus_food_gate_fed = 0
default quintus_food_gate_amount = 0

default quintus_food_bronzerod_amount = 0

default quintus_about_plague = 0
default quintus_about_plague_cured = 0
default quintus_about_staying = 0
default quintus_about_leaving = 0
default quintus_about_survival = 0
default quintus_about_gate_fluff = 0
default quintus_about_shortcut = 0
default quintus_about_shortcut2 = 0
default quintus_about_oldpagos = 0
default quintus_about_asterion = 0
default quintus_about_bandits = 0
default quintus_about_bandits_gray = 0
default quintus_about_dalit = 0
default quintus_about_ibex = 0
default quintus_about_highisland = 0
default quintus_about_missinghunters = 0
default quintus_about_vaschel = 0
default quintus_about_fatsmoke = 0
default quintus_about_gambesonrepairset = 0
default quintus_friendswithdalit = 0

default quintus_food_gate_reason_points = 0
default quintus_food_gate_reason_points_required = 6
default quintus_food_gate_reason01 = 0
default quintus_food_gate_reason02 = 0
default quintus_food_gate_reason03 = 0
default quintus_food_gate_reason04 = 0
default quintus_food_gate_reason05 = 0
default quintus_food_gate_reason06 = 0
default quintus_food_gate_reason07 = 0
default quintus_food_gate_reason08 = 0

label westgate01:
    nvl clear
    $ pc_area = "westgate"
    $ westgate_fluff = renpy.random.choice(['The long shadow cast by the crags protects you from the sun.', 'While the larger birds are singing from the trees, the sparrows are searching for berries and insects among the shrubs.', 'You hear breaking wood and roaring creatures in the east.', 'A small, gray lizard is basking on a rock, but runs away at your sight.', 'The clopping of your palfrey carries fills the silent corridor of rocks.', 'There’s fresh blood on the road, but the trail leads into the deep bushes.'])
    if quintus_left_gate and quintus_left_gate < day:
        if eudocia_bronzerod_rodin_westgate:
            show areapicture westgatewest01bronzerod at basicfade behind westgatenobar
        else:
            show areapicture westgatewest01 at basicfade behind westgatenobar
        show westgatenobar at basicfade
        if shortcut_inprogress:
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ shortcut_inprogress = 0
            $ shortcut_traveled += 1
        else:
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
        stop music fadeout 4.0
        play nature "audio/ambient/westgate01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ renpy.force_autosave(take_screenshot=False, block=True)
        jump westgate_noquintus01
    else:
        $ westgate_fluff2 = renpy.random.choice(['is sitting on a stool, washing his hands in the bucket filled with dirty water', 'is standing by the bushes, observing a snake pierced with his spear. Before he turns toward you, he licks his lips', 'is sitting on the wall, cleaning his crossbow', 'is leaning on the wall’s parapet, looking around', 'looks at you from the top of the precipice that’s near the tower. He crosses the parapet and leans forward', 'is sitting on the ground, leaning against the wall with closed eyes, which he opens after you get closer'])
        $ westgate_fluff3 = renpy.random.choice(['opens the gate for you from the other side', 'is nowhere to be seen. You wait for a minute or two, and he finally opens the gate from the other side', 'is sitting on the wall, cleaning his crossbow. He lowers the rope quickly on the other side of the wall, climbs down, and opens the gate', 'is leaning on the wall’s parapet, looking around. He nods to you, climbs down, and opens the gate from the other side of the wall', 'looks at you from the top of the precipice that’s near the tower. He crosses the parapet, gestures for you to wait, climbs down on the other side of the wall, and opens the gate'])
        if shortcut_inprogress and not westgate_firsttime:
            if eudocia_bronzerod_rodin_westgate:
                show areapicture westgateeast01bronzerod at basicfade
            else:
                show areapicture westgateeast01 at basicfade
        elif shortcut_inprogress:
            if eudocia_bronzerod_rodin_westgate:
                show areapicture westgatewest01bronzerod at basicfade
            else:
                show areapicture westgatewest01 at basicfade
        elif not westgate_firsttime:
            if eudocia_bronzerod_rodin_westgate:
                show areapicture westgatewest01bronzerod at basicfade
            else:
                show areapicture westgatewest01 at basicfade
        else:
            if eudocia_bronzerod_rodin_westgate:
                show areapicture westgatewest01bronzerod at basicfade
            else:
                show areapicture westgatewest01 at basicfade
        if not westgate_firsttime:
            stop music fadeout 4.0
            play nature "audio/ambient/westgate01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        else:
            stop nature fadeout 4.0
            if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_17shortcut.ogg":
                play music "<loop 15.0>audio/track_17shortcut.ogg" fadeout 1.0 fadein 1.0
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        $ renpy.force_autosave(take_screenshot=False, block=True)
        if shortcut_inprogress and not westgate_firsttime:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            $ shortcut_inprogress = 0
            $ world_known_npcs += 1
            $ world_known_areas += 1
            $ westgate_firsttime = 1
            $ shortcut_pcknowsabout = 1
            $ world_known_areas += 1
            $ westerncrossroads_unlocked = 1
            $ shortcut_traveled += 1
            jump westgatefirsttimealt01
        elif shortcut_inprogress:
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ shortcut_inprogress = 0
            $ shortcut_traveled += 1
            jump westgatetravelingshortcut01
        elif not westgate_firsttime:
            $ can_leave = 0
            $ can_rest = 0
            $ can_items = 0
            $ world_known_npcs += 1
            $ world_known_areas += 1
            $ westgate_firsttime = 1
            $ world_known_areas += 1
            $ westerncrossroads_unlocked = 1
            jump westgatefirsttime01
        else:
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            jump westgateregular01

label workinglabelwestgatefirsttime01: # gdy normalnie przybył do lokacji, po raz pierwszy
    label westgatefirsttime01: # gdy normalnie przybył do lokacji, po raz pierwszy
        $ at_activate = 1
        $ at = 0
        menu:
            'The corridor of leaves and gray rocks leads you to a gate, large enough for a wagon, held together by a wooden bar. The planks and rocks are covered with claw marks left by various monsters, but they weren’t able to damage the wall as much as the passage of time and the piercing rains.
            \n\n{color=#f6d6bd}A large man{/color}, covered in shadows, is observing you from the roofed tower. His voice is hoarse, distrustful. “Ye lost? I don’t know ya mug.”
            '
            ' (disabled)' ( condition="at == 0" ):
                pass
            'I introduce myself. “Good time to get to know each other!”' ( condition="at == 'friendly'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (friendly) I introduce myself. “Good time to get to know each other!”')
                $ at_activate = 0
                $ at = 0
                jump westgatefirsttime02friendly
            '“Better remember this {i}mug{/i}, friend. It’s going to stay around for a while.” I introduce myself.' ( condition="at == 'playful'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (playful) “Better remember this {i}mug{/i}, friend. It’s going to stay around for a while.”')
                $ at_activate = 0
                $ at = 0
                jump westgatefirsttime02playful
            '“I’m [pcname], the new roadwarden. And you’re the gatekeeper, I assume?”' ( condition="at == 'distanced'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (distanced) “I’m %s, the new roadwarden. And you’re the gatekeeper, I assume?”' %pcname)
                $ at_activate = 0
                $ at = 0
                jump westgatefirsttime02distanced
            '“I’m a roadwarden, let me ride through. I’ll only ask once.”' ( condition="at == 'intimidating'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (intimidating) “I’m a roadwarden, let me ride through. I’ll only ask once.”')
                $ at_activate = 0
                $ at = 0
                jump westgatefirsttime02intimidating
            'I explain who I am. “I’m not looking for trouble, stranger. Can you open the gate for me?”' ( condition="at == 'vulnerable'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (vulnerable) I explain who I am. “I’m not looking for trouble, stranger. Can you open the gate for me?”')
                $ at_activate = 0
                $ at = 0
                jump westgatefirsttime02vulnerable

    label westgatefirsttime02friendly: #I introduce myself. “Good time to get to know each other!”
        $ quintus_friendship += 1
        menu:
            '“Yeah, I’ve got naught but time,” he chuckles weakly, leaning on the parapet. “I heard no human voice in days. I’m armed, ye know,” he sticks out a loaded crossbow, “but I’m no enemy. Just on duty, guarding. Ye can hang around, but I’ve got no ale, or water.”
            \n\nHe leaves the tower. He’s wearing a black gambeson, so ragged it can’t be fastened anymore. It tells a story of claws, thorns, and improvised repairs. The hole in the man’s hemp pants reveals a scraped knee.
            \n\nIt’s hard to tell his age through his exhausted, sleepy eyes, a short, unkempt beard, and a bandage horizontally covering his ears and the spot that used to be his nose. There’s clotted blood in his brown hair, and mud on his clothes and brown neck. Despite all this, he’s of a huge shell, with wide shoulders and thick legs.
            \n\nHe crouches, places his crossbow on the wall, and gives you a curious look. “Ye new to {i}wardening{/i}?”
            '
            '“Pretty new.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pretty new.”')
                menu:
                    '“Ye chose a shit place, then. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe built this place to keep them away from us. And us from them.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttime03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttime03pcwasnotinoldpagos
            '“New here, but I know what I’m doing.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “New here, but I know what I’m doing.”')
                menu:
                    '“No past would prepare ye for this shit place. Nights are all ape piss and blood. Just before sunrise, a bird tried to pluck my eye. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe built this place to keep them away from us. And us from them.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttime03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttime03pcwasnotinoldpagos

    label westgatefirsttime02playful: #“Better remember this {i}mug{/i}, friend. It’s going to stay around for a while.” I introduce myself.
        $ quintus_friendship += 0
        menu:
            '“I will, I will. I’m good with faces. These stuff ye have, that ass,” he points at your horse, “ye might as well scream {i}I’m not from here{/i}.” A pause. “I’m armed, ye know,” he lifts a loaded crossbow and sticks it out of the shadows, “but I’m no enemy. Just on duty, guarding. We can talk, if ye want. I’ve time.”
            \n\nHe leaves the tower. He’s wearing a black gambeson, so ragged it can’t be fastened anymore. It tells a story of claws, thorns, and improvised repairs. The hole in the man’s hemp pants reveals a scraped knee.
            \n\nIt’s hard to tell his age through his exhausted, sleepy eyes, a short, unkempt beard, and a bandage horizontally covering his ears and the spot that used to be his nose. There’s clotted blood in his brown hair, and mud on his clothes and brown neck. Despite all this, he’s of a huge shell, with wide shoulders and thick legs.
            \n\nHe stands upright, observing you with curiosity. “So, a warden? Ye new to the job?”
            '
            '“Pretty new.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pretty new.”')
                menu:
                    '“Ye chose a shit place, then. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe built this place to keep them away from us. And us from them.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttime03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttime03pcwasnotinoldpagos
            '“New here, but I know what I’m doing.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “New here, but I know what I’m doing.”')
                menu:
                    '“No past would prepare ye for this shit place. Nights are all ape piss and blood. Just before sunrise, a bird tried to pluck my eye. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe built this place to keep them away from us. And us from them.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttime03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttime03pcwasnotinoldpagos

    label westgatefirsttime02distanced: #“I’m [pcname], the new roadwarden. And you’re the gatekeeper, I assume?”
        $ quintus_friendship += 0
        menu:
            '“Well, yeah. Just on duty, and armed, so ye know,” he lifts a loaded crossbow and sticks it out of the shadows, “but I’m no enemy of yas.”
            \n\nHe leaves the tower. He’s wearing a black gambeson, so ragged it can’t be fastened anymore. It tells a story of claws, thorns, and improvised repairs. The hole in the man’s hemp pants reveals a scraped knee.
            \n\nIt’s hard to tell his age through his exhausted, sleepy eyes, a short, unkempt beard, and a bandage horizontally covering his ears and the spot that used to be his nose. There’s clotted blood in his brown hair, and mud on his clothes and brown neck. Despite all this, he’s of a huge shell, with wide shoulders and thick legs.
            \n\nHe straightens up. “So, a warden? Ye new to the job?”
            '
            '“Pretty new.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pretty new.”')
                menu:
                    '“Ye chose a shit place, then. This gate, here?” He kicks a brick with his heel. “It’s older than me. All there?” He points behind him with his weapon. “Wilds and beasts. My tribe built this place to keep them away from us. And us from them.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttime03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttime03pcwasnotinoldpagos
            '“New here, but I know what I’m doing.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “New here, but I know what I’m doing.”')
                menu:
                    '“No past would prepare ye for this shit place. Nights are all ape piss and blood. Just before sunrise, a bird tried to pluck my eye. This gate, here?” He kicks a brick with his heel. “It’s older than me. All there?” He points behind him with his weapon. “Wilds and beasts. My tribe built this place to keep them away from us. And us from them.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttime03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttime03pcwasnotinoldpagos

    label westgatefirsttime02vulnerable: #I explain who I am. “I’m not looking for trouble, stranger. Can you open the gate for me?”
        $ quintus_friendship -= 1
        menu:
            '“Ye, warden? Ye better turn around, it’s a wild place, I’m not running after your screams if you enter the woods.” A short pause. “I’m armed, ye know,” he lifts a loaded crossbow and sticks it out of the shadows. “I’m just on duty, but ye know. Don’t play any tricks.”
            \n\nHe leaves the tower. He’s wearing a black gambeson, so ragged it can’t be fastened anymore. It tells a story of claws, thorns, and improvised repairs. The hole in the man’s hemp pants reveals a scraped knee.
            \n\nIt’s hard to tell his age through his exhausted, sleepy eyes, a short, unkempt beard, and a bandage horizontally covering his ears and the spot that used to be his nose. There’s clotted blood in his brown hair, and mud on his clothes and brown neck. Despite all this, he’s of a huge shell, with wide shoulders and thick legs.
            \n\nHe straightens up, towering over you. “Ye new to the job?”
            '
            '“Pretty new.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pretty new.”')
                menu:
                    '“Ye chose a shit place, then. This gate, here?” He kicks a brick with his heel. “It’s older than me. All there?” He points behind him with his weapon. “Wilds and beasts. My tribe built this place to keep them away from us. And us from them.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttime03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttime03pcwasnotinoldpagos
            '“New here, but I know what I’m doing.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “New here, but I know what I’m doing.”')
                menu:
                    '“No past would prepare ye for this shit place. Nights are all ape piss and blood. Just before sunrise, a bird tried to pluck my eye. This gate, here?” He kicks a brick with his heel. “It’s older than me. All there?” He points behind him with his weapon. “Wilds and beasts. My tribe built this place to keep them away from us. And us from them.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttime03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttime03pcwasnotinoldpagos

    label westgatefirsttime02intimidating: #“I’m a roadwarden, let me ride through. I’ll only ask once.”
        $ quintus_friendship -= 2
        $ westgate_open = 1
        $ quintus_attitude = "intimidating"
        menu:
            'His voice is cold. “Give me a minute. See?” He points at the long, twisted rope which hangs from an iron hook. “I need to climb down to the other side, there’s another bar there. Ye’ll take down yours. Ye need at least three hours to get through the woods.”
            \n\nHe leaves the tower with a loaded crossbow in his hands. He’s wearing a black gambeson, so ragged it can’t be fastened anymore. It tells a story of claws, thorns, and improvised repairs. The hole in the man’s hemp pants reveals a scraped knee.
            \n\nIt’s hard to tell his age through his exhausted, sleepy eyes, a short, unkempt beard, and a bandage horizontally covering his ears and the spot that used to be his nose. There’s clotted blood in his brown hair, and mud on his clothes and brown neck. Despite all this, he’s of a huge shell, with wide shoulders and thick legs.
            \n\nHe straightens up, pointing his crossbow in your direction. “Let me ask ye aught.”
            '
            '“Go on.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Go on.”')
                menu:
                    '“My duty is to guard this place. This gate, here?” He kicks a brick with his heel. “It’s older than me. All there?” He points behind him with his weapon. “Wilds and beasts. My tribe built this place to keep them away from us. And us from them.”
                    \n\nHe scratches the bandage on his cheek. “I’m from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttime03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttime03pcwasnotinoldpagos

    label westgatefirsttime03pcwasinoldpagos:
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_17shortcut.ogg":
            play music "<loop 15.0>audio/track_17shortcut.ogg" fadeout 1.0 fadein 1.0
        menu:
            '“So ye know. We used to send one soul here every morning, and escort them back before nightfall. But some days ago, no one came for me. I spent a night here, sneaking wolf shits almost got me.” He picks up an almost empty waterskin from behind a parapet and takes a sip.
            \n\n“I went home by myself, only to learn about the sick. I’ve been here ever since.”
            '
            '“What do you know about the plague?”' if not quintus_about_plague:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                jump westgateaboutplague01
            '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                jump westgateaboutremainingonthepost01
            '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                jump westgateaboutmovingtoadifferentvillage01
            '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                jump westgateaboutsurvival01
            '“About this gate...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About this gate...”')
                jump westgateaboutopeningthegate01

    label westgatefirsttime03pcwasnotinoldpagos:
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_17shortcut.ogg":
            play music "<loop 15.0>audio/track_17shortcut.ogg" fadeout 1.0 fadein 1.0
        menu:
            '“So ye don’t know. It’s west from here, behind the crossroads, but it’s touched by sickness. We used to send one soul here every morning, and escort them back before nightfall. But some days ago, no one came for me. I spent a night here, sneaking wolf shits almost got me.” He picks up an almost empty waterskin from behind a parapet and takes a sip.
            \n\n“I went home by myself, only to learn about the sick. I’ve been here ever since.”
            '
            '“What do you know about the plague?”' if not quintus_about_plague:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                jump westgateaboutplague01
            '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                jump westgateaboutremainingonthepost01
            '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                jump westgateaboutmovingtoadifferentvillage01
            '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                jump westgateaboutsurvival01
            '“About this gate...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About this gate...”')
                jump westgateaboutopeningthegate01

    label westgateaboutplague01: #“What do you know about the plague?”
        $ quintus_about_plague = 1
        menu:
            '“Not much. It kills, that’s all there is to know. My tribe’s smart, locking the gate. The Wright gave them strength.”
            '
            '“What do you know about the plague?”' if not quintus_about_plague:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                jump westgateaboutplague01
            '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                jump westgateaboutremainingonthepost01
            '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                jump westgateaboutmovingtoadifferentvillage01
            '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                jump westgateaboutsurvival01
            '“About this gate...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About this gate...”')
                jump westgateaboutopeningthegate01

    label westgateaboutremainingonthepost01: #“Shouldn’t you look for a real shelter?”
        $ quintus_about_staying = 1
        menu:
            'He trembles, his eyes widen. “Someone {i}has got to{/i} stay at the gate. The villages in the east don’t know about the illness, they may try crossing the woods, hit the closed gate while fleeing some wolves and stuff.” He rubs his dirty neck. “And I also can’t leave the gate open, it’s like a dam for monsters. If all I can do is choose the way I die, this is it. With my duty fulfilled.”
            '
            '“What do you know about the plague?”' if not quintus_about_plague:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                jump westgateaboutplague01
            '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                jump westgateaboutremainingonthepost01
            '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                jump westgateaboutmovingtoadifferentvillage01
            '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                jump westgateaboutsurvival01
            '“About this gate...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About this gate...”')
                jump westgateaboutopeningthegate01

    label westgateaboutmovingtoadifferentvillage01: #“You could at least spend the nighttime in one of the villages.”
        $ quintus_about_leaving = 1
        menu:
            'He adjusts his jacket by shaking his shoulders, making the buckles jingle. “I’m not a beggar, and the villages in the North won’t help me for more than a day or two. I’ve got no dragon bones, just this little ibex.” He pats his crossbow. “{color=#f6d6bd}Old Págos{/color} is by itself, we don’t look for {i}kind folks{/i}.”
            \n\nHe thinks for a moment. “I’ll just wait. I’ll get back home once the plague’s done. Or before winter.” You look at his disfigured face.
            '
            'He’s either mad or dumb.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s either mad or dumb.')
                jump westgateaboutmovingtoadifferentvillage02
            'He may be a bit too proud, but knows more about the locals than I do.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He may be a bit too proud, but knows more about the locals than I do.')
                label westgateaboutmovingtoadifferentvillage02:
                    menu:
                        'He glances at {color=#f6d6bd}[horsename]{/color}. “Ye understand, I’m sure. Wardens are souls of duty.”
                        '
                        '“What do you know about the plague?”' if not quintus_about_plague:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                            jump westgateaboutplague01
                        '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                            jump westgateaboutremainingonthepost01
                        '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                            jump westgateaboutmovingtoadifferentvillage01
                        '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                            jump westgateaboutsurvival01
                        '“About this gate...”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About this gate...”')
                            jump westgateaboutopeningthegate01

    label westgateaboutsurvival01:
        $ quintus_about_survival = 1
        menu:
            '“Well, ye can call it {i}surviving{/i}. I call it {i}potions{/i}.” His chuckle makes him wince in pain. He puts a hand on his stomach and leans away. “Beasts took me for easy prey, but the good monks from the mountains equipped our guards well. They’re helping our ill, but used to brew all sorts of stuff.” His hand moves to an earthenware bottle by his belt.
            '
            '“What do you know about the plague?”' if not quintus_about_plague:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                jump westgateaboutplague01
            '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                jump westgateaboutremainingonthepost01
            '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                jump westgateaboutmovingtoadifferentvillage01
            '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                jump westgateaboutsurvival01
            '“About this gate...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About this gate...”')
                jump westgateaboutopeningthegate01

    label westgateaboutopeningthegate01:
        $ quintus_about_gate = 1
        if westgate_open:
            if quarters <= (world_daylength-12):
                menu:
                    '“I can open it for ye... If yer sure about it. Ye need at least three hours to get to the other side of the woods.”
                    '
                    '“Do it.” I enter the forest.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do it.” I enter the forest.')
                        jump westgateenteringtheshortcut01
                    '“Maybe another time.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe another time.”')
                        jump westgateafterinteraction01
            else:
                $ questionpreset = "quintus1"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    '“But it’s almost dusk! Ye need at least three hours to get to the other side of the woods.”
                    '
                    '(quintus1 preset)':
                        pass
        elif quintus_about_plague_cured:
            $ questionpreset = "quintus1"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                'He smiles. “Yer the savior of {color=#f6d6bd}Old Págos{/color}, I’ll be happy to let ye through. Here, see?” He points at the long, twisted rope that hangs from an iron hook. “I’ll climb down and remove the beam on the other side, ye’ll take down yours. Ye need at least three hours to get through the woods.”
                '
                '(quintus1 preset)':
                    pass
        else:
            $ description_quintus01 = "He now takes care of the western gate that leads to the heart of the forest."
            menu:
                '“Here, see?” He points at the long, twisted rope that hangs from an iron hook. “I could climb down and remove the beam on the other side, ye’ll take down yours. Ye need at least three hours to get through the woods.”
                \n\nHe touches his stomach and takes a deep breath. “But I need ye to give me aught first.”
                '
                '“What do you want?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want?”')
                    jump westgateaboutopeningthegate02

#############################################################################

label workinglabelwestgatefirsttimealt01: # gdy wbił do lokacji od wschodu, podczas shortcut_inprogress, po raz pierwszy
    label westgatefirsttimealt01: # gdy wbił do lokacji od wschodu, podczas shortcut_inprogress, po raz pierwszy
        menu:
            'The corridor of leaves and gray rocks leads you to a gate, large enough to let a wagon through, held together by a wooden bar. The planks and rocks are covered with claw marks left by various monsters, but they weren’t able to damage the wall as much as the passage of time and the piercing rains.
            \n\n{color=#f6d6bd}A large man{/color}, covered in shadows, is observing you from the roofed tower. His voice is hoarse, distrustful. “Ye lost or aught? Listen, grab the wooden bar on the door. I’ll grab the one on {i}my{/i} side, just give me a minute.”
            '
            'I dismount and lift the log.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I dismount and lift the log.')
                menu:
                    'The man lowers the rope that hangs from an iron hook. You hear him pressing his feet to the wall as he climbs down, getting on the ground swiftly.
                    \n\n“Now, step back!” His voice is muffled. The man pushes both leaves of the gate and steps closer, looking around. He’s holding a loaded crossbow, but doesn’t aim at you.
                    \n\nHe’s both tall and wide. He’s wearing a black gambeson, so ragged it can’t be fastened anymore. It tells a story of claws, thorns, and improvised repairs. The hole in the man’s hemp pants reveals a scraped knee.
                    \n\n“Ye followed?” he whispers.
                    '
                    '“Not really.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not really.”')
                        if eudocia_bronzerod_rodin_westgate:
                            show areapicture westgatewest01bronzerod at basicfade
                        else:
                            show areapicture westgatewest01 at basicfade
                        $ at_activate = 1
                        $ at = 0
                        menu:
                            '“Good, good.” He steps away, letting you through. The stool and a bucket filled with dirty water don’t look like much of a resting spot.
                            \n\n“Yer safe now,” the man closes the gate and observes you with keen eyes. It’s hard to tell his age through his exhausted, sleepy eyes, a short, unkempt beard, and a bandage horizontally covering his ears and the spot that used to be his nose. There’s clotted blood in his brown hair, and mud on his clothes and brown neck. Despite all this, he’s of a huge shell, with wide shoulders and thick legs.
                            \n\n“Now, how are ye alive? ” He still holds his weapon, but doesn’t aim at you. “I don’t know ya mug.”
                            '
                            ' (disabled)' ( condition="at == 0" ):
                                pass
                            'I introduce myself. “Good time to get to know each other!”' ( condition="at == 'friendly'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (friendly) I introduce myself. “Good time to get to know each other!”')
                                $ at_activate = 0
                                $ at = 0
                                jump westgatefirsttimealt02friendly
                            '“Better remember this {i}mug{/i}, friend. It’s going to stay around for a while.” I introduce myself.' ( condition="at == 'playful'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (playful) “Better remember this {i}mug{/i}, friend. It’s going to stay around for a while.”')
                                $ at_activate = 0
                                $ at = 0
                                jump westgatefirsttimealt02playful
                            '“I’m [pcname], the new roadwarden. And you’re the gatekeeper, I assume?”' ( condition="at == 'distanced'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (distanced) “I’m %s, the new roadwarden. And you’re the gatekeeper, I assume?”' %pcname)
                                $ at_activate = 0
                                $ at = 0
                                jump westgatefirsttimealt02distanced
                            '“I’m a roadwarden. Better be ready to open this gate whenever I ask for it.”' ( condition="at == 'intimidating'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (intimidating) “I’m a roadwarden. Better be ready to open this gate whenever I ask for it.”')
                                $ at_activate = 0
                                $ at = 0
                                jump westgatefirsttimealt02intimidating
                            'I explain who I am. “I’m not looking for trouble, stranger. Though I may ask you to open this gate for me again in the future.”' ( condition="at == 'vulnerable'" ):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (vulnerable) I explain who I am. “I’m not looking for trouble, stranger. Though I may ask you to open this gate for me again in the future.”')
                                $ at_activate = 0
                                $ at = 0
                                jump westgatefirsttimealt02vulnerable

    label westgatefirsttimealt02friendly: #I introduce myself. “Good time to get to know each other!”
        $ quintus_friendship += 1
        menu:
            '“Yeah, I’ve got naught but time,” he chuckles weakly. “I heard no human voice in days,” he looks at his weapon. “I’m no enemy. Just on duty, guarding. Ye can hang around, but I’ve got no ale, or water.”
            \n\nHe takes a deep breath, observing you with curiosity. “So, a warden? Ye new to the job?”
            '
            '“Pretty new.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pretty new.”')
                menu:
                    '“Ye chose a shit place, then. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe build this place to keep them away from us. Naught but the brave ones enter the woods, and naught but the stupid ones to do it alone.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttimealt03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttimealt03pcwasnotinoldpagos
            '“New here, but I know what I’m doing.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “New here, but I know what I’m doing.”')
                menu:
                    '“No past would prepare ye for this shit place. Nights are all ape piss and blood. Just before sunrise, a bird tried to pluck my eye. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe build this place to keep them away from us. Naught but the brave ones enter the woods, and naught but the stupid ones to do it alone.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttimealt03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttimealt03pcwasnotinoldpagos

    label westgatefirsttimealt02playful: #“Better remember this {i}mug{/i}, friend. It’s going to stay around for a while.” I introduce myself.
        $ quintus_friendship += 0
        menu:
            '“I will, I will. I’m good with faces. These stuff ye have, that ass,” he points at your horse, “ye might as well scream {i}I’m not from here{/i}.” He pauses and looks at his weapon. “But I’m no enemy. Just on duty, guarding. We can talk, if ye want. I’ve time.”
            \n\nHe stands upright, observing you with curiosity. “So, a warden? Ye new to the job?”
            '
            '“Pretty new.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pretty new.”')
                menu:
                    '“Ye chose a shit place, then. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe build this place to keep them away from us. Naught but the brave ones enter the woods, and naught but the stupid ones to do it alone.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttimealt03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttimealt03pcwasnotinoldpagos
            '“New here, but I know what I’m doing.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “New here, but I know what I’m doing.”')
                menu:
                    '“No past would prepare ye for this shit place. Nights are all ape piss and blood. Just before sunrise, a bird tried to pluck my eye. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe build this place to keep them away from us. Naught but the brave ones enter the woods, and naught but the stupid ones to do it alone.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttimealt03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttimealt03pcwasnotinoldpagos

    label westgatefirsttimealt02distanced: #“I’m [pcname], the new roadwarden. And you’re the gatekeeper, I assume?”
        $ quintus_friendship += 0
        menu:
            '“Well, yeah.” He looks at his weapon. “I’m just on duty, guarding. But I’m no enemy of yas.”
            \n\nHe straightens up. “So, a warden? Ye new to the job?”
            '
            '“Pretty new.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pretty new.”')
                menu:
                    '“Ye chose a shit place, then. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe build this place to keep them away from us. Naught but the brave ones enter the woods, and naught but the stupid ones to do it alone.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttimealt03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttimealt03pcwasnotinoldpagos
            '“New here, but I know what I’m doing.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “New here, but I know what I’m doing.”')
                menu:
                    '“No past would prepare ye for this shit place. Nights are all ape piss and blood. Just before sunrise, a bird tried to pluck my eye. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe build this place to keep them away from us. Naught but the brave ones enter the woods, and naught but the stupid ones to do it alone.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttimealt03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttimealt03pcwasnotinoldpagos

    label westgatefirsttimealt02vulnerable: #I explain who I am. “I’m not looking for trouble, stranger. Can you open the gate for me?”
        $ quintus_friendship -= 1
        menu:
            '“Ye, warden? Ye better turn around, it’s a wild place, I’m not running after your screams if you enter the woods.” A short pause. “I’m armed, ye know,” he lifts a loaded crossbow and sticks it out of the shadows. “I’m just on duty, but ye know. Don’t play any tricks.”
            \n\nHe straightens up, towering over you. “Ye new to the job?”
            '
            '“Pretty new.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Pretty new.”')
                menu:
                    '“Ye chose a shit place, then. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe build this place to keep them away from us. Naught but the brave ones enter the woods, and naught but the stupid ones to do it alone.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttimealt03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttimealt03pcwasnotinoldpagos
            '“New here, but I know what I’m doing.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “New here, but I know what I’m doing.”')
                menu:
                    '“No past would prepare ye for this shit place. Nights are all ape piss and blood. Just before sunrise, a bird tried to pluck my eye. This gate, here?” He places his hand on a brick, as if to prove it exists. “It’s older than me. All there?” He points behind him. “Wilds and beasts. My tribe build this place to keep them away from us. Naught but the brave ones enter the woods, and naught but the stupid ones to do it alone.”
                    \n\nHe scratches the bandage on his cheek. “Name’s {color=#f6d6bd}Quintus{/color}, from {color=#f6d6bd}Old Págos{/color}. Been there?”
                    '
                    '“I have. They won’t let you in?”' if oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                        jump westgatefirsttimealt03pcwasinoldpagos
                    '“Not yet.”' if not oldpagos_firsttime:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                        jump westgatefirsttimealt03pcwasnotinoldpagos

    label westgatefirsttimealt02intimidating: #“I’m a roadwarden. Better be ready to open this gate whenever I ask.”
        $ quintus_friendship -= 2
        $ westgate_open = 1
        $ quintus_attitude = "intimidating"
        menu:
            'His voice is cold. “So be it, but I won’t let you through unless you’ve got enough time to get to the other side, three hours or so. Naught but the brave ones enter the woods, and naught but the stupid ones to do it alone.”
            \n\nHe scratches the bandage on his cheek. “I’m from {color=#f6d6bd}Old Págos{/color}, the builders of this place. Been there?”
            '
            '“I have. They won’t let you in?”' if oldpagos_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have. They won’t let you in?”')
                jump westgatefirsttimealt03pcwasinoldpagos
            '“Not yet.”' if not oldpagos_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Not yet.”')
                jump westgatefirsttimealt03pcwasnotinoldpagos

    label westgatefirsttimealt03pcwasinoldpagos:
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_17shortcut.ogg":
            play music "<loop 15.0>audio/track_17shortcut.ogg" fadeout 1.0 fadein 1.0
        menu:
            '“So ye know. We used to send one soul here every morning, and escort them back before nightfall. But some days ago, no one came for me. I spent a night here, sneaking wolf shits almost got me.” He crouches, draws a handful of water from the bucket, but after he smells it, he grunts and straightens up.
            \n\n“I went home by myself, only to learn about the sick. I’ve been here ever since.”
            '
            '“What do you know about the plague?”' if not quintus_about_plague:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                jump westgatealtaboutplague01
            '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                jump westgatealtaboutremainingonthepost01
            '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                jump westgatealtaboutmovingtoadifferentvillage01
            '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                jump westgatealtaboutsurvival01
            'I change the topic. “So, if I were to ask you to keep this gate open for me...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I change the topic. “So, if I were to ask you to keep this gate open for me...”')
                jump westgatealtaboutopeningthegate01

    label westgatefirsttimealt03pcwasnotinoldpagos:
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "<loop 15.0>audio/track_17shortcut.ogg":
            play music "<loop 15.0>audio/track_17shortcut.ogg" fadeout 1.0 fadein 1.0
        menu:
            '“So ye don’t know. It’s west from here, behind the crossroads, but it’s touched by sickness. We used to send one soul here every morning, and escort them back before nightfall. But some days ago, no one came for me. I spent a night here, sneaking wolf shits almost got me.” He crouches, draws a handful of water from the bucket, but after he smells it, he grunts and straightens up.
            \n\n“I went home by myself, only to learn about the sick. I’ve been here ever since.”
            '
            '“What do you know about the plague?”' if not quintus_about_plague:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                jump westgatealtaboutplague01
            '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                jump westgatealtaboutremainingonthepost01
            '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                jump westgatealtaboutmovingtoadifferentvillage01
            '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                jump westgatealtaboutsurvival01
            'I change the topic. “So, if I were to ask you to keep this gate open for me...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I change the topic. “So, if I were to ask you to keep this gate open for me...”')
                jump westgatealtaboutopeningthegate01

    label westgatealtaboutplague01: #“What do you know about the plague?”
        $ quintus_about_plague = 1
        menu:
            '“Not much. It kills, that’s all there is to know. My tribe’s smart, locking the gate. The Wright gave them strength.”
            '
            '“What do you know about the plague?”' if not quintus_about_plague:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                jump westgatealtaboutplague01
            '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                jump westgatealtaboutremainingonthepost01
            '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                jump westgatealtaboutmovingtoadifferentvillage01
            '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                jump westgatealtaboutsurvival01
            'I change the topic. “So, if I were to ask you to keep this gate open for me...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I change the topic. “So, if I were to ask you to keep this gate open for me...”')
                jump westgatealtaboutopeningthegate01

    label westgatealtaboutremainingonthepost01: #“Shouldn’t you look for a real shelter?”
        $ quintus_about_staying = 1
        menu:
            'He trembles, his eyes widen. “Someone {i}has got to{/i} stay at the gate. The villages in the east don’t know about the illness, they may try crossing the woods, hit the closed gate while fleeing some wolves and stuff.” He rubs his dirty neck. “And I also can’t leave the gate open, it’s like a dam for monsters. If all I can do is choose the way I die, this is it. With my duty fulfilled.”
            '
            '“What do you know about the plague?”' if not quintus_about_plague:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                jump westgatealtaboutplague01
            '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                jump westgatealtaboutremainingonthepost01
            '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                jump westgatealtaboutmovingtoadifferentvillage01
            '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                jump westgatealtaboutsurvival01
            'I change the topic. “So, if I were to ask you to keep this gate open for me...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I change the topic. “So, if I were to ask you to keep this gate open for me...”')
                jump westgatealtaboutopeningthegate01

    label westgatealtaboutmovingtoadifferentvillage01: #“You could at least spend the nighttime in one of the villages.”
        $ quintus_about_leaving = 1
        menu:
            'He adjusts his jacket by shaking his shoulders, making the buckles jingle. “I’m not a beggar, and the villages in the North won’t help me for more than a day or two. I’ve got no dragon bones, just this little ibex.” He pats his crossbow. “{color=#f6d6bd}Old Págos{/color} is by itself, we don’t look for {i}kind folks{/i}.”
            \n\nHe thinks for a moment. “I’ll just wait. I’ll get back home once the plague’s done. Or before winter.” You look at his disfigured face.
            '
            'He’s either mad or dumb.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s either mad or dumb.')
                jump westgatealtaboutmovingtoadifferentvillage02
            'He may be a bit too proud, but knows more about the locals than I do.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He may be a bit too proud, but knows more about the locals than I do.')
                label westgatealtaboutmovingtoadifferentvillage02:
                    menu:
                        'He glances at {color=#f6d6bd}[horsename]{/color}. “Ye understand, I’m sure. Wardens are souls of duty.”
                        '
                        '“What do you know about the plague?”' if not quintus_about_plague:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                            jump westgatealtaboutplague01
                        '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                            jump westgatealtaboutremainingonthepost01
                        '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                            jump westgatealtaboutmovingtoadifferentvillage01
                        '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                            jump westgatealtaboutsurvival01
                        'I change the topic. “So, if I were to ask you to keep this gate open for me...”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I change the topic. “So, if I were to ask you to keep this gate open for me...”')
                            jump westgatealtaboutopeningthegate01

    label westgatealtaboutsurvival01:
        $ quintus_about_survival = 1
        menu:
            '“Well, ye can call it {i}surviving{/i}. I call it {i}potions{/i}.” His chuckle makes him wince in pain. He puts a hand on his stomach and leans away. “Beasts took me for easy prey, but the good monks from the mountains equipped our guards well. They’re helping our ill, but used to brew all sorts of stuff.” His hand moves to an earthenware bottle by his belt.
            '
            '“What do you know about the plague?”' if not quintus_about_plague:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you know about the plague?”')
                jump westgatealtaboutplague01
            '“Shouldn’t you look for a real shelter?”' if not quintus_about_staying:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
                jump westgatealtaboutremainingonthepost01
            '“You could at least spend the nighttime in one of the villages.”' if quintus_about_staying and not quintus_about_leaving:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
                jump westgatealtaboutmovingtoadifferentvillage01
            '“I’m surprised you survived for this long.”' if quintus_about_staying and not quintus_about_survival:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m surprised you survived for this long.”')
                jump westgatealtaboutsurvival01
            'I change the topic. “So, if I were to ask you to keep this gate open for me...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I change the topic. “So, if I were to ask you to keep this gate open for me...”')
                jump westgatealtaboutopeningthegate01

    label westgatealtaboutopeningthegate01:
        $ quintus_about_gate = 1
        if westgate_open:
            if quarters <= (world_daylength-12):
                menu:
                    '“I can open it for ye... If yer sure about it. Ye need at least three hours to get to the other side of the woods.”
                    '
                    '“Do it.” I enter the forest.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do it.” I enter the forest.')
                        jump westgateenteringtheshortcut01
                    '“Maybe another time.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe another time.”')
                        jump westgateafterinteraction01
            else:
                $ questionpreset = "quintus1"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                menu:
                    '“But it’s almost dusk! Ye need at least three hours to get to the other side of the woods.”
                    '
                    '(quintus1 preset)':
                        pass
        elif quintus_about_plague_cured:
            $ questionpreset = "quintus1"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            menu:
                'He smiles. “Yer the savior of {color=#f6d6bd}Old Págos{/color}, I’ll be happy to let ye through. Ye need at least three hours to get to the other side of the woods.”
                '
                '(quintus1 preset)':
                    pass
        else:
            menu:
                '“Well, ye saw how it is. I {i}could{/i} open it for ye...” He touches his stomach and takes a deep breath. “But I need ye to give me aught first.”
                '
                '“What do you want?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you want?”')
                    jump westgateaboutopeningthegate02

#############################################################################

label workinglabelwestgateaboutopeningthegate02: #“What do you want?”
    label westgateaboutopeningthegate02:
        $ quintus_food_gate_amount = (5-quintus_friendship-appearance_charisma)
        if quintus_food_gate_amount < 2:
            $ quintus_food_gate_amount = 2
        menu:
            '“I’m hungry. Bring me some rations, maybe? Dried meat, apples, nuts. Maybe...” He sizes you up. “[quintus_food_gate_amount] meals. Then I’ll help ye with the gate.”
            '
            '“Sure. I’ll bring you some food.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. I’ll bring you some food.”')
                jump westgateaboutopeningthegate03yes
            '“Can’t you make an exception for me? Thanks to me, the plague of {color=#f6d6bd}Old Págos{/color} is no more.”' if not quintus_about_plague_cured and oldpagos_cured:
                jump westgateaboutcuredplague01alt
            '“Don’t you have time to hunt?”' if not quintus_food_gate_reason01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you have time to hunt?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason01
            '“I’ll go with you. I take the trophies, you get meat for roasting.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll go with you. I take the trophies, you get meat for roasting.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason04
            '“Shoot some birds with your crossbow. Surely they land on this wall?”' if quintus_food_gate_reason01 and not quintus_food_gate_reason06:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shoot some birds with your crossbow. Surely they land on this wall?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason06
            '“I can get you some quarrels. They’ll fix your problem for longer.”' if quintus_food_gate_reason06 and not quintus_food_gate_reason08:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can get you some quarrels. They’ll fix your problem for longer.”')
                jump westgateaboutopeningthegate03noalt
            '“You can just forage for nuts and berries.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can just forage for nuts and berries.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason02
            '“How about I pay you instead? Buy whatever you like in a villages.”' if not quintus_food_gate_reason03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about I pay you instead? Buy whatever you like in a villages.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason03
            '“Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”' if quintus_food_gate_reason03 and not quintus_food_gate_reason05:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason05
            '“Food rations are expensive, though.”' if quintus_food_gate_reason05 and not quintus_food_gate_reason07:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Food rations are expensive, though.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason07

    label westgateaboutopeningthegate03yes:
        $ quest_fetchingfood = 1
        $ questionpreset = "quintus1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ renpy.notify("New entry: Fetching Food")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Fetching Food{/i}')
        menu:
            '“Thanks.” His smile may be disfigured by his wounds, but is as warm as his voice. “I’ll take any help I can get.”
            '
            '(quintus1 preset)':
                pass

    label westgateaboutopeningthegate03no:
        $ westgate_open = 1
        $ quintus_friendship -= 1
        $ questionpreset = "quintus1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'He rolls his eyes, then scowls at you from above his bandages. “Shit, warden, forget it. I’ll find aught on my own.”
            '
            '(quintus1 preset)':
                pass

    label westgateaboutopeningthegate03noalt:
        $ westgate_open = 1
        $ quintus_friendship -= 1
        $ questionpreset = "quintus1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '“I...” His eyes widen, but then his lips form an annoyed grimace. He spits on the ground and sighs. “Shit, warden, forget it. I’ll find aught on my own.”
            '
            '(quintus1 preset)':
                pass

    label westgateaboutopeningthegate02reason01: # “Don’t you have time to hunt?”
        $ quintus_food_gate_reason01 = 1
        $ quintus_food_gate_reason_points += 1
        menu:
            '“Time? But I’ve {i}got to{/i} stay near the gate, I can’t keep people waiting while I track deer.” He touches the bandage on his face. “And if I die, there will be no keeper left.”
            '
            '“Sure. I’ll bring you some food.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. I’ll bring you some food.”')
                jump westgateaboutopeningthegate03yes
            '“Can’t you make an exception for me? Thanks to me, the plague of {color=#f6d6bd}Old Págos{/color} is no more.”' if not quintus_about_plague_cured and oldpagos_cured:
                jump westgateaboutcuredplague01alt
            '“Don’t you have time to hunt?”' if not quintus_food_gate_reason01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you have time to hunt?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason01
            '“I’ll go with you. I take the trophies, you get meat for roasting.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll go with you. I take the trophies, you get meat for roasting.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason04
            '“Shoot some birds with your crossbow. Surely they land on this wall?”' if quintus_food_gate_reason01 and not quintus_food_gate_reason06:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shoot some birds with your crossbow. Surely they land on this wall?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason06
            '“I can get you some quarrels. They’ll fix your problem for longer.”' if quintus_food_gate_reason06 and not quintus_food_gate_reason08:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can get you some quarrels. They’ll fix your problem for longer.”')
                jump westgateaboutopeningthegate03noalt
            '“You can just forage for nuts and berries.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can just forage for nuts and berries.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason02
            '“How about I pay you instead? Buy whatever you like in a villages.”' if not quintus_food_gate_reason03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about I pay you instead? Buy whatever you like in a villages.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason03
            '“Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”' if quintus_food_gate_reason03 and not quintus_food_gate_reason05:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason05
            '“Food rations are expensive, though.”' if quintus_food_gate_reason05 and not quintus_food_gate_reason07:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Food rations are expensive, though.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason07

    label westgateaboutopeningthegate02reason04: # “I’ll go with you. I take the trophies, you get meat for roasting.”
        $ quintus_food_gate_reason04 = 1
        $ quintus_about_fatsmoke = 1
        $ quintus_food_gate_reason_points += 1
        menu:
            '“But goblins and trolls can smell the burning fat! Roasting is the {i}opposite{/i} of what I should do.”
            '
            '“Sure. I’ll bring you some food.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. I’ll bring you some food.”')
                jump westgateaboutopeningthegate03yes
            '“Can’t you make an exception for me? Thanks to me, the plague of {color=#f6d6bd}Old Págos{/color} is no more.”' if not quintus_about_plague_cured and oldpagos_cured:
                jump westgateaboutcuredplague01alt
            '“Don’t you have time to hunt?”' if not quintus_food_gate_reason01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you have time to hunt?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason01
            '“I’ll go with you. I take the trophies, you get meat for roasting.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll go with you. I take the trophies, you get meat for roasting.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason04
            '“Shoot some birds with your crossbow. Surely they land on this wall?”' if quintus_food_gate_reason01 and not quintus_food_gate_reason06:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shoot some birds with your crossbow. Surely they land on this wall?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason06
            '“I can get you some quarrels. They’ll fix your problem for longer.”' if quintus_food_gate_reason06 and not quintus_food_gate_reason08:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can get you some quarrels. They’ll fix your problem for longer.”')
                jump westgateaboutopeningthegate03noalt
            '“You can just forage for nuts and berries.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can just forage for nuts and berries.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason02
            '“How about I pay you instead? Buy whatever you like in a villages.”' if not quintus_food_gate_reason03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about I pay you instead? Buy whatever you like in a villages.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason03
            '“Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”' if quintus_food_gate_reason03 and not quintus_food_gate_reason05:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason05
            '“Food rations are expensive, though.”' if quintus_food_gate_reason05 and not quintus_food_gate_reason07:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Food rations are expensive, though.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason07

    label westgateaboutopeningthegate02reason06: #“Shoot some birds with your crossbow. Surely they land on this wall?”
        $ quintus_food_gate_reason06 = 1
        $ quintus_food_gate_reason_points += 1
        menu:
            '“I’m not much of a shot, really.” He scratches his right arm. “I’d rather save my arrows for all the beasts and stuff.”
            '
            '“Sure. I’ll bring you some food.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. I’ll bring you some food.”')
                jump westgateaboutopeningthegate03yes
            '“Can’t you make an exception for me? Thanks to me, the plague of {color=#f6d6bd}Old Págos{/color} is no more.”' if not quintus_about_plague_cured and oldpagos_cured:
                jump westgateaboutcuredplague01alt
            '“Don’t you have time to hunt?”' if not quintus_food_gate_reason01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you have time to hunt?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason01
            '“I’ll go with you. I take the trophies, you get meat for roasting.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll go with you. I take the trophies, you get meat for roasting.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason04
            '“Shoot some birds with your crossbow. Surely they land on this wall?”' if quintus_food_gate_reason01 and not quintus_food_gate_reason06:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shoot some birds with your crossbow. Surely they land on this wall?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason06
            '“I can get you some quarrels. They’ll fix your problem for longer.”' if quintus_food_gate_reason06 and not quintus_food_gate_reason08:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can get you some quarrels. They’ll fix your problem for longer.”')
                jump westgateaboutopeningthegate03noalt
            '“You can just forage for nuts and berries.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can just forage for nuts and berries.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason02
            '“How about I pay you instead? Buy whatever you like in a villages.”' if not quintus_food_gate_reason03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about I pay you instead? Buy whatever you like in a villages.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason03
            '“Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”' if quintus_food_gate_reason03 and not quintus_food_gate_reason05:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason05
            '“Food rations are expensive, though.”' if quintus_food_gate_reason05 and not quintus_food_gate_reason07:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Food rations are expensive, though.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason07

    label westgateaboutopeningthegate02reason02: # “You can just forage for nuts and berries.”
        $ quintus_food_gate_reason02 = 1
        $ quintus_food_gate_reason_points += 1
        menu:
            '“I eat berries and sorrel every day, but this isn’t {i}real{/i} food, and I’ve got to fight off all the snakes and badgers. Nuts are nowhere around, too many squirrels, rats, and boars,” he licks his lips at the very thought. “I found some acorns, but I had never roasted them before, they may make me sick.”
            '
            '“Sure. I’ll bring you some food.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. I’ll bring you some food.”')
                jump westgateaboutopeningthegate03yes
            '“Can’t you make an exception for me? Thanks to me, the plague of {color=#f6d6bd}Old Págos{/color} is no more.”' if not quintus_about_plague_cured and oldpagos_cured:
                jump westgateaboutcuredplague01alt
            '“Don’t you have time to hunt?”' if not quintus_food_gate_reason01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you have time to hunt?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason01
            '“I’ll go with you. I take the trophies, you get meat for roasting.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll go with you. I take the trophies, you get meat for roasting.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason04
            '“Shoot some birds with your crossbow. Surely they land on this wall?”' if quintus_food_gate_reason01 and not quintus_food_gate_reason06:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shoot some birds with your crossbow. Surely they land on this wall?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason06
            '“I can get you some quarrels. They’ll fix your problem for longer.”' if quintus_food_gate_reason06 and not quintus_food_gate_reason08:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can get you some quarrels. They’ll fix your problem for longer.”')
                jump westgateaboutopeningthegate03noalt
            '“You can just forage for nuts and berries.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can just forage for nuts and berries.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason02
            '“How about I pay you instead? Buy whatever you like in a villages.”' if not quintus_food_gate_reason03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about I pay you instead? Buy whatever you like in a villages.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason03
            '“Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”' if quintus_food_gate_reason03 and not quintus_food_gate_reason05:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason05
            '“Food rations are expensive, though.”' if quintus_food_gate_reason05 and not quintus_food_gate_reason07:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Food rations are expensive, though.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason07

    label westgateaboutopeningthegate02reason03: #“How about I pay you instead? Buy whatever you like in a villages.”
        $ quintus_food_gate_reason03 = 1
        $ quintus_food_gate_reason_points += 1
        menu:
            '“I can do naught with coins. I’ve got to stay on the wall, and...” He hesitates and looks away, then says with frustration. “And traveling without an ass to ride isn’t as safe, ye know!”
            '
            '“It’s a horse, not an ass.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s a horse, not an ass.”')
                jump westgateaboutopeningthegate02ass
            '“Sure. I’ll bring you some food.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. I’ll bring you some food.”')
                jump westgateaboutopeningthegate03yes
            '“Can’t you make an exception for me? Thanks to me, the plague of {color=#f6d6bd}Old Págos{/color} is no more.”' if not quintus_about_plague_cured and oldpagos_cured:
                jump westgateaboutcuredplague01alt
            '“Don’t you have time to hunt?”' if not quintus_food_gate_reason01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you have time to hunt?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason01
            '“I’ll go with you. I take the trophies, you get meat for roasting.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll go with you. I take the trophies, you get meat for roasting.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason04
            '“Shoot some birds with your crossbow. Surely they land on this wall?”' if quintus_food_gate_reason01 and not quintus_food_gate_reason06:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shoot some birds with your crossbow. Surely they land on this wall?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason06
            '“I can get you some quarrels. They’ll fix your problem for longer.”' if quintus_food_gate_reason06 and not quintus_food_gate_reason08:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can get you some quarrels. They’ll fix your problem for longer.”')
                jump westgateaboutopeningthegate03noalt
            '“You can just forage for nuts and berries.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can just forage for nuts and berries.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason02
            '“How about I pay you instead? Buy whatever you like in a villages.”' if not quintus_food_gate_reason03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about I pay you instead? Buy whatever you like in a villages.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason03
            '“Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”' if quintus_food_gate_reason03 and not quintus_food_gate_reason05:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason05
            '“Food rations are expensive, though.”' if quintus_food_gate_reason05 and not quintus_food_gate_reason07:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Food rations are expensive, though.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason07

    label westgateaboutopeningthegate02ass: #“It’s a horse, not an ass.”
        menu:
            '“So {i}that’s{/i} why it’s so tall! First time I see one.”
            '
            '“Sure. I’ll bring you some food.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. I’ll bring you some food.”')
                jump westgateaboutopeningthegate03yes
            '“Can’t you make an exception for me? Thanks to me, the plague of {color=#f6d6bd}Old Págos{/color} is no more.”' if not quintus_about_plague_cured and oldpagos_cured:
                jump westgateaboutcuredplague01alt
            '“Don’t you have time to hunt?”' if not quintus_food_gate_reason01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you have time to hunt?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason01
            '“I’ll go with you. I take the trophies, you get meat for roasting.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll go with you. I take the trophies, you get meat for roasting.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason04
            '“Shoot some birds with your crossbow. Surely they land on this wall?”' if quintus_food_gate_reason01 and not quintus_food_gate_reason06:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shoot some birds with your crossbow. Surely they land on this wall?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason06
            '“I can get you some quarrels. They’ll fix your problem for longer.”' if quintus_food_gate_reason06 and not quintus_food_gate_reason08:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can get you some quarrels. They’ll fix your problem for longer.”')
                jump westgateaboutopeningthegate03noalt
            '“You can just forage for nuts and berries.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can just forage for nuts and berries.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason02
            '“How about I pay you instead? Buy whatever you like in a villages.”' if not quintus_food_gate_reason03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about I pay you instead? Buy whatever you like in a villages.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason03
            '“Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”' if quintus_food_gate_reason03 and not quintus_food_gate_reason05:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason05
            '“Food rations are expensive, though.”' if quintus_food_gate_reason05 and not quintus_food_gate_reason07:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Food rations are expensive, though.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason07

    label westgateaboutopeningthegate02reason05: #“Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”
        $ quintus_food_gate_reason05 = 1
        $ quintus_food_gate_reason_points += 1
        menu:
            '“I hardly have any, and have naught to barter. Why would I carry pretty stuff on a {i}wall duty{/i}?”
            '
            '“Sure. I’ll bring you some food.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. I’ll bring you some food.”')
                jump westgateaboutopeningthegate03yes
            '“Can’t you make an exception for me? Thanks to me, the plague of {color=#f6d6bd}Old Págos{/color} is no more.”' if not quintus_about_plague_cured and oldpagos_cured:
                jump westgateaboutcuredplague01alt
            '“Don’t you have time to hunt?”' if not quintus_food_gate_reason01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you have time to hunt?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason01
            '“I’ll go with you. I take the trophies, you get meat for roasting.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll go with you. I take the trophies, you get meat for roasting.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason04
            '“Shoot some birds with your crossbow. Surely they land on this wall?”' if quintus_food_gate_reason01 and not quintus_food_gate_reason06:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shoot some birds with your crossbow. Surely they land on this wall?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason06
            '“I can get you some quarrels. They’ll fix your problem for longer.”' if quintus_food_gate_reason06 and not quintus_food_gate_reason08:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can get you some quarrels. They’ll fix your problem for longer.”')
                jump westgateaboutopeningthegate03noalt
            '“You can just forage for nuts and berries.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can just forage for nuts and berries.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason02
            '“How about I pay you instead? Buy whatever you like in a villages.”' if not quintus_food_gate_reason03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about I pay you instead? Buy whatever you like in a villages.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason03
            '“Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”' if quintus_food_gate_reason03 and not quintus_food_gate_reason05:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason05
            '“Food rations are expensive, though.”' if quintus_food_gate_reason05 and not quintus_food_gate_reason07:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Food rations are expensive, though.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason07

    label westgateaboutopeningthegate02reason07: #“Food rations are expensive, though.”
        $ quintus_food_gate_reason07 = 1
        $ quintus_food_gate_reason_points += 1
        menu:
            '“That’s because they’re healthy, nah? The monks said so.”
            '
            '“Sure. I’ll bring you some food.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure. I’ll bring you some food.”')
                jump westgateaboutopeningthegate03yes
            '“Can’t you make an exception for me? Thanks to me, the plague of {color=#f6d6bd}Old Págos{/color} is no more.”' if not quintus_about_plague_cured and oldpagos_cured:
                jump westgateaboutcuredplague01alt
            '“Don’t you have time to hunt?”' if not quintus_food_gate_reason01:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you have time to hunt?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason01
            '“I’ll go with you. I take the trophies, you get meat for roasting.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason04:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll go with you. I take the trophies, you get meat for roasting.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason04
            '“Shoot some birds with your crossbow. Surely they land on this wall?”' if quintus_food_gate_reason01 and not quintus_food_gate_reason06:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shoot some birds with your crossbow. Surely they land on this wall?”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason06
            '“I can get you some quarrels. They’ll fix your problem for longer.”' if quintus_food_gate_reason06 and not quintus_food_gate_reason08:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can get you some quarrels. They’ll fix your problem for longer.”')
                jump westgateaboutopeningthegate03noalt
            '“You can just forage for nuts and berries.”' if quintus_food_gate_reason01 and not quintus_food_gate_reason02:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You can just forage for nuts and berries.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason02
            '“How about I pay you instead? Buy whatever you like in a villages.”' if not quintus_food_gate_reason03:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about I pay you instead? Buy whatever you like in a villages.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason03
            '“Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”' if quintus_food_gate_reason03 and not quintus_food_gate_reason05:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then give me coins, I’ll bring you a barrel of salted fish, or some oats and cheese.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason05
            '“Food rations are expensive, though.”' if quintus_food_gate_reason05 and not quintus_food_gate_reason07:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Food rations are expensive, though.”')
                if quintus_food_gate_reason_points >= quintus_food_gate_reason_points_required:
                    jump westgateaboutopeningthegate03no
                else:
                    jump westgateaboutopeningthegate02reason07

#############################################################################

label westgateregular01: # gdy wbił do lokacji normalnie, po raz któryś
    if dalit_about_quintus and (dalit_about_quintus+2) < day and not quintus_about_dalit:
        $ questionpreset = "quintus1"
        $ quintus_friendship += 2
        $ quintus_about_dalit = 1
        $ dalit_name = "Dalit"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '[westgate_fluff] {color=#f6d6bd}Quintus{/color} [westgate_fluff2]. “Warden! Thanks for talking with {color=#f6d6bd}Dalit{/color}. She brought me some supplies for my tusks and claws. Things could look better, but ye know!”
            '
            '(quintus1 preset)':
                pass
    else:
        $ questionpreset = "quintus1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if quintus_friendship >= 4:
            $ custom1 = "“Salutations, warden! Ye here about the gate?”"
        elif quintus_friendship > 0:
            $ custom1 = "He greets you with a nod and adjusts his jacket."
        else:
            $ custom1 = "“What d’ye want?”"
        menu:
            '[westgate_fluff] {color=#f6d6bd}Quintus{/color} [westgate_fluff2]. [custom1]
            '
            '(quintus1 preset)':
                pass

label westgatetravelingshortcut01: # gdy wbił do lokacji od wschodu, ale był już tu wcześniej
    $ questionpreset = "quintus1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if dalit_about_quintus and (dalit_about_quintus+2) < day and not quintus_about_dalit:
        $ quintus_friendship += 2
        $ quintus_about_dalit = 1
        $ dalit_name = "Dalit"
        if not westgate_open:
            $ custom2 = " I’m not a monster, I can’t keep ye at the wilds’ mercy, but ye still owe me some food!"
        else:
            $ custom2 = ""
        menu:
            '[westgate_fluff] {color=#f6d6bd}Quintus{/color} [westgate_fluff3]. “Warden! Thanks for talking with {color=#f6d6bd}Dalit{/color}. She brought me some supplies for my tusks and claws. Things could look better, but ye know![custom2]”
            '
            '(quintus1 preset)':
                pass
    else:
        if quintus_friendship >= 4:
            $ custom1 = "“Salutations, warden!"
        elif quintus_friendship > 0:
            $ custom1 = "“Still alive, eh?"
        else:
            $ custom1 = "“Ye again."
        if not westgate_open:
            $ custom2 = " I’m not a monster, I can’t keep ye at the wilds’ mercy. But ye still owe me some food!”"
        else:
            if quintus_friendship >= 4:
                $ custom2 = " What are ye, a lord of the wilds or aught?”"
            elif quintus_friendship > 0:
                $ custom2 = "”"
            else:
                $ custom2 = " What do ye want?”"
        menu:
            '[westgate_fluff] {color=#f6d6bd}Quintus{/color} [westgate_fluff3]. [custom1][custom2]
            '
            '(quintus1 preset)':
                pass

#################################################################

label westgateafterinteraction01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "quintus1"
    $ custom1 = renpy.random.choice(['He looks around, startled by a bird.', 'He stretches.', 'He yawns.', 'He adjusts his jacket.', '“Aught else?”'])
    menu:
        '[custom1]
        '
        '(quintus1 preset)':
            pass

label westgateaboutstaying01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Shouldn’t you look for a real shelter?”')
    $ quintus_about_staying = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "quintus1"
    menu:
        'He trembles, his eyes widen. “Someone {i}has got to{/i} stay at the gate. The villages in the east don’t know about the illness, they may try crossing the woods, hit the closed gate while fleeing some wolves and stuff.” He rubs his dirty neck. “And I also can’t leave the gate open, it’s like a dam for monsters. If all I can do is choose the way I die, this is it. With my duty fulfilled.”
        '
        '(quintus1 set)':
            pass

label westgateaboutleaving1:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You could at least spend the nighttime in one of the villages.”')
    $ quintus_about_leaving = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ questionpreset = "quintus1"
    menu:
        'He adjusts his jacket by shaking his shoulders, making the buckles jingle. “I’m not a beggar, and the villages in the North won’t help me for more than a day or two. I’ve got no dragon bones, just this little ibex.” He pats his crossbow. “{color=#f6d6bd}Old Págos{/color} is by itself, we don’t look for {i}kind folks{/i}.”
        \n\nHe thinks for a moment. “I’ll just wait. I’ll get back home once the plague’s done. Or before winter. Ye understand, I’m sure. Wardens are souls of duty.”
        '
        '(quintus1 set)':
            pass

label westgatepcgivesfoodrations01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have your food rations.”')
    $ item_rations -= quintus_food_gate_amount
    $ quintus_food_delivered_amount += 1
    $ renpy.notify("Quest completed: Fetching Food.\nYou lost %s food rations." %quintus_food_gate_amount)
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Fetching Food. You lost %s food rations.{/i}' %quintus_food_gate_amount)
    $ westgate_open = 1
    $ quintus_friendship += 1
    $ quest_fetchingfood = 2
    $ quest_fetchingfood_description01 = "I delivered the food."
    $ questionpreset = "quintus1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    if pc_goal == "iwanttohelp":
        $ pc_goal_iwanttohelppoints += 1
    menu:
        'He gives you a radiant smile. He cups his large, scarred hands, waiting for you to give him the packages. Once you’re done, he opens a sack of nuts and shoves them into his mouth - the bandage is the only thing that stops him from looking like a hamster.
        '
        '(quintus1 preset)':
            pass

label westgateenteringtheforest00:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’d like you to open the gate.”')
    if quarters <= (world_daylength-12):
        if not shortcut_traveled:
            $ custom1 = "“I don’t think ye should enter the wilds, but ye know. If ye say so.”"
        else:
            $ custom1 = "“Are ye really sure?”"
        menu:
            '[custom1]
            '
            '“Do it.” I enter the forest.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do it.” I enter the forest.')
                jump westgateenteringtheshortcut01
            '“Maybe another time.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe another time.”')
                jump westgateafterinteraction01
    else:
        $ questionpreset = "quintus1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '“It’s almost dusk, I can’t let ye through. Ye need at least three hours to get to the other edge, and then some to find an inn.”
            '
            '(quintus1 preset)':
                pass

label westgateenteringtheshortcut01:
    $ shortcut_traveled += 1
    $ shortcut_inprogress = 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    menu:
        'You lift the bar on your side of the gate and wait for {color=#f6d6bd}Quintus{/color}. You hear him pressing his feet to the wall as he climbs down with the help of his rope, getting on the ground swiftly. He gives you a serious look from the open gate.
        \n\n“Safe travels, warden.”
        '
        'I travel as far {color=#f6d6bd}east{/color} as I can.' if not stonesign_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel as far {color=#f6d6bd}east{/color} as I can.')
            $ questionpreset = 0
            $ travel_destination_shortcut = "stonesign"
            jump shortcut01
        'I travel to the other {color=#f6d6bd}edge of the woodland{/color}.' if stonesign_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel to the other {color=#f6d6bd}edge of the woodland{/color}.')
            $ questionpreset = 0
            $ travel_destination_shortcut = "stonesign"
            jump shortcut01
        'I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.' if shortcut_cairn_firsttime:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.')
            $ questionpreset = 0
            $ travel_destination_shortcut = "cairn"
            jump shortcut01
        'I return to {color=#f6d6bd}the bandits’ hideout{/color}.' if banditshideout_firsttime and not banditshideout_banned:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the bandits’ hideout{/color}.')
            $ questionpreset = 0
            $ travel_destination_shortcut = "hideout"
            jump shortcut01

label westgateaboutasterion01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}.”')
    $ quintus_about_asterion = 1
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    menu:
        '“That’s nice, but he hasn’t been here in many days. Ye sure he’s not dead?”
        \n\nAfter you admit that he very much may be, he puts a hand on his waist. “Well, better get ready to slit open every dragon belly in the wilds.”
        '
        '“Did he often travel through the woods?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he often travel through the woods?”')
            menu:
                '“Sure, though on a different mount. He had a saurian, four ibexes long, two ibexes tall. It moves on four legs, and jumps high and far. It’s dark green, like rotting leaves. That one time, I was taking a piss in the shrubs, and {color=#f6d6bd}Asterion{/color} made the beast run up the rock face, and it jumped {i}on{/i} that...” He points at the hill. “And like, they ran {i}above{/i} the wall, and landed on the other side, just like that!” He snaps his fingers, his voice and eyes gain new vigor.
                '
                '“You say the saurian was large and green?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You say the saurian was large and green?”')
                    if not quest_asterion_description07:
                        $ quest_asterion_description07 = "I’ve heard a more detailed description of Asterion’s {color=#f6d6bd}saurian{/color}. It’s larger than a horse, dark green, though the edges of its limbs, tail, and eyebrows are red-and-orange."
                    if not description_asterion08 and quest_asterion == 1:
                        $ description_asterion08 = "I’ve heard a more detailed description of Asterion’s {color=#f6d6bd}saurian{/color}. It’s larger than a horse, dark green, though the edges of its limbs, tail, and eyebrows are red-and-orange."
                        $ renpy.notify("Journal updated: Find the Roadwarden")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                    $ questionpreset = "quintus1"
                    $ can_leave = 1
                    $ can_rest = 1
                    $ can_items = 1
                    $ minutes += 5
                    menu:
                        '“I mean, not everywhere.” He points at his eyebrows. “He has red scales here, and on the tail, and... {i}Shoulders{/i}, I think. I don’t know what to call it.”
                        \n\nYou ask him for a bit about {color=#f6d6bd}Asterion{/color}, but he has little to add. “There used to be six of us, keepers. I saw him every now and then, but not that often.”
                        '
                        '(quintus1 preset)':
                            pass

label westgateaboutrecruitahunter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever met {color=#f6d6bd}Erastos{/color}?”')
    $ quest_recruitahunter_spokento_quintus = 1
    $ questionpreset = "quintus1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        '“Nah. I remember him trading with my neighbors once or twice, but I never spoke with him. A bit of a wimp.”
        '
        '(quintus1 preset)':
            pass

label westgateaboutbronzerod01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you know {color=#f6d6bd}Eudocia{/color}, the enchantress? I was wondering if you could place this in your tower for her.”')
    $ quintus_about_bronzerod = 1
    if quintus_about_plague_cured:
        $ eudocia_bronzerod_rodin_westgate = 1
        $ item_bronzerod -= 1
        $ eudocia_bronzerod_installed += 1
        if not item_bronzerod:
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
                    $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                    $ quest_bronzerod_description02 = 0
        $ questionpreset = "quintus1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ description_eudocia09 = "According to {color=#f6d6bd}Quintus{/color}, “she was a quiet kid, but a smart one. Never tried to steal my milk.”"
        menu:
            'You unpack and show him the rod. “Lighter than it looks.” He says quietly. “I’ll squeeze it into a crack. Ye already helped my people, and I know {color=#f6d6bd}Eudocia{/color}. She always does aught weird. She was a quiet kid, but a smart one. Never tried to steal my milk. Leave it to me.”
            '
            '(quintus1 preset)':
                pass
    else:
        $ quintus_food_bronzerod_amount = (6-quintus_friendship-appearance_charisma)
        if quintus_food_bronzerod_amount < 3:
            $ quintus_food_bronzerod_amount = 3
        menu:
            'You unpack and show him the rod. “Lighter than it looks.” He says quietly. “And I know {color=#f6d6bd}Eudocia{/color}. She always does aught weird. She was a quiet kid, but a smart one. Never tried to steal my milk.”
            \n\nHe hands it back to you and puts on an unpleasant smirk. “But I’m doing naught for free.”
            '
            '“Let me guess...”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let me guess...”')
                $ questionpreset = "quintus1"
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                $ description_eudocia09 = "{color=#f6d6bd}Quintus{/color} called her {i}a dissenter{/i}: “she was a quiet kid, but a smart one. Never tried to steal my milk.”"
                menu:
                    '“Bring me [quintus_food_bronzerod_amount] rations, some tasty ones. My people won’t be happy that I’m doing favors for a dissenter. I don’t mean you,” he clears his throat after seeing your look. “I better get strong before I start making excuses, no?”
                    '
                    '(quintus1 preset)':
                        pass

label westgategivesbronzerod01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here’s the food you asked for. And here’s the bronze rod.”')
    $ item_rations -= quintus_food_bronzerod_amount
    $ quintus_food_delivered_amount += 1
    $ renpy.notify("You lost %s food rations.\nJournal updated: Bronze Rods" %quintus_food_bronzerod_amount)
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost %s food rations. Journal updated: Bronze Rods{/i}' %quintus_food_bronzerod_amount)
    $ quintus_friendship += 1
    $ eudocia_bronzerod_rodin_westgate = 1
    $ item_bronzerod -= 1
    $ eudocia_bronzerod_installed += 1
    if not item_bronzerod:
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
                $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                $ quest_bronzerod_description02 = 0
    $ questionpreset = "quintus1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'His wide grin makes you think for a moment that he’s going to swallow an entire package at once. “Leave it to me. I’ll shove it into a crack. With one or two cords, it will resist rain, frost, and fogs.”
        '
        '(quintus1 preset)':
            pass

label westgateaboutshortcut01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about the road behind the gate?”')
    $ quintus_about_shortcut = 1
    $ minutes += 5
    $ questionpreset = "quintus1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ description_shortcut03 = "The locals claim that this place is abandoned, neglected, and unusually dangerous."
    menu:
        '“Oh, not much.” His chuckle turns into a cough. “It leads through lowlands, mostly woods and some ponds. It’s dark, and lethal.”
        \n\nHe mentions tales of ghosts, dragons, fogs, and blood mages, but whenever you ask about any creature in particular, his response is vague and brief.
        \n\n“The tribes abandoned this path. Ever since the war, the trade has been slow. People refused to patrol it. The plants are getting taller, but for at least a few more seasons it’s still a shortcut. It’s good that ye have a mount. If aught chases ye, always stay close to the paths, and ride as fast as ye can.”
        '
        '(quintus1 preset)':
            pass

label westgateaboutshortcut02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If no one uses this road... Why are you here?”')
    $ quintus_about_shortcut2 = 1
    $ quintus_left_gate_points += 1
    $ questionpreset = "quintus1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'He scowls at you. “Not no one. It’s where people hunt for monsters, and every few days, I have to open it for... {i}reasons{/i}.”
        '
        '(quintus1 preset)':
            pass

label westgateaboutoldpagos01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s it like to live in {color=#f6d6bd}Old Págos{/color}?”')
    $ quintus_about_oldpagos = 1
    $ questionpreset = "quintus1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ description_oldpagos00 = "According to {color=#f6d6bd}Quintus{/color}, {i}Págos{/i} means {i}Hill{/i}. He seems to be proud of his home."
    menu:
        'He opens his mouth, giving you a puzzled look, then lets out a weak chuckle. “What am I to say? We’ve got rocks,” he taps the wall, “and make houses, bowls, tools. We sell them, too. We grow oats and broad beans. ibexes give us wool, and skins for monks, what do ye call it, the one ye write on?” He moves on when you mention {i}parchment{/i}. “Yeah, yeah. It’s a good place, beautiful, old. {i}Hill{/i}, that’s what {i}Págos{/i} means. {color=#f6d6bd}Old Hill{/color}.”
        \n\nWhen you bring up the monastery, his eyes get brighter. “Good people! They came here on a mission, teaching us Wright’s book. My grandparents were pagans, ye know? But we now follow the River of Truth. We keep to ourselves, but help others when they need us.”
        '
        '(quintus1 preset)':
            pass

label westgateaboutbanditsALL:
    label westgateaboutbandits01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Are they bothering you?”')
        $ quintus_about_bandits = 1
        $ questionpreset = "quintus1"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            'He scratches the bandage on his cheek. “I... only know there’s one band, somewhere. But not around, I never saw them.”
            '
            '(quintus1 preset)':
                pass

    label westgateaboutbandits02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why are you afraid of {color=#f6d6bd}Glaucia{/color}?”')
        if (quintus_friendship+appearance_charisma) < 4:
            $ questionpreset = "quintus1"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ quintus_about_bandits_gray = 1
            menu:
                'His straightens up and gives you a long look. “I don’t know who yer talking about.”
                '
                '(quintus1 preset)':
                    pass
        else:
            $ quintus_about_bandits = 2
            $ questionpreset = "quintus1"
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ description_glaucia07 = "{color=#f6d6bd}Quintus{/color}, the gatekeeper, claims that she’s the one who forced him to stay on his post."
            menu:
                '“Warden, I... I can’t talk about her.” His shoulders slump, making him look like a wounded troll. “{i}I’ve got to{/i} look after the gate for her, or she’ll hurt someone... Important to me. If she learns I’m telling stories about her, I’m dead, too.”
                '
                '(quintus1 preset)':
                    pass

label westgateaboutibex01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any idea who could be the owner of an ibex marked with a red knot?”')
    $ quintus_about_ibex = 1
    $ questionpreset = "quintus1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'He flinches and narrows his eyes. “A red knot? We use those in my home. Like, not {i}my{/i}, but {color=#f6d6bd}Old Págos{/color}.”
        '
        '(quintus1 preset)':
            pass

label westgateaboutcuredplague01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring good news from {color=#f6d6bd}Old Págos{/color}. The plague is no more.”')
    $ quintus_about_plague_cured = 1
    $ quintus_friendship += 5
    if quintus_friendship < 5:
        $ quintus_friendship = 5
    if quest_fetchingfood == 1 and quintus_about_bronzerod == 1 and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_westgate:
        $ renpy.notify("Quest completed: Fetching Food.\nJournal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Fetching Food. Journal updated: Bronze Rods{/i}')
        $ custom1 = "He smiles again. “Thank ye, warden, ya soul carries duty like no other. I’ll be honored to keep the gate open for ye.” He bows to you. “If ye still have the rod, just leave it with me.”"
        $ quest_fetchingfood = 2
        $ quest_fetchingfood_description01 = "Once I brought him the news about my part in getting rid of the plague, he was grateful enough to let our deal go."
    elif quest_fetchingfood == 1:
        $ quest_fetchingfood = 2
        $ quest_fetchingfood_description01 = "Once I brought him the news about my part in getting rid of the plague, he was grateful enough to let our deal go."
        $ renpy.notify("Quest completed: Fetching Food")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Fetching Food{/i}')
        $ custom1 = "He smiles again. “Thank ye, warden, ya soul carries duty like no other. I’ll be honored to keep the gate open for ye.” He bows to you."
    elif quintus_about_bronzerod == 1 and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_westgate:
        $ renpy.notify("Journal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
        $ custom1 = "He smiles again. “Thank ye, warden, ya soul carries duty like no other. If ye still have the rod, just leave it with me.”"
    else:
        $ custom1 = "He smiles again. “Thank ye, warden, ya soul carries duty like no other.”"
    if quintus_about_bronzerod == 1 and quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_westgate:
        $ eudocia_bronzerod_rodin_westgate = 1
        $ item_bronzerod -= 1
        $ eudocia_bronzerod_installed += 1
        if not item_bronzerod:
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
                    $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                    $ quest_bronzerod_description02 = 0
    $ questionpreset = "quintus1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ minutes += 5
    menu:
        '“What?” He leans back. “Say again?” When you repeat, he tilts his head back and puts hands on his waist, bursting in laughter, though his voice is still shaking. “Tell me all!”
        \n\nHe has little patience, constantly throwing more questions at you - about the druid, his plan, your gifts for the “magic tree.” He’s far from happy when he hears about the prolonged seclusion. “I guess it’s fair. I’ll stay here for some more time. I don’t want to mess stuff up, like, I’m not as dumb as a bird.”
        \n\n[custom1]
        '
        '(quintus1 preset)':
            pass

label westgateaboutcuredplague01alt:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can’t you make an exception for me? Thanks to me, the plague of {color=#f6d6bd}Old Págos{/color} is no more.”')
    $ quintus_about_plague_cured = 1
    $ quintus_friendship += 5
    if quintus_friendship < 5:
        $ quintus_friendship = 5
    $ quest_fetchingfood = 2
    $ quest_fetchingfood_description01 = "Once I brought him the news about my part in getting rid of the plague, he was grateful enough to let our deal go."
    $ renpy.notify("Quest completed: Fetching Food")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Fetching Food{/i}')
    $ questionpreset = "quintus1"
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ minutes += 5
    menu:
        '“What?” He leans back. “Say again?” When you repeat, he tilts his head back and puts hands on his waist, bursting in laughter, though his voice is still shaking. “Tell me all!”
        \n\nHe has little patience, constantly throwing more questions at you - about the druid, his plan, your gifts for the “magic tree.” He’s far from happy when he hears about the prolonged seclusion. “I guess it’s fair. I’ll stay here for some more time. I don’t want to mess stuff up, like, I’m not as dumb as a bird.”
        \n\nHe smiles again. “Thank ye, warden, ya soul carries duty like no other. I’ll be honored to keep the gate open for ye.” He bows to you."
        '
        '(quintus1 preset)':
            pass

label westgateabouthighisland01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever heard about {color=#f6d6bd}High Island{/color}?”')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ quintus_about_highisland = 1
    $ questionpreset = "quintus1"
    menu:
        '“Eh? I heard, alright, ye can see its volcano from {color=#f6d6bd}Old Págos{/color}. The monks said it’s a weird place, but also {i}a tale for the worthy{/i}.”
        \n\nYou ask him if he knows this “tale”, and he glances in the direction of his home. “Nah.”
        '
        '(quintus1 preset)':
            pass

label westgateaboutmissinghunters01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Some time ago, a few people from {color=#f6d6bd}Creeks{/color} left their home to hunt. Have you met them?”')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ quintus_about_missinghunters = 1
    $ quest_missinghunters_vaschelknown = 1
    $ questionpreset = "quintus1"
    menu:
        '“I know naught about {i}people{/i}, but I met {color=#f6d6bd}Vaschel{/color}.” It takes him a few breaths to notice you’re waiting for him to go on. “They spent one night at this tower with me! Came from there,” he points at the woods in the east, “and then went back there. They were building a trap. Somewhere behind the lake? They shared a partridge with me, but never came here again. Good soul, very... {i}open-eyed{/i}.”
        '
        '(quintus1 preset)':
            pass

label westgateaboutvascheldead01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think {color=#f6d6bd}Vaschel’s{/color} died somewhere at the heart of the woods.”')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ quintus_about_vaschel = 1
    $ quintus_left_gate_points += 2
    $ quintus_friendship += 1
    $ questionpreset = "quintus1"
    menu:
        '“Shit,” he starts, but then nods with acceptance. “Too bad. I’d rather have more strong hunters around.”
        '
        '(quintus1 preset)':
            pass

label westgateaboutgambesonrepairset01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Need any help with your gambeson? With the repair tools I have, we could fix it together in about an hour.”')
    $ quintus_about_gambesonrepairset = 1
    $ quintus_friendship += 2
    $ quintus_left_gate_points += 1
    $ quarters += 3
    $ armor_fixingxp += 4
    $ renpy.notify("Your sewing experience increases.")
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Your sewing experience increases.{/i}')
    menu:
        '“Ye serious?” He leans forward, looking you in the eyes, then makes a confident nod. “Let’s get to it.”
        \n\n{color=#f6d6bd}Quintus{/color} turns out to know a thing or two about jackets and sewing. He gives you a few words of advice, turns his backup shirt into padding, and holds his jacket in ways that allow you to work in peace.
        \n\nWhen he puts on his restored armor, he lets out a strong laugh. “Great, great! But what am I to give you now?” He looks around and raises his finger. “Want an arrow for a crossbow? They’re not so easy to get!”
        '
        '“Sure.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sure.”')
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ item_crossbowquarrels += 1
            $ renpy.notify("You’ve got %s quarrels." %item_crossbowquarrels)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received a quarrel. You’ve got %s quarrels.{/i}' %item_crossbowquarrels)
            if item_crossbowquarrels >= 2:
                $ custom1 = "shove the quarrel into your quiver"
            else:
                $ custom1 = "wrap the quarrel with a scrap of fabric"
            $ description_quintus04 = "He has a crossbow, but claims to be bad at using it."
            $ questionpreset = "quintus1"
            menu:
                '“Not a big loss for me, I can’t hit shit anyway,” he chuckles as you [custom1].
                '
                '(quintus1 set)':
                    pass
        '“I don’t really need it.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t really need it.”')
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            $ quintus_friendship += 1
            $ description_quintus04 = "He has a crossbow, but claims to be bad at using it."
            $ questionpreset = "quintus1"
            menu:
                '“If you say so. I’m bad at shooting anyway, I wait for beasts to get {i}really{/i} close first.”
                '
                '(quintus1 set)':
                    pass

label quintus_left_gate_aboutALL:
    label quintus_left_gate_about01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “But seriously, you’re tempting the forest. You need to seek shelter.”')
        $ quintus_left_gate_about = 1
        menu:
            '“Nah,” he waves it off with a smile, but once he speaks, his voice cracks. “And where would I go, anyway?”
            '
            '“{color=#f6d6bd}Gale Rocks{/color} is safe.”' if galerocks_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Gale Rocks{/color} is safe.”')
                $ custom1 = "“I don’t know the road and I’ve heard it’s dangerous, but the people there are cold and unhelpful.” He gives you a long look. “I could spend some time with {color=#f6d6bd}Pelt’s{/color} crew again, but I can’t afford the stay from now until spring. Unless they’re looking for a pair of hands, I better stay here.”"
                $ quintus_left_gate_points += 0
                jump quintus_left_gate_about02
            '“{color=#f6d6bd}Foggy’s{/color} place is not that far.”' if foggylake_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Foggy’s{/color} place is not that far.”')
                $ custom1 = "“Maybe for ye. But her tavern is already full, I’d have even less space there than I have in this tower.” He gives you a long look. “I could spend some time with {color=#f6d6bd}Pelt’s{/color} crew again, but I can’t afford the stay from now until spring. Unless they’re looking for a pair of hands, I better stay here.”"
                $ quintus_left_gate_points += 1
                jump quintus_left_gate_about02
            '“{color=#f6d6bd}Creeks{/color} seems nice.”' if creeks_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Creeks{/color} seems nice.”')
                $ custom1 = "“It’s not bad, I guess.” He gives you a long look. “But they don’t let people stay with them, that’s what the tavern is for. Know what? I could spend some time with {color=#f6d6bd}Pelt’s{/color} crew again, but I can’t afford the stay from now until spring. Unless they’re looking for a pair of hands, I better stay here.”"
                $ quintus_left_gate_points += 2
                jump quintus_left_gate_about02
            '“{color=#f6d6bd}White Marshes{/color} isn’t {i}too{/i} bad.”' if whitemarshes_firsttime and not whitemarshes_destroyed and not whitemarshes_attacked:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}White Marshes{/color} isn’t {i}too{/i} bad.”')
                $ custom1 = "“What do ye mean? They’ve got not enough food for themselves, I’d be lucky if they wouldn’t eat {i}me{/i}.” He gives you a long look. “I could spend some time with {color=#f6d6bd}Pelt’s{/color} crew again, but I can’t afford the stay from now until spring. Unless they’re looking for a pair of hands, I better stay here.”"
                $ quintus_left_gate_points += 0
                jump quintus_left_gate_about02
            '“{color=#f6d6bd}Howler’s Dell{/color} has more supplies than you could eat in a year.”' if howlersdell_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Howler’s Dell{/color} has more supplies than you could eat in a year.”')
                $ custom1 = "“And they would take a finger from me for each bite, I’ve hardly got any dragons.” He gives you a long look. “I could spend some time with {color=#f6d6bd}Pelt’s{/color} crew again, their place is cheaper. But forget it, I can’t afford even that. Unless they’re looking for a pair of hands, I better stay here.”"
                $ quintus_left_gate_points += 1
                jump quintus_left_gate_about02
            '“{color=#f6d6bd}Pelt of the North{/color} has plenty of space.”' if peltnorth_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Pelt of the North{/color} has plenty of space.”')
                $ custom1 = "“Know what? I wouldn’t mind spending time with {color=#f6d6bd}Dalit{/color} and her crew, especially the winter... But forget it, I can’t afford even that. Unless they’re looking for a pair of hands, I better stay here.”"
                $ quintus_friendswithdalit = 1
                $ quintus_left_gate_points += 3
                jump quintus_left_gate_about02
            '“I don’t know.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t know.”')
                $ custom1 = "“Yeah, me neither. I could spend some time with {color=#f6d6bd}Pelt’s{/color} crew again, but I can’t afford the stay from now until spring. Unless they’re looking for a pair of hands, I better stay here.”"
                jump quintus_left_gate_about02

    label quintus_left_gate_about02:
        menu:
            '[custom1]
            '
            '“The woods are going to get even more dangerous. There’s a swarm of undead, just north of here.”' if whitemarshes_destroyed and not quintus_left_gate_points_argument_nomoreundead:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The woods are going to get even more dangerous. There’s a swarm of undead, just north of here.”')
                $ quintus_left_gate_points_argument_nomoreundead = 1
                $ quintus_left_gate_points += 5
                $ custom1 = "“Eh? What {i}undead{/i}? Empty ones?” He looks toward the bogs, as if a group of monsters was just about to jump upon you from the top of the scarp.\n\nYou share what may be of use to him, without putting too much of an emphasis on your role in the village’s collapse. “Those bark-eating wretches, choked by their own spells,” he spits on the ground. “I really can’t stay here much longer.”"
                jump quintus_left_gate_about03
            '“The people of {color=#f6d6bd}Gale Rocks{/color} are not going to support {color=#f6d6bd}Glaucia{/color} any longer. Her role in the peninsula will dwindle.”' if quintus_about_bandits == 2 and quest_galerockssupport == 2 and not quintus_left_gate_points_argument_glauciadefeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The people of {color=#f6d6bd}Gale Rocks{/color} are not going to support {color=#f6d6bd}Glaucia{/color} any longer. Her role in the peninsula will dwindle.”')
                $ quintus_left_gate_points_argument_glauciadefeated = 1
                $ quintus_left_gate_points += 1
                $ quintus_friendship += 2
                $ custom1 = "He looks around and reaches toward his bandage, raising it like a mask. “Did... ye do this?” You start to explain, and his voice lowers to a whisper. “Don’t bother, I don’t follow all this anyway. All I need to say is that this land {i}needed{/i} someone like ye.”"
                jump quintus_left_gate_about03
            '“I’ve entered the woods many times already, and you can trust me - the creatures there are beyond any human.”' if shortcut_traveled >= 3 and not quintus_left_gate_points_argument_shortcut:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve entered the woods many times already, and you can trust me - the creatures there are beyond any human.”')
                $ quintus_left_gate_points_argument_shortcut = 1
                $ quintus_left_gate_points += 3
                $ custom1 = "The longer he listens to your tale, the more his shoulder slump. “Thanks for throwing food at my nightmares. I heard monstrous throats before, but I hoped they would stay, I don’t know, {i}away{/i}.”"
                $ minutes += 5
                jump quintus_left_gate_about03
            '“Don’t you miss fresh, warm food? Rations lose their charm quickly.”' if quintus_food_delivered_amount >= 1 and not quintus_left_gate_points_argument_food:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you miss fresh, warm food? Rations lose their charm quickly.”')
                $ quintus_left_gate_points_argument_food = 1
                $ quintus_left_gate_points += 2
                $ custom1 = "He lets out a hiss and raises his chin proudly, but after another breath he licks his lips."
                jump quintus_left_gate_about03
            '“Maybe you don’t need shelter for winter, just autumn. The tribe of {color=#f6d6bd}Gale Rocks{/color} delivered supplies to your home. You won’t starve there.”' if oldpagos_plague_helpfromgalerocks >= 2 and not quintus_left_gate_points_argument_oldpagoshelp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe you don’t need shelter for winter, just autumn. The tribe of {color=#f6d6bd}Gale Rocks{/color} delivered supplies to your home. You won’t starve there.”')
                $ quintus_left_gate_points_argument_oldpagoshelp = 1
                $ quintus_left_gate_points += 3
                $ custom1 = "He bursts into laughter. “Great, great! Those are the last people I would expect this from! Maybe beside {color=#f6d6bd}Howler’s{/color},” he makes a wide grin."
                jump quintus_left_gate_about03
            '“So the thing that stops you from going to {color=#f6d6bd}Pelt{/color} right away is dragon bones?”' if not quintus_left_gate_points_argument_iason_about:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So the thing that stops you from going to {color=#f6d6bd}Pelt{/color} right away is dragon bones?”')
                $ quintus_left_gate_points_argument_iason_about = 1
                $ custom1 = "“I mean, that’s a pretty {i}big{/i} thing. In the North, everyone looks after themselves. The hunters may be my friends, but I won’t beg them for help.”"
                $ quintus_friendswithdalit += 1
                jump quintus_left_gate_about03
            'I could ask the innkeep to let him stay for labor. (disabled)' if quintus_left_gate_points_argument_iason_about and iason_about_workforquintus == 0 and not quintus_left_gate_points_argument_iason:
                pass
            '“{color=#f6d6bd}Iason{/color} will allow you to stay at his inn. You’ll help him as a guard on the walls, but he won’t pay you unless you can {i}prove yourself{/i}.”' if quintus_left_gate_points_argument_iason_about and iason_about_workforquintus == "guard" and not quintus_left_gate_points_argument_iason:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Iason{/color} will allow you to stay at his inn. You’ll help him as a guard on the walls, but he won’t pay you unless you can {i}prove yourself{/i}.”')
                $ quintus_left_gate_points_argument_iason = 1
                $ quintus_left_gate_points += 3
                $ custom1 = "He crosses his arms, still hesitant. “I guess that’s fair... But what before that? Am I to live on oats and water, in rags?”"
                jump quintus_left_gate_about03
            '“{color=#f6d6bd}Iason{/color} will allow you to stay at his inn. He’ll even pay you after you help the hunters on one of the more {i}vicious{/i} trips.”' if quintus_left_gate_points_argument_iason_about and iason_about_workforquintus == "hunter" and not quintus_left_gate_points_argument_iason:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Iason{/color} will allow you to stay at his inn. He’ll even pay you after you help the hunters on one of the more {i}vicious{/i} trips.”')
                $ quintus_left_gate_points_argument_iason = 1
                $ quintus_left_gate_points += 5
                $ custom1 = "He crosses his arms, still hesitant. “Won’t be more risky than this place, and I’d finally have time to rest a bit... But what before that? Am I to live on oats and water, in rags?”"
                jump quintus_left_gate_about03
            '“If you’re really this desperate for coins, I could spare you a few, enough for you to get comfortable at the inn.”' if quintus_left_gate_points_argument_iason and not quintus_left_gate_points_argument_coins and not quintus_left_gate_points_argument_coins_threshold:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you’re really this desperate for coins, I could spare you a few, enough for you to get comfortable at the inn.”')
                $ quintus_left_gate_points_argument_coins_threshold = (quintus_left_gate_points_threshold-((quintus_friendship/2)+quintus_left_gate_points))
                if quintus_left_gate_points_argument_coins_threshold < 5:
                    $ quintus_left_gate_points_argument_coins_threshold = 5
                $ custom1 = "He steps away. “Ye already helped me quite a bit... I can’t ask ye for that.”"
                jump quintus_left_gate_about03
            '“Here, take [quintus_left_gate_points_argument_coins_threshold] dragons and head to the inn.”' if quintus_left_gate_points_argument_coins_threshold and not quintus_left_gate_points_argument_coins and coins >= quintus_left_gate_points_argument_coins_threshold:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here, take %s dragons and head to the inn.”' %quintus_left_gate_points_argument_coins_threshold)
                $ coins -= quintus_left_gate_points_argument_coins_threshold
                show screen notifyimage( "-%s" %quintus_left_gate_points_argument_coins_threshold, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s {image=cointest}{/i}' %quintus_left_gate_points_threshold)
                $ quintus_left_gate_points_argument_coins = 1
                $ quintus_left_gate_points = quintus_left_gate_points_threshold
                $ custom1 = "After a long pause, he gives you a grateful nod. “Fine. I’ll gather my things, leave the gate open, and get moving tomorrow morning. I paid enough blood for my duty,” a long pause, “but I’m now in ya debt, and I’m ready to enter the woods to repay it. Find me in the inn if ye ever need my help.”"
                $ custom2 = ""
                jump quintus_left_gate_about04
            'I’d need to pay him at least [quintus_left_gate_points_argument_coins_threshold] coins to make him head to the inn. Maybe I could make him trust me some more. (disabled)' if quintus_left_gate_points_argument_coins_threshold and not quintus_left_gate_points_argument_coins and coins < quintus_left_gate_points_argument_coins_threshold:
                pass
            '“Let’s return to this later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s return to this later.”')
                jump westgateafterinteraction01

    label quintus_left_gate_about02alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About your {i}duty{/i}...”')
        $ custom1 = "“What’s there to say?”"
        jump quintus_left_gate_about03

    label quintus_left_gate_about03:
        if (quintus_friendship+quintus_left_gate_points) >= quintus_left_gate_points_threshold:
            $ custom2 = "\n\nAfter a long pause, he lets out a weak sigh. “Fine. I’ll gather my things, leave the gate open, and get moving tomorrow morning. I paid enough blood for my duty,” a long pause, “but I’m now in ya debt, and I’m ready to enter the woods to repay it. Find me in the inn if ye ever need my help.”"
            jump quintus_left_gate_about04
        if quintus_left_gate_points_argument_coins_threshold:
            $ quintus_left_gate_points_argument_coins_threshold = (quintus_left_gate_points_threshold-((quintus_friendship/2)+quintus_left_gate_points))
            if quintus_left_gate_points_argument_coins_threshold < 5:
                $ quintus_left_gate_points_argument_coins_threshold = 5
        menu:
            '[custom1]
            '
            '“The woods are going to get even more dangerous. There’s a swarm of undead, just north of here.”' if whitemarshes_destroyed and not quintus_left_gate_points_argument_nomoreundead:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The woods are going to get even more dangerous. There’s a swarm of undead, just north of here.”')
                $ quintus_left_gate_points_argument_nomoreundead = 1
                $ quintus_left_gate_points += 5
                $ custom1 = "“Eh? What {i}undead{/i}? Empty ones?” He looks toward the bogs, as if a group of monsters was just about to jump upon you from the top of the scarp.\n\nYou share what may be of use to him, without putting too much of an emphasis on your role in the village’s collapse. “Those bark-eating wretches, choked by their own spells,” he spits on the ground. “I really can’t stay here much longer.”"
                jump quintus_left_gate_about03
            '“The people of {color=#f6d6bd}Gale Rocks{/color} are not going to support {color=#f6d6bd}Glaucia{/color} any longer. Her role in the peninsula will dwindle.”' if quintus_about_bandits == 2 and quest_galerockssupport == 2 and not quintus_left_gate_points_argument_glauciadefeated:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The people of {color=#f6d6bd}Gale Rocks{/color} are not going to support {color=#f6d6bd}Glaucia{/color} any longer. Her role in the peninsula will dwindle.”')
                $ quintus_left_gate_points_argument_glauciadefeated = 1
                $ quintus_left_gate_points += 1
                $ quintus_friendship += 2
                $ custom1 = "He looks around and reaches toward his bandage, raising it like a mask. “Did... ye do this?” You start to explain, and his voice lowers to a whisper. “Don’t bother, I don’t follow all this anyway. All I need to say is that this land {i}needed{/i} someone like ye.”"
                jump quintus_left_gate_about03
            '“I’ve entered the woods many times already, and you can trust me - the creatures there are beyond any human.”' if shortcut_traveled >= 3 and not quintus_left_gate_points_argument_shortcut:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve entered the woods many times already, and you can trust me - the creatures there are beyond any human.”')
                $ quintus_left_gate_points_argument_shortcut = 1
                $ quintus_left_gate_points += 3
                $ custom1 = "The longer he listens to your tale, the more his shoulder slump. “Thanks for throwing food at my nightmares. I heard monstrous throats before, but I hoped they would stay, I don’t know, {i}away{/i}.”"
                $ minutes += 5
                jump quintus_left_gate_about03
            '“Don’t you miss fresh, warm food? Rations lose their charm quickly.”' if quintus_food_delivered_amount >= 1 and not quintus_left_gate_points_argument_food:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t you miss fresh, warm food? Rations lose their charm quickly.”')
                $ quintus_left_gate_points_argument_food = 1
                $ quintus_left_gate_points += 2
                $ custom1 = "He lets out a hiss and raises his chin proudly, but after another breath he licks his lips."
                jump quintus_left_gate_about03
            '“Maybe you don’t need shelter for winter, just autumn. The tribe of {color=#f6d6bd}Gale Rocks{/color} delivered supplies to your home. You won’t starve there.”' if oldpagos_plague_helpfromgalerocks >= 2 and not quintus_left_gate_points_argument_oldpagoshelp:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Maybe you don’t need shelter for winter, just autumn. The tribe of {color=#f6d6bd}Gale Rocks{/color} delivered supplies to your home. You won’t starve there.”')
                $ quintus_left_gate_points_argument_oldpagoshelp = 1
                $ quintus_left_gate_points += 3
                $ custom1 = "He bursts into laughter. “Great, great! Those are the last people I would expect this from! Maybe beside {color=#f6d6bd}Howler’s{/color},” he makes a wide grin."
                jump quintus_left_gate_about03
            '“So the thing that stops you from going to {color=#f6d6bd}Pelt{/color} right away is dragon bones?”' if not quintus_left_gate_points_argument_iason_about:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So the thing that stops you from going to {color=#f6d6bd}Pelt{/color} right away is dragon bones?”')
                $ quintus_left_gate_points_argument_iason_about = 1
                $ custom1 = "“I mean, that’s a pretty {i}big{/i} thing. In the North, everyone looks after themselves. The hunters may be my friends, but I won’t beg them for help.”"
                $ quintus_friendswithdalit += 1
                jump quintus_left_gate_about03
            'I could ask the innkeep to let him stay for labor. (disabled)' if quintus_left_gate_points_argument_iason_about and iason_about_workforquintus == 0 and not quintus_left_gate_points_argument_iason:
                pass
            '“{color=#f6d6bd}Iason{/color} will allow you to stay at his inn. You’ll help him as a guard on the walls, but he won’t pay you unless you can {i}prove yourself{/i}.”' if quintus_left_gate_points_argument_iason_about and iason_about_workforquintus == "guard" and not quintus_left_gate_points_argument_iason:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Iason{/color} will allow you to stay at his inn. You’ll help him as a guard on the walls, but he won’t pay you unless you can {i}prove yourself{/i}.”')
                $ quintus_left_gate_points_argument_iason = 1
                $ quintus_left_gate_points += 3
                $ custom1 = "He crosses his arms, still hesitant. “I guess that’s fair... But what before that? Am I to live on oats and water, in rags?”"
                jump quintus_left_gate_about03
            '“{color=#f6d6bd}Iason{/color} will allow you to stay at his inn. He’ll even pay you after you help the hunters on one of the more {i}vicious{/i} trips.”' if quintus_left_gate_points_argument_iason_about and iason_about_workforquintus == "hunter" and not quintus_left_gate_points_argument_iason:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Iason{/color} will allow you to stay at his inn. He’ll even pay you after you help the hunters on one of the more {i}vicious{/i} trips.”')
                $ quintus_left_gate_points_argument_iason = 1
                $ quintus_left_gate_points += 5
                $ custom1 = "He crosses his arms, still hesitant. “Won’t be more risky than this place, and I’d finally have time to rest a bit... But what before that? Am I to live on oats and water, in rags?”"
                jump quintus_left_gate_about03
            '“If you’re really this desperate for coins, I could spare you a few, enough for you to get comfortable at the inn.”' if quintus_left_gate_points_argument_iason and not quintus_left_gate_points_argument_coins and not quintus_left_gate_points_argument_coins_threshold:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “If you’re really this desperate for coins, I could spare you a few, enough for you to get comfortable at the inn.”')
                $ quintus_left_gate_points_argument_coins_threshold = (quintus_left_gate_points_threshold-((quintus_friendship/2)+quintus_left_gate_points))
                if quintus_left_gate_points_argument_coins_threshold < 5:
                    $ quintus_left_gate_points_argument_coins_threshold = 5
                $ custom1 = "He steps away. “Ye already helped me quite a bit... I can’t ask ye for that.”"
                jump quintus_left_gate_about03
            '“Here, take [quintus_left_gate_points_argument_coins_threshold] dragons and head to the inn.”' if quintus_left_gate_points_argument_coins_threshold and not quintus_left_gate_points_argument_coins and coins >= quintus_left_gate_points_argument_coins_threshold:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Here, take %s dragons and head to the inn.”' %quintus_left_gate_points_argument_coins_threshold)
                $ coins -= quintus_left_gate_points_argument_coins_threshold
                show screen notifyimage( "-%s" %quintus_left_gate_points_argument_coins_threshold, "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-%s {image=cointest}{/i}' %quintus_left_gate_points_threshold)
                $ quintus_left_gate_points_argument_coins = 1
                $ quintus_left_gate_points = quintus_left_gate_points_threshold
                $ custom1 = "After a long pause, he gives you a grateful nod. “Fine. I’ll gather my things, leave the gate open, and get moving tomorrow morning. I paid enough blood for my duty,” a long pause, “but I’m now in ya debt, and I’m ready to enter the woods to repay it. Find me in the inn if ye ever need my help.”"
                $ custom2 = ""
                jump quintus_left_gate_about04
            'I’d need to pay him at least [quintus_left_gate_points_argument_coins_threshold] coins to make him head to the inn. Maybe I could make him trust me some more. (disabled)' if quintus_left_gate_points_argument_coins_threshold and not quintus_left_gate_points_argument_coins and coins < quintus_left_gate_points_argument_coins_threshold:
                pass
            '“Let’s return to this later.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s return to this later.”')
                jump westgateafterinteraction01

    label quintus_left_gate_about04:
        $ quintus_left_gate = day
        if pc_goal == "iwanttohelp":
            $ pc_goal_iwanttohelppoints += 1
        $ westgate_open = 1
        $ quintus_friendship += 2
        if quest_fetchingfood == 1:
            $ quest_fetchingfood = 2
        menu:
            '[custom1][custom2]
            '
            '“I appreciate it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I appreciate it.”')
                $ custom1 = "He gives you a warm smile."
                jump quintus_left_gate_about05
            '“Do you want me to escort you?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you want me to escort you?”')
                $ custom1 = "“Nah, no need! I’ll stay away from the cursed tree and the ruins, through paths ye won’t follow on a horse. Thanks, though.”"
                jump quintus_left_gate_about05

    label quintus_left_gate_about05:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if quest_fetchingfood == 1:
            $ renpy.notify("Quest completed: Fetching Food")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: Fetching Food{/i}')
        $ questionpreset = "quintus1"
        menu:
            '[custom1]
            '
            '(quintus1 set)':
                pass

################################################################# Quintus in Pelt

label peltnorth01insidetalkingwithquintusALL:
    label peltnorth01insidetalkingwithquintus01:
        $ quintus_peltnorthintroduction = renpy.random.choice(['“How are ye, warden?”', '“Warden.”', '“It’s getting cold outside, eh?”', 'He greets ye by raising an empty mug.', '“Here on duty?”'])
        $ questionpreset = "quintus2"
        menu:
            '[quintus_peltnorthintroduction]
            '
            '(quintus2 preset)':
                pass

    label pelt_westgateaboutcuredplague01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bring good news from {color=#f6d6bd}Old Págos{/color}. The plague is no more.”')
        $ quintus_about_plague_cured = 1
        $ quintus_friendship += 5
        if quintus_friendship < 5:
            $ quintus_friendship = 5
        $ minutes += 5
        $ can_items = 1
        $ questionpreset = "quintus2"
        menu:
            '“What?” He leans back. “Say again?” When you repeat, he tilts his head back and puts hands on his waist, bursting in laughter. His voice got stronger. “Tell me all!”
            \n\nHe has little patience, constantly throwing more questions at you - about the druid, his plan, your gifts for the “magic tree.” He’s far from happy when he hears about the prolonged seclusion. “I guess it’s fair. I’ll stay here for some more time. I don’t want to mess stuff up, like, I’m not as dumb as a bird.”
            \n\nHe smiles again. “Thank ye, warden, ya soul carries duty like no other.”
            '
            '(quintus2 preset)':
                pass

    label pelt_westgateaboutasterion01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for {color=#f6d6bd}Asterion{/color}.”')
        $ quintus_about_asterion = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '“That’s nice, but he hasn’t been at the gate in many days. Ye sure he’s not dead?”
            \n\nAfter you admit that he very much may be, he puts a hand on his waist. “Well, better get ready to slit open every dragon belly in the wilds.”
            '
            '“Did he often travel through the woods?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Did he often travel through the woods?”')
                menu:
                    '“Sure, though on a different mount. He had a saurian, four ibexes long, two ibexes tall. It moves on four legs, and jumps high and far. It’s dark green, like rotting leaves. That one time, I was taking a piss in the shrubs, and {color=#f6d6bd}Asterion{/color} made the beast run up the rock face, and it jumped {i}onto{/i} it...” He looks around, then points at the stairs. “And like, they ran {i}above{/i} the wall, and landed on the other side, just like that!” He snaps his fingers, his voice and eyes gain new vigor.
                    '
                    '“You say the saurian was large and green?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You say the saurian was large and green?”')
                        if not quest_asterion_description07:
                            $ quest_asterion_description07 = "I’ve heard a more detailed description of Asterion’s {color=#f6d6bd}saurian{/color}. It’s larger than a horse, dark green, though the edges of its limbs, tail, and eyebrows are red-and-orange."
                        if not description_asterion08 and quest_asterion == 1:
                            $ description_asterion08 = "I’ve heard a more detailed description of Asterion’s {color=#f6d6bd}saurian{/color}. It’s larger than a horse, dark green, though the edges of its limbs, tail, and eyebrows are red-and-orange."
                            $ renpy.notify("Journal updated: Find the Roadwarden")
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Find the Roadwarden{/i}')
                        $ questionpreset = "quintus2"
                        $ can_items = 1
                        $ minutes += 5
                        menu:
                            '“I mean, not everywhere.” He points at his eyebrows. “He has red scales here, and on the tail, and... {i}Shoulders{/i}, I think. I don’t know what to call it.”
                            \n\nYou ask him for a bit about {color=#f6d6bd}Asterion{/color}, but he has little to add. “There used to be six of us, keepers. I saw him every now and then, but not that often.”
                            '
                            '(quintus2 preset)':
                                pass

    label pelt_westgateaboutrecruitahunter01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever met {color=#f6d6bd}Erastos{/color}?”')
        $ quest_recruitahunter_spokento_quintus = 1
        $ questionpreset = "quintus2"
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '“Nah. I remember him trading with my neighbors once or twice, but I never spoke with him. A bit of a wimp.”
            '
            '(quintus1 preset)':
                pass

    label pelt_westgateaboutshortcut01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What can you tell me about the road behind the gate?”')
        $ quintus_about_shortcut = 1
        $ minutes += 5
        $ questionpreset = "quintus2"
        $ can_items = 1
        $ description_shortcut03 = "The locals claim that this place is abandoned, neglected, and unusually dangerous."
        menu:
            '“Oh, not much.” His chuckle turns into a cough. “It leads through lowlands, mostly woods and some ponds. It’s dark, and lethal.”
            \n\nHe mentions tales of ghosts, dragons, fogs, and blood mages, but whenever you ask about any creature in particular, his response is vague and brief.
            \n\n“The tribes abandoned that path. Ever since the war, the trade has been slow. People refused to patrol it. The plants are getting taller, but for at least a few more seasons it’s still a shortcut. It’s good that ye have a mount. If aught chases ye, always stay close to the paths, and ride as fast as ye can.”
            '
            '(quintus2 preset)':
                pass

    label pelt_westgateabouthighisland01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever heard about {color=#f6d6bd}High Island{/color}?”')
        $ can_items = 1
        $ quintus_about_highisland = 1
        $ questionpreset = "quintus2"
        menu:
            '“Eh? I heard, alright, ye can see its volcano from {color=#f6d6bd}Old Págos{/color}. The monks said it’s a weird place, but also {i}a tale for the worthy{/i}.”
            \n\nYou ask him if he knows this “tale”, and he glances in the direction of his home. “Nah.”
            '
            '(quintus2 preset)':
                pass

    label pelt_westgateabouthighisland_recruitment01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need you to return the favor. I’m heading for {color=#f6d6bd}High Island{/color}.”')
        $ can_items = 1
        $ quintus_about_highisland_recruitment = 1
        $ quintus_about_highisland_recruitment_done = 1
        $ questionpreset = "quintus2"
        menu:
            'He squints his eyes, the bandages almost fall off his face. “Pulling me back in, eh? Well, as long as it’s not just the two of us. I’ll prepare my stuff, just tell me when you’re ready.”
            '
            '(quintus2 preset)':
                pass

    label pelt_westgateaboutmissinghunters01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Some time ago, a few people from {color=#f6d6bd}Creeks{/color} left their home to hunt. Have you met them?”')
        $ can_items = 1
        $ quintus_about_missinghunters = 1
        $ quest_missinghunters_vaschelknown = 1
        $ questionpreset = "quintus2"
        menu:
            '“I know naught about {i}people{/i}, but I met {color=#f6d6bd}Vaschel{/color}.” It takes him a few breaths to notice you’re waiting for him to go on. “They spent one night at this tower with me! Came from the east, and then went back there. They were building a trap. Somewhere behind the lake? They shared a partridge with me, but never came here again. Good soul, very... {i}open-eyed{/i}.”
            '
            '(quintus2 preset)':
                pass

    label pelt_westgateaboutvascheldead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think {color=#f6d6bd}Vaschel’s{/color} died somewhere at the heart of the woods.”')
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ quintus_about_vaschel = 1
        $ quintus_left_gate_points += 2
        $ quintus_friendship += 1
        $ questionpreset = "quintus2"
        menu:
            '“Shit,” he starts, but then nods with acceptance. “Too bad. I’d rather have more strong hunters around.”
            '
            '(quintus2 preset)':
                pass

    label pelt_westgateaboutoldpagos01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s it like to live in {color=#f6d6bd}Old Págos{/color}?”')
        $ quintus_about_oldpagos = 1
        $ questionpreset = "quintus2"
        $ can_items = 1
        $ description_oldpagos00 = "According to {color=#f6d6bd}Quintus{/color}, {i}Págos{/i} means {i}Hill{/i}. He seems to be proud of his home."
        menu:
            'He opens his mouth, giving you a puzzled look, then lets out a weak chuckle. “What am I to say? We’ve got rocks,” he taps the wall, “and make houses, bowls, tools. We sell them, too. We grow oats and broad beans. ibexes give us wool, and skins for monks, what do ye call it, the one ye write on?” He moves on when you mention {i}parchment{/i}. “Yeah, yeah. It’s a good place, beautiful, old. {i}Hill{/i}, that’s what {i}Págos{/i} means. {color=#f6d6bd}Old Hill{/color}.”
            \n\nWhen you bring up the monastery, his eyes get brighter. “Good people! They came here on a mission, teaching us Wright’s book. My grandparents were pagans, ye know? But we now follow the River of Truth. We keep to ourselves, but help others when they need us.”
            '
            '(quintus2 preset)':
                pass

    label pelt_westgateaboutbanditsALL:
        label pelt_westgateaboutbandits01:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Are they bothering you?”')
            $ quintus_about_bandits = 1
            $ questionpreset = "quintus2"
            $ can_items = 1
            menu:
                'He scratches the bandage on his cheek. “I... only know there’s one band, somewhere. But not around, I never saw them.”
                '
                '(quintus2 preset)':
                    pass

        label pelt_westgateaboutbandits02:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why are you afraid of {color=#f6d6bd}Glaucia{/color}?”')
            if (quintus_friendship+appearance_charisma) < 4:
                $ questionpreset = "quintus2"
                $ can_items = 1
                $ quintus_about_bandits_gray = 1
                menu:
                    'His straightens up and gives you a long look. “I don’t know who yer talking about.”
                    '
                    '(quintus2 preset)':
                        pass
            else:
                $ quintus_about_bandits = 2
                $ questionpreset = "quintus2"
                $ can_items = 1
                $ description_glaucia07 = "{color=#f6d6bd}Quintus{/color}, the gatekeeper, claims that she’s the one who forced him to stay on his post."
                menu:
                    '“Warden, I... I can’t talk about her.” His shoulders slump, making him look like a wounded troll. “{i}I’ve got to{/i} look after the gate for her, or she’ll hurt someone... Important to me. If she learns I’m telling stories about her, I’m dead, too.”
                    '
                    '(quintus2 preset)':
                        pass

    label pelt_westgateaboutibex01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Any idea who could be the owner of an ibex marked with a red knot?”')
        $ quintus_about_ibex = 1
        $ questionpreset = "quintus2"
        $ can_items = 1
        menu:
            'He flinches and narrows his eyes. “A red knot? We use those in my home. Like, not {i}my{/i}, but {color=#f6d6bd}Old Págos{/color}.”
            '
            '(quintus2 preset)':
                pass

#################################################################
label westgate_noquintusALL:
    label westgate_noquintus01:
        if not westgate_open:
            $ westgate_open = 1
        menu:
            '[westgate_fluff]
            '
            'I climb up the wall and look for a spot where I could place a bronze rod.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_westgate:
                jump westgate_noquintus_bronzerod
            'I enter the woods.' ( condition="quarters <= (world_daylength-12)" ):
                jump westgate_noquintus_enteringshortcut
            'I shouldn’t enter the woods at such late hour. (disabled)' ( condition="quarters > (world_daylength-12)" ):
                pass

    label westgate_noquintus_bronzerod:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb up the wall and look for a spot where I could place a bronze rod.')
        $ renpy.notify("Journal updated: Bronze Rods")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Bronze Rods{/i}')
        $ eudocia_bronzerod_rodin_westgate = 1
        $ item_bronzerod -= 1
        $ eudocia_bronzerod_installed += 1
        if not item_bronzerod:
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
                    $ quest_bronzerod_description04 = "I’ve placed at least four rods. I can return to collect a part of my reward."
                    $ quest_bronzerod_description02 = 0
        if item_bonehook: # ropehook, another ropehook - można zdobyć linę
            $ custom1 = "Thanks to your bone hook, you climb up the wall quickly and find a convenient spot -"
            $ quarters += 1
        else:
            $ custom1 = "Having no proper tools, climbing up the wall takes a few attempts, and you finally reach it through the shrubs. Nevertheless, you find a convenient spot quickly -"
            $ quarters += 3
        if eudocia_bronzerod_rodin_westgate:
            show areapicture westgatewest01bronzerod at basicfade behind westgatenobar
        else:
            show areapicture westgatewest01 at basicfade behind westgatenobar
        show westgatenobar at basicfade
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        menu:
            '[custom1] a crack between two bricks - and get back on the ground swiftly.
            '
            'I climb up the wall and look for a spot where I could place a bronze rod.' if quest_bronzerod == 1 and item_bronzerod and not eudocia_bronzerod_rodin_westgate:
                jump westgate_noquintus_bronzerod
            'I enter the woods.' ( condition="quarters <= (world_daylength-12)" ):
                jump westgate_noquintus_enteringshortcut
            'I shouldn’t enter the woods at such late hour. (disabled)' ( condition="quarters > (world_daylength-12)" ):
                pass

    label westgate_noquintus_enteringshortcut:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the woods.')
        $ shortcut_inprogress = 1
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'With the gate unlocked on both sides, it takes little effort.
            '
            'I travel as far {color=#f6d6bd}east{/color} as I can.' if not stonesign_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel as far {color=#f6d6bd}east{/color} as I can.')
                $ questionpreset = 0
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "stonesign"
                jump shortcut01
            'I travel to the other {color=#f6d6bd}edge of the woodland{/color}.' if stonesign_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I travel to the other {color=#f6d6bd}edge of the woodland{/color}.')
                $ questionpreset = 0
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "stonesign"
                jump shortcut01
            'I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.' if shortcut_cairn_firsttime:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the cairn{/color} in the middle of the forest.')
                $ questionpreset = 0
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "cairn"
                jump shortcut01
            'I return to {color=#f6d6bd}the bandits’ hideout{/color}.' if banditshideout_firsttime and not banditshideout_banned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to {color=#f6d6bd}the bandits’ hideout{/color}.')
                $ questionpreset = 0
                $ shortcut_traveled += 1
                $ travel_destination_shortcut = "hideout"
                jump shortcut01
            'I step away.' if banditshideout_firsttime and not banditshideout_banned:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                $ questionpreset = 0
                $ shortcut_inprogress = 0
                $ can_leave = 1
                $ can_rest = 1
                $ can_items = 1
                jump westgate_noquintus01
