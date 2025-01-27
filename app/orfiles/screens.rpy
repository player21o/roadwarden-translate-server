init +1 python:
    class LoadMostRecent(Action):
        def __init__(self):#\q+ (r"\d+")
            self.slot = renpy.newest_slot("[^_a]")
        def __call__(self):
            renpy.load(self.slot)
        def get_sensitive(self):
            return self.slot is not None

## Initialization
init offset = -1

## Styles

style default:
    properties gui.text_properties()
    language gui.language
style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False
style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
style gui_text:
    properties gui.text_properties("interface")
style button:
    properties gui.button_properties("button")
style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
style prompt_text is gui_text:
    properties gui.text_properties("prompt")
style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

## Say screen
screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
    # key "mouseup_1" action dismiss
    # = [ '', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT' ],
## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label
style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
#    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding
style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

## Input screen

screen input(prompt):
    style_prefix "input"
    vbox:
        xalign 0.0
        xpos 716
        xmaximum 800
        xsize 800
        ypos 63
        text prompt style "input_prompt"
        input id "input" style "input_text"
        text "\n" size 2
        textbutton _("Confirm") action GetText("input","input") text_style "input_confirm_text" text_slow_cps True xpos -7

style input_prompt is default:
    line_spacing 20
style input_prompt_text:
    properties gui.text_properties("input_prompt")
    size 30
style input_text:
    xmaximum 800
    xalign 0.0
    size 30
    color "#f6d6bd"
style input_confirm_text is button_text:
    properties gui.button_text_properties("nvl_button")
    hover_color '#f6d6bd'
    size 30

## Choice screen
screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action text_slow_cps True

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True
style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text
style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing gui.choice_spacing
style choice_button is default:
    properties gui.button_properties("choice_button")
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## Quick Menu screen

