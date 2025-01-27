################## FALLEN TREE
default fallentree_firsttime = 0
default fallentree_fluff = ""
default fallentree_fluff_old = ""
default fallentree_cleared = 0
default fallentree_traveldescription = 0
default fallentree_lumberjacks = 0
default fallentree_truth = 0

default fallentree_examined = 0
default fallentree_investigated = 0
default fallentree_investigated_area = 0
default fallentree_investigated_tree = 0
default fallentree_investigated_stump = 0
default fallentree_investigated_tracks = 0
default fallentree_investigated_wagon = 0
default fallentree_investigated_river = 0
default fallentree_investigated_bushes = 0
default fallentree_investigated_hill = 0
default fallentree_investigated_road = 0
default fallentree_investigated_opinion01 = ""
default fallentree_investigated_opinion02 = ""
default fallentree_investigated_opinion03 = ""
default fallentree_investigated_opinion04 = ""

default fallentree_fishtrap = 0
default fallentree_fishtrap_working = 0
default fallentree_fishtrap_daychecked = 0
default fallentree_fishtrap_fishtimer = 0
default fallentree_fishtrap_badthingmodifier = 0

label fallentree01:
    nvl clear
    $ pc_area = "fallentree"
    if not fallentree_cleared:
        label fallentree_fluffloop:
            $ fallentree_fluff = ""
            $ fallentree_fluff = renpy.random.choice(['The water is peaceful, but gathers plenty of busy insects. Some of the croaking frogs jump away from your palfrey’s hooves and hide under the surface of the river.', 'The blue sky is filled with the rustling of trees and the songs of birds. When you approach the blockade, a red, furry critter gets startled and runs away.','The rocks have been cleaned by centuries of rain and wind. You get startled by the sight of animal scales, then realize it’s just a basking grass-snake. Soon, it vanishes among the rocks.'])
            if fallentree_fluff_old == fallentree_fluff:
                jump fallentree_fluffloop
            else:
                $ fallentree_fluff_old = fallentree_fluff
    else:
        label fallentree_fluffloop2:
            $ fallentree_fluff = ""
            $ fallentree_fluff = renpy.random.choice(['The water is peaceful, but gathers plenty of busy insects. Some of the croaking frogs jump away from your palfrey’s hooves and hide under the surface of the river.', 'The blue sky is filled with the rustling of trees and the songs of birds. A red, furry critter gets startled by your arrival and runs away.','The rocks have been cleaned by centuries of rain and wind. You get startled by the sight of animal scales, then realize it’s just a basking grass-snake. Soon, it vanishes among the rocks.'])
            if fallentree_fluff_old == fallentree_fluff:
                jump fallentree_fluffloop2
            else:
                $ fallentree_fluff_old = fallentree_fluff
    stop music fadeout 4.0
    play nature "audio/ambient/fallentree01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    if not fallentree_cleared:
        show areapicture fallentree01 behind fishtrap at basicfade
    else:
        show areapicture fallentree02 behind fishtrap at basicfade
    if fallentree_fishtrap:
        show fishtrap fallentree01 at basicfade
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if not fallentree_firsttime:
        $ dolmen_unlocked = 1
        $ watchtower_unlocked = 1
        $ fallentree_firsttime = 1
        jump fallentree01firsttime01
    elif elah_quest_easternpath_lumberjacks == 1:
        jump creekselahaboutquesteasternroadfallentree08
    elif fallentree_cleared:
        jump fallentree02regular01
    else:
        jump fallentree01regular01

label fallentree01firsttime01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ quest_fallentree = 1
    if quest_easternpath == 1 and quest_easternpath_description01:
        $ renpy.notify("New entry: Fallen Tree,\nJournal updated: The Eastern Path")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Fallen Tree, Journal updated: The Eastern Path{/i}')
    else:
        $ renpy.notify("New entry: Fallen Tree")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}New entry: Fallen Tree{/i}')
    $ quest_easternpath_description09 = "I encountered a fallen tree in the south of the peninsula."
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        'A roundpine tree blocks the road. For a wayfarer, walking over the thin branches at the top is not much of an issue. Even {color=#f6d6bd}[horsename]{/color}, led on a rope, could walk around the stump, but a large wagon couldn’t move onward in one piece, at least not without detaching the mules, unpacking all the wares, and moving everything by hand.
        \n\nCutting a tree into pieces would take hours, even with proper tools, and you can’t hope to move it with just the muscles that you and your mount have to offer.
        '
        'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
            jump fallentree01investigation00
        'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
            jump fallentree01investigateconclusion01
        'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
            $ fallentree_investigated = 0
            $ quest_fallentree_description01 = 0
            $ renpy.notify("Journal Updated: Fallen Tree")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
            jump fallentree01investigation00
        'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
            pass
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
            jump fallentreefishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
            jump fallentreefishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
            jump fallentreefishtrap03
        'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
            jump fallentreefishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
            pass
        'I consider washing myself in the river.':
            jump fallentreebath01

label fallentree01regular01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '[fallentree_fluff]
        '
        'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
            jump fallentree01investigation00
        'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
            jump fallentree01investigateconclusion01
        'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
            $ fallentree_investigated = 0
            $ quest_fallentree_description01 = 0
            $ renpy.notify("Journal Updated: Fallen Tree")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
            jump fallentree01investigation00
        'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
            pass
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
            jump fallentreefishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
            jump fallentreefishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
            jump fallentreefishtrap03
        'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
            jump fallentreefishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
            pass
        'I consider washing myself in the river.':
            jump fallentreebath01

