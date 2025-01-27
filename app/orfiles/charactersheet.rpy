## Initialization
init offset = -1
style charactersheet_text is default:
    # size 30
    #color '#c3a38a'
    line_spacing +4
    xalign 0.5
    text_align 0.5

style charactersheet_button is default#:
    #properties gui.button_properties("charactersheet_button")
style charactersheet_button_text is button_text:
    color '#997577'
    size 28
    hover_color '#f6d6bd'
    selected_color '#c3a38a'
    properties gui.button_text_properties("charactersheet")
    line_spacing +4
    xalign 0.0
    text_align 0.0

default sheet_description1 = ""
default sheet_description2 = ""
default sheet_description3 = ""
default sheet_description4 = ""
default sheet_description5 = ""
default sheet_description6 = ""
default sheet_description7 = ""
default sheet_description8 = ""
default sheet_description9 = ""
default sheet_description10 = ""
screen charactersheet():
    tag menu
    default tt = Tooltip("")
    on "show" action SetVariable("game_menu_screen", "charactersheet")
    on "replace" action SetVariable("game_menu_screen", "charactersheet")
    use game_menu(_("Character Sheet"), scroll="viewport"):
        style_prefix "charactersheet"
        vbox:
            ypos -30
            spacing 40
            xalign 0.0
            xpos -30
            vbox:
                xalign 0.65
                spacing 40
                # xminimum 700
                # xmaximum 700
                if pc_class == "warrior":
                    $ sheet_description1 = "After years of training to become a fighter,"
                if pc_class == "mage":
                    $ sheet_description1 = "After years of practicing with axes and magical amulets,"
                if pc_class == "scholar":
                    $ sheet_description1 = "After years spent on studying old codices and training,"
                if pc_goal == "ineedmoney":
                    $ sheet_description2 = "to gather enough dragon bones to save my sibling from debt collectors."
                if pc_goal == "iwantmoney":
                    $ sheet_description2 = "to gather enough dragon bones to retire early and live in prosperity and safety."
                if pc_goal == "iwanttoberemembered":
                    $ sheet_description2 = "to be remembered as the hero who brought peace and order to this realm."
                if pc_goal == "iwanttohelp":
                    $ sheet_description2 = "to help the local villages, and to make this region safer for the locals and newcomers alike."
                if pc_goal == "iwantstatus":
                    $ sheet_description2 = "to build connections among the leaders in the North,{size=5}\n {/size}\nand to become a major player in the merchant guild."
                if pc_goal == "iwanttostartanewlife":
                    $ sheet_description2 = "I left home to escape my difficult past."
                text _("\n{color=#f6d6bd}[pcname], the Roadwarden{/color}\n\n{i}[sheet_description1]{size=5}\n {/size}\n[sheet_description2]{/i}") text_align 0.5 xalign 0.5
            add "gui/horizontalline.png":
                xalign 0.74
            hbox:
                spacing 25
                vbox:
                    xminimum 200
                    xmaximum 200
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    if pc_class == "warrior":
                        add "gui/statuspoints/axetrue.png":
                            xalign 0.5
                            yalign 0.5
                    if pc_class == "mage":
                        add "gui/statuspoints/mana/5mana.png":
                            xalign 0.5
                            yalign 0.5
                    if pc_class == "scholar":
                        add "gui/statuspoints/scholartrue.png":
                            xalign 0.5
                            yalign 0.5
                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 15
                    if pc_class == "warrior":
                        text _("{color=#f6d6bd}Force{/color} - While your {color=#f6d6bd}vitality{/color} is above 0, you find ways to overcome physical struggles.") xalign 0.0 text_align 0.0
                        text _("{color=#f6d6bd}Advanced training{/color} - You have an advantage during physical interactions that involve random chance.") xalign 0.0 text_align 0.0
                    if pc_class == "mage":
                        text _("{color=#f6d6bd}Spells{/color} - You can spend {color=#f6d6bd}pneuma{/color} to overcome challenges with wands and amulets.") xalign 0.0 text_align 0.0
                        text _("{color=#f6d6bd}Healing ritual{/color} - Whenever you go to sleep, you can spend {color=#f6d6bd}pneuma{/color} to restore your {color=#f6d6bd}vitality{/color}.") xalign 0.0 text_align 0.0
                    if pc_class == "scholar":
                        text _("{color=#f6d6bd}Knowledge{/color} - You’re literate. Your education helps you solve many mysteries.") xalign 0.0 text_align 0.0
                        text _("{color=#f6d6bd}Alchemy{/color} - With an access to an alchemy table and proper ingredients you can brew useful balms and potions.") xalign 0.0 text_align 0.0
            if pc_class == "mage":
                add "gui/horizontalline.png":
                    xalign 0.74
                hbox:
                    spacing 25
                    vbox:
                        xminimum 200
                        xmaximum 200
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        if not mana:
                            add "gui/statuspoints/mana/0mana.png":
                                xalign 0.5
                                yalign 0.5
                        elif mana == 1:
                            add "gui/statuspoints/mana/1mana.png":
                                xalign 0.5
                                yalign 0.5
                        elif mana == 2:
                            add "gui/statuspoints/mana/2mana.png":
                                xalign 0.5
                                yalign 0.5
                        elif mana == 3:
                            add "gui/statuspoints/mana/3mana.png":
                                xalign 0.5
                                yalign 0.5
                        elif mana == 4:
                            add "gui/statuspoints/mana/4mana.png":
                                xalign 0.5
                                yalign 0.5
                        elif mana == 5:
                            add "gui/statuspoints/mana/5mana.png":
                                xalign 0.5
                                yalign 0.5
                    vbox:
                        xalign 0.0
                        yalign 0.5
                        spacing 15
                        if not mana:
                            textbutton _("Pneuma: 0/5"):
                                action NullAction()
                                hovered [tt.Action("You restore {color=#f6d6bd}pneuma{/color} by sleeping and resting,\nand spend it by casting spells.")]
                                unhovered [tt.Action("")]
                                xalign 0.0
                                text_align 0.0
                        elif mana == 1:
                            textbutton _("Pneuma: 1/5"):
                                action NullAction()
                                hovered [tt.Action("You restore {color=#f6d6bd}pneuma{/color} by sleeping and resting,\nand spend it by casting spells.")]
                                unhovered [tt.Action("")]
                                xalign 0.0
                                text_align 0.0
                        elif mana == 2:
                            textbutton _("Pneuma: 2/5"):
                                action NullAction()
                                hovered [tt.Action("You restore {color=#f6d6bd}pneuma{/color} by sleeping and resting,\nand spend it by casting spells.")]
                                unhovered [tt.Action("")]
                                xalign 0.0
                                text_align 0.0
                        elif mana == 3:
                            textbutton _("Pneuma: 3/5"):
                                action NullAction()
                                hovered [tt.Action("You restore {color=#f6d6bd}pneuma{/color} by sleeping and resting,\nand spend it by casting spells.")]
                                unhovered [tt.Action("")]
                                xalign 0.0
                                text_align 0.0
                        elif mana == 4:
                            textbutton _("Pneuma: 4/5"):
                                action NullAction()
                                hovered [tt.Action("You restore {color=#f6d6bd}pneuma{/color} by sleeping and resting,\nand spend it by casting spells.")]
                                unhovered [tt.Action("")]
                                xalign 0.0
                                text_align 0.0
                        elif mana == 5:
                            textbutton _("Pneuma: 5/5"):
                                action NullAction()
                                hovered [tt.Action("You restore {color=#f6d6bd}pneuma{/color} by sleeping and resting,\nand spend it by casting spells.")]
                                unhovered [tt.Action("")]
                                xalign 0.0
                                text_align 0.0
            add "gui/horizontalline.png":
                xalign 0.74
            hbox:
                spacing 25
                vbox:
                    xminimum 200
                    xmaximum 200
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    if not pc_hp:
                        add "gui/statuspoints/hp/0hp.png":
                            xalign 0.5
                            yalign 0.5
                    elif pc_hp == 1:
                        add "gui/statuspoints/hp/1hp.png":
                            xalign 0.5
                            yalign 0.5
                    elif pc_hp == 2:
                        add "gui/statuspoints/hp/2hp.png":
                            xalign 0.5
                            yalign 0.5
                    elif pc_hp == 3:
                        add "gui/statuspoints/hp/3hp.png":
                            xalign 0.5
                            yalign 0.5
                    elif pc_hp == 4:
                        add "gui/statuspoints/hp/4hp.png":
                            xalign 0.5
                            yalign 0.5
                    elif pc_hp == 5:
                        add "gui/statuspoints/hp/5hp.png":
                            xalign 0.5
                            yalign 0.5
                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 15
                    if not pc_hp_can5:
                        $ displayedmaxhp = 4
                    else:
                        $ displayedmaxhp = 5
                    if not pc_hp:
                        textbutton _("Vitality: 0/[displayedmaxhp]"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Vitality{/color} affects your {color=#f6d6bd}appearance{/color}\nand your random chance of success during physical struggles.\n\nLow {color=#f6d6bd}vitality{/color} stops you from engaging\nin exhausting activities, and increases\nthe chance of dying in combat.\n\nYou restore {color=#f6d6bd}vitality{/color} by sleeping and resting.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_hp == 1:
                        textbutton _("Vitality: 1/[displayedmaxhp]"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Vitality{/color} affects your {color=#f6d6bd}appearance{/color}\nand your random chance of success during physical struggles.\n\nLow {color=#f6d6bd}vitality{/color} stops you from engaging\nin exhausting activities, and increases\nthe chance of dying in combat.\n\nYou restore {color=#f6d6bd}vitality{/color} by sleeping and resting.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_hp == 2:
                        textbutton _("Vitality: 2/[displayedmaxhp]"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Vitality{/color} affects your {color=#f6d6bd}appearance{/color}\nand your random chance of success during physical struggles.\n\nLow {color=#f6d6bd}vitality{/color} stops you from engaging\nin exhausting activities, and increases\nthe chance of dying in combat.\n\nYou restore {color=#f6d6bd}vitality{/color} by sleeping and resting.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_hp == 3:
                        textbutton _("Vitality: 3/[displayedmaxhp]"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Vitality{/color} affects your {color=#f6d6bd}appearance{/color}\nand your random chance of success during physical struggles.\n\nLow {color=#f6d6bd}vitality{/color} stops you from engaging\nin exhausting activities, and increases\nthe chance of dying in combat.\n\nYou restore {color=#f6d6bd}vitality{/color} by sleeping and resting.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_hp == 4:
                        textbutton _("Vitality: 4/[displayedmaxhp]"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Vitality{/color} affects your {color=#f6d6bd}appearance{/color}\nand your random chance of success during physical struggles.\n\nLow {color=#f6d6bd}vitality{/color} stops you from engaging\nin exhausting activities, and increases\nthe chance of dying in combat.\n\nYou restore {color=#f6d6bd}vitality{/color} by sleeping and resting.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_hp == 5:
                        textbutton _("Vitality: 5/[displayedmaxhp]"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Vitality{/color} affects your {color=#f6d6bd}appearance{/color}\nand your random chance of success during physical struggles.\n\nLow {color=#f6d6bd}vitality{/color} stops you from engaging\nin exhausting activities, and increases\nthe chance of dying in combat.\n\nYou restore {color=#f6d6bd}vitality{/color} by sleeping and resting.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
            add "gui/horizontalline.png":
                xalign 0.74
            hbox:
                spacing 25
                vbox:
                    xminimum 200
                    xmaximum 200
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    if not pc_food:
                        add "gui/statuspoints/food/0food.png":
                            xalign 0.5
                            yalign 0.5
                    elif pc_food == 1:
                        add "gui/statuspoints/food/1food.png":
                            xalign 0.5
                            yalign 0.5
                    elif pc_food == 2:
                        add "gui/statuspoints/food/2food.png":
                            xalign 0.5
                            yalign 0.5
                    elif pc_food == 3:
                        add "gui/statuspoints/food/3food.png":
                            xalign 0.5
                            yalign 0.5
                    elif pc_food == 4:
                        add "gui/statuspoints/food/4food.png":
                            xalign 0.5
                            yalign 0.5
                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 15
                    if not pc_food:
                        textbutton _("Nourishment: 0/4"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Nourishment{/color} affects your random chance\nof success during physical struggles.\nOn levels 1 and 0, {color=#f6d6bd}nourishment{/color} stops you\nfrom restoring health while sleeping or resting.\n\nYou lose {color=#f6d6bd}nourishment{/color} when you sleep\nor exhaust yourself,\nand gain it whenever you eat.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_food == 1:
                        textbutton _("Nourishment: 1/4"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Nourishment{/color} affects your random chance\nof success during physical struggles.\nOn levels 1 and 0, {color=#f6d6bd}nourishment{/color} stops you\nfrom restoring health while sleeping or resting.\n\nYou lose {color=#f6d6bd}nourishment{/color} when you sleep\nor exhaust yourself,\nand gain it whenever you eat.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_food == 2:
                        textbutton _("Nourishment: 2/4"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Nourishment{/color} affects your random chance\nof success during physical struggles.\nOn levels 1 and 0, {color=#f6d6bd}nourishment{/color} stops you\nfrom restoring health while sleeping or resting.\n\nYou lose {color=#f6d6bd}nourishment{/color} when you sleep\nor exhaust yourself,\nand gain it whenever you eat.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_food == 3:
                        textbutton _("Nourishment: 3/4"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Nourishment{/color} affects your random chance\nof success during physical struggles.\nOn levels 1 and 0, {color=#f6d6bd}nourishment{/color} stops you\nfrom restoring health while sleeping or resting.\n\nYou lose {color=#f6d6bd}nourishment{/color} when you sleep\nor exhaust yourself,\nand gain it whenever you eat.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_food == 4:
                        textbutton _("Nourishment: 4/4"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Nourishment{/color} affects your random chance\nof success during physical struggles.\nOn levels 1 and 0, {color=#f6d6bd}nourishment{/color} stops you\nfrom restoring health while sleeping or resting.\n\nYou lose {color=#f6d6bd}nourishment{/color} when you sleep\nor take part in exhausting labor,\nand gain it whenever you eat.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
            add "gui/horizontalline.png":
                xalign 0.74
            hbox:
                spacing 25
                vbox:
                    xminimum 200
                    xmaximum 200
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    if not armor:
                        add "gui/statuspoints/armor/0armor.png":
                            xalign 0.5
                            yalign 0.5
                    elif armor == 1:
                        add "gui/statuspoints/armor/1armor.png":
                            xalign 0.5
                            yalign 0.5
                    elif armor == 2:
                        add "gui/statuspoints/armor/2armor.png":
                            xalign 0.5
                            yalign 0.5
                    elif armor == 3:
                        if not armor_can4:
                            add "gui/statuspoints/armor/3armormax.png":
                                xalign 0.5
                                yalign 0.5
                        elif armor_can4:
                            add "gui/statuspoints/armor/3armor.png":
                                xalign 0.5
                                yalign 0.5
                    elif armor == 4:
                        add "gui/statuspoints/armor/4armor.png":
                            xalign 0.5
                            yalign 0.5
                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 15
                    if not armor:
                        textbutton _("Armor: 0/4"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Armor{/color} reduces {color=#f6d6bd}vitality{/color} losses in combat,\nand can be fixed with proper tools or by tailors.\n\nThe 4th level of {color=#f6d6bd}armor{/color} is unavailable\nat the start of the game, but\nwill give you a better chance of success during physical\ninteractions that involve random chance.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif armor == 1:
                        textbutton _("Armor: 1/4"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Armor{/color} reduces {color=#f6d6bd}vitality{/color} losses in combat,\nand can be fixed with proper tools or by tailors.\n\nThe 4th level of {color=#f6d6bd}armor{/color} is unavailable\nat the start of the game, but\nwill give you a better chance of success during physical\ninteractions that involve random chance.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif armor == 2:
                        textbutton _("Armor: 2/4"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Armor{/color} reduces {color=#f6d6bd}vitality{/color} losses in combat,\nand can be fixed with proper tools or by tailors.\n\nThe 4th level of {color=#f6d6bd}armor{/color} is unavailable\nat the start of the game, but\nwill give you a better chance of success during physical\ninteractions that involve random chance.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif armor == 3:
                        if not armor_can4:
                            textbutton _("Armor: 3/4"):
                                action NullAction()
                                hovered [tt.Action("{color=#f6d6bd}Armor{/color} reduces {color=#f6d6bd}vitality{/color} losses in combat,\nand can be fixed with proper tools or by tailors.\n\nThe 4th level of {color=#f6d6bd}armor{/color} is unavailable\nat the start of the game, but\nwill give you a better chance of success during physical\ninteractions that involve random chance.")]
                                unhovered [tt.Action("")]
                                xalign 0.0
                                text_align 0.0
                        elif armor_can4:
                            textbutton _("Armor: 3/4"):
                                action NullAction()
                                hovered [tt.Action("{color=#f6d6bd}Armor{/color} reduces {color=#f6d6bd}vitality{/color} losses in combat,\nand can be fixed with proper tools or by tailors.\n\nThe 4th level of {color=#f6d6bd}armor{/color} is unavailable\nat the start of the game, but\nwill give you a better chance of success during physical\ninteractions that involve random chance.")]
                                unhovered [tt.Action("")]
                                xalign 0.0
                                text_align 0.0
                    elif armor == 4:
                        textbutton _("Armor: 4/4"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Armor{/color} reduces {color=#f6d6bd}vitality{/color} losses in combat,\nand can be fixed with proper tools or by tailors.\n\nThe 4th level of {color=#f6d6bd}armor{/color} gives you a better chance\nof success during physical interactions\nthat involve random chance.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
            add "gui/horizontalline.png":
                xalign 0.74
            hbox:
                spacing 25
                vbox:
                    xminimum 200
                    xmaximum 200
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    if not appearance:
                        add "gui/statuspoints/appearance/0appearance.png":
                            xalign 0.5
                            yalign 0.5
                    elif appearance == 1:
                        add "gui/statuspoints/appearance/1appearance.png":
                            xalign 0.5
                            yalign 0.5
                    elif appearance == 2:
                        add "gui/statuspoints/appearance/2appearance.png":
                            xalign 0.5
                            yalign 0.5
                    elif appearance == 3:
                        add "gui/statuspoints/appearance/3appearance.png":
                            xalign 0.5
                            yalign 0.5
                    elif appearance == 4:
                        add "gui/statuspoints/appearance/4appearance.png":
                            xalign 0.5
                            yalign 0.5
                    elif appearance == 5:
                        add "gui/statuspoints/appearance/5appearance.png":
                            xalign 0.5
                            yalign 0.5
                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 15
                    if not appearance:
                        textbutton _("Appearance: 0/5"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Appearance{/color} affects your influence on others,\nas well as prices in shops.\n\nIt’s based on your {color=#f6d6bd}cleanliness{/color}, {color=#f6d6bd}vitality{/color}, and outfit.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif appearance == 1:
                        textbutton _("Appearance: 1/5"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Appearance{/color} affects your influence on others,\nas well as prices in shops.\n\nIt’s based on your {color=#f6d6bd}cleanliness{/color}, {color=#f6d6bd}vitality{/color}, and outfit.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif appearance == 2:
                        textbutton _("Appearance: 2/5"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Appearance{/color} affects your influence on others,\nas well as prices in shops.\n\nIt’s based on your {color=#f6d6bd}cleanliness{/color}, {color=#f6d6bd}vitality{/color}, and outfit.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif appearance == 3:
                        textbutton _("Appearance: 3/5"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Appearance{/color} affects your influence on others,\nas well as prices in shops.\n\nIt’s based on your {color=#f6d6bd}cleanliness{/color}, {color=#f6d6bd}vitality{/color}, and outfit.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif appearance == 4:
                        textbutton _("Appearance: 4/5"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Appearance{/color} affects your influence on others,\nas well as prices in shops.\n\nIt’s based on your {color=#f6d6bd}cleanliness{/color}, {color=#f6d6bd}vitality{/color}, and outfit.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif appearance == 5:
                        textbutton _("Appearance: 5/5"):
                            action NullAction()
                            hovered [tt.Action("{color=#f6d6bd}Appearance{/color} affects your influence on others,\nas well as prices in shops.\n\nIt’s based on your {color=#f6d6bd}cleanliness{/color}, {color=#f6d6bd}vitality{/color}, and outfit.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0

                    if not cleanliness:
                        textbutton _("+0 - Cleanliness: 0/3"):
                            action NullAction()
                            hovered [tt.Action("You lose {color=#f6d6bd}cleanliness{/color} when you sleep\nor engage in tiresome activities.\n\nYou can wash yourself in safe water sources.\nYou will do so more efficiently\nwith special equipment.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif cleanliness == 1:
                        textbutton _("+1 - Cleanliness: 1/3"):
                            action NullAction()
                            hovered [tt.Action("You lose {color=#f6d6bd}cleanliness{/color} when you sleep\nor engage in tiresome activities.\n\nYou can wash yourself in safe water sources.\nYou will do so more efficiently\nwith special equipment.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif cleanliness == 2:
                        textbutton _("+2 - Cleanliness: 2/3"):
                            action NullAction()
                            hovered [tt.Action("You lose {color=#f6d6bd}cleanliness{/color} when you sleep\nor engage in tiresome activities.\n\nYou can wash yourself in safe water sources.\nYou will do so more efficiently\nwith special equipment.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif cleanliness == 3:
                        textbutton _("+3 - Cleanliness: 3/3"):
                            action NullAction()
                            hovered [tt.Action("You lose {color=#f6d6bd}cleanliness{/color} when you sleep\nor engage in tiresome activities.\n\nYou can wash yourself in safe water sources.\nYou will do so more efficiently\nwith special equipment.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0

                    if pc_hp >= 4:
                        text _("+1 - High {color=#f6d6bd}vitality{/color}.") xalign 0.0 text_align 0.0
                    elif not pc_hp:
                        text _("-1 - Low {color=#f6d6bd}vitality{/color}.") xalign 0.0 text_align 0.0
                    else:
                        text _("{color=#6a6a6a}+0 - Regular vitality.{/color}") xalign 0.0 text_align 0.0

                    if not item_fancyclothes:
                        if not cleanliness_clothes_torn:
                            text _("{color=#6a6a6a}-0 - Your clothes need no special repairs.{/color}") xalign 0.0 text_align 0.0
                        elif cleanliness_clothes_torn:
                            text _("-1 - Your clothes are torn and worn.") xalign 0.0 text_align 0.0
                        if not cleanliness_clothes_blood:
                            text _("{color=#6a6a6a}-0 - Your clothes are not stained with blood.{/color}") xalign 0.0 text_align 0.0
                        elif cleanliness_clothes_torn:
                            text _("-0 - Your clothes are stained with blood.") xalign 0.0 text_align 0.0
                        text _("{color=#6a6a6a}+0 - You’ve got a regular outfit.{/color}") xalign 0.0 text_align 0.0
                    else:
                        if not cleanliness_clothes_torn and not cleanliness_clothes_blood:
                            text _("+1 - You possess a fancy outfit.") xalign 0.0 text_align 0.0
                        elif cleanliness_clothes_torn and cleanliness_clothes_blood:
                            text _("+1 - Your regular clothes are torn and stained with blood, but your fancy outfit hides them.") xalign 0.0 text_align 0.0
                        elif cleanliness_clothes_torn:
                            text _("+1 - Your regular clothes are torn, but your fancy outfit hides them.") xalign 0.0 text_align 0.0
                        elif cleanliness_clothes_blood:
                            text _("+1 - Your regular clothes are stained with blood, but your fancy outfit hides them.") xalign 0.0 text_align 0.0
            add "gui/horizontalline.png":
                xalign 0.74
            hbox:
                spacing 25
                vbox:
                    xminimum 200
                    xmaximum 200
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    text _("Combat\nexperience")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 15
                    if (pc_battlecounter >= 15 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 35 and item_sharpeningpotion_used == day):
                        $ sheet_description4 = "worryingly high"
                    elif (pc_battlecounter >= 12 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 32 and item_sharpeningpotion_used == day):
                        $ sheet_description4 = "high"
                    elif (pc_battlecounter >= 9 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 29 and item_sharpeningpotion_used == day):
                        $ sheet_description4 = "advanced"
                    elif (pc_battlecounter >= 6 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 26 and item_sharpeningpotion_used == day):
                        $ sheet_description4 = "average"
                    elif (pc_battlecounter >= 3 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 23 and item_sharpeningpotion_used == day):
                        $ sheet_description4 = "small"
                    elif (pc_battlecounter >= 1 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 21 and item_sharpeningpotion_used == day):
                        $ sheet_description4 = "slight"
                    elif (pc_battlecounter >= 0 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 0 and item_sharpeningpotion_used == 0) or (pc_battlecounter >= 20 and item_sharpeningpotion_used == day):
                        $ sheet_description4 = "none"
                    textbutton _("[sheet_description4]"):
                        action NullAction()
                        hovered [tt.Action("Engaging in combat helps you during\nfuture fights that involve random chance.")]
                        unhovered [tt.Action("")]
                        xalign 0.0
                        text_align 0.0
            add "gui/horizontalline.png":
                xalign 0.74
            hbox:
                spacing 25
                vbox:
                    xminimum 200
                    xmaximum 200
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    text _("Spared\nanimals")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 15
                    if achievement_animalssavedpoints >= 9:
                        $ sheet_description5 = "surprisingly many"
                    elif achievement_animalssavedpoints >= 7:
                        $ sheet_description5 = "many"
                    elif achievement_animalssavedpoints >= 5:
                        $ sheet_description5 = "quite a few"
                    elif achievement_animalssavedpoints >= 3:
                        $ sheet_description5 = "some"
                    elif achievement_animalssavedpoints >= 1:
                        $ sheet_description5 = "hardly any"
                    elif achievement_animalssavedpoints <= 0:
                        $ sheet_description5 = "none"
                    textbutton _("[sheet_description5]"):
                        action NullAction()
                        hovered [tt.Action("Depending on your beliefs, saving and sparing animals\neither makes you a weakling, or soothes your soul.")]
                        unhovered [tt.Action("")]
                        xalign 0.0
                        text_align 0.0
            add "gui/horizontalline.png":
                xalign 0.74
            hbox:
                spacing 25
                vbox:
                    xminimum 200
                    xmaximum 200
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    text _("Religion")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 15
                    if pc_religion == "theunitedchurch":
                        textbutton _("Unite - a member of The United Church"):
                            action NullAction()
                            hovered [tt.Action("You pray to The Wright and follow The River of Order.\nLike most cityfolk, you believe that people should\nunite their strength to overcome the\nthreats of nature and dark magic.\nEveryone will be judged for both good and evil deeds.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_religion == "ordersoftruth":
                        textbutton _("Seeker - a member of an Order of Truth"):
                            action NullAction()
                            hovered [tt.Action("You pray to The Wright and follow The River of Truth.\nFor many years you’ve supported a monastery\nthat does its best to advance mankind’s\nspiritual growth, artistry, herbalism, and magical research.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_religion == "fellowship":
                        textbutton _("Eremite - a member of a fellowship"):
                            action NullAction()
                            hovered [tt.Action("You pray to The Wright and follow The River of Freedom.\nYou’re from a small village and you believe that\nthe freedom of shell, pneuma, and soul\nare the main virtues of life.\nYour community is unique and independent,\nand so are its members.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_religion == "pagan":
                        textbutton _("“pagan” - the path of your ancestors"):
                            action NullAction()
                            hovered [tt.Action("You have a strong connection to nature and spirits.\nYour vanishing traditions are forbidden in The Ten Cities,\nand seen by some as sinister and treacherous.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_religion == "none":
                        textbutton _("atheist"):
                            action NullAction()
                            hovered [tt.Action("You reject the existence of gods and spirits.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                    elif pc_religion == "unknown":
                        text _("{color=#6a6a6a}unspecified{/color}") xalign 0.0 text_align 0.0
            add "gui/horizontalline.png":
                xalign 0.74
            if pc_religion == "theunitedchurch" or pc_religion == "ordersoftruth" or pc_religion == "fellowship" or pc_religion == "pagan":
                hbox:
                    spacing 25
                    vbox:
                        xminimum 200
                        xmaximum 200
                        spacing 15
                        xalign 0.5
                        yalign 0.5
                        text _("Faith")
                    vbox:
                        xalign 0.0
                        yalign 0.5
                        spacing 15
                        if description_druids10 and pc_religion == "theunitedchurch":
                            $ sheet_description6 = "{color=#c3a38a}Ever since you supported the local druids,\nmost Unites would consider you a heretic.{/color}"
                        elif pc_faithpoints < 0 and pc_faithpoints_opportunities >= 5:
                            $ sheet_description6 = "weak"
                        elif pc_faithpoints_opportunities >= 8:
                            if pc_faithpoints >= pc_faithpoints_opportunities:
                                $ sheet_description6 = "exemplary"
                            elif pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                                $ sheet_description6 = "strong"
                            elif pc_faithpoints >= (pc_faithpoints_opportunities*0.5):
                                $ sheet_description6 = "decent"
                            elif pc_faithpoints >= (pc_faithpoints_opportunities*0.25):
                                $ sheet_description6 = "struggling"
                            else:
                                $ sheet_description6 = "weak"
                        else:
                            $ sheet_description6 = "undetermined"
                        textbutton _("[sheet_description6]"):
                            action NullAction()
                            if sheet_description6 == "{color=#c3a38a}Ever since you supported the local druids,\nmost Unites would consider you a heretic.{/color}":
                                hovered NullAction()
                            else:
                                hovered [tt.Action("The strength of your religious conviction\nis measured by your actions and judgments.")]
                            unhovered [tt.Action("")]
                            xalign 0.0
                            text_align 0.0
                add "gui/horizontalline.png":
                    xalign 0.74
            hbox:
                spacing 25
                vbox:
                    xminimum 200
                    xmaximum 200
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    text _("Lies")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 15
                    if pc_lies >= 20:
                        $ sheet_description7 = "out of control"
                    elif pc_lies >= 16:
                        $ sheet_description7 = "a whole lot"
                    elif pc_lies >= 12:
                        $ sheet_description7 = "quite a bunch"
                    elif pc_lies >= 8:
                        $ sheet_description7 = "quite a few"
                    elif pc_lies >= 5:
                        $ sheet_description7 = "some"
                    elif pc_lies >= 1:
                        $ sheet_description7 = "hardly any"
                    elif pc_lies <= 0:
                        $ sheet_description7 = "none"
                    textbutton _("[sheet_description7]"):
                        action NullAction()
                        hovered [tt.Action("Lying gives you quick benefits,\nbut may turn against you after some time.\n\nSome lies are difficult to pull off\nfor an unexperienced liar.")]
                        unhovered [tt.Action("")]
                        xalign 0.0
                        text_align 0.0
            add "gui/horizontalline.png":
                xalign 0.74
            hbox:
                spacing 25
                vbox:
                    xminimum 200
                    xmaximum 200
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    text _("Sewing\nexperience")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 15
                    if armor_fixingxp >= 15:
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
                    textbutton _("[sheet_description8]"):
                        action NullAction()
                        hovered [tt.Action("Your practice with fixing your clothes\nand armor with the usage of proper tools.")]
                        unhovered [tt.Action("")]
                        xalign 0.0
                        text_align 0.0
            add "gui/horizontalline.png":
                xalign 0.74
            hbox:
                spacing 25
                vbox:
                    xminimum 200
                    xmaximum 200
                    spacing 15
                    xalign 0.5
                    yalign 0.5
                    text _("Gambling\nexperience")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 15
                    if pc_gamblingxp_scholarbonus:
                        if pc_gamblingxp >= 45:
                            $ sheet_description9 = "worryingly high"
                        elif pc_gamblingxp >= 40:
                            $ sheet_description9 = "high"
                        elif pc_gamblingxp >= 35:
                            $ sheet_description9 = "advanced"
                        elif pc_gamblingxp >= 30:
                            $ sheet_description9 = "average"
                        elif pc_gamblingxp >= 25:
                            $ sheet_description9 = "small"
                        elif pc_gamblingxp >= 20:
                            $ sheet_description9 = "slight"
                        elif pc_gamblingxp >= 16:
                            $ sheet_description9 = "negligible"
                        elif pc_gamblingxp <= 15:
                            $ sheet_description9 = "none"
                    else:
                        if pc_gamblingxp >= 30:
                            $ sheet_description9 = "worryingly high"
                        elif pc_gamblingxp >= 25:
                            $ sheet_description9 = "high"
                        elif pc_gamblingxp >= 20:
                            $ sheet_description9 = "advanced"
                        elif pc_gamblingxp >= 15:
                            $ sheet_description9 = "average"
                        elif pc_gamblingxp >= 10:
                            $ sheet_description9 = "small"
                        elif pc_gamblingxp >= 5:
                            $ sheet_description9 = "slight"
                        elif pc_gamblingxp >= 1:
                            $ sheet_description9 = "negligible"
                        elif pc_gamblingxp <= 0:
                            $ sheet_description9 = "none"
                    textbutton _("[sheet_description9]"):
                        action NullAction()
                        hovered [tt.Action("Helps you in luck-based games of dice.")]
                        unhovered [tt.Action("")]
                        xalign 0.0
                        text_align 0.0

    if tt.value != "":
        frame:
            xpadding 20
            yalign 0.8
            top_padding 15
            bottom_padding 10
            pos renpy.get_mouse_pos()
            xanchor -75
            if persistent.textstyle == "basic":
                text tt.value text_align 0.5 line_spacing 10 font "philosopher.ttf"
            if persistent.textstyle == "pixel":
                text tt.value text_align 0.5 line_spacing 10 font "munro.ttf"
