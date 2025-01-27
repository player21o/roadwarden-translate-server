################################################################################
## Initialization
################################################################################

init offset = -1

######### MAPA PODRÓŻY
default map_icon1 = 0
default map_icon2 = 0
default map_icon3 = 0
default map_icon4 = 0
default map_icon5 = 0
default map_icon6 = 0
default map_icon7 = 0
default map_icon8 = 0
# $ dolmen_firsttime = 2
# $ fallentree_firsttime = 2
# $ southerncrossroads_firsttime = 2
# $ peltnorth_firsttime = 2
# $ ruinedvillage_firsttime = 2
# $ beholder_firsttime = 2
# $ druidcave_firsttime = 2
# $ watchtower_firsttime = 2
# $ eudocia_firsttime = 2
# $ stonebridge_firsttime = 2
# $ stonesign_firsttime = 2
# $ ghoulcave_firsttime = 2
# $ huntercabin_firsttime = 2
# $ howlersdell_firsttime = 2
# $ rockslide_firsttime = 2
# $ fishinghamlet_firsttime = 2
# $ westerncrossroads_firsttime = 2
# $ oldpagos_firsttime = 2
# $ monastery_firsttime = 2
# $ westgate_firsttime = 2
# $ foggylake_firsttime = 2
# $ wanderer_firsttime = 2
# $ foragingground_firsttime = 2
# $ ford_firsttime = 2
# $ bogentrance_firsttime = 2
# $ bogcrossroads_firsttime = 2
# $ ruinedshelter_firsttime = 2
# $ northernroad_firsttime = 2
# $ howlerslair_firsttime = 2
# $ creeks_traveling = 2
# $ oldtunnel_firsttime = 2
# $ galerocks_firsttime = 2
# $ beach_firsttime = 2
# $ giantstatue_firsttime = 2
# $ mountainroad_firsttime = 2
# $ greenmountaintribe_firsttime = 2
# $ bogcrossroads_firsttime = 2
# $ bogroad_firsttime = 2
# $ peatfield_firsttime = 2
# $ whitemarshes_firsttime = 2
# $ vines_firsttime = 2
# $ shortcut_westernentrance_firsttime = 2
# $ shortcut_deepforest_firsttime = 2
# $ shortcut_deepforest_babydragon = 2
# $ shortcut_deepforest_treant = 2
# $ shortcut_deepforest_frightape = 2
# $ shortcut_deepforest_fruitgrove = 2
# $ shortcut_cairn_firsttime = 2
# $ shortcut_meadow_firsttime = 2
# $ shortcut_banditshideout_road_firsttime = 2
# $ shortcut_banditshideout_obstacle1 = 2
# $ shortcut_banditshideout_obstacle2 = 2
# $ shortcut_woodenroad_firsttime = 2
# $ shortcut_woodenroad_stoathunt = 2
# $ shortcut_woodenroad_fisheater = 2
# $ shortcut_woodenroad_horseaccident = 2
# $ shortcut_woodenroad_drinkingcat = 2
# $ shortcut_darkforest_firsttime = 2
# $ shortcut_darkforest_bandit = 2
# $ shortcut_darkforest_goblins = 2
# $ shortcut_darkforest_bagontree = 2
# $ shortcut_darkforest_birdfollower = 2
# $ shortcut_easternentrance_firsttime = 2
# $ shortcut_easternentrance_gnolls = 2
# $ shortcut_ibex = 2
screen map_display():
    modal True
    #tag menu
    zorder 130
    default tt = Tooltip("")
    default tt2 = Tooltip("")
    default tt3 = Tooltip("")
    default tt4 = Tooltip("")
    default tt5 = Tooltip("")
    key "m" action [Hide('map_display'), With(dissolve)]
    key "M" action [Hide('map_display'), With(dissolve)]
    imagemap:
        ground "map/mapbase.png" at truecenter, map_dissolve
        add "map/mapparts/citytocrossroad.png" xpos 1074 ypos 914
        if dolmen_firsttime and fallentree_firsttime:
            add "map/mapparts/dolmentofallentree.png" xpos 1300 ypos 767
        if southerncrossroads_firsttime:
            add "map/mapparts/militarycamptosoutherncrossroads.png" xpos 1074 ypos 914
        if peltnorth_firsttime:
            add "map/mapparts/southerncrossroadstopeltnorth.png" xpos 971 ypos 856
        if dolmen_firsttime:
            add "map/mapparts/southerncrossroadstodolmen.png" xpos 1146 ypos 840
        if ruinedvillage_firsttime and beholder_firsttime:
            add "map/mapparts/ruinedvillagetobeholder.png" xpos 597 ypos 739
        if peltnorth_firsttime and ruinedvillage_firsttime:
            add "map/mapparts/peltnorthtoruinedvillage.png" xpos 780 ypos 815
        if beholder_firsttime and druidcave_firsttime:
            add "map/mapparts/beholdertodruidscave.png" xpos 552 ypos 786
        if watchtower_firsttime and fallentree_firsttime and eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            add "map/mapparts/fallentreetowatchtower_fixed.png" xpos 1386 ypos 625
        elif watchtower_firsttime and fallentree_firsttime:
            add "map/mapparts/fallentreetowatchtower.png" xpos 1386 ypos 625
        if watchtower_firsttime and eudocia_firsttime and eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            add "map/mapparts/watchtowertoeudocia_fixed.png" xpos 1375 ypos 616
        elif watchtower_firsttime and eudocia_firsttime:
            add "map/mapparts/watchtowertoeudocia.png" xpos 1375 ypos 616
        if watchtower_firsttime and stonebridge_firsttime and eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            add "map/mapparts/watchtowertostonebridge_fixed.png" xpos 1344 ypos 542
        elif watchtower_firsttime and stonebridge_firsttime:
            add "map/mapparts/watchtowertostonebridge.png" xpos 1344 ypos 542
        if stonesign_firsttime and not watchtower_firsttime and eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            add "map/mapparts/stonesigntowatchtoweralt_fixed.png" xpos 1291 ypos 617
        elif stonesign_firsttime and not watchtower_firsttime:
            add "map/mapparts/stonesigntowatchtoweralt.png" xpos 1291 ypos 617
        if watchtower_firsttime and stonesign_firsttime and eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            add "map/mapparts/stonesigntowatchtower_fixed.png" xpos 1291 ypos 617
        elif watchtower_firsttime and stonesign_firsttime:
            add "map/mapparts/stonesigntowatchtower.png" xpos 1291 ypos 617
        if ghoulcave_firsttime and stonebridge_firsttime:
            add "map/mapparts/bridgetocave.png" xpos 1350 ypos 477
        if huntercabin_firsttime and stonebridge_firsttime:
            add "map/mapparts/bridgetocabin.png" xpos 1259 ypos 494
        if howlersdell_firsttime:
            add "map/mapparts/howlersdelltorockslidealt.png" xpos 479 ypos 514
        if beholder_firsttime and howlersdell_firsttime:
            add "map/mapparts/beholdertohowlersdell.png" xpos 597 ypos 601
        # if (howlersdell_firsttime and rockslide_firstblockade_seen and not rockslide_firstblockade_cleared) or (howlersdell_firsttime and rockslide_firstblockade_seen and rockslide_firstblockade_cleared and not rockslide_firsttime):
        #     add "map/mapparts/howlersdelltorockslideplusshrubs.png" xpos 479 ypos 514
        if howlersdell_firsttime and rockslide_firsttime:
            add "map/mapparts/howlersdelltorockslide.png" xpos 479 ypos 514
        if rockslide_firsttime and fishinghamlet_firsttime:
            add "map/mapparts/rockslidetofishinghamlet.png" xpos 358 ypos 492
        if howlersdell_firsttime and westerncrossroads_firsttime:
            add "map/mapparts/howlersdelltowesterncrossroads.png" xpos 653 ypos 471
        if westerncrossroads_firsttime and oldpagos_firsttime:
            add "map/mapparts/westerncrossroadstooldpagos.png" xpos 495 ypos 377
        if oldpagos_firsttime and monastery_firsttime:
            add "map/mapparts/oldpagostomonastery.png" xpos 499 ypos 332
        if westgate_firsttime and not westerncrossroads_firsttime:
            add "map/mapparts/westerncrossroadstowestgatealt.png" xpos 657 ypos 471
        if westerncrossroads_firsttime and westgate_firsttime:
            add "map/mapparts/westerncrossroadstowestgate.png" xpos 657 ypos 471
        if foggylake_firsttime and wanderer_firsttime:
            add "map/mapparts/wanderertofoggylake.png" xpos 1054 ypos 241
        if wanderer_firsttime and foragingground_firsttime:
            add "map/mapparts/foraginggroundtowanderer.png" xpos 1080 ypos 322
        if huntercabin_firsttime and foragingground_firsttime:
            add "map/mapparts/cabintoforagingground.png" xpos 1151 ypos 402
        if westerncrossroads_firsttime and ford_firsttime:
            add "map/mapparts/westerncrossroadstoford.png" xpos 622 ypos 340
        if ford_firsttime and bogentrance_firsttime:
            add "map/mapparts/fordtobogentrance.png" xpos 641 ypos 232
        if bogentrance_firsttime and bogcrossroads_firsttime:
            add "map/mapparts/bogentrancetobogcrossroads.png" xpos 746 ypos 253
        if bogentrance_firsttime and ruinedshelter_firsttime:
            add "map/mapparts/bogentrancetoruinedshelter.png" xpos 764 ypos 219
        if ruinedshelter_firsttime and northernroad_firsttime:
            add "map/mapparts/ruinedsheltertonorthernroad.png" xpos 880 ypos 223
        if howlerslair_firsttime:
            add "map/mapparts/northernroadtohowlerslair.png" xpos 946 ypos 240
        if northernroad_firsttime and foggylake_firsttime:
            add "map/mapparts/northernroadtofoggylake.png" xpos 962 ypos 237
        if northernroad_firsttime and foggylake_firsttime and wanderer_firsttime:
            add "map/mapparts/entirefoggylake.png" xpos 970 ypos 262
        if creeks_traveling:
            add "map/mapparts/foggylaketocreeks01.png" xpos 1076 ypos 192
        if creeks_traveling > 1:
            add "map/mapparts/foggylaketocreeks02.png" xpos 1151 ypos 133
        if foggylake_firsttime and oldtunnel_firsttime:
            add "map/mapparts/foggylaketooldtunnel.png" xpos 901 ypos 164
        if oldtunnel_firsttime and galerocks_firsttime:
            add "map/mapparts/oldtunneltogalerocks.png" xpos 870 ypos 108
        if galerocks_firsttime and beach_firsttime:
            add "map/mapparts/galerockstobeach.png" xpos 797 ypos 43
        if ghoulcave_firsttime and giantstatue_firsttime:
            add "map/mapparts/cavetogiantstatue.png" xpos 1494 ypos 435
        if giantstatue_firsttime and mountainroad_firsttime:
            add "map/mapparts/giantstatuetomountainroad.png" xpos 1562 ypos 410
        if mountainroad_firsttime and greenmountaintribe_firsttime:
            add "map/mapparts/mountainroadtogreenmountaintribe.png" xpos 1593 ypos 391
        if bogcrossroads_firsttime and bogroad_firsttime:
            add "map/mapparts/bogcrossroadstobogroad.png" xpos 787 ypos 276
        if bogroad_firsttime and peatfield_firsttime:
            add "map/mapparts/bogroadtopeatfield.png" xpos 831 ypos 277
        if whitemarshes_firsttime and peatfield_firsttime:
            add "map/mapparts/whitemarshestopeatfield.png" xpos 811 ypos 278
        if bogcrossroads_firsttime and vines_firsttime:
            add "map/mapparts/bogcrossroadstovines.png" xpos 752 ypos 304
        if vines_firsttime and whitemarshes_firsttime:
            add "map/mapparts/vinestowhitemarshes.png" xpos 752 ypos 304
        if shortcut_westernentrance_firsttime:
            add "map/mapparts/shortcut/westernentrance01.png" xpos 739 ypos 396
        if shortcut_ibex:
            add "map/mapparts/shortcut/westernentrance02.png" xpos 739 ypos 396
        if shortcut_deepforest_firsttime:
            add "map/mapparts/shortcut/deepforest01.png" xpos 883 ypos 428
        if shortcut_deepforest_babydragon:
            add "map/mapparts/shortcut/deepforest02.png" xpos 883 ypos 428
        if shortcut_deepforest_treant:
            add "map/mapparts/shortcut/deepforest03.png" xpos 883 ypos 428
        if shortcut_deepforest_frightape:
            add "map/mapparts/shortcut/deepforest04.png" xpos 883 ypos 428
        if shortcut_deepforest_fruitgrove:
            add "map/mapparts/shortcut/deepforest05.png" xpos 883 ypos 428
        if shortcut_cairn_firsttime:
            add "map/mapparts/shortcut/cairn01.png" xpos 965 ypos 461
        if shortcut_meadow_firsttime:
            add "map/mapparts/shortcut/cairn02.png" xpos 965 ypos 461
        if shortcut_banditshideout_road_firsttime:
            add "map/mapparts/shortcut/cairn03.png" xpos 965 ypos 461
        if shortcut_banditshideout_obstacle1:
            add "map/mapparts/shortcut/cairn04.png" xpos 965 ypos 461
        if shortcut_banditshideout_obstacle2:
            add "map/mapparts/shortcut/cairn05.png" xpos 965 ypos 461
        if shortcut_woodenroad_firsttime:
            add "map/mapparts/shortcut/woodenroad01.png" xpos 1036 ypos 490
        if shortcut_woodenroad_stoathunt:
            add "map/mapparts/shortcut/woodenroad02.png" xpos 1036 ypos 490
        if shortcut_woodenroad_fisheater:
            add "map/mapparts/shortcut/woodenroad03.png" xpos 1036 ypos 490
        if shortcut_woodenroad_horseaccident:
            add "map/mapparts/shortcut/woodenroad04.png" xpos 1036 ypos 490
        if shortcut_woodenroad_drinkingcat:
            add "map/mapparts/shortcut/woodenroad05.png" xpos 1036 ypos 490
        if shortcut_darkforest_firsttime:
            add "map/mapparts/shortcut/darkforest01.png" xpos 1130 ypos 515
        if shortcut_darkforest_bandit:
            add "map/mapparts/shortcut/darkforest02.png" xpos 1130 ypos 515
        if shortcut_darkforest_goblins:
            add "map/mapparts/shortcut/darkforest03.png" xpos 1130 ypos 515
        if shortcut_darkforest_bagontree:
            add "map/mapparts/shortcut/darkforest04.png" xpos 1130 ypos 515
        if shortcut_darkforest_birdfollower:
            add "map/mapparts/shortcut/darkforest05.png" xpos 1130 ypos 515
        if shortcut_easternentrance_firsttime:
            add "map/mapparts/shortcut/easternentrance01.png" xpos 1232 ypos 541
        if shortcut_easternentrance_gnolls:
            add "map/mapparts/shortcut/easternentrance02.png" xpos 1232 ypos 541

        # if (peltnorth_firsttime and persistent.tutorial_display) or (peltnorth_firsttime and persistent.tutorial_display) or not persistent.tutorial_display:
        vbox:
            xpos 21
            ypos 1058
            if persistent.textstyle == "basic":
                spacing 16
            if persistent.textstyle == "pixel":
                spacing 12
            xalign 0.0
            yalign 1.0
            if not showmapkey:
                hbox:
                    xpos 70
                    textbutton "Show Map Key":
                        action SetVariable("showmapkey", 1)
                        text_style "tutorial_button_text"
                        text_slow_cps False
                        if persistent.textstyle == "basic":
                            text_size 24
                        if persistent.textstyle == "pixel":
                            text_size 28
                    null height 10
            else:
                hbox:
                    xpos 107
                    textbutton "Map Key":
                        action SetVariable("showmapkey", 0)
                        text_style "tutorial_button_text"
                        text_slow_cps False
                        if persistent.textstyle == "basic":
                            text_size 24
                        if persistent.textstyle == "pixel":
                            text_size 28
                    null height 10
                hbox:
                    spacing 32
                    add "mapkeyx3shelter":
                        yalign 0.5
                    text "Nighttime shelter.":
                        yalign 0.5
                        if persistent.textstyle == "basic":
                            size 24
                        if persistent.textstyle == "pixel":
                            size 28
                if (peltnorth_firsttime and peltnorth_resting) or (howlersdell_firsttime and howlersdell_eryx_about_room) or (foggylake_firsttime and foggy_about_shelter):
                    hbox:
                        spacing 32
                        add "mapkeyx3dayrest":
                            yalign 0.5
                        text "Daytime rest.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (southerncrossroads_firsttime and day >= southerncrossroads_wildplants_start and southerncrossroads_wildplants_left) or (peltnorth_firsttime and iason_shop) or (peltnorth_firsttime and iason_food_berries == 2) or (howlersdell_firsttime and howlersdell_eryx_about_shop) or (bogentrance_firsttime and day >= 5) or (galerocks_firsttime and galerocks_porcia_firsttime) or (watchtower_firsttime and day >= watchtower_wildplants_start and watchtower_wildplants_left) or (ghoulcave_firsttime and ghoulcave_wildplants_left) or (foragingground_firsttime and foragingground_foraging_amount < 4) or (foggylake_firsttime and foggy_about_trade) or (creeks_firsttime and oldhava_about_trade):
                    hbox:
                        spacing 32
                        add "mapkeyx3food":
                            yalign 0.5
                        text "Meals or supplies.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (peltnorth_firsttime and iason_shop) or (peltnorth_firsttime and peltnorth_selling) or (howlersdell_firsttime or akakios_shop_firsttime) or (peatfield_firsttime or thyrsus_shop) or (galerocks_firsttime or galerocks_tatius_firsttime) or (eudocia_firsttime or eudocia_about_selling) or (greenmountaintribe_firsttime and cephasgaiane_shop and not cephasgaiane_shop_dragonhorn) or (foggylake_firsttime and foggy_about_trade):
                    hbox:
                        spacing 32
                        add "mapkeyx3goods":
                            yalign 0.5
                        text "Trader.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (peltnorth_firsttime and peltnorth_armorer_abouttrade) or (howlersdell_firsttime and howlersdell_bion_shop) or (galerocks_firsttime and galerocks_rufina_firsttime):
                    hbox:
                        spacing 32
                        add "mapkeyx3tailor":
                            yalign 0.5
                        text "Tailor.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (beach_firsttime and galerocks_photios_about_mundanejob) or (creeks_firsttime and creeks_mundanework) or (howlersdell_mundanework_available and not howlersdell_mundanework_blocked):
                    hbox:
                        spacing 32
                        add "mapkeyx3mundanejob":
                            yalign 0.5
                        text "Mundane job.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (peltnorth_firsttime) or (ruinedvillage_firsttime and ruinedvillage_part_river) or (fishinghamlet_firsttime and fishinghamlet_areas_seen_07) or (galerocks_firsttime and galerocks_aquila_firsttime) or (beach_firsttime) or (fallentree_firsttime) or (ghoulcave_firsttime) or (wanderer_firsttime) or (creeks_firsttime):
                    hbox:
                        spacing 32
                        add "mapkeyx3watersource":
                            yalign 0.5
                        text "Safe water source.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (ruinedvillage_firsttime and ruinedvillage_part_river) or (northernroad_firsttime) or (fallentree_firsttime) or (ghoulcave_firsttime and map_icon3) or (wanderer_firsttime):
                    hbox:
                        spacing 32
                        add "mapkeyx3fishingspot":
                            yalign 0.5
                        text "Fishing spot.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
        if persistent.demomode and beholder_firsttime and watchtower_firsttime and druidcave_firsttime:
            frame:
                yalign 0.5
                xalign 0.5
                xpadding 16
                xpos 960
                ypos 440
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text "Most quests require a further journey to be completed,\nbut you’ve already explored every area that’s a part of this demo.\nThank you for your support!" text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text "Most quests require a further journey to be completed,\nbut you’ve already explored every area that’s a part of this demo.\nThank you for your support!" text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        if persistent.tutorial_display:
            if tutorial_endgame:
                frame:
                    style "tutorial_frame"
                    ypos 900
                    xalign 0.0
                    if persistent.textstyle == "basic":
                        xpos 1166
                    if persistent.textstyle == "pixel":
                        xpos 1166
                    textbutton "Travel forward to continue your journey.\n\nOnce you’re done with the North,\nspeak with Tulia to return to Hovlavan.":
                        action SetVariable("tutorial_endgame", 0)
                        text_style "tutorial_button"
                        text_slow_cps True
        if prologuemilitarycamp_unlocked:
            $ hours_militarycamp01 = (tomilitarycamp / 4) % 24
            $ quarters_militarycamp01 = (tomilitarycamp * 15) % 60
            $ travel_duration_militarycamp01 = ("%d:%02d" % (hours_militarycamp01, quarters_militarycamp01))
            imagebutton:
                focus_mask None
                xpos 1096
                ypos 968
                xalign 0.0
                yalign 0.0
                if pc_area == "militarycamp":
                    if militarycamp_destroyed_firsttime:
                        idle "map/militarycampmap02hover.png"
                        hover "map/militarycampmap02hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Camp{/color}\n{image=mapkeyx2shelter}\nA ruined outpost,\nreclaimed by beasts.\nYou’re currently here."), SetVariable("mapxframe", 1170), SetVariable("mapyframe", 970)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "map/militarycampmap01hover.png"
                        hover "map/militarycampmap01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}Tulia’s Camp{/color}\n{image=mapkeyx2shelter}\nA military outpost surrounded by a wooden wall,\nset in the middle of the valley.\nYou’re currently here."), SetVariable("mapxframe", 1170), SetVariable("mapyframe", 970)]
                        action [Hide("map_display", transition=dissolve)]
                elif militarycamp_destroyed_firsttime:
                    idle "map/militarycampmap02LOCKED.png"
                    hover "map/militarycampmap02hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Camp{/color}\n{image=mapkeyx2shelter}\nA ruined outpost,\nreclaimed by beasts.\nThere’s nothing else to find here."), SetVariable("mapxframe", 1170), SetVariable("mapyframe", 970)]
                    action NullAction()
                elif highisland_journey_inprogress == 1:
                    idle "map/militarycampmap01LOCKED.png"
                    hover "map/militarycampmap01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Tulia’s Camp{/color}\n{image=mapkeyx2shelter}\nA military outpost surrounded by a wooden wall,\nset in the middle of the valley.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1170), SetVariable("mapyframe", 970)]
                    action NullAction()
                elif tomilitarycamp >= 100:
                    idle "map/militarycampmap01LOCKED.png"
                    hover "map/militarycampmap01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Tulia’s Camp{/color}\n{image=mapkeyx2shelter}\nA military outpost surrounded by a wooden wall,\nset in the middle of the valley.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1170), SetVariable("mapyframe", 970)]
                    action NullAction()
                elif (quarters+tomilitarycamp) > world_daylength:
                    idle "map/militarycampmap01LOCKED.png"
                    hover "map/militarycampmap01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Tulia’s Camp{/color}\n{image=mapkeyx2shelter}\nA military outpost surrounded by a wooden wall,\nset in the middle of the valley.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_militarycamp01]"), SetVariable("mapxframe", 1170), SetVariable("mapyframe", 970)]
                    action NullAction()
                else:
                    idle "map/militarycampmap01.png"
                    hover "map/militarycampmap01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Tulia’s Camp{/color}\n{image=mapkeyx2shelter}\nA military outpost surrounded by a wooden wall,\nset in the middle of the valley.\nTravel time: [travel_duration_militarycamp01]"), SetVariable("mapxframe", 1170), SetVariable("mapyframe", 970)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "militarycamp"), Jump("finaldestination")]
            if pc_area == "militarycamp":
                add "map/flag.png" xpos 1068 ypos 970

        if southerncrossroads_unlocked and not southerncrossroads_firsttime:
            imagebutton:
                focus_mask None
                xpos 1108
                ypos 900
                xalign 0.0
                yalign 0.0
                if tosoutherncrossroads >= 100:
                    idle "images/map/arrows/upLOCKED.png"
                    hover "images/map/arrows/uphoverLOCKED.png"
                    hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1088), SetVariable("mapyframe", 932)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+tosoutherncrossroads) > (world_daylength-1):
                    idle "images/map/arrows/upLOCKED.png"
                    hover "images/map/arrows/uphoverLOCKED.png"
                    hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1088), SetVariable("mapyframe", 932)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/up.png"
                    hover "images/map/arrows/uphover.png"
                    hovered [tt3.Action("Travel north."), SetVariable("mapxframe", 1088), SetVariable("mapyframe", 932)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "southerncrossroads"), Jump("finaldestination")]
        elif southerncrossroads_firsttime:
            $ hours_southerncrossroads = (tosoutherncrossroads / 4) % 24
            $ quarters_southerncrossroads = (tosoutherncrossroads * 15) % 60
            $ travel_duration_southerncrossroads = ("%d:%02d" % (hours_southerncrossroads, quarters_southerncrossroads))
            if mapxframe == 1176:
                if day >= southerncrossroads_wildplants_start and southerncrossroads_wildplants_left:
                    $ map_icon1 = "{image=mapkeyx2food}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 1108
                ypos 878
                xalign 0.0
                yalign 0.0
                if pc_area == "southerncrossroads":
                    idle "map/crossroads01hover.png"
                    hover "map/crossroads01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Southern Crossroads{/color}\n[map_icon1]A point connecting the deep forests of the East,\nthe western wetlands, and the road to Hovlavan.\nYou’re currently here."), SetVariable("mapxframe", 1176), SetVariable("mapyframe", 906)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/crossroads01LOCKED.png"
                    hover "map/crossroads01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Southern Crossroads{/color}\n[map_icon1]A point connecting the deep forests of the East,\nthe western wetlands, and the road to Hovlavan.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1176), SetVariable("mapyframe", 906)]
                    action NullAction()
                elif tosoutherncrossroads >= 100:
                    idle "map/crossroads01LOCKED.png"
                    hover "map/crossroads01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Southern Crossroads{/color}\n[map_icon1]A point connecting the deep forests of the East,\nthe western wetlands, and the road to Hovlavan.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1176), SetVariable("mapyframe", 906)]
                    action NullAction()
                elif (quarters+tosoutherncrossroads) > world_daylength:
                    idle "map/crossroads01LOCKED.png"
                    hover "map/crossroads01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Southern Crossroads{/color}\n[map_icon1]A point connecting the deep forests of the East,\nthe western wetlands, and the road to Hovlavan.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_southerncrossroads]"), SetVariable("mapxframe", 1176), SetVariable("mapyframe", 906)]
                    action NullAction()
                else:
                    idle "map/crossroads01.png"
                    hover "map/crossroads01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Southern Crossroads{/color}\n[map_icon1]A point connecting the deep forests of the East,\nthe western wetlands, and the road to Hovlavan.\nTravel time: [travel_duration_southerncrossroads]"), SetVariable("mapxframe", 1176), SetVariable("mapyframe", 906)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "southerncrossroads"), Jump("finaldestination")]
            if pc_area == "southerncrossroads":
                add "map/flag.png" xpos 1090 ypos 882

        ########################################## WEST
        if peltnorth_unlocked and not peltnorth_firsttime:
            if (southerncrossroads_firsttime and ruinedvillage_firsttime and tosoutherncrossroads <= toruinedvillage) or (southerncrossroads_firsttime and not ruinedvillage_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1036
                    ypos 908
                    xalign 0.0
                    yalign 0.0
                    if topeltnorth >= 100:
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1020), SetVariable("mapyframe", 934)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+topeltnorth) > (world_daylength-1):
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1020), SetVariable("mapyframe", 934)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/left.png"
                        hover "images/map/arrows/lefthover.png"
                        if world_known_areas < 3:
                            hovered [tt3.Action("Explore west."), SetVariable("mapxframe", 1020), SetVariable("mapyframe", 934)]
                        else:
                            hovered [tt3.Action(""), SetVariable("mapxframe", 1020), SetVariable("mapyframe", 934)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "peltnorth"), Jump("finaldestination")]
            if (ruinedvillage_firsttime and southerncrossroads_firsttime and toruinedvillage <= tosoutherncrossroads) or (ruinedvillage_firsttime and not southerncrossroads_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 856
                    ypos 856
                    xalign 0.0
                    yalign 0.0
                    if topeltnorth >= 100:
                        idle "images/map/arrows/downrightLOCKED.png"
                        hover "images/map/arrows/downrighthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 912), SetVariable("mapyframe", 884)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+topeltnorth) > (world_daylength-1):
                        idle "images/map/arrows/downrightLOCKED.png"
                        hover "images/map/arrows/downrighthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 912), SetVariable("mapyframe", 884)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/downright.png"
                        hover "images/map/arrows/downrighthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 912), SetVariable("mapyframe", 884)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "peltnorth"), Jump("finaldestination")]
        elif peltnorth_firsttime:
            $ hours_peltnorth = (topeltnorth / 4) % 24
            $ quarters_peltnorth = (topeltnorth * 15) % 60
            $ travel_duration_peltnorth = ("%d:%02d" % (hours_peltnorth, quarters_peltnorth))
            if mapxframe == 1068:
                if peltnorth_resting:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                    $ map_icon2 = "{image=mapkeyx2dayrest} "
                else:
                    $ map_icon1 = ""
                    $ map_icon2 = ""
                if iason_shop or iason_food_berries == 2:
                    $ map_icon3 = "{image=mapkeyx2food} "
                else:
                    $ map_icon3 = ""
                if iason_shop or peltnorth_selling:
                    $ map_icon4 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon4 = ""
                if peltnorth_armorer_abouttrade:
                    $ map_icon5 = "{image=mapkeyx2tailor} "
                else:
                    $ map_icon5 = ""
                $ map_icon6 = "{image=mapkeyx2watersource}\n"
            imagebutton:
                focus_mask None
                xpos 988
                ypos 828
                xalign 0.0
                yalign 0.0
                if peltnorth_ban_temp == day:
                    idle "map/peltnorth01LOCKED.png"
                    hover "map/peltnorth01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Pelt of the North{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A massive inn surrounded by a firm wall.\nYou won’t be allowed to enter this place."), SetVariable("mapxframe", 1068), SetVariable("mapyframe", 866)]
                    action NullAction()
                elif peltnorth_ban_perm:
                    idle "map/peltnorth01LOCKED.png"
                    hover "map/peltnorth01hoverLOCKED.png"
                    hovered [tt.Action("You are banned from visiting {color=#f6d6bd}Pelt of the North{/color}."), SetVariable("mapxframe", 1068), SetVariable("mapyframe", 866)]
                    action NullAction()
                elif pc_area == "peltnorth":
                    idle "map/peltnorth01hover.png"
                    hover "map/peltnorth01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Pelt of the North{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A massive inn surrounded by a wall.\nA shelter from monsters and highwaymen.\nYou’re currently here."), SetVariable("mapxframe", 1068), SetVariable("mapyframe", 866)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/peltnorth01LOCKED.png"
                    hover "map/peltnorth01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Pelt of the North{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A massive inn surrounded by a wall.\nA shelter from monsters and highwaymen.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1068), SetVariable("mapyframe", 866)]
                    action NullAction()
                elif topeltnorth >= 100:
                    idle "map/peltnorth01LOCKED.png"
                    hover "map/peltnorth01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Pelt of the North{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A massive inn surrounded by a wall.\nA shelter from monsters and highwaymen.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1068), SetVariable("mapyframe", 866)]
                    action NullAction()
                elif (quarters+topeltnorth) > world_daylength:
                    idle "map/peltnorth01LOCKED.png"
                    hover "map/peltnorth01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Pelt of the North{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A massive inn surrounded by a wall.\nA shelter from monsters and highwaymen.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_peltnorth]"), SetVariable("mapxframe", 1068), SetVariable("mapyframe", 866)]
                    action NullAction()
                else:
                    idle "map/peltnorth01.png"
                    hover "map/peltnorth01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Pelt of the North{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A massive inn surrounded by a wall.\nA shelter from monsters and highwaymen.\nTravel time: [travel_duration_peltnorth]"), SetVariable("mapxframe", 1068), SetVariable("mapyframe", 866)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "peltnorth"), Jump("finaldestination")]
            if pc_area == "peltnorth":
                add "map/flag.png" xpos 954 ypos 840

        if ruinedvillage_unlocked and not ruinedvillage_firsttime:
            if (peltnorth_firsttime and beholder_firsttime and topeltnorth <= tobeholder) or (peltnorth_firsttime and not beholder_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 908
                    ypos 860
                    xalign 0.0
                    yalign 0.0
                    if toruinedvillage >= 100:
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 900), SetVariable("mapyframe", 883)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+toruinedvillage) > (world_daylength-1):
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 900), SetVariable("mapyframe", 883)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/left.png"
                        hover "images/map/arrows/lefthover.png"
                        hovered [tt3.Action(""), SetVariable("mapxframe", 900), SetVariable("mapyframe", 883)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ruinedvillage"), Jump("finaldestination")]
            if (beholder_firsttime and peltnorth_firsttime and tobeholder <= topeltnorth) or (beholder_firsttime and not peltnorth_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 700
                    ypos 768
                    xalign 0.0
                    yalign 0.0
                    if toruinedvillage >= 100:
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 764), SetVariable("mapyframe", 792)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+toruinedvillage) > (world_daylength-1):
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 772), SetVariable("mapyframe", 800)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/right.png"
                        hover "images/map/arrows/righthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 772), SetVariable("mapyframe", 800)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ruinedvillage"), Jump("finaldestination")]
        elif ruinedvillage_firsttime:
            $ hours_ruinedvillage01 = (toruinedvillage / 4) % 24
            $ quarters_ruinedvillage01 = (toruinedvillage * 15) % 60
            $ travel_duration_ruinedvillage01 = ("%d:%02d" % (hours_ruinedvillage01, quarters_ruinedvillage01))
            if mapxframe == 883:
                if ruinedvillage_part_river:
                    $ map_icon1 = "{image=mapkeyx2watersource} {image=mapkeyx2fishingspot}\n"
                else:
                    $ map_icon1 = ""
            if dalit_about_goblins_timer and dalit_about_goblins_timer >= day:
                $ dalit_about_goblins_timer_display = (dalit_about_goblins_timer-day+1)
            imagebutton:
                focus_mask None
                xpos 811
                ypos 792
                xalign 0.0
                yalign 0.0
                if dalit_about_goblins_timer and dalit_about_goblins_timer >= day:
                    idle "map/ruinedvillage01LOCKED.png"
                    hover "map/ruinedvillage01hoverLOCKED.png"
                    if dalit_about_goblins_timer_display == 1:
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\nYou should stay away for [dalit_about_goblins_timer_display] more day\nwhile the hunters are on the job."), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\nYou should stay away for [dalit_about_goblins_timer_display] more days\nwhile the hunters are on the job."), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                    action NullAction()
                    if pc_area == "ruinedvillage":
                        idle "map/ruinedvillage01hover.png"
                        hover "map/ruinedvillage01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\nA once prosperous village,\nnow abandoned and full of debris.\nYou’re currently here."), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action [Hide("map_display", transition=dissolve)]
                elif ruinedvillage_part_topentrance_EXPLORED and ruinedvillage_part_bottomentrance_EXPLORED and not ruinedvillage_part_topentrance_gate_open:
                    if pc_area == "ruinedvillage":
                        idle "map/ruinedvillage01hover.png"
                        hover "map/ruinedvillage01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\nYou’re currently here."), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/ruinedvillage01LOCKED.png"
                        hover "map/ruinedvillage01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\nThe closed gate will slow you down.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action NullAction()
                    elif toruinedvillage >= 100:
                        idle "map/ruinedvillage01LOCKED.png"
                        hover "map/ruinedvillage01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action NullAction()
                    elif (quarters+toruinedvillage) > world_daylength:
                        idle "map/ruinedvillage01LOCKED.png"
                        hover "map/ruinedvillage01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\nThe closed gate will slow you down.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_ruinedvillage01]"), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action NullAction()
                    else:
                        idle "map/ruinedvillage01.png"
                        hover "map/ruinedvillage01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\nTravel time: [travel_duration_ruinedvillage01]"), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ruinedvillage"), Jump("finaldestination")]
                else:
                    if pc_area == "ruinedvillage":
                        idle "map/ruinedvillage01hover.png"
                        hover "map/ruinedvillage01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\nYou’re currently here."), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/ruinedvillage01LOCKED.png"
                        hover "map/ruinedvillage01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action NullAction()
                    elif toruinedvillage >= 100:
                        idle "map/ruinedvillage01LOCKED.png"
                        hover "map/ruinedvillage01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action NullAction()
                    elif (quarters+toruinedvillage) > world_daylength:
                        idle "map/ruinedvillage01LOCKED.png"
                        hover "map/ruinedvillage01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\nA once prosperous village,\nnow abandoned and full of debris.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_ruinedvillage01]"), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action NullAction()
                    else:
                        idle "map/ruinedvillage01.png"
                        hover "map/ruinedvillage01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\nTravel time: [travel_duration_ruinedvillage01]"), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ruinedvillage"), Jump("finaldestination")]
            if pc_area == "ruinedvillage":
                add "map/flag.png" xpos 780 ypos 800

        if beholder_unlocked and not beholder_firsttime:
            if (ruinedvillage_firsttime and howlersdell_firsttime and toruinedvillage <= tohowlersdell) or (ruinedvillage_firsttime and not howlersdell_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 744
                    ypos 776
                    xalign 0.0
                    yalign 0.0
                    if tobeholder >= 100:
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 736), SetVariable("mapyframe", 800)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tobeholder) > (world_daylength-1):
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 736), SetVariable("mapyframe", 800)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/left.png"
                        hover "images/map/arrows/lefthover.png"
                        hovered [tt3.Action(""), SetVariable("mapxframe", 736), SetVariable("mapyframe", 800)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "beholder"), Jump("finaldestination")]
            if (howlersdell_firsttime and ruinedvillage_firsttime and tohowlersdell <= toruinedvillage) or (howlersdell_firsttime and not ruinedvillage_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 598
                    ypos 668
                    xalign 0.0
                    yalign 0.0
                    if tobeholder >= 100:
                        idle "images/map/arrows/downLOCKED.png"
                        hover "images/map/arrows/downhoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 580), SetVariable("mapyframe", 688)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tobeholder) > (world_daylength-1):
                        idle "images/map/arrows/downLOCKED.png"
                        hover "images/map/arrows/downhoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 580), SetVariable("mapyframe", 688)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/down.png"
                        hover "images/map/arrows/downhover.png"
                        hovered [tt3.Action(""), SetVariable("mapxframe", 580), SetVariable("mapyframe", 688)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "beholder"), Jump("finaldestination")]
        elif beholder_firsttime:
            $ hours_beholder01 = (tobeholder / 4) % 24
            $ quarters_beholder01 = (tobeholder * 15) % 60
            $ travel_duration_beholder01 = ("%d:%02d" % (hours_beholder01, quarters_beholder01))
            imagebutton:
                focus_mask None
                xpos 598
                ypos 728
                xalign 0.0
                yalign 0.0
                if beholder_destroyed:
                    idle "map/beholder01LOCKED.png"
                    hover "map/beholder01hoverLOCKED.png"
                    if beholder_name_known:
                        hovered [tt.Action("{color=#f6d6bd}Beholder{/color}\nA place where a large, unusual tree\nused to grow."), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}The Large Tree{/color}\nA place where a large, unusual plant\nused to grow."), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    action NullAction()
                elif pc_area == "beholder":
                    idle "map/beholder01hover.png"
                    hover "map/beholder01hover.png"
                    if beholder_name_known:
                        hovered [tt.Action("{color=#f6d6bd}Beholder{/color}\nA large tree and a stone altar\nat the edge of the swamp.\nYou’re currently here."), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}The Large Tree{/color}\nA massive plant with no leaves\ngrowing near an altar.\nYou’re currently here."), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/beholder01LOCKED.png"
                    hover "map/beholder01hoverLOCKED.png"
                    if beholder_name_known:
                        hovered [tt.Action("{color=#f6d6bd}Beholder{/color}\nA large tree and a stone altar\nat the edge of the swamp.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    else:
                        hovered [tt.Action("A large tree at the edge of the swamp.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    action NullAction()
                elif tobeholder >= 100:
                    idle "map/beholder01LOCKED.png"
                    hover "map/beholder01hoverLOCKED.png"
                    if beholder_name_known:
                        hovered [tt.Action("{color=#f6d6bd}Beholder{/color}\nA large tree and a stone altar\nat the edge of the swamp.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    else:
                        hovered [tt.Action("A large tree at the edge of the swamp.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    action NullAction()
                elif (quarters+tobeholder) > world_daylength:
                    idle "map/beholder01LOCKED.png"
                    hover "map/beholder01hoverLOCKED.png"
                    if beholder_name_known:
                        hovered [tt.Action("{color=#f6d6bd}Beholder{/color}\nA large tree and a stone altar\nat the edge of the swamp.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_beholder01]"), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    else:
                        hovered [tt.Action("A large tree at the edge of the swamp.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_beholder01]"), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    action NullAction()
                else:
                    idle "map/beholder01.png"
                    hover "map/beholder01hover.png"
                    if beholder_name_known:
                        hovered [tt.Action("{color=#f6d6bd}Beholder{/color}\nA large tree and a stone altar\nat the edge of the swamp.\nTravel time: [travel_duration_beholder01]"), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}The Large Tree{/color}\nA massive plant with no leaves\ngrowing near an altar.\nTravel time: [travel_duration_beholder01]"), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "beholder"), Jump("finaldestination")]
            if pc_area == "beholder":
                add "map/flag.png" xpos 570 ypos 720

        if druidcave_unlocked and not druidcave_firsttime:
            imagebutton:
                focus_mask None
                xpos 632
                ypos 816
                xalign 0.0
                yalign 0.0
                if todruidcave >= 100:
                    idle "images/map/arrows/downLOCKED.png"
                    hover "images/map/arrows/downhoverLOCKED.png"
                    hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 620), SetVariable("mapyframe", 840)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+todruidcave) > (world_daylength-1):
                    idle "images/map/arrows/downLOCKED.png"
                    hover "images/map/arrows/downhoverLOCKED.png"
                    hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 620), SetVariable("mapyframe", 840)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/down.png"
                    hover "images/map/arrows/downhover.png"
                    hovered [tt3.Action(""), SetVariable("mapxframe", 620), SetVariable("mapyframe", 840)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "druidcave"), Jump("finaldestination")]
        elif druidcave_firsttime:
            $ hours_druidcave = (todruidcave / 4) % 24
            $ quarters_druidcave = (todruidcave * 15) % 60
            $ travel_duration_druidcave = ("%d:%02d" % (hours_druidcave, quarters_druidcave))
            if mapxframe == 634:
                if druidcave_cave_open:
                    $ map_icon1 = "{image=mapkeyx2shelter}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 562
                ypos 810
                xalign 0.0
                yalign 0.0
                if druidcave_banned == "druidcave":
                    idle "map/druidcaveLOCKED.png"
                    hover "map/druidcavehoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Elders’ Cave{/color}\n[map_icon1]An old mine turned into a hamlet.\nIt’s surrounded by\ndozens of wild beasts."), SetVariable("mapxframe", 634), SetVariable("mapyframe", 850)]
                    action NullAction()
                elif pc_area == "druidcave":
                    idle "map/druidcavehover.png"
                    hover "map/druidcavehover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Elders’ Cave{/color}\n[map_icon1]An old mine turned into a hamlet\nprotected by a metal door.\nYou’re currently here."), SetVariable("mapxframe", 634), SetVariable("mapyframe", 850)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/druidcaveLOCKED.png"
                    hover "map/druidcavehoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Elders’ Cave{/color}\n[map_icon1]An old mine turned into a hamlet\nprotected by a metal door.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 634), SetVariable("mapyframe", 850)]
                    action NullAction()
                elif todruidcave >= 100:
                    idle "map/druidcaveLOCKED.png"
                    hover "map/druidcavehoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Elders’ Cave{/color}\n[map_icon1]An old mine turned into a hamlet\nprotected by a metal door.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 634), SetVariable("mapyframe", 850)]
                    action NullAction()
                elif (quarters+todruidcave) > world_daylength:
                    idle "map/druidcaveLOCKED.png"
                    hover "map/druidcavehoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Elders’ Cave{/color}\n[map_icon1]An old mine turned into a hamlet\nprotected by a metal door.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_druidcave]"), SetVariable("mapxframe", 634), SetVariable("mapyframe", 850)]
                    action NullAction()
                else:
                    idle "map/druidcave.png"
                    hover "map/druidcavehover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Elders’ Cave{/color}\n[map_icon1]An old mine turned into a hamlet\nprotected by a metal door.\nTravel time: [travel_duration_druidcave]"), SetVariable("mapxframe", 634), SetVariable("mapyframe", 850)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "druidcave"), Jump("finaldestination")]
            if pc_area == "druidcave":
                add "map/flag.png" xpos 540 ypos 820

        if persistent.demomode and howlersdell_unlocked and not howlersdell_firsttime:
            imagebutton:
                focus_mask None
                xpos 648
                ypos 680
                xalign 0.0
                yalign 0.0
                idle "images/map/arrows/upLOCKED.png"
                hover "images/map/arrows/uphoverLOCKED.png"
                hovered [tt.Action("The way forward is\nnot available in the demo!"), SetVariable("mapxframe", 704), SetVariable("mapyframe", 710)]
                action NullAction()
        elif howlersdell_unlocked and not howlersdell_firsttime:
            if (beholder_firsttime and westerncrossroads_firsttime and tobeholder <= towesterncrossroads) or (beholder_firsttime and not westerncrossroads_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 648
                    ypos 680
                    xalign 0.0
                    yalign 0.0
                    if tohowlersdell >= 100:
                        idle "images/map/arrows/upLOCKED.png"
                        hover "images/map/arrows/uphoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 704), SetVariable("mapyframe", 710)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tohowlersdell) > (world_daylength-1):
                        idle "images/map/arrows/upLOCKED.png"
                        hover "images/map/arrows/uphoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 704), SetVariable("mapyframe", 710)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/up.png"
                        hover "images/map/arrows/uphover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 704), SetVariable("mapyframe", 710)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "howlersdell"), Jump("finaldestination")]
            if (westerncrossroads_firsttime and beholder_firsttime and towesterncrossroads <= tobeholder) or (westerncrossroads_firsttime and not beholder_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 668
                    ypos 536
                    xalign 0.0
                    yalign 0.0
                    if tohowlersdell >= 100:
                        idle "images/map/arrows/downLOCKED.png"
                        hover "images/map/arrows/downhoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 644), SetVariable("mapyframe", 560)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tohowlersdell) > (world_daylength-1):
                        idle "images/map/arrows/downLOCKED.png"
                        hover "images/map/arrows/downhoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 664), SetVariable("mapyframe", 542)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/down.png"
                        hover "images/map/arrows/downhover.png"
                        hovered [tt3.Action(""), SetVariable("mapxframe", 664), SetVariable("mapyframe", 542)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "howlersdell"), Jump("finaldestination")]
        elif howlersdell_firsttime:
            $ hours_howlersdell = (tohowlersdell / 4) % 24
            $ quarters_howlersdell = (tohowlersdell * 15) % 60
            $ travel_duration_howlersdell = ("%d:%02d" % (hours_howlersdell, quarters_howlersdell))
            if mapxframe == 700:
                if howlersdell_eryx_about_room:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                    $ map_icon2 = "{image=mapkeyx2dayrest} "
                else:
                    $ map_icon1 = ""
                    $ map_icon2 = ""
                if howlersdell_eryx_about_shop:
                    $ map_icon3 = "{image=mapkeyx2food} "
                else:
                    $ map_icon3 = ""
                if akakios_shop_firsttime:
                    $ map_icon4 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon4 = ""
                if howlersdell_bion_shop:
                    $ map_icon5 = "{image=mapkeyx2tailor} "
                else:
                    $ map_icon5 = ""
                if (howlersdell_mundanework_available and not howlersdell_mundanework_blocked):
                    $ map_icon7 = "{image=mapkeyx2mundanejob} "
                else:
                    $ map_icon7 = ""
                if howlersdell_eryx_about_room or howlersdell_eryx_about_shop or akakios_shop_firsttime or howlersdell_bion_shop or (howlersdell_mundanework_available and not howlersdell_mundanework_blocked):
                    $ map_icon6 = "\n"
                else:
                    $ map_icon6 = ""
            imagebutton:
                focus_mask None
                xpos 626
                ypos 583
                xalign 0.0
                yalign 0.0
                if pc_area == "howlersdell":
                    idle "map/howlersdell01hover.png"
                    hover "map/howlersdell01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Howler’s Dell{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon7][map_icon6]A prosperous village of farmers\nand animal breeders.\nYou’re currently here."), SetVariable("mapxframe", 700), SetVariable("mapyframe", 620)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/howlersdell01LOCKED.png"
                    hover "map/howlersdell01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Howler’s Dell{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon7][map_icon6]A prosperous village of farmers\nand animal breeders.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 700), SetVariable("mapyframe", 620)]
                    action NullAction()
                elif tohowlersdell >= 100:
                    idle "map/howlersdell01LOCKED.png"
                    hover "map/howlersdell01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Howler’s Dell{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon7][map_icon6]A prosperous village of farmers\nand animal breeders.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 700), SetVariable("mapyframe", 620)]
                    action NullAction()
                elif (quarters+tohowlersdell) > world_daylength:
                    idle "map/howlersdell01LOCKED.png"
                    hover "map/howlersdell01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Howler’s Dell{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon7][map_icon6]A prosperous village of farmers\nand animal breeders.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_howlersdell]"), SetVariable("mapxframe", 700), SetVariable("mapyframe", 620)]
                    action NullAction()
                else:
                    idle "map/howlersdell01.png"
                    hover "map/howlersdell01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Howler’s Dell{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon7][map_icon6]A prosperous village of farmers\nand animal breeders.\nTravel time: [travel_duration_howlersdell]"), SetVariable("mapxframe", 700), SetVariable("mapyframe", 620)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "howlersdell"), Jump("finaldestination")]
            if pc_area == "howlersdell":
                add "map/flag.png" xpos 599 ypos 590

        if rockslide_unlocked and not rockslide_firsttime and not pc_area == "rockslide_firstblockade":
            imagebutton:
                focus_mask None
                xpos 540
                ypos 540
                xalign 0.0
                yalign 0.0
                if torockslide >= 100:
                    idle "images/map/arrows/leftLOCKED.png"
                    hover "images/map/arrows/lefthoverLOCKED.png"
                    hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 528), SetVariable("mapyframe", 563)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+torockslide) > (world_daylength-1):
                    idle "images/map/arrows/leftLOCKED.png"
                    hover "images/map/arrows/lefthoverLOCKED.png"
                    hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 528), SetVariable("mapyframe", 563)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/left.png"
                    hover "images/map/arrows/lefthover.png"
                    hovered [tt3.Action(""), SetVariable("mapxframe", 564), SetVariable("mapyframe", 578)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "rockslide"), Jump("finaldestination")]
        elif (rockslide_firsttime and not rockslide_cleared) or (rockslide_firsttime and rockslide_cleared and pc_area == "rockslide"):
            $ hours_rockslide = (torockslide / 4) % 24
            $ quarters_rockslide = (torockslide * 15) % 60
            $ travel_duration_rockslide = ("%d:%02d" % (hours_rockslide, quarters_rockslide))
            imagebutton:
                focus_mask None
                xpos 492
                ypos 501
                xalign 0.0
                yalign 0.0
                if pc_area == "rockslide":
                    if not rockslide_cleared:
                        idle "map/rockslide01hover.png"
                        hover "map/rockslide01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}A Rockslide{/color}\nThe mountain pass leading to the sea,\nblocked by an earthquake.\nYou’re currently here."), SetVariable("mapxframe", 560), SetVariable("mapyframe", 530)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "map/rockslide02LOCKED.png"
                        hover "map/rockslide02hoverLOCKED.png"
                        hovered [tt.Action("A cleared mountain pass leading to the sea.\nYou’re currently here."), SetVariable("mapxframe", 560), SetVariable("mapyframe", 530)]
                        action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/rockslide01LOCKED.png"
                    hover "map/rockslide01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}A Rockslide{/color}\nThe mountain pass leading to the sea,\nblocked by an earthquake.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 560), SetVariable("mapyframe", 530)]
                    action NullAction()
                elif torockslide >= 100:
                    idle "map/rockslide01LOCKED.png"
                    hover "map/rockslide01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}A Rockslide{/color}\nThe mountain pass leading to the sea,\nblocked by an earthquake.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 560), SetVariable("mapyframe", 530)]
                    action NullAction()
                elif (quarters+torockslide) > world_daylength:
                    idle "map/rockslide01LOCKED.png"
                    hover "map/rockslide01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}A Rockslide{/color}\nThe mountain pass leading to the sea,\nblocked by an earthquake.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_rockslide]"), SetVariable("mapxframe", 560), SetVariable("mapyframe", 530)]
                    action NullAction()
                else:
                    idle "map/rockslide01.png"
                    hover "map/rockslide01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}A Rockslide{/color}\nThe mountain pass leading to the sea,\nblocked by an earthquake.\nTravel time: [travel_duration_rockslide]"), SetVariable("mapxframe", 560), SetVariable("mapyframe", 530)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "rockslide"), Jump("finaldestination")]
            if pc_area == "rockslide":
                add "map/flag.png" xpos 458 ypos 504
        if pc_area == "rockslide2":
            add "map/flag.png" xpos 458 ypos 504
        if pc_area == "rockslide_firstblockade":
            add "map/flag.png" xpos 540 ypos 510

        if fishinghamlet_unlocked and not fishinghamlet_firsttime:
            imagebutton:
                focus_mask None
                xpos 420
                ypos 520
                xalign 0.0
                yalign 0.0
                if tofishinghamlet >= 100:
                    idle "images/map/arrows/leftLOCKED.png"
                    hover "images/map/arrows/lefthoverLOCKED.png"
                    hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 412), SetVariable("mapyframe", 542)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+tofishinghamlet) > (world_daylength-1):
                    idle "images/map/arrows/leftLOCKED.png"
                    hover "images/map/arrows/lefthoverLOCKED.png"
                    hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 412), SetVariable("mapyframe", 542)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/left.png"
                    hover "images/map/arrows/lefthover.png"
                    hovered [tt3.Action(""), SetVariable("mapxframe", 424), SetVariable("mapyframe", 542)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "fishinghamlet"), Jump("finaldestination")]
        elif fishinghamlet_firsttime:
            $ hours_fishinghamlet = (tofishinghamlet / 4) % 24
            $ quarters_fishinghamlet = (tofishinghamlet * 15) % 60
            $ travel_duration_fishinghamlet = ("%d:%02d" % (hours_fishinghamlet, quarters_fishinghamlet))
            if mapxframe == 440:
                if fishinghamlet_areas_seen_07:
                    $ map_icon1 = "{image=mapkeyx2watersource}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 366
                ypos 473
                xalign 0.0
                yalign 0.0
                if pc_area == "fishinghamlet":
                    idle "map/fishinghamlet01hover.png"
                    hover "map/fishinghamlet01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Fishing Hamlet{/color}\n[map_icon1]An abandoned settlement built\namong the coastal rocks.\nYou’re currently here."), SetVariable("mapxframe", 440), SetVariable("mapyframe", 500)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/fishinghamlet01LOCKED.png"
                    hover "map/fishinghamlet01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Fishing Hamlet{/color}\n[map_icon1]An abandoned settlement built\namong the coastal rocks.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 440), SetVariable("mapyframe", 500)]
                    action NullAction()
                elif tofishinghamlet >= 100:
                    idle "map/fishinghamlet01LOCKED.png"
                    hover "map/fishinghamlet01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Fishing Hamlet{/color}\n[map_icon1]An abandoned settlement built\namong the coastal rocks.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 440), SetVariable("mapyframe", 500)]
                    action NullAction()
                elif (quarters+tofishinghamlet) > world_daylength:
                    idle "map/fishinghamlet01LOCKED.png"
                    hover "map/fishinghamlet01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Fishing Hamlet{/color}\n[map_icon1]An abandoned settlement built\namong the coastal rocks.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_fishinghamlet]"), SetVariable("mapxframe", 440), SetVariable("mapyframe", 500)]
                    action NullAction()
                else:
                    idle "map/fishinghamlet01.png"
                    hover "map/fishinghamlet01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Fishing Hamlet{/color}\n[map_icon1]An abandoned settlement built\namong the coastal rocks.\nTravel time: [travel_duration_fishinghamlet]"), SetVariable("mapxframe", 440), SetVariable("mapyframe", 500)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "fishinghamlet"), Jump("finaldestination")]
            if pc_area == "fishinghamlet":
                add "map/flag.png" xpos 408 ypos 452

        if westerncrossroads_unlocked and not westerncrossroads_firsttime:
            if pc_area == "westgate":
                imagebutton:
                    focus_mask None
                    xpos 692
                    ypos 488
                    xalign 0.0
                    yalign 0.0
                    if towesterncrossroads >= 100:
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt2.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 732), SetVariable("mapyframe", 544)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+towesterncrossroads) > (world_daylength-1):
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt2.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 732), SetVariable("mapyframe", 544)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/left.png"
                        hover "images/map/arrows/lefthover.png"
                        hovered [tt2.Action(""), SetVariable("mapxframe", 732), SetVariable("mapyframe", 544)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "westerncrossroads"), Jump("finaldestination")]
            else:
                if (howlersdell_firsttime and ford_firsttime and tohowlersdell <= toford) or (howlersdell_firsttime and not ford_firsttime):
                    imagebutton:
                        focus_mask None
                        xpos 682
                        ypos 528
                        xalign 0.0
                        yalign 0.0
                        if towesterncrossroads >= 100:
                            idle "images/map/arrows/upLOCKED.png"
                            hover "images/map/arrows/uphoverLOCKED.png"
                            hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 740), SetVariable("mapyframe", 560)]
                            action [Hide("map_display", transition=dissolve)]
                        elif (quarters+towesterncrossroads) > (world_daylength-1):
                            idle "images/map/arrows/upLOCKED.png"
                            hover "images/map/arrows/uphoverLOCKED.png"
                            hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 740), SetVariable("mapyframe", 560)]
                            action [Hide("map_display", transition=dissolve)]
                        else:
                            idle "images/map/arrows/up.png"
                            hover "images/map/arrows/uphover.png"
                            hovered [tt.Action(""), SetVariable("mapxframe", 740), SetVariable("mapyframe", 560)]
                            action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "westerncrossroads"), Jump("finaldestination")]
                if (ford_firsttime and howlersdell_firsttime and toford <= tohowlersdell) or (ford_firsttime and not howlersdell_firsttime):
                    imagebutton:
                        focus_mask None
                        xpos 648
                        ypos 388
                        xalign 0.0
                        yalign 0.0
                        if towesterncrossroads >= 100:
                            idle "images/map/arrows/downLOCKED.png"
                            hover "images/map/arrows/downhoverLOCKED.png"
                            hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 712), SetVariable("mapyframe", 414)]
                            action [Hide("map_display", transition=dissolve)]
                        elif (quarters+towesterncrossroads) > (world_daylength-1):
                            idle "images/map/arrows/downLOCKED.png"
                            hover "images/map/arrows/downhoverLOCKED.png"
                            hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 712), SetVariable("mapyframe", 414)]
                            action [Hide("map_display", transition=dissolve)]
                        else:
                            idle "images/map/arrows/down.png"
                            hover "images/map/arrows/downhover.png"
                            hovered [tt.Action(""), SetVariable("mapxframe", 712), SetVariable("mapyframe", 414)]
                            action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "westerncrossroads"), Jump("finaldestination")]
        elif westerncrossroads_firsttime:
            $ hours_westerncrossroads = (towesterncrossroads / 4) % 24
            $ quarters_westerncrossroads = (towesterncrossroads * 15) % 60
            $ travel_duration_westerncrossroads = ("%d:%02d" % (hours_westerncrossroads, quarters_westerncrossroads))
            imagebutton:
                focus_mask None
                xpos 662
                ypos 451
                xalign 0.0
                yalign 0.0
                if pc_area == "westerncrossroads":
                    idle "map/westerncrossroads01hover.png"
                    hover "map/westerncrossroads01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Western Crossroads{/color}\nA well-kept path connecting\nthe major villages of the peninsula.\nYou’re currently here."), SetVariable("mapxframe", 722), SetVariable("mapyframe", 490)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/westerncrossroads01LOCKED.png"
                    hover "map/westerncrossroads01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Western Crossroads{/color}\nA well-kept path connecting\nthe major villages of the peninsula.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 722), SetVariable("mapyframe", 490)]
                    action NullAction()
                elif towesterncrossroads >= 100:
                    idle "map/westerncrossroads01LOCKED.png"
                    hover "map/westerncrossroads01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Western Crossroads{/color}\nA well-kept path connecting\nthe major villages of the peninsula.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 722), SetVariable("mapyframe", 490)]
                    action NullAction()
                elif (quarters+towesterncrossroads) > world_daylength:
                    idle "map/westerncrossroads01LOCKED.png"
                    hover "map/westerncrossroads01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Western Crossroads{/color}\nA well-kept path connecting\nthe major villages of the peninsula.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_westerncrossroads]"), SetVariable("mapxframe", 722), SetVariable("mapyframe", 490)]
                    action NullAction()
                else:
                    idle "map/westerncrossroads01.png"
                    hover "map/westerncrossroads01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Western Crossroads{/color}\nA well-kept path connecting\nthe major villages of the peninsula.\nTravel time: [travel_duration_westerncrossroads]"), SetVariable("mapxframe", 722), SetVariable("mapyframe", 490)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "westerncrossroads"), Jump("finaldestination")]
            if pc_area == "westerncrossroads":
                add "map/flag.png" xpos 645 ypos 460

        if oldpagos_unlocked and not oldpagos_firsttime:
            imagebutton:
                focus_mask None
                xpos 592
                ypos 472
                xalign 0.0
                yalign 0.0
                if not encounter_pebbler_gone and encounter_pebbler_day == day:
                    idle "images/map/arrows/leftLOCKED.png"
                    hover "images/map/arrows/lefthoverLOCKED.png"
                    hovered [tt3.Action("{color=#6a6a6a}This path is currently\nblocked by a pebbler.{/color}"), SetVariable("mapxframe", 580), SetVariable("mapyframe", 494)]
                    action NullAction()
                else:
                    if tooldpagos >= 100:
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 580), SetVariable("mapyframe", 494)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tooldpagos) > (world_daylength-1):
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 580), SetVariable("mapyframe", 494)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/left.png"
                        hover "images/map/arrows/lefthover.png"
                        hovered [tt3.Action(""), SetVariable("mapxframe", 580), SetVariable("mapyframe", 494)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "oldpagos"), Jump("finaldestination")]
        elif oldpagos_firsttime:
            $ hours_oldpagos = (tooldpagos / 4) % 24
            $ quarters_oldpagos = (tooldpagos * 15) % 60
            $ travel_duration_oldpagos = ("%d:%02d" % (hours_oldpagos, quarters_oldpagos))
            imagebutton:
                focus_mask None
                xpos 509
                ypos 364
                xalign 0.0
                yalign 0.0
                if not encounter_pebbler_gone and encounter_pebbler_day == day:
                    idle "map/oldpagos01LOCKED.png"
                    hover "map/oldpagos01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Old Págos{/color}\nA village of stonemasons and farmers\nset on the top of a hill,\nright near the sea.\n{color=#6a6a6a}The road there is currently blocked by a pebbler.{/color}"), SetVariable("mapxframe", 592), SetVariable("mapyframe", 400)]
                    action NullAction()
                else:
                    if pc_area == "oldpagos":
                        idle "map/oldpagos01hover.png"
                        hover "map/oldpagos01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}Old Págos{/color}\nA village of stonemasons and farmers\nset on the top of a hill,\nright near the sea.\nYou’re currently here."), SetVariable("mapxframe", 592), SetVariable("mapyframe", 400)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/oldpagos01LOCKED.png"
                        hover "map/oldpagos01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}Old Págos{/color}\nA village of stonemasons and farmers\nset on the top of a hill,\nright near the sea.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 592), SetVariable("mapyframe", 400)]
                        action NullAction()
                    elif tooldpagos >= 100:
                        idle "map/oldpagos01LOCKED.png"
                        hover "map/oldpagos01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}Old Págos{/color}\nA village of stonemasons and farmers\nset on the top of a hill,\nright near the sea.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 592), SetVariable("mapyframe", 400)]
                        action NullAction()
                    elif (quarters+tooldpagos) > world_daylength:
                        idle "map/oldpagos01LOCKED.png"
                        hover "map/oldpagos01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}Old Págos{/color}\nA village of stonemasons and farmers\nset on the top of a hill,\nright near the sea.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_oldpagos]"), SetVariable("mapxframe", 592), SetVariable("mapyframe", 400)]
                        action NullAction()
                    else:
                        idle "map/oldpagos01.png"
                        hover "map/oldpagos01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}Old Págos{/color}\nA village of stonemasons and farmers\nset on the top of a hill,\nright near the sea.\nTravel time: [travel_duration_oldpagos]"), SetVariable("mapxframe", 592), SetVariable("mapyframe", 400)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "oldpagos"), Jump("finaldestination")]
            if pc_area == "oldpagos":
                add "map/flag.png" xpos 480 ypos 370

        if monastery_unlocked and not monastery_firsttime:
            imagebutton:
                focus_mask None
                xpos 548
                ypos 324
                xalign 0.0
                yalign 0.0
                if not encounter_pebbler_gone and encounter_pebbler_day == day:
                    idle "images/map/arrows/upLOCKED.png"
                    hover "images/map/arrows/uphoverLOCKED.png"
                    hovered [tt.Action("{color=#6a6a6a}This path is currently blocked by a pebbler.{/color}"), SetVariable("mapxframe", 592), SetVariable("mapyframe", 400)]
                    action NullAction()
                else:
                    if tomonastery >= 100:
                        idle "images/map/arrows/upLOCKED.png"
                        hover "images/map/arrows/uphoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 604), SetVariable("mapyframe", 388)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tomonastery) > (world_daylength-1):
                        idle "images/map/arrows/upLOCKED.png"
                        hover "images/map/arrows/uphoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 604), SetVariable("mapyframe", 388)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/up.png"
                        hover "images/map/arrows/uphover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 604), SetVariable("mapyframe", 388)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "monastery"), Jump("finaldestination")]
        elif monastery_firsttime:
            $ hours_monastery = (tomonastery / 4) % 24
            $ quarters_monastery = (tomonastery * 15) % 60
            $ travel_duration_monastery = ("%d:%02d" % (hours_monastery, quarters_monastery))
            if mapxframe == 644:
                if monastery_sleep_unlocked:
                    $ map_icon1 = "{image=mapkeyx2shelter}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 568
                ypos 315
                xalign 0.0
                yalign 0.0
                if not encounter_pebbler_gone and encounter_pebbler_day == day:
                    idle "map/monastery01LOCKED.png"
                    hover "map/monastery01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}[monastery_name]{/color}\n[map_icon1]A hard-to-reach complex of caves\nturned into a dwelling by\nthe monks of an Order of Truth.\n{color=#6a6a6a}The road there is currently blocked by a pebbler.{/color}"), SetVariable("mapxframe", 644), SetVariable("mapyframe", 352)]
                    action NullAction()
                else:
                    if pc_area == "monastery":
                        idle "map/monastery01hover.png"
                        hover "map/monastery01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}[monastery_name]{/color}\n[map_icon1]A hard-to-reach complex of caves\nturned into a dwelling by\nthe monks of an Order of Truth.\nYou’re currently here."), SetVariable("mapxframe", 644), SetVariable("mapyframe", 352)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/monastery01LOCKED.png"
                        hover "map/monastery01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}[monastery_name]{/color}\n[map_icon1]A hard-to-reach complex of caves\nturned into a dwelling by\nthe monks of an Order of Truth.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 644), SetVariable("mapyframe", 352)]
                        action NullAction()
                    elif tomonastery >= 100:
                        idle "map/monastery01LOCKED.png"
                        hover "map/monastery01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}[monastery_name]{/color}\n[map_icon1]A hard-to-reach complex of caves\nturned into a dwelling by\nthe monks of an Order of Truth.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 644), SetVariable("mapyframe", 352)]
                        action NullAction()
                    elif (quarters+tomonastery) > world_daylength:
                        idle "map/monastery01LOCKED.png"
                        hover "map/monastery01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}[monastery_name]{/color}\n[map_icon1]A hard-to-reach complex of caves\nturned into a dwelling by\nthe monks of an Order of Truth.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_monastery]"), SetVariable("mapxframe", 644), SetVariable("mapyframe", 352)]
                        action NullAction()
                    else:
                        idle "map/monastery01.png"
                        hover "map/monastery01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}[monastery_name]{/color}\n[map_icon1]A hard-to-reach complex of caves\nturned into a dwelling by\nthe monks of an Order of Truth.\nTravel time: [travel_duration_monastery]"), SetVariable("mapxframe", 644), SetVariable("mapyframe", 352)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "monastery"), Jump("finaldestination")]
            if pc_area == "monastery":
                add "map/flag.png" xpos 578 ypos 335

        if westgate_unlocked and not westgate_firsttime:
            imagebutton:
                focus_mask None
                xpos 736
                ypos 488
                xalign 0.0
                yalign 0.0
                if towestgate >= 100:
                    idle "images/map/arrows/rightLOCKED.png"
                    hover "images/map/arrows/righthoverLOCKED.png"
                    hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 804), SetVariable("mapyframe", 512)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+towestgate) > (world_daylength-1):
                    idle "images/map/arrows/rightLOCKED.png"
                    hover "images/map/arrows/righthoverLOCKED.png"
                    hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 804), SetVariable("mapyframe", 512)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/right.png"
                    hover "images/map/arrows/righthover.png"
                    hovered [tt.Action(""), SetVariable("mapxframe", 804), SetVariable("mapyframe", 512)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "westgate"), Jump("finaldestination")]
        elif westgate_firsttime:
            $ hours_westgate = (towestgate / 4) % 24
            $ quarters_westgate = (towestgate * 15) % 60
            $ travel_duration_westgate = ("%d:%02d" % (hours_westgate, quarters_westgate))
            imagebutton:
                focus_mask None
                xpos 749
                ypos 454
                xalign 0.0
                yalign 0.0
                if pc_area == "westgate":
                    idle "map/westgate01hover.png"
                    hover "map/westgate01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Gate{/color}\nAn unusual structure guarding\nthe path to the heart of the forest.\nYou’re currently here."), SetVariable("mapxframe", 820), SetVariable("mapyframe", 490)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/westgate01LOCKED.png"
                    hover "map/westgate01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Gate{/color}\nAn unusual structure guarding\nthe path to the heart of the forest.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 820), SetVariable("mapyframe", 490)]
                    action NullAction()
                elif towestgate >= 100:
                    idle "map/westgate01LOCKED.png"
                    hover "map/westgate01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Gate{/color}\nAn unusual structure guarding\nthe path to the heart of the forest.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 820), SetVariable("mapyframe", 490)]
                    action NullAction()
                elif (quarters+towestgate) > world_daylength:
                    idle "map/westgate01LOCKED.png"
                    hover "map/westgate01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Gate{/color}\nAn unusual structure guarding\nthe path to the heart of the forest.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_westgate]"), SetVariable("mapxframe", 820), SetVariable("mapyframe", 490)]
                    action NullAction()
                else:
                    idle "map/westgate01.png"
                    hover "map/westgate01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Gate{/color}\nAn unusual structure guarding\nthe path to the heart of the forest.\nTravel time: [travel_duration_westgate]"), SetVariable("mapxframe", 820), SetVariable("mapyframe", 490)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "westgate"), Jump("finaldestination")]
            if pc_area == "westgate":
                add "map/flag.png" xpos 730 ypos 454

        if ford_unlocked and not ford_firsttime:
            if (westerncrossroads_firsttime and bogentrance_firsttime and towesterncrossroads <= tobogentrance) or (westerncrossroads_firsttime and not bogentrance_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 696
                    ypos 408
                    xalign 0.0
                    yalign 0.0
                    if toford >= 100:
                        idle "images/map/arrows/upLOCKED.png"
                        hover "images/map/arrows/uphoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 756), SetVariable("mapyframe", 440)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+toford) > (world_daylength-1):
                        idle "images/map/arrows/upLOCKED.png"
                        hover "images/map/arrows/uphoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 756), SetVariable("mapyframe", 440)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/up.png"
                        hover "images/map/arrows/uphover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 756), SetVariable("mapyframe", 440)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ford"), Jump("finaldestination")]
            if (bogentrance_firsttime and westerncrossroads_firsttime and tobogentrance <= towesterncrossroads) or (bogentrance_firsttime and not westerncrossroads_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 688
                    ypos 300
                    xalign 0.0
                    yalign 0.0
                    if toford >= 100:
                        idle "images/map/arrows/downleftLOCKED.png"
                        hover "images/map/arrows/downlefthoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 676), SetVariable("mapyframe", 320)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+toford) > (world_daylength-1):
                        idle "images/map/arrows/downleftLOCKED.png"
                        hover "images/map/arrows/downlefthoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 676), SetVariable("mapyframe", 320)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/downleft.png"
                        hover "images/map/arrows/downlefthover.png"
                        hovered [tt3.Action(""), SetVariable("mapxframe", 676), SetVariable("mapyframe", 320)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ford"), Jump("finaldestination")]
        elif ford_firsttime:
            $ hours_ford = (toford / 4) % 24
            $ quarters_ford = (toford * 15) % 60
            $ travel_duration_ford = ("%d:%02d" % (hours_ford, quarters_ford))
            imagebutton:
                focus_mask None
                xpos 646
                ypos 326
                xalign 0.0
                yalign 0.0
                if ford_insects_dealtwith:
                    if pc_area == "ford":
                        idle "map/ford01hover.png"
                        hover "map/ford01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons.\nYou’re currently here."), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/ford01LOCKED.png"
                        hover "map/ford01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                        action NullAction()
                    elif toford >= 100:
                        idle "map/ford01LOCKED.png"
                        hover "map/ford01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                        action NullAction()
                    elif (quarters+toford) > world_daylength:
                        idle "map/ford01LOCKED.png"
                        hover "map/ford01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_ford]"), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                        action NullAction()
                    else:
                        idle "map/ford01.png"
                        hover "map/ford01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons.\nTravel time: [travel_duration_ford]"), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ford"), Jump("finaldestination")]
                else:
                    if pc_area == "ford":
                        idle "map/ford01hover.png"
                        hover "map/ford01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons.\nThe insects are going to slow you down.\nYou’re currently here."), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/ford01LOCKED.png"
                        hover "map/ford01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons.\nThe insects are going to slow you down.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                        action NullAction()
                    elif toford >= 100:
                        idle "map/ford01LOCKED.png"
                        hover "map/ford01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons.\nThe insects are going to slow you down.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                        action NullAction()
                    elif (quarters+toford) > world_daylength:
                        idle "map/ford01LOCKED.png"
                        hover "map/ford01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons.\nThe insects are going to slow you down.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_ford]"), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                        action NullAction()
                    else:
                        idle "map/ford01.png"
                        hover "map/ford01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons.\nThe insects are going to slow you down.\nTravel time: [travel_duration_ford]"), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ford"), Jump("finaldestination")]
            if pc_area == "ford":
                add "map/flag.png" xpos 608 ypos 305

        if bogentrance_unlocked and not bogentrance_firsttime:
            if (ford_firsttime and ruinedshelter_firsttime and toford <= toruinedshelter) or (ford_firsttime and not ruinedshelter_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 685
                    ypos 296
                    xalign 0.0
                    yalign 0.0
                    if tobogentrance >= 100:
                        idle "images/map/arrows/uprightLOCKED.png"
                        hover "images/map/arrows/uprighthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 746), SetVariable("mapyframe", 316)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tobogentrance) > (world_daylength-1):
                        idle "images/map/arrows/uprightLOCKED.png"
                        hover "images/map/arrows/uprighthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 746), SetVariable("mapyframe", 316)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/upright.png"
                        hover "images/map/arrows/uprighthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 746), SetVariable("mapyframe", 316)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "bogentrance"), Jump("finaldestination")]
            if (ruinedshelter_firsttime and ford_firsttime and toruinedshelter <= toford) or (ruinedshelter_firsttime and not ford_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 800
                    ypos 232
                    xalign 0.0
                    yalign 0.0
                    if tobogentrance >= 100:
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 780), SetVariable("mapyframe", 255)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tobogentrance) > (world_daylength-1):
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 780), SetVariable("mapyframe", 255)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/left.png"
                        hover "images/map/arrows/lefthover.png"
                        hovered [tt3.Action(""), SetVariable("mapxframe", 780), SetVariable("mapyframe", 255)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "bogentrance"), Jump("finaldestination")]
        elif bogentrance_firsttime:
            $ hours_bogentrance = (tobogentrance / 4) % 24
            $ quarters_bogentrance = (tobogentrance * 15) % 60
            $ travel_duration_bogentrance = ("%d:%02d" % (hours_bogentrance, quarters_bogentrance))
            if mapxframe == 804:
                if day >= 5:
                    $ map_icon1 = "{image=mapkeyx2food}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 732
                ypos 238
                xalign 0.0
                yalign 0.0
                if pc_area == "bogentrance":
                    idle "map/bogentrance01hover.png"
                    hover "map/bogentrance01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Forest Garden{/color}\n[map_icon1]Once tamed part of the woods,\nnow neglected.\nYou’re currently here."), SetVariable("mapxframe", 804), SetVariable("mapyframe", 270)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/bogentrance01LOCKED.png"
                    hover "map/bogentrance01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Forest Garden{/color}\n[map_icon1]Once tamed part of the woods,\nnow neglected.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 804), SetVariable("mapyframe", 270)]
                    action NullAction()
                elif tobogentrance >= 100:
                    idle "map/bogentrance01LOCKED.png"
                    hover "map/bogentrance01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Forest Garden{/color}\n[map_icon1]Once tamed part of the woods,\nnow neglected.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 804), SetVariable("mapyframe", 270)]
                    action NullAction()
                elif (quarters+tobogentrance) > world_daylength:
                    idle "map/bogentrance01LOCKED.png"
                    hover "map/bogentrance01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Forest Garden{/color}\n[map_icon1]Once tamed part of the woods,\nnow neglected.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_bogentrance]"), SetVariable("mapxframe", 804), SetVariable("mapyframe", 270)]
                    action NullAction()
                else:
                    idle "map/bogentrance01.png"
                    hover "map/bogentrance01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Forest Garden{/color}\n[map_icon1]Once tamed part of the woods,\nnow neglected.\nTravel time: [travel_duration_bogentrance]"), SetVariable("mapxframe", 804), SetVariable("mapyframe", 270)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "bogentrance"), Jump("finaldestination")]
            if pc_area == "bogentrance":
                add "map/flag.png" xpos 686 ypos 226

        if bogcrossroads_unlocked and not bogcrossroads_firsttime:
            imagebutton:
                focus_mask None
                xpos 784
                ypos 308
                xalign 0.0
                yalign 0.0
                if tobogcrossroads >= 100:
                    idle "images/map/arrows/downrightLOCKED.png"
                    hover "images/map/arrows/downrighthoverLOCKED.png"
                    hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 840), SetVariable("mapyframe", 328)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+tobogcrossroads) > (world_daylength-2):
                    idle "images/map/arrows/downrightLOCKED.png"
                    hover "images/map/arrows/downrighthoverLOCKED.png"
                    hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 840), SetVariable("mapyframe", 328)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/downright.png"
                    hover "images/map/arrows/downrighthover.png"
                    hovered [tt.Action(""), SetVariable("mapxframe", 840), SetVariable("mapyframe", 328)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "bogcrossroads"), Jump("finaldestination")]
        if pc_area == "bogcrossroads":
            add "map/flag.png" xpos 780 ypos 262

        if bogroad_unlocked and not bogroad_firsttime:
            if (bogcrossroads_firsttime and peatfield_firsttime and tobogcrossroads <= topeatfield) or (bogcrossroads_firsttime and not peatfield_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 832
                    ypos 288
                    xalign 0.0
                    yalign 0.0
                    if tobogroad >= 100:
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 900), SetVariable("mapyframe", 312)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tobogroad) > (world_daylength-2):
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 900), SetVariable("mapyframe", 312)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/right.png"
                        hover "images/map/arrows/righthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 900), SetVariable("mapyframe", 312)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "bogroad"), Jump("finaldestination")]
        if pc_area == "bogroad":
            add "map/flag.png" xpos 830 ypos 264

        if peatfield_unlocked and not peatfield_firsttime:
            imagebutton:
                focus_mask None
                xpos 862
                ypos 330
                xalign 0.0
                yalign 0.0
                if topeatfield >= 100:
                    idle "images/map/arrows/rightLOCKED.png"
                    hover "images/map/arrows/righthoverLOCKED.png"
                    hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 928), SetVariable("mapyframe", 352)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+topeatfield) > (world_daylength-2):
                    idle "images/map/arrows/rightLOCKED.png"
                    hover "images/map/arrows/righthoverLOCKED.png"
                    hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 928), SetVariable("mapyframe", 352)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/right.png"
                    hover "images/map/arrows/righthover.png"
                    hovered [tt.Action(""), SetVariable("mapxframe", 928), SetVariable("mapyframe", 352)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "peatfield"), Jump("finaldestination")]
        elif peatfield_firsttime:
            $ hours_peatfield = (topeatfield / 4) % 24
            $ quarters_peatfield = (topeatfield * 15) % 60
            $ travel_duration_peatfield = ("%d:%02d" % (hours_peatfield, quarters_peatfield))
            if mapxframe == 950:
                if thyrsus_shop:
                    $ map_icon1 = "{image=mapkeyx2goods}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 878
                ypos 272
                xalign 0.0
                yalign 0.0
                if peatfield_firsttime_destroyed:
                    idle "map/peatfield01LOCKED.png"
                    hover "map/peatfield01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Peat Fields{/color}\nA peatland surrounded by bogs,\nabandoned and haunted."), SetVariable("mapxframe", 950), SetVariable("mapyframe", 298)]
                    action NullAction()
                elif pc_area == "peatfield":
                    idle "map/peatfield01hover.png"
                    hover "map/peatfield01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Peat Fields{/color}\n[map_icon1]A peatland surrounded by bogs.\nIt provides the locals with\nbricks and fuel.\nYou’re currently here."), SetVariable("mapxframe", 950), SetVariable("mapyframe", 298)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/peatfield01LOCKED.png"
                    hover "map/peatfield01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Peat Fields{/color}\n[map_icon1]A peatland surrounded by bogs.\nIt provides the locals with\nbricks and fuel.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 950), SetVariable("mapyframe", 298)]
                    action NullAction()
                elif topeatfield >= 100:
                    idle "map/peatfield01LOCKED.png"
                    hover "map/peatfield01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Peat Fields{/color}\n[map_icon1]A peatland surrounded by bogs.\nIt provides the locals with\nbricks and fuel.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 950), SetVariable("mapyframe", 298)]
                    action NullAction()
                elif (quarters+topeatfield) > (world_daylength-4):
                    idle "map/peatfield01LOCKED.png"
                    hover "map/peatfield01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Peat Fields{/color}\n[map_icon1]A peatland surrounded by bogs.\nIt provides the locals with\nbricks and fuel.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_peatfield]"), SetVariable("mapxframe", 950), SetVariable("mapyframe", 298)]
                    action NullAction()
                else:
                    idle "map/peatfield01.png"
                    hover "map/peatfield01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Peat Fields{/color}\n[map_icon1]A peatland surrounded by bogs.\nIt provides the locals with\nbricks and fuel.\nTravel time: [travel_duration_peatfield]"), SetVariable("mapxframe", 950), SetVariable("mapyframe", 298)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "peatfield"), Jump("finaldestination")]
            if pc_area == "peatfield":
                add "map/flag.png" xpos 861 ypos 274

        if vines_unlocked and not vines_firsttime:
            imagebutton:
                focus_mask None
                xpos 768
                ypos 332
                xalign 0.0
                yalign 0.0
                if towhitemarshes >= 100:
                    idle "images/map/arrows/downLOCKED.png"
                    hover "images/map/arrows/downhoverLOCKED.png"
                    hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 834), SetVariable("mapyframe", 337)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+towhitemarshes) > (world_daylength-2):
                    idle "images/map/arrows/downLOCKED.png"
                    hover "images/map/arrows/downhoverLOCKED.png"
                    hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 834), SetVariable("mapyframe", 337)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/down.png"
                    hover "images/map/arrows/downhover.png"
                    hovered [tt.Action(""), SetVariable("mapxframe", 834), SetVariable("mapyframe", 337)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "vines"), Jump("finaldestination")]
        elif vines_firsttime:
            $ hours_vines = (tovines / 4) % 24
            $ quarters_vines = (tovines * 15) % 60
            $ travel_duration_vines = ("%d:%02d" % (hours_vines, quarters_vines))
            imagebutton:
                focus_mask None
                xpos 770
                ypos 301
                xalign 0.0
                yalign 0.0
                if (vines_open_sleep or vines_open_day == day or vines_perma_open) and not vines_perma_closed:
                    if pc_area == "vines":
                        idle "map/vines02hover.png"
                        hover "map/vines02hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\nYou’re currently here."), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/vines02LOCKED.png"
                        hover "map/vines02hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action NullAction()
                    elif tovines >= 100:
                        idle "map/vines02LOCKED.png"
                        hover "map/vines02hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action NullAction()
                    elif (quarters+tovines) > (world_daylength-4):
                        idle "map/vines02LOCKED.png"
                        hover "map/vines02hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_vines]"), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action NullAction()
                    else:
                        idle "map/vines02.png"
                        hover "map/vines02hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\nTravel time: [travel_duration_vines]"), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "vines"), Jump("finaldestination")]
                else:
                    if pc_area == "vines":
                        idle "map/vines01hover.png"
                        hover "map/vines01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\nYou’re currently here."), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/vines01LOCKED.png"
                        hover "map/vines01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action NullAction()
                    elif tovines >= 100:
                        idle "map/vines01LOCKED.png"
                        hover "map/vines01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action NullAction()
                    elif (quarters+tovines) > (world_daylength-4):
                        idle "map/vines01LOCKED.png"
                        hover "map/vines01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_vines]"), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action NullAction()
                    else:
                        idle "map/vines01.png"
                        hover "map/vines01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\nTravel time: [travel_duration_vines]"), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "vines"), Jump("finaldestination")]
            if pc_area == "vines":
                add "map/flag.png" xpos 770 ypos 288

        if whitemarshes_unlocked and not whitemarshes_firsttime:
            imagebutton:
                focus_mask None
                xpos 811
                ypos 346
                xalign 0.0
                yalign 0.0
                if not vines_open_sleep and vines_open_day != day and not vines_perma_open:
                    idle "images/map/arrows/downrightLOCKED.png"
                    hover "images/map/arrows/downrighthoverLOCKED.png"
                    hovered [tt.Action("{color=#6a6a6a}You can’t get through the creepers.{/color}"), SetVariable("mapxframe", 872), SetVariable("mapyframe", 364)]
                    action NullAction()
                elif towhitemarshes >= 100:
                    idle "images/map/arrows/downrightLOCKED.png"
                    hover "images/map/arrows/downrighthoverLOCKED.png"
                    hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 872), SetVariable("mapyframe", 364)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+towhitemarshes) > (world_daylength-2):
                    idle "images/map/arrows/downrightLOCKED.png"
                    hover "images/map/arrows/downrighthoverLOCKED.png"
                    hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 872), SetVariable("mapyframe", 364)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/downright.png"
                    hover "images/map/arrows/downrighthover.png"
                    hovered [tt.Action(""), SetVariable("mapxframe", 872), SetVariable("mapyframe", 364)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "whitemarshes"), Jump("finaldestination")]
        elif whitemarshes_firsttime:
            $ hours_whitemarshes = (towhitemarshes / 4) % 24
            $ quarters_whitemarshes = (towhitemarshes * 15) % 60
            $ travel_duration_whitemarshes = ("%d:%02d" % (hours_whitemarshes, quarters_whitemarshes))
            if mapxframe == 840:
                if whitemarshes_rest_unlocked and not whitemarshes_attacked:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if helvius_about_buying and not whitemarshes_attacked:
                    $ map_icon2 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon2 = ""
                if (whitemarshes_rest_unlocked and not whitemarshes_attacked) or (helvius_about_buying and not whitemarshes_attacked):
                    $ map_icon3 = "\n"
                else:
                    $ map_icon3 = ""
            imagebutton:
                focus_mask None
                xpos 773
                ypos 346
                xalign 0.0
                yalign 0.0
                if whitemarshes_destroyed:
                    idle "map/whitemarshes02LOCKED.png"
                    hover "map/whitemarshes02hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Ruins of\nWhite Marshes{/color}\nOnce a struggling village,\nnow a lair of awoken shells,\nwaiting for their moment to strike."), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action NullAction()
                elif vines_perma_closed:
                    idle "map/whitemarshes01LOCKED.png"
                    hover "map/whitemarshes01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}White Marshes{/color}\n[map_icon1][map_icon2][map_icon3]A struggling village of\npeat gatherers and farmers,\nrecently thrown into chaos."), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action NullAction()
                elif not vines_open_sleep and vines_open_day != day and not vines_perma_open:
                    idle "map/whitemarshes01LOCKED.png"
                    hover "map/whitemarshes01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}White Marshes{/color}\n[map_icon1][map_icon2][map_icon3]A struggling village of\npeat gatherers and farmers.\n{color=#6a6a6a}You can’t get here while\nthe creepers block the way.{/color}\nTravel time: [travel_duration_whitemarshes]"), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action NullAction()
                elif pc_area == "whitemarshes":
                    idle "map/whitemarshes01hover.png"
                    hover "map/whitemarshes01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}White Marshes{/color}\n[map_icon1][map_icon2][map_icon3]A struggling village of\npeat gatherers and farmers.\nYou’re currently here."), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/whitemarshes01LOCKED.png"
                    hover "map/whitemarshes01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}White Marshes{/color}\n[map_icon1][map_icon2][map_icon3]A struggling village of\npeat gatherers and farmers.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action NullAction()
                elif towhitemarshes >= 100:
                    idle "map/whitemarshes01LOCKED.png"
                    hover "map/whitemarshes01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}White Marshes{/color}\n[map_icon1][map_icon2][map_icon3]A struggling village of\npeat gatherers and farmers.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action NullAction()
                elif (quarters+towhitemarshes) > (world_daylength-4):
                    idle "map/whitemarshes01LOCKED.png"
                    hover "map/whitemarshes01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}White Marshes{/color}\n[map_icon1][map_icon2][map_icon3]A struggling village of\npeat gatherers and farmers.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_whitemarshes]"), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action NullAction()
                else:
                    idle "map/whitemarshes01.png"
                    hover "map/whitemarshes01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}White Marshes{/color}\n[map_icon1][map_icon2][map_icon3]A struggling village of\npeat gatherers and farmers.\nTravel time: [travel_duration_whitemarshes]"), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "whitemarshes"), Jump("finaldestination")]
            if pc_area == "whitemarshes":
                add "map/flag.png" xpos 820 ypos 330

        if ruinedshelter_unlocked and not ruinedshelter_firsttime:
            if (bogentrance_firsttime and northernroad_firsttime and tobogentrance <= tonorthernroad) or (bogentrance_firsttime and not northernroad_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 800
                    ypos 234
                    xalign 0.0
                    yalign 0.0
                    if toruinedshelter >= 100:
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 864), SetVariable("mapyframe", 260)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+toruinedshelter) > (world_daylength-2):
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 864), SetVariable("mapyframe", 260)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/right.png"
                        hover "images/map/arrows/righthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 864), SetVariable("mapyframe", 260)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ruinedshelter"), Jump("finaldestination")]
            if (northernroad_firsttime and bogentrance_firsttime and tonorthernroad <= tobogentrance) or (northernroad_firsttime and not bogentrance_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 888
                    ypos 232
                    xalign 0.0
                    yalign 0.0
                    if toruinedshelter >= 100:
                        idle "images/map/arrows/upleftLOCKED.png"
                        hover "images/map/arrows/uplefthoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 880), SetVariable("mapyframe", 256)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+toruinedshelter) > (world_daylength-1):
                        idle "images/map/arrows/upleftLOCKED.png"
                        hover "images/map/arrows/uplefthoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 880), SetVariable("mapyframe", 256)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/upleft.png"
                        hover "images/map/arrows/uplefthover.png"
                        hovered [tt3.Action(""), SetVariable("mapxframe", 880), SetVariable("mapyframe", 256)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ruinedshelter"), Jump("finaldestination")]
        elif ruinedshelter_firsttime:
            $ hours_ruinedshelter = (toruinedshelter / 4) % 24
            $ quarters_ruinedshelter = (toruinedshelter * 15) % 60
            $ travel_duration_ruinedshelter = ("%d:%02d" % (hours_ruinedshelter, quarters_ruinedshelter))
            imagebutton:
                focus_mask None
                xpos 864
                ypos 192
                xalign 0.0
                yalign 0.0
                if ruinedshelter_lefttobeasts:
                    idle "map/ruinedshelter01LOCKED.png"
                    hover "map/ruinedshelter01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}[ruinedshelter_name]{/color}\nA small hamlet inhabited by\na family of furry critters."), SetVariable("mapxframe", 934), SetVariable("mapyframe", 224)]
                    action NullAction()
                elif pc_area == "ruinedshelter":
                    idle "map/ruinedshelter01hover.png"
                    hover "map/ruinedshelter01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}[ruinedshelter_name]{/color}\nA small hamlet that could still be used\nas a stop for travelers.\nYou’re currently here."), SetVariable("mapxframe", 934), SetVariable("mapyframe", 224)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/ruinedshelter01LOCKED.png"
                    hover "map/ruinedshelter01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}[ruinedshelter_name]{/color}\nA small hamlet that could still be used\nas a stop for travelers.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 934), SetVariable("mapyframe", 224)]
                    action NullAction()
                elif toruinedshelter >= 100:
                    idle "map/ruinedshelter01LOCKED.png"
                    hover "map/ruinedshelter01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}[ruinedshelter_name]{/color}\nA small hamlet that could still be used\nas a stop for travelers.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 934), SetVariable("mapyframe", 224)]
                    action NullAction()
                elif (quarters+toruinedshelter) > world_daylength:
                    idle "map/ruinedshelter01LOCKED.png"
                    hover "map/ruinedshelter01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}[ruinedshelter_name]{/color}\nA small hamlet that could still be used\nas a stop for travelers.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_ruinedshelter]"), SetVariable("mapxframe", 934), SetVariable("mapyframe", 224)]
                    action NullAction()
                else:
                    idle "map/ruinedshelter01.png"
                    hover "map/ruinedshelter01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}[ruinedshelter_name]{/color}\nA small hamlet that could still be used\nas a stop for travelers.\nTravel time: [travel_duration_ruinedshelter]"), SetVariable("mapxframe", 934), SetVariable("mapyframe", 224)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ruinedshelter"), Jump("finaldestination")]
            if pc_area == "ruinedshelter":
                add "map/flag.png" xpos 876 ypos 202

        if northernroad_unlocked and not northernroad_firsttime:
            if (ruinedshelter_firsttime and foggylake_firsttime and toruinedshelter <= tofoggylake) or (ruinedshelter_firsttime and not foggylake_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 920
                    ypos 255
                    xalign 0.0
                    yalign 0.0
                    if tonorthernroad >= 100:
                        idle "images/map/arrows/downrightLOCKED.png"
                        hover "images/map/arrows/downrighthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 972), SetVariable("mapyframe", 274)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tonorthernroad) > (world_daylength-1):
                        idle "images/map/arrows/downrightLOCKED.png"
                        hover "images/map/arrows/downrighthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 972), SetVariable("mapyframe", 274)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/downright.png"
                        hover "images/map/arrows/downrighthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 972), SetVariable("mapyframe", 274)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "northernroad"), Jump("finaldestination")]
            if (foggylake_firsttime and ruinedshelter_firsttime and tofoggylake <= toruinedshelter) or (foggylake_firsttime and not ruinedshelter_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 972
                    ypos 248
                    xalign 0.0
                    yalign 0.0
                    if tonorthernroad >= 100:
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 964), SetVariable("mapyframe", 274)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tonorthernroad) > (world_daylength-1):
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 964), SetVariable("mapyframe", 274)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/left.png"
                        hover "images/map/arrows/lefthover.png"
                        hovered [tt3.Action(""), SetVariable("mapxframe", 964), SetVariable("mapyframe", 274)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "northernroad"), Jump("finaldestination")]
        elif northernroad_firsttime:
            $ hours_northernroad = (tonorthernroad / 4) % 24
            $ quarters_northernroad = (tonorthernroad * 15) % 60
            $ travel_duration_northernroad = ("%d:%02d" % (hours_northernroad, quarters_northernroad))
            $ map_icon1 = "{image=mapkeyx2fishingspot}\n"
            imagebutton:
                focus_mask None
                xpos 943
                ypos 249
                xalign 0.0
                yalign 0.0
                if pc_area == "northernroad":
                    idle "map/northernroad01hover.png"
                    hover "map/northernroad01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Northern Road{/color}\n[map_icon1]This well-traveled path is still maintained\neven though parts of it collapsed\ninto the lake.\nYou’re currently here."), SetVariable("mapxframe", 1012), SetVariable("mapyframe", 280)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/northernroad01LOCKED.png"
                    hover "map/northernroad01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Northern Road{/color}\n[map_icon1]This well-traveled path is still maintained\neven though parts of it collapsed\ninto the lake.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1012), SetVariable("mapyframe", 280)]
                    action NullAction()
                elif tonorthernroad >= 100:
                    idle "map/northernroad01LOCKED.png"
                    hover "map/northernroad01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Northern Road{/color}\n[map_icon1]This well-traveled path is still maintained\neven though parts of it collapsed\ninto the lake.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1012), SetVariable("mapyframe", 280)]
                    action NullAction()
                elif (quarters+tonorthernroad) > world_daylength:
                    idle "map/northernroad01LOCKED.png"
                    hover "map/northernroad01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Northern Road{/color}\n[map_icon1]This well-traveled path is still maintained\neven though parts of it collapsed\ninto the lake.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_northernroad]"), SetVariable("mapxframe", 1012), SetVariable("mapyframe", 280)]
                    action NullAction()
                else:
                    idle "map/northernroad01.png"
                    hover "map/northernroad01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Northern Road{/color}\n[map_icon1]This well-traveled path is still maintained\neven though parts of it collapsed\ninto the lake.\nTravel time: [travel_duration_northernroad]"), SetVariable("mapxframe", 1012), SetVariable("mapyframe", 280)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "northernroad"), Jump("finaldestination")]
            if pc_area == "northernroad":
                add "map/flag.png" xpos 979 ypos 228

        if howlerslair_unlocked and not howlerslair_firsttime:
            $ hours_howlerslair = (tohowlerslair / 4) % 24
            $ quarters_howlerslair = (tohowlerslair * 15) % 60
            $ travel_duration_howlerslair = ("%d:%02d" % (hours_howlerslair, quarters_howlerslair))
            imagebutton:
                focus_mask None
                xpos 960
                ypos 200
                xalign 0.0
                yalign 0.0
                if tohowlerslair >= 100:
                    idle "images/map/arrows/smallupLOCKED.png"
                    hover "images/map/arrows/smalluphoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}To The Lair of Howlers{/color}\nYou can’t currently\nreach this area."), SetVariable("mapxframe", 1004), SetVariable("mapyframe", 224)]
                    action [Hide("map_display", transition=dissolve)]
                # elif (quarters+tohowlerslair) > (world_daylength):
                #     idle "images/map/arrows/smallupLOCKED.png"
                #     hover "images/map/arrows/smalluphoverLOCKED.png"
                #     hovered [tt.Action("{color=#f6d6bd}To The Lair of Howlers{/color}\nTo reach this place, you have to\nleave your mount at Foggy Lake.\nYou can’t get here before nightfall.\nTravel time: [travel_duration_howlerslair]"), SetVariable("mapxframe", 1004), SetVariable("mapyframe", 224)]
                #     action [Hide("map_display", transition=dissolve)]
                elif (quarters+tohowlerslair) > (world_daylength-4):
                    idle "images/map/arrows/smallupLOCKED.png"
                    hover "images/map/arrows/smalluphoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}To The Lair of Howlers{/color}\nTo reach this place, you have to\nleave your mount at Foggy Lake.\nYou can’t get here\nand return back before nightfall.\nTravel time: [travel_duration_howlerslair]"), SetVariable("mapxframe", 1004), SetVariable("mapyframe", 224)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/smallup.png"
                    hover "images/map/arrows/smalluphover.png"
                    hovered [tt.Action("{color=#f6d6bd}To The Lair of Howlers{/color}\nTo reach this place, you have to\nleave your mount at Foggy Lake.\nTravel time: [travel_duration_howlerslair]"), SetVariable("mapxframe", 1004), SetVariable("mapyframe", 224)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "howlerslair"), Jump("finaldestination")]
            if pc_area == "howlerslair":
                add "map/flag.png" xpos 954 ypos 210

        if oldtunnel_unlocked and not oldtunnel_firsttime:
            imagebutton:
                focus_mask None
                xpos 992
                ypos 184
                xalign 0.0
                yalign 0.0
                if tooldtunnel >= 100:
                    idle "images/map/arrows/upleftLOCKED.png"
                    hover "images/map/arrows/uplefthoverLOCKED.png"
                    hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1044), SetVariable("mapyframe", 204)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+tooldtunnel) > (world_daylength-1):
                    idle "images/map/arrows/upleftLOCKED.png"
                    hover "images/map/arrows/uplefthoverLOCKED.png"
                    hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1044), SetVariable("mapyframe", 204)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/upleft.png"
                    hover "images/map/arrows/uplefthover.png"
                    hovered [tt.Action(""), SetVariable("mapxframe", 1044), SetVariable("mapyframe", 204)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "oldtunnel"), Jump("finaldestination")]
        elif oldtunnel_firsttime:
            $ hours_oldtunnel = (tooldtunnel / 4) % 24
            $ quarters_oldtunnel = (tooldtunnel * 15) % 60
            $ travel_duration_oldtunnel = ("%d:%02d" % (hours_oldtunnel, quarters_oldtunnel))
            imagebutton:
                focus_mask None
                xpos 933
                ypos 121
                xalign 0.0
                yalign 0.0
                if helvius_about_oldtunnel_paid == day:
                    idle "map/oldtunnel01LOCKED.png"
                    hover "map/oldtunnel01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nYou should stay away from it\nwhile it’s being explored by\nthe people of White Marshes."), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                    action NullAction()
                elif oldtunnel_inside_opened:
                    if pc_area == "oldtunnel":
                        idle "map/oldtunnel01hover.png"
                        hover "map/oldtunnel01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\nYou’re currently here."), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/oldtunnel01LOCKED.png"
                        hover "map/oldtunnel01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action NullAction()
                    elif tooldtunnel >= 100:
                        idle "map/oldtunnel01LOCKED.png"
                        hover "map/oldtunnel01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action NullAction()
                    elif (quarters+tooldtunnel) > world_daylength:
                        idle "map/oldtunnel01LOCKED.png"
                        hover "map/oldtunnel01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_oldtunnel]"), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action NullAction()
                    else:
                        idle "map/oldtunnel01.png"
                        hover "map/oldtunnel01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\nTravel time: [travel_duration_oldtunnel]"), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "oldtunnel"), Jump("finaldestination")]
                else:
                    if pc_area == "oldtunnel":
                        idle "map/oldtunnel01hover.png"
                        hover "map/oldtunnel01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\nAs long as this place remains unexplored,\nyou have to take a detour.\nYou’re currently here."), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/oldtunnel01LOCKED.png"
                        hover "map/oldtunnel01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\nAs long as this place remains unexplored,\nyou have to take a detour.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action NullAction()
                    elif tooldtunnel >= 100:
                        idle "map/oldtunnel01LOCKED.png"
                        hover "map/oldtunnel01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\nAs long as this place remains unexplored,\nyou have to take a detour.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action NullAction()
                    elif (quarters+tooldtunnel) > world_daylength:
                        idle "map/oldtunnel01LOCKED.png"
                        hover "map/oldtunnel01hoverLOCKED.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\nAs long as this place remains unexplored,\nyou have to take a detour.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_oldtunnel]"), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action NullAction()
                    else:
                        idle "map/oldtunnel01.png"
                        hover "map/oldtunnel01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\nAs long as this place remains unexplored,\nyou have to take a detour.\nTravel time: [travel_duration_oldtunnel]"), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "oldtunnel"), Jump("finaldestination")]
            if pc_area == "oldtunnel":
                add "map/flag.png" xpos 902 ypos 135

        if galerocks_unlocked and not galerocks_firsttime:
            imagebutton:
                focus_mask None
                xpos 940
                ypos 56
                xalign 0.0
                yalign 0.0
                if togalerocks >= 100:
                    idle "images/map/arrows/upLOCKED.png"
                    hover "images/map/arrows/uphoverLOCKED.png"
                    hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 920), SetVariable("mapyframe", 86)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+togalerocks) > (world_daylength-1):
                    idle "images/map/arrows/upLOCKED.png"
                    hover "images/map/arrows/uphoverLOCKED.png"
                    hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 920), SetVariable("mapyframe", 86)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/up.png"
                    hover "images/map/arrows/uphover.png"
                    hovered [tt3.Action(""), SetVariable("mapxframe", 920), SetVariable("mapyframe", 86)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "galerocks"), Jump("finaldestination")]
        elif galerocks_firsttime:
            $ hours_galerocks = (togalerocks / 4) % 24
            $ quarters_galerocks = (togalerocks * 15) % 60
            $ travel_duration_galerocks = ("%d:%02d" % (hours_galerocks, quarters_galerocks))
            if mapxframe == 940:
                if galerocks_fulvia_sleep:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if galerocks_porcia_firsttime:
                    $ map_icon2 = "{image=mapkeyx2food} "
                else:
                    $ map_icon2 = ""
                if galerocks_tatius_firsttime:
                    $ map_icon3 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon3 = ""
                if galerocks_rufina_firsttime:
                    $ map_icon4 = "{image=mapkeyx2tailor} "
                else:
                    $ map_icon4 = ""
                if galerocks_aquila_firsttime:
                    $ map_icon5 = "{image=mapkeyx2watersource} "
                else:
                    $ map_icon5 = ""
                if galerocks_fulvia_sleep or galerocks_porcia_firsttime or galerocks_tatius_firsttime or galerocks_rufina_firsttime or galerocks_aquila_firsttime:
                    $ map_icon6 = "\n"
                else:
                    $ map_icon6 = ""
            imagebutton:
                focus_mask None
                xpos 868
                ypos 105
                xalign 0.0
                yalign 0.0
                if pc_area == "galerocks":
                    idle "map/galerocks01hover.png"
                    hover "map/galerocks01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Gale Rocks{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A crude, aged village\nof fishers and salt makers,\nplaced among the hills.\nYou’re currently here."), SetVariable("mapxframe", 940), SetVariable("mapyframe", 136)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/galerocks01LOCKED.png"
                    hover "map/galerocks01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Gale Rocks{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A crude, aged village\nof fishers and salt makers,\nplaced among the hills.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 940), SetVariable("mapyframe", 136)]
                    action NullAction()
                elif togalerocks >= 100:
                    idle "map/galerocks01LOCKED.png"
                    hover "map/galerocks01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Gale Rocks{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A crude, aged village\nof fishers and salt makers,\nplaced among the hills.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 940), SetVariable("mapyframe", 136)]
                    action NullAction()
                elif (quarters+togalerocks) > world_daylength:
                    idle "map/galerocks01LOCKED.png"
                    hover "map/galerocks01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Gale Rocks{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A crude, aged village\nof fishers and salt makers,\nplaced among the hills.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_galerocks]"), SetVariable("mapxframe", 940), SetVariable("mapyframe", 136)]
                    action NullAction()
                else:
                    idle "map/galerocks01.png"
                    hover "map/galerocks01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Gale Rocks{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A crude, aged village\nof fishers and salt makers,\nplaced among the hills.\nTravel time: [travel_duration_galerocks]"), SetVariable("mapxframe", 940), SetVariable("mapyframe", 136)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "galerocks"), Jump("finaldestination")]
            if pc_area == "galerocks":
                add "map/flag.png" xpos 831 ypos 114

        if beach_unlocked and not beach_firsttime:
            imagebutton:
                focus_mask None
                xpos 829
                ypos 72
                xalign 0.0
                yalign 0.0
                if tobeach >= 100:
                    idle "images/map/arrows/upleftLOCKED.png"
                    hover "images/map/arrows/uplefthoverLOCKED.png"
                    hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 816), SetVariable("mapyframe", 90)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+tobeach) > (world_daylength-1):
                    idle "images/map/arrows/upleftLOCKED.png"
                    hover "images/map/arrows/uplefthoverLOCKED.png"
                    hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 816), SetVariable("mapyframe", 90)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/upleft.png"
                    hover "images/map/arrows/uplefthover.png"
                    hovered [tt3.Action(""), SetVariable("mapxframe", 816), SetVariable("mapyframe", 90)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "beach"), Jump("finaldestination")]
        elif beach_firsttime:
            $ hours_beach = (tobeach / 4) % 24
            $ quarters_beach = (tobeach * 15) % 60
            $ travel_duration_beach = ("%d:%02d" % (hours_beach, quarters_beach))
            if mapxframe == 808:
                if galerocks_photios_about_mundanejob:
                    $ map_icon1 = "{image=mapkeyx2mundanejob} "
                else:
                    $ map_icon1 = ""
                $ map_icon2 = "{image=mapkeyx2watersource}\n"
            imagebutton:
                focus_mask None
                xpos 826
                ypos 58
                xalign 0.0
                yalign 0.0
                if pc_area == "beach":
                    idle "map/beach01hover.png"
                    hover "map/beach01hover.png"
                    hovered [tt5.Action("{color=#f6d6bd}The Pier{/color}\n[map_icon1][map_icon2]A spot on the beach where the stones\nare spread enough for the fishers\nto depart on their boats.\nYou’re currently here."), SetVariable("mapxframe", 808), SetVariable("mapyframe", 16)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/beach01LOCKED.png"
                    hover "map/beach01hoverLOCKED.png"
                    hovered [tt5.Action("{color=#f6d6bd}The Pier{/color}\n[map_icon1][map_icon2]A spot on the beach where the stones\nare spread enough for the fishers\nto depart on their boats.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 808), SetVariable("mapyframe", 16)]
                    action NullAction()
                elif tobeach >= 100:
                    idle "map/beach01LOCKED.png"
                    hover "map/beach01hoverLOCKED.png"
                    hovered [tt5.Action("{color=#f6d6bd}The Pier{/color}\n[map_icon1][map_icon2]A spot on the beach where the stones\nare spread enough for the fishers\nto depart on their boats.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 808), SetVariable("mapyframe", 16)]
                    action NullAction()
                elif (quarters+tobeach) > world_daylength:
                    idle "map/beach01LOCKED.png"
                    hover "map/beach01hoverLOCKED.png"
                    hovered [tt5.Action("{color=#f6d6bd}The Pier{/color}\n[map_icon1][map_icon2]A spot on the beach where the stones\nare spread enough for the fishers\nto depart on their boats.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_beach]"), SetVariable("mapxframe", 808), SetVariable("mapyframe", 16)]
                    action NullAction()
                else:
                    idle "map/beach01.png"
                    hover "map/beach01hover.png"
                    hovered [tt5.Action("{color=#f6d6bd}The Pier{/color}\n[map_icon1][map_icon2]A spot on the beach where the stones\nare spread enough for the fishers\nto depart on their boats.\nTravel time: [travel_duration_beach]"), SetVariable("mapxframe", 808), SetVariable("mapyframe", 16)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "beach"), Jump("finaldestination")]
            if pc_area == "beach":
                add "map/flag.png" xpos 870 ypos 38
            if pc_area == "beforebeach":
                add "map/flag.png" xpos 839 ypos 60

        ########################################## EAST
        if dolmen_unlocked and not dolmen_firsttime:
            if (southerncrossroads_firsttime and fallentree_firsttime and tosoutherncrossroads <= tobeholder) or (southerncrossroads_firsttime and not fallentree_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1176
                    ypos 908
                    xalign 0.0
                    yalign 0.0
                    if todolmen >= 100:
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1252), SetVariable("mapyframe", 934)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+todolmen) > (world_daylength-1):
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1252), SetVariable("mapyframe", 934)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/right.png"
                        hover "images/map/arrows/righthover.png"
                        if world_known_areas < 3:
                            hovered [tt.Action("Explore east."), SetVariable("mapxframe", 1252), SetVariable("mapyframe", 934)]
                        else:
                            hovered [tt.Action(""), SetVariable("mapxframe", 1252), SetVariable("mapyframe", 934)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "dolmen"), Jump("finaldestination")]
            if (fallentree_firsttime and southerncrossroads_firsttime and tobeholder <= tosoutherncrossroads) or (fallentree_firsttime and not southerncrossroads_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1360
                    ypos 828
                    xalign 0.0
                    yalign 0.0
                    if todolmen >= 100:
                        idle "images/map/arrows/downleftLOCKED.png"
                        hover "images/map/arrows/downlefthoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 852)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+todolmen) > (world_daylength-1):
                        idle "images/map/arrows/downleftLOCKED.png"
                        hover "images/map/arrows/downlefthoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 852)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/downleft.png"
                        hover "images/map/arrows/downlefthover.png"
                        hovered [tt3.Action(""), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 852)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "dolmen"), Jump("finaldestination")]
        elif dolmen_firsttime:
            $ hours_dolmen01 = (todolmen / 4) % 24
            $ quarters_dolmen01 = (todolmen * 15) % 60
            $ travel_duration_dolmen01 = ("%d:%02d" % (hours_dolmen01, quarters_dolmen01))
            imagebutton:
                focus_mask None
                xpos 1248
                ypos 818
                xalign 0.0
                yalign 0.0
                if pc_area == "dolmen":
                    idle "map/dolmenmap01hover.png"
                    hover "map/dolmenmap01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Dolmen{/color}\nA stone chapel built centuries ago\nto provide shelter to wayfarers.\nYou’re currently here."), SetVariable("mapxframe", 1328), SetVariable("mapyframe", 846)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/dolmenmap01LOCKED.png"
                    hover "map/dolmenmap01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Dolmen{/color}\nA stone chapel built centuries ago\nto provide shelter to wayfarers.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1328), SetVariable("mapyframe", 846)]
                    action NullAction()
                elif todolmen >= 100:
                    idle "map/dolmenmap01LOCKED.png"
                    hover "map/dolmenmap01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Dolmen{/color}\nA stone chapel built centuries ago\nto provide shelter to wayfarers.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1328), SetVariable("mapyframe", 846)]
                    action NullAction()
                elif (quarters+todolmen) > world_daylength:
                    idle "map/dolmenmap01LOCKED.png"
                    hover "map/dolmenmap01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Dolmen{/color}\nA stone chapel built centuries ago\nto provide shelter to wayfarers.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_dolmen01]"), SetVariable("mapxframe", 1328), SetVariable("mapyframe", 846)]
                    action NullAction()
                else:
                    idle "map/dolmenmap01.png"
                    hover "map/dolmenmap01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Dolmen{/color}\nA stone chapel built centuries ago\nto provide shelter to wayfarers.\nTravel time: [travel_duration_dolmen01]"), SetVariable("mapxframe", 1328), SetVariable("mapyframe", 846)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "dolmen"), Jump("finaldestination")]
            if pc_area == "dolmen":
                add "map/flag.png" xpos 1290 ypos 822

        if fallentree_unlocked and not fallentree_firsttime:
            if (dolmen_firsttime and watchtower_firsttime and todolmen <= towatchtower) or (dolmen_firsttime and not watchtower_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1336
                    ypos 824
                    xalign 0.0
                    yalign 0.0
                    if tofallentree >= 100:
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1400), SetVariable("mapyframe", 840)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tofallentree) > (world_daylength-1):
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1400), SetVariable("mapyframe", 840)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/right.png"
                        hover "images/map/arrows/righthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1400), SetVariable("mapyframe", 840)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "fallentree"), Jump("finaldestination")]
            if (watchtower_firsttime and dolmen_firsttime and towatchtower <= todolmen) or (watchtower_firsttime and not dolmen_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1388
                    ypos 700
                    xalign 0.0
                    yalign 0.0
                    if tofallentree >= 100:
                        idle "images/map/arrows/downLOCKED.png"
                        hover "images/map/arrows/downhoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1444), SetVariable("mapyframe", 724)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tofallentree) > (world_daylength-1):
                        idle "images/map/arrows/downLOCKED.png"
                        hover "images/map/arrows/downhoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1444), SetVariable("mapyframe", 724)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/down.png"
                        hover "images/map/arrows/downhover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1444), SetVariable("mapyframe", 724)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "fallentree"), Jump("finaldestination")]
        elif fallentree_firsttime:
            $ hours_fallentree = (tofallentree / 4) % 24
            $ quarters_fallentree = (tofallentree * 15) % 60
            $ travel_duration_fallentree = ("%d:%02d" % (hours_fallentree, quarters_fallentree))
            if mapxframe == 1398:
                $ map_icon1 = "{image=mapkeyx2watersource}"
                $ map_icon2 = "{image=mapkeyx2fishingspot}\n"
            imagebutton:
                focus_mask None
                xpos 1408
                ypos 768
                xalign 0.0
                yalign 0.0
                if not fallentree_cleared:
                    if pc_area == "fallentree":
                        idle "map/fallentree01hover.png"
                        hover "map/fallentree01hover.png"
                        hovered [tt3.Action("{color=#f6d6bd}A Fallen Tree{/color}\n[map_icon1][map_icon2]A blocked section of the road,\nimpassable for carts and wagons.\nCrossing it slows you down."), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/fallentree01LOCKED.png"
                        hover "map/fallentree01hoverLOCKED.png"
                        hovered [tt3.Action("{color=#f6d6bd}A Fallen Tree{/color}\n[map_icon1][map_icon2]A blocked section of the road,\nimpassable for carts and wagons.\nCrossing it slows you down.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action NullAction()
                    elif tofallentree >= 100:
                        idle "map/fallentree01LOCKED.png"
                        hover "map/fallentree01hoverLOCKED.png"
                        hovered [tt3.Action("{color=#f6d6bd}A Fallen Tree{/color}\n[map_icon1][map_icon2]A blocked section of the road,\nimpassable for carts and wagons.\nCrossing it slows you down.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action NullAction()
                    elif (quarters+tofallentree) > world_daylength:
                        idle "map/fallentree01LOCKED.png"
                        hover "map/fallentree01hoverLOCKED.png"
                        hovered [tt3.Action("{color=#f6d6bd}A Fallen Tree{/color}\n[map_icon1][map_icon2]A blocked section of the road,\nimpassable for carts and wagons.\nCrossing it slows you down.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_fallentree]"), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action NullAction()
                    else:
                        idle "map/fallentree01.png"
                        hover "map/fallentree01hover.png"
                        hovered [tt3.Action("{color=#f6d6bd}A Fallen Tree{/color}\n[map_icon1][map_icon2]A blocked section of the road,\nimpassable for carts and wagons.\nCrossing it slows you down.\nTravel time: [travel_duration_fallentree]"), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "fallentree"), Jump("finaldestination")]
                else:
                    if pc_area == "fallentree":
                        idle "map/fallentree02hover.png"
                        hover "map/fallentree02hover.png"
                        hovered [tt3.Action("{color=#f6d6bd}The Riverside Turn{/color}\nThe tree was removed\nand the path is clear again."), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action [Hide("map_display", transition=dissolve)]
                    elif highisland_journey_inprogress == 1:
                        idle "map/fallentree02LOCKED.png"
                        hover "map/fallentree02hoverLOCKED.png"
                        hovered [tt3.Action("{color=#f6d6bd}The Riverside Turn{/color}\nThe tree was removed\nand the path is clear again.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action NullAction()
                    elif tofallentree >= 100:
                        idle "map/fallentree02LOCKED.png"
                        hover "map/fallentree02hoverLOCKED.png"
                        hovered [tt3.Action("{color=#f6d6bd}The Riverside Turn{/color}\nThe tree was removed\nand the path is clear again.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action NullAction()
                    elif (quarters+tofallentree) > world_daylength:
                        idle "map/fallentree02LOCKED.png"
                        hover "map/fallentree02hoverLOCKED.png"
                        hovered [tt3.Action("{color=#f6d6bd}The Riverside Turn{/color}\nThe tree was removed\nand the path is clear again.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_fallentree]"), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action NullAction()
                    else:
                        idle "map/fallentree02.png"
                        hover "map/fallentree02hover.png"
                        hovered [tt3.Action("{color=#f6d6bd}The Riverside Turn{/color}\nThe tree was removed\nand the path is clear again.\nTravel time: [travel_duration_fallentree]"), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "fallentree"), Jump("finaldestination")]
            if pc_area == "fallentree":
                add "map/flag.png" xpos 1360 ypos 750

        if watchtower_unlocked and not watchtower_firsttime:
            if pc_area == "stonesign":
                imagebutton:
                    focus_mask None
                    xpos 1360
                    ypos 652
                    xalign 0.0
                    yalign 0.0
                    if towatchtower >= 100:
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1428), SetVariable("mapyframe", 674)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+towatchtower) > (world_daylength-1):
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1428), SetVariable("mapyframe", 674)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/right.png"
                        hover "images/map/arrows/righthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1428), SetVariable("mapyframe", 674)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "watchtower"), Jump("finaldestination")]
            else:
                if (fallentree_firsttime and stonebridge_firsttime and tofallentree <= tostonebridge) or (fallentree_firsttime and not stonebridge_firsttime):
                    imagebutton:
                        focus_mask None
                        xpos 1416
                        ypos 700
                        xalign 0.0
                        yalign 0.0
                        if towatchtower >= 100:
                            idle "images/map/arrows/upLOCKED.png"
                            hover "images/map/arrows/uphoverLOCKED.png"
                            hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1476), SetVariable("mapyframe", 728)]
                            action [Hide("map_display", transition=dissolve)]
                        elif (quarters+towatchtower) > (world_daylength-1):
                            idle "images/map/arrows/upLOCKED.png"
                            hover "images/map/arrows/uphoverLOCKED.png"
                            hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1476), SetVariable("mapyframe", 728)]
                            action [Hide("map_display", transition=dissolve)]
                        else:
                            idle "images/map/arrows/up.png"
                            hover "images/map/arrows/uphover.png"
                            hovered [tt.Action(""), SetVariable("mapxframe", 1476), SetVariable("mapyframe", 728)]
                            action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "watchtower"), Jump("finaldestination")]
                if (fallentree_firsttime and stonebridge_firsttime and tostonebridge <= tofallentree) or (stonebridge_firsttime and not fallentree_firsttime):
                    imagebutton:
                        focus_mask None
                        xpos 1392
                        ypos 586
                        xalign 0.0
                        yalign 0.0
                        if towatchtower >= 100:
                            idle "images/map/arrows/downLOCKED.png"
                            hover "images/map/arrows/downhoverLOCKED.png"
                            hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1452), SetVariable("mapyframe", 612)]
                            action [Hide("map_display", transition=dissolve)]
                        elif (quarters+towatchtower) > (world_daylength-1):
                            idle "images/map/arrows/downLOCKED.png"
                            hover "images/map/arrows/downhoverLOCKED.png"
                            hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1452), SetVariable("mapyframe", 612)]
                            action [Hide("map_display", transition=dissolve)]
                        else:
                            idle "images/map/arrows/down.png"
                            hover "images/map/arrows/downhover.png"
                            hovered [tt.Action(""), SetVariable("mapxframe", 1452), SetVariable("mapyframe", 612)]
                            action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "watchtower"), Jump("finaldestination")]
        elif watchtower_firsttime:
            $ hours_watchtower = (towatchtower / 4) % 24
            $ quarters_watchtower = (towatchtower * 15) % 60
            $ travel_duration_watchtower = ("%d:%02d" % (hours_watchtower, quarters_watchtower))
            if mapxframe == 1442:
                if watchtower_open:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if day >= watchtower_wildplants_start and watchtower_wildplants_left:
                    $ map_icon2 = "{image=mapkeyx2food} "
                else:
                    $ map_icon2 = ""
                if watchtower_open or (day >= watchtower_wildplants_start and watchtower_wildplants_left):
                    $ map_icon3 = "\n "
                else:
                    $ map_icon3 = ""
            imagebutton:
                focus_mask None
                xpos 1381
                ypos 623
                xalign 0.0
                yalign 0.0
                if pc_area == "watchtower":
                    idle "map/watchtowerhover.png"
                    hover "map/watchtowerhover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Abandoned Watchtower{/color}\n[map_icon1][map_icon2][map_icon3]An outpost built at the top\nof the hill, barely taller\nthan the nearby tree crowns.\nYou’re currently here."), SetVariable("mapxframe", 1442), SetVariable("mapyframe", 656)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/watchtowerLOCKED.png"
                    hover "map/watchtowerhoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Abandoned Watchtower{/color}\n[map_icon1][map_icon2][map_icon3]An outpost built at the top\nof the hill, barely taller\nthan the nearby tree crowns.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1442), SetVariable("mapyframe", 656)]
                    action NullAction()
                elif towatchtower >= 100:
                    idle "map/watchtowerLOCKED.png"
                    hover "map/watchtowerhoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Abandoned Watchtower{/color}\n[map_icon1][map_icon2][map_icon3]An outpost built at the top\nof the hill, barely taller\nthan the nearby tree crowns.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1442), SetVariable("mapyframe", 656)]
                    action NullAction()
                elif (quarters+towatchtower) > world_daylength:
                    idle "map/watchtowerLOCKED.png"
                    hover "map/watchtowerhoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Abandoned Watchtower{/color}\n[map_icon1][map_icon2][map_icon3]An outpost built at the top\nof the hill, barely taller\nthan the nearby tree crowns.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_watchtower]"), SetVariable("mapxframe", 1442), SetVariable("mapyframe", 656)]
                    action NullAction()
                else:
                    idle "map/watchtower.png"
                    hover "map/watchtowerhover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Abandoned Watchtower{/color}\n[map_icon1][map_icon2][map_icon3]An outpost built at the top\nof the hill, barely taller\nthan the nearby tree crowns.\nTravel time: [travel_duration_watchtower]"), SetVariable("mapxframe", 1442), SetVariable("mapyframe", 656)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "watchtower"), Jump("finaldestination")]
            if pc_area == "watchtower":
                add "map/flag.png" xpos 1413 ypos 600

        if persistent.demomode and eudociahouse_unlocked and not eudocia_firsttime:
            imagebutton:
                focus_mask None
                xpos 1464
                ypos 648
                xalign 0.0
                yalign 0.0
                idle "images/map/arrows/rightLOCKED.png"
                hover "images/map/arrows/righthoverLOCKED.png"
                hovered [tt.Action("The way forward is\nnot available in the demo!"), SetVariable("mapxframe", 1532), SetVariable("mapyframe", 668)]
                action NullAction()
        elif eudociahouse_unlocked and not eudocia_firsttime:
            imagebutton:
                focus_mask None
                xpos 1456
                ypos 648
                xalign 0.0
                yalign 0.0
                if toeudociahouse >= 100:
                    idle "images/map/arrows/rightLOCKED.png"
                    hover "images/map/arrows/righthoverLOCKED.png"
                    hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1532), SetVariable("mapyframe", 668)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+toeudociahouse) > (world_daylength-1):
                    idle "images/map/arrows/rightLOCKED.png"
                    hover "images/map/arrows/righthoverLOCKED.png"
                    hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1532), SetVariable("mapyframe", 668)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/right.png"
                    hover "images/map/arrows/righthover.png"
                    hovered [tt.Action(""), SetVariable("mapxframe", 1532), SetVariable("mapyframe", 668)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "eudociahouse"), Jump("finaldestination")]
        elif eudocia_firsttime:
            $ hours_eudociahouse = (toeudociahouse / 4) % 24
            $ quarters_eudociahouse = (toeudociahouse * 15) % 60
            $ travel_duration_eudociahouse = ("%d:%02d" % (hours_eudociahouse, quarters_eudociahouse))
            if mapxframe == 1552:
                if eudocia_sleep_available:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if eudocia_about_selling:
                    $ map_icon2 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon2 = ""
                if eudocia_sleep_available or eudocia_about_selling:
                    $ map_icon3 = "\n"
                else:
                    $ map_icon3 = ""
            imagebutton:
                focus_mask None
                xpos 1519
                ypos 597
                xalign 0.0
                yalign 0.0
                if pc_area == "eudociahouse" or pc_area == "eudociahouseinside":
                    idle "map/eudociahouse01hover.png"
                    hover "map/eudociahouse01hover.png"
                    hovered [tt2.Action("{color=#f6d6bd}The Secluded Residence{/color}\n[map_icon1][map_icon2][map_icon3]A small, but luxurious hamlet,\nfor some reason spared by wild beasts.\nYou’re currently here."), SetVariable("mapxframe", 1552), SetVariable("mapyframe", 664)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/eudociahouse01LOCKED.png"
                    hover "map/eudociahouse01hoverLOCKED.png"
                    hovered [tt2.Action("{color=#f6d6bd}The Secluded Residence{/color}\n[map_icon1][map_icon2][map_icon3]A small, but luxurious hamlet,\nfor some reason spared by wild beasts.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1552), SetVariable("mapyframe", 664)]
                    action NullAction()
                elif toeudociahouse >= 100:
                    idle "map/eudociahouse01LOCKED.png"
                    hover "map/eudociahouse01hoverLOCKED.png"
                    hovered [tt2.Action("{color=#f6d6bd}The Secluded Residence{/color}\n[map_icon1][map_icon2][map_icon3]A small, but luxurious hamlet,\nfor some reason spared by wild beasts.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1552), SetVariable("mapyframe", 664)]
                    action NullAction()
                elif (quarters+toeudociahouse) > world_daylength:
                    idle "map/eudociahouse01LOCKED.png"
                    hover "map/eudociahouse01hoverLOCKED.png"
                    hovered [tt2.Action("{color=#f6d6bd}The Secluded Residence{/color}\n[map_icon1][map_icon2][map_icon3]A small, but luxurious hamlet,\nfor some reason spared by wild beasts.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_eudociahouse]"), SetVariable("mapxframe", 1552), SetVariable("mapyframe", 664)]
                    action NullAction()
                else:
                    idle "map/eudociahouse01.png"
                    hover "map/eudociahouse01hover.png"
                    hovered [tt2.Action("{color=#f6d6bd}The Secluded Residence{/color}\n[map_icon1][map_icon2][map_icon3]A small, but luxurious hamlet,\nfor some reason spared by wild beasts.\nTravel time: [travel_duration_eudociahouse]"), SetVariable("mapxframe", 1552), SetVariable("mapyframe", 664)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "eudociahouse"), Jump("finaldestination")]
            if pc_area == "eudociahouse" or pc_area == "eudociahouseinside":
                add "map/flag.png" xpos 1540 ypos 600

        if persistent.demomode and stonebridge_unlocked and not stonebridge_firsttime:
            imagebutton:
                focus_mask None
                xpos 1392
                ypos 548
                xalign 0.0
                yalign 0.0
                idle "images/map/arrows/upLOCKED.png"
                hover "images/map/arrows/uphoverLOCKED.png"
                hovered [tt.Action("The way forward is\nnot available in the demo!"), SetVariable("mapxframe", 1456), SetVariable("mapyframe", 576)]
                action NullAction()
        elif stonebridge_unlocked and not stonebridge_firsttime:
            if (watchtower_firsttime and huntercabin_firsttime and towatchtower <= tohuntercabin) or (watchtower_firsttime and not huntercabin_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1392
                    ypos 548
                    xalign 0.0
                    yalign 0.0
                    if tostonebridge >= 100:
                        idle "images/map/arrows/upLOCKED.png"
                        hover "images/map/arrows/uphoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1456), SetVariable("mapyframe", 576)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tostonebridge) > (world_daylength-1):
                        idle "images/map/arrows/upLOCKED.png"
                        hover "images/map/arrows/uphoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1456), SetVariable("mapyframe", 576)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/up.png"
                        hover "images/map/arrows/uphover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1456), SetVariable("mapyframe", 576)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "stonebridge"), Jump("finaldestination")]
            if (huntercabin_firsttime and watchtower_firsttime and tohuntercabin <= towatchtower) or (huntercabin_firsttime and not watchtower_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1320
                    ypos 536
                    xalign 0.0
                    yalign 0.0
                    if tostonebridge >= 100:
                        idle "images/map/arrows/downrightLOCKED.png"
                        hover "images/map/arrows/downrighthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1380), SetVariable("mapyframe", 556)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tostonebridge) > (world_daylength-1):
                        idle "images/map/arrows/downrightLOCKED.png"
                        hover "images/map/arrows/downrighthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1380), SetVariable("mapyframe", 556)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/downright.png"
                        hover "images/map/arrows/downrighthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1380), SetVariable("mapyframe", 556)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "stonebridge"), Jump("finaldestination")]
        elif stonebridge_firsttime:
            $ hours_stonebridge = (tostonebridge / 4) % 24
            $ quarters_stonebridge = (tostonebridge * 15) % 60
            $ travel_duration_stonebridge = ("%d:%02d" % (hours_stonebridge, quarters_stonebridge))
            imagebutton:
                focus_mask None
                xpos 1353
                ypos 537
                xalign 0.0
                yalign 0.0
                if encounter_spottedwolves == day:
                    idle "map/stonebridge01LOCKED.png"
                    hover "map/stonebridge01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Bridge{/color}\nA single stone slab\nplaced over a streambed.\nYou need to wait for a day\nfor the spotted wolves to leave."), SetVariable("mapxframe", 1424), SetVariable("mapyframe", 564)]
                    action NullAction()
                elif pc_area == "stonebridge":
                    idle "map/stonebridge01hover.png"
                    hover "map/stonebridge01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Bridge{/color}\nA single stone slab\nplaced over a streambed.\nYou’re currently here."), SetVariable("mapxframe", 1424), SetVariable("mapyframe", 564)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/stonebridge01LOCKED.png"
                    hover "map/stonebridge01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Bridge{/color}\nA single stone slab\nplaced over a streambed.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1424), SetVariable("mapyframe", 564)]
                    action NullAction()
                elif tostonebridge >= 100:
                    idle "map/stonebridge01LOCKED.png"
                    hover "map/stonebridge01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Bridge{/color}\nA single stone slab\nplaced over a streambed.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1424), SetVariable("mapyframe", 564)]
                    action NullAction()
                elif (quarters+tostonebridge) > world_daylength:
                    idle "map/stonebridge01LOCKED.png"
                    hover "map/stonebridge01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Bridge{/color}\nA single stone slab\nplaced over a streambed.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_stonebridge]"), SetVariable("mapxframe", 1424), SetVariable("mapyframe", 564)]
                    action NullAction()
                else:
                    idle "map/stonebridge01.png"
                    hover "map/stonebridge01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Bridge{/color}\nA single stone slab\nplaced over a streambed.\nTravel time: [travel_duration_stonebridge]"), SetVariable("mapxframe", 1424), SetVariable("mapyframe", 564)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "stonebridge"), Jump("finaldestination")]
            if pc_area == "stonebridge":
                add "map/flag.png" xpos 1349 ypos 509

        if persistent.demomode and stonesign_unlocked and not stonesign_firsttime:
            imagebutton:
                focus_mask None
                xpos 1316
                ypos 648
                xalign 0.0
                yalign 0.0
                idle "images/map/arrows/leftLOCKED.png"
                hover "images/map/arrows/lefthoverLOCKED.png"
                hovered [tt3.Action("The way forward is\nnot available in the demo!"), SetVariable("mapxframe", 1304), SetVariable("mapyframe", 672)]
                action NullAction()
        elif stonesign_unlocked and not stonesign_firsttime:
            imagebutton:
                focus_mask None
                xpos 1316
                ypos 648
                xalign 0.0
                yalign 0.0
                if tostonesign >= 100:
                    idle "images/map/arrows/leftLOCKED.png"
                    hover "images/map/arrows/lefthoverLOCKED.png"
                    hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1304), SetVariable("mapyframe", 672)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+tostonesign) > (world_daylength-1):
                    idle "images/map/arrows/leftLOCKED.png"
                    hover "images/map/arrows/lefthoverLOCKED.png"
                    hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1304), SetVariable("mapyframe", 672)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/left.png"
                    hover "images/map/arrows/lefthover.png"
                    hovered [tt3.Action(""), SetVariable("mapxframe", 1304), SetVariable("mapyframe", 672)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "stonesign"), Jump("finaldestination")]
        elif stonesign_firsttime:
            $ hours_stonesign = (tostonesign / 4) % 24
            $ quarters_stonesign = (tostonesign * 15) % 60
            $ travel_duration_stonesign = ("%d:%02d" % (hours_stonesign, quarters_stonesign))
            imagebutton:
                focus_mask None
                xpos 1283
                ypos 615
                xalign 0.0
                yalign 0.0
                if pc_area == "stonesign":
                    idle "map/stonesign01hover.png"
                    hover "map/stonesign01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}A Woodland Edge{/color}\nA path leading to the heart of the forest.\nThe red stone tells travelers to turn back.\nYou’re currently here."), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 654)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/stonesign01LOCKED.png"
                    hover "map/stonesign01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}A Woodland Edge{/color}\nA path leading to the heart of the forest.\nThe red stone tells travelers to turn back.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 654)]
                    action NullAction()
                elif tostonesign >= 100:
                    idle "map/stonesign01LOCKED.png"
                    hover "map/stonesign01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}A Woodland Edge{/color}\nA path leading to the heart of the forest.\nThe red stone tells travelers to turn back.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 654)]
                    action NullAction()
                elif (quarters+tostonesign) > world_daylength:
                    idle "map/stonesign01LOCKED.png"
                    hover "map/stonesign01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}A Woodland Edge{/color}\nA path leading to the heart of the forest.\nThe red stone tells travelers to turn back.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_stonesign]"), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 654)]
                    action NullAction()
                else:
                    idle "map/stonesign01.png"
                    hover "map/stonesign01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}A Woodland Edge{/color}\nA path leading to the heart of the forest.\nThe red stone tells travelers to turn back.\nTravel time: [travel_duration_stonesign]"), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 654)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "stonesign"), Jump("finaldestination")]
            if pc_area == "stonesign":
                add "map/flag.png" xpos 1318 ypos 613

        if ghoulcave_unlocked and not ghoulcave_firsttime:
            imagebutton:
                focus_mask None
                xpos 1412
                ypos 504
                xalign 0.0
                yalign 0.0
                if toghoulcave >= 100:
                    idle "images/map/arrows/uprightLOCKED.png"
                    hover "images/map/arrows/uprighthoverLOCKED.png"
                    hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1472), SetVariable("mapyframe", 520)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+toghoulcave) > (world_daylength-1):
                    idle "images/map/arrows/uprightLOCKED.png"
                    hover "images/map/arrows/uprighthoverLOCKED.png"
                    hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1472), SetVariable("mapyframe", 520)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/upright.png"
                    hover "images/map/arrows/uprighthover.png"
                    hovered [tt.Action(""), SetVariable("mapxframe", 1472), SetVariable("mapyframe", 520)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ghoulcave"), Jump("finaldestination")]
        elif ghoulcave_firsttime:
            $ hours_ghoulcave = (toghoulcave / 4) % 24
            $ quarters_ghoulcave = (toghoulcave * 15) % 60
            $ travel_duration_ghoulcave = ("%d:%02d" % (hours_ghoulcave, quarters_ghoulcave))
            if mapxframe == 1496:
                if ghoulcave_wildplants_left:
                    $ map_icon1 = "{image=mapkeyx2food} "
                else:
                    $ map_icon1 = ""
                $ map_icon2 = "{image=mapkeyx2watersource} "
                $ map_icon3 = "{image=mapkeyx2fishingspot} "
                $ map_icon4 = "\n"
            imagebutton:
                focus_mask None
                xpos 1456
                ypos 442
                xalign 0.0
                yalign 0.0
                if pc_area == "ghoulcave":
                    idle "map/ghoulcave01hover.png"
                    hover "map/ghoulcave01hover.png"
                    hovered [tt2.Action("{color=#f6d6bd}A Small Cave{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4]A dubious cave entrance\nfound on a forgotten path.\nYou’re currently here."), SetVariable("mapxframe", 1496), SetVariable("mapyframe", 512)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/ghoulcave01LOCKED.png"
                    hover "map/ghoulcave01hoverLOCKED.png"
                    hovered [tt2.Action("{color=#f6d6bd}A Small Cave{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4]A dubious cave entrance\nfound on a forgotten path.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1496), SetVariable("mapyframe", 512)]
                    action NullAction()
                elif toghoulcave >= 100:
                    idle "map/ghoulcave01LOCKED.png"
                    hover "map/ghoulcave01hoverLOCKED.png"
                    hovered [tt2.Action("{color=#f6d6bd}A Small Cave{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4]A dubious cave entrance\nfound on a forgotten path.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1496), SetVariable("mapyframe", 512)]
                    action NullAction()
                elif (quarters+toghoulcave) > world_daylength:
                    idle "map/ghoulcave01LOCKED.png"
                    hover "map/ghoulcave01hoverLOCKED.png"
                    hovered [tt2.Action("{color=#f6d6bd}A Small Cave{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4]A dubious cave entrance\nfound on a forgotten path.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_ghoulcave]"), SetVariable("mapxframe", 1496), SetVariable("mapyframe", 512)]
                    action NullAction()
                else:
                    idle "map/ghoulcave01.png"
                    hover "map/ghoulcave01hover.png"
                    hovered [tt2.Action("{color=#f6d6bd}A Small Cave{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4]A dubious cave entrance\nfound on a forgotten path.\nTravel time: [travel_duration_ghoulcave]"), SetVariable("mapxframe", 1496), SetVariable("mapyframe", 512)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "ghoulcave"), Jump("finaldestination")]
            if pc_area == "ghoulcave":
                add "map/flag.png" xpos 1483 ypos 442

        if giantstatue_unlocked and not giantstatue_firsttime:
            imagebutton:
                focus_mask None
                xpos 1536
                ypos 453
                xalign 0.0
                yalign 0.0
                if togiantstatue >= 100:
                    idle "images/map/arrows/rightLOCKED.png"
                    hover "images/map/arrows/righthoverLOCKED.png"
                    hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1524), SetVariable("mapyframe", 476)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+togiantstatue) > (world_daylength-1):
                    idle "images/map/arrows/rightLOCKED.png"
                    hover "images/map/arrows/righthoverLOCKED.png"
                    hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1524), SetVariable("mapyframe", 476)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/right.png"
                    hover "images/map/arrows/righthover.png"
                    hovered [tt3.Action(""), SetVariable("mapxframe", 1524), SetVariable("mapyframe", 476)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "giantstatue"), Jump("finaldestination")]
        elif giantstatue_firsttime:
            $ hours_giantstatue = (togiantstatue / 4) % 24
            $ quarters_giantstatue = (togiantstatue * 15) % 60
            $ travel_duration_giantstatue = ("%d:%02d" % (hours_giantstatue, quarters_giantstatue))
            imagebutton:
                focus_mask None
                xpos 1543
                ypos 386
                xalign 0.0
                yalign 0.0
                if greenmountaintribe_banned:
                    if not giantstatue_awoken:
                        idle "map/giantstatue01LOCKED.png"
                        hover "map/giantstatue01hoverLOCKED.png"
                    else:
                        idle "map/giantstatue02LOCKED.png"
                        hover "map/giantstatue02hoverLOCKED.png"
                    hovered [tt3.Action("{color=#f6d6bd}The Giant{/color}\nA centuries old monument\nportraying a huge man with a club.\n{color=#6a6a6a}If The Tribe of The Green Mountain\nfinds you here, you’ll be executed.{/color}"), SetVariable("mapxframe", 1533), SetVariable("mapyframe", 416)]
                    action NullAction()
                elif pc_area == "giantstatue":
                    if not giantstatue_awoken:
                        idle "map/giantstatue01hover.png"
                        hover "map/giantstatue01hover.png"
                    else:
                        idle "map/giantstatue02hover.png"
                        hover "map/giantstatue02hover.png"
                    hovered [tt3.Action("{color=#f6d6bd}The Giant{/color}\nA centuries old monument\nportraying a huge man with a club.\nYou’re currently here."), SetVariable("mapxframe", 1533), SetVariable("mapyframe", 416)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    if not giantstatue_awoken:
                        idle "map/giantstatue01LOCKED.png"
                        hover "map/giantstatue01hoverLOCKED.png"
                    else:
                        idle "map/giantstatue02LOCKED.png"
                        hover "map/giantstatue02hoverLOCKED.png"
                    hovered [tt3.Action("{color=#f6d6bd}The Giant{/color}\nA centuries old monument\nportraying a huge man with a club.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1533), SetVariable("mapyframe", 416)]
                    action NullAction()
                elif togiantstatue >= 100:
                    if not giantstatue_awoken:
                        idle "map/giantstatue01LOCKED.png"
                        hover "map/giantstatue01hoverLOCKED.png"
                    else:
                        idle "map/giantstatue02LOCKED.png"
                        hover "map/giantstatue02hoverLOCKED.png"
                    hovered [tt3.Action("{color=#f6d6bd}The Giant{/color}\nA centuries old monument\nportraying a huge man with a club.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1533), SetVariable("mapyframe", 416)]
                    action NullAction()
                elif (quarters+togiantstatue) > world_daylength:
                    if not giantstatue_awoken:
                        idle "map/giantstatue01LOCKED.png"
                        hover "map/giantstatue01hoverLOCKED.png"
                    else:
                        idle "map/giantstatue02LOCKED.png"
                        hover "map/giantstatue02hoverLOCKED.png"
                    hovered [tt3.Action("{color=#f6d6bd}The Giant{/color}\nA centuries old monument\nportraying a huge man with a club.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_giantstatue]"), SetVariable("mapxframe", 1533), SetVariable("mapyframe", 416)]
                    action NullAction()
                else:
                    if not giantstatue_awoken:
                        idle "map/giantstatue01.png"
                        hover "map/giantstatue01hover.png"
                    else:
                        idle "map/giantstatue02.png"
                        hover "map/giantstatue02hover.png"
                    hovered [tt3.Action("{color=#f6d6bd}The Giant{/color}\nA centuries old monument\nportraying a huge man with a club.\nTravel time: [travel_duration_giantstatue]"), SetVariable("mapxframe", 1533), SetVariable("mapyframe", 416)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "giantstatue"), Jump("finaldestination")]
            if pc_area == "giantstatue":
                add "map/flag.png" xpos 1516 ypos 400

        if mountainroad_unlocked and not mountainroad_firsttime:
            imagebutton:
                focus_mask None
                xpos 1604
                ypos 392
                xalign 0.0
                yalign 0.0
                if pc_hp < 1 and pc_area != "mountainroad" and pc_area != "greenmountaintribe":
                    idle "images/map/arrows/uprightLOCKED.png"
                    hover "images/map/arrows/uprighthoverLOCKED.png"
                    hovered [tt3.Action("You’re too exhausted to climb up a mountain."), SetVariable("mapxframe", 1584), SetVariable("mapyframe", 416)]
                    action [Hide("map_display", transition=dissolve)]
                elif tomountainroad >= 100:
                    idle "images/map/arrows/uprightLOCKED.png"
                    hover "images/map/arrows/uprighthoverLOCKED.png"
                    hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1584), SetVariable("mapyframe", 416)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+tomountainroad) > (world_daylength-1):
                    idle "images/map/arrows/uprightLOCKED.png"
                    hover "images/map/arrows/uprighthoverLOCKED.png"
                    hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1584), SetVariable("mapyframe", 416)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/upright.png"
                    hover "images/map/arrows/uprighthover.png"
                    hovered [tt3.Action(""), SetVariable("mapxframe", 1584), SetVariable("mapyframe", 416)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "mountainroad"), Jump("finaldestination")]
        elif mountainroad_firsttime:
            $ hours_mountainroad = (tomountainroad / 4) % 24
            $ quarters_mountainroad = (tomountainroad * 15) % 60
            $ travel_duration_mountainroad = ("%d:%02d" % (hours_mountainroad, quarters_mountainroad))
            imagebutton:
                focus_mask None
                xpos 1584
                ypos 401
                xalign 0.0
                yalign 0.0
                if greenmountaintribe_banned:
                    if mountainroad_egg_broken:
                        idle "map/mountainroad02LOCKED.png"
                        hover "map/mountainroad02hoverLOCKED.png"
                    elif mountainroad_egg_gone:
                        idle "map/mountainroad03LOCKED.png"
                        hover "map/mountainroad03hoverLOCKED.png"
                    else:
                        idle "map/mountainroad01LOCKED.png"
                        hover "map/mountainroad01hoverLOCKED.png"
                    hovered [tt3.Action("{color=#f6d6bd}A Nest{/color}\nA winding, but wide path\nleading into the eastern mountains.\n{color=#6a6a6a}If The Tribe of The Green Mountain\nfinds you here, you’ll be executed.{/color}"), SetVariable("mapxframe", 1590), SetVariable("mapyframe", 433)]
                    action NullAction()
                elif pc_area == "mountainroad":
                    if mountainroad_egg_broken:
                        idle "map/mountainroad02hover.png"
                        hover "map/mountainroad02hover.png"
                    elif mountainroad_egg_gone:
                        idle "map/mountainroad03hover.png"
                        hover "map/mountainroad03hover.png"
                    else:
                        idle "map/mountainroad01hover.png"
                        hover "map/mountainroad01hover.png"
                    hovered [tt3.Action("{color=#f6d6bd}A Nest{/color}\nA winding, but wide path\nleading into the eastern mountains.\nYou’re currently here."), SetVariable("mapxframe", 1590), SetVariable("mapyframe", 433)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    if mountainroad_egg_broken:
                        idle "map/mountainroad02LOCKED.png"
                        hover "map/mountainroad02hoverLOCKED.png"
                    elif mountainroad_egg_gone:
                        idle "map/mountainroad03LOCKED.png"
                        hover "map/mountainroad03hoverLOCKED.png"
                    else:
                        idle "map/mountainroad01LOCKED.png"
                        hover "map/mountainroad01hoverLOCKED.png"
                    hovered [tt3.Action("{color=#f6d6bd}A Nest{/color}\nA winding, but wide path\nleading into the eastern mountains.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1590), SetVariable("mapyframe", 433)]
                    action NullAction()
                elif tomountainroad >= 100:
                    if mountainroad_egg_broken:
                        idle "map/mountainroad02LOCKED.png"
                        hover "map/mountainroad02hoverLOCKED.png"
                    elif mountainroad_egg_gone:
                        idle "map/mountainroad03LOCKED.png"
                        hover "map/mountainroad03hoverLOCKED.png"
                    else:
                        idle "map/mountainroad01LOCKED.png"
                        hover "map/mountainroad01hoverLOCKED.png"
                    hovered [tt3.Action("{color=#f6d6bd}A Nest{/color}\nA winding, but wide path\nleading into the eastern mountains.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1590), SetVariable("mapyframe", 433)]
                    action NullAction()
                elif (quarters+tomountainroad) > world_daylength:
                    if mountainroad_egg_broken:
                        idle "map/mountainroad02LOCKED.png"
                        hover "map/mountainroad02hoverLOCKED.png"
                    elif mountainroad_egg_gone:
                        idle "map/mountainroad03LOCKED.png"
                        hover "map/mountainroad03hoverLOCKED.png"
                    else:
                        idle "map/mountainroad01LOCKED.png"
                        hover "map/mountainroad01hoverLOCKED.png"
                    hovered [tt3.Action("{color=#f6d6bd}A Nest{/color}\nA winding, but wide path\nleading into the eastern mountains.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_mountainroad]"), SetVariable("mapxframe", 1590), SetVariable("mapyframe", 433)]
                    action NullAction()
                elif pc_hp < 1 and pc_area != "mountainroad" and pc_area != "greenmountaintribe":
                    if mountainroad_egg_broken:
                        idle "map/mountainroad02LOCKED.png"
                        hover "map/mountainroad02hoverLOCKED.png"
                    elif mountainroad_egg_gone:
                        idle "map/mountainroad03LOCKED.png"
                        hover "map/mountainroad03hoverLOCKED.png"
                    else:
                        idle "map/mountainroad01LOCKED.png"
                        hover "map/mountainroad01hoverLOCKED.png"
                    hovered [tt3.Action("{color=#f6d6bd}A Nest{/color}\nA winding, but wide path\nleading into the eastern mountains.\n{color=#6a6a6a}You’re too exhausted to climb up a mountain.{/color}"), SetVariable("mapxframe", 1590), SetVariable("mapyframe", 433)]
                    action NullAction()
                else:
                    if mountainroad_egg_broken:
                        idle "map/mountainroad02.png"
                        hover "map/mountainroad02hover.png"
                    elif mountainroad_egg_gone:
                        idle "map/mountainroad03.png"
                        hover "map/mountainroad03hover.png"
                    else:
                        idle "map/mountainroad01.png"
                        hover "map/mountainroad01hover.png"
                    hovered [tt3.Action("{color=#f6d6bd}A Nest{/color}\nA winding, but wide path\nleading into the eastern mountains.\nTravel time: [travel_duration_mountainroad]"), SetVariable("mapxframe", 1590), SetVariable("mapyframe", 433)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "mountainroad"), Jump("finaldestination")]
            if pc_area == "mountainroad":
                add "map/flag.png" xpos 1615 ypos 382

        if greenmountaintribe_unlocked and not greenmountaintribe_firsttime:
            imagebutton:
                focus_mask None
                xpos 1588
                ypos 340
                xalign 0.0
                yalign 0.0
                if pc_hp < 1 and pc_area != "mountainroad" and pc_area != "greenmountaintribe":
                    idle "images/map/arrows/upLOCKED.png"
                    hover "images/map/arrows/uphoverLOCKED.png"
                    hovered [tt3.Action("You’re too exhausted to climb up a mountain."), SetVariable("mapxframe", 1576), SetVariable("mapyframe", 376)]
                    action [Hide("map_display", transition=dissolve)]
                elif togreenmountaintribe >= 100:
                    idle "images/map/arrows/upLOCKED.png"
                    hover "images/map/arrows/uphoverLOCKED.png"
                    hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1576), SetVariable("mapyframe", 376)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+togreenmountaintribe) > (world_daylength-1):
                    idle "images/map/arrows/upLOCKED.png"
                    hover "images/map/arrows/uphoverLOCKED.png"
                    hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1576), SetVariable("mapyframe", 376)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/up.png"
                    hover "images/map/arrows/uphover.png"
                    hovered [tt3.Action(""), SetVariable("mapxframe", 1576), SetVariable("mapyframe", 376)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "greenmountaintribe"), Jump("finaldestination")]
        elif greenmountaintribe_firsttime:
            $ hours_greenmountaintribe = (togreenmountaintribe / 4) % 24
            $ quarters_greenmountaintribe = (togreenmountaintribe * 15) % 60
            $ travel_duration_greenmountaintribe = ("%d:%02d" % (hours_greenmountaintribe, quarters_greenmountaintribe))
            if mapxframe == 1632:
                if greenmountaintribe_sleep:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if cephasgaiane_shop and not cephasgaiane_shop_dragonhorn:
                    $ map_icon3 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon3 = ""
                if greenmountaintribe_sleep or (cephasgaiane_shop and not cephasgaiane_shop_dragonhorn):
                    $ map_icon5 = "\n"
                else:
                    $ map_icon5 = ""
            imagebutton:
                focus_mask None
                xpos 1602
                ypos 355
                xalign 0.0
                yalign 0.0
                if greenmountaintribe_banned:
                    idle "map/greenmountaintribe01LOCKED.png"
                    hover "map/greenmountaintribe01hoverLOCKED.png"
                    hovered [tt4.Action("{color=#f6d6bd}The Tribe of The Green Mountain{/color}\nAn ancient settlement carved into\na large, natural cave.\n{color=#6a6a6a}You would be executed\nupon arrival.{/color}"), SetVariable("mapxframe", 1632), SetVariable("mapyframe", 352)]
                    action NullAction()
                elif pc_area == "greenmountaintribe":
                    idle "map/greenmountaintribe01hover.png"
                    hover "map/greenmountaintribe01hover.png"
                    hovered [tt4.Action("{color=#f6d6bd}The Tribe of The Green Mountain{/color}\n[map_icon1][map_icon3][map_icon5]An ancient settlement carved into\na large, natural cave.\nYou’re currently here."), SetVariable("mapxframe", 1632), SetVariable("mapyframe", 352)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/greenmountaintribe01LOCKED.png"
                    hover "map/greenmountaintribe01hoverLOCKED.png"
                    hovered [tt4.Action("{color=#f6d6bd}The Tribe of The Green Mountain{/color}\n[map_icon1][map_icon3][map_icon5]An ancient settlement carved into\na large, natural cave.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1632), SetVariable("mapyframe", 352)]
                    action NullAction()
                elif togreenmountaintribe >= 100:
                    idle "map/greenmountaintribe01LOCKED.png"
                    hover "map/greenmountaintribe01hoverLOCKED.png"
                    hovered [tt4.Action("{color=#f6d6bd}The Tribe of The Green Mountain{/color}\n[map_icon1][map_icon3][map_icon5]An ancient settlement carved into\na large, natural cave.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1632), SetVariable("mapyframe", 352)]
                    action NullAction()
                elif (quarters+togreenmountaintribe) > world_daylength:
                    idle "map/greenmountaintribe01LOCKED.png"
                    hover "map/greenmountaintribe01hoverLOCKED.png"
                    hovered [tt4.Action("{color=#f6d6bd}The Tribe of The Green Mountain{/color}\n[map_icon1][map_icon3][map_icon5]An ancient settlement carved into\na large, natural cave.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_greenmountaintribe]"), SetVariable("mapxframe", 1632), SetVariable("mapyframe", 352)]
                    action NullAction()
                elif pc_hp < 1 and pc_area != "mountainroad" and pc_area != "greenmountaintribe":
                    idle "map/greenmountaintribe01LOCKED.png"
                    hover "map/greenmountaintribe01hoverLOCKED.png"
                    hovered [tt4.Action("{color=#f6d6bd}The Tribe of The Green Mountain{/color}\n[map_icon1][map_icon3][map_icon5]An ancient settlement carved into\na large, natural cave.\n{color=#6a6a6a}You’re too exhausted to climb up a mountain.{/color}"), SetVariable("mapxframe", 1632), SetVariable("mapyframe", 352)]
                    action NullAction()
                else:
                    idle "map/greenmountaintribe01.png"
                    hover "map/greenmountaintribe01hover.png"
                    hovered [tt4.Action("{color=#f6d6bd}The Tribe of The Green Mountain{/color}\n[map_icon1][map_icon3][map_icon5]An ancient settlement carved into\na large, natural cave.\nTravel time: [travel_duration_greenmountaintribe]"), SetVariable("mapxframe", 1632), SetVariable("mapyframe", 352)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "greenmountaintribe"), Jump("finaldestination")]
            if pc_area == "greenmountaintribe":
                add "map/flag.png" xpos 1585 ypos 354

        if huntercabin_unlocked and not huntercabin_firsttime:
            if (stonebridge_firsttime and foragingground_firsttime and tostonebridge <= toforagingground) or (stonebridge_firsttime and not foragingground_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1308
                    ypos 504
                    xalign 0.0
                    yalign 0.0
                    if tohuntercabin >= 100:
                        idle "images/map/arrows/upleftLOCKED.png"
                        hover "images/map/arrows/uplefthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1362), SetVariable("mapyframe", 524)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tohuntercabin) > (world_daylength-1):
                        idle "images/map/arrows/upleftLOCKED.png"
                        hover "images/map/arrows/uplefthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1362), SetVariable("mapyframe", 524)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/upleft.png"
                        hover "images/map/arrows/uplefthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1362), SetVariable("mapyframe", 524)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "huntercabin"), Jump("finaldestination")]
            if (foragingground_firsttime and stonebridge_firsttime and toforagingground <= tostonebridge) or (foragingground_firsttime and not stonebridge_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1196
                    ypos 448
                    xalign 0.0
                    yalign 0.0
                    if tohuntercabin >= 100:
                        idle "images/map/arrows/downrightLOCKED.png"
                        hover "images/map/arrows/downrighthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1256), SetVariable("mapyframe", 472)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tohuntercabin) > (world_daylength-1):
                        idle "images/map/arrows/downrightLOCKED.png"
                        hover "images/map/arrows/downrighthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1256), SetVariable("mapyframe", 472)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/downright.png"
                        hover "images/map/arrows/downrighthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1256), SetVariable("mapyframe", 472)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "huntercabin"), Jump("finaldestination")]
        elif huntercabin_firsttime:
            $ hours_huntercabin = (tohuntercabin / 4) % 24
            $ quarters_huntercabin = (tohuntercabin * 15) % 60
            $ travel_duration_huntercabin = ("%d:%02d" % (hours_huntercabin, quarters_huntercabin))
            imagebutton:
                focus_mask None
                xpos 1278
                ypos 457
                xalign 0.0
                yalign 0.0
                if encounter_spottedwolves == day:
                    idle "map/huntercabin01LOCKED.png"
                    hover "map/huntercabin01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Cabin{/color}\nAn uninhabited wooden structure built\nin a clearing near a rock face.\nYou need to wait for a day\nfor the spotted wolves to leave."), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 490)]
                    action NullAction()
                elif pc_area == "huntercabin":
                    idle "map/huntercabin01hover.png"
                    hover "map/huntercabin01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Cabin{/color}\nAn uninhabited wooden structure built\nin a clearing near a rock face.\nYou’re currently here."), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 490)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/huntercabin01LOCKED.png"
                    hover "map/huntercabin01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Cabin{/color}\nAn uninhabited wooden structure built\nin a clearing near a rock face.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 490)]
                    action NullAction()
                elif tohuntercabin >= 100:
                    idle "map/huntercabin01LOCKED.png"
                    hover "map/huntercabin01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Cabin{/color}\nAn uninhabited wooden structure built\nin a clearing near a rock face.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 490)]
                    action NullAction()
                elif (quarters+tohuntercabin) > world_daylength:
                    idle "map/huntercabin01LOCKED.png"
                    hover "map/huntercabin01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Cabin{/color}\nAn uninhabited wooden structure built\nin a clearing near a rock face.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_huntercabin]"), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 490)]
                    action NullAction()
                else:
                    idle "map/huntercabin01.png"
                    hover "map/huntercabin01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Cabin{/color}\nAn uninhabited wooden structure built\nin a clearing near a rock face.\nTravel time: [travel_duration_huntercabin]"), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 490)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "huntercabin"), Jump("finaldestination")]
            if pc_area == "huntercabin":
                add "map/flag.png" xpos 1247 ypos 461

        if foragingground_unlocked and not foragingground_firsttime:
            if (huntercabin_firsttime and wanderer_firsttime and tohuntercabin <= towanderer) or (huntercabin_firsttime and not wanderer_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1232
                    ypos 468
                    xalign 0.0
                    yalign 0.0
                    if toforagingground >= 100:
                        idle "images/map/arrows/upleftLOCKED.png"
                        hover "images/map/arrows/uplefthoverLOCKED.png"
                        hovered [tt3.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1220), SetVariable("mapyframe", 492)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+toforagingground) > (world_daylength-1):
                        idle "images/map/arrows/upleftLOCKED.png"
                        hover "images/map/arrows/uplefthoverLOCKED.png"
                        hovered [tt3.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1220), SetVariable("mapyframe", 492)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/upleft.png"
                        hover "images/map/arrows/uplefthover.png"
                        hovered [tt3.Action(""), SetVariable("mapxframe", 1220), SetVariable("mapyframe", 492)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "foragingground"), Jump("finaldestination")]
            if (wanderer_firsttime and huntercabin_firsttime and towanderer <= tohuntercabin) or (wanderer_firsttime and not huntercabin_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1148
                    ypos 376
                    xalign 0.0
                    yalign 0.0
                    if toforagingground >= 100:
                        idle "images/map/arrows/downrightLOCKED.png"
                        hover "images/map/arrows/downrighthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1204), SetVariable("mapyframe", 400)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+toforagingground) > (world_daylength-1):
                        idle "images/map/arrows/downrightLOCKED.png"
                        hover "images/map/arrows/downrighthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1204), SetVariable("mapyframe", 400)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/downright.png"
                        hover "images/map/arrows/downrighthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1204), SetVariable("mapyframe", 400)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "foragingground"), Jump("finaldestination")]
        elif foragingground_firsttime:
            $ hours_foragingground = (toforagingground / 4) % 24
            $ quarters_foragingground = (toforagingground * 15) % 60
            $ travel_duration_foragingground = ("%d:%02d" % (hours_foragingground, quarters_foragingground))
            if mapxframe == 1234:
                if foragingground_foraging_amount < 4:
                    $ map_icon1 = "{image=mapkeyx2food}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 1156
                ypos 384
                xalign 0.0
                yalign 0.0
                if pc_area == "foragingground":
                    idle "map/foragingground01hover.png"
                    hover "map/foragingground01hover.png"
                    if not foragingground_foraging_vein:
                        hovered [tt.Action("{color=#f6d6bd}The Foraging Grounds{/color}\n[map_icon1]A dry, rocky plain with sparse vegetation,\nand very few hideouts for predators.\nYou’re currently here."), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}Copper Ore?{/color}\nA possible spot for a mine\nat the edge of a foraging ground.\nYou’re currently here."), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/foragingground01LOCKED.png"
                    hover "map/foragingground01hoverLOCKED.png"
                    if not foragingground_foraging_vein:
                        hovered [tt.Action("{color=#f6d6bd}The Foraging Grounds{/color}\n[map_icon1]A dry, rocky plain with sparse vegetation,\nand very few hideouts for predators.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}Copper Ore?{/color}\nA possible spot for a mine\nat the edge of a foraging ground.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    action NullAction()
                elif toforagingground >= 100:
                    idle "map/foragingground01LOCKED.png"
                    hover "map/foragingground01hoverLOCKED.png"
                    if not foragingground_foraging_vein:
                        hovered [tt.Action("{color=#f6d6bd}The Foraging Grounds{/color}\n[map_icon1]A dry, rocky plain with sparse vegetation,\nand very few hideouts for predators.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}Copper Ore?{/color}\nA possible spot for a mine\nat the edge of a foraging ground.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    action NullAction()
                elif (quarters+toforagingground) > world_daylength:
                    idle "map/foragingground01LOCKED.png"
                    hover "map/foragingground01hoverLOCKED.png"
                    if not foragingground_foraging_vein:
                        hovered [tt.Action("{color=#f6d6bd}The Foraging Grounds{/color}\n[map_icon1]A dry, rocky plain with sparse vegetation,\nand very few hideouts for predators.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_foragingground]"), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}Copper Ore?{/color}\nA possible spot for a mine\nat the edge of a foraging ground.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_foragingground]"), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    action NullAction()
                else:
                    idle "map/foragingground01.png"
                    hover "map/foragingground01hover.png"
                    if not foragingground_foraging_vein:
                        hovered [tt.Action("{color=#f6d6bd}The Foraging Grounds{/color}\n[map_icon1]A dry, rocky plain with sparse vegetation,\nand very few hideouts for predators.\nTravel time: [travel_duration_foragingground]"), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}Copper Ore?{/color}\nA possible spot for a mine\nat the edge of a foraging ground.\nTravel time: [travel_duration_foragingground]"), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "foragingground"), Jump("finaldestination")]
            if pc_area == "foragingground":
                add "map/flag.png" xpos 1130 ypos 390

        if wanderer_unlocked and not wanderer_firsttime:
            if (foragingground_firsttime and foggylake_firsttime and toforagingground <= tofoggylake) or (foragingground_firsttime and not foggylake_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1120
                    ypos 344
                    xalign 0.0
                    yalign 0.0
                    if towanderer >= 100:
                        idle "images/map/arrows/upleftLOCKED.png"
                        hover "images/map/arrows/uplefthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1168), SetVariable("mapyframe", 364)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+towanderer) > (world_daylength-1):
                        idle "images/map/arrows/upleftLOCKED.png"
                        hover "images/map/arrows/uplefthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1168), SetVariable("mapyframe", 364)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/upleft.png"
                        hover "images/map/arrows/uplefthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1168), SetVariable("mapyframe", 364)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "wanderer"), Jump("finaldestination")]
            if (foggylake_firsttime and foragingground_firsttime and tofoggylake <= toforagingground) or (foggylake_firsttime and not foragingground_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1068
                    ypos 296
                    xalign 0.0
                    yalign 0.0
                    if towanderer >= 100:
                        idle "images/map/arrows/downLOCKED.png"
                        hover "images/map/arrows/downhoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1128), SetVariable("mapyframe", 320)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+towanderer) > (world_daylength-1):
                        idle "images/map/arrows/downLOCKED.png"
                        hover "images/map/arrows/downhoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1128), SetVariable("mapyframe", 320)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/down.png"
                        hover "images/map/arrows/downhover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1128), SetVariable("mapyframe", 320)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "wanderer"), Jump("finaldestination")]
        elif wanderer_firsttime:
            $ hours_wanderer = (towanderer / 4) % 24
            $ quarters_wanderer = (towanderer * 15) % 60
            $ travel_duration_wanderer = ("%d:%02d" % (hours_wanderer, quarters_wanderer))
            if mapxframe == 1160:
                $ map_icon1 = "{image=mapkeyx2watersource} "
                $ map_icon2 = "{image=mapkeyx2fishingspot}\n"
            imagebutton:
                focus_mask None
                xpos 1089
                ypos 291
                xalign 0.0
                yalign 0.0
                if pc_area == "wanderer":
                    idle "map/wanderer01hover.png"
                    hover "map/wanderer01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}[wanderer_name]{/color}\n[map_icon1][map_icon2]Made of stone,\nshe’s holding a long staff.\nYou’re currently here."), SetVariable("mapxframe", 1160), SetVariable("mapyframe", 322)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/wanderer01LOCKED.png"
                    hover "map/wanderer01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}[wanderer_name]{/color}\n[map_icon1][map_icon2]Made of stone,\nshe’s holding a long staff.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1160), SetVariable("mapyframe", 322)]
                    action NullAction()
                elif towanderer >= 100:
                    idle "map/wanderer01LOCKED.png"
                    hover "map/wanderer01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}[wanderer_name]{/color}\n[map_icon1][map_icon2]Made of stone,\nshe’s holding a long staff.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1160), SetVariable("mapyframe", 322)]
                    action NullAction()
                elif (quarters+towanderer) > world_daylength:
                    idle "map/wanderer01LOCKED.png"
                    hover "map/wanderer01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}[wanderer_name]{/color}\n[map_icon1][map_icon2]Made of stone,\nshe’s holding a long staff.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_wanderer]"), SetVariable("mapxframe", 1160), SetVariable("mapyframe", 322)]
                    action NullAction()
                else:
                    idle "map/wanderer01.png"
                    hover "map/wanderer01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}[wanderer_name]{/color}\n[map_icon1][map_icon2]Made of stone,\nshe’s holding a long staff.\nTravel time: [travel_duration_wanderer]"), SetVariable("mapxframe", 1160), SetVariable("mapyframe", 322)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "wanderer"), Jump("finaldestination")]
            if pc_area == "wanderer":
                add "map/flag.png" xpos 1105 ypos 303

        if foggylake_unlocked and not foggylake_firsttime:
            if (wanderer_firsttime and northernroad_firsttime and towanderer <= tonorthernroad) or (wanderer_firsttime and not northernroad_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1076
                    ypos 240
                    xalign 0.0
                    yalign 0.0
                    if tofoggylake >= 100:
                        idle "images/map/arrows/upLOCKED.png"
                        hover "images/map/arrows/uphoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1132), SetVariable("mapyframe", 272)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tofoggylake) > (world_daylength):
                        idle "images/map/arrows/upLOCKED.png"
                        hover "images/map/arrows/uphoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1132), SetVariable("mapyframe", 272)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/up.png"
                        hover "images/map/arrows/uphover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1132), SetVariable("mapyframe", 272)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "foggylake"), Jump("finaldestination")]
            if (northernroad_firsttime and wanderer_firsttime and tonorthernroad <= towanderer) or (northernroad_firsttime and not wanderer_firsttime):
                imagebutton:
                    focus_mask None
                    xpos 1029
                    ypos 249
                    xalign 0.0
                    yalign 0.0
                    if tofoggylake >= 100:
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1096), SetVariable("mapyframe", 270)]
                        action [Hide("map_display", transition=dissolve)]
                    elif (quarters+tofoggylake) > (world_daylength):
                        idle "images/map/arrows/rightLOCKED.png"
                        hover "images/map/arrows/righthoverLOCKED.png"
                        hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1096), SetVariable("mapyframe", 270)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/right.png"
                        hover "images/map/arrows/righthover.png"
                        hovered [tt.Action(""), SetVariable("mapxframe", 1096), SetVariable("mapyframe", 270)]
                        action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "foggylake"), Jump("finaldestination")]
        elif foggylake_firsttime:
            $ hours_foggylake = (tofoggylake / 4) % 24
            $ quarters_foggylake = (tofoggylake * 15) % 60
            $ travel_duration_foggylake = ("%d:%02d" % (hours_foggylake, quarters_foggylake))
            if mapxframe == 1113:
                if foggy_about_shelter:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if foggy_about_shelter:
                    $ map_icon2 = "{image=mapkeyx2dayrest} "
                else:
                    $ map_icon2 = ""
                if foggy_about_trade:
                    $ map_icon3 = "{image=mapkeyx2food} "
                else:
                    $ map_icon3 = ""
                if foggy_about_trade:
                    $ map_icon4 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon4 = ""
                if foggy_about_shelter or foggy_about_trade:
                    $ map_icon5 = "\n"
                else:
                    $ map_icon5 = ""
            imagebutton:
                focus_mask None
                xpos 1039
                ypos 220
                xalign 0.0
                yalign 0.0
                if pc_area == "foggylake":
                    idle "map/foggylake01hover.png"
                    hover "map/foggylake01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Foggy Lake{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5]The tavern set at the northern crossroads.\nA poorly protected shelter used by hunters and foragers.\nYou’re currently here."), SetVariable("mapxframe", 1113), SetVariable("mapyframe", 251)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/foggylake01LOCKED.png"
                    hover "map/foggylake01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Foggy Lake{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5]The tavern set at the northern crossroads.\nA poorly protected shelter used by hunters and foragers.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1113), SetVariable("mapyframe", 251)]
                    action NullAction()
                elif tofoggylake >= 100:
                    idle "map/foggylake01LOCKED.png"
                    hover "map/foggylake01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Foggy Lake{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5]The tavern set at the northern crossroads.\nA poorly protected shelter used by hunters and foragers.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1113), SetVariable("mapyframe", 251)]
                    action NullAction()
                elif (quarters+tofoggylake) > world_daylength:
                    idle "map/foggylake01LOCKED.png"
                    hover "map/foggylake01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Foggy Lake{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5]The tavern set at the northern crossroads.\nA poorly protected shelter used by hunters and foragers.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_foggylake]"), SetVariable("mapxframe", 1113), SetVariable("mapyframe", 251)]
                    action NullAction()
                else:
                    idle "map/foggylake01.png"
                    hover "map/foggylake01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Foggy Lake{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5]The tavern set at the northern crossroads.\nA poorly protected shelter used by hunters and foragers.\nTravel time: [travel_duration_foggylake]"), SetVariable("mapxframe", 1113), SetVariable("mapyframe", 251)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "foggylake"), Jump("finaldestination")]
            if pc_area == "foggylake":
                add "map/flag.png" xpos 1042 ypos 232

        if creeks_unlocked and not creeks_firsttime:
            imagebutton:
                focus_mask None
                xpos 1120
                ypos 224
                xalign 0.0
                yalign 0.0
                if tocreeks >= 100:
                    idle "images/map/arrows/rightLOCKED.png"
                    hover "images/map/arrows/righthoverLOCKED.png"
                    hovered [tt.Action("You can’t currently\nreach this area."), SetVariable("mapxframe", 1196), SetVariable("mapyframe", 248)]
                    action [Hide("map_display", transition=dissolve)]
                elif (quarters+tocreeks) > (world_daylength-1):
                    idle "images/map/arrows/rightLOCKED.png"
                    hover "images/map/arrows/righthoverLOCKED.png"
                    hovered [tt.Action("It’d be too late to explore\nan unfamiliar area."), SetVariable("mapxframe", 1196), SetVariable("mapyframe", 248)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "images/map/arrows/right.png"
                    hover "images/map/arrows/righthover.png"
                    hovered [tt.Action(""), SetVariable("mapxframe", 1196), SetVariable("mapyframe", 248)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "creeks"), Jump("finaldestination")]
        elif creeks_firsttime:
            $ hours_creeks = (tocreeks / 4) % 24
            $ quarters_creeks = (tocreeks * 15) % 60
            $ travel_duration_creeks = ("%d:%02d" % (hours_creeks, quarters_creeks))
            if mapxframe == 1278:
                if creeks_sleep_available:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if oldhava_about_trade:
                    $ map_icon3 = "{image=mapkeyx2food} "
                else:
                    $ map_icon3 = ""
                if creeks_mundanework:
                    $ map_icon4 = "{image=mapkeyx2mundanejob} "
                else:
                    $ map_icon4 = ""
                $ map_icon5 = "{image=mapkeyx2watersource}\n"
            imagebutton:
                focus_mask None
                xpos 1211
                ypos 102
                xalign 0.0
                yalign 0.0
                if pc_area == "creeks":
                    idle "map/creeks01hover.png"
                    hover "map/creeks01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Creeks{/color}\n[map_icon1][map_icon3][map_icon4][map_icon5]A young village of hunters and woodcutters\nplaced among a few brooks.\nYou’re currently here."), SetVariable("mapxframe", 1278), SetVariable("mapyframe", 134)]
                    action [Hide("map_display", transition=dissolve)]
                elif highisland_journey_inprogress == 1:
                    idle "map/creeks01LOCKED.png"
                    hover "map/creeks01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Creeks{/color}\n[map_icon1][map_icon3][map_icon4][map_icon5]A young village of hunters and woodcutters\nplaced among a few brooks.\n{color=#6a6a6a}You can’t reach this place\nwithout using the boat first.{/color}"), SetVariable("mapxframe", 1278), SetVariable("mapyframe", 134)]
                    action NullAction()
                elif tocreeks >= 100:
                    idle "map/creeks01LOCKED.png"
                    hover "map/creeks01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Creeks{/color}\n[map_icon1][map_icon3][map_icon4][map_icon5]A young village of hunters and woodcutters\nplaced among a few brooks.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1278), SetVariable("mapyframe", 134)]
                    action NullAction()
                elif (quarters+tocreeks) > world_daylength:
                    idle "map/creeks01LOCKED.png"
                    hover "map/creeks01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Creeks{/color}\n[map_icon1][map_icon3][map_icon4][map_icon5]A young village of hunters and woodcutters\nplaced among a few brooks.\n{color=#6a6a6a}You can’t get here before nightfall.{/color}\nTravel time: [travel_duration_creeks]"), SetVariable("mapxframe", 1278), SetVariable("mapyframe", 134)]
                    action NullAction()
                else:
                    idle "map/creeks01.png"
                    hover "map/creeks01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Creeks{/color}\n[map_icon1][map_icon3][map_icon4][map_icon5]A young village of hunters and woodcutters\nplaced among a few brooks.\nTravel time: [travel_duration_creeks]"), SetVariable("mapxframe", 1278), SetVariable("mapyframe", 134)]
                    action [Hide("map_display", transition=dissolve), SetVariable("travel_destination", "creeks"), Jump("finaldestination")]
            if pc_area == "creeks":
                add "map/flag.png" xpos 1226 ypos 102

        if banditshideout_firsttime:
            imagebutton:
                focus_mask None
                xpos 1033
                ypos 463
                xalign 0.0
                yalign 0.0
                if banditshideout_banned:
                    idle "map/banditshideout01LOCKED.png"
                    hover "map/banditshideout01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Hideout{/color}\nAn old woodcutters’ hamlet\nat the heart of an impenetrable forest.\n{color=#6a6a6a}Glaucia has threatened to\nkill you without questions.{/color}"), SetVariable("mapxframe", 1120), SetVariable("mapyframe", 496)]
                    action [Hide("map_display", transition=dissolve)]
                elif pc_area == "banditshideout":
                    idle "map/banditshideout01hover.png"
                    hover "map/banditshideout01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Hideout{/color}\nAn old woodcutters’ hamlet\nat the heart of an impenetrable forest."), SetVariable("mapxframe", 1120), SetVariable("mapyframe", 496)]
                    action [Hide("map_display", transition=dissolve)]
                else:
                    idle "map/banditshideout01LOCKED.png"
                    hover "map/banditshideout01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Hideout{/color}\nAn old woodcutters’ hamlet\nat the heart of an impenetrable forest.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1120), SetVariable("mapyframe", 496)]
                    action [Hide("map_display", transition=dissolve)]
            if pc_area == "banditshideout":
                add "map/flag.png" xpos 1072 ypos 464

        if quest_gatheracrew == 1 and quest_asterion == 1 and not asterion_found:
            if beach_firsttime:
                imagebutton:
                    focus_mask None
                    xpos 732
                    ypos 80
                    xalign 0.0
                    yalign 0.0
                    if not galerocks_navica_boat_bought:
                        idle "images/map/arrows/leftLOCKED.png"
                        hover "images/map/arrows/lefthoverLOCKED.png"
                        hovered [tt.Action("To reach {color=#f6d6bd}High Island{/color}, I’d need a boat."), SetVariable("mapxframe", 812), SetVariable("mapyframe", 106)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/left.png"
                        hover "images/map/arrows/lefthover.png"
                        hovered [tt.Action("I consider leaving for {color=#f6d6bd}High Island{/color}."), SetVariable("mapxframe", 812), SetVariable("mapyframe", 106)]
                        action [tt.Action(""), SetVariable("world_popupnarration_name", "highislandprep"), SetVariable("highisland_journey_startingpoint", "beach"), Show('world_popupnarration_box'), With(dissolve)]
            if fishinghamlet_firsttime and fishinghamlet_areas_seen_07:
                imagebutton:
                    focus_mask None
                    xpos 344
                    ypos 420
                    xalign 0.0
                    yalign 0.0
                    if not aegidia_about_highisland_recruitment_done and not aegidia_favor:
                        idle "images/map/arrows/upLOCKED.png"
                        hover "images/map/arrows/uphoverLOCKED.png"
                        hovered [tt.Action("To reach {color=#f6d6bd}High Island{/color}, I’d need a boat."), SetVariable("mapxframe", 400), SetVariable("mapyframe", 448)]
                        action [Hide("map_display", transition=dissolve)]
                    else:
                        idle "images/map/arrows/up.png"
                        hover "images/map/arrows/uphover.png"
                        hovered [tt.Action("I consider leaving for {color=#f6d6bd}High Island{/color}."), SetVariable("mapxframe", 400), SetVariable("mapyframe", 448)]
                        action [tt.Action(""), SetVariable("world_popupnarration_name", "highislandprep"), SetVariable("highisland_journey_startingpoint", "hamlet"), Show('world_popupnarration_box'), With(dissolve)]
        if mapxframe == 1176:
            if day >= southerncrossroads_wildplants_start and southerncrossroads_wildplants_left:
                $ map_icon1 = "{image=mapkeyx2food}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 1068:
            if peltnorth_resting:
                $ map_icon1 = "{image=mapkeyx2shelter} "
                $ map_icon2 = "{image=mapkeyx2dayrest} "
            else:
                $ map_icon1 = ""
                $ map_icon2 = ""
            if iason_shop or iason_food_berries == 2:
                $ map_icon3 = "{image=mapkeyx2food} "
            else:
                $ map_icon3 = ""
            if iason_shop or peltnorth_selling:
                $ map_icon4 = "{image=mapkeyx2goods} "
            else:
                $ map_icon4 = ""
            if peltnorth_armorer_abouttrade:
                $ map_icon5 = "{image=mapkeyx2tailor} "
            else:
                $ map_icon5 = ""
            $ map_icon6 = "{image=mapkeyx2watersource}\n"
        if mapxframe == 883:
            if ruinedvillage_part_river:
                $ map_icon1 = "{image=mapkeyx2watersource} {image=mapkeyx2fishingspot}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 634:
            if druidcave_cave_open:
                $ map_icon1 = "{image=mapkeyx2shelter}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 700:
            if howlersdell_eryx_about_room:
                $ map_icon1 = "{image=mapkeyx2shelter} "
                $ map_icon2 = "{image=mapkeyx2dayrest} "
            else:
                $ map_icon1 = ""
                $ map_icon2 = ""
            if howlersdell_eryx_about_shop:
                $ map_icon3 = "{image=mapkeyx2food} "
            else:
                $ map_icon3 = ""
            if akakios_shop_firsttime:
                $ map_icon4 = "{image=mapkeyx2goods} "
            else:
                $ map_icon4 = ""
            if howlersdell_bion_shop:
                $ map_icon5 = "{image=mapkeyx2tailor} "
            else:
                $ map_icon5 = ""
            if (howlersdell_mundanework_available and not howlersdell_mundanework_blocked):
                $ map_icon7 = "{image=mapkeyx2mundanejob} "
            else:
                $ map_icon7 = ""
            if howlersdell_eryx_about_room or howlersdell_eryx_about_shop or akakios_shop_firsttime or howlersdell_bion_shop or (howlersdell_mundanework_available and not howlersdell_mundanework_blocked):
                $ map_icon6 = "\n"
            else:
                $ map_icon6 = ""
        if mapxframe == 440:
            if fishinghamlet_areas_seen_07:
                $ map_icon1 = "{image=mapkeyx2watersource}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 644:
            if monastery_sleep_unlocked:
                $ map_icon1 = "{image=mapkeyx2shelter}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 804:
            if day >= 5:
                $ map_icon1 = "{image=mapkeyx2food}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 950:
            if thyrsus_shop:
                $ map_icon1 = "{image=mapkeyx2goods}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 840:
            if whitemarshes_rest_unlocked and not whitemarshes_attacked:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if helvius_about_buying and not whitemarshes_attacked:
                $ map_icon2 = "{image=mapkeyx2goods} "
            else:
                $ map_icon2 = ""
            if (whitemarshes_rest_unlocked and not whitemarshes_attacked) or (helvius_about_buying and not whitemarshes_attacked):
                $ map_icon3 = "\n"
            else:
                $ map_icon3 = ""
        if mapxframe == 940:
            if galerocks_fulvia_sleep:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if galerocks_porcia_firsttime:
                $ map_icon2 = "{image=mapkeyx2food} "
            else:
                $ map_icon2 = ""
            if galerocks_tatius_firsttime:
                $ map_icon3 = "{image=mapkeyx2goods} "
            else:
                $ map_icon3 = ""
            if galerocks_rufina_firsttime:
                $ map_icon4 = "{image=mapkeyx2tailor} "
            else:
                $ map_icon4 = ""
            if galerocks_aquila_firsttime:
                $ map_icon5 = "{image=mapkeyx2watersource} "
            else:
                $ map_icon5 = ""
            if galerocks_fulvia_sleep or galerocks_porcia_firsttime or galerocks_tatius_firsttime or galerocks_rufina_firsttime or galerocks_aquila_firsttime:
                $ map_icon6 = "\n"
            else:
                $ map_icon6 = ""
        if mapxframe == 808:
            if galerocks_photios_about_mundanejob:
                $ map_icon1 = "{image=mapkeyx2mundanejob} "
            else:
                $ map_icon1 = ""
            $ map_icon2 = "{image=mapkeyx2watersource}\n"
        if mapxframe == 1398:
            $ map_icon1 = "{image=mapkeyx2watersource}"
            $ map_icon2 = "{image=mapkeyx2fishingspot}\n"
        if mapxframe == 1442:
            if watchtower_open:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if day >= watchtower_wildplants_start and watchtower_wildplants_left:
                $ map_icon2 = "{image=mapkeyx2food} "
            else:
                $ map_icon2 = ""
            if watchtower_open or (day >= watchtower_wildplants_start and watchtower_wildplants_left):
                $ map_icon3 = "\n "
            else:
                $ map_icon3 = ""
        if mapxframe == 1552:
            if eudocia_sleep_available:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if eudocia_about_selling:
                $ map_icon2 = "{image=mapkeyx2goods} "
            else:
                $ map_icon2 = ""
            if eudocia_sleep_available or eudocia_about_selling:
                $ map_icon3 = "\n"
            else:
                $ map_icon3 = ""
        if mapxframe == 1496:
            if ghoulcave_wildplants_left:
                $ map_icon1 = "{image=mapkeyx2food} "
            else:
                $ map_icon1 = ""
            $ map_icon2 = "{image=mapkeyx2watersource} "
            $ map_icon3 = "{image=mapkeyx2fishingspot} "
            $ map_icon4 = "\n"
        if mapxframe == 1632:
            if greenmountaintribe_sleep:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if cephasgaiane_shop and not cephasgaiane_shop_dragonhorn:
                $ map_icon3 = "{image=mapkeyx2goods} "
            else:
                $ map_icon3 = ""
            if greenmountaintribe_sleep or (cephasgaiane_shop and not cephasgaiane_shop_dragonhorn):
                $ map_icon5 = "\n"
            else:
                $ map_icon5 = ""
        if mapxframe == 1234:
            if foragingground_foraging_amount < 4:
                $ map_icon1 = "{image=mapkeyx2food}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 1160:
            $ map_icon1 = "{image=mapkeyx2watersource} "
            $ map_icon2 = "{image=mapkeyx2fishingspot}\n"
        if mapxframe == 1113:
            if foggy_about_shelter:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if foggy_about_shelter:
                $ map_icon2 = "{image=mapkeyx2dayrest} "
            else:
                $ map_icon2 = ""
            if foggy_about_trade:
                $ map_icon3 = "{image=mapkeyx2food} "
            else:
                $ map_icon3 = ""
            if foggy_about_trade:
                $ map_icon4 = "{image=mapkeyx2goods} "
            else:
                $ map_icon4 = ""
            if foggy_about_shelter or foggy_about_trade:
                $ map_icon5 = "\n"
            else:
                $ map_icon5 = ""
        if mapxframe == 1278:
            if creeks_sleep_available:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if oldhava_about_trade:
                $ map_icon3 = "{image=mapkeyx2food} "
            else:
                $ map_icon3 = ""
            if creeks_mundanework:
                $ map_icon4 = "{image=mapkeyx2mundanejob} "
            else:
                $ map_icon4 = ""
            $ map_icon5 = "{image=mapkeyx2watersource}\n"
        if mapxframe == 1012:
            $ map_icon1 = "{image=mapkeyx2fishingspot}\n"

        imagebutton:
            idle "gui/clossingarrowidle.png"
            hover "gui/clossingarrowhover.png"
            focus_mask None
            action [Hide("map_display", transition=dissolve), SetVariable("tutorial_endgame", 0)]
            xalign 0.0
            yalign 0.0
            xpos 1818
            ypos 0
        if (weathermud and pc_area == "bogroad") or (weathermud and pc_area == "bogcrossroads") or (weathermud and pc_area == "peatfield") or (weathermud and pc_area == "whitemarshes"):
            frame:
                yalign 0.0
                xalign 0.5
                xpadding 16
                xpos 960
                ypos 4
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text "The wetlands get dangerous an hour earlier.\nThe muddy roads slow you down." text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text "The wetlands get dangerous an hour earlier.\nThe muddy roads slow you down." text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        elif weathermud:
            frame:
                yalign 0.0
                xalign 0.5
                xpadding 16
                xpos 960
                ypos 4
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text "The muddy roads slow you down." text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text "The muddy roads slow you down." text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        elif pc_area == "bogroad" or pc_area == "bogcrossroads" or pc_area == "peatfield" or pc_area == "whitemarshes":
            frame:
                yalign 0.0
                xalign 0.5
                xpadding 16
                xpos 960
                ypos 4
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text "The wetlands get dangerous an hour earlier." text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text "The wetlands get dangerous an hour earlier." text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        if tt.value != "":
            frame:
                yalign 0.5
                xpadding 16
                xpos mapxframe
                ypos mapyframe
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text tt.value text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text tt.value text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        if tt2.value != "":
            frame:
                yalign 0.0
                xalign 0.5
                xpadding 16
                xpos mapxframe
                ypos mapyframe
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text tt2.value text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text tt2.value text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        if tt3.value != "":
            frame:
                yalign 0.5
                xalign 1.0
                xpadding 16
                xpos mapxframe
                ypos mapyframe
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text tt3.value text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text tt3.value text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        if tt4.value != "":
            frame:
                yalign 1.0
                xalign 0.5
                xpadding 16
                xpos mapxframe
                ypos mapyframe
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text tt4.value text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text tt4.value text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        if tt5.value != "":
            frame:
                yalign 0.0
                xalign 1.0
                xpadding 16
                xpos mapxframe
                ypos mapyframe
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text tt5.value text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text tt5.value text_align 0.5 size 28 line_spacing 8 font "munro.ttf"

    if world_popupnarration_name == "highislandprep" or world_popupnarration_name == "highislandprep_selecting":
        key "game_menu" action [Hide("map_display", transition=dissolve), SetVariable("tutorial_endgame", 0), SetVariable("world_popupnarration_name", 0)]
    else:
        key "game_menu" action [Hide("map_display", transition=dissolve), SetVariable("tutorial_endgame", 0)]

####################### MAPA NIEAKTYWNA
screen map_onlyview():
    modal True
    #tag menu
    zorder 130
    default tt = Tooltip("")
    default tt2 = Tooltip("")
    default tt3 = Tooltip("")
    default tt4 = Tooltip("")
    default tt5 = Tooltip("")
    key "m" action [Hide('map_onlyview'), With(dissolve)]
    key "M" action [Hide('map_onlyview'), With(dissolve)]
    imagemap:
        ground "map/mapbase.png" at truecenter, map_dissolve
        add "map/mapparts/citytocrossroad.png" xpos 1074 ypos 914
        if dolmen_firsttime and fallentree_firsttime:
            add "map/mapparts/dolmentofallentree.png" xpos 1300 ypos 767
        if southerncrossroads_firsttime:
            add "map/mapparts/militarycamptosoutherncrossroads.png" xpos 1074 ypos 914
        if peltnorth_firsttime:
            add "map/mapparts/southerncrossroadstopeltnorth.png" xpos 971 ypos 856
        if dolmen_firsttime:
            add "map/mapparts/southerncrossroadstodolmen.png" xpos 1146 ypos 840
        if ruinedvillage_firsttime and beholder_firsttime:
            add "map/mapparts/ruinedvillagetobeholder.png" xpos 597 ypos 739
        if peltnorth_firsttime and ruinedvillage_firsttime:
            add "map/mapparts/peltnorthtoruinedvillage.png" xpos 780 ypos 815
        if beholder_firsttime and druidcave_firsttime:
            add "map/mapparts/beholdertodruidscave.png" xpos 552 ypos 786
        if watchtower_firsttime and fallentree_firsttime and eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            add "map/mapparts/fallentreetowatchtower_fixed.png" xpos 1386 ypos 625
        elif watchtower_firsttime and fallentree_firsttime:
            add "map/mapparts/fallentreetowatchtower.png" xpos 1386 ypos 625
        if watchtower_firsttime and eudocia_firsttime and eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            add "map/mapparts/watchtowertoeudocia_fixed.png" xpos 1375 ypos 616
        elif watchtower_firsttime and eudocia_firsttime:
            add "map/mapparts/watchtowertoeudocia.png" xpos 1375 ypos 616
        if watchtower_firsttime and stonebridge_firsttime and eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            add "map/mapparts/watchtowertostonebridge_fixed.png" xpos 1344 ypos 542
        elif watchtower_firsttime and stonebridge_firsttime:
            add "map/mapparts/watchtowertostonebridge.png" xpos 1344 ypos 542
        if stonesign_firsttime and not watchtower_firsttime and eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            add "map/mapparts/stonesigntowatchtoweralt_fixed.png" xpos 1291 ypos 617
        elif stonesign_firsttime and not watchtower_firsttime:
            add "map/mapparts/stonesigntowatchtoweralt.png" xpos 1291 ypos 617
        if watchtower_firsttime and stonesign_firsttime and eudocia_about_roadclearing_cleared and day > eudocia_about_roadclearing_cleared:
            add "map/mapparts/stonesigntowatchtower_fixed.png" xpos 1291 ypos 617
        elif watchtower_firsttime and stonesign_firsttime:
            add "map/mapparts/stonesigntowatchtower.png" xpos 1291 ypos 617
        if ghoulcave_firsttime and stonebridge_firsttime:
            add "map/mapparts/bridgetocave.png" xpos 1350 ypos 477
        if huntercabin_firsttime and stonebridge_firsttime:
            add "map/mapparts/bridgetocabin.png" xpos 1259 ypos 494
        if howlersdell_firsttime:
            add "map/mapparts/howlersdelltorockslidealt.png" xpos 479 ypos 514
        if beholder_firsttime and howlersdell_firsttime:
            add "map/mapparts/beholdertohowlersdell.png" xpos 597 ypos 601
        # if (howlersdell_firsttime and rockslide_firstblockade_seen and not rockslide_firstblockade_cleared) or (howlersdell_firsttime and rockslide_firstblockade_seen and rockslide_firstblockade_cleared and not rockslide_firsttime):
        #     add "map/mapparts/howlersdelltorockslideplusshrubs.png" xpos 479 ypos 514
        if howlersdell_firsttime and rockslide_firsttime:
            add "map/mapparts/howlersdelltorockslide.png" xpos 479 ypos 514
        if rockslide_firsttime and fishinghamlet_firsttime:
            add "map/mapparts/rockslidetofishinghamlet.png" xpos 358 ypos 492
        if howlersdell_firsttime and westerncrossroads_firsttime:
            add "map/mapparts/howlersdelltowesterncrossroads.png" xpos 653 ypos 471
        if westerncrossroads_firsttime and oldpagos_firsttime:
            add "map/mapparts/westerncrossroadstooldpagos.png" xpos 495 ypos 377
        if oldpagos_firsttime and monastery_firsttime:
            add "map/mapparts/oldpagostomonastery.png" xpos 499 ypos 332
        if westgate_firsttime and not westerncrossroads_firsttime:
            add "map/mapparts/westerncrossroadstowestgatealt.png" xpos 657 ypos 471
        if westerncrossroads_firsttime and westgate_firsttime:
            add "map/mapparts/westerncrossroadstowestgate.png" xpos 657 ypos 471
        if foggylake_firsttime and wanderer_firsttime:
            add "map/mapparts/wanderertofoggylake.png" xpos 1054 ypos 241
        if wanderer_firsttime and foragingground_firsttime:
            add "map/mapparts/foraginggroundtowanderer.png" xpos 1080 ypos 322
        if huntercabin_firsttime and foragingground_firsttime:
            add "map/mapparts/cabintoforagingground.png" xpos 1151 ypos 402
        if westerncrossroads_firsttime and ford_firsttime:
            add "map/mapparts/westerncrossroadstoford.png" xpos 622 ypos 340
        if ford_firsttime and bogentrance_firsttime:
            add "map/mapparts/fordtobogentrance.png" xpos 641 ypos 232
        if bogentrance_firsttime and bogcrossroads_firsttime:
            add "map/mapparts/bogentrancetobogcrossroads.png" xpos 746 ypos 253
        if bogentrance_firsttime and ruinedshelter_firsttime:
            add "map/mapparts/bogentrancetoruinedshelter.png" xpos 764 ypos 219
        if ruinedshelter_firsttime and northernroad_firsttime:
            add "map/mapparts/ruinedsheltertonorthernroad.png" xpos 880 ypos 223
        if howlerslair_firsttime:
            add "map/mapparts/northernroadtohowlerslair.png" xpos 946 ypos 240
        if northernroad_firsttime and foggylake_firsttime:
            add "map/mapparts/northernroadtofoggylake.png" xpos 962 ypos 237
        if northernroad_firsttime and foggylake_firsttime and wanderer_firsttime:
            add "map/mapparts/entirefoggylake.png" xpos 970 ypos 262
        if creeks_traveling:
            add "map/mapparts/foggylaketocreeks01.png" xpos 1076 ypos 192
        if creeks_traveling > 1:
            add "map/mapparts/foggylaketocreeks02.png" xpos 1151 ypos 133
        if foggylake_firsttime and oldtunnel_firsttime:
            add "map/mapparts/foggylaketooldtunnel.png" xpos 901 ypos 164
        if oldtunnel_firsttime and galerocks_firsttime:
            add "map/mapparts/oldtunneltogalerocks.png" xpos 870 ypos 108
        if galerocks_firsttime and beach_firsttime:
            add "map/mapparts/galerockstobeach.png" xpos 797 ypos 43
        if ghoulcave_firsttime and giantstatue_firsttime:
            add "map/mapparts/cavetogiantstatue.png" xpos 1494 ypos 435
        if giantstatue_firsttime and mountainroad_firsttime:
            add "map/mapparts/giantstatuetomountainroad.png" xpos 1562 ypos 410
        if mountainroad_firsttime and greenmountaintribe_firsttime:
            add "map/mapparts/mountainroadtogreenmountaintribe.png" xpos 1593 ypos 391
        if bogcrossroads_firsttime and bogroad_firsttime:
            add "map/mapparts/bogcrossroadstobogroad.png" xpos 787 ypos 276
        if bogroad_firsttime and peatfield_firsttime:
            add "map/mapparts/bogroadtopeatfield.png" xpos 831 ypos 277
        if whitemarshes_firsttime and peatfield_firsttime:
            add "map/mapparts/whitemarshestopeatfield.png" xpos 811 ypos 278
        if bogcrossroads_firsttime and vines_firsttime:
            add "map/mapparts/bogcrossroadstovines.png" xpos 752 ypos 304
        if vines_firsttime and whitemarshes_firsttime:
            add "map/mapparts/vinestowhitemarshes.png" xpos 752 ypos 304
        if shortcut_westernentrance_firsttime:
            add "map/mapparts/shortcut/westernentrance01.png" xpos 739 ypos 396
        if shortcut_ibex:
            add "map/mapparts/shortcut/westernentrance02.png" xpos 739 ypos 396
        if shortcut_deepforest_firsttime:
            add "map/mapparts/shortcut/deepforest01.png" xpos 883 ypos 428
        if shortcut_deepforest_babydragon:
            add "map/mapparts/shortcut/deepforest02.png" xpos 883 ypos 428
        if shortcut_deepforest_treant:
            add "map/mapparts/shortcut/deepforest03.png" xpos 883 ypos 428
        if shortcut_deepforest_frightape:
            add "map/mapparts/shortcut/deepforest04.png" xpos 883 ypos 428
        if shortcut_deepforest_fruitgrove:
            add "map/mapparts/shortcut/deepforest05.png" xpos 883 ypos 428
        if shortcut_cairn_firsttime:
            add "map/mapparts/shortcut/cairn01.png" xpos 965 ypos 461
        if shortcut_meadow_firsttime:
            add "map/mapparts/shortcut/cairn02.png" xpos 965 ypos 461
        if shortcut_banditshideout_road_firsttime:
            add "map/mapparts/shortcut/cairn03.png" xpos 965 ypos 461
        if shortcut_banditshideout_obstacle1:
            add "map/mapparts/shortcut/cairn04.png" xpos 965 ypos 461
        if shortcut_banditshideout_obstacle2:
            add "map/mapparts/shortcut/cairn05.png" xpos 965 ypos 461
        if shortcut_woodenroad_firsttime:
            add "map/mapparts/shortcut/woodenroad01.png" xpos 1036 ypos 490
        if shortcut_woodenroad_stoathunt:
            add "map/mapparts/shortcut/woodenroad02.png" xpos 1036 ypos 490
        if shortcut_woodenroad_fisheater:
            add "map/mapparts/shortcut/woodenroad03.png" xpos 1036 ypos 490
        if shortcut_woodenroad_horseaccident:
            add "map/mapparts/shortcut/woodenroad04.png" xpos 1036 ypos 490
        if shortcut_woodenroad_drinkingcat:
            add "map/mapparts/shortcut/woodenroad05.png" xpos 1036 ypos 490
        if shortcut_darkforest_firsttime:
            add "map/mapparts/shortcut/darkforest01.png" xpos 1130 ypos 515
        if shortcut_darkforest_bandit:
            add "map/mapparts/shortcut/darkforest02.png" xpos 1130 ypos 515
        if shortcut_darkforest_goblins:
            add "map/mapparts/shortcut/darkforest03.png" xpos 1130 ypos 515
        if shortcut_darkforest_bagontree:
            add "map/mapparts/shortcut/darkforest04.png" xpos 1130 ypos 515
        if shortcut_darkforest_birdfollower:
            add "map/mapparts/shortcut/darkforest05.png" xpos 1130 ypos 515
        if shortcut_easternentrance_firsttime:
            add "map/mapparts/shortcut/easternentrance01.png" xpos 1232 ypos 541
        if shortcut_easternentrance_gnolls:
            add "map/mapparts/shortcut/easternentrance02.png" xpos 1232 ypos 541

        vbox:
            xpos 21
            ypos 1058
            if persistent.textstyle == "basic":
                spacing 16
            if persistent.textstyle == "pixel":
                spacing 12
            xalign 0.0
            yalign 1.0
            if not showmapkey:
                hbox:
                    xpos 70
                    textbutton "Show Map Key":
                        action SetVariable("showmapkey", 1)
                        text_style "tutorial_button_text"
                        text_slow_cps False
                        if persistent.textstyle == "basic":
                            text_size 24
                        if persistent.textstyle == "pixel":
                            text_size 28
                    null height 10
            else:
                hbox:
                    xpos 107
                    textbutton "Map Key":
                        action SetVariable("showmapkey", 0)
                        text_style "tutorial_button_text"
                        text_slow_cps False
                        if persistent.textstyle == "basic":
                            text_size 24
                        if persistent.textstyle == "pixel":
                            text_size 28
                    null height 10
                hbox:
                    spacing 32
                    add "mapkeyx3shelter":
                        yalign 0.5
                    text "Nighttime shelter.":
                        yalign 0.5
                        if persistent.textstyle == "basic":
                            size 24
                        if persistent.textstyle == "pixel":
                            size 28
                if (peltnorth_firsttime and peltnorth_resting) or (howlersdell_firsttime and howlersdell_eryx_about_room) or (foggylake_firsttime and foggy_about_shelter):
                    hbox:
                        spacing 32
                        add "mapkeyx3dayrest":
                            yalign 0.5
                        text "Daytime rest.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (southerncrossroads_firsttime and day >= southerncrossroads_wildplants_start and southerncrossroads_wildplants_left) or (peltnorth_firsttime and iason_shop) or (peltnorth_firsttime and iason_food_berries == 2) or (howlersdell_firsttime and howlersdell_eryx_about_shop) or (bogentrance_firsttime and day >= 5) or (galerocks_firsttime and galerocks_porcia_firsttime) or (watchtower_firsttime and day >= watchtower_wildplants_start and watchtower_wildplants_left) or (ghoulcave_firsttime and ghoulcave_wildplants_left) or (foragingground_firsttime and foragingground_foraging_amount < 4) or (foggylake_firsttime and foggy_about_trade) or (creeks_firsttime and oldhava_about_trade):
                    hbox:
                        spacing 32
                        add "mapkeyx3food":
                            yalign 0.5
                        text "Meals or supplies.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (peltnorth_firsttime and iason_shop) or (peltnorth_firsttime and peltnorth_selling) or (howlersdell_firsttime or akakios_shop_firsttime) or (peatfield_firsttime or thyrsus_shop) or (galerocks_firsttime or galerocks_tatius_firsttime) or (eudocia_firsttime or eudocia_about_selling) or (greenmountaintribe_firsttime and cephasgaiane_shop and not cephasgaiane_shop_dragonhorn) or (foggylake_firsttime and foggy_about_trade):
                    hbox:
                        spacing 32
                        add "mapkeyx3goods":
                            yalign 0.5
                        text "Trader.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (peltnorth_firsttime and peltnorth_armorer_abouttrade) or (howlersdell_firsttime and howlersdell_bion_shop) or (galerocks_firsttime and galerocks_rufina_firsttime):
                    hbox:
                        spacing 32
                        add "mapkeyx3tailor":
                            yalign 0.5
                        text "Tailor.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (beach_firsttime and galerocks_photios_about_mundanejob) or (creeks_firsttime and creeks_mundanework) or (howlersdell_mundanework_available and not howlersdell_mundanework_blocked):
                    hbox:
                        spacing 32
                        add "mapkeyx3mundanejob":
                            yalign 0.5
                        text "Mundane job.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (peltnorth_firsttime) or (ruinedvillage_firsttime and ruinedvillage_part_river) or (fishinghamlet_firsttime and fishinghamlet_areas_seen_07) or (galerocks_firsttime and galerocks_aquila_firsttime) or (beach_firsttime) or (fallentree_firsttime) or (ghoulcave_firsttime) or (wanderer_firsttime) or (creeks_firsttime):
                    hbox:
                        spacing 32
                        add "mapkeyx3watersource":
                            yalign 0.5
                        text "Safe water source.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28
                if (ruinedvillage_firsttime and ruinedvillage_part_river) or (northernroad_firsttime) or (fallentree_firsttime) or (ghoulcave_firsttime and map_icon3) or (wanderer_firsttime):
                    hbox:
                        spacing 32
                        add "mapkeyx3fishingspot":
                            yalign 0.5
                        text "Fishing spot.":
                            yalign 0.5
                            if persistent.textstyle == "basic":
                                size 24
                            if persistent.textstyle == "pixel":
                                size 28

        if persistent.demomode and beholder_firsttime and watchtower_firsttime and druidcave_firsttime:
            frame:
                yalign 0.5
                xalign 0.5
                xpadding 16
                xpos 960
                ypos 440
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text "Most quests require a further journey to be completed,\nbut you’ve already explored every area that’s a part of this demo.\nThank you for your support!" text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text "Most quests require a further journey to be completed,\nbut you’ve already explored every area that’s a part of this demo.\nThank you for your support!" text_align 0.5 size 28 line_spacing 8 font "munro.ttf"

        imagebutton:
            focus_mask None
            xpos 1096
            ypos 968
            xalign 0.0
            yalign 0.0
            if pc_area == "militarycamp":
                if militarycamp_destroyed_firsttime:
                    idle "map/militarycampmap02hover.png"
                    hover "map/militarycampmap02hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Camp{/color}\n{image=mapkeyx2shelter}\nA ruined outpost,\nreclaimed by beasts.\nYou’re currently here."), SetVariable("mapxframe", 1170), SetVariable("mapyframe", 970)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/militarycampmap01hover.png"
                    hover "map/militarycampmap01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Tulia’s Camp{/color}\n{image=mapkeyx2shelter}\nA military outpost surrounded by a wooden wall,\nset in the middle of the valley.\nYou’re currently here."), SetVariable("mapxframe", 1170), SetVariable("mapyframe", 970)]
                    action [Hide("map_onlyview", transition=dissolve)]
            elif militarycamp_destroyed_firsttime:
                idle "map/militarycampmap02LOCKED.png"
                hover "map/militarycampmap02hoverLOCKED.png"
                hovered [tt.Action("{color=#f6d6bd}The Old Camp{/color}\n{image=mapkeyx2shelter}\nA ruined outpost,\nreclaimed by beasts.\nThere’s nothing else to find here."), SetVariable("mapxframe", 1170), SetVariable("mapyframe", 970)]
                action [Hide("map_onlyview", transition=dissolve)]
            else:
                idle "map/militarycampmap01.png"
                hover "map/militarycampmap01hover.png"
                hovered [tt.Action("{color=#f6d6bd}Tulia’s Camp{/color}\n{image=mapkeyx2shelter}\nA military outpost surrounded by a wooden wall,\nset in the middle of the valley."), SetVariable("mapxframe", 1170), SetVariable("mapyframe", 970)]
                action [Hide("map_onlyview", transition=dissolve)]
        if pc_area == "militarycamp":
            add "map/flag.png" xpos 1068 ypos 970

        if southerncrossroads_firsttime:
            if mapxframe == 1176:
                if day >= southerncrossroads_wildplants_start and southerncrossroads_wildplants_left:
                    $ map_icon1 = "{image=mapkeyx2food}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 1108
                ypos 878
                xalign 0.0
                yalign 0.0
                if pc_area == "southerncrossroads":
                    idle "map/crossroads01hover.png"
                    hover "map/crossroads01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Southern Crossroads{/color}\n[map_icon1]A point connecting the deep forests of the East,\nthe western wetlands, and the road to Hovlavan.\nYou’re currently here."), SetVariable("mapxframe", 1176), SetVariable("mapyframe", 906)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/crossroads01.png"
                    hover "map/crossroads01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Southern Crossroads{/color}\n[map_icon1]A point connecting the deep forests of the East,\nthe western wetlands, and the road to Hovlavan"), SetVariable("mapxframe", 1176), SetVariable("mapyframe", 906)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "southerncrossroads":
                add "map/flag.png" xpos 1090 ypos 882

