default shortcut_darkforest_bandit_inpeltnorth = 0
default shortcut_darkforest_bandit_inpeltnorthpcknowsabout = 0
default shortcut_darkforest_bandit_leftFROMpeltnorth = 0

default shortcut_darkforest_bandit_about_beingabandit = 0
default shortcut_darkforest_bandit_peltnorthintroduction = 0

default shortcut_bandit_identity = 0
default shortcut_bandit_peltnorth_fluff = ""
default shortcut_bandit_peltnorth_fluff_old = 0

default peltnorth_armorer_firsttime = 0
default peltnorth_armorer_description = 0
default peltnorth_armorer_abouttrade = 0
default peltnorth_armorer_aboutarmor_can4 = 0
default peltnorth_armorer_aboutcleanliness_clothes_torn = 0
default peltnorth_armorer_aboutearplugs = 0
default peltnorth_armorer_aboutthemselves = 0

default quintus_pelt_firsttime = 0
default quintus_pelt_inside = 0
default quintus_pelt_left = 0
default quintus_peltnorth_fluff = 0
default quintus_peltnorth_fluff_old = 0
default quintus_peltnorthintroduction = 0

############################################# Pyrrhos
label peltnorth01insidetalkingwithpyrrhosALL:
    label peltnorth01insidetalkingwithpyrrhos:
        menu:
            '“Ay, roadster. Need anything?”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                jump peltnorthpyrrhos01aboutironingot01
            '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                $ pyrrhos_about_highisland_recruitment = 1
                $ pyrrhos_about_highisland_recruitment_done = 1
                jump pyrrhos_about_highisland_recruitment_pelt01
            '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                $ pyrrhos_about_newplace = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                jump peltnorthpyrrhos01abouthimselfinpeltnorth
            '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                $ pyrrhos_quest_reward_debt = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                jump peltnorthpyrrhos01askingforreward
            '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                $ pyrrhos_about_peninsula = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                jump peltnorthpyrrhos01aboutpeninsula
            '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                $ pyrrhos_about_himself = 1
                jump peltnorthpyrrhos01abouthimself
            '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                $ pyrrhos_about_undead = 1
                jump peltnorthpyrrhos01aboutundead
            '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                $ pyrrhos_about_thingsleftbehind = 1
                jump peltnorthpyrrhos01aboutthingsleftbehind
            '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                $ pyrrhos_about_ruins = 1
                jump peltnorthpyrrhos01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                $ pyrrhos_about_bandits = 1
                jump peltnorthpyrrhos01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                $ pyrrhos_about_asterion = 1
                $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                jump peltnorthpyrrhos01aboutasterion
            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            '“Bye.” I go outside.':
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                jump leavingthepeltnorth

    label peltnorth01regularquestions:
        menu:
            '“Ay, we can talk. Go ahead.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                jump peltnorthpyrrhos01aboutironingot01
            '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                $ pyrrhos_about_highisland_recruitment = 1
                $ pyrrhos_about_highisland_recruitment_done = 1
                jump pyrrhos_about_highisland_recruitment_pelt01
            '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                $ pyrrhos_about_newplace = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                jump peltnorthpyrrhos01abouthimselfinpeltnorth
            '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                $ pyrrhos_quest_reward_debt = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                jump peltnorthpyrrhos01askingforreward
            '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                $ pyrrhos_about_peninsula = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                jump peltnorthpyrrhos01aboutpeninsula
            '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                $ pyrrhos_about_himself = 1
                jump peltnorthpyrrhos01abouthimself
            '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                $ pyrrhos_about_undead = 1
                jump peltnorthpyrrhos01aboutundead
            '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                $ pyrrhos_about_thingsleftbehind = 1
                jump peltnorthpyrrhos01aboutthingsleftbehind
            '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                $ pyrrhos_about_ruins = 1
                jump peltnorthpyrrhos01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                $ pyrrhos_about_bandits = 1
                jump peltnorthpyrrhos01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                $ pyrrhos_about_asterion = 1
                $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                jump peltnorthpyrrhos01aboutasterion
            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            '“Bye.” I go outside.':
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                jump leavingthepeltnorth

    label peltnorth01regularquestionsv02:
        menu:
            '“So, anything else bothering ye?”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                jump peltnorthpyrrhos01aboutironingot01
            '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                $ pyrrhos_about_highisland_recruitment = 1
                $ pyrrhos_about_highisland_recruitment_done = 1
                jump pyrrhos_about_highisland_recruitment_pelt01
            '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                $ pyrrhos_about_newplace = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                jump peltnorthpyrrhos01abouthimselfinpeltnorth
            '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                $ pyrrhos_quest_reward_debt = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                jump peltnorthpyrrhos01askingforreward
            '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                $ pyrrhos_about_peninsula = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                jump peltnorthpyrrhos01aboutpeninsula
            '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                $ pyrrhos_about_himself = 1
                jump peltnorthpyrrhos01abouthimself
            '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                $ pyrrhos_about_undead = 1
                jump peltnorthpyrrhos01aboutundead
            '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                $ pyrrhos_about_thingsleftbehind = 1
                jump peltnorthpyrrhos01aboutthingsleftbehind
            '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                $ pyrrhos_about_ruins = 1
                jump peltnorthpyrrhos01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                $ pyrrhos_about_bandits = 1
                jump peltnorthpyrrhos01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                $ pyrrhos_about_asterion = 1
                $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                jump peltnorthpyrrhos01aboutasterion
            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            '“Bye.” I go outside.':
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                jump leavingthepeltnorth

    label peltnorthpyrrhos01abouthimself:
        $ pyrrhos_about_himself = 2
        $ description_pyrrhos01 = "He calls himself a drifter and a trader, and isn’t afraid of some more dangerous tasks. He claims that he came here by ship, looking for dragon bones."
        $ description_pyrrhos02 = "He claims that he was healed by powerful magic in the local monastery."
        menu:
            '“I could tell ye stories for days, but who cares?” He chuckles. “I’m just doing my thing, moving from wall to wall, sleeping where they let me, buying what I need, selling what I can, saving dragons for later on. I used to be a sailor, people called me {color=#f6d6bd}Pyrrhos{/color} because of the, ye know, forehead. But I’m not one to push a plough or patch ship sails all day long. I don’t care if a corpser eats my bones one day, as long as I can stay free for a couple of years more.”
            \n\n“And I’m damn good at staying safe, or rather I was before I landed in this shithole.” He touches his scarred face and smirks unpleasantly. “I haven’t gotten one of these in years, but it didn’t take two weeks on the road here and I almost lost my legs. Spent all my coin in {color=#f6d6bd}Howler’s Dell{/color} for elders’ magic.” He brushes some invisible dust off his pants. “Not the first time I have an empty pouch, not gonna lie, but there’s no coin waiting here. Once I push all the iron to the locals, I’m moving South. Though I won’t ride alone, I’m not making that mistake again.”
            '
            '“I’ve heard no ships can land on this coast.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard no ships can land on this coast.”')
                jump peltnorthpyrrhos01abouthimself02
            'He’s probably lying, but I don’t let him know that I’ve noticed it. “I have another question.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- He’s probably lying, but I don’t let him know that I’ve noticed it. “I have another question.”')
                jump peltnorth01regularquestions

        label peltnorthpyrrhos01abouthimself02:
            $ pyrrhos_friendship -= 1
            $ quest_explorepeninsula_description03 = "I heard that some of the locals know ways to move safely through the rocky coasts, so it may be possible to get access by the sea after all."
            $ description_galerocks04 = "I heard that the fishers from {color=#f6d6bd}Gale Rocks{/color} know how to move between the coastal rocks."
            $ renpy.notify("Journal updated: Explore the Peninsula")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Explore the Peninsula{/i}')
            menu:
                '“Well,” he tilts his head to the right and gives you a distrustful look. “If yer patient and take ya time, ye can get to {color=#f6d6bd}Gale Rocks{/color} from the sea. In a light boat, or a raft, or something that can avoid the rocky teeth. Sure, no hope for a ship, or any trade, ba’with some help, ye can do it. Ba’don’t tell anyone I told ye this.” His tone gets significantly colder. “It’s not something people should talk about.”
                '
                'I nod. “I have some questions.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod. “I have some questions.”')
                    jump peltnorth01regularquestions

    label peltnorthpyrrhos01aboutundead:
        if quest_ruins == 1 and not quest_ruins_description01:
            $ quest_ruins_description01 = "I heard that the village was destroyed almost ten years ago."
            $ renpy.notify("Journal updated: The Ruined Village")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: The Ruined Village{/i}')
        menu:
            'He nods. “I’ve seen none. People say it’s been less than ten years since the herds came there, b’I don’t know if anyone bothered with raising the pyres. If not, the dead are all roaming in the forest now.” He clicks his tongue with frustration. “It may be that there’s a walker somewhere under the debris, waiting to break through like a dragon in an egg.” He looks straight at you. “Ay, ye’d better not dig.”
            '
            '“I have some other questions.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some other questions.”')
                jump peltnorth01regularquestions

    label peltnorthpyrrhos01aboutthingsleftbehind:
        $ pyrrhos_about_thingsleftbehind += 1
        menu:
            '“It was a bad place to seek loot. Time, moisture, and the damn borers devoured all of it. I was there for a couple of days, and all that’s left is this iron I carried here. I was planning to get back there with some hired muscle and clear the collapsed buildings, b’I doubt it’s worth the time and risk.”
            '
            '“I have some other questions.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some other questions.”')
                jump peltnorth01regularquestions

    label peltnorthpyrrhos01aboutruins:
        menu:
            '“Well, I won’t guess, but I saw many ruins. There’s no treasure and skeletons there, so that place means as much as dirt. Someone was barking too loud, so the beasts broke through and made them quiet again,” he clicks his tongue. “And that’s that. Talking about nature’s fury brings bad luck, don’t ye know?”
            '
            '“I have some other questions.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some other questions.”')
                jump peltnorth01regularquestions

    label peltnorthpyrrhos01aboutbandits:
        menu:
            '“Nah, I think they are in the North, or East. I stuck to the western road and no shell bothered me. Sorry, can’t help ye.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                jump peltnorthpyrrhos01aboutironingot01
            '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                $ pyrrhos_about_highisland_recruitment = 1
                $ pyrrhos_about_highisland_recruitment_done = 1
                jump pyrrhos_about_highisland_recruitment_pelt01
            '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                $ pyrrhos_about_newplace = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                jump peltnorthpyrrhos01abouthimselfinpeltnorth
            '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                $ pyrrhos_quest_reward_debt = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                jump peltnorthpyrrhos01askingforreward
            '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                $ pyrrhos_about_peninsula = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                jump peltnorthpyrrhos01aboutpeninsula
            '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                $ pyrrhos_about_himself = 1
                jump peltnorthpyrrhos01abouthimself
            '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                $ pyrrhos_about_undead = 1
                jump peltnorthpyrrhos01aboutundead
            '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                $ pyrrhos_about_thingsleftbehind = 1
                jump peltnorthpyrrhos01aboutthingsleftbehind
            '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                $ pyrrhos_about_ruins = 1
                jump peltnorthpyrrhos01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                $ pyrrhos_about_bandits = 1
                jump peltnorthpyrrhos01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                $ pyrrhos_about_asterion = 1
                $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                jump peltnorthpyrrhos01aboutasterion
            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            '“Bye.” I go outside.':
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                jump leavingthepeltnorth

    label peltnorthpyrrhos01aboutasterion:
        $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the south, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
        menu:
            '“Ay, I’ve never met him, b’I surely heard his name many times. He vanished long before I got to the coast. At first, people were asking about him. Now they think he’s dead.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                jump peltnorthpyrrhos01aboutironingot01
            '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                $ pyrrhos_about_highisland_recruitment = 1
                $ pyrrhos_about_highisland_recruitment_done = 1
                jump pyrrhos_about_highisland_recruitment_pelt01
            '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                $ pyrrhos_about_newplace = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                jump peltnorthpyrrhos01abouthimselfinpeltnorth
            '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                $ pyrrhos_quest_reward_debt = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                jump peltnorthpyrrhos01askingforreward
            '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                $ pyrrhos_about_peninsula = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                jump peltnorthpyrrhos01aboutpeninsula
            '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                $ pyrrhos_about_himself = 1
                jump peltnorthpyrrhos01abouthimself
            '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                $ pyrrhos_about_undead = 1
                jump peltnorthpyrrhos01aboutundead
            '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                $ pyrrhos_about_thingsleftbehind = 1
                jump peltnorthpyrrhos01aboutthingsleftbehind
            '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                $ pyrrhos_about_ruins = 1
                jump peltnorthpyrrhos01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                $ pyrrhos_about_bandits = 1
                jump peltnorthpyrrhos01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                $ pyrrhos_about_asterion = 1
                $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                jump peltnorthpyrrhos01aboutasterion
            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            '“Bye.” I go outside.':
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                jump leavingthepeltnorth

    label peltnorthpyrrhos01abouthimselfinpeltnorth:
        if pyrrhos_peltnorth_counter == day:
            menu:
                '“Well, I’ve just arrived. I can tell ye more tomorrow, when I spend a few hours on something soft. Ba’damn, that smell around me is quite something, isn’t it? I’m going to the well soon.”
                '
                'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                    jump peltnorthpyrrhos01aboutironingot01
                '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                    $ pyrrhos_about_highisland_recruitment = 1
                    $ pyrrhos_about_highisland_recruitment_done = 1
                    jump pyrrhos_about_highisland_recruitment_pelt01
                '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                    $ pyrrhos_about_newplace = day
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                    jump peltnorthpyrrhos01abouthimselfinpeltnorth
                '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                    $ pyrrhos_quest_reward_debt = day
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                    jump peltnorthpyrrhos01askingforreward
                '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                    $ pyrrhos_about_peninsula = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                    jump peltnorthpyrrhos01aboutpeninsula
                '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                    $ pyrrhos_about_himself = 1
                    jump peltnorthpyrrhos01abouthimself
                '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                    $ pyrrhos_about_undead = 1
                    jump peltnorthpyrrhos01aboutundead
                '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                    $ pyrrhos_about_thingsleftbehind = 1
                    jump peltnorthpyrrhos01aboutthingsleftbehind
                '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                    $ pyrrhos_about_ruins = 1
                    jump peltnorthpyrrhos01aboutruins
                '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                    $ pyrrhos_about_bandits = 1
                    jump peltnorthpyrrhos01aboutbandits
                '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                    $ pyrrhos_about_asterion = 1
                    $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                    jump peltnorthpyrrhos01aboutasterion
                'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                    $ can_rest = 0
                    $ can_leave = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                    jump peltnorth01insidechoosenpc
                '“Bye.” I go outside.':
                    $ can_rest = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                    jump leavingthepeltnorth
        else:
            $ pyrrhos_about_himselfinpeltnorth = 1
            menu:
                '“It’s not bad here, not bad at all. They bought what I could sell, ba’the hunters want my entire pouch for getting me South. We’ve agreed to a lower price, ba’they won’t just drop whatever it is they’re doing to escort me. I don’t care, I’ll wait for a couple of days, do some chores for the innkeep, rest from the forests. Once the hunters are done with their plans, we’ll move out.”
                \n\nHe scratches his cheek and beard and finally sighs. “B’I do feel like I’ve eaten a trollshit, ay. When I landed here, I had my pile of bundles and trinkets, and now... I’m starting with nothing, again. I should’ve listened to the warnings. This land belongs to no man.”
                '
                'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                    jump peltnorthpyrrhos01aboutironingot01
                '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                    $ pyrrhos_about_highisland_recruitment = 1
                    $ pyrrhos_about_highisland_recruitment_done = 1
                    jump pyrrhos_about_highisland_recruitment_pelt01
                '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                    $ pyrrhos_about_newplace = day
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                    jump peltnorthpyrrhos01abouthimselfinpeltnorth
                '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                    $ pyrrhos_quest_reward_debt = day
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                    jump peltnorthpyrrhos01askingforreward
                '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                    $ pyrrhos_about_peninsula = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                    jump peltnorthpyrrhos01aboutpeninsula
                '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                    $ pyrrhos_about_himself = 1
                    jump peltnorthpyrrhos01abouthimself
                '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                    $ pyrrhos_about_undead = 1
                    jump peltnorthpyrrhos01aboutundead
                '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                    $ pyrrhos_about_thingsleftbehind = 1
                    jump peltnorthpyrrhos01aboutthingsleftbehind
                '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                    $ pyrrhos_about_ruins = 1
                    jump peltnorthpyrrhos01aboutruins
                '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                    $ pyrrhos_about_bandits = 1
                    jump peltnorthpyrrhos01aboutbandits
                '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                    $ pyrrhos_about_asterion = 1
                    $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                    jump peltnorthpyrrhos01aboutasterion
                'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                    $ can_rest = 0
                    $ can_leave = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                    jump peltnorth01insidechoosenpc
                '“Bye.” I go outside.':
                    $ can_rest = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                    jump leavingthepeltnorth

    label peltnorthpyrrhos01aboutironingot01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”')
        $ pyrrhos_about_ironingot = 1
        menu:
            'He instantly reaches toward his belt, but after taking a glance at the guards, he raises his hands, as if trying to calm you down. “Come on, roadster. Without it I’ll have nothing to sell once I get south.”
            '
            'I observe him in silence.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I observe him in silence.')
                $ custom1 = "He rephrases his request a few more times, but seeing no change in your gaze, he finally pauses and clicks his tongue. He scratches the scar on his face."
                $ pyrrhos_friendship += 1
                jump peltnorth01aboutironingot02
            '“Don’t try to play me. You stole it long before you lost your belongings.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Don’t try to play me. You stole it long before you lost your belongings.”')
                $ custom1 = "He raises his voice. “Ay, but {i}I{/i} need it more than some fishers.” He looks at you with contempt, and scratches his scared face."
                $ pyrrhos_friendship -= 1
                jump peltnorth01aboutironingot02

        label peltnorth01aboutironingot02:
            menu:
                '[custom1] “Have mercy. Let me keep it, and I’ll be in ya debt. My thinker is heavier than my muscles, but I know how to use my ballista, and I can help ye on a dangerous trip. This ingot is my only path forward, roadster.”
                '
                '“Give me the iron, scavenger. Before I report you to the innkeep.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Give me the iron, scavenger. Before I report you to the innkeep.”')
                    $ item_ironingot += 1
                    $ renpy.notify("You received the iron ingot.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the iron ingot.{/i}')
                    $ pyrrhos_gave_ironingot = 1
                    $ pyrrhos_friendship -= 5
                    menu:
                        'Without another word, he nods for you to follow him to his bags. You keep a hand on your blade, just in case, but the man turns back to you with a brick-sized bundle. He unwraps it slowly, allowing you to see the dark ingot. You take it from him, at first underestimating how heavy it is, but {color=#f6d6bd}Pyrrhos{/color} doesn’t risk taking the opportunity.
                        \n\nYou step back. He doesn’t meet your eyes.
                        '
                        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                            jump peltnorthpyrrhos01aboutironingot01
                        '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                            $ pyrrhos_about_highisland_recruitment = 1
                            $ pyrrhos_about_highisland_recruitment_done = 1
                            jump pyrrhos_about_highisland_recruitment_pelt01
                        '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                            $ pyrrhos_about_newplace = day
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                            jump peltnorthpyrrhos01abouthimselfinpeltnorth
                        '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                            $ pyrrhos_quest_reward_debt = day
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                            jump peltnorthpyrrhos01askingforreward
                        '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                            $ pyrrhos_about_peninsula = 1
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                            jump peltnorthpyrrhos01aboutpeninsula
                        '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                            $ pyrrhos_about_himself = 1
                            jump peltnorthpyrrhos01abouthimself
                        '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                            $ pyrrhos_about_undead = 1
                            jump peltnorthpyrrhos01aboutundead
                        '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                            $ pyrrhos_about_thingsleftbehind = 1
                            jump peltnorthpyrrhos01aboutthingsleftbehind
                        '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                            $ pyrrhos_about_ruins = 1
                            jump peltnorthpyrrhos01aboutruins
                        '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                            $ pyrrhos_about_bandits = 1
                            jump peltnorthpyrrhos01aboutbandits
                        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                            $ pyrrhos_about_asterion = 1
                            $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                            jump peltnorthpyrrhos01aboutasterion
                        'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                            $ can_rest = 0
                            $ can_leave = 0
                            $ can_items = 1
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                            jump peltnorth01insidechoosenpc
                        '“Bye.” I go outside.':
                            $ can_rest = 0
                            $ can_items = 1
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                            jump leavingthepeltnorth
                '“Very well. But if you try to leave the peninsula before I collect your debt, I won’t be so kind the next time I find you.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. But if you try to leave the peninsula before I collect your debt, I won’t be so kind the next time I find you.”')
                    $ pyrrhos_debt = 1
                    $ pyrrhos_friendship += 1
                    menu:
                        'He spares you a smirk. “Ye have my word. I’ll wait here for ya call.”
                        '
                        'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                            jump peltnorthpyrrhos01aboutironingot01
                        '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                            $ pyrrhos_about_highisland_recruitment = 1
                            $ pyrrhos_about_highisland_recruitment_done = 1
                            jump pyrrhos_about_highisland_recruitment_pelt01
                        '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                            $ pyrrhos_about_newplace = day
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                            jump peltnorthpyrrhos01abouthimselfinpeltnorth
                        '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                            $ pyrrhos_quest_reward_debt = day
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                            jump peltnorthpyrrhos01askingforreward
                        '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                            $ pyrrhos_about_peninsula = 1
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                            jump peltnorthpyrrhos01aboutpeninsula
                        '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                            $ pyrrhos_about_himself = 1
                            jump peltnorthpyrrhos01abouthimself
                        '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                            $ pyrrhos_about_undead = 1
                            jump peltnorthpyrrhos01aboutundead
                        '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                            $ pyrrhos_about_thingsleftbehind = 1
                            jump peltnorthpyrrhos01aboutthingsleftbehind
                        '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                            $ pyrrhos_about_ruins = 1
                            jump peltnorthpyrrhos01aboutruins
                        '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                            $ pyrrhos_about_bandits = 1
                            jump peltnorthpyrrhos01aboutbandits
                        '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                            $ pyrrhos_about_asterion = 1
                            $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                            jump peltnorthpyrrhos01aboutasterion
                        'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                            $ can_rest = 0
                            $ can_leave = 0
                            $ can_items = 1
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                            jump peltnorth01insidechoosenpc
                        '“Bye.” I go outside.':
                            $ can_rest = 0
                            $ can_items = 1
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                            jump leavingthepeltnorth

    label pyrrhos_about_highisland_recruitment_pelt01:
        menu:
            '“Shit, another boat?” He snorts, rubbing his burnt face. “I’ve no choice, do I? I’ll prepare my ballista, but be sure, I’m doing nothing else for ye.”
            '
            'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                jump peltnorthpyrrhos01aboutironingot01
            '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                $ pyrrhos_about_highisland_recruitment = 1
                $ pyrrhos_about_highisland_recruitment_done = 1
                jump pyrrhos_about_highisland_recruitment_pelt01
            '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                $ pyrrhos_about_newplace = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                jump peltnorthpyrrhos01abouthimselfinpeltnorth
            '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                $ pyrrhos_quest_reward_debt = day
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                jump peltnorthpyrrhos01askingforreward
            '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                $ pyrrhos_about_peninsula = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                jump peltnorthpyrrhos01aboutpeninsula
            '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                $ pyrrhos_about_himself = 1
                jump peltnorthpyrrhos01abouthimself
            '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                $ pyrrhos_about_undead = 1
                jump peltnorthpyrrhos01aboutundead
            '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                $ pyrrhos_about_thingsleftbehind = 1
                jump peltnorthpyrrhos01aboutthingsleftbehind
            '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                $ pyrrhos_about_ruins = 1
                jump peltnorthpyrrhos01aboutruins
            '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                $ pyrrhos_about_bandits = 1
                jump peltnorthpyrrhos01aboutbandits
            '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                $ pyrrhos_about_asterion = 1
                $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                jump peltnorthpyrrhos01aboutasterion
            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            '“Bye.” I go outside.':
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                jump leavingthepeltnorth

    label peltnorthpyrrhos01askingforreward:
        if pyrrhos_peltnorth_counter == day:
            menu:
                '“I don’t have ya coin yet, I should have it tomorrow, when I sell all the iron we were carrying.”
                '
                'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                    jump peltnorthpyrrhos01aboutironingot01
                '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                    $ pyrrhos_about_highisland_recruitment = 1
                    $ pyrrhos_about_highisland_recruitment_done = 1
                    jump pyrrhos_about_highisland_recruitment_pelt01
                '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                    $ pyrrhos_about_newplace = day
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                    jump peltnorthpyrrhos01abouthimselfinpeltnorth
                '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                    $ pyrrhos_quest_reward_debt = day
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                    jump peltnorthpyrrhos01askingforreward
                '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                    $ pyrrhos_about_peninsula = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                    jump peltnorthpyrrhos01aboutpeninsula
                '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                    $ pyrrhos_about_himself = 1
                    jump peltnorthpyrrhos01abouthimself
                '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                    $ pyrrhos_about_undead = 1
                    jump peltnorthpyrrhos01aboutundead
                '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                    $ pyrrhos_about_thingsleftbehind = 1
                    jump peltnorthpyrrhos01aboutthingsleftbehind
                '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                    $ pyrrhos_about_ruins = 1
                    jump peltnorthpyrrhos01aboutruins
                '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                    $ pyrrhos_about_bandits = 1
                    jump peltnorthpyrrhos01aboutbandits
                '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                    $ pyrrhos_about_asterion = 1
                    $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                    jump peltnorthpyrrhos01aboutasterion
                'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                    $ can_rest = 0
                    $ can_leave = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                    jump peltnorth01insidechoosenpc
                '“Bye.” I go outside.':
                    $ can_rest = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                    jump leavingthepeltnorth
        else:
            jump peltnorthpyrrhos01askingforreward02

    label peltnorthpyrrhos01askingforreward02:
        if not pyrrhos_quest_saved:
            $ pyrrhos_quest_reward_debt_paid = 1
            $ coins += 5
            show screen notifyimage( "+5", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+5 {image=cointest}{/i}')
            menu:
                '“And ye shall have it! Ye saved my life, or what’s left of it, and if I could give ye more, I would. B’I need to pay the innkeep for balms on my damn arm, ye see, so here’s as much as we said. Five dragons.”
                '
                'I nod and put the dragons in my pouch. “I have some other questions.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and put the dragons in my pouch. “I have some other questions.”')
                    $ quest_escortpyrrhos = 2
                    $ renpy.notify("Journal updated: Escort The Scavenger")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Escort The Scavenger{/i}')
                    $ quest_escortpyrrhos_description05 = "I’ve got my coin."
                    jump peltnorth01regularquestions
                'I smile and put the dragons in my pouch. “Happy to help.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile and put the dragons in my pouch. “Happy to help.”')
                    $ quest_escortpyrrhos = 2
                    $ renpy.notify("Journal updated: Escort The Scavenger")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Escort The Scavenger{/i}')
                    $ quest_escortpyrrhos_description05 = "I’ve got my coin."
                    jump peltnorth01regularquestionsv02
        else:
            $ pyrrhos_quest_reward_debt_paid = 1
            $ coins += 6
            show screen notifyimage( "+6", "gui/coin2.png")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+6 {image=cointest}{/i}')
            menu:
                '“And ye shall have it! Ye saved my life, or what’s left of it, and thanks to ye, the griffs didn’t tear me to pieces. Here’s what we’ve agreed to, five dragons, and this one coin is for ya help on the road. I hope ye eat and sleep well for it, ye deserve it.”
                '
                'I nod and put the dragons in my pouch. “I have some other questions.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I nod and put the dragons in my pouch. “I have some other questions.”')
                    $ quest_escortpyrrhos = 2
                    $ renpy.notify("Journal updated: Escort The Scavenger")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Escort The Scavenger{/i}')
                    $ quest_escortpyrrhos_description05 = "I’ve got my coin."
                    jump peltnorth01regularquestions
                'I smile and put the dragons in my pouch. “Happy to help.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile and put the dragons in my pouch. “Happy to help.”')
                    $ quest_escortpyrrhos = 2
                    $ renpy.notify("Journal updated: Escort The Scavenger")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Escort The Scavenger{/i}')
                    $ quest_escortpyrrhos_description05 = "I’ve got my coin."
                    jump peltnorth01regularquestionsv02

    label peltnorthpyrrhos01aboutpeninsula:
        $ quarters += 1
        $ description_galerocks01 = "A large fishing village near the northern shore."
        $ description_galerocks02 = "During sunny days, the locals go to the shores to hunt the fish and birds that live there. When it gets dark, they hide behind the walls, boiling water for salt."
        $ description_galerocks03 = "According to {color=#f6d6bd}the scavenger{/color}, the locals are unfriendly, but got more talkative once he helped them with a few tasks."
        menu:
            '“Ye must understand. Yer a roadster, people ask ye for help, they don’t think ye’ll steal from them when they’re in bed,” he pats his bag. “It’s not the same when yer a drifter. They don’t ask me to stay, to marry their kids, or to help them with harvest, they just ask if I {i}plan to pay{/i} for the room, or buy stuff.”
            \n\nYou talk for quite some time, though it’s difficult to uncover the details hidden in his tale.
            \n\nHe claims he and his pack bird came here by boat, about which he refuses to speak. He landed just next to {color=#f6d6bd}Gale Rocks{/color}, a large fishing village near the northern shore. People there were irritable and unwilling to idly chat with him, but “opened their mouths” after he helped them at the smokehouse. On sunny days, the locals hunt on the shore, and when it gets dark, they hide behind the walls, gutting the fish.
            \n\n“And when the weather goes to shit, they boil water for salt and put fish in it, then hop to the barrels, though I don’t know how, they don’t have many trees around. Then they sell the meat to the villages and... And, ye know. Places.” He clears his throat. “For crops.”
            '
            'I let him continue.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I let him continue.')
                $ description_oldpagos04 = "According to {color=#f6d6bd}the scavenger{/color}, the locals “are cold, they spend days praying and talking on and on about their {i}duty{/i}, and are gray like an ashworm.”"
                menu:
                    '“I was told to stay away from {color=#f6d6bd}White Marshes{/color}, though no shell told me why. I joined a group of fish traders who were going to {color=#f6d6bd}Old Págos{/color} and its monastery. B’I hate that place, bah, everyone does,” he shrugs. “I traded there for a bit, ba’the villagers are cold, they spend days praying and talking on and on about their {i}duty{/i}, and are gray like an ashworm. So I left once at dawn, me and my bird, and wasn’t that a mistake!”
                    \n\nHe was attacked by a short bear-like creature. He tried to run away, but following his bird was a bad idea. He fell over in the thicket, so the monster had time to get to him. “I hit it with a bolt, wasn’t enough. I kicked it, so it bites my legs, tears my flesh away. I almost dozed off from pain, ba’can ye believe it? That lazy bird came back and charged at it with its beak!” His dagger was enough to get through the surprised animal’s belly. It ran away.
                    '
                    '“How did you survive with such deep wounds?”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How did you survive with such deep wounds?”')
                        $ description_druids02 = "I can find the local druids in the village of {color=#f6d6bd}Howler’s Dell{/color}, at the western road."
                        $ description_thais03 = "According to {color=#f6d6bd}the scavenger{/color}, she’s a lively soul who enjoys games and jokes. “She’s short, and her blond hair is straight and long. She wears dresses and rouges her cheeks like a merchant.”"
                        $ description_thais03b = "She hates being asked about the origins of her wealth."
                        $ description_howlersdell05 = "The locals are following the teachings of a group of druids."
                        menu:
                            '“The bird was patient, it let me lean on it. My ballista scared griffs away and we got to {color=#f6d6bd}Howler’s Dell{/color}. That’s where I found the elders. They agreed to heal me, b’only for coin, and told me it’s an exception.” After a few questions, you’re sure that by the {i}elders{/i} he means the local druids, held by the villagers in great esteem. “They didn’t want to talk with me a whole lot, said I’m {i}impudent{/i},” his tone is filled with mockery. “Ye hear that? I spent time with {color=#f6d6bd}Thais{/color}, at least she wasn’t so boring.”
                            \n\nYou ask him about her and he’s more than happy to answer. “She’s the mayor, so to speak. Once ye get there, she’ll make sure to see ye. Ye’ll know it’s her. She’s short, and her blond hair is straight and long. She wears dresses and rouges her cheeks like a merchant.” He points at the scar on his own face, which doesn’t help your imagination. “She’s not scary, not scary at all, at least as long as ye don’t ask about her wealth. Tell her a joke or two, drink some mead, or play dice. Her laugh is something else!”
                            '
                            '“So, why did you leave {color=#f6d6bd}Howler’s Dell{/color} alone? It wasn’t smart to move to the ruins all by yourself.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So, why did you leave {color=#f6d6bd}Howler’s Dell{/color} alone? It wasn’t smart to move to the ruins all by yourself.”')
                                $ quarters += 1
                                menu:
                                    '“Ha! It’s my trade. I shouldn’t tell, and I won’t. You already know all that you need to.”
                                    '
                                    'I cross my arms and straighten up. “Give me back the iron you took from the people of {color=#f6d6bd}Gale Rocks{/color}.”' if pyrrhos_about_himself == 2 and galerocks_pastrobbery and not pyrrhos_about_ironingot:
                                        jump peltnorthpyrrhos01aboutironingot01
                                    '“I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and pyrrhos_debt == 1 and not pyrrhos_about_highisland_recruitment:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need your assistance. We’re going to spend a single night on {color=#f6d6bd}High Island{/color}, west of the peninsula.”')
                                        $ pyrrhos_about_highisland_recruitment = 1
                                        $ pyrrhos_about_highisland_recruitment_done = 1
                                        jump pyrrhos_about_highisland_recruitment_pelt01
                                    '“Enjoying your stay?”' if not pyrrhos_about_himselfinpeltnorth and pyrrhos_about_newplace != day:
                                        $ pyrrhos_about_newplace = day
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Enjoying your stay?”')
                                        jump peltnorthpyrrhos01abouthimselfinpeltnorth
                                    '“I came for my reward.”' if not pyrrhos_quest_reward_debt_paid and pyrrhos_quest_reward_debt != day:
                                        $ pyrrhos_quest_reward_debt = day
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I came for my reward.”')
                                        jump peltnorthpyrrhos01askingforreward
                                    '“I want to learn more about the peninsula. Tell me about your travels.”' if not pyrrhos_about_peninsula:
                                        $ pyrrhos_about_peninsula = 1
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want to learn more about the peninsula. Tell me about your travels.”')
                                        jump peltnorthpyrrhos01aboutpeninsula
                                    '“Tell me about yourself.”' if pyrrhos_about_himself < 2:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me about yourself.”')
                                        $ pyrrhos_about_himself = 1
                                        jump peltnorthpyrrhos01abouthimself
                                    '“Are you sure there are no undead in the village where I found you?”' if not pyrrhos_about_undead:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you sure there are no undead in the village where I found you?”')
                                        $ pyrrhos_about_undead = 1
                                        jump peltnorthpyrrhos01aboutundead
                                    '“Have you searched the entire ruins? Are there no hidden treasures left?”' if not pyrrhos_about_thingsleftbehind:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Have you searched the entire ruins? Are there no hidden treasures left?”')
                                        $ pyrrhos_about_thingsleftbehind = 1
                                        jump peltnorthpyrrhos01aboutthingsleftbehind
                                    '“Do you have any idea what happened to the ruined village?”' if not pyrrhos_about_ruins:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Do you have any idea what happened to the ruined village?”')
                                        $ pyrrhos_about_ruins = 1
                                        jump peltnorthpyrrhos01aboutruins
                                    '“I’ve heard about some bandits. Have you seen any hideouts?”' if not pyrrhos_about_bandits and not banditshideout_pcknowswhere and quest_intelforpeltnorth == 1:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about some bandits. Have you seen any hideouts?”')
                                        $ pyrrhos_about_bandits = 1
                                        jump peltnorthpyrrhos01aboutbandits
                                    '“I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”' if not pyrrhos_about_asterion:
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for another roadwarden. A man known as {color=#f6d6bd}Asterion{/color=#f6d6bd}.”')
                                        $ pyrrhos_about_asterion = 1
                                        $ description_asterion04 = "According to {color=#f6d6bd}the scavenger{/color} I met in a ruined village in the South, people in the northern villages were asking him about {color=#f6d6bd}Asterion{/color}, but after a couple of weeks they dropped the topic."
                                        jump peltnorthpyrrhos01aboutasterion
                                    'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                                        $ can_rest = 0
                                        $ can_leave = 0
                                        $ can_items = 1
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                                        jump peltnorth01insidechoosenpc
                                    '“Bye.” I go outside.':
                                        $ can_rest = 0
                                        $ can_items = 1
                                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Bye.” I go outside.')
                                        jump leavingthepeltnorth

    label pyrrhospeltnorth01arrival:
        $ iason_friendship_moneybonus_points += 3
        $ description_pyrrhos03 = "I’ve helped him get to {color=#f6d6bd}Pelt{/color}."
        $ quarters += 1
        $ renpy.force_autosave(take_screenshot=False, block=True)
        $ pc_goal_iwanttohelppoints += 1
        if pyrrhos_quest_saved:
            menu:
                'The man breathes heavily, but doesn’t ask for a break. Once you get close to {color=#f6d6bd}Pelt{/color}, he whistles enthusiastically. “Ye weren’t kidding, ay, what a fortress.” The guards open the gate and take care of the scavenger’s bundles, which {color=#f6d6bd}[horsename]{/color} welcomes with a nicker.
                \n\nThe man introduces himself quickly and once he’s told to speak with {color=#f6d6bd}the innkeeper{/color}, he sighs with relief, stretches out loudly, and looks at you. “Ha! Now I don’t have to point my ballista at the door whenever I hear paws on the ground.”
                \n\nBefore you mention the reward, his face once again gets serious. “So, like I told ye. If ye want ya coins, ye have to come back tomorrow, when my pouch gets heavier. B’I can, and would prefer to, give ye the potion that repels apemen instead. It’s useful, ba’not as much in the South as it is here, in the woods.”
                '
                '“I’ll be here, tomorrow or later. Don’t leave before you pay me. Five dragon bones.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll be here, tomorrow or later. Don’t leave before you pay me. Five dragon bones.”')
                    $ renpy.notify("Journal updated: Escort The Scavenger")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Escort The Scavenger{/i}')
                    $ quest_escortpyrrhos_description05 = "I have to wait for a day before I can can collect my coin in {color=#f6d6bd}Pelt{/color}."
                    jump pyrrhospeltnorth01arrivaliwantcoins
                '“I’ll take the jar.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take the jar.”')
                    $ renpy.notify("Journal updated: Escort The Scavenger")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Escort The Scavenger{/i}')
                    $ quest_escortpyrrhos_description05 = "As a reward, I took a... potion."
                    $ quest_escortpyrrhos = 2
                    $ pyrrhos_quest_reward_debt_paid = 1
                    jump pyrrhospeltnorth01arrivaliwantpotion
        else:
            menu:
                'The man’s sleeve and stomach are soaked with blood, but he tells you to ignore it. Once you get close to {color=#f6d6bd}Pelt{/color}, he whistles enthusiastically. “Ye weren’t kidding, ay, what a fortress.” The guards open the gate and take care of {color=#f6d6bd}the scavenger’s {/color}bundles, which {color=#f6d6bd}[horsename]{/color} welcomes with a nicker.
                \n\nThe man introduces himself quickly and asks to be brought some water from the well. “Thank ye, roadster. I need to ask the innkeep if he has any soap. I’m not going to chop off my damn arm.” He clicks with his tongue. “Ba’like I told ye. If ye want ya coins, ye have to come back tomorrow, when my pouch gets heavier. B’I can, and would prefer to, give ye the potion that repels apemen instead. It’s useful, ba’not as much in the South as it is here, in the woods.”
                '
                '“I’ll be here, tomorrow or later. Don’t leave before you pay me. Five dragon bones.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll be here, tomorrow or later. Don’t leave before you pay me. Five dragon bones.”')
                    $ renpy.notify("Journal updated: Escort The Scavenger")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Escort The Scavenger{/i}')
                    $ quest_escortpyrrhos_description05 = "I have to wait for a day before I can can collect my coin in {color=#f6d6bd}Pelt{/color}."
                    jump pyrrhospeltnorth01arrivaliwantcoins
                '“I’ll take the jar.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll take the jar.”')
                    $ renpy.notify("Journal updated: Escort The Scavenger")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Escort The Scavenger{/i}')
                    $ quest_escortpyrrhos_description05 = "As a reward, I took a... potion."
                    $ quest_escortpyrrhos = 2
                    $ pyrrhos_quest_reward_debt_paid = 1
                    jump pyrrhospeltnorth01arrivaliwantpotion

        label pyrrhospeltnorth01arrivaliwantcoins:
            menu:
                '“Don’t worry, if anything, I can always leave them to the innkeep. I’ll be here for at least a couple of days, ye’ll find me around. After all my recent camping, I’m going to spend a few hours kissing this nice, strong wall.” He starts to laugh and walks away, waving goodbye.
                '
                'I enter the inn.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I enter the inn.')
                    jump peltnorth01inside
                'I approach the guards.' ( condition="quarters < (world_daylength-4)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the guards.')
                    if dalit_firsttime:
                        jump peltnorthtalkingwithguards01
                    else:
                        $ dalit_firsttime = 1
                        jump dalit_firsttime01
                'The guards are currently on watch. They won’t talk with me. (disabled)' ( condition="quarters >= (world_daylength-4)" ):
                    pass
                'I head to the armorer.' ( condition="quarters >= 32 and quarters < (world_daylength-12)" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the armorer.')
                    if peltnorth_armorer_firsttime:
                        jump peltnorthtalkingwitharmorer01
                    else:
                        $ peltnorth_armorer_firsttime = 1
                        jump peltnorthtalkingwitharmorerfirsttime01
                'The armorer is nowhere in sight. (disabled)' ( condition="quarters < 32 or quarters >= (world_daylength-12)" ):
                    pass
                'I go to the well.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to the well.')
                    jump peltnorthwell01
                'I should go outside and forage for berries.' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters <= (world_daylength-4) and not item_peltnorthberries" ):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should to outside and forage for berries.')
                    jump peltnorthleftoversquestforberries02
                'It’s too dark to gather the berries right now. (disabled)' ( condition="iason_food_berries == 1 and item_peltnorthberrytools == 1 and quarters > (world_daylength-4) and not item_peltnorthberries" ):
                    pass
                'I shouldn’t try to gather the berries without the hook. (disabled)' ( condition="iason_food_berries == 1 and not item_peltnorthberrytools and not item_peltnorthberries" ):
                    pass

        label pyrrhospeltnorth01arrivaliwantpotion:
            menu:
                '“Ha, I’m glad!” He unpacks a large jar made of clay. “I’m not gonna lie, roadster, it’s pure troll urine,” he chuckles. “Don’t ask me how I got it, ay? If ye want to scare off some apemen, use it before they see ye. Trolls eat them all the time, so they stay away for as long as they can.”
                \n\nYou imagine that you can feel warmth from the jar. “Well, I won’t miss it. I’ll be here for at least a couple of days, ye’ll find me around if ye need me. After all my recent camping, I’m going to spend a few hours kissing this nice, strong wall.” He starts to laugh and walks away, waving goodbye.
                '
                'I pack the jar and make sure it won’t spill in my bag.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack the jar and make sure it won’t spill in my bag.')
                    $ renpy.notify("You got... Troll urine?")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You got... Troll urine?{/i}')
                    $ item_trollurine = 1
                    jump leavingthepeltnorth02