label fallentree01investigation00:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ fallentree_examined = 1
    menu:
        'What do you investigate?
        '
        'The surrounding area.' if not fallentree_investigated_area:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The surrounding area.')
            jump fallentree_investigated_area
        'The tree.' if not fallentree_investigated_tree:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tree.')
            jump fallentree_investigated_tree
        'The stump.' if not fallentree_investigated_stump:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stump.')
            jump fallentree_investigated_stump
        'The tracks.' if not fallentree_investigated_tracks:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tracks.')
            jump fallentree_investigated_tracks
        'The wagon.' if not fallentree_investigated_wagon:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The wagon.')
            jump fallentree_investigated_wagon
        'The river.' if not fallentree_investigated_river:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The river.')
            jump fallentree_investigated_river
        'The bushes.' if not fallentree_investigated_bushes:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bushes.')
            jump fallentree_investigated_bushes
        'The western hill.' if not fallentree_investigated_hill:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western hill.')
            jump fallentree_investigated_hill
        'The road.' if not fallentree_investigated_road:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- The road.')
            jump fallentree_investigated_road
        'I think I know what happened here.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
            jump fallentree01investigateconclusion01
        'I take another look at the surrounding area.' if fallentree_investigated_area:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the surrounding area.')
            jump fallentree_investigated_area
        'I go back to the tree.' if fallentree_investigated_tree:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the tree.')
            jump fallentree_investigated_tree
        'I go back to the stump.' if fallentree_investigated_stump:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the stump.')
            jump fallentree_investigated_stump
        'I take another look at the tracks.' if fallentree_investigated_tracks:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the tracks.')
            jump fallentree_investigated_tracks
        'I return to the wagon.' if fallentree_investigated_wagon:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the wagon.')
            jump fallentree_investigated_wagon
        'I approach the river again.' if fallentree_investigated_river:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the river again.')
            jump fallentree_investigated_river
        'I go back to the bushes.' if fallentree_investigated_bushes:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the bushes.')
            jump fallentree_investigated_bushes
        'I climb on the western hill again.' if fallentree_investigated_hill:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb on the western hill again.')
            jump fallentree_investigated_hill
        'I take another look at the road.' if fallentree_investigated_road:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the road.')
            jump fallentree_investigated_road

