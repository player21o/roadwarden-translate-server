# ###################### FORD
default ford_firsttime = 0
default ford_insects_dealtwith = 0
default ford_fluff = ""
default ford_fluff_old = ""
default ford_fluff_looked = 0
default ford_side = 0
default ford_differentroute = 0
default ford_torch = 0
default ford_wrapping = 0

label ford01:
    nvl clear
    $ pc_area = "ford"
    stop music fadeout 4.0
    play nature "audio/ambient/ford01.ogg" fadeout 2.0 fadein 5.0 volume 1.0
    show areapicture ford01 at basicfade
    label ford_fluffloop:
        $ ford_fluff = ""
        $ ford_fluff = renpy.random.choice(['The creek is gentle today, but the insects are as ubiquitous as ever. Something sits down on your lips even before you reach the ford.', 'You spot a corpse of a small monkey at the side of the creek, getting devoured by thousands of buzzing flies. Many more insects are flying nearby.', 'You ride slowly as you notice an unusual movement at the top of the crag. A large bird is sitting among the rocks like you’re its next dinner.', 'A dance of flies, gnats, and mosquitoes is disturbed by the arrival of feasting dragonflies, though they present no threat to the sheer number of the blood-sucking creatures.', 'As you get closer to the creek, you hear the pained screech of a small beast. A badger is crossing the water, trying to outrun the insects and hide between the blades of grass.'])
        if ford_fluff_old == ford_fluff:
            jump ford_fluffloop
        else:
            $ ford_fluff_old = ford_fluff
    with Fade(1.5, 1.0, 1.5, color="#0f2a3f")
    if not ford_firsttime:
        $ can_leave = 0
        $ can_rest = 0
        $ can_items = 0
        $ world_known_areas += 1
        $ ford_firsttime = 1
        $ westerncrossroads_unlocked = 1
        $ bogentrance_unlocked = 1
        jump fordfirsttime01
    elif not fordinsectsdescription:
        jump fordfirsttime01
    else:
        $ can_leave = 1
        $ can_rest = 1
        $ can_items = 1
        if not ford_insects_dealtwith:
            jump fordregular01
        else:
            jump fordregular01cleared

label fordfirsttime01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    $ fordinsectsdescription = 1
    if ford_side == "south":
        $ custom1 = "southern"
    else:
        $ custom1 = "northern"
    menu:
        'The road leads to a gentle creek, filled with the buzzing of flies, mosquitoes, and gnats. You don’t spot any critters among the tall meadows, tree branches, or rocky slopes. Seeing the shapeless, dark vortex of wings, {color=#f6d6bd}[horsename]{/color} snorts.
        \n\nYou’re currently on the [custom1] bank.
        '
        'It’s time to test the ointment I carry in my bundles.' if not ford_insects_dealtwith and item_stingointment:
            jump fordcrossingwithointment01
        'With access to an alchemy table, I could make a protective ointment against their bites. (disabled)' if not ford_insects_dealtwith and not item_stingointment and pc_class == "scholar":
            pass
        'I look for a different route.' if not ford_differentroute and not ford_insects_dealtwith:
            jump forddifferentroute01
        'I ride forward with a blazing torch.' if not ford_insects_dealtwith and not ford_torch:
            jump fordcrossingwithtorch01
        'It will take some time, but I’ll wrap myself up with every piece of clothing I own.' if not ford_insects_dealtwith and not ford_wrapping:
            jump fordcrossingwithwrappingup01
        'Time to wrap myself up.' if not ford_insects_dealtwith and ford_wrapping:
            jump fordcrossingwithwrappingup02
        'I don’t care. I just hurry {color=#f6d6bd}[horsename]{/color}.' if not ford_insects_dealtwith:
            jump fordcrossingwithnothing01

label fordregular01:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    if ford_side == "south":
        $ custom1 = "southern"
    else:
        $ custom1 = "northern"
    menu:
        '[ford_fluff]
        \n\nYou’re standing on the [custom1] bank.
        '
        'It’s time to test the ointment I carry in my bundles.' if not ford_insects_dealtwith and item_stingointment:
            jump fordcrossingwithointment01
        'With access to an alchemy table, I could make a protective ointment against their bites. (disabled)' if not ford_insects_dealtwith and not item_stingointment and pc_class == "scholar":
            pass
        'I look for a different route.' if not ford_differentroute and not ford_insects_dealtwith:
            jump forddifferentroute01
        'I ride forward with a blazing torch.' if not ford_insects_dealtwith and not ford_torch:
            jump fordcrossingwithtorch01
        'It will take some time, but I’ll wrap myself up with every piece of clothing I own.' if not ford_insects_dealtwith and not ford_wrapping:
            jump fordcrossingwithwrappingup01
        'Time to wrap myself up.' if not ford_insects_dealtwith and ford_wrapping:
            jump fordcrossingwithwrappingup02
        'I don’t care. I just hurry {color=#f6d6bd}[horsename]{/color}.' if not ford_insects_dealtwith:
            jump fordcrossingwithnothing01