########################################## WEST
        if peltnorth_firsttime:
            if mapxframe == 1068:
                if peltnorth_resting:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                    $ map_icon2 = "{image=mapkeyx2dayrest} "
                else:
                    $ map_icon1 = ""
                    $ map_icon2 = ""
                if iason_shop or iason_food_berries == 2:
                    $ map_icon3 = "{image=mapkeyx2food} "
                else:
                    $ map_icon3 = ""
                if iason_shop or peltnorth_selling:
                    $ map_icon4 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon4 = ""
                if peltnorth_armorer_abouttrade:
                    $ map_icon5 = "{image=mapkeyx2tailor} "
                else:
                    $ map_icon5 = ""
                $ map_icon6 = "{image=mapkeyx2watersource}\n"
            imagebutton:
                focus_mask None
                xpos 988
                ypos 828
                xalign 0.0
                yalign 0.0
                if pc_area == "peltnorth":
                    idle "map/peltnorth01hover.png"
                    hover "map/peltnorth01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Pelt of the North{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A massive inn surrounded by a wall.\nA shelter from monsters and highwaymen.\nYou’re currently here."), SetVariable("mapxframe", 1068), SetVariable("mapyframe", 866)]
                    action [Hide("map_onlyview", transition=dissolve)]
                elif peltnorth_ban_temp == day:
                    idle "map/peltnorth01LOCKED.png"
                    hover "map/peltnorth01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Pelt of the North{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A massive inn surrounded by a wall.\nA shelter from monsters and highwaymen.\nYou won’t be allowed to enter this place."), SetVariable("mapxframe", 1068), SetVariable("mapyframe", 866)]
                    action [Hide("map_onlyview", transition=dissolve)]
                elif peltnorth_ban_perm:
                    idle "map/peltnorth01LOCKED.png"
                    hover "map/peltnorth01hoverLOCKED.png"
                    hovered [tt.Action("You are banned from visiting {color=#f6d6bd}Pelt of the North{/color}."), SetVariable("mapxframe", 1068), SetVariable("mapyframe", 866)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/peltnorth01.png"
                    hover "map/peltnorth01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Pelt of the North{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A massive inn surrounded by a wall.\nA shelter from monsters and highwaymen."), SetVariable("mapxframe", 1068), SetVariable("mapyframe", 866)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "peltnorth":
                add "map/flag.png" xpos 954 ypos 840

        if ruinedvillage_firsttime:
            if dalit_about_goblins_timer and dalit_about_goblins_timer >= day:
                $ dalit_about_goblins_timer_display = (dalit_about_goblins_timer-day+1)
            if mapxframe == 883:
                if ruinedvillage_part_river:
                    $ map_icon1 = "{image=mapkeyx2watersource} {image=mapkeyx2fishingspot}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 811
                ypos 792
                xalign 0.0
                yalign 0.0
                if dalit_about_goblins_timer and dalit_about_goblins_timer >= day:
                    idle "map/ruinedvillage01LOCKED.png"
                    hover "map/ruinedvillage01hoverLOCKED.png"
                    if dalit_about_goblins_timer_display == 1:
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\nYou should stay away for [dalit_about_goblins_timer_display] more day\nwhile the hunters are on the job."), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\nYou should stay away for [dalit_about_goblins_timer_display] more days\nwhile the hunters are on the job."), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                    action NullAction()
                else:
                    if pc_area == "ruinedvillage":
                        idle "map/ruinedvillage01hover.png"
                        hover "map/ruinedvillage01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris.\nYou’re currently here."), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action [Hide("map_onlyview", transition=dissolve)]
                    else:
                        idle "map/ruinedvillage01.png"
                        hover "map/ruinedvillage01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}[ruinedvillage_name]{/color}\n[map_icon1]A once prosperous village,\nnow abandoned and full of debris. "), SetVariable("mapxframe", 883), SetVariable("mapyframe", 824)]
                        action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "ruinedvillage":
                add "map/flag.png" xpos 780 ypos 800

        if beholder_firsttime:
            imagebutton:
                focus_mask None
                xpos 598
                ypos 728
                xalign 0.0
                yalign 0.0
                if pc_area == "beholder":
                    idle "map/beholder01hover.png"
                    hover "map/beholder01hover.png"
                    if beholder_name_known:
                        hovered [tt.Action("{color=#f6d6bd}Beholder{/color}\nA large tree and a stone altar\nat the edge of the swamp.\nYou’re currently here."), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}The Large Tree{/color}\nA massive plant with no leaves\ngrowing near an altar.\nYou’re currently here."), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/beholder01.png"
                    hover "map/beholder01hover.png"
                    if beholder_name_known:
                        hovered [tt.Action("{color=#f6d6bd}Beholder{/color}\nA large tree and a stone altar\nat the edge of the swamp."), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}The Large Tree{/color}\nA massive plant with no leaves\ngrowing near an altar."), SetVariable("mapxframe", 664), SetVariable("mapyframe", 760)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "beholder":
                add "map/flag.png" xpos 570 ypos 720

        if druidcave_firsttime:
            if mapxframe == 634:
                if druidcave_cave_open:
                    $ map_icon1 = "{image=mapkeyx2shelter}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 562
                ypos 810
                xalign 0.0
                yalign 0.0
                if pc_area == "druidcave":
                    idle "map/druidcavehover.png"
                    hover "map/druidcavehover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Elders’ Cave{/color}\n[map_icon1]An old mine turned into a hamlet\nprotected by a metal door.\nYou’re currently here."), SetVariable("mapxframe", 634), SetVariable("mapyframe", 850)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/druidcave.png"
                    hover "map/druidcavehover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Elders’ Cave{/color}\n[map_icon1]An old mine turned into a hamlet\nprotected by a metal door."), SetVariable("mapxframe", 634), SetVariable("mapyframe", 850)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "druidcave":
                add "map/flag.png" xpos 540 ypos 820

        if howlersdell_firsttime:
            if mapxframe == 700:
                if howlersdell_eryx_about_room:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                    $ map_icon2 = "{image=mapkeyx2dayrest} "
                else:
                    $ map_icon1 = ""
                    $ map_icon2 = ""
                if howlersdell_eryx_about_shop:
                    $ map_icon3 = "{image=mapkeyx2food} "
                else:
                    $ map_icon3 = ""
                if akakios_shop_firsttime:
                    $ map_icon4 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon4 = ""
                if howlersdell_bion_shop:
                    $ map_icon5 = "{image=mapkeyx2tailor} "
                else:
                    $ map_icon5 = ""
                if (howlersdell_mundanework_available and not howlersdell_mundanework_blocked):
                    $ map_icon7 = "{image=mapkeyx2mundanejob} "
                else:
                    $ map_icon7 = ""
                if howlersdell_eryx_about_room or howlersdell_eryx_about_shop or akakios_shop_firsttime or howlersdell_bion_shop or (howlersdell_mundanework_available and not howlersdell_mundanework_blocked):
                    $ map_icon6 = "\n"
                else:
                    $ map_icon6 = ""
            imagebutton:
                focus_mask None
                xpos 626
                ypos 583
                xalign 0.0
                yalign 0.0
                if pc_area == "howlersdell":
                    idle "map/howlersdell01hover.png"
                    hover "map/howlersdell01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Howler’s Dell{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon7][map_icon6]A prosperous village of farmers\nand animal breeders.\nYou’re currently here."), SetVariable("mapxframe", 700), SetVariable("mapyframe", 620)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/howlersdell01.png"
                    hover "map/howlersdell01.png"
                    hovered [tt.Action("{color=#f6d6bd}Howler’s Dell{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon7][map_icon6]A prosperous village of farmers\nand animal breeders."), SetVariable("mapxframe", 700), SetVariable("mapyframe", 620)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "howlersdell":
                add "map/flag.png" xpos 599 ypos 590

        if (rockslide_firsttime and not rockslide_cleared) or (rockslide_firsttime and rockslide_cleared and pc_area == "rockslide"):
            imagebutton:
                focus_mask None
                xpos 492
                ypos 501
                xalign 0.0
                yalign 0.0
                if pc_area == "rockslide":
                    if not rockslide_cleared:
                        idle "map/rockslide01hover.png"
                        hover "map/rockslide01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}A Rockslide{/color}\nThe mountain pass leading to the sea,\nblocked by an earthquake.\nYou’re currently here."), SetVariable("mapxframe", 560), SetVariable("mapyframe", 530)]
                        action [Hide("map_onlyview", transition=dissolve)]
                    else:
                        idle "map/rockslide02.png"
                        hover "map/rockslide02hover.png"
                        hovered [tt.Action("A cleared mountain pass leading to the sea.\nYou’re currently here."), SetVariable("mapxframe", 560), SetVariable("mapyframe", 530)]
                        action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/rockslide01.png"
                    hover "map/rockslide01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}A Rockslide{/color}\nThe mountain pass leading to the sea,\nblocked by an earthquake."), SetVariable("mapxframe", 560), SetVariable("mapyframe", 530)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "rockslide":
                add "map/flag.png" xpos 458 ypos 504
        if pc_area == "rockslide2":
            add "map/flag.png" xpos 458 ypos 504
        if pc_area == "rockslide_firstblockade":
            add "map/flag.png" xpos 540 ypos 510

        if fishinghamlet_firsttime:
            if mapxframe == 440:
                if fishinghamlet_areas_seen_07:
                    $ map_icon1 = "{image=mapkeyx2watersource}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 366
                ypos 473
                xalign 0.0
                yalign 0.0
                if pc_area == "fishinghamlet":
                    idle "map/fishinghamlet01hover.png"
                    hover "map/fishinghamlet01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Fishing Hamlet{/color}\n[map_icon1]An abandoned settlement built\namong the coastal rocks.\nYou’re currently here."), SetVariable("mapxframe", 440), SetVariable("mapyframe", 500)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/fishinghamlet01.png"
                    hover "map/fishinghamlet01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Fishing Hamlet{/color}\n[map_icon1]An abandoned settlement built\namong the coastal rocks."), SetVariable("mapxframe", 440), SetVariable("mapyframe", 500)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "fishinghamlet":
                add "map/flag.png" xpos 408 ypos 452

        if westerncrossroads_firsttime:
            imagebutton:
                focus_mask None
                xpos 662
                ypos 451
                xalign 0.0
                yalign 0.0
                if pc_area == "westerncrossroads":
                    idle "map/westerncrossroads01hover.png"
                    hover "map/westerncrossroads01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Western Crossroads{/color}\nA well-kept path connecting\nthe major villages of the peninsula.\nYou’re currently here."), SetVariable("mapxframe", 722), SetVariable("mapyframe", 490)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/westerncrossroads01.png"
                    hover "map/westerncrossroads01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Western Crossroads{/color}\nA well-kept path connecting\nthe major villages of the peninsula."), SetVariable("mapxframe", 722), SetVariable("mapyframe", 490)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "westerncrossroads":
                add "map/flag.png" xpos 645 ypos 460

        if oldpagos_firsttime:
            imagebutton:
                focus_mask None
                xpos 509
                ypos 364
                xalign 0.0
                yalign 0.0
                if not encounter_pebbler_gone and encounter_pebbler_day == day:
                    idle "map/oldpagos01LOCKED.png"
                    hover "map/oldpagos01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}Old Págos{/color}\nA village of stonemasons and farmers\nset on the top of a hill,\nright near the sea.\n{color=#6a6a6a}The road there is currently blocked by a pebbler.{/color}"), SetVariable("mapxframe", 592), SetVariable("mapyframe", 400)]
                    action NullAction()
                else:
                    if pc_area == "oldpagos":
                        idle "map/oldpagos01hover.png"
                        hover "map/oldpagos01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}Old Págos{/color}\nA village of stonemasons and farmers\nset on the top of a hill,\nright near the sea.\nYou’re currently here.\nYou’re currently here."), SetVariable("mapxframe", 592), SetVariable("mapyframe", 400)]
                        action [Hide("map_onlyview", transition=dissolve)]
                    else:
                        idle "map/oldpagos01.png"
                        hover "map/oldpagos01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}Old Págos{/color}\nA village of stonemasons and farmers\nset on the top of a hill,\nright near the sea."), SetVariable("mapxframe", 592), SetVariable("mapyframe", 400)]
                        action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "oldpagos":
                add "map/flag.png" xpos 480 ypos 370

        if monastery_firsttime:
            if mapxframe == 644:
                if monastery_sleep_unlocked:
                    $ map_icon1 = "{image=mapkeyx2shelter}\n"
            imagebutton:
                focus_mask None
                xpos 568
                ypos 315
                xalign 0.0
                yalign 0.0
                if not encounter_pebbler_gone and encounter_pebbler_day == day:
                    idle "map/monastery01LOCKED.png"
                    hover "map/monastery01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}[monastery_name]{/color}\n[map_icon1]A hard-to-reach complex of caves\nturned into a dwelling by\nthe monks of an Order of Truth.\n{color=#6a6a6a}The road there is currently blocked by a pebbler.{/color}"), SetVariable("mapxframe", 644), SetVariable("mapyframe", 352)]
                    action NullAction()
                else:
                    if pc_area == "monastery":
                        idle "map/monastery01hover.png"
                        hover "map/monastery01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}[monastery_name]{/color}\n[map_icon1]A hard-to-reach complex of caves\nturned into a dwelling by\nthe monks of an Order of Truth.\nYou’re currently here."), SetVariable("mapxframe", 644), SetVariable("mapyframe", 352)]
                        action [Hide("map_onlyview", transition=dissolve)]
                    else:
                        idle "map/monastery01.png"
                        hover "map/monastery01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}[monastery_name]{/color}\nA hard-to-reach complex of caves\nturned into a dwelling by\nthe monks of an Order of Truth."), SetVariable("mapxframe", 644), SetVariable("mapyframe", 352)]
                        action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "monastery":
                add "map/flag.png" xpos 578 ypos 335

        if westgate_firsttime:
            imagebutton:
                focus_mask None
                xpos 749
                ypos 454
                xalign 0.0
                yalign 0.0
                if pc_area == "westgate":
                    idle "map/westgate01hover.png"
                    hover "map/westgate01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Gate{/color}\nAn unusual structure guarding\nthe path to the heart of the forest.\nYou’re currently here."), SetVariable("mapxframe", 820), SetVariable("mapyframe", 490)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/westgate01.png"
                    hover "map/westgate01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Gate{/color}\nAn unusual structure guarding\nthe path to the heart of the forest."), SetVariable("mapxframe", 820), SetVariable("mapyframe", 490)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "westgate":
                add "map/flag.png" xpos 730 ypos 454

        if ford_firsttime:
            imagebutton:
                focus_mask None
                xpos 646
                ypos 326
                xalign 0.0
                yalign 0.0
                if pc_area == "ford":
                    idle "map/ford01hover.png"
                    hover "map/ford01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons.\nYou’re currently here."), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/ford01.png"
                    hover "map/ford01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}A Ford{/color}\nA shallow crossing, broad enough for wagons."), SetVariable("mapxframe", 711), SetVariable("mapyframe", 355)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "ford":
                add "map/flag.png" xpos 608 ypos 305

        if bogentrance_firsttime:
            if mapxframe == 804:
                if day >= 5:
                    $ map_icon1 = "{image=mapkeyx2food}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 732
                ypos 238
                xalign 0.0
                yalign 0.0
                if pc_area == "bogentrance":
                    idle "map/bogentrance01hover.png"
                    hover "map/bogentrance01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Forest Garden{/color}\n[map_icon1]Once tamed part of the woods,\nnow neglected.\nYou’re currently here."), SetVariable("mapxframe", 804), SetVariable("mapyframe", 270)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/bogentrance01.png"
                    hover "map/bogentrance01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Forest Garden{/color}\n[map_icon1]Once tamed part of the woods,\nnow neglected."), SetVariable("mapxframe", 804), SetVariable("mapyframe", 270)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "bogentrance":
                add "map/flag.png" xpos 686 ypos 226

            if pc_area == "bogcrossroads":
                add "map/flag.png" xpos 760 ypos 280

            if pc_area == "bogroad":
                add "map/flag.png" xpos 830 ypos 264

        if peatfield_firsttime:
            if mapxframe == 950:
                if thyrsus_shop:
                    $ map_icon1 = "{image=mapkeyx2goods}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 878
                ypos 272
                xalign 0.0
                yalign 0.0
                if peatfield_firsttime_destroyed:
                    idle "map/peatfield01LOCKED.png"
                    hover "map/peatfield01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Peat Fields{/color}\nA peatland surrounded by bogs,\nabandoned and haunted."), SetVariable("mapxframe", 950), SetVariable("mapyframe", 298)]
                    action NullAction()
                elif pc_area == "peatfield":
                    idle "map/peatfield01hover.png"
                    hover "map/peatfield01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Peat Fields{/color}\n[map_icon1]A peatland surrounded by bogs.\nIt provides the locals with\nbricks and fuel.\nYou’re currently here."), SetVariable("mapxframe", 950), SetVariable("mapyframe", 298)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/peatfield01.png"
                    hover "map/peatfield01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Peat Fields{/color}\n[map_icon1]A peatland surrounded by bogs.\nIt provides the locals with\nbricks and fuel."), SetVariable("mapxframe", 950), SetVariable("mapyframe", 298)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "peatfield":
                add "map/flag.png" xpos 861 ypos 274

        if vines_firsttime:
            imagebutton:
                focus_mask None
                xpos 770
                ypos 301
                xalign 0.0
                yalign 0.0
                if (vines_open_sleep or vines_open_day == day or vines_perma_open) and not vines_perma_closed:
                    if pc_area == "vines":
                        idle "map/vines02hover.png"
                        hover "map/vines02hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\nYou’re currently here."), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action [Hide("map_onlyview", transition=dissolve)]
                    else:
                        idle "map/vines02.png"
                        hover "map/vines02hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs."), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action [Hide("map_onlyview", transition=dissolve)]
                else:
                    if pc_area == "vines":
                        idle "map/vines01hover.png"
                        hover "map/vines01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs.\nYou’re currently here."), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action [Hide("map_onlyview", transition=dissolve)]
                    else:
                        idle "map/vines01.png"
                        hover "map/vines01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Creepers{/color}\nA wall of plants that blocks\nthe road to the deeper bogs."), SetVariable("mapxframe", 837), SetVariable("mapyframe", 332)]
                        action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "vines":
                add "map/flag.png" xpos 770 ypos 288

        if whitemarshes_firsttime:
            if mapxframe == 840:
                if whitemarshes_rest_unlocked and not whitemarshes_attacked:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if helvius_about_buying and not whitemarshes_attacked:
                    $ map_icon2 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon2 = ""
                if (whitemarshes_rest_unlocked and not whitemarshes_attacked) or (helvius_about_buying and not whitemarshes_attacked):
                    $ map_icon3 = "\n"
                else:
                    $ map_icon3 = ""
            imagebutton:
                focus_mask None
                xpos 773
                ypos 346
                xalign 0.0
                yalign 0.0
                if whitemarshes_destroyed:
                    idle "map/whitemarshes02LOCKED.png"
                    hover "map/whitemarshes02hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Ruins of\nWhite Marshes{/color}\nOnce a struggling village,\nnow a lair of awoken shells,\nwaiting for their moment to strike."), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action NullAction()
                elif vines_perma_closed:
                    idle "map/whitemarshes01LOCKED.png"
                    hover "map/whitemarshes01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}White Marshes{/color}\n[map_icon1][map_icon2][map_icon3]A struggling village of\npeat gatherers and farmers,\nrecently thrown into chaos."), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action NullAction()
                elif pc_area == "whitemarshes":
                    idle "map/whitemarshes01hover.png"
                    hover "map/whitemarshes01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}White Marshes{/color}\n[map_icon1][map_icon2][map_icon3]A struggling village of\npeat gatherers and farmers.\nYou’re currently here."), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/whitemarshes01.png"
                    hover "map/whitemarshes01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}White Marshes{/color}\n[map_icon1][map_icon2][map_icon3]A struggling village of\npeat gatherers and farmers."), SetVariable("mapxframe", 840), SetVariable("mapyframe", 377)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "whitemarshes":
                add "map/flag.png" xpos 820 ypos 330

        if ruinedshelter_firsttime:
            imagebutton:
                focus_mask None
                xpos 864
                ypos 192
                xalign 0.0
                yalign 0.0
                if ruinedshelter_lefttobeasts:
                    idle "map/ruinedshelter01LOCKED.png"
                    hover "map/ruinedshelter01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}[ruinedshelter_name]{/color}\nA small hamlet inhabited by\na family of furry critters."), SetVariable("mapxframe", 934), SetVariable("mapyframe", 224)]
                    action NullAction()
                elif pc_area == "ruinedshelter":
                    idle "map/ruinedshelter01hover.png"
                    hover "map/ruinedshelter01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}[ruinedshelter_name]{/color}\nA small hamlet that could still be used\nas a stop for travelers.\nYou’re currently here."), SetVariable("mapxframe", 934), SetVariable("mapyframe", 224)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/ruinedshelter01.png"
                    hover "map/ruinedshelter01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}[ruinedshelter_name]{/color}\nA small hamlet that could still be used\nas a stop for travelers."), SetVariable("mapxframe", 934), SetVariable("mapyframe", 224)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "ruinedshelter":
                add "map/flag.png" xpos 876 ypos 202

        if northernroad_firsttime:
            $ map_icon1 = "{image=mapkeyx2fishingspot}\n"
            imagebutton:
                focus_mask None
                xpos 943
                ypos 249
                xalign 0.0
                yalign 0.0
                if pc_area == "northernroad":
                    idle "map/northernroad01hover.png"
                    hover "map/northernroad01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Northern Road{/color}\n[map_icon1]This well-traveled path is still maintained\neven though parts of it collapsed\ninto the lake.\nYou’re currently here."), SetVariable("mapxframe", 1012), SetVariable("mapyframe", 280)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/northernroad01.png"
                    hover "map/northernroad01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Northern Road{/color}\n[map_icon1]This well-traveled path is still maintained\neven though parts of it collapsed\ninto the lake."), SetVariable("mapxframe", 1012), SetVariable("mapyframe", 280)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "northernroad":
                add "map/flag.png" xpos 979 ypos 228
            if pc_area == "howlerslair":
                add "map/flag.png" xpos 954 ypos 210

        if oldtunnel_firsttime:
            imagebutton:
                focus_mask None
                xpos 933
                ypos 121
                xalign 0.0
                yalign 0.0
                if helvius_about_oldtunnel_paid == day:
                    idle "map/oldtunnel01LOCKED.png"
                    hover "map/oldtunnel01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nYou should stay away from it\nwhile it’s being explored by\nthe people of White Marshes."), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                    action NullAction()
                elif oldtunnel_inside_opened:
                    if pc_area == "oldtunnel":
                        idle "map/oldtunnel01hover.png"
                        hover "map/oldtunnel01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\nYou’re currently here."), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action [Hide("map_onlyview", transition=dissolve)]
                    else:
                        idle "map/oldtunnel01.png"
                        hover "map/oldtunnel01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain."), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action [Hide("map_onlyview", transition=dissolve)]
                else:
                    if pc_area == "oldtunnel":
                        idle "map/oldtunnel01hover.png"
                        hover "map/oldtunnel01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\nAs long as this place remains unexplored,\nyou have to take a detour.\nYou’re currently here."), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action [Hide("map_onlyview", transition=dissolve)]
                    else:
                        idle "map/oldtunnel01.png"
                        hover "map/oldtunnel01hover.png"
                        hovered [tt.Action("{color=#f6d6bd}The Old Tunnel{/color}\nAn adit carved into a tall mountain.\nAs long as this place remains unexplored,\nyou have to take a detour."), SetVariable("mapxframe", 1002), SetVariable("mapyframe", 152)]
                        action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "oldtunnel":
                add "map/flag.png" xpos 902 ypos 135

        if galerocks_firsttime:
            if mapxframe == 940:
                if galerocks_fulvia_sleep:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if galerocks_porcia_firsttime:
                    $ map_icon2 = "{image=mapkeyx2food} "
                else:
                    $ map_icon2 = ""
                if galerocks_tatius_firsttime:
                    $ map_icon3 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon3 = ""
                if galerocks_rufina_firsttime:
                    $ map_icon4 = "{image=mapkeyx2tailor} "
                else:
                    $ map_icon4 = ""
                if galerocks_aquila_firsttime:
                    $ map_icon5 = "{image=mapkeyx2watersource} "
                else:
                    $ map_icon5 = ""
                if galerocks_fulvia_sleep or galerocks_porcia_firsttime or galerocks_tatius_firsttime or galerocks_rufina_firsttime or galerocks_aquila_firsttime:
                    $ map_icon6 = "\n"
                else:
                    $ map_icon6 = ""
            imagebutton:
                focus_mask None
                xpos 868
                ypos 105
                xalign 0.0
                yalign 0.0
                if pc_area == "galerocks":
                    idle "map/galerocks01hover.png"
                    hover "map/galerocks01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Gale Rocks{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A crude, aged village\nof fishers and salt makers,\nplaced among the hills.\nYou’re currently here."), SetVariable("mapxframe", 940), SetVariable("mapyframe", 136)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/galerocks01.png"
                    hover "map/galerocks01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Gale Rocks{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5][map_icon6]A crude, aged village\nof fishers and salt makers,\nplaced among the hills."), SetVariable("mapxframe", 940), SetVariable("mapyframe", 136)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "galerocks":
                add "map/flag.png" xpos 831 ypos 114

        if beach_firsttime:
            if mapxframe == 808:
                if galerocks_photios_about_mundanejob:
                    $ map_icon1 = "{image=mapkeyx2mundanejob} "
                else:
                    $ map_icon1 = ""
                $ map_icon2 = "{image=mapkeyx2watersource}\n"
            imagebutton:
                focus_mask None
                xpos 826
                ypos 58
                xalign 0.0
                yalign 0.0
                if pc_area == "beach":
                    idle "map/beach01hover.png"
                    hover "map/beach01hover.png"
                    hovered [tt5.Action("{color=#f6d6bd}The Pier{/color}\n[map_icon1][map_icon2]A spot on the beach where the stones\nare spread enough for the fishers\nto depart on their boats.\nYou’re currently here."), SetVariable("mapxframe", 808), SetVariable("mapyframe", 16)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/beach01.png"
                    hover "map/beach01hover.png"
                    hovered [tt5.Action("{color=#f6d6bd}The Pier{/color}\n[map_icon1][map_icon2]A spot on the beach where the stones\nare spread enough for the fishers\nto depart on their boats."), SetVariable("mapxframe", 808), SetVariable("mapyframe", 16)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "beach":
                add "map/flag.png" xpos 870 ypos 38
            if pc_area == "beforebeach":
                add "map/flag.png" xpos 839 ypos 60

########################################## EAST
        if dolmen_firsttime:
            imagebutton:
                focus_mask None
                xpos 1248
                ypos 818
                xalign 0.0
                yalign 0.0
                if pc_area == "dolmen":
                    idle "map/dolmenmap01hover.png"
                    hover "map/dolmenmap01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Dolmen{/color}\nA stone chapel built centuries ago\nto provide shelter to wayfarers.\nYou’re currently here."), SetVariable("mapxframe", 1328), SetVariable("mapyframe", 846)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/dolmenmap01.png"
                    hover "map/dolmenmap01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Dolmen{/color}\nA stone chapel built centuries ago\nto provide shelter to wayfarers."), SetVariable("mapxframe", 1328), SetVariable("mapyframe", 846)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "dolmen":
                add "map/flag.png" xpos 1290 ypos 822

        if fallentree_firsttime:
            if mapxframe == 1398:
                $ map_icon1 = "{image=mapkeyx2watersource}"
                $ map_icon2 = "{image=mapkeyx2fishingspot}\n"
            imagebutton:
                focus_mask None
                xpos 1408
                ypos 768
                xalign 0.0
                yalign 0.0
                if not fallentree_cleared:
                    if pc_area == "fallentree":
                        idle "map/fallentree01hover.png"
                        hover "map/fallentree01hover.png"
                        hovered [tt3.Action("{color=#f6d6bd}A Fallen Tree{/color}\n[map_icon1][map_icon2]A blocked section of the road,\nimpassable for carts and wagons.\nCrossing it slows you down."), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action [Hide("map_onlyview", transition=dissolve)]
                    else:
                        idle "map/fallentree01.png"
                        hover "map/fallentree01hover.png"
                        hovered [tt3.Action("{color=#f6d6bd}A Fallen Tree{/color}\n[map_icon1][map_icon2]A blocked section of the road,\nimpassable for carts and wagons.\nCrossing it slows you down."), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action [Hide("map_onlyview", transition=dissolve)]
                else:
                    if pc_area == "fallentree":
                        idle "map/fallentree02hover.png"
                        hover "map/fallentree02hover.png"
                        hovered [tt3.Action("{color=#f6d6bd}The Riverside Turn{/color}\nThe tree was removed\nand the path is clear again."), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action [Hide("map_onlyview", transition=dissolve)]
                    else:
                        idle "map/fallentree02.png"
                        hover "map/fallentree02hover.png"
                        hovered [tt3.Action("{color=#f6d6bd}The Riverside Turn{/color}\nThe tree was removed\nand the path is clear again."), SetVariable("mapxframe", 1398), SetVariable("mapyframe", 810)]
                        action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "fallentree":
                add "map/flag.png" xpos 1360 ypos 750

        if watchtower_firsttime:
            if mapxframe == 1442:
                if watchtower_open:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if day >= watchtower_wildplants_start and watchtower_wildplants_left:
                    $ map_icon2 = "{image=mapkeyx2food} "
                else:
                    $ map_icon2 = ""
                if watchtower_open or (day >= watchtower_wildplants_start and watchtower_wildplants_left):
                    $ map_icon3 = "\n "
                else:
                    $ map_icon3 = ""
            imagebutton:
                focus_mask None
                xpos 1381
                ypos 623
                xalign 0.0
                yalign 0.0
                if pc_area == "watchtower":
                    idle "map/watchtowerhover.png"
                    hover "map/watchtowerhover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Abandoned Watchtower{/color}\n[map_icon1][map_icon2][map_icon3]An outpost built at the top\nof the hill, barely taller\nthan the nearby tree crowns."), SetVariable("mapxframe", 1442), SetVariable("mapyframe", 656)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/watchtower.png"
                    hover "map/watchtowerhover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Abandoned Watchtower{/color}\n[map_icon1][map_icon2][map_icon3]An outpost built at the top\nof the hill, barely taller\nthan the nearby tree crowns."), SetVariable("mapxframe", 1442), SetVariable("mapyframe", 656)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "watchtower":
                add "map/flag.png" xpos 1413 ypos 600

        if eudocia_firsttime:
            if mapxframe == 1552:
                if eudocia_sleep_available:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if eudocia_about_selling:
                    $ map_icon2 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon2 = ""
                if eudocia_sleep_available or eudocia_about_selling:
                    $ map_icon3 = "\n"
                else:
                    $ map_icon3 = ""
            imagebutton:
                focus_mask None
                xpos 1519
                ypos 597
                xalign 0.0
                yalign 0.0
                if pc_area == "eudociahouse" or pc_area == "eudociahouseinside":
                    idle "map/eudociahouse01hover.png"
                    hover "map/eudociahouse01hover.png"
                    hovered [tt2.Action("{color=#f6d6bd}The Secluded Residence{/color}\n[map_icon1][map_icon2][map_icon3]A small, but luxurious hamlet,\nfor some reason spared by wild beasts."), SetVariable("mapxframe", 1552), SetVariable("mapyframe", 664)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/eudociahouse01.png"
                    hover "map/eudociahouse01hover.png"
                    hovered [tt2.Action("{color=#f6d6bd}The Secluded Residence{/color}\n[map_icon1][map_icon2][map_icon3]A small, but luxurious hamlet,\nfor some reason spared by wild beasts."), SetVariable("mapxframe", 1552), SetVariable("mapyframe", 664)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "eudociahouse" or pc_area == "eudociahouseinside":
                add "map/flag.png" xpos 1540 ypos 600

        if stonebridge_firsttime:
            imagebutton:
                focus_mask None
                xpos 1353
                ypos 537
                xalign 0.0
                yalign 0.0
                if pc_area == "stonebridge":
                    idle "map/stonebridge01hover.png"
                    hover "map/stonebridge01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Bridge{/color}\nA single stone slab\nplaced over a streambed.\nYou’re currently here."), SetVariable("mapxframe", 1424), SetVariable("mapyframe", 564)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/stonebridge01.png"
                    hover "map/stonebridge01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Old Bridge{/color}\nA single stone slab\nplaced over a streambed."), SetVariable("mapxframe", 1424), SetVariable("mapyframe", 564)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "stonebridge":
                add "map/flag.png" xpos 1349 ypos 509

        if stonesign_firsttime:
            imagebutton:
                focus_mask None
                xpos 1283
                ypos 615
                xalign 0.0
                yalign 0.0
                if pc_area == "stonesign":
                    idle "map/stonesign01hover.png"
                    hover "map/stonesign01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}A Woodland Edge{/color}\nA path leading to the heart of the forest.\nThe red stone tells travelers to turn back.\nYou’re currently here."), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 654)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/stonesign01.png"
                    hover "map/stonesign01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}A Woodland Edge{/color}\nA path leading to the heart of the forest.\nThe red stone tells travelers to turn back."), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 654)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "stonesign":
                add "map/flag.png" xpos 1318 ypos 613

        if ghoulcave_firsttime:
            if mapxframe == 1496:
                if ghoulcave_wildplants_left:
                    $ map_icon1 = "{image=mapkeyx2food} "
                else:
                    $ map_icon1 = ""
                $ map_icon2 = "{image=mapkeyx2watersource} "
                $ map_icon3 = "{image=mapkeyx2fishingspot} "
                $ map_icon4 = "\n"
            imagebutton:
                focus_mask None
                xpos 1456
                ypos 442
                xalign 0.0
                yalign 0.0
                if pc_area == "ghoulcave":
                    idle "map/ghoulcave01hover.png"
                    hover "map/ghoulcave01hover.png"
                    hovered [tt2.Action("{color=#f6d6bd}A Small Cave{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4]A dubious cave entrance\nfound on a forgotten path.\nYou’re currently here."), SetVariable("mapxframe", 1496), SetVariable("mapyframe", 512)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/ghoulcave01.png"
                    hover "map/ghoulcave01hover.png"
                    hovered [tt2.Action("{color=#f6d6bd}A Small Cave{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4]A dubious cave entrance\nfound on a forgotten path."), SetVariable("mapxframe", 1496), SetVariable("mapyframe", 512)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "ghoulcave":
                add "map/flag.png" xpos 1483 ypos 442

        if giantstatue_firsttime:
            imagebutton:
                focus_mask None
                xpos 1543
                ypos 386
                xalign 0.0
                yalign 0.0
                if greenmountaintribe_banned:
                    if not giantstatue_awoken:
                        idle "map/giantstatue01LOCKED.png"
                        hover "map/giantstatue01hoverLOCKED.png"
                    else:
                        idle "map/giantstatue02LOCKED.png"
                        hover "map/giantstatue02hoverLOCKED.png"
                    hovered [tt3.Action("{color=#f6d6bd}The Giant{/color}\nA centuries old monument\nportraying a huge man with a club.\n{color=#6a6a6a}If The Tribe of The Green Mountain\nfinds you here, you’ll be executed.{/color}"), SetVariable("mapxframe", 1533), SetVariable("mapyframe", 416)]
                    action NullAction()
                elif pc_area == "giantstatue":
                    if not giantstatue_awoken:
                        idle "map/giantstatue01hover.png"
                        hover "map/giantstatue01hover.png"
                    else:
                        idle "map/giantstatue02hover.png"
                        hover "map/giantstatue02hover.png"
                    hovered [tt3.Action("{color=#f6d6bd}The Giant{/color}\nA centuries old monument\nportraying a huge man with a club.\nYou’re currently here."), SetVariable("mapxframe", 1533), SetVariable("mapyframe", 416)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    if not giantstatue_awoken:
                        idle "map/giantstatue01.png"
                        hover "map/giantstatue01hover.png"
                    else:
                        idle "map/giantstatue02.png"
                        hover "map/giantstatue02hover.png"
                    hovered [tt3.Action("{color=#f6d6bd}The Giant{/color}\nA centuries old monument\nportraying a huge man with a club."), SetVariable("mapxframe", 1533), SetVariable("mapyframe", 416)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "giantstatue":
                add "map/flag.png" xpos 1516 ypos 400

        if mountainroad_firsttime:
            imagebutton:
                focus_mask None
                xpos 1584
                ypos 401
                xalign 0.0
                yalign 0.0
                if greenmountaintribe_banned:
                    if mountainroad_egg_broken:
                        idle "map/mountainroad02LOCKED.png"
                        hover "map/mountainroad02hoverLOCKED.png"
                    elif mountainroad_egg_gone:
                        idle "map/mountainroad03LOCKED.png"
                        hover "map/mountainroad03hoverLOCKED.png"
                    else:
                        idle "map/mountainroad01LOCKED.png"
                        hover "map/mountainroad01hoverLOCKED.png"
                    hovered [tt3.Action("{color=#f6d6bd}A Nest{/color}\nA winding, but wide path\nleading into the eastern mountains.\n{color=#6a6a6a}If The Tribe of The Green Mountain\nfinds you here, you’ll be executed.{/color}"), SetVariable("mapxframe", 1590), SetVariable("mapyframe", 433)]
                    action NullAction()
                elif pc_area == "mountainroad":
                    if mountainroad_egg_broken:
                        idle "map/mountainroad02hover.png"
                        hover "map/mountainroad02hover.png"
                    elif mountainroad_egg_gone:
                        idle "map/mountainroad03hover.png"
                        hover "map/mountainroad03hover.png"
                    else:
                        idle "map/mountainroad01hover.png"
                        hover "map/mountainroad01hover.png"
                    hovered [tt3.Action("{color=#f6d6bd}A Nest{/color}\nA winding, but wide path\nleading into the eastern mountains.\nYou’re currently here."), SetVariable("mapxframe", 1590), SetVariable("mapyframe", 433)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    if mountainroad_egg_broken:
                        idle "map/mountainroad02.png"
                        hover "map/mountainroad02hover.png"
                    elif mountainroad_egg_gone:
                        idle "map/mountainroad03.png"
                        hover "map/mountainroad03hover.png"
                    else:
                        idle "map/mountainroad01.png"
                        hover "map/mountainroad01hover.png"
                    hovered [tt3.Action("{color=#f6d6bd}A Nest{/color}\nA winding, but wide path\nleading into the eastern mountains."), SetVariable("mapxframe", 1590), SetVariable("mapyframe", 433)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "mountainroad":
                add "map/flag.png" xpos 1615 ypos 382

        if greenmountaintribe_firsttime:
            if mapxframe == 1632:
                if greenmountaintribe_sleep:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if cephasgaiane_shop and not cephasgaiane_shop_dragonhorn:
                    $ map_icon3 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon3 = ""
                if greenmountaintribe_sleep or (cephasgaiane_shop and not cephasgaiane_shop_dragonhorn):
                    $ map_icon5 = "\n"
                else:
                    $ map_icon5 = ""
            imagebutton:
                focus_mask None
                xpos 1602
                ypos 355
                xalign 0.0
                yalign 0.0
                if greenmountaintribe_banned:
                    idle "map/greenmountaintribe01LOCKED.png"
                    hover "map/greenmountaintribe01hoverLOCKED.png"
                    hovered [tt4.Action("{color=#f6d6bd}The Tribe of The Green Mountain{/color}\nAn ancient settlement carved into\na large, natural cave.\n{color=#6a6a6a}You would be executed\nupon arrival.{/color}"), SetVariable("mapxframe", 1632), SetVariable("mapyframe", 352)]
                    action NullAction()
                elif pc_area == "greenmountaintribe":
                    idle "map/greenmountaintribe01hover.png"
                    hover "map/greenmountaintribe01hover.png"
                    hovered [tt4.Action("{color=#f6d6bd}The Tribe of The Green Mountain{/color}\n[map_icon1][map_icon3][map_icon5]An ancient settlement carved into\na large, natural cave.\nYou’re currently here."), SetVariable("mapxframe", 1632), SetVariable("mapyframe", 352)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/greenmountaintribe01.png"
                    hover "map/greenmountaintribe01hover.png"
                    hovered [tt4.Action("{color=#f6d6bd}The Tribe of The Green Mountain{/color}\n[map_icon1][map_icon3][map_icon5]An ancient settlement carved into\na large, natural cave."), SetVariable("mapxframe", 1632), SetVariable("mapyframe", 352)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "greenmountaintribe":
                add "map/flag.png" xpos 1585 ypos 354

        if huntercabin_firsttime:
            imagebutton:
                focus_mask None
                xpos 1278
                ypos 457
                xalign 0.0
                yalign 0.0
                if pc_area == "huntercabin":
                    idle "map/huntercabin01hover.png"
                    hover "map/huntercabin01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Cabin{/color}\nAn uninhabited wooden structure built\nin a clearing near a rock face.\nYou’re currently here."), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 490)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/huntercabin01.png"
                    hover "map/huntercabin01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Cabin{/color}\nAn uninhabited wooden structure built\nin a clearing near a rock face."), SetVariable("mapxframe", 1348), SetVariable("mapyframe", 490)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "huntercabin":
                add "map/flag.png" xpos 1247 ypos 461

        if foragingground_firsttime:
            if mapxframe == 1234:
                if foragingground_foraging_amount < 4:
                    $ map_icon1 = "{image=mapkeyx2food}\n"
                else:
                    $ map_icon1 = ""
            imagebutton:
                focus_mask None
                xpos 1156
                ypos 384
                xalign 0.0
                yalign 0.0
                if pc_area == "foragingground":
                    idle "map/foragingground01hover.png"
                    hover "map/foragingground01hover.png"
                    if not foragingground_foraging_vein:
                        hovered [tt.Action("{color=#f6d6bd}The Foraging Grounds{/color}\n[map_icon1]A dry, rocky plain with sparse vegetation,\nand very few hideouts for predators.\nYou’re currently here."), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}Copper Ore?{/color}\nA possible spot for a mine\nat the edge of a foraging ground.\nYou’re currently here."), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/foragingground01.png"
                    hover "map/foragingground01hover.png"
                    if not foragingground_foraging_vein:
                        hovered [tt.Action("{color=#f6d6bd}The Foraging Grounds{/color}\n[map_icon1]A dry, rocky plain with sparse vegetation,\nand very few hideouts for predators."), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    else:
                        hovered [tt.Action("{color=#f6d6bd}Copper Ore?{/color}\nA possible spot for a mine\nat the edge of a foraging ground."), SetVariable("mapxframe", 1234), SetVariable("mapyframe", 415)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "foragingground":
                add "map/flag.png" xpos 1130 ypos 390

        if wanderer_firsttime:
            if mapxframe == 1160:
                $ map_icon1 = "{image=mapkeyx2watersource} "
                $ map_icon2 = "{image=mapkeyx2fishingspot}\n"
            imagebutton:
                focus_mask None
                xpos 1089
                ypos 291
                xalign 0.0
                yalign 0.0
                if pc_area == "wanderer":
                    idle "map/wanderer01hover.png"
                    hover "map/wanderer01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}[wanderer_name]{/color}\n[map_icon1][map_icon2]Made of stone,\nshe’s holding a long staff.\nYou’re currently here."), SetVariable("mapxframe", 1160), SetVariable("mapyframe", 322)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/wanderer01.png"
                    hover "map/wanderer01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}[wanderer_name]{/color}\n[map_icon1][map_icon2]Made of stone,\nshe’s holding a long staff."), SetVariable("mapxframe", 1160), SetVariable("mapyframe", 322)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "wanderer":
                add "map/flag.png" xpos 1105 ypos 303

        if foggylake_firsttime:
            if mapxframe == 1113:
                if foggy_about_shelter:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if foggy_about_shelter:
                    $ map_icon2 = "{image=mapkeyx2dayrest} "
                else:
                    $ map_icon2 = ""
                if foggy_about_trade:
                    $ map_icon3 = "{image=mapkeyx2food} "
                else:
                    $ map_icon3 = ""
                if foggy_about_trade:
                    $ map_icon4 = "{image=mapkeyx2goods} "
                else:
                    $ map_icon4 = ""
                if foggy_about_shelter or foggy_about_trade:
                    $ map_icon5 = "\n"
                else:
                    $ map_icon5 = ""
            imagebutton:
                focus_mask None
                xpos 1039
                ypos 220
                xalign 0.0
                yalign 0.0
                if pc_area == "foggylake":
                    idle "map/foggylake01hover.png"
                    hover "map/foggylake01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Foggy Lake{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5]The tavern set at the northern crossroads.\nA poorly protected shelter used by hunters and foragers.\nYou’re currently here."), SetVariable("mapxframe", 1113), SetVariable("mapyframe", 251)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/foggylake01.png"
                    hover "map/foggylake01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Foggy Lake{/color}\n[map_icon1][map_icon2][map_icon3][map_icon4][map_icon5]The tavern set at the northern crossroads.\nA poorly protected shelter used by hunters and foragers."), SetVariable("mapxframe", 1113), SetVariable("mapyframe", 251)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "foggylake":
                add "map/flag.png" xpos 1042 ypos 232

        if creeks_firsttime:
            if mapxframe == 1278:
                if creeks_sleep_available:
                    $ map_icon1 = "{image=mapkeyx2shelter} "
                else:
                    $ map_icon1 = ""
                if oldhava_about_trade:
                    $ map_icon3 = "{image=mapkeyx2food} "
                else:
                    $ map_icon3 = ""
                if creeks_mundanework:
                    $ map_icon4 = "{image=mapkeyx2mundanejob} "
                else:
                    $ map_icon4 = ""
                $ map_icon5 = "{image=mapkeyx2watersource}\n"
            imagebutton:
                focus_mask None
                xpos 1211
                ypos 102
                xalign 0.0
                yalign 0.0
                if pc_area == "creeks":
                    idle "map/creeks01hover.png"
                    hover "map/creeks01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Creeks{/color}\n[map_icon1][map_icon3][map_icon4][map_icon5]A young village of hunters and woodcutters\nplaced among a few brooks.\nYou’re currently here."), SetVariable("mapxframe", 1278), SetVariable("mapyframe", 134)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/creeks01.png"
                    hover "map/creeks01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}Creeks{/color}\n[map_icon1][map_icon3][map_icon4][map_icon5]A young village of hunters and woodcutters\nplaced among a few brooks."), SetVariable("mapxframe", 1278), SetVariable("mapyframe", 134)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "creeks":
                add "map/flag.png" xpos 1226 ypos 102

        if banditshideout_firsttime:
            imagebutton:
                focus_mask None
                xpos 1033
                ypos 463
                xalign 0.0
                yalign 0.0
                if banditshideout_banned:
                    idle "map/banditshideout01LOCKED.png"
                    hover "map/banditshideout01hoverLOCKED.png"
                    hovered [tt.Action("{color=#f6d6bd}The Hideout{/color}\nAn old woodcutters’ hamlet\nat the heart of an impenetrable forest.\n{color=#6a6a6a}Glaucia has threatened to\nkill you without questions.{/color}"), SetVariable("mapxframe", 1120), SetVariable("mapyframe", 496)]
                    action [Hide("map_onlyview", transition=dissolve)]
                elif pc_area == "banditshideout":
                    idle "map/banditshideout01hover.png"
                    hover "map/banditshideout01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Hideout{/color}\nAn old woodcutters’ hamlet\nat the heart of an impenetrable forest."), SetVariable("mapxframe", 1120), SetVariable("mapyframe", 496)]
                    action [Hide("map_onlyview", transition=dissolve)]
                else:
                    idle "map/banditshideout01.png"
                    hover "map/banditshideout01hover.png"
                    hovered [tt.Action("{color=#f6d6bd}The Hideout{/color}\nAn old woodcutters’ hamlet\nat the heart of an impenetrable forest.\n{color=#6a6a6a}The only path to this place you know of\nleads through the heart of the forest.{/color}"), SetVariable("mapxframe", 1120), SetVariable("mapyframe", 496)]
                    action [Hide("map_onlyview", transition=dissolve)]
            if pc_area == "banditshideout":
                add "map/flag.png" xpos 1072 ypos 464

        if pc_area == "griffonsroad01":
            add "map/flag.png" xpos 1106 ypos 906

        if mapxframe == 1176:
            if day >= southerncrossroads_wildplants_start and southerncrossroads_wildplants_left:
                $ map_icon1 = "{image=mapkeyx2food}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 1068:
            if peltnorth_resting:
                $ map_icon1 = "{image=mapkeyx2shelter} "
                $ map_icon2 = "{image=mapkeyx2dayrest} "
            else:
                $ map_icon1 = ""
                $ map_icon2 = ""
            if iason_shop or iason_food_berries == 2:
                $ map_icon3 = "{image=mapkeyx2food} "
            else:
                $ map_icon3 = ""
            if iason_shop or peltnorth_selling:
                $ map_icon4 = "{image=mapkeyx2goods} "
            else:
                $ map_icon4 = ""
            if peltnorth_armorer_abouttrade:
                $ map_icon5 = "{image=mapkeyx2tailor} "
            else:
                $ map_icon5 = ""
            $ map_icon6 = "{image=mapkeyx2watersource}\n"
        if mapxframe == 883:
            if ruinedvillage_part_river:
                $ map_icon1 = "{image=mapkeyx2watersource} {image=mapkeyx2fishingspot}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 634:
            if druidcave_cave_open:
                $ map_icon1 = "{image=mapkeyx2shelter}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 700:
            if howlersdell_eryx_about_room:
                $ map_icon1 = "{image=mapkeyx2shelter} "
                $ map_icon2 = "{image=mapkeyx2dayrest} "
            else:
                $ map_icon1 = ""
                $ map_icon2 = ""
            if howlersdell_eryx_about_shop:
                $ map_icon3 = "{image=mapkeyx2food} "
            else:
                $ map_icon3 = ""
            if akakios_shop_firsttime:
                $ map_icon4 = "{image=mapkeyx2goods} "
            else:
                $ map_icon4 = ""
            if howlersdell_bion_shop:
                $ map_icon5 = "{image=mapkeyx2tailor} "
            else:
                $ map_icon5 = ""
            if (howlersdell_mundanework_available and not howlersdell_mundanework_blocked):
                $ map_icon7 = "{image=mapkeyx2mundanejob} "
            else:
                $ map_icon7 = ""
            if howlersdell_eryx_about_room or howlersdell_eryx_about_shop or akakios_shop_firsttime or howlersdell_bion_shop or (howlersdell_mundanework_available and not howlersdell_mundanework_blocked):
                $ map_icon6 = "\n"
            else:
                $ map_icon6 = ""
        if mapxframe == 440:
            if fishinghamlet_areas_seen_07:
                $ map_icon1 = "{image=mapkeyx2watersource}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 644:
            if monastery_sleep_unlocked:
                $ map_icon1 = "{image=mapkeyx2shelter}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 804:
            if day >= 5:
                $ map_icon1 = "{image=mapkeyx2food}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 950:
            if thyrsus_shop:
                $ map_icon1 = "{image=mapkeyx2goods}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 840:
            if whitemarshes_rest_unlocked and not whitemarshes_attacked:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if helvius_about_buying and not whitemarshes_attacked:
                $ map_icon2 = "{image=mapkeyx2goods} "
            else:
                $ map_icon2 = ""
            if (whitemarshes_rest_unlocked and not whitemarshes_attacked) or (helvius_about_buying and not whitemarshes_attacked):
                $ map_icon3 = "\n"
            else:
                $ map_icon3 = ""
        if mapxframe == 940:
            if galerocks_fulvia_sleep:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if galerocks_porcia_firsttime:
                $ map_icon2 = "{image=mapkeyx2food} "
            else:
                $ map_icon2 = ""
            if galerocks_tatius_firsttime:
                $ map_icon3 = "{image=mapkeyx2goods} "
            else:
                $ map_icon3 = ""
            if galerocks_rufina_firsttime:
                $ map_icon4 = "{image=mapkeyx2tailor} "
            else:
                $ map_icon4 = ""
            if galerocks_aquila_firsttime:
                $ map_icon5 = "{image=mapkeyx2watersource} "
            else:
                $ map_icon5 = ""
            if galerocks_fulvia_sleep or galerocks_porcia_firsttime or galerocks_tatius_firsttime or galerocks_rufina_firsttime or galerocks_aquila_firsttime:
                $ map_icon6 = "\n"
            else:
                $ map_icon6 = ""
        if mapxframe == 808:
            if galerocks_photios_about_mundanejob:
                $ map_icon1 = "{image=mapkeyx2mundanejob} "
            else:
                $ map_icon1 = ""
            $ map_icon2 = "{image=mapkeyx2watersource}\n"
        if mapxframe == 1398:
            $ map_icon1 = "{image=mapkeyx2watersource}"
            $ map_icon2 = "{image=mapkeyx2fishingspot}\n"
        if mapxframe == 1442:
            if watchtower_open:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if day >= watchtower_wildplants_start and watchtower_wildplants_left:
                $ map_icon2 = "{image=mapkeyx2food} "
            else:
                $ map_icon2 = ""
            if watchtower_open or (day >= watchtower_wildplants_start and watchtower_wildplants_left):
                $ map_icon3 = "\n "
            else:
                $ map_icon3 = ""
        if mapxframe == 1552:
            if eudocia_sleep_available:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if eudocia_about_selling:
                $ map_icon2 = "{image=mapkeyx2goods} "
            else:
                $ map_icon2 = ""
            if eudocia_sleep_available or eudocia_about_selling:
                $ map_icon3 = "\n"
            else:
                $ map_icon3 = ""
        if mapxframe == 1496:
            if ghoulcave_wildplants_left:
                $ map_icon1 = "{image=mapkeyx2food} "
            else:
                $ map_icon1 = ""
            $ map_icon2 = "{image=mapkeyx2watersource} "
            $ map_icon3 = "{image=mapkeyx2fishingspot} "
            $ map_icon4 = "\n"
        if mapxframe == 1632:
            if greenmountaintribe_sleep:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if cephasgaiane_shop and not cephasgaiane_shop_dragonhorn:
                $ map_icon3 = "{image=mapkeyx2goods} "
            else:
                $ map_icon3 = ""
            if greenmountaintribe_sleep or (cephasgaiane_shop and not cephasgaiane_shop_dragonhorn):
                $ map_icon5 = "\n"
            else:
                $ map_icon5 = ""
        if mapxframe == 1234:
            if foragingground_foraging_amount < 4:
                $ map_icon1 = "{image=mapkeyx2food}\n"
            else:
                $ map_icon1 = ""
        if mapxframe == 1160:
            $ map_icon1 = "{image=mapkeyx2watersource} "
            $ map_icon2 = "{image=mapkeyx2fishingspot}\n"
        if mapxframe == 1113:
            if foggy_about_shelter:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if foggy_about_shelter:
                $ map_icon2 = "{image=mapkeyx2dayrest} "
            else:
                $ map_icon2 = ""
            if foggy_about_trade:
                $ map_icon3 = "{image=mapkeyx2food} "
            else:
                $ map_icon3 = ""
            if foggy_about_trade:
                $ map_icon4 = "{image=mapkeyx2goods} "
            else:
                $ map_icon4 = ""
            if foggy_about_shelter or foggy_about_trade:
                $ map_icon5 = "\n"
            else:
                $ map_icon5 = ""
        if mapxframe == 1278:
            if creeks_sleep_available:
                $ map_icon1 = "{image=mapkeyx2shelter} "
            else:
                $ map_icon1 = ""
            if oldhava_about_trade:
                $ map_icon3 = "{image=mapkeyx2food} "
            else:
                $ map_icon3 = ""
            if creeks_mundanework:
                $ map_icon4 = "{image=mapkeyx2mundanejob} "
            else:
                $ map_icon4 = ""
            $ map_icon5 = "{image=mapkeyx2watersource}\n"
        if mapxframe == 1012:
            $ map_icon1 = "{image=mapkeyx2fishingspot}\n"

        imagebutton:
            idle "gui/clossingarrowidle.png"
            hover "gui/clossingarrowhover.png"
            focus_mask None
            action [Hide("map_onlyview", transition=dissolve)]
            xalign 0.0
            yalign 0.0
            xpos 1818
            ypos 0
        #down and left
        if tt.value != "":
            frame:
                yalign 0.5
                xpadding 16
                xpos mapxframe
                ypos mapyframe
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text tt.value text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text tt.value text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        if tt2.value != "":
            frame:
                yalign 0.0
                xalign 0.5
                xpadding 16
                xpos mapxframe
                ypos mapyframe
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text tt2.value text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text tt2.value text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        if tt3.value != "":
            frame:
                yalign 0.5
                xalign 1.0
                xpadding 16
                xpos mapxframe
                ypos mapyframe
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text tt3.value text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text tt3.value text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        if tt4.value != "":
            frame:
                yalign 1.0
                xalign 0.5
                xpadding 16
                xpos mapxframe
                ypos mapyframe
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text tt4.value text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text tt4.value text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
        if tt5.value != "":
            frame:
                yalign 0.0
                xalign 1.0
                xpadding 16
                xpos mapxframe
                ypos mapyframe
                if persistent.textstyle == "basic":
                    top_padding 10 bottom_padding 4
                    text tt5.value text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
                if persistent.textstyle == "pixel":
                    top_padding 8 bottom_padding 4
                    text tt5.value text_align 0.5 size 28 line_spacing 8 font "munro.ttf"

    key "game_menu" action Hide("map_onlyview", transition=dissolve)