label fallentree01investigateALL:
    label fallentree_investigated_area:
        if not fallentree_investigated_area:
            $ fallentree_investigated_area = 1
            $ minutes += 10
        menu:
            'You walk deeper into the wilderness, searching through the shrubs and trees. You don’t find any sidepaths, nor remains of a camp or a hamlet. The first game trail you find has been used exclusively by animals.
            '
            'The surrounding area.' if not fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The surrounding area.')
                jump fallentree_investigated_area
            'The tree.' if not fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tree.')
                jump fallentree_investigated_tree
            'The stump.' if not fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stump.')
                jump fallentree_investigated_stump
            'The tracks.' if not fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tracks.')
                jump fallentree_investigated_tracks
            'The wagon.' if not fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The wagon.')
                jump fallentree_investigated_wagon
            'The river.' if not fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The river.')
                jump fallentree_investigated_river
            'The bushes.' if not fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bushes.')
                jump fallentree_investigated_bushes
            'The western hill.' if not fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western hill.')
                jump fallentree_investigated_hill
            'The road.' if not fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The road.')
                jump fallentree_investigated_road
            'I think I know what happened here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I take another look at the surrounding area.' if fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the surrounding area.')
                jump fallentree_investigated_area
            'I go back to the tree.' if fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the tree.')
                jump fallentree_investigated_tree
            'I go back to the stump.' if fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the stump.')
                jump fallentree_investigated_stump
            'I take another look at the tracks.' if fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the tracks.')
                jump fallentree_investigated_tracks
            'I return to the wagon.' if fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the wagon.')
                jump fallentree_investigated_wagon
            'I approach the river again.' if fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the river again.')
                jump fallentree_investigated_river
            'I go back to the bushes.' if fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the bushes.')
                jump fallentree_investigated_bushes
            'I climb on the western hill again.' if fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb on the western hill again.')
                jump fallentree_investigated_hill
            'I take another look at the road.' if fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the road.')
                jump fallentree_investigated_road

    label fallentree_investigated_tree:
        if not fallentree_investigated_tree:
            $ fallentree_investigated_tree = 1
            $ minutes += 2
        menu:
            'The leaves are not completely dry, and when you break one of the twigs, it still contains water. There are no signs of sickness that you can recognize, and the termites and other bugs are still sparse. Beneath the trunk, there’s no blood, no abandoned limbs.
            '
            'The surrounding area.' if not fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The surrounding area.')
                jump fallentree_investigated_area
            'The tree.' if not fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tree.')
                jump fallentree_investigated_tree
            'The stump.' if not fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stump.')
                jump fallentree_investigated_stump
            'The tracks.' if not fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tracks.')
                jump fallentree_investigated_tracks
            'The wagon.' if not fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The wagon.')
                jump fallentree_investigated_wagon
            'The river.' if not fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The river.')
                jump fallentree_investigated_river
            'The bushes.' if not fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bushes.')
                jump fallentree_investigated_bushes
            'The western hill.' if not fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western hill.')
                jump fallentree_investigated_hill
            'The road.' if not fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The road.')
                jump fallentree_investigated_road
            'I think I know what happened here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I take another look at the surrounding area.' if fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the surrounding area.')
                jump fallentree_investigated_area
            'I go back to the tree.' if fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the tree.')
                jump fallentree_investigated_tree
            'I go back to the stump.' if fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the stump.')
                jump fallentree_investigated_stump
            'I take another look at the tracks.' if fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the tracks.')
                jump fallentree_investigated_tracks
            'I return to the wagon.' if fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the wagon.')
                jump fallentree_investigated_wagon
            'I approach the river again.' if fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the river again.')
                jump fallentree_investigated_river
            'I go back to the bushes.' if fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the bushes.')
                jump fallentree_investigated_bushes
            'I climb on the western hill again.' if fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb on the western hill again.')
                jump fallentree_investigated_hill
            'I take another look at the road.' if fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the road.')
                jump fallentree_investigated_road

    label fallentree_investigated_stump:
        if not fallentree_investigated_stump:
            $ fallentree_investigated_stump = 1
            $ minutes += 1
        menu:
            'You don’t find any marks of a maw or paws. The top is hip-high and unnaturally smooth. You could comfortably sit down on it.
            '
            'The surrounding area.' if not fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The surrounding area.')
                jump fallentree_investigated_area
            'The tree.' if not fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tree.')
                jump fallentree_investigated_tree
            'The stump.' if not fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stump.')
                jump fallentree_investigated_stump
            'The tracks.' if not fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tracks.')
                jump fallentree_investigated_tracks
            'The wagon.' if not fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The wagon.')
                jump fallentree_investigated_wagon
            'The river.' if not fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The river.')
                jump fallentree_investigated_river
            'The bushes.' if not fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bushes.')
                jump fallentree_investigated_bushes
            'The western hill.' if not fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western hill.')
                jump fallentree_investigated_hill
            'The road.' if not fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The road.')
                jump fallentree_investigated_road
            'I think I know what happened here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I take another look at the surrounding area.' if fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the surrounding area.')
                jump fallentree_investigated_area
            'I go back to the tree.' if fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the tree.')
                jump fallentree_investigated_tree
            'I go back to the stump.' if fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the stump.')
                jump fallentree_investigated_stump
            'I take another look at the tracks.' if fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the tracks.')
                jump fallentree_investigated_tracks
            'I return to the wagon.' if fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the wagon.')
                jump fallentree_investigated_wagon
            'I approach the river again.' if fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the river again.')
                jump fallentree_investigated_river
            'I go back to the bushes.' if fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the bushes.')
                jump fallentree_investigated_bushes
            'I climb on the western hill again.' if fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb on the western hill again.')
                jump fallentree_investigated_hill
            'I take another look at the road.' if fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the road.')
                jump fallentree_investigated_road

    label fallentree_investigated_tracks:
        if not fallentree_investigated_tracks:
            $ fallentree_investigated_tracks = 1
            $ minutes += 5
        menu:
            'In the trampled grass, you find two sets of tracks to follow. There are no hoofprints.
            \n\nThe first set is near the destroyed wagon. The wayfarers suddenly stopped - you can see where they made a sharp turn.
            \n\nThe second trail is close to the tree stump. Most of the marks were left by flat, cheap boots, not suitable for long walks, but someone was wearing hard, wide heels, distorting the ground.
            \n\nBoth trails avoid the eastern wilderness. They stick to the main road, and lead you north. They could have belonged to two dozen people, maybe more. You follow them for a bit, but lose them once there’s no more mud and tree needles to find.
            '
            'The surrounding area.' if not fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The surrounding area.')
                jump fallentree_investigated_area
            'The tree.' if not fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tree.')
                jump fallentree_investigated_tree
            'The stump.' if not fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stump.')
                jump fallentree_investigated_stump
            'The tracks.' if not fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tracks.')
                jump fallentree_investigated_tracks
            'The wagon.' if not fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The wagon.')
                jump fallentree_investigated_wagon
            'The river.' if not fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The river.')
                jump fallentree_investigated_river
            'The bushes.' if not fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bushes.')
                jump fallentree_investigated_bushes
            'The western hill.' if not fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western hill.')
                jump fallentree_investigated_hill
            'The road.' if not fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The road.')
                jump fallentree_investigated_road
            'I think I know what happened here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I take another look at the surrounding area.' if fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the surrounding area.')
                jump fallentree_investigated_area
            'I go back to the tree.' if fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the tree.')
                jump fallentree_investigated_tree
            'I go back to the stump.' if fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the stump.')
                jump fallentree_investigated_stump
            'I take another look at the tracks.' if fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the tracks.')
                jump fallentree_investigated_tracks
            'I return to the wagon.' if fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the wagon.')
                jump fallentree_investigated_wagon
            'I approach the river again.' if fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the river again.')
                jump fallentree_investigated_river
            'I go back to the bushes.' if fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the bushes.')
                jump fallentree_investigated_bushes
            'I climb on the western hill again.' if fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb on the western hill again.')
                jump fallentree_investigated_hill
            'I take another look at the road.' if fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the road.')
                jump fallentree_investigated_road

    label fallentree_investigated_wagon:
        if not fallentree_investigated_wagon:
            $ fallentree_investigated_wagon = 1
            $ minutes += 3
        menu:
            'The planks are still firm and there’s no mustiness in the air, but the vehicle needs just a push to fall to pieces, like a child’s toy with nothing to keep the parts together. There are ways to construct a wagon with just wood, leather, and fiber, but you find the marks of hinges, braces, nails, and clamps, which are now all gone. The wheels are missing their steel rims. You find only one linen bag, empty and moist.
            \n\nYou can’t estimate how deep the tracks are - the ground was hard, so the cart’s weight wasn’t a significant factor.
            '
            'The surrounding area.' if not fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The surrounding area.')
                jump fallentree_investigated_area
            'The tree.' if not fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tree.')
                jump fallentree_investigated_tree
            'The stump.' if not fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stump.')
                jump fallentree_investigated_stump
            'The tracks.' if not fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tracks.')
                jump fallentree_investigated_tracks
            'The wagon.' if not fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The wagon.')
                jump fallentree_investigated_wagon
            'The river.' if not fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The river.')
                jump fallentree_investigated_river
            'The bushes.' if not fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bushes.')
                jump fallentree_investigated_bushes
            'The western hill.' if not fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western hill.')
                jump fallentree_investigated_hill
            'The road.' if not fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The road.')
                jump fallentree_investigated_road
            'I think I know what happened here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I take another look at the surrounding area.' if fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the surrounding area.')
                jump fallentree_investigated_area
            'I go back to the tree.' if fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the tree.')
                jump fallentree_investigated_tree
            'I go back to the stump.' if fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the stump.')
                jump fallentree_investigated_stump
            'I take another look at the tracks.' if fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the tracks.')
                jump fallentree_investigated_tracks
            'I return to the wagon.' if fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the wagon.')
                jump fallentree_investigated_wagon
            'I approach the river again.' if fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the river again.')
                jump fallentree_investigated_river
            'I go back to the bushes.' if fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the bushes.')
                jump fallentree_investigated_bushes
            'I climb on the western hill again.' if fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb on the western hill again.')
                jump fallentree_investigated_hill
            'I take another look at the road.' if fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the road.')
                jump fallentree_investigated_road

    label fallentree_investigated_river:
        if not fallentree_investigated_river:
            $ fallentree_investigated_river = 1
            $ minutes += 1
        menu:
            'It would only take two steps to disappear in the deep water. The rocky bank smells fresh and is filled with the sounds of frogs, insects, and birds. It’s not a good spot to quench your thirst - the beds of long kelp, pulled by the flow of the river, are crowded with fish and four-legged creatures that you don’t even recognize.
            \n\nYou keep an eye on the land. There’s no carcass in sight and no signs of shells that would be left nearby.
            '
            'The surrounding area.' if not fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The surrounding area.')
                jump fallentree_investigated_area
            'The tree.' if not fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tree.')
                jump fallentree_investigated_tree
            'The stump.' if not fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stump.')
                jump fallentree_investigated_stump
            'The tracks.' if not fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tracks.')
                jump fallentree_investigated_tracks
            'The wagon.' if not fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The wagon.')
                jump fallentree_investigated_wagon
            'The river.' if not fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The river.')
                jump fallentree_investigated_river
            'The bushes.' if not fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bushes.')
                jump fallentree_investigated_bushes
            'The western hill.' if not fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western hill.')
                jump fallentree_investigated_hill
            'The road.' if not fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The road.')
                jump fallentree_investigated_road
            'I think I know what happened here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I take another look at the surrounding area.' if fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the surrounding area.')
                jump fallentree_investigated_area
            'I go back to the tree.' if fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the tree.')
                jump fallentree_investigated_tree
            'I go back to the stump.' if fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the stump.')
                jump fallentree_investigated_stump
            'I take another look at the tracks.' if fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the tracks.')
                jump fallentree_investigated_tracks
            'I return to the wagon.' if fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the wagon.')
                jump fallentree_investigated_wagon
            'I approach the river again.' if fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the river again.')
                jump fallentree_investigated_river
            'I go back to the bushes.' if fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the bushes.')
                jump fallentree_investigated_bushes
            'I climb on the western hill again.' if fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb on the western hill again.')
                jump fallentree_investigated_hill
            'I take another look at the road.' if fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the road.')
                jump fallentree_investigated_road

    label fallentree_investigated_bushes:
        if not fallentree_investigated_bushes:
            $ fallentree_investigated_bushes = 1
            $ minutes += 3
            $ item_arrow = 1
            $ renpy.notify("You found an arrow.")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You found an arrow.{/i}')
            $ custom1 = "You notice a pointy arrow made by a human hand, with a head made of horn and black-orange fletching. "
            if pc_class != "scholar":
                $ custom2 = "You don’t know what type of bird would have such feathers.\n\n"
            else:
                $ custom2 = "These feathers originally belonged to one of the local pheasants.\n\n"
        else:
            $ custom1 = ""
            $ custom2 = ""
        menu:
            'There are no berries left, only broken twigs, fallen leaves, and trampled grass. [custom1][custom2]You see no arrow marks around, not even on the wagon.
            '
            'The surrounding area.' if not fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The surrounding area.')
                jump fallentree_investigated_area
            'The tree.' if not fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tree.')
                jump fallentree_investigated_tree
            'The stump.' if not fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stump.')
                jump fallentree_investigated_stump
            'The tracks.' if not fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tracks.')
                jump fallentree_investigated_tracks
            'The wagon.' if not fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The wagon.')
                jump fallentree_investigated_wagon
            'The river.' if not fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The river.')
                jump fallentree_investigated_river
            'The bushes.' if not fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bushes.')
                jump fallentree_investigated_bushes
            'The western hill.' if not fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western hill.')
                jump fallentree_investigated_hill
            'The road.' if not fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The road.')
                jump fallentree_investigated_road
            'I think I know what happened here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I take another look at the surrounding area.' if fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the surrounding area.')
                jump fallentree_investigated_area
            'I go back to the tree.' if fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the tree.')
                jump fallentree_investigated_tree
            'I go back to the stump.' if fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the stump.')
                jump fallentree_investigated_stump
            'I take another look at the tracks.' if fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the tracks.')
                jump fallentree_investigated_tracks
            'I return to the wagon.' if fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the wagon.')
                jump fallentree_investigated_wagon
            'I approach the river again.' if fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the river again.')
                jump fallentree_investigated_river
            'I go back to the bushes.' if fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the bushes.')
                jump fallentree_investigated_bushes
            'I climb on the western hill again.' if fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb on the western hill again.')
                jump fallentree_investigated_hill
            'I take another look at the road.' if fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the road.')
                jump fallentree_investigated_road

    label fallentree_investigated_hill:
        if not fallentree_investigated_hill:
            $ fallentree_investigated_hill = 1
            $ minutes += 6
        menu:
            'The rocky wall isn’t much of a challenge. The top of the hill is covered with short grass and sparse trees. You notice a couple of bushes with a good view of the road, just next to the remains of a campfire - charred pieces of wood, ash, bird bones, trampled grass, and a broken earthenware bottle.
            \n\nYou follow the deepest tracks, leading to the edge of the soft earth. Someone jumped down, or at least stopped stepping on the grass.
            '
            'The surrounding area.' if not fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The surrounding area.')
                jump fallentree_investigated_area
            'The tree.' if not fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tree.')
                jump fallentree_investigated_tree
            'The stump.' if not fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stump.')
                jump fallentree_investigated_stump
            'The tracks.' if not fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tracks.')
                jump fallentree_investigated_tracks
            'The wagon.' if not fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The wagon.')
                jump fallentree_investigated_wagon
            'The river.' if not fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The river.')
                jump fallentree_investigated_river
            'The bushes.' if not fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bushes.')
                jump fallentree_investigated_bushes
            'The western hill.' if not fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western hill.')
                jump fallentree_investigated_hill
            'The road.' if not fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The road.')
                jump fallentree_investigated_road
            'I think I know what happened here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I take another look at the surrounding area.' if fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the surrounding area.')
                jump fallentree_investigated_area
            'I go back to the tree.' if fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the tree.')
                jump fallentree_investigated_tree
            'I go back to the stump.' if fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the stump.')
                jump fallentree_investigated_stump
            'I take another look at the tracks.' if fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the tracks.')
                jump fallentree_investigated_tracks
            'I return to the wagon.' if fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the wagon.')
                jump fallentree_investigated_wagon
            'I approach the river again.' if fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the river again.')
                jump fallentree_investigated_river
            'I go back to the bushes.' if fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the bushes.')
                jump fallentree_investigated_bushes
            'I climb on the western hill again.' if fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb on the western hill again.')
                jump fallentree_investigated_hill
            'I take another look at the road.' if fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the road.')
                jump fallentree_investigated_road

    label fallentree_investigated_road:
        if not fallentree_investigated_road:
            $ fallentree_investigated_road = 1
            $ minutes += 1
        menu:
            'The road here is already being overgrown, fading away, but it’s in no worse shape than the other parts of the southeastern route. No alternate path has formed around the blockade.
            '
            'The surrounding area.' if not fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The surrounding area.')
                jump fallentree_investigated_area
            'The tree.' if not fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tree.')
                jump fallentree_investigated_tree
            'The stump.' if not fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The stump.')
                jump fallentree_investigated_stump
            'The tracks.' if not fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The tracks.')
                jump fallentree_investigated_tracks
            'The wagon.' if not fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The wagon.')
                jump fallentree_investigated_wagon
            'The river.' if not fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The river.')
                jump fallentree_investigated_river
            'The bushes.' if not fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The bushes.')
                jump fallentree_investigated_bushes
            'The western hill.' if not fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The western hill.')
                jump fallentree_investigated_hill
            'The road.' if not fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The road.')
                jump fallentree_investigated_road
            'I think I know what happened here.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I take another look at the surrounding area.' if fallentree_investigated_area:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the surrounding area.')
                jump fallentree_investigated_area
            'I go back to the tree.' if fallentree_investigated_tree:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the tree.')
                jump fallentree_investigated_tree
            'I go back to the stump.' if fallentree_investigated_stump:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the stump.')
                jump fallentree_investigated_stump
            'I take another look at the tracks.' if fallentree_investigated_tracks:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the tracks.')
                jump fallentree_investigated_tracks
            'I return to the wagon.' if fallentree_investigated_wagon:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I return to the wagon.')
                jump fallentree_investigated_wagon
            'I approach the river again.' if fallentree_investigated_river:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I approach the river again.')
                jump fallentree_investigated_river
            'I go back to the bushes.' if fallentree_investigated_bushes:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I go back to the bushes.')
                jump fallentree_investigated_bushes
            'I climb on the western hill again.' if fallentree_investigated_hill:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I climb on the western hill again.')
                jump fallentree_investigated_hill
            'I take another look at the road.' if fallentree_investigated_road:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take another look at the road.')
                jump fallentree_investigated_road