default autosaveswitch = 0
screen quick_menu():
    zorder 100
    default tt = Tooltip("")
    if quick_menu:
        vbox:#quick menu lewo
            style_prefix "quick"
            xalign 0.0
            yalign 0.0
            xpos 1558
            ypos 63
            if persistent.textstyle == "basic":
                spacing 8
            if persistent.textstyle == "pixel":
                spacing 10
            ########
            if not endgame_mode:
                if tutorial_sheet and persistent.tutorial_display:
                    textbutton _("Character"):
                        if tutorial_sheet_display == 1:
                            action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('charactersheet'), SetVariable("tutorial_sheet_display", 0), With(dissolve)] style_prefix "quicktutorial"
                        else:
                            action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('charactersheet'), With(dissolve)]
                elif not persistent.tutorial_display:
                    textbutton _("Character"):
                        if tutorial_sheet:
                            action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('charactersheet'), With(dissolve)]
            if isinventory and persistent.tutorial_display:
                if tutorial_inventory == 1:
                    textbutton _("Inventory") action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('inventory'), SetVariable("tutorial_inventory", 0)] style_prefix "quicktutorial"
                else:
                    textbutton _("Inventory") action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('inventory')]
            elif not persistent.tutorial_display:
                textbutton _("Inventory") action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('inventory')]
            if not endgame_mode:
                textbutton _("Wait"):
                    if not pc_area == "bogroad" and not pc_area == "bogcrossroads" and not pc_area == "peatfield" and not pc_area == "whitemarshes":
                        if can_leave and quarters < world_daylength and waitunlocked:
                            action [SelectedIf(interface_menuscreenbypas==True), Show('waitscreen'), With(dissolve)]
                    else:
                        if can_leave and quarters < world_daylength-4 and waitunlocked:
                            action [SelectedIf(interface_menuscreenbypas==True), Show('waitscreen'), With(dissolve)]
            if not endgame_mode:
                if mapunlocked and persistent.tutorial_display:
                    if can_leave and quarters < world_daylength:
                        textbutton _("Travel"):
                                if tutorial_map == 1:
                                    action [Show('map_display'), SetVariable("tutorial_map", 0), With(dissolve)] style_prefix "quicktutorial"
                                elif tutorial_map == 3:
                                    action [Show('map_display'), SetVariable("tutorial_map", 0), With(dissolve)] style_prefix "quicktutorial"
                                elif not pc_area == "bogroad" and not pc_area == "bogcrossroads" and not pc_area == "peatfield" and not pc_area == "whitemarshes":
                                    if quarters < world_daylength:
                                        action [Show('map_display'), With(dissolve)] style_prefix "quicktutorial"
                                else:
                                    if quarters < world_daylength-4:
                                        action [Show('map_display'), With(dissolve)] style_prefix "quicktutorial"
                    else:
                        textbutton _("Map"):
                            action [Show('map_onlyview'), With(dissolve)]
                elif not persistent.tutorial_display:
                    if can_leave and quarters < world_daylength:
                        textbutton _("Travel"):
                            if not pc_area == "bogroad" and not pc_area == "bogcrossroads" and not pc_area == "peatfield" and not pc_area == "whitemarshes":
                                if quarters < world_daylength:
                                    action [Show('map_display'), With(dissolve)] style_prefix "quicktutorial"
                            else:
                                if quarters < world_daylength-4:
                                    action [Show('map_display'), With(dissolve)] style_prefix "quicktutorial"
                    else:
                        textbutton _("Map"):
                            action [Show('map_onlyview'), With(dissolve)]
            if not endgame_mode:
                if restunlocked and persistent.tutorial_display:
                    if (pc_area == "militarycamp" and not tutorial_finished) or (pc_area == "militarycamp" and not militarycamp_destroyed and not (day >= militarycamp_destroyed_day)) or (pc_area == "howlersdell") or (pc_area == "foggylake") or (pc_area == "peltnorth" and not peltnorth_ban_perm) or (pc_area == "druidcave" and druidcave_cave_open) or (pc_area == "monastery" and monastery_sleep_unlocked) or (pc_area == "watchtower" and watchtower_open) or (pc_area == "eudociahouse" and eudocia_sleep_available and not eudocia_ban) or (pc_area == "eudociahouseinside" and eudocia_sleep_available and not eudocia_ban) or (pc_area == "galerocks") or (pc_area == "whitemarshes" and whitemarshes_rest_unlocked) or (pc_area == "greenmountaintribe" and greenmountaintribe_sleep and not greenmountaintribe_banned) or (pc_area == "creeks" and creeks_sleep_available):
                        if (quarters >= (world_daylength-12)):
                            textbutton _("Sleep"):
                                if can_rest:
                                    if tutorial_sleep == 1:
                                        action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), SetVariable("tutorial_sleep", 0), With(dissolve)] style_prefix "quicktutorial"
                                    elif not tutorial_lateevening and day == 1:
                                        action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), SetVariable("tutorial_lateevening", 1), With(dissolve)] style_prefix "quicktutorial"
                                    else:
                                        action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), With(dissolve)] style_prefix "quicktutorial"
                        elif quarters < 40 and pc_area == "howlersdell" and howlersdell_eryx_about_room and not quest_ruins_choice == "thais_won" and not quest_ruins_choice == "thais_alliance_fail" and not thais_bigmad_beaten:
                            textbutton _("Rest"):
                                if can_rest:
                                    if not tutorial_restatinn:
                                        action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), SetVariable("tutorial_restatinn", 1), With(dissolve)] style_prefix "quicktutorial"
                                    else:
                                        action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), With(dissolve)] style_prefix "quicktutorial"
                        elif (quarters < 36 and pc_area == "peltnorth" and peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day) or (quarters < 36 and pc_area == "foggylake" and foggy_about_shelter):
                            textbutton _("Rest"):
                                if can_rest:
                                    if not tutorial_restatinn:
                                        action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), SetVariable("tutorial_restatinn", 1), With(dissolve)] style_prefix "quicktutorial"
                                    else:
                                        action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), With(dissolve)] style_prefix "quicktutorial"
                        else:
                            textbutton _("{color=#4c4c4c}Sleep{/color}") action NullAction()
                    else:
                        textbutton _("Seek Shelter"):
                            if can_rest:
                                if (quarters >= (world_daylength-12)) or (world_daylength_bogs and quarters >= (world_daylength-16)):
                                    if tutorial_sleep == 1:
                                        action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), SetVariable("tutorial_sleep", 0), With(dissolve)] style_prefix "quicktutorial"
                                    elif not tutorial_lateevening and day == 1:
                                        action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), SetVariable("tutorial_lateevening", 1), With(dissolve)] style_prefix "quicktutorial"
                                    else:
                                        action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), With(dissolve)] style_prefix "quicktutorial"
                elif not persistent.tutorial_display:
                    if (pc_area == "militarycamp" and not tutorial_finished) or (pc_area == "militarycamp" and not militarycamp_destroyed and not (day >= militarycamp_destroyed_day)) or (pc_area == "howlersdell") or (pc_area == "foggylake") or (pc_area == "peltnorth" and not peltnorth_ban_perm) or (pc_area == "druidcave" and druidcave_cave_open) or (pc_area == "monastery" and monastery_sleep_unlocked) or (pc_area == "watchtower" and watchtower_open) or (pc_area == "eudociahouse" and eudocia_sleep_available and not eudocia_ban) or (pc_area == "eudociahouseinside" and eudocia_sleep_available and not eudocia_ban) or (pc_area == "galerocks") or (pc_area == "whitemarshes" and whitemarshes_rest_unlocked) or (pc_area == "greenmountaintribe" and greenmountaintribe_sleep and not greenmountaintribe_banned) or (pc_area == "creeks" and creeks_sleep_available):
                        if (quarters >= (world_daylength-12)):
                            textbutton _("Sleep"):
                                if can_rest:
                                    action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), With(dissolve)] style_prefix "quicktutorial"
                        elif quarters < 40 and pc_area == "howlersdell" and howlersdell_eryx_about_room and not quest_ruins_choice == "thais_won" and not quest_ruins_choice == "thais_alliance_fail" and not thais_bigmad_beaten:
                            textbutton _("Rest"):
                                action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), With(dissolve)] style_prefix "quicktutorial"
                        elif (quarters < 36 and pc_area == "peltnorth" and peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day) or (quarters < 36 and pc_area == "foggylake" and foggy_about_shelter):
                            textbutton _("Rest"):
                                action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), With(dissolve)] style_prefix "quicktutorial"
                        else:
                            textbutton _("{color=#4c4c4c}Sleep{/color}") action NullAction()
                    else:
                        textbutton _("Seek Shelter"):
                            if (can_rest and quarters >= (world_daylength-12)) or (can_rest and world_daylength_bogs and quarters >= (world_daylength-16)):
                                action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), With(dissolve)] style_prefix "quicktutorial"
        vbox: #quick menu prawo
            style_prefix "quick"
            xalign 0.0
            yalign 0.0
            xpos 1736
            ypos 63
            if persistent.textstyle == "basic":
                spacing 8
            if persistent.textstyle == "pixel":
                spacing 10
            textbutton _("Settings") action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('preferences')]
            textbutton _("Q. Save") action QuickSave()
            textbutton _("Q. Load") action QuickLoad()
            if tutorial_archive == 1 and persistent.tutorial_display:
                textbutton _("Archive") action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('history'), SetVariable("tutorial_archive", 0)] style_prefix "quicktutorial"
            else:
                textbutton _("Archive") action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('history')]
            if isjournal and persistent.tutorial_display:
                if tutorial_journal == 1:
                    textbutton _("Journal") action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('journal'), SetVariable("tutorial_journal", 2)] style_prefix "quicktutorial"
                else:
                    textbutton _("Journal") action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('journal')]
            elif not persistent.tutorial_display:
                textbutton _("Journal") action [SelectedIf(interface_menuscreenbypas==True), ShowMenu('journal')]
        if autosave_counter >= 30:
            timer 0.5 repeat False action [SetVariable("autosave_switch", 1), SetVariable("autosave_counter", 0)]
        if autosave_switch:
            timer 3.0 repeat False action [Function(renpy.force_autosave), SetVariable("autosave_switch", 0), SetVariable("autosave_counter", 0)]
        ######
        timer 0.5 repeat True action [SetVariable("appearance", calculate_appearance(0)), SetVariable("appearance_charisma", calculate_appearance_charisma(0)), SetVariable("appearance_price", calculate_appearance_price(0))]
        if watchtower_firsttime and stonebridge_firsttime >= 2 and huntercabin_firsttime >= 2 and wanderer_firsttime and foragingground_firsttime and not elah_quest_easternpath_fallentree_roadknown:
            timer 0.5 repeat True action [SetVariable("elah_quest_easternpath_fallentree_roadknown", 1)]
        if foggy_friendship_tradepoints >= foggy_friendship_tradepoints_threshold:
            timer 0.5 repeat True action [SetVariable("foggy_friendship_tradepoints", foggy_friendship_tradepoints-foggy_friendship_tradepoints_threshold), SetVariable("foggy_friendship_tradepoints_threshold", foggy_friendship_tradepoints_threshold+1)]
        ######
        if description_highisland00 or description_highisland01:
            if (can_leave and quest_asterion == 1 and asterion_highisland_clues >= 3 and highisland_howtoreach_pcknows and world_popupnarration_name == 0 and world_popupnarration_highisland1 and not world_popupnarration_highisland2) or (pc_area == "shortcut-cairn" and quest_asterion == 1 and asterion_highisland_clues >= 3 and highisland_howtoreach_pcknows and world_popupnarration_name == 0 and world_popupnarration_highisland1 and not world_popupnarration_highisland2): # learned just now, now needs to gather the crew
                timer 0.1 repeat False action [Show('world_popupnarration_box'), SetVariable("world_popupnarration_name", "gatherthecrew"), With(dissolve)]
            elif (can_leave and quest_asterion == 1 and asterion_highisland_clues >= 3 and highisland_howtoreach_pcknows and world_popupnarration_name == 0 and not world_popupnarration_highisland1 and not world_popupnarration_highisland2) or (pc_area == "shortcut-cairn" and quest_asterion == 1 and asterion_highisland_clues >= 3 and highisland_howtoreach_pcknows and world_popupnarration_name == 0 and not world_popupnarration_highisland1 and not world_popupnarration_highisland2): # learned before, just needs to gather the crew
                timer 0.1 repeat False action [Show('world_popupnarration_box'), SetVariable("world_popupnarration_name", "gatherthecrewskippedstep"), With(dissolve)]
            elif (can_leave and quest_asterion == 1 and asterion_highisland_clues >= 3 and not highisland_howtoreach_pcknows and world_popupnarration_name == 0 and not world_popupnarration_highisland1) or (pc_area == "shortcut-cairn" and quest_asterion == 1 and asterion_highisland_clues >= 3 and not highisland_howtoreach_pcknows and world_popupnarration_name == 0 and not world_popupnarration_highisland1): # learn, how to reach high island
                timer 0.1 repeat False action [Show('world_popupnarration_box'), SetVariable("world_popupnarration_name", "highisland"), With(dissolve)]
        else:
            if (can_leave and quest_asterion == 1 and asterion_highisland_clues >= 3 and not highisland_howtoreach_pcknows and world_popupnarration_name == 0 and not world_popupnarration_highisland0) or (pc_area == "shortcut-cairn" and quest_asterion == 1 and asterion_highisland_clues >= 3 and not highisland_howtoreach_pcknows and world_popupnarration_name == 0 and not world_popupnarration_highisland0): # learn about high island
                timer 0.1 repeat False action [Show('world_popupnarration_box'), SetVariable("world_popupnarration_name", "learnabouthighisland"), With(dissolve)]
        ######
        if autosave_counter_temp != autosave_counter:
            $ autosave_counter_temp = autosave_counter
            $ quest_ruins_calculateclues = 0
            if quest_ruins_10yclue01:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue02:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue03:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue04p2:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue05:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue05p2:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue06:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue07:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue08:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue09:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue10:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue11:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue12:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_10yclue13:
                $ quest_ruins_calculateclues += 1
            if quest_ruins_treepicture and item_howlersdelltoken:
                $ quest_ruins_calculateclues += 3
            elif quest_ruins_treepicture and howlersdell_firsttime:
                $ quest_ruins_calculateclues += 2
        # if quest_ruins == 1 and quest_ruins_description01 and ruinedvillage_truth and not quest_ruinsconflictopen:
        #     timer 0.1 repeat False action [Show('world_popupnarration_box'), SetVariable("world_popupnarration_name", "steephousestartskippedclues"), With(dissolve)]
        if (can_leave and quest_ruins == 1 and quest_ruins_description01 and ruinedvillage_truth and not quest_ruinsconflictopen) or (pc_area == "shortcut-cairn" and quest_ruins == 1 and quest_ruins_description01 and ruinedvillage_truth and not quest_ruinsconflictopen):
            timer 0.1 repeat False action [Show('world_popupnarration_box'), SetVariable("world_popupnarration_name", "steephousestartconflict"), With(dissolve)]
        elif (can_leave and quest_ruins == 1 and quest_ruins_description01 and quest_ruins_calculateclues >= 7 and not ruinedvillage_truth and not ruinedvillage_confront_can) or (pc_area == "shortcut-cairn" and quest_ruins == 1 and quest_ruins_description01 and quest_ruins_calculateclues >= 7 and not ruinedvillage_truth and not ruinedvillage_confront_can):
            timer 0.1 repeat False action [Show('world_popupnarration_box'), SetVariable("world_popupnarration_name", "steephouseseektruth"), With(dissolve)]
        ######
        if item_rawfish_gaining:
            timer 0.5 repeat True:
                if quarters <= ((world_daylength/2)+11):
                    if not item_rawfish01:
                        action [SetVariable("item_rawfish01", (day+1)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish02:
                        action [SetVariable("item_rawfish02", (day+1)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish03:
                        action [SetVariable("item_rawfish03", (day+1)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish04:
                        action [SetVariable("item_rawfish04", (day+1)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish05:
                        action [SetVariable("item_rawfish05", (day+1)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish06:
                        action [SetVariable("item_rawfish06", (day+1)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish07:
                        action [SetVariable("item_rawfish07", (day+1)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish08:
                        action [SetVariable("item_rawfish08", (day+1)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish09:
                        action [SetVariable("item_rawfish09", (day+1)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish10:
                        action [SetVariable("item_rawfish10", (day+1)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                else:
                    if not item_rawfish01:
                        action [SetVariable("item_rawfish01", (day+2)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish02:
                        action [SetVariable("item_rawfish02", (day+2)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish03:
                        action [SetVariable("item_rawfish03", (day+2)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish04:
                        action [SetVariable("item_rawfish04", (day+2)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish05:
                        action [SetVariable("item_rawfish05", (day+2)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish06:
                        action [SetVariable("item_rawfish06", (day+2)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish07:
                        action [SetVariable("item_rawfish07", (day+2)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish08:
                        action [SetVariable("item_rawfish08", (day+2)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish09:
                        action [SetVariable("item_rawfish09", (day+2)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
                    elif not item_rawfish10:
                        action [SetVariable("item_rawfish10", (day+2)), SetVariable("item_rawfish_gaining", (item_rawfish_gaining-1))]
        if item_rawfish_losing:
            timer 0.5 repeat True:
                if item_rawfish01 and item_rawfish01 <= item_rawfish02 and item_rawfish01 <= item_rawfish02 and item_rawfish01 <= item_rawfish03 and item_rawfish01 <= item_rawfish04 and item_rawfish01 <= item_rawfish05 and item_rawfish01 <= item_rawfish06 and item_rawfish01 <= item_rawfish07 and item_rawfish01 <= item_rawfish08 and item_rawfish01 <= item_rawfish09 and item_rawfish01 <= item_rawfish10:
                    action [SetVariable("item_rawfish01", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish02 and item_rawfish02 <= item_rawfish02 and item_rawfish02 <= item_rawfish02 and item_rawfish02 <= item_rawfish03 and item_rawfish02 <= item_rawfish04 and item_rawfish02 <= item_rawfish05 and item_rawfish02 <= item_rawfish06 and item_rawfish02 <= item_rawfish07 and item_rawfish02 <= item_rawfish08 and item_rawfish02 <= item_rawfish09 and item_rawfish02 <= item_rawfish10:
                    action [SetVariable("item_rawfish02", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish03 and item_rawfish03 <= item_rawfish02 and item_rawfish03 <= item_rawfish02 and item_rawfish03 <= item_rawfish01 and item_rawfish03 <= item_rawfish04 and item_rawfish03 <= item_rawfish05 and item_rawfish03 <= item_rawfish06 and item_rawfish03 <= item_rawfish07 and item_rawfish03 <= item_rawfish08 and item_rawfish03 <= item_rawfish09 and item_rawfish03 <= item_rawfish10:
                    action [SetVariable("item_rawfish03", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish04 and item_rawfish04 <= item_rawfish02 and item_rawfish04 <= item_rawfish02 and item_rawfish04 <= item_rawfish03 and item_rawfish04 <= item_rawfish01 and item_rawfish04 <= item_rawfish05 and item_rawfish04 <= item_rawfish06 and item_rawfish04 <= item_rawfish07 and item_rawfish04 <= item_rawfish08 and item_rawfish04 <= item_rawfish09 and item_rawfish04 <= item_rawfish10:
                    action [SetVariable("item_rawfish04", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish05 and item_rawfish05 <= item_rawfish02 and item_rawfish05 <= item_rawfish02 and item_rawfish05 <= item_rawfish03 and item_rawfish05 <= item_rawfish04 and item_rawfish05 <= item_rawfish01 and item_rawfish05 <= item_rawfish06 and item_rawfish05 <= item_rawfish07 and item_rawfish05 <= item_rawfish08 and item_rawfish05 <= item_rawfish09 and item_rawfish05 <= item_rawfish10:
                    action [SetVariable("item_rawfish05", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish06 and item_rawfish06 <= item_rawfish02 and item_rawfish06 <= item_rawfish02 and item_rawfish06 <= item_rawfish03 and item_rawfish06 <= item_rawfish04 and item_rawfish06 <= item_rawfish05 and item_rawfish06 <= item_rawfish01 and item_rawfish06 <= item_rawfish07 and item_rawfish06 <= item_rawfish08 and item_rawfish06 <= item_rawfish09 and item_rawfish06 <= item_rawfish10:
                    action [SetVariable("item_rawfish06", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish07 and item_rawfish07 <= item_rawfish02 and item_rawfish07 <= item_rawfish02 and item_rawfish07 <= item_rawfish03 and item_rawfish07 <= item_rawfish04 and item_rawfish07 <= item_rawfish05 and item_rawfish07 <= item_rawfish06 and item_rawfish07 <= item_rawfish01 and item_rawfish07 <= item_rawfish08 and item_rawfish07 <= item_rawfish09 and item_rawfish07 <= item_rawfish10:
                    action [SetVariable("item_rawfish07", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish08 and item_rawfish08 <= item_rawfish02 and item_rawfish08 <= item_rawfish02 and item_rawfish08 <= item_rawfish03 and item_rawfish08 <= item_rawfish04 and item_rawfish08 <= item_rawfish05 and item_rawfish08 <= item_rawfish06 and item_rawfish08 <= item_rawfish07 and item_rawfish08 <= item_rawfish01 and item_rawfish08 <= item_rawfish09 and item_rawfish08 <= item_rawfish10:
                    action [SetVariable("item_rawfish08", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish09 and item_rawfish09 <= item_rawfish02 and item_rawfish09 <= item_rawfish02 and item_rawfish09 <= item_rawfish03 and item_rawfish09 <= item_rawfish04 and item_rawfish09 <= item_rawfish05 and item_rawfish09 <= item_rawfish06 and item_rawfish09 <= item_rawfish07 and item_rawfish09 <= item_rawfish08 and item_rawfish09 <= item_rawfish01 and item_rawfish09 <= item_rawfish10:
                    action [SetVariable("item_rawfish09", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish10 and item_rawfish10 <= item_rawfish02 and item_rawfish10 <= item_rawfish02 and item_rawfish10 <= item_rawfish03 and item_rawfish10 <= item_rawfish04 and item_rawfish10 <= item_rawfish05 and item_rawfish10 <= item_rawfish06 and item_rawfish10 <= item_rawfish07 and item_rawfish10 <= item_rawfish08 and item_rawfish10 <= item_rawfish09 and item_rawfish10 <= item_rawfish01:
                        action [SetVariable("item_rawfish10", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish01:
                    action [SetVariable("item_rawfish01", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish02:
                    action [SetVariable("item_rawfish02", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish03:
                    action [SetVariable("item_rawfish03", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish04:
                    action [SetVariable("item_rawfish04", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish05:
                    action [SetVariable("item_rawfish05", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish06:
                    action [SetVariable("item_rawfish06", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish07:
                    action [SetVariable("item_rawfish07", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish08:
                    action [SetVariable("item_rawfish08", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish09:
                    action [SetVariable("item_rawfish09", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
                elif item_rawfish10:
                    action [SetVariable("item_rawfish10", 0), SetVariable("item_rawfish_losing", (item_rawfish_losing-1))]
        if item_rawfishtotalnumber < 0:
            timer 0.5 repeat False:
                action [SetVariable("item_rawfishtotalnumber", 0), SetVariable("item_rawfish01", 0), SetVariable("item_rawfish02", 0), SetVariable("item_rawfish03", 0), SetVariable("item_rawfish04", 0), SetVariable("item_rawfish05", 0), SetVariable("item_rawfish06", 0), SetVariable("item_rawfish07", 0), SetVariable("item_rawfish08", 0), SetVariable("item_rawfish09", 0), SetVariable("item_rawfish10", 0), SetVariable("item_rawfish_losing", 0)]
        if item_cookedfish < 0:
            timer 0.5 repeat False:
                action [SetVariable("item_cookedfish", 0)]
        if item_wildplants < 0:
            timer 0.5 repeat False:
                action [SetVariable("item_wildplants", 0)]
        if coins < 0:
            timer 0.5 repeat False:
                action [SetVariable("coins", 0)]
        if item_rations < 0:
            timer 0.5 repeat False:
                action [SetVariable("item_rations", 0)]
        if minutes >= 30:
            timer 0.5 repeat True action [SetVariable("minutes", (minutes-30)), SetVariable("quarters", (quarters+2))]
        elif minutes >= 15:
            timer 0.5 repeat True action [SetVariable("minutes", (minutes-15)), SetVariable("quarters", (quarters+1))]
        if howlersdell_reputation_points >= 6:
            timer 0.5 repeat True action [SetVariable("howlersdell_reputation_points", (howlersdell_reputation_points-6)), SetVariable("howlersdell_reputation", (howlersdell_reputation+1))]
        key "K_F5" action QuickSave()
        key "K_F8" action QuickLoad()
        if isinventory:
            if tutorial_inventory == 1:
                key "i" action [ShowMenu('inventory'), SetVariable("tutorial_inventory", 0)]
                key "I" action [ShowMenu('inventory'), SetVariable("tutorial_inventory", 0)]
            else:
                key "i" action [ShowMenu('inventory')]
                key "I" action [ShowMenu('inventory')]
        if not endgame_mode:
            if mapunlocked:
                if can_leave and quarters < world_daylength:
                    if tutorial_map == 1:
                        if quarters < world_daylength:
                            key "m" action [Show('map_display'), SetVariable("tutorial_map", 0), With(dissolve)]
                            key "M" action [Show('map_display'), SetVariable("tutorial_map", 0), With(dissolve)]
                    elif tutorial_map == 3:
                        if quarters < world_daylength:
                            key "m" action [Show('map_display'), SetVariable("tutorial_map", 0), With(dissolve)]
                            key "M" action [Show('map_display'), SetVariable("tutorial_map", 0), With(dissolve)]
                    elif quarters < world_daylength-4 and not pc_area == "bogroad" and not pc_area == "bogcrossroads" and not pc_area == "peatfield" and not pc_area == "whitemarshes":
                        if quarters < world_daylength:
                            key "m" action [Show('map_display'), With(dissolve)]
                            key "M" action [Show('map_display'), With(dissolve)]
                        else:
                            key "m" action [Show('map_onlyview'), With(dissolve)]
                            key "M" action [Show('map_onlyview'), With(dissolve)]
                    else:
                        if quarters < world_daylength:
                            key "m" action [Show('map_display'), With(dissolve)]
                            key "M" action [Show('map_display'), With(dissolve)]
                        else:
                            key "m" action [Show('map_onlyview'), With(dissolve)]
                            key "M" action [Show('map_onlyview'), With(dissolve)]
                else:
                    key "m" action [Show('map_onlyview'), With(dissolve)]
                    key "M" action [Show('map_onlyview'), With(dissolve)]
        if not endgame_mode:
            if can_leave and quarters < world_daylength and waitunlocked:
                key "w" action [Show('waitscreen'), With(dissolve)]
                key "W" action [Show('waitscreen'), With(dissolve)]
        if isjournal:
            if tutorial_journal == 1:
                key "j" action [ShowMenu('journal'), SetVariable("tutorial_journal", 2)]
                key "J" action [ShowMenu('journal'), SetVariable("tutorial_journal", 2)]
            else:
                key "j" action [ShowMenu('journal')]
                key "J" action [ShowMenu('journal')]
        if not endgame_mode:
            if restunlocked:
                if can_rest:
                    if (quarters >= (world_daylength-12)) or (world_daylength_bogs and quarters >= (world_daylength-16)):
                        key "r":
                            if tutorial_sleep == 1:
                                action [Show('restscreen'), SetVariable("tutorial_sleep", 0), With(dissolve)]
                            elif not tutorial_lateevening and day == 1:
                                action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), SetVariable("tutorial_lateevening", 1), With(dissolve)] style_prefix "quicktutorial"
                            else:
                                action [Show('restscreen'), With(dissolve)]
                        key "R":
                            if tutorial_sleep == 1:
                                action [Show('restscreen'), SetVariable("tutorial_sleep", 0), With(dissolve)]
                            elif not tutorial_lateevening and day == 1:
                                action [SelectedIf(interface_menuscreenbypas==True), Show('restscreen'), SetVariable("tutorial_lateevening", 1), With(dissolve)] style_prefix "quicktutorial"
                            else:
                                action [Show('restscreen'), With(dissolve)]
                    if quarters < 36:
                        if (pc_area == "peltnorth" and peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day) or (pc_area == "foggylake" and foggy_about_shelter):
                            key "r":
                                if not tutorial_restatinn:
                                    action [Show('restscreen'), SetVariable("tutorial_restatinn", 1), With(dissolve)]
                                else:
                                    action [Show('restscreen'), With(dissolve)]
                            key "R":
                                if not tutorial_restatinn:
                                    action [Show('restscreen'), SetVariable("tutorial_restatinn", 1), With(dissolve)]
                                else:
                                    action [Show('restscreen'), With(dissolve)]
                    if quarters < 40:
                        if (pc_area == "howlersdell" and howlersdell_eryx_about_room and not quest_ruins_choice == "thais_won" and not quest_ruins_choice == "thais_alliance_fail" and not thais_bigmad_beaten):
                            key "r":
                                if not tutorial_restatinn:
                                    action [Show('restscreen'), SetVariable("tutorial_restatinn", 1), With(dissolve)]
                                else:
                                    action [Show('restscreen'), With(dissolve)]
                            key "R":
                                if not tutorial_restatinn:
                                    action [Show('restscreen'), SetVariable("tutorial_restatinn", 1), With(dissolve)]
                                else:
                                    action [Show('restscreen'), With(dissolve)]
        if not endgame_mode and tutorial_sheet:
            if tutorial_sheet_display:
                key "c" action [ShowMenu('charactersheet'), With(dissolve), SetVariable("tutorial_sheet_display", 0), With(dissolve)]
                key "C" action [ShowMenu('charactersheet'), With(dissolve), SetVariable("tutorial_sheet_display", 0), With(dissolve)]
            else:
                key "c" action [ShowMenu('charactersheet'), With(dissolve)]
                key "C" action [ShowMenu('charactersheet'), With(dissolve)]


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")
default quick_menu = True

style quick_button is default
style quick_button_text is button_text:
    hover_color '#f6d6bd'
style quick_button:
    properties gui.button_properties("quick_button")
style quick_button_text:
    size 30
    properties gui.button_text_properties("quick_button")

style quick2_button is quick_button
style quick2_button_text is quick_button_text:
    hover_color '#fff1e5'
    idle_color '#f6d6bd'

style quicktutorial_button is quick_button
style quicktutorial_button_text is quick_button_text:
    hover_color '#fff1e5'
    idle_color '#f6d6bd'

## Main and Game Menu Screens
default hidemainmenu = 0
default mainmenu_ignore_black = 0
screen navigation():
    if persistent.randomquote_displayed_currently:
        frame:
            style_prefix "main_menu_quote"
            vbox:
                spacing 14
                if persistent.randomquote == "specialanniversary":
                    xmaximum 800
                    text '{color=#f6d6bd}Welcome to Roadwarden’s Anniversary Patch!{/color}\n\nIt improves a few stories and bits of interface, but, sadly, it {b}won’t{/b} work well with the old saves.\n\nI recommend starting your playthrough from the beginning. In the newly available {b}advanced difficulty settings{/b}, you can choose to skip the opening section of the game.\n\nThank you so much for giving my game a chance, for your bug reports, editing tips, and gameplay suggestions. Thank you for making {color=#f6d6bd}Roadwarden{/color} what it is now.'
                    text '{color=#f6d6bd}Aureus{/color}' xalign 1.0
                if persistent.randomquote == 1:
                    text '“We marvel at the serenity of the forest\nand crave the shroud of its silence.”'
                if persistent.randomquote == 2:
                    text '“Who falls asleep in the forest, wakes up in a troll’s mouth.”'
                if persistent.randomquote == 3:
                    text '“Travels invite death.”'
                if persistent.randomquote == 4:
                    text '“The Ten Cities have the emperors,\nvillages have the wilderness.”'
                if persistent.randomquote == 5:
                    text 'The oldest pagan tribes use {i}the Old Speech{/i},\nwhat alienates them from the cityfolk.'
                if persistent.randomquote == 6:
                    text 'The phrase “safe travels” is used ironically\nwhen someone hopes to be extremely fortunate.'
                if persistent.randomquote == 7:
                    text '“Beasts feel only hunger.”'
                if persistent.randomquote == 8:
                    text 'Some settlements collaborate with the highwaymen, providing them with\nsupplies and shelter in exchange for protection and loot.'
                if persistent.randomquote == 9:
                    text '{i}To walk into the fogs{/i}\n- to die mysteriously.'
                if persistent.randomquote == 10:
                    text 'The orphans are raised by an entire village\nand are expected to return the favor\nonce they grow old enough to work.'
                if persistent.randomquote == 11:
                    text '{i}To invite a dragon{/i} - to be careless.'
                if persistent.randomquote == 12:
                    text 'Only a couple of species are capable of wielding magic,\nand none are as naturally gifted as humankind.'
                if persistent.randomquote == 13:
                    text '“Blood carries the soul, blood is power.”'
                if persistent.randomquote == 14:
                    text 'There are three {i}Rivers of Faith{/i}, the core readings of\nWright’s Tablets - the Rivers of Order, Truth, and Freedom.'
                if persistent.randomquote == 15:
                    text 'The United Church teaches that the path to fulfillment\nleads through obedience, strength, and courage.'
                if persistent.randomquote == 16:
                    text 'The monks of The Orders of Truth study Wright’s Tablets,\nmagic, crafts, and nature, and teach their followers\nto understand and accept the world.'
                if persistent.randomquote == 17:
                    text 'The fellowships are united in their love of independence, community, and modesty.\nThey embrace their unique traditions and beliefs.'
                if persistent.randomquote == 18:
                    text 'For centuries, the corsairs of The Ten Cities have pillaged The Southern Realms\nin search of copper, iron, and steel. Losing the war has made\nthese resources more scarce than ever.'
                if persistent.randomquote == 19:
                    text 'Some communities distinguish tamable {i}animals{/i} from dangerous {i}beasts{/i},\nwhile others see them all as wild {i}monsters{/i}\nor dark {i}creatures{/i} - the enemies of our kind.'
                if persistent.randomquote == 20:
                    text '“A bird house brings feathers, but also talons.”'
                if persistent.randomquote == 21:
                    text '“Each traveler sees with different eyes.”'
                if persistent.randomquote == 22:
                    text '“Wait two days for the lost, ten for the wounded,\ntwenty for the ill and mad. Then it’s time to grieve.”'
                if persistent.randomquote == 23:
                    text 'Altering the wilderness too much or too quickly spurs animals to join forces\nto push away or devour their shared enemy - humankind.\nSuch events are known as {i}wrath of the herds{/i}, {i}animal unions{/i}, or {i}nature’s fury{/i}.'
                if persistent.randomquote == 24:
                    text 'Fogs carry magical pneuma. They enhance spellcasters’ talents,\nbut also awake any human corpse they touch.\nThey are rare in spring and common during fall.'
                if persistent.randomquote == 25:
                    text 'Dragon carcasses are used in all sorts of crafts,\nincluding alchemy and coinmaking,\nbut there aren’t many dragon hunters around.'
                if persistent.randomquote == 26:
                    text 'Animals and humans can be healed with spells,\nbut a master in one field of magic\nmay know nothing about the other.'
                if persistent.randomquote == 27:
                    text 'Assuming a new identity takes only\nmoving to a distant settlement.'
                if persistent.randomquote == 28:
                    text '“They try to carve the world, yet their memories and tales dwindle,\ntheir shells wither away, homes and statues turn to dust.\nThe wilderness prevails, as indifferent as time.”'
                if persistent.randomquote == 29:
                    text 'Before the invasion that took place one generation ago,\nThe Southern Tribes were called {i}barbarians{/i},\nand The Southern Realms were known as The Wastelands.'
                if persistent.randomquote == 30:
                    text '“Travelers don’t know people, just stories.”'
                if persistent.randomquote == 31:
                    text 'The countryside needs roadwardens more than ever,\nbut trails are getting overgrown, roadside shelters are desolate,\nthere are fewer horses to train, and not enough iron for new blades.'
                if persistent.randomquote == 32:
                    text '“Wanderlust is an illness\ncured by talons and claws.”'
                if persistent.randomquote == 33:
                    text 'A living human is made of a {i}shell{/i}, {i}pneuma{/i}, and {i}soul{/i}.\nThe undead are shells moved by wild pneuma,\nwith no soul to tame it.'
                if persistent.randomquote == 34:
                    text 'The phrase {i}soul carrier{/i} describes any shell inhabited by a soul,\nincluding humans, spirits, and The Wright themselves.'
                if persistent.randomquote == 35:
                    text 'In the countryside, {i}spirits{/i} are believed to be centuries-old creatures.\nThey are seen as a part of the wilderness who\npunish those opposing the natural order.'
                if persistent.randomquote == 36:
                    text '“There are no roads under the moon.”'
                if persistent.randomquote == 37:
                    text '{i}Death by banishment{/i}\n- sending an evildoer into the wilderness\nwith only a flint dagger.'
                if persistent.randomquote == 38:
                    text '“Tribes come and go, but the woods abide.”'
                if persistent.randomquote == 39:
                    text 'Undead are known by many names, such as\n{i}the awoken{/i}, {i}the hollow{/i}, or {i}the empty ones{/i}.'
                if persistent.firsttime_aniversary_welcome and persistent.randomquote != "specialanniversary":
                    textbutton _("Enter") action [SetField(persistent, "randomquote", "specialanniversary"), With(dissolve)] text_align 0.5 xalign 0.5
                elif persistent.firsttime_aniversary_welcome and persistent.randomquote == "specialanniversary":
                    textbutton _("Proceed") action [SetField(persistent, "randomquote_displayed_currently", 0), SetField(persistent, "firsttime_aniversary_welcome", 0), SetField(persistent, "randomquote", 1), With(dissolve)] text_align 0.5 xalign 0.5
                else:
                    textbutton _("Enter") action [SetField(persistent, "randomquote_displayed_currently", 0), With(dissolve)] text_align 0.5 xalign 0.5
        # add "gui/splashscreen2.png"
    else:
        if main_menu:
            if not hidemainmenu:
                if not renpy.get_screen("preferences") and not renpy.get_screen("load") and not renpy.get_screen("about") and not renpy.get_screen("help") and persistent.demomode:
                    add "images/titlescreen/logodemo.png"
        vbox:
            style_prefix "navigation"
            xpos gui.navigation_xpos
            yalign 0.5
            if main_menu:
                if not hidemainmenu:
                    if not renpy.get_screen("preferences") and not renpy.get_screen("load") and not renpy.get_screen("about") and not renpy.get_screen("help"):
                        style_prefix "navigation_mm"
                        xalign 0.5
                        yalign 0.5
                        xpos 960
                        ypos 540
                        if persistent.textstyle == "basic":
                            spacing -6
                        if persistent.textstyle == "pixel":
                            spacing -8
                        add "images/titlescreen/logodarktitle.png"
                        text ""
                        if LoadMostRecent().get_sensitive():
                            textbutton _("Continue") action LoadMostRecent() text_align 0.5 xalign 0.5
                        else:
                            textbutton _("{color=#6a6a6a}Continue{/color}") action NullAction() text_align 0.5 xalign 0.5
                        if LoadMostRecent().get_sensitive():
                            textbutton _("Load") action [SelectedIf(ShowMenu("load")), ShowMenu("load")] text_align 0.5 xalign 0.5
                        else:
                            textbutton _("{color=#6a6a6a}Load{/color}") action NullAction() text_align 0.5 xalign 0.5
                        # textbutton _("New Game") action [SelectedIf(SetVariable("hidemainmenu", 1)), SetVariable("hidemainmenu", 1), ShowMenu("main_menu"), With(dissolve)] text_color "#997577" text_hover_color "#f6d6bd" text_align 0.5 xalign 0.5
                        textbutton _("New Game") action [SelectedIf(SetVariable("hidemainmenu", 1)), SetVariable("hidemainmenu", 1), ToggleScreen("startbox", transition=dissolve), SetVariable("mainmenu_ignore_black", 1), ShowMenu("main_menu"), With(dissolve)] text_color "#997577" text_hover_color "#f6d6bd" text_align 0.5 xalign 0.5
                        textbutton _("Settings") action [SelectedIf(ShowMenu("preferences")), ShowMenu("preferences")] text_align 0.5 xalign 0.5
                        textbutton _("Visit {color=#e5e1c0}Windy Meadow{/color}") action [OpenURL("https://store.steampowered.com/app/2366430/Windy_Meadow__A_Roadwarden_Tale/")] text_align 0.5 xalign 0.5 #{color=#e5e1c0}Windy Meadow{/color} # Windy Meadow
                        if renpy.variant("pc"):
                            textbutton _("Quit") action Quit(confirm=not main_menu) text_align 0.5 xalign 0.5
                    else:
                        style_prefix "navigation_mm"
                        ypos 908
                        if persistent.textstyle == "basic":
                            spacing -6
                        if persistent.textstyle == "pixel":
                            spacing -8
                        if LoadMostRecent().get_sensitive():
                            textbutton _("Continue") action LoadMostRecent()
                        else:
                            textbutton _("{color=#6a6a6a}Continue{/color}") action NullAction()
                        if LoadMostRecent().get_sensitive():
                            textbutton _("Load") action [SelectedIf(ShowMenu("load")), ShowMenu("load")]
                        else:
                            textbutton _("{color=#6a6a6a}Load{/color}") action NullAction()
                        # textbutton _("New Game") action [SelectedIf(SetVariable("hidemainmenu", 1)), SetVariable("hidemainmenu", 1), ShowMenu("main_menu"), With(dissolve)] text_color "#997577" text_hover_color "#f6d6bd"
                        textbutton _("New Game") action [SelectedIf(SetVariable("hidemainmenu", 1)), SetVariable("hidemainmenu", 1), ToggleScreen("startbox", transition=dissolve), SetVariable("mainmenu_ignore_black", 1), ShowMenu("main_menu"), With(dissolve)] text_color "#997577" text_hover_color "#f6d6bd"
                        textbutton _("Settings") action [SelectedIf(ShowMenu("preferences")), ShowMenu("preferences")]
                        if renpy.variant("pc"):
                            textbutton _("Quit") action Quit(confirm=not main_menu)
            else:
                ypos 686
                if persistent.textstyle == "basic":
                    spacing 8
                if persistent.textstyle == "pixel":
                    spacing 6
                if inventoryinteraction:
                    textbutton _("{color=#6a6a6a}Return{/color}") action NullAction()
                    textbutton _("{color=#6a6a6a}Save{/color}") action NullAction()
                    textbutton _("{color=#6a6a6a}Load{/color}") action NullAction()
                    textbutton _("{color=#6a6a6a}Journal{/color}") action NullAction()
                    textbutton _("{color=#6a6a6a}Inventory{/color}") action NullAction()
                    if tutorial_sheet:
                        textbutton _("{color=#6a6a6a}Character sheet{/color}") action NullAction()
                    textbutton _("{color=#6a6a6a}Archive{/color}") action NullAction()
                    textbutton _("{color=#6a6a6a}Settings{/color}") action NullAction()
                    textbutton _("Main Menu") action MainMenu()
                    if renpy.variant("pc"):
                        textbutton _("Quit") action Quit(confirm=not main_menu)
                else:
                    textbutton _("Return") action [Return()]
                    textbutton _("Save") action [SelectedIf(ShowMenu("save")), ShowMenu("save")]
                    textbutton _("Load") action [SelectedIf(ShowMenu("load")), ShowMenu("load")]
                    textbutton _("Journal") action [SelectedIf(ShowMenu("journal")), ShowMenu("journal")]
                    textbutton _("Inventory") action [SelectedIf(ShowMenu("inventory")), ShowMenu("inventory")]
                    if tutorial_sheet:
                        textbutton _("Character sheet") action [SelectedIf(ShowMenu("charactersheet")), ShowMenu("charactersheet")]
                    textbutton _("Archive") action [SelectedIf(ShowMenu("history")), ShowMenu("history")]
                    textbutton _("Settings") action [SelectedIf(ShowMenu("preferences")), ShowMenu("preferences")]
                    textbutton _("Main Menu") action MainMenu()
                    if renpy.variant("pc"):
                        textbutton _("Quit") action Quit(confirm=not main_menu)

style main_menu_quote_text is main_menu_text:
    text_align 0.5
    color "#997577"
    size 30
    # outlines [ (absolute(2), "#0f2a3f", absolute(0), absolute(0)) ]
    line_spacing +10

style main_menu_quote_button_text is navigation_button_text:
    color "#816271" # c3a38a
    hover_color "#c3a38a" # fff1e5
    selected_color '#997577' # f6d6bd
    size 30
    outlines [ (absolute(1), "#0f2a3f", absolute(0), absolute(0)) ]

style main_menu_quote_vbox is vbox
style main_menu_quote_title is main_menu_text
style main_menu_quote_version is main_menu_text
style main_menu_quote_frame is confirm_frame:
    xalign 0.5
    yalign 0.5
    xpadding 36
    top_padding 36
    bottom_padding 32

style navigation_button is gui_button
style navigation_button_text is gui_button_text:
    hover_color '#c3a38a'
    color "#997577"
    size 50
style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    hover_color "#f6d6bd"
    selected_color '#c3a38a'
style navigation_mm_button_text is navigation_button_text:
    color "#997577" # c3a38a
    hover_color "#f6d6bd" # fff1e5
    selected_color '#c3a38a' # f6d6bd
    outlines [ (absolute(3), "#0f2a3f", absolute(0), absolute(0)) ]

## Main Menu screen - Title Screen
default persistent.introsillytext = 0
screen main_menu():
    tag menu
    style_prefix "main_menu"
    add "titlescreen06"
    add "titlescreen05"
    add "titlescreen04"
    add "titlescreen03"
    add "titlescreen02"
    add "titlescreen01"
    add "titlescreenbird05"
    add "titlescreenbird04"
    add "titlescreenbird03"
    add "titlescreenbird02"
    add "titlescreenbird01"
    if not mainmenu_ignore_black:
        add "titlescreen07"
    # add "titlescreentreesoverlay"
    # add gui.main_menu_background
    ## This empty frame darkens the main menu.
    frame:
        pass
    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

screen startbox():
    if persistent.textstyle == "basic":
        frame:
            background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
            xalign 0.5
            yalign 0.4
            xpadding 56
            top_padding 56
            bottom_padding 48
            xsize 852
            xfill True
            vbox:
                spacing 40
                vbox:
                    yalign 0.5
                    xalign 0.0
                    #xpos 1433 ypos 130 #{font=munro.ttf}{/font}
                    text '{color=#c3a38a}{size=28}Everyone knows to stay away from the wilderness.\nMost people would never risk a lonely journey.\n\nRoadwardens not only accept this struggle, they embrace it.\nThey deliver messages, assist merchants, burn human corpses,\nand, if possible, get rid of the beasts and highwaymen.\n\nThey live on the road, die young or retire early.\n\nIt’s a dangerous job, but a respectable one.\nAnd it pays well.{/size}{/color}' text_align 0.0 line_spacing +5
                hbox:
                    xfill True
                    style_prefix "navigation_mmbonus_button_text"
                    if persistent.demomode != 1:
                        vbox:
                            xalign 0.0
                            if not persistent.introsillytext:
                                textbutton _("I leave the safety\nof the city walls") action [SetVariable("hidemainmenu", 1), ToggleScreen("startbox", transition=dissolve), ToggleScreen("difficultypick", transition=dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0
                            else:
                                textbutton _("I leave the safety\nof the city walls") action [SetVariable("hidemainmenu", 1), SetField(persistent, "introsillytext", 0), ToggleScreen("startbox", transition=dissolve), ToggleScreen("difficultypick", transition=dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0
                    else:
                        vbox:
                            xalign 0.0
                            if not persistent.introsillytext:
                                textbutton _("I leave the safety\nof the city walls") action [ToggleScreen("startbox", transition=dissolve), SetField(persistent, "difficulty", 2), SetVariable("hidemainmenu", 0), Start()] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0
                            else:
                                textbutton _("I leave the safety\nof the city walls") action [SetVariable("hidemainmenu", 1), SetField(persistent, "introsillytext", 0), ToggleScreen("startbox", transition=dissolve), SetField(persistent, "difficulty", 2), SetVariable("hidemainmenu", 0), Start()] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0
                    vbox:
                        xalign 1.0
                        if not persistent.introsillytext:
                            textbutton _("I still have my doubts") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 1), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 1:
                            textbutton _("I better check my bundles") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 2), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 2:
                            textbutton _("I think my horse has a cold") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 3), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 3:
                            textbutton _("I should practice\nwith my axe") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 4), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 4:
                            textbutton _("I’ll work in the harbor,\nbuy better supplies") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 5), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 5:
                            textbutton _("I’ll share one more day\nwith my loved ones") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 6), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 6:
                            textbutton _("I don’t like this weather") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 7), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 7:
                            textbutton _("I better go to\nthat wedding first") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 8), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 8:
                            textbutton _("One more evening in\nan alehouse won’t hurt") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 9), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 9:
                            textbutton _("I don’t feel so well") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 10), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 10:
                            textbutton _("I’ve been sleeping too much") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 11), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 28 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        else:
                            textbutton _("{color=#6a6a6a}No more waiting!{/color}") action NullAction() text_size 28 xpadding 0 text_align 1.0
    else:
        frame:
            background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
            xalign 0.5
            yalign 0.4
            xpadding 56
            top_padding 56
            bottom_padding 48
            xsize 900
            xfill True
            vbox:
                spacing 40
                vbox:
                    yalign 0.5
                    xalign 0.0
                    #xpos 1433 ypos 130 #{font=munro.ttf}{/font}
                    text '{color=#c3a38a}{size=30}Everyone knows to stay away from the wilderness.\nMost people would never risk a lonely journey.\n\nRoadwardens not only accept this struggle, they embrace it.\nThey deliver messages, assist merchants, burn human corpses,\nand, if possible, get rid of the beasts and highwaymen.\n\nThey live on the road, die young or retire early.\n\nIt’s a dangerous job, but a respectable one.\nAnd it pays well.{/size}{/color}' text_align 0.0 line_spacing +2
                hbox:
                    xfill True
                    style_prefix "navigation_mmbonus_button_text"
                    if persistent.demomode != 1:
                        vbox:
                            xalign 0.0
                            if not persistent.introsillytext:
                                textbutton _("I leave the safety\nof the city walls") action [SetVariable("hidemainmenu", 1), ToggleScreen("startbox", transition=dissolve), ToggleScreen("difficultypick", transition=dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0
                            else:
                                textbutton _("I leave the safety\nof the city walls") action [SetVariable("hidemainmenu", 1), SetField(persistent, "introsillytext", 0), ToggleScreen("startbox", transition=dissolve), ToggleScreen("difficultypick", transition=dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0
                    else:
                        vbox:
                            xalign 0.0
                            if not persistent.introsillytext:
                                textbutton _("I leave the safety\nof the city walls") action [ToggleScreen("startbox", transition=dissolve), SetField(persistent, "difficulty", 2), SetVariable("hidemainmenu", 0), Start()] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0
                            else:
                                textbutton _("I leave the safety\nof the city walls") action [SetVariable("hidemainmenu", 1), SetField(persistent, "introsillytext", 0), ToggleScreen("startbox", transition=dissolve), SetField(persistent, "difficulty", 2), SetVariable("hidemainmenu", 0), Start()] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0
                    vbox:
                        xalign 1.0
                        if not persistent.introsillytext:
                            textbutton _("I still have my doubts") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 1), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 1:
                            textbutton _("I better check my bundles") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 2), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 2:
                            textbutton _("I think my horse has a cold") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 3), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 3:
                            textbutton _("I should practice\nwith my axe") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 4), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 4:
                            textbutton _("I’ll work in the harbor,\nbuy better supplies") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 5), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 5:
                            textbutton _("I’ll share one more day\nwith my loved ones") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 6), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0 xalign 1.0
                        elif persistent.introsillytext == 6:
                            textbutton _("I don’t like this weather") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 7), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 7:
                            textbutton _("I better go to\nthat wedding first") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 8), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 8:
                            textbutton _("One more evening in\nan alehouse won’t hurt") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 9), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 9:
                            textbutton _("I don’t feel so well") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 10), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        elif persistent.introsillytext == 10:
                            textbutton _("I’ve been sleeping too much") action [SetVariable("hidemainmenu", 0), SetField(persistent, "introsillytext", 11), ToggleScreen("startbox", transition=dissolve), With(dissolve)] text_size 30 text_color "#816271" text_hover_color "#f6d6bd" xpadding 0 text_align 1.0
                        else:
                            textbutton _("{color=#6a6a6a}No more waiting!{/color}") action NullAction() text_size 30 xpadding 0 text_align 1.0

default persistent.difficulty = 2
default difficultypick_advanced = 0
default persistent.difficultypick_advanced_world_deadline = 40
default persistent.difficultypick_advanced_questseasier = 0
default persistent.difficultypick_advanced_bonusdamage = 0
default persistent.difficultypick_advanced_coins = 5
default persistent.difficultypick_advanced_potion = 0
default persistent.difficultypick_advanced_skip_prologue = 0
default world_skippingprologue = 0

screen difficultypick():
    frame:
        background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        xalign 0.5
        yalign 0.4
        xpadding 50
        top_padding 40
        bottom_padding 40
        if not difficultypick_advanced:
            if persistent.textstyle == "basic":
                vbox:
                    spacing 20
                    yalign 0.5
                    xalign 0.5
                    #xpos 1433 ypos 130 #{font=munro.ttf}{/font}
                    text '{color=#c3a38a}{size=28}Pick difficulty mode.{/size}{/color}' text_align 0.5 xalign 0.5
                    text '{color=#c3a38a}{size=28}This choice {b}can’t{/b} be altered later on.{/size}{/color}' text_align 0.5 xalign 0.5
                    null height (6)
                    textbutton _("{size=28}(switch to advanced options){/size}") action [SetVariable("difficultypick_advanced", 1)] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                    null height (1)
                    hbox:
                        spacing 90
                        style_prefix "navigation_mmbonus_button_text"
                        yalign 0.0
                        xalign 0.5
                        vbox:
                            spacing 26
                            xsize 420
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            # ymaximum 400
                            # yminimum 400
                            textbutton _("{size=28}{b}Casual{/b}{/size}") action [SetField(persistent, "difficulty", 1), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), Start()] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                            # textbutton _("{size=28}{b}1{/b}{/size}") action [SetField(persistent, "difficulty", 1), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), Start()] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                            text '{color=#c3a38a}{size=28}For those focused on the story.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=28}* No time limit.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=28}* More cash at the start.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=28}* Some quests are more forgiving.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                        vbox:
                            spacing 26
                            xsize 420
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            # ymaximum 400
                            # yminimum 400
                            textbutton _("{size=28}{b}Standard{/b}{/size}") action [SetField(persistent, "difficulty", 2), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), Start()] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                            # textbutton _("{size=28}{b}1{/b}{/size}") action [SetField(persistent, "difficulty", 2), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), Start()] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                            text '{color=#c3a38a}{size=28}For those familiar with RPGs.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=28}* 40-day time limit.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=28}* Regular rule set.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                        vbox:
                            spacing 26
                            xsize 420
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            # ymaximum 400
                            # yminimum 400
                            textbutton _("{size=28}{b}Restrictive{/b}{/size}") action [SetField(persistent, "difficulty", 3), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), Start()] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                            # textbutton _("{size=28}{b}1{/b}{/size}") action [SetField(persistent, "difficulty", 3), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), Start()] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                            text '{color=#c3a38a}{size=28}For the returning roadwardens.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=28}* 30-day time limit.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=28}* Increased nighttime damage.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
            if persistent.textstyle == "pixel":
                vbox:
                    spacing 20
                    yalign 0.5
                    xalign 0.5
                    #xpos 1433 ypos 130 #{font=munro.ttf}{/font}
                    text '{color=#c3a38a}{size=30}Pick difficulty mode.{/size}{/color}' text_align 0.5 xalign 0.5
                    text '{color=#c3a38a}{size=30}This choice {b}can’t{/b} be altered later on.{/size}{/color}' text_align 0.5 xalign 0.5
                    null height (7)
                    textbutton _("{size=30}(switch to advanced options){/size}") action [SetVariable("difficultypick_advanced", 1)] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                    null height (1)
                    hbox:
                        spacing 70
                        style_prefix "navigation_mmbonus_button_text"
                        yalign 0.0
                        xalign 0.5
                        vbox:
                            spacing 28
                            xsize 430
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            # ymaximum 400
                            # yminimum 400
                            textbutton _("{size=30}{b}Casual{/b}{/size}") action [SetField(persistent, "difficulty", 1), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), Start()] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                            text '{color=#c3a38a}{size=30}For those focused on the story.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=30}* No time limit.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=30}* More cash at the start.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=30}* Some quests are more forgiving.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                        vbox:
                            spacing 28
                            xsize 430
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            # ymaximum 400
                            # yminimum 400
                            textbutton _("{size=30}{b}Standard{/b}{/size}") action [SetField(persistent, "difficulty", 2), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), Start()] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                            text '{color=#c3a38a}{size=30}For those familiar with RPGs.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=30}* 40-day time limit.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=30}* Regular rule set.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                        vbox:
                            spacing 28
                            xsize 430
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            # ymaximum 400
                            # yminimum 400
                            textbutton _("{size=30}{b}Restrictive{/b}{/size}") action [SetField(persistent, "difficulty", 3), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), Start()] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                            text '{color=#c3a38a}{size=30}For the returning roadwardens.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=30}* 30-day time limit.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
                            text '{color=#c3a38a}{size=30}* Increased nighttime damage.{/size}{/color}' text_align 0.0 xalign 0.0 yalign 0.0
        else:
            if persistent.textstyle == "basic":
                vbox:
                    spacing 20
                    yalign 0.5
                    xalign 0.5
                    text '{color=#c3a38a}{size=28}Pick difficulty mode.{/size}{/color}' text_align 0.5 xalign 0.5
                    text '{color=#c3a38a}{size=28}This choice {b}can’t{/b} be altered later on.{/size}{/color}' text_align 0.5 xalign 0.5
                    null height (6)
                    textbutton _("{size=28}(switch to preset options){/size}") action [SetVariable("difficultypick_advanced", 0)] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                    null height (6)
                    hbox:
                        spacing 90
                        style_prefix "check_alt"
                        yalign 0.0
                        xalign 0.5
                        vbox:
                            spacing 20
                            xsize 420
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            text _("{b}{color=#c3a38a}{size=28}Time limit{/size}{/color}{/b}") text_align 0.0 xalign 0.0 yalign 0.0
                            textbutton _("{size=28}45 days{/size}") action [SelectedIf(SetField(persistent, "difficultypick_advanced_world_deadline", 45)), SetField(persistent, "difficultypick_advanced_world_deadline", 45), SetField(persistent, "difficultypick_advanced_questseasier", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                            textbutton _("{size=28}40 days{/size}") action [SelectedIf(SetField(persistent, "difficultypick_advanced_world_deadline", 40)), SetField(persistent, "difficultypick_advanced_world_deadline", 40), SetField(persistent, "difficultypick_advanced_questseasier", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                            textbutton _("{size=28}30 days{/size}") action [SelectedIf(SetField(persistent, "difficultypick_advanced_world_deadline", 30)), SetField(persistent, "difficultypick_advanced_world_deadline", 30), SetField(persistent, "difficultypick_advanced_questseasier", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                            textbutton _("{size=28}None{/size}") action [SelectedIf(SetField(persistent, "difficultypick_advanced_world_deadline", 1000)), SetField(persistent, "difficultypick_advanced_world_deadline", 1000)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                        vbox:
                            spacing 20
                            xsize 420
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            text _("{b}{color=#c3a38a}{size=28}Increased nighttime damage{/size}{/color}{/b}") text_align 0.0 xalign 0.0 yalign 0.0
                            hbox:
                                xsize 420
                                xfill True
                                textbutton _("{size=28}Yes{/size}") action [SetField(persistent, "difficultypick_advanced_bonusdamage", 1)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                                textbutton _("{size=28}No{/size}") action [SetField(persistent, "difficultypick_advanced_bonusdamage", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 0.5
                                textbutton _("{size=28} {/size}") action NullAction() text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 1.0
                            null height (22)
                            if persistent.difficultypick_advanced_world_deadline != 1000:
                                text _("{b}{color=#6a6a6a}{size=28}Easier quests{/size}{/color}{/b}") text_align 0.0 xalign 0.0 yalign 0.0
                                textbutton _("{color=#6a6a6a}{size=28}(select no time limit to unlock){/size}{/size}") action NullAction() text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                            else:
                                text _("{b}{color=#c3a38a}{size=28}Easier quests{/size}{/color}{/b}") text_align 0.0 xalign 0.0 yalign 0.0
                                hbox:
                                    xsize 420
                                    xfill True
                                    textbutton _("{size=28}Yes{/size}") action [SetField(persistent, "difficultypick_advanced_questseasier", 1)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                                    textbutton _("{size=28}No{/size}") action [SetField(persistent, "difficultypick_advanced_questseasier", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 0.5
                                    textbutton _("{size=28} {/size}") action NullAction() text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 1.0
                        vbox:
                            spacing 20
                            xsize 420
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            text _("{b}{color=#c3a38a}{size=28}Bonus healing potion at start{/size}{/color}{/b}") text_align 0.0 xalign 0.0 yalign 0.0
                            hbox:
                                xfill True
                                textbutton _("{size=28}Yes{/size}") action [SetField(persistent, "difficultypick_advanced_potion", 1)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                                textbutton _("{size=28}No{/size}") action [SetField(persistent, "difficultypick_advanced_potion", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 0.5 text_align 0.5
                                textbutton _("{size=28} {/size}") action NullAction() text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 1.0
                            null height (22)
                            text _("{b}{color=#c3a38a}{size=28}Coins at start{/size}{/color}{/b}") text_align 0.0 xalign 0.0 yalign 0.0
                            hbox:
                                xsize 420
                                xfill True
                                textbutton _("{size=28}10{/size}") action [SetField(persistent, "difficultypick_advanced_coins", 10)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                                textbutton _("{size=28}5{/size}") action [SetField(persistent, "difficultypick_advanced_coins", 5)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 0.5 text_align 0.5
                                textbutton _("{size=28}0{/size}") action [SetField(persistent, "difficultypick_advanced_coins", 1)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 1.0 yalign 0.5 text_align 1.0
                    vbox:
                        spacing 20
                        xsize 420
                        yalign 0.0
                        xalign 0.5
                        style_prefix "check_alt"
                        xfill True
                        null height (20)
                        text _("{b}{color=#c3a38a}{size=28}Skip the prologue/tutorial{/size}{/color}{/b}") text_align 0.0 xalign 0.0 yalign 0.0
                        hbox:
                            xsize 430
                            xfill True
                            textbutton _("{size=28}Yes{/size}") action [SetField(persistent, "difficultypick_advanced_skip_prologue", 1)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                            textbutton _("{size=28}No{/size}") action [SetField(persistent, "difficultypick_advanced_skip_prologue", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                    textbutton _("{size=28}{b}Proceed{/b}{/size}") action [SetField(persistent, "difficulty", 0), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), Start()] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0

            if persistent.textstyle == "pixel":
                vbox:
                    spacing 20
                    yalign 0.5
                    xalign 0.5
                    text '{color=#c3a38a}{size=30}Pick difficulty mode.{/size}{/color}' text_align 0.5 xalign 0.5
                    text '{color=#c3a38a}{size=30}This choice {b}can’t{/b} be altered later on.{/size}{/color}' text_align 0.5 xalign 0.5
                    null height (7)
                    textbutton _("{size=30}(switch to preset options){/size}") action [SetVariable("difficultypick_advanced", 0)] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
                    null height (7)
                    hbox:
                        spacing 70
                        style_prefix "check_alt"
                        yalign 0.0
                        xalign 0.5
                        vbox:
                            spacing 28
                            xsize 430
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            text _("{color=#c3a38a}{size=30}Time limit{/size}{/color}") text_align 0.0 xalign 0.0 yalign 0.0
                            textbutton _("{size=30}45 days{/size}") action [SelectedIf(SetField(persistent, "difficultypick_advanced_world_deadline", 45)), SetField(persistent, "difficultypick_advanced_world_deadline", 45), SetField(persistent, "difficultypick_advanced_questseasier", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                            textbutton _("{size=30}40 days{/size}") action [SelectedIf(SetField(persistent, "difficultypick_advanced_world_deadline", 40)), SetField(persistent, "difficultypick_advanced_world_deadline", 40), SetField(persistent, "difficultypick_advanced_questseasier", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                            textbutton _("{size=30}30 days{/size}") action [SelectedIf(SetField(persistent, "difficultypick_advanced_world_deadline", 30)), SetField(persistent, "difficultypick_advanced_world_deadline", 30), SetField(persistent, "difficultypick_advanced_questseasier", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                            textbutton _("{size=30}None{/size}") action [SelectedIf(SetField(persistent, "difficultypick_advanced_world_deadline", 1000)), SetField(persistent, "difficultypick_advanced_world_deadline", 1000)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                        vbox:
                            spacing 28
                            xsize 430
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            text _("{color=#c3a38a}{size=30}Increased nighttime damage{/size}{/color}") text_align 0.0 xalign 0.0 yalign 0.0
                            hbox:
                                xsize 430
                                xfill True
                                textbutton _("{size=30}Yes{/size}") action [SetField(persistent, "difficultypick_advanced_bonusdamage", 1)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                                textbutton _("{size=30}No{/size}") action [SetField(persistent, "difficultypick_advanced_bonusdamage", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 0.5
                                textbutton _("{size=30} {/size}") action NullAction() text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 1.0
                            null height (22)
                            if persistent.difficultypick_advanced_world_deadline != 1000:
                                text _("{color=#6a6a6a}{size=30}Easier quests{/size}{/color}") text_align 0.0 xalign 0.0 yalign 0.0
                                textbutton _("{color=#6a6a6a}{size=30}(select no time limit to unlock){/size}{/size}") action NullAction() text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                            else:
                                text _("{color=#c3a38a}{size=30}Easier quests{/size}{/color}") text_align 0.0 xalign 0.0 yalign 0.0
                                hbox:
                                    xsize 430
                                    xfill True
                                    textbutton _("{size=30}Yes{/size}") action [SetField(persistent, "difficultypick_advanced_questseasier", 1)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                                    textbutton _("{size=30}No{/size}") action [SetField(persistent, "difficultypick_advanced_questseasier", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 0.5
                                    textbutton _("{size=30} {/size}") action NullAction() text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 1.0
                        vbox:
                            spacing 28
                            xsize 430
                            yalign 0.0
                            xalign 0.5
                            xfill True
                            text _("{color=#c3a38a}{size=30}Bonus healing potion at start{/size}{/color}") text_align 0.0 xalign 0.0 yalign 0.0
                            hbox:
                                xfill True
                                textbutton _("{size=30}Yes{/size}") action [SetField(persistent, "difficultypick_advanced_potion", 1)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                                textbutton _("{size=30}No{/size}") action [SetField(persistent, "difficultypick_advanced_potion", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 0.5
                                textbutton _("{size=30} {/size}") action NullAction() text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 1.0
                            null height (22)
                            text _("{color=#c3a38a}{size=30}Coins at start{/size}{/color}") text_align 0.0 xalign 0.0 yalign 0.0
                            hbox:
                                xsize 430
                                xfill True
                                textbutton _("{size=30}10{/size}") action [SetField(persistent, "difficultypick_advanced_coins", 10)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                                textbutton _("{size=30}5{/size}") action [SetField(persistent, "difficultypick_advanced_coins", 5)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.5 yalign 0.5
                                textbutton _("{size=30}0{/size}") action [SetField(persistent, "difficultypick_advanced_coins", 1)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 1.0 yalign 0.5
                    vbox:
                        spacing 20
                        xsize 420
                        yalign 0.0
                        xalign 0.5
                        style_prefix "check_alt"
                        xfill True
                        null height (20)
                        text _("{color=#c3a38a}{size=30}Skip the prologue/tutorial{/size}{/color}") text_align 0.0 xalign 0.0 yalign 0.0
                        hbox:
                            xsize 430
                            xfill True
                            textbutton _("{size=30}Yes{/size}") action [SetField(persistent, "difficultypick_advanced_skip_prologue", 1)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                            textbutton _("{size=30}No{/size}") action [SetField(persistent, "difficultypick_advanced_skip_prologue", 0)] text_color "#816271" text_hover_color "#f6d6bd" text_selected_color '#c3a38a' xalign 0.0 yalign 0.5
                    null height (10)
                    textbutton _("{size=30}{b}Proceed{/b}{/size}") action [SetField(persistent, "difficulty", 0), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), Start()] text_color "#816271" text_hover_color "#f6d6bd" xalign 0.5 yalign 0.0
    key "game_menu" action [SetVariable("mainmenu_ignore_black", 1), SetVariable("hidemainmenu", 0), ToggleScreen("difficultypick", transition=dissolve), With(dissolve)] # ShowMenu("main_menu")

style navigation_mmbonus_button_text is navigation_mm_button_text:
    color "#f6d6bd"
    hover_color "#fff1e5"
    outlines [ (absolute(3), "#0f2a3f", absolute(0), absolute(0)) ]

style check_alt_label is pref_label
style check_alt_label_text is pref_label_text:
    color "#997577"
style check_alt_vbox is pref_vbox
style check_alt_vbox:
    spacing gui.pref_button_spacing
style check_alt_button is gui_button
style check_alt_button_text is gui_button_text:
    size 48
style check_alt_button:
    properties gui.button_properties("check2_button")
    foreground "gui/button/check2_[prefix_]foreground.png"

style check_alt_button_text:
    properties gui.button_text_properties("check2_button")
    color "#816271"
    hover_color "#f6d6bd"
    selected_color '#c3a38a'
    insensitive_color "#7d7d7d"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_frame:
    xsize 420
    yfill True
    background "gui/overlay/main_menu.png"
# style main_menu_vbox:
#     xalign 1.0
#     xoffset -30
#     xmaximum 1200
#     yalign 1.0
#     yoffset -30
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
style main_menu_title:
    properties gui.text_properties("title")
style main_menu_version:
    properties gui.text_properties("version")

## Game Menu screen
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    if main_menu:
        add "titlescreen06"
        add "titlescreen05"
        add "titlescreen04"
        add "titlescreen03"
        add "titlescreen02"
        add "titlescreen01"
        add "titlescreenbird05"
        add "titlescreenbird04"
        add "titlescreenbird03"
        add "titlescreenbird02"
        add "titlescreenbird01"
        # add "titlescreentreesoverlay"
    else:
        add gui.game_menu_background
    frame:
        if main_menu:
            if not renpy.get_screen("preferences"):
                style "game_menu_outer_frame_transparent"
            else:
                style "game_menu_outer_frame_transparent"
                top_padding 60
        else:
            if not renpy.get_screen("preferences"):
                style "game_menu_outer_frame"
            else:
                style "game_menu_outer_frame"
                top_padding 60
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude
    use navigation
    label title
    if main_menu:
        key "game_menu" action [SetVariable("mainmenu_ignore_black", 1), ShowMenu("main_menu")]

style game_menu_outer_frame is empty
style game_menu_outer_frame_transparent is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text
style return_button is navigation_button
style return_button_text is navigation_button_text
style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background "gui/overlay/game_menu.png"
style game_menu_outer_frame_transparent:
    bottom_padding 45
    top_padding 180
    background "gui/overlay/game_menu_transparent.png"
style game_menu_navigation_frame:
    xsize 420
    yfill True
style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15
style game_menu_viewport:
    xsize 1380
style game_menu_vscrollbar:
    unscrollable gui.unscrollable
style game_menu_side:
    spacing 15
style game_menu_label:
    xpos 75
    ysize 180
style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
style return_button:
    xpos gui.navigation_xpos
    ypos 482
    yalign 1.0
    yoffset -45

## About screen
screen about():
    tag menu
    use game_menu(_("Credits"), scroll="viewport"):
        style_prefix "about"
        vbox:
            spacing 22
            xalign 0.5
            text _("While the game portrays wildlife as monstrous, in reality animals are an essential part of healthy ecosystems and the threat they present to us is negligible. Please consider supporting charities such as {color=#f6d6bd}Endangered Species International{/color}.\n") # Defenders of Wildlife / Animal Welfare Institute
            hbox:
                spacing 100
                vbox:
                    xminimum 275
                    xmaximum 275
                    spacing 15
                    xalign 0.0
                    yalign 0.0
                    text _("{color=#f6d6bd}Aureus{/color}")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    text _("story, pixel art, design, programming")
            add "gui/horizontalline.png":
                xalign 0.5
            hbox:
                spacing 100
                vbox:
                    xminimum 275
                    xmaximum 275
                    spacing 15
                    xalign 0.0
                    yalign 0.0
                    text _("{color=#f6d6bd}Lisa Olsen{/color}")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    text _("editing")
            add "gui/horizontalline.png":
                xalign 0.5
            hbox:
                spacing 100
                vbox:
                    xminimum 275
                    xmaximum 275
                    spacing 15
                    xalign 0.0
                    yalign 0.0
                    text _("{color=#f6d6bd}Nicholas Roder{/color}")
                    text _("{color=#f6d6bd}Felix Watson{/color}")
                    text _("{color=#f6d6bd}Finn Bennet{/color}")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    text _("original music")
            add "gui/horizontalline.png":
                xalign 0.5
            hbox:
                spacing 100
                vbox:
                    xminimum 275
                    xmaximum 275
                    spacing 15
                    xalign 0.0
                    yalign 0.0
                    text _("{color=#f6d6bd}Black Yen{/color}")
                    text _("{color=#f6d6bd}Dan Caine{/color}")
                    text _("{color=#f6d6bd}Hinterheim{/color}")
                    text _("{color=#f6d6bd}Jonathan Fraser{/color}")
                    text _("{color=#f6d6bd}Scott Buckley{/color}")
                    text _("and more")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    text _("additional music")
            add "gui/horizontalline.png":
                xalign 0.5
            hbox:
                spacing 100
                vbox:
                    xminimum 275
                    xmaximum 275
                    spacing 15
                    xalign 0.0
                    yalign 0.0
                    text _("{color=#f6d6bd}Yar{/color}")
                    text _("{color=#f6d6bd}Jetrel{/color}")
                    text _("{color=#f6d6bd}Zabin{/color}")
                    text _("{color=#f6d6bd}Bertram{/color}")
                    text _("{color=#f6d6bd}Kimmo Rundelin{/color}")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    text _("stock images")
            add "gui/horizontalline.png":
                xalign 0.5
            hbox:
                spacing 75
                vbox:
                    xminimum 300
                    xmaximum 300
                    spacing 15
                    xalign 0.0
                    yalign 0.0
                    text _("{color=#f6d6bd}Dennis Blumenthal{/color}")
                    text _("{color=#f6d6bd}Michele Busiello{/color}")
                    text _("{color=#f6d6bd}Marian Denefleh{/color}")
                    text _("{color=#f6d6bd}Tim Freund{/color}")
                    text _("{color=#f6d6bd}Daniel Gubala{/color}")
                    text _("{color=#f6d6bd}Tobias Hanika{/color}")
                    text _("{color=#f6d6bd}Marion Mager{/color}")
                    text _("{color=#f6d6bd}Stefan Marcinek{/color}")
                    text _("{color=#f6d6bd}Helge Peglow{/color}")
                    text _("{color=#f6d6bd}Lars Racky{/color}")
                    text _("{color=#f6d6bd}Uwe Roth{/color}")
                    text _("{color=#f6d6bd}Christian Schlütter{/color}")
                    text _("{color=#f6d6bd}Maurice Skotschir{/color}")
                    text _("{color=#f6d6bd}Jerome Zenker{/color}")
                    text _("{color=#f6d6bd}Maria Zubova{/color}")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    text _("the Assemble Team")
            add "gui/horizontalline.png":
                xalign 0.5
            hbox:
                spacing 100
                vbox:
                    xminimum 275
                    xmaximum 275
                    spacing 15
                    xalign 0.0
                    yalign 0.0
                    text _("{color=#f6d6bd}Koyama Satsuki{/color}")
                    text _("{color=#f6d6bd}Freesfx{/color}")
                    text _("{color=#f6d6bd}Zapsplat{/color}")
                    text _("and more")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    text _("stock sounds")
            add "gui/horizontalline.png":
                xalign 0.5
            hbox:
                spacing 100
                vbox:
                    xminimum 275
                    xmaximum 275
                    spacing 15
                    xalign 0.0
                    yalign 0.0
                    text _("special thanks to")
                vbox:
                    xalign 0.0
                    yalign 0.5
                    text _("{color=#f6d6bd}Joanna Falkowska{/color}")
            add "gui/horizontalline.png":
                xalign 0.5




            # hbox:
            #     vbox:
            #         xalign 0.0
            #         yalign 0.0
            #         text _("")
            #     vbox:
            #         xalign 0.0
            #         yalign 0.0
            #         text _("")
            text _("Made with the {color=#f6d6bd}Ren’Py{/color} engine.")
            text _("Contact: moralanxietystudio@gmail.com")
            textbutton _("Back") action ShowMenu("preferences") xpos -10

## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text:
    size 40
    color "#c3a38a"
style about_label_text:
    size gui.label_text_size
style about_label_texthistory:
    size 12
style about_button_text is gui_button_text:
    properties gui.button_text_properties("about_button")
style about_button:
    properties gui.button_properties("about_button")
    xmargin 4

default endcredits_counter = 0
screen endcredits():
    zorder 100
    default tt = Tooltip("")
    vbox:
        style_prefix "quick"
        xalign 0.5
        yalign 0.5
        xpos 1701
        ypos 540
        spacing +12
        # 300
        ########
        if endcredits_counter == 0:
            text _("{color=#f6d6bd}Roadwarden{/color}\nby\n{color=#f6d6bd}Aureus{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            # text _("story, pixel art, design, programming") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
        elif endcredits_counter == 1:
            text _("with the help of:") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
        elif endcredits_counter == 2:
            text _("{color=#f6d6bd}Lisa Olsen{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("\nediting") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
        elif endcredits_counter == 3:
            text _("{color=#f6d6bd}Nicholas Roder{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Felix Watson{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Finn Bennet{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("\noriginal music") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
        elif endcredits_counter == 4:
            text _("{color=#f6d6bd}Black Yen{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Dan Caine{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Hinterheim{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Jonathan Fraser{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Scott Buckley{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("and more") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("\nadditional music") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
        elif endcredits_counter == 5:
            text _("{color=#f6d6bd}Yar{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Jetrel{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Zabin{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Bertram{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Kimmo Rundelin{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("\nstock images") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
        elif endcredits_counter == 6:
            text _("{color=#f6d6bd}Dennis Blumenthal{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Michele Busiello{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Marian Denefleh{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Tim Freund{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Daniel Gubala{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Tobias Hanika{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Marion Mager{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Stefan Marcinek{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Helge Peglow{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Lars Racky{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Uwe Roth{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Christian Schlütter{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Maurice Skotschir{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Jerome Zenker{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Maria Zubova{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("\nthe Assemble Team") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
        elif endcredits_counter == 7:
            text _("{color=#f6d6bd}Koyama Satsuki{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Freesfx{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("{color=#f6d6bd}Zapsplat{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("and more") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("\nstock sounds") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
        elif endcredits_counter == 8:
            text _("special thanks to") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
            text _("\n{color=#f6d6bd}Joanna Falkowska{/color}") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
        elif endcredits_counter == 9:
            text _("Made with\nthe {color=#f6d6bd}Ren’Py{/color} engine.") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
        elif endcredits_counter == 10:
            text _("Thank you\nfor joining us.") text_align 0.5 xmaximum 300 xminimum 300 xalign .5
## Load and Save screens
screen save():
    tag menu
    use file_slots1(_("Save"))
screen file_slots1(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Save on page {}"), auto=_("Automatic saves"), quick=_("Save on a quick save"))
    on "show" action SetVariable("game_menu_screen", "save")
    on "replace" action SetVariable("game_menu_screen", "save")
    use game_menu(title):
        fixed:
            spacing 20
            ypos -25
            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True
            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value
            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    vbox:
                        button:
                            action FileAction(slot)
                            has vbox
                            add FileScreenshot(slot) xalign 0.5
                            null height (10)
                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"
                            # text FileSaveName(slot):
                            #     style "slot_name_text"
                            key "save_delete" action FileDelete(slot)
                        # null height (15)
                        textbutton _("delete save"):
                            xalign 0.5
                            style_prefix "slot_button_text2"
                            text_hover_color '#f6d6bd'
                            action [FileDelete(slot)]
                        # null height (15) # SelectedIf(interface_menuscreenbypas==True),
                        # if persistent.textstyle == "basic":
                        #     textbutton "" action text_align 0.5 text_size 21 style "slot_button_text" SelectedIf(interface_menuscreenbypas==True)# font "philosopher.ttf"
                        # if persistent.textstyle == "pixel":
                        #     textbutton "Delete save" action FileDelete(slot) text_align 0.5 text_size 21 style "slot_button_text" SelectedIf(interface_menuscreenbypas==True)# style "slot_button_text" font "munro.ttf" style_prefix
            ## Buttons to access other pages.
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 0.98#0.94
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious(max=8)
                #if config.has_autosave:
                textbutton _("{#auto_page}{color=#6a6a6a}A{/color}") action NullAction()#FilePage("auto")
                #if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")
                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 9):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext(max=8)
screen load():
    tag menu
    use file_slots2(_("Load"))
screen file_slots2(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Load from page {}"), auto=_("Load an automatic save"), quick=_("Load a quick save"))
    on "show" action SetVariable("game_menu_screen", "load")
    on "replace" action SetVariable("game_menu_screen", "load")
    use game_menu(title):
        fixed:
            ypos -25
            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True
            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value
            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    vbox:
                        button:
                            action FileAction(slot)
                            has vbox
                            add FileScreenshot(slot) xalign 0.5
                            null height (10)
                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"
                            # text FileSaveName(slot):
                            #     style "slot_name_text"
                            key "save_delete" action FileDelete(slot)
                        textbutton _("delete save"):
                            xalign 0.5
                            style_prefix "slot_button_text2"
                            text_hover_color '#f6d6bd'
                            action [FileDelete(slot)]
            ## Buttons to access other pages.
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 0.98
                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious(max=8)
                #if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")
                #if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")
                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 9):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext(max=8)

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button
style slot_button_text is gui_button_text:
    hover_color '#f6d6bd'
style slot_time_text is slot_button_text:
    hover_color '#f6d6bd'
    idle_color '#997577'
style slot_button_text2 is slot_button_text:
    hover_color '#f6d6bd'
    selected_color '#f6d6bd'
    idle_color '#997577'
style slot_name_text is slot_button_text
style page_label:
    xpadding 75
    ypadding 5
style page_label_text:
    text_align 0.5
    layout "subtitle"
    # hover_color gui.hover_color
    hover_color '#f6d6bd'
    selected_color '#c3a38a'
style page_button:
    properties gui.button_properties("page_button")
style page_button_text:
    properties gui.button_text_properties("page_button")
    size 30
    hover_color '#f6d6bd'
    selected_color '#c3a38a'
style slot_button:
    properties gui.button_properties("slot_button")
style slot_button_text:
    properties gui.button_text_properties("slot_button")

## Preferences screen
screen preferences():
    tag menu
    default tt = Tooltip("")
    default tt2 = Tooltip("")
    default tt3 = Tooltip("")
    default tt4 = Tooltip("")
    on "show" action SetVariable("game_menu_screen", "preferences")
    on "replace" action SetVariable("game_menu_screen", "preferences")
    use game_menu(_("Settings"), scroll="viewport"):
        vbox:
            ypos -25
            hbox:
                if renpy.variant("pc"):
                    vbox:
                        style_prefix "check"
                        xsize 400
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                else:
                    vbox:
                        xsize 400
                vbox:
                    xsize 160
                vbox:
                    xsize 100
                vbox:
                    style_prefix "check"
                    xsize 280
                    label _("Font")
                    textbutton "Basic" action [SetVariable ("style.input.caret", "gui/caret.png"), StylePreference("text", "normal"), SetField(persistent, "textstyle", "basic")] hovered [tt.Action("basic")] unhovered [tt.Action("")]
                    textbutton "Pixel" action [SetVariable ("style.input.caret", "gui/caret2.png"), StylePreference("text", "pixel"), SetField(persistent, "textstyle", "pixel")] hovered [tt.Action("pixel")] unhovered [tt.Action("")]
                vbox:
                    yalign 0.75
                    if tt.value == "basic":
                        xsize 300
                        frame:
                            xalign 0.5
                            yalign 0.6
                            xpadding 18
                            ypadding 10
                            text "Easier to read." text_align 0.5 size 28 font "philosopher.ttf"
                    elif tt.value == "pixel":
                        xsize 280
                        frame:
                            xalign 0.5
                            yalign 0.6
                            xpadding 20
                            ypadding 10
                            text "Matches the illustrations." text_align 0.5 size 30 font "munro.ttf"
            null height (1 * gui.pref_spacing)
            hbox:
                vbox:
                    hbox:
                        style_prefix "slider"
                        box_wrap True
                        vbox:
                            label _("Music Volume")
                            hbox:
                                bar value Preference("music volume")
                            label _("Ambient Volume")
                            hbox:
                                bar value Preference("ambient volume")
                            # label _("Sound Effects Volume")
                            # hbox:
                            #     bar value Preference("sound volume")
                            null height gui.pref_spacing
                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"
                vbox:
                    style_prefix "slider"
                    # box_wrap True
                    # xpos -15
                    # null height (2 * gui.pref_spacing)
                    label _("Narration Text Speed")
                    # bar value Preference("text speed")
                    hbox:
                        style_prefix "check"
                        spacing 32
                        # xpos -28
                        textbutton _("Slow") action [SelectedIf(SetVariable("preferences.text_cps", 130)), SetVariable("preferences.text_cps", 130)]
                        textbutton _("Fast") action [SelectedIf(SetVariable("preferences.text_cps", 220)), SetVariable("preferences.text_cps", 220)]
                        textbutton _("Instant") action [SelectedIf(SetVariable("preferences.text_cps", 0)), SetVariable("preferences.text_cps", 0)]
            null height (1 * gui.pref_spacing)
            hbox:
                # box_wrap True
                vbox:
                    style_prefix "check"
                    xsize 660
                    label _("Describe Attitudes")
                    hbox:
                        vbox:
                            xsize 140
                            textbutton _("Yes") action [SetField(persistent, "showattitudetips", True)] hovered [tt3.Action("show")] unhovered [tt.Action("")]
                            textbutton _("No") action [SetField(persistent, "showattitudetips", False)] hovered [tt3.Action("hide")] unhovered [tt.Action("")]
                        vbox:
                            yalign 0.5
                            xsize 520
                            if tt3.value == "show":
                                frame:
                                    xalign 0.5
                                    yalign 0.6
                                    xpadding 18
                                    ypadding 10
                                    if persistent.textstyle == "basic":
                                        text "Essential for\nthe new players." text_align 0.5 size 28 font "philosopher.ttf"
                                    if persistent.textstyle == "pixel":
                                        text "Essential for\nthe new players." text_align 0.5 size 30 font "munro.ttf"
                            elif tt3.value == "hide":
                                frame:
                                    xalign 0.5
                                    yalign 0.6
                                    xpadding 20
                                    ypadding 10
                                    if persistent.textstyle == "basic":
                                        text "Hides the text boxes\nwhen you point at Attitudes." text_align 0.5 size 28 font "philosopher.ttf"
                                    if persistent.textstyle == "pixel":
                                        text "Hides the text boxes\nwhen you point at Attitudes." text_align 0.5 size 30 font "munro.ttf"
                vbox:
                    style_prefix "check"
                    xsize 280
                    label _("Tutorials")
                    textbutton _("Show") action [SetField(persistent, "tutorial_display", True)]
                    textbutton _("Hide") action [SetField(persistent, "tutorial_display", False)]
                vbox:
                    xsize 280
            hbox:
                vbox:
                    style_prefix "check"
                    xsize 280
                    label _("Quotes")
                    textbutton "Show" action [SetField(persistent, "randomquote_show", True)] hovered [tt4.Action("show")] unhovered [tt.Action("")]
                    textbutton "Skip" action [SetField(persistent, "randomquote_show", False)] hovered [tt4.Action("skip")] unhovered [tt.Action("")]
                vbox:
                    yalign 0.5
                    xsize 280
                    if tt4.value == "show":
                        frame:
                            xalign 0.5
                            yalign 0.6
                            xpadding 18
                            ypadding 10
                            if persistent.textstyle == "basic":
                                text "Shows a bit of fluff\nwhenever the game is launched." text_align 0.5 size 28 font "philosopher.ttf"
                            if persistent.textstyle == "pixel":
                                text "Shows a bit of fluff\nwhenever the game is launched." text_align 0.5 size 30 font "munro.ttf"
                    elif tt4.value == "skip":
                        frame:
                            xalign 0.5
                            yalign 0.6
                            xpadding 20
                            ypadding 10
                            if persistent.textstyle == "basic":
                                text "Skips right into the main menu." text_align 0.5 size 28 font "philosopher.ttf"
                            if persistent.textstyle == "pixel":
                                text "Skips right into the main menu." text_align 0.5 size 30 font "munro.ttf"
                vbox:
                    xsize 100
                vbox:
                    style_prefix "check"
                    xsize 280
                    label _("Deaf Support")
                    textbutton _("On") action [SetField(persistent, "deafmode", True)] hovered [tt2.Action("deafmodeon")] unhovered [tt2.Action("")]
                    textbutton _("Off") action [SetField(persistent, "deafmode", False)] hovered [tt2.Action("deafmodeoff")] unhovered [tt2.Action("")]
                vbox:
                    yalign 0.5
                    xsize 280
                    if tt2.value == "deafmodeon":
                        frame:
                            xalign 0.5
                            yalign 0.8
                            xpadding 18
                            ypadding 10
                            if persistent.textstyle == "basic":
                                text "The narration describes sounds\nin greater detail." text_align 0.5 size 28 font "philosopher.ttf"
                            if persistent.textstyle == "pixel":
                                text "The narration describes sounds\nin greater detail." text_align 0.5 size 30 font "munro.ttf"
                    elif tt2.value == "deafmodeoff":
                        frame:
                            xalign 0.5
                            yalign 0.8
                            xpadding 18
                            ypadding 10
                            if persistent.textstyle == "basic":
                                text "Keeps the narration slightly more concise." text_align 0.5 size 28 font "philosopher.ttf"
                            if persistent.textstyle == "pixel":
                                text "Keeps the narration slightly more concise." text_align 0.5 size 30 font "munro.ttf"
            null height (1 * gui.pref_spacing)
            hbox:
                vbox:
                    yalign 0.5
                    xsize 660
                    style_prefix "radio"
                    spacing 20
                    # xpos -28
                    textbutton _("Controls") action ShowMenu("help")
                    textbutton _("Credits") action ShowMenu("about")
                # null height (1 * gui.pref_spacing)
                # vbox:
                #     xsize 100
                hbox:
                    vbox:
                        style_prefix "check"
                        xsize 280
                        label _("Achievements")
                        textbutton _("Show") action [SetField(persistent, "display_achievements", True)]
                        textbutton _("Hide") action [SetField(persistent, "display_achievements", False)]
                    vbox:
                        xsize 280

style pref_label is gui_label
style pref_label_text is gui_label_text:
    size 48
style pref_vbox is vbox
style radio_label is pref_label
style radio_label_text is pref_label_text:
    color "#997577"
style radio_button is gui_button:
    size 48
style radio_button_text is gui_button_text:
    size 48
style radio_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text:
    color "#997577"
style check_button is gui_button
style check_button_text is gui_button_text:
    size 48
style check_vbox is pref_vbox
style slider_label is pref_label
style slider_label_text is pref_label_text:
    color "#997577"
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text:
    size 48
style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text
style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3
style pref_label_text:
    yalign 1.0
style pref_vbox:
    xsize 280
style radio_vbox:
    spacing gui.pref_button_spacing
style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"
style radio_button_text:
    properties gui.button_text_properties("radio_button")
    color "#816271"
    hover_color "#f6d6bd"
    selected_color '#c3a38a'
    insensitive_color "#7d7d7d"
style check_vbox:
    spacing gui.pref_button_spacing
style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
style check_button_text:
    properties gui.button_text_properties("check_button")
    color "#816271"
    hover_color "#f6d6bd"
    selected_color '#c3a38a'
    insensitive_color "#7d7d7d"
style slider_slider:
    xsize 525
style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15
style slider_button_text:
    properties gui.button_text_properties("slider_button")
style slider_vbox:
    xsize 675

## History screen
screen history():
    tag menu
    ## Avoid predicting this screen, as it can be very large.
    predict True
    on "show" action SetVariable("game_menu_screen", "history")
    on "replace" action SetVariable("game_menu_screen", "history")
    use game_menu(_("Archive"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"
        for h in _history_list:
            window:
                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True
                #if h.who:
                #    label h.who:
                #        style "history_name"
                #        substitute False
                        ## Take the color of the who text from the Character, if
                        ## set.
                #        if "color" in h.who_args:
                #            text_color h.who_args["color"]
                $ what = renpy.filter_text_tags(h.what, "color, i, image")
                text what:
                    substitute False
        if not _history_list:
            label _("The archive is empty.")

## This determines what tags are allowed to be displayed on the history screen.
#define gui.history_allow_tags = set("color")

style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_text is gui_text:
    size 30
    color "#c3a38a"
style history_label is gui_label
style history_label_text is gui_label_text
style history_window:
    xfill True
    ysize gui.history_height
style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    line_spacing 12
style history_label:
    xfill True
style history_label_text:
    xalign 0.5

## Help screen

screen help():
    tag menu
    use game_menu(_("Controls"), scroll="viewport"):
        style_prefix "help"
        vbox:
            vbox:
                xpos -100
                spacing 20
                # text "Keyboard"
                use keyboard_help
            vbox:
                textbutton _("Back") action ShowMenu("preferences")

screen keyboard_help():
    hbox:
        label _("Left Click")
        text _("Selects the dialogue options and activates buttons.\nSpeeds up the game.")
    hbox:
        label _("Right Click,\nEscape")
        text _("Opens the main menu, closes various menus."):
            yalign 0.5
    hbox:
        label _("Mouse Wheel")
        text _("Scrolls various windows up and down.")
    hbox:
        label "F5"
        text _("Quick save.")
    hbox:
        label "F8"
        text _("Quick load.")
    hbox:
        label "I"
        text _("Opens the inventory menu.")
    hbox:
        label "J"
        text _("Opens the journal menu.")
    hbox:
        label "C"
        text _("Opens the character sheet menu.")
    hbox:
        label "M"
        text _("Opens the map or the traveling menu.")
    hbox:
        label "R"
        text _("Opens the resting menu.")
    hbox:
        label "W"
        text _("Opens the waiting menu.")
    hbox:
        label _("S")
        text _("Takes a screenshot.")
    hbox:
        label _("Alt+Shift+S")
        text _("Takes a screenshot even with the text input shown.")
    hbox:
        label _("F11,\nF")
        text _("Toggle the full screen."):
            yalign 0.5
    hbox:
        label _("Space")
        text _("Speeds up the game.")
    hbox:
        label _("Shift+O")
        text _("Runs the in-game console. Useful for debugging.")
    hbox:
        label _("Shift+D")
        text _("Runs the developer menu.")

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text:
    color "#997577"
style help_text is gui_text:
    size 40
    color "#c3a38a"
style help_button:
    properties gui.button_properties("help_button")
    xmargin 4
style help_button_text:
    properties gui.button_text_properties("help_button")
style help_label:
    xsize 375
    right_padding 30
style help_label_text:
    size 40
    xalign 1.0
    text_align 1.0

## Confirm screen
screen confirm(message, yes_action, no_action):
    modal True # Ensure other screens do not get input while this screen is displayed.
    zorder 500
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45
            if message == layout.QUIT:
                label _("Are you sure that you want to quit?\nThe game is now autosaved, but you may want to save it manually."):
                    style "confirm_prompt"
                    xalign 0.5
            elif message == layout.ARE_YOU_SURE:
                label _("Are you sure?"):
                    style "confirm_prompt"
                    xalign 0.5
            elif message == layout.DELETE_SAVE:
                label _("Are you sure that you want to\ndelete this save?"):
                    style "confirm_prompt"
                    xalign 0.5
            elif message == layout.OVERWRITE_SAVE:
                label _("Are you sure that you want to\nreplace this save?"):
                    style "confirm_prompt"
                    xalign 0.5
            elif message == layout.LOADING:
                label _("Are you sure?\nLoading will lose the unsaved progress."):
                    style "confirm_prompt"
                    xalign 0.5
            elif message == layout.MAIN_MENU:
                label _("Are you sure that you want to return to the main menu?\nThe game is now autosaved, but you may want to save it manually."):
                    style "confirm_prompt"
                    xalign 0.5
            elif message == layout.END_REPLAY:
                label _("Are you sure that you want to end the replay?"):
                    style "confirm_prompt"
                    xalign 0.5
            elif message == layout.SLOW_SKIP:
                label _("Are you sure that you want to begin skipping?"):
                    style "confirm_prompt"
                    xalign 0.5
            elif message == layout.FAST_SKIP_SEEN:
                label _("Are you sure that you want to skip\nthe seen text until you reach the next choice?"):
                    style "confirm_prompt"
                    xalign 0.5
            elif message == layout.FAST_SKIP_UNSEEN:
                label _("Are you sure that you want to skip\nthe unseen text until you reach the next choice?"):
                    style "confirm_prompt"
                    xalign 0.5
            # elif renpy.get_screen("chooseyourstory"):
            #     label _("Are you sure that you want to\nreset this chapter?"):
            #         style "confirm_prompt"
            #         xalign 0.5
            else:
                label _("[message!t]"):
                    style "confirm_prompt"
                    xalign 0.5
            hbox:
                xalign 0.5
                spacing 150
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
    ## Right-click and escape answer "no".
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text:
    size 40
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text:
    color "#997577"
    hover_color "#f6d6bd"
    size 40
style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
style confirm_text is gui_text
style confirm_prompt_text:
    color "#c3a38a"
    text_align 0.5
    layout "subtitle"
style confirm_button:
    properties gui.button_properties("confirm_button")
style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

## Skip indicator screen
define config.skip_indicator = False
screen skip_indicator():
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 9
            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat
style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text
style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding
style skip_text:
    size gui.notify_text_size
style skip_triangle:
    font "munro.ttf"

screen notify(message):
    zorder 400
    style_prefix "notify"
    button at notify_appear:
        action Hide('notify')
        ypos 44
        xpos 695
        xalign 1.0
        yalign 0.0
        frame:
            xfill True
            style "notify_frame"
            text "[message!tq]":
                style "notify_button_text"
                yalign 0.5
    if message == "Quick save complete.":
        timer 2.00 action Hide('notify')
    elif message == "You’ve restored the quarrel.":
        timer 2.00 action Hide('notify')
    else:
        timer 4.50 action Hide('notify')
    if renpy.get_screen("preferences") or renpy.get_screen("map_display") or renpy.get_screen("map_onlyview") or renpy.get_screen("inventory") or renpy.get_screen("load") or renpy.get_screen("about") or renpy.get_screen("help"):
        timer 0.10 action Hide('notify')

screen notifyimage( msg=None, img=None ):
    zorder 400
    style_prefix "notifyimage"
    button at notify_appear:
        action Hide('notifyimage')
        ypos 44
        xpos 695
        xalign 1.0
        yalign 0.0
        frame:
            xfill True
            xalign 1.0
            style "notifyimage_frame"
            hbox:
                xalign 1.0
                if persistent.textstyle == "basic":
                    text "[msg!tq] {image=[img]}":
                        # xfill True
                        xalign 0.5
                        text_align 1.0
                        style "notifyimage_button_text"
                        yalign 0.5
                if persistent.textstyle == "pixel":
                    text "[msg!tq] {image=coin3}":
                        # xfill True
                        xalign 0.5
                        text_align 1.0
                        style "notifyimage_button_text"
                        yalign 0.5
    timer 4.50 action Hide('notifyimage')
    if renpy.get_screen("preferences") or renpy.get_screen("map_display") or renpy.get_screen("map_onlyview") or renpy.get_screen("inventory") or renpy.get_screen("load") or renpy.get_screen("about") or renpy.get_screen("help"):
        timer 0.10 action Hide('notifyimage')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is say_dialogue:
    # ypos 0
    # xpos 0
    color "#997577"
style notify_button_text is button_text:
    properties gui.button_text_properties("nvl_button")
    hover_color '#f6d6bd'
    size 30
    text_align 1.0
    xalign 1.0
style notify_frame:
    xalign 1.0
    xmaximum 640
    xminimum 640
    background Frame([ "gui/borders_frame.png", "gui/frame.png"], gui.frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
style notify_text:
    properties gui.text_properties("notify")

###################
style notifyimage_frame is empty
style notifyimage_text is say_dialogue:
    text_align 1.0
    xalign 1.0
    color "#997577"
style notifyimage_button_text is button_text:
    properties gui.button_text_properties("nvl_button")
    hover_color '#f6d6bd'
    size 30
    text_align 1.0
    xalign 1.0
style notifyimage_frame:
    xalign 1.0
    xmaximum 640
    xminimum 640
    background Frame([ "gui/borders_frame.png", "gui/frame.png"], gui.frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
style notifyimage_text:
    properties gui.text_properties("notify")

######### ACHIEVEMENTS - ramka z osiągnięciami
default summarizemyjourney = 0
default world_known_npcs = 1 # 1 from military camp
default world_known_areas = 1 # 1 from military camp
default world_peninsulaname = 0
default achievement_readyforaction = 0
default achievement_had100coins = 0
default achievement_animalssavedpoints = 0
default achievement_breakingstuff_points = 0
default achievement_01 = 0
default achievement_magicfruit = 0
default achievement_fish = 0
default achievement_fish_cooked = 0
default achievement_wildplants = 0
default achievement_council = 0
default achievement_anticity = 0
default achievement_murder_fluff = ""
default achievement_alchemy_bugrepellent = 0
default achievement_alchemy_stingointment = 0
default achievement_alchemy_blindingpowder = 0
default achievement_alchemy_witheringdust = 0
default achievement_alchemy_healingpotion = 0
default achievement_alchemy_sharpeningpotion = 0
default achievement_pyrepoints = 0
default persistent.display_achievements = 1

screen achievements(): #steam - basic
    zorder 9
    default tt = Tooltip("")
    default tt2 = Tooltip("")
    if persistent.display_achievements:
        hbox:
            xpos 10
            ypos 5
            spacing 23
            if achievement_01:
                imagebutton:
                    style "achievements_imagebutton"
                    if pc_class == "warrior":
                        idle "achievements/classwarrior.png" at map_dissolve
                        hovered tt.Action("My name is [pcname]. I used to be a fighter.")
                        action NullAction()
                    elif pc_class == "mage":
                        idle "achievements/classmage.png" at map_dissolve
                        hovered tt.Action("My name is [pcname]. I used to be a mage.")
                        action NullAction()
                    elif pc_class == "scholar":
                        idle "achievements/classscholar.png" at map_dissolve
                        hovered tt.Action("My name is [pcname]. I used to be a scholar.")
                        action NullAction()
            if achievement_alchemy_bugrepellent and achievement_alchemy_stingointment and achievement_alchemy_blindingpowder and achievement_alchemy_healingpotion and achievement_alchemy_witheringdust and achievement_alchemy_sharpeningpotion:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/allpotions.png" at map_dissolve
                    hovered tt.Action("I’ve prepared quite a collection of magical mixtures.")
                    action NullAction()
            if pc_firstvillage and not pc_firstvillage == "greenmountaintribe":
                imagebutton:
                    style "achievements_imagebutton"
                    action NullAction()
                    if pc_firstvillage == "howlersdell":
                        hovered tt.Action("The first village I reached was Howler’s Dell.")
                        idle "achievements/firstvillagehowlersdell.png" at map_dissolve
                    if pc_firstvillage == "oldpagos":
                        hovered tt.Action("The first village I reached was Old Págos.")
                        idle "achievements/firstvillageoldpagos.png" at map_dissolve
                    if pc_firstvillage == "whitemarshes":
                        hovered tt.Action("The first village I reached was White Marshes.")
                        idle "achievements/firstvillagewhitemarshes.png" at map_dissolve
                    if pc_firstvillage == "galerocks":
                        hovered tt.Action("The first village I reached was Gale Rocks.")
                        idle "achievements/firstvillagegalerocks.png" at map_dissolve
                    if pc_firstvillage == "creeks":
                        hovered tt.Action("The first village I reached was Creeks.")
                        idle "achievements/firstvillagecreeks.png" at map_dissolve
            if pc_sea_fluff:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/ocean.png" at map_dissolve
                    hovered tt.Action("I managed to reach the sea.")
                    action NullAction()
            if galerocks_npcsmet >= 10 and galerocks_albus_firsttime and galerocks_domitia_firsttime and galerocks_fulvia_firsttime and severina_firsttime and galerocks_saltery_firsttime:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/galerocksnpcs.png" at map_dissolve
                    hovered tt.Action("Even though the people of Gale Rocks were far from friendly,\nI found ways to speak with many of the locals.")
                    action NullAction()
            if westerncrossroads_firsttime and watchtower_firsttime and foggylake_firsttime:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/fourcrossroads.png" at map_dissolve
                    hovered tt.Action("I traveled to the four major crossroads that connect the peninsula.")
                    action NullAction()
            if sleep_monastery and sleep_howlersdell and sleep_druidcave and sleep_watchtower and sleep_eudociahouse and sleep_foggylake and sleep_galerocks and sleep_whitemarshes and sleep_greenmountaintribe:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/slepteverywhere.png" at map_dissolve
                    hovered tt.Action("I rested in each place where a traveler may find shelter.")
                    action NullAction()
            if peltnorth_firsttime and howlersdell_firsttime and oldpagos_firsttime and monastery_firsttime and whitemarshes_firsttime and foggylake_firsttime and creeks_firsttime and galerocks_firsttime and banditshideout_firsttime and greenmountaintribe_firsttime_achievement:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/beenineveryvillage.png" at map_dissolve
                    hovered tt.Action("I visited every settlement in the peninsula.")
                    action NullAction()
            if shortcut_westernentrance_firsttime and shortcut_ibex and shortcut_deepforest_firsttime and shortcut_deepforest_babydragon and shortcut_deepforest_treant and shortcut_deepforest_frightape and shortcut_deepforest_fruitgrove and shortcut_cairn_firsttime and shortcut_meadow_firsttime and shortcut_banditshideout_road_firsttime and shortcut_banditshideout_obstacle1 and shortcut_banditshideout_obstacle2 and shortcut_woodenroad_firsttime and shortcut_woodenroad_stoathunt and shortcut_woodenroad_fisheater and shortcut_woodenroad_horseaccident and shortcut_woodenroad_drinkingcat and shortcut_darkforest_firsttime and shortcut_darkforest_bandit and shortcut_darkforest_goblins and shortcut_darkforest_bagontree and shortcut_darkforest_birdfollower and shortcut_easternentrance_firsttime and shortcut_easternentrance_gnolls:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/shortcutfull.png" at map_dissolve
                    hovered tt.Action("I managed to uncover the entire road leading through the heart of the woods.")
                    action NullAction()
            elif westgate_firsttime and shortcut_westernentrance_firsttime and shortcut_deepforest_firsttime and shortcut_cairn_firsttime and shortcut_woodenroad_firsttime and shortcut_darkforest_firsttime and shortcut_easternentrance_firsttime and stonesign_firsttime:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/shortcut.png" at map_dissolve
                    hovered tt.Action("I managed to get through the heart of the woods.")
                    action NullAction()
            if glaucia_metwith:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/foundbanditshideout.png" at map_dissolve
                    hovered tt.Action("I reached the bandits’ hideout at the heart of the woods.")
                    action NullAction()
            if quest_glauciasupport_description03:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/glauciabravery.png" at map_dissolve
                    hovered tt.Action("I turned Glaucia’s tribe against her,\nand was brave enough to tell her about it.")
                    action NullAction()
            if quest_explorepeninsula_description15a:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/eudociadeal.png" at map_dissolve
                    hovered tt.Action("I convinced Eudocia to start negotiations with the merchants.")
                    action NullAction()
            if greenmountaintribe_firsttime_achievement:
                if not cephasgaiane_dayvisit:
                    imagebutton:
                        style "achievements_imagebutton"
                        idle "achievements/foundgreenmountaintribe.png" at map_dissolve
                        if pc_firstvillage != "greenmountaintribe":
                            hovered tt.Action("I reached The Tribe of The Green Mountain.")
                        else:
                            hovered tt.Action("The first village I reached was The Tribe of The Green Mountain.\nIt was a complete accident.")
                        action NullAction()
                else:
                    imagebutton:
                        style "achievements_imagebutton"
                        idle "achievements/foundgreenmountaintribe2.png" at map_dissolve
                        if pc_firstvillage != "greenmountaintribe":
                            hovered tt.Action("I reached The Tribe of The Green Mountain and spoke with its leaders.")
                        else:
                            hovered tt.Action("I reached The Tribe of The Green Mountain and spoke with its leaders.\nAccidentally, it was the first village I visited.")
                        action NullAction()
            if asterion_found and quest_asterion_description00goodresult:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/asterion02.png" at map_dissolve
                    hovered tt.Action("I managed to discover what happened to Asterion, against all odds,\nand I collected my reward.")
                    action NullAction()
            elif asterion_found:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/asterion01.png" at map_dissolve
                    hovered tt.Action("I managed to discover what happened to Asterion, against all odds.")
                    action NullAction()
            if achievement_council == 1:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/city1.png" at map_dissolve
                    hovered tt.Action("I returned to Hovlavan, and convinced the council\nto invest cautiously in the [world_peninsulaname].")
                    action NullAction()
            elif achievement_council == 2:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/city1.png" at map_dissolve
                    hovered tt.Action("I returned to Hovlavan, and convinced the council\nto invest in [world_peninsulaname].")
                    action NullAction()
            elif achievement_council == 3:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/city2.png" at map_dissolve
                    hovered tt.Action("I returned to Hovlavan, and convinced the council\nto invest eagerly in [world_peninsulaname].")
                    action NullAction()
            if achievement_anticity == 1:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/anticity1.png" at map_dissolve
                    hovered tt.Action("I cut ties with Hovlavan and returned to the peninsula.\nThe tribes, however, have drifted apart.")
                    action NullAction()
            elif achievement_anticity == 2:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/anticity1_alt.png" at map_dissolve
                    hovered tt.Action("I cut ties with Hovlavan and returned to the peninsula.\nIts future was rough, but the tribes tried to help one another.")
                    action NullAction()
            elif achievement_anticity == 3:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/anticity2.png" at map_dissolve
                    hovered tt.Action("I cut ties with Hovlavan and returned to the peninsula.\nThe tribes grew stronger, healing the wounds of the past.")
                    action NullAction()
        hbox:
            xpos 10
            ypos 1035
            spacing 23
            if quest_pc_goal == 2:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/questpcgoal.png" at map_dissolve
                    hovered tt2.Action("[achievement_pc_goal_description]")
                    action NullAction()
            if pc_murdered:
                if sleep_dream_pc_murdered == "doubt":
                    $ achievement_murder_fluff = " I’m not sure it was the right decision."
                elif sleep_dream_pc_murdered == "regret":
                    $ achievement_murder_fluff = " I wish I could go back in time."
                elif sleep_dream_pc_murdered == "shame":
                    $ achievement_murder_fluff = " I hope no one in the city learns the truth."
                elif sleep_dream_pc_murdered == "noregret":
                    $ achievement_murder_fluff = " It was the right choice."
                else:
                    $ achievement_murder_fluff = ""
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/manslaughter.png" at map_dissolve
                    hovered tt.Action("I’ve killed a human.[achievement_murder_fluff]")
                    action NullAction()
            if whitemarshes_nomoreundead or whitemarshes_destroyed:
                if whitemarshes_destroyed:
                    imagebutton:
                        style "achievements_imagebutton"
                        idle "achievements/nomoreundead1.png" at map_dissolve
                        hovered tt2.Action("I got rid of the necromancers of White Marshes, though at a great cost.")
                        action NullAction()
                elif orentius_banished:
                    imagebutton:
                        style "achievements_imagebutton"
                        idle "achievements/nomoreundead2.png" at map_dissolve
                        hovered tt2.Action("I got rid of the undead of White Marshes, though against the villagers’ wishes.")
                        action NullAction()
                elif orentius_convinced:
                    imagebutton:
                        style "achievements_imagebutton"
                        idle "achievements/nomoreundead3.png" at map_dissolve
                        hovered tt2.Action("I convinced the prophet of White Marshes to abandon necromancy.")
                        action NullAction()
            if achievement_pyrepoints >= 5:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/pyre.png" at map_dissolve
                    hovered tt2.Action("I stopped many dead shells from awakening.")
                    action NullAction()
            if description_druids10 and pc_religion == "theunitedchurch":
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/heretic.png" at map_dissolve
                    hovered tt2.Action("I’ve betrayed The United Church by supporting the local druids.\nOther Unites would call me a heretic.")
                    action NullAction()
            elif pc_faithpoints_opportunities >= 8 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75):
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/faithfull.png" at map_dissolve
                    hovered tt2.Action("I’ve relied on my faith to guide me through these difficult times.")
                    action NullAction()
            elif pc_faithpoints_opportunities >= 10 and pc_faithpoints < (pc_faithpoints_opportunities*0.5):
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/nonfaithfull.png" at map_dissolve
                    hovered tt2.Action("During my travels, I left a part of my faith behind me.")
                    action NullAction()
            if achievement_magicfruit:
                imagebutton:
                    style "achievements_imagebutton"
                    if achievement_magicfruit == "atefruit":
                        idle "achievements/magicfruit.png" at map_dissolve
                        hovered tt2.Action("Thanks to a magical fruit, my shell has become stronger than ever.")
                        action NullAction()
                    elif achievement_magicfruit == "sacrificedfruit":
                        idle "achievements/magicfruitb.png" at map_dissolve
                        hovered tt2.Action("I was ready to sacrifice a magical fruit for the sake of others.")
                        action NullAction()
            if item_howlersdelltoken:
                if howlersdell_reputation_status == "ally":
                    imagebutton:
                        style "achievements_imagebutton"
                        idle "achievements/howlersdell.png" at map_dissolve
                        hovered tt2.Action("I’ve become an {i}ally{/i} of Howler’s Dell.")
                        action NullAction()
                elif howlersdell_reputation_status == "friend":
                    imagebutton:
                        style "achievements_imagebutton"
                        idle "achievements/howlersdell.png" at map_dissolve
                        hovered tt2.Action("I’ve become a {i}friend{/i} of Howler’s Dell.")
                        action NullAction()
                else:
                    imagebutton:
                        style "achievements_imagebutton"
                        idle "achievements/howlersdell.png" at map_dissolve
                        hovered tt2.Action("I’ve been rewarded by the people of Howler’s Dell for my service.")
                        action NullAction()
            if pc_lies >= 10:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/lies.png" at map_dissolve
                    hovered tt2.Action("I never hesitated to use lies for my own gain.")
                    action NullAction()
            if thais_rumor_counter >= 10 or (thais_rumor_counter >= 8 and monastery_betrayal_done):
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/rumors.png" at map_dissolve
                    hovered tt2.Action("No soul’s secret was safe with me.")
                    action NullAction()
            if coins >= 100 or achievement_had100coins:
                $ achievement_had100coins = 1
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/100coins.png" at map_dissolve
                    hovered tt2.Action("Even though my journey was short, I was able to gather a great fortune.")
                    action NullAction()
            if monastery_cave_firsttime:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/monastery.png" at map_dissolve
                    hovered tt2.Action("The monks have revealed their secret to me.")
                    action NullAction()
            if foragingground_foraging_vein:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/copper.png" at map_dissolve
                    hovered tt2.Action("I found a promising copper vein.")
                    action NullAction()
            if quest_easternpath_description04 or shortcut_easternentrance_ford_cleared:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/ford.png" at map_dissolve
                    hovered tt2.Action("I fixed the old ford leading to the heart of the forest.")
                    action NullAction()
            if (pc_battlecounter >= 15 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 35 and item_sharpeningpotion_used == day):
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/fightcount03.png" at map_dissolve
                    hovered tt2.Action("I survived more confrontations with hostile creatures than most travelers.")
                    action NullAction()
            elif (pc_battlecounter >= 10 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 30 and item_sharpeningpotion_used == day):
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/fightcount02.png" at map_dissolve
                    hovered tt2.Action("I survived many confrontations with hostile creatures.")
                    action NullAction()
            elif (pc_battlecounter >= 5 and item_sharpeningpotion_used != day) or (pc_battlecounter >= 25 and item_sharpeningpotion_used == day):
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/fightcount01.png" at map_dissolve
                    hovered tt2.Action("I survived a few confrontations with hostile creatures.")
                    action NullAction()
            if achievement_animalssavedpoints >= 7:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/savinganimals.png" at map_dissolve
                    hovered tt2.Action("I often showed mercy to beasts and animals I faced.")
                    action NullAction()
            if bestiary:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/bestiary.png" at map_dissolve
                    hovered tt2.Action("I gained insight into methods of defending myself from wild creatures.")
                    action NullAction()
            if (armor == 4 and pc_hp == 5 and item_axe03) or achievement_readyforaction:
                $ achievement_readyforaction = 1
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/readyforaction.png" at map_dissolve
                    hovered tt2.Action("With a fine axe, gambeson, and vitality I was ready for action.")
                    action NullAction()
            if armor_fixingxp >= 15:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/armorer.png" at map_dissolve
                    hovered tt2.Action("After many hours with thread and tools I became my own armorer.")
                    action NullAction()
            if achievement_fish >= 10:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/caughtafish2.png" at map_dissolve
                    hovered tt2.Action("During my journey, I caught [achievement_fish] fish.")
                    action NullAction()
            elif achievement_fish:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/caughtafish1.png" at map_dissolve
                    hovered tt2.Action("With some time and effort, I managed to catch a fish.")
                    action NullAction()
            if achievement_wildplants >= 12:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/wildplantspicked.png" at map_dissolve
                    hovered tt2.Action("I became quite a forager.")
                    action NullAction()
            if oldtunnel_inside_explored and ruinedvillage_explored and fishinghamlet_areas_seen >= 7 and ruinedshelter_bushes == 2 and ruinedshelter_ruin_cleared:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/ruinsexplored.png" at map_dissolve
                    hovered tt2.Action("I was determined to thoroughly explore every ruin I could find.")
                    action NullAction()
            if quest_easternpath_points >= quest_easternpath_points_max:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/easternpath.png" at map_dissolve
                    hovered tt2.Action("Thanks to me, the eastern path got just a bit safer.")
                    action NullAction()
            if quest_ruins_choice == "thais_defeated":
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/thais_defeated.png" at map_dissolve
                    hovered tt2.Action("Because of me, {color=#f6d6bd}Thais{/color} will face justice\nfor the destruction of {color=#f6d6bd}Steep House{/color}.")
                    action NullAction()
            elif quest_ruins_choice == "thais_alliance":
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/thais_alliance.png" at map_dissolve
                    hovered tt2.Action("I used what my knowledge about {color=#f6d6bd}Steep House{/color} to\ncoerce {color=#f6d6bd}Thais{/color} into working for me.")
                    action NullAction()
            if achievement_breakingstuff_points >= 3:
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/brokendoors.png" at map_dissolve
                    hovered tt2.Action("I had no time for locks and puzzles. It was easier to just break them.")
                    action NullAction()
            if iason_shop_potions_block: # and quest_healingpotion_description03
                imagebutton:
                    style "achievements_imagebutton"
                    idle "achievements/potionsblock.png" at map_dissolve
                    hovered tt2.Action("I managed to flood the market with healing potions.")
                    action NullAction()

    # $achievement.grant("achievement_prologue")
    # init:
    #     $achievement.register("achievement_prologue")
    #     $achievement.sync()

        # $achievement.clear_all()
        # $achievement.grant("achievement_prologue")
        # $achievement.register("achievement_prologue")
        # $achievement.sync()

    if achievement_01 and not achievement.has("achievement_prologue"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_prologue"), Function(achievement.register, "achievement_prologue"), Function(achievement.sync)]
    if achievement_alchemy_bugrepellent and achievement_alchemy_stingointment and achievement_alchemy_blindingpowder and achievement_alchemy_healingpotion and achievement_alchemy_witheringdust and achievement_alchemy_sharpeningpotion and not achievement.has("achievement_potionsset"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_potionsset"), Function(achievement.register, "achievement_potionsset"), Function(achievement.sync)]
    if pc_sea_fluff and not achievement.has("achievement_sea"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_sea"), Function(achievement.register, "achievement_sea"), Function(achievement.sync)]
    if westerncrossroads_firsttime and watchtower_firsttime and foggylake_firsttime and not achievement.has("achievement_crossroads"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_crossroads"), Function(achievement.register, "achievement_crossroads"), Function(achievement.sync)]
    if sleep_monastery and sleep_howlersdell and sleep_druidcave and sleep_watchtower and sleep_eudociahouse and sleep_foggylake and sleep_galerocks and sleep_whitemarshes and sleep_greenmountaintribe and not achievement.has("achievement_slepteverywhere"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_slepteverywhere"), Function(achievement.register, "achievement_slepteverywhere"), Function(achievement.sync)]
    if peltnorth_firsttime and howlersdell_firsttime and oldpagos_firsttime and monastery_firsttime and whitemarshes_firsttime and foggylake_firsttime and creeks_firsttime and galerocks_firsttime and banditshideout_firsttime and greenmountaintribe_firsttime_achievement and not achievement.has("achievement_beenineveryvillage"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_beenineveryvillage"), Function(achievement.register, "achievement_beenineveryvillage"), Function(achievement.sync)]
    if shortcut_westernentrance_firsttime and shortcut_ibex and shortcut_deepforest_firsttime and shortcut_deepforest_babydragon and shortcut_deepforest_treant and shortcut_deepforest_frightape and shortcut_deepforest_fruitgrove and shortcut_cairn_firsttime and shortcut_meadow_firsttime and shortcut_banditshideout_road_firsttime and shortcut_banditshideout_obstacle1 and shortcut_banditshideout_obstacle2 and shortcut_woodenroad_firsttime and shortcut_woodenroad_stoathunt and shortcut_woodenroad_fisheater and shortcut_woodenroad_horseaccident and shortcut_woodenroad_drinkingcat and shortcut_darkforest_firsttime and shortcut_darkforest_bandit and shortcut_darkforest_goblins and shortcut_darkforest_bagontree and shortcut_darkforest_birdfollower and shortcut_easternentrance_firsttime and shortcut_easternentrance_gnolls and not achievement.has("achievement_shortcut"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_shortcut"), Function(achievement.register, "achievement_shortcut"), Function(achievement.sync)]
    if glaucia_metwith and not achievement.has("achievement_foundbanditshideout"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_foundbanditshideout"), Function(achievement.register, "achievement_foundbanditshideout"), Function(achievement.sync)]
    if quest_glauciasupport_description03 and not achievement.has("achievement_glauciabravery"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_glauciabravery"), Function(achievement.register, "achievement_glauciabravery"), Function(achievement.sync)]
    if quest_explorepeninsula_description15a and not achievement.has("achievement_eudociadeal"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_eudociadeal"), Function(achievement.register, "achievement_eudociadeal"), Function(achievement.sync)]
    if greenmountaintribe_firsttime_achievement and cephasgaiane_dayvisit and not achievement.has("achievement_greenmountaintribe"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_greenmountaintribe"), Function(achievement.register, "achievement_greenmountaintribe"), Function(achievement.sync)]
    if asterion_found and not achievement.has("achievement_foundasterion"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_foundasterion"), Function(achievement.register, "achievement_foundasterion"), Function(achievement.sync)]
    if achievement_council == 1 and not achievement.has("achievement_city1"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_city1"), Function(achievement.register, "achievement_city1"), Function(achievement.sync)]
    if achievement_council == 2 and not achievement.has("achievement_city1"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_city1"), Function(achievement.register, "achievement_city1"), Function(achievement.sync)]
    if achievement_council == 3 and not achievement.has("achievement_city1"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_city1"), Function(achievement.register, "achievement_city1"), Function(achievement.sync)]
    if achievement_council == 3 and not achievement.has("achievement_city2"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_city2"), Function(achievement.register, "achievement_city2"), Function(achievement.sync)]

    if achievement_anticity == 2 and not achievement.has("achievement_anticity1"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_anticity1"), Function(achievement.register, "achievement_anticity1"), Function(achievement.sync)]
    if achievement_anticity == 3 and not achievement.has("achievement_anticity1"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_anticity1"), Function(achievement.register, "achievement_anticity1"), Function(achievement.sync)]
    if achievement_anticity == 3 and not achievement.has("achievement_anticity2"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_anticity2"), Function(achievement.register, "achievement_anticity2"), Function(achievement.sync)]

    if item_howlersdelltoken and not achievement.has("achievement_howlersdelltoken"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_howlersdelltoken"), Function(achievement.register, "achievement_howlersdelltoken"), Function(achievement.sync)]
    if pc_lies >= 10 and not achievement.has("achievement_lies"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_lies"), Function(achievement.register, "achievement_lies"), Function(achievement.sync)]
    if (thais_rumor_counter >= 10 and not achievement.has("achievement_rumors")) or (thais_rumor_counter >= 8 and monastery_betrayal_done and not achievement.has("achievement_rumors")):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_rumors"), Function(achievement.register, "achievement_rumors"), Function(achievement.sync)]
    if coins >= 100 or achievement_had100coins and not achievement.has("achievement_coins100"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_coins100"), Function(achievement.register, "achievement_coins100"), Function(achievement.sync)]
    if monastery_cave_firsttime and not achievement.has("achievement_monastery"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_monastery"), Function(achievement.register, "achievement_monastery"), Function(achievement.sync)]
    if foragingground_foraging_vein and not achievement.has("achievement_coppervein"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_coppervein"), Function(achievement.register, "achievement_coppervein"), Function(achievement.sync)]
    if (pc_battlecounter >= 15 and item_sharpeningpotion_used != day and not achievement.has("achievement_battlecounter3")) or (pc_battlecounter >= 35 and item_sharpeningpotion_used == day and not achievement.has("achievement_battlecounter3")):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_battlecounter3"), Function(achievement.register, "achievement_battlecounter3"), Function(achievement.sync)]
    if achievement_animalssavedpoints >= 7 and not achievement.has("achievement_savinganimals"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_savinganimals"), Function(achievement.register, "achievement_savinganimals"), Function(achievement.sync)]
    if bestiary and not achievement.has("achievement_bestiary"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_bestiary"), Function(achievement.register, "achievement_bestiary"), Function(achievement.sync)]
    if (armor == 4 and pc_hp == 5 and item_axe03 and not achievement.has("achievement_readyforaction")) or (achievement_readyforaction and not achievement.has("achievement_readyforaction")):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_readyforaction"), Function(achievement.register, "achievement_readyforaction"), Function(achievement.sync)]
    if armor_fixingxp >= 15 and not achievement.has("achievement_armorer"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_armorer"), Function(achievement.register, "achievement_armorer"), Function(achievement.sync)]
    if achievement_fish >= 10 and not achievement.has("achievement_fish"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_fish"), Function(achievement.register, "achievement_fish"), Function(achievement.sync)]
    if achievement_wildplants >= 12 and not achievement.has("achievement_wildplants"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_wildplants"), Function(achievement.register, "achievement_wildplants"), Function(achievement.sync)]
    if oldtunnel_inside_explored and ruinedvillage_explored and fishinghamlet_areas_seen >= 7 and ruinedshelter_bushes == 2 and ruinedshelter_ruin_cleared and not achievement.has("achievement_ruinsexplored"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_ruinsexplored"), Function(achievement.register, "achievement_ruinsexplored"), Function(achievement.sync)]
    if quest_easternpath_points >= quest_easternpath_points_max and not achievement.has("achievement_easternpath"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_easternpath"), Function(achievement.register, "achievement_easternpath"), Function(achievement.sync)]
    if quest_ruins_choice == "thais_defeated" and not achievement.has("achievement_thais_defeated"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_thais_defeated"), Function(achievement.register, "achievement_thais_defeated"), Function(achievement.sync)]
    if quest_ruins_choice == "thais_alliance" and not achievement.has("achievement_thais_allience"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_thais_allience"), Function(achievement.register, "achievement_thais_allience"), Function(achievement.sync)]
    if achievement_breakingstuff_points >= 3 and not achievement.has("achievement_brokendoors"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_brokendoors"), Function(achievement.register, "achievement_brokendoors"), Function(achievement.sync)]
    if iason_shop_potions_block and not achievement.has("achievement_potionsblock"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_potionsblock"), Function(achievement.register, "achievement_potionsblock"), Function(achievement.sync)]
    if quest_pc_goal == 2 and not achievement.has("achievement_pcgoal"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_pcgoal"), Function(achievement.register, "achievement_pcgoal"), Function(achievement.sync)]
    if pc_murdered and sleep_dream_pc_murdered and not achievement.has("achievement_murdered"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_murdered"), Function(achievement.register, "achievement_murdered"), Function(achievement.sync)]
    if whitemarshes_nomoreundead and orentius_banished and not achievement.has("achievement_nomoreundead"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_nomoreundead"), Function(achievement.register, "achievement_nomoreundead"), Function(achievement.sync)]
    if whitemarshes_nomoreundead and orentius_convinced and not achievement.has("achievement_nomoreundead"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_nomoreundead"), Function(achievement.register, "achievement_nomoreundead"), Function(achievement.sync)]
    if achievement_pyrepoints >= 5 and not achievement.has("achievement_pyre"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_pyre"), Function(achievement.register, "achievement_pyre"), Function(achievement.sync)]
    if pc_faithpoints_opportunities >= 8 and pc_faithpoints >= (pc_faithpoints_opportunities*0.75) and not achievement.has("achievement_faith1"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_faith1"), Function(achievement.register, "achievement_faith1"), Function(achievement.sync)]
    if pc_faithpoints_opportunities >= 10 and pc_faithpoints < (pc_faithpoints_opportunities*0.5) and not achievement.has("achievement_faith2"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_faith2"), Function(achievement.register, "achievement_faith2"), Function(achievement.sync)]
    if achievement_magicfruit == "atefruit" and not achievement.has("achievement_fruit1"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_fruit1"), Function(achievement.register, "achievement_fruit1"), Function(achievement.sync)]
    if achievement_magicfruit == "sacrificedfruit" and not achievement.has("achievement_fruit2"):
        timer 0.5 repeat False action [Function(achievement.grant, "achievement_fruit2"), Function(achievement.register, "achievement_fruit2"), Function(achievement.sync)]

    if tt.value != "":
        frame:
            xalign 0.0
            xpos 49
            ypos 50
            if persistent.textstyle == "basic":
                text tt.value font "philosopher.ttf"
            if persistent.textstyle == "pixel":
                text tt.value font "munro.ttf"
    if tt2.value != "":
        frame:
            xalign 0.0
            xpos 49
            ypos 1030
            yalign 1.0
            if persistent.textstyle == "basic":
                text tt2.value font "philosopher.ttf"
            if persistent.textstyle == "pixel":
                text tt2.value font "munro.ttf"

style achievements_imagebutton:
    xalign 0.0
    yalign 0.0
    focus_mask True

#### TUTORIALS - tutoriale
screen tutorialtooltips():
    zorder 180
    if persistent.tutorial_display:
        if tutorial_inventory:
            frame:
                xalign 0.5
                style "tutorial_frame"
                if persistent.textstyle == "basic":
                    ypos 108
                if persistent.textstyle == "pixel":
                    ypos 110
                xpos 1616
                textbutton "Open your {b}inventory{/b}\nto see your possessions.":
                    action SetVariable("tutorial_inventory", 0)
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if tutorial_journal == 1:
            frame:
                xalign 0.5
                style "tutorial_frame"
                if persistent.textstyle == "basic":
                    ypos 264
                if persistent.textstyle == "pixel":
                    ypos 288
                xpos 1736
                textbutton "Use your {b}journal{/b} to see\nthe list of quests.":
                    action SetVariable("tutorial_journal", 2)
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if tutorial_sheet_display == 1:
            frame:
                style "tutorial_frame"
                xpos 1616
                if persistent.textstyle == "basic":
                    ypos 108
                if persistent.textstyle == "pixel":
                    ypos 110
                textbutton "You can learn more\nabout your abilities\nin the {b}character sheet{/b}.":
                    action SetVariable("tutorial_sheet_display", 0)
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if tutorial_archive:
            frame:
                xalign 0.5
                style "tutorial_frame"
                if persistent.textstyle == "basic":
                    ypos 224
                if persistent.textstyle == "pixel":
                    ypos 242
                xpos 1736
                textbutton "Open the {b}archive{/b} to reread\nthe most recent text.":
                    action SetVariable("tutorial_archive", 0)
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if tutorial_hp == 1:
            frame:
                style "tutorial_frame"
                ypos 550
                xpos 1701
                xalign 0.5
                vbox:
                    spacing 10
                    textbutton "Take care of yourself.\nIf you’re hurt or exhausted,\nsome actions won’t be\navailable to you.{size=-15}\n {/size}\nThe weaker you are, the higher\nthe chance you’ll die in combat.":
                        action SetVariable("tutorial_hp", 2)
                        text_style "tutorial_button_text"
                        text_slow_cps True
        if tutorial_armor == 1:
            frame:
                style "tutorial_frame"
                ypos 680
                xpos 1701
                textbutton "Taking hits will\ndamage your armor.{size=-15}\n {/size}\nYou can then fix it\nin various settlements.":
                    action SetVariable("tutorial_armor", 2)
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if tutorial_eating == 1:
            frame:
                style "tutorial_frame"
                ypos 560
                xpos 1701
                xalign 0.5
                textbutton "Keeping your stomach full\nwill make you stronger.{size=-15}\n {/size}\nStarvation won’t allow you\nto restore vitality\nwhile resting.{size=-15}\n {/size}\nYou can find your supplies\nin the inventory.":
                    action SetVariable("tutorial_eating", 2)
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if tutorial_appearance == 1:
            frame:
                style "tutorial_frame"
                if persistent.textstyle == "basic":
                    ypos 680
                if persistent.textstyle == "pixel":
                    ypos 680
                xpos 1701
                textbutton "Stay tidy to have\na better chance to\ninfluence others.":
                    action SetVariable("tutorial_appearance", 2)
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if tutorial_sleep:
            frame:
                style "tutorial_frame"
                xpos 1588
                if persistent.textstyle == "basic":
                    ypos 184
                if persistent.textstyle == "pixel":
                    ypos 198
                textbutton "You can’t travel during the night.\nPress the {b}sleep{/b} button to rest.":
                    action SetVariable("tutorial_sleep", 0)
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if not tutorial_restatinn:
            if quarters < 36:
                if (quarters < 36 and pc_area == "peltnorth" and peltnorth_resting and not peltnorth_ban_perm and peltnorth_ban_temp != day and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview")) or (quarters < 36 and pc_area == "foggylake" and foggy_about_shelter and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview")) or (quarters < 40 and pc_area == "howlersdell" and howlersdell_eryx_about_room and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview")):
                    frame:
                        style "tutorial_frame"
                        xpos 1588
                        if persistent.textstyle == "basic":
                            ypos 264
                        if persistent.textstyle == "pixel":
                            ypos 288
                        textbutton "If you are at an {b}inn{/b}\nin the morning, you can spend\nthe entire day on resting.":
                            action SetVariable("tutorial_restatinn", 1)
                            text_style "tutorial_button_text"
                            text_slow_cps True
        if tutorial_map == 1:
            frame:
                style "tutorial_frame"
                xpos 1588
                if persistent.textstyle == "basic":
                    ypos 184
                if persistent.textstyle == "pixel":
                    ypos 198
                textbutton "Use the {b}travel{/b} button to\nsee the map and move\nto another area.":
                    action SetVariable("tutorial_map", 0)
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if tutorial_achievements and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview") and persistent.display_achievements:
            frame:
                style "tutorial_frame"
                ypos 2
                xpos 60
                xalign 0
                textbutton "Keep track of your {b}achievements{/b} as your journey unfolds.":
                    action SetVariable("tutorial_achievements", 0)
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if tutorial_input == 1 and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview"):
            frame:
                style "tutorial_frame"
                ypos 90
                xpos 690
                xalign 1.0
                if pc_area == "peltnorth":
                    textbutton "Use your {b}keyboard{/b} to name\npeople that you’re interested in.":
                        action SetVariable("tutorial_input", 2)
                        text_style "tutorial_button_text"
                        text_slow_cps True
                elif pc_area == "foggylake":
                    textbutton "Use your {b}keyboard{/b} to name\nplaces that you’re interested in.":
                        action SetVariable("tutorial_input", 2)
                        text_style "tutorial_button_text"
                        text_slow_cps True
                elif pc_area == "galerocks":
                    textbutton "Use your {b}keyboard{/b} to name\nnames or trades that\nyou’re interested in.":
                        action SetVariable("tutorial_input", 2)
                        text_style "tutorial_button_text"
                        text_slow_cps True
                elif tutorial_input_roots:
                    textbutton "Use your {b}keyboard{/b} to name\nactions that you’re interested in.":
                        action [SetVariable("tutorial_input", 2), SetVariable("tutorial_input_roots", 0)]
                        text_style "tutorial_button_text"
                        text_slow_cps True
                else:
                    textbutton "Use your {b}keyboard{/b} to name\nobjects that you’re interested in.":
                        action SetVariable("tutorial_input", 2)
                        text_style "tutorial_button_text"
                        text_slow_cps True
        if not tutorial_twopictures and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview"):
            if pc_area == "eudociahouse":
                frame:
                    style "tutorial_frame"
                    ypos 63
                    xpos 80
                    xalign 0.0
                    yalign 0.5
                    textbutton "Point at this icon to display\nan entire area at once.":
                        action SetVariable("tutorial_twopictures", 1)
                        text_style "tutorial_button_text"
                        text_slow_cps True
        if tutorial_5hp == 1 and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview"):
            frame:
                style "tutorial_frame"
                # xpos 1704
                xpos 1634
                ypos 548
                xalign 0.5
                yalign 0.0
                xpadding 5
                bottom_padding 10
                vbox:
                    spacing 9
                    textbutton "Your maximum\nvitality grows\nfrom 4 to 5.":
                        action SetVariable("tutorial_5hp", 2)
                        text_style "tutorial_button_text"
                        text_slow_cps True
                        xalign 0.5
                        yalign 0.5
                    # imagebutton:
                    #     focus_mask True
                    #     action SetVariable("tutorial_5hp", 2)
                    #     xalign 0.5
                    #     yalign 0.5
                    #     idle "gui/statuspoints/hp/5hp.png"
        if tutorial_selling == 1 and not tutorial_selling2 and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview"):
            frame:
                style "tutorial_frame"
                xalign 1.0
                yalign 0.0
                ypos 81
                xpos 690
                textbutton "Different traders are interested in different goods.\nThey will purchase only some of the things\nyou have to sell, and their offers may vary.":
                    action SetVariable("tutorial_selling", 2)
                    text_style "tutorial_button_text"
                    text_slow_cps True
        elif tutorial_selling == 1 and tutorial_selling2 == 1 and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview") and renpy.get_screen("selling"):
            frame:
                style "tutorial_frame"
                xalign 1.0
                yalign 0.0
                ypos 81
                xpos 587
                textbutton "Select an item you’d like to offer.\n\nDifferent traders are interested\nin different goods.\nThey will purchase only some of the things\nyou have to sell, and their offers may vary.":
                    action [SetVariable("tutorial_selling", 2), SetVariable("tutorial_selling2", 2)]
                    text_style "tutorial_button_text"
                    text_slow_cps True
        elif tutorial_selling2 == 1 and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview") and renpy.get_screen("selling"):
            frame:
                style "tutorial_frame"
                xalign 1.0
                yalign 0.0
                ypos 81
                xpos 587
                textbutton "Select an item you’d like to offer.":
                    action [SetVariable("tutorial_selling2", 2)]
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if tutorial_bogdaylength == 1 and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview"):
            frame:
                style "tutorial_frame"
                ypos 412
                # if persistent.textstyle == "basic":
                #     ypos 258
                # if persistent.textstyle == "pixel":
                #     ypos 272
                xpos 1702
                textbutton "Bogs are darker than forests.\nThe local creatures start their hunt\nup to an hour earlier.":
                    action [SetVariable("tutorial_bogdaylength", 2)]
                    text_style "tutorial_button_text"
                    text_slow_cps True
        if (not tutorial_lateevening and day == 1 and quarters >= (world_daylength-12) and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview")) or (not tutorial_lateevening and day == 1 and world_daylength_bogs and quarters >= (world_daylength-16) and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview")):
            frame:
                xalign 0.5
                style "tutorial_frame"
                ypos 412
                # if persistent.textstyle == "basic":
                #     ypos 264
                # if persistent.textstyle == "pixel":
                #     ypos 288
                xpos 1701
                textbutton "It’s getting late.\nBetter look for\na safe place to {b}sleep{/b}.":
                    action SetVariable("tutorial_lateevening", 1)
                    text_style "tutorial_button_text"
                    text_slow_cps True

style tutorial_button_text is button_text:
    properties gui.button_text_properties("nvl_button")
    hover_color '#f6d6bd'
    size 24
    text_align 0.5
    line_spacing +2
style tutorial_button2_text is button_text:
    properties gui.button_text_properties("nvl_button")
    hover_color '#f6d6bd'
    size 27
    text_align 0.5
style tutorial_frame is gui_frame:
    background Frame([ "gui/borders_frame.png", "gui/frame.png"], gui.frame_borders, tile=gui.frame_tile)
    xpadding 8
    ypadding 6
    xalign 0.5
    yalign 0.0

######### CHARACTER STATUS SCREEN
screen characterstatus():
    zorder 100
    default tt = Tooltip("")
    default displayedmaxhp = 4
    default didisplayedappearance = ""
    default displayedcleanliness = ""
    default displayedcleanliness_clothes_torn = ""
    default displayedcleanliness_clothes_blood = ""
    default displayedfancyclothes = ""
    default displayedappearancehp = ""
    if not pc_hp_can5:
        $ displayedmaxhp = 4
    else:
        $ displayedmaxhp = 5
    if timescreen == 1:#clock
        imagebutton:
            # focus_mask True
            xpos 1667
            ypos 401
            yalign 1.0
            if day >= world_deadline:
                idle "gui/clock/80/51.png" at map_dissolve
                hovered [SetVariable("charactertooltipypos", 0), tt.Action("clock")]
                action NullAction()
            else:
                if world_daylength == 84:
                    if quarters == 22:
                        idle "gui/clock/84/22.png" at map_dissolve
                    elif quarters == 23:
                        idle "gui/clock/84/23.png" at map_dissolve
                    elif quarters == 24:
                        idle "gui/clock/84/24.png" at map_dissolve
                    elif quarters == 25:
                        idle "gui/clock/84/25.png" at map_dissolve
                    elif quarters == 26:
                        idle "gui/clock/84/26.png" at map_dissolve
                    elif quarters == 27:
                        idle "gui/clock/84/27.png" at map_dissolve
                    elif quarters == 28:
                        idle "gui/clock/84/28.png" at map_dissolve
                    elif quarters == 29:
                        idle "gui/clock/84/29.png" at map_dissolve
                    elif quarters == 30:
                        idle "gui/clock/84/30.png" at map_dissolve
                    elif quarters == 31:
                        idle "gui/clock/84/31.png" at map_dissolve
                    elif quarters == 32:
                        idle "gui/clock/84/32.png" at map_dissolve
                    elif quarters == 33:
                        idle "gui/clock/84/33.png" at map_dissolve
                    elif quarters == 34:
                        idle "gui/clock/84/34.png" at map_dissolve
                    elif quarters == 35:
                        idle "gui/clock/84/35.png" at map_dissolve
                    elif quarters == 36:
                        idle "gui/clock/84/36.png" at map_dissolve
                    elif quarters == 37:
                        idle "gui/clock/84/37.png" at map_dissolve
                    elif quarters == 38:
                        idle "gui/clock/84/38.png" at map_dissolve
                    elif quarters == 39:
                        idle "gui/clock/84/39.png" at map_dissolve
                    elif quarters == 40:
                        idle "gui/clock/84/40.png" at map_dissolve
                    elif quarters == 41:
                        idle "gui/clock/84/41.png" at map_dissolve
                    elif quarters == 42:
                        idle "gui/clock/84/42.png" at map_dissolve
                    elif quarters == 43:
                        idle "gui/clock/84/43.png" at map_dissolve
                    elif quarters == 44:
                        idle "gui/clock/84/44.png" at map_dissolve
                    elif quarters == 45:
                        idle "gui/clock/84/45.png" at map_dissolve
                    elif quarters == 46:
                        idle "gui/clock/84/46.png" at map_dissolve
                    elif quarters == 47:
                        idle "gui/clock/84/47.png" at map_dissolve
                    elif quarters == 48:
                        idle "gui/clock/84/48.png" at map_dissolve
                    elif quarters == 49:
                        idle "gui/clock/84/49.png" at map_dissolve
                    elif quarters == 50:
                        idle "gui/clock/84/50.png" at map_dissolve
                    elif quarters == 51:
                        idle "gui/clock/84/51.png" at map_dissolve
                    elif quarters == 52:
                        idle "gui/clock/84/52.png" at map_dissolve
                    elif quarters == 53:
                        idle "gui/clock/84/53.png" at map_dissolve
                    elif quarters == 54:
                        idle "gui/clock/84/54.png" at map_dissolve
                    elif quarters == 55:
                        idle "gui/clock/84/55.png" at map_dissolve
                    elif quarters == 56:
                        idle "gui/clock/84/56.png" at map_dissolve
                    elif quarters == 57:
                        idle "gui/clock/84/57.png" at map_dissolve
                    elif quarters == 58:
                        idle "gui/clock/84/58.png" at map_dissolve
                    elif quarters == 59:
                        idle "gui/clock/84/59.png" at map_dissolve
                    elif quarters == 60:
                        idle "gui/clock/84/60.png" at map_dissolve
                    elif quarters == 61:
                        idle "gui/clock/84/61.png" at map_dissolve
                    elif quarters == 62:
                        idle "gui/clock/84/62.png" at map_dissolve
                    elif quarters == 63:
                        idle "gui/clock/84/63.png" at map_dissolve
                    elif quarters == 64:
                        idle "gui/clock/84/64.png" at map_dissolve
                    elif quarters == 65:
                        idle "gui/clock/84/65.png" at map_dissolve
                    elif quarters == 66:
                        idle "gui/clock/84/66.png" at map_dissolve
                    elif quarters == 67:
                        idle "gui/clock/84/67.png" at map_dissolve
                    elif quarters == 68:
                        idle "gui/clock/84/68.png" at map_dissolve
                    elif quarters == 69:
                        idle "gui/clock/84/69.png" at map_dissolve
                    elif quarters == 70:
                        idle "gui/clock/84/70.png" at map_dissolve
                    elif quarters == 71:
                        idle "gui/clock/84/71.png" at map_dissolve
                    elif quarters == 72:
                        idle "gui/clock/84/72.png" at map_dissolve
                    elif quarters == 73:
                        idle "gui/clock/84/73.png" at map_dissolve
                    elif quarters == 74:
                        idle "gui/clock/84/74.png" at map_dissolve
                    elif quarters == 75:
                        idle "gui/clock/84/75.png" at map_dissolve
                    elif quarters == 76:
                        idle "gui/clock/84/76.png" at map_dissolve
                    elif quarters == 77:
                        idle "gui/clock/84/77.png" at map_dissolve
                    elif quarters == 78:
                        idle "gui/clock/84/78.png" at map_dissolve
                    elif quarters == 79:
                        idle "gui/clock/84/79.png" at map_dissolve
                    elif quarters == 80:
                        idle "gui/clock/84/80.png" at map_dissolve
                    elif quarters == 81:
                        idle "gui/clock/84/81.png" at map_dissolve
                    elif quarters == 82:
                        idle "gui/clock/84/82.png" at map_dissolve
                    elif quarters == 83:
                        idle "gui/clock/84/83.png" at map_dissolve
                    elif quarters == 84:
                        idle "gui/clock/84/84.png" at map_dissolve
                    else:
                        idle "gui/clock/midnight.png" at map_dissolve
                elif world_daylength == 83:
                    if quarters == 22:
                        idle "gui/clock/83/22.png" at map_dissolve
                    elif quarters == 23:
                        idle "gui/clock/83/23.png" at map_dissolve
                    elif quarters == 24:
                        idle "gui/clock/83/24.png" at map_dissolve
                    elif quarters == 25:
                        idle "gui/clock/83/25.png" at map_dissolve
                    elif quarters == 26:
                        idle "gui/clock/83/26.png" at map_dissolve
                    elif quarters == 27:
                        idle "gui/clock/83/27.png" at map_dissolve
                    elif quarters == 28:
                        idle "gui/clock/83/28.png" at map_dissolve
                    elif quarters == 29:
                        idle "gui/clock/83/29.png" at map_dissolve
                    elif quarters == 30:
                        idle "gui/clock/83/30.png" at map_dissolve
                    elif quarters == 31:
                        idle "gui/clock/83/31.png" at map_dissolve
                    elif quarters == 32:
                        idle "gui/clock/83/32.png" at map_dissolve
                    elif quarters == 33:
                        idle "gui/clock/83/33.png" at map_dissolve
                    elif quarters == 34:
                        idle "gui/clock/83/34.png" at map_dissolve
                    elif quarters == 35:
                        idle "gui/clock/83/35.png" at map_dissolve
                    elif quarters == 36:
                        idle "gui/clock/83/36.png" at map_dissolve
                    elif quarters == 37:
                        idle "gui/clock/83/37.png" at map_dissolve
                    elif quarters == 38:
                        idle "gui/clock/83/38.png" at map_dissolve
                    elif quarters == 39:
                        idle "gui/clock/83/39.png" at map_dissolve
                    elif quarters == 40:
                        idle "gui/clock/83/40.png" at map_dissolve
                    elif quarters == 41:
                        idle "gui/clock/83/41.png" at map_dissolve
                    elif quarters == 42:
                        idle "gui/clock/83/42.png" at map_dissolve
                    elif quarters == 43:
                        idle "gui/clock/83/43.png" at map_dissolve
                    elif quarters == 44:
                        idle "gui/clock/83/44.png" at map_dissolve
                    elif quarters == 45:
                        idle "gui/clock/83/45.png" at map_dissolve
                    elif quarters == 46:
                        idle "gui/clock/83/46.png" at map_dissolve
                    elif quarters == 47:
                        idle "gui/clock/83/47.png" at map_dissolve
                    elif quarters == 48:
                        idle "gui/clock/83/48.png" at map_dissolve
                    elif quarters == 49:
                        idle "gui/clock/83/49.png" at map_dissolve
                    elif quarters == 50:
                        idle "gui/clock/83/50.png" at map_dissolve
                    elif quarters == 51:
                        idle "gui/clock/83/51.png" at map_dissolve
                    elif quarters == 52:
                        idle "gui/clock/83/52.png" at map_dissolve
                    elif quarters == 53:
                        idle "gui/clock/83/53.png" at map_dissolve
                    elif quarters == 54:
                        idle "gui/clock/83/54.png" at map_dissolve
                    elif quarters == 55:
                        idle "gui/clock/83/55.png" at map_dissolve
                    elif quarters == 56:
                        idle "gui/clock/83/56.png" at map_dissolve
                    elif quarters == 57:
                        idle "gui/clock/83/57.png" at map_dissolve
                    elif quarters == 58:
                        idle "gui/clock/83/58.png" at map_dissolve
                    elif quarters == 59:
                        idle "gui/clock/83/59.png" at map_dissolve
                    elif quarters == 60:
                        idle "gui/clock/83/60.png" at map_dissolve
                    elif quarters == 61:
                        idle "gui/clock/83/61.png" at map_dissolve
                    elif quarters == 62:
                        idle "gui/clock/83/62.png" at map_dissolve
                    elif quarters == 63:
                        idle "gui/clock/83/63.png" at map_dissolve
                    elif quarters == 64:
                        idle "gui/clock/83/64.png" at map_dissolve
                    elif quarters == 65:
                        idle "gui/clock/83/65.png" at map_dissolve
                    elif quarters == 66:
                        idle "gui/clock/83/66.png" at map_dissolve
                    elif quarters == 67:
                        idle "gui/clock/83/67.png" at map_dissolve
                    elif quarters == 68:
                        idle "gui/clock/83/68.png" at map_dissolve
                    elif quarters == 69:
                        idle "gui/clock/83/69.png" at map_dissolve
                    elif quarters == 70:
                        idle "gui/clock/83/70.png" at map_dissolve
                    elif quarters == 71:
                        idle "gui/clock/83/71.png" at map_dissolve
                    elif quarters == 72:
                        idle "gui/clock/83/72.png" at map_dissolve
                    elif quarters == 73:
                        idle "gui/clock/83/73.png" at map_dissolve
                    elif quarters == 74:
                        idle "gui/clock/83/74.png" at map_dissolve
                    elif quarters == 75:
                        idle "gui/clock/83/75.png" at map_dissolve
                    elif quarters == 76:
                        idle "gui/clock/83/76.png" at map_dissolve
                    elif quarters == 77:
                        idle "gui/clock/83/77.png" at map_dissolve
                    elif quarters == 78:
                        idle "gui/clock/83/78.png" at map_dissolve
                    elif quarters == 79:
                        idle "gui/clock/83/79.png" at map_dissolve
                    elif quarters == 80:
                        idle "gui/clock/83/80.png" at map_dissolve
                    elif quarters == 81:
                        idle "gui/clock/83/81.png" at map_dissolve
                    elif quarters == 82:
                        idle "gui/clock/83/82.png" at map_dissolve
                    elif quarters == 83:
                        idle "gui/clock/83/83.png" at map_dissolve
                    else:
                        idle "gui/clock/midnight.png" at map_dissolve
                elif world_daylength == 82:
                    if quarters == 22:
                        idle "gui/clock/82/22.png" at map_dissolve
                    elif quarters == 23:
                        idle "gui/clock/82/23.png" at map_dissolve
                    elif quarters == 24:
                        idle "gui/clock/82/24.png" at map_dissolve
                    elif quarters == 25:
                        idle "gui/clock/82/25.png" at map_dissolve
                    elif quarters == 26:
                        idle "gui/clock/82/26.png" at map_dissolve
                    elif quarters == 27:
                        idle "gui/clock/82/27.png" at map_dissolve
                    elif quarters == 28:
                        idle "gui/clock/82/28.png" at map_dissolve
                    elif quarters == 29:
                        idle "gui/clock/82/29.png" at map_dissolve
                    elif quarters == 30:
                        idle "gui/clock/82/30.png" at map_dissolve
                    elif quarters == 31:
                        idle "gui/clock/82/31.png" at map_dissolve
                    elif quarters == 32:
                        idle "gui/clock/82/32.png" at map_dissolve
                    elif quarters == 33:
                        idle "gui/clock/82/33.png" at map_dissolve
                    elif quarters == 34:
                        idle "gui/clock/82/34.png" at map_dissolve
                    elif quarters == 35:
                        idle "gui/clock/82/35.png" at map_dissolve
                    elif quarters == 36:
                        idle "gui/clock/82/36.png" at map_dissolve
                    elif quarters == 37:
                        idle "gui/clock/82/37.png" at map_dissolve
                    elif quarters == 38:
                        idle "gui/clock/82/38.png" at map_dissolve
                    elif quarters == 39:
                        idle "gui/clock/82/39.png" at map_dissolve
                    elif quarters == 40:
                        idle "gui/clock/82/40.png" at map_dissolve
                    elif quarters == 41:
                        idle "gui/clock/82/41.png" at map_dissolve
                    elif quarters == 42:
                        idle "gui/clock/82/42.png" at map_dissolve
                    elif quarters == 43:
                        idle "gui/clock/82/43.png" at map_dissolve
                    elif quarters == 44:
                        idle "gui/clock/82/44.png" at map_dissolve
                    elif quarters == 45:
                        idle "gui/clock/82/45.png" at map_dissolve
                    elif quarters == 46:
                        idle "gui/clock/82/46.png" at map_dissolve
                    elif quarters == 47:
                        idle "gui/clock/82/47.png" at map_dissolve
                    elif quarters == 48:
                        idle "gui/clock/82/48.png" at map_dissolve
                    elif quarters == 49:
                        idle "gui/clock/82/49.png" at map_dissolve
                    elif quarters == 50:
                        idle "gui/clock/82/50.png" at map_dissolve
                    elif quarters == 51:
                        idle "gui/clock/82/51.png" at map_dissolve
                    elif quarters == 52:
                        idle "gui/clock/82/52.png" at map_dissolve
                    elif quarters == 53:
                        idle "gui/clock/82/53.png" at map_dissolve
                    elif quarters == 54:
                        idle "gui/clock/82/54.png" at map_dissolve
                    elif quarters == 55:
                        idle "gui/clock/82/55.png" at map_dissolve
                    elif quarters == 56:
                        idle "gui/clock/82/56.png" at map_dissolve
                    elif quarters == 57:
                        idle "gui/clock/82/57.png" at map_dissolve
                    elif quarters == 58:
                        idle "gui/clock/82/58.png" at map_dissolve
                    elif quarters == 59:
                        idle "gui/clock/82/59.png" at map_dissolve
                    elif quarters == 60:
                        idle "gui/clock/82/60.png" at map_dissolve
                    elif quarters == 61:
                        idle "gui/clock/82/61.png" at map_dissolve
                    elif quarters == 62:
                        idle "gui/clock/82/62.png" at map_dissolve
                    elif quarters == 63:
                        idle "gui/clock/82/63.png" at map_dissolve
                    elif quarters == 64:
                        idle "gui/clock/82/64.png" at map_dissolve
                    elif quarters == 65:
                        idle "gui/clock/82/65.png" at map_dissolve
                    elif quarters == 66:
                        idle "gui/clock/82/66.png" at map_dissolve
                    elif quarters == 67:
                        idle "gui/clock/82/67.png" at map_dissolve
                    elif quarters == 68:
                        idle "gui/clock/82/68.png" at map_dissolve
                    elif quarters == 69:
                        idle "gui/clock/82/69.png" at map_dissolve
                    elif quarters == 70:
                        idle "gui/clock/82/70.png" at map_dissolve
                    elif quarters == 71:
                        idle "gui/clock/82/71.png" at map_dissolve
                    elif quarters == 72:
                        idle "gui/clock/82/72.png" at map_dissolve
                    elif quarters == 73:
                        idle "gui/clock/82/73.png" at map_dissolve
                    elif quarters == 74:
                        idle "gui/clock/82/74.png" at map_dissolve
                    elif quarters == 75:
                        idle "gui/clock/82/75.png" at map_dissolve
                    elif quarters == 76:
                        idle "gui/clock/82/76.png" at map_dissolve
                    elif quarters == 77:
                        idle "gui/clock/82/77.png" at map_dissolve
                    elif quarters == 78:
                        idle "gui/clock/82/78.png" at map_dissolve
                    elif quarters == 79:
                        idle "gui/clock/82/79.png" at map_dissolve
                    elif quarters == 80:
                        idle "gui/clock/82/80.png" at map_dissolve
                    elif quarters == 81:
                        idle "gui/clock/82/81.png" at map_dissolve
                    elif quarters == 82:
                        idle "gui/clock/82/82.png" at map_dissolve
                    else:
                        idle "gui/clock/midnight.png" at map_dissolve
                elif world_daylength == 81:
                    if quarters == 22:
                        idle "gui/clock/81/22.png" at map_dissolve
                    elif quarters == 23:
                        idle "gui/clock/81/23.png" at map_dissolve
                    elif quarters == 24:
                        idle "gui/clock/81/24.png" at map_dissolve
                    elif quarters == 25:
                        idle "gui/clock/81/25.png" at map_dissolve
                    elif quarters == 26:
                        idle "gui/clock/81/26.png" at map_dissolve
                    elif quarters == 27:
                        idle "gui/clock/81/27.png" at map_dissolve
                    elif quarters == 28:
                        idle "gui/clock/81/28.png" at map_dissolve
                    elif quarters == 29:
                        idle "gui/clock/81/29.png" at map_dissolve
                    elif quarters == 30:
                        idle "gui/clock/81/30.png" at map_dissolve
                    elif quarters == 31:
                        idle "gui/clock/81/31.png" at map_dissolve
                    elif quarters == 32:
                        idle "gui/clock/81/32.png" at map_dissolve
                    elif quarters == 33:
                        idle "gui/clock/81/33.png" at map_dissolve
                    elif quarters == 34:
                        idle "gui/clock/81/34.png" at map_dissolve
                    elif quarters == 35:
                        idle "gui/clock/81/35.png" at map_dissolve
                    elif quarters == 36:
                        idle "gui/clock/81/36.png" at map_dissolve
                    elif quarters == 37:
                        idle "gui/clock/81/37.png" at map_dissolve
                    elif quarters == 38:
                        idle "gui/clock/81/38.png" at map_dissolve
                    elif quarters == 39:
                        idle "gui/clock/81/39.png" at map_dissolve
                    elif quarters == 40:
                        idle "gui/clock/81/40.png" at map_dissolve
                    elif quarters == 41:
                        idle "gui/clock/81/41.png" at map_dissolve
                    elif quarters == 42:
                        idle "gui/clock/81/42.png" at map_dissolve
                    elif quarters == 43:
                        idle "gui/clock/81/43.png" at map_dissolve
                    elif quarters == 44:
                        idle "gui/clock/81/44.png" at map_dissolve
                    elif quarters == 45:
                        idle "gui/clock/81/45.png" at map_dissolve
                    elif quarters == 46:
                        idle "gui/clock/81/46.png" at map_dissolve
                    elif quarters == 47:
                        idle "gui/clock/81/47.png" at map_dissolve
                    elif quarters == 48:
                        idle "gui/clock/81/48.png" at map_dissolve
                    elif quarters == 49:
                        idle "gui/clock/81/49.png" at map_dissolve
                    elif quarters == 50:
                        idle "gui/clock/81/50.png" at map_dissolve
                    elif quarters == 51:
                        idle "gui/clock/81/51.png" at map_dissolve
                    elif quarters == 52:
                        idle "gui/clock/81/52.png" at map_dissolve
                    elif quarters == 53:
                        idle "gui/clock/81/53.png" at map_dissolve
                    elif quarters == 54:
                        idle "gui/clock/81/54.png" at map_dissolve
                    elif quarters == 55:
                        idle "gui/clock/81/55.png" at map_dissolve
                    elif quarters == 56:
                        idle "gui/clock/81/56.png" at map_dissolve
                    elif quarters == 57:
                        idle "gui/clock/81/57.png" at map_dissolve
                    elif quarters == 58:
                        idle "gui/clock/81/58.png" at map_dissolve
                    elif quarters == 59:
                        idle "gui/clock/81/59.png" at map_dissolve
                    elif quarters == 60:
                        idle "gui/clock/81/60.png" at map_dissolve
                    elif quarters == 61:
                        idle "gui/clock/81/61.png" at map_dissolve
                    elif quarters == 62:
                        idle "gui/clock/81/62.png" at map_dissolve
                    elif quarters == 63:
                        idle "gui/clock/81/63.png" at map_dissolve
                    elif quarters == 64:
                        idle "gui/clock/81/64.png" at map_dissolve
                    elif quarters == 65:
                        idle "gui/clock/81/65.png" at map_dissolve
                    elif quarters == 66:
                        idle "gui/clock/81/66.png" at map_dissolve
                    elif quarters == 67:
                        idle "gui/clock/81/67.png" at map_dissolve
                    elif quarters == 68:
                        idle "gui/clock/81/68.png" at map_dissolve
                    elif quarters == 69:
                        idle "gui/clock/81/69.png" at map_dissolve
                    elif quarters == 70:
                        idle "gui/clock/81/70.png" at map_dissolve
                    elif quarters == 71:
                        idle "gui/clock/81/71.png" at map_dissolve
                    elif quarters == 72:
                        idle "gui/clock/81/72.png" at map_dissolve
                    elif quarters == 73:
                        idle "gui/clock/81/73.png" at map_dissolve
                    elif quarters == 74:
                        idle "gui/clock/81/74.png" at map_dissolve
                    elif quarters == 75:
                        idle "gui/clock/81/75.png" at map_dissolve
                    elif quarters == 76:
                        idle "gui/clock/81/76.png" at map_dissolve
                    elif quarters == 77:
                        idle "gui/clock/81/77.png" at map_dissolve
                    elif quarters == 78:
                        idle "gui/clock/81/78.png" at map_dissolve
                    elif quarters == 79:
                        idle "gui/clock/81/79.png" at map_dissolve
                    elif quarters == 80:
                        idle "gui/clock/81/80.png" at map_dissolve
                    elif quarters == 81:
                        idle "gui/clock/81/81.png" at map_dissolve
                    else:
                        idle "gui/clock/midnight.png" at map_dissolve
                elif world_daylength == 80:
                    if quarters == 22:
                        idle "gui/clock/80/22.png" at map_dissolve
                    elif quarters == 23:
                        idle "gui/clock/80/23.png" at map_dissolve
                    elif quarters == 24:
                        idle "gui/clock/80/24.png" at map_dissolve
                    elif quarters == 25:
                        idle "gui/clock/80/25.png" at map_dissolve
                    elif quarters == 26:
                        idle "gui/clock/80/26.png" at map_dissolve
                    elif quarters == 27:
                        idle "gui/clock/80/27.png" at map_dissolve
                    elif quarters == 28:
                        idle "gui/clock/80/28.png" at map_dissolve
                    elif quarters == 29:
                        idle "gui/clock/80/29.png" at map_dissolve
                    elif quarters == 30:
                        idle "gui/clock/80/30.png" at map_dissolve
                    elif quarters == 31:
                        idle "gui/clock/80/31.png" at map_dissolve
                    elif quarters == 32:
                        idle "gui/clock/80/32.png" at map_dissolve
                    elif quarters == 33:
                        idle "gui/clock/80/33.png" at map_dissolve
                    elif quarters == 34:
                        idle "gui/clock/80/34.png" at map_dissolve
                    elif quarters == 35:
                        idle "gui/clock/80/35.png" at map_dissolve
                    elif quarters == 36:
                        idle "gui/clock/80/36.png" at map_dissolve
                    elif quarters == 37:
                        idle "gui/clock/80/37.png" at map_dissolve
                    elif quarters == 38:
                        idle "gui/clock/80/38.png" at map_dissolve
                    elif quarters == 39:
                        idle "gui/clock/80/39.png" at map_dissolve
                    elif quarters == 40:
                        idle "gui/clock/80/40.png" at map_dissolve
                    elif quarters == 41:
                        idle "gui/clock/80/41.png" at map_dissolve
                    elif quarters == 42:
                        idle "gui/clock/80/42.png" at map_dissolve
                    elif quarters == 43:
                        idle "gui/clock/80/43.png" at map_dissolve
                    elif quarters == 44:
                        idle "gui/clock/80/44.png" at map_dissolve
                    elif quarters == 45:
                        idle "gui/clock/80/45.png" at map_dissolve
                    elif quarters == 46:
                        idle "gui/clock/80/46.png" at map_dissolve
                    elif quarters == 47:
                        idle "gui/clock/80/47.png" at map_dissolve
                    elif quarters == 48:
                        idle "gui/clock/80/48.png" at map_dissolve
                    elif quarters == 49:
                        idle "gui/clock/80/49.png" at map_dissolve
                    elif quarters == 50:
                        idle "gui/clock/80/50.png" at map_dissolve
                    elif quarters == 51:
                        idle "gui/clock/80/51.png" at map_dissolve
                    elif quarters == 52:
                        idle "gui/clock/80/52.png" at map_dissolve
                    elif quarters == 53:
                        idle "gui/clock/80/53.png" at map_dissolve
                    elif quarters == 54:
                        idle "gui/clock/80/54.png" at map_dissolve
                    elif quarters == 55:
                        idle "gui/clock/80/55.png" at map_dissolve
                    elif quarters == 56:
                        idle "gui/clock/80/56.png" at map_dissolve
                    elif quarters == 57:
                        idle "gui/clock/80/57.png" at map_dissolve
                    elif quarters == 58:
                        idle "gui/clock/80/58.png" at map_dissolve
                    elif quarters == 59:
                        idle "gui/clock/80/59.png" at map_dissolve
                    elif quarters == 60:
                        idle "gui/clock/80/60.png" at map_dissolve
                    elif quarters == 61:
                        idle "gui/clock/80/61.png" at map_dissolve
                    elif quarters == 62:
                        idle "gui/clock/80/62.png" at map_dissolve
                    elif quarters == 63:
                        idle "gui/clock/80/63.png" at map_dissolve
                    elif quarters == 64:
                        idle "gui/clock/80/64.png" at map_dissolve
                    elif quarters == 65:
                        idle "gui/clock/80/65.png" at map_dissolve
                    elif quarters == 66:
                        idle "gui/clock/80/66.png" at map_dissolve
                    elif quarters == 67:
                        idle "gui/clock/80/67.png" at map_dissolve
                    elif quarters == 68:
                        idle "gui/clock/80/68.png" at map_dissolve
                    elif quarters == 69:
                        idle "gui/clock/80/69.png" at map_dissolve
                    elif quarters == 70:
                        idle "gui/clock/80/70.png" at map_dissolve
                    elif quarters == 71:
                        idle "gui/clock/80/71.png" at map_dissolve
                    elif quarters == 72:
                        idle "gui/clock/80/72.png" at map_dissolve
                    elif quarters == 73:
                        idle "gui/clock/80/73.png" at map_dissolve
                    elif quarters == 74:
                        idle "gui/clock/80/74.png" at map_dissolve
                    elif quarters == 75:
                        idle "gui/clock/80/75.png" at map_dissolve
                    elif quarters == 76:
                        idle "gui/clock/80/76.png" at map_dissolve
                    elif quarters == 77:
                        idle "gui/clock/80/77.png" at map_dissolve
                    elif quarters == 78:
                        idle "gui/clock/80/78.png" at map_dissolve
                    elif quarters == 79:
                        idle "gui/clock/80/79.png" at map_dissolve
                    elif quarters == 80:
                        idle "gui/clock/80/80.png" at map_dissolve
                    else:
                        idle "gui/clock/midnight.png" at map_dissolve
                else:
                    if quarters == 22:
                        idle "gui/clock/80/22.png" at map_dissolve
                    elif quarters == 23:
                        idle "gui/clock/80/23.png" at map_dissolve
                    elif quarters == 24:
                        idle "gui/clock/80/24.png" at map_dissolve
                    elif quarters == 25:
                        idle "gui/clock/80/25.png" at map_dissolve
                    elif quarters == 26:
                        idle "gui/clock/80/26.png" at map_dissolve
                    elif quarters == 27:
                        idle "gui/clock/80/27.png" at map_dissolve
                    elif quarters == 28:
                        idle "gui/clock/80/28.png" at map_dissolve
                    elif quarters == 29:
                        idle "gui/clock/80/29.png" at map_dissolve
                    elif quarters == 30:
                        idle "gui/clock/80/30.png" at map_dissolve
                    elif quarters == 31:
                        idle "gui/clock/80/31.png" at map_dissolve
                    elif quarters == 32:
                        idle "gui/clock/80/32.png" at map_dissolve
                    elif quarters == 33:
                        idle "gui/clock/80/33.png" at map_dissolve
                    elif quarters == 34:
                        idle "gui/clock/80/34.png" at map_dissolve
                    elif quarters == 35:
                        idle "gui/clock/80/35.png" at map_dissolve
                    elif quarters == 36:
                        idle "gui/clock/80/36.png" at map_dissolve
                    elif quarters == 37:
                        idle "gui/clock/80/37.png" at map_dissolve
                    elif quarters == 38:
                        idle "gui/clock/80/38.png" at map_dissolve
                    elif quarters == 39:
                        idle "gui/clock/80/39.png" at map_dissolve
                    elif quarters == 40:
                        idle "gui/clock/80/40.png" at map_dissolve
                    elif quarters == 41:
                        idle "gui/clock/80/41.png" at map_dissolve
                    elif quarters == 42:
                        idle "gui/clock/80/42.png" at map_dissolve
                    elif quarters == 43:
                        idle "gui/clock/80/43.png" at map_dissolve
                    elif quarters == 44:
                        idle "gui/clock/80/44.png" at map_dissolve
                    elif quarters == 45:
                        idle "gui/clock/80/45.png" at map_dissolve
                    elif quarters == 46:
                        idle "gui/clock/80/46.png" at map_dissolve
                    elif quarters == 47:
                        idle "gui/clock/80/47.png" at map_dissolve
                    elif quarters == 48:
                        idle "gui/clock/80/48.png" at map_dissolve
                    elif quarters == 49:
                        idle "gui/clock/80/49.png" at map_dissolve
                    elif quarters == 50:
                        idle "gui/clock/80/50.png" at map_dissolve
                    elif quarters == 51:
                        idle "gui/clock/80/51.png" at map_dissolve
                    elif quarters == 52:
                        idle "gui/clock/80/52.png" at map_dissolve
                    elif quarters == 53:
                        idle "gui/clock/80/53.png" at map_dissolve
                    elif quarters == 54:
                        idle "gui/clock/80/54.png" at map_dissolve
                    elif quarters == 55:
                        idle "gui/clock/80/55.png" at map_dissolve
                    elif quarters == 56:
                        idle "gui/clock/80/56.png" at map_dissolve
                    elif quarters == 57:
                        idle "gui/clock/80/57.png" at map_dissolve
                    elif quarters == 58:
                        idle "gui/clock/80/58.png" at map_dissolve
                    elif quarters == 59:
                        idle "gui/clock/80/59.png" at map_dissolve
                    elif quarters == 60:
                        idle "gui/clock/80/60.png" at map_dissolve
                    elif quarters == 61:
                        idle "gui/clock/80/61.png" at map_dissolve
                    elif quarters == 62:
                        idle "gui/clock/80/62.png" at map_dissolve
                    elif quarters == 63:
                        idle "gui/clock/80/63.png" at map_dissolve
                    elif quarters == 64:
                        idle "gui/clock/80/64.png" at map_dissolve
                    elif quarters == 65:
                        idle "gui/clock/80/65.png" at map_dissolve
                    elif quarters == 66:
                        idle "gui/clock/80/66.png" at map_dissolve
                    elif quarters == 67:
                        idle "gui/clock/80/67.png" at map_dissolve
                    elif quarters == 68:
                        idle "gui/clock/80/68.png" at map_dissolve
                    elif quarters == 69:
                        idle "gui/clock/80/69.png" at map_dissolve
                    elif quarters == 70:
                        idle "gui/clock/80/70.png" at map_dissolve
                    elif quarters == 71:
                        idle "gui/clock/80/71.png" at map_dissolve
                    elif quarters == 72:
                        idle "gui/clock/80/72.png" at map_dissolve
                    elif quarters == 73:
                        idle "gui/clock/80/73.png" at map_dissolve
                    elif quarters == 74:
                        idle "gui/clock/80/74.png" at map_dissolve
                    elif quarters == 75:
                        idle "gui/clock/80/75.png" at map_dissolve
                    elif quarters == 76:
                        idle "gui/clock/80/76.png" at map_dissolve
                    elif quarters == 77:
                        idle "gui/clock/80/77.png" at map_dissolve
                    elif quarters == 78:
                        idle "gui/clock/80/78.png" at map_dissolve
                    elif quarters == 79:
                        idle "gui/clock/80/79.png" at map_dissolve
                    else:
                        idle "gui/clock/midnight.png" at map_dissolve
                hovered [SetVariable("charactertooltipypos", 0), tt.Action("clock")]
                action NullAction()
    if (hpscreen and persistent.tutorial_display) or not persistent.tutorial_display:
        imagebutton:
            focus_mask None
            action NullAction()
            if (not foodscreen and persistent.tutorial_display):
                xpos 1663
            else:
                xpos 1595
            ypos 466
            if not pc_hp:
                idle "gui/statuspoints/hp/0hp.png"
                hovered [SetVariable("charactertooltipypos", 1), tt.Action("{color=#f6d6bd}Vitality: 0/[displayedmaxhp]{/color}\nYou’re on the verge of death and\nit affects your appearance.")]
            if pc_hp == 1:
                idle "gui/statuspoints/hp/1hp.png"
                hovered [SetVariable("charactertooltipypos", 1), tt.Action("{color=#f6d6bd}Vitality: 1/[displayedmaxhp]{/color}\nYou’re barely standing.")]
            if pc_hp == 2:
                idle "gui/statuspoints/hp/2hp.png"
                hovered [SetVariable("charactertooltipypos", 1), tt.Action("{color=#f6d6bd}Vitality: 2/[displayedmaxhp]{/color}\nYou should take a break.")]
            if pc_hp == 3:
                idle "gui/statuspoints/hp/3hp.png"
                hovered [SetVariable("charactertooltipypos", 1), tt.Action("{color=#f6d6bd}Vitality: 3/[displayedmaxhp]{/color}\nYou feel well.")]
            if pc_hp == 4:
                idle "gui/statuspoints/hp/4hp.png"
                hovered [SetVariable("charactertooltipypos", 1), tt.Action("{color=#f6d6bd}Vitality: 4/[displayedmaxhp]{/color}\nYou’re in great shape and\nit affects your appearance.")]
            if pc_hp == 5:
                idle "gui/statuspoints/hp/5hp.png"
                hovered [SetVariable("charactertooltipypos", 1), tt.Action("{color=#f6d6bd}Vitality: 5/[displayedmaxhp]{/color}\nYou feel amazing and\nit affects your appearance.")]
    if (foodscreen and persistent.tutorial_display) or not persistent.tutorial_display:
        imagebutton:
            focus_mask None
            action NullAction()
            xpos 1731
            ypos 466
            if not pc_food:
                idle "gui/statuspoints/food/0food.png"
                hovered [SetVariable("charactertooltipypos", 1), tt.Action("{color=#f6d6bd}Nourishment: 0/4{/color}\nStarvation weakens you in the physical struggles.")]
            if pc_food == 1:
                idle "gui/statuspoints/food/1food.png"
                hovered [SetVariable("charactertooltipypos", 1), tt.Action("{color=#f6d6bd}Nourishment: 1/4{/color}\nYou won’t restore health while sleeping or resting.")]
            if pc_food == 2:
                idle "gui/statuspoints/food/2food.png"
                hovered [SetVariable("charactertooltipypos", 1), tt.Action("{color=#f6d6bd}Nourishment: 2/4{/color}\nYou experience no penalties and bonuses.")]
            if pc_food == 3:
                idle "gui/statuspoints/food/3food.png"
                hovered [SetVariable("charactertooltipypos", 1), tt.Action("{color=#f6d6bd}Nourishment: 3/4{/color}\nIt’s easier for you to overcome physical struggles.")]
            if pc_food == 4:
                idle "gui/statuspoints/food/4food.png"
                hovered [SetVariable("charactertooltipypos", 1), tt.Action("{color=#f6d6bd}Nourishment: 4/4{/color}\nIt’s much easier for you to overcome physical struggles.")]
    if (armorscreen and persistent.tutorial_display) or not persistent.tutorial_display:
        imagebutton:
            focus_mask None
            action NullAction()
            if (not foodscreen and persistent.tutorial_display):
                xpos 1663
            else:
                xpos 1595
            ypos 598
            if not armor:
                idle "gui/statuspoints/armor/0armor.png"
                hovered [SetVariable("charactertooltipypos", 2), tt.Action("{color=#f6d6bd}Armor: 0/4{/color}\nIn its current state, it offers you no protection.")]
            if armor == 1:
                idle "gui/statuspoints/armor/1armor.png"
                hovered [SetVariable("charactertooltipypos", 2), tt.Action("{color=#f6d6bd}Armor: 1/4{/color}\nIt’s too worn out to make a real difference in combat.")]
            if armor == 2:
                idle "gui/statuspoints/armor/2armor.png"
                hovered [SetVariable("charactertooltipypos", 2), tt.Action("{color=#f6d6bd}Armor: 2/4{/color}\nIt will stop the lighter attacks, but not for long.")]
            if armor == 3:
                if not armor_can4:
                    idle "gui/statuspoints/armor/3armormax.png"
                    hovered [SetVariable("charactertooltipypos", 2), tt.Action("{color=#f6d6bd}Armor: 3/4{/color}\nIt will stop even a life-threatening strike.\nWith your current gambeson, it’s the best protection you can get.")]
                else:
                    idle "gui/statuspoints/armor/3armor.png"
                    hovered [SetVariable("charactertooltipypos", 2), tt.Action("{color=#f6d6bd}Armor: 3/4{/color}\nIt will stop even a life-threatening strike.")]
            if armor == 4:
                idle "gui/statuspoints/armor/4armor.png"
                hovered [SetVariable("charactertooltipypos", 2), tt.Action("{color=#f6d6bd}Armor: 4/4{/color}\nIt suits you well and doesn’t encumber you in combat.")]
    if (appearancescreen and persistent.tutorial_display) or not persistent.tutorial_display:
        if not appearance:
            $ didisplayedappearance = "People stay away from you.{size=-32}\n {/size}"
        elif appearance == 1:
            $ didisplayedappearance = "People are hesitant to trust you.{size=-32}\n {/size}"
        elif appearance == 2:
            $ didisplayedappearance = "You don’t stand out from the crowd.{size=-32}\n {/size}"
        elif appearance == 3:
            $ didisplayedappearance = "People are more willing to trust you.{size=-32}\n {/size}"
        elif appearance == 4:
            $ didisplayedappearance = "People are more willing to trust you\nand will offer you better prices.{size=-32}\n {/size}"
        elif appearance == 5:
            $ didisplayedappearance = "You receive much better prices\nand open many doors.{size=-32}\n {/size}"
        else:
            $ didisplayedappearance = ""
        if not cleanliness:
            $ displayedcleanliness = "\nYou smell of sweat and dirt."
        elif cleanliness == 1:
            $ displayedcleanliness = "\nYour face is dirty."
        elif cleanliness == 2:
            $ displayedcleanliness = "\nYou won’t get much cleaner without a proper bath."
        elif cleanliness == 3:
            $ displayedcleanliness = "\nYou’re clean and tidy."
        else:
            $ displayedcleanliness = ""
        if cleanliness_clothes_torn and not item_fancyclothes:
            $ displayedcleanliness_clothes_torn = "\nYour clothes are torn and worn."
        else:
            $ displayedcleanliness_clothes_torn = ""
        if cleanliness_clothes_blood and not item_fancyclothes:
            $ displayedcleanliness_clothes_blood = "\nYour clothes are stained with blood."
        else:
            $ displayedcleanliness_clothes_blood = ""
        if item_fancyclothes and cleanliness_clothes_torn and cleanliness_clothes_blood:
            $ displayedfancyclothes = "\nYour fancy outfit covers the\ntorn and bloodied clothes."
        elif item_fancyclothes and cleanliness_clothes_torn:
            $ displayedfancyclothes = "\nYour fancy outfit covers\nthe torn clothes."
        elif item_fancyclothes and cleanliness_clothes_blood:
            $ displayedfancyclothes = "\nYour fancy outfit covers\nthe bloodied clothes."
        elif item_fancyclothes:
            $ displayedfancyclothes = "\nYou have a fancy outfit."
        else:
            $ displayedfancyclothes = ""
        if pc_hp >= 4:
            $ displayedappearancehp = "\nYou seem healthy."
        elif not pc_hp:
            $ displayedappearancehp = "\nYou seem exhausted."
        else:
            $ displayedappearancehp = ""
        imagebutton:
            focus_mask None
            action NullAction()
            xpos 1731
            ypos 598
            if not appearance:
                idle "gui/statuspoints/appearance/0appearance.png"
            if appearance == 1:
                idle "gui/statuspoints/appearance/1appearance.png"
            if appearance == 2:
                idle "gui/statuspoints/appearance/2appearance.png"
            if appearance == 3:
                idle "gui/statuspoints/appearance/3appearance.png"
            if appearance == 4:
                idle "gui/statuspoints/appearance/4appearance.png"
            if appearance == 5:
                idle "gui/statuspoints/appearance/5appearance.png"
            hovered [SetVariable("charactertooltipypos", 2), tt.Action("{color=#f6d6bd}Appearance: [appearance]/5{/color}\n[didisplayedappearance][displayedcleanliness][displayedappearancehp][displayedfancyclothes][displayedcleanliness_clothes_torn][displayedcleanliness_clothes_blood]")]
    if (pc_class and classabilityscreen and persistent.tutorial_display) or (pc_class and not persistent.tutorial_display):
        imagebutton:
            focus_mask None
            action NullAction()
            xpos 1663
            ypos 730
            if pc_class == "warrior":
                if not pc_hp:
                    idle "gui/statuspoints/axefalse.png"
                    hovered [SetVariable("charactertooltipypos", 3), tt.Action("{color=#f6d6bd}Force{/color}\nYou’re too exhausted to\nget any use from your training.")]
                else:
                    idle "gui/statuspoints/axetrue.png"
                    hovered [SetVariable("charactertooltipypos", 3), tt.Action("{color=#f6d6bd}Force{/color}\nAs an experienced warrior you gain\nan advantage during physical struggles.")]
            if pc_class == "scholar":
                idle "gui/statuspoints/scholartrue.png"
                hovered [SetVariable("charactertooltipypos", 3), tt.Action("{color=#f6d6bd}Knowledge{/color}\nThanks to your education,\nyou can read and\npractice alchemy.")]
            if pc_class == "mage":
                if mana <= 0:
                    idle "gui/statuspoints/mana/0mana.png"
                elif mana == 1:
                    idle "gui/statuspoints/mana/1mana.png"
                elif mana == 2:
                    idle "gui/statuspoints/mana/2mana.png"
                elif mana == 3:
                    idle "gui/statuspoints/mana/3mana.png"
                elif mana == 4:
                    idle "gui/statuspoints/mana/4mana.png"
                else:
                    idle "gui/statuspoints/mana/5mana.png"
                hovered [SetVariable("charactertooltipypos", 3), tt.Action("{color=#f6d6bd}Pneuma: [mana]/5{/color}\nYou can use your magical amulets\nto cast minor spells.")]
    if tt.value == "clock":
        if day >= world_deadline:
            frame:
                xalign 1.0
                yalign 0.5
                xpos 1526
                ypos 370
                xmaximum 640
                xpadding 16
                top_padding 16
                bottom_padding 8
                if persistent.textstyle == "basic":
                    text ("The last day of your journey.") font "philosopher.ttf" text_align 0.5 line_spacing 12
                if persistent.textstyle == "pixel":
                    text ("The last day of your journey.") font "munro.ttf" text_align 0.5 line_spacing 12
        else:
            frame:
                xalign 1.0
                yalign 0.5
                xpos 1526
                ypos 370
                xmaximum 640
                xpadding 16
                top_padding 16
                bottom_padding 8
                if quarters == world_daylength:
                    $ quarters_counter = "0 h 00 min"
                elif quarters == world_daylength-1:
                    $ quarters_counter = "0 h 15 min"
                elif quarters == world_daylength-2:
                    $ quarters_counter = "0 h 30 min"
                elif quarters == world_daylength-3:
                    $ quarters_counter = "0 h 45 min"
                elif quarters == world_daylength-4:
                    $ quarters_counter = "1 h 00 min"
                elif quarters == world_daylength-5:
                    $ quarters_counter = "1 h 15 min"
                elif quarters == world_daylength-6:
                    $ quarters_counter = "1 h 30 min"
                elif quarters == world_daylength-7:
                    $ quarters_counter = "1 h 45 min"
                elif quarters == world_daylength-8:
                    $ quarters_counter = "2 h 00 min"
                elif quarters == world_daylength-9:
                    $ quarters_counter = "2 h 15 min"
                elif quarters == world_daylength-10:
                    $ quarters_counter = "2 h 30 min"
                elif quarters == world_daylength-11:
                    $ quarters_counter = "2 h 45 min"
                elif quarters == world_daylength-12:
                    $ quarters_counter = "3 h 00 min"
                elif quarters == world_daylength-13:
                    $ quarters_counter = "3 h 15 min"
                elif quarters == world_daylength-14:
                    $ quarters_counter = "3 h 30 min"
                elif quarters == world_daylength-15:
                    $ quarters_counter = "3 h 45 min"
                elif quarters == world_daylength-16:
                    $ quarters_counter = "4 h 00 min"
                elif quarters == world_daylength-17:
                    $ quarters_counter = "4 h 15 min"
                elif quarters == world_daylength-18:
                    $ quarters_counter = "4 h 30 min"
                elif quarters == world_daylength-19:
                    $ quarters_counter = "4 h 45 min"
                elif quarters == world_daylength-20:
                    $ quarters_counter = "5 h 00 min"
                elif quarters == world_daylength-21:
                    $ quarters_counter = "5 h 15 min"
                elif quarters == world_daylength-22:
                    $ quarters_counter = "5 h 30 min"
                elif quarters == world_daylength-23:
                    $ quarters_counter = "5 h 45 min"
                elif quarters == world_daylength-24:
                    $ quarters_counter = "6 h 00 min"
                elif quarters == world_daylength-25:
                    $ quarters_counter = "6 h 15 min"
                elif quarters == world_daylength-26:
                    $ quarters_counter = "6 h 30 min"
                elif quarters == world_daylength-27:
                    $ quarters_counter = "6 h 45 min"
                elif quarters == world_daylength-28:
                    $ quarters_counter = "7 h 00 min"
                elif quarters == world_daylength-29:
                    $ quarters_counter = "7 h 15 min"
                elif quarters == world_daylength-30:
                    $ quarters_counter = "7 h 30 min"
                elif quarters == world_daylength-31:
                    $ quarters_counter = "7 h 45 min"
                elif quarters == world_daylength-32:
                    $ quarters_counter = "8 h 00 min"
                elif quarters == world_daylength-33:
                    $ quarters_counter = "8 h 15 min"
                elif quarters == world_daylength-34:
                    $ quarters_counter = "8 h 30 min"
                elif quarters == world_daylength-35:
                    $ quarters_counter = "8 h 45 min"
                elif quarters == world_daylength-36:
                    $ quarters_counter = "9 h 00 min"
                elif quarters == world_daylength-37:
                    $ quarters_counter = "9 h 15 min"
                elif quarters == world_daylength-38:
                    $ quarters_counter = "9 h 30 min"
                elif quarters == world_daylength-39:
                    $ quarters_counter = "9 h 45 min"
                elif quarters == world_daylength-40:
                    $ quarters_counter = "10 h 00 min"
                elif quarters == world_daylength-41:
                    $ quarters_counter = "10 h 15 min"
                elif quarters == world_daylength-42:
                    $ quarters_counter = "10 h 30 min"
                elif quarters == world_daylength-43:
                    $ quarters_counter = "10 h 45 min"
                elif quarters == world_daylength-44:
                    $ quarters_counter = "11 h 00 min"
                elif quarters == world_daylength-45:
                    $ quarters_counter = "11 h 15 min"
                elif quarters == world_daylength-46:
                    $ quarters_counter = "11 h 30 min"
                elif quarters == world_daylength-47:
                    $ quarters_counter = "11 h 45 min"
                elif quarters == world_daylength-48:
                    $ quarters_counter = "12 h 00 min"
                elif quarters == world_daylength-49:
                    $ quarters_counter = "12 h 15 min"
                elif quarters == world_daylength-50:
                    $ quarters_counter = "12 h 30 min"
                elif quarters == world_daylength-51:
                    $ quarters_counter = "12 h 45 min"
                elif quarters == world_daylength-52:
                    $ quarters_counter = "13 h 00 min"
                elif quarters == world_daylength-53:
                    $ quarters_counter = "13 h 15 min"
                elif quarters == world_daylength-54:
                    $ quarters_counter = "13 h 30 min"
                elif quarters == world_daylength-55:
                    $ quarters_counter = "13 h 45 min"
                elif quarters == world_daylength-56:
                    $ quarters_counter = "14 h 00 min"
                elif quarters == world_daylength-57:
                    $ quarters_counter = "14 h 15 min"
                elif quarters == world_daylength-58:
                    $ quarters_counter = "14 h 30 min"
                elif quarters == world_daylength-59:
                    $ quarters_counter = "14 h 45 min"
                elif quarters == world_daylength-60:
                    $ quarters_counter = "15 h 00 min"
                elif quarters == world_daylength-61:
                    $ quarters_counter = "15 h 15 min"
                elif quarters == world_daylength-62:
                    $ quarters_counter = "15 h 30 min"
                elif quarters == world_daylength-63:
                    $ quarters_counter = "15 h 45 min"
                elif quarters == world_daylength-64:
                    $ quarters_counter = "16 h 00 min"
                elif quarters == world_daylength-65:
                    $ quarters_counter = "16 h 15 min"
                elif quarters == world_daylength-66:
                    $ quarters_counter = "16 h 30 min"
                elif quarters == world_daylength-67:
                    $ quarters_counter = "16 h 45 min"
                elif quarters == world_daylength-68:
                    $ quarters_counter = "17 h 00 min"
                elif quarters == world_daylength-69:
                    $ quarters_counter = "17 h 15 min"
                elif quarters == world_daylength-70:
                    $ quarters_counter = "17 h 30 min"
                elif quarters == world_daylength-71:
                    $ quarters_counter = "17 h 45 min"
                elif quarters == world_daylength-72:
                    $ quarters_counter = "18 h 00 min"
                elif quarters == world_daylength-73:
                    $ quarters_counter = "18 h 15 min"
                elif quarters == world_daylength-74:
                    $ quarters_counter = "18 h 30 min"
                elif quarters == world_daylength-75:
                    $ quarters_counter = "18 h 45 min"
                elif quarters == world_daylength-76:
                    $ quarters_counter = "19 h 00 min"
                elif quarters == world_daylength-77:
                    $ quarters_counter = "19 h 15 min"
                elif quarters == world_daylength-78:
                    $ quarters_counter = "19 h 30 min"
                elif quarters == world_daylength-79:
                    $ quarters_counter = "19 h 45 min"
                elif quarters == world_daylength-80:
                    $ quarters_counter = "20 h 00 min"
                elif quarters == world_daylength-81:
                    $ quarters_counter = "20 h 15 min"
                elif quarters == world_daylength-82:
                    $ quarters_counter = "20 h 30 min"
                elif quarters == world_daylength-83:
                    $ quarters_counter = "20 h 45 min"
                elif quarters == world_daylength-84:
                    $ quarters_counter = "21 h 00 min"
                if game_mode != 1: # Placeholder
                    if day >= 1:
                        $ day_counter = (world_deadline-day)
                    else:
                        $ day_counter = 0
                    if day_counter == 1:
                        $ day_counter_plural = "day"
                    else:
                        $ day_counter_plural = "days"
                    if quarters <= world_daylength:
                        if day <= 0:
                            if persistent.textstyle == "basic":
                                text ("[quarters_counter] before dusk") font "philosopher.ttf" text_align 0.5 line_spacing 12
                            if persistent.textstyle == "pixel":
                                text ("[quarters_counter] before dusk") font "munro.ttf" text_align 0.5 line_spacing 12
                        else:
                            if persistent.textstyle == "basic":
                                text ("[quarters_counter] before dusk\nDay [day]\n%d %s before autumn" % (day_counter, day_counter_plural)) font "philosopher.ttf" text_align 0.5 line_spacing 12
                            if persistent.textstyle == "pixel":
                                text ("[quarters_counter] before dusk\nDay [day]\n%d %s before autumn" % (day_counter, day_counter_plural)) font "munro.ttf" text_align 0.5 line_spacing 12
                    else:
                        if day <= 0:
                            if persistent.textstyle == "basic":
                                text "{color=#6a6a6a}Nighttime{/color}" font "philosopher.ttf" text_align 0.5 line_spacing 12
                            if persistent.textstyle == "pixel":
                                text "{color=#6a6a6a}Nighttime{/color}" font "munro.ttf" text_align 0.5 line_spacing 12
                        else:
                            if persistent.textstyle == "basic":
                                text ("{color=#6a6a6a}Nighttime{/color}\nDay [day]\n%d %s before autumn" % (day_counter, day_counter_plural)) font "philosopher.ttf" text_align 0.5 line_spacing 12
                            if persistent.textstyle == "pixel":
                                text ("{color=#6a6a6a}Nighttime{/color}\nDay [day]\n%d %s before autumn" % (day_counter, day_counter_plural)) font "munro.ttf" text_align 0.5 line_spacing 12
                else:
                    if quarters <= world_daylength:
                        if day <= 0:
                            if persistent.textstyle == "basic":
                                text ("[quarters_counter] before dusk") font "philosopher.ttf" text_align 0.5 line_spacing 12
                            if persistent.textstyle == "pixel":
                                text ("[quarters_counter] before dusk") font "munro.ttf" text_align 0.5 line_spacing 12
                        else:
                            if persistent.textstyle == "basic":
                                text ("[quarters_counter] before dusk\nDay [day]") font "philosopher.ttf" text_align 0.5 line_spacing 12
                            if persistent.textstyle == "pixel":
                                text ("[quarters_counter] before dusk\nDay [day]") font "munro.ttf" text_align 0.5 line_spacing 12
                    else:
                        if day <= 0:
                            if persistent.textstyle == "basic":
                                text "{color=#6a6a6a}Nighttime{/color}" font "philosopher.ttf" text_align 0.5 line_spacing 12
                            if persistent.textstyle == "pixel":
                                text "{color=#6a6a6a}Nighttime{/color}" font "munro.ttf" text_align 0.5 line_spacing 12
                        else:
                            if persistent.textstyle == "basic":
                                text ("{color=#6a6a6a}Nighttime{/color}\nDay [day]") font "philosopher.ttf" text_align 0.5 line_spacing 12
                            if persistent.textstyle == "pixel":
                                text ("{color=#6a6a6a}Nighttime{/color}\nDay [day]") font "munro.ttf" text_align 0.5 line_spacing 12
    elif tt.value != "":
        frame:
            xalign 1.0
            yalign 0.5
            xpos 1526
            if charactertooltipypos == 1:
                ypos 502
            elif charactertooltipypos == 2:
                ypos 634
            elif charactertooltipypos == 3:
                ypos 766
            xmaximum 640
            xpadding 16
            top_padding 16
            bottom_padding 8
            if persistent.textstyle == "basic":
                text tt.value font "philosopher.ttf" text_align 0.5 line_spacing 12
            if persistent.textstyle == "pixel":
                text tt.value font "munro.ttf" text_align 0.5 line_spacing 12

################################## DOUBLE IMAGE
screen doubleimage():
    zorder 120
    if pc_area == "eudociahouse" and not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview") and not eudocia_invitation_attempt_inprogress and not sleep_inprogress:
        imagebutton:
            focus_mask True
            xpos 47
            ypos 48
            hovered [SetVariable("interface_doubleimage", 1), SetVariable("tutorial_twopictures", 1)]
            unhovered SetVariable("interface_doubleimage", 0)
            idle "images/cancel2.png"
            hover "images/cancel2hover.png"
            action NullAction()
screen doubleimage2():
    zorder 110
    imagemap:
        ground "achievements/empty.png" at truecenter
        if interface_doubleimage:
            if eudocia_image_left == "base":
                add "images/areapictures/eudociahouse/eudociahouseleft01.png" xpos 49 ypos 50
            if eudocia_image_left == "dark":
                add "images/areapictures/eudociahouse/eudociahouseleft00.png" xpos 49 ypos 50
            if eudocia_image_golem02 == "nogolem":
                add "images/areapictures/eudociahouse/eudocianosittinggolem.png" xpos 49 ypos 50
            if eudocia_image_golem02 == "nogolemplusback":
                add "images/areapictures/eudociahouse/eudocianosittinggolembutback.png" xpos 49 ypos 50
            if eudocia_image_right == "base":
                add "images/areapictures/eudociahouse/eudociahouseright01.png" xpos 689 ypos 50
            if eudocia_image_right == "dark":
                add "images/areapictures/eudociahouse/eudociahouseright00.png" xpos 689 ypos 50
            if eudocia_image_right == "gate":
                add "images/areapictures/eudociahouse/eudociahouserightgate.png" xpos 689 ypos 50
            if eudocia_image_golem01 == "gate":
                add "images/areapictures/eudociahouse/eudociagolemgate.png" xpos 689 ypos 50
            if eudocia_image_eyes == 1:
                add "images/areapictures/eudociahouse/eudociaeyes.png" xpos 689 ypos 50
            if eudocia_image_golem01 == "turnedright":
                add "images/areapictures/eudociahouse/eudociagolemturnedright.png" xpos 689 ypos 50
            if eudocia_image_golem01 == "turnedleft":
                add "images/areapictures/eudociahouse/eudociagolemturnedleft.png" xpos 689 ypos 50
            if eudocia_image_golem01 == "turnedback":
                add "images/areapictures/eudociahouse/eudociagolemturnedback.png" xpos 689 ypos 50
            add "images/areapictures/eudociahouse/eudociaoverlay.png" xpos 0 ypos 0
screen oldtunnel():
    zorder 8
    if not renpy.get_screen("map_display") and not renpy.get_screen("map_onlyview"):
        imagemap:
            ground "images/areapictures/oldtunnel/oldtunnelscrapbackground.png" xpos 49 ypos 50
            if oldtunnel_exploration_scrap00_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap00.png"
            if oldtunnel_exploration_scrap01_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap01.png"
            if oldtunnel_exploration_scrap02_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap02.png"
            if oldtunnel_exploration_scrap03_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap03.png"
            if oldtunnel_exploration_scrap04_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap04.png"
            if oldtunnel_exploration_scrap05_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap05.png"
            if oldtunnel_exploration_scrap06_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap06.png"
            if oldtunnel_exploration_scrap07_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap07.png"
            if oldtunnel_exploration_scrap08_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap08.png"
            if oldtunnel_exploration_scrap09_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap09.png"
            if oldtunnel_exploration_scrap10_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap10.png"
            if oldtunnel_exploration_scrap11_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap11.png"
            if oldtunnel_exploration_scrap12_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap12.png"
            if oldtunnel_exploration_scrap13_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap13.png"
            if oldtunnel_exploration_scrap14_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap14.png"
            if oldtunnel_exploration_scrap15_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap15.png"
            if oldtunnel_exploration_scrap16_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap16.png"
            if oldtunnel_exploration_scrap17_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap17.png"
            if oldtunnel_exploration_scrap18_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap18.png"
            if oldtunnel_exploration_scrap19_firsttime and oldtunnel_inside_opened:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap19a.png"
            if oldtunnel_exploration_scrap19_firsttime:
                add "images/areapictures/oldtunnel/dark/oldtunnelscrap19.png"
            if oldtunnel_exploration_position == 0:
                add "oldtunnelscrap00"
            if oldtunnel_exploration_position == 1:
                add "oldtunnelscrap01"
            if oldtunnel_exploration_position == 2:
                add "oldtunnelscrap02"
            if oldtunnel_exploration_position == 3:
                add "oldtunnelscrap03"
            if oldtunnel_exploration_position == 4:
                add "oldtunnelscrap04"
            if oldtunnel_exploration_position == 5:
                add "oldtunnelscrap05"
            if oldtunnel_exploration_scrap07_firsttime and oldtunnel_exploration_position == 6:
                add "oldtunnelscrap06"
                add "oldtunnelscrap07"
            elif oldtunnel_exploration_position == 6:
                add "oldtunnelscrap06"
            if oldtunnel_exploration_position == 8:
                add "oldtunnelscrap08"
            if oldtunnel_exploration_position == 9:
                add "oldtunnelscrap09"
            if oldtunnel_exploration_position == 10:
                add "oldtunnelscrap10"
            if oldtunnel_exploration_position == 11:
                add "oldtunnelscrap11"
            if oldtunnel_exploration_position == 12:
                add "oldtunnelscrap12"
            if oldtunnel_exploration_position == 13:
                add "oldtunnelscrap13"
            if oldtunnel_exploration_position == 14:
                add "oldtunnelscrap14"
            if oldtunnel_exploration_position == 15:
                add "oldtunnelscrap15"
            if oldtunnel_exploration_position == 16:
                add "oldtunnelscrap16"
            if oldtunnel_exploration_position == 17:
                add "oldtunnelscrap17"
            if oldtunnel_exploration_position == 18:
                add "oldtunnelscrap18"
            if oldtunnel_exploration_position == 19 and oldtunnel_inside_opened:
                add "oldtunnelscrap19a"
            elif oldtunnel_exploration_position == 19:
                add "oldtunnelscrap19"

            # if oldtunnel_exploration_scrap00_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap00.png"
            # if oldtunnel_exploration_scrap01_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap01.png"
            # if oldtunnel_exploration_scrap02_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap02.png"
            # if oldtunnel_exploration_scrap03_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap03.png"
            # if oldtunnel_exploration_scrap04_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap04.png"
            # if oldtunnel_exploration_scrap05_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap05.png"
            # if oldtunnel_exploration_scrap06_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap06.png"
            # if oldtunnel_exploration_scrap07_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap07.png"
            # if oldtunnel_exploration_scrap08_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap08.png"
            # if oldtunnel_exploration_scrap09_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap09.png"
            # if oldtunnel_exploration_scrap10_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap10.png"
            # if oldtunnel_exploration_scrap11_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap11.png"
            # if oldtunnel_exploration_scrap12_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap12.png"
            # if oldtunnel_exploration_scrap13_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap13.png"
            # if oldtunnel_exploration_scrap14_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap14.png"
            # if oldtunnel_exploration_scrap15_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap15.png"
            # if oldtunnel_exploration_scrap16_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap16.png"
            # if oldtunnel_exploration_scrap17_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap17.png"
            # if oldtunnel_exploration_scrap18_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap18.png"
            # if oldtunnel_exploration_scrap19_firsttime and oldtunnel_inside_opened:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap19a.png"
            # if oldtunnel_exploration_scrap19_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap19.png"
            # if oldtunnel_exploration_position == 0:
            #     add "oldtunnelscrap00"
            # if oldtunnel_exploration_position == 1:
            #     add "oldtunnelscrap01"
            # if oldtunnel_exploration_position == 2:
            #     add "oldtunnelscrap02"
            # if oldtunnel_exploration_position == 3:
            #     add "oldtunnelscrap03"
            # if oldtunnel_exploration_position == 4:
            #     add "oldtunnelscrap04"
            # if oldtunnel_exploration_position == 5:
            #     add "oldtunnelscrap05"
            # if oldtunnel_exploration_scrap07_firsttime and oldtunnel_exploration_position == 6:
            #     add "oldtunnelscrap06"
            #     add "oldtunnelscrap07"
            # elif oldtunnel_exploration_position == 6:
            #     add "oldtunnelscrap06"
            # if oldtunnel_exploration_position == 8:
            #     add "oldtunnelscrap08"
            # if oldtunnel_exploration_position == 9:
            #     add "oldtunnelscrap09"
            # if oldtunnel_exploration_position == 10:
            #     add "oldtunnelscrap10"
            # if oldtunnel_exploration_position == 11:
            #     add "oldtunnelscrap11"
            # if oldtunnel_exploration_position == 12:
            #     add "oldtunnelscrap12"
            # if oldtunnel_exploration_position == 13:
            #     add "oldtunnelscrap13"
            # if oldtunnel_exploration_position == 14:
            #     add "oldtunnelscrap14"
            # if oldtunnel_exploration_position == 15:
            #     add "oldtunnelscrap15"
            # if oldtunnel_exploration_position == 16:
            #     add "oldtunnelscrap16"
            # if oldtunnel_exploration_position == 17:
            #     add "oldtunnelscrap17"
            # if oldtunnel_exploration_position == 18:
            #     add "oldtunnelscrap18"
            # if oldtunnel_exploration_position == 19 and oldtunnel_inside_opened:
            #     add "oldtunnelscrap19a"
            # elif oldtunnel_exploration_position == 19:
            #     add "oldtunnelscrap19"

            # ground "images/areapictures/oldtunnel/oldtunnelscrapbackground.png" xpos 49 ypos 50
            # if oldtunnel_exploration_scrap00_firsttime and oldtunnel_exploration_position == 0:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap00.png"
            # elif oldtunnel_exploration_scrap00_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap00.png"
            # if oldtunnel_exploration_scrap01_firsttime and oldtunnel_exploration_position == 1:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap01.png"
            # elif oldtunnel_exploration_scrap01_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap01.png"
            # if oldtunnel_exploration_scrap02_firsttime and oldtunnel_exploration_position == 2:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap02.png"
            # elif oldtunnel_exploration_scrap02_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap02.png"
            # if oldtunnel_exploration_scrap03_firsttime and oldtunnel_exploration_position == 3:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap03.png"
            # elif oldtunnel_exploration_scrap03_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap03.png"
            # if oldtunnel_exploration_scrap04_firsttime and oldtunnel_exploration_position == 4:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap04.png"
            # elif oldtunnel_exploration_scrap04_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap04.png"
            # if oldtunnel_exploration_scrap05_firsttime and oldtunnel_exploration_position == 5:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap05.png"
            # elif oldtunnel_exploration_scrap05_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap05.png"
            # if oldtunnel_exploration_scrap06_firsttime and oldtunnel_exploration_scrap07_firsttime and oldtunnel_exploration_position == 6:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap06.png"
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap07.png"
            # elif oldtunnel_exploration_scrap06_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap06.png"
            #     if oldtunnel_exploration_scrap07_firsttime:
            #         add "images/areapictures/oldtunnel/dark/oldtunnelscrap07.png"
            # if oldtunnel_exploration_scrap08_firsttime and oldtunnel_exploration_position == 8:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap08.png"
            # elif oldtunnel_exploration_scrap08_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap08.png"
            # if oldtunnel_exploration_scrap09_firsttime and oldtunnel_exploration_position == 9:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap09.png"
            # elif oldtunnel_exploration_scrap09_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap09.png"
            # if oldtunnel_exploration_scrap10_firsttime and oldtunnel_exploration_position == 10:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap10.png"
            # elif oldtunnel_exploration_scrap10_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap10.png"
            # if oldtunnel_exploration_scrap11_firsttime and oldtunnel_exploration_position == 11:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap11.png"
            # elif oldtunnel_exploration_scrap11_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap11.png"
            # if oldtunnel_exploration_scrap12_firsttime and oldtunnel_exploration_position == 12:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap12.png"
            # elif oldtunnel_exploration_scrap12_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap12.png"
            # if oldtunnel_exploration_scrap13_firsttime and oldtunnel_exploration_position == 13:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap13.png"
            # elif oldtunnel_exploration_scrap13_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap13.png"
            # if oldtunnel_exploration_scrap14_firsttime and oldtunnel_exploration_position == 14:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap14.png"
            # elif oldtunnel_exploration_scrap14_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap14.png"
            # if oldtunnel_exploration_scrap15_firsttime and oldtunnel_exploration_position == 15:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap15.png"
            # elif oldtunnel_exploration_scrap15_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap15.png"
            # if oldtunnel_exploration_scrap16_firsttime and oldtunnel_exploration_position == 16:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap16.png"
            # elif oldtunnel_exploration_scrap16_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap16.png"
            # if oldtunnel_exploration_scrap17_firsttime and oldtunnel_exploration_position == 17:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap17.png"
            # elif oldtunnel_exploration_scrap17_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap17.png"
            # if oldtunnel_exploration_scrap18_firsttime and oldtunnel_exploration_position == 18:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap18.png"
            # elif oldtunnel_exploration_scrap18_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap18.png"
            # if oldtunnel_exploration_scrap19_firsttime and oldtunnel_exploration_position == 19 and oldtunnel_inside_opened:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap19a.png"
            # elif oldtunnel_exploration_scrap19_firsttime and oldtunnel_inside_opened:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap19a.png"
            # elif oldtunnel_exploration_scrap19_firsttime and oldtunnel_exploration_position == 19:
            #     add "images/areapictures/oldtunnel/base/oldtunnelscrap19.png"
            # elif oldtunnel_exploration_scrap19_firsttime:
            #     add "images/areapictures/oldtunnel/dark/oldtunnelscrap19.png"

##### WAITING
screen waitscreen():
    zorder 200
    modal True
    style_prefix "wait"
    add "gui/overlay/confirm.png"
    key "w" action [Hide('waitscreen'), With(dissolve)]
    key "W" action [Hide('waitscreen'), With(dissolve)]
    key "game_menu" action [Hide('waitscreen'), With(dissolve)]
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
                action Hide("waitscreen", transition=dissolve)
        frame:
            vbox:
                xalign .5
                yalign .5
                spacing 40
                label _("Wait for..."):
                    style "wait_prompt"
                hbox:
                    ypos -10
                    if quarters < world_daylength:
                        textbutton _("0:15") action [SetVariable("quarters", quarters+1), Hide("waitscreen", transition=dissolve)]:
                            xminimum 140 text_align 0.5 xalign 0.5
                    else:
                        textbutton _("{color=#6a6a6a}0:15{/color}"):
                            xminimum 140 text_align 0.5 xalign 0.5 action NullAction()
                    if quarters < world_daylength-1:
                        textbutton _("0:30") action [SetVariable("quarters", quarters+2), Hide("waitscreen", transition=dissolve)]:
                            xminimum 140 text_align 0.5 xalign 0.5
                    else:
                        textbutton _("{color=#6a6a6a}0:30{/color}"):
                            xminimum 140 text_align 0.5 xalign 0.5 action NullAction()
                    if quarters < world_daylength-2:
                        textbutton _("0:45") action [SetVariable("quarters", quarters+3), Hide("waitscreen", transition=dissolve)]:
                            xminimum 140 text_align 0.5 xalign 0.5
                    else:
                        textbutton _("{color=#6a6a6a}0:45{/color}"):
                            xminimum 140 text_align 0.5 xalign 0.5 action NullAction()
                    if quarters < world_daylength-3:
                        textbutton _("1:00") action [SetVariable("quarters", quarters+4), Hide("waitscreen", transition=dissolve)]:
                            xminimum 140 text_align 0.5 xalign 0.5
                    else:
                        textbutton _("{color=#6a6a6a}1:00{/color}"):
                            xminimum 140 text_align 0.5 xalign 0.5 action NullAction()
                label _("Wait until..."):
                    style "wait_prompt"
                hbox:
                    ypos -10
                    if quarters < 36:
                        textbutton _("Morning") action [SetVariable("quarters", 36), Hide("waitscreen", transition=dissolve)]:
                            xminimum 140 text_align 0.5 xalign 0.5
                    else:
                        textbutton _("{color=#6a6a6a}Morning{/color}"):
                            xminimum 140 text_align 0.5 xalign 0.5 action NullAction()
                    if quarters < ((world_daylength/2)+11):
                        textbutton _("Noon") action [SetVariable("quarters", ((world_daylength/2)+11)), Hide("waitscreen", transition=dissolve)]:
                            xminimum 140 text_align 0.5 xalign 0.5
                    else:
                        textbutton _("{color=#6a6a6a}Noon{/color}"):
                            xminimum 140 text_align 0.5 xalign 0.5 action NullAction()
                    if quarters < ((world_daylength/2)+11+10):
                        textbutton _("Afternoon") action [SetVariable("quarters", ((world_daylength/2)+11+10)), Hide("waitscreen", transition=dissolve)]:
                            xminimum 140 text_align 0.5 xalign 0.5
                    else:
                        textbutton _("{color=#6a6a6a}Afternoon{/color}"):
                            xminimum 140 text_align 0.5 xalign 0.5 action NullAction()
                    if quarters < (world_daylength-12):
                        textbutton _("Evening") action [SetVariable("quarters", (world_daylength-12)), Hide("waitscreen", transition=dissolve)]:
                            xminimum 140 text_align 0.5 xalign 0.5
                    else:
                        textbutton _("{color=#6a6a6a}Evening{/color}"):
                            xminimum 140 text_align 0.5 xalign 0.5 action NullAction()
                # hbox:
                #     ypos -10
                #     xalign 0.5
                #     textbutton _("Return") action Hide("waitscreen", transition=dissolve)

##### POP UP
default world_popupnarration_name = 0
default world_popupnarration_highisland0 = 0 # learn, which island
# if world_popupnarration_highisland0 and not description_highisland00
# $ description_highisland00 = "The largest island in the North. Unreachable without a boat."
# $ description_highisland01 = "The island’s surface is high above the water, and it’s covered with a lush forest. In its center stands a large volcano."
default world_popupnarration_highisland1 = 0 # learn, how to reach high island
default world_popupnarration_highisland2 = 0 # learned before, just needs to gather the crew
default world_popupnarration_crewcounter = 0
default world_popupnarration_crewcounter_picked = 0
default world_popupnarration_crewcounter_max = 4
screen world_popupnarration_box():
    zorder 200
    modal True
    style_prefix "shop"
    add "gui/overlay/confirm.png"
    if world_popupnarration_name == "learnabouthighisland": # learn about high island
        frame:
            vbox:
                xalign .5
                spacing 28
                xmaximum 660
                xminimum 660
                label _("The Mysterious Destination"):
                    style "shop_prompt"
                    xalign 0.5
                text "According to the rumours, {color=#f6d6bd}Asterion{/color} has traveled to some unknown island." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                hbox:
                    xalign 0.5
                    if foggy_about_rumors_available:
                        textbutton _("Maybe Foggy knows\nmore about it") action [SetVariable("world_popupnarration_name", 0), SetVariable("world_popupnarration_highisland0", 1), Hide("world_popupnarration_box", transition=dissolve)] text_align 0.5 xalign .5
                    else:
                        textbutton _("I’ll ask someone who\nknows a lot about these lands") action [SetVariable("world_popupnarration_name", 0), SetVariable("world_popupnarration_highisland0", 1), Hide("world_popupnarration_box", transition=dissolve)] text_align 0.5 xalign .5
    elif world_popupnarration_name == "highisland": # learn, how to reach high island
        frame:
            vbox:
                xalign .5
                spacing 28
                xmaximum 660
                xminimum 660
                label _("The Forbidden Island"):
                    style "shop_prompt"
                    xalign 0.5
                text "You’ve found enough clues to believe that {color=#f6d6bd}Asterion{/color} has traveled to {color=#f6d6bd}High Island{/color}, northwest of the peninsula, and hasn’t been seen ever since.\n\nSo far, you know almost nothing about this place." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                hbox:
                    xalign 0.5
                    textbutton _("I need to ask\nthe locals about it") action [SetVariable("world_popupnarration_name", 0), SetVariable("asterion_highisland_knowsabout", 1), SetVariable("world_popupnarration_highisland1", 1), Notify("Journal updated: Find the Roadwarden"), Hide("world_popupnarration_box", transition=dissolve)] text_align 0.5 xalign .5
    elif world_popupnarration_name == "gatherthecrew": # learned just now, now needs to gather the crew
        frame:
            vbox:
                xalign .5
                spacing 28
                xmaximum 660
                xminimum 660
                label _("Gathering A Crew"):
                    style "shop_prompt"
                    xalign 0.5
                text "According to what you’ve learned, you can only reach {color=#fff1e5}High Island{/color} by a boat, leaving the coast during the day and landing at nighttime, during high tide.\n\nA chance that you’re going to find him there on your own is {i}slim{/i}." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                hbox:
                    xalign 0.5
                    textbutton _("So I need a boat...\nAnd maybe a few friends or mercenaries") action [SetVariable("world_popupnarration_name", 0), SetVariable("asterion_highisland_knowsabout", 1), SetVariable("world_popupnarration_highisland1", 1), SetVariable("world_popupnarration_highisland2", 1), SetVariable("quest_gatheracrew", 1), Notify("New entry: Gather a Crew"), Hide("world_popupnarration_box", transition=dissolve)] text_align 0.5 xalign .5
    elif world_popupnarration_name == "gatherthecrewskippedstep": # learned before, just needs to gather the crew
        frame:
            vbox:
                xalign .5
                spacing 28
                xmaximum 660
                xminimum 660
                label _("Reaching {color=#fff1e5}High Island{/color}"):
                    style "shop_prompt"
                    xalign 0.5
                text "You’ve found enough clues to believe that {color=#f6d6bd}Asterion{/color} has traveled to {color=#f6d6bd}High Island{/color}, northwest of the peninsula, and hasn’t been seen ever since.\n\nYou can only reach the island by a boat, leaving the coast during the day, and landing at nighttime, during high tide.\n\nA chance that you’re going to find him there on your own is {i}slim{/i}." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                hbox:
                    xalign 0.5
                    textbutton _("So I need a boat...\nAnd maybe a few friends or mercenaries") action [SetVariable("world_popupnarration_name", 0), SetVariable("asterion_highisland_knowsabout", 1), SetVariable("world_popupnarration_highisland1", 1), SetVariable("world_popupnarration_highisland2", 1), SetVariable("quest_gatheracrew", 1), Notify("New entry: Gather a Crew"), Hide("world_popupnarration_box", transition=dissolve)] text_align 0.5 xalign .5
    elif world_popupnarration_name == "highislandprep":
        on "show" action FileSave("highisland", confirm=False, newest=True, page=None, cycle=False, slot=True)
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
                    action Hide("world_popupnarration_box", transition=dissolve)
            $ world_popupnarration_crewcounter = 0
            if aegidia_favor or aegidia_about_highisland_recruitment_done:
                $ world_popupnarration_crewcounter += 1
            if dalit_about_highisland_recruitment_done:
                $ world_popupnarration_crewcounter += 1
            if galerocks_navica_about_highisland_recruitment_done:
                $ world_popupnarration_crewcounter += 1
            if thyrsus_orentius_debt_achieved:
                $ world_popupnarration_crewcounter += 1
            if pyrrhos_debt == 1 and not pyrrhos_dead:
                $ world_popupnarration_crewcounter += 1
            if shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_fled:
                $ world_popupnarration_crewcounter += 1
            if tulia_about_highisland_recruited and not asterion_lie:
                $ world_popupnarration_crewcounter += 1
            if foragers_about_gatherthecrew_tzvi_recruited:
                $ world_popupnarration_crewcounter += 1
            if quintus_alive == 1 and quintus_left_gate and quintus_left_gate < day:
                $ world_popupnarration_crewcounter += 1
            if quest_missinghunters_description02:
                $ world_popupnarration_crewcounter += 1
            frame:
                vbox:
                    xalign .5
                    spacing 28
                    xmaximum 660
                    xminimum 660
                    label _("Reaching {color=#fff1e5}High Island{/color}"):
                        style "shop_prompt"
                        xalign 0.5
                    if not world_popupnarration_crewcounter:
                        text "The boat awaits you at the coast. You need to take exactly [world_popupnarration_crewcounter_max] people with you, but, so far, you doubt anyone would be willing to join you." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                    elif world_popupnarration_crewcounter == 1:
                        text "The boat awaits you at the coast. You need to take exactly [world_popupnarration_crewcounter_max] people with you, but, so far, only 1 soul would be willing to join you." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                    else:
                        text "The boat awaits you at the coast. You need to take exactly [world_popupnarration_crewcounter_max] people with you, and, so far, [world_popupnarration_crewcounter] souls would be willing to join you." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                    if world_popupnarration_crewcounter:
                        text "To leave with the crew, you need to start preparations in the morning." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                    text "Before leaving, better make sure you’re well-prepared to face the unknown." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                    hbox:
                        xalign 0.5
                        spacing 75
                        if highisland_journey_startingpoint == "hamlet":
                            textbutton _("I travel\nalone") action [SetVariable("world_popupnarration_name", 0), Hide("world_popupnarration_box", transition=dissolve), SetVariable("travel_destination", "fishinghamlet"), SetVariable("highisland_mode", "solo"), Hide("map_display", transition=dissolve), Jump("finaldestination")] text_align 0.5 xalign .5
                            if world_popupnarration_crewcounter and quarters <= ((world_daylength/2)+11):
                                textbutton _("I gather\nmy crew") action [SetVariable("world_popupnarration_name", "highislandprep_selecting")] text_align 0.5 xalign .5
                            elif world_popupnarration_crewcounter and quarters > ((world_daylength/2)+11):
                                textbutton _("{color=#6a6a6a}It’s too late to\ngather the crew{/color}") action NullAction()
                            else:
                                textbutton _("{color=#6a6a6a}I don’t\nhave a crew{/color}") action NullAction()
                            if thais_about_highisland_recruitment_done:
                                textbutton _("{color=#6a6a6a}Aegidia won’t allow me\nto leave with the guards\nfrom Howler’s{/color}") action NullAction()
                        else:
                            textbutton _("I travel\nalone") action [SetVariable("world_popupnarration_name", 0), Hide("world_popupnarration_box", transition=dissolve), SetVariable("travel_destination", "beach"), SetVariable("highisland_mode", "solo"), Hide("map_display", transition=dissolve), Jump("finaldestination")] text_align 0.5 xalign .5
                            if world_popupnarration_crewcounter and quarters <= ((world_daylength/2)+11):
                                textbutton _("I gather\nmy crew") action [SetVariable("world_popupnarration_name", "highislandprep_selecting")] text_align 0.5 xalign .5
                            elif world_popupnarration_crewcounter and quarters > ((world_daylength/2)+11):
                                textbutton _("{color=#6a6a6a}It’s too late to\ngather the crew{/color}") action NullAction()
                            else:
                                textbutton _("{color=#6a6a6a}I don’t\nhave a crew{/color}") action NullAction()
                            if thais_about_highisland_recruitment_done:
                                textbutton _("I get help\nfrom Howler’s") action [SetVariable("world_popupnarration_name", 0), Hide("world_popupnarration_box", transition=dissolve), SetVariable("travel_destination", "beach"), SetVariable("highisland_mode", "howlers"), Hide("map_display", transition=dissolve), Jump("finaldestination")] text_align 0.5 xalign .5
    elif world_popupnarration_name == "highislandprep_selecting":
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
                    action Hide("world_popupnarration_box", transition=dissolve)
            frame:
                vbox:
                    xalign .5
                    spacing 28
                    xmaximum 900
                    xminimum 660
                    label _("Reaching {color=#fff1e5}High Island{/color}"):
                        style "shop_prompt"
                        xalign 0.5
                    text "You need to take four souls with you." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                    hbox:
                        spacing 75
                        vbox:
                            spacing 20
                            #style_prefix "check_journey"
                            if aegidia_favor or aegidia_about_highisland_recruitment_done:
                                if highisland_journey_startingpoint == "hamlet":
                                    if not highisland_recruitment_option_aegidia:
                                        textbutton _("Aegidia") action [SetVariable("highisland_recruitment_option_aegidia", 1), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked+1)] padding(0, 0, 0, 0)
                                    else:
                                        textbutton _("{color=#f6d6bd}Aegidia{/color}") action [SetVariable("highisland_recruitment_option_aegidia", 0), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked-1)] padding(0, 0, 0, 0)
                                else:
                                    textbutton _("{color=#6a6a6a}Aegidia{/color}") action NullAction() padding(0, 0, 0, 0)
                            if shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_fled:
                                if not highisland_recruitment_option_bandit:
                                    textbutton _("The Bandit") action [SetVariable("highisland_recruitment_option_bandit", 1), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked+1)] padding(0, 0, 0, 0)
                                else:
                                    textbutton _("{color=#f6d6bd}The Bandit{/color}") action [SetVariable("highisland_recruitment_option_bandit", 0), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked-1)] padding(0, 0, 0, 0)
                            if dalit_about_highisland_recruitment_done:
                                if not highisland_recruitment_option_dalit:
                                    textbutton _("Dalit") action [SetVariable("highisland_recruitment_option_dalit", 1), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked+1)] padding(0, 0, 0, 0)
                                else:
                                    textbutton _("{color=#f6d6bd}Dalit{/color}") action [SetVariable("highisland_recruitment_option_dalit", 0), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked-1)] padding(0, 0, 0, 0)
                            if quest_missinghunters_description02:
                                if not highisland_recruitment_option_efren:
                                    textbutton _("Efren") action [SetVariable("highisland_recruitment_option_efren", 1), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked+1)] padding(0, 0, 0, 0)
                                else:
                                    textbutton _("{color=#f6d6bd}Efren{/color}") action [SetVariable("highisland_recruitment_option_efren", 0), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked-1)] padding(0, 0, 0, 0)
                            if galerocks_navica_about_highisland_recruitment_done:
                                if not highisland_recruitment_option_navica:
                                    textbutton _("Navica") action [SetVariable("highisland_recruitment_option_navica", 1), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked+1)] padding(0, 0, 0, 0)
                                else:
                                    textbutton _("{color=#f6d6bd}Navica{/color}") action [SetVariable("highisland_recruitment_option_navica", 0), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked-1)] padding(0, 0, 0, 0)
                            if pyrrhos_debt == 1 and not pyrrhos_dead:
                                if not highisland_recruitment_option_pyrrhos:
                                    textbutton _("Pyrrhos") action [SetVariable("highisland_recruitment_option_pyrrhos", 1), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked+1)] padding(0, 0, 0, 0)
                                else:
                                    textbutton _("{color=#f6d6bd}Pyrrhos{/color}") action [SetVariable("highisland_recruitment_option_pyrrhos", 0), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked-1)] padding(0, 0, 0, 0)
                            if quintus_alive == 1 and quintus_left_gate and quintus_left_gate < day:
                                if not highisland_recruitment_option_quintus:
                                    textbutton _("Quintus") action [SetVariable("highisland_recruitment_option_quintus", 1), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked+1)] padding(0, 0, 0, 0)
                                else:
                                    textbutton _("{color=#f6d6bd}Quintus{/color}") action [SetVariable("highisland_recruitment_option_quintus", 0), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked-1)] padding(0, 0, 0, 0)
                            if thyrsus_orentius_debt_achieved:
                                if not highisland_recruitment_option_thyrsus:
                                    textbutton _("Thyrsus") action [SetVariable("highisland_recruitment_option_thyrsus", 1), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked+1)] padding(0, 0, 0, 0)
                                else:
                                    textbutton _("{color=#f6d6bd}Thyrsus{/color}") action [SetVariable("highisland_recruitment_option_thyrsus", 0), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked-1)] padding(0, 0, 0, 0)
                            if tulia_about_highisland_recruited and not asterion_lie:
                                if not highisland_recruitment_option_tulia:
                                    textbutton _("Tulia") action [SetVariable("highisland_recruitment_option_tulia", 1), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked+1)] padding(0, 0, 0, 0)
                                else:
                                    textbutton _("{color=#f6d6bd}Tulia{/color}") action [SetVariable("highisland_recruitment_option_tulia", 0), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked-1)] padding(0, 0, 0, 0)
                            if foragers_about_gatherthecrew_tzvi_recruited:
                                if not highisland_recruitment_option_tzvi:
                                    textbutton _("Tzvi") action [SetVariable("highisland_recruitment_option_tzvi", 1), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked+1)] padding(0, 0, 0, 0)
                                else:
                                    textbutton _("{color=#f6d6bd}Tzvi{/color}") action [SetVariable("highisland_recruitment_option_tzvi", 0), SetVariable("world_popupnarration_crewcounter_picked", world_popupnarration_crewcounter_picked-1)] padding(0, 0, 0, 0)
                        vbox:
                            spacing 20
                            if aegidia_favor or aegidia_about_highisland_recruitment_done:
                                if highisland_journey_startingpoint == "hamlet":
                                    text "The free-spirited archeress." text_align 0 xalign 0 #xmaximum 610 xminimum 610
                                else:
                                    text "She won’t travel through Howler’s." text_align 0 xalign 0
                            if shortcut_darkforest_bandit_promisedtocoverforhim and not shortcut_darkforest_bandit_killed and not shortcut_darkforest_bandit_fled:
                                text "The sneaky runaway." text_align 0 xalign 0
                            if dalit_about_highisland_recruitment_done:
                                text "The leader of the big-game hunters." text_align 0 xalign 0
                            if quest_missinghunters_description02:
                                text "The mostly-careful trapper." text_align 0 xalign 0
                            if galerocks_navica_about_highisland_recruitment_done:
                                text "The boatwoman and carpenter." text_align 0 xalign 0
                            if pyrrhos_debt == 1 and not pyrrhos_dead:
                                text "The scavenging crossbowman." text_align 0 xalign 0
                            if quintus_alive == 1 and quintus_left_gate and quintus_left_gate < day:
                                text "As strong as he is stubborn." text_align 0 xalign 0
                            if thyrsus_orentius_debt_achieved:
                                text "The plant-bending warlock." text_align 0 xalign 0
                            if tulia_about_highisland_recruited and not asterion_lie:
                                text "The army veteran." text_align 0 xalign 0
                            if foragers_about_gatherthecrew_tzvi_recruited:
                                text "The hired cutthroat." text_align 0 xalign 0
                    hbox:
                        xalign 0.5
                        spacing 75
                        if highisland_journey_startingpoint == "hamlet":
                            if world_popupnarration_crewcounter_picked == world_popupnarration_crewcounter_max:
                                textbutton _("Selected [world_popupnarration_crewcounter_picked]/[world_popupnarration_crewcounter_max]") action [SetVariable("world_popupnarration_name", 0), Hide("world_popupnarration_box", transition=dissolve), SetVariable("travel_destination", "fishinghamlet"), SetVariable("highisland_mode", "crew"), Hide("map_display", transition=dissolve), Jump("finaldestination")] text_align 0.5 xalign .5
                            else:
                                textbutton _("{color=#6a6a6a}Selected [world_popupnarration_crewcounter_picked]/[world_popupnarration_crewcounter_max]{/color}") action NullAction()
                        else:
                            if world_popupnarration_crewcounter_picked == world_popupnarration_crewcounter_max:
                                textbutton _("Selected [world_popupnarration_crewcounter_picked]/[world_popupnarration_crewcounter_max]") action [SetVariable("world_popupnarration_name", 0), Hide("world_popupnarration_box", transition=dissolve), SetVariable("travel_destination", "beach"), SetVariable("highisland_mode", "crew"), Hide("map_display", transition=dissolve), Jump("finaldestination")] text_align 0.5 xalign .5
                            else:
                                textbutton _("{color=#6a6a6a}Selected [world_popupnarration_crewcounter_picked]/[world_popupnarration_crewcounter_max]{/color}") action NullAction()
    elif world_popupnarration_name == "steephouseseektruth":
        frame:
            vbox:
                xalign .5
                spacing 28
                xmaximum 660
                xminimum 660
                label _("The Ten-Year Old Mystery"):
                    style "shop_prompt"
                    xalign 0.5
                text "The clues you’ve gathered suggest that this “lazy” peninsula went through many changes ten years ago, “accidentally” around the time when the southern village has fallen.\n\nYou could use what you’ve learned to ask the locals what exactly happened." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                hbox:
                    xalign 0.5
                    textbutton _("Gaining their trust\nmay take a bit of work") action [SetVariable("world_popupnarration_name", 0), SetVariable("ruinedvillage_confront_can", 1), Notify("Journal updated: The Ruined Village"), Hide("world_popupnarration_box", transition=dissolve)] text_align 0.5 xalign .5
    elif world_popupnarration_name == "steephousestartconflict":
        frame:
            vbox:
                xalign .5
                spacing 28
                xmaximum 660
                xminimum 660
                label _("{color=#fff1e5}Steep House{/color}"):
                    style "shop_prompt"
                    xalign 0.5
                text "Having discovered the truth, you could force the people of {color=#f6d6bd}Howler’s Dell{/color} to confront their past... Though they may not take kindly to your threats and requests.\n\nThe more you’ll learn about their deeds and conflicts, the more tools you’ll have to use against them." text_align 0.5 xmaximum 610 xminimum 610 xalign .5
                hbox:
                    xalign 0.5
                    textbutton _("If they will listen\nto me at all") action [SetVariable("world_popupnarration_name", 0), SetVariable("ruinedvillage_confront_can", 2), SetVariable("quest_ruinsconflictopen", 1), Notify("Journal updated: The Ruined Village"), Hide("world_popupnarration_box", transition=dissolve)] text_align 0.5 xalign .5

style wait_frame is confirm_frame:
    xalign .5
    yalign .5
    xpadding 40
    ypadding 40
style wait_text is confirm_text:
    size 30
    color "#c3a38a"
    text_align 0.5
    xalign 0.5
style wait_prompt is confirm_prompt:
    xalign 0.5
style wait_prompt_text is confirm_prompt_text:
    color "#f6d6bd"
    xalign 0.5
    size 30
style wait_button_text is confirm_prompt_text:
    color "#997577"
    hover_color "#f6d6bd"
    size 30
    xalign 0.5
    text_align 0.5

screen splashscreenbug():
    zorder 1
    key "game_menu" action Return()

init python:
    renpy.register_style_preference("text", "normal", style.gui_text, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.gui_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.gui_text, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.gui_text, "size", 30)
########
    renpy.register_style_preference("text", "normal", style.say_dialogue, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.say_dialogue, "size", 28)
    renpy.register_style_preference("text", "pixel", style.say_dialogue, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.say_dialogue, "size", 30)
########
    renpy.register_style_preference("text", "normal", style.interface_text, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.interface_text, "size", 48)
    renpy.register_style_preference("text", "pixel", style.interface_text, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.interface_text, "size", 48)
########
    renpy.register_style_preference("text", "normal", style.label_text, "font", "philosopher.ttf")
    #renpy.register_style_preference("text", "normal", style.label_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.label_text, "font", "munro.ttf")
    #renpy.register_style_preference("text", "pixel", style.label_text, "size", 30)
########
    renpy.register_style_preference("text", "normal", style.button_text, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.button_text, "size", 20)
    renpy.register_style_preference("text", "pixel", style.button_text, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.button_text, "size", 20)
########
    renpy.register_style_preference("text", "normal", style.tooltip_text, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.tooltip_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.tooltip_text, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.tooltip_text, "size", 30)
########
    renpy.register_style_preference("text", "normal", style.endmenu_text, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.endmenu_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.endmenu_text, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.endmenu_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.endmenu_prompt_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.endmenu_prompt_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.endmenu_button_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.endmenu_button_text, "size", 30)
########
    renpy.register_style_preference("text", "normal", style.invdetailedmenu_button_text, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.invdetailedmenu_button_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.invdetailedmenu_button_text, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.invdetailedmenu_button_text, "size", 30)
########
    renpy.register_style_preference("text", "normal", style.invdetailedmenu_text, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.invdetailedmenu_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.invdetailedmenu_text, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.invdetailedmenu_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.invdetailedmenu_button_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.invdetailedmenu_button_text, "size", 30)
########
    renpy.register_style_preference("text", "normal", style.input_prompt, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.input_prompt, "size", 28)
    renpy.register_style_preference("text", "pixel", style.input_prompt, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.input_prompt, "size", 29)
########
    renpy.register_style_preference("text", "normal", style.input_text, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.input_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.input_text, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.input_text, "size", 29)
########
    renpy.register_style_preference("text", "normal", style.input_confirm_text, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.input_confirm_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.input_confirm_text, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.input_confirm_text, "size", 29)
########
    renpy.register_style_preference("text", "normal", style.hyperlink_text, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.hyperlink_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.hyperlink_text, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.hyperlink_text, "size", 30)
########
    renpy.register_style_preference("text", "normal", style.default, "font", "philosopher.ttf")
    renpy.register_style_preference("text", "normal", style.default, "size", 28)
    renpy.register_style_preference("text", "pixel", style.default, "font", "munro.ttf")
    renpy.register_style_preference("text", "pixel", style.default, "size", 30)
########
    renpy.register_style_preference("text", "normal", style.nvl_button_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.nvl_button_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.nvl_button2_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.nvl_button2_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.quick_button_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.quick_button_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.navigation_button_text, "size", 48)
    renpy.register_style_preference("text", "pixel", style.navigation_button_text, "size", 50)
    renpy.register_style_preference("text", "normal", style.main_menu_quote_text, "size", 30)
    renpy.register_style_preference("text", "pixel", style.main_menu_quote_text, "size", 32)
    renpy.register_style_preference("text", "normal", style.main_menu_quote_button_text, "size", 30)
    renpy.register_style_preference("text", "pixel", style.main_menu_quote_button_text, "size", 32)
    renpy.register_style_preference("text", "normal", style.about_text, "size", 34)
    renpy.register_style_preference("text", "pixel", style.about_text, "size", 38)
    renpy.register_style_preference("text", "normal", style.pref_label_text, "size", 44)
    renpy.register_style_preference("text", "pixel", style.pref_label_text, "size", 46)
    renpy.register_style_preference("text", "normal", style.radio_button_text, "size", 44)
    renpy.register_style_preference("text", "pixel", style.radio_button_text, "size", 46)
    renpy.register_style_preference("text", "normal", style.radio_button, "foreground", "gui/button/check_[prefix_]foreground_alt.png")
    renpy.register_style_preference("text", "pixel", style.radio_button, "foreground", "gui/button/check_[prefix_]foreground.png")
    renpy.register_style_preference("text", "normal", style.check_button, "foreground", "gui/button/check_[prefix_]foreground_alt.png")
    renpy.register_style_preference("text", "pixel", style.check_button, "foreground", "gui/button/check_[prefix_]foreground.png")
    renpy.register_style_preference("text", "normal", style.check_alt_button, "foreground", "gui/button/check2_[prefix_]foreground_alt.png")
    renpy.register_style_preference("text", "pixel", style.check_alt_button, "foreground", "gui/button/check2_[prefix_]foreground.png")
    renpy.register_style_preference("text", "normal", style.check_button_text, "size", 44)
    renpy.register_style_preference("text", "pixel", style.check_button_text, "size", 46)
    renpy.register_style_preference("text", "normal", style.slider_button_text, "size", 44)
    renpy.register_style_preference("text", "pixel", style.slider_button_text, "size", 46)
    renpy.register_style_preference("text", "normal", style.history_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.history_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.history_text, "line_spacing", 3)
    renpy.register_style_preference("text", "pixel", style.history_text, "line_spacing", 2)
    renpy.register_style_preference("text", "normal", style.help_text, "size", 36)
    renpy.register_style_preference("text", "pixel", style.help_text, "size", 38)
    renpy.register_style_preference("text", "normal", style.help_label_text, "size", 36)
    renpy.register_style_preference("text", "pixel", style.help_label_text, "size", 48)
    renpy.register_style_preference("text", "normal", style.confirm_prompt_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.confirm_prompt_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.confirm_button_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.confirm_button_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.tutorial_button_text, "size", 26)
    renpy.register_style_preference("text", "pixel", style.tutorial_button_text, "size", 28)
    renpy.register_style_preference("text", "normal", style.tutorial_button2_text, "size", 27)
    renpy.register_style_preference("text", "pixel", style.tutorial_button2_text, "size", 27)
    renpy.register_style_preference("text", "normal", style.help_button_text, "size", 44)
    renpy.register_style_preference("text", "pixel", style.help_button_text, "size", 46)
    renpy.register_style_preference("text", "normal", style.about_button_text, "size", 44)
    renpy.register_style_preference("text", "pixel", style.about_button_text, "size", 46)
    # renpy.register_style_preference("text", "normal", style.input_prompt, "spacing", 10)
    # renpy.register_style_preference("text", "pixel", style.input_prompt, "spacing", 12)
    renpy.register_style_preference("text", "normal", style.invdetailedmenu_prompt_text, "size", 35)
    renpy.register_style_preference("text", "pixel", style.invdetailedmenu_prompt_text, "size", 36)
    renpy.register_style_preference("text", "normal", style.nvl_thought, "line_spacing", 8)
    renpy.register_style_preference("text", "pixel", style.nvl_thought, "line_spacing", 6)
    renpy.register_style_preference("text", "normal", style.journal_button_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.journal_button_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.journal_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.journal_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.journalmode_button_text, "size", 36)
    renpy.register_style_preference("text", "pixel", style.journalmode_button_text, "size", 38)
    renpy.register_style_preference("text", "normal", style.journalmode_text, "size", 36)
    renpy.register_style_preference("text", "pixel", style.journalmode_text, "size", 38)
    renpy.register_style_preference("text", "normal", style.resting_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.resting_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.resting_prompt_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.resting_prompt_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.resting_button_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.resting_button_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.wait_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.wait_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.wait_prompt_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.wait_prompt_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.wait_button_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.wait_button_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.inventory_prompt_text, "size", 34)
    renpy.register_style_preference("text", "pixel", style.inventory_prompt_text, "size", 34)
    renpy.register_style_preference("text", "normal", style.shop_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.shop_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.shop_prompt_text, "size", 32)
    renpy.register_style_preference("text", "pixel", style.shop_prompt_text, "size", 32)
    renpy.register_style_preference("text", "normal", style.shop_button_text, "size", 28)
    renpy.register_style_preference("text", "pixel", style.shop_button_text, "size", 30)
    renpy.register_style_preference("text", "normal", style.journal_prompt_text, "size", 36)
    renpy.register_style_preference("text", "pixel", style.journal_prompt_text, "size", 38)

    renpy.register_style_preference("text", "normal", style.input, "caret", "gui/caret.png")
    renpy.register_style_preference("text", "pixel", style.input, "caret", "gui/caret2.png")
    # renpy.register_style_preference("text", "normal", style.notify_frame, "ypos", 50)
    # renpy.register_style_preference("text", "pixel", style.notify_frame, "ypos", 50)
    # renpy.register_style_preference("text", "normal", style.notify_text, "ypos", 4)
    # renpy.register_style_preference("text", "pixel", style.notify_text, "ypos", 4)
    # if persistent.textstyle == "basic":
    #     style.input.caret = "gui/caret2.png"
    # if persistent.textstyle == "pixel":
    #     style.input.caret = "gui/caret2.png"
