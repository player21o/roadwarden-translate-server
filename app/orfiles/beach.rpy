###################### BEACH
default beach_firsttime = 0
default beach_fluff = ""
default beach_fluff_old = ""
default beach_fishers_fluff = ""

default beach_fishers_introduction = 0
default beach_shed_explored = 0
default beach_shed_triestoopen = 0
default beach_driftwoodtaken = 0
default beach_boatprepared = 0

label beach01:
    if highisland_mode and not asterion_found:
        jump highisland_journey_beach00
    nvl clear
    $ pc_area = "beach"
    stop music fadeout 4.0
    play nature "audio/ambient/beach01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture galerockstobeach at basicfade
    label beach_fluffloop:
        $ beach_fluff = ""
        $ beach_fluff = renpy.random.choice(['The seagulls are as loud as the waves.', 'The relentless waves keep sharpening the teeth-like rocks.', 'The grass and the sand remain in their fight over the coast.', 'There are fresh pieces of driftwood and the remains of little animals sinking into the sand.', 'The refreshing smell tempts into taking a few, deep breaths.'])
        if beach_fluff_old == beach_fluff:
            jump beach_fluffloop
        else:
            $ beach_fluff_old = beach_fluff
    if quarters < 35:
        $ beach_fishers_fluff = "There are no boats, nets, or fishers in sight."
        $ beachfishersarearound = 0
    elif quarters <= 38:
        $ beach_fishers_fluff = "The fishers have just arrived. They unload the barge at the river and prepare their tools and boats."
        $ beachfishersarearound = 2
    elif quarters < 52:
        $ beach_fishers_fluff = "The fishers are in the middle of their work. Most of them are either away from the coast, casting the nets from the boats, or just walk around with heavy clothes, but revealed legs, using their fancily shaped spears to catch either a fish, or a bird sitting at one of the rocks. There’s also a few people on the land, resting, eating, and keeping an eye on the equipment."
        $ beachfishersarearound = 1
    elif quarters >= 52 and quarters < 56:
        $ beach_fishers_fluff = "The fishers are currently having a break, eating their largest meal and refilling their waterskins from the barrels. The relieved conversations are focused on the plans for the evening."
        $ beachfishersarearound = 2
    elif quarters >= 56 and quarters < world_daylength-16:
        $ beach_fishers_fluff = "The fishers are in the middle of their work. Most of them are either away from the coast, casting the nets from the boats, or just walk around with heavy clothes, but revealed legs, using their fancily shaped spears to catch either a fish, or a bird sitting at one of the rocks. There’s also a few people on the land, resting, eating, and keeping an eye on the equipment."
        $ beachfishersarearound = 1
    elif quarters < world_daylength-12:
        $ beach_fishers_fluff = "The fishers are preparing themselves to leave, tired, but at least not sweaty."
        $ beachfishersarearound = 2
    else:
        $ beach_fishers_fluff = "There are no boats, nets, or fishers in sight."
        $ beachfishersarearound = 0
    if quarters >= world_daylength-12 and quarters <= world_daylength-10:
        jump beforebeach01
    elif not beach_firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ world_known_areas += 1
        $ beach_firsttime = 1
        $ galerocks_unlocked = 1
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        jump beachfirsttime01
    else:
        with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
        if not beach_fishers_introduction and beachfishersarearound:
            $ beach_fishers_introduction = 1
            if quarters < 64:
                $ beach_fishers_fluff = "The human activity you witness is intense. A large barge is resting on the river, immobilized by the ropes and wooden posts, and you see a few people foraging at the beach and in the grasses. Even more people, most of them without wrinkles, are gathered at the pier, where they prepare their boats and nets, and talk about their plans for the following hours."
            else:
                $ beach_fishers_fluff = "The human activity you witness is intense. A large barge is resting on the river, immobilized by the ropes and wooden posts, and you see a few people foraging at the beach and in the grasses. Even more people, most of them without wrinkles, are gathered at the pier, where they clean and fix their boats and nets, and talk about their plans for the evening."
        else:
            $ beach_fishers_fluff = "There are no boats, nets, or fishers in sight, but there are countless boot prints and footprints in sight, both on the road and next to it."
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        jump beachregular01

