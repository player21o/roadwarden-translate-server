###################### {color=#f6d6bd}Aegidia{/color}
default aegidia_alive = 1
default aegidia_firsttime = 0
default aegidia_dayofvisit = 0
default aegidia_friendship = 0
default aegidia_bow = 0
default aegidia_crossbow = 0
default aegidia_name = 0

default aegidia_about_highisland_recruitment = 0
default aegidia_about_highisland_recruitment_done = 0
default aegidia_highisland_joined = 0
default aegidia_about_asterion_found = 0

default aegidia_about_hamlet = 0
default aegidia_about_peninsula = 0
default aegidia_about_asterion = 0
default aegidia_about_asterion_gray = 0
default aegidia_about_herself = 0
default aegidia_about_boat = 0
default aegidia_about_necklace1 = 0
default aegidia_about_necklace2 = 0
default aegidia_about_resting = 0
default aegidia_about_survival = 0
default aegidia_about_payment = 0
default aegidia_about_whatshewants = 0
default aegidia_about_thais = 0
default aegidia_about_arrow = 0
default aegidia_about_fishtrap1 = 0
default aegidia_about_fishtrap2 = 0
default aegidia_about_shortcut = 0
default aegidia_about_highisland = 0
default aegidia_about_steephouse = 0
default aegidia_about_steephouse_truth = 0
default aegidia_about_nomoreundead = 0

default aegidia_about_hamletalone = 0
default aegidia_about_hamletalone_doubt01 = 0
default aegidia_about_hamletalone_doubt02 = 0
default aegidia_about_hamletalone_doubt03 = 0
default aegidia_favor = 0

