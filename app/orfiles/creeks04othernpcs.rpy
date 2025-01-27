default oldhava_known = 0
default oldhava_fluff = 0
default oldhava_firsttime = 0
default oldhava_friendship = 0
default oldhava_background = 0

default oldhava_moneyspent = 0
default oldhava_about_earplugs = 0
default oldhava_about_trade = 0
default oldhava_about_chicken = 0
default oldhava_about_sleep = 0
default oldhava_about_sleep_available = 0
default oldhava_about_foggy = 0
default oldhava_seeds = 0

label creeksoldhavaALL:
    label creeksoldhava01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go to {color=#f6d6bd}Old Hava{/color}, the farmer.')
        $ shop = "creeksmerchant"
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        if not oldhava_firsttime:
            jump oldhava_firsttime01
        else:
            $ oldhava_fluff = renpy.random.choice(['She’s sitting next to a field, inspecting a few picked leaves in the light.', 'She’s carrying her stool between the fields, seeking a spot to sit down. She chooses a wild cabbage patch.', 'She’s sitting in the shadow of a shed, resting her hands and a cheek on the handle of a garden hoe.', 'She’s standing next to the stream, speaking with another farmer, who leaves her once you get closer.', 'She’s observing the birds, ignoring your presence.'])
            menu:
                '[oldhava_fluff]
                '
                '{image=cointest} “What do you have for sale?”' if not oldhava_about_trade:
                    jump creeksoldhavaabouttrade01
                '{image=cointest} “I need supplies.”' if oldhava_about_trade:
                    jump creeksoldhavaabouttrade03
                '“I met some annoying howlers... Do you have any earplugs?”' if not item_earplugs and northernroad_firsttime and not oldhava_about_earplugs and oldhava_about_trade:
                    jump creeksoldhavaaboutearplugs01
                '“About those earplugs...”' if not item_earplugs and northernroad_firsttime and oldhava_about_earplugs and oldhava_about_trade:
                    jump creeksoldhavaaboutearplugs02
                '“I’m looking for a place to sleep.”' if not oldhava_about_sleep and not creeks_sleep_available:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a place to sleep.”')
                    if quest_missinghunters != 2:
                        jump creeksoldhavaaboutroom01
                    elif (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                        jump creeksoldhavaaboutroom01alt
                    else:
                        jump creeksoldhavaaboutroom02
                'The locals don’t have any room for me to rent. (disabled)' if oldhava_about_sleep == 1 and not creeks_feast:
                    pass
                'The locals don’t trust me enough to let me own a room here. (disabled)' if oldhava_about_sleep == 1 and creeks_feast and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    pass
                '“We were talking about the room...”' if (oldhava_about_sleep == 1 and creeks_feast and not creeks_sleep_available) or (oldhava_about_sleep == 2 and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) >= 25 and not creeks_sleep_available):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We were talking about the room...”')
                    if (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                        jump creeksoldhavaaboutroom01alt
                    else:
                        jump creeksoldhavaaboutroom02
                '“I know about your past, {color=#f6d6bd}Erith{/color}.”' if description_creeks08 and not oldhava_background:
                    jump creeksoldhavaaboutherself01
                '“I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”' if oldhava_about_trade and not oldhava_about_foggy:
                    jump creeksoldhavaaboutfoggy01
                'She’s not willing to tell me more about merchants. (disabled)' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) < 10:
                    pass
                '“I was asking about the merchants...”' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) >= 10:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”')
                    jump creeksoldhavaaboutfoggy02
                '“Farewell.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                    jump creeksafterinteraction01
                # '':
                #     $ narrator.add_history(kind='nvl', who=narrator.name, what='- ')
                #     jump z

    label creeksoldhavaafterinteraction01:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            '[custom5]
            '
            '{image=cointest} “What do you have for sale?”' if not oldhava_about_trade:
                jump creeksoldhavaabouttrade01
            '{image=cointest} “I need supplies.”' if oldhava_about_trade:
                jump creeksoldhavaabouttrade03
            '“I met some annoying howlers... Do you have any earplugs?”' if not item_earplugs and northernroad_firsttime and not oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs01
            '“About those earplugs...”' if not item_earplugs and northernroad_firsttime and oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs02
            '“I’m looking for a place to sleep.”' if not oldhava_about_sleep and not creeks_sleep_available:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a place to sleep.”')
                if quest_missinghunters != 2:
                    jump creeksoldhavaaboutroom01
                elif (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            'The locals don’t have any room for me to rent. (disabled)' if oldhava_about_sleep == 1 and not creeks_feast:
                pass
            'The locals don’t trust me enough to let me own a room here. (disabled)' if oldhava_about_sleep == 1 and creeks_feast and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                pass
            '“We were talking about the room...”' if (oldhava_about_sleep == 1 and creeks_feast and not creeks_sleep_available) or (oldhava_about_sleep == 2 and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) >= 25 and not creeks_sleep_available):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We were talking about the room...”')
                if (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            '“I know about your past, {color=#f6d6bd}Erith{/color}.”' if description_creeks08 and not oldhava_background:
                jump creeksoldhavaaboutherself01
            '“I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”' if oldhava_about_trade and not oldhava_about_foggy:
                jump creeksoldhavaaboutfoggy01
            'She’s not willing to tell me more about merchants. (disabled)' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) < 10:
                pass
            '“I was asking about the merchants...”' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) >= 10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”')
                jump creeksoldhavaaboutfoggy02
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump creeksafterinteraction01

    label oldhava_firsttime01:
        $ oldhava_firsttime = 1
        menu:
            'You follow the path between the fields, witnessing a one-sided conversation between {color=#f6d6bd}Old Hava{/color} and a barely adult man. She orders him around, pointing at various plants, criticizing the sight of weeds, and addressing the {i}fancy{/i} clothes he’s wearing. He observes his red-dyed boots and lets out a relieved sigh after your arrival. “I better change,” he mumbles, heading to the main square.
            '
            'I step out of his way.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step out of his way.')
                $ at_activate = 1
                $ at = 0
                menu:
                    'The woman spares you a wry glance, then turns away, focused on the struggling vegetables. She’s the only person in the village who wears clothes made of plant fabric, but they’re weathered and covered with decades-old patches.
                    \n\nHer hands, clasped behind her back, are constantly twitching.
                    '
                    ' (disabled)' ( condition="at == 0" ):
                        pass
                    '“How are you doing?”' ( condition="at == 'friendly'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(friendly) - “How are you doing?”')
                        $ at_activate = 0
                        $ at = 0
                        $ oldhava_friendship -= 1
                        $ custom1 = "After a moment, she turns to you slowly, chewing her bottom lip. “I’m {i}doing{/i} my break. Say what you want, and fast.”"
                        jump oldhava_firsttime02
                    '“Youth, huh? {i}Back in my day!{/i}”' ( condition="at == 'playful'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(playful) - “Youth, huh? {i}Back in my day!{/i}”')
                        $ at_activate = 0
                        $ at = 0
                        $ oldhava_friendship -= 2
                        $ custom1 = "After another minute you consider leaving, but she finally breaks the silence. “You’d be crying in bed like a tot if you had seen the things I did at your age. Mock my years, I’m {i}proud{/i} of them,” she turns toward you and raises her shaking hands. “My soul’s still here, but fog is crawling into my shell. Yet you waste my time, stranger.”"
                        jump oldhava_firsttime02
                    '{image=cointest} “What do you have for sale?”' ( condition="at == 'distanced'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(distanced) - {image=cointest} “What do you have for sale?”')
                        $ at_activate = 0
                        $ at = 0
                        $ oldhava_friendship -= 0
                        $ oldhava_about_trade = 1
                        $ renpy.notify("New trader unlocked.")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
                        menu:
                            'After a moment, she turns to you slowly, chewing her bottom lip. “We sold hwat we had, we’re lacking hunters. And these,” she looks at the wrinkled vegetables, “will go into a stew, if they’re even worth picking.”
                            \n\nWithout noticing it, she grabs her left forearm with her right hand, but it doesn’t stop the twitching. “We always have a fish trap to spare, we make them just in case. A large basket, put it in a creek and wait a day or two, until something swims inside. I’ll sell you one for two dragon bones.”
                            \n\n“And if you’d rather eat something right away,” she carries on after a short pause, “our cooks would spare you a roast grouse, or a chicken. It’ll be cold, but fresh. We always have one. You never know when there are maggots in your supplies, and kids shouldn’t skip a meal.”
                            \n\nYou ask her to tell you more, but her patience grows thin. “It’s the best light roast in the North. We add plenty of spices to it, so it spoils slowly. That’s it.”
                            '
                            '“Fine. Show me how this trap works.”':
                                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. Show me how this trap works.”')
                                jump creeksoldhavaabouttrade02
                    '“Don’t test my patience.”' ( condition="at == 'intimidating'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(intimidating) - “Don’t test my patience.”')
                        $ at_activate = 0
                        $ at = 0
                        $ oldhava_friendship -= 2
                        $ custom1 = "After another minute you consider leaving, but she finally breaks the silence, though without looking at you. “Don’t test our hospitality. Say hwat you need and fuck off.”"
                        jump oldhava_firsttime02
                    'I wait patiently.' ( condition="at == 'vulnerable'" ):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='(vulnerable) - I wait patiently.')
                        $ at_activate = 0
                        $ at = 0
                        $ oldhava_friendship += 1
                        $ custom1 = "After a minute, you realize that her keen eyes are indeed observing the leaves, instead of just disregarding your presence. She clears her throat and points at one of the carrots. “Their color is good, dark, but they’re small. I think the soil is too dense.” She’s gathering her thoughts for another few breaths, then looks at you softly. “I have time now, roadwarden.”"
                        jump oldhava_firsttime02
    label oldhava_firsttime02:
        if oldhava_moneyspent >= 4:
            $ oldhava_friendship += 1
            $ oldhava_moneyspent -= 4
        menu:
            '[custom1]
            '
            '{image=cointest} “What do you have for sale?”' if not oldhava_about_trade:
                jump creeksoldhavaabouttrade01
            '{image=cointest} “I need supplies.”' if oldhava_about_trade:
                jump creeksoldhavaabouttrade03
            '“I met some annoying howlers... Do you have any earplugs?”' if not item_earplugs and northernroad_firsttime and not oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs01
            '“About those earplugs...”' if not item_earplugs and northernroad_firsttime and oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs02
            '“I’m looking for a place to sleep.”' if not oldhava_about_sleep and not creeks_sleep_available:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a place to sleep.”')
                if quest_missinghunters != 2:
                    jump creeksoldhavaaboutroom01
                elif (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            'The locals don’t have any room for me to rent. (disabled)' if oldhava_about_sleep == 1 and not creeks_feast:
                pass
            'The locals don’t trust me enough to let me own a room here. (disabled)' if oldhava_about_sleep == 1 and creeks_feast and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                pass
            '“We were talking about the room...”' if (oldhava_about_sleep == 1 and creeks_feast and not creeks_sleep_available) or (oldhava_about_sleep == 2 and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) >= 25 and not creeks_sleep_available):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We were talking about the room...”')
                if (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            '“I know about your past, {color=#f6d6bd}Erith{/color}.”' if description_creeks08 and not oldhava_background:
                jump creeksoldhavaaboutherself01
            '“I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”' if oldhava_about_trade and not oldhava_about_foggy:
                jump creeksoldhavaaboutfoggy01
            'She’s not willing to tell me more about merchants. (disabled)' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) < 10:
                pass
            '“I was asking about the merchants...”' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) >= 10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”')
                jump creeksoldhavaaboutfoggy02
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump creeksafterinteraction01

    label creeksoldhavaabouttrade01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “What do you have for sale?”')
        $ oldhava_about_trade = 1
        $ renpy.notify("New trader unlocked.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New trader unlocked.{/i}')
        menu:
            '“We sold hwat we had, we’re lacking hunters. And these,” she looks at the wrinkled vegetables, “will go into a stew, if they’re even worth picking.”
            \n\nWithout noticing it, she grabs her left forearm with her right hand, but it doesn’t stop the twitching. “We always have a fish trap to spare, we make them just in case. A large basket, put it in a creek and wait a day or two, until something swims inside. I’ll sell you one for two dragon bones.”
            \n\n“And if you’d rather eat something right away,” she carries on after a short pause, “our cooks would spare you a roast grouse, or a chicken. It’ll be cold, but fresh. We always have one. You never know when there are maggots in your supplies, and kids shouldn’t skip a meal.”
            \n\nYou ask her to tell you more, but her patience grows thin. “It’s the best light roast in the North. We add plenty of spices to it, so it spoils slowly. That’s it.”
            '
            '“Fine. Show me how this trap works.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Fine. Show me how this trap works.”')
                jump creeksoldhavaabouttrade02

    label creeksoldhavaabouttrade02:
        $ shop = "creeksmerchant"
        show screen shopscreen with dissolve
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'She says nothing.
            '
            '{image=cointest} “What do you have for sale?”' if not oldhava_about_trade:
                jump creeksoldhavaabouttrade01
            '{image=cointest} “I need supplies.”' if oldhava_about_trade:
                jump creeksoldhavaabouttrade03
            '“I met some annoying howlers... Do you have any earplugs?”' if not item_earplugs and northernroad_firsttime and not oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs01
            '“About those earplugs...”' if not item_earplugs and northernroad_firsttime and oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs02
            '“I’m looking for a place to sleep.”' if not oldhava_about_sleep and not creeks_sleep_available:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a place to sleep.”')
                if quest_missinghunters != 2:
                    jump creeksoldhavaaboutroom01
                elif (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            'The locals don’t have any room for me to rent. (disabled)' if oldhava_about_sleep == 1 and not creeks_feast:
                pass
            'The locals don’t trust me enough to let me own a room here. (disabled)' if oldhava_about_sleep == 1 and creeks_feast and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                pass
            '“We were talking about the room...”' if (oldhava_about_sleep == 1 and creeks_feast and not creeks_sleep_available) or (oldhava_about_sleep == 2 and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) >= 25 and not creeks_sleep_available):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We were talking about the room...”')
                if (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            '“I know about your past, {color=#f6d6bd}Erith{/color}.”' if description_creeks08 and not oldhava_background:
                jump creeksoldhavaaboutherself01
            '“I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”' if oldhava_about_trade and not oldhava_about_foggy:
                jump creeksoldhavaaboutfoggy01
            'She’s not willing to tell me more about merchants. (disabled)' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) < 10:
                pass
            '“I was asking about the merchants...”' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) >= 10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”')
                jump creeksoldhavaaboutfoggy02
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump creeksafterinteraction01

    label creeksoldhavaaboutearplugs01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I met some annoying howlers... Do you have any earplugs?”')
        $ oldhava_about_earplugs = 1
        menu:
            'Her shoulders flinch. “But will that work? They can break the skull of a deaf shell.” After you shrug, she looks at one of the farmers who’s wearing mouflon fur.
            \n\n“Give me something good to eat and I’ll give you a few tufts of thick wool. Put them into your ears, then wear them under a tight hood.”
            '
            '“How about some wild fruits and greens?”' if item_wildplants:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about some wild fruits and greens?”')
                $ custom5 = "She nods and orders the farmer to bring her a knife. “We’ll need more seeds anyway.”\n\nAfter a few minutes, you hold a new pair of earplugs."
                $ minutes += 5
                $ item_wildplants -= 1
                $ oldhava_moneyspent += 2
                $ item_earplugs = "wool"
                $ renpy.notify("You lost a few wild plants.\nYou add the wool earplugs\nto your travel set.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a few wild plants. You add the wool earplugs to your travel set.{/i}')
                jump creeksoldhavaafterinteraction01
            '“I have a food ration to spare.”' if item_rations:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have a food ration to spare.”')
                $ custom5 = "“And we always need more of them.” She orders the farmer to bring her a knife. After a few minutes, you hold a new pair of earplugs."
                $ minutes += 5
                $ item_rations -= 1
                $ oldhava_moneyspent += 1
                $ item_earplugs = "wool"
                $ renpy.notify("You lost a food ration.\nYou add the wool earplugs\nto your travel set.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration. You add the wool earplugs to your travel set.{/i}')
                jump creeksoldhavaafterinteraction01
            '“Will a dragon bone be fine?”' if coins > 0:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Will a dragon bone be fine?”')
                $ custom5 = "She chews her bottom lip. “I’d never {i}ask{/i} for so much, but if you insist.” She orders the farmer to bring her a knife. After a few minutes, you hold a new pair of earplugs."
                $ minutes += 5
                $ coins -= 1
                $ oldhava_moneyspent += 1
                $ item_earplugs = "wool"
                show screen notifyimage( "You add the wool earplugs\nto your travel set.\n-1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You add the wool earplugs to your travel set. -1 {image=cointest}{/i}')
                jump creeksoldhavaafterinteraction01
            'I have nothing to offer. (disabled)' if not coins and not item_rations and not item_wildplants:
                pass
            '“I’ll think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                $ custom5 = "Her eyes stay on the members of her crew."
                jump creeksoldhavaafterinteraction01

    label creeksoldhavaaboutearplugs02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “About those earplugs...”')
        $ oldhava_about_earplugs = 1
        menu:
            'She waits for you to carry on.
            '
            '“How about some wild fruits and greens?”' if item_wildplants:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How about some wild fruits and greens?”')
                $ custom5 = "She nods and orders the farmer to bring her a knife. “We’ll need more seeds anyway.”\n\nAfter a few minutes, you hold a new pair of earplugs."
                $ minutes += 5
                $ item_wildplants -= 1
                $ oldhava_moneyspent += 2
                $ item_earplugs = "wool"
                $ renpy.notify("You lost a few wild plants.\nYou add the wool earplugs\nto your travel set.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a few wild plants. You add the wool earplugs to your travel set.{/i}')
                jump creeksoldhavaafterinteraction01
            '“I have a food ration to spare.”' if item_rations:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have a food ration to spare.”')
                $ custom5 = "“And we always need more of them.” She orders the farmer to bring her a knife. After a few minutes, you hold a new pair of earplugs."
                $ minutes += 5
                $ item_rations -= 1
                $ oldhava_moneyspent += 1
                $ item_earplugs = "wool"
                $ renpy.notify("You lost a food ration.\nYou add the wool earplugs\nto your travel set.")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You lost a food ration. You add the wool earplugs to your travel set.{/i}')
                jump creeksoldhavaafterinteraction01
            '“Will a dragon bone be fine?”' if coins > 0:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Will a dragon bone be fine?”')
                $ custom5 = "She chews her bottom lip. “I’d never {i}ask{/i} for so much, but if you insist.” She orders the farmer to bring her a knife. After a few minutes, you hold a new pair of earplugs."
                $ minutes += 5
                $ coins -= 1
                $ oldhava_moneyspent += 1
                $ item_earplugs = "wool"
                show screen notifyimage( "You add the wool earplugs\nto your travel set.\n-1", "gui/coin2.png")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You add the wool earplugs to your travel set. -1 {image=cointest}{/i}')
                jump creeksoldhavaafterinteraction01
            'I have nothing to offer. (disabled)' if not coins and not item_rations and not item_wildplants:
                pass
            '“I’ll think about it.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ll think about it.”')
                $ custom5 = "Her eyes stay on the members of her crew."
                jump creeksoldhavaafterinteraction01

    label creeksoldhavaabouttrade03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=cointest} “I need supplies.”')
        $ shop = "creeksmerchant"
        show screen shopscreen with dissolve
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        menu:
            'She says nothing.
            '
            '{image=cointest} “What do you have for sale?”' if not oldhava_about_trade:
                jump creeksoldhavaabouttrade01
            '{image=cointest} “I need supplies.”' if oldhava_about_trade:
                jump creeksoldhavaabouttrade03
            '“I met some annoying howlers... Do you have any earplugs?”' if not item_earplugs and northernroad_firsttime and not oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs01
            '“About those earplugs...”' if not item_earplugs and northernroad_firsttime and oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs02
            '“I’m looking for a place to sleep.”' if not oldhava_about_sleep and not creeks_sleep_available:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a place to sleep.”')
                if quest_missinghunters != 2:
                    jump creeksoldhavaaboutroom01
                elif (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            'The locals don’t have any room for me to rent. (disabled)' if oldhava_about_sleep == 1 and not creeks_feast:
                pass
            'The locals don’t trust me enough to let me own a room here. (disabled)' if oldhava_about_sleep == 1 and creeks_feast and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                pass
            '“We were talking about the room...”' if (oldhava_about_sleep == 1 and creeks_feast and not creeks_sleep_available) or (oldhava_about_sleep == 2 and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) >= 25 and not creeks_sleep_available):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We were talking about the room...”')
                if (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            '“I know about your past, {color=#f6d6bd}Erith{/color}.”' if description_creeks08 and not oldhava_background:
                jump creeksoldhavaaboutherself01
            '“I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”' if oldhava_about_trade and not oldhava_about_foggy:
                jump creeksoldhavaaboutfoggy01
            'She’s not willing to tell me more about merchants. (disabled)' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) < 10:
                pass
            '“I was asking about the merchants...”' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) >= 10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”')
                jump creeksoldhavaaboutfoggy02
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump creeksafterinteraction01

    label creeksoldhavaaboutroom01:
        $ oldhava_about_sleep = 1
        menu:
            '“We need another hut, and we have no space for it,” she gazes at you with dry, tired eyes. “If you need a scrap of floor, go to the tavern.”
            '
            '{image=cointest} “What do you have for sale?”' if not oldhava_about_trade:
                jump creeksoldhavaabouttrade01
            '{image=cointest} “I need supplies.”' if oldhava_about_trade:
                jump creeksoldhavaabouttrade03
            '“I met some annoying howlers... Do you have any earplugs?”' if not item_earplugs and northernroad_firsttime and not oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs01
            '“About those earplugs...”' if not item_earplugs and northernroad_firsttime and oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs02
            '“I’m looking for a place to sleep.”' if not oldhava_about_sleep and not creeks_sleep_available:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a place to sleep.”')
                if quest_missinghunters != 2:
                    jump creeksoldhavaaboutroom01
                elif (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            'The locals don’t have any room for me to rent. (disabled)' if oldhava_about_sleep == 1 and not creeks_feast:
                pass
            'The locals don’t trust me enough to let me own a room here. (disabled)' if oldhava_about_sleep == 1 and creeks_feast and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                pass
            '“We were talking about the room...”' if (oldhava_about_sleep == 1 and creeks_feast and not creeks_sleep_available) or (oldhava_about_sleep == 2 and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) >= 25 and not creeks_sleep_available):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We were talking about the room...”')
                if (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            '“I know about your past, {color=#f6d6bd}Erith{/color}.”' if description_creeks08 and not oldhava_background:
                jump creeksoldhavaaboutherself01
            '“I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”' if oldhava_about_trade and not oldhava_about_foggy:
                jump creeksoldhavaaboutfoggy01
            'She’s not willing to tell me more about merchants. (disabled)' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) < 10:
                pass
            '“I was asking about the merchants...”' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) >= 10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”')
                jump creeksoldhavaaboutfoggy02
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump creeksafterinteraction01

    label creeksoldhavaaboutroom01alt:
        $ oldhava_about_sleep = 2
        menu:
            '“You want a sleeping spot from one of the hunters?” She glances up at you with curiosity. “Let us mourn first, stranger. The tribe isn’t ready for new neighbors.”
            '
            '{image=cointest} “What do you have for sale?”' if not oldhava_about_trade:
                jump creeksoldhavaabouttrade01
            '{image=cointest} “I need supplies.”' if oldhava_about_trade:
                jump creeksoldhavaabouttrade03
            '“I met some annoying howlers... Do you have any earplugs?”' if not item_earplugs and northernroad_firsttime and not oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs01
            '“About those earplugs...”' if not item_earplugs and northernroad_firsttime and oldhava_about_earplugs and oldhava_about_trade:
                jump creeksoldhavaaboutearplugs02
            '“I’m looking for a place to sleep.”' if not oldhava_about_sleep and not creeks_sleep_available:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a place to sleep.”')
                if quest_missinghunters != 2:
                    jump creeksoldhavaaboutroom01
                elif (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            'The locals don’t have any room for me to rent. (disabled)' if oldhava_about_sleep == 1 and not creeks_feast:
                pass
            'The locals don’t trust me enough to let me own a room here. (disabled)' if oldhava_about_sleep == 1 and creeks_feast and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                pass
            '“We were talking about the room...”' if (oldhava_about_sleep == 1 and creeks_feast and not creeks_sleep_available) or (oldhava_about_sleep == 2 and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) >= 25 and not creeks_sleep_available):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We were talking about the room...”')
                if (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    jump creeksoldhavaaboutroom01alt
                else:
                    jump creeksoldhavaaboutroom02
            '“I know about your past, {color=#f6d6bd}Erith{/color}.”' if description_creeks08 and not oldhava_background:
                jump creeksoldhavaaboutherself01
            '“I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”' if oldhava_about_trade and not oldhava_about_foggy:
                jump creeksoldhavaaboutfoggy01
            'She’s not willing to tell me more about merchants. (disabled)' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) < 10:
                pass
            '“I was asking about the merchants...”' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) >= 10:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”')
                jump creeksoldhavaaboutfoggy02
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump creeksafterinteraction01

    label creeksoldhavaaboutroom02:
        $ creeks_sleep_available = 1
        menu:
            '“Aye, the tribe says you’re worth keeping around. I’ll show you your scrap of floor.” She leads you to the main square where a few people wave at you, then simply pushes open the door of the building that’s near the northern bridge.
            \n\nOn a bench, next to the entrance, a young, visibly pregnant woman is leaning against the wall. Her bare feet are stretched out and make small circles, warming up before taking a walk. “A new neighbor,” she warmly announces. “Finally free from inns and caves, aye?”
            \n\nBefore you respond, you hear {color=#f6d6bd}Hava’s{/color} frustration. “I’m done waiting.”
            '
            'I follow her inside.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I follow her inside.')
                menu:
                    'The house is a single, large chamber, airy and bright. While the door has no lock, a massive bar that may be used to barricade it is right at hand, and the shutters seem just as safe. Signs of the residents are spread on the floor, shelves, tables, stools, and inside an open chest. At first they seem disorderly, but you then recognize that the sleeping spots under the walls are surrounded with items of distinct purpose, such as tools or toys. While there’s not much privacy to be found here, there’s still some sense of ownership and attachment to objects and spaces.
                    \n\nAs you have already seen, the lives of the locals takes place outside. You recognize but one shape sleeping in a corner - a guard you’ve seen before, resting after a night shift. {color=#f6d6bd}Your guide{/color} is standing above another corner, next to an open window. It’s the only spot that’s free of clothes and other odds and ends. “You are the eighth dweller, so be quiet during the nighttime. And be clean at all times. That’s it.” She turns around and leaves you with a large pile of furs, on which you spot no dust or dirt.
                    '
                    'It’s always good to have more options, but that’s about it. I leave the house - I’m no one’s “neighbor.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s always good to have more options, but that’s about it. I leave the house - I’m no one’s “neighbor.”')
                        jump creeksafterinteraction01
                    'I look at the empty corner... My new “home,” and sit down for a bit. I place around a few small things of mine, as a mark of ownership.':
                        $ quarters += 1
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at the empty corner... My new “home,” and sit down for a bit. I place around a few small things of mine, as a mark of ownership.')
                        jump creeksafterinteraction01

    label creeksoldhavaaboutfoggy01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”')
        if (oldhava_friendship+appearance_charisma+creeks_reputation) < 10:
            $ oldhava_about_foggy = 1
            menu:
                '“Hwat’s it to you?” She doesn’t wait for your response. “Does her yard look like it has space for nets?”
                '
                '{image=cointest} “What do you have for sale?”' if not oldhava_about_trade:
                    jump creeksoldhavaabouttrade01
                '{image=cointest} “I need supplies.”' if oldhava_about_trade:
                    jump creeksoldhavaabouttrade03
                '“I met some annoying howlers... Do you have any earplugs?”' if not item_earplugs and northernroad_firsttime and not oldhava_about_earplugs and oldhava_about_trade:
                    jump creeksoldhavaaboutearplugs01
                '“About those earplugs...”' if not item_earplugs and northernroad_firsttime and oldhava_about_earplugs and oldhava_about_trade:
                    jump creeksoldhavaaboutearplugs02
                '“I’m looking for a place to sleep.”' if not oldhava_about_sleep and not creeks_sleep_available:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a place to sleep.”')
                    if quest_missinghunters != 2:
                        jump creeksoldhavaaboutroom01
                    elif (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                        jump creeksoldhavaaboutroom01alt
                    else:
                        jump creeksoldhavaaboutroom02
                'The locals don’t have any room for me to rent. (disabled)' if oldhava_about_sleep == 1 and not creeks_feast:
                    pass
                'The locals don’t trust me enough to let me own a room here. (disabled)' if oldhava_about_sleep == 1 and creeks_feast and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    pass
                '“We were talking about the room...”' if (oldhava_about_sleep == 1 and creeks_feast and not creeks_sleep_available) or (oldhava_about_sleep == 2 and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) >= 25 and not creeks_sleep_available):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We were talking about the room...”')
                    if (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                        jump creeksoldhavaaboutroom01alt
                    else:
                        jump creeksoldhavaaboutroom02
                '“I know about your past, {color=#f6d6bd}Erith{/color}.”' if description_creeks08 and not oldhava_background:
                    jump creeksoldhavaaboutherself01
                '“I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”' if oldhava_about_trade and not oldhava_about_foggy:
                    jump creeksoldhavaaboutfoggy01
                'She’s not willing to tell me more about merchants. (disabled)' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) < 10:
                    pass
                '“I was asking about the merchants...”' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) >= 10:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”')
                    jump creeksoldhavaaboutfoggy02
                '“Farewell.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                    jump creeksafterinteraction01
        else:
            label creeksoldhavaaboutfoggy02:
                $ oldhava_about_foggy = 2
                $ description_creeks07 = "{color=#f6d6bd}Old Hava{/color} claims that her tribe lacks ability when it comes to trade, and is completely dependent on {color=#f6d6bd}Foggy{/color} and the safety of the road leading to her."
                $ description_foggy06 = "According to {color=#f6d6bd}Old Hava{/color}, {color=#f6d6bd}Foggy{/color} is essential to sustain the trade between {color=#f6d6bd}Creeks{/color} and other settlements."
                menu:
                    '“Our hunters push away the beasts, but it’s not safe enough for us to keep roaming from here to there on a hwim. But you’re right, roadwarden, I’m just a farmer with a past.” During the pause that follows, a cold gust of wind ruffles your cloak. “It’s {color=#f6d6bd}Foggy{/color} who speaks with travelers and merchants, knows how to price wares and labor. We need both her place and her experience, but you know how these roads are. When we need to resupply, we send a whole expedition with a cart, not a lonely peddler.”
                    '
                    '{image=cointest} “What do you have for sale?”' if not oldhava_about_trade:
                        jump creeksoldhavaabouttrade01
                    '{image=cointest} “I need supplies.”' if oldhava_about_trade:
                        jump creeksoldhavaabouttrade03
                    '“I met some annoying howlers... Do you have any earplugs?”' if not item_earplugs and northernroad_firsttime and not oldhava_about_earplugs and oldhava_about_trade:
                        jump creeksoldhavaaboutearplugs01
                    '“About those earplugs...”' if not item_earplugs and northernroad_firsttime and oldhava_about_earplugs and oldhava_about_trade:
                        jump creeksoldhavaaboutearplugs02
                    '“I’m looking for a place to sleep.”' if not oldhava_about_sleep and not creeks_sleep_available:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a place to sleep.”')
                        if quest_missinghunters != 2:
                            jump creeksoldhavaaboutroom01
                        elif (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                            jump creeksoldhavaaboutroom01alt
                        else:
                            jump creeksoldhavaaboutroom02
                    'The locals don’t have any room for me to rent. (disabled)' if oldhava_about_sleep == 1 and not creeks_feast:
                        pass
                    'The locals don’t trust me enough to let me own a room here. (disabled)' if oldhava_about_sleep == 1 and creeks_feast and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                        pass
                    '“We were talking about the room...”' if (oldhava_about_sleep == 1 and creeks_feast and not creeks_sleep_available) or (oldhava_about_sleep == 2 and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) >= 25 and not creeks_sleep_available):
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We were talking about the room...”')
                        if (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                            jump creeksoldhavaaboutroom01alt
                        else:
                            jump creeksoldhavaaboutroom02
                    '“I know about your past, {color=#f6d6bd}Erith{/color}.”' if description_creeks08 and not oldhava_background:
                        jump creeksoldhavaaboutherself01
                    '“I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”' if oldhava_about_trade and not oldhava_about_foggy:
                        jump creeksoldhavaaboutfoggy01
                    'She’s not willing to tell me more about merchants. (disabled)' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) < 10:
                        pass
                    '“I was asking about the merchants...”' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) >= 10:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”')
                        jump creeksoldhavaaboutfoggy02
                    '“Farewell.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                        jump creeksafterinteraction01

    label creeksoldhavaaboutherself01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know about your past, {color=#f6d6bd}Erith{/color}.”')
        $ oldhava_background = 1
        if pc_class == "scholar":
            $ at_unlock_knowledge = 1
            $ at = 0
        menu:
            'She stares into the nearest creek, then suddenly reaches to her side, though you have enough time to take a defensive stance. She finds nothing there at her belt, and her weak fingers couldn’t hold even the memory of a dagger.
            \n\n“I should have known you’re bad news,” she moves her hands behind her back and steps away. “So, you’ve found a farmer on the brink of death, too fragile to travel to the city’s hangman.” Her lips, twisted in a smirk, can’t hide the fury in her eyes. “Hwat happens now?”
            '
            '“I just want to ask you about your life. But tell me, does your tribe know who’s hiding among them?”' ( condition="at != 'knowledge'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I just want to ask you about your life. But tell me, does your tribe know who’s hiding among them?”')
                $ at = 0
                $ custom1 = "She observes your weapon, still hesitating. “You think we took random strangers with us, twenty-five years ago? Other than a few hunters, most of us were folk of the city trades. Merchants, bards, a priest, a juggler,” her voice is tense. “They were desperate for a soul who knew how to swing a mace or an axe, and so I saved many lives in the first few years of our new home. Erith, the bandit, has vanished with the war. Hava, the guardian, asked only for silence.”\n\nShe takes a long pause and you realize how much heavier her breath is, how her arms start to shake. “I have tales in me, so many of them, ‘bout violence, opulence, betrayal. Not the stories you need, but a lesson. Take these words with you.” She stares into your eyes with the watchfulness of an eagle. “A leader fueled by greed, pride, or vengeance will burn their own soul. They {i}will{/i} die in misery, but if their efforts outlive them, their heir must be even more ruthless, proving to their last breath that they {i}deserve{/i} to lead. Or... they may be weak, and loved by their underlings, but that’s an even harsher fate to face, as they won’t stop the rage of those who have already been harmed. And once the punishment comes...” She raises her weak hands and makes a gesture like breaking a twig, or maybe a chicken’s neck."
                jump creeksoldhavaaboutherself02
            '“That depends. Tell me something of value.”' ( condition="at != 'knowledge'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That depends. Tell me something of value.”')
                $ at = 0
                $ custom1 = "She straightens up, as much as her back allows her. “You think I’m afraid? Hwat do you think will happen, you’ll butcher me in the middle of the field and the others will let you leave?” Her voice is close to a shout. “I have tales in me, so many of them, ‘bout violence, opulence, betrayal. I’ve lived days that would make you fall in tears. And I regret {i}none{/i} of them.”\n\nShe takes a long pause and you realize how much heavier her breath is, how her arms start to shake. “Not the stories you need, but a lesson. Take these words with you.” She stares into your eyes with the watchfulness of an eagle. “A leader fueled by greed, pride, or vengeance will burn their own soul. They {i}will{/i} die in misery, but if their efforts outlive them, their heir must be even more ruthless, proving to their last breath that they {i}deserve{/i} to lead. Or... they may be weak, and loved by their underlings, but that’s an even harsher fate to face, as they won’t stop the rage of those who have already been harmed. And once the punishment comes...” She raises her weak hands and makes a gesture like breaking a twig, or maybe a chicken’s neck."
                $ oldhava_friendship -= 1
                $ creeks_reputation -= 1
                jump creeksoldhavaaboutherself02
            '“I doubt there are many living souls so consumed by revenge that I could claim any reward for myself. Striking you down almost three decades after your last robbery wouldn’t stop any future crime, and may harm this village. As a roadwarden, I’m going to follow the laws of these lands and respect the judgment of your tribe. The city officials will learn nothing from me... And I expect to learn more from you, as a sign of friendship.”' ( condition="at == 'knowledge'" ):
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I doubt there are many living souls so consumed by revenge that I could claim any reward for myself. Striking you down almost three decades after your last robbery wouldn’t stop any future crime, and may harm this village. As a roadwarden, I’m going to follow the laws of these lands and respect the judgment of your tribe. The city officials will learn nothing from me... And I expect to learn more from you, as a sign of friendship.”')
                $ at = 0
                $ custom1 = "She closes her eyes, and the tension leaves her lips. As she heads to a stool, you hear her exhausted breaths, and her voice is close to a whisper. “I have tales in me, so many of them, ‘bout violence, opulence, betrayal. I wouldn’t know hwere to start,” she sits down and looks at your boots. “My memory is torn. The dead, friends and foes, chase me through dreams and shadows, Wright’s face in all of them, waiting to take me to the darkest abyss.”\n\nIt takes her a few more breaths before she can speak again. “Not the stories you need, but a lesson. Take these words with you.” She stares into your eyes with the watchfulness of an eagle. “A leader fueled by greed, pride, or vengeance will burn their own soul. They {i}will{/i} die in misery, but if their efforts outlive them, their heir must be even more ruthless, proving to their last breath that they {i}deserve{/i} to lead. Or... they may be weak, and loved by their underlings, but that’s an even harsher fate to face, as they won’t stop the rage of those who have already been harmed. And once the punishment comes...” She raises her weak hands and makes a gesture like breaking a twig, or maybe a chicken’s neck."
                $ oldhava_friendship += 2
                $ creeks_reputation += 2
                jump creeksoldhavaaboutherself02

        label creeksoldhavaaboutherself02:
            $ description_glaucia10 = "According to {color=#f6d6bd}Old Hava{/color}, every bandit leader will fall to their own desires, bringing only more suffering onto others."
            $ at_unlock_knowledge = 0
            $ minutes += 5
            menu:
                '[custom1]
                '
                '{image=cointest} “What do you have for sale?”' if not oldhava_about_trade:
                    jump creeksoldhavaabouttrade01
                '{image=cointest} “I need supplies.”' if oldhava_about_trade:
                    jump creeksoldhavaabouttrade03
                '“I met some annoying howlers... Do you have any earplugs?”' if not item_earplugs and northernroad_firsttime and not oldhava_about_earplugs and oldhava_about_trade:
                    jump creeksoldhavaaboutearplugs01
                '“About those earplugs...”' if not item_earplugs and northernroad_firsttime and oldhava_about_earplugs and oldhava_about_trade:
                    jump creeksoldhavaaboutearplugs02
                '“I’m looking for a place to sleep.”' if not oldhava_about_sleep and not creeks_sleep_available:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m looking for a place to sleep.”')
                    if quest_missinghunters != 2:
                        jump creeksoldhavaaboutroom01
                    elif (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                        jump creeksoldhavaaboutroom01alt
                    else:
                        jump creeksoldhavaaboutroom02
                'The locals don’t have any room for me to rent. (disabled)' if oldhava_about_sleep == 1 and not creeks_feast:
                    pass
                'The locals don’t trust me enough to let me own a room here. (disabled)' if oldhava_about_sleep == 1 and creeks_feast and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                    pass
                '“We were talking about the room...”' if (oldhava_about_sleep == 1 and creeks_feast and not creeks_sleep_available) or (oldhava_about_sleep == 2 and (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) >= 25 and not creeks_sleep_available):
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “We were talking about the room...”')
                    if (creeks_reputation+efren_friendship+elah_friendship+oldhava_friendship+appearance_charisma) < 25:
                        jump creeksoldhavaaboutroom01alt
                    else:
                        jump creeksoldhavaaboutroom02
                '“I know about your past, {color=#f6d6bd}Erith{/color}.”' if description_creeks08 and not oldhava_background:
                    jump creeksoldhavaaboutherself01
                '“I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”' if oldhava_about_trade and not oldhava_about_foggy:
                    jump creeksoldhavaaboutfoggy01
                'She’s not willing to tell me more about merchants. (disabled)' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) < 10:
                    pass
                '“I was asking about the merchants...”' if oldhava_about_trade and oldhava_about_foggy == 1 and (oldhava_friendship+appearance_charisma+creeks_reputation) >= 10:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t expect many merchants to reach this place. Why don’t you move your traps to {color=#f6d6bd}Foggy’s{/color}?”')
                    jump creeksoldhavaaboutfoggy02
                '“Farewell.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                    jump creeksafterinteraction01

### INVITATION
label creeksinvitingpctojointhetribe01:
    $ elah_lastseen = day
    $ creeks_offeredtojoin = 1
    $ travel_destination = "creeks"
    menu:
        '[custom1] Ever since we said farewell to our hunting friends and siblings, the tribe of {color=#f6d6bd}Creeks{/color} sees we’re lacking fresh blood, and that we got too cocky with these woods and roads. If you think this is a good place for you...” His dramatic pause is betrayed by the shaking lips of his concealed smile. “You could stay with us for however long you’d like. We already voted on it, and to be honest, you’re quite popular!” His laughter is so honest you can’t help but feel warmth in your stomach.
        '
        '“That sounds... I’d love that, friend. But I need to finish a few things first.”':
            jump creeksinvitingpctojointhetribe01a
        '“I don’t know what to say. I need some time to think.”':
            jump creeksinvitingpctojointhetribe01b
        '“I’m honored and grateful, but I have to refuse.”':
            jump creeksinvitingpctojointhetribe01c
        '“You misconstrue my motivations to help you, {color=#f6d6bd}Elah{/color}. I have an exciting life ahead of me, and I’m not going to get tied to a little hamlet like yours.”':
            jump creeksinvitingpctojointhetribe01d
        '“...Care to elaborate?”':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “...Care to elaborate?”')
            if creeks_youth_sex or creeks_youth_gambling >= 3:
                $ custom1 = ", and a few tales make me think you’ll find a way to start a family, and very soon,” he winks at you with a smirk."
            elif creeks_youth_gambling == 2:
                $ custom1 = ", and a few tales make me think you can find a companion here, if you have some patience for it,” he gives you a humble smile."
            else:
                $ custom1 = ". I can’t promise you’ll find a family here, but you’ll have friends at your side,” he gives you a humble smile."
            menu:
                '“You’ve seen our days, there isn’t much to explain,” he pats his stomach. “Hwile you have all your limbs and a clear head, you’ll escort your neighbors on their hunts, and merchants on their trips to other villages. We hope to trade much more in the following months, you know!” He adjusts his shoulder cloak and takes a deep breath. His posture is uncharacteristically relaxed.
                \n\n“We’ll keep you fed and clothed, and you’ll never have a lonely day again in your life. You’ll feast with us not as a traveler, but as one of us[custom1] “Hwatever spirit you may pray toward, you’ll have your space to do so. You’ll witness the grand growth of {i}your{/i} home, farms, art, visitors! Trust us, [pcname],” he looks around and you notice many more faces observing you. “As we are ready to trust you.”
                '
                '“That sounds... I’d love that, friend. But I need to finish a few things first.”':
                    jump creeksinvitingpctojointhetribe01a
                '“I don’t know what to say. I need some time to think.”':
                    jump creeksinvitingpctojointhetribe01b
                '“I’m honored and grateful, but I have to refuse.”':
                    jump creeksinvitingpctojointhetribe01c
                '“You misconstrue my motivations to help you, {color=#f6d6bd}Elah{/color}. I have an exciting life ahead of me, and I’m not going to get tied to a little hamlet like yours.”':
                    jump creeksinvitingpctojointhetribe01d
                '“You do realize I’m not always going to be young, and having me patrolling the roads will sooner or later result in me losing a hand or a leg, if not my head. What then?”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You do realize I’m not always going to be young, and having me patrolling the roads will sooner or later result in me losing a hand or a leg, if not my head. What then?”')
                    menu:
                        '“You’ve seen our elders, friend. They are cared for. Our lives are rough, but full. No matter if I am to see only a few more years or a few more generations, I know my eyes will be grateful,” his white teeth are almost shining. “Can you say the same about living in the city?”
                        '
                        '“That sounds... I’d love that, friend. But I need to finish a few things first.”':
                            jump creeksinvitingpctojointhetribe01a
                        '“I don’t know what to say. I need some time to think.”':
                            jump creeksinvitingpctojointhetribe01b
                        '“I’m honored and grateful, but I have to refuse.”':
                            jump creeksinvitingpctojointhetribe01c
                        '“You misconstrue my motivations to help you, {color=#f6d6bd}Elah{/color}. I have an exciting life ahead of me, and I’m not going to get tied to a little hamlet like yours.”':
                            jump creeksinvitingpctojointhetribe01d

    label creeksinvitingpctojointhetribe01a:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “That sounds... I’d love that, friend. But I need to finish a few things first.”')
        $ pc_goal_iwantnewlife_creeks = 1
        $ creeks_reputation += 1
        if pc_goal == "iwanttostartanewlife":
            $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s' %quest_pc_goal_name)
        menu:
            'He spreads his arms. “Do so! The Ten Cities may take a step back from your life, but it’s not like we’re hermits! Close this old chest of yours and come back, just don’t die before spring!”
            \n\nHe’s standing a few feet away, not sure what to say.
            '
            'I smile. “Oh, I don’t plan to die anytime soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Oh, I don’t plan to die anytime soon.”')
                menu:
                    '“We are both souls with big plans,” his eyes are gentle. “Goodbye, [pcname].”
                    '
                    '“Farewell.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                        jump creeksafterinteraction01
            'I shake his hand.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake his hand.')
                $ elah_friendship += 1
                menu:
                    'His large hand is callused, and even the brief touch is enough to notice the cuts and chopped off skin, signs of his amateurish labor. “I knew when I saw you that your arrival would start something new. Have a safe journey to {color=#f6d6bd}Hovlavan{/color}, [pcname].”
                    \n\nHe steps away and starts to climb up the hill.
                    '
                    '“{i}Aye{/i}. Good luck with the winter preparations.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}Aye{/i}. Good luck with the winter preparations.”')
                        jump creeksafterinteraction01
            'I step closer and hug him.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step closer and hug him.')
                $ elah_friendship += 2
                menu:
                    'He smells of wood shavings and mud, but also cooked meat. You stay in a brief embrace, without a word. After a few breaths, he heads up the hill.
                    '
                    'I also walk away, without looking back.':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I also walk away, without looking back.')
                        jump creeksafterinteraction01

    label creeksinvitingpctojointhetribe01b:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t know what to say. I need some time to think.”')
        $ pc_goal_iwantnewlife_creeks = 1
        if pc_goal == "iwanttostartanewlife":
            $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s' %quest_pc_goal_name)
        menu:
            '“Think however long you need, we’re not going anywhere,” he grins. “But the roads won’t get any safer after the spring. Be back with the new year, we’ll gather wood for a bonfire!”
            \n\nHe’s standing a few feet away, not sure what to say.
            '
            'I smile. “Oh, I don’t plan to die anytime soon.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smile. “Oh, I don’t plan to die anytime soon.”')
                menu:
                    '“We are both souls with big plans,” his eyes are gentle. “Goodbye, [pcname].”
                    '
                    '“Farewell.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                        jump creeksafterinteraction01
            'I shake his hand.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I shake his hand.')
                $ elah_friendship += 1
                menu:
                    'His large hand is callused, and even the brief touch is enough to notice the cuts and chopped off skin, signs of his amateurish labor. “I knew when I saw you that your arrival would start something new. Have a safe journey to {color=#f6d6bd}Hovlavan{/color}, [pcname].”
                    \n\nHe steps away and starts to climb up the hill.
                    '
                    '“{i}Aye{/i}. Good luck with the winter preparations.”':
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{i}Aye{/i}. Good luck with the winter preparations.”')
                        jump creeksafterinteraction01

    label creeksinvitingpctojointhetribe01c:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m honored and grateful, but I have to refuse.”')
        $ elah_friendship -= 1
        menu:
            'He skips a breath. “But I thought...” He clenches his jacket and bites his upper lip, fighting with the words he wants to say. “I respect your decision and honesty, {i}good luck{/i} on the road.” The last few words reach you when he’s already turned away, approaching the gate.
            '
            '“Farewell.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Farewell.”')
                jump creeksafterinteraction01

    label creeksinvitingpctojointhetribe01d:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You misconstrue my motivations to help you, {color=#f6d6bd}Elah{/color}. I have an exciting life ahead of me, and I’m not going to get tied to a little hamlet like yours.”')
        $ elah_friendship -= 2
        $ creeks_reputation -= 1
        $ elah_locked = day
        menu:
            'He observes you for a few breaths, then turns away and goes up the hill.
            '
            'I glance at the disappointed faces and return to {color=#f6d6bd}[horsename]{/color}.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I glance at the disappointed faces and return to {color=#f6d6bd}%s{/color}.' %horsename)
                jump creeksafterinteraction01

