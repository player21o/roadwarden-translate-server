###################### ROAD BEFORE BEACH
default beforebeach_fluff = 0
default beforebeach_fluff_old = 0

label beforebeach01:
    nvl clear
    $ pc_area = "beforebeach"
    $ renpy.music.play("audio/track_14galerocks.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    # stop music fadeout 4.0
    # play nature "audio/ambient/beach01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    stop nature fadeout 4.0
    show areapicture galerockstobeach at basicfade
    label beforebeach_fluffloop:
        $ beforebeach_fluff = ""
        $ beforebeach_fluff = renpy.random.choice(['The smells of the fresh fish and salt are intense.', 'There aren’t that many fishes in sight, and the grumpy faces suggest it was a rough day.', 'The silver fishes are almost flowing out of the barrels.', 'Some of the wayfarers eat while they’re walking, commenting on how hungry they are after a long day.'])
        if beforebeach_fluff_old == beforebeach_fluff:
            jump beforebeach_fluffloop
        else:
            $ beforebeach_fluff_old = beforebeach_fluff
    $ can_leave = 0
    $ can_rest = 0
    $ can_items = 0
    $ quarters -= 1
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    jump beforebeachregular01

label beforebeachregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        'On your way north, the fishers greet you with polite nods and tired looks. Some of them carry the boats and tools, dividing the weight between them, while the others are pulling the ropes attached to the wide barge, moving it up the river slowly. [beforebeach_fluff]
        '
        'I slow down and talk to them.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I slow down and talk to them.')
            $ quarters += 1
            if galerocks_photios_firsttime:
                jump galerocksphotios01
            else:
                jump galerocksphotios01firsttime
        'I don’t have the time now to stop.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t have the time now to stop.')
            $ quarters += 1
            jump beach01

label beforebeachafterinteraction01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        'Followed by the fishers’ goodbyes, you lead {color=#f6d6bd}[horsename]{/color} away.
        '
        'I ride to {color=#f6d6bd}the beach{/color}.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride to {color=#f6d6bd}the beach{/color}.')
            $ quarters += 1
            jump beach01
        'I ride back to {color=#f6d6bd}Gale Rocks{/color}.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride back to {color=#f6d6bd}Gale Rocks{/color}.')
            $ travel_destination = "galerocks"
            $ quarters += 1
            jump galerocks01