label fishinghamletaegidiafirsttimeALL:
    label fishinghamletdiscoveringscrap06:
        show fishinghamletscrap06 at basicfade
        $ fishinghamlet_areas_seen_06 = 1
        $ fishinghamlet_areas_seen += 1
        $ minutes += 5
        $ aegidia_firsttime = 1
        $ world_known_npcs += 1
        label fishinghamletdiscoveringscrap06after:
            menu:
                'The roaring ocean overwhelms the whimper of soggy, broken beams. The huts would take a lot of work, but are not beyond restoration - especially the one in the center, whose simple roof has managed to protect its walls. By its open entrance, you spot a bucket of water, as well as boot prints.
                '
                '“Anyone here? I don’t want to hurt you!”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Anyone here? I don’t want to hurt you!”')
                    if aegidia_crossbow:
                        menu:
                            'The strong voice of a young woman reaches you from the building in front of you.
                            \n\n“If so, maybe put down that crossbow, aye?”
                            '
                            '“Fine!” I put it on the ground. “Let me see you!”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine!” I put it on the ground. “Let me see you!”')
                                $ aegidia_crossbow = 0
                                $ aegidia_friendship += 1
                                jump fishinghamletdiscoveringscrap06aegidiahasnobow
                            '“As long as you don’t give me a reason to shoot, you’re safe!”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “As long as you don’t give me a reason to shoot, you’re safe!”')
                                $ aegidia_bow = 1
                                jump fishinghamletdiscoveringscrap06aegidia_bow
                    else:
                        $ aegidia_friendship += 1
                        jump fishinghamletdiscoveringscrap06aegidiahasnobow
                '“Come out before I find you first!”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Come out before I find you first!”')
                    $ aegidia_bow = 1
                    jump fishinghamletdiscoveringscrap06aegidia_bow

    label fishinghamletdiscoveringscrap06aegidiahasnobow: #ma łuk w ręce, zwieszony u boku
        $ custom1 = ""
        menu:
            'After a few breaths, the tall and slim woman steps onto the threshold. Her strung longbow is resting against her hip, and you spot the arrow quills sticking out from the quiver. She’s standing sideways to you, ready to take a shooting stance. This, combined with her raised chin, gives her a proud, confident look.
            \n\nIf she’s a traveler, it’s unusual that she carries no major scars, bruises, or wounds. She’s tanned, with flaxen curly hair that is too short to reach her shoulders. It’s disorderly, and of uneven length, most likely cut with a dagger. Her upper lip is unusually large.
            '
            'A thief, most likely.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- A thief, most likely.')
                jump fishinghamletdiscoveringscrap06aegidia_bowb
            'A runaway slave?':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- A runaway slave?')
                jump fishinghamletdiscoveringscrap06aegidia_bowb
            'Maybe she’s a big-game huntress.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe she’s a big-game huntress.')
                label fishinghamletdiscoveringscrap06aegidia_bowb:
                    $ at_activate = 1
                    $ at = 0
                    menu:
                        'Her worn, baggy tunic has no sleeves, and her legs are uncovered, showing how impeccably clean her skin is. She observes you keenly, but her sparkling, curious hazel eyes carry no anger.
                        '
                        ' (disabled)' ( condition="at == 0" ):
                            pass
                        '“I’m sorry to disturb your peace. Can we talk?”' ( condition="at == 'friendly'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sorry to disturb your peace. Can we talk?”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletdiscoveringscrap06seesherfriendly
                        '“I hope you’re not looking for target practice!”' ( condition="at == 'playful'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I hope you’re not looking for target practice!”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletdiscoveringscrap06seesherplayful
                        '“I didn’t expect to find someone in these ruins.”' ( condition="at == 'distanced'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t expect to find someone in these ruins.”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletdiscoveringscrap06seesherdistanced
                        '“Keep that bow away. I’m not in the mood for bloodshed.”' ( condition="at == 'intimidating'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Keep that bow away. I’m not in the mood for bloodshed.”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletdiscoveringscrap06seesherintimidating
                        'I point my crossbow at the ground. “I’m not your enemy.”' ( condition="at == 'vulnerable' and aegidia_crossbow == 1" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I point my crossbow at the ground. “I’m not your enemy.”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletdiscoveringscrap06seeshervulnerable
                        'I raise my hands. “I yield.”' ( condition="at == 'vulnerable' and not aegidia_crossbow" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise my hands. “I yield.”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletdiscoveringscrap06seeshervulnerable

    label fishinghamletdiscoveringscrap06aegidia_bow: #ma naciągnięty, gotowa, by zabić
        $ renpy.save("combatsave", extra_info='Combat Auto Save')
        $ custom1 = "She lowers her weapon, keeping it in front of her. "
        menu:
            'After a few breaths, the tall and slim woman steps onto the threshold. She’s holding a drawn longbow, and you spot a few more arrow quills sticking out from the quiver. She’s standing sideways to you, ready to take a shooting stance. This, combined with her raised chin, gives her a proud, confident look.
            \n\nIf she’s a traveler, it’s unusual that she carries no major scars, bruises, or wounds. She’s tanned, with flaxen curly hair that is too short to reach her shoulders. It’s disorderly, and of uneven length, most likely cut with a dagger. Her upper lip is unusually large.
            '
            'A thief, most likely.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- A thief, most likely.')
                jump fishinghamletdiscoveringscrap06aegidia_bowa
            'A runaway slave?':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- A runaway slave?')
                jump fishinghamletdiscoveringscrap06aegidia_bowa
            'Maybe she’s a big-game huntress.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Maybe she’s a big-game huntress.')
                label fishinghamletdiscoveringscrap06aegidia_bowa:
                    $ at_activate = 1
                    $ at = 0
                    menu:
                        'Her worn, baggy tunic has no sleeves, and her legs are uncovered, showing how impeccably clean her skin is. She observes you keenly - her sparkling, curious hazel eyes carry a hint of a threat.
                        '
                        ' (disabled)' ( condition="at == 0" ):
                            pass
                        '“I’m sorry to disturb your peace. Can we talk?”' ( condition="at == 'friendly'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m sorry to disturb your peace. Can we talk?”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletdiscoveringscrap06seesherfriendly
                        '“I hope you’re not looking for target practice!”' ( condition="at == 'playful'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I hope you’re not looking for target practice!”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletdiscoveringscrap06seesherplayful
                        '“I didn’t expect to find someone in these ruins.”' ( condition="at == 'distanced'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I didn’t expect to find someone in these ruins.”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletdiscoveringscrap06seesherdistanced
                        '“I’m going to count to three. After that, you better lower that damn bow, or else.”' ( condition="at == 'intimidating'" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m going to count to three. After that, you better lower that damn bow, or else.”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletgameover
                        'I point my crossbow at the ground. “I’m not your enemy.”' ( condition="at == 'vulnerable' and aegidia_crossbow" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I point my crossbow at the ground. “I’m not your enemy.”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletdiscoveringscrap06seeshervulnerable
                        'I raise my hands. “I yield.”' ( condition="at == 'vulnerable' and not aegidia_crossbow" ):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I raise my hands. “I yield.”')
                            $ at_activate = 0
                            $ at = 0
                            $ at_unlock_force = 0
                            jump fishinghamletdiscoveringscrap06seeshervulnerable

    label fishinghamletgameover:
        $ pc_hp = 0
        show minus5hp at hpchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-5 vitality points.{/i}')
        if pc_religion == "pagan":
            show areapicture gameover_alt at basicfade
        else:
            show areapicture gameover at basicfade
        menu:
            'She releases the string and the arrow shatters your teeth. You fall on your shoulder without even opening your clenched fists, the woman screams in shock. You can taste wood.
            \n
            \n\n[pcname]’s soul has left its shell.
            '
            'Let me replay this conversation.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let me replay this conversation.')
                stop music fadeout 4.0
                $ renpy.load("combatsave")

    label fishinghamletdiscoveringscrap06seesherfriendly: # “I’m sorry to disturb your peace. Can we talk?”
        $ questionpreset = "aegidia1"
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "audio/weloveindies_vastlands_hamletloop.ogg":
            play music "audio/weloveindies_vastlands_hamletloop.ogg" fadeout 1.0 fadein 0.0
        menu:
            'She bites her lower lip and glances at {color=#f6d6bd}[horsename]{/color}. [custom1]“About what? You think I came here to find new neighbors?”
            '
            '(aegidia1 set)':
                pass

    label fishinghamletdiscoveringscrap06seesherplayful: # “I hope you’re not looking for target practice!”
        $ questionpreset = "aegidia1"
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "audio/weloveindies_vastlands_hamletloop.ogg":
            play music "audio/weloveindies_vastlands_hamletloop.ogg" fadeout 1.0 fadein 0.0
        menu:
            '“I...” she takes a deep breath and bites her lower lip, then looks at {color=#f6d6bd}[horsename]{/color}. [custom1]“I need nea toys to play with. I’ve hunting to do anyway.”
            '
            '(aegidia1 set)':
                pass

    label fishinghamletdiscoveringscrap06seesherdistanced: # “I didn’t expect to find someone in these ruins.”
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "audio/weloveindies_vastlands_hamletloop.ogg":
            play music "audio/weloveindies_vastlands_hamletloop.ogg" fadeout 1.0 fadein 0.0
        menu:
            '“I’m ne just {i}someone{/i},” she raises her shoulders. “‘Tis ma home, en I do ne plan to share it. What are you doing here?”[custom1]
            '
            '“The people of {color=#f6d6bd}Howler’s Dell{/color} want me to check on this place. It belongs to them.”' if quest_fisherhamlet and not aegidia_about_hamlet:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The people of {color=#f6d6bd}Howler’s Dell{/color} want me to check on this place. It belongs to them.”')
                jump fishinghamletaegidiapcabouthamlet01after
            '“I’m a roadwarden. I need to learn more about this land.”' if quest_explorepeninsula and not aegidia_about_peninsula:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m a roadwarden. I need to learn more about this land.”')
                jump fishinghamletaegidiapcaboutthemself01alt
            '“I’m trying to find {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”' if quest_asterion and not aegidia_about_asterion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to find {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
                jump fishinghamletaegidiapcaboutasterion01after
            '“Nothing. It’s time for me to leave.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Nothing. It’s time for me to leave.”')
                if not aegidia_about_hamlet:
                    jump fishinghamletaegidiapcabouthamlet00
                else:
                    jump fishinghamletselectwheretogover02

    label fishinghamletdiscoveringscrap06seesherintimidating: # “Keep that bow away. I’m not in the mood for bloodshed.”
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "audio/weloveindies_vastlands_hamletloop.ogg":
            play music "audio/weloveindies_vastlands_hamletloop.ogg" fadeout 1.0 fadein 0.0
        $ aegidia_friendship -= 1
        $ questionpreset = "aegidia1"
        menu:
            '“Do ne try to scare me. I was belt-high when I shot my first rabbit. I’m ne scared of your jacket. I’ll hit your bloody eye.” She bites her lower lip and says nothing more.
            '
            '(aegidia1 set)':
                pass

    label fishinghamletdiscoveringscrap06seeshervulnerable: # I point my crossbow at the ground. “I’m not your enemy.” / I raise my hands. “I yield.”
        $ aegidia_friendship += 1
        $ aegidia_crossbow = 0
        stop nature fadeout 4.0
        if not renpy.music.get_playing(channel='music') == "audio/weloveindies_vastlands_hamletloop.ogg":
            play music "audio/weloveindies_vastlands_hamletloop.ogg" fadeout 1.0 fadein 0.0
        menu:
            'She tilts her head to the right, bites her upper lip, and returns the arrow to her quiver. “I accept your, well, surrender.”
            \n\nShe takes a few steps forward, stepping barefoot on the sand and suddenly looks around with scared eyes. Once she realizes it’s not a trap after all, she takes a deep breath and points at {color=#f6d6bd}[horsename]{/color}. “‘Tis a horse, is it ne?” She heads in its direction, and your palfrey snorts, shaking its head.
            '
            '“Don’t bother it. It’s not used to this place.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t bother it. It’s not used to this place.”')
                $ questionpreset = "aegidia1"
                menu:
                    'She purses her lips, but nods compliantly. “I wish I had some treat for it!” Her eyes return to you “You are ne here to pay me a visit, aye?”
                    '
                    '(aegidia1 set)':
                        pass
            'I tell {color=#f6d6bd}[horsename]{/color} to relax and show the woman how to pet it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I tell {color=#f6d6bd}%s{/color} to relax and show the woman how to pet it.' %horsename)
                stop nature fadeout 4.0
                $ aegidia_friendship += 1
                $ quarters += 1
                $ questionpreset = "aegidia1"
                menu:
                    'She follows your lead with a wide grin, but then showers you with questions. What does it eat? A male or a female? Is it faster than a deer? Can it kill a wolf? How does it sleep? Can it do any tricks?
                    \n\nAfter some time, you notice that {color=#f6d6bd}[horsename]’s{/color} ears start to flinch, and you explain that you should give it some privacy. The woman obediently leaps away, huffing with enthusiasm. “Sure, sure! What a lovely beast!” She keeps to observe your mount, even though it already walks away from her.
                    '
                    '(aegidia1 set)':
                        pass

label fishinghamletaegidiaregular01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if aegidia_dayofvisit != day:
        $ aegidia_dayofvisit = day
        if aegidia_friendship < 0:
            $ custom1 = "She keenly watches your steps, with one hand held behind her back, as if she’s holding a knife. “Here again?”"
        elif aegidia_friendship < 4:
            $ custom1 = "She’s putting her weight on one leg, keeping a hand on her hip. She greets you with a nod, her eyes are curious."
        else:
            $ custom1 = "She waves at you from a distance, her voice is bright. “Good to see you alive!”"
    else:
        if aegidia_friendship < 0:
            $ custom1 = "She’s busy, but spares you an annoyed glance. “Hm?”"
        elif aegidia_friendship < 4:
            $ custom1 = "She asks you to wait for a bit, but once she’s done with her task, she gives you a kind smile."
        else:
            $ custom1 = "You find her relaxing in a shadow, looking at you with a cheerful smile."
    $ questionpreset = "aegidia1"
    stop nature fadeout 4.0
    if not renpy.music.get_playing(channel='music') == "audio/weloveindies_vastlands_hamletloop.ogg":
        play music "audio/weloveindies_vastlands_hamletloop.ogg" fadeout 1.0 fadein 0.0
    menu:
        '[custom1]
        '
        '(aegidia1 set)':
            pass

label fishinghamletaegidiapcabouthamletALL:
    label fishinghamletaegidiapcabouthamlet01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The people of {color=#f6d6bd}Howler’s Dell{/color} want me to check on this place. It belongs to them.”')
        label fishinghamletaegidiapcabouthamlet01after:
            $ aegidia_about_hamlet = 1
            menu:
                '“Nae, let’s ne trollshit one another. What does {color=#f6d6bd}Thais{/color} want?” Coming from her mouth, {color=#f6d6bd}the mayor’s{/color} name is like a toothache.
                '
                '“Why do you think it’s her?”':
                    label fishinghamletaegidiapcabouthamlet01alt:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why do you think it’s her?”')
                        menu:
                            '“Everyone else has given up on this place, only she still brings it up. If your horse is here, someone helped you with the rocks, en nae farmer would come here without an order.”
                            '
                            '“She wanted me to take a look. See if there are any monsters here.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “She wanted me to take a look. See if there are any monsters here.”')
                                menu:
                                    '“Blood on all of it.” She looks at the gate, lets out a huff, then straightens up and meets your eyes. “She must ne know what you’ve seen,” she points at you with a tip of her bow. “Do ne tell her I’m here. Or better yet, do ne tell her this place is still standing.”
                                    '
                                    '“You’re her daughter. The one {i}slaughtered{/i} by goblins.”' if thais_about_asterion:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You’re her daughter. The one {i}slaughtered{/i} by goblins.”')
                                        jump fishinghamletaegidiapcabouthamlet04a
                                    '“You ask for a lot without offering much.”' if not thais_about_asterion:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- You ask for a lot without offering much.”')
                                        jump fishinghamletaegidiapcabouthamlet04b
                                    '“Explain.”' if not thais_about_asterion:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Explain.”')
                                        jump fishinghamletaegidiapcabouthamlet04c

    label fishinghamletaegidiapcabouthamlet04a: #“You’re her daughter. The one {i}slaughtered{/i} by goblins.”
        $ aegidia_name = 1
        $ aegidia_about_herself = 2
        $ aegidia_friendship += 1
        $ description_aegidia01 = "An adopted daughter of {color=#f6d6bd}Thais{/color} and {color=#f6d6bd}Eryx{/color}. She despises her mother."
        $ quest_fisherhamlet_description04cd = "I met {color=#f6d6bd}Aegidia{/color}, the not-so-dead daughter of {color=#f6d6bd}Thais{/color}. She’s asked me to lie in her name and to talk her mother out of regaining the hamlet."
        $ renpy.notify("Journal updated: The Old Hamlet")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Old Hamlet{/i}')
        $ questionpreset = "aegidia2"
        menu:
            '“Aye, tha’s ma story, en I need it to stay this way. {color=#f6d6bd}Asterion{/color} helped me. Ma m...” Tears well up in her eyes and her brown cheeks blush. Her voice fills up with spite. “{color=#f6d6bd}Thais{/color} takes whatever fits in her talons. She was pushing me into marriage out of spite, to punish me. But I will ne be chained, ne by her, ne by others. I’m a master of the bow, the hunt, en spells of mine. I’ll come back as ma own soul, as {color=#f6d6bd}Aegidia, the archeress{/color}, nae {i}a mayor’s daughter{/i}. And she’ll have nae power over me.”
            '
            '(aegidia2 set)':
                pass

    label fishinghamletaegidiapcabouthamlet04bpre:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What’s in it for me?”')
        label fishinghamletaegidiapcabouthamlet04b: #“You ask for a lot without offering much.”
            $ aegidia_about_payment = 1
            $ questionpreset = "aegidia2"
            menu:
                'She chews on her lower lip and straightens up. “A favor for a favor,” she looks into your eyes. “Keep ma secret en one day I’ll help you back. In the wilderness, ma talents are of great value,” she raises her bow slightly. “One tha’s been able to stay alive all by herself for half a year.”
                '
                '(aegidia2 set)':
                    pass

    label fishinghamletaegidiapcabouthamlet04cpre:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Why do you want the villagers to stay away?”')
        label fishinghamletaegidiapcabouthamlet04c:
            $ aegidia_about_hamletalone = 1
            $ questionpreset = "aegidia2"
            menu:
                'She puts a hand on the tip of her bow and starts to stroke it with her fingers. “I hope {color=#f6d6bd}Howler’s{/color} will prosper, I do. But they already have more than they can eat. I’ll meet with the forest speakers after the first thaw en show them I can handle this place. I’ll be its guardian, live here with ma friends, en ne {color=#f6d6bd}the mayor’s{/color} eye.” She steps closer to you, the corners of her eyes are turning red. “I {i}need{/i} it, more than {i}they{/i} need some fish.”
                '
                '(aegidia2 set)':
                    pass

    label fishinghamletaegidiapcabouthamlet04d:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Who are you, exactly?”')
        $ aegidia_about_herself = 2
        $ aegidia_name = 1
        menu:
            'She looks around, lowering her voice. “You do ne need to know.”
            '
            '“I can just tell the others I’ve seen you, you know. Your name won’t make much of a difference.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I can just tell the others I’ve seen you, you know. Your name won’t make much of a difference.”')
                $ description_aegidia01 = "An adopted daughter of {color=#f6d6bd}Thais{/color} and {color=#f6d6bd}Eryx{/color}. She despises her mother."
                $ quest_fisherhamlet_description04cd = "I met {color=#f6d6bd}Aegidia{/color}, the not-so-dead daughter of {color=#f6d6bd}Thais{/color}. She’s asked me to lie in her name and to talk her mother out of regaining the hamlet."
                $ renpy.notify("Journal updated: The Old Hamlet")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Old Hamlet{/i}')
                $ questionpreset = "aegidia2"
                menu:
                    'She waggles her bow for a bit, then smiles and extends it as far to the left as she can, puts her right hand on her stomach, draws her left foot on the ground so harshly that the sand stirs up, and bows deeply, hiding her face. Even in {color=#f6d6bd}Hovlavan{/color}, it would be seen as mockingly theatrical.
                    \n\nHer tone is disarmingly playful. “Ma name is {color=#f6d6bd}Aegidia{/color}, the greatest archeress of {color=#f6d6bd}Howler’s Dell{/color}, an orphan from birth, against ma will taken under the wings of {color=#f6d6bd}Eryx{/color} en talons of {color=#f6d6bd}Thais{/color}.” She straightens up. “But ne anymore. {color=#f6d6bd}Asterion{/color} helped me escape, like a {i}real{/i} roadwarden would.”
                    \n\nHer eyes fill up with hatred. “That harpy of a mother will have nae power over me, en if she tries to peck me again, I’ll break her beak.”
                    '
                    '(aegidia2 set)':
                        pass

    label fishinghamletaegidiapcabouthamlet04e:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What do you have against {color=#f6d6bd}Thais{/color}?”')
        $ description_thais02 = "According to {color=#f6d6bd}Aegidia{/color}, {color=#f6d6bd}Elpis{/color} describes {color=#f6d6bd}Thais{/color} as a soul who hates to be seen as a weakling."
        $ aegidia_about_thais = 1
        $ questionpreset = "aegidia2"
        menu:
            'She pulls the string of her bow. “I’m ne a bard, words escape me, en ma pain shall die with me. But {color=#f6d6bd}Elpis{/color}, a forest speaker, also {i}knows{/i} the {i}real{/i} mayor. She wants others to see her as strong, at all costs.”
            \n\nShe swings the bow like a staff, right above the ground, as if to hit invisible legs. “She punishes those who stand against her. En I did the worst crime of them all,” she makes a dramatic pause. “I doubted her.”
            '
            '(aegidia2 set)':
                pass

    label fishinghamletaegidiapcabouthamlet04ca:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t have the right to hinder the well-being of the entire village.”')
        $ aegidia_about_hamletalone_doubt01 = 1
        $ custom1 = "“They’ve got everything they need. The harvest, the mouflons, the wild game. En they did ne protect me from {color=#f6d6bd}Thais{/color}. But I do ne hate them for it, you see? She {i}is{/i} cruel. What I take, is what I deserve after their... silence.”"
        jump fishinghamletaegidiapcabouthamlet04cd

    label fishinghamletaegidiapcabouthamlet04cb:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You {i}assume{/i} a lot. You can’t expect all your plans to succeed.”')
        $ aegidia_about_hamletalone_doubt02 = 1
        $ custom1 = "“I can en I do. I know these folks, traveler. You sound like the mayor, right now. Only {i}she{/i} is allowed to take risks. Only {i}she{/i} can make mistakes. Only {i}she{/i} can be brave. Well!” She straightens up, grasping her bow firmly. “I carry a brave soul. I’m ready to be wrong, en to face consequences, if tha’s the only path to freedom.”"
        jump fishinghamletaegidiapcabouthamlet04cd

    label fishinghamletaegidiapcabouthamlet04cc:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “The druids don’t control the village. {color=#f6d6bd}Thais{/color} does.”')
        $ aegidia_about_hamletalone_doubt03 = 1
        $ custom1 = "“She {i}controls{/i} what ma neighbors let her control, en only because she’s good at hiding from them what they do ne want to see. But let her fail!” She smiles. “Let the others hear that their good old fishing spot has turned into ruins. Once I’m back, this moment of weakness may make just the difference.”"
        jump fishinghamletaegidiapcabouthamlet04cd

    label fishinghamletaegidiapcabouthamlet04cd:
        $ questionpreset = "aegidia2"
        if aegidia_about_hamletalone_doubt01 and aegidia_about_hamletalone_doubt02 and aegidia_about_hamletalone_doubt03:
            $ aegidia_friendship -= 1
            menu:
                '[custom1]
                \n\nShe suddenly bites her lip, revealing her white teeth, then points at you with her bow. “I’m done with your mistrust. I do ne need your approval to know I’m right.”
                '
                '(aegidia2 set)':
                    pass
        else:
            menu:
                '[custom1]
                '
                '(aegidia2 set)':
                    pass

    label fishinghamletaegidiapcabouthamlet05:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m ready to give you my answer.”')
        menu:
            'She observes you in silence, drawing short lines in the sand with her foot.
            '
            '“{color=#f6d6bd}Thais{/color} deserves to know the truth.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Thais{/color} deserves to know the truth.”')
                $ aegidia_favor = 0
                $ aegidia_friendship -= 4
                $ minutes += 10
                jump fishinghamletaegidiapcabouthamlet05a
            '“I’ll cover for you. I trust you’ll put the time you have to good use.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll cover for you. I trust you’ll put the time you have to good use.”')
                $ quarters += 1
                $ aegidia_favor = "iwill"
                $ aegidia_friendship += 4
                if pc_goal == "iwanttohelp":
                    $ pc_goal_iwanttohelppoints += 1
                jump fishinghamletaegidiapcabouthamlet05b
            '“I’ll cover for you, but only until spring. You can’t take this place away from {color=#f6d6bd}Howler’s Dell{/color}.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll cover for you, but only until spring. You can’t take this place away from {color=#f6d6bd}Howler’s Dell{/color}.”')
                $ aegidia_favor = "iwillforatime"
                $ aegidia_friendship += 3
                $ minutes += 5
                if pc_goal == "iwanttohelp":
                    $ pc_goal_iwanttohelppoints += 1
                jump fishinghamletaegidiapcabouthamlet05c
            '(lie) “You have nothing to worry about. I’ve got your back.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- (lie) “You have nothing to worry about. I’ve got your back.”')
                $ quarters += 1
                $ pc_lies += 2
                $ aegidia_favor = "lie"
                $ aegidia_friendship += 4
                jump fishinghamletaegidiapcabouthamlet05b

    label fishinghamletaegidiapcabouthamlet05a:
        $ questionpreset = "aegidia1"
        menu:
            'She bites her lower lip and takes a few steps away, toward her cabin, raising her voice.
            \n\n“A bad call, but ‘tis yours. I hope you believe ‘tis the right thing to do, en you’re ne just another one of,” she pauses, “the mayor’s goblins. Give me a minute.” She enters the building and you think about your axe.
            \n\nAfter a few heartbeats, you hear the sound of shattered clay. A few minutes later, she shows up again, still holding her bow, but her hair is now combed, and she’s wearing a brown linen tunic, slightly darker than her skin, with red trim on its neck and sleeves, long enough to reach her knees. It’s as good as new - a relic of {color=#f6d6bd}Thais’{/color} luxuries.
            '
            '(aegidia1 set)':
                pass

    label fishinghamletaegidiapcabouthamlet05b:
        $ questionpreset = "aegidia1"
        menu:
            'She closes her eyes, takes a few deep breaths, and starts to walk around you, with light steps that turn into skipping. There are tears in her eyes.
            \n\n“Thank you, thank you! I’d hug you, but, oh well!” She waves her hand in front of her, drawing your attention to the rags that she’s wearing.
            \n\n{color=#f6d6bd}Aegidia{/color} asks you to give her a few minutes, and you return to {color=#f6d6bd}[horsename]{/color}. Once she returns, her hair is combed, and she’s wearing a brown linen tunic, slightly darker than her skin, with red trim on its neck and sleeves, long enough to reach her knees. It’s as good as new - a relic of {color=#f6d6bd}Thais’{/color} luxuries.
            '
            '(aegidia1 set)':
                pass

    label fishinghamletaegidiapcabouthamlet05c:
        $ questionpreset = "aegidia1"
        menu:
            'She closes her eyes, takes a few deep breaths and starts to stretch her arms and back, as well as walking about. You can see the tension leaving her shell with every step.
            \n\n“Fair, more than fair. Thank you!” Tears well up in her eyes, but her voice stays strong. “I’d hug you, but you must forgive me!” She grabs a strap of her rag, as if it’s meant to explain everything.
            \n\n{color=#f6d6bd}Aegidia{/color} asks you to give her a few minutes, and you return to {color=#f6d6bd}[horsename]{/color}. Once she returns, her hair is combed, and she’s wearing a brown linen tunic, slightly darker than her skin, with red trim on its neck and sleeves, long enough to reach her knees. It’s as good as new - a relic of {color=#f6d6bd}Thais’{/color} luxuries.
            '
            '(aegidia1 set)':
                pass

label fishinghamletaegidiapcaboutthemself01alt: #“I’m a roadwarden. I need to learn more about this land.”
    $ aegidia_about_peninsula = 1
    $ questionpreset = "aegidia1"
    menu:
        'She clicks her tongue and looks away, observing the sand dancing in the wind. “So, the’s a new one already.” Pause. “But the’s ne much for you to find here. There are ne eva ghosts here.”
        '
        '(aegidia1 set)':
            pass

    label fishinghamletaegidiapcaboutthemself01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m %s, the new roadwarden.”' %pcname)
        jump fishinghamletaegidiapcaboutthemself01alt

label fishinghamletaegidiapcaboutasterion01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m trying to find {color=#f6d6bd}Asterion{/color}, the previous roadwarden.”')
    label fishinghamletaegidiapcaboutasterion01after:
        $ aegidia_about_asterion = 1
        $ questionpreset = "aegidia1"
        menu:
            'She huffs loudly, then spreads out her arms, as if to show there’s no one here. “I need to speak with him maself. Tell him that, if you ever find him.”
            '
            '(aegidia1 set)':
                pass

label fishinghamletaegidiapcaboutasterion01alt:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about {color=#f6d6bd}Asterion{/color}.”')
    if (aegidia_friendship+appearance_charisma) >= 2:
        $ aegidia_about_asterion = 2
        menu:
            'She touches her lips with the tip of her bow. “Well, I do ne know where he is. I spent little time with him, but he’s a stranger with a pure heart, like it’s made of iron.” She glances at you. “He does ne talk much. Must be a warden thing, aye? {i}Nae, I will ne stay around{/i}, he said,” she tries awkwardly to imitate a male voice. “{i}I ride east, next.{/i} East, I ask? To Howler’s? {i}Farther{/i}, he said. To the enchantress, maybe? {i}Eva farther than that.{/i} His own words!”
            \n\nShe looks at you triumphantly.
            '
            '“...What?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...What?”')
                $ quest_reachthepaganvillage_description00b = "I’ve heard a rumor that {color=#f6d6bd}Asterion{/color} has kept in touch with them."
                if not quest_reachthepaganvillage:
                    $ quest_reachthepaganvillage = 1
                    $ renpy.notify("New entry: The Hidden Village")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: The Hidden Village{/i}')
                elif quest_reachthepaganvillage == 1:
                    $ renpy.notify("Journal updated: The Hidden Village")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Hidden Village{/i}')
                $ questionpreset = "aegidia1"
                menu:
                    '“Oh, he means {color=#f6d6bd}The Tribe of The Green Mountain{/color}, I’m sure. Tha’s where they live. Away from any road, I’m ne eva sure how to find them. Maybe one of the forest speakers could guide you.”
                    '
                    '(aegidia1 set)':
                        pass
    else:
        $ questionpreset = "aegidia1"
        $ aegidia_about_asterion_gray = 1
        menu:
            'She scoffs. “You’re ne a friend of mine. I have nae reason to betray a kind soul.”
            '
            '(aegidia1 set)':
                pass

label fishinghamletaegidiapcaboutherself01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Who are you?”')
    $ aegidia_about_herself = 1
    $ questionpreset = "aegidia1"
    menu:
        '“Just a friendly recluse.” She draws the bowstring gently. “Though ne very patient one. Better tell me what brought you here.”
        '
        '(aegidia1 set)':
            pass

label fishinghamletaegidiapcaboutboat01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I saw a boat. If I was ever in need of borrowing one, would you care?”')
    $ aegidia_about_boat = 1
    if aegidia_favor:
        $ custom1 = "She pauses. “Though... I do owe you a favor. We may figure something out.”"
    else:
        $ custom1 = ""
    $ questionpreset = "aegidia1"
    menu:
        '“Of course I {i}would care{/i}. ‘Tis ma boat. Kind of. Nae, wait.” She raises her chin. “Yes, ‘tis {i}ma{/i} boat. ‘En ‘tis ne cheap.” [custom1]
        '
        '(aegidia1 set)':
            pass

label fishinghamletaegidiapcaboutnecklace01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is this your necklace?”')
    $ aegidia_about_necklace1 = 1
    $ questionpreset = "aegidia1"
    menu:
        'She doesn’t reach for it, and instead lowers her head to your open palm. “Nae, ‘tis ugly. You found it here? Must be old, from before ma time.”
        '
        '(aegidia1 set)':
            pass

label fishinghamletaegidiapcaboutresting01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Is it safe to rest here during the night?”')
    $ aegidia_about_resting = 1
    $ questionpreset = "aegidia1"
    menu:
        'She points her bow at the broken palisade. “I do ne know, you tell me. ‘I’m ne sharing ma shelter with you. Your horse would ne fit through the door anyway. Better turn back to {color=#f6d6bd}Howler’s{/color}.”
        '
        '(aegidia1 set)':
            pass

label fishinghamletaegidiapcabouthersurvival01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How did you manage to survive for so long, all by yourself?”')
    $ aegidia_about_survival = 1
    $ description_aegidia06 = "She tries to learn how to catch the small fish from the stream."
    $ questionpreset = "aegidia1"
    menu:
        '“‘Twas ne so hard, but it will change now, with the road cleared for larger beasts,” she bites her lower lip. “I eat birds, some green leaves from the top of the cliff, to keep my hair strong,” she touches it with an open palm, “en I learn how to catch the small fish from the stream. The nights are ne much better than in the woods, I admit. If ne for ma spell, the monsters would have gotten through many times, the door is ne enough. Ma smell is around, you see. They know I’m but food.”
        \n\n“You’re a spellcaster?” you ask, and she playfully touches her canine with the tip of her tongue. “I’ve many talents, pray to ne learn about them all!”
        '
        '(aegidia1 set)':
            pass

label fishinghamletaegidiapcaboutfishtrap01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have a fish trap with me. That basket with a lid. Would you like to buy it?”')
    $ aegidia_about_fishtrap1 = 1
    menu:
        'She raises an eyebrow. “Show me.” You grab it, then start to explain how it works. “Oh, I get it. We do ne place such traps often, {color=#f6d6bd}Howler’s Creek{/color} is clean and all, but ne very generous.”
        \n\nShe looks toward the brook, then at the trap again. Lost in her thoughts, she walks around, tapping her bow. “I do ne have dragons, you realize. But there was brine here, in a barrel, en I made a sealskin with it. ‘Tis a nice pelt, I wanted it for some winter clothes, but I’d rather have this basket, learn how to make more of them. I’m worried about all the salt I eat.”
        '
        '“A pelt for a trap? Sounds good.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “A pelt for a trap? Sounds good.”')
            label fishinghamletaegidiapcaboutfishtrap01after:
                $ renpy.notify("You sold a fish trap\nfor a sealskin.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You sold a fish trap\nfor a sealskin.{/i}')
                $ aegidia_about_fishtrap2 = 1
                $ item_fishtrap -= 1
                $ item_sealskin += 1
                $ minutes += 5
                $ questionpreset = "aegidia1"
                menu:
                    'She bows to you, then enters her cabin. After a few minutes, you inspect the thick, gray fur that would do well among the cobblers and tailors from {color=#f6d6bd}Hovlavan{/color}. As you roll it and tie it to your bundles, {color=#f6d6bd}Aegidia{/color} studies her new purchase with a warm grin.
                    '
                    '(aegidia1 set)':
                        pass
        '“I’ll think about it.”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
            $ questionpreset = "aegidia1"
            menu:
                '“Better do so while I’m alive,” she gives you a warm smile.
                '
                '(aegidia1 set)':
                    pass

    label fishinghamletaegidiapcaboutfishtrap02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About the fish trap...”')
        menu:
            '“Aye, I’m still interested.”
            '
            '“It’s yours. Go, grab the sealskin.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s yours. Go, grab the sealskin.”')
                jump fishinghamletaegidiapcaboutfishtrap01after
            '“I still have my doubts.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I still have my doubts.”')
                $ questionpreset = "aegidia1"
                menu:
                    'She just shrugs.
                    '
                    '(aegidia1 set)':
                        pass

label fishinghamletaegidiapcaboutarrow01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I show her the arrow I found near the fallen tree. “Could you tell me anything about this?”')
    $ aegidia_about_arrow = 1
    $ galerocks_florus_about_arrow = 1
    menu:
        '“Ah, ma {i}expertise{/i} is required!” Her smile turns into a chuckle. “Let me take a look.”
        \n\nShe returns it to you after a few moments. “‘Tis naething special. Where did you find it? It wasn’t used in a hunt, was it?”
        '
        '“On the side of the road. What makes you say that?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “On the side of the road. What makes you say that?”')
            menu:
                '“People from {color=#f6d6bd}Gale Rocks{/color} make those. Orange en black, you see?” She points at the fletching. “Colors for combat. {i}Human arrows{/i}, as I was told. ‘Tis a spell thing of theirs. Brown feathers are for deer, green en orange are for goblins, en so on.”
                '
                '“Spell, you say? Does it work?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Spell, you say? Does it work?”')
                    $ questionpreset = "aegidia1"
                    menu:
                        'She gives the arrow back. “How can one tell? They say it works. Maybe the’s a ritual or something, like a secret. A fletcher may know it.”
                        '
                        '(aegidia1 set)':
                            pass

label fishinghamletaegidia_about_shortcut01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you ever been at the heart of the woods?”')
    $ aegidia_about_shortcut = 1
    $ questionpreset = "aegidia1"
    menu:
        '“Nae, we do ne hunt for beasts beyond the nearest hills and ponds. If I were to enter the deep roads, I’d have some long preparations to do. Good gambeson, sharp blade, healthy shell, food in ma belly en in a sack.”
        \n\nShe glances at {color=#f6d6bd}[horsename]{/color} and can’t stop her chuckle. “En I’d take someone with me, or a group of someones, but you already have all the help you need, I see.”
        '
        '(aegidia1 set)':
            pass

label fishinghamletaegidia_about_highislandALL:
    label fishinghamletaegidia_about_highisland01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I think {color=#f6d6bd}Asterion{/color} has sailed to {color=#f6d6bd}High Island{/color}. Do you know anything about it?”')
        $ aegidia_about_highisland = 1
        $ aegidia_friendship += 2
        $ questionpreset = "aegidia1"
        $ description_highisland08 = "According to {color=#f6d6bd}Aegidia{/color}, "
        menu:
            'She opens her mouth, but needs a few breaths to speak. “He left like that, without a word? To that death trap?” She raises her bow and points in the north-west. “You can see the island from here! ‘Tis ne easy to get there, eva on a boat.”
            \n\nWhen you mention you’d appreciate any tip that could help you survive there, she moves her lips left and right, humming to herself. “I have ne seen it maself, but I heard that when the winters are at their darkest, the water from here to there is all frozen, en eva a big beast can get there on their paws.” Seeing your puzzled look, she explains. “The creatures there are ne too different from the ones we have here. The more you learn about them, the more prepared you’ll be.”
            \n\nBefore you change the subject, she lets out a huff. “I do hope you’ll bring him back.”
            '
            '(aegidia1 set)':
                pass

    label aegidia_about_highisland_recruitment01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could use your help on the island.”')
        $ aegidia_about_highisland_recruitment = 1
        if aegidia_favor:
            $ aegidia_about_highisland_recruitment_done = 1
            $ quest_gatheracrew_description00boatfishinghamlet = 1
            $ questionpreset = "aegidia1"
            menu:
                'Her curiosity grows as you describe your plan. “En you think {i}he{/i} may still be alive, truly?” After your vague nod, she straightens up, raising her bow in a salute. “You helped me already, so ‘tis only fair for me to join you! And if you’ve nae boat yet - you can use mine!”
                '
                '(aegidia1 set)':
                    pass
        else:
            $ questionpreset = "aegidia1"
            menu:
                'Her curiosity grows as you describe your plan. “En you think {i}he{/i} may still be alive, truly?” After your vague nod, she scratches her cheek with her bow. “I wish I could just show up there en bring him to safety, but I’m ne going to jump into a boat with {color=#f6d6bd}Thais’{/color} ally,” her voice gets cold. “You’re ne eva a sailor.”
                '
                '(aegidia1 set)':
                    pass

    label aegidia_about_highisland_recruitment02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Please, {color=#f6d6bd}Aegidia{/color}. Help me find {color=#f6d6bd}Asterion{/color}.”')
        $ aegidia_about_highisland_recruitment_done = 1
        $ quest_gatheracrew_description00boatfishinghamlet = 1
        $ questionpreset = "aegidia1"
        menu:
            'She gives you a long look, then lets out an exaggerated sigh. “Why are roadwardens bringing so much noise, good en bad? Fine, fine, [pcname].” She straightens up, raising her bow in a salute. “I’ll prepare my stuff. En if you’ve nae boat yet - you can use mine!”
            '
            '(aegidia1 set)':
                pass

    label aegidia_about_highisland_recruitment02alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know you don’t trust me, but I {i}need{/i} your help on the island. I offer you {color=#f6d6bd}Asterion’s{/color} bow to show my good will.”')
        $ aegidia_about_highisland_recruitment_done = 1
        $ quest_gatheracrew_description00boatfishinghamlet = 1
        $ renpy.notify("You gave away Asterion’s bow.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You gave away Asterion’s bow.{/i}')
        $ item_asterionbow = 0
        $ questionpreset = "aegidia1"
        menu:
            'She gives you a long look, then lets out an exaggerated sigh. “Why are roadwardens bringing so much noise, good en bad? Fine, fine, [pcname].” She steps closer, takes the bow out of your hands, then raises it in a salute. “I’ll prepare my stuff. En if you’ve nae boat yet - you can use mine!”
            '
            '(aegidia1 set)':
                pass

    label aegidia_about_asterion_found01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I found {color=#f6d6bd}Asterion{/color}, but I’m not bringing good news.”')
        $ aegidia_about_asterion_found = 1
        $ aegidia_friendship += 2
        $ minutes += 1
        $ description_thais02a = "According to {color=#f6d6bd}Aegidia{/color}, she’s getting weaker with every year, struggling with a mysterious illness."
        $ questionpreset = "aegidia1"
        menu:
            '“Ah, shit fire,” her shoulders slope as she starts to wander around the yard. “What happened to him?”
            \n\nYou share as little as you need, and she doesn’t inquire further. “Is this ne weird? How souls like his get swallowed by the forest, whilst {color=#f6d6bd}Thais{/color} sits on her throne of dragon bones? She gets weaker en weaker from that illness of hers, but still has enough of a breath to lie en scheme. Just stupid.”
            '
            '(aegidia1 set)':
                pass

label fishinghamletaegidia_about_steephouse01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the village in the south?”')
    $ aegidia_about_steephouse = 1
    $ howlersdell_steephouseconfrontation_childrenshame = 1
    $ questionpreset = "aegidia1"
    menu:
        '“Ne really. I was still this tall,” she raises her open hand, palm down, to her chest. “I just heard ‘tis {i}difficult{/i}, en that I should ne ask about it.”
        \n\nShe then bites her lower lip. “I’ve ne been thinking about it for years... But maybe I should, knowing it was {color=#f6d6bd}Thais{/color} who told me this."
        '
        '(aegidia1 set)':
            pass

label fishinghamletaegidia_about_steephouse01alt:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How do you feel about what happened to {color=#f6d6bd}Steep House{/color}?”')
    $ aegidia_about_steephouse = 1
    $ howlersdell_steephouseconfrontation_childrenshame = 1
    $ questionpreset = "aegidia1"
    menu:
        '“How should I feel? I was still this tall,” she raises her open hand, palm down, to her chest. “I just heard ‘tis {i}difficult{/i}, en that I should ne ask about it.”
        \n\nShe then bites her lower lip. “I’ve ne been thinking about it for years... But maybe I should, knowing it was {color=#f6d6bd}Thais{/color} who told me this."
        '
        '(aegidia1 set)':
            pass

label fishinghamletaegidia_about_steephouse02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know what happened to {color=#f6d6bd}Steep House{/color}. Would you like to learn the truth?”')
    $ aegidia_about_steephouse_truth = 1
    $ aegidia_friendship += 2
    $ questionpreset = "aegidia1"
    $ quarters += 1
    menu:
        'Her hands squeeze her bow, her eyes are keen. After her gentle nod, you tell her what you’ve learned. Tears well up in her eyes even before you finish, but she stares at you intensely, trying to catch a hint of a lie, something to grab on before she puts her trust in your tale.
        \n\nIn the end, she scratches the sand with her foot, lowering her head. Then, she covers her eyes. “Shame on them. Shame on my... {color=#f6d6bd}Thais{/color}, en on me, for I asked nae questions.”
        \n\nBefore you respond, she enters her hut for a minute, then returns with fresh water dripping from her face. While her eyes are red, she holds her bow with determination. “‘Tis better to know the truth. I planned to return home one year, but now I do ne know. If I do... {i}I will be heard.{/i}”
        '
        '(aegidia1 set)':
            pass

label fishinghamletaegidia_about_nomoreundead01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It may be better for you to leave this place, even before fall. The bogs east from here are overrun by undead.”')
    $ aegidia_about_nomoreundead = 1
    $ aegidia_friendship += 1
    $ questionpreset = "aegidia1"
    menu:
        '“But what do you mean by that? Something happened?” She raises a fist to her mouth. “To {color=#f6d6bd}White Marshes{/color}?”
        \n\nYou confirm her suspicions, without revealing too much. Her grimaces shift between sorrow and fear. “But they’d need to cross {color=#f6d6bd}Howler’s Creek{/color}, maybe ‘tis too far away...” She looks toward the fallen stakes of the useless wall. “Bloody monsters. Ma spell can ne help me with them.”
        '
        '(aegidia1 set)':
            pass

label aegidia_about_recruitahunter01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I bet you spent some time working with {color=#f6d6bd}Erastos{/color}?”')
    $ quest_recruitahunter_spokento_aegidia = 1
    $ quest_recruitahunter_erastos_points += 1
    if quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold2 and not quest_recruitahunter_erastos_points_notify2:
        $ quest_recruitahunter_erastos_points_notify2 = 1
        $ quest_recruitahunter_erastos_points_notify1 = 1
        $ renpy.notify("Journal updated: Recruit a Hunter")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
    elif quest_recruitahunter_erastos_points >= quest_recruitahunter_erastos_threshold and not quest_recruitahunter_erastos_points_notify1:
        $ quest_recruitahunter_erastos_points_notify1 = 1
        $ renpy.notify("Journal updated: Recruit a Hunter")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Recruit a Hunter{/i}')
    $ questionpreset = "aegidia1"
    menu:
        '“Believe me or ne, but you’d lose this bet.” Her smiling lip softens her gaze. “{color=#f6d6bd}Erastos{/color} did ne spend any time with those of us who put their lives at risk in the woods. He was too busy chasing after my sister, and building these wooden boxes of his. But he’s still young, you know? Give him some time to get smarter.”
        '
        '(aegidia1 set)':
            pass

label fishinghamletaegidiapcabouthamlet00:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s time for me to leave.”')
    if not aegidia_about_hamlet:
        $ aegidia_about_hamlet = 1
        menu:
            '“Apologies,” she sighs, then raises her bow again and aims at your neck. “I do ne think so, nae. If you’re here, it means I’m in danger. Tell me, what does {color=#f6d6bd}Thais{/color} want?” Coming from her mouth, {color=#f6d6bd}the mayor’s{/color} name is like a toothache.
            '
            '“Why do you think it’s her?”':
                jump fishinghamletaegidiapcabouthamlet01alt

    else:
        # if aegidia_firsttime:
        #     if not renpy.music.get_playing(channel='music') == "audio/weloveindies_vastlands_hamletloop.ogg":
        #         play music "audio/weloveindies_vastlands_hamletloop.ogg" fadeout 1.0 fadein 0.0
        # else:
        #     stop music fadeout 4.0
        #     play nature "audio/ambient/fishinghamlet01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
        jump fishinghamletselectwheretogover02