### THE FEAST
label creekthegrandfeast01:
    $ item_rawhide = 0
    # $ renpy.notify("You lost the rawhide.")
    # $ narrator.add_history(kind='nvl', who=narrator.name, what='- You lost the rawhide.')
    $ quarters = world_daylength
    stop music fadeout 4.0
    play nature "audio/ambient/creeksbonfire01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture creeksbonfire01 at basicfade
    $ creeks_feast = 1
    nvl clear
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if quest_missinghunters_vaschelfound == 2:
        $ custom1 = " The bone earring instantly vanishes among the logs."
    else:
        $ custom1 = ""
    ###
    if quest_missinghunters_admonfound == 2:
        $ custom2 = " The broken knife is already black from soot."
    else:
        $ custom2 = ""
    ####
    if item_bonebuckle_returned:
        $ custom2 = " The belt buckle is disappearing in a growing pile of ash."
    else:
        $ custom2 = ""
    ####
    if item_pileofbones_returned:
        $ custom4 = " The bones you collected are cracking hauntingly from the heat, but that doesn’t stop the cooks from piercing chunks of game meat with long sticks and holding them in the flames."
    else:
        $ custom4 = " The cooks have pierced the chunks of game meat with long sticks, and are holding them in the flames."
    menu:
        'The rites take little time and go by without prayers, singing, or sacrifices. The family members share their memories and regrets. Every story you hear is vague, yet accompanied by understanding nods and looks shared among the tribe, as well as chuckles and tears that start long before the conclusion. After the years you spent in {color=#f6d6bd}Hovlavan{/color}, it’s hard for you to imagine how familiar and intimate all of the people around you are. Even {color=#f6d6bd}Foggy{/color} and her staff are paying a visit - this evening, the tavern is closed.
        \n\nYou now sit at a table, and the first few meals are brought in. The bowls are mostly filled with meat, but it’s the humble loaves of bread, slices of cheese, herb sauces, smoked fish, and wild fruits that disappear first. The warmth of the bonfire is reaching your hands and face, comforting you whenever a cold gust of wind hits the square.[custom1][custom2][custom4]
        '
        'There may be no priests, but I share the solemnity of the moment.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- There may be no priests, but I share the solemnity of the moment.')
            $ custom1 = "The wood cracks beneath the flames. You’ve never seen the village of {color=#f6d6bd}Creeks{/color} as quiet as it is now, but the way the locals face their mourning is anything but lonely. Pats on backs or hands are common, as well as long embraces and whispered condolences."
            jump creekthegrandfeast01a
        'I mostly focus on the food.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I mostly focus on the food.')
            $ custom1 = "The fat and juices drip from your fingers and chin. Having no bread-like trancher forces you to either wash yourself in the creek, or use a piece of cloth between the bites. The birds were roasted hours earlier and are already cold, mixed with salads and fruits to compensate for their underseasoned, stale flavor. The red meats are still warm, and more of them will come later."
            jump creekthegrandfeast01a

    label creekthegrandfeast01a:
        $ pc_food = limit_pc_food(pc_food+4)
        show plus4food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+4 nourishment points.{/i}')
        menu:
            '[custom1]
            \n\nAs time goes on, more and more people rest on the stools and chairs, though there are few exceptions - an old man with no legs is lying on a blanket, served by a girl who seems to be his great-granddaughter. One of the hunters steps away to get back on the watchtower, keeping an eye out for any being that may be lured by the noises. [shoshi_namebig] is sitting in front of a building, singing about the forests of the past and the gardens of tomorrow. The cooks are bustling about, bringing supplies from the house of gatherings and taking care of the roasting meat. Most of the children are only half-awake.
            \n\nAs the cups get filled with mead, ale, and cider, brought here by {color=#f6d6bd}Foggy{/color}, {color=#f6d6bd}Efren{/color} is the first person to sit down next to you, and loudly, though he’s still observing the flames. His wolf cloak is nowhere in sight, though from time to time he reaches toward his head, as if he’s not used to the wind brushing his black hair, now shining in the dancing light. Judging by the way he sways and how absent his eyes are, he opened one of the casks a few hours back.
            '
            '“How are you holding up?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “How are you holding up?”')
                $ custom1 = "“I’m using my privilege of being {i}still alive{/i} to heal,” he starts with confidence, but then his voice cracks. “Folks say I did nothing wrong, but, you know? I could’ve, you know? Said {i}no{/i}, stopped them. And I’ve seen how, what’s her face? {color=#f6d6bd}Dalia’s{/color} li’l sis looks at me. She’s only ten, and now alone! I’m as useful as a spirit!” Once you figure out what he’s talking about, you try to respond, but he interrupts you by pointing at you with his mug."
                jump creekthegrandfeast01b
            '“Where’s your hood?”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Where’s your hood?”')
                $ custom1 = "He scoffs. “My boring-ass brother told me it’s too {i}silly{/i} for the rites, you hear that? My trophy, my biggest prey, {i}too silly{/i} to say farewell to three {i}hunters{/i}.” You try to respond, but he interrupts you by pointing at you with his mug."
                $ elah_efren_siblings = 1
                jump creekthegrandfeast01b

    label creekthegrandfeast01b:
        $ quest_missinghunters = 2
        if pc_goal == "iwanttohelp":
            $ pc_goal_iwanttohelppoints += 2
        if pc_goal == "iwanttoberemembered":
            if (quest_missinghunters_admonfound == 2 and quest_missinghunters_daliafound == 2 and quest_missinghunters_vaschelfound == 2):
                $ pc_goal_iwanttoberememberedpoints += 2
                if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                    $ renpy.notify("Quest completed: The Missing Hunters.\nJournal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Missing Hunters.\nJournal updated: %s{/i}' %quest_pc_goal_name)
            elif (quest_missinghunters_admonfound == 2 and quest_missinghunters_daliafound == 2) or (quest_missinghunters_admonfound == 2 and quest_missinghunters_vaschelfound == 2) or (quest_missinghunters_vaschelfound == 2 and quest_missinghunters_daliafound == 2):
                $ pc_goal_iwanttoberememberedpoints += 1
                if quest_pc_goal == 1 and pc_goal == "iwanttoberemembered":
                    $ renpy.notify("Quest completed: The Missing Hunters.\nJournal updated: %s" %quest_pc_goal_name)
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Missing Hunters.\nJournal updated: %s{/i}' %quest_pc_goal_name)
            else:
                $ renpy.notify("Quest completed: The Missing Hunters")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Missing Hunters{/i}')
        else:
            $ renpy.notify("Quest completed: The Missing Hunters")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Missing Hunters{/i}')
        $ quest_missinghunters_description02 = "{color=#f6d6bd}Efren{/color} will help me in a time of need."
        if efren_about_missinghunters_dayreported < (day-3):
            $ creeks_reputation += 1
            menu:
                '[custom1]
                \n\n“I’m now in your debt, aye? We going on a journey? I was losing my wits waiting for this evening, thanks for not keeping me... waiting...” As he rambles, his thoughts wander off somewhere else, and before he gets back to you, {color=#f6d6bd}Elah{/color} gives him a pat on his back and places a full mug in front of you.
                '
                'I smell the contents before I drink anything.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smell the contents before I drink anything.')
                    $ custom1 = "You catch the sweetness and distinctive aromas of roasted malts. A single sip makes you think of a cookie coated with caramelized sugar - something you smelled a few times among the city stalls, though you never bought more than one at a time. The beverage is much stronger than most beers and ales you’ve tasted, but far from being dull, so you decide to enjoy it slowly. {color=#f6d6bd}The carpenter{/color} nods approvingly, grabs himself a stump, and joins you with his own slow drinking."
                    $ elah_friendship += 1
                    jump creekthegrandfeast01c
                'I’d better chug it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’d better chug it.')
                    $ custom1 = "You hardly manage to get through half of the mug, almost spitting it out. The distinct malts are heavy and after a few gulps burn your mouth. The beverage is much stronger than most beers and ales you’ve tasted and for now you put it away, resting your forehead on an open palm as you try to forget your mistake. {color=#f6d6bd}The hunter{/color} bursts into laughter, luring interested looks from his melancholic tribe, while {color=#f6d6bd}the carpenter{/color} simply smiles, grabs himself a stump, and joins you with his own slow drinking."
                    $ efren_friendship += 1
                    jump creekthegrandfeast01c
                '“I’m not getting drunk tonight.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not getting drunk tonight.”')
                    $ custom1 = "“Your call, but at least taste it. It’s {i}too good{/i} to go to waste,” he smiles to you, but then the mug appears in {color=#f6d6bd}the hunter’s{/color} hands, and all that remains for {color=#f6d6bd}the carpenter{/color} is to sigh with resignation. He grabs himself a stump and drinks from his own wooden mug."
                    jump creekthegrandfeast01c
        else:
            $ efren_friendship -= 1
            menu:
                '[custom1]
                \n\n“I’m now in your debt, aye? We going on a journey?” His eyes shift into anger. “I was losing my wits waiting for this evening, you kept me for so long... waiting... can’t you see those hwere my friends...” As he rambles, his thoughts wander off somewhere else, and before he gets back to you, {color=#f6d6bd}Elah{/color} gives him a pat on his back and places a full mug in front of you.
                '
                'I smell the contents before I drink anything.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I smell the contents before I drink anything.')
                    $ custom1 = "You catch the sweetness and distinctive aromas of roasted malts. A single sip makes you think of a cookie coated with caramelized sugar - something you smelled a few times among the city stalls, though you never bought more than one at a time. The beverage is much stronger than most beers and ales you’ve tasted, but far from being dull, so you decide to enjoy it slowly. {color=#f6d6bd}The carpenter{/color} nods approvingly, grabs himself a stump, and joins you with his own slow drinking."
                    $ elah_friendship += 1
                    jump creekthegrandfeast01c
                'I’d better chug it.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’d better chug it.')
                    $ custom1 = "You hardly manage to get through half of the mug, almost spitting it out. The distinct malts are heavy and after a few gulps burn your mouth. The beverage is much stronger than most beers and ales you’ve tasted and for now you put it away, resting your forehead on an open palm as you try to forget your mistake. {color=#f6d6bd}The hunter{/color} bursts into laughter, luring interested looks from his melancholic tribe, while {color=#f6d6bd}the carpenter{/color} simply smiles, grabs himself a stump, and joins you with his own slow drinking."
                    $ efren_friendship += 1
                    jump creekthegrandfeast01c
                '“I’m not getting drunk tonight.”':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’m not getting drunk tonight.”')
                    $ custom1 = "“Your call, but at least taste it. It’s {i}too good{/i} to go to waste,” he smiles to you, but then the mug appears in {color=#f6d6bd}the hunter’s{/color} hands, and all that remains for {color=#f6d6bd}the carpenter{/color} is to sigh with resignation. He grabs himself a stump and drinks from his own wooden mug."
                    jump creekthegrandfeast01c

    label creekthegrandfeast01c:
        menu:
            '[custom1]
            \n\nAll three of you stare into the flames, hardly noticing a few more tribesfolk that gather behind you. {color=#f6d6bd}The carpenter{/color} breaks the silence. “How are you doing, [pcname]? Life’s been treating you good in the peninsula?”
            '
            '“I’ve had some good days. I’m making progress.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve had some good days. I’m making progress.”')
                $ custom1 = "“Wonderful,” he strokes his stomach and meets your eyes. “Just don’t disappear like {color=#f6d6bd}Asterion{/color}. He’d rather chase after something his whole life than walk away with li’l. Not unlike me, but also,” he tilts his mug, pointing the mouth of it at the flames. “Not unlike them.”"
                jump creekthegrandfeast01d
            '“Every day is a struggle. I feel stuck.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Every day is a struggle. I feel stuck.”')
                $ custom1 = "“I’m so sorry to hear that,” his eyes match his words. “Just like {color=#f6d6bd}Asterion{/color}, you’re ambitious, and much more than I’d expect a roadwarden to be. I wish there was a way to simply want... Less.”"
                jump creekthegrandfeast01d
            '“It’s a savage place, {color=#f6d6bd}Elah{/color}. I’m just trying to survive.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “It’s a savage place, {color=#f6d6bd}Elah{/color}. I’m just trying to survive.”')
                $ custom1 = "He nods. “I hear you, I could never live on the road. You may be free, but at hwat cost? This land won’t belong to humans anytime soon, if ever.”"
                jump creekthegrandfeast01d
            '“I don’t even think about it. I’ll start living once I’m done with what I need to do.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I don’t even think about it. I’ll start living once I’m done with what I need to do.”')
                $ custom1 = "He clenches his stomach. “I keep saying the same thing. {i}Once I’m done with this{/i}, hwatever this is, {i}I’ll be ready, things will change{/i}. And then I look for another thing, and the years go by. I hope you’re smarter than I am.”"
                jump creekthegrandfeast01d

    label creekthegrandfeast01d:
        menu:
            '[custom1]
            \n\nAfter a few moments you realize that almost all of the adults are gathered behind you, observing you keenly. As the tension rises, you think about your blade, now resting by your saddlebags. It’s {color=#f6d6bd}Elah{/color} who asks the question.
            \n\n“We owe you a lot, [pcname]. Hwy do you really help us?”
            '
            '“{color=#f6d6bd}Hovlavan{/color} wants to reach this land. For your own sake, you should join it. Taxes for their protection, loyalty for the renewed trading route.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “{color=#f6d6bd}Hovlavan{/color} wants to reach this land. For your own sake, you should join it. Taxes for their protection, loyalty for the renewed trading route.”')
                jump creekthegrandfeast01e

    label creekthegrandfeast01e:
        $ questionpreset = "creeksfeast1"
        menu:
            '“{color=#f6d6bd}Old Hava{/color} was right,” says one of the farmers. “So {i}that’s{/i} hwy they sent the second one,” adds a woodcutter. The fuss stops as quickly as it started, cut by the loud voice of the drunk {color=#f6d6bd}Efren{/color}. “Let the roadwarden make a case for it!”
            \n\nYou glance at the eyes of the locals. Some of them are distrustful, others are curious, and a few are excited. Even though you already recognize many of these faces, the dancing flames make them look like a strange crowd awaiting a prophecy.
            '
            '(creeksfeast1 set)':
                pass

    label creeksefeastaboutbeastattacks01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “An old druid who lives on the opposite side of the peninsula told me about the recent migrations of beasts in the North. You’ve been struggling with monsters for decades now - it’s finally time for you to seek allies.”')
        jump creeksefeastaboutbeastattacks02
        label creeksefeastaboutbeastattacks01alt:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve heard about the recent migrations of beasts in the North. You’ve been struggling with monsters for decades now - it’s finally time for you to seek allies.”')
            jump creeksefeastaboutbeastattacks02
        label creeksefeastaboutbeastattacks02:
            $ creeks_reasonstojoin_feast_beastattacks += 1
            $ creeks_reasonstojoin_points += 2
            $ questionpreset = "creeksfeast1"
            menu:
                '“Beasts don’t enter our valley,” says one of the hunters, but is quickly shushed. “{i}Yet{/i},” adds a one-handed farmer harshly, while an herbalist with wavy hair points at the bonfire. “And even if, it’s turning into a prison.”
                \n\nSome of the locals nod in agreement, but {color=#f6d6bd}Old Hava’s{/color} tone is far from docile. “Better to have a troll in the yard than a dragon in the bed.”
                '
                '(creeksfeast1 set)':
                    pass

    label creeksefeastaboutlackofmetal01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I’ve seen your tools, weapons, houses. You {i}need{i} iron, you {i}need{/i} copper. {color=#f6d6bd}Hovlavan{/color} will help you gain steel, bronze, and brass.”')
        $ creeks_reasonstojoin_feast_lackofmetal += 1
        $ creeks_reasonstojoin_points += 1
        $ questionpreset = 0
        menu:
            'A dark-skinned builder crosses her arms. “We’ve got no smiths, either. No furnaces, no place to learn.” You mention that there are always artisans looking for work. “{i}Apprentices{/i}, maybe,” {color=#f6d6bd}Foggy{/color} corrects you.
            '
            '“At least you may be sure that they will have enough arms to assist your labor, and enough years left to stay with you for a long time.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “At least you may be sure that they will have enough arms to assist your labor, and enough years left to stay with you for a long time.”')
                $ creeks_reasonstojoin_points += 1
                $ questionpreset = "creeksfeast1"
                menu:
                    'You note approving looks among the youth. “Fresh blood is of value,” says a forager, and {color=#f6d6bd}Elah{/color} encourages them with a smile. “And after hwat I’ve heard about the city guilds, I don’t think an apprentice would be a lazy good-for-nothing.”
                    '
                    '(creeksfeast1 set)':
                        pass
            '“Then forget about smiths. You can buy the tools and blades instead of alloys.”':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Then forget about smiths. You can buy the tools and blades instead of alloys.”')
                $ questionpreset = "creeksfeast1"
                menu:
                    '“Buy with hwat?” A farmer gestures for you to look around, as if the village’s very nature is proof they won’t be able to afford such luxuries. The discussion starts to circle around the practicality of this solution, and the delay between making an order and receiving new equipment. After a few minutes of futile squabbles, {color=#f6d6bd}Elah{/color} encourages you to go on, causing the others to fall silent.
                    '
                    '(creeksfeast1 set)':
                        pass

    label creeksefeastaboutmeat01:
        $ creeks_reasonstojoin_feast_lackofmeat += 1
        $ creeks_reasonstojoin_points += 1
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I know you don’t have as many supplies as you need. Depending on animals you keep alive to butcher is not a safe way to deal with the winters.”')
        $ questionpreset = "creeksfeast1"
        menu:
            'Some of them don’t meet your eyes, as if to avoid admitting to the days of hunger. {color=#f6d6bd}Efren{/color} lets out a sigh. “At the beginning of summer, I’d say...” He pauses to break through the cloud of drink. “We had more hunters than ever, but...” He takes a glance at the bonfire and turns back to the crowd quickly, clenching his teeth.
            \n\n{color=#f6d6bd}Elah{/color} observes him for a moment, but doesn’t comment on his behavior. “We {i}do{/i} have a field now. It may not be so bad.” The rest of the tribe adds to both sides of the argument, though no conclusion is reached.
            '
            '(creeksfeast1 set)':
                pass

    label creeksefeastaboutlackingwall01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You don’t really believe this wall will keep you safe, do you? Without a forest garden, you lack wood, and you can’t afford stone. You need proper guards to protect your homes and lumberjacks.”')
        $ creeks_reasonstojoin_feast_lackingwall += 1
        $ creeks_reasonstojoin_points += 1
        $ questionpreset = "creeksfeast1"
        menu:
            '“Our wall has been enough so far,” starts one of the farmers, but his partner, now holding an arm around his back, is more doubtful. “We lost children, chicken, and food to the smaller beasts, we don’t have enough eyes to watch {i}everything{/i}.”
            \n\n{color=#f6d6bd}Elah{/color} chips in with enthusiasm. “If we hope to grow our families or invite new folks, we’ll need more homes, more ground, a new wall. I’d rather have it be a strong one.”
            \n\nStill, some of the locals would rather see more effort put into the new fields rather than a wall. “One bad fire in the forest and we go hungry,” mentions a forager, and a few others agree.
            '
            '(creeksfeast1 set)':
                pass

    label creeksefeastaboutweakness01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look at {color=#f6d6bd}Elah{/color} and {color=#f6d6bd}Efren{/color}. “I know you don’t agree about what it means to be {i}weak{/i}, but you don’t have to. With allies at your side, the days of weakness won’t be so punishing.”')
        $ creeks_reasonstojoin_feast_weakness += 1
        $ creeks_reasonstojoin_points += 1
        $ questionpreset = "creeksfeast1"
        menu:
            'The brothers exchange looks, but don’t respond. Still, this thought seems to spark the imagination of the tribesfolk, some of who remember a “harsh winter” that fell upon them a year ago, and they’d rather be sure they can buy extra supplies in autumn, or grain in spring. On the other hand, {color=#f6d6bd}Foggy{/color} mentions that food gets especially pricy during such seasons, and that it may take all of her savings much sooner than the others expect.
            '
            '(creeksfeast1 set)':
                pass

    label creeksefeastaboutinbreeding1:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Your blood is growing thick. You can seek new settlers among cityfolk, or use the safer roads to find willing people in other villages.”')
        $ creeks_reasonstojoin_feast_inbreeding += 1
        $ creeks_reasonstojoin_points += 1
        $ questionpreset = "creeksfeast1"
        menu:
            'A skinny farmer snickers. “Do you address our blood, or our loins?” A few of the locals chuckle, but even though the scarcity of food is brought up, most of the locals seem to agree it’s a problem that needs to be addressed sooner rather than later.
            '
            '(creeksfeast1 set)':
                pass

    label creeksefeastaboutseeds01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You want to grow crops, but you have no experience. With the city’s help, you may hire a specialist to teach you everything you need to know, and invest in the best seeds.”')
        $ creeks_reasonstojoin_feast_lakingseeds += 1
        $ creeks_reasonstojoin_points += 1
        $ questionpreset = "creeksfeast1"
        menu:
            '{color=#f6d6bd}Old Hava{/color} is quick to mention that the fine grain will cost much more than the seeds of wild fruits and vegetables, but as soon as she finishes, one of the hunters confronts her. “{color=#f6d6bd}Hava{/color}, you don’t always know {i}how{/i} to plant these seeds. I’ve heard about the plant beds having nothing but grass for more than a year,” as he mentions it, the other farmers observe their boots, as if to avoid their angry headwoman. Once the argument between the two gets a bit too bitter, {color=#f6d6bd}Efren{/color} nudges you to go on.
            '
            '(creeksfeast1 set)':
                pass

    label creeksefeastaboutsteephouse01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take a longer pause and scowl at the tribe. “You know well what happened to {color=#f6d6bd}Steep House{/color}. Are you truly willing to trust that none of your neighbors will look at your village with greedy eyes once you become prosperous?”')
        $ creeks_reasonstojoin_feast_steephouse += 1
        $ questionpreset = "creeksfeast1"
        if elah_about_nomoreundead == 3:
            menu:
                'The tribe gives you a long look, until a quiet, but disdainful voice breaks the silence. “Sad by the butcher of {color=#f6d6bd}White Marshes{/color},” she says, and the others grunt in agreement. While a few souls look down, most of them can withstand your gaze.
                '
                '(creeksfeast1 set)':
                    pass
        else:
            if not quest_ruins_description_creeksparticipated:
                $ creeks_reasonstojoin_points += 1
            else:
                $ creeks_reasonstojoin_points += 2
            menu:
                'The tribe gives you a long look, but with every breath a new pair of eyes fills with shame. Only one of the elders raises his voice. “True! They’re not to be trusted!”
                \n\n“Aye. And neither are we,” adds {color=#f6d6bd}Elah{/color} quietly, and his words are followed by silence.
                '
                '(creeksfeast1 set)':
                    pass

    label creeksefeastaboutmissinghunters01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “You know how dangerous this land is. I brought you evidence that I found three of your finest hunters, all of them felled by beasts. You can’t afford more losses, and you can see that {i}cityfolk{/i} can get things done.”')
        $ creeks_reasonstojoin_feast_missinghunters += 1
        $ creeks_reasonstojoin_points += 1
        $ questionpreset = "creeksfeast1"
        menu:
            '“Aye, friend. You’ve proven your bravery,” adds one of {color=#f6d6bd}Dalia’s sisters{/color}, though her voice is weak. You mention the city’s soldiers, artisans, pathfinders, and scholars, but one of the younger foragers chips in. “And priests,” she whispers, and the crowd exchanges worried looks.
            '
            '(creeksfeast1 set)':
                pass

    label creeksefeastaboutplague01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Sooner or later, a plague will reach your village. Living in isolation will postpone this day, but once it comes, how can you know help will ever come? Your best chance is to keep people like me around.”')
        $ creeks_reasonstojoin_feast_plague += 1
        $ creeks_reasonstojoin_points += 1
        $ questionpreset = "creeksfeast1"
        menu:
            '“If you’re so eager, maybe it’s {i}you{/i} who should stay around,” mentions [shoshi_namesmall], but her herbalist friend shakes her head. “We need not one soul, but a way to find many in its place. Plagues are stronger than one’s shell and will.”
            \n\nEven though she says so, a many in the tribe give you warm smiles.
            '
            '(creeksfeast1 set)':
                pass

    label creeksefeastabouteasternpath01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “Just look how much work I was able to complete at the eastern path. You can’t keep it clear all by yourself, but with the city’s army and regular merchant trips it will endure winters and rains.”')
        $ creeks_reasonstojoin_feast_easternpath += 1
        $ creeks_reasonstojoin_points += 2
        $ questionpreset = "creeksfeast1"
        menu:
            '{color=#f6d6bd}Elah{/color} eagerly agrees. “Your horsemanship got you further than any of us in a long time...”
            \n\nOne of the hunters interrupts him. “But you can see that the roadwarden has never helped us for our sake, aye? They’re the city’s spy.”
            \n\n{color=#f6d6bd}The carpenter{/color} gives him a long look, then carries on slowly. “Spy or not, [pcname]’s past efforts will change our future, and I’m willing to see hwat else a single roadwarden can do. Not to mention a squad of soldiers.”
            '
            '(creeksfeast1 set)':
                pass

    label creeksefeastaboutfoggy01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} Maybe I shouldn’t try it, but... “{color=#f6d6bd}Foggy{/color}, won’t you vouch for me? You know I’m a valuable ally, and the tribe depends on your tavern. The city will bring many more people to help you.”')
        $ creeks_reasonstojoin_feast_foggy += 1
        $ creeks_reasonstojoin_points += 1
        $ questionpreset = "creeksfeast1"
        if foggy_friendship >= 15 or foggy_food_meals_available_free:
            $ creeks_reasonstojoin_points += 1
            menu:
                'For a moment you’re convinced that her laughter has put out the fire behind you. “Of course, love! You trust the cityfolk, and I trust you. I’ll speak with any official who dares to leave their silk sheets and hit the road.”
                '
                '(creeksfeast1 set)':
                    pass
        elif foggy_friendship >= 10:
            menu:
                'She scratches her large chin and lets out a loud sigh. “I don’t know, love. Your deeds speak for themselves, but {i}not{/i} for the city priests, merchants, and officials. I’d rather listen to hwat you think we can gain from an alliance.”
                '
                '(creeksfeast1 set)':
                    pass
        elif foggy_friendship >= 6:
            $ foggy_friendship -= 1
            menu:
                'She frowns. After a longer moment, she raises her only arm and gestures for you to stop. “You’re asking the wrong soul, dear. You’re my client, that’s it.”
                \n\nIn awkward silence, you think about your next move.
                '
                '(creeksfeast1 set)':
                    pass
        else:
            $ foggy_friendship -= 1
            $ creeks_reputation -= 1
            $ creeks_reasonstojoin_points -= 1
            menu:
                'She scoffs and waves at you with her only arm. “Dear, you’re but a stranger. You think I’d risk my good name for your games? Show me first you can survive until winter.”
                \n\nSurrounded by awkward whispers and harsh looks, you think about your next move.
                '
                '(creeksfeast1 set)':
                    pass

    label creeksefeastaboutreputation01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- {image=d6} It’s risky, but... “You know me well, I have your trust. I wouldn’t try to trick you.”')
        $ creeks_reasonstojoin_feast_reputation += 1
        $ questionpreset = "creeksfeast1"
        if creeks_reputation >= 16:
            $ creeks_reasonstojoin_points += 2
            menu:
                'One of the hunters nods with conviction and licks his lips before he speaks. “Roadwarden is a friend of our tribe,” he starts, and many {i}ayes{/i} come from other parts of the square. Brief anecdotes focused on your deeds and words serve you well, but {color=#f6d6bd}Efren{/color} reaches for his absent hood and scoffs. “We ought to listen to strong thoughts, not soft hearts,” he says loudly, but the majority of the group dismisses his point.
                '
                '(creeksfeast1 set)':
                    pass
        elif creeks_reputation >= 12:
            $ creeks_reasonstojoin_points += 1
            menu:
                'After a few breaths, one of the foragers speaks softly. “Roadwarden has brought us a lot of good, and isn’t just a city servant.” A few {i}ayes{/i} come from the people around her, as well as brief anecdotes focused on your deeds and words, until {color=#f6d6bd}Efren{/color} reaches for his absent hood and scoffs. “We ought to listen to strong thoughts, not soft hearts,” he says loudly, and the majority of the group nods in agreement.
                '
                '(creeksfeast1 set)':
                    pass
        elif creeks_reputation >= 8:
            $ creeks_reputation -= 1
            menu:
                'After a few breaths and many awkward looks, one of the farmers raises his voice. “You’re not one of us, friend, even if we wish you well.” A few {i}ayes{/i} come from the people around him, as well as brief anecdotes proving that you don’t know much about the locals and their troubles. {color=#f6d6bd}Efren{/color} clears his throat and speaks loudly. “We’ll listen to strong thoughts, not a soft heart.” The majority of the group nods in agreement.
                '
                '(creeksfeast1 set)':
                    pass
        else:
            $ creeks_reputation -= 1
            $ creeks_reasonstojoin_points -= 1
            menu:
                'A surprised muttering spreads through the tribe, and you even hear a louder “Hwat’s this outsider talking about?” Once the locals start giving you angry looks, {color=#f6d6bd}Efren’s{/color} the first one to address you. “For our tribe, you’re but a stranger. If we were to ever trust you, better use your thoughts, not your heart.” The group either nods in agreement, or observes you harshly.
                '
                '(creeksfeast1 set)':
                    pass

    label creeksefeastaboutcopper01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I should take it directly to the guild, but... “You want to be sure that your worth is going to be seen and respected? I’ll give you something you can use to gain an edge. I know where you can find copper.”')
        $ foragingground_foraging_vein_sabotaged = 1
        $ creeks_reasonstojoin_feast_copper += 1
        $ creeks_reasonstojoin_points += 3
        $ creeks_reputation += 2
        $ elah_friendship += 2
        $ foggy_friendship += 2
        $ questionpreset = "creeksfeast1"
        menu:
            'A few shocked gasps encourage you to continue. You describe the ravine and the opportunities it presents, but before you can propose any plan on how to approach it, {color=#f6d6bd}Elah{/color} is on his feet, spreading his arms, sharing his own ideas on what to do next. After a few minutes of dispute, {color=#f6d6bd}Efren{/color} calls for everyone to focus.
            \n\n{color=#f6d6bd}The carpenter{/color} is eager to pat you on the back. “You clear a new path for the tribe, but there’s only a few of us, and we can’t know yet how much ore we’ll find in those rocks. But sharing this news with us before you take it to the officials,” he flashes his smile first toward you, then to the rest of the tribe, “is a great price to pay for our votes of trust.”
            '
            '(creeksfeast1 set)':
                pass

    label creeksefeastafterallreasons01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- “I have nothing more to add.”')
        if creeks_reasonstojoin_points >= 9:
            $ quest_creekssupport = 2
            $ quest_creekssupport_description01 = "I gained the support of the tribe."
            $ renpy.notify("Quest completed: The Support of Creeks")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Creeks{/i}')
            menu:
                '“Then it’s time for the discussion and the vote,” announces {color=#f6d6bd}Elah{/color}, gesturing for everyone to form a circle, and {color=#f6d6bd}Foggy{/color} agrees. “And fast. We wake up early, I want to reach the tavern soon after sunrise. Oh, and love,” she looks at you with a wolf-like grin, “better take care of that before it burns,” she points at a piece of roasting mouflon.
                \n\nFor the next few minutes, you listen to a lively discussion, but it turns out to be rather one-sided, and most of the doubts get buried by pointed replies and references to your previous deeds. Finally, the voting occurs, and it takes no scribe to spot many more hands raised for the “aye” side.
                '
                'I stand up.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I stand up.')
                    if pc_goal == "iwantstatus":
                        $ pc_goal_iwantstatuspoints += 2
                    if quest_pc_goal == 1 and pc_goal == "iwantstatus":
                        $ renpy.notify("Journal updated: %s" %quest_pc_goal_name)
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: %s{/i}' %quest_pc_goal_name)
                    menu:
                        'There’s no clapping or cheerful shouts. {color=#f6d6bd}Elah{/color} spreads his arms, lit by the glow of the bonfire. “We will meet with the cityfolk and negotiate the terms.” The shadow of his words spreads above the old, untamed paths of the tribe, and the grief follows.
                        \n\nNevertheless, a few of the locals approach you to share good words and to wish you a safe journey to the city. Some hope you’ll bring back a few gifts.
                        \n\nThe feast continues with heavy souls, but the tension leaves your shell. All you have left are heavy eyelids and some time to kill.
                        '
                        'I think my “gambling friends” are giving me inviting looks.' if creeks_youth_gambling >= 3:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think my “gambling friends” are giving me inviting looks.')
                            $ creeks_reputation += 1
                            $ sleep_destination = "creeksaftersleep2sex"
                            jump sleeping
                        'Time to eat and drink!':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to eat and drink!')
                            $ custom6 = "You reach a pile of furs with a full stomach and enough booze to make your head spin. You wake up after many hours, still tired, and unable to swallow even one bite of food. The first thing you do after relieving yourself is gulp down half a bucket of water.\n\nThe locals in the square wish you a good day, but many people are already preparing for work."
                            $ sleep_destination = "creeksaftersleep2food"
                            jump sleeping
                        'I find {color=#f6d6bd}Elah{/color} and chat with him about the future.' if elah_friendship >= 6:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I find {color=#f6d6bd}Elah{/color} and chat with him about the future.')
                            $ elah_friendship += 1
                            $ custom6 = "You wake up on a pile of furs after just a few hours, still thinking about the feast and your conversation with {color=#f6d6bd}the carpenter{/color}. He didn’t take much interest in your pursuits, but some of his aspirations are admirable, while many will most likely never happen, at least not in a single lifetime.\n\nIt had been quite a few days since you’d had the opportunity to participate in a conversation during which there was nothing to win or lose. The long walk you took between the buildings and fields allowed you to observe the stars at a later hour than usual.\n\nNow, there are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Some of them wish you a great day."
                            $ sleep_destination = "creeksaftersleep2chatting"
                            jump sleeping
                        'I find {color=#f6d6bd}Efren{/color} and chat with him about the past.' if efren_friendship >= 4:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I find {color=#f6d6bd}Efren{/color} and chat with him about the past.')
                            $ efren_friendship += 1
                            $ custom6 = "You wake up on a pile of furs after just a few hours, still thinking about the feast and your conversation with {color=#f6d6bd}the hunter{/color}. At first you got bored with the half-drunk man and considered seeking a sleeping spot, but then he revealed the guilt that still bites his soul. While you couldn’t heal him, he found comfort in having someone to talk to, and in the stories you shared with him as you observed the flowing creek below the village.\n\nNow, there are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Some of them wish you a great day."
                            $ sleep_destination = "creeksaftersleep2chatting"
                            jump sleeping
                        'I’ll relax for a bit with my “gambling friends.”' if creeks_youth_gambling == 2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll relax for a bit with my “gambling friends.”')
                            $ creeks_reputation += 2
                            $ custom6 = "You wake up on a pile of furs after just a few hours, still thinking about the feast and the time you spent with the group of young people. You told them about the many places and creatures that you’ve seen, the inns and their food in the South, what living in {color=#f6d6bd}Hovlavan{/color} is like... When there was nothing else to say, you noticed your aching throat. In return, you received tales of hunts and memories of petty squabbles that, after seasons, cause mostly laughter and embarrassment. The warm arms of your companions get you through the cold night with comfort.\n\nNow, there are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Many of them wish you a great day."
                            $ sleep_destination = "creeksaftersleep2chatting"
                            jump sleeping
                        'I seek a group of amicable locals and share a story or two with them.' if creeks_youth_gambling < 2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I seek a group of amicable locals and share a story or two with them.')
                            $ creeks_reputation += 1
                            $ custom6 = "You wake up on a pile of furs after just a few hours, forgetting the feast and your long storytime shared with the locals. You described the many places and creatures that you’ve seen, the inns and their food in the South, what living in {color=#f6d6bd}Hovlavan{/color} is like... When there was nothing else to say, you noticed your aching throat.\n\nNow, there are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Many of them wish you a great day."
                            $ sleep_destination = "creeksaftersleep2chatting"
                            jump sleeping
                        'Once people leave me to myself, I ask someone to show me a spot to sleep, then shut my eyes for the entire night.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Once people leave me to myself, I ask someone to show me a spot to sleep, then shut my eyes for the entire night.')
                            $ custom6 = "You reach a pile of furs and allow yourself to skip some of your chores, dozing off right away. In the morning, you feel ready for action.\n\nThere are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Some of them wish you a great day."
                            $ sleep_destination = "creeksaftersleep2resting"
                            jump sleeping
        elif creeks_reasonstojoin_points >= 5:
            $ quest_creekssupport = 3
            $ quest_creekssupport_description04 = "The tribe is not going to collaborate with the city anytime soon."
            $ renpy.notify("Quest completed: The Support of Creeks")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Creeks{/i}')
            menu:
                '“Then it’s time for the discussion and the vote,” announces {color=#f6d6bd}Elah{/color}, gesturing for everyone to form a circle, and {color=#f6d6bd}Foggy{/color} agrees. “And fast. We wake up early, I want to reach the tavern soon after sunrise. Oh, and love,” she looks at you with a wolf-like grin, “better take care of that before it burns,” she points at a piece of roasting mouflon.
                \n\nFor the next half an hour or so, you listen to a lively discussion, and the opinions are mixed. Many doubts are raised, some of which get buried by pointed replies and references to your previous deeds, but others stand strong. Finally, the voting occurs, and it takes a good few breaths to count the hands. Then you hear the result - the margin is small, but it’s a “no”.
                '
                'Shit. I stand up.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Shit. I stand up.')
                    menu:
                        'A few people clap, then most of them follow, adding a bunch of cheerful laughter and shouts. {color=#f6d6bd}Elah{/color} spreads his arms, though his eyes are unconvinced. “We will not participate in any negotiations for five more springs,” he announces, starting another wave of joy.
                        \n\nA few of the locals approach you to share a kind word and to wish you a safe journey to the city. You recognize that they are a part of the “aye” crowd, though their looks are far from sadness.
                        \n\nThe lively feast continues, and the tension leaves your shell. All you have left are heavy eyelids and some time to kill.
                        '
                        'I think my “gambling friends” are giving me inviting looks.' if creeks_youth_gambling >= 3:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think my “gambling friends” are giving me inviting looks.')
                            $ creeks_reputation += 1
                            $ sleep_destination = "creeksaftersleep2sex"
                            jump sleeping
                        'Time to eat and drink!':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to eat and drink!')
                            $ custom6 = "You reach a pile of furs with a full stomach and enough booze to make your head spin. You wake up after many hours, still tired, and unable to swallow even one bite of food. The first thing you do after relieving yourself is gulp down half a bucket of water.\n\nThe locals in the square wish you a good day, but many people are already preparing for work."
                            $ sleep_destination = "creeksaftersleep2food"
                            jump sleeping
                        'I find {color=#f6d6bd}Elah{/color} and chat with him about the future.' if elah_friendship >= 6:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I find {color=#f6d6bd}Elah{/color} and chat with him about the future.')
                            $ elah_friendship += 1
                            $ custom6 = "You wake up on a pile of furs after just a few hours, still thinking about the feast and your conversation with {color=#f6d6bd}the carpenter{/color}. He didn’t take much interest in your pursuits, but some of his aspirations are admirable, while many will most likely never happen, at least not in a single lifetime.\n\nIt had been quite a few days since you’d had an opportunity to participate in a conversation during which there was nothing to win or lose. The long walk you took between the buildings and fields allowed you to observe the stars at a later hour than usual.\n\nNow, there are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Some of them wish you a great day."
                            $ sleep_destination = "creeksaftersleep2chatting"
                            jump sleeping
                        'I find {color=#f6d6bd}Efren{/color} and chat with him about the past.' if efren_friendship >= 4:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I find {color=#f6d6bd}Efren{/color} and chat with him about the past.')
                            $ efren_friendship += 1
                            $ custom6 = "You wake up on a pile of furs after just a few hours, still thinking about the feast and your conversation with {color=#f6d6bd}the hunter{/color}. At first you got bored with the half-drunk man and considered seeking a sleeping spot, but then he revealed the guilt that still bites his soul. While you couldn’t heal him, he found comfort in having someone to talk to, and in the stories you shared with him as you observed the flowing creek below the village.\n\nNow, there are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Some of them wish you a great day."
                            $ sleep_destination = "creeksaftersleep2chatting"
                            jump sleeping
                        'I’ll relax for a bit with my “gambling friends.”' if creeks_youth_gambling == 2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll relax for a bit with my “gambling friends.”')
                            $ creeks_reputation += 2
                            $ custom6 = "You wake up on a pile of furs after just a few hours, still thinking about the feast and the time you spent with the group of young people. You told them about the many places and creatures that you’ve seen, the inns and their food in the South, what living in {color=#f6d6bd}Hovlavan{/color} is like... When there was nothing else to say, you noticed your aching throat. In return, you received tales of hunts and memories of petty squabbles that, after seasons, cause mostly laughter and embarrassment. The warm arms of your companions get you through the cold night with comfort.\n\nNow, there are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Many of them wish you a great day."
                            $ sleep_destination = "creeksaftersleep2chatting"
                            jump sleeping
                        'I seek a group of amicable locals and share a story or two with them.' if creeks_youth_gambling < 2:
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I seek a group of amicable locals and share a story or two with them.')
                            $ creeks_reputation += 1
                            $ custom6 = "You wake up on a pile of furs after just a few hours, forgetting the feast and your long storytime shared with the locals. You described the many places and creatures that you’ve seen, the inns and their food in the South, what living in {color=#f6d6bd}Hovlavan{/color} is like... When there was nothing else to say, you noticed your aching throat.\n\nNow, there are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Many of them wish you a great day."
                            $ sleep_destination = "creeksaftersleep2chatting"
                            jump sleeping
                        'Once people leave me to myself, I ask someone to show me a spot to sleep, then shut my eyes for the entire night.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Once people leave me to myself, I ask someone to show me a spot to sleep, then shut my eyes for the entire night.')
                            $ custom6 = "You reach a pile of furs and allow yourself to skip some of your chores, dozing off right away. In the morning, you feel ready for action.\n\nThere are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. Some of them wish you a great day."
                            $ sleep_destination = "creeksaftersleep2resting"
                            jump sleeping
        elif creeks_reasonstojoin_points >= 2:
            $ quest_creekssupport = 3
            $ quest_creekssupport_description04 = "The tribe is not going to collaborate with the city anytime soon."
            $ renpy.notify("Quest completed: The Support of Creeks")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Creeks{/i}')
            menu:
                '“Then it’s time for the discussion and the vote,” announces {color=#f6d6bd}Elah{/color}, gesturing for everyone to form a circle, and {color=#f6d6bd}Foggy{/color} agrees. “And fast. We wake up early, I want to reach the tavern soon after sunrise. Oh, and dear,” she looks at you gently, “better take a seat, it may take us some time.” You find a stool for yourself and listen to the conversation.
                \n\nFor the next half an hour or so, the discussion is rather cold. Many doubts are raised, some of which get buried by pointed replies and references to your previous deeds, but most of them stand strong. Finally, the voting occurs, and it takes but a few breaths to count the hands. It’s unquestionably a “no”.
                '
                'Shit. I stand up.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Shit. I stand up.')
                    menu:
                        'A few people clap, then most of them follow, adding a bunch of cheerful laughters and shouts. {color=#f6d6bd}Elah{/color} spreads his arms, and while he takes a deep breath, there’s relief on his face. “We will not participate in any negotiations for five more springs,” he announces, starting another wave of joy.
                        \n\nThe lively feast continues, and the tension leaves your shell. All you have left are heavy eyelids and some time to kill. The locals mostly ignore you.
                        '
                        'Embarrassing. I eat and drink as much as I can, then go to sleep.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Embarrassing. I eat and drink as much as I can, then go to sleep.')
                            $ custom6 = "You reach a pile of furs with a full stomach and enough booze to make your head spin. You wake up after many hours, still tired, and unable to swallow even one bite of food. The first thing you do after relieving yourself is gulp down half a bucket of water.\n\nThe people in the square don’t pay you any attention, and many of them are already preparing for work."
                            $ sleep_destination = "creeksaftersleep2food"
                            jump sleeping
                        'Uh. I ask someone to show me a spot to sleep, then shut my eyes for the entire night.':
                            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Uh. I ask someone to show me a spot to sleep, then shut my eyes for the entire night.')
                            $ custom6 = "You reach a pile of furs and allow yourself to skip some of your chores, dozing off right away. In the morning, you feel ready for action.\n\nThere are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. They don’t pay you any attention."
                            $ sleep_destination = "creeksaftersleep2resting"
                            jump sleeping
        else:
            $ quest_creekssupport = 3
            $ quest_creekssupport_description05 = "I don’t think the tribe will ever agree to collaborate with the city."
            $ renpy.notify("Quest completed: The Support of Creeks")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Quest completed: The Support of Creeks{/i}')
            menu:
                '“Then I don’t expect many of us to give an {i}aye{/i} to this matter,” {color=#f6d6bd}Elah{/color} looks around and, seeing many approving nods, he proposes skipping the discussion. “If the results are close, we’ll get back to it, then vote again.” As he’s gesturing for everyone to form a circle, {color=#f6d6bd}Foggy{/color} simply states she’s a “no”, and announces she’d like to get back to the tavern early in the morning.
                \n\nYou take a step back and indeed, only a few of the younger folks vote “aye.” The air is tense - people give you unpleasant looks, and as they spread, you hear someone stating it’s been {i}a big waste of time{/i}.
                \n\nThe feast continues. You’re stressed and tired, and everyone seems to avoid you.
                '
                'Embarrassing. I eat and drink as much as I can, then go to sleep.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Embarrassing. I eat and drink as much as I can, then go to sleep.')
                    $ custom6 = "You reach a pile of furs with a full stomach and enough booze to make your head spin. You wake up after many hours, still tired, and unable to swallow even one bite of food. The first thing you do after relieving yourself is gulp down half a bucket of water.\n\nThe people in the square don’t pay you any attention, and many of them are already preparing for work."
                    $ sleep_destination = "creeksaftersleep2food"
                    jump sleeping
                'Uh. I ask someone to show me a spot to sleep, then shut my eyes for the entire night.':
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Uh. I ask someone to show me a spot to sleep, then shut my eyes for the entire night.')
                    $ custom6 = "You reach a pile of furs and allow yourself to skip some of your chores, dozing off right away. In the morning, you feel ready for action.\n\nThere are loud conversations coming from the main square, where people are sitting with plates of cold meat and bowls of gruel, chatting about the plans for the day. They don’t pay you any attention."
                    $ sleep_destination = "creeksaftersleep2resting"
                    jump sleeping