label forddifferentroute01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I look for a different route.')
    $ ford_differentroute = 1
    $ minutes += 5
    menu:
        'The path is barely squeezed between the hills, with no signs of settlements or game trails, and the grasses too tall and dense to allow you safely ride through the wilderness. You won’t reach the other bank without entering the swarm.
        '
        'It’s time to test the ointment I carry in my bundles.' if not ford_insects_dealtwith and item_stingointment:
            jump fordcrossingwithointment01
        'With access to an alchemy table, I could make a protective ointment against their bites. (disabled)' if not ford_insects_dealtwith and not item_stingointment and pc_class == "scholar":
            pass
        'I look for a different route.' if not ford_differentroute and not ford_insects_dealtwith:
            jump forddifferentroute01
        'I ride forward with a blazing torch.' if not ford_insects_dealtwith and not ford_torch:
            jump fordcrossingwithtorch01
        'It will take some time, but I’ll wrap myself up with every piece of clothing I own.' if not ford_insects_dealtwith and not ford_wrapping:
            jump fordcrossingwithwrappingup01
        'Time to wrap myself up.' if not ford_insects_dealtwith and ford_wrapping:
            jump fordcrossingwithwrappingup02
        'I don’t care. I just hurry {color=#f6d6bd}[horsename]{/color}.' if not ford_insects_dealtwith:
            jump fordcrossingwithnothing01