label beachfirsttime01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if not pc_sea_fluff:
        $ pc_sea_fluff = 1
        menu:
            'The roars of the sea reach you first, then the cold wind and the light - there are hardly any shrubs nearby, and as you ride downhill, toward the white-and-gold beach, the sunbeams hit you with full force.
            \n\nThe sea here is not like the one from {color=#f6d6bd}Hovlavan’s{/color} port. The harbor and waters most people see during their busy days are full of life - ships, warehouses, traders, dockers. And of course, there’s Sickle, the barrier island that provides the city with its lagoon, but also serves as a home to dozens of species of birds, monkeys, and rodents. For most people, the sea is never silent.
            \n\nBut if one travels to Sickle and looks west, or embarks on a boat and sails away, there’s yet another view, a very different one. The never-ending blue, the emptiness, the humming waves, the monsters swimming to the surface just to take a breath, not even interested in the wooden vessels. Many say that if one jumps off a ship with a heavy stone, they will drown before they touch the seabed.
            \n\nHere, however, the water can’t be separated from the rocks that cut through it, like a swarm of mushrooms in a dark forest. Their shapes and sizes vary, but it’s their number that makes them unusual. If you were to name each one, you’d have to make up at least half of the names.
            \n\nThere’s no doubt where the name of {color=#f6d6bd}Gale Rocks{/color} comes from. The stones piercing through the surface of the water are shaped like beast fangs, as if they’re asking the ships to dare and test their strength.
            '
            'Where it’s possible, I keep to the greener parts of the beach. Sand is awful for hooves.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Where it’s possible, I keep to the greener parts of the beach. Sand is awful for hooves.')
                jump beachfirsttime02
    else:
        menu:
            'The roars of the sea reach you first, then the cold wind and the light - there are hardly any shrubs nearby, and as you ride downhill, toward the white-and-gold beach, the sunbeams hit you with full force. There’s no doubt where the name of {color=#f6d6bd}Gale Rocks{/color} comes from. The stones piercing through the surface of the water are shaped like beast fangs, as if they’re asking the ships to dare and test their strength.
            '
            'Where it’s possible, I keep to the greener parts of the beach. Sand is awful for hooves.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Where it’s possible, I keep to the greener parts of the beach. Sand is awful for hooves.')
                jump beachfirsttime02

    label beachfirsttime02:
        if not beach_boatprepared:
            show areapicture beach01 at basicfade
        else:
            show areapicture beach02 at basicfade
        if beachfishersarearound:
            $ beach_fishers_introduction = 1
            if quarters < 64:
                $ beach_fishers_fluff = "The human activity you witness is intense. A large barge is resting on the river, immobilized by the ropes and wooden posts, and you see a few people foraging at the beach and in the grasses. Even more people, most of them without wrinkles, are gathered at the pier, where they prepare their boats and nets, and talk about their plans for the following hours."
            else:
                $ beach_fishers_fluff = "The human activity you witness is intense. A large barge is resting on the river, immobilized by the ropes and wooden posts, and you see a few people foraging at the beach and in the grasses. Even more people, most of them without wrinkles, are gathered at the pier, where they clean and fix their boats and nets, and talk about their plans for the evening."
        else:
            $ beach_fishers_fluff = "There are no boats, nets, or fishers in sight, but there are countless boot prints and footprints in sight, both on the road and next to it."
        menu:
            'You follow the sharp turn to the right. The road remains broad enough for carts and wagons, and avoids the sands, letting {color=#f6d6bd}[horsename]{/color} trot without disturbances. The grasses to the east and south are short, and hardly any shrubs have managed to oppose the harsh winds.
            \n\n[beach_fishers_fluff]
            \n\nYou reach the end of the beaten path, getting to the stone-made pier, just next to a small, dolmen-shaped shed. Only the door seems to be fairly new, and you don’t doubt that both of the structures have been repaired many times in the past, crumbling under the touch of the waves.
            '
            'I look for my boat.' if galerocks_navica_boat_bought and not beach_boatprepared and quest_asterion == 1:
                jump beachboat01
            'I head to the fishers.' if beachfishersarearound:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the fishers.')
                if galerocks_photios_firsttime:
                    jump galerocksphotios01
                else:
                    jump galerocksphotios01firsttime
            'I leave the pier.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
                jump beachafterinteraction01

label beachregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if pc_class == "scholar" and not beach_driftwoodtaken and not item_driftwood and not fishinghamlet_driftwood:
        $ at_unlock_knowledge = 1
        $ at = 0
    menu:
        '[beach_fluff] [beach_fishers_fluff]
        '
        'I approach the pier.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the pier.')
            $ at = 0
            jump beachenteringthepier01
        'I spend some time looking through the pieces of driftwood. They could be useful at an alchemy table.' ( condition="at == 'knowledge'" ):
            $ at = 0
            jump beachcollectingdriftwood01
        'I wash myself in the ocean.' if cleanliness <= 0:
            $ at = 0
            jump beachtakingabath01
        'I won’t get any cleaner in the ocean. (disabled)' if cleanliness > 0:
            pass

    label beachafterinteraction01:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        $ at = 0
        show areapicture galerockstobeach at basicfade
        if pc_class == "scholar" and not beach_driftwoodtaken and not item_driftwood and not fishinghamlet_driftwood:
            $ at_unlock_knowledge = 1
            $ at = 0
        menu:
            'You lead {color=#f6d6bd}[horsename]{/color} back to the road.
            '
            'I approach the pier.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the pier.')
                $ at = 0
                jump beachenteringthepier01
            'I spend some time looking through the pieces of driftwood. They could be useful at an alchemy table.' ( condition="at == 'knowledge'" ):
                $ at = 0
                jump beachcollectingdriftwood01
            'I wash myself in the ocean.' if cleanliness <= 0:
                $ at = 0
                jump beachtakingabath01
            'I won’t get any cleaner in the ocean. (disabled)' if cleanliness > 0:
                pass

    label beachtakingabath01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash myself in the ocean.')
        $ at_unlock_knowledge = 0
        $ minutes += 10
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        show plus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        $ cleanliness = limit_cleanliness(1)
        menu:
            'The water is freezing and after you’re done, sand makes you wait for a while before you dry up enough to put your clothes back on. The unpleasant touch of salt covering your skin will travel with you.
            '
            'I pack my things.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
                jump beachafterinteraction01

    label beachcollectingdriftwood01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I spend some time looking through the pieces of driftwood. They could be useful at an alchemy table.')
        $ at_unlock_knowledge = 0
        $ at = 0
        $ quarters += 1
        $ beach_driftwoodtaken = 1
        $ item_driftwood += 1
        $ renpy.notify("You added the driftwood to your bag of ingredients.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You added the driftwood to your bag of ingredients.{/i}')
        if pc_class == "scholar" and not beach_driftwoodtaken and not item_driftwood and not fishinghamlet_driftwood:
            $ at_unlock_knowledge = 1
            $ at = 0
        menu:
            'You stay close to your mount, observing the disorder of rocks, dead plants, and animal remains that are coating the sand. The pieces of wood, with their forgotten stories of foreign lands and sunk ships, are gathered in short stacks. You approach the largest pile, and push all the sticks, boughs, and branches aside, sparking displeased shouts of worms, crabs, and other beings that used to live among them.
            \n\nYou find the piece you were looking for, which is unlike the others. Not too thick, nor too long, and with a few little chunks of wood coming out of only one end, like a bunch of fingers. You nod with approval, reciting in your head a part of the withering dust recipe: {i}fuel with an ocean wood in the shape of a flower{/i}.
            '
            'I approach the pier.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the pier.')
                $ at = 0
                jump beachenteringthepier01
            'I spend some time looking through the pieces of driftwood. They could be useful at an alchemy table.' ( condition="at == 'knowledge'" ):
                $ at = 0
                jump beachcollectingdriftwood01
            'I wash myself in the ocean.' if cleanliness <= 0:
                $ at = 0
                jump beachtakingabath01
            'I won’t get any cleaner in the ocean. (disabled)' if cleanliness > 0:
                pass

