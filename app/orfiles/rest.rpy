## Initialization

init offset = -1

######### REST
screen restscreen():
    zorder 200
    modal True
    default tt = Tooltip("")
    style_prefix "resting"
    key "r" action [Hide('restscreen'), With(dissolve)]
    key "R" action [Hide('restscreen'), With(dissolve)]
    if pc_class != "mage":
        if pc_hp != 5:
            add "gui/overlay/confirmrest.png"
        else:
            add "gui/overlay/confirmrest2.png"
    else:
        if pc_hp != 5:
            add "gui/overlay/confirmrestmage.png"
        else:
            add "gui/overlay/confirmrestmage2.png"
    if (quarters < 36 and pc_area != "howlersdell") or (quarters < 40 and pc_area == "howlersdell"):
        hbox:
            xalign 1.0
            xpos 1526
            yalign 0.5
            vbox:
                fixed:
                    maximum (102,102)
                    minimum (102,102)
                    style "inventoryimage2"
                    if pc_area == "howlersdell" and item_howlersdelltoken:
                        imagebutton:
                            # style "inventoryimage2"
                            idle "inventory/howlersdelltokenidle.png"
                            action NullAction()
                    else:
                        imagebutton:
                            # style "inventoryimage2"
                            idle "inventory/coinscoupleidle.png"
                            action NullAction()
                        if persistent.textstyle == "basic":
                            text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        if persistent.textstyle == "pixel":
                            text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,102)
                    minimum (102,102)
                    style "inventoryimage2"
                    imagebutton:
                        if pc_food < 2:
                            if item_rations:
                                idle "images/inventory/foodrationsidle.png"
                                hover "images/inventory/foodrationshover.png"
                                hovered tt.Action("Eat a food ration")
                                action [SetVariable("item_rations", item_rations-1), SetVariable("pc_food", limit_pc_food(pc_food+2))]
                            else:
                                idle "images/inventory/foodrationslockedidle.png"
                                hover "images/inventory/foodrationslockedhover.png"
                                hovered tt.Action("You have no\nrations left")
                                action NullAction()
                        else:
                            idle "images/inventory/foodrationslockedidle.png"
                            hover "images/inventory/foodrationslockedhover.png"
                            hovered tt.Action("You don’t need\nto eat now")
                            action NullAction()
                    if pc_food < 2 and item_rations:
                        if persistent.textstyle == "basic":
                            text "[item_rations]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        if persistent.textstyle == "pixel":
                            text "[item_rations]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                    else:
                        if persistent.textstyle == "basic":
                            text "{color=#6a6a6a}[item_rations]{/color}" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        if persistent.textstyle == "pixel":
                            text "{color=#6a6a6a}[item_rations]{/color}" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,102)
                    minimum (102,102)
                    imagebutton:
                        style "inventoryimage2"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action Hide("restscreen", transition=dissolve)
            frame:
                vbox:
                    spacing 25
                    if pc_area == "peltnorth":
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                label _("Resting at the inn"):
                                    style "resting_prompt"
                                    yalign 0.0
                                text "You’ll spend the entire day taking care of smaller chores and allowing your shell and soul to rest." xmaximum 600 yalign 0.0
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                hbox:
                                    spacing 0
                                    xalign 0.5
                                    #xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    if pc_class == "mage":
                                        add "gui/statuspoints/hp/plus1hp.png":
                                            xalign 0.5
                                        add "gui/statuspoints/mana/plus3mana.png":
                                            xalign 0.5
                                    else:
                                        add "gui/statuspoints/hp/plus1hp.png":
                                            xalign 0.5
                                if pc_food >= 2:
                                    textbutton _("Rest") action [SetVariable("sleep_destination", "peltnorthafterrelaxing"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                else:
                                    textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                    elif pc_area == "foggylake":
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                label _("Resting at the tavern"):
                                    style "resting_prompt"
                                    yalign 0.0
                                text "You’ll spend the entire day taking care of smaller chores and allowing your shell and soul to rest." xmaximum 600 yalign 0.0
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                hbox:
                                    spacing 0
                                    xalign 0.5
                                    #xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    if pc_class == "mage":
                                        add "gui/statuspoints/hp/plus1hp.png":
                                            xalign 0.5
                                        add "gui/statuspoints/mana/plus3mana.png":
                                            xalign 0.5
                                    else:
                                        add "gui/statuspoints/hp/plus1hp.png":
                                            xalign 0.5
                                if pc_food >= 2:
                                    textbutton _("Rest") action [SetVariable("sleep_destination", "foggylakeafterrelaxing"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                else:
                                    textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                    elif pc_area == "howlersdell":
                        hbox:
                            spacing 80
                            if not item_howlersdelltoken:
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("Resting in\nthe village"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    text "You’ll spend the entire day taking care of smaller chores and allowing your shell and soul to rest." xmaximum 600 yalign 0.0
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                label _("Resting at\nthe inn"):
                                    style "resting_prompt"
                                    yalign 0.0
                                text "The staff will take care of all your chores\nand you’ll receive a fancy meal." xmaximum 600 yalign 0.0
                        hbox:
                            spacing 80
                            if not item_howlersdelltoken:
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        if pc_class == "mage":
                                            add "gui/statuspoints/hp/plus1hp.png":
                                                xalign 0.5
                                            add "gui/statuspoints/mana/plus3mana.png":
                                                xalign 0.5
                                        else:
                                            add "gui/statuspoints/hp/plus1hp.png":
                                                xalign 0.5
                                    if pc_food >= 2:
                                        textbutton _("Rest: 0 {image=coin}") action [SetVariable("sleep_destination", "howlersdellafterrelaxing"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                    else:
                                        textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                hbox:
                                    spacing 0
                                    xalign 0.5
                                    #xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    if pc_class == "mage":
                                        add "gui/statuspoints/hp/plus2hp.png":
                                            xalign 0.5
                                        add "gui/statuspoints/mana/plus4mana.png":
                                            xalign 0.5
                                    else:
                                        add "gui/statuspoints/hp/plus2hp.png":
                                            xalign 0.5
                                    add "gui/statuspoints/food/plus3food.png":
                                        xalign 0.5
                                if item_howlersdelltoken:
                                    textbutton _("Rest: 0 {image=coin}") action [SetVariable("sleep_destination", "howlersdellafterrelaxingpremium"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                elif coins >= 2:
                                    textbutton _("Rest: 2 {image=coin}") action [SetVariable("coins", limit_coins(coins-2)), SetVariable("sleep_destination", "howlersdellafterrelaxingpremium"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                else:
                                    textbutton _("{color=#6a6a6a}Rest: 2 {image=coingray}{/color}") action NullAction() yalign 1.0 xalign 0.5
                    else:
                        frame:
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 45
                                text "You can’t rest right now." xmaximum 600
                                hbox:
                                    xalign 0.5
                                    spacing 150
                                    textbutton _("Return") action Hide("restscreen", transition=dissolve)
    elif (pc_area == "militarycamp" and not tutorial_finished) or (pc_area == "militarycamp" and not militarycamp_destroyed and not (day >= militarycamp_destroyed_day)) or (pc_area == "peltnorth" and not peltnorth_ban_perm) or pc_area == "howlersdell" or (pc_area == "druidcave" and druidcave_cave_open) or (pc_area == "monastery" and monastery_sleep_unlocked) or (pc_area == "watchtower" and watchtower_open) or (pc_area == "eudociahouse" and eudocia_sleep_available and not eudocia_ban) or (pc_area == "eudociahouseinside" and eudocia_sleep_available and not eudocia_ban) or (pc_area == "foggylake" and foggy_about_shelter) or (pc_area == "creeks" and creeks_sleep_available) or (pc_area == "galerocks") or (pc_area == "whitemarshes" and whitemarshes_rest_unlocked) or (pc_area == "greenmountaintribe" and greenmountaintribe_sleep and not greenmountaintribe_banned):
        hbox:
            xalign 1.0
            xpos 1526
            yalign 0.5
            vbox:
                fixed:
                    maximum (102,102)
                    minimum (102,102)
                    if pc_area == "howlersdell" and item_howlersdelltoken:
                        imagebutton:
                            style "inventoryimage2"
                            idle "inventory/howlersdelltokenidle.png"
                            action NullAction()
                    else:
                        imagebutton:
                            style "inventoryimage2"
                            idle "inventory/coinscoupleidle.png"
                            action NullAction()
                        if persistent.textstyle == "basic":
                            text "[coins]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        if persistent.textstyle == "pixel":
                            text "[coins]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                fixed:
                    maximum (102,102)
                    minimum (102,102)
                    style "inventoryimage2"
                    imagebutton:
                        if pc_food < 2:
                            if item_rations:
                                idle "images/inventory/foodrationsidle.png"
                                hover "images/inventory/foodrationshover.png"
                                hovered tt.Action("Eat a food ration")
                                action [SetVariable("item_rations", item_rations-1), SetVariable("pc_food", limit_pc_food(pc_food+2))]
                            else:
                                idle "images/inventory/foodrationslockedidle.png"
                                hover "images/inventory/foodrationslockedhover.png"
                                hovered tt.Action("You have no\nrations left")
                                action NullAction()
                        else:
                            idle "images/inventory/foodrationslockedidle.png"
                            hover "images/inventory/foodrationslockedhover.png"
                            hovered tt.Action("You don’t need\nto eat now")
                            action NullAction()
                    if pc_food < 2 and item_rations:
                        if persistent.textstyle == "basic":
                            text "[item_rations]" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        if persistent.textstyle == "pixel":
                            text "[item_rations]" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                    else:
                        if persistent.textstyle == "basic":
                            text "{color=#6a6a6a}[item_rations]{/color}" xpos 10 ypos 7 xalign 0.0 text_align 0.0 font "philosopher.ttf"
                        if persistent.textstyle == "pixel":
                            text "{color=#6a6a6a}[item_rations]{/color}" xpos 12 ypos 6 xalign 0.0 text_align 0.0 font "munro.ttf"
                if pc_class == "mage" and tutorial_finished:
                    fixed:
                        maximum (102,102)
                        minimum (102,102)
                        imagebutton:
                            style "inventoryimage2"
                            if mana >= 2 or (mana >= 1 and healingritual_discount):
                                if pc_food >= 2:
                                    if not healingritual_using:
                                        if not healingritual_discount:
                                            idle "gui/spell2idle.png"
                                            hover "gui/spell2idlehovered.png"
                                            hovered tt.Action("Start the ritual\nPneuma: [mana]/5\nCost: 2")
                                            unhovered tt.Action("")
                                            action [SetVariable("healingritual_using", 1), tt.Action("Skip the ritual\nPneuma: [mana]/5\nCost: 2")]
                                        else:
                                            idle "gui/spell1idle.png"
                                            hover "gui/spell1idlehovered.png"
                                            hovered tt.Action("Start the ritual\nPneuma: [mana]/5\nCost: 1")
                                            unhovered tt.Action("")
                                            action [SetVariable("healingritual_using", 1), tt.Action("Skip the ritual\nPneuma: [mana]/5\nCost: 1")]
                                    else:
                                        if not healingritual_discount:
                                            idle "gui/spell2active.png"
                                            hover "gui/spell2activehovered.png"
                                            hovered tt.Action("Skip the ritual\nPneuma: [mana]/5\nCost: 2")
                                            unhovered tt.Action("")
                                            action [SetVariable("healingritual_using", 0), tt.Action("Start the ritual\nPneuma: [mana]/5\nCost: 2")]
                                        else:
                                            idle "gui/spell1idle.png"
                                            hover "gui/spell1idlehovered.png"
                                            hovered tt.Action("Skip the ritual\nPneuma: [mana]/5\nCost: 1")
                                            unhovered tt.Action("")
                                            action [SetVariable("healingritual_using", 0), tt.Action("Start the ritual\nPneuma: [mana]/5\nCost: 1")]
                                else:
                                    if not healingritual_discount:
                                        idle "gui/spell2locked.png"
                                        hover "gui/spell2locked.png"
                                        hovered tt.Action("{color=#6a6a6a}The ritual won’t do much\nwhile you’re hungry{/color}")
                                        unhovered tt.Action("")
                                        action NullAction()
                                    else:
                                        idle "gui/spell1locked.png"
                                        hover "gui/spell1locked.png"
                                        hovered tt.Action("{color=#6a6a6a}The ritual won’t do much\nwhile you’re hungry{/color}")
                                        unhovered tt.Action("")
                                        action NullAction()
                            else:
                                if not healingritual_discount:
                                    idle "gui/spell2locked.png"
                                    hover "gui/spell2locked.png"
                                    hovered tt.Action("{color=#6a6a6a}You can’t start\nthe ritual\nPneuma: [mana]/5\nCost: 2{/color}")
                                    unhovered tt.Action("")
                                    action NullAction()
                                else:
                                    idle "gui/spell1locked.png"
                                    hover "gui/spell1locked.png"
                                    hovered tt.Action("{color=#6a6a6a}You can’t start\nthe ritual\nPneuma: [mana]/5\nCost: 1{/color}")
                                    unhovered tt.Action("")
                                    action NullAction()
                fixed:
                    maximum (102,102)
                    minimum (102,102)
                    imagebutton:
                        style "inventoryimage2"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action Hide("restscreen", transition=dissolve)
            frame:
                vbox:
                    spacing 25
                    if (pc_area == "militarycamp" and not tutorial_finished) or (pc_area == "militarycamp" and not militarycamp_destroyed and not (day >= militarycamp_destroyed_day)):
                        if not tutorial_finished:
                            if militarycamp_sleep_tent:
                                hbox:
                                    spacing 80
                                    vbox:
                                        spacing 25
                                        xalign 0.5
                                        xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        label _("Sleeping in a tent"):
                                            style "resting_prompt"
                                            yalign 0.0
                                        text "You can spend the night in a borrowed tent. It’s nothing special, but it will protect you from the wind and rain, and the ground won’t be painfully hard, nor cold." xmaximum 600 yalign 0.0
                                        if item_asterioncloak:
                                            text "Asterion’s cloak will soften the bench, at least." xmaximum 600 yalign 0.0
                                hbox:
                                    spacing 80
                                    vbox:
                                        spacing 25
                                        xalign 0.5
                                        xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if pc_class == "mage":
                                                add "gui/statuspoints/hp/plus0hp.png":
                                                    xalign 0.5
                                                add "gui/statuspoints/mana/plus2mana.png":
                                                    xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus0hp.png":
                                                    xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                        textbutton _("Sleep") action [SetVariable("sleep_destination", "prolcamp01newdaytent"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                            else:
                                hbox:
                                    spacing 80
                                    vbox:
                                        spacing 25
                                        xalign 0.5
                                        xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        label _("Sleeping on the ground"):
                                            style "resting_prompt"
                                            yalign 0.0
                                        if persistent.tutorial_display:
                                            text "Your blanket won’t be much of a bed and the palisade barely covers you from the wind.\nSleeping here will be severely uncomfortable." xmaximum 600 yalign 0.0
                                        else:
                                            text "Your blanket won’t be much of a bed and the palisade barely covers you from the wind.\nSleeping here will be severely uncomfortable." xmaximum 600 yalign 0.0
                                        if item_asterioncloak:
                                            text "Asterion’s cloak will soften the bench, at least." xmaximum 600 yalign 0.0
                                hbox:
                                    spacing 80
                                    vbox:
                                        spacing 25
                                        xalign 0.5
                                        xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if pc_class == "mage":
                                                add "gui/statuspoints/hp/minus1hp.png":
                                                    xalign 0.5
                                                add "gui/statuspoints/mana/plus1mana.png":
                                                    xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/minus1hp.png":
                                                    xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                        textbutton _("Sleep") action [SetVariable("sleep_destination", "prolcamp01newday"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5

                        else:
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("Sleeping on the ground"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    text "Your blanket won’t be much of a bed and the palisade barely covers you from the wind.\nSleeping here will be severely uncomfortable." xmaximum 600 yalign 0.0
                                    if item_asterioncloak:
                                        text "At least Asterion’s cloak is going to keep you warm." xmaximum 600 yalign 0.0
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    if pc_food < 2:
                                        textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if not item_asterioncloak:
                                                add "gui/statuspoints/hp/minus1hp.png":
                                                    xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                    else:
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if item_asterioncloak:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/mana/plus2mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                            else:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/minus1hp.png":
                                                            xalign 0.5
                                                        if not healingritual_discount:
                                                            add "gui/statuspoints/mana/plus1mana.png":
                                                                xalign 0.5
                                                        else:
                                                            add "gui/statuspoints/mana/plus2mana.png":
                                                                xalign 0.5
                                                    else:
                                                        if not healingritual_discount:
                                                            add "gui/statuspoints/mana/minus1mana.png":
                                                                xalign 0.5
                                                        else:
                                                            add "gui/statuspoints/mana/plus0mana.png":
                                                                xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/minus1hp.png":
                                                        xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                    textbutton _("Sleep") action [SetVariable("sleep_destination", "prolcamp01regularaftersleeping"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5

                    elif pc_area == "peltnorth" and not peltnorth_ban_perm:
                        if peltnorth_ban_temp == day:
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("Sleeping on a bench"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    text "Your blanket won’t be much of a bed. The staff will keep opening the nearby door, walking around, or talking with one another. Sleeping here will be rather uncomfortable." xmaximum 600 yalign 0.0
                                    if item_asterioncloak:
                                        text "Asterion’s cloak will soften the bench, at least." xmaximum 600 yalign 0.0
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    if pc_food < 2:
                                        textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                    else:
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if item_asterioncloak:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus3mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus2hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus1mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                            else:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        # add "gui/statuspoints/hp/plus0hp.png":
                                                        #     xalign 0.5
                                                        add "gui/statuspoints/mana/plus2mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                        # add "gui/statuspoints/mana/plus0mana.png":
                                                        #     xalign 0.5
                                                # else:
                                                #     add "gui/statuspoints/hp/plus0hp.png":
                                                #         xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                    textbutton _("Sleep") action [SetVariable("sleep_destination", "peltnorthafterbansleep"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                        else:
                            hbox:
                                spacing 80
                                if not iason_freeroom:
                                    vbox:
                                        spacing 25
                                        xalign 0.5
                                        xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        label _("Sleeping on a bench"):
                                            style "resting_prompt"
                                            yalign 0.0
                                        text "Your blanket won’t be much of a bed. The staff will keep opening the nearby door, walking around, or talking with one another. Sleeping here will be rather uncomfortable." xmaximum 600 yalign 0.0
                                        if item_asterioncloak:
                                            text "Asterion’s cloak will soften the bench, at least." xmaximum 600 yalign 0.0
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("Sleeping in a room"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    text "A comfy bed with a clean blanket in an isolated chamber. You’ll also get a large breakfast, a washtub with water and soap, and some cloves to wash your teeth." xmaximum 600 yalign 0.0
                                    if item_asterioncloak:
                                        text "With Asterion’s cloak, you could fall into a long, deep sleep." xmaximum 600 yalign 0.0
                            if pc_food < 2:
                                textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                hbox:
                                    spacing 80
                                    if not iason_freeroom:
                                        vbox:
                                            spacing 25
                                            xalign 0.5
                                            xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            hbox:
                                                spacing 0
                                                xalign 0.5
                                                #xminimum 520
                                                xmaximum 520
                                                yalign 0.0
                                                add "gui/statuspoints/food/minus2food.png":
                                                    xalign 0.5
                                                add "gui/statuspoints/appearance/minus1appearance.png":
                                                    xalign 0.5
                                            textbutton _("Sleep") action [SetVariable("sleep_destination", "peltnorthaftersleepfloor"), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+1), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                    vbox:
                                        spacing 25
                                        xalign 0.5
                                        xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            # add "gui/statuspoints/food/plus0food.png":
                                            #     xalign 0.5
                                            add "gui/statuspoints/appearance/plus3appearance.png":
                                                xalign 0.5
                                        if iason_freeroom:
                                            textbutton _("Rent: 0 {image=coin}") action [SetVariable("sleep_destination", "peltnorthaftersleeproom"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                        elif coins:
                                            textbutton _("Rent: 1 {image=coin}") action [SetVariable("coins", limit_coins(coins-1)), SetVariable("sleep_destination", "peltnorthaftersleeproom"), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+1), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                        else:
                                            textbutton _("{color=#6a6a6a}Rent: 1 {image=coingray}{/color}") action NullAction() yalign 1.0 xalign 0.5
                            else:
                                hbox:
                                    spacing 80
                                    if not iason_freeroom:
                                        vbox:
                                            spacing 25
                                            xalign 0.5
                                            xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            hbox:
                                                spacing 0
                                                xalign 0.5
                                                #xminimum 520
                                                xmaximum 520
                                                yalign 0.0
                                                if item_asterioncloak:
                                                    if pc_class == "mage":
                                                        if not healingritual_using:
                                                            add "gui/statuspoints/hp/plus1hp.png":
                                                                xalign 0.5
                                                            add "gui/statuspoints/mana/plus3mana.png":
                                                                xalign 0.5
                                                        else:
                                                            add "gui/statuspoints/hp/plus2hp.png":
                                                                xalign 0.5
                                                            add "gui/statuspoints/mana/plus1mana.png":
                                                                xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                else:
                                                    if pc_class == "mage":
                                                        if not healingritual_using:
                                                            # add "gui/statuspoints/hp/plus0hp.png":
                                                            #     xalign 0.5
                                                            add "gui/statuspoints/mana/plus2mana.png":
                                                                xalign 0.5
                                                        else:
                                                            add "gui/statuspoints/hp/plus1hp.png":
                                                                xalign 0.5
                                                            # add "gui/statuspoints/mana/plus0mana.png":
                                                            #     xalign 0.5
                                                    # else:
                                                    #     add "gui/statuspoints/hp/plus0hp.png":
                                                    #         xalign 0.5
                                                add "gui/statuspoints/food/minus2food.png":
                                                    xalign 0.5
                                                add "gui/statuspoints/appearance/minus1appearance.png":
                                                    xalign 0.5
                                            textbutton _("Sleep") action [SetVariable("sleep_destination", "peltnorthaftersleepfloor"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                    vbox:
                                        spacing 25
                                        xalign 0.5
                                        xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if item_asterioncloak:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/plus2hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus4mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus3hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus2mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                            else:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus3mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus2hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus1mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                            # add "gui/statuspoints/food/plus0food.png":
                                            #     xalign 0.5
                                            add "gui/statuspoints/appearance/plus3appearance.png":
                                                xalign 0.5
                                        if iason_freeroom:
                                            textbutton _("Rent: 0 {image=coin}") action [SetVariable("sleep_destination", "peltnorthaftersleeproom"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                        elif coins:
                                            textbutton _("Rent: 1 {image=coin}") action [SetVariable("coins", limit_coins(coins-1)), SetVariable("sleep_destination", "peltnorthaftersleeproom"), SetVariable("iason_friendship_moneybonus_points", iason_friendship_moneybonus_points+1), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                        else:
                                            textbutton _("{color=#6a6a6a}Rent: 1 {image=coingray}{/color}") action NullAction() yalign 1.0 xalign 0.5

                    elif pc_area == "howlersdell":
                        hbox:
                            spacing 80
                            if not item_howlersdelltoken:
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("Sleeping on a mouflon pelt"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    text "There’s a lot of noise outside and you can sense a heavy, unpleasant smell coming from the cauldron. At least the fur is fluffy, and you can cover yourself with your blanket." xmaximum 600 yalign 0.0
                                    if item_asterioncloak:
                                        text "Asterion’s cloak may make this spot quite comfy." xmaximum 600 yalign 0.0
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                label _("Sleeping in a room"):
                                    style "resting_prompt"
                                    yalign 0.0
                                text "Your own room, with a comfy bed, a locked door, and a lot of space. You’ll also get a large breakfast, a washtub with water and soap, and cleaning for your shoes and underwear." xmaximum 600 yalign 0.0
                                if item_asterioncloak:
                                    text "With Asterion’s cloak, you could fall into a long, deep sleep." xmaximum 600 yalign 0.0
                        if pc_food < 2:
                            textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                            hbox:
                                spacing 80
                                if not item_howlersdelltoken:
                                    vbox:
                                        spacing 25
                                        xalign 0.5
                                        xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                        textbutton _("Sleep") action [SetVariable("sleep_destination", "howlersdellwakinguphall"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        add "gui/statuspoints/food/plus1food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/plus4appearance.png":
                                            xalign 0.5
                                    if item_howlersdelltoken:
                                        textbutton _("Rent: 0 {image=coin}") action [SetVariable("sleep_destination", "howlersdellwakinguproom"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                    elif coins >= 2:
                                        textbutton _("Rent: 2 {image=coin}") action [SetVariable("coins", limit_coins(coins-2)), SetVariable("sleep_destination", "howlersdellwakinguproom"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                    else:
                                        textbutton _("{color=#6a6a6a}Rent: 2 {image=coingray}{/color}") action NullAction() yalign 1.0 xalign 0.5
                        else:
                            hbox:
                                spacing 80
                                if not item_howlersdelltoken:
                                    vbox:
                                        spacing 25
                                        xalign 0.5
                                        xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if item_asterioncloak:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus3mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus2hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus1mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                            else:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        # add "gui/statuspoints/hp/plus0hp.png":
                                                        #     xalign 0.5
                                                        add "gui/statuspoints/mana/plus2mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                        # add "gui/statuspoints/mana/plus0mana.png":
                                                        #     xalign 0.5
                                                # else:
                                                #     add "gui/statuspoints/hp/plus0hp.png":
                                                #         xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                        textbutton _("Sleep") action [SetVariable("sleep_destination", "howlersdellwakinguphall"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        if item_asterioncloak:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus4mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus3hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus2mana.png":
                                                        xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus2hp.png":
                                                    xalign 0.5
                                        else:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus3mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus1mana.png":
                                                        xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus1hp.png":
                                                    xalign 0.5
                                        add "gui/statuspoints/food/plus1food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/plus4appearance.png":
                                            xalign 0.5
                                    if item_howlersdelltoken:
                                        textbutton _("Rent: 0 {image=coin}") action [SetVariable("sleep_destination", "howlersdellwakinguproom"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                    elif coins >= 2:
                                        textbutton _("Rent: 2 {image=coin}") action [SetVariable("coins", limit_coins(coins-2)), SetVariable("sleep_destination", "howlersdellwakinguproom"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                    else:
                                        textbutton _("{color=#6a6a6a}Rent: 2 {image=coingray}{/color}") action NullAction() yalign 1.0 xalign 0.5

                    elif pc_area == "druidcave" and druidcave_cave_open:
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                label _("Sleeping on a pile of furs"):
                                    style "resting_prompt"
                                    yalign 0.0
                                text "You can cover yourself with your cape to avoid the draught, but sleeping on a surface made of stone is never comfortable." xmaximum 600 yalign 0.0
                                if item_asterioncloak:
                                    text "Asterion’s cloak will help your back a lot." xmaximum 600 yalign 0.0
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                if pc_food < 2:
                                    textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                else:
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        if item_asterioncloak:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus3mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus1mana.png":
                                                        xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus1hp.png":
                                                    xalign 0.5
                                        else:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    # add "gui/statuspoints/hp/plus0hp.png":
                                                    #     xalign 0.5
                                                    add "gui/statuspoints/mana/plus2mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                                    # add "gui/statuspoints/mana/plus0mana.png":
                                                    #     xalign 0.5
                                            # else:
                                            #     add "gui/statuspoints/hp/plus0hp.png":
                                            #         xalign 0.5
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                textbutton _("Sleep") action [SetVariable("sleep_destination", "druidcavecavernwakingup"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5

                    elif pc_area == "monastery" and monastery_sleep_unlocked:
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                label _("Sleeping in a shed"):
                                    style "resting_prompt"
                                    yalign 0.0
                                text "There’s a pile of hay on which you can lay down. There’s something calming about the rustling leaves and the wind that batters the walls like a gentle thunderstorm." xmaximum 600 yalign 0.0
                                if item_asterioncloak:
                                    text "With Asterion’s cloak, you could fall into a long, deep sleep." xmaximum 600 yalign 0.0
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                if pc_food < 2:
                                    textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                else:
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        if item_asterioncloak:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus5mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus3hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus3mana.png":
                                                        xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus2hp.png":
                                                    xalign 0.5
                                        else:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus4mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus2mana.png":
                                                        xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus1hp.png":
                                                    xalign 0.5
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                textbutton _("Sleep") action [SetVariable("sleep_destination", "monasteryaftersleep"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5

                    elif pc_area == "watchtower" and watchtower_open:
                        if not watchtower_tower_bugs_cleared:
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("Sleeping on a buggy pallet"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    if watchtower_open == "key":
                                        text "The pallet is buggy and far from fresh, but with your cape, it’s going to be soft. The thick walls will protect you from the wind and monsters." xmaximum 600 yalign 0.0
                                    if watchtower_open == "axe":
                                        text "The pallet is buggy and far from fresh, but with your cape, it’s going to be soft. The thick walls will protect you from the wind and monsters, but you have to barricade the entrance with a pile of furniture." xmaximum 600 yalign 0.0
                                    if item_asterioncloak:
                                        text "Asterion’s cloak may keep you warm, but it won’t be able to protect you from all the creatures crawling around." xmaximum 600 yalign 0.0
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    if pc_food < 2:
                                        textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                    else:
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plusquestionmarkhp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus2mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plusquestionmarkhp.png":
                                                        xalign 0.5
                                                    # add "gui/statuspoints/mana/plus0mana.png":
                                                    #     xalign 0.5
                                            # else:
                                                # add "gui/statuspoints/hp/plus0hp.png":
                                                #     xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                    textbutton _("Sleep") action [SetVariable("sleep_destination", "watchtoweraftersleep01"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                        else:
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("Sleeping on a pallet"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    if watchtower_open == "key":
                                        text "The pallet is far from fresh, but with your cape, it’s going to be soft. The thick walls will protect you from the wind and monsters." xmaximum 600 yalign 0.0
                                    if watchtower_open == "axe":
                                        text "The pallet is far from fresh, but with your cape, it’s going to be soft. The thick walls will protect you from the wind and monsters, but you have to barricade the entrance with a pile of furniture." xmaximum 600 yalign 0.0
                                    if item_asterioncloak:
                                        text "With Asterion’s cloak, you could fall into a long, deep sleep." xmaximum 600 yalign 0.0
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    if pc_food < 2:
                                        textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                    else:
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if item_asterioncloak:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus3mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus2hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus1mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                            else:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        # add "gui/statuspoints/hp/plus0hp.png":
                                                        #     xalign 0.5
                                                        add "gui/statuspoints/mana/plus2mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                        # add "gui/statuspoints/mana/plus0mana.png":
                                                        #     xalign 0.5
                                                # else:
                                                #     add "gui/statuspoints/hp/plus0hp.png":
                                                #         xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                    textbutton _("Sleep") action [SetVariable("sleep_destination", "watchtoweraftersleep01nobugs"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5

                    elif (pc_area == "eudociahouse" and eudocia_sleep_available and not eudocia_ban) or (pc_area == "eudociahouseinside" and eudocia_sleep_available and not eudocia_ban):
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                label _("Sleeping in a shed"):
                                    style "resting_prompt"
                                    yalign 0.0
                                text "There’s a soft haystack on which you can lay down. The golems are ordered to scare off any intruders and the walls will to protect you from the wind. You can also use a washtub and repair your equipment." xmaximum 600 yalign 0.0
                                if item_asterioncloak:
                                    text "With Asterion’s cloak, you could fall into a long, deep sleep." xmaximum 600 yalign 0.0
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                if pc_food < 2:
                                    textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                else:
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        if item_asterioncloak:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus4mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus3hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus2mana.png":
                                                        xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus2hp.png":
                                                    xalign 0.5
                                        else:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus3mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus1mana.png":
                                                        xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus1hp.png":
                                                    xalign 0.5
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                textbutton _("Sleep") action [SetVariable("sleep_destination", "eudociahouseaftersleep"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5

                    elif pc_area == "foggylake" and foggy_about_shelter:
                        if foggy_friendship < 15 and foggy_quest_iason_relationship != "mad":
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("Sleeping in\nthe main hall"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    text "The bear fur will be a fine sleeping spot, but your horse will disturb your rest, and in the morning you’ll have to clean after it. Sleeping here will be rather uncomfortable." xmaximum 600 yalign 0.0
                                    if item_asterioncloak:
                                        text "Maybe Asterion’s cloak will help you ignore the smell." xmaximum 600 yalign 0.0
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("Sleeping in\nthe attic"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    text "You’ll have plenty of space and many furs to choose from. The staff will help you take care of your mount’s filth." xmaximum 600 yalign 0.0
                                    if item_asterioncloak:
                                        text "With Asterion’s cloak, you could fall into a long, deep sleep." xmaximum 600 yalign 0.0
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    if pc_food < 2:
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if not item_asterioncloak:
                                                add "gui/statuspoints/hp/minus1hp.png":
                                                    xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus2appearance.png":
                                                xalign 0.5
                                    else:
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if item_asterioncloak:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        # add "gui/statuspoints/hp/plus0hp.png":
                                                        #     xalign 0.5
                                                        add "gui/statuspoints/mana/plus2mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                        # add "gui/statuspoints/mana/plus0mana.png":
                                                        #     xalign 0.5
                                                # else:
                                                #     add "gui/statuspoints/hp/plus0hp.png":
                                                #         xalign 0.5
                                            else:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/minus1hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus1mana.png":
                                                            xalign 0.5
                                                    else:
                                                        # add "gui/statuspoints/hp/plus0hp.png":
                                                        #     xalign 0.5
                                                        add "gui/statuspoints/mana/minus1mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/minus1hp.png":
                                                        xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus2appearance.png":
                                                xalign 0.5
                                    textbutton _("Sleep") action [SetVariable("sleep_destination", "foggylakegroundflooraftersleep"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    if pc_food < 2:
                                        textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                    else:
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if item_asterioncloak:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/plus2hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus4mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus3hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus2mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                            else:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus3mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus2hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus1mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                    if coins:
                                        textbutton _("Rent: 1 {image=coin}") action [SetVariable("coins", limit_coins(coins-1)), SetVariable("foggy_friendship_tradepoints", foggy_friendship_tradepoints+1), SetVariable("sleep_destination", "foggylakeatticaftersleep"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                    else:
                                        textbutton _("{color=#6a6a6a}Rent: 1 {image=coingray}{/color}") action NullAction() yalign 1.0 xalign 0.5
                                    if item_rations >= 2:
                                        textbutton _("Rent: 2 rations") action [SetVariable("item_rations", limit_item_rations(item_rations-2)), SetVariable("foggy_friendship_tradepoints", foggy_friendship_tradepoints+1), SetVariable("sleep_destination", "foggylakeatticaftersleep"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                    else:
                                        textbutton _("{color=#6a6a6a}Rent: 2 rations{/color}") action NullAction() yalign 1.0 xalign 0.5
                        else:
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("Sleeping in\nthe attic"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    text "You’ll have plenty of space and many furs to choose from, and the staff will help you take care of your mount’s filth." xmaximum 600 yalign 0.0
                                    text "{color=#f6d6bd}Foggy{/color} offers you to rest here for free." xmaximum 600 yalign 0.0
                                    if item_asterioncloak:
                                        text "With Asterion’s cloak, you could fall into a long, deep sleep." xmaximum 600 yalign 0.0
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    if pc_food < 2:
                                        textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                    else:
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if item_asterioncloak:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/plus2hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus4mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus3hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus2mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                            else:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus3mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus2hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus1mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                    textbutton _("Sleep") action [SetVariable("sleep_destination", "foggylakeatticaftersleep"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5

                    elif pc_area == "creeks" and creeks_sleep_available:
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                label _("Sleeping at your place"):
                                    style "resting_prompt"
                                    yalign 0.0
                                text "A pile of fresh furs is waiting for you. For some time, you’ll hear the steps and conversations of your neighbors, but the conditions are better than in most common rooms and the locals respect the rest of others." xmaximum 600 yalign 0.0
                                if item_asterioncloak:
                                    text "With Asterion’s cloak, you could fall into a long, deep sleep." xmaximum 600 yalign 0.0
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                if pc_food < 2:
                                    textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                else:
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        if item_asterioncloak:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus4mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus3hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus2mana.png":
                                                        xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus2hp.png":
                                                    xalign 0.5
                                        else:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus3mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus1mana.png":
                                                        xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus1hp.png":
                                                    xalign 0.5
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                textbutton _("Sleep") action [SetVariable("sleep_destination", "creeksaftersleep"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5

                    elif pc_area == "galerocks":
                        if not galerocks_fulvia_sleep:
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("You ask for an inn"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    text "While the guards explain to you that the village doesn’t run such a place, you should visit {color=#f6d6bd}Fulvia{/color}, who may have a room to spare." xmaximum 600 yalign 0.0
                                    textbutton _("I ask them\nfor directions") action [SetVariable("galerocks_fulvia_firsttime", 1), Hide("restscreen", transition=dissolve), Jump('galerocksfulvia01firsttime')] yalign 1.0 xalign 0.5
                        else:
                            hbox:
                                spacing 80
                                vbox:
                                    spacing 25
                                    xalign 0.5
                                    xminimum 520
                                    xmaximum 520
                                    yalign 0.0
                                    label _("Sleeping at a house"):
                                        style "resting_prompt"
                                        yalign 0.0
                                    text "An elder allows you to spend the night in crude conditions. In return, she requires an absurd payment, or half a day of your labor." xmaximum 600 yalign 0.0
                                    if item_asterioncloak:
                                        text "With Asterion’s cloak, you could fall into a long, deep sleep." xmaximum 600 yalign 0.0
                            if pc_food < 2:
                                textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                vbox:
                                    spacing 80
                                    vbox:
                                        spacing 25
                                        xalign 0.5
                                        xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                        if galerocks_sleep_free:
                                            textbutton _("Rent: 0 {image=coin}") action [SetVariable("sleep_destination", "galerocksaftersleepmoney"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                        elif coins >= 2:
                                            textbutton _("Rent: 2 {image=coin}") action [SetVariable("sleep_destination", "galerocksaftersleepmoney"), SetVariable("coins", coins-2), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                        else:
                                            textbutton _("{color=#6a6a6a}Rent: 2 {image=coingray}{/color}") action NullAction() yalign 1.0 xalign 0.5
                                    if not galerocks_sleep_free:
                                        vbox:
                                            spacing 25
                                            xalign 0.5
                                            xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            hbox:
                                                spacing 0
                                                xalign 0.5
                                                #xminimum 520
                                                xmaximum 520
                                                yalign 0.0
                                                add "gui/statuspoints/food/minus3food.png":
                                                    xalign 0.5
                                                add "gui/statuspoints/appearance/minus2appearance.png":
                                                    xalign 0.5
                                            textbutton _("Rent: labor") action [SetVariable("sleep_destination", "galerocksaftersleeplabor"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                            else:
                                vbox:
                                    spacing 80
                                    vbox:
                                        spacing 25
                                        xalign 0.5
                                        xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        hbox:
                                            spacing 0
                                            xalign 0.5
                                            #xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            if item_asterioncloak:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/plus2hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus3mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus3hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus1mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                            else:
                                                if pc_class == "mage":
                                                    if not healingritual_using:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus3mana.png":
                                                            xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus2hp.png":
                                                            xalign 0.5
                                                        add "gui/statuspoints/mana/plus1mana.png":
                                                            xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                            add "gui/statuspoints/food/minus2food.png":
                                                xalign 0.5
                                            add "gui/statuspoints/appearance/minus1appearance.png":
                                                xalign 0.5
                                        if galerocks_sleep_free:
                                            textbutton _("Rent: 0 {image=coin}") action [SetVariable("sleep_destination", "galerocksaftersleepmoney"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                        elif coins >= 2:
                                            textbutton _("Rent: 2 {image=coin}") action [SetVariable("sleep_destination", "galerocksaftersleepmoney"), SetVariable("coins", coins-2), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5
                                        elif coins <= 0:
                                            textbutton _("{color=#6a6a6a}Rent: 2 {image=coingray}{/color}") action NullAction() yalign 1.0 xalign 0.5
                                    if not galerocks_sleep_free:
                                        vbox:
                                            spacing 25
                                            xalign 0.5
                                            xminimum 520
                                            xmaximum 520
                                            yalign 0.0
                                            hbox:
                                                spacing 0
                                                xalign 0.5
                                                #xminimum 520
                                                xmaximum 520
                                                yalign 0.0
                                                if item_asterioncloak:
                                                    if pc_class == "mage":
                                                        if not healingritual_using:
                                                            add "gui/statuspoints/hp/plus1hp.png":
                                                                xalign 0.5
                                                            add "gui/statuspoints/mana/plus3mana.png":
                                                                xalign 0.5
                                                        else:
                                                            add "gui/statuspoints/hp/plus2hp.png":
                                                                xalign 0.5
                                                            add "gui/statuspoints/mana/plus1mana.png":
                                                                xalign 0.5
                                                    else:
                                                        add "gui/statuspoints/hp/plus1hp.png":
                                                            xalign 0.5
                                                else:
                                                    if pc_class == "mage":
                                                        if not healingritual_using:
                                                            # add "gui/statuspoints/hp/plus0hp.png":
                                                            #     xalign 0.5
                                                            add "gui/statuspoints/mana/plus2mana.png":
                                                                xalign 0.5
                                                        else:
                                                            add "gui/statuspoints/hp/plus1hp.png":
                                                                xalign 0.5
                                                            # add "gui/statuspoints/mana/plus0mana.png":
                                                            #     xalign 0.5
                                                    # else:
                                                    #     add "gui/statuspoints/hp/plus0hp.png":
                                                    #         xalign 0.5
                                                add "gui/statuspoints/food/minus3food.png":
                                                    xalign 0.5
                                                add "gui/statuspoints/appearance/minus2appearance.png":
                                                    xalign 0.5
                                            textbutton _("Rent: labor") action [SetVariable("sleep_destination", "galerocksaftersleeplabor"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5

                    elif pc_area == "whitemarshes" and whitemarshes_rest_unlocked:
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                label _("Sleeping in a shed"):
                                    style "resting_prompt"
                                    yalign 0.0
                                if not whitemarshes_nomoreundead:
                                    text "You have to rest on your own blanket. The never-ending sounds of the wall construction and walking skeletons won’t help you catch a good sleep." xmaximum 600 yalign 0.0
                                else:
                                    text "You have to rest on your own blanket. The haunting silence of the village and the smell of burnt flesh won’t help you catch a good sleep." xmaximum 600 yalign 0.0
                                if item_asterioncloak:
                                    text "With Asterion’s cloak, you could ease your shell a bit." xmaximum 600 yalign 0.0
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                if pc_food < 2:
                                    textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                else:
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        if item_asterioncloak:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus2mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                                    # add "gui/statuspoints/hp/plus0hp.png":
                                                    #     xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus1hp.png":
                                                    xalign 0.5
                                        else:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    # add "gui/statuspoints/hp/plus0hp.png":
                                                    #     xalign 0.5
                                                    add "gui/statuspoints/mana/plus1mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/minus1mana.png":
                                                        xalign 0.5
                                            # else:
                                            #     add "gui/statuspoints/hp/plus0hp.png":
                                            #         xalign 0.5
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                textbutton _("Sleep") action [SetVariable("sleep_destination", "whitemarshesaftersleep"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5

                    elif pc_area == "greenmountaintribe" and greenmountaintribe_sleep and not greenmountaintribe_banned:
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                label _("Sleeping in the shed"):
                                    style "resting_prompt"
                                    yalign 0.0
                                text "You’re offered a wisent pelt to cover the cold rocks, but you’ll be often disturbed by people patrolling the territory, and the echoes of roaring beasts." xmaximum 600 yalign 0.0
                                if item_asterioncloak:
                                    text "With Asterion’s cloak, you could ignore some of these issues." xmaximum 600 yalign 0.0
                        hbox:
                            spacing 80
                            vbox:
                                spacing 25
                                xalign 0.5
                                xminimum 520
                                xmaximum 520
                                yalign 0.0
                                if pc_food < 2:
                                    textbutton _("{color=#6a6a6a}You’re hungry!{/color}") action NullAction() yalign 1.0 xalign 0.5
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                else:
                                    hbox:
                                        spacing 0
                                        xalign 0.5
                                        #xminimum 520
                                        xmaximum 520
                                        yalign 0.0
                                        if item_asterioncloak:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/plus2mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus2hp.png":
                                                        xalign 0.5
                                                    # add "gui/statuspoints/hp/plus0hp.png":
                                                    #     xalign 0.5
                                            else:
                                                add "gui/statuspoints/hp/plus1hp.png":
                                                    xalign 0.5
                                        else:
                                            if pc_class == "mage":
                                                if not healingritual_using:
                                                    # add "gui/statuspoints/hp/plus0hp.png":
                                                    #     xalign 0.5
                                                    add "gui/statuspoints/mana/plus1mana.png":
                                                        xalign 0.5
                                                else:
                                                    add "gui/statuspoints/hp/plus1hp.png":
                                                        xalign 0.5
                                                    add "gui/statuspoints/mana/minus1mana.png":
                                                        xalign 0.5
                                            # else:
                                            #     add "gui/statuspoints/hp/plus0hp.png":
                                            #         xalign 0.5
                                        add "gui/statuspoints/food/minus2food.png":
                                            xalign 0.5
                                        add "gui/statuspoints/appearance/minus1appearance.png":
                                            xalign 0.5
                                textbutton _("Sleep") action [SetVariable("sleep_destination", "greenmountaintribeaftersleep"), Hide("restscreen", transition=dissolve), Jump('sleeping')] yalign 1.0 xalign 0.5

    ######################################################
    $ sleep_options = 0
    if not (pc_area == "militarycamp" and not tutorial_finished) and not (pc_area == "militarycamp" and not militarycamp_destroyed and not (day >= militarycamp_destroyed_day)) and not (pc_area == "howlersdell") and not (pc_area == "foggylake") and not (pc_area == "peltnorth" and not peltnorth_ban_perm) and not (pc_area == "druidcave" and druidcave_cave_open) and not (pc_area == "monastery" and monastery_sleep_unlocked) and not (pc_area == "watchtower" and watchtower_open) and not (pc_area == "eudociahouse" and eudocia_sleep_available and not eudocia_ban) and not (pc_area == "eudociahouseinside" and eudocia_sleep_available and not eudocia_ban) and not (pc_area == "galerocks") and not (pc_area == "whitemarshes" and whitemarshes_rest_unlocked) and not (pc_area == "greenmountaintribe" and greenmountaintribe_sleep and not greenmountaintribe_banned) and not (pc_area == "creeks" and creeks_sleep_available): # REMEMBER ABOUT quickmenurestdisplay
        if (not whitemarshes_rest_unlocked and not whitemarshes_attacked and not whitemarshes_destroyed and pc_area == "bogroad") or (not whitemarshes_rest_unlocked and not whitemarshes_attacked and not whitemarshes_destroyed and pc_area == "bogcrossroads") or (not whitemarshes_rest_unlocked and not whitemarshes_attacked and not whitemarshes_destroyed and pc_area == "peatfield") or (not whitemarshes_rest_unlocked and not whitemarshes_attacked and not whitemarshes_destroyed and pc_area == "whitemarshes") or (vines_perma_closed and pc_area == "bogroad") or (vines_perma_closed and pc_area == "bogcrossroads") or (vines_perma_closed and pc_area == "peatfield") or (vines_perma_closed and pc_area == "vines") or (not vines_open_sleep and vines_open_day != day and not vines_perma_open and pc_area == "bogroad") or (not vines_open_sleep and vines_open_day != day and not vines_perma_open and pc_area == "bogcrossroads") or (not vines_open_sleep and vines_open_day != day and not vines_perma_open and pc_area == "peatfield") or (not vines_open_sleep and vines_open_day != day and not vines_perma_open and pc_area == "vines") or (not whitemarshes_rest_unlocked and pc_area == "vines"):
            $ sleep_options = "bogentrance"

        elif (whitemarshes_rest_unlocked and not whitemarshes_attacked and not whitemarshes_destroyed and pc_area == "bogroad") or (whitemarshes_rest_unlocked and not whitemarshes_attacked and not whitemarshes_destroyed and pc_area == "bogcrossroads") or (whitemarshes_rest_unlocked and not whitemarshes_attacked and not whitemarshes_destroyed and pc_area == "peatfield") or (whitemarshes_rest_unlocked and not whitemarshes_attacked and not whitemarshes_destroyed and pc_area == "vines"):
            $ sleep_options = "whitemarshes"

        else:
            if sleep_options == 0:
                if not howlersdell_firsttime:
                    if topeltnorth >= 100 or peltnorth_ban_perm == 1 or peltnorth_ban_temp == day:
                        if tomonastery >= 100 or not monastery_sleep_unlocked:
                            if towatchtower >= 100 or not watchtower_open:
                                if toeudociahouse >= 100 or not eudocia_sleep_available or eudocia_ban:
                                    if todruidcave >= 100 or not druidcave_cave_open:
                                        if togalerocks >= 100 or not galerocks_fulvia_sleep:
                                            if togreenmountaintribe >= 100 or not greenmountaintribe_sleep or greenmountaintribe_banned:
                                                if tomilitarycamp >= 100 or militarycamp_destroyed or day >= militarycamp_destroyed_day: #jeśli wszędzie jest za daleko i nie było się w Howlers
                                                    $ sleep_options = "blindhowlers"

            if sleep_options == 0:
                if topeltnorth >= 100 or peltnorth_ban_perm == 1 or peltnorth_ban_temp == day:
                    if tohowlersdell >= 100:
                        if tomonastery >= 100 or not monastery_sleep_unlocked:
                            if towatchtower >= 100 or not watchtower_open:
                                if toeudociahouse >= 100 or not eudocia_sleep_available or eudocia_ban:
                                    if todruidcave >= 100 or not druidcave_cave_open:
                                        if togalerocks >= 100 or not galerocks_fulvia_sleep:
                                            if togreenmountaintribe >= 100 or not greenmountaintribe_sleep or greenmountaintribe_banned:
                                                if tomilitarycamp >= 100: #jeśli wszędzie jest za daleko i było się w Howlers
                                                    $ sleep_options = "blindmilitarycamp"

            if sleep_options == 0:
                if pc_area == "mountainroad" and not greenmountaintribe_firsttime:
                    $ sleep_options = "blindgreenmountaintribe"

            if sleep_options == 0:
                if peltnorth_ban_perm != 1 and peltnorth_ban_temp != day:
                    if topeltnorth <= tomilitarycamp or militarycamp_destroyed or (day >= militarycamp_destroyed_day):
                        if topeltnorth <= todruidcave or not druidcave_cave_open:
                            if topeltnorth <= tohowlersdell or not howlersdell_firsttime or thais_bigmad:
                                if topeltnorth <= tomonastery or not monastery_sleep_unlocked:
                                    if topeltnorth <= towatchtower or not watchtower_open:
                                        if topeltnorth <= toeudociahouse or not eudocia_sleep_available or eudocia_ban:
                                            if topeltnorth <= togalerocks or not galerocks_fulvia_sleep:
                                                if topeltnorth <= togreenmountaintribe or not greenmountaintribe_sleep or greenmountaintribe_banned:
                                                    if topeltnorth <= tofoggylake or not foggylake_firsttime:
                                                        $ sleep_options = "peltnorth"

            if sleep_options == 0:
                if howlersdell_firsttime:
                    if not thais_bigmad:
                        if tohowlersdell <= topeltnorth or peltnorth_ban_perm == 1 or peltnorth_ban_temp == day:
                            if tohowlersdell <= tomilitarycamp or militarycamp_destroyed or (day >= militarycamp_destroyed_day):
                                if tohowlersdell <= todruidcave or not druidcave_cave_open:
                                    if tohowlersdell <= tomonastery or not monastery_sleep_unlocked:
                                        if tohowlersdell <= towatchtower or not watchtower_open:
                                            if tohowlersdell <= toeudociahouse or not eudocia_sleep_available or eudocia_ban:
                                                if tohowlersdell <= togalerocks or not galerocks_fulvia_sleep:
                                                    if tohowlersdell <= togreenmountaintribe or not greenmountaintribe_sleep or greenmountaintribe_banned:
                                                        if tohowlersdell <= tofoggylake or not foggylake_firsttime:
                                                                $ sleep_options = "howlersdell"

            if sleep_options == 0:
                if foggylake_firsttime:
                    if tofoggylake <= topeltnorth or peltnorth_ban_perm == 1 or peltnorth_ban_temp == day:
                        if tofoggylake <= tomilitarycamp or militarycamp_destroyed or (day >= militarycamp_destroyed_day):
                            if tofoggylake <= todruidcave or not druidcave_cave_open:
                                if tofoggylake <= tohowlersdell or not howlersdell_firsttime or thais_bigmad:
                                    if tofoggylake <= tomonastery or not monastery_sleep_unlocked:
                                        if tofoggylake <= towatchtower or not watchtower_open:
                                            if tofoggylake <= togalerocks or not galerocks_fulvia_sleep:
                                                if tofoggylake <= togreenmountaintribe or not greenmountaintribe_sleep or greenmountaintribe_banned:
                                                    if tofoggylake <= toeudociahouse or not eudocia_sleep_available or eudocia_ban:
                                                        $ sleep_options = "foggylake"

            if sleep_options == 0:
                if tomonastery <= topeltnorth or peltnorth_ban_perm == 1 or peltnorth_ban_temp == day:
                    if tomonastery <= tomilitarycamp or militarycamp_destroyed or (day >= militarycamp_destroyed_day):
                        if tomonastery <= todruidcave or not druidcave_cave_open:
                            if tomonastery <= tohowlersdell or not howlersdell_firsttime or thais_bigmad:
                                if tomonastery <= towatchtower or not watchtower_open:
                                    if tomonastery <= toeudociahouse or not eudocia_sleep_available or eudocia_ban:
                                        if tomonastery <= tofoggylake or not foggylake_firsttime:
                                            if tomonastery <= togalerocks or not galerocks_fulvia_sleep:
                                                if tomonastery <= togreenmountaintribe or not greenmountaintribe_sleep or greenmountaintribe_banned:
                                                    if monastery_sleep_unlocked:
                                                        $ sleep_options = "monastery"

            if sleep_options == 0:
                if towatchtower <= topeltnorth or peltnorth_ban_perm == 1 or peltnorth_ban_temp == day:
                    if towatchtower <= tomilitarycamp or militarycamp_destroyed or (day >= militarycamp_destroyed_day):
                        if towatchtower <= todruidcave or not druidcave_cave_open:
                            if towatchtower <= tohowlersdell or not howlersdell_firsttime or thais_bigmad:
                                if towatchtower <= tomonastery or not monastery_sleep_unlocked:
                                    if towatchtower <= toeudociahouse or not eudocia_sleep_available or eudocia_ban:
                                        if towatchtower <= tofoggylake or not foggylake_firsttime:
                                            if towatchtower <= togalerocks or not galerocks_fulvia_sleep:
                                                if towatchtower <= togreenmountaintribe or not greenmountaintribe_sleep or greenmountaintribe_banned:
                                                    if watchtower_open:
                                                        $ sleep_options = "abandonedwatchtower"
            if sleep_options == 0:
                if eudocia_sleep_available and not eudocia_ban:
                    if toeudociahouse <= topeltnorth or peltnorth_ban_perm == 1 or peltnorth_ban_temp == day:
                        if toeudociahouse <= tomilitarycamp or militarycamp_destroyed or (day >= militarycamp_destroyed_day):
                            if toeudociahouse <= todruidcave or not druidcave_cave_open:
                                if toeudociahouse <= tohowlersdell or not howlersdell_firsttime or thais_bigmad:
                                    if toeudociahouse <= tomonastery or not monastery_sleep_unlocked:
                                        if toeudociahouse <= towatchtower or not watchtower_open:
                                            if toeudociahouse <= togalerocks or not galerocks_fulvia_sleep:
                                                if toeudociahouse <= togreenmountaintribe or not greenmountaintribe_sleep or greenmountaintribe_banned:
                                                    if toeudociahouse <= tofoggylake or not foggylake_firsttime:
                                                        $ sleep_options = "eudociahouse"

            if sleep_options == 0:
                if druidcave_cave_open:
                    if todruidcave <= topeltnorth or peltnorth_ban_perm == 1 or peltnorth_ban_temp == day:
                        if todruidcave <= tomilitarycamp or militarycamp_destroyed or (day >= militarycamp_destroyed_day):
                            if todruidcave <= tohowlersdell or not howlersdell_firsttime or thais_bigmad:
                                if todruidcave <= tomonastery or not monastery_sleep_unlocked:
                                    if todruidcave <= towatchtower or not watchtower_open:
                                        if todruidcave <= toeudociahouse or not eudocia_sleep_available or eudocia_ban:
                                            if todruidcave <= togalerocks or not galerocks_fulvia_sleep:
                                                if todruidcave <= togreenmountaintribe or not greenmountaintribe_sleep or greenmountaintribe_banned:
                                                    if todruidcave <= tofoggylake or not foggylake_firsttime:
                                                        $ sleep_options = "druidcave"

            if sleep_options == 0:
                if galerocks_fulvia_sleep:
                    if togalerocks <= topeltnorth or peltnorth_ban_perm == 1 or peltnorth_ban_temp == day:
                        if togalerocks <= tomilitarycamp or militarycamp_destroyed or (day >= militarycamp_destroyed_day):
                            if togalerocks <= tohowlersdell or not howlersdell_firsttime or thais_bigmad:
                                if togalerocks <= tomonastery or not monastery_sleep_unlocked:
                                    if togalerocks <= towatchtower or not watchtower_open:
                                        if togalerocks <= toeudociahouse or not eudocia_sleep_available or eudocia_ban:
                                            if togalerocks <= todruidcave or not druidcave_cave_open:
                                                if togalerocks <= togreenmountaintribe or not greenmountaintribe_sleep or greenmountaintribe_banned:
                                                    if togalerocks <= tofoggylake or not foggylake_firsttime:
                                                        $ sleep_options = "galerocks"

            if sleep_options == 0:
                if greenmountaintribe_sleep and not greenmountaintribe_banned:
                    if togreenmountaintribe <= topeltnorth or peltnorth_ban_perm == 1 or peltnorth_ban_temp == day:
                        if togreenmountaintribe <= tomilitarycamp or militarycamp_destroyed or (day >= militarycamp_destroyed_day):
                            if togreenmountaintribe <= tohowlersdell or not howlersdell_firsttime or thais_bigmad:
                                if togreenmountaintribe <= tomonastery or not monastery_sleep_unlocked:
                                    if togreenmountaintribe <= towatchtower or not watchtower_open:
                                        if togreenmountaintribe <= toeudociahouse or not eudocia_sleep_available or eudocia_ban:
                                            if togreenmountaintribe <= togalerocks or not galerocks_fulvia_sleep:
                                                if togreenmountaintribe <= todruidcave or not druidcave_cave_open:
                                                    if togreenmountaintribe <= tofoggylake or not foggylake_firsttime:
                                                        $ sleep_options = "greenmountaintribe"

            if sleep_options == 0:
                if not militarycamp_destroyed and not (day >= militarycamp_destroyed_day):
                    if tomilitarycamp <= topeltnorth or peltnorth_ban_perm == 1 or peltnorth_ban_temp == day:
                        if tomilitarycamp <= todruidcave or not druidcave_cave_open:
                            if tomilitarycamp <= tohowlersdell or not howlersdell_firsttime or thais_bigmad:
                                if tomilitarycamp <= tomonastery or not monastery_sleep_unlocked:
                                    if tomilitarycamp <= towatchtower or not watchtower_open:
                                        if tomilitarycamp <= toeudociahouse or not eudocia_sleep_available or eudocia_ban:
                                            if tomilitarycamp <= togalerocks or not galerocks_fulvia_sleep:
                                                if tomilitarycamp <= togreenmountaintribe or not greenmountaintribe_sleep or greenmountaintribe_banned:
                                                    if tomilitarycamp <= tofoggylake or not foggylake_firsttime:
                                                        $ sleep_options = "militarycamp"

######################################################

    if sleep_options == "bogentrance":
        $ estimatedtravel_duration = (quarters+tobogentrance)
        if estimatedtravel_duration < (world_daylength-3):
            hbox:
                xalign 0.4615
                yalign 0.5
                vbox:
                    fixed:
                        maximum (102,102)
                        minimum (102,102)
                        imagebutton:
                            style "inventoryimage2"
                            idle "gui/clossingarrowidle.png"
                            hover "gui/clossingarrowhover.png"
                            action Hide("restscreen", transition=dissolve)
                frame:
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 45
                        label _("It’s too dangerous to stay here!"):
                            style "resting_prompt"
                        text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou should head to {color=#f6d6bd}the old forest garden{/color}." xmaximum 600 text_align 0.5
                        hbox:
                            xalign 0.5
                            spacing 130
                            textbutton _("Travel") action [Hide("restscreen", transition=dissolve), SetVariable("travel_destination", "bogentrance"), Jump('finaldestinationafterevent')]
        else:
            hbox:
                xalign 0.4615
                yalign 0.5
                vbox:
                    fixed:
                        maximum (102,102)
                        minimum (102,102)
                        imagebutton:
                            style "inventoryimage2"
                            idle "gui/clossingarrowidle.png"
                            hover "gui/clossingarrowhover.png"
                            action Hide("restscreen", transition=dissolve)
                frame:
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 45
                        label _("It’s too dangerous to stay here!"):
                            style "resting_prompt"
                        text "You can’t sleep here, yet you have to find\na safe place as soon as possible.\n\nYou should head to {color=#f6d6bd}the old forest garden{/color},\nbut the creatures of the bogs are surely going to attack you." xmaximum 600 text_align 0.5
                        if estimatedtravel_duration < (world_daylength-2):
                            $ traveldamage = 1
                            add "gui/statuspoints/hp/minus1hp.png":
                                xalign 0.5
                        elif estimatedtravel_duration < (world_daylength+0):
                            $ traveldamage = 2
                            add "gui/statuspoints/hp/minus2hp.png":
                                xalign 0.5
                        elif estimatedtravel_duration < (world_daylength+2):
                            $ traveldamage = 3
                            add "gui/statuspoints/hp/minus3hp.png":
                                xalign 0.5
                        elif estimatedtravel_duration < (world_daylength+4):
                            $ traveldamage = 4
                            add "gui/statuspoints/hp/minus4hp.png":
                                xalign 0.5
                        else:
                            $ traveldamage = 5
                            add "gui/statuspoints/hp/minus5hp.png":
                                xalign 0.5
                        hbox:
                            xalign 0.5
                            spacing 130
                            textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "bogentrance"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]

    if sleep_options == "blindhowlers" or sleep_options == "blindmilitarycamp" or sleep_options == "militarycamp" or sleep_options == "peltnorth" or sleep_options == "druidcave" or sleep_options == "howlersdell" or sleep_options == "monastery" or sleep_options == "abandonedwatchtower" or sleep_options == "eudociahouse" or sleep_options == "foggylake" or sleep_options == "galerocks" or sleep_options == "whitemarshes" or sleep_options == "greenmountaintribe" or sleep_options == "blindgreenmountaintribe":
        hbox:
            xalign 0.4615
            yalign 0.5
            vbox:
                fixed:
                    maximum (102,102)
                    minimum (102,102)
                    imagebutton:
                        style "inventoryimage2"
                        idle "gui/clossingarrowidle.png"
                        hover "gui/clossingarrowhover.png"
                        action Hide("restscreen", transition=dissolve)
            frame:
                if sleep_options == "blindhowlers":
                    $ estimatedtravel_duration = (quarters+tohowlersdell)
                elif sleep_options == "blindmilitarycamp":
                    $ estimatedtravel_duration = (quarters+tomilitarycamp)
                elif sleep_options == "militarycamp":
                    $ estimatedtravel_duration = (quarters+tomilitarycamp)
                elif sleep_options == "peltnorth":
                    $ estimatedtravel_duration = (quarters+topeltnorth)
                elif sleep_options == "druidcave":
                    $ estimatedtravel_duration = (quarters+todruidcave)
                elif sleep_options == "howlersdell":
                    $ estimatedtravel_duration = (quarters+tohowlersdell)
                elif sleep_options == "monastery":
                    $ estimatedtravel_duration = (quarters+tomonastery)
                elif sleep_options == "abandonedwatchtower":
                    $ estimatedtravel_duration = (quarters+towatchtower)
                elif sleep_options == "eudociahouse":
                    $ estimatedtravel_duration = (quarters+toeudociahouse)
                elif sleep_options == "foggylake":
                    $ estimatedtravel_duration = (quarters+tofoggylake)
                elif sleep_options == "galerocks":
                    $ estimatedtravel_duration = (quarters+togalerocks)
                elif sleep_options == "whitemarshes":
                    $ estimatedtravel_duration = (quarters+towhitemarshes+2)
                elif sleep_options == "greenmountaintribe":
                    $ estimatedtravel_duration = (quarters+togreenmountaintribe)
                elif sleep_options == "blindgreenmountaintribe":
                    $ estimatedtravel_duration = (quarters+togreenmountaintribe)
                if estimatedtravel_duration < (world_daylength+1) and not sleep_options == "blindhowlers" and not sleep_options == "blindmilitarycamp":
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 45
                        label _("It’s too dangerous to stay here!"):
                            style "resting_prompt"
                        if sleep_options == "militarycamp":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Tulia’s camp{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "peltnorth":
                            text "You can’t sleep here, but there’s still time\nto move to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Pelt of the North{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "druidcave":
                            text "You can’t sleep here, yet you have to find\na safe place as soon as possible.\n\nYou can find the closest shelter in {color=#f6d6bd}Druid’s Cave{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "howlersdell":
                            text "You can’t sleep here, yet you have to find\na safe place as soon as possible.\n\nYou can find the closest shelter in {color=#f6d6bd}Howler’s Dell{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "monastery":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Monastery{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "abandonedwatchtower":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}the abandoned watchtower{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "eudociahouse":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Eudocia’s house{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "foggylake":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Foggy Lake{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "galerocks":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Gale Rocks{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "whitemarshes":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}White Marshes{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "greenmountaintribe":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at\n{color=#f6d6bd}The Tribe of The Green Mountain{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "blindgreenmountaintribe":
                            text "You can’t sleep here, but you could still try\nto find shelter ahead." xmaximum 600 text_align 0.5
                        hbox:
                            xalign 0.5
                            spacing 130
                            if sleep_options == "militarycamp":
                                textbutton _("Travel") action [SetVariable("travel_destination", "militarycamp"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "peltnorth":
                                textbutton _("Travel") action [SetVariable("travel_destination", "peltnorth"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "druidcave":
                                textbutton _("Travel") action [SetVariable("travel_destination", "druidcave"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "howlersdell":
                                textbutton _("Travel") action [SetVariable("travel_destination", "howlersdell"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "monastery":
                                textbutton _("Travel") action [SetVariable("travel_destination", "monastery"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "abandonedwatchtower":
                                textbutton _("Travel") action [SetVariable("travel_destination", "watchtower"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "eudociahouse":
                                textbutton _("Travel") action [SetVariable("travel_destination", "eudociahouse"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "foggylake":
                                textbutton _("Travel") action [SetVariable("travel_destination", "foggylake"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "galerocks":
                                textbutton _("Travel") action [SetVariable("travel_destination", "galerocks"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "whitemarshes":
                                textbutton _("Travel") action [SetVariable("travel_destination", "whitemarshes"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "greenmountaintribe":
                                textbutton _("Travel") action [SetVariable("travel_destination", "greenmountaintribe"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "blindgreenmountaintribe":
                                textbutton _("Travel") action [SetVariable("travel_destination", "greenmountaintribe"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                elif (sleep_options == "foggylake" and pc_area == "creeks" and not creeks_sleep_available) or (sleep_options == "foggylake" and pc_area == "wanderer"):
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 45
                        label _("It’s too dangerous to stay here!"):
                            style "resting_prompt"
                        text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Foggy Lake{/color}.\n\nThankfuly, this part of the peninsula is safer than most." xmaximum 600 text_align 0.5
                        hbox:
                            xalign 0.5
                            spacing 130
                            textbutton _("Travel") action [SetVariable("travel_destination", "foggylake"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                elif (sleep_options == "galerocks" and pc_area == "beach"):
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 45
                        label _("It’s too dangerous to stay here!"):
                            style "resting_prompt"
                        text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Gale Rocks{/color}.\n\nThankfuly, this part of the peninsula is safer than most." xmaximum 600 text_align 0.5
                        hbox:
                            xalign 0.5
                            spacing 130
                            textbutton _("Travel") action [SetVariable("travel_destination", "foggylake"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                else:
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 45
                        label _("It’s too dangerous to stay here!"):
                            style "resting_prompt"
                        if sleep_options == "blindhowlers":
                            text "You can’t sleep here, but you won’t reach\nany shelter without entering\nthe heart of the woods.\n\nYou have to ride ahead blindly and\nlook for a place that will take you in." xmaximum 600 text_align 0.5
                        elif sleep_options == "blindmilitarycamp":
                            text "You can’t sleep here, but you won’t reach\nany shelter without entering\nthe heart of the woods.\n\nYou have to ride ahead blindly, and\nmaybe you’ll survive long enough\nto get to {color=#f6d6bd}Tulia’s camp{/color}." xmaximum 600 text_align 0.5
                        elif sleep_options == "militarycamp":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Tulia’s camp{/color},\nbut the creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        elif sleep_options == "peltnorth":
                            text "You can’t sleep here, but there’s still time\nto move to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Pelt of the North{/color},\nbut the creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        elif sleep_options == "druidcave":
                            text "You can’t sleep here, yet you have to find\na safe place as soon as possible.\n\nYou can find the closest shelter in {color=#f6d6bd}Druid’s Cave{/color},\nbut the creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        elif sleep_options == "howlersdell":
                            text "You can’t sleep here, yet you have to find\na safe place as soon as possible.\n\nYou can find the closest shelter in {color=#f6d6bd}Howler’s Dell{/color},\nbut the creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        elif sleep_options == "monastery":
                            text "You can’t sleep here, yet you have to find\na safe place as soon as possible.\n\nYou can find the closest shelter in {color=#f6d6bd}Monastery{/color},\nbut the creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        elif sleep_options == "abandonedwatchtower":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}the abandoned watchtower{/color},\nbut the creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        elif sleep_options == "eudociahouse":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Eudocia’s house{/color},\nbut the creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        elif sleep_options == "foggylake":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Foggy Lake{/color},\nbut the creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        elif sleep_options == "galerocks":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}Gale Rocks{/color},\nbut the creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        elif sleep_options == "whitemarshes":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at {color=#f6d6bd}White Marshes{/color},\nbut the creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        elif sleep_options == "greenmountaintribe":
                            text "You can’t sleep here, but there’s still time\nto travel to a safer spot.\n\nYou can find the closest shelter at\n{color=#f6d6bd}The Tribe of The Green Mountain{/color},\nbut the creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        elif sleep_options == "blindgreenmountaintribe":
                            text "You can’t sleep here, but you could still try\nto find shelter ahead.\nThe creatures of the night are surely going to attack you." xmaximum 600 text_align 0.5
                        if sleep_options == "blindhowlers" or sleep_options == "blindmilitarycamp":
                            $ traveldamage = 5
                            add "gui/statuspoints/hp/minus5hp.png":
                                xalign 0.5
                        elif game_mode < 3 and not world_higher_night_damage:
                            if estimatedtravel_duration <= (world_daylength+2):
                                $ traveldamage = 1
                                add "gui/statuspoints/hp/minus1hp.png":
                                    xalign 0.5
                            elif estimatedtravel_duration <= (world_daylength+4):
                                $ traveldamage = 2
                                add "gui/statuspoints/hp/minus2hp.png":
                                    xalign 0.5
                            elif estimatedtravel_duration <= (world_daylength+6):
                                $ traveldamage = 3
                                add "gui/statuspoints/hp/minus3hp.png":
                                    xalign 0.5
                            elif estimatedtravel_duration <= (world_daylength+8):
                                $ traveldamage = 4
                                add "gui/statuspoints/hp/minus4hp.png":
                                    xalign 0.5
                            else:
                                $ traveldamage = 5
                                add "gui/statuspoints/hp/minus5hp.png":
                                    xalign 0.5
                        else:
                            if estimatedtravel_duration <= (world_daylength+1):
                                $ traveldamage = 1
                                add "gui/statuspoints/hp/minus1hp.png":
                                    xalign 0.5
                            elif estimatedtravel_duration <= (world_daylength+2):
                                $ traveldamage = 2
                                add "gui/statuspoints/hp/minus2hp.png":
                                    xalign 0.5
                            elif estimatedtravel_duration <= (world_daylength+3):
                                $ traveldamage = 3
                                add "gui/statuspoints/hp/minus3hp.png":
                                    xalign 0.5
                            elif estimatedtravel_duration <= (world_daylength+4):
                                $ traveldamage = 4
                                add "gui/statuspoints/hp/minus4hp.png":
                                    xalign 0.5
                            else:
                                $ traveldamage = 5
                                add "gui/statuspoints/hp/minus5hp.png":
                                    xalign 0.5
                        hbox:
                            xalign 0.5
                            spacing 130
                            if sleep_options == "blindhowlers":
                                textbutton _("Travel") action [SetVariable("howlersdell_firsttime_night", 1), SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "howlersdell"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "blindmilitarycamp":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "militarycamp"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "militarycamp":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "militarycamp"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "peltnorth":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "peltnorth"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "druidcave":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "druidcave"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "howlersdell":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "howlersdell"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "monastery":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "monastery"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "abandonedwatchtower":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "watchtower"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "eudociahouse":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "eudociahouse"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "foggylake":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "foggylake"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "galerocks":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "galerocks"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "whitemarshes":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "whitemarshes"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "greenmountaintribe":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "greenmountaintribe"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]
                            elif sleep_options == "blindgreenmountaintribe":
                                textbutton _("Travel") action [SetVariable("pc_hp", limit_pc_hp(pc_hp-traveldamage)), SetVariable("travel_destination", "greenmountaintribe"), Hide("restscreen", transition=dissolve), Jump('finaldestinationafterevent')]

    if tt.value != "":
        frame:
            yalign 0.5
            xpadding 16
            xalign 0.0
            pos renpy.get_mouse_pos()
            if persistent.textstyle == "basic":
                top_padding 10 bottom_padding 4
                text tt.value text_align 0.5 size 24 line_spacing 8 font "philosopher.ttf"
            if persistent.textstyle == "pixel":
                top_padding 8 bottom_padding 4
                text tt.value text_align 0.5 size 28 line_spacing 8 font "munro.ttf"
    if pc_area == "galerocks" and not galerocks_fulvia_sleep:
        key "game_menu" action [SetVariable("galerocks_fulvia_firsttime", 1), Hide("restscreen", transition=dissolve)]
    else:
        key "game_menu" action Hide("restscreen", transition=dissolve)

style resting_frame is confirm_frame:
    xalign 0.5
    yalign 0.5
    xpadding 40
    ypadding 40
style resting_text is confirm_text:
    size 30
    color "#c3a38a"
    text_align 0.5
    xalign 0.5
style resting_prompt is confirm_prompt:
    xalign 0.5
style resting_prompt_text is confirm_prompt_text:
    color "#f6d6bd"
    xalign 0.5
    size 30
style resting_button_text is confirm_prompt_text:
    color "#997577"
    hover_color "#f6d6bd"
    size 30
    xalign 0.5
    text_align 0.5