############################################# BANDIT / The man with no name

label peltnorth01insidetalkingwithbanditALL:
    label peltnorth01insidetalkingwithbandit:
        $ shortcut_darkforest_bandit_peltnorthintroduction = renpy.random.choice(['The man nods without looking at you.', 'The man doesn’t look at you. “Stranger?”', '“What brings you here?”', 'The man looks at you, then turns his head away.', 'The man is heavily breathing, lost in his thoughts.'])
        menu:
            '[shortcut_darkforest_bandit_peltnorthintroduction]
            '
            '“There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_about_highisland_recruitment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”')
                $ shortcut_darkforest_bandit_about_highisland_recruitment = 1
                $ shortcut_darkforest_bandit_about_highisland_recruitment_done = 1
                jump peltnorthbanditaboutdebt01
            '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                $ shortcut_darkforest_bandit_about_reward = 2
                jump peltnorthbanditaboutreward01
            '“So... A bandit?”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So... A bandit?”')
                $ shortcut_darkforest_bandit_about_beingabandit = 1
                jump peltnorthbanditaboutbeingabandit01
            '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                $ shortcut_darkforest_bandit_about_corpse = 2
                $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                jump peltnorthbanditaboutcorpse01
            '“Are you planning to stay here for long?”' if shortcut_darkforest_bandit_about_stayingaround < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                $ shortcut_darkforest_bandit_about_stayingaround = 2
                jump peltnorthbanditaboutstayingaround01
            '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                $ shortcut_darkforest_bandit_about_questions = 1
                jump peltnorthbanditaboutquestions01
            '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump peltnorthbanditconfrontedaboutglauciasquest01
            '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                $ custom1 = "He takes a deep breath and keenly observes your lips."
                jump peltnorthbanditconfrontedaboutglauciasquest01past
            '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump peltnorthbanditconfrontedaboutglauciasquest02
            '“I must say... You don’t look like a regular bandit.”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I must say... You don’t look like a regular bandit.”')
                $ shortcut_darkforest_bandit_about_beingabandit = 1
                jump peltnorthbanditaboutbeingabandit01b
            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            'I go outside.':
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump leavingthepeltnorth

    label peltnorthbanditaboutdebt01:
        menu:
            'He glances at the exit, then scowls at you. “You helped me just to kill me like that? What do I need to take?” You explain your plan briefly, which is greeted by his resigned shrug. “Fine. I’ll wait for you here.”
            '
            '“There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_about_highisland_recruitment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”')
                $ shortcut_darkforest_bandit_about_highisland_recruitment = 1
                $ shortcut_darkforest_bandit_about_highisland_recruitment_done = 1
                jump peltnorthbanditaboutdebt01
            '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                $ shortcut_darkforest_bandit_about_reward = 2
                jump peltnorthbanditaboutreward01
            '“So... A bandit?”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So... A bandit?”')
                $ shortcut_darkforest_bandit_about_beingabandit = 1
                jump peltnorthbanditaboutbeingabandit01
            '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                $ shortcut_darkforest_bandit_about_corpse = 2
                $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                jump peltnorthbanditaboutcorpse01
            '“Are you planning to stay here for long?”' if shortcut_darkforest_bandit_about_stayingaround < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                $ shortcut_darkforest_bandit_about_stayingaround = 2
                jump peltnorthbanditaboutstayingaround01
            '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                $ shortcut_darkforest_bandit_about_questions = 1
                jump peltnorthbanditaboutquestions01
            '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump peltnorthbanditconfrontedaboutglauciasquest01
            '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                $ custom1 = "He takes a deep breath and keenly observes your lips."
                jump peltnorthbanditconfrontedaboutglauciasquest01past
            '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump peltnorthbanditconfrontedaboutglauciasquest02
            '“I must say... You don’t look like a regular bandit.”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I must say... You don’t look like a regular bandit.”')
                $ shortcut_darkforest_bandit_about_beingabandit = 1
                jump peltnorthbanditaboutbeingabandit01b
            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            'I go outside.':
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump leavingthepeltnorth

    label peltnorthbanditaboutreward01:
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
                '“Right, right. You helped me find this place, and I want to be even with you.” He takes a look at the innkeep, but then shrugs. “You’re going to look for the camp of the bandits, stranger. If not now, then another day. You’re just one of those,” his look is absent, wandering to different places. “So listen carefully. Head to the middle of the shortcut, to a pile of stones, then turn north. There’s no path in sight, but don’t worry, you’ll find it soon, you will.”
                \n\nHe pauses. [custom1]
                '
                '“There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_about_highisland_recruitment:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”')
                    $ shortcut_darkforest_bandit_about_highisland_recruitment = 1
                    $ shortcut_darkforest_bandit_about_highisland_recruitment_done = 1
                    jump peltnorthbanditaboutdebt01
                '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                    $ shortcut_darkforest_bandit_about_reward = 2
                    jump peltnorthbanditaboutreward01
                '“So... A bandit?”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and not shortcut_darkforest_bandit_confronted:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So... A bandit?”')
                    $ shortcut_darkforest_bandit_about_beingabandit = 1
                    jump peltnorthbanditaboutbeingabandit01
                '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                    $ shortcut_darkforest_bandit_about_corpse = 2
                    $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                    jump peltnorthbanditaboutcorpse01
                '“Are you planning to stay here for long?”' if shortcut_darkforest_bandit_about_stayingaround < 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                    $ shortcut_darkforest_bandit_about_stayingaround = 2
                    jump peltnorthbanditaboutstayingaround01
                '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                    $ shortcut_darkforest_bandit_about_questions = 1
                    jump peltnorthbanditaboutquestions01
                '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                    $ shortcut_darkforest_bandit_confronted = 1
                    jump peltnorthbanditconfrontedaboutglauciasquest01
                '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                    $ custom1 = "He takes a deep breath and keenly observes your lips."
                    jump peltnorthbanditconfrontedaboutglauciasquest01past
                '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                    $ shortcut_darkforest_bandit_confronted = 1
                    jump peltnorthbanditconfrontedaboutglauciasquest02
                '“I must say... You don’t look like a regular bandit.”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and shortcut_darkforest_bandit_confronted:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I must say... You don’t look like a regular bandit.”')
                    $ shortcut_darkforest_bandit_about_beingabandit = 1
                    jump peltnorthbanditaboutbeingabandit01b
                'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                    $ can_rest = 0
                    $ can_leave = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                    jump peltnorth01insidechoosenpc
                'I go outside.':
                    $ can_rest = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                    jump leavingthepeltnorth
        else:
            $ description_glaucia19 = "According to {color=#f6d6bd}the runaway bandit{/color}, “for as long as she’s backed by the council of {color=#f6d6bd}Gale Rocks{/color}, she has a full stomach and warm togs. She won’t hesitate to kill you if she feels threatened by you.”"
            menu:
                'He gives you an embarrassed look. “I wanted to tell you how to reach {color=#f6d6bd}Glaucia{/color}, but you already know all that.” He approaches the entrance and looks outside, maybe making sure that you’re not being followed. “Be wary of her, stranger. You’d need a large squad to threaten her, and for as long as she’s backed by the council of {color=#f6d6bd}Gale Rocks{/color}, she has a full stomach and warm togs. She won’t hesitate to kill you if she feels threatened by you.”
                '
                '“There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_about_highisland_recruitment:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”')
                    $ shortcut_darkforest_bandit_about_highisland_recruitment = 1
                    $ shortcut_darkforest_bandit_about_highisland_recruitment_done = 1
                    jump peltnorthbanditaboutdebt01
                '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                    $ shortcut_darkforest_bandit_about_reward = 2
                    jump peltnorthbanditaboutreward01
                '“So... A bandit?”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and not shortcut_darkforest_bandit_confronted:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So... A bandit?”')
                    $ shortcut_darkforest_bandit_about_beingabandit = 1
                    jump peltnorthbanditaboutbeingabandit01
                '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                    $ shortcut_darkforest_bandit_about_corpse = 2
                    $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                    jump peltnorthbanditaboutcorpse01
                '“Are you planning to stay here for long?”' if shortcut_darkforest_bandit_about_stayingaround < 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                    $ shortcut_darkforest_bandit_about_stayingaround = 2
                    jump peltnorthbanditaboutstayingaround01
                '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                    $ shortcut_darkforest_bandit_about_questions = 1
                    jump peltnorthbanditaboutquestions01
                '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                    $ shortcut_darkforest_bandit_confronted = 1
                    jump peltnorthbanditconfrontedaboutglauciasquest01
                '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                    $ custom1 = "He takes a deep breath and keenly observes your lips."
                    jump peltnorthbanditconfrontedaboutglauciasquest01past
                '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                    $ shortcut_darkforest_bandit_confronted = 1
                    jump peltnorthbanditconfrontedaboutglauciasquest02
                '“I must say... You don’t look like a regular bandit.”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and shortcut_darkforest_bandit_confronted:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I must say... You don’t look like a regular bandit.”')
                    $ shortcut_darkforest_bandit_about_beingabandit = 1
                    jump peltnorthbanditaboutbeingabandit01b
                'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                    $ can_rest = 0
                    $ can_leave = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                    jump peltnorth01insidechoosenpc
                'I go outside.':
                    $ can_rest = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                    jump leavingthepeltnorth

    label peltnorthbanditaboutstayingaround01:
        menu:
            '“I may. I was asking the people here how much a coin would buy me in {color=#f6d6bd}Hovlavan{/color}, and they said it wouldn’t be much, they did. I need a heavier pouch, and that means work, either here, or on the other side of Hag Hills.” His eyes get warmer. “Let me know when you have something for a fighter. I know how to move through the woods, and how to keep myself in the shadows.”
            '
            '“There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_about_highisland_recruitment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”')
                $ shortcut_darkforest_bandit_about_highisland_recruitment = 1
                $ shortcut_darkforest_bandit_about_highisland_recruitment_done = 1
                jump peltnorthbanditaboutdebt01
            '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                $ shortcut_darkforest_bandit_about_reward = 2
                jump peltnorthbanditaboutreward01
            '“So... A bandit?”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So... A bandit?”')
                $ shortcut_darkforest_bandit_about_beingabandit = 1
                jump peltnorthbanditaboutbeingabandit01
            '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                $ shortcut_darkforest_bandit_about_corpse = 2
                $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                jump peltnorthbanditaboutcorpse01
            '“Are you planning to stay here for long?”' if shortcut_darkforest_bandit_about_stayingaround < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                $ shortcut_darkforest_bandit_about_stayingaround = 2
                jump peltnorthbanditaboutstayingaround01
            '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                $ shortcut_darkforest_bandit_about_questions = 1
                jump peltnorthbanditaboutquestions01
            '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump peltnorthbanditconfrontedaboutglauciasquest01
            '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                $ custom1 = "He takes a deep breath and keenly observes your lips."
                jump peltnorthbanditconfrontedaboutglauciasquest01past
            '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump peltnorthbanditconfrontedaboutglauciasquest02
            '“I must say... You don’t look like a regular bandit.”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I must say... You don’t look like a regular bandit.”')
                $ shortcut_darkforest_bandit_about_beingabandit = 1
                jump peltnorthbanditaboutbeingabandit01b
            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            'I go outside.':
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump leavingthepeltnorth

    label peltnorthbanditaboutcorpse01:
        $ quest_missinghunters_vaschelfound = 1
        $ quest_missinghunters_vaschelknown = 1
        menu:
            '“Let me think... It wasn’t in all that good shape, quite slaughtered, you see. It was a male, I saw them before, name was {color=#f6d6bd}Vaschel{/color}. Darker than me, black hair, this tall,” he raises his hand to estimate the person’s size. “Was wearing leather, brown and green, them people at {color=#f6d6bd}Creeks{/color} wear such things all the time. He had scraps of his face, he did, and here,” he points to his left ear, “he had an animal bone, an earling.”
            '
            '“There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_about_highisland_recruitment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”')
                $ shortcut_darkforest_bandit_about_highisland_recruitment = 1
                $ shortcut_darkforest_bandit_about_highisland_recruitment_done = 1
                jump peltnorthbanditaboutdebt01
            '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                $ shortcut_darkforest_bandit_about_reward = 2
                jump peltnorthbanditaboutreward01
            '“So... A bandit?”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So... A bandit?”')
                $ shortcut_darkforest_bandit_about_beingabandit = 1
                jump peltnorthbanditaboutbeingabandit01
            '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                $ shortcut_darkforest_bandit_about_corpse = 2
                $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                jump peltnorthbanditaboutcorpse01
            '“Are you planning to stay here for long?”' if shortcut_darkforest_bandit_about_stayingaround < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                $ shortcut_darkforest_bandit_about_stayingaround = 2
                jump peltnorthbanditaboutstayingaround01
            '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                $ shortcut_darkforest_bandit_about_questions = 1
                jump peltnorthbanditaboutquestions01
            '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump peltnorthbanditconfrontedaboutglauciasquest01
            '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                $ custom1 = "He takes a deep breath and keenly observes your lips."
                jump peltnorthbanditconfrontedaboutglauciasquest01past
            '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump peltnorthbanditconfrontedaboutglauciasquest02
            '“I must say... You don’t look like a regular bandit.”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I must say... You don’t look like a regular bandit.”')
                $ shortcut_darkforest_bandit_about_beingabandit = 1
                jump peltnorthbanditaboutbeingabandit01b
            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            'I go outside.':
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump leavingthepeltnorth

    label peltnorthbanditaboutquestions01:
        menu:
            'He shrugs. “I don’t care. I’ve no reason to amuse you. And I’ve made a pledge to keep things to myself.”
            '
            '“There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_about_highisland_recruitment:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”')
                $ shortcut_darkforest_bandit_about_highisland_recruitment = 1
                $ shortcut_darkforest_bandit_about_highisland_recruitment_done = 1
                jump peltnorthbanditaboutdebt01
            '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                $ shortcut_darkforest_bandit_about_reward = 2
                jump peltnorthbanditaboutreward01
            '“So... A bandit?”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So... A bandit?”')
                $ shortcut_darkforest_bandit_about_beingabandit = 1
                jump peltnorthbanditaboutbeingabandit01
            '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                $ shortcut_darkforest_bandit_about_corpse = 2
                $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                jump peltnorthbanditaboutcorpse01
            '“Are you planning to stay here for long?”' if shortcut_darkforest_bandit_about_stayingaround < 2:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                $ shortcut_darkforest_bandit_about_stayingaround = 2
                jump peltnorthbanditaboutstayingaround01
            '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                $ shortcut_darkforest_bandit_about_questions = 1
                jump peltnorthbanditaboutquestions01
            '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump peltnorthbanditconfrontedaboutglauciasquest01
            '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                $ custom1 = "He takes a deep breath and keenly observes your lips."
                jump peltnorthbanditconfrontedaboutglauciasquest01past
            '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                $ shortcut_darkforest_bandit_confronted = 1
                jump peltnorthbanditconfrontedaboutglauciasquest02
            '“I must say... You don’t look like a regular bandit.”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and shortcut_darkforest_bandit_confronted:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I must say... You don’t look like a regular bandit.”')
                $ shortcut_darkforest_bandit_about_beingabandit = 1
                jump peltnorthbanditaboutbeingabandit01b
            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                $ can_rest = 0
                $ can_leave = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                jump peltnorth01insidechoosenpc
            'I go outside.':
                $ can_rest = 0
                $ can_items = 1
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                jump leavingthepeltnorth

    label peltnorthbanditaboutbeingabandit01:
        menu:
            'He looks at you with a raised eyebrow, but avoids your eyes. “You must have known already. Or are you surprised?”
            '
            '“I wanted to be sure before I threw around accusations.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I wanted to be sure before I threw around accusations.”')
                $ custom1 = "“You may be the only soul in this place who would give me more than a harsh look,” his blue eyes get brighter."
                jump peltnorthbanditaboutbeingabandit02
            '“You don’t look like a regular bandit.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t look like a regular bandit.”')
                label peltnorthbanditaboutbeingabandit01b:
                    menu:
                        'He looks puzzled. “And what do I look like?”
                        '
                        '“Clean.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Clean.”')
                            $ shortcut_darkforest_bandit_friendship += 1
                            $ custom1 = "“What can I say, I’m trying, unlike some. My head gets cloudy when it smells my own dirt.” His wide smile makes his blue eyes genial."
                            jump peltnorthbanditaboutbeingabandit02
                        'I smile. “Handsome.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Handsome.”')
                            $ shortcut_darkforest_bandit_friendship += 1
                            $ custom1 = "He looks at you in silence, then allows himself a chuckle. “I don’t know, thank you, I think. Many handsome folks are plowing the fields, they just don’t have the time to shave.” His blue eyes get brighter."
                            jump peltnorthbanditaboutbeingabandit02
                        '“Like an assassin.”':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Like an assassin.”')
                            $ custom1 = "“Well, some people would like me to be one, but I’d rather not. My soul is already heavy, I’d rather not add to it more burden,” he looks at his blade."
                            jump peltnorthbanditaboutbeingabandit02
            '“I judge people by their actions. Prejudice is a weakness.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I judge people by their actions. Prejudice is a weakness.”')
                $ custom1 = "He collects his thoughts. “You have to be slow to think one would just hang around a cave in the middle of the woods. Though maybe not as slow as one who actually did it,” he strokes his shaved chin."
                jump peltnorthbanditaboutbeingabandit02

        label peltnorthbanditaboutbeingabandit02:
            if shortcut_darkforest_bandit_confronted == 1:
                $ custom2 = "\n\n“Well, I’m a new soul now. {color=#f6d6bd}Glaucia{/color} is pushing things too far, too much, and I ain’t one to stay on a ship that’s heading for the rocks. I left before we turned into nought but murderers.” His fingers are getting pale from clutching the dagger’s handle."
            else:
                $ custom2 = "\n\n“Well, I’m a new soul now. {color=#f6d6bd}Glaucia{/color} is pushing things too far, too much, and I ain’t one to stay on a ship that’s heading for the rocks. I left before we turned into nought but murderers.” His fingers are getting pale from clutching the dagger’s handle. “Don’t you think about locking me up, stranger. We’re still in my land, no tribe is going to keep a prisoner like me, and I know you won’t take me South now. I’ll start a new life, and you won’t get in my way.”"
            $ description_glaucia09 = "According to the bandit I met in the heart of the woods, she’s “pushing things too far, too much.” He left her “before we turned into nought but murderers.”"
            menu:
                '[custom1][custom2]
                '
                '“There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_about_highisland_recruitment:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”')
                    $ shortcut_darkforest_bandit_about_highisland_recruitment = 1
                    $ shortcut_darkforest_bandit_about_highisland_recruitment_done = 1
                    jump peltnorthbanditaboutdebt01
                '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                    $ shortcut_darkforest_bandit_about_reward = 2
                    jump peltnorthbanditaboutreward01
                '“So... A bandit?”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and not shortcut_darkforest_bandit_confronted:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So... A bandit?”')
                    $ shortcut_darkforest_bandit_about_beingabandit = 1
                    jump peltnorthbanditaboutbeingabandit01
                '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                    $ shortcut_darkforest_bandit_about_corpse = 2
                    $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                    jump peltnorthbanditaboutcorpse01
                '“Are you planning to stay here for long?”' if shortcut_darkforest_bandit_about_stayingaround < 2:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                    $ shortcut_darkforest_bandit_about_stayingaround = 2
                    jump peltnorthbanditaboutstayingaround01
                '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                    $ shortcut_darkforest_bandit_about_questions = 1
                    jump peltnorthbanditaboutquestions01
                '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                    $ shortcut_darkforest_bandit_confronted = 1
                    jump peltnorthbanditconfrontedaboutglauciasquest01
                '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                    $ custom1 = "He takes a deep breath and keenly observes your lips."
                    jump peltnorthbanditconfrontedaboutglauciasquest01past
                '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                    $ shortcut_darkforest_bandit_confronted = 1
                    jump peltnorthbanditconfrontedaboutglauciasquest02
                '“I must say... You don’t look like a regular bandit.”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and shortcut_darkforest_bandit_confronted:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I must say... You don’t look like a regular bandit.”')
                    $ shortcut_darkforest_bandit_about_beingabandit = 1
                    jump peltnorthbanditaboutbeingabandit01b
                'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                    $ can_rest = 0
                    $ can_leave = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                    jump peltnorth01insidechoosenpc
                'I go outside.':
                    $ can_rest = 0
                    $ can_items = 1
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                    jump leavingthepeltnorth

        label peltnorthbanditconfrontedaboutglauciasquestALL:
            label peltnorthbanditconfrontedaboutglauciasquest01:
                $ shortcut_bandit_identity = 1
                menu:
                    'His breath gets heavier, and after you notice him reaching for something behind his back, he rests his shoulders on the table, and turns toward you his empty palms. “Please,” he whispers. “She’ll kill me.”
                    '
                    '“Tell me your story.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Tell me your story.”')
                        $ custom1 = "“There ain’t much of one. Wanted to be a free soul, hunt beasts, maybe take away a little something from what merchants keep in their lake-deep pockets. But {color=#f6d6bd}Glaucia’s{/color} obsessed with {color=#f6d6bd}White Marshes{/color} and their {i}awoken{/i}. She told me my day is coming, that it’s time to do my share of {i}work{/i}. But I won’t murder in her name, I won’t.” With every word, he speaks a bit quicker, and ends his tale with a flinch, as if a bad memory just pinched his ear."
                        jump peltnorthbanditconfrontedaboutglauciasquest01past

            label peltnorthbanditconfrontedaboutglauciasquest01past:
                menu:
                    '[custom1]
                    '
                    '“Just give me the things you stole from her. I’ll try to convince her to forget about all this.”' if glaucia_about_runaway_bonusquestion6 and not shortcut_darkforest_bandit_confronted_question1:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just give me the things you stole from her. I’ll try to convince her to forget about all this.”')
                        $ custom1 = "“I... don’t have it,” he looks away. “I got all them powder soggy. I tried to then use it to torch some wood, but that was {i}not{/i} a good idea.”"
                        $ shortcut_darkforest_bandit_confronted_question1 = 1
                        jump peltnorthbanditconfrontedaboutglauciasquest01past
                    '“Can I be sure you won’t just look for another band once you cross {color=#f6d6bd}Hag Hills{/color}?”' if not shortcut_darkforest_bandit_confronted_question3:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can I be sure you won’t just look for another band once you cross {color=#f6d6bd}Hag Hills{/color}?”')
                        $ custom1 = "“I don’t know much about the lands in the south, but they can’t be as bad as they are here,” you consider refuting his statement, but he carries on. “I may stay at a few inns, and get to {color=#f6d6bd}Hovlavan{/color} before winter with a heavy pouch. I have skills,” he spares you a charming smirk, “that I could put there to hire.”"
                        $ shortcut_darkforest_bandit_confronted_question3 = 1
                        jump peltnorthbanditconfrontedaboutglauciasquest01past
                    '“What are those {i}skills{/i} of yours?”' if shortcut_darkforest_bandit_confronted_question4 and not shortcut_darkforest_bandit_confronted_question4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “What are those {i}skills{/i} of yours?”')
                        $ custom1 = "“Quick legs, fast hands, a healthy back... Oh, and I can blend in with shadows, if I’m rested.” Seeing your frown, he gives you a dishonest smile, but his eyes are as tense as his teeth are white. “You didn’t think I was staying around for so long all playing fair, did you? I don’t care who’s going to hire me. Priests, merchants, officials, even adventurers. They’ll sure pay me better than {color=#f6d6bd}Glaucia{/color} did.”"
                        $ shortcut_darkforest_bandit_confronted_question4 = 1
                        jump peltnorthbanditconfrontedaboutglauciasquest01past
                    '“Helping you may turn out to be costly. What can you give me in return?”' if not shortcut_darkforest_bandit_confronted_question2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Helping you may turn out to be costly. What can you give me in return?”')
                        $ custom1 = "He falls quiet. He glances at his knife, which is made of fine steel, but has a rather simple handle. “I’m broke,” he purses his lips, “but you may need my help, one day. I could help you get to a dangerous place, even fight beasts for you. And then, maybe I’ll join you on your ride to the city, alright? You’ll find me here, I’ll wait.”"
                        $ shortcut_darkforest_bandit_confronted_question2 = 1
                        jump peltnorthbanditconfrontedaboutglauciasquest01past
                    '“Very well. I’ll cover for you for {color=#f6d6bd}Glaucia{/color}. Wait for me here until the end of summer.”' if shortcut_darkforest_bandit_confronted_question2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Very well. I’ll cover for you for {color=#f6d6bd}Glaucia{/color}. Wait for me here until the end of summer.”')
                        label peltnorthbanditconfrontedaboutglauciasquest02:
                            $ shortcut_darkforest_bandit_promisedtocoverforhim = 1
                            $ pc_goal_iwanttohelppoints += 1
                            $ description_glaucia20 = "According to {color=#f6d6bd}the runaway bandit{/color}, “her gratitude goes only as far as it takes to spare one’s life. She thinks she’s saving the innocent and punishing the monsters, so in her view it’s {i}us{/i} who should be grateful to {i}her{/i}.”"
                            menu:
                                '“You won’t regret this,” he gives you a grateful nod. “Her gratitude goes only as far as it takes to spare one’s life. She thinks she’s saving the innocent and punishing the monsters, so in her view it’s {i}us{/i} who should be grateful to {i}her{/i}.”
                                '
                                '“There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_about_highisland_recruitment:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”')
                                    $ shortcut_darkforest_bandit_about_highisland_recruitment = 1
                                    $ shortcut_darkforest_bandit_about_highisland_recruitment_done = 1
                                    jump peltnorthbanditaboutdebt01
                                '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                                    $ shortcut_darkforest_bandit_about_reward = 2
                                    jump peltnorthbanditaboutreward01
                                '“So... A bandit?”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and not shortcut_darkforest_bandit_confronted:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So... A bandit?”')
                                    $ shortcut_darkforest_bandit_about_beingabandit = 1
                                    jump peltnorthbanditaboutbeingabandit01
                                '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                                    $ shortcut_darkforest_bandit_about_corpse = 2
                                    $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                                    jump peltnorthbanditaboutcorpse01
                                '“Are you planning to stay here for long?”' if shortcut_darkforest_bandit_about_stayingaround < 2:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                                    $ shortcut_darkforest_bandit_about_stayingaround = 2
                                    jump peltnorthbanditaboutstayingaround01
                                '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                                    $ shortcut_darkforest_bandit_about_questions = 1
                                    jump peltnorthbanditaboutquestions01
                                '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                                    $ shortcut_darkforest_bandit_confronted = 1
                                    jump peltnorthbanditconfrontedaboutglauciasquest01
                                '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                                    $ custom1 = "He takes a deep breath and keenly observes your lips."
                                    jump peltnorthbanditconfrontedaboutglauciasquest01past
                                '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                                    $ shortcut_darkforest_bandit_confronted = 1
                                    jump peltnorthbanditconfrontedaboutglauciasquest02
                                '“I must say... You don’t look like a regular bandit.”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and shortcut_darkforest_bandit_confronted:
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I must say... You don’t look like a regular bandit.”')
                                    $ shortcut_darkforest_bandit_about_beingabandit = 1
                                    jump peltnorthbanditaboutbeingabandit01b
                                'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                                    $ can_rest = 0
                                    $ can_leave = 0
                                    $ can_items = 1
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                                    jump peltnorth01insidechoosenpc
                                'I go outside.':
                                    $ can_rest = 0
                                    $ can_items = 1
                                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                                    jump leavingthepeltnorth
                    '“I want nothing to do with a bandit, but I’m not going to use your life as a ware to sell. Just leave the peninsula, and right now.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I want nothing to do with a bandit, but I’m not going to use your life as a ware to sell. Just leave the peninsula, and right now.”')
                        $ shortcut_darkforest_bandit_leftthepeninsula = 1
                        $ shortcut_bandit_peltnorth_fluff = ""
                        $ peltnorth_bonusnpcs -= 1
                        $ shortcut_darkforest_bandit_inpeltnorth = 0
                        $ shortcut_darkforest_bandit_leftFROMpeltnorth = 1
                        menu:
                            'He gives you a long look, then, without a word, grabs his sparse belongings, places a dragon bone on the counter, and leaves the inn - for good.
                            '
                            'I go to {color=#f6d6bd}the innkeeper{/color}.':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the innkeeper{/color}.')
                                jump peltnorth01insidetalkingwithiasonalt
                            'I join {color=#f6d6bd}Tulia{/color}.' if tulia_pelt_inside and not tulia_pelt_left:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I join {color=#f6d6bd}Tulia{/color}.')
                                $ can_rest = 0
                                jump peltnorth01insidetalkingwithtulia01
                            'I approach {color=#f6d6bd}Pyrrhos{/color}.' if pyrrhos_peltnorth == 1 and description_pyrrhos01:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Pyrrhos{/color}.')
                                $ can_rest = 0
                                jump peltnorth01insidetalkingwithpyrrhos
                            'I approach {color=#f6d6bd}the scavenger{/color}.' if pyrrhos_peltnorth == 1 and not description_pyrrhos01:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}the scavenger{/color}.')
                                $ can_rest = 0
                                jump peltnorth01insidetalkingwithpyrrhos
                            'I speak to {color=#f6d6bd}the man without a name{/color}.' if shortcut_darkforest_bandit_inpeltnorth == 1 and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll and not shortcut_bandit_identity:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I speak to {color=#f6d6bd}the man without a name{/color}.')
                                $ can_rest = 0
                                jump peltnorth01insidetalkingwithbandit
                            'I speak to {color=#f6d6bd}the bandit{/color}.' if shortcut_darkforest_bandit_inpeltnorth == 1 and not shortcut_darkforest_bandit_leftFROMpeltnorth and not shortcut_darkforest_bandit_dead_troll and shortcut_bandit_identity:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I speak to {color=#f6d6bd}the bandit{/color}.')
                                $ can_rest = 0
                                jump peltnorth01insidetalkingwithbandit
                            'I step toward {color=#f6d6bd}Quintus{/color}.' if quintus_pelt_firsttime and not quintus_pelt_left:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step toward {color=#f6d6bd}Quintus{/color}.')
                                $ can_rest = 0
                                jump peltnorth01insidetalkingwithquintus01
                            'I go outside.':
                                $ can_rest = 0
                                $ can_items = 1
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                                jump leavingthepeltnorth
                    '“I need to think about all this.”' if shortcut_darkforest_bandit_confronted_question2:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I need to think about all this.”')
                        menu:
                            '“Don’t play with me, stranger,” he growls. “I’m not going to sit around and wait for your mercy without end.”
                            '
                            '“There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”' if not asterion_found and quest_asterion == 1 and quest_gatheracrew == 1 and shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_about_highisland_recruitment:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “There’s a way for you to pay off your debt. You’ll assist me in a short journey to {color=#f6d6bd}High Island{/color}.”')
                                $ shortcut_darkforest_bandit_about_highisland_recruitment = 1
                                $ shortcut_darkforest_bandit_about_highisland_recruitment_done = 1
                                jump peltnorthbanditaboutdebt01
                            '“You wanted to talk with me.”' if not shortcut_darkforest_bandit_about_reward:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You wanted to talk with me.”')
                                $ shortcut_darkforest_bandit_about_reward = 2
                                jump peltnorthbanditaboutreward01
                            '“So... A bandit?”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and not shortcut_darkforest_bandit_confronted:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “So... A bandit?”')
                                $ shortcut_darkforest_bandit_about_beingabandit = 1
                                jump peltnorthbanditaboutbeingabandit01
                            '“I still need to know who was the soul devoured by the furless wolf.”' if shortcut_darkforest_bandit_about_corpse < 2 and not shortcut_darkforest_furlesswolf_corpseidentity and not shortcut_darkforest_furlesswolf_studyingthecorpse:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I still need to know who was the soul devoured by the furless wolf.')
                                $ shortcut_darkforest_bandit_about_corpse = 2
                                $ shortcut_darkforest_furlesswolf_corpseidentity = 1
                                jump peltnorthbanditaboutcorpse01
                            '“Are you planning to stay here for long?”' if shortcut_darkforest_bandit_about_stayingaround < 2:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Are you planning to stay here for long?”')
                                $ shortcut_darkforest_bandit_about_stayingaround = 2
                                jump peltnorthbanditaboutstayingaround01
                            '“I have some questions about the peninsula.”' if not shortcut_darkforest_bandit_about_questions and shortcut_darkforest_bandit_about_reward:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have some questions about the peninsula.”')
                                $ shortcut_darkforest_bandit_about_questions = 1
                                jump peltnorthbanditaboutquestions01
                            '“{color=#f6d6bd}Glaucia{/color} is looking for you.”' if quest_runaway and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_confronted:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Glaucia{/color} is looking for you.”')
                                $ shortcut_darkforest_bandit_confronted = 1
                                jump peltnorthbanditconfrontedaboutglauciasquest01
                            '“Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”' if quest_runaway and not shortcut_darkforest_bandit_killed and shortcut_darkforest_bandit_confronted and not shortcut_darkforest_bandit_promisedtocoverforhim:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Let’s talk about your past with {color=#f6d6bd}Glaucia{/color}.”')
                                $ custom1 = "He takes a deep breath and keenly observes your lips."
                                jump peltnorthbanditconfrontedaboutglauciasquest01past
                            '“My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”' if (shortcut_darkforest_bandit_confronted and quest_runaway == 3 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2) or (shortcut_darkforest_bandit_confronted and quest_runaway == 2 and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_promisedtocoverforhim and shortcut_darkforest_bandit_confronted_question2):
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “My deal with {color=#f6d6bd}Glaucia{/color} is done. You’re safe, for now.”')
                                $ shortcut_darkforest_bandit_confronted = 1
                                jump peltnorthbanditconfrontedaboutglauciasquest02
                            '“I must say... You don’t look like a regular bandit.”' if shortcut_bandit_identity and not shortcut_darkforest_bandit_about_beingabandit and shortcut_darkforest_bandit_confronted:
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I must say... You don’t look like a regular bandit.”')
                                $ shortcut_darkforest_bandit_about_beingabandit = 1
                                jump peltnorthbanditaboutbeingabandit01b
                            'I take another look at the main hall.' if peltnorth_bonusnpcs > 0:
                                $ can_rest = 0
                                $ can_leave = 0
                                $ can_items = 1
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the main hall.')
                                jump peltnorth01insidechoosenpc
                            'I go outside.':
                                $ can_rest = 0
                                $ can_items = 1
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go outside.')
                                jump leavingthepeltnorth

############################################# ARMORER

label peltnorthtalkingwitharmorerALL:
    label peltnorthtalkingwitharmorerfirsttime01:
        $ shop = "peltnorth_armorer"
        $ can_rest = 0
        $ can_items = 0
        $ can_leave = 0
        menu:
            'You walk past the well and find a small, open shed, not unlike the stable, but with a humble set of tables, carving tools, hammers, sharpening stones, pincers, knives, and other tools. As long as something can be solved by brute force, this place will find a way to do so.
            \n\nThere are two people sitting on a long bench. The first one is a male with maybe inch-long hair, a cleanly shaven face, a thin, long, yellow tunic, bare legs, and sandals. He ignores your presence, sewing a gambeson with great concentration.
            \n\nThe second person is a boy, maybe fifteen, who’s wearing the crude outfit of a farmer. He glances at you, but soon returns to sharpening a long dagger.
            '
            '“Greetings.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Greetings.”')
                menu:
                    'The man raises his head, but it’s the boy who speaks, focused on his task. “He ain’t talking. Tell him what it is that you need.”
                    \n\nThe man smiles in confirmation, looks at the piece of garment in his hands, then looks around, shrugs, and returns to you with a raised eyebrow.
                    '
                    '{image=cointest} “I’m in need of your services.”' if (peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                        jump peltnorth_armorer_aboutservices02
                    '{image=coingray} My gambeson needs no repairs. (disabled)' if (peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                        pass
                    '{image=cointest} “I’m in need of your services.”' if (not peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                        jump peltnorth_armorer_aboutservices01
                    '{image=cointest} “Maybe not right now, but I may be in need of your services.”' if (not peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                        jump peltnorth_armorer_aboutservices01
                    '“I feel like this gambeson could use some adjustments.”' if peltnorth_armorer_abouttrade and armor == 3 and not armor_can4 and not peltnorth_armorer_aboutarmor_can4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Maybe not right now, but I may be in need of your services.”')
                        jump peltnorth_armorer_aboutarmor_can401
                    '“Can you patch my clothes?”' if cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
                        jump peltnorth_armorer_aboutcleanliness_clothes_torn01
                    '“Could you patch my clothes if they were torn?”' if not cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
                        jump peltnorth_armorer_aboutcleanliness_clothes_torn01alt
                    '“I could use some earplugs... I’ve had a few issues with a pack of howlers.”' if not item_earplugs and northernroad_firsttime and not peltnorth_armorer_aboutearplugs:
                        jump peltnorth_armorer_aboutearplugs01
                    '“Could you give me a new handle for this axe head?”' if item_axehead:
                        jump peltnorth_armorer_aboutaxehead01
                    'I look at the youngster. “Learning the trade, I see?”' if not peltnorth_armorer_aboutthemselves:
                        jump peltnorth_armorer_aboutthemselves01
                    'I leave the shed.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the shed.')
                        jump leavingthepeltnorth02
            'I wait for him to notice me.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wait for him to notice me.')
                $ minutes += 5
                menu:
                    'After a few minutes, the man finishes his task and raises his head. He puts away the piece of garment on a table, stands up, bows to you, and shrugs, waiting for you to speak.
                    '
                    '{image=cointest} “I’m in need of your services.”' if (peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                        jump peltnorth_armorer_aboutservices02
                    '{image=coingray} My gambeson needs no repairs. (disabled)' if (peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                        pass
                    '{image=cointest} “I’m in need of your services.”' if (not peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                        jump peltnorth_armorer_aboutservices01
                    '{image=cointest} “Maybe not right now, but I may be in need of your services.”' if (not peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                        jump peltnorth_armorer_aboutservices01
                    '“I feel like this gambeson could use some adjustments.”' if peltnorth_armorer_abouttrade and armor == 3 and not armor_can4 and not peltnorth_armorer_aboutarmor_can4:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Maybe not right now, but I may be in need of your services.”')
                        jump peltnorth_armorer_aboutarmor_can401
                    '“Can you patch my clothes?”' if cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
                        jump peltnorth_armorer_aboutcleanliness_clothes_torn01
                    '“Could you patch my clothes if they were torn?”' if not cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
                        jump peltnorth_armorer_aboutcleanliness_clothes_torn01alt
                    '“I could use some earplugs... I’ve had a few issues with a pack of howlers.”' if not item_earplugs and northernroad_firsttime and not peltnorth_armorer_aboutearplugs:
                        jump peltnorth_armorer_aboutearplugs01
                    '“Could you give me a new handle for this axe head?”' if item_axehead:
                        jump peltnorth_armorer_aboutaxehead01
                    'I look at the youngster. “Learning the trade, I see?”' if not peltnorth_armorer_aboutthemselves:
                        jump peltnorth_armorer_aboutthemselves01
                    'I leave the shed.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the shed.')
                        jump leavingthepeltnorth02

    label peltnorthtalkingwitharmorer01:
        $ shop = "peltnorth_armorer"
        $ can_rest = 0
        $ can_items = 0
        $ can_leave = 0
        menu:
            '{color=#f6d6bd}The armorer{/color} is focused on his repetitive tasks.
            '
            '{image=cointest} “I’m in need of your services.”' if (peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                jump peltnorth_armorer_aboutservices02
            '{image=coingray} My gambeson needs no repairs. (disabled)' if (peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                pass
            '{image=cointest} “I’m in need of your services.”' if (not peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                jump peltnorth_armorer_aboutservices01
            '{image=cointest} “Maybe not right now, but I may be in need of your services.”' if (not peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                jump peltnorth_armorer_aboutservices01
            '“I feel like this gambeson could use some adjustments.”' if peltnorth_armorer_abouttrade and armor == 3 and not armor_can4 and not peltnorth_armorer_aboutarmor_can4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Maybe not right now, but I may be in need of your services.”')
                jump peltnorth_armorer_aboutarmor_can401
            '“Can you patch my clothes?”' if cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
                jump peltnorth_armorer_aboutcleanliness_clothes_torn01
            '“Could you patch my clothes if they were torn?”' if not cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
                jump peltnorth_armorer_aboutcleanliness_clothes_torn01alt
            '“I could use some earplugs... I’ve had a few issues with a pack of howlers.”' if not item_earplugs and northernroad_firsttime and not peltnorth_armorer_aboutearplugs:
                jump peltnorth_armorer_aboutearplugs01
            '“Could you give me a new handle for this axe head?”' if item_axehead:
                jump peltnorth_armorer_aboutaxehead01
            'I look at the youngster. “Learning the trade, I see?”' if not peltnorth_armorer_aboutthemselves:
                jump peltnorth_armorer_aboutthemselves01
            'I leave the shed.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the shed.')
                jump leavingthepeltnorth02

    label peltnorth_armorer_aboutservices01:
        $ peltnorth_armorer_abouttrade = 1
        $ renpy.notify("New trader unlocked.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
        $ minutes += 5
        menu:
            'He nods, points at the laces in the front of your jacket, raises his clenched fingers to his shoulders, then gently spreads and lowers them, as if he’s taking off a robe. You follow his command and allow him to properly inspect your gambeson.
            \n\nAfter a few minutes, he gives it back, then reaches for his pouch. He pulls out one dragon bone, shrugs, then another one and waves both of them in the air, pursing his lips. He makes a few speech-like noises with his empty mouth, groaning what sounds like “I don’t know.”
            '
            'I consider his offer.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider his offer.')
                show screen shopscreen with dissolve
                jump peltnorthtalkingwitharmorer01

    label peltnorth_armorer_aboutservices02:
        $ shop = "peltnorth_armorer"
        show screen shopscreen with dissolve
        menu:
            'He nods and prepares his tools.
            '
            '{image=cointest} “I’m in need of your services.”' if (peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                jump peltnorth_armorer_aboutservices02
            '{image=coingray} My gambeson needs no repairs. (disabled)' if (peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                pass
            '{image=cointest} “I’m in need of your services.”' if (not peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                jump peltnorth_armorer_aboutservices01
            '{image=cointest} “Maybe not right now, but I may be in need of your services.”' if (not peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                jump peltnorth_armorer_aboutservices01
            '“I feel like this gambeson could use some adjustments.”' if peltnorth_armorer_abouttrade and armor == 3 and not armor_can4 and not peltnorth_armorer_aboutarmor_can4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Maybe not right now, but I may be in need of your services.”')
                jump peltnorth_armorer_aboutarmor_can401
            '“Can you patch my clothes?”' if cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
                jump peltnorth_armorer_aboutcleanliness_clothes_torn01
            '“Could you patch my clothes if they were torn?”' if not cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
                jump peltnorth_armorer_aboutcleanliness_clothes_torn01alt
            '“I could use some earplugs... I’ve had a few issues with a pack of howlers.”' if not item_earplugs and northernroad_firsttime and not peltnorth_armorer_aboutearplugs:
                jump peltnorth_armorer_aboutearplugs01
            '“Could you give me a new handle for this axe head?”' if item_axehead:
                jump peltnorth_armorer_aboutaxehead01
            'I look at the youngster. “Learning the trade, I see?”' if not peltnorth_armorer_aboutthemselves:
                jump peltnorth_armorer_aboutthemselves01
            'I leave the shed.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the shed.')
                jump leavingthepeltnorth02

    label peltnorth_armorer_aboutarmor_can401:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I feel like this gambeson could use some adjustments.”')
        $ peltnorth_armorer_aboutarmor_can4 = 1
        menu:
            'He nods enthusiastically, but then apologetically points behind him, at a small box filled with basic tools. “He ain’t that experienced,” says his assistant. “We do this and that, but only the simple things.”
            '
            '{image=cointest} “I’m in need of your services.”' if (peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                jump peltnorth_armorer_aboutservices02
            '{image=coingray} My gambeson needs no repairs. (disabled)' if (peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                pass
            '{image=cointest} “I’m in need of your services.”' if (not peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                jump peltnorth_armorer_aboutservices01
            '{image=cointest} “Maybe not right now, but I may be in need of your services.”' if (not peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                jump peltnorth_armorer_aboutservices01
            '“I feel like this gambeson could use some adjustments.”' if peltnorth_armorer_abouttrade and armor == 3 and not armor_can4 and not peltnorth_armorer_aboutarmor_can4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Maybe not right now, but I may be in need of your services.”')
                jump peltnorth_armorer_aboutarmor_can401
            '“Can you patch my clothes?”' if cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
                jump peltnorth_armorer_aboutcleanliness_clothes_torn01
            '“Could you patch my clothes if they were torn?”' if not cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
                jump peltnorth_armorer_aboutcleanliness_clothes_torn01alt
            '“I could use some earplugs... I’ve had a few issues with a pack of howlers.”' if not item_earplugs and northernroad_firsttime and not peltnorth_armorer_aboutearplugs:
                jump peltnorth_armorer_aboutearplugs01
            '“Could you give me a new handle for this axe head?”' if item_axehead:
                jump peltnorth_armorer_aboutaxehead01
            'I look at the youngster. “Learning the trade, I see?”' if not peltnorth_armorer_aboutthemselves:
                jump peltnorth_armorer_aboutthemselves01
            'I leave the shed.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the shed.')
                jump leavingthepeltnorth02

    label peltnorth_armorer_aboutcleanliness_clothes_torn01alt:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
        jump peltnorth_armorer_aboutcleanliness_clothes_torn02

    label peltnorth_armorer_aboutcleanliness_clothes_torn01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
        label peltnorth_armorer_aboutcleanliness_clothes_torn02:
            $ peltnorth_armorer_aboutcleanliness_clothes_torn = 1
            menu:
                'He shakes his head and points at the uneven seams on his own tunic, then grabs a crude bone needle and shows you its broken head.
                \n\n“He wouldn’t even {i}if{/i} he had the tools,” says the boy. “But you can try in {color=#f6d6bd}Howler’s Dell{/color}, or {color=#f6d6bd}Gale Rocks{/color}.”
                '
                '{image=cointest} “I’m in need of your services.”' if (peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                    jump peltnorth_armorer_aboutservices02
                '{image=coingray} My gambeson needs no repairs. (disabled)' if (peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                    pass
                '{image=cointest} “I’m in need of your services.”' if (not peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                    jump peltnorth_armorer_aboutservices01
                '{image=cointest} “Maybe not right now, but I may be in need of your services.”' if (not peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                    jump peltnorth_armorer_aboutservices01
                '“I feel like this gambeson could use some adjustments.”' if peltnorth_armorer_abouttrade and armor == 3 and not armor_can4 and not peltnorth_armorer_aboutarmor_can4:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Maybe not right now, but I may be in need of your services.”')
                    jump peltnorth_armorer_aboutarmor_can401
                '“Can you patch my clothes?”' if cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
                    jump peltnorth_armorer_aboutcleanliness_clothes_torn01
                '“Could you patch my clothes if they were torn?”' if not cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
                    jump peltnorth_armorer_aboutcleanliness_clothes_torn01alt
                '“I could use some earplugs... I’ve had a few issues with a pack of howlers.”' if not item_earplugs and northernroad_firsttime and not peltnorth_armorer_aboutearplugs:
                    jump peltnorth_armorer_aboutearplugs01
                '“Could you give me a new handle for this axe head?”' if item_axehead:
                    jump peltnorth_armorer_aboutaxehead01
                'I look at the youngster. “Learning the trade, I see?”' if not peltnorth_armorer_aboutthemselves:
                    jump peltnorth_armorer_aboutthemselves01
                'I leave the shed.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the shed.')
                    jump leavingthepeltnorth02

    label peltnorth_armorer_aboutearplugs01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I could use some earplugs... I’ve had a few issues with a pack of howlers.”')
        $ peltnorth_armorer_aboutearplugs = 1
        $ item_earplugs = "cotton"
        $ renpy.notify("You add the cotton earplugs\nto your travel set.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You add the cotton earplugs\nto your travel set.{/i}')
        menu:
            'He raises an eyebrow, moves away, reaches to a small box, and hands you a few scraps of cotton, making a gesture of squeezing them inside an ear.
            '
            '{image=cointest} “I’m in need of your services.”' if (peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                jump peltnorth_armorer_aboutservices02
            '{image=coingray} My gambeson needs no repairs. (disabled)' if (peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                pass
            '{image=cointest} “I’m in need of your services.”' if (not peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                jump peltnorth_armorer_aboutservices01
            '{image=cointest} “Maybe not right now, but I may be in need of your services.”' if (not peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                jump peltnorth_armorer_aboutservices01
            '“I feel like this gambeson could use some adjustments.”' if peltnorth_armorer_abouttrade and armor == 3 and not armor_can4 and not peltnorth_armorer_aboutarmor_can4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Maybe not right now, but I may be in need of your services.”')
                jump peltnorth_armorer_aboutarmor_can401
            '“Can you patch my clothes?”' if cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
                jump peltnorth_armorer_aboutcleanliness_clothes_torn01
            '“Could you patch my clothes if they were torn?”' if not cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
                jump peltnorth_armorer_aboutcleanliness_clothes_torn01alt
            '“I could use some earplugs... I’ve had a few issues with a pack of howlers.”' if not item_earplugs and northernroad_firsttime and not peltnorth_armorer_aboutearplugs:
                jump peltnorth_armorer_aboutearplugs01
            '“Could you give me a new handle for this axe head?”' if item_axehead:
                jump peltnorth_armorer_aboutaxehead01
            'I look at the youngster. “Learning the trade, I see?”' if not peltnorth_armorer_aboutthemselves:
                jump peltnorth_armorer_aboutthemselves01
            'I leave the shed.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the shed.')
                jump leavingthepeltnorth02

    label peltnorth_armorer_aboutaxehead01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you give me a new handle for this axe head?”')
        if iason_friendship_moneybonus_level2_given or (dalit_friendship+appearance_charisma) >= 10:
            $ item_axehead = 0
            $ item_axeset = 1
            $ renpy.notify("You received the axe handle.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You received the axe handle.{/i}')
            menu:
                'He bites his bottom lip, looks at you, and gives you a few gentle nods, then gestures at his assistant to get up. The boy finds a few pieces of necessary equipment - a handle, kerf, leather straps, and so on - then hands them to you.
                '
                '{image=cointest} “I’m in need of your services.”' if (peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                    jump peltnorth_armorer_aboutservices02
                '{image=coingray} My gambeson needs no repairs. (disabled)' if (peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                    pass
                '{image=cointest} “I’m in need of your services.”' if (not peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                    jump peltnorth_armorer_aboutservices01
                '{image=cointest} “Maybe not right now, but I may be in need of your services.”' if (not peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                    jump peltnorth_armorer_aboutservices01
                '“I feel like this gambeson could use some adjustments.”' if peltnorth_armorer_abouttrade and armor == 3 and not armor_can4 and not peltnorth_armorer_aboutarmor_can4:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Maybe not right now, but I may be in need of your services.”')
                    jump peltnorth_armorer_aboutarmor_can401
                '“Can you patch my clothes?”' if cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
                    jump peltnorth_armorer_aboutcleanliness_clothes_torn01
                '“Could you patch my clothes if they were torn?”' if not cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
                    jump peltnorth_armorer_aboutcleanliness_clothes_torn01alt
                '“I could use some earplugs... I’ve had a few issues with a pack of howlers.”' if not item_earplugs and northernroad_firsttime and not peltnorth_armorer_aboutearplugs:
                    jump peltnorth_armorer_aboutearplugs01
                '“Could you give me a new handle for this axe head?”' if item_axehead:
                    jump peltnorth_armorer_aboutaxehead01
                'I look at the youngster. “Learning the trade, I see?”' if not peltnorth_armorer_aboutthemselves:
                    jump peltnorth_armorer_aboutthemselves01
                'I leave the shed.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the shed.')
                    jump leavingthepeltnorth02
        else:
            menu:
                'He scratches his head, looks around, then at you again, and squints his eyes. He then grabs a dragon bone from his pouch and puts it on his chest.
                '
                '“One dragon? Fine.”' if coins >= 1:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “One dragon? Fine.”')
                    $ iason_friendship_moneybonus_points += 1
                    $ item_axehead = 0
                    $ item_axeset = 1
                    $ coins -= 1
                    show screen notifyimage( "You bought the axe handle.\n-1", "gui/coin2.png")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You bought the axe handle. -1 {image=cointest}{/i}')
                    menu:
                        'He takes it with a smile and gestures at his assistant to get up. The boy finds a few pieces of necessary equipment - a handle, kerf, leather straps, and so on - then hands them to you.
                        '
                        '{image=cointest} “I’m in need of your services.”' if (peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                            jump peltnorth_armorer_aboutservices02
                        '{image=coingray} My gambeson needs no repairs. (disabled)' if (peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                            pass
                        '{image=cointest} “I’m in need of your services.”' if (not peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                            jump peltnorth_armorer_aboutservices01
                        '{image=cointest} “Maybe not right now, but I may be in need of your services.”' if (not peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                            jump peltnorth_armorer_aboutservices01
                        '“I feel like this gambeson could use some adjustments.”' if peltnorth_armorer_abouttrade and armor == 3 and not armor_can4 and not peltnorth_armorer_aboutarmor_can4:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Maybe not right now, but I may be in need of your services.”')
                            jump peltnorth_armorer_aboutarmor_can401
                        '“Can you patch my clothes?”' if cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
                            jump peltnorth_armorer_aboutcleanliness_clothes_torn01
                        '“Could you patch my clothes if they were torn?”' if not cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
                            jump peltnorth_armorer_aboutcleanliness_clothes_torn01alt
                        '“I could use some earplugs... I’ve had a few issues with a pack of howlers.”' if not item_earplugs and northernroad_firsttime and not peltnorth_armorer_aboutearplugs:
                            jump peltnorth_armorer_aboutearplugs01
                        '“Could you give me a new handle for this axe head?”' if item_axehead:
                            jump peltnorth_armorer_aboutaxehead01
                        'I look at the youngster. “Learning the trade, I see?”' if not peltnorth_armorer_aboutthemselves:
                            jump peltnorth_armorer_aboutthemselves01
                        'I leave the shed.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the shed.')
                            jump leavingthepeltnorth02
                'I don’t have even a single dragon. (disabled)' if coins < 1:
                    pass
                '{image=cointest} “I’m in need of your services.”' if (peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                    jump peltnorth_armorer_aboutservices02
                '{image=coingray} My gambeson needs no repairs. (disabled)' if (peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                    pass
                '{image=cointest} “I’m in need of your services.”' if (not peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                    jump peltnorth_armorer_aboutservices01
                '{image=cointest} “Maybe not right now, but I may be in need of your services.”' if (not peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                    jump peltnorth_armorer_aboutservices01
                '“I feel like this gambeson could use some adjustments.”' if peltnorth_armorer_abouttrade and armor == 3 and not armor_can4 and not peltnorth_armorer_aboutarmor_can4:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Maybe not right now, but I may be in need of your services.”')
                    jump peltnorth_armorer_aboutarmor_can401
                '“Can you patch my clothes?”' if cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
                    jump peltnorth_armorer_aboutcleanliness_clothes_torn01
                '“Could you patch my clothes if they were torn?”' if not cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
                    jump peltnorth_armorer_aboutcleanliness_clothes_torn01alt
                '“I could use some earplugs... I’ve had a few issues with a pack of howlers.”' if not item_earplugs and northernroad_firsttime and not peltnorth_armorer_aboutearplugs:
                    jump peltnorth_armorer_aboutearplugs01
                '“Could you give me a new handle for this axe head?”' if item_axehead:
                    jump peltnorth_armorer_aboutaxehead01
                'I look at the youngster. “Learning the trade, I see?”' if not peltnorth_armorer_aboutthemselves:
                    jump peltnorth_armorer_aboutthemselves01
                'I leave the shed.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the shed.')
                    jump leavingthepeltnorth02

    label peltnorth_armorer_aboutthemselves01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the youngster. “Learning the trade, I see?”')
        $ peltnorth_armorer_aboutthemselves = 1
        menu:
            '“Kind of,” he answers reluctantly, but his teacher pats his knee, giving him a harsh look. The kid clears his throat. “Yes, but we {i}both{/i} ain’t masters, you see? There’s not a soul to teach us, so once I’m ready, I’ll try hunting instead. Fixing things for others is boring.”
            \n\nThe man grunts a sound, though you don’t understand it. Seeing your face, the boy chuckles. “He said {i}safe{/i}. Let’s meet in the middle - boring, but safe.”
            \n\nThe man nods.
            '
            '{image=cointest} “I’m in need of your services.”' if (peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                jump peltnorth_armorer_aboutservices02
            '{image=coingray} My gambeson needs no repairs. (disabled)' if (peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                pass
            '{image=cointest} “I’m in need of your services.”' if (not peltnorth_armorer_abouttrade and armor < 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor < 4 and armor_can4):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I’m in need of your services.”')
                jump peltnorth_armorer_aboutservices01
            '{image=cointest} “Maybe not right now, but I may be in need of your services.”' if (not peltnorth_armorer_abouttrade and armor >= 3 and not armor_can4) or (not peltnorth_armorer_abouttrade and armor >= 4 and armor_can4):
                jump peltnorth_armorer_aboutservices01
            '“I feel like this gambeson could use some adjustments.”' if peltnorth_armorer_abouttrade and armor == 3 and not armor_can4 and not peltnorth_armorer_aboutarmor_can4:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “Maybe not right now, but I may be in need of your services.”')
                jump peltnorth_armorer_aboutarmor_can401
            '“Can you patch my clothes?”' if cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Can you patch my clothes?”')
                jump peltnorth_armorer_aboutcleanliness_clothes_torn01
            '“Could you patch my clothes if they were torn?”' if not cleanliness_clothes_torn and not peltnorth_armorer_aboutcleanliness_clothes_torn:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Could you patch my clothes if they were torn?”')
                jump peltnorth_armorer_aboutcleanliness_clothes_torn01alt
            '“I could use some earplugs... I’ve had a few issues with a pack of howlers.”' if not item_earplugs and northernroad_firsttime and not peltnorth_armorer_aboutearplugs:
                jump peltnorth_armorer_aboutearplugs01
            '“Could you give me a new handle for this axe head?”' if item_axehead:
                jump peltnorth_armorer_aboutaxehead01
            'I look at the youngster. “Learning the trade, I see?”' if not peltnorth_armorer_aboutthemselves:
                jump peltnorth_armorer_aboutthemselves01
            'I leave the shed.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I leave the shed.')
                jump leavingthepeltnorth02