label beachenteringthepier01:
    $ at_unlock_knowledge = 0
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ at = 0
    if not beach_boatprepared:
        show areapicture beach01 at basicfade
    else:
        show areapicture beach02 at basicfade
    if quarters < 36:
        $ beach_fishers_fluff = "There are no boats, nets, or fishers in sight."
        $ beachfishersarearound = 0
    elif quarters <= 38:
        $ beach_fishers_fluff = "The fishers have just arrived. They unload the barge at the river and prepare their tools and boats."
        $ beachfishersarearound = 2
    elif quarters < 52:
        $ beach_fishers_fluff = "The fishers are in the middle of their work. Most of them are either away from the coast, casting the nets from the boats, or just walk around with heavy clothes, but revealed legs, using their fancily shaped spears to catch either a fish, or a bird sitting at one of the rocks. There’s also a few people on the land, resting, eating, and keeping an eye on the equipment."
        $ beachfishersarearound = 1
    elif quarters >= 52 and quarters < 56:
        $ beach_fishers_fluff = "The fishers are currently having a break, eating their largest meal and refilling their waterskins from the barrels. The relieved conversations are focused on the plans for the evening."
        $ beachfishersarearound = 2
    elif quarters >= 56 and quarters < world_daylength-16:
        $ beach_fishers_fluff = "The fishers are in the middle of their work. Most of them are either away from the coast, casting the nets from the boats, or just walk around with heavy clothes, but revealed legs, using their fancily shaped spears to catch either a fish, or a bird sitting at one of the rocks. There’s also a few people on the land, resting, eating, and keeping an eye on the equipment."
        $ beachfishersarearound = 1
    elif quarters < world_daylength-12:
        $ beach_fishers_fluff = "The fishers are preparing themselves to leave, tired, but at least not sweaty."
        $ beachfishersarearound = 2
    else:
        $ beach_fishers_fluff = "There are no boats, nets, or fishers in sight."
        $ beachfishersarearound = 0
    if not beach_fishers_introduction and beachfishersarearound:
        $ beach_fishers_introduction = 1
        if quarters < 64:
            $ beach_fishers_fluff = "The human activity you witness is intense. A large barge is resting on the river, immobilized by the ropes and wooden posts, and you see a few people foraging at the beach and in the grasses. Even more people, most of them without wrinkles, are gathered at the pier, where they prepare their boats and nets, and talk about their plans for the following hours."
        else:
            $ beach_fishers_fluff = "The human activity you witness is intense. A large barge is resting on the river, immobilized by the ropes and wooden posts, and you see a few people foraging at the beach and in the grasses. Even more people, most of them without wrinkles, are gathered at the pier, where they clean and fix their boats and nets, and talk about their plans for the evening."
    menu:
        'You’re next to the shed. [beach_fishers_fluff]
        '
        'I look for my boat.' if galerocks_navica_boat_bought and not beach_boatprepared and quest_asterion == 1:
            jump beachboat01
        'I head to the fishers.' if beachfishersarearound:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the fishers.')
            if galerocks_photios_firsttime:
                jump galerocksphotios01
            else:
                jump galerocksphotios01firsttime
        'I leave the pier.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
            jump beachafterinteraction01

# label beachtriestoexploretheshed01:
            # 'I approach the shed.' if not beach_shed_triestoopen and not beach_shed_explored:
            #     jump beachtriestoexploretheshed01
            # 'Since there’s no one around, I approach the shed.' if not beachfishersarearound and not beach_shed_explored and beach_shed_triestoopen:
            #     jump beachexploringtheshed01
            # 'The fishers won’t allow me to get to look into the shed. (disabled)' if beachfishersarearound and not beach_shed_explored and beach_shed_triestoopen:
            #     pass
