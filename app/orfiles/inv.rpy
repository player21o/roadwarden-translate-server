################################################################################
## Initialization
################################################################################

init offset = -1

###################### Items / Inventory
default item_all_merch = 0
default item_all_misc = 0
default item_all_tools = 0

### consumables
default item_rations = 2
default item_chicken = 0
default item_wildplants = 0
default item_spiritrock = 0
default item_generichealingpotion = 0
default item_magicfruit = 0
default item_magicfruit_lost = 0
default item_potiondolmen = 0
default item_potiondolmen_known = 0
default item_smallhealingpotion = 0
default item_sharpeningpotion = 0
default item_sharpeningpotion_used = 0 # day

### useful for combat
default item_gambeson01 = 1
default item_gambeson02 = 0

default item_asterionspear = 0
default item_axe01 = 0
default item_axe02 = 0
default item_axe02alt = 0
default item_axehead = 0
default item_axeset = 0
default item_axe03 = 0
default item_crossbow = 0
default item_crossbowquarrels = 0
default item_mountainroadspear = 0
default item_shield = 0 # 1 - kite, 2 - rounded
default item_golemglove = 0
default item_trollurine = 0
# default item_machete = 0

default item_blindingpowder = 0

### useful for other special interactions
default item_bonehook = 0 # + rope
default item_dragonhorn = 0
default item_lantern = 0
default item_magicchisel = 0 #0 - no, 1 - regular, 2 - changed by Eudocia
default item_travelequipment = 1
default item_witheringdust = 0
default item_machete = 0

default item_gambesonrepairset = 0
default item_sewingkit = 0

### quest items
default item_arrow = 0
default item_boxfromdolmen = 0
default item_peltnorthberries = 0
default item_empresscarp = 0
default item_empresscarp_timelimit = 0
default item_snakebait = 0
default item_snakebait_truth = 0
default item_oceannecklace = 0
default item_bronzerod = 0
default item_magicpens = 0

default item_asterionkey = 0
default item_oldtunnelkey = 0
default item_trapdoorkeydolmen = 0
default item_watchtowerkey = 0
default item_piershedkey = 0
default item_oldtunnesmallkey = 0

default item_bonebuckle = 0
default item_bonebuckle_returned = 0
default item_boneearring = 0
default item_brokenknife = 0
default item_rawhide = 0
default item_pileofbones = 0
default item_pileofbones_returned = 0
default item_pileofbones_destroyed = 0
default item_pileofbones_sold = 0
default item_signpost = 0
default item_casket = 0
default item_casket_tested = 0
default item_letterwhitemarshes = 0
default item_letterwhitemarshes_read = 0

### merchandise
default coins = 5
default item_peltnorthberryclaw = 0
default item_peltnorthberrytools = 0
default item_elkfur = 0
default item_harepelt = 0
default item_sealskin = 0
default item_asterionwine = 0
default item_asterionwine_pcknows_1 = 0
default item_asterionwine_pcknows_2 = 0

default item_antlers = 0
default item_asterionbow = 0
default item_boartusks = 0
default item_bonering = 0
default item_cidercask = 0
default item_furlesswolftrophy = 0 # 1 - owned
default item_furlesswolftrophy_day = 0
default item_griffonegg = 0
default item_ironscraps = 0
default item_linen = 0
default item_dragonlingpaw = 0
default item_dragonlingclaws = 0
default item_spidersilk = 0
default item_stoat = 0 # 1 - owned, bad quality, 2 - owned, good quality
default item_stoat_day = 0
default item_wingedhourglass = 0
default item_wingedhourglass_worn = 0
default item_wingedhourglass_taboo_broken = 0

### other / trash
default item_cloak01 = 0
default item_horse = 0
default item_horse_coat = 0
default item_mageamulets = 0
default item_scholaringredients = 0
default item_writinginstruments = 0
default item_rope = 0

default item_bogfriend = 0
default item_blackwoundwort = 0
default item_ghoulblood = 0
default item_marshbules = 0
default item_powderedrock = 0
default item_rocktobepowdered = 0
default item_shortcutherbs = 0
default item_spidervenom = 0
default item_driftwood = 0
default item_cursedsoil = 0
default item_cavemushroom = 0

default item_thyrsusgift = 0
default item_stingointment = 0
default item_asterioncloak = 0
default item_asterionpurse = 0
default item_asteriontablet = 0
default item_asteriontablet_read = 0
default item_beholderroot = 0
default item_bugrepellent = 0
default item_earplugs = 0
default item_goblinspear = 0
default item_howlersdelltoken = 0
default item_magicalsapling = 0
default item_thaisletter = 0
default item_thaisletter_opened = 0
default item_thaisletter_read = 0
default item_thaisletter_readingblocked = 0
default item_teethset = 0 # hazel, cloves, salt
default item_teethset_type = "hazelnut" # apple, hazelnut, oak, willow, walnut
default item_soap = 0
default item_perfume = 0
default item_perfume_type = "Cherry"
default item_fancyclothes = 0
default item_rawfish_gaining = 0
default item_rawfish_losing = 0
default item_rawfishtotalnumber = 0
default item_rawfish01 = 0
default item_rawfish02 = 0
default item_rawfish03 = 0
default item_rawfish04 = 0
default item_rawfish05 = 0
default item_rawfish06 = 0
default item_rawfish07 = 0
default item_rawfish08 = 0
default item_rawfish09 = 0
default item_rawfish10 = 0
default item_fishtrap = 0
default item_cookedfish = 0
default item_ironingot = 0
default item_ironingot_sold_whitemarshes = 0
default item_ironingot_sold_howlers = 0
default item_ironingot_sold_pelt = 0
default item_ironingot_sold_greenmountain = 0
default item_ironingot_sold_galerocks = 0
default item_spices = 0

#####
default item_detailedmenu = 0

default item_hover_foodrations = 0
default item_hover_potiondolmen = 0
default item_hover_magicfruit = 0
default item_hover_coinscouple = 0
default item_hover_ironscraps = 0
default item_hover_furs = 0
default item_hover_berriespeltnorth = 0
default item_hover_dragonlingclaws = 0
default item_hover_clawpeltnorth = 0
default item_hover_wingedhourglass = 0
default item_hover_keys3item = 0
default item_hover_horse1 = 0
default item_hover_axe01 = 0
default item_hover_axe02 = 0
default item_hover_axe03 = 0
default item_hover_crossbow = 0
default item_hover_cloak = 0
default item_hover_gambeson = 0
default item_hover_rope = 0
default item_hover_amuletsmage = 0
default item_hover_scholaringredients = 0
default item_hover_potionsscholar = 0
default item_hover_writinginstruments = 0
default item_hover_boxfromdolmenitem = 0
default item_hover_toolsberries = 0
default item_hover_dragonlingpaw = 0
default item_hover_goblinrepellent = 0
default item_hover_empresscarp = 0
default item_hover_arrow = 0
default item_hover_bugrepellent = 0
default item_hover_witheringdust = 0
default item_hover_magicpens = 0
default item_hover_bronzerod = 0
default item_hover_eudociaflower = 0
default item_hover_asterionbow = 0
default item_hover_asterionspear = 0
default item_hover_smallhealingpotion = 0
default item_hover_sharpeningpotion = 0
default item_hover_asterionpurse = 0
default item_hover_spiritrock = 0
default asterionitem_hover_cloak = 0
default asterionwineitem_hover = 0
default spidersilkitem_hover = 0
default linenitem_hover = 0
default teethsetitem_hover = 0
default howlersdelltokenitem_hover = 0
default thaisletteritem_hover = 0
default oceannecklaceitem_hover = 0
default asteriontabletitem_hover = 0
default magicchiselitem_hover = 0
default generichealingpotionitem_hover = 0
default shielditem_hover = 0
default furlesswolftrophyitem_hover = 0
default stoatitem_hover = 0
default boartusksitem_hover = 0
default boneringitem_hover = 0
default scholarpotionsitem_hover = 0
default bonehookitem_hover = 0
default crossbowquarrelsitem_hover = 0
default travelequipmentitem_hover = 0
default brokenknifeitem_hover = 0
default magicalsaplingitem_hover = 0
default cidercaskitem_hover = 0
default goblinspearitem_hover = 0
default chickenitem_hover = 0
default blindingpowderitem_hover = 0
default boneearringitem_hover = 0
default axe02altitem_hover = 0
default axeheaditem_hover = 0
default axesetitem_hover = 0
default antlersitem_hover = 0
default mountainroadspearitem_hover = 0
default stingointmentitem_hover = 0
default lanternitem_hover = 0
default lostmanblanketitem_hover = 0
default rawfishitem_hover = 0
default earplugsitem_hover = 0
default fishtrapitem_hover = 0
default dragonhornitem_hover = 0
default bonebuckleitem_hover = 0
default pileofbonesitem_hover = 0
default beholderrootitem_hover = 0
default cookedfishitem_hover = 0
default fancyclothesitem_hover = 0
default gambesonrepairsetitem_hover = 0
default sewingkititem_hover = 0
default wildplantsitem_hover = 0
default signpostitem_hover = 0
default ironingotitem_hover = 0
default spicesitem_hover = 0
default macheteitem_hover = 0
default ghoulblooditem_hover = 0
default item_hover_cavemushroom = 0
default item_hover_golemglove = 0
default item_hover_casket = 0
default griffoneggitem_hover = 0
default pc_goal_lost100coins_hover = 0
default letterwhitemarshes_hover = 0
default item_hover_thyrsusgift = 0

#### INVENTORY
default inventory = False
default inventoryscreenmode = "list" #/"details"
style inventory_label:
    xalign 0.2