label fallentree01investigateconclusion01:
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    menu:
        'What do you think has happened to the tree?
        '
        'Actually, I’ve second thoughts.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Actually, I’ve second thoughts.')
            $ fallentree_investigated = 0
            $ quest_fallentree_description01 = 0
            $ renpy.notify("Journal Updated: Fallen Tree")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
            jump fallentree01investigation00
        'It was cut down to set up an ambush.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It was cut down to set up an ambush.')
            $ fallentree_investigated += 1
            $ fallentree_investigated_opinion01 = "was cut down to set up an ambush"
            jump fallentree01investigateconclusion01p02
        'It was broken by a monster.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It was broken by a monster.')
            $ fallentree_investigated_opinion01 = "was broken by a monster"
            jump fallentree01investigateconclusion01p02
        'It was broken by the wind.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It was broken by the wind.')
            $ fallentree_investigated_opinion01 = "was broken by the wind"
            jump fallentree01investigateconclusion01p02
        'It was dying from an illness.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It was dying from an illness.')
            $ fallentree_investigated_opinion01 = "was dying from an illness"
            jump fallentree01investigateconclusion01p02
        'It’s impossible to tell.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s impossible to tell.')
            $ fallentree_investigated_opinion01 = "has mysteriously collapsed"
            jump fallentree01investigateconclusion01p02

    label fallentree01investigateconclusion01p02:
        menu:
            'Why was the wagon abandoned?
            '
            'Actually, I’ve second thoughts.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Actually, I’ve second thoughts.')
                $ fallentree_investigated = 0
                $ quest_fallentree_description01 = 0
                $ renpy.notify("Journal Updated: Fallen Tree")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                jump fallentree01investigation00
            'It was attacked by monsters.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It was attacked by monsters.')
                $ fallentree_investigated_opinion02 = "was attacked by monsters"
                jump fallentree01investigateconclusion01p03
            'The owners had no time to move it, so they left it behind.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- The owners had no time to move it, so they left it behind.')
                $ fallentree_investigated_opinion02 = "was left behind by the owners, who had no time to move it"
                jump fallentree01investigateconclusion01p03
            'It was attacked by highwaymen.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It was attacked by highwaymen.')
                $ fallentree_investigated_opinion02 = "was attacked by highwaymen"
                $ fallentree_investigated += 1
                jump fallentree01investigateconclusion01p03
            'It broke and the owners weren’t able to fix it.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It broke and the owners weren’t able to fix it.')
                $ fallentree_investigated_opinion02 = "broke and the owners weren’t able to fix it"
                jump fallentree01investigateconclusion01p03
            'It’s impossible to tell.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s impossible to tell.')
                $ fallentree_investigated_opinion02 = "was abandoned for no specific reason"
                jump fallentree01investigateconclusion01p03

    label fallentree01investigateconclusion01p03:
        menu:
            'What was originally transported on the wagon?
            '
            'Actually, I’ve second thoughts.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Actually, I’ve second thoughts.')
                $ fallentree_investigated = 0
                $ quest_fallentree_description01 = 0
                $ renpy.notify("Journal Updated: Fallen Tree")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                jump fallentree01investigation00
            'Some valuable merchandise.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Some valuable merchandise.')
                $ fallentree_investigated += 1
                $ fallentree_investigated_opinion03 = "which transported some valuable merchandise"
                jump fallentree01investigateconclusion01p04
            'Someone’s belongings.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Someone’s belongings.')
                $ fallentree_investigated_opinion03 = "which transported someone’s belongings"
                jump fallentree01investigateconclusion01p04
            'Passengers.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Passengers.')
                $ fallentree_investigated_opinion03 = "which transported human passengers"
                jump fallentree01investigateconclusion01p04
            'Food supplies.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Food supplies.')
                $ fallentree_investigated_opinion03 = "which transported food supplies"
                jump fallentree01investigateconclusion01p04
            'It’s impossible to tell.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s impossible to tell.')
                $ fallentree_investigated_opinion03 = "which transported unknown contents"
                $ fallentree_investigated += 1
                jump fallentree01investigateconclusion01p04

    label fallentree01investigateconclusion01p04:
        menu:
            'What happened to the owners of the wagon?
            '
            'Actually, I’ve second thoughts.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Actually, I’ve second thoughts.')
                $ fallentree_investigated = 0
                $ quest_fallentree_description01 = 0
                $ renpy.notify("Journal Updated: Fallen Tree")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                jump fallentree01investigation00
            'They were taken north.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- They were taken north.')
                $ fallentree_investigated_opinion04 = "were taken north"
                $ fallentree_investigated += 1
                jump fallentree01investigateconclusion01plast
            'They were killed on the spot.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- They were killed on the spot.')
                $ fallentree_investigated_opinion04 = "were killed on the spot"
                jump fallentree01investigateconclusion01plast
            'They’ve disappeared in the wilderness.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- They’ve disappeared in the wilderness.')
                $ fallentree_investigated_opinion04 = "have disappeared in the wilderness"
                jump fallentree01investigateconclusion01plast
            'They turned back.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- They turned back.')
                $ fallentree_investigated_opinion04 = "turned back"
                jump fallentree01investigateconclusion01plast
            'It’s impossible to tell.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s impossible to tell.')
                $ fallentree_investigated_opinion04 = "are missing"
                jump fallentree01investigateconclusion01plast

    label fallentree01investigateconclusion01plast:
        menu:
            'You think that the tree [fallentree_investigated_opinion01]. The cart, [fallentree_investigated_opinion03], [fallentree_investigated_opinion02]. Its owners [fallentree_investigated_opinion04].
            \n\nAre you sure that this is most likely what happened?
            '
            'Actually, I’ve second thoughts.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- Actually, I’ve second thoughts.')
                $ fallentree_investigated = 0
                $ quest_fallentree_description01 = 0
                $ renpy.notify("Journal Updated: Fallen Tree")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                jump fallentree01investigation00
            'I’m sure.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’m sure.')
                jump fallentree01investigation02after

    label fallentree01investigation02after:
        $ renpy.notify("Journal Updated: Fallen Tree")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
        $ quest_fallentree_description01 = 1
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if fallentree_investigated == 4:
            $ fallentree_investigated = "truth"
        else:
            $ fallentree_investigated = "false"
        if fallentree_investigated_opinion01 == "has mysteriously collapsed" and fallentree_investigated_opinion02 == "was abandoned for no specific reason" and fallentree_investigated_opinion03 == "which transported unknown contents" and fallentree_investigated_opinion04 == "are missing":
            menu:
                'Trying to figure out what happened here is no better than reading fortunes from chicken entrails. There are no real clues for you to follow.
                '
                'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
                    jump fallentree01investigation00
                'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                    jump fallentree01investigateconclusion01
                'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
                    $ fallentree_investigated = 0
                    $ quest_fallentree_description01 = 0
                    $ renpy.notify("Journal Updated: Fallen Tree")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                    jump fallentree01investigation00
                'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
                    pass
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
                    jump fallentreefishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
                    jump fallentreefishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
                    jump fallentreefishtrap03
                'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
                    jump fallentreefishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
                    pass
                'I consider washing myself in the river.':
                    jump fallentreebath01
        else:
            menu:
                'While you can’t be sure of what really happened here, you don’t think there’s much left for you to find. Let’s hope you haven’t missed anything.
                '
                'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
                    jump fallentree01investigation00
                'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                    jump fallentree01investigateconclusion01
                'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
                    $ fallentree_investigated = 0
                    $ quest_fallentree_description01 = 0
                    $ renpy.notify("Journal Updated: Fallen Tree")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                    jump fallentree01investigation00
                'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
                    pass
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
                    jump fallentreefishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
                    jump fallentreefishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
                    jump fallentreefishtrap03
                'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
                    jump fallentreefishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
                    pass
                'I consider washing myself in the river.':
                    jump fallentreebath01