label fordcrossingwithointment01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It’s time to test the ointment I carry in my bundles.')
    $ ford_insects_dealtwith = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    label fordcrossingwithointment01groupvariables:
        if ford_side == "south":
            $ ford_side = "north"
        else:
            $ ford_side = "south"
        if ford_insects_dealtwith:
            $ FROMwesterncrossroadsTOford = 3
            $ FROMfordTObogentrance = 3
        elif ford_side == "south":
            $ FROMwesterncrossroadsTOford = 3
            $ FROMfordTObogentrance = 5
        else:
            $ FROMwesterncrossroadsTOford = 5
            $ FROMfordTObogentrance = 3
        if westerncrossroads_firsttime and bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime:
            $ NWcornerunlocked = 1
        #########TO SOUTHERN CROSSROADS
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime:
            $ tosoutherncrossroads = (FROMwesterncrossroadsTOfordULT + SWcorner)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ tosoutherncrossroads = (FROMfoggylakeTOfordULT + NEcorner + SEcorner)
        else:
            $ tosoutherncrossroads = 100
        #########TO MILITARY CAMP
        $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
        #########TO WESTERN CROSSROADS
        $ towesterncrossroads = (FROMwesterncrossroadsTOfordULT)
        #########TO WEST GATE
        $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
        #########TO OLD PAGOS
        $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
        #########TO MONASTERY
        $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
        #########TO WATCHTOWER
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime:
            $ towatchtower = (FROMfoggylakeTOfordULT + NEcorner)
        elif SWcornerunlocked and dolmen_firsttime and fallentree_firsttime:
            $ towatchtower = (FROMwesterncrossroadsTOfordULT + SWcorner + SEcorner)
        else:
            $ towatchtower = 100
        #########TO EUDOCIA’S HOUSE
        $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
        #########TO STONE SIGN
        $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
        #########TO FOGGY LAKE
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime:
            $ tofoggylake = (FROMfoggylakeTOfordULT)
        elif SWcornerunlocked and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime and wanderer_firsttime and foragingground_firsttime:
            $ tofoggylake = (tosoutherncrossroads + SEcorner + NEcorner)
        else:
            $ tofoggylake = 100
        #########TO CREEKS
        $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
        #########TO OLD TUNNEL
        $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
        #########TO GALE ROCKS
        $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
        #########TO BEACH
        $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
        #########TO PELT OF THE NORTH
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
            $ topeltnorth = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell + FROMruinedvillageTObeholder + FROMpeltnorthTOruinedvillage)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
        else:
            $ topeltnorth = 100
        #########TO RUINED VILLAGE
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime:
            $ toruinedvillage = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell + FROMruinedvillageTObeholder)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
        else:
            $ toruinedvillage = 100
        #########TO BEHOLDER
        if westerncrossroads_firsttime and howlersdell_firsttime:
            $ tobeholder = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell)
        elif NEcornerunlocked and bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime:
            $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
        else:
            $ tobeholder = 100
        #########TO DRUID’S CAVE
        $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
        #########TO HOWLER’S DELL
        if westerncrossroads_firsttime:
            $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
        elif NEcornerunlocked and ruinedshelter_firsttime and northernroad_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime and beholder_firsttime:
            $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
        else:
            $ tohowlersdell = 100
        #########TO ROCKSLIDE
        $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
        #########TO FISHING HAMLET
        $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
        #########TO DOLMEN
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime:
            $ todolmen = (tosoutherncrossroads + FROMsoutherncrossroadsTOdolmenULT)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and fallentree_firsttime:
            $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
        else:
            $ todolmen = 100
        #########TO FALLEN TREE
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and dolmen_firsttime:
            $ tofallentree = (tosoutherncrossroads + FROMsoutherncrossroadsTOfallentreeULT)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked:
            $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
        else:
            $ tofallentree = 100
        #########TO STONE BRIDGE
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime and huntercabin_firsttime:
            $ tostonebridge = (tofoggylake + FROMfoggylakeTOstonebridgeULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and watchtower_firsttime:
            $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
        else:
            $ tostonebridge = 100
        #########TO GHOUL CAVE
        $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
        #########TO GIANT STATUE
        $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
        #########TO MOUNTAIN ROAD
        $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
        #########TO TRIBE OF THE GREEN MOUNTAIN
        $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
        #########TO HUNTER’S CABIN
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime:
            $ tohuntercabin = (tofoggylake + FROMfoggylakeTOhuntercabinULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime:
            $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
        else:
            $ tohuntercabin = 100
        #########TO FORAGING GROUND
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime:
            $ toforagingground = (tofoggylake + FROMfoggylakeTOforaginggroundULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime:
            $ toforagingground = (towatchtower + FROMwatchtowerTOforaginggroundULT)
        else:
            $ toforagingground = 100
        #########TO WANDERER
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime:
            $ towanderer = (tofoggylake + FROMfoggylakeTOwandererULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime:
            $ towanderer = (towatchtower + FROMwatchtowerTOwandererULT)
        else:
            $ towanderer = 100
        #########TO FORD
        $ toford = 0
        #########TO BOG ENTRANCE
        $ tobogentrance = (FROMfordTObogentrance)
        #########TO BOG CROSSROADS
        $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
        #########TO BOG ROAD
        $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
        #########TO PEAT FIELD
        $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
        #########TO WHITE MARSHES
        $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
        #########TO RUINED SHELTER
        if bogentrance_firsttime:
            $ toruinedshelter = (FROMfordTObogentrance + FROMbogentranceTOruinedshelter)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and NEcornerunlocked and northernroad_firsttime:
            $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
        else:
            $ toruinedshelter = 100
        #########TO NORTHERN ROAD
        if bogentrance_firsttime and ruinedshelter_firsttime:
            $ tonorthernroad = (FROMfordTObogentrance + FROMbogentranceTOruinedshelter + FROMruinedshelterTOnorthernroad)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and NEcornerunlocked:
            $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
        else:
            $ tonorthernroad = 100
        #########TO HOWLERS LAIR
        $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
    menu:
        'You open the ointment, getting hit by the unappetizing scent of lavender, mint, and basil. You apply a thin layer of balm to your open skin, as well as to a few spread out spots on {color=#f6d6bd}[horsename]{/color}. You hope the smell won’t stay for long.
        \n\nYou carry on. The swarm notices you right away, gliding at you like a dark boulder, but before you collide with it, it shatters, forming a tunnel in the middle, though buzzing even louder than before. A few extraordinarily resilient gnats still sit on your horse’s back, so you try to throw them off.
        '
        'Riding through this path should be much easier from now on. (disabled)':
            pass

label fordcrossingwithtorch01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I ride forward with a blazing torch.')
    $ quarters += 1
    menu:
        'You move away from the creek, get on your feet, and unpack the tinderbox, the wooden stave, and the set of rags, as well as the oil. After you assemble a torch, you sit down on the ground, preparing the flint and the linen char cloth. Decades ago, before The Southern Invasion, people used fire strikers made of thick steel, but all you have is a cube-like piece of harsh pyrite. It’s not ideal, but good enough for a couple of sparks.
        \n\nHolding the fire, you get back in the saddle. You swing your weapon left and right - there isn’t as much smoke as you expected.
        '
        'Let’s put it to the test.':
            $ narrator.add_history(kind='nvl', who=narrator.name, what='- Let’s put it to the test.')
            $ ford_torch = 1
            $ pc_hp = limit_pc_hp(pc_hp-1)
            show minus1hp at hpchange onlayer myoverlay
            $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
            $ can_leave = 1
            $ can_rest = 1
            $ can_items = 1
            label fordcrossingwithtorch01groupvariables:
                if ford_side == "south":
                    $ ford_side = "north"
                else:
                    $ ford_side = "south"
                if ford_insects_dealtwith:
                    $ FROMwesterncrossroadsTOford = 3
                    $ FROMfordTObogentrance = 3
                elif ford_side == "south":
                    $ FROMwesterncrossroadsTOford = 3
                    $ FROMfordTObogentrance = 5
                else:
                    $ FROMwesterncrossroadsTOford = 5
                    $ FROMfordTObogentrance = 3
                if westerncrossroads_firsttime and bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime:
                    $ NWcornerunlocked = 1
                #########TO SOUTHERN CROSSROADS
                if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime:
                    $ tosoutherncrossroads = (FROMwesterncrossroadsTOfordULT + SWcorner)
                elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
                    $ tosoutherncrossroads = (FROMfoggylakeTOfordULT + NEcorner + SEcorner)
                else:
                    $ tosoutherncrossroads = 100
                #########TO MILITARY CAMP
                $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
                #########TO WESTERN CROSSROADS
                $ towesterncrossroads = (FROMwesterncrossroadsTOfordULT)
                #########TO WEST GATE
                $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
                #########TO OLD PAGOS
                $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
                #########TO MONASTERY
                $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
                #########TO WATCHTOWER
                if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime:
                    $ towatchtower = (FROMfoggylakeTOfordULT + NEcorner)
                elif SWcornerunlocked and dolmen_firsttime and fallentree_firsttime:
                    $ towatchtower = (FROMwesterncrossroadsTOfordULT + SWcorner + SEcorner)
                else:
                    $ towatchtower = 100
                #########TO EUDOCIA’S HOUSE
                $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
                #########TO STONE SIGN
                $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
                #########TO FOGGY LAKE
                if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime:
                    $ tofoggylake = (FROMfoggylakeTOfordULT)
                elif SWcornerunlocked and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime and wanderer_firsttime and foragingground_firsttime:
                    $ tofoggylake = (tosoutherncrossroads + SEcorner + NEcorner)
                else:
                    $ tofoggylake = 100
                #########TO CREEKS
                $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
                #########TO OLD TUNNEL
                $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
                #########TO GALE ROCKS
                $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
                #########TO BEACH
                $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
                #########TO PELT OF THE NORTH
                if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
                    $ topeltnorth = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell + FROMruinedvillageTObeholder + FROMpeltnorthTOruinedvillage)
                elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
                    $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
                else:
                    $ topeltnorth = 100
                #########TO RUINED VILLAGE
                if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime:
                    $ toruinedvillage = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell + FROMruinedvillageTObeholder)
                elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
                    $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
                else:
                    $ toruinedvillage = 100
                #########TO BEHOLDER
                if westerncrossroads_firsttime and howlersdell_firsttime:
                    $ tobeholder = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell)
                elif NEcornerunlocked and bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime:
                    $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
                else:
                    $ tobeholder = 100
                #########TO DRUID’S CAVE
                $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
                #########TO HOWLER’S DELL
                if westerncrossroads_firsttime:
                    $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
                elif NEcornerunlocked and ruinedshelter_firsttime and northernroad_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime and beholder_firsttime:
                    $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
                else:
                    $ tohowlersdell = 100
                #########TO ROCKSLIDE
                $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
                #########TO FISHING HAMLET
                $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
                #########TO DOLMEN
                if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime:
                    $ todolmen = (tosoutherncrossroads + FROMsoutherncrossroadsTOdolmenULT)
                elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and fallentree_firsttime:
                    $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
                else:
                    $ todolmen = 100
                #########TO FALLEN TREE
                if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and dolmen_firsttime:
                    $ tofallentree = (tosoutherncrossroads + FROMsoutherncrossroadsTOfallentreeULT)
                elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked:
                    $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
                else:
                    $ tofallentree = 100
                #########TO STONE BRIDGE
                if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime and huntercabin_firsttime:
                    $ tostonebridge = (tofoggylake + FROMfoggylakeTOstonebridgeULT)
                elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and watchtower_firsttime:
                    $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
                else:
                    $ tostonebridge = 100
                #########TO GHOUL CAVE
                $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
                #########TO GIANT STATUE
                $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
                #########TO MOUNTAIN ROAD
                $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
                #########TO TRIBE OF THE GREEN MOUNTAIN
                $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
                #########TO HUNTER’S CABIN
                if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime:
                    $ tohuntercabin = (tofoggylake + FROMfoggylakeTOhuntercabinULT)
                elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime:
                    $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
                else:
                    $ tohuntercabin = 100
                #########TO FORAGING GROUND
                if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime:
                    $ toforagingground = (tofoggylake + FROMfoggylakeTOforaginggroundULT)
                elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime:
                    $ toforagingground = (towatchtower + FROMwatchtowerTOforaginggroundULT)
                else:
                    $ toforagingground = 100
                #########TO WANDERER
                if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime:
                    $ towanderer = (tofoggylake + FROMfoggylakeTOwandererULT)
                elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime:
                    $ towanderer = (towatchtower + FROMwatchtowerTOwandererULT)
                else:
                    $ towanderer = 100
                #########TO FORD
                $ toford = 0
                #########TO BOG ENTRANCE
                $ tobogentrance = (FROMfordTObogentrance)
                #########TO BOG CROSSROADS
                $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
                #########TO BOG ROAD
                $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
                #########TO PEAT FIELD
                $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
                #########TO WHITE MARSHES
                $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
                #########TO RUINED SHELTER
                if bogentrance_firsttime:
                    $ toruinedshelter = (FROMfordTObogentrance + FROMbogentranceTOruinedshelter)
                elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and NEcornerunlocked and northernroad_firsttime:
                    $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
                else:
                    $ toruinedshelter = 100
                #########TO NORTHERN ROAD
                if bogentrance_firsttime and ruinedshelter_firsttime:
                    $ tonorthernroad = (FROMfordTObogentrance + FROMbogentranceTOruinedshelter + FROMruinedshelterTOnorthernroad)
                elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and NEcornerunlocked:
                    $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
                else:
                    $ tonorthernroad = 100
                #########TO HOWLERS LAIR
                $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
            menu:
                'Once you get closer to the ford, countless creatures beset you, filling your eyes, mouth, and nose, hitting you like a squishy, buzzing hail. You ride forward blindly, instantly forgetting about your preparations, trying to get out of here as fast as you can, but the insects are sticking with you for much longer than the smoke.
                \n\nIt takes a few minutes for you to escape. The red marks on your skin start to burn. You get down to put out the torch by rubbing it against the beaten track. {color=#f6d6bd}[horsename]{/color} swishes its tail angrily as it gives you a reproachful look, pinning its ears back to its head.
                \n\nUnless you find an easier way to protect yourself, the insects will keep slowing you down.
                '
                'Well, that didn’t help much. (disabled)':
                    pass

label fordcrossingwithwrappingup01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- It will take some time, but I’ll wrap myself up with every piece of clothing I own.')
    $ ford_wrapping = 1
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ quarters += 2
    label fordcrossingwithwrappingup01groupvariables:
        if ford_side == "south":
            $ ford_side = "north"
        else:
            $ ford_side = "south"
        if ford_insects_dealtwith:
            $ FROMwesterncrossroadsTOford = 3
            $ FROMfordTObogentrance = 3
        elif ford_side == "south":
            $ FROMwesterncrossroadsTOford = 3
            $ FROMfordTObogentrance = 5
        else:
            $ FROMwesterncrossroadsTOford = 5
            $ FROMfordTObogentrance = 3
        #########TO SOUTHERN CROSSROADS
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime:
            $ tosoutherncrossroads = (FROMwesterncrossroadsTOfordULT + SWcorner)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ tosoutherncrossroads = (FROMfoggylakeTOfordULT + NEcorner + SEcorner)
        else:
            $ tosoutherncrossroads = 100
        #########TO MILITARY CAMP
        $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
        #########TO WESTERN CROSSROADS
        $ towesterncrossroads = (FROMwesterncrossroadsTOfordULT)
        #########TO WEST GATE
        $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
        #########TO OLD PAGOS
        $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
        #########TO MONASTERY
        $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
        #########TO WATCHTOWER
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime:
            $ towatchtower = (FROMfoggylakeTOfordULT + NEcorner)
        elif SWcornerunlocked and dolmen_firsttime and fallentree_firsttime:
            $ towatchtower = (FROMwesterncrossroadsTOfordULT + SWcorner + SEcorner)
        else:
            $ towatchtower = 100
        #########TO EUDOCIA’S HOUSE
        $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
        #########TO STONE SIGN
        $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
        #########TO FOGGY LAKE
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime:
            $ tofoggylake = (FROMfoggylakeTOfordULT)
        elif SWcornerunlocked and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime and wanderer_firsttime and foragingground_firsttime:
            $ tofoggylake = (tosoutherncrossroads + SEcorner + NEcorner)
        else:
            $ tofoggylake = 100
        #########TO CREEKS
        $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
        #########TO OLD TUNNEL
        $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
        #########TO GALE ROCKS
        $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
        #########TO BEACH
        $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
        #########TO PELT OF THE NORTH
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
            $ topeltnorth = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell + FROMruinedvillageTObeholder + FROMpeltnorthTOruinedvillage)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
        else:
            $ topeltnorth = 100
        #########TO RUINED VILLAGE
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime:
            $ toruinedvillage = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell + FROMruinedvillageTObeholder)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
        else:
            $ toruinedvillage = 100
        #########TO BEHOLDER
        if westerncrossroads_firsttime and howlersdell_firsttime:
            $ tobeholder = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell)
        elif NEcornerunlocked and bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime:
            $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
        else:
            $ tobeholder = 100
        #########TO DRUID’S CAVE
        $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
        #########TO HOWLER’S DELL
        if westerncrossroads_firsttime:
            $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
        elif NEcornerunlocked and ruinedshelter_firsttime and northernroad_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime and beholder_firsttime:
            $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
        else:
            $ tohowlersdell = 100
        #########TO ROCKSLIDE
        $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
        #########TO FISHING HAMLET
        $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
        #########TO DOLMEN
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime:
            $ todolmen = (tosoutherncrossroads + FROMsoutherncrossroadsTOdolmenULT)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and fallentree_firsttime:
            $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
        else:
            $ todolmen = 100
        #########TO FALLEN TREE
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and dolmen_firsttime:
            $ tofallentree = (tosoutherncrossroads + FROMsoutherncrossroadsTOfallentreeULT)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked:
            $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
        else:
            $ tofallentree = 100
        #########TO STONE BRIDGE
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime and huntercabin_firsttime:
            $ tostonebridge = (tofoggylake + FROMfoggylakeTOstonebridgeULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and watchtower_firsttime:
            $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
        else:
            $ tostonebridge = 100
        #########TO GHOUL CAVE
        $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
        #########TO GIANT STATUE
        $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
        #########TO MOUNTAIN ROAD
        $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
        #########TO TRIBE OF THE GREEN MOUNTAIN
        $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
        #########TO HUNTER’S CABIN
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime:
            $ tohuntercabin = (tofoggylake + FROMfoggylakeTOhuntercabinULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime:
            $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
        else:
            $ tohuntercabin = 100
        #########TO FORAGING GROUND
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime:
            $ toforagingground = (tofoggylake + FROMfoggylakeTOforaginggroundULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime:
            $ toforagingground = (towatchtower + FROMwatchtowerTOforaginggroundULT)
        else:
            $ toforagingground = 100
        #########TO WANDERER
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime:
            $ towanderer = (tofoggylake + FROMfoggylakeTOwandererULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime:
            $ towanderer = (towatchtower + FROMwatchtowerTOwandererULT)
        else:
            $ towanderer = 100
        #########TO FORD
        $ toford = 0
        #########TO BOG ENTRANCE
        $ tobogentrance = (FROMfordTObogentrance)
        #########TO BOG CROSSROADS
        $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
        #########TO BOG ROAD
        $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
        #########TO PEAT FIELD
        $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
        #########TO WHITE MARSHES
        $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
        #########TO RUINED SHELTER
        if bogentrance_firsttime:
            $ toruinedshelter = (FROMfordTObogentrance + FROMbogentranceTOruinedshelter)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and NEcornerunlocked and northernroad_firsttime:
            $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
        else:
            $ toruinedshelter = 100
        #########TO NORTHERN ROAD
        if bogentrance_firsttime and ruinedshelter_firsttime:
            $ tonorthernroad = (FROMfordTObogentrance + FROMbogentranceTOruinedshelter + FROMruinedshelterTOnorthernroad)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and NEcornerunlocked:
            $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
        else:
            $ tonorthernroad = 100
        #########TO HOWLERS LAIR
        $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
    menu:
        'It takes you longer than you would hope for, but you manage to cover yourself with an armor of at least three layers of linen, leather, wool, and hemp. Only your eyes and a single finger remain without cover.
        \n\nOnce you get closer to the ford, countless creatures beset you, making you instantly shut your eyes. They are striking the clothes covering your open mouth, and hitting your shell like a squishy, buzzing hail. You ride forward blindly, trying to get out of here as fast as you can, but the insects stick with you for another few minutes.
        \n\nThe red marks on your finger start to burn slowly. {color=#f6d6bd}[horsename]{/color} swishes its tail angrily as it turns its head to its left, observing you with one reproachful eye, pinning its ears back.
        \n\nYou look around to make sure nothing will try to jump on you, and once you decide you’re safe, you take off the suit. Unless you find an easier way to protect yourself, the insects will keep slowing you down.
        '
        'At least I kept my blood. (disabled)':
            pass

label fordcrossingwithwrappingup02:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- Time to wrap myself up.')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    $ quarters += 2
    $ minutes += 5
    label fordcrossingwithwrappingup02groupvariables:
        if ford_side == "south":
            $ ford_side = "north"
        else:
            $ ford_side = "south"
        if ford_insects_dealtwith:
            $ FROMwesterncrossroadsTOford = 3
            $ FROMfordTObogentrance = 3
        elif ford_side == "south":
            $ FROMwesterncrossroadsTOford = 3
            $ FROMfordTObogentrance = 5
        else:
            $ FROMwesterncrossroadsTOford = 5
            $ FROMfordTObogentrance = 3
        #########TO SOUTHERN CROSSROADS
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime:
            $ tosoutherncrossroads = (FROMwesterncrossroadsTOfordULT + SWcorner)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ tosoutherncrossroads = (FROMfoggylakeTOfordULT + NEcorner + SEcorner)
        else:
            $ tosoutherncrossroads = 100
        #########TO MILITARY CAMP
        $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
        #########TO WESTERN CROSSROADS
        $ towesterncrossroads = (FROMwesterncrossroadsTOfordULT)
        #########TO WEST GATE
        $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
        #########TO OLD PAGOS
        $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
        #########TO MONASTERY
        $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
        #########TO WATCHTOWER
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime:
            $ towatchtower = (FROMfoggylakeTOfordULT + NEcorner)
        elif SWcornerunlocked and dolmen_firsttime and fallentree_firsttime:
            $ towatchtower = (FROMwesterncrossroadsTOfordULT + SWcorner + SEcorner)
        else:
            $ towatchtower = 100
        #########TO EUDOCIA’S HOUSE
        $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
        #########TO STONE SIGN
        $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
        #########TO FOGGY LAKE
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime:
            $ tofoggylake = (FROMfoggylakeTOfordULT)
        elif SWcornerunlocked and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime and wanderer_firsttime and foragingground_firsttime:
            $ tofoggylake = (tosoutherncrossroads + SEcorner + NEcorner)
        else:
            $ tofoggylake = 100
        #########TO CREEKS
        $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
        #########TO OLD TUNNEL
        $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
        #########TO GALE ROCKS
        $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
        #########TO BEACH
        $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
        #########TO PELT OF THE NORTH
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
            $ topeltnorth = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell + FROMruinedvillageTObeholder + FROMpeltnorthTOruinedvillage)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
        else:
            $ topeltnorth = 100
        #########TO RUINED VILLAGE
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime:
            $ toruinedvillage = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell + FROMruinedvillageTObeholder)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
        else:
            $ toruinedvillage = 100
        #########TO BEHOLDER
        if westerncrossroads_firsttime and howlersdell_firsttime:
            $ tobeholder = (towesterncrossroads + FROMhowlersdellTOwesterncrossroads + FROMbeholderTOhowlersdell)
        elif NEcornerunlocked and bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime:
            $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
        else:
            $ tobeholder = 100
        #########TO DRUID’S CAVE
        $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
        #########TO HOWLER’S DELL
        if westerncrossroads_firsttime:
            $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
        elif NEcornerunlocked and ruinedshelter_firsttime and northernroad_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime and beholder_firsttime:
            $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
        else:
            $ tohowlersdell = 100
        #########TO ROCKSLIDE
        $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
        #########TO FISHING HAMLET
        $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
        #########TO DOLMEN
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime:
            $ todolmen = (tosoutherncrossroads + FROMsoutherncrossroadsTOdolmenULT)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and fallentree_firsttime:
            $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
        else:
            $ todolmen = 100
        #########TO FALLEN TREE
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and dolmen_firsttime:
            $ tofallentree = (tosoutherncrossroads + FROMsoutherncrossroadsTOfallentreeULT)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked:
            $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
        else:
            $ tofallentree = 100
        #########TO STONE BRIDGE
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime and huntercabin_firsttime:
            $ tostonebridge = (tofoggylake + FROMfoggylakeTOstonebridgeULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and watchtower_firsttime:
            $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
        else:
            $ tostonebridge = 100
        #########TO GHOUL CAVE
        $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
        #########TO GIANT STATUE
        $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
        #########TO MOUNTAIN ROAD
        $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
        #########TO TRIBE OF THE GREEN MOUNTAIN
        $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
        #########TO HUNTER’S CABIN
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime:
            $ tohuntercabin = (tofoggylake + FROMfoggylakeTOhuntercabinULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime:
            $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
        else:
            $ tohuntercabin = 100
        #########TO FORAGING GROUND
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime:
            $ toforagingground = (tofoggylake + FROMfoggylakeTOforaginggroundULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime:
            $ toforagingground = (towatchtower + FROMwatchtowerTOforaginggroundULT)
        else:
            $ toforagingground = 100
        #########TO WANDERER
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime:
            $ towanderer = (tofoggylake + FROMfoggylakeTOwandererULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime:
            $ towanderer = (towatchtower + FROMwatchtowerTOwandererULT)
        else:
            $ towanderer = 100
        #########TO FORD
        $ toford = 0
        #########TO BOG ENTRANCE
        $ tobogentrance = (FROMfordTObogentrance)
        #########TO BOG CROSSROADS
        $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
        #########TO BOG ROAD
        $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
        #########TO PEAT FIELD
        $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
        #########TO WHITE MARSHES
        $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
        #########TO RUINED SHELTER
        if bogentrance_firsttime:
            $ toruinedshelter = (FROMfordTObogentrance + FROMbogentranceTOruinedshelter)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and NEcornerunlocked and northernroad_firsttime:
            $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
        else:
            $ toruinedshelter = 100
        #########TO NORTHERN ROAD
        if bogentrance_firsttime and ruinedshelter_firsttime:
            $ tonorthernroad = (FROMfordTObogentrance + FROMbogentranceTOruinedshelter + FROMruinedshelterTOnorthernroad)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and NEcornerunlocked:
            $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
        else:
            $ tonorthernroad = 100
        #########TO HOWLERS LAIR
        $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
    menu:
        'You repeat the procedure, already knowing that {color=#f6d6bd}[horsename]{/color} won’t be happy about what’s to come. As you surround yourself with linen, leather, wool, and hemp, you leave a thin open line for your eyes.
        \n\nAfter more than half an hour, you get to the other side and leave the buzzing swarm behind you.
        '
        'At least I kept my blood. (disabled)':
            pass

label fordcrossingwithnothing01:
    $ narrator.add_history(kind='nvl', who=narrator.name, what='- I don’t care. I just hurry {color=#f6d6bd}%s{/color}.' %horsename)
    $ pc_hp = limit_pc_hp(pc_hp-1)
    show minus1hp at hpchange onlayer myoverlay
    $ narrator.add_history(kind='nvl', who=narrator.name, what='{i}-1 vitality point.{/i}')
    $ can_leave = 1
    $ can_rest = 1
    $ can_items = 1
    label fordcrossingwithnothing01groupvariables:
        if ford_side == "south":
            $ ford_side = "north"
        else:
            $ ford_side = "south"
        if ford_insects_dealtwith:
            $ FROMwesterncrossroadsTOford = 3
            $ FROMfordTObogentrance = 3
        elif ford_side == "south":
            $ FROMwesterncrossroadsTOford = 3
            $ FROMfordTObogentrance = 5
        else:
            $ FROMwesterncrossroadsTOford = 5
            $ FROMfordTObogentrance = 3
        if westerncrossroads_firsttime and bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime:
            $ NWcornerunlocked = 1
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime:
            $ tosoutherncrossroads = (FROMwesterncrossroadsTOfordULT + SWcorner)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ tosoutherncrossroads = (FROMfoggylakeTOfordULT + NEcorner + SEcorner)
        else:
            $ tosoutherncrossroads = 100
        $ tomilitarycamp = (tosoutherncrossroads + FROMsoutherncrossroadsTOmilitarycampULT)
        $ towesterncrossroads = (FROMwesterncrossroadsTOfordULT)
        $ towestgate = (towesterncrossroads + FROMwesterncrossroadsTOwestgateULT)
        $ tooldpagos = (towesterncrossroads + FROMwesterncrossroadsTOoldpagosULT)
        $ tomonastery = (towesterncrossroads + FROMwesterncrossroadsTOmonasteryULT)
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime and huntercabin_firsttime and stonebridge_firsttime:
            $ towatchtower = (FROMfoggylakeTOfordULT + NEcorner)
        elif SWcornerunlocked and dolmen_firsttime and fallentree_firsttime:
            $ towatchtower = (FROMwesterncrossroadsTOfordULT + SWcorner + SEcorner)
        else:
            $ towatchtower = 100
        $ toeudociahouse = (towatchtower + FROMwatchtowerTOeudociahouseULT)
        $ tostonesign = (towatchtower + FROMwatchtowerTOstonesignULT)
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime:
            $ tofoggylake = (FROMfoggylakeTOfordULT)
        elif SWcornerunlocked and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime and wanderer_firsttime and foragingground_firsttime:
            $ tofoggylake = (tosoutherncrossroads + SEcorner + NEcorner)
        else:
            $ tofoggylake = 100
        $ tocreeks = (tofoggylake + FROMfoggylakeTOcreeks)
        $ tooldtunnel = (tofoggylake + FROMfoggylakeTOoldtunnel)
        $ togalerocks = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks)
        $ tobeach = (tofoggylake + FROMfoggylakeTOoldtunnel + FROMoldtunnelTOgalerocks + FROMgalerocksTObeach)
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime:
            $ topeltnorth = (tosoutherncrossroads - FROMsoutherncrossroadsTOpeltnorthULT)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ topeltnorth = (tosoutherncrossroads + FROMsoutherncrossroadsTOpeltnorthULT)
        else:
            $ topeltnorth = 100
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime:
            $ toruinedvillage = (tosoutherncrossroads - FROMsoutherncrossroadsTOruinedvillageULT)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and SEcornerunlocked:
            $ toruinedvillage = (tosoutherncrossroads + FROMsoutherncrossroadsTOruinedvillageULT)
        else:
            $ toruinedvillage = 100
        if westerncrossroads_firsttime and howlersdell_firsttime:
            $ tobeholder = (tosoutherncrossroads - FROMsoutherncrossroadsTObeholderULT)
        elif NEcornerunlocked and bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime:
            $ tobeholder = (towesterncrossroads + FROMwesterncrossroadsTObeholderULT)
        else:
            $ tobeholder = 100
        $ todruidcave = (tobeholder + FROMbeholderTOdruidcave)
        if westerncrossroads_firsttime:
            $ tohowlersdell = (tosoutherncrossroads + FROMsoutherncrossroadsTOhowlersdellULT)
        elif NEcornerunlocked and ruinedshelter_firsttime and northernroad_firsttime and SEcornerunlocked and peltnorth_firsttime and ruinedvillage_firsttime and beholder_firsttime:
            $ tohowlersdell = (towesterncrossroads + FROMwesterncrossroadsTOhowlersdellULT)
        else:
            $ tohowlersdell = 100
        $ torockslide = (tohowlersdell + FROMhowlersdellTOrockslide)
        $ tofishinghamlet = (torockslide + FROMrockslideTOfishinghamlet)
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime:
            $ todolmen = (tosoutherncrossroads + FROMsoutherncrossroadsTOdolmenULT)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked and fallentree_firsttime:
            $ todolmen = (towatchtower + FROMwatchtowerTOdolmenULT)
        else:
            $ todolmen = 100
        if westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and dolmen_firsttime:
            $ tofallentree = (tosoutherncrossroads + FROMsoutherncrossroadsTOfallentreeULT)
        elif bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and NEcornerunlocked:
            $ tofallentree = (towatchtower + FROMwatchtowerTOfallentreeULT)
        else:
            $ tofallentree = 100
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime and huntercabin_firsttime:
            $ tostonebridge = (tofoggylake + FROMfoggylakeTOstonebridgeULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and watchtower_firsttime:
            $ tostonebridge = (towatchtower + FROMwatchtowerTOstonebridgeULT)
        else:
            $ tostonebridge = 100
        $ toghoulcave = (tostonebridge + FROMstonebridgeTOghoulcave)
        $ togiantstatue = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue)
        $ tomountainroad = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad)
        $ togreenmountaintribe = (tostonebridge + FROMstonebridgeTOghoulcave + FROMghoulcaveTOgiantstatue + FROMgiantstatueTOmountainroad + FROMmountainroadTOgreenmountaintribe)
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime and foragingground_firsttime:
            $ tohuntercabin = (tofoggylake + FROMfoggylakeTOhuntercabinULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime:
            $ tohuntercabin = (towatchtower + FROMwatchtowerTOhuntercabinULT)
        else:
            $ tohuntercabin = 100
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime and wanderer_firsttime:
            $ toforagingground = (tofoggylake + FROMfoggylakeTOforaginggroundULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime:
            $ toforagingground = (towatchtower + FROMwatchtowerTOforaginggroundULT)
        else:
            $ toforagingground = 100
        if bogentrance_firsttime and ruinedshelter_firsttime and northernroad_firsttime and foggylake_firsttime:
            $ towanderer = (tofoggylake + FROMfoggylakeTOwandererULT)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and stonebridge_firsttime and huntercabin_firsttime and foragingground_firsttime:
            $ towanderer = (towatchtower + FROMwatchtowerTOwandererULT)
        else:
            $ towanderer = 100
        $ toford = 0
        $ tobogentrance = (FROMfordTObogentrance)
        $ tobogcrossroads = (tobogentrance + FROMbogentranceTObogcrossroads)
        $ tobogroad = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad)
        $ topeatfield = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTObogroad + FROMbogroadTOpeatfield)
        $ towhitemarshes = (tobogentrance + FROMbogentranceTObogcrossroads + FROMbogcrossroadsTOvines + FROMvinesTOwhitemarshes)
        if bogentrance_firsttime:
            $ toruinedshelter = (FROMfordTObogentrance + FROMbogentranceTOruinedshelter)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and NEcornerunlocked and northernroad_firsttime:
            $ toruinedshelter = (tofoggylake + FROMfoggylakeTOruinedshelterULT)
        else:
            $ toruinedshelter = 100
        if bogentrance_firsttime and ruinedshelter_firsttime:
            $ tonorthernroad = (FROMfordTObogentrance + FROMbogentranceTOruinedshelter + FROMruinedshelterTOnorthernroad)
        elif westerncrossroads_firsttime and howlersdell_firsttime and beholder_firsttime and ruinedvillage_firsttime and peltnorth_firsttime and SEcornerunlocked and NEcornerunlocked:
            $ tonorthernroad = (tofoggylake + FROMfoggylakeTOnorthernroadULT)
        else:
            $ tonorthernroad = 100
        $ tohowlerslair = (tofoggylake + FROMfoggylakeTOhowlerslairULT)
    menu:
        'Once you get closer to the ford, countless creatures beset you, filling your eyes, mouth, and nose, hitting you like a squishy, buzzing hail. You ride forward blindly, instantly forgetting about your preparations, trying to get out of here as fast as you can, but the insects are sticking with you for another few minutes.
        \n\nThe red marks on your skin start to burn slowly. {color=#f6d6bd}[horsename]{/color} swishes its tail angrily as it turns its head to its left, observing you with one reproachful eye, pinning its ears back to its head.
        \n\nUnless you find a way to protect yourself, the insects will keep slowing you down.
        '
        'At least I didn’t waste any time. (disabled)':
            pass

label fordregular01cleared:
    $ renpy.force_autosave(take_screenshot=True, block=True)
    menu:
        '[ford_fluff] You apply the ointment on you and your mount, an the insects keep a fair distance.
        '
        'There isn’t much more I could do here. (disabled)':
            pass