screen inventory():
    tag menu
    default tt = Tooltip("")
    # $ config.keymap['game_menu'].append('i')
    # $ config.keymap['game_menu'].append('I')
    # key "i" action [Hide("inventory"), Hide("navigation"), Hide("game_menu"), Hide("main_menu")]
    $ item_all_merch = 0
    $ item_all_misc = 0
    $ item_all_tools = 0
    # if coins:
    #     $ item_all_merch += 1
    if item_gambesonrepairset:
        $ item_all_tools += 1
    if item_sewingkit:
        $ item_all_tools += 1
    if item_antlers:
        $ item_all_merch += 1
    if item_asterionbow:
        $ item_all_merch += 1
    if item_asterionwine:
        $ item_all_merch += 1
    if item_boartusks:
        $ item_all_merch += 1
    if item_bonebuckle:
        $ item_all_merch += 1
    if item_bonebuckle:
        $ item_all_merch += 1
    if item_boneearring:
        $ item_all_merch += 1
    if item_brokenknife:
        $ item_all_merch += 1
    if item_axehead:
        $ item_all_merch += 1
    if item_peltnorthberries and iason_food_berries != 3:
        $ item_all_merch += 1
    if item_cidercask == 1:
        $ item_all_merch += 1
    if item_stoat == 1:
        $ item_all_merch += 1
    if item_stoat == 2:
        $ item_all_merch += 1
    if item_goblinspear:
        $ item_all_merch += 1
    if item_elkfur or item_sealskin or item_harepelt:
        $ item_all_merch += 1
    if item_snakebait:
        $ item_all_merch += 1
    if item_oceannecklace:
        $ item_all_merch += 1
    if item_furlesswolftrophy:
        $ item_all_merch += 1
    if item_griffonegg:
        $ item_all_merch += 1
    if item_ironscraps:
        $ item_all_merch += 1
    if item_ironingot:
        $ item_all_merch += 1
    if item_linen:
        $ item_all_merch += 1
    if item_spices:
        $ item_all_merch += 1
    if item_magicpens:
        $ item_all_merch += 1
    if item_peltnorthberryclaw:
        $ item_all_merch += 1
    if item_rawfishtotalnumber:
        $ item_all_merch += 1
    if item_dragonlingclaws:
        $ item_all_merch += 1
    if item_spidersilk:
        $ item_all_merch += 1
    if item_wingedhourglass:
        $ item_all_merch += 1
    if item_ghoulblood:
        $ item_all_merch += 1
    if item_letterwhitemarshes == 2:
        $ item_all_merch += 1
    if item_arrow:
        $ item_all_misc += 1
    if item_asterionpurse:
        $ item_all_misc += 1
    if item_boxfromdolmen:
        $ item_all_misc += 1
    if item_peltnorthberrytools:
        $ item_all_misc += 1
    if item_dragonlingpaw:
        $ item_all_misc += 1
    if item_empresscarp:
        $ item_all_misc += 1
    if item_bugrepellent:
        $ item_all_misc += 1
    if item_stingointment:
        $ item_all_misc += 1
    if item_trollurine:
        $ item_all_misc += 1
    if item_teethset:
        $ item_all_misc += 1
    if item_howlersdelltoken:
        $ item_all_misc += 1
    if item_thaisletter:
        $ item_all_misc += 1
    if item_thaisletter_opened:
        $ item_all_misc += 1
    if item_asteriontablet:
        $ item_all_misc += 1
    if item_rawhide:
        $ item_all_misc += 1
    if item_rawfishtotalnumber:
        $ item_all_misc += 1
    if item_pileofbones:
        $ item_all_misc += 1
    if item_beholderroot:
        $ item_all_misc += 1
    if item_signpost:
        $ item_all_misc += 1
    if item_cavemushroom:
        $ item_all_misc += 1
    if item_casket:
        $ item_all_misc += 1
    if item_bronzerod:
        $ item_all_misc += 1
    if item_letterwhitemarshes == 1:
        $ item_all_misc += 1
    if item_thyrsusgift == 1:
        $ item_all_misc += 1
    on "show" action [SetVariable("game_menu_screen", "inventory"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
    on "replace" action [SetVariable("game_menu_screen", "inventory"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
    use game_menu(_("Inventory")):
        style_prefix "inventory"
        # $ config.keymap['viewport_drag_start'].append('mousedown_1')
        # $ config.keymap['viewport_drag_end'].append('mouseup_1')
        if inventoryscreenmode == "list":
            vbox:
                if item_all_misc and item_all_merch:
                    ypos -145
                else:
                    ypos -15
                hbox:
                    box_wrap True
                    minimum (1380,130)
                    if tt.value != "":
                        frame:
                            ypos 0
                            xpos 0
                            # top_padding 12
                            # bottom_padding 8
                            xpadding 8
                            maximum (1380,130)
                            minimum (1380,130)
                            if persistent.textstyle == "basic":
                                text tt.value xpos 10 size 28 line_spacing + 2 font "philosopher.ttf" yalign 0.5
                            if persistent.textstyle == "pixel":
                                text tt.value xpos 12 size 28 font "munro.ttf" yalign 0.5
                    elif tutorial_using_items == 0 and persistent.tutorial_display:
                        frame:
                            ypos 0
                            xpos 0
                            # top_padding 12
                            # bottom_padding 8
                            xpadding 8
                            maximum (1380,130)
                            minimum (1380,130)
                            if persistent.textstyle == "basic":
                                # textbutton "Unless you’re occupied with another task, you can eat food, drink potions,\nand use your items from this menu. You can examine your possessions at all times.": #Be sure to examine each new item - some of them may have .
                                textbutton "Unless you’re occupied with another task, you can eat food, drink potions, and use your items from this menu.\nBe sure to click on each new item you receive, as some of them can have unusual applications.":
                                    action SetVariable("tutorial_using_items", 1)
                                    text_slow_cps False
                                    text_font "philosopher.ttf"
                                    text_size 28
                                    yalign 0.5
                                    text_line_spacing + 2
                                    xpos 6
                            if persistent.textstyle == "pixel":
                                # textbutton "Unless you’re occupied with another task, you can eat food, drink potions,\nand use your items from this menu. You can examine your possessions at all times.":
                                textbutton "Unless you’re occupied with another task, you can eat food, drink potions, and use your items from this menu.\nBe sure to click on each new item you receive, as some of them can have unusual applications.":
                                    action SetVariable("tutorial_using_items", 1)
                                    text_slow_cps False
                                    text_font "munro.ttf"
                                    text_size 28
                                    yalign 0.5
                                    xpos 8
                hbox:
                    if item_all_misc and item_all_merch:
                        ymaximum (860)
                        yminimum (860)
                    else:
                        ymaximum (710)
                        yminimum (710)
                    xmaximum (1410)
                    xminimum (1410)
                    viewport id "allitems":
                        draggable True
                        mousewheel True
                        arrowkeys True
                        vbox:
                        #    box_wrap True
                            spacing 4
                            if item_all_tools:
                                label _("Supplies & Tools"):
                                    style "inventory_prompt"
                            else:
                                label _("Supplies"):
                                    style "inventory_prompt"
                            hbox:
                                ypos 8
                                spacing 16
                                box_wrap True
                                if not item_rations:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/foodrationslockedidle.png"
                                            hover "inventory/foodrationslockedhover.png"
                                            hovered tt.Action("Food Rations\n{color=#997577}They consist of dried meat and fruits, crackers, nuts, seeds, and water,\nwhich spoil slowly and don’t require additional cooking.{/color}"), SetVariable("item_hover_foodrations", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "rations")]
                                        if persistent.textstyle == "basic":
                                            text "[item_rations]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_rations]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_foodrations:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                else:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/foodrationsidle.png"
                                            hover "inventory/foodrationshover.png"
                                            hovered tt.Action("Food Rations\n{color=#997577}They consist of dried meat, crackers, nuts, seeds, fruits, and water,\nwhich spoil slowly and don’t require additional cooking.{/color}"), SetVariable("item_hover_foodrations", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "rations")]
                                        if persistent.textstyle == "basic":
                                            text "[item_rations]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_rations]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_foodrations:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_peltnorthberries and iason_food_berries == 3:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/berriespeltnorthidle.png"
                                            hover "inventory/berriespeltnorthhover.png"
                                            hovered tt.Action("A Bucketful of Berries\n{color=#997577}Picked near Pelt of the North, you can eat them for a bit of taste.{/color}"), SetVariable("item_hover_berriespeltnorth", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "peltnorthberries")]
                                        if not item_hover_berriespeltnorth:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_chicken:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/chickenidle.png"
                                            hover "inventory/chickenhover.png"
                                            hovered tt.Action("A Roast Chicken\n{color=#997577}A spiced, whole meal made by an experienced cook.{/color}"), SetVariable("chickenitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "chicken")]
                                        if persistent.textstyle == "basic":
                                            text "[item_chicken]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_chicken]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not chickenitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_cookedfish:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/cookedfishidle.png"
                                            hover "inventory/cookedfishhover.png"
                                            hovered tt.Action("Roast Fish\n{color=#997577}A simple, small meal.{/color}"), SetVariable("cookedfishitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "cookedfish")]
                                        if persistent.textstyle == "basic":
                                            text "[item_cookedfish]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_cookedfish]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not cookedfishitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_wildplants:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/wildplantsidle.png"
                                            hover "inventory/wildplantshover.png"
                                            hovered tt.Action("Wild Plants\n{color=#997577}Fruits and vegetables that can be found in the wilderness.\nNot very filling.{/color}"), SetVariable("wildplantsitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "wildplants")]
                                        if persistent.textstyle == "basic":
                                            text "[item_wildplants]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_wildplants]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not wildplantsitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_sharpeningpotion and item_sharpeningpotion_used != day:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/sharpeningpotionidle.png"
                                            hover "inventory/sharpeningpotionhover.png"
                                            hovered tt.Action("A Sharpening Poison\n{color=#997577}After consumption, it makes one’s senses quicker and alerted. It gives an edge in combat,\nbut puts a burden on the shell a day after consumption.{/color}"), SetVariable("item_hover_sharpeningpotion", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "sharpeningpotion")]
                                        if persistent.textstyle == "basic":
                                            text "[item_sharpeningpotion]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_sharpeningpotion]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_sharpeningpotion:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                elif item_sharpeningpotion_used > 0 and item_sharpeningpotion_used == day:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/sharpeningpotionlockedidle.png"
                                            hover "inventory/sharpeningpotionlockedhover.png"
                                            hovered tt.Action("A Sharpening Poison\n{color=#997577}After drinking, it makes one’s senses quicker and alerted.\nYou’re currently under its influence.{/color}"), SetVariable("item_hover_sharpeningpotion", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "sharpeningpotion")]
                                        if persistent.textstyle == "basic":
                                            text "[item_sharpeningpotion]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_sharpeningpotion]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_sharpeningpotion:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_spiritrock:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/spiritrockidle.png"
                                            hover "inventory/spiritrockhover.png"
                                            hovered tt.Action("A Spirit Rock\n{color=#997577}A smooth blue pebble that stores pneuma.\nIt helps to strengthen an exhausted spellcaster.{/color}"), SetVariable("item_hover_spiritrock", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "spiritrock")]
                                        if persistent.textstyle == "basic":
                                            text "[item_spiritrock]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_spiritrock]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_spiritrock:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_generichealingpotion:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/generichealingpotionidle.png"
                                            hover "inventory/generichealingpotionhover.png"
                                            hovered tt.Action("A Fresh Healing Potion\n{color=#997577}An earthenware bottle with a liquid which heals one’s wounds.{/color}"), SetVariable("generichealingpotionitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "generichealingpotion")]
                                        if persistent.textstyle == "basic":
                                            text "[item_generichealingpotion]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_generichealingpotion]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not generichealingpotionitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_potiondolmen:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/potiondolmenidle.png"
                                            hover "inventory/potiondolmenhover.png"
                                            if item_potiondolmen_known:
                                                hovered tt.Action("A Potion from the Dolmen\n{color=#997577}A healing mixture that smells like fruits cooked with honey.{/color}"), SetVariable("item_hover_potiondolmen", "1")
                                            else:
                                                hovered tt.Action("A Bottle from the Dolmen\n{color=#997577}An earthenware bottle with an unknown content.{/color}"), SetVariable("item_hover_potiondolmen", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "potiondolmen")]
                                        if not item_hover_potiondolmen:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_smallhealingpotion:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/smallhealingpotionidle.png"
                                            hover "inventory/smallhealingpotionhover.png"
                                            hovered tt.Action("A Small Healing Potion\n{color=#997577}A set of earthenware bottles that contain small amounts of magical concoctions.{/color}"), SetVariable("item_hover_smallhealingpotion", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "smallhealingpotion")]
                                        if persistent.textstyle == "basic":
                                            text "[item_smallhealingpotion]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_smallhealingpotion]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_smallhealingpotion:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_magicfruit == 1:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/magicfruitidle.png"
                                            hover "inventory/magicfruithover.png"
                                            if druidcave_druid_about_plague01 or howlersdell_elpis_about_magicfruit:
                                                hovered tt.Action("The Seed\n{color=#997577}A fruit borne by a pneuma-draining tree.\nIt resembles a bone-colored apple with an unusually hard skin.{/color}"), SetVariable("item_hover_magicfruit", "1")
                                            else:
                                                hovered tt.Action("A Weird Fruit\n{color=#997577}A fruit borne by a pneuma-draining tree.\nIt resembles a bone-colored apple with an unusually hard skin.{/color}"), SetVariable("item_hover_magicfruit", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "magicfruit")]
                                        if not item_hover_magicfruit:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_gambesonrepairset:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/gambesonrepairsetidle.png"
                                            hover "inventory/gambesonrepairsethover.png"
                                            hovered tt.Action("A Gambeson Repair Set\n{color=#997577}With a bit of time, you can patch your jacket,\nbut your lack of proper training will hold you back.{/color}"), SetVariable("gambesonrepairsetitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "gambesonrepairset")]
                                        if not gambesonrepairsetitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_sewingkit:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/sewingkitidle.png"
                                            hover "inventory/sewingkithover.png"
                                            hovered tt.Action("A Sewing Kit\n{color=#997577}It will take you a lot more time than it would take for a tailor,\nbut you can fix your clothes and make them tidy.{/color}"), SetVariable("sewingkititem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "sewingkit")]
                                        if not sewingkititem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                            if item_all_merch or (coins and not item_all_misc):
                                label _("Merchandise"):
                                    style "inventory_prompt"
                            hbox:
                                ypos 8
                                spacing 16
                                box_wrap True
                                if (coins and item_all_merch) or (coins and not item_all_misc):
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/coinscoupleidle.png"
                                            hover "inventory/coinscouplehover.png"
                                            hovered tt.Action("A Pouch with Coins\n{color=#997577}The city artisans make coins by cutting dragon bones into slices.\nThey are valued by merchants, though rarely used in the countryside.{/color}"), SetVariable("item_hover_coinscouple", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "coins")]
                                        if persistent.textstyle == "basic":
                                            text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_coinscouple:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_antlers:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/antlersidle.png"
                                            hover "inventory/antlershover.png"
                                            hovered tt.Action("A Set of Antlers\n{color=#997577}A useful resource used in all sorts of crafts, but since the deer-like creatures\nshed and grow a new pair of antlers every year, they are less valuable than most trophies.{/color}"), SetVariable("antlersitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "antlers")]
                                        if persistent.textstyle == "basic":
                                            text "[item_antlers]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_antlers]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not antlersitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_asterionbow:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/asterionbowidle.png"
                                            hover "inventory/asterionbowhover.png"
                                            hovered tt.Action("Asterion’s Bow\n{color=#997577}A smooth bow, about five feet long.\nYou lack proper training, but you could still sell it.{/color}"), SetVariable("item_hover_asterionbow", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "asterionbow")]
                                        if not item_hover_asterionbow:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_asterionwine:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/asterionwineidle.png"
                                            hover "inventory/asterionwinehover.png"
                                            if item_asterionwine_pcknows_2:
                                                hovered tt.Action("Night’s Bane\n{color=#997577}A large bottle of rare, expensive wine. Since grapes can’t be cultivated in The Dragonwoods,\nsuch drinks are considered a valuable curiosity.{/color}"), SetVariable("asterionwineitem_hover", "1")
                                            elif item_asterionwine_pcknows_1:
                                                hovered tt.Action("Asterion’s Wine\n{color=#997577}A large bottle of wine. Since grapes can’t be cultivated in The Dragonwoods,\nsuch drinks are considered a valuable curiosity.{/color}"), SetVariable("asterionwineitem_hover", "1")
                                            else:
                                                hovered tt.Action("Asterion’s Bottle\n{color=#997577}A large, earthenware bottle, filled with some liquid.{/color}"), SetVariable("asterionwineitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "asterionwine")]
                                        if not asterionwineitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_boartusks:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/boartusksidle.png"
                                            hover "inventory/boartuskshover.png"
                                            hovered tt.Action("Boar Tusks\n{color=#997577}One of the more common trophies used in the north, often turned into\nwall decorations, with the smaller pair of tusks being surrounded by the larger one.{/color}"), SetVariable("boartusksitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "boartusks")]
                                        if not boartusksitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_boneearring:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/boneearringidle.png"
                                            hover "inventory/boneearringhover.png"
                                            hovered tt.Action("A Bone Earring\n{color=#997577}A small trinket that you found with the corpse in the heart of the woods.{/color}"), SetVariable("boneearringitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "boneearring")]
                                        if not boneearringitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_bonering:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/boneringidle.png"
                                            hover "inventory/boneringhover.png"
                                            hovered tt.Action("A Bone Ring\n{color=#997577}A piece of polished bone that bears\ncarvings of scales and fish.{/color}"), SetVariable("boneringitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "bonering")]
                                        if not boneringitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_brokenknife:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/brokenknifeidle.png"
                                            hover "inventory/brokenknifehover.png"
                                            hovered tt.Action("The Broken Knife\n{color=#997577}A polished, decorated bone handle with the remains of a steel blade.\nYou found it in a cave inhabited by a corpse eater.{/color}"), SetVariable("brokenknifeitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "brokenknife")]
                                        if not brokenknifeitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_axehead:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/axeheadidle.png"
                                            hover "inventory/axeheadhover.png"
                                            hovered tt.Action("A Bronze Axe Head\n{color=#997577}It has seen some better days, but decent bronze can endure centuries.\nIt’s slightly heavier than steel and, with some sharpening, will serve you well in combat.{/color}"), SetVariable("axeheaditem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "axehead")]
                                        if not axeheaditem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_peltnorthberries and iason_food_berries != 3:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/berriespeltnorthidle.png"
                                            hover "inventory/berriespeltnorthhover.png"
                                            hovered tt.Action("A Bucketful of Berries\n{color=#997577}Filled with fruit that grows near Pelt of the North.\nThe innkeeper asked you to fetch them for him.{/color}"), SetVariable("item_hover_berriespeltnorth", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "peltnorthberries")]
                                        if not item_hover_berriespeltnorth:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_ghoulblood:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/ghoulbloodidle.png"
                                            hover "inventory/ghoulbloodhover.png"
                                            hovered tt.Action("Corpse Eater’s Blood\n{color=#997577}A poisonous substance collected from one of the\nmost loathed monsters of The Dragonwoods."), SetVariable("ghoulblooditem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "ghoulblood")]
                                        if not ghoulblooditem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_cidercask:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/cidercaskidle.png"
                                            hover "inventory/cidercaskhover.png"
                                            hovered tt.Action("A Cask of Cider\n{color=#997577}Made of wood and steel straps, contains a valuable hard drink made of apples.\nFoggy asked you to deliver it to White Marshes."), SetVariable("cidercaskitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "cidercask")]
                                        if not cidercaskitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_stoat == 1:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/stoatidle.png"
                                            hover "inventory/stoathover.png"
                                            hovered tt.Action("A Dead Stoat\n{color=#997577}Once processed, the fur of this carcass will be worth some coin.\nIt was slightly damaged during your hunt."), SetVariable("stoatitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "stoat")]
                                        if not stoatitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_stoat == 2:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/stoatidle.png"
                                            hover "inventory/stoathover.png"
                                            hovered tt.Action("A Dead Stoat\n{color=#997577}Once processed, the fur of this carcass will be worth some coin.\nIt’s in perfect condition."), SetVariable("stoatitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "stoat")]
                                        if not stoatitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_bonebuckle:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/bonebuckleidle.png"
                                            hover "inventory/bonebucklehover.png"
                                            hovered tt.Action("A Decorative Buckle\n{color=#997577}A small trinket that you found with the corpse at a lair of howlers.{/color}"), SetVariable("bonebuckleitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "bonebuckle")]
                                        if not bonebuckleitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_goblinspear:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/goblinspearidle.png"
                                            hover "inventory/goblinspearhover.png"
                                            hovered tt.Action("A Goblin Spear\n{color=#997577}A sharpened stick that’s been either made or found by a goblin.{/color}"), SetVariable("goblinspearitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "goblinspear")]
                                        if not goblinspearitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_elkfur or item_sealskin or item_harepelt:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/fursidle.png"
                                            hover "inventory/furshover.png"
                                            hovered tt.Action("Furs and Skins\n{color=#997577}Used to make clothing, flasks, bed covers, parchment,\ntoys, or to decorate walls and floors.{/color}"), SetVariable("item_hover_furs", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "furs")]
                                        if not item_hover_furs:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_oceannecklace:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/oceannecklaceidle.png"
                                            hover "inventory/oceannecklacehover.png"
                                            hovered tt.Action("An Ocean Necklace\n{color=#997577}A leather strip with a couple of silver fish scales and a single long seashell.\nYou found it at the fishing hamlet.{/color}"), SetVariable("oceannecklaceitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "oceannecklace")]
                                        if not oceannecklaceitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_griffonegg:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/griffoneggidle.png"
                                            hover "inventory/griffonegghover.png"
                                            hovered tt.Action("A Griffon Egg\n{color=#997577}It’s dried-out, larger than your head, with a firm shell.\nYou took it from the nest in the eastern mountains.{/color}"), SetVariable("griffoneggitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "griffonegg")]
                                        if not griffoneggitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_furlesswolftrophy:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/furlesswolftrophyidle.png"
                                            hover "inventory/furlesswolftrophyhover.png"
                                            hovered tt.Action("A Head of a Beast\n{color=#997577}The fresh head of a wolf-like creature you faced in the heart of the forest.\nYou should get rid of it before it decomposes.{/color}"), SetVariable("furlesswolftrophyitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "furlesswolftrophy")]
                                        if not furlesswolftrophyitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_ironingot:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/ironingotidle.png"
                                            hover "inventory/ironingothover.png"
                                            if galerocks_pastrobbery:
                                                hovered tt.Action("An Iron Ingot\n{color=#997577}A valuable chunk of crude iron stolen from Gale Rocks.{/color}"), SetVariable("ironingotitem_hover", "1")
                                            else:
                                                hovered tt.Action("An Iron Ingot\n{color=#997577}A valuable chunk of crude iron.{/color}"), SetVariable("ironingotitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "ironingot")]
                                        if not ironingotitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_ironscraps:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/ironscrapsidle.png"
                                            hover "inventory/ironscrapshover.png"
                                            hovered tt.Action("Iron Scraps\n{color=#997577}A set of bits and pieces made of iron and steel. After melting and cleaning,\nthey can be reforged into tools, nails, hoops, or hinges.{/color}"), SetVariable("item_hover_ironscraps", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "ironscraps")]
                                        if persistent.textstyle == "basic":
                                            text "[item_ironscraps]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_ironscraps]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_ironscraps:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_peltnorthberryclaw:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/clawpeltnorthidle.png"
                                            hover "inventory/clawpeltnorthhover.png"
                                            hovered tt.Action("A Pebbler’s Claw\n{color=#997577}It’s large and dark, and was used as a hook.{/color}"), SetVariable("item_hover_clawpeltnorth", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "peltnorthberryclaw")]
                                if item_rawfishtotalnumber:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/rawfishidle.png"
                                            hover "inventory/rawfishhover.png"
                                            hovered tt.Action("Raw Fish\n{color=#997577}A dead, raw fish. Not worth much,\nbut could be bartered for food or sold.{/color}"), SetVariable("rawfishitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "rawfish")]
                                        if persistent.textstyle == "basic":
                                            text "[item_rawfishtotalnumber]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_rawfishtotalnumber]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not rawfishitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_spices:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/spicesidle.png"
                                            hover "inventory/spiceshover.png"
                                            hovered tt.Action("The Sacks of Spices\n{color=#997577}Valuable ingredients that break the monotony of life.{/color}"), SetVariable("spicesitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "spices")]
                                        if not spicesitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_dragonlingclaws:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/dragonlingclawsidle.png"
                                            hover "inventory/dragonlingclawshover.png"
                                            hovered tt.Action("A Set of Dragonling Claws\n{color=#997577}Useful for crafting trinkets, spears, or tools.{/color}"), SetVariable("item_hover_dragonlingclaws", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "dragonlingclaws")]
                                        if not item_hover_dragonlingclaws:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_spidersilk:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/spidersilkidle.png"
                                            hover "inventory/spidersilkhover.png"
                                            hovered tt.Action("Spider Silk\n{color=#997577}A stick wrapped with thick threads of spider web.\nA skillful tailor will use it to increase the durability of a garment.{/color}"), SetVariable("spidersilkitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "spidersilk")]
                                        if not spidersilkitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_linen:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/linenidle.png"
                                            hover "inventory/linenhover.png"
                                            hovered tt.Action("A Stack of Linen Fabric\n{color=#997577}High quality, clean, and new.\nYou carry in a waterproof sack.{/color}"), SetVariable("linenitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "linen")]
                                        if not linenitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_letterwhitemarshes == 2:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/letterwhitemarshes2idle.png"
                                            hover "inventory/letterwhitemarshes2hover.png"
                                            hovered tt.Action("The Troll-Bone Tablet\n{color=#997577}A fancy wax tablet carved in a hip bone of a troll,\nsuplemented with the matching stylus.{/color}"), SetVariable("letterwhitemarshes_hover", "1")
                                            if item_letterwhitemarshes_read:
                                                action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "letterwhitemarshes")]
                                            else:
                                                if pc_class == "scholar":
                                                    action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "letterwhitemarshes"), SetVariable("item_letterwhitemarshes_read", 1)]
                                                else:
                                                    action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "letterwhitemarshes")]
                                        if not letterwhitemarshes_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_wingedhourglass:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/wingedhourglassidle.png"
                                            hover "inventory/wingedhourglasshover.png"
                                            if item_wingedhourglass_worn:
                                                hovered tt.Action("A Winged Hourglass (worn)\n{color=#997577}A steel pendant hanging from a leather strap.\nIt’s common to wear such jewelry to demonstrate one’s allegiance to The Wright.{/color}"), SetVariable("item_hover_wingedhourglass", "1")
                                            else:
                                                hovered tt.Action("A Winged Hourglass (hidden)\n{color=#997577}A steel pendant hanging from a leather strap.\nIt’s common to wear such jewelry to demonstrate one’s allegiance to The Wright.{/color}"), SetVariable("item_hover_wingedhourglass", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "wingedhourglass")]
                                        if not item_hover_wingedhourglass:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0

                            if item_all_misc:
                                label _("Miscellaneous"):
                                    style "inventory_prompt"
                            hbox:
                                ypos 8
                                spacing 16
                                box_wrap True
                                if (coins and not item_all_merch and item_all_misc):
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/coinscoupleidle.png"
                                            hover "inventory/coinscouplehover.png"
                                            hovered tt.Action("A Pouch with Coins\n{color=#997577}The city artisans make coins by cutting dragon bones into slices.\nThey are valued by merchants, though rarely used in the countryside.{/color}"), SetVariable("item_hover_coinscouple", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "coins")]
                                        if persistent.textstyle == "basic":
                                            text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_coinscouple:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_asterionpurse:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/asterionpurseidle.png"
                                            hover "inventory/asterionpursehover.png"
                                            hovered tt.Action("Asterion’s Pouch\n{color=#997577}You hear dragon bones hitting something made of metal.{/color}"), SetVariable("item_hover_asterionpurse", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "asterionpurse")]
                                        if not item_hover_asterionpurse:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_boxfromdolmen:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/boxfromdolmenidle.png"
                                            hover "inventory/boxfromdolmenhover.png"
                                            hovered tt.Action("A Box from the Dolmen\n{color=#997577}Made of timber. You can’t open it without damaging the fiber cords.{/color}"), SetVariable("item_hover_boxfromdolmenitem", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "boxfromdolmen")]
                                        if not item_hover_boxfromdolmenitem:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_peltnorthberrytools:
                                    if iason_food_berries == 2:
                                        fixed:
                                            maximum (106,126)
                                            minimum (106,126)
                                            imagebutton:
                                                style "inventoryimage"
                                                idle "inventory/toolsberriesidle02.png"
                                                hover "inventory/toolsberrieshover02.png"
                                                hovered tt.Action("A Berry Picking Hook\n{color=#997577}A tool from Pelt of the North\nwith a head made of a large animal claw.{/color}"), SetVariable("item_hover_toolsberries", "1")
                                                action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "peltnorthberrytools02")]
                                            if not item_hover_toolsberries:
                                                add "images/inventory/border.png":
                                                    xpos 0
                                                    ypos 0
                                    else:
                                        fixed:
                                            maximum (106,126)
                                            minimum (106,126)
                                            imagebutton:
                                                style "inventoryimage"
                                                idle "inventory/toolsberriesidle.png"
                                                hover "inventory/toolsberrieshover.png"
                                                hovered tt.Action("Tools for Berry Picking\n{color=#997577}A set given to you by the innkeeper from Pelt of the North. A hook, a pair of gloves,\nand a bucket to help you forage for berries.{/color}"), SetVariable("item_hover_toolsberries", "1")
                                                action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "peltnorthberrytools")]
                                            if not item_hover_toolsberries:
                                                add "images/inventory/border.png":
                                                    xpos 0
                                                    ypos 0
                                if item_bronzerod:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/bronzerodidle.png"
                                            hover "inventory/bronzerodhover.png"
                                            hovered tt.Action("Bronze Rods\n{color=#997577}A set of magical bronze rods, given to you by Eudocia.\nThey’re empty inside.{/color}"), SetVariable("item_hover_bronzerod", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "bronzerod")]
                                        if persistent.textstyle == "basic":
                                            text "[item_bronzerod]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_bronzerod]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_bronzerod:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_cavemushroom and pc_class != "scholar":
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/cavemushroomidle.png"
                                            hover "inventory/cavemushroomhover.png"
                                            hovered tt.Action("A Cave Ear\n{color=#997577}A poisonous mushroom that grows in moist caves and is often used as\nan ingredient of various combat-enhancing substances.{/color}"), SetVariable("item_hover_cavemushroom", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "cavemushroom")]
                                        if not item_hover_cavemushroom:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_casket:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/casketidle.png"
                                            hover "inventory/caskethover.png"
                                            hovered tt.Action("A Casket of Coins\n{color=#997577}The box with the “cursed” payment that you’re meant to sacrifice.{/color}"), SetVariable("item_hover_casket", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "casket")]
                                        if not item_hover_casket:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_dragonlingpaw:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/dragonlingpawidle.png"
                                            hover "inventory/dragonlingpawhover.png"
                                            hovered tt.Action("A Dragonling’s Paw\n{color=#997577}A paw that belonged to a dragonling.\nIts detached, cleaned claws could be worth something.{/color}"), SetVariable("item_hover_dragonlingpaw", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "dragonlingpaw")]
                                        if not item_hover_dragonlingpaw:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_empresscarp:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/empresscarpidle.png"
                                            hover "inventory/empresscarphover.png"
                                            hovered tt.Action("An Empress Carp\n{color=#997577}It’s covered with red and golden scales, currently kept in a sealed bucket.\nThe druid from the cave has asked you to deliver it to him.{/color}"), SetVariable("item_hover_empresscarp", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "empresscarp")]
                                        if not item_hover_empresscarp:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_bugrepellent:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/bugrepellentidle.png"
                                            hover "inventory/bugrepellenthover.png"
                                            hovered tt.Action("A Herbal Bug Repellent\n{color=#997577}A jar with a bug-killing ointment. It smells of herbs.{/color}"), SetVariable("item_hover_bugrepellent", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "bugrepellent")]
                                        if not item_hover_bugrepellent:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_pileofbones:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/pileofbonesidle.png"
                                            hover "inventory/pileofboneshover.png"
                                            hovered tt.Action("The Human Bones\n{color=#997577}The remains of the huntress that lost her soul in the lair of howlers.{/color}"), SetVariable("pileofbonesitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "pileofbones")]
                                        if not pileofbonesitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_trollurine:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/goblinrepellentidle.png"
                                            hover "inventory/goblinrepellenthover.png"
                                            hovered tt.Action("A Jar Of Troll’s Urine\n{color=#997577}Its stench allegedly scares goblins and pebblers away.{/color}"), SetVariable("item_hover_goblinrepellent", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "goblinrepellent")]
                                        if not item_hover_goblinrepellent:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_thaisletter:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/thaisletter01idle.png"
                                            hover "inventory/thaisletter01hover.png"
                                            hovered tt.Action("The Letter From Thais (sealed)\n{color=#997577}The sealed scroll given to you by the mayor of Howler’s Dell.{/color}"), SetVariable("thaisletteritem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "thaisletter")]
                                        if not thaisletteritem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_thaisletter_opened:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/thaisletter02idle.png"
                                            hover "inventory/thaisletter02hover.png"
                                            hovered tt.Action("The Letter From Thais (opened)\n{color=#997577}The scroll given to you by the mayor of Howler’s Dell.\nYou’ve already broken its seal.{/color}"), SetVariable("thaisletteritem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "thaisletteropened")]
                                        if not thaisletteritem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                # if item_teethset:
                                #     fixed:
                                #         maximum (106,126)
                                #         minimum (106,126)
                                #         imagebutton:
                                #             style "inventoryimage"
                                #             idle "inventory/teethsetidle.png"
                                #             hover "inventory/teethsethover.png"
                                #             hovered tt.Action("A Teeth-Cleaning Set\n{color=#997577}A leather bag with twigs and a cleaning paste.{/color}"), SetVariable("teethsetitem_hover", "1")
                                #             action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "teethset")]
                                #         if not teethsetitem_hover:
                                #             add "images/inventory/border.png":
                                #                 xpos 0
                                #                 ypos 0
                                if item_magicalsapling:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/magicalsaplingidle.png"
                                            hover "inventory/magicalsaplinghover.png"
                                            hovered tt.Action("Eudocia’s Sapling\n{color=#997577}A herb that’s meant to change its leaves\nwhen planted in soil storing large amounts of pneuma.{/color}"), SetVariable("magicalsaplingitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "magicalsapling")]
                                        if not magicalsaplingitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_rawhide:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/lostmanblanketidle.png"
                                            hover "inventory/lostmanblankethover.png"
                                            hovered tt.Action("An Old Blanket\n{color=#997577}A piece of rawhide you found at the northern road.{/color}"), SetVariable("lostmanblanketitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "lostmanblanket")]
                                        if not lostmanblanketitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_signpost:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/signpostidle.png"
                                            hover "inventory/signposthover.png"
                                            hovered tt.Action("A Painted Sign\n{color=#997577}A plank covered with reddish paint.\n{color=#f6d6bd}Elah{/color} wants you to place it in a visible spot at the old stone bridge.{/color}"), SetVariable("signpostitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "signpost")]
                                        if not signpostitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_arrow:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/arrowidle.png"
                                            hover "inventory/arrowhover.png"
                                            if not aegidia_about_arrow and not galerocks_florus_about_arrow:
                                                hovered tt.Action("A Simple Arrow\n{color=#997577}A pointy arrow with a head made of horn and black-orange fletching.{/color}"), SetVariable("item_hover_arrow", "1")
                                            else:
                                                hovered tt.Action("A Human Arrow\n{color=#997577}A pointy arrow with a head made of horn and black-orange fletching.{/color}"), SetVariable("item_hover_arrow", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "arrow")]
                                        if not item_hover_arrow:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_magicpens:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/magicpensidle.png"
                                            hover "inventory/magicpenshover.png"
                                            if pc_class == "scholar":
                                                hovered tt.Action("A Set of Magic Quills\n{color=#997577}A set of excellent writing instruments made of goose and swan feathers,\nsupposedly toughened with magical pneuma.{/color}"), SetVariable("item_hover_magicpens", "1")
                                            else:
                                                hovered tt.Action("A Set of Magic Quills\n{color=#997577}A set of sharpened writing instruments made of bird feathers,\nsupposedly toughened with magical pneuma.{/color}"), SetVariable("item_hover_magicpens", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "magicpens")]
                                        if not item_hover_magicpens:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_snakebait and pc_class != "scholar":
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/snakebaitidle.png"
                                            hover "inventory/snakebaithover.png"
                                            if quest_eudociaflower == 1:
                                                if pc_class == "scholar" or item_snakebait_truth:
                                                    hovered tt.Action("Snake Bait\n{color=#997577}A picked herb. Its leaves and flowers are a valuable remedy and an alchemical ingredient.\nEudocia has asked you to deliver it to her.{/color}"), SetVariable("item_hover_eudociaflower", "1")
                                                else:
                                                    hovered tt.Action("Snake Bait\n{color=#997577}A bunch of picked flowers that resemble a tulip.\nEudocia has asked you to deliver it to her.{/color}"), SetVariable("item_hover_eudociaflower", "1")
                                            else:
                                                if pc_class == "scholar" or item_snakebait_truth:
                                                    hovered tt.Action("Snake Bait\n{color=#997577}A picked herb. Its leaves and flowers are a valuable remedy\nand an alchemical ingredient.{/color}"), SetVariable("item_hover_eudociaflower", "1")
                                                else:
                                                    hovered tt.Action("Snake Bait\n{color=#997577}A bunch of picked flowers that resemble a tulip.{/color}"), SetVariable("item_hover_eudociaflower", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "eudociaflower")]
                                        if persistent.textstyle == "basic":
                                            text "[item_snakebait]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_snakebait]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_eudociaflower:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_stingointment:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/stingointmentidle.png"
                                            hover "inventory/stingointmenthover.png"
                                            hovered tt.Action("A Sting Ointment\n{color=#997577}A large supply of an herbal mixture which repels blood-drinking insects.{/color}"), SetVariable("stingointmentitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "stingointment")]
                                        if not stingointmentitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_thyrsusgift:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/thyrsusgiftidle.png"
                                            hover "inventory/thyrsusgifthover.png"
                                            hovered tt.Action("Thyrsus’ Gift\n{color=#997577}The odds and ends that are meant to be offered\nto an old couple in White Marshes.{/color}"), SetVariable("item_hover_thyrsusgift", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "thyrsusgift")]
                                        if not item_hover_thyrsusgift:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_howlersdelltoken:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/howlersdelltokenidle.png"
                                            hover "inventory/howlersdelltokenhover.png"
                                            hovered tt.Action("The “Token of Gratitude”\n{color=#997577}An illustrated scroll that you received as a “friend” of Howler’s Dell.{/color}"), SetVariable("howlersdelltokenitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "howlersdelltoken")]
                                        if not howlersdelltokenitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_letterwhitemarshes == 1:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/letterwhitemarshesidle.png"
                                            hover "inventory/letterwhitemarsheshover.png"
                                            hovered tt.Action("The Troll-Bone Tablet\n{color=#997577}A fancy wax tablet carved in a hip bone of a troll.\nYou were asked to read its contents.{/color}"), SetVariable("letterwhitemarshes_hover", "1")
                                            if item_letterwhitemarshes_read:
                                                action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "letterwhitemarshes")]
                                            else:
                                                if pc_class == "scholar":
                                                    action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "letterwhitemarshes"), SetVariable("item_letterwhitemarshes_read", 1)]
                                                else:
                                                    action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "letterwhitemarshes")]
                                        if not letterwhitemarshes_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_asteriontablet:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/asteriontabletidle.png"
                                            hover "inventory/asteriontablethover.png"
                                            hovered tt.Action("A Wax Tablet\n{color=#997577}A cheap, old, moldy instrument used for writing.\nA wooden frame filled with dyed wax.{/color}"), SetVariable("asteriontabletitem_hover", "1")
                                            if pc_class == "scholar":
                                                if not item_asteriontablet_read:
                                                    action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "asteriontablet"), SetVariable("item_asteriontablet_read", 1), SetVariable("asterion_highisland_clues", asterion_highisland_clues+1)]
                                                else:
                                                    action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "asteriontablet")]
                                            else:
                                                action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "asteriontablet")]
                                        if not asteriontabletitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_beholderroot:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/beholderrootidle.png"
                                            hover "inventory/beholderroothover.png"
                                            if beholder_name_known:
                                                hovered tt.Action("A Weird Root\n{color=#997577}A jar with a chunk you cut away from Beholder.{/color}"), SetVariable("beholderrootitem_hover", "1")
                                            else:
                                                hovered tt.Action("A Weird Root\n{color=#997577}A jar with a chunk you cut away from the tree growing at the altar.{/color}"), SetVariable("beholderrootitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "beholderroot")]
                                        if not beholderrootitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0

                            label _("Equipment"):
                                style "inventory_prompt"
                            hbox:
                                ypos 8
                                spacing 16
                                box_wrap True
                                if item_trapdoorkeydolmen or item_watchtowerkey or item_asterionkey or item_oldtunnelkey or item_piershedkey or item_oldtunnesmallkey:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/keys3idle.png"
                                            hover "inventory/keys3hover.png"
                                            hovered tt.Action("Keys\n{color=#997577}The limited access to iron makes padlocks a rare commodity. Outside of city walls,\nburglary happens sporadically and is usually blamed on strangers.{/color}"), SetVariable("item_hover_keys3item", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "keysidle")]
                                        if not item_hover_keys3item:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_horse:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/horse1idle.png"
                                            hover "inventory/horse1hover.png"
                                            hovered tt.Action("[horsename]\n{color=#997577}While valuable, they can’t survive in The Dragonwoods on their own.\nThey are owned by messengers, scouts, or rich cityfolk.{/color}"), SetVariable("item_hover_horse1", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "horse01")]
                                        if not item_hover_horse1:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_asterioncloak:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/asterioncloakidle.png"
                                            hover "inventory/asterioncloakhover.png"
                                            hovered tt.Action("Asterion’s Cloak\n{color=#997577}A green cloak with embroidered leaves. It’s downy, made from lambswool.{/color}"), SetVariable("asterionitem_hover_cloak", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "asterioncloak")]
                                        if not asterionitem_hover_cloak:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_axeset:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/axesetidle.png"
                                            hover "inventory/axesethover.png"
                                            hovered tt.Action("An Axe Head With A Handle\n{color=#997577}With the other tools in your possession,\nyou may turn this set into a decent weapon.{/color}"), SetVariable("axesetitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "axeset")]
                                        if not axesetitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_bonehook:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/bonehookidle.png"
                                            hover "inventory/bonehookhover.png"
                                            hovered tt.Action("A Bone Hook\n{color=#997577}A set of three connected bones that are meant to be used as a cheap grappling hook.{/color}"), SetVariable("bonehookitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "bonehook")]
                                        if not bonehookitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                # if item_bonehook: # ropehook
                                #     fixed:
                                #         maximum (106,126)
                                #         minimum (106,126)
                                #         imagebutton:
                                #             style "inventoryimage"
                                #             idle "inventory/bonehookidle.png"
                                #             hover "inventory/bonehookhover.png"
                                #             hovered tt.Action("A Bone Hook\n{color=#997577}A set of three connected bones that are meant to be used as a cheap grappling hook. Useless without a rope.{/color}"), SetVariable("bonehookitem_hover", "1")
                                #             action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "bonehook")]
                                #         if not bonehookitem_hover:
                                #             add "images/inventory/border.png":
                                #                 xpos 0
                                #                 ypos 0
                                if item_dragonhorn:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/dragonhornidle.png"
                                            hover "inventory/dragonhornhover.png"
                                            hovered tt.Action("A Dragon Horn\n{color=#997577}An instrument made of a twisted animal horn.\nWhen blown, it imitates a roar of an enormous creature.{/color}"), SetVariable("dragonhornitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "dragonhorn")]
                                        if not dragonhornitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_fancyclothes:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            if item_fancyclothes == 1:
                                                idle "inventory/fancyclothes1idle.png"
                                                hover "inventory/fancyclothes1hover.png"
                                                hovered tt.Action("A Fancy Tunic\n{color=#997577}An expensive tunic, shoes, pants, belt, and jewelry\nthat you put on when you’re not on the road.{/color}"), SetVariable("fancyclothesitem_hover", "1")
                                            if item_fancyclothes == 2:
                                                idle "inventory/fancyclothes2idle.png"
                                                hover "inventory/fancyclothes2hover.png"
                                                hovered tt.Action("A Fancy Robe\n{color=#997577}An expensive robe, shoes, pants, belt, and jewelry\nthat you put on when you’re not on the road.{/color}"), SetVariable("fancyclothesitem_hover", "1")
                                            if item_fancyclothes == 3:
                                                idle "inventory/fancyclothes3idle.png"
                                                hover "inventory/fancyclothes3hover.png"
                                                hovered tt.Action("A Fancy Dress\n{color=#997577}An expensive dress, shoes, belt, and jewelry\nthat you put on when you’re not on the road.{/color}"), SetVariable("fancyclothesitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "fancyclothes")]
                                        if not fancyclothesitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_fishtrap:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/fishtrapidle.png"
                                            hover "inventory/fishtraphover.png"
                                            hovered tt.Action("A Fish Trap\n{color=#997577}A basket made of vines and willow branches. If a large fish swims into it,\nit won’t be able to get out on its own.{/color}"), SetVariable("fishtrapitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "fishtrap")]
                                        if not fishtrapitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                elif northernroad_fishtrap or wanderer_fishtrap or fallentree_fishtrap or ghoulcave_fishtrap or ruinedvillage_fishtrap:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/fishtraplockedidle.png"
                                            hover "inventory/fishtraplockedhover.png"
                                            hovered tt.Action("The Fish Trap Locations\n{color=#997577}The list of fish traps you already set up.{/color}"), SetVariable("fishtrapitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "fishtrap")]
                                        if not fishtrapitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_gambeson01 and not item_gambeson02:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/gambeson01idle.png"
                                            hover "inventory/gambeson01hover.png"
                                            hovered tt.Action("A Gambeson\n{color=#997577}A padded defensive jacket made of linen filled with rags. It’s the cheapest type of armor,\nyet surprisingly effective and, as a result, very common.{/color}"), SetVariable("item_hover_gambeson", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "gambeson01")]
                                        if not item_hover_gambeson:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_gambeson02:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/gambeson02idle.png"
                                            hover "inventory/gambeson02hover.png"
                                            hovered tt.Action("A Strengthened Gambeson\n{color=#997577}A padded defensive jacket made of linen filled with rags. It’s the cheapest type of armor,\nyet surprisingly effective and, as a result, very common.{/color}"), SetVariable("item_hover_gambeson", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "gambeson02")]
                                        if not item_hover_gambeson:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_mageamulets:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/amuletsmageidle.png"
                                            hover "inventory/amuletsmagehover.png"
                                            hovered tt.Action("Magical Amulets\n{color=#997577}Magic is unreliable, so you’ve spent a sack of coins to collect a couple of enhancing amulets.\nThey help you focus your pneuma in ways that you don’t quite understand.{/color}"), SetVariable("item_hover_amuletsmage", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "mageamulets")]
                                        if not item_hover_amuletsmage:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_magicchisel == 1:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/magicchiselidle.png"
                                            hover "inventory/magicchiselhover.png"
                                            hovered tt.Action("The Magic Chisel\n{color=#997577}The {i}treasure{/i} given to you by the villagers from Old Págos.\nEven though it’s made of steel, it’s as warm as your skin."), SetVariable("magicchiselitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "magicchisel")]
                                        if not magicchiselitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_magicchisel == 2:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/magicchiselidle.png"
                                            hover "inventory/magicchiselhover.png"
                                            hovered tt.Action("The Tool of Destruction\n{color=#997577}The trembling {i}treasure{/i} given to you by the villagers from Old Págos.\nEven though it’s made of steel, it’s as warm as your skin."), SetVariable("magicchiselitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "magicchisel2")]
                                        if not magicchiselitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_rope:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/ropeidle.png"
                                            hover "inventory/ropehover.png"
                                            hovered tt.Action("A Rope\n{color=#997577}Made of a durable hemp fiber.\nIt can support the weight of four people with their traveling equipment.{/color}"), SetVariable("item_hover_rope", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "rope")]
                                        if not item_hover_rope:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                # if item_rope: # ropehook
                                #     fixed:
                                #         maximum (106,126)
                                #         minimum (106,126)
                                #         imagebutton:
                                #             style "inventoryimage"
                                #             idle "inventory/ropeidle.png"
                                #             hover "inventory/ropehover.png"
                                #             hovered tt.Action("A Rope\n{color=#997577}Made of a durable hemp fiber.\nIt can support the weight of four people with their traveling equipment.{/color}"), SetVariable("item_hover_rope", "1")
                                #             action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "rope")]
                                #         if persistent.textstyle == "basic":
                                #             text "[item_rope]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                #         if persistent.textstyle == "pixel":
                                #             text "[item_rope]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                #         if not item_hover_rope:
                                #             add "images/inventory/border.png":
                                #                 xpos 0
                                #                 ypos 0
                                #     redukcja rope:
                                #     oldtunnel2 - stawianie deadfall traps, zrzucenie stalaktytu
                                #     highisland0 / 1 - wspinaczka
                                #     można związać zwierzę?
                                if item_scholaringredients:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/scholaringredientsidle.png"
                                            hover "inventory/scholaringredientshover.png"
                                            hovered tt.Action("Alchemical Ingredients\n{color=#997577}To brew new potions, you need to find suitable tools and some undisturbed time.\nBrewing is difficult and your alchemical skills, while humble, are valuable.{/color}"), SetVariable("item_hover_scholaringredients", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "scholaringredients")]
                                        if not item_hover_scholaringredients:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_travelequipment:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/travelequipmentidle.png"
                                            hover "inventory/travelequipmenthover.png"
                                            hovered tt.Action("The Travel Set\n{color=#997577}Your sacks contain all sorts of useful tools.{/color}"), SetVariable("travelequipmentitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "travelset")]
                                        if not travelequipmentitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_witheringdust:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/witheringdustidle.png"
                                            hover "inventory/witheringdusthover.png"
                                            hovered tt.Action("The Withering Dust\n{color=#997577}A leather bag containing poisonous, yellow dust, which can “wither” any plant.{/color}"), SetVariable("item_hover_witheringdust", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "witheringdust")]
                                        if not item_hover_witheringdust:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_lantern:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/lanternidle.png"
                                            hover "inventory/lanternhover.png"
                                            hovered tt.Action("A Wooden Lantern\n{color=#997577}A cheap frame with parchment windows, held together by glue. Not very durable,\nbut much cheaper, quieter, and lighter than the metal ones.{/color}"), SetVariable("item_hover_amuletsmage", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "lantern")]
                                        if not item_hover_amuletsmage:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_writinginstruments:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/writinginstrumentsidle.png"
                                            hover "inventory/writinginstrumentshover.png"
                                            hovered tt.Action("Writing Instruments\n{color=#997577}Parchment scrolls kept in tubes, ink, quills, and wax tablets with a bone stylus.\nMost Northerners are illiterate, but they are happy to meet someone who can write a letter in their name.{/color}"), SetVariable("item_hover_writinginstruments", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "writinginstruments")]
                                        if not item_hover_writinginstruments:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if pc_goal_lost100coins:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/100coinsidle.png"
                                            hover "inventory/100coinshover.png"
                                            if pc_goal == "ineedmoney":
                                                hovered tt.Action("Your Savings\n{color=#997577}The box storing 100 life-saving dragon bones.{/color}"), SetVariable("pc_goal_lost100coins_hover", "1")
                                            if pc_goal == "iwantmoney":
                                                hovered tt.Action("Your Savings\n{color=#997577}The box storing 100 life-changing dragon bones.{/color}"), SetVariable("pc_goal_lost100coins_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "100coins")]
                                        if not pc_goal_lost100coins_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                            if item_axe01 or item_axe02 or item_axe03 or item_axe02alt:
                                label _("Weapons"):
                                    style "inventory_prompt"
                            hbox:
                                ypos 8
                                spacing 16
                                box_wrap True
                                if item_asterionspear:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/asterionspearidle.png"
                                            hover "inventory/asterionspearhover.png"
                                            hovered tt.Action("Asterion’s Spear\n{color=#997577}A long spear with an oak shaft, steel head, and an old linen cord in the middle.{/color}"), SetVariable("item_hover_asterionspear", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "asterionspear")]
                                        if not item_hover_asterionspear:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_axe01:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/axe01idle.png"
                                            hover "inventory/axe01hover.png"
                                            hovered tt.Action("A Simple Battle Axe\n{color=#997577}Traveling with an axe shows that you’ve learned how to fight humans and human-sized monsters.\nIt's not masterfully made, but it’s already been put to test and you’ve practiced with it for many days.{/color}"), SetVariable("item_hover_axe01", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "axe01")]
                                        if not item_hover_axe01:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_axe02:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/axe02idle.png"
                                            hover "inventory/axe02hover.png"
                                            hovered tt.Action("A Well-Crafted Battle Axe\n{color=#997577}Traveling with an axe shows that you’ve learned how to fight humans and human-sized monsters,\nwhile having a weapon made of steel makes it clear that you are someone to be reckoned with.{/color}"), SetVariable("item_hover_axe02", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "axe02")]
                                        if not item_hover_axe02:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_axe03:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/axe03idle.png"
                                            hover "inventory/axe03hover.png"
                                            hovered tt.Action("A Brand-New Battle Axe\n{color=#997577}A steel axe that you purchased in Howler’s Dell.\nIt’s as sharp as can be, well balanced, and light.{/color}"), SetVariable("item_hover_axe03", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "axe03")]
                                        if not item_hover_axe03:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_axe02alt:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/axe02altidle.png"
                                            hover "inventory/axe02althover.png"
                                            hovered tt.Action("A Bronze Axe\n{color=#997577}Its head has seen some better days, but decent bronze can endure centuries.\nIt’s slightly heavier than steel and, with some sharpening, will serve you well in combat.{/color}"), SetVariable("axe02altitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "axe02alt")]
                                        if not axe02altitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_blindingpowder:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/blindingpowderidle.png"
                                            hover "inventory/blindingpowderhover.png"
                                            hovered tt.Action("The Blinding Powder\n{color=#997577}A pouch of magical dust which hurts any creatures’ eyes and mouth.{/color}"), SetVariable("blindingpowderitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "blindingpowder")]
                                        if not blindingpowderitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_crossbow:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            if item_crossbowquarrels:
                                                idle "inventory/crossbowidle.png"
                                                hover "inventory/crossbowhover.png"
                                            else:
                                                idle "inventory/crossbowlockedidle.png"
                                                hover "inventory/crossbowlockedhover.png"
                                            hovered tt.Action("A Crossbow\n{color=#997577}Difficult to make and valued for their usefulness, crossbows can be used even by\nan inexperienced traveler, and can pierce most scales and armors.{/color}"), SetVariable("item_hover_crossbow", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "crossbow")]
                                        if persistent.textstyle == "basic":
                                            text "[item_crossbowquarrels]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_crossbowquarrels]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not item_hover_crossbow:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_crossbowquarrels and not item_crossbow:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/quarrelsidle.png"
                                            hover "inventory/quarrelshover.png"
                                            hovered tt.Action("The Crossbow Quarrels\n{color=#997577}A supply of arrows made for a crossbow -\na weapon that you do not possess.{/color}"), SetVariable("crossbowquarrelsitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "crossbowquarrels")]
                                        if persistent.textstyle == "basic":
                                            text "[item_crossbowquarrels]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                        if persistent.textstyle == "pixel":
                                            text "[item_crossbowquarrels]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                                        if not crossbowquarrelsitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_golemglove:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/golemgloveidle.png"
                                            hover "inventory/golemglovehover.png"
                                            hovered tt.Action("The Golem Glove\n{color=#997577}The floating rocks are clenching to the back of your hand,\nadding brutal weight to your hits without encumbering you.{/color}"), SetVariable("item_hover_golemglove", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "golemglove")]
                                        if not item_hover_golemglove:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_shield:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            if item_shield == 1:
                                                idle "inventory/shield1idle.png"
                                                hover "inventory/shield1hover.png"
                                                hovered tt.Action("A Shield\n{color=#997577}A wooden shield covered with decorated leather\nattached to the surface with a steel frame and rivets.{/color}"), SetVariable("shielditem_hover", "1")
                                            if item_shield == 2:
                                                idle "inventory/shield2idle.png"
                                                hover "inventory/shield2hover.png"
                                                hovered tt.Action("A Shield\n{color=#997577}A wooden shield covered with decorated leather\nattached to the surface with steel rivets.{/color}"), SetVariable("shielditem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "shield")]
                                        if not shielditem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                                if item_mountainroadspear:
                                    fixed:
                                        maximum (106,126)
                                        minimum (106,126)
                                        imagebutton:
                                            style "inventoryimage"
                                            idle "inventory/mountainroadspearidle.png"
                                            hover "inventory/mountainroadspearhover.png"
                                            hovered tt.Action("A Spear\n{color=#997577}A simple spear with an ash shaft and an iron head.\nThe bar at the end of the blade stops it from getting too deep into the flesh.{/color}"), SetVariable("mountainroadspearitem_hover", "1")
                                            action [SetVariable("inventoryscreenmode", "details"), SetVariable("item_detailedmenu", "mountainroadspear")]
                                        if not mountainroadspearitem_hover:
                                            add "images/inventory/border.png":
                                                xpos 0
                                                ypos 0
                    vbar value YScrollValue ("allitems"):
                        xpos -50
                        unscrollable "hide"
        if inventoryscreenmode == "details":
            vbox:
                frame:
                    xpos 1
                    # maximum (1025,112)
                    minimum (1025,112)
                    right_padding 24
                    hbox:
                        spacing 20
                        ypos -1
                        xpos -1
                        maximum (1025,102)
                        minimum (0,102)
                        if item_detailedmenu == "thyrsusgift":
                            add "inventory/thyrsusgiftidle.png"
                            label _("Thyrsus’ Gift"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "stingointment":
                            add "inventory/stingointmentidle.png"
                            label _("A Sting Ointment"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "antlers":
                            add "inventory/antlersidle.png"
                            label _("A Set of Antlers"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "asterionbow":
                            add "inventory/asterionbowidle.png"
                            label _("Asterion’s Bow"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "asterionwine":
                            add "inventory/asterionwineidle.png"
                            if item_asterionwine_pcknows_2:
                                label _("Night’s Bane"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                            elif item_asterionwine_pcknows_1:
                                label _("Asterion’s Wine"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                            else:
                                label _("Asterion’s Bottle"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                        if item_detailedmenu == "asterioncloak":
                            add "inventory/asterioncloakidle.png"
                            label _("Asterion’s Cloak"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "smallhealingpotion" or item_detailedmenu == "smallhealingpotiondrunk":
                            add "inventory/smallhealingpotionidle.png"
                            label _("A Small Healing Potion"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "asterionpurse" or item_detailedmenu == "asterionpurseopened":
                            add "inventory/asterionpurseidle.png"
                            label _("Asterion’s Pouch"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "asterionspear":
                            add "inventory/asterionspearidle.png"
                            label _("Asterion’s Spear"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "asteriontablet":
                            add "inventory/asteriontabletidle.png"
                            label _("A Wax Tablet"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "axe01":
                            add "inventory/axe01idle.png"
                            label _("A Simple Battle Axe"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "axe02":
                            add "inventory/axe02idle.png"
                            label _("A Well-Crafted Battle Axe"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "axe02alt" or item_detailedmenu == "axesetputtingtogether":
                            add "inventory/axe02altidle.png"
                            label _("A Bronze Axe"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "axehead":
                            add "inventory/axeheadidle.png"
                            label _("A Bronze Axe Head"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "axeset":
                            add "inventory/axesetidle.png"
                            label _("An Axe Head With A Handle"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "axe03":
                            add "inventory/axe03idle.png"
                            label _("A Brand-New Battle Axe"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "arrow":
                            add "inventory/arrowidle.png"
                            if not aegidia_about_arrow:
                                label _("A Simple Arrow"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                            else:
                                label _("A Human Arrow"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                        if item_detailedmenu == "beholderroot":
                            add "inventory/beholderrootidle.png"
                            label _("A Weird Root"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "blindingpowder":
                            add "inventory/blindingpowderidle.png"
                            label _("The Blinding Powder"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "boartusks":
                            add "inventory/boartusksidle.png"
                            label _("Boar Tusks"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "bonebuckle":
                            add "inventory/bonebuckleidle.png"
                            label _("A Decorative Buckle"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "boneearring":
                            add "inventory/boneearringidle.png"
                            label _("A Bone Earring"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "bonehook":
                            add "inventory/bonehookidle.png"
                            label _("A Bone Hook"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "bonering":
                            add "inventory/boneringidle.png"
                            label _("A Bone Ring"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "boxfromdolmen" or item_detailedmenu == "boxfromdolmenopened":
                            add "inventory/boxfromdolmenidle.png"
                            if item_detailedmenu == "boxfromdolmenopened":
                                label _("A Box from the Dolmen (opened)"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                            else:
                                label _("A Box from the Dolmen"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                        if item_detailedmenu == "brokenknife":
                            add "inventory/brokenknifeidle.png"
                            label _("The Broken Knife"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "bugrepellent":
                            add "inventory/bugrepellentidle.png"
                            label _("A Herbal Bug Repellent"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "chicken" or item_detailedmenu == "chickeneating":
                            fixed:
                                maximum (102,102)
                                minimum (102,102)
                                add "inventory/chickenidle.png"
                                if persistent.textstyle == "basic":
                                    text "[item_chicken]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                if persistent.textstyle == "pixel":
                                    text "[item_chicken]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                            label _("A Roast Chicken"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "cidercask":
                            add "inventory/cidercaskidle.png"
                            label _("A Cask of Cider"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "peltnorthberries" or item_detailedmenu == "peltnorthberrieseaten":
                            add "inventory/berriespeltnorthidle.png"
                            label _("A Bucketful of Berries"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "peltnorthberrytools02":
                            add "inventory/toolsberriesidle02.png"
                            label _("A Berry Picking Hook"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "peltnorthberrytools":
                            add "inventory/toolsberriesidle.png"
                            label _("Tools for Berry Picking"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "peltnorthberryclaw":
                            add "inventory/clawpeltnorthidle.png"
                            label _("A Pebbler’s Claw"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        # if item_detailedmenu == "cloak01":
                        #     add "inventory/cloakidle.png"
                        #     label _("A Cloak with a Hood"):
                        #         style "invdetailedmenu_prompt"
                        #         yalign 0.5
                        if item_detailedmenu == "coins":
                            fixed:
                                maximum (102,102)
                                minimum (102,102)
                                add "inventory/coinscoupleidle.png"
                                if persistent.textstyle == "basic":
                                    text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                if persistent.textstyle == "pixel":
                                    text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                            label _("A Pouch with Coins"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "cookedfish":
                            fixed:
                                maximum (102,102)
                                minimum (102,102)
                                if not item_cookedfish:
                                    add "inventory/cookedfishlockedidle.png"
                                else:
                                    add "inventory/cookedfishidle.png"
                                if persistent.textstyle == "basic":
                                    text "[item_cookedfish]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                if persistent.textstyle == "pixel":
                                    text "[item_cookedfish]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                            label _("Roast Fish"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "crossbow":
                            fixed:
                                maximum (102,102)
                                minimum (102,102)
                                add "inventory/crossbowidle.png"
                                if persistent.textstyle == "basic":
                                    text "[item_crossbowquarrels]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                if persistent.textstyle == "pixel":
                                    text "[item_crossbowquarrels]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                            label _("A Crossbow"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "crossbowquarrels":
                            fixed:
                                maximum (102,102)
                                minimum (102,102)
                                add "inventory/quarrelsidle.png"
                                if persistent.textstyle == "basic":
                                    text "[item_crossbowquarrels]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                if persistent.textstyle == "pixel":
                                    text "[item_crossbowquarrels]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                            label _("The Crossbow Quarrels"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "dragonhorn":
                            add "inventory/dragonhornidle.png"
                            label _("A Dragon Horn"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "empresscarp" or item_detailedmenu == "empresscarpcheck":
                            add "inventory/empresscarpidle.png"
                            label _("An Empress Carp"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "spiritrock" or item_detailedmenu == "spiritrockeaten":
                            add "inventory/spiritrockidle.png"
                            label _("A Spirit Rock"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "sharpeningpotion" or item_detailedmenu == "sharpeningpotionconsume":
                            add "inventory/sharpeningpotionidle.png"
                            label _("A Sharpening Poison"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "eudociaflower":
                            add "inventory/snakebaitidle.png"
                            label _("Snake Bait"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "fancyclothes":
                            if item_fancyclothes == 1:
                                add "inventory/fancyclothes1idle.png"
                                label _("A Fancy Tunic"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                            if item_fancyclothes == 2:
                                add "inventory/fancyclothes2idle.png"
                                label _("A Fancy Robe"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                            if item_fancyclothes == 3:
                                add "inventory/fancyclothes3idle.png"
                                label _("A Fancy Dress"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                        if item_detailedmenu == "oceannecklace":
                            add "inventory/oceannecklaceidle.png"
                            label _("An Ocean Necklace"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "fishtrap":
                            if item_fishtrap:
                                add "inventory/fishtrapidle.png"
                                label _("A Fish Trap"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                            else:
                                add "inventory/fishtraplockedidle.png"
                                label _("The Fish Trap Locations"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                        if item_detailedmenu == "golemglove":
                            add "inventory/golemgloveidle.png"
                            label _("The Golem Glove"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "griffonegg":
                            add "inventory/griffoneggidle.png"
                            label _("A Griffon Egg"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "rations":
                            fixed:
                                maximum (102,102)
                                minimum (102,102)
                                if not item_rations:
                                    add "inventory/foodrationslockedidle.png"
                                else:
                                    add "inventory/foodrationsidle.png"
                                if persistent.textstyle == "basic":
                                    text "[item_rations]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                if persistent.textstyle == "pixel":
                                    text "[item_rations]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                            label _("Food Rations"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "furlesswolftrophy":
                            add "inventory/furlesswolftrophyidle.png"
                            label _("A Head of a Beast"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "furs":
                            add "inventory/fursidle.png"
                            label _("Furs and Skins"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "gambesonrepairset":
                            add "inventory/gambesonrepairsetidle.png"
                            label _("A Gambeson Repair Set"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "gambeson01":
                            add "inventory/gambeson01idle.png"
                            label _("A Gambeson"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "gambeson02":
                            add "inventory/gambeson02idle.png"
                            label _("A Strengthened Gambeson"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "generichealingpotion" or item_detailedmenu == "generichealingpotiondrunk":
                            add "inventory/generichealingpotionidle.png"
                            label _("A Fresh Healing Potion"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "ghoulblood":
                            add "inventory/ghoulbloodidle.png"
                            label _("Corpse Eater’s Blood"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "goblinrepellent":
                            add "inventory/goblinrepellentidle.png"
                            label _("A Jar Of Troll’s Urine"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "goblinspear":
                            add "inventory/goblinspearidle.png"
                            label _("A Goblin Spear"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "bronzerod":
                            add "inventory/bronzerodidle.png"
                            label _("Bronze Rods"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "howlersdelltoken":
                            add "inventory/howlersdelltokenidle.png"
                            label _("The “Token of Gratitude”"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "horse01":
                            add "inventory/horse1idle.png"
                            label _("[horsename]"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "ironingot":
                            add "inventory/ironingotidle.png"
                            label _("An Iron Ingot"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "ironscraps":
                            add "inventory/ironscrapsidle.png"
                            label _("Iron Scraps"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "keysidle":
                            add "inventory/keys3idle.png"
                            label _("Keys"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "lantern":
                            add "inventory/lanternidle.png"
                            label _("A Wooden Lantern"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "linen":
                            add "inventory/linenidle.png"
                            label _("A Stack of Linen Fabric"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "lostmanblanket":
                            add "inventory/lostmanblanketidle.png"
                            label _("An Old Blanket"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "mageamulets":
                            add "inventory/amuletsmageidle.png"
                            label _("Magical Amulets"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "magicalsapling":
                            add "inventory/magicalsaplingidle.png"
                            label _("Eudocia’s Sapling"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "magicchisel":
                            add "inventory/magicchiselidle.png"
                            label _("The Magic Chisel"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "magicchisel2":
                            add "inventory/magicchiselidle.png"
                            label _("The Tool of Destruction"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "magicfruit" or item_detailedmenu == "magicfruiteating":
                            add "inventory/magicfruitidle.png"
                            if druidcave_druid_about_plague01 or howlersdell_elpis_about_magicfruit:
                                label _("The Seed"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                            else:
                                label _("A Weird Fruit"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                        if item_detailedmenu == "magicpens":
                            add "inventory/magicpensidle.png"
                            label _("A Set of Magic Quills"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "mountainroadspear":
                            add "inventory/mountainroadspearidle.png"
                            label _("A Spear"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "pileofbones" or item_detailedmenu == "item_pileofbones_destroyed":
                            add "inventory/pileofbonesidle.png"
                            label _("The Human Bones"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "potiondolmen" or item_detailedmenu == "potiondolmendrunk":
                            add "inventory/potiondolmenidle.png"
                            if not item_potiondolmen_known:
                                if item_detailedmenu == "potiondolmendrunk":
                                    label _("A Bottle from the Dolmen (empty)"):
                                        style "invdetailedmenu_prompt"
                                        yalign 0.5
                                else:
                                    label _("A Bottle from the Dolmen"):
                                        style "invdetailedmenu_prompt"
                                        yalign 0.5
                            else:
                                if item_detailedmenu == "potiondolmendrunk":
                                    label _("A Potion from the Dolmen (empty)"):
                                        style "invdetailedmenu_prompt"
                                        yalign 0.5
                                else:
                                    label _("A Potion from the Dolmen"):
                                        style "invdetailedmenu_prompt"
                                        yalign 0.5
                        if item_detailedmenu == "rawfish":
                            add "inventory/rawfishidle.png"
                            label _("Raw Fish"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        # if item_detailedmenu == "rope": # ropehook
                        #     fixed:
                        #         maximum (102,102)
                        #         minimum (102,102)
                        #         add "inventory/ropeidle.png"
                        #         if persistent.textstyle == "basic":
                        #             text "[item_rope]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        #         if persistent.textstyle == "pixel":
                        #             text "[item_rope]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                        #     label _("A Rope"):
                        #         style "invdetailedmenu_prompt"
                        #         yalign 0.5
                        if item_detailedmenu == "rope":
                            add "inventory/ropeidle.png"
                            label _("A Rope"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "spices":
                            add "inventory/spicesidle.png"
                            label _("The Sacks of Spices"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "letterwhitemarshes":
                            if item_letterwhitemarshes == 1:
                                add "inventory/letterwhitemarshesidle.png"
                            elif item_letterwhitemarshes == 2:
                                add "inventory/letterwhitemarshes2idle.png"
                            label _("The Troll-Bone Tablet"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "dragonlingclaws":
                            add "inventory/dragonlingclawsidle.png"
                            label _("A Set of Dragonling’s Claws"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "cavemushroom":
                            add "inventory/cavemushroomidle.png"
                            label _("A Cave Ear"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "casket" or item_detailedmenu == "caskettaken":
                            add "inventory/casketidle.png"
                            label _("A Casket of Coins"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "dragonlingpaw":
                            add "inventory/dragonlingpawidle.png"
                            label _("A Dragonling’s Paw"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "scholaringredients":
                            add "inventory/scholaringredientsidle.png"
                            label _("Alchemical Ingredients"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "sewingkit" or item_detailedmenu == "sewingkit2" or item_detailedmenu == "sewingkit3":
                            add "inventory/sewingkitidle.png"
                            label _("A Sewing Kit"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "signpost":
                            add "inventory/signpostidle.png"
                            label _("A Painted Sign"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "shield":
                            if item_shield == 1:
                                add "inventory/shield1idle.png"
                            if item_shield == 2:
                                add "inventory/shield2idle.png"
                            label _("A Shield"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "spidersilk":
                            add "inventory/spidersilkidle.png"
                            label _("Spider Silk"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "stoat":
                            add "inventory/stoatidle.png"
                            label _("A Dead Stoat"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "teethset":
                            add "inventory/teethsetidle.png"
                            label _("A Teeth-Cleaning Set"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "thaisletter":
                            add "inventory/thaisletter01idle.png"
                            label _("The Letter From Thais (sealed)"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "thaisletteropened":
                            add "inventory/thaisletter02idle.png"
                            label _("The Letter From Thais (opened)"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "travelset" or item_detailedmenu == "travelequipmentearplugs":
                            add "inventory/travelequipmentidle.png"
                            label _("The Travel Set"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "wildplants":
                            fixed:
                                maximum (102,102)
                                minimum (102,102)
                                add "inventory/wildplantsidle.png"
                                if persistent.textstyle == "basic":
                                    text "[item_wildplants]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                                if persistent.textstyle == "pixel":
                                    text "[item_wildplants]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                            label _("Wild Plants"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "wingedhourglass":
                            add "inventory/wingedhourglassidle.png"
                            if item_wingedhourglass_worn:
                                label _("A Winged Hourglass (worn)"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                            else:
                                label _("A Winged Hourglass (hidden)"):
                                    style "invdetailedmenu_prompt"
                                    yalign 0.5
                        if item_detailedmenu == "witheringdust":
                            add "inventory/witheringdustidle.png"
                            label _("The Withering Dust"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "writinginstruments":
                            add "inventory/writinginstrumentsidle.png"
                            label _("Writing Instruments"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5
                        if item_detailedmenu == "100coins":
                            add "inventory/100coinsidle.png"
                            label _("Your Savings"):
                                style "invdetailedmenu_prompt"
                                yalign 0.5

                vbox:
                    #style_prefix "journal"
                    xalign 0.0
                    #yalign 0.5
                    xmaximum 1000
                    ymaximum 2000
                    xpos 20
                    ypos 30
                    spacing 20
                    style_prefix "invdetailedmenu"
                    hbox:
                        xmaximum 1000
                        viewport id "inventoryscroll":
                            draggable True
                            ymaximum 700
                            mousewheel True
                            arrowkeys True
                            vbox:
                                spacing 20
                                if item_detailedmenu == "thyrsusgift":
                                    text "An old, slightly moldy bundle that contains a doll, a small shirt, a broken wand, and a vine-shaped buckle."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "stingointment":
                                    text "This green and blue combination of herbs includes basil, mint, and lavender, and its smell is unpleasantly overwhelming. While edible, it won’t fill an angry stomach. Safe for human skin."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "antlers":
                                    text "Antlers are one of the very few goods which can be collected from wild beasts without harming them, and, for that matter, without encountering them at all. Every spring, groups of hunters and foragers combine their efforts to collect these bone-like remains left behind by all sorts of deers, usually males, though the time is not on the side of humans. For some reason, many animals chew on the antlers, making them unusable."
                                    text "No matter if the antlers were dropped by its owner willingly or cut away from a wild game, they can be used in all sorts of crafts. Their shape and size rarely allows one to turn them into weapons and tools, but it’s easy to carve and polish them with simple tools. They are a great base for small sculptures, combs, tool handles, clamps, buckles, gaming pieces, dice, toys, and many more. They’re also a cheaper replacement for the novices who wish to master the art of bone carving."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "asterionbow":
                                    text "As heavy breastplates are uncommon in the North, it’s not rare to finish off an opponent before they get close enough to make use of their close-range weapons. Bows are also valued among hunters, who use them to kill small or medium game without completely destroying the furs and skins."
                                    text "While the basics of crossbows can be learned in less than an hour, bows require years, if not decades, of regular training that may lead to injuries. The bows require a strong back and arms, and mastering a bunch of techniques related to drawing, maintaining a proper stance while moving, aiming, speed... On the other hand, they can be prepared for combat in just a few breaths and may be used even more than ten times per minute. "
                                    text "The simplest of bows don’t require much more than flexible wood, linen, hemp, and some leather straps. They are not expensive to make, but rarely provide the amount of power that is required to pierce through shields and chitin armors, or, perhaps more importantly, through the scales and fur of larger beasts. The type of wood used is particularly important and the longer the bow gets, the more power it requires to be fully drawn."
                                    text "Asterion’s bow was made of a sapling of a red oak. The string is still fresh, made of linen, and the leather straps won’t need replacement anytime soon. Putting the string on and off is not easy and you’re surprised by the strength it takes to draw it."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "asterioncloak":
                                    text "Cloaks are always popular, especially on the colder days. They are long enough to cover an entire shell, so cityfolk tend to embellish them with colorful threads and pieces of jewelry. Travelers, however, are more focused on utility, so they wear cloaks of thick and multilayered cloth, made of various fabrics at once, including linen, wool, and skins. The best cloaks are rainproof and keep the wearer warm in autumn."
                                    text "Asterion’s cloak is unusually soft and as you cover yourself with it, you feel an unnatural warmth and coziness."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "smallhealingpotion":
                                    text "You recognize a magical potion when you see one - it has a tall wax seal, inside of which there’s a thin stick, enabling swift opening. According to what you’ve heard, it’s a healing potion, but you estimate that it’s not enough to heal an entire shell."
                                    text "Healing potions may be the most desired liquid in The Dragonwoods, especially among travelers, hunters, and fighters."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items or can_potions:
                                        if item_smallhealingpotion:
                                            if (pc_hp < 4 and not pc_hp_can5) or (pc_hp < 5 and pc_hp_can5):
                                                textbutton _("Drink the potion") action [SetVariable("item_smallhealingpotion", item_smallhealingpotion-1), SetVariable("pc_hp", limit_pc_hp(pc_hp+2)), SetVariable("inventoryinteraction", 1), SetVariable("item_detailedmenu", "smallhealingpotiondrunk")]
                                            else:
                                                text "{color=#6a6a6a}You don’t need to heal your shell right now{/color}"
                                        else:
                                            text "{color=#6a6a6a}You already drank the last bottle{/color}"
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "smallhealingpotiondrunk":
                                    if can_potions and not can_items:
                                        text "You vaguely recognize some of the local, fruity tastes. There’s a sort of unpleasant bitterness to it, maybe wormwood, and every sip makes it even more strange and disgusting."
                                        text "An ecstatic warmth fills your limbs and you can’t help but smile for a moment."
                                    else:
                                        text "You vaguely recognize some of the local, fruity tastes. There’s a sort of unpleasant bitterness to it, maybe wormwood, and every sip makes it even more strange and disgusting."
                                        text "You finish the bottle quickly and prepare your waterskin to rinse your mouth. Your shell feels refreshed, stronger. An ecstatic warmth fills your limbs and you can’t help but smile for a moment."
                                    add "gui/statuspoints/hp/plus2hp.png":
                                        xalign 0.5
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("inventoryinteraction", 0), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                    timer 0.1 action [SetVariable("appearance", calculate_appearance(0))]
                                    timer 0.2 action [SetVariable("appearance_charisma", calculate_appearance_charisma(0)), SetVariable("appearance_price", calculate_appearance_price(0))]
                                if item_detailedmenu == "asterionpurse":
                                    text "You toss up the linen pouch and hear not only some dragon bones, but also the sound of bone hitting a piece of metal."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        textbutton _("Open the pouch") action [SetVariable("item_asterionpurse", 0), SetVariable("coins", coins+6), SetVariable("item_asterionkey", 1), SetVariable("item_detailedmenu", "asterionpurseopened")]
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "asterionpurseopened":
                                    text "Turns out that the large piece of metal was an iron key, but there is no clue explaining its purpose."
                                    text "Aside from that, you’ve found six dragon bones"
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "asterionspear":
                                    text "Spears are the most common type of weapon used in The Dragonwoods, but it’s impossible to describe how a “regular” spear looks. The name covers everything from flexible, pointed sticks; through polished, processed branches with spearheads made of rock or bone; to masterfully preserved, rounded woodblocks with heads made of iron, copper, bronze, or steel. Some designs are characteristic for areas or tribes and have unique names, but there are also hundreds of types of spears that take into account available resources, artisans’ experience, the weapon’s purpose, and customers’ individual preferences."
                                    text "The difference between a fighter specialized in using spears and a greenhorn is vast, but it’s common for untrained travelers to carry long-range weapons just in case. It helps them keep their distance and allows them to jab at their opponent when an opportunity arises. A group of villagers with spears is like a moving wall and shouldn’t be underestimated."
                                    text "On the other hand, some fighters and monsters are capable of shortening the distance quickly and getting to the spear bearer. In such situations, this weapon becomes close to useless, so most spear masters train in another type of martial art and carry a shorter weapon as a backup."
                                    text "Asterion spared no expense. Oak makes the shaft exceptionally hard, allowing it to endure a lot of pressure despite its length. The spearhead is finely sharpened and was covered with an oiled cloth that kept the iron from rusting. The linen strip could be replaced with leather, but even now it’s going to firm your grasp."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "asterionwine":
                                    text "This bottle was previously owned by Asterion. It’s closed, but not sealed."
                                    if pc_class == "scholar":
                                        text "There are two letters engraved on its surface: “NB.”"
                                    else:
                                        text "There are two letters engraved on its surface, but you don’t recognize them."
                                    if item_asterionwine_pcknows_2:
                                        text "The smell coming from the inside is both fruity and floral. It brings to the soul sweet berries, sour apples, and violets. You need a good minute to detect the scent of a hard drink."
                                        text "You were told that this bottle contains {i}Night’s Bane{/i}, a very rare and expensive type of wine produced beyond The Growing Mountains."
                                        text "Such bottles are not only a valuable find, but also a valued gift among friends and associates."
                                        if pc_goal == "iwantmoney":
                                            text "Taking this back to Hovlavan is surely going to secure your future for many years to come, as long as you get the merchant guild pay as well."
                                        if pc_goal == "ineedmoney":
                                            text "Taking this back to Hovlavan is surely going to save your sibling from debt collectors, as long as you get the merchant guild pay as well."
                                    elif item_asterionwine_pcknows_1:
                                        text "The smell coming from the inside is both fruity and floral. It brings to the soul sweet berries, sour apples, and violets. You struggle to detect the scent of a hard drink, but once you find it, it’s clear that it’s wine."
                                        text "In The Cities, such drinks are considered rare and often get expensive. The only ones you’ve tasted were made locally and considered to be of low quality."
                                        text "This one here may be the real deal, but you’d need an expert to confirm it."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if not item_asterionwine_pcknows_1:
                                        if can_items:
                                            textbutton _("Open and sniff the bottle") action [SetVariable("item_asterionwine_pcknows_1", 1)]
                                        else:
                                            text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "asteriontablet":
                                    text "These planks holding a thick layer of beeswax are the most common writing instrument used in the North. The pointed stylus can be made of wood, bone, or metal. Tablets usually fit in one’s hand and are used to make notes or write down short messages, especially when there’s no option to prepare a scroll and inkstand. It’s also easy to erase the previous inscriptions, and a single tablet may be used dozens or hundreds of times."
                                    if pc_class == "scholar":
                                        text "As far as you can tell, this tablet is filled with small pictures and chaotic notes focused on the construction of boats and oars. One word seems to be a name: {i}Navica{/i}. Could it be Asterion’s tablet that Tulia mentioned to you?"
                                    else:
                                        if not item_asteriontablet_read:
                                            text "Being illiterate, you can’t decipher the letters and weird shapes drawn by the previous owner, but you remember that Tulia has mentioned something about a wax tablet used by Asterion. Maybe there’s someone who could read it for you?"
                                        else:
                                            text "As far as you can tell, the tablet is filled with small pictures and chaotic notes focused on the construction of boats and oars. One word seems to be a name: {i}Navica{/i}."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "axe01":
                                    text "Axes made of metals or alloys are among the most common weapons used by travelers. Not as safe as spears, not as fancy as swords, but their powerful strikes can get through animal shells, scales, or thick furs, as well as most armors. They are not great when it comes to parrying, but a single strike may be enough to leave a devastating wound."
                                    text "Still, the vast majority of them are used by lumberjacks, farmers, or carpenters, and pretty much every household in the countryside owns at least one, just in case. Their shapes, sizes, and used materials vary. Heads are made of stone (especially flint), bones, chitin, and massive seashells, while handles are almost always made of wood, antlers, and leather straps."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "axe02":
                                    text "Axes made of metals or alloys are among the most common weapons used by travelers. Not as safe as spears, not as fancy as swords, but their powerful strikes can get through animal shells, scales, or thick furs, as well as most armors. They are not great when it comes to parrying, but a single strike may be enough to leave a devastating wound."
                                    text "Still, the vast majority of them are used by lumberjacks, farmers, or carpenters, and pretty much every household in the countryside owns at least one, just in case. Their shapes, sizes, and used materials vary. Heads are made of stone (especially flint), bones, chitin, and massive seashells, while handles are almost always made of wood, antlers, and leather straps."
                                    text "You’ve spent a lot of time training how to fight and like most warriors, your grip is reliable. If needed, you can throw an axe to hit a target over a dozen feet away."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "axehead":
                                    text "Bronze is highly regarded for its durability, appearance, and the ease with which it’s forged. It’s more reliable than iron, and for centuries was the prime choice among all the fighters who could afford it. As the centuries went by and the artisans invented advanced types of steel, bronze became obsolete, especially since it requires not only the fairly common copper, but also an extremely rare tin, which seems to be pretty much depleted in the North."
                                    if item_axe03:
                                        text "This axe head is a bit heavier than you’d like it to be, but it’s still a decent blade, though not as fine as the one you bought in Howler’s Dell. It requires a new wooden handle and a bit of work."
                                    elif item_axe02:
                                        text "This axe head is a bit heavier than you’d like it to be, but it’s still a decent blade, about as useful as the one you’re already carrying. It requires a new wooden handle and a bit of work."
                                    elif item_axe01:
                                        text "This axe head is a bit heavier than you’d like it to be, but it’s surely a finer blade than the one you’re carrying. It requires a new wooden handle and a bit of work."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "axeset":
                                    text "Bronze is highly regarded for its durability, appearance, and the ease with which it’s forged. It’s more reliable than iron, and for centuries was the prime choice among all the fighters who could afford it. As the centuries went by and the artisans invented advanced types of steel, bronze became obsolete, especially since it requires not only the fairly common copper, but also an extremely rare tin, which seems to be pretty much depleted in the North."
                                    if item_axe03:
                                        text "This axe head is a bit heavier than you’d like it to be, but it’s still a decent blade, though not as fine as the one you bought in Howler’s Dell."
                                    elif item_axe02:
                                        text "This axe head is a bit heavier than you’d like it to be, but it’s still a decent blade, about as useful as the one you’re already carrying."
                                    elif item_axe01:
                                        text "This axe head is a bit heavier than you’d like it to be, but it’s surely a finer blade than the one you’re carrying."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        if (pc_area == "militarycamp") or (pc_area == "howlersdell") or (pc_area == "foggylake") or (pc_area == "peltnorth" and not peltnorth_ban_perm) or (pc_area == "druidcave") or (pc_area == "monastery") or (pc_area == "watchtower" and watchtower_open) or (pc_area == "eudociahouse" and eudocia_sleep_available and not eudocia_ban) or (pc_area == "eudociahouseinside" and eudocia_sleep_available and not eudocia_ban) or (pc_area == "creeks") or (pc_area == "galerocks") or (pc_area == "whitemarshes") or (pc_area == "greenmountaintribe"):
                                            textbutton _("Spend some time putting it together") action [SetVariable("item_axeset", 0), SetVariable("item_axe02alt", 1), SetVariable("quarters", quarters+4), SetVariable("item_detailedmenu", "axesetputtingtogether")]
                                        else:
                                            text "{color=#6a6a6a}To put it together you need better working conditions - a settlement or an inn would do{/color}"
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "axesetputtingtogether":
                                    text "You gather your tools and let your mount relax for a bit. The entire procedure takes you almost an hour - the kerf saves you a lot of time, but using the simple wooden logs and surfaces to put the head in its new place takes a lot of effort, and you do your best to make sure the wooden wedge will get to the bottom of the cut. At one point you’re almost sure it’s all for nothing, but the next good hit eases your thoughts. The wedge squeezes in, and just in case, you tie it all with a cord. You take a few swings, then strike a log. The weapon holds."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Sharpen the blade and put it with the rest of your equipment") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "axe02alt":
                                    text "Bronze is highly regarded for its durability, appearance, and the ease with which it is forged. It’s much more reliable than iron, and for centuries was the prime choice among all the fighters who could afford it. As the centuries went by and the craftspeople invented advanced forms of steel, bronze became obsolete, especially since it requires not only the fairly common copper, but also an extremely rare tin, which seems to be pretty much depleted in the North."
                                    if item_axe03:
                                        text "This axe head is a bit heavier than you’d like it to be, but it’s still a decent blade, though not as fine as the one you bought in Howler’s Dell."
                                    elif item_axe02:
                                        text "This axe head is a bit heavier than you’d like it to be, but it’s still a decent blade, about as useful as the one you’re already carrying."
                                    elif item_axe01:
                                        text "This axe head is a bit heavier than you’d like it to be, but it’s surely a finer blade than the one you’re carrying."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "axe03":
                                    text "Axes made of metals or alloys are among the most common weapons used by travelers. Not as safe as spears, not as fancy as swords, but their powerful strikes can get through animal shells, scales, or thick furs, as well as most armors. They are not great when it comes to parrying, but a single strike may be enough to leave a devastating wound."
                                    text "Still, the vast majority of them are used by lumberjacks, farmers, or carpenters, and pretty much every household in the countryside owns at least one, just in case. Their shapes, sizes, and used materials vary. Heads are made of stone (especially flint), bones, chitin, and massive seashells, while handles are almost always made of wood, antlers, and leather straps."
                                    text "While most axes that you’ve trained with had larger, heavier heads, you get used to its feel quickly. After some practice you’ll be able to rely on it just fine."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "arrow":
                                    if galerocks_arrow_clue:
                                        text "You found it in the south-eastern part of the woods, near a fallen tree. The feathers used in this fletching originally belonged to one of the local pheasants, such as those you’ve seen in Gale Rocks."
                                    elif pc_class == "scholar" or eudocia_about_arrow:
                                        text "You found it in the south-eastern part of the woods, near a fallen tree. The feathers used in this fletching originally belonged to one of the local pheasants."
                                    else:
                                        text "You found it in the south-eastern part of the woods, near a fallen tree. You don’t recognize the type of bird feathers used in this fletching."
                                    if aegidia_about_arrow or galerocks_florus_about_arrow:
                                        text "Arrows like this one are believed to possess magical properties and are used to fight humans."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "beholderroot":
                                    text "A hybrid between wood and flesh, covered with hair and partially sunk in its own, red ooze. When taken out, it twitches on its own."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "blindingpowder":
                                    text "This mixture is safe when touched with just dry skin, and is sometimes carried by inexperienced travelers as a medium-ranged weapon. It can be transported in a pouch, taken with a bare hand and quickly thrown forward, ideally while looking in another direction. A small cloud of dust either makes the enemy turn back, or lands on their face."
                                    text "Once it touches one’s eyes or tongue, it causes a painful burn. A pinch of it will blind a creature for a few minutes, while the larger doses take away one’s eyesight indefinitely."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "boartusks":
                                    text "Boars are the most common medium-sized wild game living in the North, appearing everywhere where there’s enough undergrowth to provide them with shelter, which means almost every part of the realm aside from the wetlands, lakes, and mountains. They seem to enjoy a diet that’s even more varied than that of humans - roots, tubers, leaves, bark, nuts, eggs, worms, small animals, carrion... No matter how much they are prayed upon by wolves or dragonlings, they always manage to restore their population."
                                    text "While boars don’t hunt on creatures larger than hares and prefer to stay away from humans, from time to time they feel threatened enough to charge at their opponents, even when unprovoked. If it happens, they are rarely satisfied by simply knocking down their victims, feeling at ease only after their enemy lets out the last breath. Because of this, some villages see boar hunting as a display of strength and bravery, even using it as a rite of passage for young fighters."
                                    text "Usually, tusks are preserved in their entirety as a stand-alone trinket or a piece of jewelry, though some people use them as a base for sculptures or turn them into decorative layers that cover wooden surfaces."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "bonebuckle":
                                    text "Belts not only keep pants and skirts from falling down, but also maintain shapes of all sorts of clothes, from crude armors and tunics to the fanciest dresses and robes. In experienced hands, they showcase the more desired physical features and hide the imperfections. Because of this, buckles are among the most common pieces of garments, not only in The Ten Cities, and are used as a foundation for an artistic expression, or to mark their owner’s status."
                                    text "The buckles are made of metal, wood, or bones. Even the simplest of them are elegantly modest, avoiding the unwanted attention. Moderate ones are covered with simple carvings, sometimes quite abstract ones, and come in unusual shapes, while the most expensive options are quite sizable and not especially practical, but resemble specific creatures, objects, such as an hourglass or a tree. The especially complex portray small scenes - maybe a duel, or the bread-baking process in a few phases. If possible, such artisanship is accompanied by complementary brooches."
                                    text "This specific buckle quite accurately portrays a jumping boar, and has an oversized tusk made of silver."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "boneearring":
                                    text "Tiny bones are not as popular among jewelry makers as claws and tusks, and they are often mocked for resembling the remains of chickens, rats, and squirrels. This specific bone is almost completely round, like an unusual rib of a little creature."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "bonehook":
                                    text "Grappling hooks were introduced to The Ten Cities as a curiosity brought by the corsairs during their pillages. The Southern Tribes use these tools during warfare as they’re helpful for breaching walls and other defensive structures. The corsairs have repurposed them, using them to catch the riggings of opposing ships to then board them."
                                    text "Such hooks never became popular across the provinces of The Dragonwoods, finding no use in the defense-oriented army. They were, however, put to good use by adventurers, who use them to climb trees and rock faces, scavenge through the abandoned settlements, or get inside a protected building during a break-in."
                                    text "This specific hook is an example of the creativity that comes into play when there’s not enough iron to make high-quality tools. Its three bones are naturally curved, not unlike ribs, and tied together with a couple of steel wires. While you wouldn’t use it to take down a ship, its low price compensates the poor quality."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "bonering":
                                    text "While similar to a dragon ring, it’s of an uneven shape, and lacks the distinctive grooves that are present in coins, so it most likely belonged to a furry beast. It was meant to be worn on a large finger."
                                    text "The decorative carvings show a fish on one side and scales on the other, though they’re rather simple."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "boxfromdolmen":
                                    text "A light, wooden box. You shake it for a bit, trying to guess what’s inside, but you hear little to nothing. The cords are tightly tied together and you can’t look inside without cutting them."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        textbutton _("Open it") action [SetVariable("item_boxfromdolmen", 0), SetVariable("item_potiondolmen", 1), SetVariable("item_detailedmenu", "boxfromdolmenopened")]
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "boxfromdolmenopened":
                                    text "The box turns out to be filled with rags, covering a fragile, earthen bottle. It’s small and sealed with a tall wax seal, inside of which you see a thin stick. It should be easy to instantly open it."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Take a look at the bottle") action [SetVariable("item_detailedmenu", "potiondolmen")]
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "brokenknife":
                                    text "This knife was surely not cheap, but all that remains of it is an old handle made of the polished bone of a large animal. The engravings on its surface are old, but you recognize the shapes of creepers and flowers. It’s worth a coin or two, and maybe has sentimental value to someone."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "bugrepellent":
                                    text "A combination of about a dozen leaves and flowers found among the local forests and hills. It’s green and dense, and smells like pleasant seasoning for baked fish. Safe for human skin, but inedible."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "chicken":
                                    text "“The best light roast in the North,” claimed the cook, and the meat surely smells delicious. A coin for such a treat is a bit expensive, but covers the work of an experienced master and a set of a mysterious blend of spices."
                                    text "Chickens, similar to boars, don’t require much care or space and are not picky eaters. They usually know better than to leave village walls and are allowed to roam through the gardens and alleys, looking for worms, seeds, fruits, and leftovers. They are valued for their nutritious eggs, and once they turn old, they are butchered not just for their meat, but also the edible offals, and the feet and bones that add flavor to stews and soups. Their down feathers, or even the regular ones, can be used as a lower-quality padding."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        if pc_food < 4:
                                            textbutton _("Eat a chicken to increase your {color=#f6d6bd}nourishment{/color} by 3") action [SetVariable("item_detailedmenu", "chickeneating"), SetVariable("item_chicken", item_chicken-1), SetVariable("pc_food", limit_pc_food(pc_food+3))]
                                        else:
                                            text "{color=#6a6a6a}You don’t need to eat right now{/color}"
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "chickeneating":
                                    text "Even when cold, it’s delicious. Juicy and fresh, with enough herbs to give it an unusual flavor, but not enough that would overwhelm your senses. You wish you had an opportunity to combine it with other foods, but it’s already much fancier than a regular chicken pie that you would normally buy in Hovlavan. Once you’re done, you wash your mouth and fingers with water stored in your bundles."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "cidercask":
                                    text "It’s easy to produce the basic cider, assuming one owns a special mill that squeezes out the juices of dozens of chopped apples or pears picked by foragers at the end of summer. The juice can be drunk right away or mixed with yeast, resulting in a hard drink after just a few days."
                                    text "Tasty both chilled and heated, in many places across The Dragonwoods ciders are a part of the pre-winter festivities. Some villages specialize in raising orchards where they favor the trees that grow the largest fruits."
                                    text "Ciders, like ales and beers, don’t last long. They spoil after a few dozen days, introducing more and more unwanted flavors, getting unpleasantly bitter or unbearably sour, and often starting to smell like rotten eggs. This process accelerates rapidly from the moment the barrel is opened, sometimes ruining the entire contents in just two days."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "peltnorthberries":
                                    text "The innkeeper has asked you to forage some berries that grow near Pelt of the North. Their red color is unsettling."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if iason_food_berries == 3:
                                        if can_items:
                                            if pc_food < 4:
                                                textbutton _("Eat the berries to increase your {color=#f6d6bd}nourishment{/color} by 1") action [SetVariable("item_peltnorthberries", 0), SetVariable("pc_food", limit_pc_food(pc_food+1)), SetVariable("item_detailedmenu", "peltnorthberrieseaten")]
                                            else:
                                                text "{color=#6a6a6a}You don’t need to eat right now{/color}"
                                        else:
                                            text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    else:
                                        text "{color=#6a6a6a}You were asked to take them to Pelt of the North{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "peltnorthberrieseaten":
                                    text "They are a bit sour, but pleasantly sweet."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "peltnorthberrytools":
                                    text "A set of tools given to you by the innkeeper from Pelt of the North. A hook, a pair of gloves, and a bucket."
                                    text "The hook has caught your eye. Its head is made from a dark animal claw. People in the countryside often use bones, claws, tusks, or even stones to make tools and weapons, but this one is quite large."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        textbutton _("Detach the claw") action [SetVariable("item_peltnorthberrytools", 0), SetVariable("item_peltnorthberryclaw", 1), SetVariable("item_detailedmenu", "peltnorthberryclaw")]
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "peltnorthberrytools02":
                                    text "A hook given to you by the innkeeper from Pelt of the North. Its head is made from a dark animal claw. People in the countryside often use bones, claws, tusks, or even stones to make tools and weapons, but this one is quite large."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        textbutton _("Detach the claw") action [SetVariable("item_peltnorthberrytools", 0), SetVariable("item_peltnorthberryclaw", 1), SetVariable("item_detailedmenu", "peltnorthberryclaw")]
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "peltnorthberryclaw":
                                    text "Claws are sculpted into brooches, amulets, pendants, styluses, or toys, while a whole set of them may be turned into a large necklace. In the countryside, larger claws are often used for constructing tools or weapons, though they are not too flexible."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        if iason_food_berries == 2:
                                            textbutton _("Make a hook") action [SetVariable("item_peltnorthberrytools", 1), SetVariable("item_peltnorthberryclaw", 0), SetVariable("item_detailedmenu", "peltnorthberrytools02")]
                                        else:
                                            textbutton _("Make a hook") action [SetVariable("item_peltnorthberrytools", 1), SetVariable("item_peltnorthberryclaw", 0), SetVariable("item_detailedmenu", "peltnorthberrytools")]
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "coins":
                                    text "When it comes to trade, there's barely any connection between Hovlavan’s marketplaces and the inns of the countryside. While city officials keep track of the value of different goods and oversee the legitimacy of used coins, the villages prefer to barter, or exchange their resources for work and other favors."
                                    text "A single coin is worth quite a lot among merchants - it allows you to stay and eat in a shoddy city tavern for about five days. For ten coins you’d buy a decent bow, for twenty - a sword, and for a hundred a squad of mercenaries will be willing to face a family of trolls."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "cookedfish":
                                    text "A fresh, simple meal. In a perfect world, you’d eat it with a decent pinch of salt and a thick herbal sauce based on yogurt, but it already smells nice."
                                    text "The annoying part will be avoiding all the fishbones."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        if item_cookedfish:
                                            if pc_food < 4:
                                                textbutton _("Eat a fish to increase your {color=#f6d6bd}nourishment{/color} by 1") action [SetVariable("item_cookedfish", item_cookedfish-1), SetVariable("pc_food", limit_pc_food(pc_food+1))]
                                            else:
                                                text "{color=#6a6a6a}You don’t need to eat right now{/color}"
                                        else:
                                            text "{color=#6a6a6a}You already ate your last fish{/color}"
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "crossbow":
                                    text "It’s difficult to buy a crossbow outside of a city craft guild. They require complex mechanisms made by combined efforts of specialized artisans, but their expensive parts may keep the weapon drawn for many hours. They are easy to aim and shoot, and their quarrels hit much harder than the regular bow arrows. While loading takes a fair bit of time, in some cases even half a minute, the newer models don’t require much effort, nor strength, thanks to the introduction of advanced winches. Such a weapon can be a powerful tool even in the hands of an untrained monk."
                                    text "Since crossbows are much more complex than bows, they are often altered by enchanters, who focus their attention on a specific, small part. The most popular enhancements include faster reload speed, extended draw weight, increased durability, and lighter weight."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "crossbowquarrels":
                                    text "Known also as bolts, they are shorter, even much shorter, than bow arrows. Their heads are in the shape of a square, and making them requires advanced tools used to melt and shape iron or steel. They use hard wood and a small amount of fletching, but are overall a bit expensive, especially since they are produced by experienced artisans."
                                    text "Quarrels are most effective when it comes to piercing through thicker surfaces, including animal scutes, thick furs, and scales. While they don’t leave spectacular wounds, they manage to get to the vital organs, injuring them beyond the capabilities of the natural healing."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "dragonhorn":
                                    text "The purpose of a horn depends on its loudness, as well as its origins. Brass horns, as representatives of technological capabilities of humans, are ceremonially used by The United Church, while the status assigned to an animal horn is usually based on the threat presented by its original owner. When it comes to the more practical side of things, the quieter, easier to use horns are introduced during theatrical or musical performances, while the louder ones are blown to send a warning to a distant group. In cities, for example, different horns are attached to unique signals, related to events such as fire, flying beasts, plagues, or floods."
                                    text "The horn you possess doesn’t look too impressive and most likely didn’t belong to an actual dragon, but its terrifying sounds would worry even the largest of beasts, at least until they realize it’s not followed by shaking ground and breaking trees. It looks like one of the instruments that, in the not so distant past, were used to exchange messages between neighboring villages."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "empresscarp":
                                    if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "unknown" or pc_religion == "none":
                                        text "Wright’s Tablets tell a story of Dafna, a fighter and an ancestor of the first emperor. One day, as she was returning from her hunting trip, she heard a voice coming from under a bridge. It belonged to a gorgeous fish, whose scales were shining in colors of iron, copper, silver, and gold."
                                        text "The fish introduced herself as the guardian of the river and promised Dafna all the ore of the forest, but only if she was to fulfill three tasks - widen the riverbed, destroy the bridge, and hunt down a dangerous saurian consumed by its hunger and greed. These tasks took not only time, but also strength and tenacity. When Dafna returned for her reward, she was exhausted."
                                        text "The “guardian” had tricked her - nature had been so reshaped by these tasks that creatures of all kinds united their strength to kill not only Dafna, but also the people of her village."
                                        text "The Wright decided to punish the fish for its betrayal. The brilliant colors of its offspring got dulled to red, orange, gold, and white. The cityfolk know them as “empress carp,” since many believe that Dafna would have become the first empress of the realm."
                                        if pc_religion == "theunitedchurch":
                                            text "According to the priests of The United Church, this tale is a warning that no matter how much you befriend the creatures of this land, they will always be ready to hurt you."
                                        if pc_religion == "ordersoftruth":
                                            text "According to the monks of the Orders of Truth, this tale is a caution that there are no shortcuts in achieving one’s goals. Instead of depending on gifts of an unknown nature, one should focus on building their own skills and wisdom."
                                        if pc_religion == "fellowship":
                                            text "Many fellowships interpret this tale as a caution of vanity hidden in beauty. Wright’s followers must free themselves from the tricks and illusions that hold back their piety."
                                    else:
                                        text "In many tribes that practice druidic rituals, empress carp, known also as “water chieftains,” are seen as nature’s selfless gift to humankind. Eating them is taboo, as they are praised for their role in cleaning springs and lakes from leeches and mosquitoes. They are used as an example that humans are able to coexist with various creatures, not only those that were brought to The Dragonwoods from The Southern Tribes, like mouflons and horses."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        if item_empresscarp_timelimit+2 < day:
                                            textbutton _("Check on the fish") action [SetVariable("item_empresscarp", 0), SetVariable("item_detailedmenu", "empresscarpcheck")]
                                        else:
                                            textbutton _("Check on the fish") action [SetVariable("item_detailedmenu", "empresscarpcheck")]
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "empresscarpcheck":
                                    if item_empresscarp_timelimit+2 < day:
                                        text "You lift the lid, but there’s no more fish inside, just an empty shell floating bottom-up. You empty the bucket onto the grass and leave it behind."
                                    else:
                                        text "It’s swimming in circles."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "spices":
                                    text "Spices are more intense in smell and flavor than dried herbs, as they are made from the most aromatic bits of plants. Some of them are produced by the villages of The Dragonwoods, while others are delivered by the merchants of The Southern Tribes, or collected by adventurers during their journeys into the deep woods. In general, the more exotic and rare they are, the more expensive they get, even if they aren’t necessarily all that useful in the kitchen - they find some use on alchemy tables, or in herbalist balms."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "spiritrock":
                                    text "This small rock was filled with pneuma by an enchantress. It looks ordinary, like a pebble from a creek."
                                    text "Spellcasters look for ways to restore their pneuma, especially in time of need, though an abuse of such tools by an unsuited soul may be extremely dangerous."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items or can_potions:
                                        if pc_class == "mage":
                                            if mana < 5 and item_detailedmenu == "spiritrock":
                                                textbutton _("Drain its pneuma") action [SetVariable("item_spiritrock", item_spiritrock-1), SetVariable("mana", 5), SetVariable("item_detailedmenu", "spiritrockeaten")]
                                            else:
                                                text "{color=#6a6a6a}You don’t need to use it right now{/color}"
                                        else:
                                            text "{color=#6a6a6a}It should be used only by spellcasters{/color}"
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "spiritrockeaten":
                                    if can_potions and not can_items:
                                        text "You put the smooth rock in your mouth and use your tongue to press it to your palate. You breathe with your nose, once, twice, and a sudden warmth spills into your jaw, fills your head, spreads to your shoulders, and overtakes the rest of your shell, to the point where you want to take off your clothes. Before you seriously consider it, the effect is gone."
                                    else:
                                        text "The rock is cold and pleasantly smooth. You make sure it’s clean, wondering if it’s possible to somehow “wash away” the pneuma stored in it."
                                        text "You put it in your mouth and use your tongue to press it to your palate. You breathe with your nose, once, twice, and a sudden warmth spills into your jaw, fills your head, spreads to your shoulders, and overtakes the rest of your shell, to the point where you want to take off your clothes. Before you seriously consider it, the effect is gone."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "sharpeningpotion":
                                    text "A magic powder that “sharpens” one’s senses. Even its ingredients are infamous among the herbalists of The Dragonwoods for they tend to lead their users to a weakening addiction."
                                    text "You can consume some of it to enhance your combat abilities for the rest of the day, but you’ll pay the cost during nighttime. Better to go to sleep with a full stomach."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items or can_potions:
                                        if item_sharpeningpotion_used != day:
                                            textbutton _("Rub it in your gums") action [SetVariable("item_sharpeningpotion", item_sharpeningpotion-1), SetVariable("item_sharpeningpotion_used", day), SetVariable("pc_throwingxp", pc_throwingxp+20), SetVariable("pc_battlecounter", pc_battlecounter+20), SetVariable("item_detailedmenu", "sharpeningpotionconsume")]
                                        else:
                                            text "{color=#6a6a6a}You’re already under its effect{/color}"
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "sharpeningpotionconsume":
                                    text "The taste of ash grows intense, while the world slows down. You blink a few times, getting used to the sharp lights and colors. Each gesture of yours is precise and conscious, your heavy breathing is full of excitement."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "eudociaflower":
                                    if pc_class == "scholar" or item_snakebait_truth:
                                        text "It’s infamous for its alleged power to lure serpents and saurians, though some scholars question this story. When consumed in moderation, it makes a shell more responsive to stimuli and makes periods of sleeplessness easier to bear."
                                        text "Juice from a single leaf is enough to induce hallucinations or an addicting sense of dreamlike euphoria. Using a large dose at once, or small doses too often, leads to frailty or death."
                                    else:
                                        text "It’s infamous for its alleged power to lure serpents and saurians, but is sometimes picked in forests and used in alchemical potions that enhance one’s combat potential."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "fancyclothes":
                                    if item_fancyclothes == 1:
                                        text "To protect the fine fabrics, you only put on these clothes when you’re close to a settlement. The dim, elegant colors won’t draw too much attention in a tavern, or make you look out of place during ceremonial gatherings. The comfortable tunic won’t encumber you during longer walks, and the entire set makes you look more like a rich city official than a traveler."
                                    if item_fancyclothes == 2:
                                        text "To protect the fine fabrics, you only put on these clothes when you’re close to a settlement. The dim, elegant colors won’t draw too much attention in a tavern, or make you look out of place during ceremonial gatherings. The entire set makes you look more like a merchant than a traveler, especially since the heavy robe gets tiresome after a longer walk."
                                    if item_fancyclothes == 3:
                                        text "To protect the fine fabrics, you only put on these clothes when you’re close to a settlement. The dim, elegant colors won’t draw too much attention in a tavern, or make you look out of place during ceremonial gatherings. The entire set makes you look like a socialite or diplomat rather than a traveler, especially since the light dress is very thin, yet limits your movements."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "oceannecklace":
                                    text "Its leather strip is covered in mold. The silver fish scales, about an inch long each, used to belong to a huge sea monster. Seeing how hard they are, you wonder if thousands of them can be turned into armor."
                                    text "The long, cream-colored seashell was meant to be the lowest part of the worn necklace, allowing the scales to form a somewhat-symmetrical ring on its sides."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "fishtrap":
                                    if northernroad_fishtrap or wanderer_fishtrap or fallentree_fishtrap or ghoulcave_fishtrap or ruinedvillage_fishtrap:
                                        text "You already set up:"
                                    if ghoulcave_fishtrap:
                                        text "* A creek trap at the eastern cave. Sealed on day [ghoulcave_fishtrap_working], last checked on day [ghoulcave_fishtrap_daychecked]."
                                    if wanderer_fishtrap:
                                        text "* A creek trap at the statue on the eastern road. Sealed on day [wanderer_fishtrap_working], last checked on day [wanderer_fishtrap_daychecked]."
                                    if northernroad_fishtrap:
                                        text "* A lake trap at the northern road. Sealed on day [northernroad_fishtrap_working], last checked on day [northernroad_fishtrap_daychecked]."
                                    if ruinedvillage_fishtrap:
                                        text "* A river trap at the ruined village. Sealed on day [ruinedvillage_fishtrap_working], last checked on day [ruinedvillage_fishtrap_daychecked]."
                                    if fallentree_fishtrap:
                                        text "* A river trap at the south-eastern turn. Sealed on day [fallentree_fishtrap_working], last checked on day [fallentree_fishtrap_daychecked]."
                                    text "The basket-like tool meant to be kept in a shallow freshwater. Fish enter it from time to time, seeking shelter or getting lured by a set bait. The basket’s lid has a single funnel-shaped hole, which resizes when a creature tries to squeeze through it, but then returns to its original position, prisoning the prey."
                                    text "In an ideal situation, fish catch themselves on their own, while the hunter takes care of other chores. Still, building a fine trap may take even half a day, depending on size, shape, and used materials, and they are anything but permanent. They tend to rot, and are often destroyed or robbed by the local wildlife, tempted by the easy reward. Because of this, they are usually seen as a source of additional luxury, rather than the main source of food."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "rations":
                                    text "The fresh snacks spoil fast outside of a cellar, while long-lasting foods are either expensive, like honey or dried meat, or require cooking before consumption, like beans or grains."
                                    text "Most travelers spend their nights in taverns, huts, and villages, where they can trade for cheap, warm meals or even eat leftovers for free. As a result, food rations are eaten only when necessary."
                                    if not pc_food:
                                        text "{color=#f6d6bd}Nourishment{/color}: {color=#f6d6bd}0{/color}/4. You won’t restore health while sleeping. Starvation weakens you in the physical struggles."
                                    if pc_food == 1:
                                        text "{color=#f6d6bd}Nourishment{/color}: {color=#f6d6bd}1{/color}/4. You won’t restore health while sleeping."
                                    if pc_food == 2:
                                        text "{color=#f6d6bd}Nourishment{/color}: {color=#f6d6bd}2{/color}/4. You experience no penalties, nor bonuses."
                                    if pc_food == 3:
                                        text "{color=#f6d6bd}Nourishment{/color}: {color=#f6d6bd}3{/color}/4. It’s easier for you to overcome physical struggles."
                                    if pc_food == 4:
                                        text "{color=#f6d6bd}Nourishment{/color}: {color=#f6d6bd}4{/color}/4. It’s much easier for you to overcome physical struggles."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if item_rations:
                                        if can_items:
                                            if pc_food < 4:
                                                textbutton _("Eat a food ration to increase your {color=#f6d6bd}nourishment{/color} by 2") action [SetVariable("item_rations", item_rations-1), SetVariable("pc_food", limit_pc_food(pc_food+2))]
                                            else:
                                                text "{color=#6a6a6a}You don’t need to eat right now{/color}"
                                        else:
                                            text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    else:
                                        text "{color=#6a6a6a}You don’t have any rations left{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "furlesswolftrophy":
                                    text "The disturbing appearance of this wolf-like creature is not going to turn it into an appealing wall decoration. Processing it will involve many hours of unpleasant, pungent work spread across days of waiting, not to mention tools, a bunch of salt, and a place where it can dry without being disturbed."
                                    text "It can still be turned into a decent trophy, but needs to be sold soon, before it begins to decompose."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "furs":
                                    text "You currently possess:"
                                    if item_elkfur:
                                        text "* a high-class elk fur bought in Pelt of the North;"
                                    if item_harepelt:
                                        text "* a high-class hare pelt you got in Creeks;"
                                    if item_sealskin:
                                        text "* a sealskin you bought from Aegidia."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    text "Thicker skins of livestock can be turned into durable clothing, boots, leather straps, belts, quivers, bags, water skins... Cheaper ones are used as a protective layer for wooden objects, such as chests, codex covers, or tool handles. Thin mouflon skins and ibexeskins are especially valued among farmers, who turn them into expensive parchments."
                                    text "Furs, on the other hand, are often kept as a single pelt. They’re used as blankets or piled on one another to form a sleeping spot. Rich cityfolk use them to trim necklines, hats, and cuffs, but even impoverished families display them on walls or place them on floors, like a carpet. In many provinces, furs are a popular wedding gift and each type has its own symbolic meaning."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "gambesonrepairset":
                                    if armor_fixingxp >= 18:
                                        $ sheet_description8 = "expert"
                                    elif armor_fixingxp >= 15:
                                        $ sheet_description8 = "promisingly high"
                                    elif armor_fixingxp >= 12:
                                        $ sheet_description8 = "high"
                                    elif armor_fixingxp >= 8:
                                        $ sheet_description8 = "advanced"
                                    elif armor_fixingxp >= 6:
                                        $ sheet_description8 = "average"
                                    elif armor_fixingxp >= 3:
                                        $ sheet_description8 = "small"
                                    elif armor_fixingxp >= 1:
                                        $ sheet_description8 = "slight"
                                    elif armor_fixingxp <= 0:
                                        $ sheet_description8 = "none"
                                    if not armor:
                                        text "The tools and needles made of iron will help you brute-force your way through the threads of your quilted jacket. Before resewing them, you’ll repad the holes with clothes and hair. You’ll also replace the torn leather laces in the front."
                                    else:
                                        text "The tools and needles made of iron will help you brute-force your way through the threads of your quilted jacket. Before resewing them, you’ll repad the holes with clothes and hair."
                                    text "The more you practice, the less time it takes for you to complete the repairs. Current experience: [sheet_description8]"
                                    if not armor:
                                        text "{color=#f6d6bd}Armor{/color}: {color=#f6d6bd}0{/color}/4. In its current state, it offers you no protection."
                                    if armor == 1:
                                        text "{color=#f6d6bd}Armor{/color}: {color=#f6d6bd}1{/color}/4. It’s too worn out to make a real difference in combat."
                                    if armor == 2:
                                        text "{color=#f6d6bd}Armor{/color}: {color=#f6d6bd}2{/color}/4. It will stop the lighter attacks, but not for long."
                                    if armor == 3:
                                        text "{color=#f6d6bd}Armor{/color}: {color=#f6d6bd}3{/color}/4. It will stop even a life-threatening strike."
                                    if armor == 4:
                                        text "{color=#f6d6bd}Armor{/color}: {color=#f6d6bd}4{/color}/4. It suits you well and doesn’t encumber you in combat."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if (quarters < world_daylength+1 and armor_fixingxp < 9) or (quarters < world_daylength+2 and armor_fixingxp >= 9) or (quarters < world_daylength+4 and armor_fixingxp >= 15):
                                        if (armor_can4 and armor < 4) or (not armor_can4 and armor < 3):
                                            if can_items:
                                                if armor_fixingxp < 3:
                                                    textbutton _("Spend 2h to increase your {color=#f6d6bd}armor{/color} by 1") action [SetVariable("quarters", quarters+8), SetVariable("armor", limit_armor(armor+1)), SetVariable("armor_fixingxp", armor_fixingxp+2)]
                                                elif armor_fixingxp >= 3 and armor_fixingxp < 6:
                                                    textbutton _("Spend 1h 45min to increase your {color=#f6d6bd}armor{/color} by 1") action [SetVariable("quarters", quarters+7), SetVariable("armor", limit_armor(armor+1)), SetVariable("armor_fixingxp", armor_fixingxp+2)]
                                                elif armor_fixingxp >= 6 and armor_fixingxp < 9:
                                                    textbutton _("Spend 1h 30min to increase your {color=#f6d6bd}armor{/color} by 1") action [SetVariable("quarters", quarters+6), SetVariable("armor", limit_armor(armor+1)), SetVariable("armor_fixingxp", armor_fixingxp+2)]
                                                elif armor_fixingxp >= 9 and armor_fixingxp < 12:
                                                    textbutton _("Spend 1h 15min to increase your {color=#f6d6bd}armor{/color} by 1") action [SetVariable("quarters", quarters+5), SetVariable("armor", limit_armor(armor+1)), SetVariable("armor_fixingxp", armor_fixingxp+2)]
                                                elif (armor_fixingxp >= 12 and armor_fixingxp < 15):
                                                    textbutton _("Spend 1 hour to increase your {color=#f6d6bd}armor{/color} by 1") action [SetVariable("quarters", quarters+4), SetVariable("armor", limit_armor(armor+1)), SetVariable("armor_fixingxp", armor_fixingxp+2)]
                                                elif armor_fixingxp >= 15:
                                                    textbutton _("Spend 45min hour to increase your {color=#f6d6bd}armor{/color} by 1") action [SetVariable("quarters", quarters+3), SetVariable("armor", limit_armor(armor+1)), SetVariable("armor_fixingxp", armor_fixingxp+2)]
                                                elif armor_fixingxp >= 18:
                                                    textbutton _("Spend 30min hour to increase your {color=#f6d6bd}armor{/color} by 1") action [SetVariable("quarters", quarters+2), SetVariable("armor", limit_armor(armor+1)), SetVariable("armor_fixingxp", armor_fixingxp+2)]
                                            else:
                                                text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                        else:
                                            text "{color=#6a6a6a}You gambeson is already as good as it can get{/color}"
                                    else:
                                        text "{color=#6a6a6a}It’s too dark and you’re too sleepy to work on your gambeson{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "gambeson01" or item_detailedmenu == "gambeson02":
                                    text "Padded jackets are an essential piece of any armor set. They protect the wearer’s chest, abdomen, arms, and thighs. The lighter jackets, called {i}aketons{/i}, are worn under heavier sets made of alloys or chitin, while the thicker ones, known as {i}gambesons{/i}, are worn alone. They are relatively easy to make and while not all travelers can afford them or wear them for hours without getting tired, they are commonly used by guides, mercenaries, and soldiers."
                                    if not item_gambeson02:
                                        text "Your armor is not in best shape and could use some additional work."
                                    else:
                                        text "Thanks to recent addition of spider silk your gambeson has no weak spots and feels easier to your hips and shoulder."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "ghoulblood":
                                    text "The scent that filled your nostrils while you were filling up this phial taught you to never open it again."
                                    text "Blood of rare monsters is useful for alchemists and ritualists, though many people believe that the blood of corpse eaters is cursed, and brings bad luck on those who use it."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "goblinrepellent":
                                    text "According to the scavenger who gave you this jar, you can use its content to mark an area with a terrifying smell, which should work especially well if you want to keep away any meddlesome goblins or pebblers."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "goblinspear":
                                    text "Goblins are one of the very few creatures that use tools and weapons commonly, though they don’t seem to be smart enough to make something more complex than a sharp rock or a pointed stick. If they have no other option, a long branch will do. Some of the objects they carry around are actually too heavy for the goblins to efficiently use them, while others are counterintuitive. It’s not rare to find a goblin using a sword or a crossbow as if they were a club."
                                    text "The older, stronger packs try to gather as many dangerous objects as they can find. They are notorious for scavenging for the abandoned blades and clothes, and if they’re brave enough, they even attack farmers or hunters, adding to their rewards fresh human meat."
                                    if encounter_fallentree_goblins_bloodonspear:
                                        text "The weapon you took is stained by goblin blood. It has a light-blue scrap of fabric tied to it, just beneath the pointed tip. You wonder why a monster would care about decorating their tool."
                                    else:
                                        text "The weapon you took has a light-blue scrap of fabric tied to it, just beneath the pointed tip. You wonder why a monster would care about decorating their tool."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "bronzerod":
                                    text "Each rod is as long as your arm. They’re clean, glossy, and made of high quality bronze. You’re meant to place them in high points all across the peninsula, which will allow golems to reach new parts of the land and collect resources."
                                    text "You have [item_bronzerod] left."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "golemglove":
                                    text "The glove is made of thin rock shards and covers your hand and forearm only on the outer side. As you lift it, it’s about as heavy as your axe, but once it clings to your skin, and clothes, you hardly notice its presence."
                                    text "It maintains its general shape, no matter how long you twist it or press any of the shards together, though you were told that pulling the rocks too fiercely will break the holding spell."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "griffonegg":
                                    text "The Northerners attach a great value to young beasts that can be tamed in separation, without the influence of a parent that would teach its offspring independence and combat. Stealing the foals of pterippi and the eggs of wyverns and noble griffons is an unusual trade, involving weeks of travels through the hills and mountains, which more likely end up in one’s demise than fortune."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "horse01":
                                    text "Horses are not a common sight in The Dragonwoods. They were brought here from the conquests in the South and can’t survive in the forests by themselves. They can run for a long time, but not fast enough to escape all of the local monsters."
                                    text "Usually, riders maintain a steady, human-like speed, saving the strength of their mount for the unavoidable dangers that require galloping."
                                    if item_horse_coat:
                                        text "[item_horse_coat]"
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "howlersdelltoken":
                                    text "A parchment scroll made of lambskin. One of its sides is covered with an awkwardly drawn tree which bears no leaves and fruits, similar to the one you’ve seen in the village square. To make this picture, someone has used a couple of shades of blue and purple ink."
                                    if pc_class == "scholar":
                                        text "The other side is covered with red letters, which read as follows: “No friend of Howler’s Dell walks hungry. May [pcname] feast with us to the end of the sky and trees."
                                    else:
                                        text "The other side is covered with red letters, but you can’t read them. They look pretty, though."
                                    text "According to the trader Akakios, this “letter” entitles you to “free bed and victuals,” as well as free tailor services."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "ironingot":
                                    text "Opening and maintaining mines without provoking the wrath of the herds takes a lot of effort and is time-consuming. Most villages can’t produce enough food and fuel for all the diggers, soldiers, and carriers that such a settlement requires. Because of that, northern metallurgy is far from advanced and the cityfolk have to transport most of the ore from The Growing Mountains, which in and of itself is a risky procedure."
                                    text "In the past, items made of metals, such as weapons, cauldrons, and pieces of art were stolen and moved to The Ten Cities from The Southern Tribes by corsairs. Since the end of the war, which put an end to the raids, iron has become even more difficult to obtain."
                                    text "Crude iron contains a significant amount of coal and dross, and is too brittle to be of much use. Once remelted, it will be purified and strengthened, most likely turned into steel."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "ironscraps":
                                    text "Opening and maintaining mines without provoking the wrath of the herds takes a lot of effort and is time-consuming. Most villages can’t produce enough food and fuel for all the diggers, soldiers, and carriers that such a settlement requires. Because of that, northern metallurgy is far from advanced and the cityfolk have to transport most of the ore from The Growing Mountains, which in and of itself is a risky procedure."
                                    text "In the past, items made of metals, such as weapons, cauldrons, and pieces of art were stolen and moved to The Ten Cities from The Southern Tribes by corsairs. Since the end of the war, which put an end to the raids, iron has become even more difficult to obtain."
                                    text "The scraps you own could be easily sold anywhere, though they will be especially useful in areas with access to a smithy."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "keysidle":
                                    text "You currently possess:"
                                    if item_trapdoorkeydolmen:
                                        text "A key to a secret passage in the dolmen. You can find it in the south-east of the peninsula."
                                    if item_oldtunnelkey:
                                        text "A huge, bronze key from the old tunnel in the north."
                                    if item_oldtunnesmallkey:
                                        text "A small, iron key from old tunnel in the north."
                                    if item_piershedkey:
                                        text "A small, brass key to the shed placed on the northern beach."
                                    if item_watchtowerkey and item_asterionkey:
                                        text "Two keys to the abandoned watchtower. One of them was found in Asterion’s pouch."
                                    elif item_watchtowerkey:
                                        text "An iron key to the abandoned watchtower."
                                    elif item_asterionkey:
                                        text "An iron key that you found in Asterion’s pouch."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "lantern":
                                    text "Lanterns protect candles from winds and drafts. They can be held or hung on a hook by a handle, or placed on any flat surface. The proper, iron lanterns also avoid tragic accidents by containing the fire inside."
                                    text "In the decades preceding The Southern Invasion, the city artisans were putting a lot of effort into perfecting the various lantern designs. They were testing new materials, shapes, and handles; comparing glass windows with those made of perforated metal and horn; replacing candles with wicks in oil; or using the layers of windows to regulate the offered light."
                                    text "Ever since the supplies of iron and copper have thinned out, the more primitive types of lantern regained their lost popularity, even though some of them are quite a fire hazard. The lantern you own is made of wood and parchment, which makes it a terrible tool for a farmer, but should work just fine for a sneaky adventurer."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "linen":
                                    text "There are many reasons to give up on linen. The cultivation of flax and the processing of fibers takes a tremendous effort, which could instead be spent on what’s essential for survival. The plants cover valuable scraps of land, and provide no nourishment other than in the oil. They require knowledge for multiple steps of processing, and a lot of time to pass from sowing to receiving an actual piece of cloth. Also, the rotting or badly cultivated plants smell terrible. Less wealthy settlements use hemp or leather to produce clothes and, if they’re based on animal husbandry, wool and mohair."
                                    text "Nevertheless, it remains one of the most desirable types of fabric in The Ten Cities. With some care, linen clothes can last for years, then be used as rags or turned into sacks, or into stuffing for pillows, mattresses, jackets, dolls, dummies... Such clothing is light and pleasant to touch, cleans easily, and dries quickly. The regular, grayish color of linen is not too appealing, but the sheets easily react to dyeing. New colors also open the way for contrast and dynamic designs - colorful threads can turn even a simple tunic into a distinctive, expressive item."
                                    text "The price of masterfully made linen clothes can reach unexplainable levels, but they all start with a decent material, such as this one. The potential of these clean sheets still needs to be awakened, but because of it, you should be able to sell it almost anywhere."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "lostmanblanket":
                                    text "A torn and frayed rawhide, a simple material made of animal skin, but without the tanning process that would turn it into leather. It’s not rotten yet, but it provided a couple of howlers with a lot of joy - their playtime made it so damaged it’s pretty much worthless."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "mageamulets":
                                    text "A satchel that includes:"
                                    text "* the leather pendant, with a single pearl covered with cryptic engravings. You use it for simple tricks involving light;"
                                    text "* the clean linen bandage soaked in old herbal balms. You use it to heal fresh, minor wounds;"
                                    text "* a couple of wooden spheres. They get warmer when put nearby an unusual amount of pneuma;"
                                    text "* the wand made of a willow branch, partially filled with quicksilver. It helps you channel your magical blast;"
                                    text "* your lucky button."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "magicalsapling":
                                    text "According to Eudocia, this herb will react whenever it touches magically altered soil. In about half an hour, it should either burst into bloom, or wither."
                                    text "Enhancing a field through spells is a valuable skill, one that’s practiced through complex rituals, tremendous magical power, or huge amounts of time and hard work from less-skilled sorcerers. Cursing an area is just as difficult, but in most areas it’s considered to be highly immoral and harmful, comparable with setting the forest on fire, since it hurts not just a specific community, but also any group of people that will come to the same land in the future."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "magicchisel":
                                    text "A simple tool used for cutting or splitting hard surfaces, especially essential for people who carve in wood, rocks, bone, chitin, and metal. It channels the strength of a mallet, club, or a stone in a specific spot, allowing the sculptor to achieve a high level of precision."
                                    text "This specific chisel is made of steel, with marks of being stricken with other tools thousands of times. As far as you can tell, it’s a bit too heavy and narrow to be used on wood, but should work well with all sorts of stone. It bears no decorations - seeing it in an artisan’s workshop, you wouldn’t pay it any attention."
                                    text "According to the soul who gave it to you, “it was filled with magic decades ago, and makes its owner’s hands confident, so powerful they can carve in granite, so precise they can write in glass.”"
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "magicchisel2":
                                    text "A simple tool used for cutting or splitting hard surfaces, especially essential for people who carve in wood, stone, bone, chitin, and metal. It channels the strength of a mallet, club, or a stone in a specific spot, allowing the sculptor to achieve a high level of precision."
                                    text "This specific chisel is made of steel, with marks of being stricken with other tools thousands of times. As far as you can tell, it’s a bit too heavy and narrow to be used on wood, but should work well with all sorts of stone. It bears no decorations - seeing it in an artisan’s workshop, you wouldn’t pay it any attention."
                                    text "Eudocia has altered the spells stored in this item, allowing it to release huge amounts of pneuma whenever it’s hit while it stands on a firm surface."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "magicfruit":
                                    text "Its shape and size resemble an apple, or a quince. It’s also pale, entwining the whites and grays of bone. Based on how tough it seems to be, you don't imagine you can bite into it. However, the fruit is divided into natural {i}slices{/i}, which you can try to separate from the rest."
                                    text "There may be someone interested in getting it into their hands."
                                    if beholder_fruit_truth:
                                        text "[beholder_fruit_truth]"
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        textbutton _("Try to eat the fruit") action [SetVariable("item_magicfruit", 2), SetVariable("achievement_magicfruit", "atefruit"), SetVariable("pc_foodmagicfruit", 1), SetVariable("mana", 5), SetVariable("ruinedvillage_curse_points", 0), SetVariable("ruinedvillage_curse_block", 0), SetVariable("beholder_fruit_interaction", 1), SetVariable("inventoryinteraction", 1), SetVariable("quarters", quarters+4), SetVariable("pc_hp_can5", 1), SetVariable("pc_food", 4), SetVariable("item_detailedmenu", "magicfruiteating")]
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "magicfruiteating":
                                    if beholder_fruit_interaction == 1:
                                        text "Detaching the first “slice” isn’t difficult, and it feels like smooth granite. Before you take a good look at it, it turns into a gray powder and slips through your fingers. The rest of the fruit follows its example, covering your surroundings with an ash-like dust."
                                        text "The thing in front of you resembles yet another fruit, or a cherry-sized seed, levitating in the middle of a floral “rib-cage.” You can almost taste the pneuma effusing from it, tempting you to embrace it. It’s already going to waste, as if you completely destroyed the only force that was keeping it together."
                                        text "You know this is your last chance. You reach for the seed. It’s soft, warm, somehow innocent and gentle."
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                        textbutton _("I put it in my mouth") action [SetVariable("pc_hp", limit_pc_hp(pc_hp+5)), SetVariable("beholder_fruit_interaction", 2)]
                                    if beholder_fruit_interaction == 2:
                                        if pc_goal == "ineedmoney":
                                            text "It’s juicy, disgustingly close to the flavor of blood. You chew quickly and instantly experience the purest taste of being in love, of a never-ending friendship, of brotherhood. You start smiling, chuckling, laughing hysterically. Time flows without you and when it comes back, you feel sweat on your forehead. But you’re not tired, quite the opposite - you’re refreshed like you have never been before, without a single sign of illness or harm on your flesh."
                                        if pc_goal == "iwantmoney":
                                            text "It’s juicy, disgustingly close to the flavor of blood. You chew quickly and instantly experience the purest taste of wealth, of abundance and satiety. You start smiling, chuckling, laughing hysterically. Time flows without you and when it comes back, you feel sweat on your forehead. But you’re not tired, quite the opposite - you’re refreshed like you have never been before, without a single sign of illness or harm on your flesh."
                                        if pc_goal == "iwanttoberemembered":
                                            text "It’s juicy, disgustingly close to the flavor of blood. You chew quickly and instantly experience the purest taste of bravery, of valor, of greatness and glory. You start smiling, chuckling, laughing hysterically. Time flows without you and when it comes back, you feel sweat on your forehead. But you’re not tired, quite the opposite - you’re refreshed like you have never been before, without a single sign of illness or harm on your flesh."
                                        if pc_goal == "iwanttohelp":
                                            text "It’s juicy, disgustingly close to the flavor of blood. You chew quickly and instantly experience the purest taste of safety, of camaraderie, of benevolence. You start smiling, chuckling, laughing hysterically. Time flows without you and when it comes back, you feel sweat on your forehead. But you’re not tired, quite the opposite - you’re refreshed like you have never been before, without a single sign of illness or harm on your flesh."
                                        if pc_goal == "iwanttostartanewlife":
                                            text "It’s juicy, disgustingly close to the flavor of blood. You chew quickly and instantly experience the purest taste of freedom, of forgiveness, of a new beginning. You start smiling, chuckling, laughing hysterically. Time flows without you and when it comes back, you feel sweat on your forehead. But you’re not tired, quite the opposite - you’re refreshed like you have never been before, without a single sign of illness or harm on your flesh."
                                        if pc_goal == "iwantstatus":
                                            text "It’s juicy, disgustingly close to the flavor of blood. You chew quickly and instantly experience the purest taste of fame, of power, of wealth and control. You start smiling, chuckling, laughing hysterically. Time flows without you and when it comes back, you feel sweat on your forehead. But you’re not tired, quite the opposite - you’re refreshed like you have never been before, without a single sign of illness or harm on your flesh."
                                        text "After a few more breaths, you gather your senses. Your eyesight feels sharper."
                                        add "gui/statuspoints/hp/plus5hp.png":
                                            xalign 0.5
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                        textbutton _("Return") action [SetVariable("beholder_fruit_interaction", 0), SetVariable("inventoryinteraction", 0), Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                        timer 0.1 action [SetVariable("appearance", calculate_appearance(0))]
                                        timer 0.2 action [SetVariable("appearance_charisma", calculate_appearance_charisma(0)), SetVariable("appearance_price", calculate_appearance_price(0))]
                                if item_detailedmenu == "magicpens":
                                    if pc_class == "scholar":
                                        text "Quill pens are the most popular and durable tools used to write on parchment sheets. These particular feathers came from the left wings of geese and a swan and allow for lines of various thickness. As far as you can estimate, they were masterfully sharpened and could be used to write letters, draw miniatures, or make simple lines to divide pages into sections."
                                        text "You were asked by a monk from Old Págos to bring him this set from Eudocia, the enchantress."
                                    else:
                                        text "As far as you can tell, bird feathers are the main tool used to write on parchment. You were asked by a monk from Old Págos to bring them from Eudocia, the enchantress."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "mountainroadspear":
                                    text "Spears are the most common type of weapon used in The Dragonwoods, but it’s impossible to describe how a “regular” spear looks. The name covers everything from flexible, pointed sticks; through polished, processed branches with spearheads made of rock or bone; to masterfully preserved, rounded woodblocks with heads made of iron, copper, bronze, or steel. Some designs are characteristic for areas or tribes and have unique names, but there are also hundreds of types of spears that take into account available resources, artisans’ experience, the weapon’s purpose, and customers’ individual preferences."
                                    text "The difference between a fighter specialized in using spears and a greenhorn is vast, but it’s common for untrained travelers to carry long-range weapons just in case. It helps them keep their distance and allows them to jab at their opponent when an opportunity arises. A group of villagers with spears is like a moving wall and shouldn’t be underestimated."
                                    text "On the other hand, some fighters and monsters are capable of shortening the distance quickly and getting to the spear bearer. In such situations, this weapon becomes close to useless, so most spear masters train in another type of martial art and carry a shorter weapon as a backup."
                                    text "The spear you found in the mountains is rather simple, and was most likely meant to help during combat with medium-sized beasts. The bar set at the bottom of the head would stop the weapon from digging too deep into the opponent, while the iron ferrule placed at the bottom of the weapon could serve as a club in a desperate situation."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "pileofbones":
                                    text "If possible, human corpses are burnt on a pyre, where they turn into ash, what stops them from awakening. There are, however, other procedures that can obtain the same goal. Grinding bones into dust, or even just cutting them into tiny pieces, is enough to make them harmless. Still, most people see the process of butchering the shells as cruel and inhumane, and burning them instead is seen as a proper, “divine” way of saying farewell, even though it’s not a part of the teachings expressed in Wright’s Tablets."
                                    text "In the older times, there were rituals that took all these facts into consideration. To this day, some pagans throw their dead to the wild beasts, collecting back their bones only after they have been scraped clean. Such an approach is often criticized by The United Church, as it too often results in a shell disappearing in the wilderness, or getting awoken by a fog - an event that can never be predicted. However, it saves a lot of wood and labor."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        textbutton _("Destroy the bones") action [SetVariable("item_pileofbones", 0), SetVariable("item_pileofbones_destroyed", 1), SetVariable("quarters", (quarters+2)), SetVariable("item_detailedmenu", "item_pileofbones_destroyed"), SetVariable("achievement_pyrepoints", (achievement_pyrepoints+1))]
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "item_pileofbones_destroyed":
                                    text "The process is enervating, more so for your soul than shell. You pick one bone after another, place it on the nearest tree stump, and hit it with the back of your axe, repetitively, until it looks like crushed eggshells. The cracks are disheartening, but the longer it takes, the more numb you become."
                                    text "It takes you almost half an hour. You slip away without looking back."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "potiondolmen":
                                    if not item_potiondolmen_known:
                                        text "You can’t look inside and if you open it, you may not be able to seal it again. Nevertheless, you recognize a magical potion when you see one - it has a tall wax seal, inside of which there’s a thin stick, enabling swift opening. It could be anything."
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                        if can_items:
                                            textbutton _("Open and drink") action [SetVariable("item_potiondolmen", 0), SetVariable("inventoryinteraction", 1), SetVariable("quest_healingpotion_description04", "I have lost the potion. I should speak with the merchant."), SetVariable("pc_hp", limit_pc_hp(pc_hp+4)), SetVariable("item_detailedmenu", "potiondolmendrunk")]
                                            textbutton _("Open and smell") action [SetVariable("item_potiondolmen_known", 1)]
                                        else:
                                            text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                        textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                    else:
                                        text "It smells tasty, like fruits cooked in honey syrup. You don’t sense any hard drinks. Probably a healing potion."
                                        text "Healing potions may be the most desired liquid in The Dragonwoods, especially among travelers, hunters, and fighters. "
                                        text "You can safely seal the bottle again. The potion shouldn’t spoil anytime soon."
                                        add "gui/horizontalline.png":
                                            xalign 0.5
                                        if can_items or can_potions:
                                            textbutton _("Drink") action [SetVariable("item_potiondolmen", 0), SetVariable("inventoryinteraction", 1), SetVariable("quest_healingpotion_description04", "I have lost the potion. I should speak with the merchant."), SetVariable("pc_hp", limit_pc_hp(pc_hp+4)), SetVariable("item_detailedmenu", "potiondolmendrunk")]
                                        else:
                                            text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                        textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "potiondolmendrunk":
                                    if can_potions and not can_items:
                                        text "It tastes like honey, raspberries, and wormwood. The ecstatic warmth fills your limbs, and you can’t help but smile and giggle for a few breaths."
                                    else:
                                        text "It tastes like honey, raspberries, and wormwood. Initially, it’s awful, but you forget about your senses quickly. Your shell feels refreshed, strong, ready to act. Even the scratches are instantly healed. The ecstatic warmth fills your limbs, and you can’t help but smile and giggle for a few breaths."
                                    add "gui/statuspoints/hp/plus4hp.png":
                                        xalign 0.5
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("inventoryinteraction", 0), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                    timer 0.1 action [SetVariable("appearance", calculate_appearance(0))]
                                    timer 0.2 action [SetVariable("appearance_charisma", calculate_appearance_charisma(0)), SetVariable("appearance_price", calculate_appearance_price(0))]
                                if item_detailedmenu == "generichealingpotion":
                                    text "You recognize a magical potion when you see one - it has a tall wax seal, inside of which there’s a thin stick, enabling swift opening. The potion smells nice, like fresh herbs cooked with honey. You don’t sense a hint of a hard drink. Most healing potions have a similar aroma."
                                    text "Healing potions may be the most desired liquid in The Dragonwoods, especially among travelers, hunters, and fighters."
                                    text "It shouldn’t spoil anytime soon."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items or can_potions:
                                        if item_generichealingpotion:
                                            if (pc_hp < 4 and not pc_hp_can5) or (pc_hp < 5 and pc_hp_can5):
                                                textbutton _("Drink") action [SetVariable("item_generichealingpotion", item_generichealingpotion-1), SetVariable("inventoryinteraction", 1), SetVariable("pc_hp", limit_pc_hp(pc_hp+4)), SetVariable("item_detailedmenu", "generichealingpotiondrunk")]
                                            else:
                                                text "{color=#6a6a6a}You don’t need to heal your shell right now{/color}"
                                        else:
                                            text "{color=#6a6a6a}You already drank the last bottle{/color}"
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "generichealingpotiondrunk":
                                    if can_potions and not can_items:
                                        text "It tastes like honey, raspberries, and wormwood. The ecstatic warmth fills your limbs, and you can’t help but smile and giggle for a few breaths."
                                    else:
                                        text "It tastes like honey, raspberries, and wormwood. Initially, it’s awful, but you forget about your senses quickly. Your shell feels refreshed, strong, ready to act. Even the scratches are instantly healed. The ecstatic warmth fills your limbs, and you can’t help but smile and giggle for a few breaths."
                                    add "gui/statuspoints/hp/plus4hp.png":
                                        xalign 0.5
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("inventoryinteraction", 0), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                    timer 0.1 action [SetVariable("appearance", calculate_appearance(0))]
                                    timer 0.2 action [SetVariable("appearance_charisma", calculate_appearance_charisma(0)), SetVariable("appearance_price", calculate_appearance_price(0))]
                                if item_detailedmenu == "rawfish":
                                    if item_rawfishtotalnumber == 1:
                                        text "A freshwater fish, caught and killed by you. It would be better to put it to use soon, before it spoils."
                                    else:
                                        text "Freshwater fish, caught and killed by you. It would be better to put them to use soon, before they spoil."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "rope":
                                    text "Making a rope takes a lot of time and involves complex tools that combine thousands of fibers harvested from plants, mostly hemp, linen, or straws. Since it doesn’t take much skill and can be handled even by children, it’s rare to find an artisan who would specialize in twisting them all day long."
                                    text "Ropes are much more durable than leather strips and are used for all sorts of things, though their durability doesn’t make them a common merchandise. They can be heavy and awkward, so it’s common for groups of travelers to share a single one among all of them during their journey."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "cavemushroom":
                                    text "While it’s a common sense that one shouldn’t eat anything that grows on a wall of a cave, alchemists use some of the underground mushrooms to turn them into medicaments."
                                    text "Cave ears are believed to store the sounds of their surroundings that they release once they’re consumed by a living creature. Since they’re lethally poisonous, they should be first prepared by an experienced herbalist."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "casket":
                                    if item_casket_tested:
                                        text "{i}After some time of holding your wooden spheres together with the “cursed” coins, they’re as cold as usual. You doubt the bones store any pneuma inside.{/i}"
                                    text "{color=#f6d6bd}Navica’s{/color} box contains the payment she got for taking a group of adventurers to {color=#f6d6bd}High Island{/color}. She believes the dragon bones are now cursed, and bring bad fortune onto those who use them."
                                    text "You take a look inside - there’s 15 coins in total."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        if not item_casket_tested and pc_class == "mage":
                                            if mana >= 0:
                                                textbutton _("I examine the coins with the help of my pneuma-detecting amulets") action [SetVariable("item_casket_tested", 1), SetVariable("quarters", quarters+1)]
                                            else:
                                                text "{color=#6a6a6a}Your spirit is too weak to detect any pneuma in the dragon bones{/color}"
                                        if pc_religion != "pagan":
                                            textbutton _("I keep the coins for myself and will later lie to {color=#f6d6bd}Navica{/color} about them") action [SetVariable("item_casket", 0), SetVariable("inventoryinteraction", 1), SetVariable("quest_cursedcoins_description01", 1), SetVariable("coins", (coins+15)), SetVariable("item_detailedmenu", "caskettaken")]
                                            textbutton _("I add the coins to my own pouch and forget about this whole ordeal") action [SetVariable("item_casket", 0), SetVariable("inventoryinteraction", 1), SetVariable("quest_cursedcoins_description02", 1), SetVariable("coins", (coins+15)), SetVariable("quest_cursedcoins", 3), SetVariable("item_detailedmenu", "caskettaken")]
                                        else:
                                            textbutton _("I keep the coins for myself and will later lie to {color=#f6d6bd}Navica{/color} about them") action [SetVariable("item_casket", 0), SetVariable("inventoryinteraction", 1), SetVariable("quest_cursedcoins_description01", 1), SetVariable("coins", (coins+15)), SetVariable("pc_faithpoints_opportunities", (pc_faithpoints_opportunities+1)), SetVariable("pc_faithpoints", (pc_faithpoints-1)), SetVariable("item_detailedmenu", "caskettaken")]
                                            textbutton _("I add the coins to my own pouch and forget about this whole ordeal") action [SetVariable("item_casket", 0), SetVariable("inventoryinteraction", 1), SetVariable("quest_cursedcoins_description02", 1), SetVariable("pc_faithpoints_opportunities", (pc_faithpoints_opportunities+1)), SetVariable("pc_faithpoints", (pc_faithpoints-1)), SetVariable("coins", (coins+15)), SetVariable("quest_cursedcoins", 3), SetVariable("item_detailedmenu", "caskettaken")]
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "caskettaken":
                                    if pc_religion != "pagan":
                                        text "They rattle exactly the same as any other dragon bone. The casket will serve you as a container for a fragile bottle."
                                    else:
                                        text "They rattle exactly the same as any other dragon bone, even though you get the feeling of abandoning a sacred ritual. The casket will serve you as a container for a fragile bottle."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("inventoryinteraction", 0), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "dragonlingclaws":
                                    text "Claws are sculpted into brooches, amulets, pendants, styluses, or toys, while a whole set of them may be turned into a large necklace. In the countryside, larger claws are often used for constructing tools or weapons, though they are not too flexible."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "dragonlingpaw":
                                    text "You can get rid of the flesh and keep just the dragonling’s claws, which could be sold for at least a dragon bone. It will take you about half an hour."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        textbutton _("Detach the claws") action [SetVariable("item_detailedmenu", "dragonlingclaws"), SetVariable("item_dragonlingpaw", 0), SetVariable("item_dragonlingclaws", 1), SetVariable("item_hover_dragonlingclaws", 1), SetVariable("quarters", quarters+2)]
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "scholaringredients":
                                    if item_shortcutherbs or item_marshbules or item_bogfriend or item_rocktobepowdered or item_powderedrock or item_blackwoundwort or item_driftwood or item_cursedsoil:
                                        text "The list of useful ingredients you can look for:"
                                    if item_blackwoundwort == 1:
                                        text "* a bundle of black woundwort;"
                                    elif item_blackwoundwort > 1:
                                        text "* [item_blackwoundwort] bundles of black woundwort;"
                                    else:
                                        text "{color=#6a6a6a}* a bundle of black woundwort;{/color}"
                                    if item_snakebait == 2 and quest_eudociaflower == 1:
                                        text "* 2 snake bait flowers. Eudocia asked you for one of them;"
                                    if item_cavemushroom:
                                        text "* a cave ear mushroom;"
                                    else:
                                        text "{color=#6a6a6a}* a cave ear mushroom;{/color}"
                                    if item_snakebait == 2:
                                        text "* 2 snake bait flowers;"
                                    elif item_snakebait == 1 and quest_eudociaflower == 1:
                                        text "* a snake bait flower. Eudocia asked you for it;"
                                    elif item_snakebait == 1:
                                        text "* a snake bait flower;"
                                    else:
                                        text "{color=#6a6a6a}* a snake bait flower;{/color}"
                                    if item_cursedsoil:
                                        text "* a jar of cursed soil;"
                                    else:
                                        text "{color=#6a6a6a}* a jar of cursed soil;{/color}"
                                    if item_driftwood:
                                        text "* a piece of flower-looking driftwood;"
                                    else:
                                        text "{color=#6a6a6a}* a piece of flower-looking driftwood;{/color}"
                                    # if item_spidervenom:
                                    #     text "* a flask of spider venom;"
                                    # else:
                                    #     "{color=#6a6a6a}* a flask of spider venom;{/color}"
                                    if item_shortcutherbs:
                                        text "* a collection of herbs from the heart of the forest;"
                                    else:
                                        text "{color=#6a6a6a}* a collection of fresh, rare herbs;{/color}"
                                    if item_bogfriend:
                                        text "* bogfriend, a mushroom found at the wetlands;"
                                    else:
                                        text "{color=#6a6a6a}* bogfriend, a mushroom found at the wetlands;{/color}"
                                    if item_rocktobepowdered:
                                        text "* a basalt rock I need to powder on the top of the eastern mountain;"
                                    else:
                                        text "{color=#6a6a6a}* a basalt rock powdered on the top of a mountain;{/color}"
                                    if item_powderedrock:
                                        text "* a basalt rock powdered on the top of a mountain;"
                                    if item_marshbules == 1:
                                        text "* a bunch of marshbules;"
                                    elif item_marshbules > 1:
                                        text "* [item_marshbules] bunches of marshbules;"
                                    else:
                                        text "{color=#6a6a6a}* a bunch of marshbules.{/color}"
                                    text "Alchemy is meant to fill liquids with pneuma, replacing the required power and the mastery of spells with special ingredients, rituals, and instruments. Your collection includes rare liquids, plants, rocks, and animal remains. It’s not enough to brew a powerful mixture, but without them, even the most expensive workroom would be of little use."
                                    text "Finding new ingredients takes a bit of courage, but it’s also a part of your daily routine. Whenever you find something interesting growing near a road, you gather it for later use, just in case. Because of that, you also know the basics of herbalism, a less spectacular art which allows you to achieve predictable results without depending on unreliable pneuma."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "sewingkit":
                                    text "The needles, threads, and patches will help you fix the more outrageous damage your clothes and boots have received. It’s a time-consuming process, but that’s what it’ll take to camouflage your work and make your outfit presentable."
                                    if cleanliness_clothes_torn:
                                        text "The current poor condition of your clothes will draw a lot of attention."
                                    if armor_fixingxp >= 18:
                                        $ sheet_description8 = "expert"
                                    elif armor_fixingxp >= 15:
                                        $ sheet_description8 = "promisingly high"
                                    elif armor_fixingxp >= 12:
                                        $ sheet_description8 = "high"
                                    elif armor_fixingxp >= 8:
                                        $ sheet_description8 = "advanced"
                                    elif armor_fixingxp >= 6:
                                        $ sheet_description8 = "average"
                                    elif armor_fixingxp >= 3:
                                        $ sheet_description8 = "small"
                                    elif armor_fixingxp >= 1:
                                        $ sheet_description8 = "slight"
                                    elif armor_fixingxp <= 0:
                                        $ sheet_description8 = "none"
                                    if armor_fixingxp < 3:
                                        text "Having hardly any experience with the needle, you have to work slowly."
                                    elif armor_fixingxp >= 3 and armor_fixingxp < 6:
                                        text "Though you have some experience with the needle, you still have to work carefully."
                                    elif armor_fixingxp >= 6 and armor_fixingxp < 9:
                                        text "Your growing experience with the needle significantly speeds up the process."
                                    elif armor_fixingxp >= 9 and armor_fixingxp < 12:
                                        text "You are so used to working with the needle it takes you little time."
                                    elif armor_fixingxp >= 12:
                                        text "When it comes to fixing your own clothes, you’re pretty much an expert."
                                    text "The more you practice, the less time it takes for you to complete the repairs. Current experience: [sheet_description8]"
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if (quarters < world_daylength+1 and armor_fixingxp < 9) or (quarters < world_daylength+2 and armor_fixingxp >= 9) or (quarters < world_daylength+4 and armor_fixingxp >= 15):
                                        if can_items:
                                            if cleanliness_clothes_torn:
                                                if armor_fixingxp < 3:
                                                    textbutton _("Spend 2h to patch your clothes") action [SetVariable("quarters", quarters+8), SetVariable("cleanliness_clothes_torn", 0), SetVariable("armor_fixingxp", armor_fixingxp+1), SetVariable("inventoryinteraction", 1), SetVariable("item_detailedmenu", "sewingkit2")]
                                                elif armor_fixingxp >= 3 and armor_fixingxp < 6:
                                                    textbutton _("Spend 1h 45min to patch your clothes") action [SetVariable("quarters", quarters+7), SetVariable("cleanliness_clothes_torn", 0), SetVariable("armor_fixingxp", armor_fixingxp+1), SetVariable("inventoryinteraction", 1), SetVariable("item_detailedmenu", "sewingkit2")]
                                                elif armor_fixingxp >= 6 and armor_fixingxp < 9:
                                                    textbutton _("Spend 1h 30min to patch your clothes") action [SetVariable("quarters", quarters+6), SetVariable("cleanliness_clothes_torn", 0), SetVariable("armor_fixingxp", armor_fixingxp+1), SetVariable("inventoryinteraction", 1), SetVariable("item_detailedmenu", "sewingkit2")]
                                                elif armor_fixingxp >= 9 and armor_fixingxp < 12:
                                                    textbutton _("Spend 1h 15min to patch your clothes") action [SetVariable("quarters", quarters+5), SetVariable("cleanliness_clothes_torn", 0), SetVariable("armor_fixingxp", armor_fixingxp+1), SetVariable("inventoryinteraction", 1), SetVariable("item_detailedmenu", "sewingkit2")]
                                                elif armor_fixingxp >= 12:
                                                    textbutton _("Spend 1h to patch your clothes") action [SetVariable("quarters", quarters+4), SetVariable("cleanliness_clothes_torn", 0), SetVariable("armor_fixingxp", armor_fixingxp+1), SetVariable("inventoryinteraction", 1), SetVariable("item_detailedmenu", "sewingkit2")]
                                                elif armor_fixingxp >= 15:
                                                    textbutton _("Spend 45min to patch your clothes") action [SetVariable("quarters", quarters+4), SetVariable("cleanliness_clothes_torn", 0), SetVariable("armor_fixingxp", armor_fixingxp+1), SetVariable("inventoryinteraction", 1), SetVariable("item_detailedmenu", "sewingkit2")]
                                                elif armor_fixingxp >= 18:
                                                    textbutton _("Spend 30min to patch your clothes") action [SetVariable("quarters", quarters+4), SetVariable("cleanliness_clothes_torn", 0), SetVariable("armor_fixingxp", armor_fixingxp+1), SetVariable("inventoryinteraction", 1), SetVariable("item_detailedmenu", "sewingkit2")]
                                            else:
                                                text "{color=#6a6a6a}Your outfit doesn’t require any work right now.{/color}"
                                        else:
                                            text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    else:
                                        text "{color=#6a6a6a}It’s too dark and you’re too sleepy to work on your outfit{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "sewingkit2":
                                    text "Once you’re done, you spend a few minutes hiding your sewing kit."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("inventoryinteraction", 0), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                    timer 0.1 action [SetVariable("appearance", calculate_appearance(0))]
                                    timer 0.2 action [SetVariable("appearance_charisma", calculate_appearance_charisma(0)), SetVariable("appearance_price", calculate_appearance_price(0))]
                                if item_detailedmenu == "shield":
                                    text "There are countless designs of shields, some of them answering specific needs and tactics used by local fighters, while others are a result of limited resources or vague traditions, the feeling that a specific shape is how a shield {i}should{/i} look. They are a bit different in every village, though every few dozen miles it’s hard to consider them in any way similar, especially since they are decorated in many ways, making even identical designs unique in their execution."
                                    text "In The Dragonwoods, they are mainly used by three groups of people: farmers and workers, who in desperate times grab simple spears and light shields to form a wall, hoping to avoid close combat; soldiers, especially those who specialize in fighting with bandits or undead, using their shields to their advantage thanks to years of training; and adventurers, especially those who are meant to stay in the first row during combat. Shields are not especially useful when it comes to fighting massive predators, capable of breaking them to pieces with a single strike, or completely ignoring them during their charge."
                                    text "You’ve hardly trained with a shield and you almost always take just your axe, relying on the nimbleness of your legs and having the option to make a cut from every direction or with two hands at once, but such an item can be used in many other ways, especially to protect yourself from arrows or stones."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "signpost":
                                    text "The Northerners who live outside of cities invent various signs to replace letters. This plank is covered with dark red paint, a sign understood in most provinces - “blood there,” or “a danger to be found.”"
                                    text "The few pieces of a hemp cord will help you attach it to a post or a tree."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "spidersilk":
                                    text "While humans avoid or exterminate the larger spiders, they are not without their use. The {i}silk{/i} they produce is thick and, if properly stored, can be used in its entirety to produce an unusually firm thread, excellent for sewing together pieces of fabric."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "stoat":
                                    text "These little critters are turned into soft, luxurious clothing or, if there’s not enough of them, into trimming added to cloaks and robes. While their furs are worth much more than their meat, processing them takes skills that you lack and involves a couple of hours of unpleasant, pungent work spread across days of waiting, not to mention tools, a bunch of salt, and a place where it can dry without being disturbed."
                                    if item_stoat == 1:
                                        text "This carcass was damaged during your hunt, but should be worth a couple of dragons. It needs to be sold soon, before it begins to spoil."
                                    if item_stoat == 2:
                                        text "This carcass is in pretty much perfect condition, but needs to be sold soon, before it begins to spoil."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "letterwhitemarshes":
                                    text "Wax tablets are the most common writing instrument used in the North, though they are usually made of wood. The previous owner of this carved bone is depicted on the back - a massive, furry troll. Tablets usually fit in one’s hand and are used to make notes or write down short messages, especially when there’s no option to prepare a scroll and inkstand. It’s also easy to erase the previous inscriptions, and a single tablet may be used dozens or hundreds of times."
                                    if item_letterwhitemarshes_read:
                                        if pc_class == "scholar":
                                            text "It’s a short farewell letter addressed to {color=#f6d6bd}Valens{/color} from {color=#f6d6bd}White Marshes{/color}, with a mixture of apologies and bitterness. His husband has decided to leave him for another soul."
                                        else:
                                            text "You were told that it’s a farewell letter addressing {color=#f6d6bd}Valens{/color} from {color=#f6d6bd}White Marshes{/color}. His husband has decided to leave him for another soul."
                                    else:
                                        text "You can’t read the contents of the tablets on your own."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "teethset":
                                    text "Most people lose at least one tooth every decade or so. According to herbalists, cleaning your teeth regularly may help you reach your elderly days with enough teeth left to bite off and chew meat."
                                    text "Those who care enough about their health use partially chewed ends of young twigs to brush their teeth at least once a day. However, it’s well-known that a bad smell can invite bad health, or even spread illnesses to other people. Because of that, various ingredients are used to create helpful pastes that provide pleasant, fresh breath."
                                    text "The set you own is rather fancy. The [item_teethset_type] twigs are stored in a solid, leather holder and the small, wooden box has four separate compartments. One of them contains salt, another one - cloves, the third one - leaves of mint, which won’t last for long, but you should be able to replace them easily. The last part, shaped like a bowl, is empty, used to grind the ingredients with a stone pestle and mix them into a single paste. While cloves and mint don’t mix well together, at least you can easily switch the flavors when you get bored."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "thaisletter":
                                    text "A scroll made of smooth mouflon skin. Its wooden handles are polished and covered in fresh wax."
                                    text "The letter was written by Thais, the mayor of Howler’s Dell, and as far as you know, she described her plans to secure a trade route with the merchant guild and to start paying taxes to receive the support of Hovlavan’s military. You were asked to take it to your superiors in the city."
                                    text "The scroll is tied with a tight linen cord, which, together with the parchment, is sealed. You don’t see a way to slide the cord off without breaking the seal, which is a work of art on its own - it presents a tree that bears no leaves, nor fruits, similar to the one you’ve seen in the village square."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if not item_thaisletter_readingblocked:
                                        if can_items:
                                            if pc_class == "scholar" and not banditshideout_galerocks_tiestobandits:
                                                textbutton _("Break the seal") action [SetVariable("item_thaisletter", 0), SetVariable("item_thaisletter_opened", 1), SetVariable("item_thaisletter_read", 1), SetVariable("banditshideout_galerocks_tiestobandits", 1), SetVariable("quarters", quarters+1), SetVariable("item_detailedmenu", "thaisletteropened")]
                                            elif pc_class == "scholar":
                                                textbutton _("Break the seal") action [SetVariable("item_thaisletter", 0), SetVariable("item_thaisletter_opened", 1), SetVariable("item_thaisletter_read", 1), SetVariable("quarters", quarters+1), SetVariable("item_detailedmenu", "thaisletteropened")]
                                            else:
                                                textbutton _("Break the seal") action [SetVariable("item_thaisletter", 0), SetVariable("item_thaisletter_opened", 1), SetVariable("quarters", quarters+1), SetVariable("item_detailedmenu", "thaisletteropened")]
                                        else:
                                            text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "thaisletteropened":
                                    if pc_class != "scholar":
                                        text "A scroll made of smooth mouflon skin. Its wooden handles are polished up and covered in fresh wax."
                                        text "In it, you find a bunch of letters, mostly green, but some of them are larger and red. However, you don't know what they are trying to convey."
                                        text "The letter was written by Thais, the mayor of Howler’s Dell, and as far as you know, she described her plans to secure a trade route with the merchant guild and to start paying taxes to receive the support of Hovlavan’s military. You were asked to take it to your superiors in the city."
                                    else:
                                        text "A scroll made of smooth mouflon skin. Its wooden handles are polished and covered in fresh wax."
                                        text "It mostly uses green ink - one of the most expensive ones, made of verdigris, a masterfully destroyed copper. Each paragraph starts with a red initial, decorated with leaves, shrubs, and creepers. The letter is long and filled with boring, very “official” salutations. One of the parts directly contradicts what Thais has told you:"
                                        text "{i}The beliefs of our fathers are sacred to us, but depending on the proof of your good will, we will permit your missionaries to stay within our walls. I promise they will be treated with the dignity they deserve.{/i}"
                                        text "One more part also grabs your attention:"
                                        text "{i}This piece of information is sensitive, but I trust that you will put it to good use. Gale Rocks, a village set near the northern shore, participates in trade with the local bandits, led by their own Glaucia. Their alliance grows in strength, and therefore brings many threats to our potential collaboration.{/i}"
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "travelset":
                                    if item_earplugs:
                                        $ earplugsitem_hover = ", earplugs"
                                    else:
                                        $ earplugsitem_hover = ""
                                    text "All sorts of odds and ends that you’ve taken on this journey “just in case.” A rainproof cloak; a set of bone needles and a thread; an iron knife; a blade sharpener; a tinderbox and a couple of tallow candles; a bunch of rags used to make torches, as well as a flask of oil; a pair of protective gloves made of thick leather[earplugsitem_hover]..."
                                    if item_teethset or item_soap or item_perfume:
                                        text "You also found some equipment that will help you stay clean:"
                                    if item_teethset:
                                        text "{color=#f6d6bd}A Teeth-Cleaning Set{/color} - A few [item_teethset_type] twigs stored in a solid, leather holder and a small, wooden box with four compartments. One of them contains salt, another one - cloves, the third one - leaves of mint. The herbs won’t last for long, but you’ll easily replace them. The last part, shaped like a bowl, is empty, used to grind the ingredients with a stone pestle, then mix them into a single paste. While cloves and mint don’t mix well together, at least you can easily switch the flavors when you get bored."
                                    if item_soap:
                                        text "{color=#f6d6bd}An Oak-Ash Soap{/color} - A box with thick balm that needs to be rubbed against the skin, then rinsed before it starts to burn. Made of ash, tallow, quicklime, water, and a few other ingredients, it lets you get rid of dirt and fat in no time. It’s almost odorless."
                                    if item_perfume:
                                        text "{color=#f6d6bd}A [item_perfume_type] Perfume{/color} - An oil that was squeezed out after being mixed with petals of hundreds of flowers, then combined with a few other ingredients. It’s intense and keeps its smell for a while, unless you get wet or sweaty. You usually place it behind your ears and on your wrists."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if not item_earplugs and northernroad_firsttime:
                                        if can_items:
                                            textbutton _("I make a set of earplugs from a wax candle") action [SetVariable("item_earplugs", 1), SetVariable("item_detailedmenu", "travelequipmentearplugs")]
                                        else:
                                            text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "travelequipmentearplugs":
                                    text "You cut off parts of a candle, remove the wick, and grap the small chunks of wax. You roll them in your hands, warming them up and forming them into a new shape. Once you’re done, you put the new earplugs with the rest of your travel equipment."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "wildplants":
                                    text "Foraging is an essential labor in the villages of the North. Lethally dangerous in the wilderness, but more of a routine in the forest gardens, though never completely safe - it’s done in groups, and only by adults."
                                    text "Wild fruits, including grapes, apples, pears, and plums, are smaller and more sour than the ones cultivated by farmers and tend to have larger seeds. Children from a very young age are taught how to identify poisonous berries. Vegetables usually take some cooking, or at least cutting and cleaning. Carrots, fennels, cabbage, onions, sorrels, and lettuce are just some of the ones that can be eaten raw, though they feel either too bland or too intense to be enjoyed by themselves."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if item_wildplants:
                                        if can_items:
                                            if pc_food < 4:
                                                textbutton _("Eat some plants to increase your {color=#f6d6bd}nourishment{/color} by 1") action [SetVariable("item_wildplants", item_wildplants-1), SetVariable("pc_food", limit_pc_food(pc_food+1))]
                                            else:
                                                text "{color=#6a6a6a}You don’t need to eat right now{/color}"
                                        else:
                                            text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    else:
                                        text "{color=#6a6a6a}You don’t have any plants left{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "wingedhourglass":
                                    text "The winged hourglass was adapted by the largest religions of The Ten Cities - The United Church, the Orders of Truth, and the majority of fellowships. It’s used in temples and funeral rites, but also to decorate expensive codices or pieces of clothing. Not every soul who wears such a trinket in a visible place is a devoted believer, but it can be seen as a sign of solidarity with the more conservative section of the city culture."
                                    text "Emblems like this one are meant to portray the ephemerality of life and the rigidity of time. The traditional pendants are made of steel, signifying the strength of humankind’s determination and innovation. Wright’s Tablets highlight the important role of iron when it came to fighting monsters and expanding the lands of the tribes. Other materials, such as bone, gold, or even wood, are also used, though various communities interpret such alterations in their own ways. The pendants made of steel are not so contentious."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    if can_items:
                                        if pc_religion == "pagan":
                                            if not item_wingedhourglass_taboo_broken:
                                                textbutton _("I {i}shouldn’t{/i} wear it, but it may help me get closer to some of the locals") action [SetVariable("item_wingedhourglass_worn", 1), SetVariable("item_wingedhourglass_taboo_broken", 1), SetVariable("pc_faithpoints", pc_faithpoints-2)]
                                            else:
                                                if item_wingedhourglass_worn:
                                                    textbutton _("Move it to your pouch") action [SetVariable("item_wingedhourglass_worn", 0)]
                                                else:
                                                    textbutton _("Wear it on your neck") action [SetVariable("item_wingedhourglass_worn", 1)]
                                        else:
                                            if item_wingedhourglass_worn:
                                                textbutton _("Move it to your pouch") action [SetVariable("item_wingedhourglass_worn", 0), SetVariable("pc_faithpoints", pc_faithpoints-1)]
                                            else:
                                                textbutton _("Wear it on your neck") action [SetVariable("item_wingedhourglass_worn", 1), SetVariable("pc_faithpoints", pc_faithpoints+1)]
                                    else:
                                        text "{color=#6a6a6a}You can’t use your inventory right now{/color}"
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "witheringdust":
                                    text "It’s a mix of dried, toxic plants and dangerous, powdered stones. Such substances should be placed on the ground near the roots of a plant and sprinkled with water. Ideally while wearing thick, leather gloves and keeping one’s nostrils as far away as possible."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "writinginstruments":
                                    text "Most people in The Dragonwoods don’t need to know how to read or write. The lessons are time-consuming and, often, expensive. The exchange of written texts is practiced among people who need to create complex, exact documents and keep them in good condition for years, or even centuries. This group includes priests, lawyers, inventors, officials, richer merchants, and high-ranking military chieftains. Less than ten percent of society is literate, and the major part of this group lives in The Cities."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                                if item_detailedmenu == "100coins":
                                    if pc_goal == "ineedmoney":
                                        text "Once you combine this small fortune with the merchant guild’s pay, it’ll be enough to save your sibling from debt collectors."
                                    if pc_goal == "iwantmoney":
                                        text "Once you combine this small fortune with the merchant guild’s pay, it’ll be enough to help you invest into some trading ships or caravans."
                                    add "gui/horizontalline.png":
                                        xalign 0.5
                                    textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                        vbar value YScrollValue ("inventoryscroll"):
                            xpos 40
                            unscrollable "hide"
            if inventoryinteraction:
                key "game_menu" action NullAction()
                key "mouseup_2" action NullAction()
                key "mousedown_2" action NullAction()
            else:
                key "game_menu" action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                key "mouseup_2" action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                key "mousedown_2" action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
                # text ""
                # textbutton _("Return") action [Hide("inv_detailedmenu"), SetVariable("item_detailedmenu", 0), SetVariable("inventoryscreenmode", "list")]
        # $ config.keymap['game_menu'].append('i')
        # $ config.keymap['game_menu'].append('I')
        # key "i" action [Hide"_game_menu_screen"]

style inventory_prompt_text is gui_prompt_text:
    size 34
    color "#6a6a6a"
    xpos 4
    ypos 2
    layout "subtitle"
style invdetailedmenu_prompt is gui_prompt
style invdetailedmenu_prompt_text is gui_prompt_text:
    size 36
    yalign 0.5
    color "#c3a38a"
style invdetailedmenu_button is gui_medium_button:
    xpos -6
style invdetailedmenu_button_text is gui_medium_button_text:
    color "#997577"
    hover_color "#f6d6bd" # c3a38a
    size 30
style invdetailedmenu_text is gui_text:
    size 30
    color '#c3a38a'
style invdetailedmenu_frame is gui_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.invdetailedmenu_frame_borders, tile=gui.frame_tile)
    padding gui.invdetailedmenu_frame_borders.padding
    xalign .5
    yalign .5
style invdetailedmenu_prompt_text:
    text_align 0.5
    layout "subtitle"

style inventoryimage:
    focus_mask True
    xalign 0.5
    yalign 0.5
    yminimum 122

style inventoryimage2:
    focus_mask True
    xalign 0.5
    yalign 0.5