label fallentree02regular01:
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ renpy.force_autosave(take_screenshot=False, block=True)
    menu:
        '[fallentree_fluff]
        '
        'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
            jump fallentree01investigation00
        'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
            jump fallentree01investigateconclusion01
        'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
            $ fallentree_investigated = 0
            $ quest_fallentree_description01 = 0
            $ renpy.notify("Journal Updated: Fallen Tree")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
            jump fallentree01investigation00
        'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
            pass
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
            jump fallentreefishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
            jump fallentreefishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
            jump fallentreefishtrap03
        'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
            jump fallentreefishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
            pass
        'I consider washing myself in the river.':
            jump fallentreebath01

label fallentreefishtrapALL:
    label fallentreefishtrap01:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ll spend some time setting up a fish trap at the bank.')
        show fishtrap fallentree01 at basicfade
        $ quarters += 2
        $ item_fishtrap -= 1
        $ fallentree_fishtrap = 1
        $ fallentree_fishtrap_daychecked = day
        $ fallentree_fishtrap_working = day
        $ fallentree_fishtrap_fishtimer = renpy.random.randint(1, 3)
        $ fallentree_fishtrap_fishtimer = (fallentree_fishtrap_fishtimer+day)
        menu:
            'You place the basket on the ground, then grab a bowl and start digging, looking for a few larger worms. You bait the stick and push it inside the basket, locking it between the sides, then cover the entrance with the lid - tying it together takes you a few good moments, but will be easier later on. You tie the rope to a rock and push it into the river, far enough that it sinks entirely.
            \n\nWho knows how long it will take before something large enough swims inside. Still, it would be better to not wait for too long - otherwise, the prey may die of hunger.
            '
            'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
                jump fallentree01investigation00
            'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
                $ fallentree_investigated = 0
                $ quest_fallentree_description01 = 0
                $ renpy.notify("Journal Updated: Fallen Tree")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                jump fallentree01investigation00
            'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
                pass
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
                jump fallentreefishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
                jump fallentreefishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
                jump fallentreefishtrap03
            'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
                jump fallentreefishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
                pass
            'I consider washing myself in the river.':
                jump fallentreebath01

    label fallentreefishtrap02:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I check if the fish trap had any luck.')
        if fallentree_fishtrap_fishtimer > day:
            $ fallentree_fishtrap_daychecked = day
            $ minutes += 5
            menu:
                'Unfortunately, it’s still empty.
                '
                'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
                    jump fallentree01investigation00
                'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                    jump fallentree01investigateconclusion01
                'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
                    $ fallentree_investigated = 0
                    $ quest_fallentree_description01 = 0
                    $ renpy.notify("Journal Updated: Fallen Tree")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                    jump fallentree01investigation00
                'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
                    pass
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
                    jump fallentreefishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
                    jump fallentreefishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
                    jump fallentreefishtrap03
                'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
                    jump fallentreefishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
                    pass
                'I consider washing myself in the river.':
                    jump fallentreebath01
        elif fallentree_fishtrap_fishtimer+3 > day:
            $ d100roll = 0
            $ d100roll = renpy.random.randint(1, 100)
            $ d100roll += fallentree_fishtrap_badthingmodifier
            $ minutes += 5
            if d100roll > 100: # harsh fail
                $ fallentree_fishtrap_badthingmodifier = 0
                $ fallentree_fishtrap_working = 0
                # $ fallentree_fishtrap = 0
                $ fallentree_fishtrap_fishtimer = 0
                $ fallentree_fishtrap_daychecked = 0
                menu:
                    'Sadly, it’s not only empty, the bait is already gone. Whatever had squeezed into the trap, was small enough to catch the worms and swim outside.
                    '
                    'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
                        jump fallentree01investigation00
                    'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                        jump fallentree01investigateconclusion01
                    'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
                        $ fallentree_investigated = 0
                        $ quest_fallentree_description01 = 0
                        $ renpy.notify("Journal Updated: Fallen Tree")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                        jump fallentree01investigation00
                    'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
                        pass
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
                        jump fallentreefishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
                        jump fallentreefishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
                        jump fallentreefishtrap03
                    'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
                        jump fallentreefishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
                        pass
                    'I consider washing myself in the river.':
                        jump fallentreebath01
            elif d100roll > 80: # soft fail
                $ fallentree_fishtrap_fishtimer = 0
                $ fallentree_fishtrap_working = 0
                menu:
                    'Sadly, it’s not only empty, the bait is already gone. Whatever had squeezed into the trap, was small enough to catch the worms and swim outside.
                    '
                    'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
                        jump fallentree01investigation00
                    'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                        jump fallentree01investigateconclusion01
                    'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
                        $ fallentree_investigated = 0
                        $ quest_fallentree_description01 = 0
                        $ renpy.notify("Journal Updated: Fallen Tree")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                        jump fallentree01investigation00
                    'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
                        pass
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
                        jump fallentreefishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
                        jump fallentreefishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
                        jump fallentreefishtrap03
                    'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
                        jump fallentreefishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
                        pass
                    'I consider washing myself in the river.':
                        jump fallentreebath01
            else: # success
                $ fallentree_fishtrap_fishtimer = 0
                $ quarters += 1
                if fallentree_fishtrap_badthingmodifier:
                    $ fallentree_fishtrap_badthingmodifier += 10
                $ fallentree_fishtrap_working = 0
                $ d100roll = 0
                $ d100roll = renpy.random.randint(1, 100)
                if d100roll > 65:
                    $ item_rawfishtotalnumber += 1
                    $ achievement_fish += 1
                    $ item_rawfish_gaining = 1
                    $ renpy.notify("You caught a fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught a fish.{/i}')
                    $ custom1 = "You pull the rope and see a flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animal with two careful blows in the top of its head, then finish it off with a knife, cutting it underneath the gill plate. You spend another minute or two bleeding out the fish in the river, then cover it with a waxed linen sheet.\n\nYou should eat it soon, before it spoils."
                elif d100roll > 30:
                    $ item_rawfishtotalnumber += 2
                    $ achievement_fish += 2
                    $ item_rawfish_gaining = 2
                    $ renpy.notify("You caught 2 fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught 2 fish.{/i}')
                    $ custom1 = "You pull the rope and see two flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animals one by one, with two careful blows in the top of their heads, then finish them off with a knife, cutting underneath the gill plates. You spend another minute or two bleeding out the fish in the river, then cover them with a waxed linen sheet.\n\nYou should eat them soon, before they spoil."
                else:
                    $ item_rawfishtotalnumber += 3
                    $ achievement_fish += 3
                    $ item_rawfish_gaining = 3
                    $ renpy.notify("You caught 3 fish.")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You caught 3 fish.{/i}')
                    $ custom1 = "You pull the rope and see three flopping fish inside. You prepare your axe, then open the lid and reach for your catch. You stun the animals one by one, with two careful blows in the top of their heads, then finish them off with a knife, cutting underneath the gill plates. You spend another minute or two bleeding out the fish in the river, then cover them with a waxed linen sheet.\n\nYou should eat them soon, before they spoil."
                menu:
                    '[custom1]
                    '
                    'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
                        jump fallentree01investigation00
                    'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                        jump fallentree01investigateconclusion01
                    'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
                        $ fallentree_investigated = 0
                        $ quest_fallentree_description01 = 0
                        $ renpy.notify("Journal Updated: Fallen Tree")
                        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                        jump fallentree01investigation00
                    'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
                        pass
                    'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
                        pass
                    'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
                        jump fallentreefishtrap01
                    'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
                        pass
                    'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
                        jump fallentreefishtrap02
                    'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
                        pass
                    'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
                        jump fallentreefishtrap03
                    'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
                        jump fallentreefishtrap04
                    'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
                        pass
                    'I consider washing myself in the river.':
                        jump fallentreebath01
        else:
            $ fallentree_fishtrap_working = 0
            $ fallentree_fishtrap_fishtimer = 0
            $ minutes += 5
            menu:
                'Sadly, you’re too late. Your catch has already starved to death, and is now eaten by dozens of little creatures. You open the lid and pour out the contents into the river.
                '
                'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
                    jump fallentree01investigation00
                'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                    jump fallentree01investigateconclusion01
                'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
                    $ fallentree_investigated = 0
                    $ quest_fallentree_description01 = 0
                    $ renpy.notify("Journal Updated: Fallen Tree")
                    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                    jump fallentree01investigation00
                'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
                    pass
                'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
                    pass
                'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
                    jump fallentreefishtrap01
                'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
                    pass
                'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
                    jump fallentreefishtrap02
                'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
                    pass
                'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
                    jump fallentreefishtrap03
                'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
                    jump fallentreefishtrap04
                'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
                    pass
                'I consider washing myself in the river.':
                    jump fallentreebath01

    label fallentreefishtrap03:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I set the fish trap again.')
        $ fallentree_fishtrap_working = day
        $ minutes += 5
        $ fallentree_fishtrap = 1
        show fishtrap fallentree01 at basicfade
        $ fallentree_fishtrap_daychecked = day
        $ fallentree_fishtrap_fishtimer = renpy.random.randint(1, 4)
        $ fallentree_fishtrap_fishtimer = (fallentree_fishtrap_fishtimer+day)
        menu:
            'You need to look for worms again, but at least sealing the lid takes only a moment.
            '
            'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
                jump fallentree01investigation00
            'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
                $ fallentree_investigated = 0
                $ quest_fallentree_description01 = 0
                $ renpy.notify("Journal Updated: Fallen Tree")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                jump fallentree01investigation00
            'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
                pass
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
                jump fallentreefishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
                jump fallentreefishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
                jump fallentreefishtrap03
            'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
                jump fallentreefishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
                pass
            'I consider washing myself in the river.':
                jump fallentreebath01

    label fallentreefishtrap04:
        $ narrator.add_history(kind='nvl', who=narrator.name, what='- I take the trap back')
        $ minutes += 5
        $ item_fishtrap += 1
        $ renpy.notify("You dismantled the trap.")
        $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}You dismantled the trap.{/i}')
        $ fallentree_fishtrap = 0
        hide fishtrap
        $ fallentree_fishtrap_daychecked = 0
        $ fallentree_fishtrap_working = 0
        $ fallentree_fishtrap_fishtimer = 0
        menu:
            'You shake the basket, expecting it will get drier during your ride, then attach it to your saddle.
            '
            'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
                jump fallentree01investigation00
            'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
                jump fallentree01investigateconclusion01
            'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
                $ fallentree_investigated = 0
                $ quest_fallentree_description01 = 0
                $ renpy.notify("Journal Updated: Fallen Tree")
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
                jump fallentree01investigation00
            'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
                pass
            'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
                pass
            'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
                jump fallentreefishtrap01
            'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
                pass
            'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
                jump fallentreefishtrap02
            'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
                pass
            'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
                jump fallentreefishtrap03
            'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
                jump fallentreefishtrap04
            'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
                pass
            'I consider washing myself in the river.':
                jump fallentreebath01

label fallentreebath01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I consider washing myself in the river.')
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    if cleanliness_equipment <= 0:
        $ custom1 = "{color=#6a6a6a}You need at least 1 piece of bathing equipment to get more out of this place.{/color}"
        $ custom2 = ""
    elif cleanliness_equipment == 1:
        if item_soap:
            $ custom1 = "The oak-ash soap you own can help you get cleaner."
        elif item_teethset:
            $ custom1 = "The teeth set you own can help you get cleaner."
        elif item_perfume:
            $ custom1 = "The perfume you own can help you get cleaner."
        $ custom2 = "\n\n{color=#6a6a6a}You need 3 pieces of bathing equipment to get more out of this place.{/color}"
    elif cleanliness_equipment == 2:
        if item_soap and item_teethset:
            $ custom1 = "The oak-ash soap and the teeth set you own can help you get cleaner."
        elif item_soap and item_perfume:
            $ custom1 = "The oak-ash soap and the perfume you own can help you get cleaner."
        elif item_teethset and item_perfume:
            $ custom1 = "The teeth set and the perfume you own can help you get cleaner."
        $ custom2 = "\n\n{color=#6a6a6a}You need 3 pieces of bathing equipment to get more out of this place.{/color}"
    elif cleanliness_equipment >= 3:
        $ custom1 = "The oak-ash soap, the teeth set, and the perfume you own can help you get cleaner."
        $ custom2 = ""
    menu:
        'The river is full of life, not only a bit brown-and-greenish, but also smelling of algae. It won’t help you much.
        \n\n[custom1][custom2]
        '
        'I wash my hands, face, and neck.' if (cleanliness < 1 and cleanliness_equipment < 1):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my hands, face, and neck.')
            jump fallentreebath02
        'I wash my shell.' if (cleanliness < 2 and cleanliness_equipment < 3 and cleanliness_equipment > 0):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell.')
            jump fallentreebath02
        'I wash my shell carefully.' if (cleanliness < 3 and cleanliness_equipment >= 3):
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my shell carefully.')
            jump fallentreebath02
        'I won’t get any cleaner here. (disabled)' if (cleanliness >= 1 and cleanliness < 3 and cleanliness_equipment < 1) or (cleanliness == 2 and cleanliness_equipment >= 1 and cleanliness_equipment < 3):
            pass
        'I’m as clean as I can get. (disabled)' if cleanliness == 3:
            pass
        'I step away.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
            jump fallentreebathornobath01

    label fallentreebath02:
        if not cleanliness:
            if cleanliness_equipment >= 3:
                $ minutes += 20
                $ cleanliness = limit_cleanliness(cleanliness+3)
                show plus3appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+3 appearance points.{/i}')
            if cleanliness_equipment >= 1:
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness+2)
                show plus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 appearance points.{/i}')
            else:
                $ minutes += 10
                $ cleanliness = limit_cleanliness(cleanliness+1)
                show plus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance points.{/i}')
        elif cleanliness == 1:
            if cleanliness_equipment >= 3:
                $ quarters += 1
                $ cleanliness = limit_cleanliness(cleanliness+2)
                show plus2appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+2 appearance points.{/i}')
            else:
                $ minutes += 10
                $ cleanliness = limit_cleanliness(cleanliness+1)
                show plus1appearance at appearancechange onlayer myoverlay
                $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        elif cleanliness == 2:
            $ minutes += 10
            $ cleanliness = limit_cleanliness(cleanliness+1)
            show plus1appearance at appearancechange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}+1 appearance point.{/i}')
        menu:
            'You scare away a few frogs, crouch by the bank, and draw handfuls of water.
            '
            'I put on my clothes.':
                $ narrator.add_history(kind='nvl', who=narrator.name, what='- I step away.')
                jump fallentreebathornobath01