#     $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the shed.')
#     $ beach_shed_triestoopen = 1
#     if beachfishersarearound:
#         menu:
#             'You’re quickly stopped by a few fishers. “What do you need from there?” You explain that you just need to look around, and they scowl at you, in silence opening the door, though not to the full extent.
#             \n\n“Just barrels, nets, firewood, paddles,” says one of them. Indeed, as far as you can tell, the shed is filled with all sorts of fishing tools, as well as cupboards allowing to store them in some sort of order. The floor, made of stone, is significantly covered with sand. “We close it with a key, so don’t even think of stealing from us, outsider.”
#             '
#             'I look for my boat.' if galerocks_navica_boat_bought and not beach_boatprepared and quest_asterion == 1:
#                 jump beachboat01
#             'I head to the fishers.' if beachfishersarearound:
#                 $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the fishers.')
#                 if galerocks_photios_firsttime:
#                     jump galerocksphotios01
#                 else:
#                     jump galerocksphotios01firsttime
#             'I approach the shed.' if not beach_shed_triestoopen and not beach_shed_explored:
#                 jump beachtriestoexploretheshed01
#             'Since there’s no one around, I approach the shed.' if not beachfishersarearound and not beach_shed_explored and beach_shed_triestoopen:
#                 jump beachexploringtheshed01
#             'The fishers won’t allow me to get to look into the shed. (disabled)' if beachfishersarearound and not beach_shed_explored and beach_shed_triestoopen:
#                 pass
#             'I leave the pier.':
#                 $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
#                 jump beachafterinteraction01
#     else:
#         menu:
#             '
#             \n\n
#             '
#             'I look for my boat.' if galerocks_navica_boat_bought and not beach_boatprepared and quest_asterion == 1:
#                 jump beachboat01
#             'I head to the fishers.' if beachfishersarearound:
#                 $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the fishers.')
#                 if galerocks_photios_firsttime:
#                     jump galerocksphotios01
#                 else:
#                     jump galerocksphotios01firsttime
#             'I approach the shed.' if not beach_shed_triestoopen and not beach_shed_explored:
#                 jump beachtriestoexploretheshed01
#             'Since there’s no one around, I approach the shed.' if not beachfishersarearound and not beach_shed_explored and beach_shed_triestoopen:
#                 jump beachexploringtheshed01
#             'The fishers won’t allow me to get to look into the shed. (disabled)' if beachfishersarearound and not beach_shed_explored and beach_shed_triestoopen:
#                 pass
#             'I leave the pier.':
#                 $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
#                 jump beachafterinteraction01

    # label beachexploringtheshed01:
    #     $ narrator.add_history(kind='nvl', who=narrator.name, what='- Since there’s no one around, I approach the shed.')
    #     $ beach_shed_explored = 1
    #     $ quarters += 1
    #     $ quest_gatheracrew_description00boatgalerockssteal = 1
    #     $ renpy.notify("Journal updated: Gather a Crew")
    #     $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal updated: Gather a Crew{/i}')
    #     menu:
    #         '
    #         \n\n
    #         '
    #         'I look for my boat.' if galerocks_navica_boat_bought and not beach_boatprepared and quest_asterion == 1:
    #             jump beachboat01
    #         'I head to the fishers.' if beachfishersarearound:
    #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the fishers.')
    #             if galerocks_photios_firsttime:
    #                 jump galerocksphotios01
    #             else:
    #                 jump galerocksphotios01firsttime
    #         'I approach the shed.' if not beach_shed_triestoopen and not beach_shed_explored:
    #             jump beachtriestoexploretheshed01
    #         'Since there’s no one around, I approach the shed.' if not beachfishersarearound and not beach_shed_explored and beach_shed_triestoopen:
    #             jump beachexploringtheshed01
    #         'The fishers won’t allow me to get to look into the shed. (disabled)' if beachfishersarearound and not beach_shed_explored and beach_shed_triestoopen:
    #             pass
    #         'I leave the pier.':
    #             $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
    #             jump beachafterinteraction01

label beachboat01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for my boat.')
    $ beach_boatprepared = 1
    show areapicture beach02 at basicfade
    if beachfishersarearound and (galerocks_reputation+galerocks_photios_friendship) >= 10:
        $ quarters += 1
        $ custom1 = "The fishers are eager to help you carry it closer to the pier, and assure you it won’t leak."
    elif beachfishersarearound and (galerocks_reputation+galerocks_photios_friendship) >= 6:
        $ quarters += 2
        $ custom1 = "After you struggle for a bit with trying to carry the boat by yourself, the fishers offer to help you, and assure you it won’t leak."
    else:
        $ quarters += 4
        $ custom1 = "Without anyone to help you, it’s a long and tiresome task that leaves you hungry and sweaty, especially since you also have to place in water and sit down to test. Thankfully, no leaks."
        $ pc_food = limit_pc_food(pc_food-1)
        show minus1food at foodchange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 nourishment point.{/i}')
        $ cleanliness = limit_cleanliness(cleanliness-1)
        show minus1appearance at appearancechange onlayer myoverlay
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 appearance point.{/i}')
    menu:
        'You find it close to a hill’s rockface, safe from the tides, turned upside down to protect it from rains. It’s simple and old, without any paint, but you find no holes. It has three pairs of paddles, and benches for a few more people to sit down. [custom1]
        '
        'I look for my boat.' if galerocks_navica_boat_bought and not beach_boatprepared and quest_asterion == 1:
            jump beachboat01
        'I head to the fishers.' if beachfishersarearound:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I head to the fishers.')
            if galerocks_photios_firsttime:
                jump galerocksphotios01
            else:
                jump galerocksphotios01firsttime
        'I leave the pier.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I pack my things.')
            jump beachafterinteraction01
