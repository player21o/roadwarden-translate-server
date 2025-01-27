################################################################################
## Initialization
################################################################################

init offset = -1

######### SHOP
default bath_estimateappearance = 0
default thyrsus_estimate_wares = 0
screen shopscreen():
    zorder 200
    modal True
    style_prefix "shop"
    add "gui/overlay/confirm.png"
    if shop == "tutorial":
        key "game_menu" action NullAction()
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/foodrationsidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[item_rations]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[item_rations]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
            frame:
                vbox:
                    xalign .5
                    spacing 28
                    label _("A Fine Rope"):
                        style "shop_prompt"
                        xalign 0.5
                    add "inventory/ropeidle.png":
                        xalign 0.5
                    text "A regular rope made of hemp fibers." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                    textbutton _("Buy: 0 {image=coin}") action [SetVariable("item_rope", 1), Notify("You received a rope."), Hide("shopscreen", transition=dissolve), Jump('militarycamp01askingabouttherope03')] text_align 0.5 xalign .5
                    textbutton _("I take it and offer\nsome food in return") action [SetVariable("item_rope", 1), Notify("You received a rope and lost a food ration."), Hide("shopscreen", transition=dissolve), Jump('militarycamp01askingabouttherope03a')] text_align 0.5 xalign .5

    elif shop == "peltnorth":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('peltnorthregularquestionsv03')]
        $ iason_shop_crossbow_price = (30-iason_shop_crossbow_discount+(appearance_price*2))
        if iason_friendship >= 12:
            $ iason_shop_furprice_base = (14+appearance_price)
        elif iason_friendship >= 8:
            $ iason_shop_furprice_base = (15+appearance_price)
        elif iason_friendship >= 4:
            $ iason_shop_furprice_base = (16+appearance_price)
        elif iason_friendship > 0:
            $ iason_shop_furprice_base = (17+appearance_price)
        elif iason_friendship == 0:
            $ iason_shop_furprice_base = (18+appearance_price)
        elif iason_friendship == -1:
            $ iason_shop_furprice_base = (19+appearance_price)
        else:
            $ iason_shop_furprice_base = (20+appearance_price)
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/foodrationsidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[item_rations]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[item_rations]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('peltnorthregularquestionsv03')]
            frame:
                vbox:
                    spacing 30
                    hbox:
                        spacing 0
                        xmaximum 1080
                        box_wrap True
                        box_wrap_spacing 30
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("Food Rations"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/foodrationsidle.png":
                                xalign 0.5
                            text "Three filling meals that\nwon’t spoil anytime soon." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            hbox:
                                xalign 0.5
                                if iason_shop_foodrations_day != day:
                                    if coins:
                                        textbutton _("Buy: 1 {image=coin}") action [SetVariable("quarters", quarters+1), SetVariable("coins", limit_coins(coins-1)), SetVariable("item_rations", item_rations+3), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+1), SetVariable("iason_shop_foodrations_day", day), Notify("You bought three food rations.")] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Buy: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}You can buy\nmore tomorrow{/color}") action NullAction() text_align 0.5 xalign .5
                        if not iason_shop_furbought:
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                label _("An Elk Fur"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/fursidle.png":
                                    xalign 0.5
                                text "A high-class fur.\nA valuable commodity." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if coins >= iason_shop_furprice_base:
                                        textbutton _("Buy: [iason_shop_furprice_base] {image=coin}") action [SetVariable("item_elkfur", 1), SetVariable("coins", limit_coins(coins-iason_shop_furprice_base)), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+3), SetVariable("iason_shop_furbought", day), Notify("You bought the elk fur.")] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Buy: [iason_shop_furprice_base] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        if not iason_shop_crossbow_bought and not item_crossbow:
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                label _("A Crossbow"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/crossbowshopidle.png":
                                    xalign 0.5
                                text "A decent crossbow\nwith 5 quarrels." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if coins >= iason_shop_crossbow_price and not item_crossbow:
                                        textbutton _("Buy: [iason_shop_crossbow_price] {image=coin}") action [SetVariable("item_crossbow", 1), SetVariable("item_crossbowquarrels", item_crossbowquarrels+5), SetVariable("coins", limit_coins(coins-iason_shop_crossbow_price)), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+5), SetVariable("iason_shop_crossbow_bought", day), Notify("You bought the crossbow and a set of quarrels.")] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Buy: [iason_shop_crossbow_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        if iason_shop_shield and not iason_shop_shield_bought:
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                label _("A Shield"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/shield1idle.png":
                                    xalign 0.5
                                text "You’re not used\nto using it in combat." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if coins >= iason_shop_shield_price and not item_shield:
                                        textbutton _("Buy: [iason_shop_shield_price] {image=coin}") action [SetVariable("item_shield", 1), SetVariable("coins", limit_coins(coins-iason_shop_shield_price)), SetVariable("iason_shop_shield_bought", day), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+2), Notify("You bought a shield.")] text_align 0.5 xalign .5
                                    elif item_shield:
                                        textbutton _("{color=#6a6a6a}You already\nown one{/color}") action NullAction() text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Buy: [iason_shop_shield_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        if not iason_shop_quarrels:
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                label _("Quarrels"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/quarrelsidle.png":
                                    xalign 0.5
                                text "A set of 5 arrows\nfor a crossbow." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if coins >= 2:
                                        textbutton _("Buy: 2 {image=coin}") action [SetVariable("item_crossbowquarrels", item_crossbowquarrels+5), SetVariable("coins", limit_coins(coins-2)), SetVariable("iason_shop_quarrels", day), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+5), Notify("You bought a set of quarrels.")] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Buy: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        if not iason_shop_soap:
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                label _("A Box of Soap"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/soapidle.png":
                                    xalign 0.5
                                text "An oak-based balm that burns skin on longer contact." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if not item_soap:
                                        if coins:
                                            textbutton _("Buy: 1 {image=coin}") action [SetVariable("item_soap", 1), SetVariable("coins", limit_coins(coins-1)), SetVariable("iason_shop_soap", day), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+1), SetVariable("cleanliness_equipment", cleanliness_equipment+1), Notify("You add the soap to your travel set.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}You already\nown one{/color}") action NullAction() text_align 0.5 xalign .5
    elif shop == "peltnorth_armorer":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('peltnorthtalkingwitharmorer01')]
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('peltnorthtalkingwitharmorer01')]
            frame:
                if quarters >= (world_daylength-8):
                    yalign 0.0
                    vbox:
                        xalign .5
                        spacing 28
                        ypos 10
                        xmaximum 360
                        xminimum 360
                        yminimum 123
                        ymaximum 123
                        text "{color=#6a6a6a}The armorer is closing his workshop.{/color}" text_align 0.5 xmaximum 410 xminimum 410 xalign .5 yalign .5
                else:
                    vbox:
                        spacing 30
                        hbox:
                            spacing 0
                            xmaximum 1080
                            box_wrap True
                            box_wrap_spacing 30
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 400
                                xminimum 400
                                label _("Gambeson Repairs"):
                                    style "shop_prompt"
                                    xalign 0.5
                                if not armor:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/plus2armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "In 1h 30 min, your jacket will be partially resewn and repadded." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                    if coins >= 2:
                                        textbutton _("Pay: 2 {image=coin}") action [SetVariable("armor", limit_armor(armor+2)), Function(renpy.show, "plus2armor", at_list=[armorchange]), SetVariable("coins", limit_coins(coins-2)), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+1), SetVariable("quarters", quarters+6)] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Pay: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                if armor == 1:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/plus1armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "In one hour, your jacket will be partially resewn and repadded." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                    if coins >= 1:
                                        textbutton _("Pay: 1 {image=coin}") action [SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("coins", limit_coins(coins-1)), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+1), SetVariable("quarters", quarters+4)] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Pay: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                if armor == 2:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/plus1armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "In one hour, your jacket will be carefully patched up." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                    if coins >= 1:
                                        textbutton _("Pay: 1 {image=coin}") action [SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("coins", limit_coins(coins-1)), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+1), SetVariable("quarters", quarters+4)] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Pay: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                if armor == 3 and not armor_can4:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/3armormax.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "Your jacket is as good as this armorer can make it." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                if armor == 3 and armor_can4:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/3armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "Your jacket is as good as this armorer can make it." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                if armor == 4:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/4armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "Your jacket is already\nas good as it can get." text_align 0.5 xmaximum 410 xminimum 410 xalign .5

    elif shop == "eudociahouse": #or shop == "eudociahouseinside"
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('eudociahouseafterquestione')]
        $ eudocia_about_spiritrock_price = (eudocia_about_spiritrock_price_base+appearance_price)
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('eudociahouseafterquestione')]
            frame:
                vbox:
                    #spacing 30
                    hbox:
                        spacing 0
                        xmaximum 1080
                        box_wrap True
                        box_wrap_spacing 30
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 400
                            xminimum 400
                            label _("A Spirit Rock"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/spiritrockidle.png":
                                xalign 0.5
                            text "A pebble filled\nwith pneuma.\nUseful for spellcasters." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            if coins >= eudocia_about_spiritrock_price:
                                textbutton _("Buy: [eudocia_about_spiritrock_price] {image=coin}") action [SetVariable("item_spiritrock", item_spiritrock+1), SetVariable("coins", limit_coins(coins-eudocia_about_spiritrock_price)), Notify("You bought a spirit rock."), Hide("shopscreen", transition=dissolve)] text_align 0.5 xalign .5
                            else:
                                textbutton _("{color=#6a6a6a}Buy: [eudocia_about_spiritrock_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        if not item_magicalsapling and quest_ruins == 1 and eudocia_about_magicsapling and ruinedvillage_part_leftfield_EXPLORED == 1:
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 400
                                xminimum 400
                                label _("Eudocia’s Sapling"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/magicalsaplingidle.png":
                                    xalign 0.5
                                text "It’s meant to react to\nmagically altered soil." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                if coins >= 2:
                                    textbutton _("Buy: 2 {image=coin}") action [SetVariable("item_magicalsapling", (item_magicalsapling+1)), SetVariable("coins", limit_coins(coins-2)), Notify("You bought the sapling."), Hide("shopscreen", transition=dissolve)] text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Buy: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5

    elif shop == "howlersdelltailor":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('howlersdelltailorafterinteraction')]
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                if item_howlersdelltoken:
                    fixed:
                        maximum (102,121)
                        minimum (102,121)
                        imagebutton:
                            style "inventoryimage"
                            idle "inventory/howlersdelltokenidle.png"
                            action NullAction()
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('howlersdelltailorafterinteraction')]
            frame:
                if quarters >= (world_daylength+6):
                    yalign 0.0
                    vbox:
                        xalign .5
                        spacing 28
                        ypos 10
                        xmaximum 360
                        xminimum 360
                        yminimum 123
                        ymaximum 123
                        text "{color=#6a6a6a}Bion is closing her shop.{/color}" text_align 0.5 xmaximum 410 xminimum 410 xalign .5 yalign .5
                else:
                    vbox:
                        spacing 30
                        hbox:
                            spacing 0
                            xmaximum 1080
                            box_wrap True
                            box_wrap_spacing 30
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 400
                                xminimum 400
                                label _("Gambeson Repairs"):
                                    style "shop_prompt"
                                    xalign 0.5
                                if not armor:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/plus2armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    if not item_howlersdelltoken:
                                        text "In an hour, your jacket will be partially resewn and repadded." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                        if coins >= 3:
                                            textbutton _("Pay: 3 {image=coin}") action [SetVariable("armor", limit_armor(armor+2)), Function(renpy.show, "plus2armor", at_list=[armorchange]), SetVariable("coins", limit_coins(coins-3)), SetVariable("quarters", quarters+4)] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: 3 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                    else:
                                        text "In an hour, your jacket will be partially resewn and repadded." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                        textbutton _("Pay: 0 {image=coin}") action [SetVariable("armor", limit_armor(armor+2)), Function(renpy.show, "plus2armor", at_list=[armorchange]), SetVariable("quarters", quarters+4)] text_align 0.5 xalign .5
                                if armor == 1:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/plus1armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    if not item_howlersdelltoken:
                                        text "In half an hour, your jacket will be partially resewn and repadded." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                        if coins >= 2:
                                            textbutton _("Pay: 2 {image=coin}") action [SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("coins", limit_coins(coins-2)), SetVariable("quarters", quarters+2)] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                    else:
                                        text "In half an hour, your jacket will be partially resewn and repadded." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                        textbutton _("Pay: 0 {image=coin}") action [SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("quarters", quarters+2)] text_align 0.5 xalign .5
                                if armor == 2:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/plus1armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    if not item_howlersdelltoken:
                                        text "In half an hour, your jacket will be carefully patched up." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                        if coins >= 2:
                                            textbutton _("Pay: 2 {image=coin}") action [SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("coins", limit_coins(coins-2)), SetVariable("quarters", quarters+2)] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                    else:
                                        text "In half an hour, your jacket\nwill carefully be patched up." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                        textbutton _("Pay: 0 {image=coin}") action [SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("quarters", quarters+2)] text_align 0.5 xalign .5
                                if armor == 3 and not armor_can4:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/3armormax.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "Your jacket is already\nas good as it can get." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                if armor == 3 and armor_can4:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/plus1armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    if not item_howlersdelltoken:
                                        text "In half an hour, your jacket will be precisely adjusted to your figure, making it easier to fight in it." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                        if coins >= 2:
                                            textbutton _("Pay: 2 {image=coin}") action [SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("coins", limit_coins(coins-2)), SetVariable("quarters", quarters+2)] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                    else:
                                        text "In half an hour, your jacket will be precisely adjusted to your figure, making it easier to fight in it." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                        textbutton _("Pay: 0 {image=coin}") action [SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("quarters", quarters+2)] text_align 0.5 xalign .5
                                if armor == 4:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/4armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "Your jacket is already\nas good as it can get." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 400
                                xminimum 400
                                label _("Outfit Repairs"):
                                    style "shop_prompt"
                                    xalign 0.5
                                vbox:
                                    yminimum 102
                                    xalign 0.5
                                    add "gui/statuspoints/appearance/plus1appearance.png":
                                        xalign 0.5
                                        yalign 0.5
                                text "In 15 min, your clothes will\nget patched and tidy." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                if cleanliness_clothes_torn:
                                    if coins >= 1:
                                        textbutton _("Pay: 1 {image=coin}") action [SetVariable("cleanliness_clothes_torn", 0), Function(renpy.show, "plus1appearance", at_list=[appearancechange]), SetVariable("coins", limit_coins(coins-1)), SetVariable("quarters", quarters+1)] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Pay: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Your outfit\nneeds no work{/color}") action NullAction() text_align 0.5 xalign .5
                            if not armor_can4:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 400
                                    xminimum 400
                                    label _("Gambeson Enhancement"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/gambeson02idle.png":
                                        xalign 0.5
                                    text "In two hours, parts of its\nthread will be replaced by\nthe spider silk." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    vbox:
                                        xalign 0.5
                                        if coins >= 20:
                                            textbutton _("Pay: 20 {image=coin}") action [Hide("shopscreen", transition=dissolve), Jump('howlersdelltailorspidersilk02')] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: 20 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                        if item_spidersilk:
                                            textbutton _("Offer the\nspider silk") action [Hide("shopscreen", transition=dissolve), Jump('howlersdelltailorspidersilk01')] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Find your own silk\nto get a better price{/color}") action NullAction() text_align 0.5 xalign .5
    elif shop == "howlersdelltailor2":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('howlersdelltailorafterinteraction')]
        $ howlersdell_bion_shop_clothes_price1 = (howlersdell_bion_shop_clothes_price1_base-(howlersdell_reputation/3)+(appearance_price*2))
        $ howlersdell_bion_shop_clothes_price2 = (howlersdell_bion_shop_clothes_price2_base-(howlersdell_reputation/3)+(appearance_price*3))
        $ howlersdell_bion_shop_clothes_price3 = (howlersdell_bion_shop_clothes_price3_base-(howlersdell_reputation/3)+(appearance_price*3))
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('howlersdelltailorafterinteraction')]
            frame:
                vbox:
                    spacing 30
                    text "Each outfit includes shoes, pants, belt, and jewelry." text_align 0.5 xmaximum 820 xminimum 820 xalign .5
                    hbox:
                        spacing 0
                        xmaximum 1200
                        box_wrap True
                        box_wrap_spacing 30
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 400
                            xminimum 400
                            label _("A Fancy Tunic"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/fancyclothes1idle.png":
                                xalign 0.5
                            text "Fitting for a\nrich city official.\nTakes one day of work." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                            hbox:
                                xalign 0.5
                                if coins >= howlersdell_bion_shop_clothes_price1:
                                    textbutton _("Pay: [howlersdell_bion_shop_clothes_price1] {image=coin}") action [SetVariable("howlersdell_bion_shop_clothes_daypickingup", day), SetVariable("coins", limit_coins(coins-howlersdell_bion_shop_clothes_price1)), SetVariable("quarters", quarters+3), SetVariable("howlersdell_bion_shop_clothes_bought", 1), Hide("shopscreen", transition=dissolve), Jump('howlersdell_bion_shop_clothes_about03')] text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Pay: [howlersdell_bion_shop_clothes_price1] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("A Fancy Robe"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/fancyclothes2idle.png":
                                xalign 0.5
                            text "Would make you look\nlike a merchant.\nTakes two days of work." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            hbox:
                                xalign 0.5
                                if coins >= howlersdell_bion_shop_clothes_price2:
                                    textbutton _("Pay: [howlersdell_bion_shop_clothes_price2] {image=coin}") action [SetVariable("howlersdell_bion_shop_clothes_daypickingup", (day+1)), SetVariable("coins", limit_coins(coins-howlersdell_bion_shop_clothes_price2)), SetVariable("quarters", quarters+4), SetVariable("howlersdell_bion_shop_clothes_bought", 2), Hide("shopscreen", transition=dissolve), Jump('howlersdell_bion_shop_clothes_about03')] text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Pay: [howlersdell_bion_shop_clothes_price2] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("A Fancy Dress"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/fancyclothes3idle.png":
                                xalign 0.5
                            text "Good for a socialite\nor a diplomat.\nTakes two days of work." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            hbox:
                                xalign 0.5
                                if coins >= howlersdell_bion_shop_clothes_price3:
                                    textbutton _("Pay: [howlersdell_bion_shop_clothes_price3] {image=coin}") action [SetVariable("howlersdell_bion_shop_clothes_daypickingup", (day+1)), SetVariable("coins", limit_coins(coins-howlersdell_bion_shop_clothes_price3)), SetVariable("quarters", quarters+4), SetVariable("howlersdell_bion_shop_clothes_bought", 3), Hide("shopscreen", transition=dissolve), Jump('howlersdell_bion_shop_clothes_about03')] text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Pay: [howlersdell_bion_shop_clothes_price3] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
    elif shop == "howlersstall":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('howlersdellstallafterinteraction')]
        $ akakios_shop_linen_price = (akakios_shop_linen_price_base+appearance_price)
        $ akakios_shop_axe_price = (akakios_shop_axe_price_base+appearance_price)
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('howlersdellstallafterinteraction')]
            frame:
                if (akakios_shop_snakebait and akakios_shop_lantern and akakios_shop_linen and akakios_shop_axe and akakios_quest_healingpotion_cangetback != 1) or (not akakios_shop_snakebait and not akakios_shop_snakebait_available and akakios_shop_lantern and akakios_shop_linen and akakios_shop_axe and akakios_quest_healingpotion_cangetback != 1):
                    yalign 0.0
                    vbox:
                        xalign .5
                        spacing 28
                        ypos 10
                        xmaximum 360
                        xminimum 360
                        yminimum 123
                        ymaximum 123
                        text "{color=#6a6a6a}Akakios has no other wares.{/color}" text_align 0.5 xmaximum 410 xminimum 410 xalign .5 yalign .5
                else:
                    vbox:
                        spacing 30
                        hbox:
                            spacing 0
                            xmaximum 1080
                            box_wrap True
                            box_wrap_spacing 30
                            if not akakios_shop_snakebait and akakios_shop_snakebait_available:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 340
                                    xminimum 340
                                    label _("Snake Bait"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/snakebaitidle.png":
                                        xalign 0.5
                                    text "A freshly picked\norange flower\nand leaves." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= 3:
                                            if pc_class != "scholar":
                                                textbutton _("Buy: 3 {image=coin}") action [SetVariable("item_snakebait", item_snakebait+1), SetVariable("coins", limit_coins(coins-3)), SetVariable("akakios_shop_snakebait", 1), Notify("You bought the snake bait.")] text_align 0.5 xalign .5
                                            if pc_class == "scholar":
                                                textbutton _("Buy: 3 {image=coin}") action [SetVariable("item_snakebait", item_snakebait+1), SetVariable("coins", limit_coins(coins-3)), SetVariable("akakios_shop_snakebait", 1), Notify("You added the snake bait to your bag of ingredients.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: 3 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                            if not akakios_shop_lantern:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 340
                                    xminimum 340
                                    label _("A Wooden Lantern"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/lanternidle.png":
                                        xalign 0.5
                                    text "Primitive,\nbut convenient." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if item_lantern:
                                            textbutton _("{color=#6a6a6a}You already\nown one{/color}") action NullAction() text_align 0.5 xalign .5
                                        elif coins >= akakios_shop_lantern_price_base:
                                            textbutton _("Buy: [akakios_shop_lantern_price_base] {image=coin}") action [SetVariable("item_lantern", 1), SetVariable("coins", limit_coins(coins-akakios_shop_lantern_price_base)), SetVariable("howlersdell_reputation_points", howlersdell_reputation_points+3), SetVariable("akakios_shop_lantern", 1), Notify("You bought a wooden lantern.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: [akakios_shop_lantern_price_base] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                            if not akakios_shop_linen:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 340
                                    xminimum 340
                                    label _("The Linen Fabric"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/linenidle.png":
                                        xalign 0.5
                                    text "A stack of linen sheets.\nA valuable commodity." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= akakios_shop_linen_price:
                                            textbutton _("Buy: [akakios_shop_linen_price] {image=coin}") action [SetVariable("item_linen", 1), SetVariable("coins", limit_coins(coins-akakios_shop_linen_price)), SetVariable("howlersdell_reputation", howlersdell_reputation+1), SetVariable("akakios_shop_linen", 1), Notify("You bought a pack of linen fabric.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: [akakios_shop_linen_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                            if not akakios_shop_axe:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 340
                                    xminimum 340
                                    label _("A New Battle Axe"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/axe03idle.png":
                                        xalign 0.5
                                    text "A light, sharp axe with\na head made of steel." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= akakios_shop_axe_price:
                                            textbutton _("Buy: [akakios_shop_axe_price] {image=coin}") action [SetVariable("item_axe03", 1), SetVariable("coins", limit_coins(coins-akakios_shop_axe_price)), SetVariable("howlersdell_reputation", howlersdell_reputation+1), SetVariable("akakios_shop_axe", 1), Notify("You bought the axe.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: [akakios_shop_axe_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                            if akakios_quest_healingpotion_cangetback == 1:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 340
                                    xminimum 340
                                    label _("A Healing Potion"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    if akakios_quest_healingpotion_generic:
                                        add "inventory/generichealingpotionidle.png":
                                            xalign 0.5
                                    else:
                                        add "inventory/potiondolmenidle.png":
                                            xalign 0.5
                                    text "The potion you\nsold to {color=#f6d6bd}Akakios{/color}." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= 5:
                                            if akakios_quest_healingpotion_generic:
                                                textbutton _("Buy: 5 {image=coin}") action [SetVariable("item_generichealingpotion", item_generichealingpotion+1), SetVariable("coins", limit_coins(coins-5)), SetVariable("akakios_quest_healingpotion_cangetback", 2), Notify("You bought the potion back.")] text_align 0.5 xalign .5
                                            else:
                                                textbutton _("Buy: 5 {image=coin}") action [SetVariable("item_potiondolmen", 1), SetVariable("coins", limit_coins(coins-5)), SetVariable("akakios_quest_healingpotion_cangetback", 2), Notify("You bought the potion back.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: 5 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
    elif shop == "howlersinn":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('howlersdellinnafterinteraction')]
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/foodrationsidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[item_rations]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[item_rations]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('howlersdellinnafterinteraction')]
            frame:
                vbox:
                    spacing 30
                    hbox:
                        spacing 0
                        xmaximum 1080
                        box_wrap True
                        box_wrap_spacing 30
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("Food Rations"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/foodrationsidle.png":
                                xalign 0.5
                            text "Two filling meals which\nwon’t spoil anytime soon.\n\n" text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            hbox:
                                xalign 0.5
                                if coins:
                                    textbutton _("Buy: 1 {image=coin}") action [SetVariable("quarters", quarters+1), SetVariable("coins", limit_coins(coins-1)), SetVariable("item_rations", item_rations+2), Notify("You bought two food rations.")] text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Buy: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        if not quest_ruins_choice == "thais_won" and not quest_ruins_choice == "thais_alliance_fail" and not thais_bigmad_beaten:
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                label _("Bath and Dinner"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/mealsidle.png":
                                    xalign 0.5
                                text "In an hour, you’ll get as much food as you can eat and a proper bath with laundry." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if pc_food < 4 or cleanliness < 3 or cleanliness_clothes_blood:
                                        if coins >= 2:
                                            textbutton _("Pay: 2 {image=coin}") action [Hide("shopscreen", transition=dissolve), Jump('howlersdellinnboughtbathanddinner')] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}You don’t need it{/color}") action NullAction() text_align 0.5 xalign .5
                        if not item_teethset:
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                label _("A Teeth-Cleaning Set"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/teethsetidle.png":
                                    xalign 0.5
                                text "A set to help you\nkeep your teeth clean.\n\n" text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if coins >= 3:
                                        textbutton _("Buy: 3 {image=coin}") action [SetVariable("coins", limit_coins(coins-3)), SetVariable("item_teethset", 1), Notify("You add the teeth-cleaning set to your travel equipment."), Hide("shopscreen", transition=dissolve), Jump('howlersdellinnboughttoothbrush')] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Buy: 3 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
    elif shop == "howlersdruids":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('howlersdelldruidsafterinteraction01')]
        if howlersdell_elpis_about_magicfruit_received or howlersdell_elpis_about_plague_cured:
            hbox:
                xalign 0.4615
                yalign 0.5
                vbox:
                    spacing -20
                    fixed:
                        maximum (102,121)
                        minimum (102,121)
                        imagebutton:
                            style "inventoryimage"
                            idle "inventory/howlersdelltokenidle.png"
                            action NullAction()
                    fixed:
                        maximum (102,121)
                        minimum (102,121)
                        imagebutton:
                            style "inventoryimage"
                            idle "gui/clossingarrowidle.png"
                            hover "gui/clossingarrowhover.png"
                            action [Hide("shopscreen", transition=dissolve), Jump('howlersdelldruidsafterinteraction01')]
                frame:
                    vbox:
                        #spacing 30
                        hbox:
                            spacing 0
                            xmaximum 1080
                            box_wrap True
                            box_wrap_spacing 30
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 440
                                xminimum 440
                                label _("A Healing Touch"):
                                    style "shop_prompt"
                                    xalign 0.5
                                vbox:
                                    yminimum 102
                                    xalign 0.5
                                    add "gui/statuspoints/hp/plus1hp.png":
                                        xalign 0.5
                                        yalign 0.5
                                text "Your shell will be strengthened\nby a {i}friendly spirit{/i}." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                if howlersdell_elpis_about_healing_limit < day:
                                    if pc_hp <= 1:
                                        textbutton _("Ask for healing") action [SetVariable("pc_hp", limit_pc_hp(pc_hp+1)), SetVariable("howlersdell_elpis_about_healing_limit", day), Notify("Your shell has been healed."), Hide("shopscreen", transition=dissolve), Jump('howlersdelldruidsafterinteraction01')] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}You don’t require\nany immediate help{/color}") action NullAction() text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}You’ve already been\nhealed today{/color}") action NullAction() text_align 0.5 xalign .5
        else:
            hbox:
                xalign 0.4615
                yalign 0.5
                vbox:
                    spacing -20
                    fixed:
                        maximum (102,121)
                        minimum (102,121)
                        imagebutton:
                            style "inventoryimage"
                            idle "inventory/howlersdelltokenidle.png"
                            action NullAction()
                    fixed:
                        maximum (102,121)
                        minimum (102,121)
                        imagebutton:
                            style "inventoryimage"
                            idle "gui/clossingarrowidle.png"
                            hover "gui/clossingarrowhover.png"
                            action [Hide("shopscreen", transition=dissolve), Jump('howlersdelldruidsafterinteraction01')]
                frame:
                    vbox:
                        #spacing 30
                        hbox:
                            spacing 0
                            xmaximum 1080
                            box_wrap True
                            box_wrap_spacing 30
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 440
                                xminimum 440
                                label _("A Healing Touch"):
                                    style "shop_prompt"
                                    xalign 0.5
                                vbox:
                                    yminimum 102
                                    xalign 0.5
                                    add "gui/statuspoints/hp/plus1hp.png":
                                        xalign 0.5
                                        yalign 0.5
                                text "Your shell will be strengthened\nby a {i}friendly spirit{/i}." text_align 0.5 xmaximum 410 xminimum 410 xalign .5
                                if howlersdell_elpis_about_healing_limit < day:
                                    if pc_hp <= 0:
                                        textbutton _("Ask for healing") action [SetVariable("pc_hp", limit_pc_hp(pc_hp+1)), SetVariable("howlersdell_elpis_about_healing_limit", day), Notify("Your shell has been healed."), Hide("shopscreen", transition=dissolve), Jump('howlersdelldruidsafterinteraction01')] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}You don’t require\nany immediate help{/color}") action NullAction() text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}You’ve already been\nhealed today{/color}") action NullAction() text_align 0.5 xalign .5

    elif shop == "foggylakefoggy":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('foggylakefoggyafterinteraction01')]
        $ foggy_shop_asterionscloak_price = (18-(foggy_friendship/4)+(appearance_price*2))
        if foggy_friendship < 10:
            if appearance_price == -2:
                $ foggy_shop_ironscraps_price = 5
            else:
                $ foggy_shop_ironscraps_price = 6
        else:
            if appearance_price == -2:
                $ foggy_shop_ironscraps_price = 4
            else:
                $ foggy_shop_ironscraps_price = 5
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('foggylakefoggyafterinteraction01')]
            frame:
                vbox:
                    spacing 30
                    hbox:
                        spacing 0
                        xmaximum 1080
                        box_wrap True
                        box_wrap_spacing 30
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("Fresh Meals"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/mealsidle.png":
                                xalign 0.5
                            if not foggy_food_meals_available_free:
                                if foggy_food_meals_available == 1:
                                    text "Four meals bought in advance.\nYou have 1 meal left." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                else:
                                    text "Four meals bought in advance.\nYou have [foggy_food_meals_available] meals left." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            else:
                                if foggy_food_meals_available == 1:
                                    text "Four meals bought in advance.\nYou have 1 meal left and can eat once a day for free." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                else:
                                    text "Four meals bought in advance.\nYou have [foggy_food_meals_available] meals left and can eat once a day for free." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            hbox:
                                xalign 0.5
                                if coins:
                                    textbutton _("Pay: 1 {image=coin}") action [SetVariable("coins", limit_coins(coins-1)), SetVariable("foggy_food_meals_available", foggy_food_meals_available+4), SetVariable("foggy_friendship_tradepoints", foggy_friendship_tradepoints+1), Notify("You’ve paid for four meals in advance.")] text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Pay: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        if not foggy_shop_ironscraps:
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                label _("The Iron Scraps"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/ironscrapsidle.png":
                                    xalign 0.5
                                text "A set of bits and pieces\nmade of iron and steel.\n" text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if coins >= foggy_shop_ironscraps_price:
                                        textbutton _("Buy: [foggy_shop_ironscraps_price] {image=coin}") action [SetVariable("item_ironscraps", item_ironscraps+1), SetVariable("coins", limit_coins(coins-foggy_shop_ironscraps_price)), SetVariable("foggy_friendship", foggy_friendship+1), SetVariable("foggy_shop_ironscraps", 1), Notify("You bought a set of iron scraps.")] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Buy: [foggy_shop_ironscraps_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        if foggy_shop_asterionscloak == 1: # foggy_shop_asterionscloak = 2 - sprzedane
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                label _("Asterion’s Cloak"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/asterioncloakidle.png":
                                    xalign 0.5
                                text "Its magic warms up the shell and helps to\nfall asleep in any conditions.\n" text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if coins >= foggy_shop_asterionscloak_price:
                                        textbutton _("Buy: [foggy_shop_asterionscloak_price] {image=coin}") action [SetVariable("item_asterioncloak", 1), SetVariable("coins", limit_coins(coins-foggy_shop_asterionscloak_price)), SetVariable("foggy_shop_asterionscloak", 2), SetVariable("foggy_friendship", foggy_friendship+3), Notify("You bought the magical cloak.")] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Buy: [foggy_shop_asterionscloak_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        if (foggy_shop_cidercask_returned and not foggy_shop_cidercask_bought) or (foggy_about_whitemarshes_cancelled and not foggy_shop_cidercask_bought):
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                label _("A Cask of Cider"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/cidercaskidle.png":
                                    xalign 0.5
                                text "A strong apple drink that\nwill spoil before winter.\n" text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if coins >= 4:
                                        textbutton _("Buy: 4 {image=coin}") action [SetVariable("item_cidercask", 1), SetVariable("coins", limit_coins(coins-4)), SetVariable("foggy_shop_cidercask_bought", 1), SetVariable("foggy_friendship_tradepoints", foggy_friendship_tradepoints+2), Notify("You bought the cider cask.")] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Buy: 4 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5

    elif shop == "creeksmerchant":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), SetVariable("custom5", "She cracks her knuckles."), Jump('creeksoldhavaafterinteraction01')]
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), SetVariable("custom5", "She cracks her knuckles."), Jump('creeksoldhavaafterinteraction01')]
            frame:
                vbox:
                    spacing 30
                    hbox:
                        spacing 0
                        xmaximum 1080
                        box_wrap True
                        box_wrap_spacing 30
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("A Fish Trap"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/fishtrapidle.png":
                                xalign 0.5
                            text "A basket made of vines\nand willow branches.\n\n" text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            hbox:
                                xalign 0.5
                                if not item_fishtrap:
                                    if coins >= 2:
                                        textbutton _("Buy: 2 {image=coin}") action [SetVariable("item_fishtrap", item_fishtrap+1), SetVariable("coins", limit_coins(coins-2)), SetVariable("oldhava_moneyspent", (oldhava_moneyspent+2)), Notify("You bought a fish trap.")] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Buy: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}You can carry only\none at a time{/color}") action NullAction() text_align 0.5 xalign .5
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("A Roast Chicken"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/chickenidle.png":
                                xalign 0.5
                            text "A spiced, whole meal\ncooked with care.\nYou currently have [item_chicken] of them." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            hbox:
                                xalign 0.5
                                if oldhava_about_chicken != day:
                                    if coins >= 1:
                                        textbutton _("Buy: 1 {image=coin}") action [SetVariable("item_chicken", (item_chicken+1)), SetVariable("coins", limit_coins(coins-1)), SetVariable("oldhava_moneyspent", (oldhava_moneyspent+1)), SetVariable("oldhava_about_chicken", day), Notify("You bought a roast chicken.")] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Buy: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}You can buy next\none tomorrow{/color}") action NullAction() text_align 0.5 xalign .5

    elif shop == "galerocksweaponsmith":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('galerocksweaponsmithafterinteraction')]
        if galerocks_reputation <= 5:
            if appearance_price != -2:
                $ galerocks_tatius_shop_shield_price = 4
            else:
                $ galerocks_tatius_shop_shield_price = 3
        else:
            if appearance_price != -2:
                $ galerocks_tatius_shop_shield_price = 3
            else:
                $ galerocks_tatius_shop_shield_price = 2
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('galerocksweaponsmithafterinteraction')]
            frame:
                if galerocks_tatius_shop_shield_bought and galerocks_tatius_shop_bolts:
                    yalign 0.0
                    vbox:
                        xalign .5
                        spacing 28
                        ypos 10
                        xmaximum 360
                        xminimum 360
                        yminimum 123
                        ymaximum 123
                        text "{color=#6a6a6a}Tatius has no other wares.{/color}" text_align 0.5 xmaximum 410 xminimum 410 xalign .5 yalign .5
                else:
                    vbox:
                        spacing 30
                        hbox:
                            spacing 0
                            xmaximum 1080
                            box_wrap True
                            box_wrap_spacing 30
                            if not galerocks_tatius_shop_shield_bought:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 360
                                    xminimum 360
                                    label _("A Shield"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/shield2idle.png":
                                        xalign 0.5
                                    text "You’re not used\nto using it in combat." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= galerocks_tatius_shop_shield_price and not item_shield:
                                            textbutton _("Buy: [galerocks_tatius_shop_shield_price] {image=coin}") action [SetVariable("item_shield", 2), SetVariable("coins", limit_coins(coins-galerocks_tatius_shop_shield_price)), SetVariable("galerocks_tatius_shop_shield_bought", day), Notify("You bought a shield.")] text_align 0.5 xalign .5
                                        elif item_shield:
                                            textbutton _("{color=#6a6a6a}You already\nown one{/color}") action NullAction() text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: [galerocks_tatius_shop_shield_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                            if not galerocks_tatius_shop_bolts:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 360
                                    xminimum 360
                                    label _("Quarrels"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/quarrelsidle.png":
                                        xalign 0.5
                                    text "A set of 5 arrows\nfor a crossbow." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= 2:
                                            textbutton _("Buy: 2 {image=coin}") action [SetVariable("item_crossbowquarrels", item_crossbowquarrels+5), SetVariable("coins", limit_coins(coins-2)), SetVariable("galerocks_tatius_shop_bolts", day), Notify("You bought a set of quarrels.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
    elif shop == "galerocksdinner":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('galerocksdinnerafterinteraction')]
        if galerocks_reputation <= 8 or appearance_price == -2:
            $ galerocks_porcia_wildplants_price = 3
        else:
            $ galerocks_porcia_wildplants_price = 2
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/foodrationsidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[item_rations]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[item_rations]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/wildplantsidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[item_wildplants]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[item_wildplants]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('galerocksdinnerafterinteraction')]
            frame:
                vbox:
                    spacing 30
                    hbox:
                        spacing 0
                        xmaximum 1080
                        box_wrap True
                        box_wrap_spacing 30
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("A Large Diner"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/mealsidle.png":
                                xalign 0.5
                            text "A fresh meal you’ll\neat on-site." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                if pc_food < 4:
                                    if galerocks_food_free:
                                        textbutton _("Pay: 0 {image=coin}") action [Hide("shopscreen", transition=dissolve), Jump('galerocksdinnerbuyingfoodfree')] text_align 0.5 xalign .5
                                    else:
                                        if quarters < (world_daylength-8):
                                            textbutton _("Work for 2 hours") action [Hide("shopscreen", transition=dissolve), Jump('galerocksdinnerbuyingfoodlabor')] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}It’s too late for work{/color}") action NullAction() text_align 0.5 xalign .5
                                        if coins:
                                            textbutton _("Pay: 1 {image=coin}") action [Hide("shopscreen", transition=dissolve), Jump('galerocksdinnerbuyingfoodmoney')] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}You need no food{/color}") action NullAction() text_align 0.5 xalign .5
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("A Food Ration"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/foodrationsidle.png":
                                xalign 0.5
                            text "A filling meal that\nwon’t spoil anytime soon." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                if item_wildplants >= galerocks_porcia_wildplants_price:
                                    if galerocks_porcia_wildplants_counter < 4:
                                        textbutton _("Barter: [galerocks_porcia_wildplants_price] bunches\nof wild plants") action [SetVariable("item_wildplants", item_wildplants-galerocks_porcia_wildplants_price), SetVariable("item_rations", item_rations+1), SetVariable("galerocks_porcia_wildplants_counter", galerocks_porcia_wildplants_counter+1), Notify("You bartered for a food ration.")] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("Barter: [galerocks_porcia_wildplants_price] bunches\nof wild plants") action [SetVariable("item_wildplants", item_wildplants-galerocks_porcia_wildplants_price), SetVariable("item_rations", item_rations+1), SetVariable("galerocks_porcia_wildplants_counter", galerocks_porcia_wildplants_counter-4), SetVariable("galerocks_work_hours", galerocks_work_hours+1), Notify("You bartered for a food ration.")] text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Barter: [galerocks_porcia_wildplants_price] bunches\nof wild plants{/color}") action NullAction() text_align 0.5 xalign .5
    elif shop == "galerocksbath":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('galerocksbathafterinteraction')]
        if galerocks_reputation < 4:
            $ galerocks_aquila_shop_perfume_price = 6
        elif galerocks_reputation < 8:
            $ galerocks_aquila_shop_perfume_price = 5
        else:
            $ galerocks_aquila_shop_perfume_price = 4
        if cleanliness_clothes_blood:
            if cleanliness <= 0:
                $ bath_estimateappearance = 4
            elif cleanliness == 1:
                $ bath_estimateappearance = 3
            elif cleanliness == 2:
                $ bath_estimateappearance = 2
            elif cleanliness == 3:
                $ bath_estimateappearance = 1
            elif cleanliness == 3:
                $ bath_estimateappearance = 0
        else:
            if cleanliness <= 0:
                $ bath_estimateappearance = 3
            elif cleanliness == 1:
                $ bath_estimateappearance = 2
            elif cleanliness == 2:
                $ bath_estimateappearance = 1
            else:
                $ bath_estimateappearance = 0
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('galerocksbathafterinteraction')]
            frame:
                vbox:
                    spacing 30
                    hbox:
                        spacing 0
                        xmaximum 1080
                        box_wrap True
                        box_wrap_spacing 30
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("Bath & Laundry"):
                                style "shop_prompt"
                                xalign 0.5
                            vbox:
                                yminimum 102
                                xalign 0.5
                                if bath_estimateappearance == 0:
                                    add "gui/statuspoints/appearance/plus0appearance.png":
                                        xalign 0.5
                                        yalign 0.5
                                elif bath_estimateappearance == 1:
                                    add "gui/statuspoints/appearance/plus1appearance.png":
                                        xalign 0.5
                                        yalign 0.5
                                elif bath_estimateappearance == 2:
                                    add "gui/statuspoints/appearance/plus2appearance.png":
                                        xalign 0.5
                                        yalign 0.5
                                elif bath_estimateappearance == 3:
                                    add "gui/statuspoints/appearance/plus3appearance.png":
                                        xalign 0.5
                                        yalign 0.5
                                elif bath_estimateappearance == 4:
                                    add "gui/statuspoints/appearance/plus4appearance.png":
                                        xalign 0.5
                                        yalign 0.5
                            text "You will be washed in\na tub filled with water.\n(Result depends on\ncharacter’s cleanliness.)" text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                            vbox:
                                xalign 0.5
                                if cleanliness < 3 or cleanliness_clothes_blood:
                                    if galerocks_bath_free:
                                        textbutton _("Pay: 0 {image=coin}") action [SetVariable("cleanliness", 1), SetVariable("cleanliness", limit_cleanliness(3)), SetVariable("cleanliness_clothes_blood", 0), Function(renpy.show, "plus4appearance", at_list=[appearancechange])] text_align 0.5 xalign .5
                                    else:
                                        if quarters < (world_daylength-2):
                                            textbutton _("Work for 2 hours") action [Function(renpy.show, "plus4appearance", at_list=[appearancechange]), SetVariable("quarters", quarters+8), SetVariable("galerocks_work_hours", galerocks_work_hours+2), SetVariable("cleanliness", limit_cleanliness(3)), SetVariable("cleanliness_clothes_blood", 0)] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}It’s too late for work{/color}") action NullAction() text_align 0.5 xalign .5
                                        if coins:
                                            textbutton _("Pay: 1 {image=coin}") action [Function(renpy.show, "plus4appearance", at_list=[appearancechange]), SetVariable("coins", limit_coins(coins-1)), SetVariable("cleanliness", limit_cleanliness(3)), SetVariable("cleanliness_clothes_blood", 0), Function(renpy.show, "plus4appearance", at_list=[appearancechange])] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}You don’t need\na bath{/color}") action NullAction() text_align 0.5 xalign .5
                        if not galerocks_aquila_shop_perfume_bought:
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                label _("A Bottle of Perfume"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/perfumeidle.png":
                                    xalign 0.5
                                text "Oil and other ingredients mixed\nwith thousands of flower petals." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if not item_perfume:
                                        if coins >= galerocks_aquila_shop_perfume_price:
                                            textbutton _("Buy: [galerocks_aquila_shop_perfume_price] {image=coin}") action [Hide("shopscreen", transition=dissolve), Jump('galerocksbathbuyingperfume')] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: [galerocks_aquila_shop_perfume_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}You already\nown one{/color}") action NullAction() text_align 0.5 xalign .5
    elif shop == "galerockstailor":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('galerockstailorafterinteraction')]
        if galerocks_reputation < 4:
            $ galerocks_rufina_shop_sewingkit_price = (5+appearance_price)
            $ galerocks_rufina_shop_repairset_price = (8+appearance_price)
        elif galerocks_reputation < 8:
            $ galerocks_rufina_shop_sewingkit_price = (4+appearance_price)
            $ galerocks_rufina_shop_repairset_price = (6+appearance_price)
        else:
            $ galerocks_rufina_shop_sewingkit_price = (4+appearance_price)
            $ galerocks_rufina_shop_repairset_price = (5+appearance_price)
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('galerockstailorafterinteraction')]
            frame:
                if quarters >= (world_daylength):
                    yalign 0.0
                    vbox:
                        xalign .5
                        spacing 28
                        ypos 10
                        xmaximum 360
                        xminimum 360
                        yminimum 123
                        ymaximum 123
                        text "{color=#6a6a6a}Rufina is closing her shop.{/color}" text_align 0.5 xmaximum 410 xminimum 410 xalign .5 yalign .5
                else:
                    vbox:
                        spacing 30
                        hbox:
                            spacing 0
                            xmaximum 1200
                            box_wrap True
                            box_wrap_spacing 30
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 400
                                xminimum 400
                                label _("Gambeson Repairs"):
                                    style "shop_prompt"
                                    xalign 0.5
                                if not armor:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/plus2armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "In 1h 30 min, your jacket will be partially resewn and repadded." text_align 0.5 xmaximum 400 xminimum 400 xalign .5
                                    if galerocks_armorer_free:
                                        textbutton _("Pay: 1/[galerocks_armorer_free] free repairs") action [SetVariable("galerocks_armorer_free", galerocks_armorer_free-1), SetVariable("armor", limit_armor(armor+2)), Function(renpy.show, "plus2armor", at_list=[armorchange]), SetVariable("quarters", quarters+6)] text_align 0.5 xalign .5
                                    else:
                                        if coins >= 2:
                                            textbutton _("Pay: 2 {image=coin}") action [SetVariable("armor", limit_armor(armor+2)), Function(renpy.show, "plus2armor", at_list=[armorchange]), SetVariable("coins", limit_coins(coins-2)), SetVariable("quarters", quarters+6)] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                if armor == 1:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/plus1armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "In one hour, your jacket will be partially resewn and repadded." text_align 0.5 xmaximum 400 xminimum 400 xalign .5
                                    if galerocks_armorer_free:
                                        textbutton _("Pay: 1/[galerocks_armorer_free] free repairs") action [SetVariable("galerocks_armorer_free", galerocks_armorer_free-1), SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("quarters", quarters+4)] text_align 0.5 xalign .5
                                    else:
                                        if coins >= 1:
                                            textbutton _("Pay: 1 {image=coin}") action [SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("coins", limit_coins(coins-1)), SetVariable("quarters", quarters+4)] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                if armor == 2:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/plus1armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "In one hour, your jacket will be carefully patched up." text_align 0.5 xmaximum 400 xminimum 400 xalign .5
                                    if galerocks_armorer_free:
                                        textbutton _("Pay: 1/[galerocks_armorer_free] free repairs") action [SetVariable("galerocks_armorer_free", galerocks_armorer_free-1), SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("quarters", quarters+4)] text_align 0.5 xalign .5
                                    else:
                                        if coins >= 1:
                                            textbutton _("Pay: 1 {image=coin}") action [SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("coins", limit_coins(coins-1)), SetVariable("quarters", quarters+4)] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                if armor == 3 and not armor_can4:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/3armormax.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "Your jacket is as good as this tailor can make it." text_align 0.5 xmaximum 400 xminimum 400 xalign .5
                                if armor == 3 and armor_can4:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/plus1armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "In an hour, your jacket will be precisely adjusted to your figure, making it easier to fight in it." text_align 0.5 xmaximum 400 xminimum 400 xalign .5
                                    if galerocks_armorer_free:
                                        textbutton _("Pay: 1/[galerocks_armorer_free] free repairs") action [SetVariable("galerocks_armorer_free", galerocks_armorer_free-1), SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("quarters", quarters+4)] text_align 0.5 xalign .5
                                    else:
                                        if coins >= 2:
                                            textbutton _("Pay: 2 {image=coin}") action [SetVariable("armor", limit_armor(armor+1)), Function(renpy.show, "plus1armor", at_list=[armorchange]), SetVariable("coins", limit_coins(coins-2)), SetVariable("quarters", quarters+4)] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Pay: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                if armor == 4:
                                    vbox:
                                        yminimum 102
                                        xalign 0.5
                                        add "gui/statuspoints/armor/4armor.png":
                                            xalign 0.5
                                            yalign 0.5
                                    text "Your jacket is\nas good as it can get." text_align 0.5 xmaximum 400 xminimum 400 xalign .5
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 400
                                xminimum 400
                                label _("Outfit Repairs"):
                                    style "shop_prompt"
                                    xalign 0.5
                                vbox:
                                    yminimum 102
                                    xalign 0.5
                                    add "gui/statuspoints/appearance/plus1appearance.png":
                                        xalign 0.5
                                        yalign 0.5
                                text "In 30 min, your clothes\nwill get patched and tidy." text_align 0.5 xmaximum 400 xminimum 400 xalign .5
                                hbox:
                                    xalign 0.5
                                    if cleanliness_clothes_torn:
                                        vbox:
                                            if quarters < (world_daylength-2):
                                                textbutton _("Work for 2 hours") action [SetVariable("cleanliness_clothes_torn", 0), Function(renpy.show, "plus1appearance", at_list=[appearancechange]), SetVariable("quarters", quarters+8), SetVariable("galerocks_work_hours", galerocks_work_hours+2)] text_align 0.5 xalign .5
                                            else:
                                                textbutton _("{color=#6a6a6a}It’s too late for work{/color}") action NullAction() text_align 0.5 xalign .5
                                            if coins >= 1:
                                                textbutton _("Pay: 1 {image=coin}") action [SetVariable("cleanliness_clothes_torn", 0), Function(renpy.show, "plus1appearance", at_list=[appearancechange]), SetVariable("coins", limit_coins(coins-1)), SetVariable("quarters", quarters+2)] text_align 0.5 xalign .5
                                            else:
                                                textbutton _("{color=#6a6a6a}Pay: 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Your outfit\nneeds no work{/color}") action NullAction() text_align 0.5 xalign .5
                            if not galerocks_rufina_shop_repairset_bought and not item_gambesonrepairset:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 400
                                    xminimum 400
                                    label _("A Gambeson Repair Set"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/gambesonrepairsetidle.png":
                                        xalign 0.5
                                    text "Everything you need to\nwork on your gambeson,\nwhat’s not an easy task." text_align 0.5 xmaximum 400 xminimum 400 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= galerocks_rufina_shop_repairset_price and not item_gambesonrepairset:
                                            textbutton _("Buy: [galerocks_rufina_shop_repairset_price] {image=coin}") action [SetVariable("item_gambesonrepairset", 1), SetVariable("coins", limit_coins(coins-galerocks_rufina_shop_repairset_price)), SetVariable("galerocks_rufina_shop_repairset_bought", day), Notify("You bought a repair set.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: [galerocks_rufina_shop_repairset_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                            if not galerocks_rufina_shop_sewingkit_bought and not item_sewingkit:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 400
                                    xminimum 400
                                    label _("A Sewing Kit"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/sewingkitidle.png":
                                        xalign 0.5
                                    text "Everything you need\nto patch your outfit\nwhen torn." text_align 0.5 xmaximum 400 xminimum 400 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= galerocks_rufina_shop_sewingkit_price and not item_sewingkit:
                                            textbutton _("Buy: [galerocks_rufina_shop_sewingkit_price] {image=coin}") action [SetVariable("item_sewingkit", 1), SetVariable("coins", limit_coins(coins-galerocks_rufina_shop_sewingkit_price)), SetVariable("galerocks_rufina_shop_sewingkit_bought", day), Notify("You bought a sewing kit.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: [galerocks_rufina_shop_sewingkit_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 400
                                xminimum 400
                                label _("A Winged Hourglass"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/wingedhourglassidle.png":
                                    xalign 0.5
                                text "A pendant showing\nloyalty to The Wright\nand their churches." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if galerocks_rufina_shop_hourglass_free:
                                        if not item_wingedhourglass:
                                            textbutton _("Buy: 0 {image=coin}") action [SetVariable("item_wingedhourglass", 1), SetVariable("item_wingedhourglass_worn", 0), SetVariable("galerocks_rufina_shop_hourglass_bought", day), Notify("You received a winged hourglass.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}You already\nown one{/color}") action NullAction() text_align 0.5 xalign .5
                                    else:
                                        if not item_wingedhourglass:
                                            if coins >= 2:
                                                textbutton _("Buy: 2 {image=coin}") action [SetVariable("item_wingedhourglass", 1), SetVariable("item_wingedhourglass_worn", 0), SetVariable("coins", limit_coins(coins-2)), SetVariable("galerocks_rufina_shop_hourglass_bought", day), Notify("You bought a winged hourglass.")] text_align 0.5 xalign .5
                                            else:
                                                textbutton _("{color=#6a6a6a}Buy: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}You already\nown one{/color}") action NullAction() text_align 0.5 xalign .5

    elif shop == "thyrsuswares":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('thyrsusafterinteraction01')]
        $ thyrsus_shop_witheringdust_price = (8+appearance_price)
        $ thyrsus_shop_powderedrock_price = (10+appearance_price)
        $ thyrsus_shop_ghoulblood_price = (8+appearance_price)
        if appearance_price != -2:
            $ thyrsus_shop_venom_price = 4
        else:
            $ thyrsus_shop_venom_price = 3
        $ thyrsus_estimate_wares = 0
        if not thyrsus_shop_bonehook and not item_bonehook:
            $ thyrsus_estimate_wares += 1
        if not thyrsus_shop_witheringdust and not item_witheringdust:
            $ thyrsus_estimate_wares += 1
        if not thyrsus_shop_stingointment and not item_stingointment:
            $ thyrsus_estimate_wares += 1
        if not thyrsus_shop_bugrepellent and not item_bugrepellent and not watchtower_tower_bugs_cleared:
            $ thyrsus_estimate_wares += 1
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('thyrsusafterinteraction01')]
            frame:
                if thyrsus_estimate_wares == 0:
                    yalign 0.0
                    vbox:
                        xalign .5
                        spacing 28
                        ypos 10
                        xmaximum 360
                        xminimum 360
                        yminimum 123
                        ymaximum 123
                        text "{color=#6a6a6a}Thyrsus has no other wares.{/color}" text_align 0.5 xmaximum 410 xminimum 410 xalign .5 yalign .5
                else:
                    vbox:
                        spacing 30
                        hbox:
                            spacing 0
                            xmaximum 1080
                            box_wrap True
                            box_wrap_spacing 30
                            if not thyrsus_shop_witheringdust and not item_witheringdust:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 360
                                    xminimum 360
                                    label _("The Withering Dust"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/witheringdustidle.png":
                                        xalign 0.5
                                    text "A poisonous, yellow dust\nthat “withers” the plants." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= thyrsus_shop_witheringdust_price:
                                            textbutton _("Buy: [thyrsus_shop_witheringdust_price] {image=coin}") action [SetVariable("item_witheringdust", 1), SetVariable("thyrsus_friendship", thyrsus_friendship+1), SetVariable("achievement_alchemy_witheringdust", 1), SetVariable("coins", limit_coins(coins-thyrsus_shop_witheringdust_price)), SetVariable("thyrsus_shop_witheringdust", day), Notify("You bought the withering dust.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: [thyrsus_shop_witheringdust_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                            if not thyrsus_shop_stingointment and not item_stingointment:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 360
                                    xminimum 360
                                    label _("The Sting Ointment"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/stingointmentidle.png":
                                        xalign 0.5
                                    text "A jar with an ointment that keeps insects away." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= 3:
                                            textbutton _("Buy: 3 {image=coin}") action [SetVariable("item_stingointment", 1), SetVariable("achievement_alchemy_stingointment", 1), SetVariable("coins", limit_coins(coins-3)), SetVariable("thyrsus_shop_stingointment", day), Notify("You bought the sting ointment.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: 3 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                            if not thyrsus_shop_bugrepellent and not item_bugrepellent and not watchtower_tower_bugs_cleared:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 360
                                    xminimum 360
                                    label _("The Herbal Bug Repellent"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/bugrepellentidle.png":
                                        xalign 0.5
                                    text "A jar with\na bug-killing ointment." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= thyrsus_shop_bugrepellent_price:
                                            textbutton _("Buy [thyrsus_shop_bugrepellent_price] {image=coin}") action [SetVariable("item_bugrepellent", 1), SetVariable("achievement_alchemy_bugrepellent", 1), SetVariable("coins", limit_coins(coins-thyrsus_shop_bugrepellent_price)), SetVariable("thyrsus_shop_bugrepellent", day), Notify("You bought a bug repellent.")] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: [thyrsus_shop_bugrepellent_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                            if not thyrsus_shop_bonehook and not item_bonehook:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 360
                                    xminimum 360
                                    label _("A Bone Hook"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/bonehookidle.png":
                                        xalign 0.5
                                    text "Three connected bones,\nmeant to be used as\na grappling hook." text_align 0.5 xmaximum 340 xminimum 340 xalign .5 # ropehook
                                    hbox:
                                        xalign 0.5
                                        if (thyrsus_friendship+appearance_charisma) < 5:
                                            if coins >= 3:
                                                textbutton _("Buy: 3 {image=coin}") action [SetVariable("item_bonehook", 1), SetVariable("thyrsus_friendship", thyrsus_friendship+1), SetVariable("coins", limit_coins(coins-3)), SetVariable("thyrsus_shop_bonehook", day), Notify("You bought a bone hook.")] text_align 0.5 xalign .5
                                            else:
                                                textbutton _("{color=#6a6a6a}Buy: 3 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                                        else:
                                            if coins >= 2:
                                                textbutton _("Buy: 2 {image=coin}") action [SetVariable("item_bonehook", 1), SetVariable("thyrsus_friendship", thyrsus_friendship+1), SetVariable("coins", limit_coins(coins-2)), SetVariable("thyrsus_shop_bonehook", day), Notify("You bought a bone hook.")] text_align 0.5 xalign .5
                                            else:
                                                textbutton _("{color=#6a6a6a}Buy: 2 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
    elif shop == "thyrsusingredients":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('thyrsusafterinteraction01')]
        $ thyrsus_shop_powderedrock_price = (10+appearance_price)
        $ thyrsus_shop_ghoulblood_price = (8+appearance_price)
        if appearance_price != -2:
            $ thyrsus_shop_venom_price = 4
        else:
            $ thyrsus_shop_venom_price = 3
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('thyrsusafterinteraction01')]
            frame:
                vbox:
                    spacing 30
                    vbox:
                        spacing 100
                        hbox:
                            xalign 0.0
                            spacing 80
                            vbox:
                                spacing 30
                                yalign 0.0
                                label _("An Ingredient"):
                                    style "shop_prompt"
                                    text_size 30
                                    xalign 0.5
                                hbox:
                                    ymaximum 50
                                    yminimum 50
                                    text "{color=#f6d6bd}Black Woundwort{/color}" text_align 0.0 xalign 0.0 yalign 0.5
                                hbox:
                                    ymaximum 50
                                    yminimum 50
                                    text "{color=#f6d6bd}Marshbules{/color}" text_align 0.0 xalign 0.0 yalign 0.5
                                if not thyrsus_shop_powderedrock and not item_powderedrock and not item_blindingpowder:
                                    hbox:
                                        ymaximum 50
                                        yminimum 50
                                        text "{color=#f6d6bd}Powdered Basalt{/color}" text_align 0.0 xalign 0.0 yalign 0.5
                            vbox:
                                spacing 30
                                yalign 0.0
                                label _("Useful for..."):
                                    style "shop_prompt"
                                    text_size 30
                                    xalign 0.5
                                hbox:
                                    ymaximum 50
                                    yminimum 50
                                    text "healing potions" text_align 0.0 xalign 0.0 yalign 0.5
                                hbox:
                                    ymaximum 50
                                    yminimum 50
                                    text "healing potions" text_align 0.0 xalign 0.0 yalign 0.5
                                if not thyrsus_shop_powderedrock and not item_powderedrock and not item_blindingpowder:
                                    hbox:
                                        ymaximum 50
                                        yminimum 50
                                        text "blinding powder" text_align 0.0 xalign 0.0 yalign 0.5
                            vbox:
                                spacing 30
                                yalign 0.0
                                label _("{image=coin} "):
                                    style "shop_prompt"
                                    text_size 30
                                    xalign 0.5
                                hbox:
                                    ymaximum 50
                                    yminimum 50
                                    xalign 0.5
                                    text "1" text_align 0.5 xalign 0.5 yalign 0.5
                                hbox:
                                    ymaximum 50
                                    yminimum 50
                                    xalign 0.5
                                    text "1" text_align 0.5 xalign 0.5 yalign 0.5
                                if not thyrsus_shop_powderedrock and not item_powderedrock and not item_blindingpowder:
                                    hbox:
                                        ymaximum 50
                                        yminimum 50
                                        xalign 0.5
                                        text "[thyrsus_shop_powderedrock_price]" text_align 0.5 xalign 0.5 yalign 0.5
                            vbox:
                                spacing 30
                                yalign 0.0
                                label _(" "):
                                    style "shop_prompt"
                                    text_size 30
                                    xalign 0.5
                                if not thyrsus_shop_blackwoundwort or thyrsus_shop_blackwoundwort < (day-1):
                                    hbox:
                                        ymaximum 50
                                        yminimum 50
                                        if coins >= 1:
                                            textbutton _("Buy") action [SetVariable("item_blackwoundwort", item_blackwoundwort+1), SetVariable("thyrsus_shop_blackwoundwort", day), SetVariable("coins", limit_coins(coins-1)), Notify("You bought the black woundwort.")] text_align 0.0 xalign 0.0 yalign 0.5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy{/color}") action NullAction() text_align 0.0 xalign 0.0 yalign 0.5
                                else:
                                    hbox:
                                        ymaximum 50
                                        yminimum 50
                                        textbutton _("{color=#6a6a6a}out of stock{/color}") action NullAction() text_align 0.0 xalign 0.0 yalign 0.5
                                if not thyrsus_shop_marshbules or thyrsus_shop_marshbules < (day-1):
                                    hbox:
                                        ymaximum 50
                                        yminimum 50
                                        if coins >= 1:
                                            textbutton _("Buy") action [SetVariable("item_marshbules", item_marshbules+1), SetVariable("thyrsus_shop_marshbules", day), SetVariable("coins", limit_coins(coins-1)), Notify("You bought the marshbules.")] text_align 0.0 xalign 0.0 yalign 0.5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy{/color}") action NullAction() text_align 0.0 xalign 0.0 yalign 0.5
                                else:
                                    hbox:
                                        ymaximum 50
                                        yminimum 50
                                        textbutton _("{color=#6a6a6a}out of stock{/color}") action NullAction() text_align 0.0 xalign 0.0 yalign 0.5
                                if not thyrsus_shop_powderedrock and not item_powderedrock and not item_blindingpowder:
                                    hbox:
                                        ymaximum 50
                                        yminimum 50
                                        if coins >= thyrsus_shop_powderedrock_price:
                                            textbutton _("Buy") action [SetVariable("item_powderedrock", item_powderedrock+1), SetVariable("thyrsus_friendship", thyrsus_friendship+1), SetVariable("thyrsus_shop_powderedrock", day), SetVariable("coins", limit_coins(coins-thyrsus_shop_powderedrock_price)), Notify("You bought the powdered basalt.")] text_align 0.0 xalign 0.0 yalign 0.0
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy{/color}") action NullAction() text_align 0.0 xalign 0.0 yalign 0.5

    elif shop == "glaucia":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('banditshideoutglauciaafterinteraction01')]
        $ glaucia_spices_price = (glaucia_spices_price_base-glaucia_friendship+appearance_price)
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("shopscreen", transition=dissolve), Jump('banditshideoutglauciaafterinteraction01')]
            frame:
                if glaucia_spices_bought or item_spices:
                    yalign 0.0
                    vbox:
                        xalign .5
                        spacing 28
                        ypos 10
                        xmaximum 360
                        xminimum 360
                        yminimum 123
                        ymaximum 123
                        text "{color=#6a6a6a}Glaucia has no other wares.{/color}" text_align 0.5 xmaximum 410 xminimum 410 xalign .5 yalign .5
                else:
                    vbox:
                        spacing 30
                        hbox:
                            spacing 0
                            xmaximum 1080
                            box_wrap True
                            box_wrap_spacing 30
                            if not glaucia_spices_bought and not item_spices:
                                vbox:
                                    xalign .5
                                    spacing 28
                                    xmaximum 360
                                    xminimum 360
                                    label _("The Sacks of Spices"):
                                        style "shop_prompt"
                                        xalign 0.5
                                    add "inventory/spicesidle.png":
                                        xalign 0.5
                                    text "Valuable ingredients that break the monotony of life." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                    hbox:
                                        xalign 0.5
                                        if coins >= glaucia_spices_price and not item_spices:
                                            textbutton _("Buy: [glaucia_spices_price] {image=coin}") action [SetVariable("item_spices", 1), SetVariable("coins", limit_coins(coins-glaucia_spices_price)), SetVariable("glaucia_friendship", glaucia_friendship+1), SetVariable("glaucia_questionstoday", glaucia_questionstoday+1), SetVariable("glaucia_spices_bought", day), Notify("You bought the spices."), Hide("shopscreen", transition=dissolve), Jump('banditshideoutglauciaafterinteraction01')] text_align 0.5 xalign .5
                                        else:
                                            textbutton _("{color=#6a6a6a}Buy: [glaucia_spices_price] {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5

    elif shop == "greenmountaintribechief":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('greenmountaintribechiefaftertrading01')]
        if item_axe02alt or item_axehead or item_axeset:
            $ thingstosell += 1
        if item_axe03:
            $ thingstosell += 1
        if item_cidercask:
            $ thingstosell += 1
        if item_ironingot:
            $ thingstosell += 1
        if item_sealskin:
            $ thingstosell += 1
        if item_spices:
            $ thingstosell += 1
        if item_beholderroot:
            $ thingstosell += 1
        hbox:
            xalign 0.4615
            yalign 0.5
            fixed:
                maximum (102,121)
                minimum (102,121)
                imagebutton:
                    style "inventoryimage"
                    idle "gui/clossingarrowidle.png"
                    hover "gui/clossingarrowhover.png"
                    action [Hide("shopscreen", transition=dissolve), Jump('greenmountaintribechiefaftertrading01')]
            frame:
                vbox:
                    spacing 30
                    hbox:
                        spacing 0
                        xmaximum 1080
                        box_wrap True
                        box_wrap_spacing 30
                        if not cephasgaiane_shop_dragonhorn and not item_dragonhorn:
                            vbox:
                                xalign .5
                                spacing 28
                                label _("The Dragon Horn"):
                                    style "shop_prompt"
                                    xalign 0.5
                                add "inventory/dragonhornidle.png":
                                    xalign 0.5
                                text "When blown, it imitates a roar of an enormous creature." text_align 0.5 xmaximum 340 xminimum 340 xalign .5
                                hbox:
                                    xalign 0.5
                                    if thingstosell:
                                        textbutton _("Barter") action [Hide("shopscreen", transition=dissolve), Jump('greenmountaintribechiefbarteringfordragonhorn01')] text_align 0.5 xalign .5
                                    else:
                                        textbutton _("{color=#6a6a6a}Barter{/color}") action NullAction() text_align 0.5 xalign .5
                        if not thingstosell:
                            textbutton _("{color=#6a6a6a}You have nothing\nthe tribe wants\nin return{/color}") action NullAction() text_align 0.5 xalign .5

    elif shop == "helvius":
        key "game_menu" action [Hide("shopscreen", transition=dissolve), Jump('whitemarshes_valens_aftertrading01')]
        hbox:
            xalign 0.4615
            yalign 0.5
            hbox:
                spacing 0
                vbox:
                    spacing -20
                    fixed:
                        maximum (102,121)
                        minimum (102,121)
                        imagebutton:
                            style "inventoryimage"
                            idle "inventory/coinscoupleidle.png"
                            action NullAction()
                        if persistent.textstyle == "basic":
                            text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        if persistent.textstyle == "pixel":
                            text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                    fixed:
                        maximum (102,121)
                        minimum (102,121)
                        imagebutton:
                            style "inventoryimage"
                            idle "inventory/foodrationsidle.png"
                            action NullAction()
                        if persistent.textstyle == "basic":
                            text "[item_rations]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        if persistent.textstyle == "pixel":
                            text "[item_rations]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                    fixed:
                        maximum (102,121)
                        minimum (102,121)
                        imagebutton:
                            style "inventoryimage"
                            idle "gui/clossingarrowidle.png"
                            hover "gui/clossingarrowhover.png"
                            action [Hide("shopscreen", transition=dissolve), Jump('whitemarshes_valens_aftertrading01')]
                vbox:
                    spacing -20
                    fixed:
                        maximum (102,121)
                        minimum (102,121)
                        imagebutton:
                            style "inventoryimage"
                            idle "inventory/wildplantsidle.png"
                            action NullAction()
                        if persistent.textstyle == "basic":
                            text "[item_wildplants]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        if persistent.textstyle == "pixel":
                            text "[item_wildplants]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                    fixed:
                        maximum (102,121)
                        minimum (102,121)
                        imagebutton:
                            style "inventoryimage"
                            idle "inventory/chickenidle.png"
                            action NullAction()
                        if persistent.textstyle == "basic":
                            text "[item_chicken]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        if persistent.textstyle == "pixel":
                            text "[item_chicken]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                    fixed:
                        maximum (102,121)
                        minimum (102,121)
                        imagebutton:
                            style "inventoryimage"
                            idle "inventory/cookedfishidle.png"
                            action NullAction()
                        if persistent.textstyle == "basic":
                            text "[item_cookedfish]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        if persistent.textstyle == "pixel":
                            text "[item_cookedfish]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
            frame:
                vbox:
                    spacing 30
                    hbox:
                        spacing 0
                        xmaximum 1080
                        box_wrap True
                        box_wrap_spacing 30
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("Food Rations"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/foodrationsidle.png":
                                xalign 0.5
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                if item_rations >= 3:
                                    textbutton _("Sell 3 rations\nfor 1 {image=coin}") action [SetVariable("item_rations", item_rations-3), SetVariable("coins", limit_coins(coins+1)), SetVariable("whitemarshes_valens_sellingpoints", whitemarshes_valens_sellingpoints+9), Notify("You sold 3 food rations.")] text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Sell 3 rations\nfor 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("Wild Plants"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/wildplantsidle.png":
                                xalign 0.5
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                if item_wildplants >= 8:
                                    textbutton _("Sell 8 bunches\nfor 1 {image=coin}") action [SetVariable("item_wildplants", item_wildplants-8), SetVariable("coins", limit_coins(coins+1)), SetVariable("whitemarshes_valens_sellingpoints", whitemarshes_valens_sellingpoints+8), Notify("You sold 8 bunches of wild plants.")] text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Sell 8 bunches\nfor 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                    hbox:
                        spacing 0
                        xmaximum 1080
                        box_wrap True
                        box_wrap_spacing 30
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("A Roast Chicken"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/chickenidle.png":
                                xalign 0.5
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                if item_chicken >= 1:
                                    textbutton _("Sell 1 chicken\nfor 1 {image=coin}") action [SetVariable("item_chicken", item_chicken-1), SetVariable("coins", limit_coins(coins+1)), SetVariable("whitemarshes_valens_sellingpoints", whitemarshes_valens_sellingpoints+5), Notify("You sold a roast chicken.")] text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Sell 1 chicken\nfor 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5
                        vbox:
                            xalign .5
                            spacing 28
                            xmaximum 360
                            xminimum 360
                            label _("Roast Fish"):
                                style "shop_prompt"
                                xalign 0.5
                            add "inventory/cookedfishidle.png":
                                xalign 0.5
                            vbox:
                                xalign .5
                                spacing 28
                                xmaximum 360
                                xminimum 360
                                if item_cookedfish >= 2:
                                    textbutton _("Sell 2 fish\nfor 1 {image=coin}") action [SetVariable("item_cookedfish", item_cookedfish-2), SetVariable("coins", limit_coins(coins+1)), SetVariable("whitemarshes_valens_sellingpoints", whitemarshes_valens_sellingpoints+4), Notify("You sold 2 roast fish.")] text_align 0.5 xalign .5
                                else:
                                    textbutton _("{color=#6a6a6a}Sell 2 fish\nfor 1 {image=coingray}{/color}") action NullAction() text_align 0.5 xalign .5

    else:
        frame:
            vbox:
                xalign .5
                yalign .5
                spacing 45
                text "You can’t currently use the shop."
                textbutton _("Return") action Hide("shopscreen", transition=dissolve) text_align 0.5 xalign .5 #transition=dissolve

style shop_frame is confirm_frame:
    xalign .5
    yalign .5
    xpadding 40
    ypadding 40
style shop_text is confirm_text:
    size 30
    color "#c3a38a"
style shop_prompt is confirm_prompt:
    xalign 0.5
style shop_prompt_text is confirm_prompt_text:
    color "#f6d6bd"
    xalign 0.5
    size 34
style shop_button_text is confirm_button_text:
    color "#997577"
    hover_color "#f6d6bd"
    size 30
    xalign 0.5
    text_align 0.5

################################### Selling
screen selling():
    zorder 170
    modal False
    style_prefix "shop"
    default tt = Tooltip("")
    vbox:
        ypos 81
        spacing 0
        ymaximum 930
        box_wrap True
        if thingstosell <= 9:
            xpos 587 # 689
        elif thingstosell <= 18:
            xpos 485
        elif thingstosell <= 27:
            xpos 383
        if shop == "peltnorth":
            if item_antlers:
                imagebutton:
                    idle "images/inventory/antlersidle.png"
                    hover "images/inventory/antlershover.png"
                    hovered tt.Action("A Set of Antlers")
                    action [tt.Action(""), Jump('peltnorth_sellingantlers')]
            if item_asterionbow:
                imagebutton:
                    idle "images/inventory/asterionbowidle.png"
                    hover "images/inventory/asterionbowhover.png"
                    hovered tt.Action("Asterion’s Bow")
                    action [tt.Action(""), Jump('peltnorth_sellingasterionbow')]
            if item_asterionwine and not item_asterionwine_pcknows_2:
                imagebutton:
                    idle "images/inventory/asterionwineidle.png"
                    hover "images/inventory/asterionwinehover.png"
                    hovered tt.Action("Asterion’s Wine")
                    action [tt.Action(""), Jump('peltnorth_sellingasterionwine01')]
            if item_boartusks:
                imagebutton:
                    idle "images/inventory/boartusksidle.png"
                    hover "images/inventory/boartuskshover.png"
                    hovered tt.Action("Boar Tusks")
                    action [tt.Action(""), Jump('peltnorth_sellingboartusks')]
            if item_axe02alt:
                imagebutton:
                    idle "images/inventory/axe02altidle.png"
                    hover "images/inventory/axe02althover.png"
                    hovered tt.Action("A Bronze Axe")
                    action [tt.Action(""), Jump('peltnorth_sellingaxe02alt')]
            if item_axehead or item_axeset:
                if item_axehead:
                    imagebutton:
                        idle "images/inventory/axeheadidle.png"
                        hover "images/inventory/axeheadhover.png"
                        hovered tt.Action("A Bronze Axe Head")
                        action [tt.Action(""), Jump('peltnorth_sellingaxehead')]
                if item_axeset:
                    imagebutton:
                        idle "images/inventory/axesetidle.png"
                        hover "images/inventory/axesethover.png"
                        hovered tt.Action("An Axe Head With A Handle")
                        action [tt.Action(""), Jump('peltnorth_sellingaxehead')]
            if item_brokenknife:
                imagebutton:
                    idle "images/inventory/brokenknifeidle.png"
                    hover "images/inventory/brokenknifehover.png"
                    hovered tt.Action("The Broken Knife")
                    action [tt.Action(""), Jump('peltnorth_sellingbrokenknife')]
            if item_cidercask:
                imagebutton:
                    idle "images/inventory/cidercaskidle.png"
                    hover "images/inventory/cidercaskhover.png"
                    hovered tt.Action("A Cask of Cider")
                    action [tt.Action(""), Jump('peltnorth_sellingcidercask')]
            if item_stoat:
                imagebutton:
                    idle "images/inventory/stoatidle.png"
                    hover "images/inventory/stoathover.png"
                    hovered tt.Action("A Dead Stoat")
                    action [tt.Action(""), Jump('peltnorth_sellingstoat')]
            if item_bonebuckle:
                imagebutton:
                    idle "images/inventory/bonebuckleidle.png"
                    hover "images/inventory/bonebucklehover.png"
                    hovered tt.Action("A Decorative Buckle")
                    action [tt.Action(""), Jump('peltnorth_sellingbonebuckle')]
            if item_generichealingpotion and not iason_shop_potions_block:
                imagebutton:
                    idle "images/inventory/generichealingpotionidle.png"
                    hover "images/inventory/generichealingpotionhover.png"
                    hovered tt.Action("A Fresh Healing Potion")
                    action [tt.Action(""), Jump('peltnorth_sellinggenerichealingpotion')]
            if item_griffonegg:
                imagebutton:
                    idle "images/inventory/griffoneggidle.png"
                    hover "images/inventory/griffonegghover.png"
                    hovered tt.Action("A Griffon Egg")
                    action [tt.Action(""), Jump('peltnorth_sellinggriffonegg')]
            if item_furlesswolftrophy:
                imagebutton:
                    idle "images/inventory/furlesswolftrophyidle.png"
                    hover "images/inventory/furlesswolftrophyhover.png"
                    hovered tt.Action("A Head of a Beast")
                    action [tt.Action(""), Jump('peltnorth_sellingfurlesswolftrophy')]
            if item_ironingot:
                imagebutton:
                    idle "images/inventory/ironingotidle.png"
                    hover "images/inventory/ironingothover.png"
                    hovered tt.Action("An Iron Ingot")
                    action [tt.Action(""), Jump('peltnorth_sellingironingot')]
            if item_ironscraps:
                imagebutton:
                    idle "images/inventory/ironscrapsidle.png"
                    hover "images/inventory/ironscrapshover.png"
                    hovered tt.Action("Iron Scraps")
                    action [tt.Action(""), Jump('peltnorth_sellingironscraps')]
            if item_asterionwine and item_asterionwine_pcknows_2 and not iason_shop_wine:
                imagebutton:
                    idle "images/inventory/asterionwineidle.png"
                    hover "images/inventory/asterionwinehover.png"
                    hovered tt.Action("Night’s Bane")
                    action [tt.Action(""), Jump('peltnorth_sellingasterionwine02')]
            if item_potiondolmen and item_potiondolmen_known and not iason_shop_potions_block:
                imagebutton:
                    idle "images/inventory/potiondolmenidle.png"
                    hover "images/inventory/potiondolmenhover.png"
                    hovered tt.Action("A Potion from the Dolmen")
                    action [tt.Action(""), Jump('peltnorth_sellingpotiondolmen')]
            if item_rawfishtotalnumber and not iason_about_fish:
                imagebutton:
                    idle "images/inventory/rawfishidle.png"
                    hover "images/inventory/rawfishhover.png"
                    hovered tt.Action("A Raw Fish")
                    action [tt.Action(""), Jump('peltnorth_sellingrawfish01')]
            if item_linen:
                imagebutton:
                    idle "images/inventory/linenidle.png"
                    hover "images/inventory/linenhover.png"
                    hovered tt.Action("A Stack of Linen Fabric")
                    action [tt.Action(""), Jump('peltnorth_sellinglinen')]
            if item_wingedhourglass and item_wingedhourglass_worn and not iason_shop_wingedhourglass_sold:
                imagebutton:
                    idle "images/inventory/wingedhourglassidle.png"
                    hover "images/inventory/wingedhourglasshover.png"
                    hovered tt.Action("A Winged Hourglass")
                    action [tt.Action(""), Jump('peltnorth_sellingwingedhourglass')]
        if shop == "howlersstall":
            if item_antlers:
                imagebutton:
                    idle "images/inventory/antlersidle.png"
                    hover "images/inventory/antlershover.png"
                    hovered tt.Action("A Set of Antlers")
                    action [tt.Action(""), Jump('howlersdellsellingantlers')]
            if item_asterionbow:
                imagebutton:
                    idle "images/inventory/asterionbowidle.png"
                    hover "images/inventory/asterionbowhover.png"
                    hovered tt.Action("Asterion’s Bow")
                    action [tt.Action(""), Jump('howlersdellsellingasterionbow')]
            if item_asterionwine and item_asterionwine_pcknows_1 and not item_asterionwine_pcknows_2 and not akakios_about_wine:
                imagebutton:
                    idle "images/inventory/asterionwineidle.png"
                    hover "images/inventory/asterionwinehover.png"
                    hovered tt.Action("Asterion’s Wine")
                    action [tt.Action(""), Jump('howlersdellsellingasterionwine')]
            if item_boartusks:
                imagebutton:
                    idle "images/inventory/boartusksidle.png"
                    hover "images/inventory/boartuskshover.png"
                    hovered tt.Action("Boar Tusks")
                    action [tt.Action(""), Jump('howlersdellsellingboartusks')]
            if item_boneearring:
                imagebutton:
                    idle "images/inventory/boneearringidle.png"
                    hover "images/inventory/boneearringhover.png"
                    hovered tt.Action("The Bone Earring")
                    action [tt.Action(""), Jump('howlersdellsellingboneearring')]
            if item_bonering:
                imagebutton:
                    idle "images/inventory/boneringidle.png"
                    hover "images/inventory/boneringhover.png"
                    hovered tt.Action("The Bone Ring")
                    action [tt.Action(""), Jump('howlersdellsellingbonering')]
            if item_axehead:
                imagebutton:
                    idle "images/inventory/axeheadidle.png"
                    hover "images/inventory/axeheadhover.png"
                    hovered tt.Action("A Bronze Axe Head")
                    action [tt.Action(""), Jump('howlersdellsellingaxehead')]
            if item_brokenknife:
                imagebutton:
                    idle "images/inventory/brokenknifeidle.png"
                    hover "images/inventory/brokenknifehover.png"
                    hovered tt.Action("The Broken Knife")
                    action [tt.Action(""), Jump('howlersdellsellingbrokenknife')]
            if item_cidercask:
                imagebutton:
                    idle "images/inventory/cidercaskidle.png"
                    hover "images/inventory/cidercaskhover.png"
                    hovered tt.Action("A Cask of Cider")
                    action [tt.Action(""), Jump('howlersdellsellingcidercask')]
            if item_stoat:
                imagebutton:
                    idle "images/inventory/stoatidle.png"
                    hover "images/inventory/stoathover.png"
                    hovered tt.Action("A Dead Stoat")
                    action [tt.Action(""), Jump('howlersdellsellingstoat')]
            if item_bonebuckle:
                imagebutton:
                    idle "images/inventory/bonebuckleidle.png"
                    hover "images/inventory/bonebucklehover.png"
                    hovered tt.Action("A Decorative Buckle")
                    action [tt.Action(""), Jump('howlersdellsellingbonebuckle')]
            if item_elkfur:
                imagebutton:
                    idle "images/inventory/fursidle.png"
                    hover "images/inventory/furshover.png"
                    hovered tt.Action("An Elk Fur")
                    action [tt.Action(""), Jump('howlersdellsellingelkfur')]
            if item_bronzerod:
                imagebutton:
                    idle "images/inventory/bronzerodidle.png"
                    hover "images/inventory/bronzerodhover.png"
                    hovered tt.Action("A Golem Rod")
                    action [tt.Action(""), Jump('howlersdellsellingbronzerod')]
            if item_griffonegg:
                imagebutton:
                    idle "images/inventory/griffoneggidle.png"
                    hover "images/inventory/griffonegghover.png"
                    hovered tt.Action("A Griffon Egg")
                    action [tt.Action(""), Jump('howlersdellsellinggriffonegg')]
            if item_harepelt:
                imagebutton:
                    idle "images/inventory/fursidle.png"
                    hover "images/inventory/furshover.png"
                    hovered tt.Action("A Hare Pelt")
                    action [tt.Action(""), Jump('howlersdellsellingharepelt')]
            if item_furlesswolftrophy:
                imagebutton:
                    idle "images/inventory/furlesswolftrophyidle.png"
                    hover "images/inventory/furlesswolftrophyhover.png"
                    hovered tt.Action("A Head of a Beast")
                    action [tt.Action(""), Jump('howlersdellsellingfurlesswolftrophy')]
            if item_ironingot:
                imagebutton:
                    idle "images/inventory/ironingotidle.png"
                    hover "images/inventory/ironingothover.png"
                    hovered tt.Action("An Iron Ingot")
                    action [tt.Action(""), Jump('howlersdellsellingironingot')]
            if item_ironscraps:
                imagebutton:
                    idle "images/inventory/ironscrapsidle.png"
                    hover "images/inventory/ironscrapshover.png"
                    hovered tt.Action("Iron Scraps")
                    action [tt.Action(""), Jump('howlersdellsellingironscraps')]
            if item_asterionwine and item_asterionwine_pcknows_2 and akakios_about_wine != 2:
                imagebutton:
                    idle "images/inventory/asterionwineidle.png"
                    hover "images/inventory/asterionwinehover.png"
                    hovered tt.Action("Night’s Bane")
                    action [tt.Action(""), Jump('howlersdellsellingasterionwine')]
            if item_peltnorthberryclaw:
                imagebutton:
                    idle "images/inventory/clawpeltnorthidle.png"
                    hover "images/inventory/clawpeltnorthhover.png"
                    hovered tt.Action("A Pebbler’s Claw")
                    action [tt.Action(""), Jump('howlersdellsellingpeltnorthberryclaw')]
            if item_rawfishtotalnumber and not akakios_about_fish:
                imagebutton:
                    idle "images/inventory/rawfishidle.png"
                    hover "images/inventory/rawfishhover.png"
                    hovered tt.Action("A Raw Fish")
                    action [tt.Action(""), Jump('howlersdellsellingrawfish')]
            if item_sealskin:
                imagebutton:
                    idle "images/inventory/fursidle.png"
                    hover "images/inventory/furshover.png"
                    hovered tt.Action("A Sealskin")
                    action [tt.Action(""), Jump('howlersdellsellingsealskin')]
            if item_dragonlingclaws:
                imagebutton:
                    idle "images/inventory/dragonlingclawsidle.png"
                    hover "images/inventory/dragonlingclawshover.png"
                    hovered tt.Action("A Set of Dragonling Claws")
                    action [tt.Action(""), Jump('howlersdellsellingdragonlingclaws')]
            if item_spidersilk and not akakios_about_spidersilk:
                imagebutton:
                    idle "images/inventory/spidersilkidle.png"
                    hover "images/inventory/spidersilkhover.png"
                    hovered tt.Action("Spider Silk")
                    action [tt.Action(""), Jump('howlersdellsellingspidersilk')]
            if item_letterwhitemarshes == 1:
                imagebutton:
                    idle "images/inventory/letterwhitemarshesidle.png"
                    hover "images/inventory/letterwhitemarsheshover.png"
                    hovered tt.Action("The Troll-Bone Tablet")
                    action [tt.Action(""), Jump('howlersdellsellingletterwhitemarshes')]
            if item_letterwhitemarshes == 2:
                imagebutton:
                    idle "images/inventory/letterwhitemarshes2idle.png"
                    hover "images/inventory/letterwhitemarshes2hover.png"
                    hovered tt.Action("The Troll-Bone Tablet")
                    action [tt.Action(""), Jump('howlersdellsellingletterwhitemarshes2')]
        if shop == "foggylakefoggy":
            if item_asterionbow:
                imagebutton:
                    idle "images/inventory/asterionbowidle.png"
                    hover "images/inventory/asterionbowhover.png"
                    hovered tt.Action("Asterion’s Bow")
                    action [tt.Action(""), Jump('foggylakesellingasterionbow')]
            if item_asterionspear:
                imagebutton:
                    idle "images/inventory/asterionspearidle.png"
                    hover "images/inventory/asterionspearhover.png"
                    hovered tt.Action("Asterion’s Spear")
                    action [tt.Action(""), Jump('foggylakesellingasterionspear')]
            if item_asterionwine and item_asterionwine_pcknows_1 and item_asterionwine_pcknows_2:
                imagebutton:
                    idle "images/inventory/asterionwineidle.png"
                    hover "images/inventory/asterionwinehover.png"
                    hovered tt.Action("Asterion’s Wine")
                    action [tt.Action(""), Jump('foggylakesellingasterionwine01')]
            if item_peltnorthberrytools:
                imagebutton:
                    idle "images/inventory/toolsberriesidle02.png"
                    hover "images/inventory/toolsberrieshover02.png"
                    hovered tt.Action("A Berry Picking Hook")
                    action [tt.Action(""), Jump('foggylakesellingpeltnorthberrytools')]
            if item_boartusks:
                imagebutton:
                    idle "images/inventory/boartusksidle.png"
                    hover "images/inventory/boartuskshover.png"
                    hovered tt.Action("Boar Tusks")
                    action [tt.Action(""), Jump('foggylakesellingboartusks')]
            if item_axe02alt:
                imagebutton:
                    idle "images/inventory/axe02altidle.png"
                    hover "images/inventory/axe02althover.png"
                    hovered tt.Action("A Bronze Axe")
                    action [tt.Action(""), Jump('foggylakesellingaxe02alt')]
            if item_axehead or item_axeset:
                if item_axehead:
                    imagebutton:
                        idle "images/inventory/axeheadidle.png"
                        hover "images/inventory/axeheadhover.png"
                        hovered tt.Action("A Bronze Axe Head")
                        action [tt.Action(""), Jump('foggylakesellingaxehead')]
                if item_axeset:
                    imagebutton:
                        idle "images/inventory/axesetidle.png"
                        hover "images/inventory/axesethover.png"
                        hovered tt.Action("An Axe Head With A Handle")
                        action [tt.Action(""), Jump('foggylakesellingaxehead')]
            if item_stoat:
                imagebutton:
                    idle "images/inventory/stoatidle.png"
                    hover "images/inventory/stoathover.png"
                    hovered tt.Action("A Dead Stoat")
                    action [tt.Action(""), Jump('foggylakesellingstoat')]
            if item_elkfur:
                imagebutton:
                    idle "images/inventory/fursidle.png"
                    hover "images/inventory/furshover.png"
                    hovered tt.Action("An Elk Fur")
                    action [tt.Action(""), Jump('foggylakesellingelkfur')]
            if item_goblinspear:
                imagebutton:
                    idle "images/inventory/goblinspearidle.png"
                    hover "images/inventory/goblinspearhover.png"
                    hovered tt.Action("A Goblin Spear")
                    action [tt.Action(""), Jump('foggylakesellinggoblinspear')]
            if item_griffonegg:
                imagebutton:
                    idle "images/inventory/griffoneggidle.png"
                    hover "images/inventory/griffonegghover.png"
                    hovered tt.Action("A Griffon Egg")
                    action [tt.Action(""), Jump('foggylakesellinggriffonegg')]
            if item_furlesswolftrophy:
                imagebutton:
                    idle "images/inventory/furlesswolftrophyidle.png"
                    hover "images/inventory/furlesswolftrophyhover.png"
                    hovered tt.Action("A Head of a Beast")
                    action [tt.Action(""), Jump('foggylakesellingfurlesswolftrophy')]
            if item_ironingot and not foggy_about_ironingot:
                imagebutton:
                    idle "images/inventory/ironingotidle.png"
                    hover "images/inventory/ironingothover.png"
                    hovered tt.Action("An Iron Ingot")
                    action [tt.Action(""), Jump('foggylakesellingfurlesswolfironingot')]
            if item_trollurine:
                imagebutton:
                    idle "images/inventory/goblinrepellentidle.png"
                    hover "images/inventory/goblinrepellenthover.png"
                    hovered tt.Action("A Jar Of Troll’s Urine")
                    action [tt.Action(""), Jump('foggylakesellingtrollurine')]
            if item_asterionwine and item_asterionwine_pcknows_1 and not item_asterionwine_pcknows_2:
                imagebutton:
                    idle "images/inventory/asterionwineidle.png"
                    hover "images/inventory/asterionwinehover.png"
                    hovered tt.Action("Night’s Bane")
                    action [tt.Action(""), Jump('foggylakesellingasterionwine02')]
            if item_peltnorthberryclaw:
                imagebutton:
                    idle "images/inventory/clawpeltnorthidle.png"
                    hover "images/inventory/clawpeltnorthhover.png"
                    hovered tt.Action("A Pebbler’s Claw")
                    action [tt.Action(""), Jump('foggylakesellingpeltnorthberryclaw')]
            if item_rawfishtotalnumber and not foggy_about_fish:
                imagebutton:
                    idle "images/inventory/rawfishidle.png"
                    hover "images/inventory/rawfishhover.png"
                    hovered tt.Action("A Raw Fish")
                    action [tt.Action(""), Jump('foggylakesellingrawfish')]
            if item_sealskin:
                imagebutton:
                    idle "images/inventory/fursidle.png"
                    hover "images/inventory/furshover.png"
                    hovered tt.Action("A Sealskin")
                    action [tt.Action(""), Jump('foggylakesellingsealskin')]
            if item_dragonlingclaws:
                imagebutton:
                    idle "images/inventory/dragonlingclawsidle.png"
                    hover "images/inventory/dragonlingclawshover.png"
                    hovered tt.Action("A Set of Dragonling Claws")
                    action [tt.Action(""), Jump('foggylakesellingdragonlingclaws')]
            if item_linen:
                imagebutton:
                    idle "images/inventory/linenidle.png"
                    hover "images/inventory/linenhover.png"
                    hovered tt.Action("A Stack of Linen Fabric")
                    action [tt.Action(""), Jump('foggylakesellinglinen')]
        if shop == "thyrsuswares" or shop == "thyrsusingredients":
            if item_asterioncloak:
                imagebutton:
                    idle "images/inventory/asterioncloakidle.png"
                    hover "images/inventory/asterioncloakhover.png"
                    hovered tt.Action("Asterion’s Cloak")
                    action [tt.Action(""), Jump('peatfieldsellingasterioncloak')]
            if item_ghoulblood:
                imagebutton:
                    idle "images/inventory/ghoulbloodidle.png"
                    hover "images/inventory/ghoulbloodhover.png"
                    hovered tt.Action("Corpse Eater’s Blood")
                    action [tt.Action(""), Jump('peatfieldsellingghoulblood')]
            if item_magicchisel == 1 and not thyrsus_about_magicchisel1:
                imagebutton:
                    idle "images/inventory/magicchiselidle.png"
                    hover "images/inventory/magicchiselhover.png"
                    hovered tt.Action("The Magic Chisel")
                    action [tt.Action(""), Jump('peatfieldsellingmagicchisel1')]
            if item_magicchisel == 2:
                imagebutton:
                    idle "images/inventory/magicchiselidle.png"
                    hover "images/inventory/magicchiselhover.png"
                    hovered tt.Action("The Tool of Destruction")
                    action [tt.Action(""), Jump('peatfieldsellingmagicchisel2')]
            # if item_trollurine:
            #     imagebutton:
            #         idle "images/inventory/goblinrepellentidle.png"
            #         hover "images/inventory/goblinrepellenthover.png"
            #         hovered tt.Action("A Jar Of Troll’s Urine")
            #         action [tt.Action(""), Jump('peatfieldsellingtrollurine')]
        if shop == "helvius":
            if item_ironscraps:
                imagebutton:
                    idle "images/inventory/ironscrapsidle.png"
                    hover "images/inventory/ironscrapshover.png"
                    hovered tt.Action("Iron Scraps")
                    action [tt.Action(""), Jump('whitemarshessellingironscraps')]
            if item_ironingot:
                imagebutton:
                    idle "images/inventory/ironingotidle.png"
                    hover "images/inventory/ironingothover.png"
                    hovered tt.Action("An Iron Ingot")
                    action [tt.Action(""), Jump('whitemarshessellingironingot')]
            if item_pileofbones:
                imagebutton:
                    idle "images/inventory/pileofbonesidle.png"
                    hover "images/inventory/pileofboneshover.png"
                    hovered tt.Action("The Human Bones")
                    action [tt.Action(""), Jump('whitemarshessellingpileofbones')]
            if item_crossbowquarrels:
                imagebutton:
                    idle "images/inventory/quarrelsidle.png"
                    hover "images/inventory/quarrelshover.png"
                    hovered tt.Action("The Quarrels")
                    action [tt.Action(""), Jump('whitemarshessellingquarrels')]
            if item_linen:
                imagebutton:
                    idle "images/inventory/linenidle.png"
                    hover "images/inventory/linenhover.png"
                    hovered tt.Action("A Stack of Linen Fabric")
                    action [tt.Action(""), Jump('whitemarshessellinglinen')]
            if item_beholderroot:
                imagebutton:
                    idle "images/inventory/beholderrootidle.png"
                    hover "images/inventory/beholderroothover.png"
                    hovered tt.Action("A Weird Root")
                    action [tt.Action(""), Jump('whitemarshessellingbeholderroot')]
        if shop == "greenmountaintribeentrance":
            if item_spices:
                imagebutton:
                    idle "images/inventory/spicesidle.png"
                    hover "images/inventory/spiceshover.png"
                    hovered tt.Action("The Sacks of Spices")
                    action [tt.Action(""), Jump('greenmountaintribeentrancesellingspices')]
            if item_asterioncloak:
                imagebutton:
                    idle "images/inventory/asterioncloakidle.png"
                    hover "images/inventory/asterioncloakhover.png"
                    hovered tt.Action("Asterion’s Cloak")
                    action [tt.Action(""), Jump('greenmountaintribeentrancesellingasterionscloak')]
            if item_axe02alt:
                imagebutton:
                    idle "images/inventory/axe02altidle.png"
                    hover "images/inventory/axe02althover.png"
                    hovered tt.Action("A Bronze Axe")
                    action [tt.Action(""), Jump('greenmountaintribeentrancesellingaxe02')]
            if item_axehead:
                imagebutton:
                    idle "images/inventory/axeheadidle.png"
                    hover "images/inventory/axeheadidle.png"
                    hovered tt.Action("A Bronze Axe Head")
                    action [tt.Action(""), Jump('greenmountaintribeentrancesellingaxe02')]
            if item_axeset:
                imagebutton:
                    idle "images/inventory/axesetidle.png"
                    hover "images/inventory/axesethover.png"
                    hovered tt.Action("An Axe Head With A Handle")
                    action [tt.Action(""), Jump('greenmountaintribeentrancesellingaxe02')]
            if item_axe03:
                imagebutton:
                    idle "images/inventory/axe03idle.png"
                    hover "images/inventory/axe03hover.png"
                    hovered tt.Action("A Brand-New Battle Axe")
                    action [tt.Action(""), Jump('greenmountaintribeentrancesellingaxe03')]
            if item_cidercask:
                imagebutton:
                    idle "images/inventory/cidercaskidle.png"
                    hover "images/inventory/cidercaskhover.png"
                    hovered tt.Action("A Cask of Cider")
                    action [tt.Action(""), Jump('greenmountaintribeentrancesellingcidercask')]
            if item_ironingot:
                imagebutton:
                    idle "images/inventory/ironingotidle.png"
                    hover "images/inventory/ironingothover.png"
                    hovered tt.Action("An Iron Ingot")
                    action [tt.Action(""), Jump('greenmountaintribeentrancesellingironingot')]
            if item_sealskin:
                imagebutton:
                    idle "images/inventory/fursidle.png"
                    hover "images/inventory/furshover.png"
                    hovered tt.Action("A Sealskin")
                    action [tt.Action(""), Jump('greenmountaintribeentrancesellingsealskin')]
            if item_beholderroot:
                imagebutton:
                    idle "images/inventory/beholderrootidle.png"
                    hover "images/inventory/beholderroothover.png"
                    hovered tt.Action("A Weird Root")
                    action [tt.Action(""), Jump('greenmountaintribeentrancesellingbeholderroot')]
        if shop == "greenmountaintribechief":
            if item_spices:
                imagebutton:
                    idle "images/inventory/spicesidle.png"
                    hover "images/inventory/spiceshover.png"
                    hovered tt.Action("The Sacks of Spices")
                    action [tt.Action(""), Jump('greenmountaintribechiefssellingspices')]
            if item_asterioncloak:
                imagebutton:
                    idle "images/inventory/asterioncloakidle.png"
                    hover "images/inventory/asterioncloakhover.png"
                    hovered tt.Action("Asterion’s Cloak")
                    action [tt.Action(""), Jump('greenmountaintribechiefssellingasterionscloak')]
            if item_axe02alt:
                imagebutton:
                    idle "images/inventory/axe02altidle.png"
                    hover "images/inventory/axe02althover.png"
                    hovered tt.Action("A Bronze Axe")
                    action [tt.Action(""), Jump('greenmountaintribechiefsellingaxe02')]
            if item_axehead:
                imagebutton:
                    idle "images/inventory/axeheadidle.png"
                    hover "images/inventory/axeheadidle.png"
                    hovered tt.Action("A Bronze Axe Head")
                    action [tt.Action(""), Jump('greenmountaintribechiefsellingaxe02')]
            if item_axeset:
                imagebutton:
                    idle "images/inventory/axesetidle.png"
                    hover "images/inventory/axesethover.png"
                    hovered tt.Action("An Axe Head With A Handle")
                    action [tt.Action(""), Jump('greenmountaintribechiefsellingaxe02')]
            if item_axe03:
                imagebutton:
                    idle "images/inventory/axe03idle.png"
                    hover "images/inventory/axe03hover.png"
                    hovered tt.Action("A Brand-New Battle Axe")
                    action [tt.Action(""), Jump('greenmountaintribechiefsellingaxe03')]
            if item_cidercask:
                imagebutton:
                    idle "images/inventory/cidercaskidle.png"
                    hover "images/inventory/cidercaskhover.png"
                    hovered tt.Action("A Cask of Cider")
                    action [tt.Action(""), Jump('greenmountaintribechiefsellingcidercask')]
            if item_ironingot:
                imagebutton:
                    idle "images/inventory/ironingotidle.png"
                    hover "images/inventory/ironingothover.png"
                    hovered tt.Action("An Iron Ingot")
                    action [tt.Action(""), Jump('greenmountaintribechiefsellingironingot')]
            if item_sealskin:
                imagebutton:
                    idle "images/inventory/fursidle.png"
                    hover "images/inventory/furshover.png"
                    hovered tt.Action("A Sealskin")
                    action [tt.Action(""), Jump('greenmountaintribechiefsellingsealskin')]
            if item_beholderroot:
                imagebutton:
                    idle "images/inventory/beholderrootidle.png"
                    hover "images/inventory/beholderroothover.png"
                    hovered tt.Action("A Weird Root")
                    action [tt.Action(""), Jump('greenmountaintribechiefsellingbeholderroot')]
            # if item_ITEMNAME:
            #     imagebutton:
            #         idle "images/inventory/ITENMNAMEidle.png"
            #         hover "images/inventory/ITENMNAMEhover.png"
            #         hovered tt.Action("NAME")
            #         action [tt.Action(""), Jump('peltnorth_sellingNAME')]
    if tt.value != "":
        frame:
            xpadding 20
            ypadding 20
            xalign 0.0
            pos renpy.get_mouse_pos()
            xpos 689
            if persistent.textstyle == "basic":
                text tt.value text_align 0.5 font "philosopher.ttf"
            if persistent.textstyle == "pixel":
                text tt.value text_align 0.5 font "munro.ttf"

default mundanejob_labelname = ""
default mundanejob_fluff = ""
default mundanejob_fluff2 = ""
screen mundanejob():
    zorder 200
    modal True
    style_prefix "shop"
    add "gui/overlay/confirm.png"
    if pc_area == "creeks":
        key "game_menu" action [Hide("mundanejob", transition=dissolve)]
        if creeks_mundanework_numberoftimes == 0:
            $ mundanejob_labelname = "A Big Delivery"
            $ mundanejob_fluff = "The villagers need to deliver a few barrels to Foggy and stay around for a few hours to set up traps and repair a collapsed part of the palisade."
        elif creeks_mundanework_numberoftimes == 1:
            $ mundanejob_labelname = "Exploration"
            $ mundanejob_fluff = "A few hunters would like to get to know the gargoyle-infested forest that grows nearby."
        elif creeks_mundanework_numberoftimes == 2:
            $ mundanejob_labelname = "Adventurous Foragers"
            $ mundanejob_fluff = "The locals would like to search for food in an area they haven’t entered in a few years, ever since the last dragonling attack."
        elif creeks_mundanework_numberoftimes == 3:
            $ mundanejob_labelname = "A Hunting Trip"
            $ mundanejob_fluff = "The hunters could use an extra blade, especially if they were to get hemmed while returning with their prey - or a wounded team member."
        elif creeks_mundanework_numberoftimes == 4:
            $ mundanejob_labelname = "The Missing Ingredient"
            $ mundanejob_fluff = "A beast stole the entire supply of a rare herb growing at the clearing behind the village. You’re asked to find some seedlings in the distant forest."
        elif creeks_mundanework_numberoftimes == 5:
            $ mundanejob_labelname = "A Wolf Pack"
            $ mundanejob_fluff = "The hunters need to scare away a pack of gray wolves before they get used to this area."
        elif creeks_mundanework_numberoftimes == 6:
            $ mundanejob_labelname = "Guard"
            $ mundanejob_fluff = "An ambitious villager would like to visit another settlement."
        elif creeks_mundanework_numberoftimes == 7:
            $ mundanejob_labelname = "A Day-Long Patrol"
            $ mundanejob_fluff = "You’re asked to spend an entire day in the saddle and estimate how safe it would be to cross the northern and eastern road on foot."
        else:
            $ mundanejob_labelname = "Just In Case"
            $ mundanejob_fluff = "The locals hope to spend a few hours moving things between Creeks and Foggy Lake and preparing for autumn."
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("mundanejob", transition=dissolve)]
            frame:
                vbox:
                    xalign .5
                    spacing 28
                    xmaximum 520
                    xminimum 520
                    label _("[mundanejob_labelname]"):
                        style "shop_prompt"
                        xalign 0.5
                    text "[mundanejob_fluff]\n\nThis task will take you an entire day, and may get dangerous." text_align 0.5 xmaximum 420 xminimum 420 xalign .5
                    hbox:
                        spacing 0
                        xalign 0.5
                        #xminimum 520
                        xmaximum 520
                        yalign 0.0
                        add "gui/statuspoints/hp/minusquestionmarkhp.png":
                            xalign 0.5
                        add "gui/statuspoints/appearance/minusquestionmarkappearance.png":
                            xalign 0.5
                        add "gui/statuspoints/food/plus2food.png":
                            xalign 0.5
                    hbox:
                        xalign 0.5
                        textbutton _("Work for [creeks_mundanework_payment] {image=coin}") action [Hide("mundanejob", transition=dissolve), Jump('creeksaftermundanejob')] text_align 0.5 xalign .5
    elif pc_area == "beach" or pc_area == "galerocks":
        key "game_menu" action [Hide("mundanejob", transition=dissolve)]
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("mundanejob", transition=dissolve)]
            frame:
                vbox:
                    xalign .5
                    spacing 28
                    xmaximum 520
                    xminimum 520
                    label _("Securing The Coast"):
                        style "shop_prompt"
                        xalign 0.5
                    text "You’ll keep an eye on the caught fish, equipment, and resting fishers.\n\nThis task will take you an entire day, and may get dangerous, but if so, you’ll get an extra dragon bone." text_align 0.5 xmaximum 420 xminimum 420 xalign .5
                    hbox:
                        spacing 0
                        xalign 0.5
                        #xminimum 520
                        xmaximum 520
                        yalign 0.0
                        add "gui/statuspoints/hp/minusquestionmarkhp.png":
                            xalign 0.5
                        add "gui/statuspoints/appearance/minusquestionmarkappearance.png":
                            xalign 0.5
                        add "gui/statuspoints/food/plus2food.png":
                            xalign 0.5
                    hbox:
                        xalign 0.5
                        textbutton _("Work for 2 or 3 {image=coin}") action [Hide("mundanejob", transition=dissolve), Jump('galerocksphotiosaftermundanejob01')] text_align 0.5 xalign .5
    elif pc_area == "howlersdell":
        key "game_menu" action [Hide("mundanejob", transition=dissolve)]
        if howlersdell_mundanework_type == "elpis":
            $ mundanejob_labelname = "Favor for Elpis"
            $ mundanejob_fluff = "You are to head into the forest garden and assist one of the druids. Who knows what for."
        elif howlersdell_mundanework_type == "herbalists":
            $ mundanejob_labelname = "A Search for Herbs"
            $ mundanejob_fluff = "You’ll join a group of guards and druids in their search for useful herbs, ready to carry the elders on your palfrey to safety, if needed."
        elif howlersdell_mundanework_type == "hunters":
            $ mundanejob_labelname = "A Hunting Trip"
            $ mundanejob_fluff = "You’ll be a messenger between a few groups of hunters that will hide in various parts of the wetlands, close to the southern road."
        elif howlersdell_mundanework_type == "pathclearing":
            $ mundanejob_labelname = "Clearing The Paths"
            $ mundanejob_fluff = "You’ll join a group of guards and workers that are meant to remove branches and other obstacles. You’ll keep them in touch with the village."
        elif howlersdell_mundanework_type == "farmers":
            $ mundanejob_labelname = "Securing The Fields"
            $ mundanejob_fluff = "An edge of the local fields was destroyed by some beasts. You’ll stay in the saddle, helping the guards and workers oversee the area while they’re placing a new fence."
        elif howlersdell_mundanework_type == "lumberjacks":
            $ mundanejob_labelname = "Escorting The Foragers"
            $ mundanejob_fluff = "A group of workers is going to explore the forest garden, seeking wood and mushrooms. You’ll ride ahead, looking out for threats."
        elif howlersdell_mundanework_type == "fishers":
            $ mundanejob_labelname = "Patrol To The Coast"
            $ mundanejob_fluff = "Now that the road to the coast is clear, you’re asked to make sure it’s somewhat safe."
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                spacing -20
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "inventory/coinscoupleidle.png"
                        action NullAction()
                    if persistent.textstyle == "basic":
                        text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                    if persistent.textstyle == "pixel":
                        text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,121)
                    minimum (102,121)
                    imagebutton:
                        style "inventoryimage"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action [Hide("mundanejob", transition=dissolve)]
            frame:
                vbox:
                    xalign .5
                    spacing 28
                    xmaximum 520
                    xminimum 520
                    label _("[mundanejob_labelname]"):
                        style "shop_prompt"
                        xalign 0.5
                    if howlersdell_mundanework_type == "elpis":
                        text "[mundanejob_fluff]\n\nThis task will take you a few hours, if not more." text_align 0.5 xmaximum 420 xminimum 420 xalign .5
                    else:
                        text "[mundanejob_fluff]\n\nThis task will take you about half a day and may get dangerous." text_align 0.5 xmaximum 420 xminimum 420 xalign .5
                    hbox:
                        spacing 0
                        xalign 0.5
                        #xminimum 520
                        xmaximum 520
                        yalign 0.0
                        add "gui/statuspoints/hp/minusquestionmarkhp.png":
                            xalign 0.5
                        add "gui/statuspoints/appearance/minusquestionmarkappearance.png":
                            xalign 0.5
                    hbox:
                        xalign 0.5
                        if howlersdell_mundanework_type == "elpis":
                            textbutton _("Work for Elpis") action [Hide("mundanejob", transition=dissolve), Jump('howlersdell_mundanework_elpis')] text_align 0.5 xalign .5
                        else:
                            textbutton _("Work for [howlersdell_mundanework_payment_total] {image=coin}") action [Hide("mundanejob", transition=dissolve), Jump('howlersdell_mundanework02')] text_align 0.5 xalign .5
    else:
        frame:
            vbox:
                xalign .5
                yalign .5
                spacing 45
                text "You can’t currently work."
                textbutton _("Return") action Hide("shopscreen", transition=dissolve) text_align 0.5 xalign .5