label fallentreebathornobath01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I wash my hands, neck, and face in the river.')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    menu:
        'You go back to {color=#f6d6bd}[horsename]{/color}.
        '
        'I want to look around.' if not quest_fallentree_description01 and not fallentree_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I want to look around.')
            jump fallentree01investigation00
        'I think I know what happened here.' if not quest_fallentree_description01 and not fallentree_cleared and fallentree_examined:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I think I know what happened here.')
            jump fallentree01investigateconclusion01
        'I’ve second thoughts about the investigation.' if quest_fallentree_description01 and not fallentree_cleared:
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I’ve second thoughts about the investigation.')
            $ fallentree_investigated = 0
            $ quest_fallentree_description01 = 0
            $ renpy.notify("Journal Updated: Fallen Tree")
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}Journal Updated: Fallen Tree{/i}')
            jump fallentree01investigation00
        'I can’t get rid of this obstacle all by myself. (disabled)' if not fallentree_cleared:
            pass
        'It would be a decent spot for a fish trap, if I had one. (disabled)' if not item_fishtrap and not fallentree_fishtrap:
            pass
        'I’ll spend some time setting up a fish trap at the bank.' ( condition="item_fishtrap and not fallentree_fishtrap and quarters <= (world_daylength-8)" ):
            jump fallentreefishtrap01
        'It’s already dark. Setting up a fish trap right now would be dangerous. (disabled)' ( condition="item_fishtrap and not fallentree_fishtrap and quarters > (world_daylength-8)" ):
            pass
        'Let’s see if the fish trap had any luck.' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked != day:
            jump fallentreefishtrap02
        'I can inspect the fish trap tomorrow, or later. (disabled)' if fallentree_fishtrap and fallentree_fishtrap_working and fallentree_fishtrap_daychecked == day:
            pass
        'I set the fish trap again.' if fallentree_fishtrap and not fallentree_fishtrap_working:
            jump fallentreefishtrap03
        'I take the fish trap back.' if fallentree_fishtrap and not fallentree_fishtrap_working and not item_fishtrap:
            jump fallentreefishtrap04
        'These fish traps are so large I can only carry one of them at a time. (disabled)' if fallentree_fishtrap and not fallentree_fishtrap_working and item_fishtrap:
            pass
        'I consider washing myself in the river.':
            jump fallentreebath01
